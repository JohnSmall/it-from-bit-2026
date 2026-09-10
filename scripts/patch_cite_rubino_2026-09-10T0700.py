#!/usr/bin/env python3
"""Cite Rubino alongside Procopio at both indefinite-causal-order sites.

Both experiments support the framework's boundary claim -- indefiniteness
below the locking threshold, never amplified into records while remaining
indefinite -- but they are not the same kind of experiment, and the
difference is the point.

Procopio et al. (Nat. Commun. 6:7913, 2015) realise the switch: a
superposition of gate orders. Rubino et al. (Sci. Adv. 3:e1602589, 2017)
measure a causal witness, certifying causal non-separability. Rubino's is
therefore the harder case for "no experiment will ever hold a record of
indefinite causal order", because it is precisely a record certifying
indefiniteness -- and the claim survives it, since what the witness records
is that the process was non-separable, not an indefinite order persisting
through amplification.

The two items had been sharing one citation key in Zotero. That is fixed:
784D632M is now rubino2017indefinite, verified against Crossref and arXiv.

Anchors matched whitespace-insensitively, each exactly once; .bak written;
"% EDITED" header prepended; refuses to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-10"
SCRIPT = "scripts/patch_cite_rubino_2026-09-10T0700.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

EDITS = [
    ("paper1/spacetime_from_non-computability.tex",
     r"demonstrations of indefinite causal order \autocite{procopio2015experimental} are, on this",
     r"demonstrations of indefinite causal order \autocite{procopio2015experimental, rubino2017indefinite} are, on this"),
    ("paper2/paper2_main_2026-07-07.tex",
     r"\autocite{procopio2015experimental} demonstrate sub-threshold indefiniteness that definitises at",
     r"\autocite{procopio2015experimental, rubino2017indefinite} demonstrate sub-threshold indefiniteness that definitises at"),
]


def ws(a):
    return r"\s+".join(re.escape(p) for p in a.split())


def main():
    files = []
    for f, _, _ in EDITS:
        if f not in files:
            files.append(f)

    text = {}
    for f in files:
        t = open(f, encoding="utf-8").read()
        if HEADER.strip() in t:
            sys.exit("REFUSING: %s already patched by %s" % (f, SCRIPT))
        text[f] = t

    for f, anchor, _ in EDITS:
        n = len(re.findall(ws(anchor), text[f]))
        if n != 1:
            sys.exit("REFUSING: anchor in %s matched %d times, expected 1" % (f, n))
        if "rubino2017indefinite" in text[f]:
            sys.exit("REFUSING: %s already cites rubino2017indefinite" % f)
    print("both anchors matched exactly once")

    for f, anchor, rep in EDITS:
        pat = re.compile(ws(anchor))
        m = pat.search(text[f])
        text[f] = text[f][:m.start()] + rep + text[f][m.end():]
        print("  %s" % f)

    for f in files:
        if text[f].count("rubino2017indefinite") != 1:
            sys.exit("REFUSING: %s does not cite rubino2017indefinite exactly once" % f)
        orig = open(f, encoding="utf-8").read()
        if sum(1 for c in text[f] if ord(c) > 127) != sum(1 for c in orig if ord(c) > 127):
            sys.exit("REFUSING: %s changed its non-ASCII content" % f)
        shutil.copy2(f, f + ".bak")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(HEADER + text[f])
        print("wrote %s (backup %s.bak)" % (f, f))


if __name__ == "__main__":
    main()
