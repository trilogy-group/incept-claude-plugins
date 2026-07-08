#!/usr/bin/env python3
"""Choice-lane gate + deploy (pilot). Hardened per this session's learnings:
- gate: gpt-4.1 blind must fail 2-of-2 votes; with-passage must succeed
- deploy: snapshot CURRENT LIVE xml; carry modal feedback into rebuilt xml; PUT; read-back verify
Stages: rebuild <edits.json> | classify | deploy
"""
import sys, os, json, re, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # co-located g5_regen_lib
sys.path.insert(0, "/Users/stanhus/Documents/grade3-reading/artifacts/alpha-read-packager/examples")  # ADAPT: push_to_timeback.py location
import g5_regen_lib as L
try:
    import push_to_timeback as P  # packager helper, if present on this machine
except ImportError:
    import timeback_client as P   # co-located self-contained fallback (same surface)

WORK = "/tmp/g5_choice_pilot_work"; os.makedirs(WORK, exist_ok=True)
INPUT = {json.loads(l)["item_id"]: json.loads(l) for l in open("/tmp/g5_choice_pilot_input.jsonl")}
TFY = os.environ["TFY_BASE_URL"].rstrip("/") + "/openai/chat/completions"
TKEY = os.environ["TFY_API_KEY"]

def ask(msgs):
    body = json.dumps({"model": "gpt-4.1", "messages": msgs, "temperature": 0,
                       "response_format": {"type": "json_object"}}).encode()
    req = urllib.request.Request(TFY, data=body, method="POST",
          headers={"Authorization": "Bearer " + TKEY, "Content-Type": "application/json"})
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(json.loads(r.read())["choices"][0]["message"]["content"])
        except Exception:
            pass
    return {}

def solve(iid, xml, with_passage):
    row = L.parse_choice(iid, xml)
    if not row: return None
    pas = INPUT[iid]["passage"] if with_passage else ""
    pre = f"PASSAGE:\n{pas}\n\n" if with_passage else ""
    lst = "\n".join(f'{o["id"]}: {o["text"]}' for o in row["items"])
    r = ask([{"role": "system", "content": 'Answer' + (' using the passage' if with_passage else
              ' from general knowledge and reasoning alone (no passage available)') + '. JSON {"ids":[...]}.'},
             {"role": "user", "content": f'{pre}{row["question"]}\n\n{lst}\n\nPick '
              + ("all correct ids" if row["multi"] else "the single correct id") + "."}])
    return set(r.get("ids", [])) == set(row["answer"])

def rebuild_stage(edits_path):
    edits = json.load(open(edits_path))
    if isinstance(edits, dict): edits = edits.get("edits", edits)
    rebuilt = {}; rej = []
    for e in edits:
        iid = e["item_id"]
        if iid not in INPUT: rej.append((iid, "not-in-input")); continue
        orig = L.load_item(iid)
        new, errs = L.rebuild_choice(orig, {"stem": e.get("stem"), "aff": e.get("aff") or {},
                                            "key": e.get("key_choice")})
        if errs: rej.append((iid, "rebuild:" + ";".join(errs))); continue
        ok, reason = L.validate_choice(new, orig)
        if not ok: rej.append((iid, "validate:" + reason)); continue
        pas = INPUT[iid]["passage"] or ""
        ev = (e.get("key_evidence") or "").strip()
        nrm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
        if ev and nrm(ev)[:40] not in nrm(pas):
            rej.append((iid, "key_evidence-not-in-passage")); continue
        rebuilt[iid] = new
    json.dump(rebuilt, open(f"{WORK}/rebuilt.json", "w"))
    json.dump(rej, open(f"{WORK}/rejects.json", "w"), indent=1)
    print(f"rebuilt {len(rebuilt)} | rejected {len(rej)}")
    for r in rej[:8]: print("  REJECT", r)

def classify_stage():
    rebuilt = json.load(open(f"{WORK}/rebuilt.json"))
    def gate(iid):
        x = rebuilt[iid]
        b1 = solve(iid, x, False); b2 = solve(iid, x, False)  # 2 blind votes, both must fail
        wp = solve(iid, x, True)
        keep = (b1 is False) and (b2 is False) and (wp is True)
        return iid, {"blind1": b1, "blind2": b2, "wp": wp, "keep": keep}
    out = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        for iid, v in ex.map(gate, list(rebuilt)): out[iid] = v
    keepers = {iid: rebuilt[iid] for iid, v in out.items() if v["keep"]}
    json.dump(keepers, open(f"{WORK}/keepers.json", "w"))
    json.dump(out, open(f"{WORK}/classify.json", "w"), indent=1)
    from collections import Counter
    print(f"keepers {len(keepers)}/{len(rebuilt)}")
    print("fail modes:", dict(Counter(
        ("blind-solved" if (v["blind1"] or v["blind2"]) else "wp-failed") for v in out.values() if not v["keep"])))

def deploy_stage():
    keepers = json.load(open(f"{WORK}/keepers.json"))
    tok, _ = P.mint_token()
    snap = {}
    for iid in list(keepers):
        sc, d = P.get_json(P.QTI + f"/assessment-items/{iid}", tok)
        live = (d or {}).get("rawXml", "")
        snap[iid] = live
        modals = re.findall(r'<qti-modal-feedback.*?</qti-modal-feedback>', live, re.S)
        if modals and "<qti-modal-feedback" not in keepers[iid]:
            keepers[iid] = keepers[iid].replace("</qti-assessment-item>",
                                                "".join(modals) + "</qti-assessment-item>", 1)
    json.dump(snap, open(f"{WORK}/originals_snapshot.json", "w"))
    def put(iid, raw):
        body = json.dumps({"format": "xml", "xml": raw}).encode()
        req = urllib.request.Request(P.QTI + f"/assessment-items/{iid}", data=body, method="PUT",
              headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=40) as r: return r.status
        except urllib.error.HTTPError as e: return f"{e.code}"
    ok = 0; fail = []
    for iid, raw in keepers.items():
        st = put(iid, raw)
        if st == 200:
            sc, d = P.get_json(P.QTI + f"/assessment-items/{iid}", tok)
            live = (d or {}).get("rawXml", "")
            want = L.parse_choice(iid, raw); got = L.parse_choice(iid, live) if live else None
            if got and sorted(got["answer"]) == sorted(want["answer"]) and \
               [o["text"] for o in got["items"]] == [o["text"] for o in want["items"]]:
                ok += 1
            else: fail.append((iid, "readback-mismatch"))
        else: fail.append((iid, f"put-{st}"))
    print(f"deployed+verified {ok}/{len(keepers)} | failures {len(fail)}", fail[:5])
    json.dump({"deployed": ok, "failures": fail}, open(f"{WORK}/deploy_report.json", "w"), indent=1)

if __name__ == "__main__":
    s = sys.argv[1]
    if s == "rebuild": rebuild_stage(sys.argv[2])
    elif s == "classify": classify_stage()
    elif s == "deploy": deploy_stage()
