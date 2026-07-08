#!/usr/bin/env python3
"""Build feedback-authoring input records for a list of Unit-2 item ids.
Sources: live XML (/tmp/g5_u2_live_items.json) for stem/options/key; readback stimuli for passages.
Usage: build_fb_input.py <ids.json> <out_prefix>   (writes <out_prefix>_input.json + chunk dir)"""
import sys, os, re, json
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # co-located g5_regen_lib
import g5_regen_lib as L

RB_STIM = "/Users/stanhus/Documents/grade3-reading/artifacts/g5-merged-course/readback/stimuli"
xmls = json.load(open("/tmp/g5_u2_live_items.json"))
ids = json.load(open(sys.argv[1]))
prefix = sys.argv[2]

def local(t): return t.split("}", 1)[-1]
def text_of(el): return re.sub(r"\s+", " ", "".join(el.itertext())).strip()

def passage_of(iid):
    p = f"{RB_STIM}/{iid}-s.xml"
    if not os.path.exists(p): return None
    try:
        root = ET.fromstring(open(p).read())
        return text_of(root)
    except ET.ParseError:
        return re.sub(r"<[^>]+>", " ", open(p).read()).strip()

def live_type(xml):
    if "qti-order-interaction" in xml: return "sequence"
    if "qti-match-interaction" in xml or "qti-gap-match-interaction" in xml: return "match"
    if "qti-hottext-interaction" in xml: return "hot-text"
    if "qti-choice-interaction" in xml: return "choice"
    return None

def choice_extract(iid, xml):
    """mcq/msq/ebsr: one or more choice interactions."""
    root = ET.fromstring(xml)
    # correct values per response declaration
    correct = {}
    for rd in root.iter():
        if local(rd.tag) == "qti-response-declaration":
            rid = rd.get("identifier")
            vals = [text_of(v) for c in rd.iter() if local(c.tag) == "qti-correct-response"
                    for v in c.iter() if local(v.tag) == "qti-value"]
            correct[rid] = vals
    parts = []
    for inter in root.iter():
        if local(inter.tag) != "qti-choice-interaction": continue
        rid = inter.get("response-identifier")
        prompt = ""
        for c in inter.iter():
            if local(c.tag) == "qti-prompt": prompt = text_of(c); break
        opts = []
        for ch in inter.iter():
            if local(ch.tag) == "qti-simple-choice":
                cid = ch.get("identifier")
                mark = " [CORRECT]" if cid in (correct.get(rid) or []) else ""
                opts.append(f"{cid}: {text_of(ch)}{mark}")
        parts.append({"prompt": prompt, "choices": opts})
    stem = L.stem_of(root)
    return {"question": stem or (parts[0]["prompt"] if parts else ""), "options": parts}

rows, skipped = [], []
for iid in ids:
    xml = xmls.get(iid)
    if not xml: skipped.append((iid, "no-live-xml")); continue
    t = live_type(xml)
    pas = passage_of(iid)
    if not pas: skipped.append((iid, "no-passage")); continue
    try:
        if t == "choice":
            ext = choice_extract(iid, xml)
            typ = "ebsr" if len(ext["options"]) > 1 else ("mcq/msq")
            rows.append({"item_id": iid, "type": typ, "question": ext["question"],
                         "options": ext["options"], "passage": pas})
        elif t in ("sequence", "match", "hot-text"):
            r = L.parse_xml(iid, t, xml)
            if r is None: skipped.append((iid, "parse-none")); continue
            if t == "sequence":
                opts = {"items": r["items"], "correct_order_first_to_last": r["correct_order"]}
            elif t == "match":
                opts = {"items": r["items"], "categories": r.get("categories")}
            else:
                opts = {"tokens": r["tokens"], "correct_token_ids": r["answer"],
                        "max_selections": r.get("max_selections")}
            rows.append({"item_id": iid, "type": t, "question": r["question"],
                         "options": opts, "passage": pas})
        else:
            skipped.append((iid, "unknown-type"))
    except Exception as e:
        skipped.append((iid, f"err:{e}"))

json.dump(rows, open(f"{prefix}_input.json", "w"))
cd = f"{prefix}_chunks"; os.makedirs(cd, exist_ok=True)
n = 0
for i in range(0, len(rows), 8):
    json.dump(rows[i:i+8], open(f"{cd}/chunk_{n:02d}.json", "w"))
    n += 1
from collections import Counter
print(f"rows {len(rows)} | skipped {len(skipped)} | chunks {n} -> {cd}")
print("types:", dict(Counter(r['type'] for r in rows)))
for s in skipped[:8]: print("  SKIP", s)
