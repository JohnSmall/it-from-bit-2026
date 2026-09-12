#!/usr/bin/env python3
"""Input the sedenions/three-generations section into main.tex.

Placement is the one the section's own preamble specifies: after the
electroweak/boson-mass arc and the superconductor witness, before the
interactions section, "so the register-level generation reading (zoo
sec:generations) and the mass hierarchy (sec:masses) are both on the table when
the deeper account arrives".

The section defines sec:sedenions-generations and sec:sedenions-mixing, the two
labels wigners_friend has been referencing into thin air.

Anchor matched whitespace-insensitively, exactly once. A .bak is written, an
"% EDITED" header prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-12"
SCRIPT = "scripts/patch_input_sedenions_section_2026-09-12T1610.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/main.tex"

AFTER = r"\input{superconductor_witness_section_2026-07-07}"
BEFORE = r"\input{interactions_circuits_section_2026-06-08}"
ADDED = r"\input{sedenions_generations_section_2026-08-27}"


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))
    if "sedenions_generations_section" in text:
        sys.exit("REFUSING: the section is already input")

    for a in (AFTER, BEFORE):
        if text.count(a) != 1:
            sys.exit("REFUSING: %s occurs %d times, expected 1" % (a, text.count(a)))
    i, j = text.index(AFTER), text.index(BEFORE)
    if not i < j:
        sys.exit("REFUSING: the two anchors are in the wrong order")
    between = text[i + len(AFTER):j]
    if between.strip():
        sys.exit("REFUSING: unexpected content between the anchors: %r" % between[:80])

    n_inputs = text.count(r"\input{")
    text = text[:i + len(AFTER)] + "\n" + ADDED + text[i + len(AFTER):]

    if text.count(r"\input{") != n_inputs + 1:
        sys.exit("REFUSING: input count did not rise by exactly one")

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("input the sedenions section into %s" % DEST)


if __name__ == "__main__":
    main()
