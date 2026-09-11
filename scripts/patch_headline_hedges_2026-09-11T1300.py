#!/usr/bin/env python3
"""Hedge two items in the headline-results snippet to match the paper.

The snippet lists seven headline results for the introduction. Two of them
claim more than the sections they summarise.

KOIDE. The snippet reads "with its single angle fixed at delta_0 = 2/9,
matching to about a tenth of a per cent". masses_section_2026-06-08.tex says
the relation is "derived, not fitted" but that the phase is "matched to five
significant figures", "matched rather than derived", and flags it as "the one
genuine gap", attaching op:koide-delta -- "the single most important open
calculation in the mass sector". The snippet's figure is also inconsistent
with both the section (five significant figures) and the results ledger
(<0.006%); the section is followed here, and the ledger/section disagreement
is left for John.

NEUTRINO. Sum m_nu ~ 52 meV is CANDIDATE in the results ledger but reads in
the list with the same confidence as y_t = 1, which is ESTABLISHED. The
closing sentence of the snippet promises statuses are "attached where each
result is derived and are never silently upgraded"; in the list itself only
the three-dimensions item carries its hedge.

Both items stay, and the list still closes on the falsifiable neutrino bet, as
the snippet's header intended.

The file is not yet part of the build, so this only makes it consistent.
Anchors matched whitespace-insensitively, each exactly once.
"""

import re
import shutil
import sys

DATE = "2026-09-11"
SCRIPT = "scripts/patch_headline_hedges_2026-09-11T1300.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
FILE = "orphans/headline_results_snippet_2026-07-07.tex"

EDITS = [
 (r"""\item The Koide charged-lepton relation with its single angle fixed at $\delta_{0} = \tfrac29$, matching to about a tenth of a per cent (\S\ref{sec:masses}).""",
  r"""\item The Koide charged-lepton relation derived rather than fitted, with its single angle
      matched to five significant figures at $\delta_{0} = \tfrac29$ --- a value the framework
      matches but does not yet derive (Open Problem~\ref{op:koide-delta};
      \S\ref{sec:masses})."""),
 (r"""$\sum m_{\nu} \approx 52$~meV: consistent with every current bound and decidable by JUNO within a few years (\S\ref{sec:predictions}).""",
  r"""$\sum m_{\nu} \approx 52$~meV: consistent with every current bound and decidable by JUNO
      within a few years --- the framework's sharpest falsifiable prediction, and a candidate
      rather than a settled result (\S\ref{sec:predictions})."""),
]


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    t = open(FILE, encoding="utf-8").read()
    if HEADER.strip() in t:
        sys.exit("REFUSING: %s already patched by %s" % (FILE, SCRIPT))

    for old, new in EDITS:
        pat = re.compile(ws(old))
        n = len(pat.findall(t))
        if n != 1:
            sys.exit("REFUSING: anchor %r matched %d times, expected 1" % (old[:44], n))
        t = pat.sub(lambda _m, r=new: r, t)

    for gone in ("a tenth of a per cent",):
        if gone in t:
            sys.exit("REFUSING: %r survives" % gone)
    for needed in ("op:koide-delta", "does not yet derive", "candidate\n      rather than a settled result"):
        if needed not in t:
            sys.exit("REFUSING: %r missing after edit" % needed)
    if t.count(r"\item") != 7:
        sys.exit("REFUSING: %d items after edit, expected 7" % t.count(r"\item"))

    shutil.copy2(FILE, FILE + ".bak")
    open(FILE, "w", encoding="utf-8").write(HEADER + t)
    print("hedged 2 items in %s" % FILE)
    print("  items still: %d" % t.count(r"\item"))


if __name__ == "__main__":
    main()
