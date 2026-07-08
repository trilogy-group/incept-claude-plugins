#!/usr/bin/env python3
"""G5 regen gate + deploy driver.
  stage=rebuild : edits.json -> rebuilt rawXml + probe rows (blind bundle + with-passage bundle). Validates.
  stage=classify: read blind + with-passage probe outputs -> keepers (valid, blind-wrong, passage-answerable).
  stage=deploy  : PUT keepers live (snapshot originals first), read-back verify.
  stage=remeasure: pull deployed live, rebuild probe bundle for a final blind run.
Usage: python3 g5_gate_deploy.py <stage> [args]"""
import sys, os, json, re, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # co-located g5_regen_lib
sys.path.insert(0, "/Users/stanhus/Documents/grade3-reading/artifacts/alpha-read-packager/examples")  # ADAPT: push_to_timeback.py location
import g5_regen_lib as L
try:
    import push_to_timeback as P  # packager helper, if present on this machine
except ImportError:
    import timeback_client as P   # co-located self-contained fallback (same surface)

WORK = "/tmp/g5_regen_work"
os.makedirs(WORK, exist_ok=True)
INPUT = {json.loads(l)["item_id"]: json.loads(l) for l in open("/tmp/g5_regen_input.jsonl")}

def rebuild_stage(edits_path):
    edits = json.load(open(edits_path))
    if isinstance(edits, dict): edits = edits.get("edits", edits)
    rebuilt = {}; blind_rows = []; wp_rows = []; rejects = []
    for e in edits:
        iid = e["item_id"]; t = e["type"]
        if iid not in INPUT: rejects.append((iid, "not-in-input")); continue
        orig = L.load_item(iid)
        key = e.get("key_match") if t == "match" else e.get("key_order")
        ed = {"stem": e.get("stem"), "aff": e.get("aff") or {}, "categories": e.get("categories") or {}, "key": key}
        new_xml, errs = L.rebuild(orig, t, ed)
        if errs: rejects.append((iid, "rebuild:" + ";".join(errs))); continue
        ok, reason = L.validate(new_xml, orig, t)
        if not ok: rejects.append((iid, "validate:" + reason)); continue
        # key_evidence must be a verbatim passage substring (correctness anchor)
        pas = INPUT[iid].get("passage") or INPUT[iid].get("stimulus") or ""
        ev = (e.get("key_evidence") or "").strip()
        norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
        if ev and norm(ev)[:40] not in norm(pas):
            rejects.append((iid, "key_evidence-not-in-passage")); continue
        row = L.parse_xml(iid, t, new_xml)
        row["stimulus"] = pas
        rebuilt[iid] = new_xml
        blind_rows.append({k: v for k, v in row.items() if k != "stimulus"})
        wp_rows.append(row)
    json.dump(rebuilt, open(f"{WORK}/rebuilt.json", "w"))
    with open(f"{WORK}/blind_bundle.jsonl", "w") as f:
        for r in blind_rows: f.write(json.dumps(r) + "\n")
    with open(f"{WORK}/wp_bundle.jsonl", "w") as f:
        for r in wp_rows: f.write(json.dumps(r) + "\n")
    json.dump(rejects, open(f"{WORK}/rejects.json", "w"), indent=1)
    print(f"rebuilt {len(rebuilt)} | rejected {len(rejects)}")
    from collections import Counter
    print("reject reasons:", dict(Counter(r[1].split(':')[0] for r in rejects)))
    for iid, why in rejects[:12]: print("  REJECT", iid, why)

def _item_map(probe_out):
    """item_id -> per-item result dict, from a blind_solve_probe --out json."""
    d = json.load(open(probe_out))
    out = {}
    for r in d.get("results", []):
        out[r.get("src_id") or r.get("item_id")] = r
    return out

def classify_stage(blind_out, wp_out):
    blind = _item_map(blind_out); wp = _item_map(wp_out)
    rebuilt = json.load(open(f"{WORK}/rebuilt.json"))
    keepers = {}; report = []
    for iid in rebuilt:
        b = blind.get(iid, {}); w = wp.get(iid, {})
        t = INPUT[iid]["type"]
        b_exact = b.get("exact", 1)
        b_partial = b.get("jaccard", b.get("pair_acc", b.get("frac", 1.0)))
        w_exact = w.get("exact", 0)
        w_partial = w.get("jaccard", w.get("pair_acc", w.get("frac", 0.0)))
        passage_dependent = (b_exact == 0) and (b_partial is None or b_partial < 0.6)
        answerable = (w_exact == 1) or (w_partial is not None and w_partial >= 0.8)
        keep = passage_dependent and answerable
        report.append({"id": iid, "type": t, "blind_exact": b_exact, "blind_partial": round(b_partial, 2) if b_partial is not None else None,
                       "wp_exact": w_exact, "wp_partial": round(w_partial, 2) if w_partial is not None else None, "keep": keep})
        if keep: keepers[iid] = rebuilt[iid]
    json.dump(keepers, open(f"{WORK}/keepers.json", "w"))
    json.dump(report, open(f"{WORK}/classify_report.json", "w"), indent=1)
    from collections import Counter
    print(f"keepers {len(keepers)}/{len(rebuilt)}")
    print("by type kept:", dict(Counter(r["type"] for r in report if r["keep"])))
    print("by type total:", dict(Counter(r["type"] for r in report)))
    for r in report:
        flag = "KEEP" if r["keep"] else "drop"
        print(f"  {flag} {r['type']:9} b_exact={r['blind_exact']} b_part={r['blind_partial']} wp_exact={r['wp_exact']} wp_part={r['wp_partial']} {r['id'][-26:]}")

def deploy_stage():
    keepers = json.load(open(f"{WORK}/keepers.json"))
    tok, _ = P.mint_token()
    # snapshot originals first (reversible)
    snap = {iid: L.load_item(iid) for iid in keepers}
    json.dump(snap, open(f"{WORK}/originals_snapshot.json", "w"))
    def put(iid, raw):
        body = json.dumps({"format": "xml", "xml": raw}).encode()
        req = urllib.request.Request(P.QTI + f"/assessment-items/{iid}", data=body, method="PUT",
              headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=40) as r: return r.status
        except urllib.error.HTTPError as e: return f"{e.code}:{e.read()[:120]}"
    ok = 0; fail = []
    for iid, raw in keepers.items():
        st = put(iid, raw)
        if st == 200:
            # read back: parse live -> compare key to intended
            sc, d = P.get_json(P.QTI + f"/assessment-items/{iid}", tok)
            live = (d or {}).get("rawXml", "")
            t = INPUT[iid]["type"]
            want = L.parse_xml(iid, t, raw); got = L.parse_xml(iid, t, live) if live else None
            match = got is not None and (
                (t == "hot-text" and sorted(got["answer"]) == sorted(want["answer"])) or
                (t == "sequence" and got["correct_order"] == want["correct_order"]) or
                (t == "match" and sorted((s["id"], s.get("correct_category_id")) for s in got["items"]) ==
                                  sorted((s["id"], s.get("correct_category_id")) for s in want["items"])))
            if match: ok += 1
            else: fail.append((iid, "readback-mismatch"))
        else:
            fail.append((iid, f"put-{st}"))
    print(f"deployed+verified {ok}/{len(keepers)} | failures {len(fail)}")
    for iid, why in fail[:10]: print("  FAIL", iid, why)
    json.dump({"deployed": ok, "failures": fail}, open(f"{WORK}/deploy_report.json", "w"), indent=1)

def remeasure_stage():
    """Pull deployed keepers live, build a blind bundle for a final gate run."""
    keepers = json.load(open(f"{WORK}/keepers.json"))
    tok, _ = P.mint_token()
    rows = []
    for iid in keepers:
        sc, d = P.get_json(P.QTI + f"/assessment-items/{iid}", tok)
        live = (d or {}).get("rawXml", "")
        t = INPUT[iid]["type"]
        r = L.parse_xml(iid, t, live) if live else None
        if r: rows.append(r)
    with open(f"{WORK}/deployed_blind_bundle.jsonl", "w") as f:
        for r in rows: f.write(json.dumps(r) + "\n")
    print(f"wrote deployed blind bundle: {len(rows)} items -> {WORK}/deployed_blind_bundle.jsonl")

if __name__ == "__main__":
    stage = sys.argv[1]
    if stage == "rebuild": rebuild_stage(sys.argv[2])
    elif stage == "classify": classify_stage(sys.argv[2], sys.argv[3])
    elif stage == "deploy": deploy_stage()
    elif stage == "remeasure": remeasure_stage()
