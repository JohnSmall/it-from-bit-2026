#!/usr/bin/env python3
"""Splice the headline-results list into main.tex's introduction.

The introduction already carries \\subsection{Principal Results}, an enumerate
of seven STRUCTURAL features "derived, not assumed": gauge group, particle
content, dimensionality, generations, chirality, Born rule, monogamy. The
snippet is the QUANTITATIVE counterpart -- its stated selection criterion is
"a number against a measurement, one line each" -- and the two overlap on
exactly one item, spacetime dimensionality.

PLACEMENT: immediately after \\end{enumerate} closing Principal Results. The
snippet opens "From the chain summarised above", which is that list, so the
two read as one movement: what the framework derives, then what it predicts to
a number.

The snippet is \\input rather than pasted, keeping it a separate file as the
other sections are.

Note for John, not fixed here: spacetime dimensionality now appears in both
lists -- as a structural derivation in the first and a hedged glimpse
(op:three-dimensions) in the second. That may be deliberate, the same result
seen structurally and numerically, or it may read as repetition.

Anchors matched whitespace-insensitively, each exactly once. A .bak is
written, an "% EDITED" header prepended, and this script's own header makes it
refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-11"
SCRIPT = "scripts/patch_splice_headline_results_2026-09-11T1400.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/main.tex"

ANCHOR = ("geometrically from the compactness of the $S^4$ base of the quaternionic Hopf "
          "fibration: a ball has a unique centre, and one cannot overshoot it. \\end{enumerate}")
FOLLOWS = "The idea that entanglement and particle physics share the same algebraic structure"
ADDED = r"\input{headline_results_snippet_2026-07-07}"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    dest = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in dest:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))
    if "headline_results_snippet" in dest:
        sys.exit("REFUSING: main.tex already inputs the headline snippet")

    pat = re.compile(ws(ANCHOR))
    n = len(pat.findall(dest))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % n)
    m = pat.search(dest)
    if FOLLOWS not in dest[m.end():m.end() + 400]:
        sys.exit("REFUSING: the expected following paragraph is not where it should be")

    new = dest[:m.end()] + "\n\n" + ADDED + dest[m.end():]

    if new.count(ADDED) != 1:
        sys.exit("REFUSING: input line appears %d times" % new.count(ADDED))
    if new.count(r"\end{enumerate}") != dest.count(r"\end{enumerate}"):
        sys.exit("REFUSING: enumerate structure changed")

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + new)
    print("spliced the headline list into %s" % DEST)


if __name__ == "__main__":
    main()
