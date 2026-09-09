#!/usr/bin/env python3
"""Collapse Spekkens2004a onto spekkens2007toy.

Both .bib entries describe one paper: the arXiv preprint "In defense of the
epistemic view of quantum states: a toy theory" (quant-ph/0401052) was
published as "Evidence for the epistemic view of quantum states: A toy
theory", Phys. Rev. A 75, 032110 (2007).  The Spekkens2004a entry is a
Mendeley record that welds the preprint's 2004 title and year to the
published DOI 10.1103/PhysRevA.75.032110, so it is internally inconsistent.

spekkens2007toy survives: correct title and year for the published version,
and used in two files (what_is_a_quantum_state.tex,
spacetime_from_non-computability.tex) against this one.

The two Zotero records were merged in stage 1 and the survivor is pinned as
spekkens2007toy, so without this change that citation would go undefined on
the next export.

Anchor is matched whitespace-insensitively and must match exactly once; a
.bak is written, an "% EDITED" header prepended, and the presence of this
script's own header line makes it refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-09"
SCRIPT = "scripts/patch_spekkens_citekey_2026-09-09T1810.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

FILE = "hopf_justification_section_2026-06-08.tex"
ANCHOR = r"obtainable about a system \autocite{Spekkens2004a}, and Szangolies derives such an epistemic"
OLD = "Spekkens2004a"
NEW = "spekkens2007toy"


def ws_insensitive(anchor):
    return r"\s+".join(re.escape(p) for p in anchor.split())


def main():
    orig = open(FILE, encoding="utf-8").read()

    if HEADER.strip() in orig:
        sys.exit("REFUSING: %s already patched by %s" % (FILE, SCRIPT))

    pat = re.compile(ws_insensitive(ANCHOR))
    if len(pat.findall(orig)) != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1"
                 % len(pat.findall(orig)))
    print("anchor matched exactly once")

    if orig.count(OLD) != 1:
        sys.exit("REFUSING: %s occurs %d times in file, expected 1"
                 % (OLD, orig.count(OLD)))
    if NEW in orig:
        sys.exit("REFUSING: %s already present, would duplicate a key" % NEW)

    m = pat.search(orig)
    span = m.group(0)
    new_span = span.replace("{" + OLD + "}", "{" + NEW + "}")
    if new_span == span:
        sys.exit("REFUSING: no braced key {%s} in matched span" % OLD)
    text = orig[:m.start()] + new_span + orig[m.end():]

    before = sum(1 for c in orig if ord(c) > 127)
    after = sum(1 for c in text if ord(c) > 127)
    if after != before:
        sys.exit("REFUSING: non-ASCII count changed %d -> %d" % (before, after))

    shutil.copy2(FILE, FILE + ".bak")
    with open(FILE, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("wrote %s (backup %s.bak)" % (FILE, FILE))
    print("replaced {%s} -> {%s} (1 occurrence)" % (OLD, NEW))


if __name__ == "__main__":
    main()
