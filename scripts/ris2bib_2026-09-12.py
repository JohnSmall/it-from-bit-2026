#!/usr/bin/env python3
"""
ris2bib_2026-09-12.py -- convert the project's RIS batches to biblatex .bib.

Purpose (JS, 2026-09-12): migration from Mendeley to Zotero + Better BibTeX.
BBT honours the .bib entry key on import (pinning it as the citation key), so
the RIS ID fields -- the \\autocite keys the paper uses -- survive the move,
which the RIS route through Mendeley never guaranteed.

Field mapping (biber-compatible, BBT-import-friendly):
  TY JOUR -> @article        TY GEN -> @misc
  ID      -> the entry key (preserved verbatim -- the point of the exercise)
  AU*     -> author = {A and B and ...}   (Family, Given form kept; UTF-8)
  TI      -> title = {...}  (single-braced; biblatex does not downcase
             titles and BBT preserves case, so no extra bracing needed.
             Quote heuristic: '...' and "..." become LaTeX quotes; a
             title with a lone apostrophe is untouched, but one with
             BOTH an apostrophe and quoted text would need a hand check)
  JO      -> journal          JA -> shortjournal
  VL/IS   -> volume/number    SP[/EP] -> pages = {SP[--EP]}
  PY      -> year             DA -> appended to annotation (fidelity only)
  DO      -> doi              UR -> url, DROPPED when it merely repeats the doi
  PB=arXiv + arXiv UR -> eprinttype = {arxiv}, eprint = {NNNN.NNNNN}
  KW*     -> keywords = {a, b, c}   (Zotero imports these as tags)
  N1      -> annotation = {...}  -- NOT `note`, because biblatex PRINTS note
             in the bibliography; annotation is ignored by standard styles,
             so the VERIFY-CITE working flags travel without ever typesetting.
             (Caveat: annotations contain math-ish ASCII with underscores;
             fine while unprinted -- do not switch them to `note`.)

Targeted typesetting restorations (titles only; the RIS kept plain ASCII for
Mendeley's sake, which the .bib no longer needs):
  - standalone S3 -> $S_3$
  - "quoted" -> ``quoted''   and  'quoted' -> `quoted'

Usage:
    python3 ris2bib_2026-09-12.py file1.ris [file2.ris ...]
Writes file1.bib alongside, with a provenance header. UTF-8 in, UTF-8 out
(biber is UTF-8 native; Zotero likewise).
"""
import datetime
import re
import sys

TYPE_MAP = {"JOUR": "article", "GEN": "misc"}


def parse_ris(text):
    records, rec = [], None
    for raw in text.splitlines():
        if not raw.strip():
            continue
        m = re.match(r"^([A-Z][A-Z0-9])  - ?(.*)$", raw)
        if not m:
            continue
        tag, val = m.group(1), m.group(2).strip()
        if tag == "TY":
            rec = {"TY": val, "AU": [], "KW": []}
        elif rec is None:
            continue
        elif tag == "ER":
            records.append(rec)
            rec = None
        elif tag in ("AU", "KW"):
            rec[tag].append(val)
        else:
            rec[tag] = val
    return records


def fix_title(t):
    t = re.sub(r"\bS3\b", r"$S_3$", t)
    t = re.sub(r'"([^"]+)"', r"``\1''", t)
    t = re.sub(r"'([^']+)'", r"`\1'", t)
    return t


def to_entry(rec):
    key = rec.get("ID")
    assert key, "record without ID: %r" % rec
    etype = TYPE_MAP.get(rec.get("TY", ""), "misc")
    f = []  # (field, value) in output order

    if rec["AU"]:
        f.append(("author", " and ".join(rec["AU"])))
    if "TI" in rec:
        f.append(("title", "{" + fix_title(rec["TI"]) + "}"))
    if "JO" in rec:
        f.append(("journal", rec["JO"]))
    if "JA" in rec:
        f.append(("shortjournal", rec["JA"]))
    if "VL" in rec:
        f.append(("volume", rec["VL"]))
    if "IS" in rec:
        f.append(("number", rec["IS"]))
    if "SP" in rec:
        pages = rec["SP"] + ("--" + rec["EP"] if "EP" in rec else "")
        f.append(("pages", pages))
    if "PY" in rec:
        f.append(("year", rec["PY"]))
    if "DO" in rec:
        f.append(("doi", rec["DO"]))
    ur = rec.get("UR", "")
    if ur and ur != "https://doi.org/" + rec.get("DO", "\0"):
        arx = re.search(r"arxiv\.org/abs/([0-9.]+[0-9])", ur)
        if arx or rec.get("PB", "").lower() == "arxiv":
            if arx:
                f.append(("eprinttype", "arxiv"))
                f.append(("eprint", arx.group(1)))
        f.append(("url", ur))
    if rec["KW"]:
        f.append(("keywords", ", ".join(rec["KW"])))
    ann = rec.get("N1", "")
    if "DA" in rec:
        ann = (ann + " " if ann else "") + "[RIS DA: %s]" % rec["DA"]
    if ann:
        # balance check: unbalanced braces would corrupt the entry
        assert ann.count("{") == ann.count("}"), "unbalanced braces in N1 of " + key
        f.append(("annotation", ann))

    width = max(len(name) for name, _ in f)
    lines = ["@%s{%s," % (etype, key)]
    for name, val in f:
        wrapped = val if val.startswith("{") else "{" + val + "}"
        lines.append("  %-*s = %s," % (width, name, wrapped))
    lines.append("}")
    return key, "\n".join(lines)


def convert(path):
    text = open(path, encoding="utf-8").read()
    records = parse_ris(text)
    assert records, "no RIS records parsed from " + path
    out = path[:-4] + ".bib" if path.endswith(".ris") else path + ".bib"
    today = datetime.date.today().isoformat()
    header = [
        "% " + "=" * 70,
        "% " + out.split("/")[-1],
        "% Converted from " + path.split("/")[-1]
        + " by ris2bib_2026-09-12.py (conversion run " + today + ")",
        "% for the Zotero + Better BibTeX migration. Entry keys are the RIS ID",
        "% fields, preserved verbatim; BBT pins them as citation keys on import",
        "% (they appear as 'Citation Key: <key>' in each item's Extra field).",
        "% The RIS N1 working notes (VERIFY-CITE flags etc.) travel in the",
        "% non-printing `annotation` field -- do not move them to `note`,",
        "% which standard biblatex styles typeset. UTF-8 throughout (biber-",
        "% native). Titles: S3 restored to $S_3$; straight quotes to LaTeX",
        "% quotes; url dropped where it merely repeated the doi.",
        "% " + "=" * 70,
        "",
    ]
    keys, chunks = [], []
    for rec in records:
        k, entry = to_entry(rec)
        keys.append(k)
        chunks.append(entry)
    open(out, "w", encoding="utf-8").write(
        "\n".join(header) + "\n\n".join(chunks) + "\n")
    print("%-52s -> %-52s (%d entries): %s"
          % (path.split("/")[-1], out.split("/")[-1], len(keys), ", ".join(keys)))
    return out, keys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for p in sys.argv[1:]:
        convert(p)
