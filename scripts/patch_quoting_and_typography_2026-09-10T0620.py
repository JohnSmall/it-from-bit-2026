#!/usr/bin/env python3
"""Move all quoting to \\enquote{}, set British English, fix typography.

Decisions this encodes:

* Both papers use British English. paper1 loaded babel with [english], which
  makes csquotes emit American-convention quotes (double outside, single
  within); paper2 already used [british]. The same \\enquote{} therefore
  rendered differently in the two papers.

* All quoting uses \\enquote{}. csquotes offers \\textquote{} as well, but
  that macro belongs to the citation machinery -- it takes an optional
  citation argument and pairs with \\blockquote. None of the 30 existing
  \\textquote{} uses carries a citation, and they are overwhelmingly
  mentioned terms and scare quotes ("closest environment", "predictor",
  "naive", "CTCs"), for which \\enquote{} is the right macro.

* \\textquote(quantum omelet) was malformed: parentheses instead of braces.
  csquotes took "(" as the argument, so the PDF currently reads
      if we look at the "(" quantum omelet), the density matrix
  with a stray closing parenthesis. Legal TeX, hence no compile error.

* Literal typographic characters become LaTeX idioms, per CLAUDE.md and
  README.md: --- for the em dash, ' for the apostrophe, \\S for the section
  sign. Letters with diacritics in names (Godel, Gottingen) are untouched.

* Dubois-Violette is spelled with a hyphen in references.bib and in two
  other .tex files; one occurrence used an en dash. It is a surname, not a
  range, so it becomes a plain hyphen rather than --.

Each file gets a .bak and an "% EDITED" header; the presence of this
script's own header line makes it refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-10"
SCRIPT = "scripts/patch_quoting_and_typography_2026-09-10T0620.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

WIQS = "paper1/what_is_a_quantum_state.tex"
MAIN = "paper1/main.tex"
ENT  = "paper1/entanglement_classes_and_gauge_groups_2026-06-08.tex"
SFN  = "paper1/spacetime_from_non-computability.tex"
P2   = "paper2/paper2_main_2026-07-07.tex"

# (file, kind, pattern, replacement, expected count)
EDITS = [
    (MAIN, "literal", r"\usepackage[english]{babel}", r"\usepackage[british]{babel}", 1),
    (MAIN, "literal", r"\textquote{", r"\enquote{", 2),
    (SFN,  "literal", r"\textquote{", r"\enquote{", 1),
    (WIQS, "literal", r"\textquote(quantum omelet)", r"\enquote{quantum omelet}", 1),
    (WIQS, "literal", r"\textquote{", r"\enquote{", 27),
    (WIQS, "regex",   "\u201c([^\u201d]*)\u201d", r"\\enquote{\1}", 4),
    (WIQS, "literal", "\u2019", "'", 1),
    (WIQS, "literal", "\u2014", "---", 2),
    (ENT,  "literal", "Dubois\u2013Violette", "Dubois-Violette", 1),
    (P2,   "literal", "\u00a7", r"\S", 2),
]


def main():
    files = []
    for e in EDITS:
        if e[0] not in files:
            files.append(e[0])

    text = {}
    for f in files:
        t = open(f, encoding="utf-8").read()
        if HEADER.strip() in t:
            sys.exit("REFUSING: %s already patched by %s" % (f, SCRIPT))
        text[f] = t

    # verify every expected count before changing anything
    for f, kind, pat, rep, n in EDITS:
        got = len(re.findall(pat, text[f])) if kind == "regex" else text[f].count(pat)
        if got != n:
            sys.exit("REFUSING: %s: expected %d of %r, found %d" % (f, n, pat, got))
    print("all %d edits matched their expected counts" % len(EDITS))

    for f, kind, pat, rep, n in EDITS:
        if kind == "regex":
            text[f] = re.sub(pat, rep, text[f])
        else:
            text[f] = text[f].replace(pat, rep)
        print("  %-52s %d x %r" % (f, n, pat[:34]))

    # nothing we removed may survive; no new non-ASCII may appear
    for f in files:
        for _, kind, pat, _, _ in [e for e in EDITS if e[0] == f]:
            left = len(re.findall(pat, text[f])) if kind == "regex" else text[f].count(pat)
            if left:
                sys.exit("REFUSING: %s still contains %r after patching" % (f, pat))
        orig = open(f, encoding="utf-8").read()
        if sum(1 for c in text[f] if ord(c) > 127) > sum(1 for c in orig if ord(c) > 127):
            sys.exit("REFUSING: %s gained non-ASCII characters" % f)

    for f in files:
        shutil.copy2(f, f + ".bak")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(HEADER + text[f])
        print("wrote %s (backup %s.bak)" % (f, f))


if __name__ == "__main__":
    main()
