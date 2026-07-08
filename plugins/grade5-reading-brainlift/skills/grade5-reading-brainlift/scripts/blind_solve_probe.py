#!/usr/bin/env python3
"""Binding anti-leak gate (Gate 1): passage-blind solve by a DIFFERENT model family.

For every item we strip the passage (stimulus), the key, and all feedback, present
the answer affordances in a SHUFFLED, id-anonymized form, and force a different-family
solver default = gpt-4o-mini (OpenAI direct); certification-grade runs override to gpt-4.1 via run_probe_tfy.py (TFY) -- a different model family from the Claude generator
to COMMIT to a full answer using world knowledge only. We then score objectively
against the withheld key and compare recovery to chance.

An item LEAKS if a blind solver recovers its answer above chance -- it can be solved
without reading the passage, so it is not measuring reading.

Scoring per type (objective, key withheld from the model):
  sequence : exact-order match (chance = 1/N!) + mean adjacent-pair accuracy
  hot-text : exact-set match (chance = 1/C(T,k)) + Jaccard
  match    : per-item correct fraction (chance = 1/num_categories)

NO passage, NO key, NO feedback ever enters the prompt. Presentation order is a fixed
seeded shuffle so input order cannot leak the answer.
"""
from __future__ import annotations
import argparse, json, math, os, random, collections
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import urllib.request, urllib.error

import hashlib
LABELS = [chr(ord("A") + i) for i in range(26)]
MODEL = "gpt-4o-mini"          # OpenAI family, different from the Claude generator
ENDPOINT = "https://api.openai.com/v1/chat/completions"


def item_sig(r: dict) -> str:
    """Stable content signature, identical across runs/sources (robust join key)."""
    t = r.get("type", "")
    q = (r.get("question") or r.get("stem") or "").strip().lower()
    if t == "sequence":
        aff = "|".join(sorted((x.get("content") or x.get("text") or "") for x in r.get("items", [])))
    elif t == "hot-text":
        aff = "|".join(sorted(x.get("text", "") for x in r.get("tokens", [])))
    elif t == "match":
        aff = "|".join(sorted(x.get("text", "") for x in r.get("items", [])))
    else:
        aff = ""
    return hashlib.md5((t + "||" + q + "||" + aff).encode()).hexdigest()


def _seeded_perm(n: int, seed_key: str) -> list[int]:
    rnd = random.Random(seed_key)            # deterministic per-item shuffle
    idx = list(range(n))
    rnd.shuffle(idx)
    return idx


def build_prompt(r: dict, with_passage: bool = False) -> tuple[dict, dict] | None:
    """Return (messages, scoring_ctx) or None if the item shape is unusable.

    with_passage=True is the CONTROL: include the stimulus so we can measure whether
    the item is answerable WITH the passage (lift over blind = the item requires reading;
    low with-passage accuracy = the item is broken/ambiguous, not a good item)."""
    t = r["type"]
    q = r.get("question", "").strip()
    if with_passage:
        passage = (r.get("stimulus") or "").strip()
        sys = ("You are taking a reading comprehension test. Read the passage, then answer "
               "using ONLY the passage. Commit to a single best answer. Respond JSON only.\n\n"
               f"PASSAGE:\n{passage}")
    else:
        sys = ("You are taking a reading comprehension test, but the reading passage is "
               "MISSING from this item. Answer using ONLY general world knowledge. You MUST "
               "commit to a single best answer even when unsure -- guessing is required, do "
               "not refuse or say you need the passage. Respond with JSON only.")

    if t == "sequence":
        items = r.get("items", [])
        order = r.get("correct_order", [])
        if len(items) < 2 or len(order) != len(items):
            return None
        perm = _seeded_perm(len(items), "seq:" + str(r.get("lesson_id", "")) + q)
        shown = [items[i] for i in perm]
        id2label = {it["id"]: LABELS[j] for j, it in enumerate(shown)}
        _txt = lambda it: it.get("content") or it.get("text") or ""
        lines = "\n".join(f"  {LABELS[j]}: {_txt(it)}" for j, it in enumerate(shown))
        user = (f"Question: {q}\n\nPut these events/steps in the correct order. "
                f"Items (shuffled):\n{lines}\n\n"
                f'Respond JSON: {{"order": [labels first-to-last]}} e.g. {{"order": ["B","A","C"]}}')
        truth = [id2label[i] for i in order]            # correct labels in order
        return ([{"role": "system", "content": sys}, {"role": "user", "content": user}],
                {"type": t, "truth_order": truth, "n": len(items)})

    if t == "hot-text":
        tokens = r.get("tokens", [])
        ans = r.get("answer", [])
        if len(tokens) < 2 or not ans:
            return None
        perm = _seeded_perm(len(tokens), "ht:" + str(r.get("lesson_id", "")) + q)
        shown = [tokens[i] for i in perm]
        id2label = {tok["id"]: LABELS[j] for j, tok in enumerate(shown)}
        lines = "\n".join(f"  {LABELS[j]}: {tok['text']}" for j, tok in enumerate(shown))
        k = len(ans)
        hint = f"Select exactly {k}." if r.get("max_selections") else "Select all that apply."
        user = (f"Question: {q}\n\nChoose the option(s) the question asks for. {hint}\n"
                f"Options (shuffled):\n{lines}\n\n"
                f'Respond JSON: {{"selected": [labels]}} e.g. {{"selected": ["A","C"]}}')
        truth = {id2label[i] for i in ans if i in id2label}
        return ([{"role": "system", "content": sys}, {"role": "user", "content": user}],
                {"type": t, "truth_set": sorted(truth), "n_tok": len(tokens), "k": k})

    if t == "match":
        items = r.get("items", [])
        cats = r.get("categories", [])
        if len(items) < 2 or len(cats) < 2:
            return None
        # anonymize categories to numbers in fixed shuffled order
        cperm = _seeded_perm(len(cats), "mc:" + str(r.get("lesson_id", "")) + q)
        shown_cats = [cats[i] for i in cperm]
        cid2num = {c["id"]: j + 1 for j, c in enumerate(shown_cats)}
        cat_lines = "\n".join(f"  {j+1}: {c['label']}" for j, c in enumerate(shown_cats))
        iperm = _seeded_perm(len(items), "mi:" + str(r.get("lesson_id", "")) + q)
        shown_items = [items[i] for i in iperm]
        id2label = {it["id"]: LABELS[j] for j, it in enumerate(shown_items)}
        item_lines = "\n".join(f"  {LABELS[j]}: {it['text']}" for j, it in enumerate(shown_items))
        user = (f"Question: {q}\n\nAssign each item to exactly one category.\n"
                f"Categories:\n{cat_lines}\nItems:\n{item_lines}\n\n"
                f'Respond JSON: {{"assignments": {{"A":1,"B":2,...}}}} using item labels and category numbers.')
        truth = {id2label[it["id"]]: cid2num.get(it["correct_category_id"])
                 for it in shown_items if it["id"] in id2label}
        truth = {k: v for k, v in truth.items() if v is not None}
        return ([{"role": "system", "content": sys}, {"role": "user", "content": user}],
                {"type": t, "truth_map": truth, "n_cat": len(cats)})

    return None


def call_openai(messages: list[dict], key: str, retries: int = 2) -> dict | None:
    body = json.dumps({"model": MODEL, "messages": messages, "temperature": 0,
                       "response_format": {"type": "json_object"}}).encode()
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                         headers={"Authorization": f"Bearer {key}",
                                                  "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
            return json.loads(data["choices"][0]["message"]["content"])
        except (urllib.error.URLError, KeyError, json.JSONDecodeError, TimeoutError):
            if attempt == retries:
                return None
    return None


def score(ctx: dict, ans: dict | None) -> dict:
    t = ctx["type"]
    if ans is None:
        return {"type": t, "ok": False, "error": True}
    try:
        if t == "sequence":
            got = [str(x).strip().upper() for x in ans.get("order", [])]
            truth = ctx["truth_order"]
            exact = int(got == truth)
            # adjacent-pair accuracy (order recovery even if not exact)
            pos = {lab: i for i, lab in enumerate(got)}
            pairs = sum(1 for a, b in zip(truth, truth[1:])
                        if pos.get(a, -1) >= 0 and pos.get(b, -2) >= 0 and pos[a] < pos[b])
            denom = max(1, len(truth) - 1)
            chance = 1.0 / math.factorial(ctx["n"])
            return {"type": t, "exact": exact, "pair_acc": pairs / denom,
                    "chance": chance, "n": ctx["n"]}
        if t == "hot-text":
            got = {str(x).strip().upper() for x in ans.get("selected", [])}
            truth = set(ctx["truth_set"])
            inter = len(got & truth)
            union = len(got | truth) or 1
            exact = int(got == truth)
            chance = 1.0 / math.comb(ctx["n_tok"], ctx["k"]) if ctx["k"] <= ctx["n_tok"] else 0.0
            return {"type": t, "exact": exact, "jaccard": inter / union,
                    "chance": chance, "n_tok": ctx["n_tok"], "k": ctx["k"]}
        if t == "match":
            raw = ans.get("assignments", {}) or {}
            truth = ctx["truth_map"]
            got = {str(k).strip().upper(): v for k, v in raw.items()}
            correct = sum(1 for lab, cat in truth.items()
                          if str(got.get(lab)) == str(cat))
            frac = correct / max(1, len(truth))
            chance = 1.0 / ctx["n_cat"]
            return {"type": t, "frac": frac, "exact": int(correct == len(truth)),
                    "chance": chance, "n_cat": ctx["n_cat"]}
    except Exception:
        return {"type": t, "ok": False, "error": True}
    return {"type": t, "ok": False, "error": True}


def is_clean(sc: dict, strict: bool = True) -> bool:
    """A clean item = blind solver does NOT recover it (genuinely needs the passage)."""
    if sc.get("error"):
        return False
    t = sc["type"]
    if t == "sequence":
        return sc["exact"] == 0 and sc["pair_acc"] <= (0.5 if strict else 0.75)
    if t == "hot-text":
        return sc["exact"] == 0 and sc["jaccard"] < (0.5 if strict else 0.7)
    if t == "match":
        return sc["frac"] <= (0.5 if strict else 0.6)
    return False


def stratified(rows: list[dict], per_cell: int) -> list[dict]:
    cells = collections.defaultdict(list)
    for i, r in enumerate(rows):
        cells[(r["type"], r.get("expedition_index", 0))].append((i, r))
    out = []
    for k in sorted(cells):
        bucket = sorted(cells[k], key=lambda x: x[0])
        out.extend(r for _, r in bucket[:per_cell])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", default="/tmp/g5_sc_bundle.jsonl")
    ap.add_argument("--out", default="/tmp/g5_blind_solve_out.json")
    ap.add_argument("--per-cell", type=int, default=0, help="0 = all items")
    ap.add_argument("--threads", type=int, default=8)
    ap.add_argument("--harvest-out", default="", help="write clean (passage-dependent) source rows here")
    ap.add_argument("--strict", action="store_true", default=True)
    ap.add_argument("--loose", dest="strict", action="store_false")
    ap.add_argument("--with-passage", action="store_true", help="CONTROL: include stimulus (answerability check)")
    args = ap.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise SystemExit("OPENAI_API_KEY not in environment")

    rows = [json.loads(l) for l in open(args.bundle) if l.strip()]
    sample = rows if args.per_cell <= 0 else stratified(rows, args.per_cell)
    jobs = []
    for r in sample:
        built = build_prompt(r, with_passage=args.with_passage)
        if built:
            jobs.append((r, built[0], built[1]))
    mode = "WITH-PASSAGE (answerability control)" if args.with_passage else "BLIND (leak probe)"
    print(f"items: {len(rows)} | scorable & sampled: {len(jobs)} | model: {MODEL} | mode: {mode}")

    results = []
    clean_rows = []
    with ThreadPoolExecutor(max_workers=args.threads) as ex:
        futs = {ex.submit(call_openai, msgs, key): (r, ctx)
                for (r, msgs, ctx) in jobs}
        done = 0
        for fut in as_completed(futs):
            r, ctx = futs[fut]
            ans = fut.result()
            sc = score(ctx, ans)
            sc["band"] = {0: "830L", 1: "920L", 2: "1010L"}.get(r.get("expedition_index", 0))
            sc["src_id"] = r.get("item_id") or r.get("id") or r.get("row_id") or ""
            sc["sig"] = item_sig(r)
            results.append(sc)
            if is_clean(sc, args.strict):
                clean_rows.append(r)
            done += 1
            if done % 25 == 0:
                print(f"  {done}/{len(jobs)}")

    if args.harvest_out:
        with open(args.harvest_out, "w") as fh:
            for r in clean_rows:
                fh.write(json.dumps(r) + "\n")
        print(f"harvested {len(clean_rows)} clean rows -> {args.harvest_out} "
              f"(strict={args.strict})")

    # aggregate
    by_type = collections.defaultdict(list)
    for sc in results:
        by_type[sc["type"]].append(sc)
    summary = {}
    for t, lst in by_type.items():
        good = [s for s in lst if not s.get("error")]
        n = len(good)
        if t == "sequence":
            summary[t] = {"n": n, "errors": len(lst) - n,
                          "exact_recovery": round(sum(s["exact"] for s in good) / max(1, n), 3),
                          "mean_pair_acc": round(sum(s["pair_acc"] for s in good) / max(1, n), 3),
                          "mean_chance_exact": round(sum(s["chance"] for s in good) / max(1, n), 4)}
        elif t == "hot-text":
            summary[t] = {"n": n, "errors": len(lst) - n,
                          "exact_recovery": round(sum(s["exact"] for s in good) / max(1, n), 3),
                          "mean_jaccard": round(sum(s["jaccard"] for s in good) / max(1, n), 3),
                          "mean_chance_exact": round(sum(s["chance"] for s in good) / max(1, n), 4)}
        elif t == "match":
            summary[t] = {"n": n, "errors": len(lst) - n,
                          "mean_frac_correct": round(sum(s["frac"] for s in good) / max(1, n), 3),
                          "exact_recovery": round(sum(s["exact"] for s in good) / max(1, n), 3),
                          "mean_chance_per_item": round(sum(s["chance"] for s in good) / max(1, n), 4)}
    out = {"model": MODEL, "n_total": len(results), "summary": summary, "results": results}
    Path(args.out).write_text(json.dumps(out, indent=2))
    print("\n=== BLIND-SOLVE LEAK SUMMARY (cross-family: OpenAI solver vs Claude generator) ===")
    for t in sorted(summary):
        print(f"  {t}: {summary[t]}")
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
