#!/usr/bin/env python3
"""Inject authored item-specific feedback into FRESH live XML and PUT.
Replaces the inner content of the existing CORRECT/INCORRECT qti-modal-feedback blocks only —
no other XML is touched. Snapshots the pre-PUT XML for every item (reversible).
Usage: g5_u2_fb_deploy.py <authored.json> <workdir> [--dry-run]"""
import sys, os, re, json, html, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "/Users/stanhus/Documents/grade3-reading/artifacts/alpha-read-packager/examples")  # ADAPT: push_to_timeback.py location (optional)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # co-located fallback
try:
    import push_to_timeback as P  # packager helper, if present on this machine
except ImportError:
    import timeback_client as P   # co-located self-contained fallback (same surface)

AUTHORED = sys.argv[1]
WORK = sys.argv[2]
DRY = "--dry-run" in sys.argv
os.makedirs(WORK, exist_ok=True)

rows = json.load(open(AUTHORED))
tok, _ = P.mint_token()

def set_modal(xml, ident, text):
    """Replace inner content of the modal block with identifier=ident, or INSERT the block
    (the live-verified Unit-1 pattern: appended before </qti-assessment-item>, no outcome
    declaration or response-processing change needed). Returns (xml, ok)."""
    body = "<qti-content-body><p>%s</p></qti-content-body>" % html.escape(text, quote=False)
    pat = re.compile(
        r'(<qti-modal-feedback[^>]*identifier="%s"[^>]*>).*?(</qti-modal-feedback>)' % ident, re.S)
    new, n = pat.subn(lambda m: m.group(1) + body + m.group(2), xml, count=1)
    if n == 1:
        return new, True
    block = ('<qti-modal-feedback outcome-identifier="FEEDBACK" identifier="%s" show-hide="show">%s'
             '</qti-modal-feedback>' % (ident, body))
    close = "</qti-assessment-item>"
    if close not in xml:
        return xml, False
    return xml.replace(close, block + close, 1), True

def put(iid, raw):
    body = json.dumps({"format": "xml", "xml": raw}).encode()
    req = urllib.request.Request(P.QTI + f"/assessment-items/{iid}", data=body, method="PUT",
          headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r: return r.status
    except urllib.error.HTTPError as e: return f"{e.code}:{e.read()[:120]}"

snap, report = {}, []

def process(r):
    iid = r["item_id"]
    sc, d = P.get_json(P.QTI + f"/assessment-items/{iid}", tok)
    xml = (d or {}).get("rawXml", "")
    if sc != 200 or not xml: return (iid, "get-fail", None)
    x1, ok1 = set_modal(xml, "CORRECT", r["feedback_correct"])
    x2, ok2 = set_modal(x1, "INCORRECT", r["feedback_incorrect"])
    if not (ok1 and ok2): return (iid, f"modal-miss c={ok1} i={ok2}", None)
    if DRY: return (iid, "dry-ok", None)
    st = put(iid, x2)
    if st != 200: return (iid, f"put-{st}", xml)
    sc2, d2 = P.get_json(P.QTI + f"/assessment-items/{iid}", tok)
    live = (d2 or {}).get("rawXml", "")
    want_c = html.escape(r["feedback_correct"], quote=False)
    want_i = html.escape(r["feedback_incorrect"], quote=False)
    ok = want_c in live and want_i in live
    return (iid, "ok" if ok else "readback-mismatch", xml)

with ThreadPoolExecutor(6) as ex:
    for iid, status, orig in ex.map(process, rows):
        report.append({"item_id": iid, "status": status})
        if orig is not None: snap[iid] = orig

json.dump(report, open(f"{WORK}/fb_deploy_report.json", "w"), indent=0)
if snap: json.dump(snap, open(f"{WORK}/fb_originals_snapshot.json", "w"))
from collections import Counter
print("statuses:", dict(Counter(r["status"] for r in report)))
bad = [r for r in report if r["status"] not in ("ok", "dry-ok")]
for r in bad[:10]: print("  ISSUE", r["item_id"], r["status"])
