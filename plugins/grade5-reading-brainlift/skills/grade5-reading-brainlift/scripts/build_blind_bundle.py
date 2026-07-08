#!/usr/bin/env python3
"""Final wave-3 re-probe prep: pull EVERY certified Unit-2 item live (fresh, not cached),
live-detect its interaction type from the XML, and build a blind bundle for the gpt-4.1 gate.
Usage: build_final_blind_bundle.py <ids.json> <out_bundle.jsonl>"""
import sys, os, json
sys.path.insert(0, "/Users/stanhus/Documents/grade3-reading/artifacts/alpha-read-packager/examples")  # ADAPT: push_to_timeback.py location
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # co-located g5_regen_lib
ENV = '/Users/stanhus/Documents/grade3-reading/knowledge_bot/.env'  # ADAPT: gitignored credential env (optional; creds may come from the shell env instead)
if os.path.exists(ENV):
    for line in open(ENV):
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            os.environ.setdefault(k.strip().replace('export ', ''), v.strip().strip('"'))
try:
    import push_to_timeback as P  # packager helper, if present on this machine
except ImportError:
    import timeback_client as P   # co-located self-contained fallback (same surface)
import g5_regen_lib as L

def live_type(xml):
    if "qti-order-interaction" in xml: return "sequence"
    if "qti-match-interaction" in xml or "qti-gap-match-interaction" in xml: return "match"
    if "qti-hottext-interaction" in xml: return "hot-text"
    return None

# This bundle probes ONLY hot-text/sequence/match. Choice (MCQ/MSQ) and EBSR items are
# deliberately not probed here — choice-leak was measured historically via the 2-vote choice
# lane (choice_gate_deploy.py). A choice/EBSR id in the input list is skipped, not certified,
# and each skip is reported explicitly below so the omission is never silent.
CHOICE_SKIP = ("MCQ/MSQ/choice/EBSR are not probed by this bundle -- the blind probe covers "
               "hot-text/sequence/match; choice-leak was measured historically via the "
               "2-vote choice lane")

def skip_reason(sc, xml):
    if not xml:
        return f"no rawXml returned (HTTP {sc})"
    n_choice = xml.count("<qti-choice-interaction")
    if n_choice >= 2:
        return CHOICE_SKIP + " (rendered EBSR: multi-part choice)"
    if n_choice == 1:
        return CHOICE_SKIP + " (rendered choice: MCQ/MSQ)"
    return "unrecognized interaction -- not a hot-text/sequence/match item"

ids = json.load(open(sys.argv[1]))
tok, _ = P.mint_token()
rows, misses = [], []
for iid in ids:
    sc, d = P.get_json(P.QTI + f"/assessment-items/{iid}", tok)
    xml = (d or {}).get("rawXml", "")
    t = live_type(xml) if xml else None
    r = L.parse_xml(iid, t, xml) if t else None
    if r: rows.append(r)
    else: misses.append((iid, skip_reason(sc, xml)))
with open(sys.argv[2], "w") as f:
    for r in rows: f.write(json.dumps(r) + "\n")
print(f"bundle {len(rows)}/{len(ids)} | skipped {len(misses)}")
for iid, why in misses: print(f"skipped {iid}: {why}")
