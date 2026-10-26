#!/usr/bin/env python3
"""patch_inflation_paragraph_2026-10-07T1300.py

paper1/spacetime_from_non-computability.tex: replace the paragraph "Spatial
infinitude and the status of inflation" (one edit).  Reasons, from
knowledge/project-docs/inflation_horizon_infinitude_2026-10-07T1200.md:
"infinite, therefore flat" is wrong (an open universe is infinite and never
flat; flatness is a Friedmann fine-tuning the framework has not derived, so it
is owed under op:comp-metric); "spatially infinite" is weakened to "unbounded
by anything in the framework"; the horizon answer is stated as a claim about
initial data having no places to differ on, with "same laws" named as
insufficient; background (relational) and fluctuations (first records) are
separated; the spectrum stays the hard debt; the tensor-mode prediction is
added.  Cites Planck2020 (library) and bicepkeck2021improved (batch
bib/inflation_alternatives_refs_2026-10-07T1300.bib, undefined until imported).

DRAFTED UNRUN; JS to rule.  Re-anchored 2026-10-07T1400 on the text left by
scripts/patch_infinite_not_flat_2026-10-07T1400.py (applied at JS's ruling), so
that patch must be in place first.  Sentinel-gated; anchor matches once; .bak;
"% EDITED" header; refuses twice; --check verifies only.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-10-07"
SCRIPT = Path(__file__).name
STAMP = "2026-10-07T1300"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/spacetime_from_non-computability.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


def replace_once(text, anchor, repl, label):
    hits = list(re.finditer(ws(anchor), text))
    if len(hits) != 1:
        sys.exit("%s: anchor matched %d times" % (label, len(hits)))
    m = hits[0]
    return text[: m.start()] + repl + text[m.end():]


A1 = r"""\paragraph{Spatial infinitude and the status of inflation.}
There is no upper bound on non-computability, so the space of computations is
unbounded: the universe is spatially infinite, which leaves its spatial sections flat or of
negative curvature and excludes only the closed case. Infinitude on its own, however, does not
settle flatness, which is a fine-tuning of the Friedmann dynamics the framework has not yet
derived (Open Problem~\ref{op:comp-metric}); and flatness was in any case never inflation's
principal task. The horizon problem is, and an infinite space does nothing for it. The framework's actual lever against
inflation is the relational thesis of Section~\ref{sec:gr-nonlocality}: if
pre-spatial entanglement correlates regions before \textsc{fanout} spreads them
into spatial separation, then the observed large-scale homogeneity is fixed
relationally, before any question of causal contact, and the horizon problem
dissolves without an inflaton. This is a real argument, but it carries a real
bill: inflation also generates the nearly scale-invariant spectrum of primordial
fluctuations seen in the microwave background \autocite{Planck2020}, and any
account that dispenses with inflation owes an alternative origin for that
spectrum. That, not the horizon problem, is the hard empirical debt, and it is
named here rather than discharged."""

R1 = r"""\paragraph{Spatial infinitude and the status of inflation.}
There is no upper bound on non-computability, so nothing in the framework bounds spacelike
distance: the space of computations is unbounded, and the universe is spatially infinite unless
something outside the framework closes it, which leaves its spatial sections flat or of negative
curvature and excludes only the closed case. Three properties are commonly run together here and
must be kept apart. Infinitude is not flatness: an open universe of negative curvature is
infinite at every epoch and never flat, and the framework at present derives neither the
curvature of its spatial sections nor the Friedmann dynamics in which the flatness problem is
posed (Open Problem~\ref{op:comp-metric}), so flatness is owed, not settled. Nor does infinitude
touch the horizon problem, which was inflation's principal task: an infinite space does nothing
to explain why regions that share no past light cone share a temperature to one part in
$10^{5}$. The framework's lever against inflation is the relational thesis of
Section~\ref{sec:gr-nonlocality}, and it is a claim about initial data, not about laws. That the
laws are the same everywhere is not enough, since the same laws applied to different initial
data give different temperatures; the horizon problem is a problem about initial data, and in a
theory with a pre-existing stage the data on the first surface are free to differ from place to
place. Here there are no places on which they could differ. Before the first records form there
is one knowledge-space location, one thermal state and one temperature; the regions of the
later sky are produced by \textsc{fanout} from that single state and inherit its temperature
because they were never separate things that had to agree. The homogeneity of the background is
fixed relationally, before any question of causal contact, and the horizon problem dissolves
without an inflaton; the fluctuations about that background are the Born-rule randomness of the
first records, which is also where inflation puts them, with the inflaton's stretched vacuum
replaced by the first \textsc{fanout} operations. This is a real argument, but it carries a real
bill: inflation also generates the nearly scale-invariant spectrum of those fluctuations seen in
the microwave background, with its measured tilt \autocite{Planck2020}, and any account that
dispenses with inflation owes that spectrum. That, not the horizon problem, is the hard
empirical debt, and it is named here rather than discharged. One consequence is falsifiable
now: with no inflaton, and no metric to fluctuate before records form
(\S\ref{sec:no-quantised-gravity}), the framework predicts no primordial tensor spectrum of
inflationary form, so a detection of primordial $B$-mode polarisation obeying the inflationary
consistency relation, within the present bound $r<0.036$ \autocite{bicepkeck2021improved},
would count against it."""


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    new = replace_once(text, A1, R1, "inflation paragraph")
    for s in ["flatness is owed, not settled", "no places on which they could differ", "bicepkeck2021improved"]:
        if new.count(s) != 1:
            sys.exit("post-check failed: %r" % s)
    for lab in ["sec:no-quantised-gravity", "op:comp-metric", "sec:gr-nonlocality"]:
        if ("\\label{%s}" % lab) not in new:
            sys.exit("label missing: %s" % lab)
    print("verified: %s (1 edit)" % TARGET.relative_to(ROOT))
    if CHECK:
        print("--check: nothing written"); return
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s)" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
