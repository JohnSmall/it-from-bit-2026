#!/usr/bin/env python3
"""Replace the associator-debt/Higgs subsection with the norm-defect version.

orphans/associator_debt_higgs_mechanism_2026-07-03.tex holds a fuller draft of
the subsection already sitting in boson_masses_section_2026-06-08.tex. 89% of
its substantive prose matches the live version verbatim; the difference is one
paragraph carrying the norm-defect elaboration, whose vocabulary -- "norm-defect
identity", "algebraically empty", "division-clean", "unmediated channel",
"coassociative calibration" -- appears nowhere else in Paper 1.

That paragraph is the bridge the project memory records as commissioned on
2026-09-01, when the norm-defect formulation was adopted as the companion to
associator debt: the associator prices the debt at issuance, the sedenion norm
defect is where it settles. It cross-references \\eqref{eq:debt-defect}, a real
label in masses_section_2026-06-08.tex, so the reference resolves once spliced.

The live version asserts that a bare fermion mass term is forbidden; the orphan
derives it -- forbidden because algebraically empty, an unmediated channel
settling no debt. John judged the elaboration essential, so the whole subsection
is replaced rather than the paragraph alone.

The orphan's companion snippet for sec:predictions is NOT carried over: it is
commented out there and already present, near-verbatim, at
predictions_section_2026-06-13.tex line 198.

Boundaries are located by their sectioning commands rather than line numbers,
and every anchor must match exactly once. A .bak is written, an "% EDITED"
header prepended, and this script's own header makes it refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-10"
SCRIPT = "scripts/patch_splice_norm_defect_subsection_2026-09-10T1800.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

DEST = "paper1/boson_masses_section_2026-06-08.tex"
SRC = "orphans/associator_debt_higgs_mechanism_2026-07-03.tex"

START = r"\subsection{The associator debt and the Higgs mechanism}"
END = r"\subsection{What is settled, and what is owed}"
SRC_END = "%  COMPANION SNIPPET"


def main():
    dest = open(DEST, encoding="utf-8").read()
    src = open(SRC, encoding="utf-8").read()

    if HEADER.strip() in dest:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))

    for text, needle, label in ((dest, START, "destination start"),
                                (dest, END, "destination end"),
                                (src, START, "source start")):
        if text.count(needle) != 1:
            sys.exit("REFUSING: %s matched %d times, expected 1" % (label, text.count(needle)))

    d_start = dest.index(START)
    d_end = dest.index(END)
    if d_end <= d_start:
        sys.exit("REFUSING: destination subsections are out of order")

    s_start = src.index(START)
    s_end = src.index(SRC_END)
    if s_end <= s_start:
        sys.exit("REFUSING: companion-snippet marker precedes the subsection")
    # trim the rule of '=' characters that opens the snippet's comment block
    replacement = src[s_start:s_end].rstrip()
    replacement = re.sub(r"\n%\s*=+\s*$", "", replacement).rstrip() + "\n\n"

    if "norm-defect" not in replacement.replace("\n", " ").replace("-\n", ""):
        if "norm-defect" not in re.sub(r"\s+", " ", replacement):
            sys.exit("REFUSING: replacement lacks the norm-defect paragraph")
    if r"\eqref{eq:debt-defect}" not in re.sub(r"\s+", " ", replacement):
        sys.exit("REFUSING: replacement lacks the eq:debt-defect reference")

    new = dest[:d_start] + replacement + dest[d_end:]

    if new.count(START) != 1 or new.count(END) != 1:
        sys.exit("REFUSING: sectioning damaged by the splice")
    before_na = sum(1 for c in dest if ord(c) > 127)
    after_na = sum(1 for c in new if ord(c) > 127)

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + new)
    print("replaced the subsection in %s" % DEST)
    print("  destination lines %d -> %d" % (dest.count("\n") + 1, new.count("\n") + 1))
    print("  non-ASCII %d -> %d" % (before_na, after_na))
    print("  backup %s.bak" % DEST)


if __name__ == "__main__":
    main()
