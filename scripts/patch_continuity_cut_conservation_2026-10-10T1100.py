#!/usr/bin/env python3
"""patch_continuity_cut_conservation_2026-10-10T1100.py

paper1/continuity_section_2026-07-04.tex, subsection "Why the cut matters
physically", one edit.  JS, 2026-10-10: measured probability must sum to 1,
therefore probability must be conserved.  The paragraph attributes the cut
from GL(n,C) to U(n) to continuity, which cannot make it (GL(n,C) is
connected); conservation of probability makes it, from exactly one outcome
per FANOUT at any operation count and the closed-loop squares of
sec:born-cost-ledger (which precedes this section), with the renormalised
alternative excluded by analyticity and named as Aaronson's signalling
theory; continuity selects the norm and the connectedness of the isometry
group (sec:reversible-continuity-l2, a forward reference).  Record:
knowledge/sessions/continuity_probability_conservation_2026-10-10T1000.md.

DRAFTED UNRUN; JS to rule.  Sentinel-gated; anchor matches once; .bak;
"% EDITED" header; refuses twice; --check verifies only.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-10-10"
SCRIPT = Path(__file__).name
STAMP = "2026-10-10T1100"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/continuity_section_2026-07-04.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


def replace_once(text, anchor, repl, label):
    hits = list(re.finditer(ws(anchor), text))
    if len(hits) != 1:
        sys.exit("%s: anchor matched %d times" % (label, len(hits)))
    m = hits[0]
    return text[: m.start()] + repl + text[m.end():]


A1 = r"""The cut
from $GL(n, \mathbb{C})$ down to the unitary group is the conserved quadratic form, and continuity
is what entitles the theory to make it: with the fifth axiom in hand, Hardy's theorem delivers the
complex Hilbert space, the quadratic norm and the unitary group in one stroke \autocite{Hardy2001a}
--- cited here, not re-proved."""

R1 = r"""The cut
from $GL(n, \mathbb{C})$ down to the unitary group is not continuity's to make, since
$GL(n,\mathbb{C})$ is itself connected; it is made by conservation of probability, and the
framework has that from the record side. A \textsc{fanout} writes exactly one outcome, it could
occur at any operation count, and the outcome weights are the closed-loop squares of
\S\ref{sec:born-cost-ledger}, $|\psi_{i}|^{2}$ and not ratios of them, so the dynamics must carry
the unit sphere $\sum_{i}|\psi_{i}|^{2}=1$ to itself at every step; a linear map that preserves a
sphere is an isometry of its norm, and the isometries of the quadratic norm are the unitaries.
Said in the regime's own terms, every event is undone by its anti-event, and for a process the
anti-event is the time reverse $U^{\dagger}$, so undoability is $U^{\dagger}U=1$ and not mere
invertibility. (The alternative that keeps the sum at one by renormalising, weights
$|\psi_{i}|^{2}/\sum_{j}|\psi_{j}|^{2}$ under any invertible map, is excluded by the analyticity
declared at \S\ref{sec:complex-amplitudes}, and it is the signalling theory just cited.) What
continuity adds is which norm and how much of its isometry group is reached: for $p\neq2$ the
isometries are generalised permutations that carry no basis state to a superposition
(\S\ref{sec:reversible-continuity-l2}, a forward reference), and conservation alone would be
satisfied by a discrete subgroup such as the Clifford group of the stabiliser fragment; with the
fifth axiom in hand, Hardy's theorem delivers the complex Hilbert space, the quadratic norm and the
unitary group in one stroke \autocite{Hardy2001a} --- cited here, not re-proved."""


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    new = replace_once(text, A1, R1, "cut paragraph")
    if new.count("not continuity's to make") != 1:
        sys.exit("post-check failed")
    for lab, f in (("sec:born-cost-ledger", "paper1/what_is_a_quantum_state.tex"),
                   ("sec:complex-amplitudes", None), ("sec:reversible-continuity-l2", "paper1/L2_metric_global_phase_section_2026_06_07.tex")):
        hay = (ROOT / f).read_text() if f else "".join(p.read_text() for p in (ROOT / "paper1").glob("*.tex"))
        if ("\\label{%s}" % lab) not in hay:
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
