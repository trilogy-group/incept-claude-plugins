#!/usr/bin/env python3
"""Pull all 600 Unit-2 items live, extract modal-feedback text, classify generic vs item-specific.
Writes /tmp/g5_u2_live_items.json (id -> rawXml) and /tmp/g5_u2_fb_scan.json (per-item record)."""
import sys, os, re, json
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "/Users/stanhus/Documents/grade3-reading/artifacts/alpha-read-packager/examples")  # ADAPT: push_to_timeback.py location (optional)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # co-located fallback
try:
    import push_to_timeback as P  # packager helper, if present on this machine
except ImportError:
    import timeback_client as P   # co-located self-contained fallback (same surface)

MANIFEST = "/Users/stanhus/Documents/grade3-reading/ti-courseplans/courses/g5-reading/item_ledger_manifest.json"  # ADAPT: repo ledger (optional)
if not os.path.exists(MANIFEST):  # portable fallback: the co-located compact ledger
    MANIFEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "item-ledger.json")
led = json.load(open(MANIFEST))

def collect_ids(o):
    ids = []
    if isinstance(o, str) and o.startswith("g5-reading-ela-pp-9801"): ids.append(o)
    elif isinstance(o, list):
        for v in o: ids.extend(collect_ids(v))
    elif isinstance(o, dict):
        for v in o.values(): ids.extend(collect_ids(v))
    return ids

ids = sorted(set(collect_ids(led)))
print("unit-2 ids from ledger:", len(ids))
tok, _ = P.mint_token()

def fetch(iid):
    sc, d = P.get_json(P.QTI + f"/assessment-items/{iid}", tok)
    return iid, sc, (d or {}).get("rawXml", "")

out, xmls = [], {}
with ThreadPoolExecutor(8) as ex:
    for iid, sc, xml in ex.map(fetch, ids):
        m = re.findall(r'<qti-modal-feedback[^>]*identifier="(CORRECT|INCORRECT)"[^>]*>(.*?)</qti-modal-feedback>', xml, re.S)
        fb = {k: re.sub(r"<[^>]+>", " ", v).strip() for k, v in m}
        fb = {k: re.sub(r"\s+", " ", v) for k, v in fb.items()}
        out.append({"item_id": iid, "status": sc, "correct": fb.get("CORRECT", ""), "incorrect": fb.get("INCORRECT", "")})
        xmls[iid] = xml

json.dump(xmls, open("/tmp/g5_u2_live_items.json", "w"))

# generic = feedback text shared by many items
from collections import Counter
cc = Counter(r["correct"] for r in out)
ic = Counter(r["incorrect"] for r in out)
for r in out:
    r["generic"] = (cc[r["correct"]] >= 5) or (ic[r["incorrect"]] >= 5) or not r["correct"] or not r["incorrect"]
json.dump(out, open("/tmp/g5_u2_fb_scan.json", "w"), indent=0)

gen = [r for r in out if r["generic"]]
print("pulled:", len(out), "| non-200:", sum(1 for r in out if r["status"] != 200))
print("generic:", len(gen), "| item-specific:", len(out) - len(gen))
print("top shared CORRECT texts:")
for t, n in cc.most_common(3): print(f"  x{n}: {t[:90]}")
