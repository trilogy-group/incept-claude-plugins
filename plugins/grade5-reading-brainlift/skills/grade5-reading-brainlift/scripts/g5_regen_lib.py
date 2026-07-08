#!/usr/bin/env python3
"""G5 regen support: parse a QTI rawXml string -> blind_solve_probe row, and validate a
regenerated rawXml against its original (structure-preserving). Single source of truth =
the rawXml we deploy is the rawXml we gate."""
import re, json
import xml.etree.ElementTree as ET
from pathlib import Path

RB_ITEMS = Path("/Users/stanhus/Documents/grade3-reading/artifacts/g5-merged-course/readback/items")
RB_STIM  = Path("/Users/stanhus/Documents/grade3-reading/artifacts/g5-merged-course/readback/stimuli")

def local(t): return t.split("}", 1)[-1]
def find(el, n):
    for c in el.iter():
        if local(c.tag) == n: return c
    return None
def findall(el, n): return [c for c in el.iter() if local(c.tag) == n]
def text_of(el): return re.sub(r"\s+", " ", "".join(el.itertext())).strip()
def correct_values(root):
    rd = find(root, "qti-correct-response")
    return [text_of(v) for v in findall(rd, "qti-value")] if rd is not None else []
def stem_of(root):
    body = find(root, "qti-item-body")
    if body is None: return ""
    for d in findall(body, "div"):
        if (d.get("class") or "") == "stem": return text_of(d)
    p = find(body, "p")
    return text_of(p) if p is not None else ""
def expedition_index(iid):
    m = re.search(r"-u(\d+)-", iid); return int(m.group(1)) if m else 0

def parse_xml(item_id, mtype, xml):
    """mtype in {hot-text,sequence,match}. Returns probe row or None."""
    root = ET.fromstring(xml)
    q = stem_of(root)
    base = {"item_id": item_id, "question": q, "lesson_id": item_id,
            "expedition_index": expedition_index(item_id)}
    if mtype == "hot-text":
        inter = find(root, "qti-hottext-interaction")
        if inter is None: return None
        toks = [{"id": h.get("identifier"), "text": text_of(h)} for h in findall(inter, "qti-hottext")]
        mx = inter.get("max-choices")
        return {**base, "type": "hot-text", "tokens": toks, "answer": correct_values(root),
                "max_selections": int(mx) if mx and mx != "0" else None}
    if mtype == "sequence":
        inter = find(root, "qti-order-interaction")
        if inter is None: return None
        items = [{"id": c.get("identifier"), "content": text_of(c)} for c in findall(inter, "qti-simple-choice")]
        return {**base, "type": "sequence", "items": items, "correct_order": correct_values(root)}
    if mtype == "match":
        inter = find(root, "qti-match-interaction")
        if inter is None: return None
        sets = findall(inter, "qti-simple-match-set")
        if len(sets) < 2: return None
        src = [{"id": c.get("identifier"), "text": text_of(c)} for c in findall(sets[0], "qti-simple-associable-choice")]
        cats = [{"id": c.get("identifier"), "label": text_of(c)} for c in findall(sets[1], "qti-simple-associable-choice")]
        item_ids = {s["id"] for s in src}
        correct = {}
        for v in correct_values(root):
            iid, _, cid = v.partition(" ")
            if iid in item_ids: correct[iid] = cid
        for s in src: s["correct_category_id"] = correct.get(s["id"])
        return {**base, "type": "match", "items": src, "categories": cats}
    return None

INTER = {"hot-text": "qti-hottext-interaction", "sequence": "qti-order-interaction", "match": "qti-match-interaction"}

def validate(new_xml, orig_xml, mtype):
    """Structure-preserving check: parses, same interaction type, same affordance ids set,
    key present & references existing ids, non-empty texts. Returns (ok, reason)."""
    try:
        nr = ET.fromstring(new_xml); orr = ET.fromstring(orig_xml)
    except Exception as e:
        return False, f"xml-parse: {e}"
    if find(nr, INTER[mtype]) is None:
        return False, f"missing {INTER[mtype]}"
    np = parse_xml("x", mtype, new_xml); op = parse_xml("x", mtype, orig_xml)
    if np is None: return False, "new unparseable to probe row"
    def aff_ids(p):
        if mtype == "hot-text": return {t["id"] for t in p["tokens"]}
        if mtype == "sequence": return {t["id"] for t in p["items"]}
        return {t["id"] for t in p["items"]}
    if aff_ids(np) != aff_ids(op):
        return False, "affordance id set changed"
    # key checks
    if mtype == "hot-text":
        ids = aff_ids(np); ans = np["answer"]
        if not ans or any(a not in ids for a in ans): return False, "bad hottext key"
        if any(not t["text"].strip() for t in np["tokens"]): return False, "empty token text"
    if mtype == "sequence":
        ids = aff_ids(np); order = np["correct_order"]
        if sorted(order) != sorted(ids): return False, "order key != permutation of ids"
        if any(not t["content"].strip() for t in np["items"]): return False, "empty option text"
        # anti-leak lexical guard: no ordinal self-labels in option text
        bad = [t["content"] for t in np["items"] if re.search(r"\b(first|second|third|next|then|finally|last|lastly|begin(?:s|ning)?|start(?:s|ing)?)\b", t["content"], re.I)]
        if bad: return False, f"ordinal self-label in option: {bad[0][:40]!r}"
    if mtype == "match":
        cats = {c["id"] for c in np["categories"]}
        keyed = [s for s in np["items"] if s.get("correct_category_id")]
        if len(keyed) != len(np["items"]): return False, "not all sources keyed"
        if any(s["correct_category_id"] not in cats for s in keyed): return False, "key cat not in set"
        if any(not s["text"].strip() for s in np["items"]): return False, "empty source text"
    return True, "ok"

def load_item(item_id):
    return (RB_ITEMS / f"{item_id}.xml").read_text()
def passage_of(item_id, xml=None):
    xml = xml or load_item(item_id)
    m = re.search(r'stimulus-ref[^>]*identifier="([^"]+)"|/stimuli/([^"/]+)"', xml)
    sid = (m.group(1) or m.group(2)) if m else None
    if not sid: return None, None
    f = RB_STIM / f"{sid}.xml"
    if not f.exists(): return sid, None
    return sid, re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", f.read_text())).strip()

if __name__ == "__main__":
    # round-trip test: parse current rawXml -> probe row, compare to the existing bundle row
    rows = {json.loads(l)["item_id"]: json.loads(l) for l in open("/tmp/a2_unknown_353.jsonl")}
    ok = 0; mism = 0; n = 0
    for iid, want in list(rows.items()):
        xml = load_item(iid)
        got = parse_xml(iid, want["type"], xml)
        n += 1
        if got is None: mism += 1; continue
        # compare answer/affordance counts
        def aff(p): return len(p.get("tokens") or p.get("items") or [])
        def key(p):
            if p["type"] == "hot-text": return sorted(p["answer"])
            if p["type"] == "sequence": return p["correct_order"]
            return sorted((s["id"], s.get("correct_category_id")) for s in p["items"])
        if aff(got) == aff(want) and key(got) == key(want): ok += 1
        else:
            mism += 1
            if mism <= 5: print(f"MISMATCH {iid}: aff {aff(got)}v{aff(want)} keyEq={key(got)==key(want)}")
    print(f"round-trip: {ok}/{n} exact match, {mism} mismatch")


# ---- deterministic rebuild: apply structured text-edits to the original rawXml by element id ----
from xml.sax.saxutils import escape as _esc

def _sub_inner(xml, tag, ident, new_text):
    """Replace inner content of <tag ... identifier="ident" ...>...</tag> with escaped new_text."""
    pat = re.compile(r'(<' + tag + r'\b[^>]*\bidentifier="' + re.escape(ident) + r'"[^>]*>)(.*?)(</' + tag + r'>)', re.S)
    if not pat.search(xml): return xml, False
    return pat.sub(lambda m: m.group(1) + _esc(new_text) + m.group(3), xml, count=1), True

def _sub_stem(xml, new_stem):
    pat = re.compile(r'(<div\b[^>]*\bclass="stem"[^>]*>)(.*?)(</div>)', re.S)
    if pat.search(xml):
        return pat.sub(lambda m: m.group(1) + "<p>" + _esc(new_stem) + "</p>" + m.group(3), xml, count=1), True
    # fallback: first qti-prompt
    pat2 = re.compile(r'(<qti-prompt\b[^>]*>)(.*?)(</qti-prompt>)', re.S)
    if pat2.search(xml):
        return pat2.sub(lambda m: m.group(1) + _esc(new_stem) + m.group(3), xml, count=1), True
    return xml, False

def _sub_key(xml, mtype, key):
    """key: hot-text -> [ids]; sequence -> [ordered ids]; match -> {src:cat}."""
    if mtype == "match":
        vals = "".join(f"<qti-value>{_esc(s)} {_esc(c)}</qti-value>" for s, c in key.items())
    else:
        vals = "".join(f"<qti-value>{_esc(v)}</qti-value>" for v in key)
    pat = re.compile(r'(<qti-correct-response\b[^>]*>)(.*?)(</qti-correct-response>)', re.S)
    if not pat.search(xml): return xml, False
    return pat.sub(lambda m: m.group(1) + vals + m.group(3), xml, count=1), True

TAG = {"hot-text": "qti-hottext", "sequence": "qti-simple-choice", "match": "qti-simple-associable-choice"}

def rebuild(orig_xml, mtype, edits):
    """edits = {stem, aff:{id:text}, categories:{id:label}?, key}. Returns (new_xml, errors[])."""
    xml = orig_xml; errs = []
    if edits.get("stem"):
        xml, ok = _sub_stem(xml, edits["stem"])
        if not ok: errs.append("stem-not-substituted")
    for ident, txt in (edits.get("aff") or {}).items():
        xml, ok = _sub_inner(xml, TAG[mtype], ident, txt)
        if not ok: errs.append(f"aff-miss:{ident}")
    if mtype == "match":
        for ident, txt in (edits.get("categories") or {}).items():
            xml, ok = _sub_inner(xml, "qti-simple-associable-choice", ident, txt)
            if not ok: errs.append(f"cat-miss:{ident}")
    if edits.get("key") is not None:
        xml, ok = _sub_key(xml, mtype, edits["key"])
        if not ok: errs.append("key-not-substituted")
    return xml, errs


# ---- choice support (mastery-gate regen) ----
def parse_choice(item_id, xml):
    root = ET.fromstring(xml)
    q = stem_of(root)
    inter = find(root, "qti-choice-interaction")
    if inter is None: return None
    opts = [{"id": c.get("identifier"), "text": text_of(c)} for c in findall(inter, "qti-simple-choice")]
    mx = inter.get("max-choices")
    multi = (mx == "0") or (mx and mx.isdigit() and int(mx) > 1)
    return {"item_id": item_id, "type": "choice", "question": q, "items": opts,
            "answer": correct_values(root), "multi": multi,
            "lesson_id": item_id, "expedition_index": expedition_index(item_id)}

def validate_choice(new_xml, orig_xml):
    try: nr = ET.fromstring(new_xml)
    except Exception as e: return False, f"xml-parse:{e}"
    if find(nr, "qti-choice-interaction") is None: return False, "missing choice interaction"
    np = parse_choice("x", new_xml); op = parse_choice("x", orig_xml)
    if np is None: return False, "unparseable"
    if {o["id"] for o in np["items"]} != {o["id"] for o in op["items"]}: return False, "choice id set changed"
    ids = {o["id"] for o in np["items"]}
    if not np["answer"] or any(a not in ids for a in np["answer"]): return False, "bad key"
    if np["multi"] and len(np["answer"]) < 2: return False, "multi<2 keys"
    if not np["multi"] and len(np["answer"]) != 1: return False, "single!=1 key"
    if any(not o["text"].strip() for o in np["items"]): return False, "empty option"
    return True, "ok"

def rebuild_choice(orig_xml, edits):
    """edits = {stem, aff:{id:text}, key:[ids]}."""
    xml = orig_xml; errs = []
    if edits.get("stem"):
        xml, ok = _sub_stem(xml, edits["stem"])
        if not ok: errs.append("stem")
    for ident, txt in (edits.get("aff") or {}).items():
        xml, ok = _sub_inner(xml, "qti-simple-choice", ident, txt)
        if not ok: errs.append(f"aff:{ident}")
    if edits.get("key") is not None:
        xml, ok = _sub_key(xml, "choice", edits["key"])
        if not ok: errs.append("key")
    return xml, errs
