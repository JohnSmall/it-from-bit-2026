#!/usr/bin/env python3
"""patch_prop_w_access_outline_2026-09-23T1100.py

paper1/entanglement_classes_and_gauge_groups_2026-06-08.tex: Proposition
prop:w-access ("W accessibility") stood with no text of its own; the proof
outline that follows prop:w-doublet covered both propositions, so the first
read as a placeholder. JS, 2026-09-23: "It looks like a placeholder, please
write appropriate text." Two edits: (1) after prop:w-access, a statement of
what it says, its own proof outline (the computation of appendix app:w-proof,
checked numerically 2026-09-23 by scripts/w_orbit_cfrac_check_2026-09-23T1100.py),
and two remarks (the orbit's image geometry; the hardware measurement of the
ninth, Appendix app:hw-ninth); (2) the outline after prop:w-doublet trimmed to
the doublet statement, so nothing is said twice.

Sentinel-gated: anchors match exactly once (whitespace-insensitive), .bak
written, "% EDITED" header, refuses to run twice; `--check` verifies only.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-23"
SCRIPT = Path(__file__).name
STAMP = "2026-09-23T1100"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/entanglement_classes_and_gauge_groups_2026-06-08.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


def replace_once(text, anchor, repl, label):
    hits = list(re.finditer(ws(anchor), text))
    if len(hits) != 1:
        sys.exit("%s: anchor matched %d times" % (label, len(hits)))
    m = hits[0]
    return text[: m.start()] + repl + text[m.end():]


A1 = r"""$\sup C_{\mathrm{frac}} = \tfrac19$.
\end{proposition}"""
R1 = A1 + r"""

Where the GHZ orbit is confined to the colour sector, the W orbit reaches the lepton sector, and
does so generically: the $\mathbb{C}$-component of its Hopf image is nonzero at every point of the
orbit but a set of measure zero, and it is bounded, never exceeding one ninth of the image's squared
norm. Both facts come from the same one-line computation as Proposition~\ref{prop:ghz}, with one
norm changed.

\emph{Proof outline.} Split on the first qubit. The bare W has branches
$o_1 = \tfrac{1}{\sqrt3}(0,1,1,0)$ and $o_2 = \tfrac{1}{\sqrt3}(1,0,0,0)$, orthogonal but of
\emph{unequal} norm, $\lvert o_1\rvert^2 = \tfrac23$ and $\lvert o_2\rvert^2 = \tfrac13$. Unitaries
on the other two qubits act on both branches alike and change neither their inner product nor
their norms, so $C_{\mathrm{frac}}$ depends only on the first-qubit unitary
$U_1 = \bigl(\begin{smallmatrix} a & b \\ -\bar b & \bar a\end{smallmatrix}\bigr)$. Orthogonality
kills the $\bar a^{2}$ and $\bar b^{2}$ terms of the mixing formula, and the unequal norms leave the
residue $\langle o_1, o_2\rangle = \bar a\bar b\,(\tfrac13 - \tfrac23) = -\tfrac13\bar a\bar b$: the
equal-norm cancellation of the GHZ proof, failing by exactly the norm difference. It vanishes only
when $ab = 0$, $U_1$ diagonal or anti-diagonal, a measure-zero subset of $SU(2)$ on which the bare
representative itself sits. With $p = \lvert a\rvert^2$ the branch norms are
$\lvert o_1\rvert^2 = (1+p)/3$ and $\lvert o_2\rvert^2 = (2-p)/3$, and by Lemma~\ref{lem:cproj}
together with the composition identity,
\[
C_{\mathrm{frac}} \;=\; \frac{p(1-p)}{(1+p)(2-p)},
\]
maximised at $p = \tfrac12$ with value $\tfrac19$: the first-qubit Bloch vector rotated into the
equatorial plane. The reduced spectrum $(\tfrac23,\tfrac13)$ is a local-unitary invariant, so the
statement holds across the orbit, and by the permutation symmetry of $\lvert\mathrm{W}\rangle$ under
each of the three splits. The ceiling is the instance $r = \tfrac13$ of the general identity
$\sup C_{\mathrm{frac}} = r^{2}$, the squared Bloch radius of the marginal (Appendix~\ref{app:setup},
Lemma~\ref{app:lem:ceiling}); the full derivation is in Appendix~\ref{app:w-proof}.
\hfill$\square$

Two remarks. The geometry is sharper than a bound. With $r$ fixed at $\tfrac13$ on the orbit the
colour component of the image has constant norm $\sqrt{8/9}$, so the W orbit's Hopf image lies on
the product of a colour five-sphere of radius $\sqrt{8/9}$ and a Bloch two-sphere of radius
$\tfrac13$, disjoint from the colour equator of unit radius that carries the GHZ image; the missing
ninth of squared norm sits in the $\mathbb{C}$-plane, and the two canonical orbits occupy disjoint
compact loci on the base, which is the geometric form of the statement that no change of local
frame connects them. And the ceiling has been measured: single-wire tomography of the W register on
hardware returned a probe-corrected $r^{2} = 0.1095 \pm 0.0051$ against $\tfrac19 = 0.1111$
(Appendix~\ref{app:hw-ninth}), the number this paper calls the leptonic ninth."""

A2 = r"""\emph{Proof outline.} The W branches are orthogonal but of \emph{unequal} norm,
$\lvert o_1\rvert^2 = \tfrac23$, $\lvert o_2\rvert^2 = \tfrac13$, so the same mixing computation
leaves a residue $\langle o_1,o_2\rangle = -\tfrac13\bar a\bar b$, vanishing only when the
first-qubit unitary is diagonal or anti-diagonal; the supremum follows by maximising the exact
expression for $C_{\mathrm{frac}}$, and equals the squared Bloch radius $(\tfrac13)^2$ of the
marginal --- an instance of the general ceiling identity $\sup C_{\mathrm{frac}} = r^2$ proved in
Appendix~\ref{app:setup}. The doublet statement is immediate from the spectrum:
non-degeneracy fixes a unique eigenbasis, a distinguished $T_3$ axis between whose members the
$SU(2)$ raising and lowering operators act --- structure the degenerate GHZ marginal lacks. Full
derivations are in Appendix~\ref{app:w-proof}. \hfill$\square$"""
R2 = r"""\emph{Proof outline.} Immediate from the spectrum. The single-qubit marginal of
$\lvert\mathrm{W}\rangle$ is $\mathrm{diag}(\tfrac23,\tfrac13)$ in the computational basis, the
same on each qubit by the permutation symmetry, and a local-unitary invariant up to conjugation.
Non-degeneracy fixes a unique eigenbasis, a distinguished $T_3$ axis between whose members the
$SU(2)$ raising and lowering operators act, and leaves invariant only the $U(1)$ of rotations about
that axis. The degenerate GHZ marginal $\tfrac12\mathbb{1}$ has every basis as an eigenbasis and
singles out no direction. Full derivations are in Appendix~\ref{app:w-proof}. \hfill$\square$"""


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    new = replace_once(text, A1, R1, "prop:w-access outline")
    new = replace_once(new, A2, R2, "prop:w-doublet outline")
    for s in ["Where the GHZ orbit is confined", "Immediate from the spectrum"]:
        if new.count(s) != 1:
            sys.exit("post-check failed: %r" % s)
    print("verified: %s (2 edits)" % TARGET.relative_to(ROOT))
    if CHECK:
        print("--check: nothing written"); return
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s)" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
