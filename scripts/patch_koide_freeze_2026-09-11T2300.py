#!/usr/bin/env python3
"""Freeze op:koide-delta: two targets, a ceiling, nine closed routes; say which masses.

Companion to knowledge/sessions/koide_qed_corrections_2026-09-11T2200.md and to
scripts/koide_qed_corrections_2026-09-11T2200.py, whose numbers are quoted. JS's
instruction of 2026-09-11: freeze the open problem with the ceiling and the alpha target,
write it up so it appears in paper1, collect open problems as we go.

One file, one header, one run only.

paper1/masses_section_2026-06-08.tex
  1. Header comment: the op:koide-delta line no longer says "from Hopf holonomy".
  2. The "one genuine gap" paragraph: the gap has two parts of different standing;
     alpha = sqrt2 is identified (doubling norm; pairwise unbiased states), delta = 2/9
     is matched; the open problem carries both, and we do not expect to close it here.
  3. op:koide-delta, retitled "The Koide phase and amplitude": invariant targets
     3 delta = 2/3 and alpha = 2 rho = sqrt2; PASS bands for both; the comparison is
     made with the band and not below 1e-6 rad, where the pole-mass and self-scale
     readings part; FAIL clauses (algebraic e^{i delta}; a relation among running
     masses at a common scale); nine closed routes; what survives.
  4. The summary paragraph: "the derivation of delta = 2/9 from the Hopf holonomy
     (..., the key open calculation)" becomes the frozen problem's description.
  5. sec:koide-gap gains a closing paragraph, "Which masses", after "Flat, but not
     a torus": the one-loop common-scale shifts (170 to 230 sigma), the on-shell
     reading, the two-loop fork of 1.4e-6 rad, the ceiling, and the tau precision
     that would separate the readings. Cites sumino2009family, sumino2009origin
     (bib/koide_attribution_refs_2026-09-11T2011.bib, import pending) and
     melnikovvanritbergen2000threeloop (bib/koide_qed_refs_2026-09-11T2300.bib);
     the paper does not build cleanly until both batches are imported and
     references.bib re-exported.

Every anchor is matched whitespace-insensitively and must match exactly once;
replacements are pre-filled to 96 columns. A dated .bak is written, a "% EDITED"
header is prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-11"
STAMP = "2026-09-11T2300"
SCRIPT = "scripts/patch_koide_freeze_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

MASSES = "paper1/masses_section_2026-06-08.tex"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def fill(s):
    return textwrap.fill(" ".join(s.split()), width=WIDTH,
                         break_long_words=False, break_on_hyphens=False)


def replace_once(text, anchor, replacement):
    pat = re.compile(ws(anchor.strip()))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1:\n  %s" % (n, anchor.strip()[:70]))
    m = pat.search(text)
    return text[:m.start()] + replacement + text[m.end():]


# 1. header comment
OLD_HDR = r"""
%    op:koide-delta         -- derive delta = 2/9 from Hopf holonomy
%                              (key open calculation; sin^4 holonomy route
%                              recorded as tried-and-failed);
"""
NEW_HDR = """%    op:koide-delta         -- derive the Koide phase and amplitude
%                              (frozen 2026-09-11 with bands, a 1e-6 rad
%                              ceiling and nine closed routes);"""

# 2. the gap paragraph
OLD_GAP = r"""
We flag the one genuine gap squarely. Proposition~\ref{prop:koide} derives the $2/3$ relation from
$\alpha=\sqrt2$ and the $\mathbb{Z}_3$ ansatz, both of which the framework supplies; but the specific
phase $\delta = 2/9$ is at present a \emph{matched} value with a suggestive geometric interpretation,
not a derived one.
"""
NEW_GAP = fill(r"""
We flag the one genuine gap squarely, and it has two parts of different standing.
Proposition~\ref{prop:koide} derives the $2/3$ relation from $\alpha=\sqrt2$ and the
$\mathbb{Z}_3$ form, and Proposition~\ref{prop:koide-jordan} below derives the form itself from
the Jordan algebra. The amplitude $\alpha = \sqrt2$ is \emph{identified} --- with the doubling
norm, or equivalently with pairwise unbiased generation states --- and not yet derived from a
mechanism that forces it; the phase $\delta = 2/9$ is \emph{matched}, with a suggestive
geometric reading and no derivation. The open problem that follows carries both as targets,
with the bands a derivation must meet and the routes already closed. We do not expect to close
it in this paper; it is stated so that it can be worked on.
""")

# 3. the open problem
OLD_OP = r"""
\begin{openproblem}[The Koide phase]\label{op:koide-delta}
Derive $\delta = 2/9$ from the holonomy of the octonionic Hopf connection. This is the single
most important open calculation in the mass sector. A derivation passes if it lands inside the
measured band, $\delta = 0.222225 \pm 0.000006$ radians, with no fitted input; the invariant
target is $3\delta = 2/3$, the phase of the cyclic product of the three off-diagonal units
(Proposition~\ref{prop:koide-jordan}). It fails before any number is checked if it ends in an
algebraic value of $e^{i\delta}$ --- a root of unity, the argument of a configuration of vectors
with algebraic coordinates, the phase of a cyclic product of algebraic octonions --- since
$e^{2i/9}$ is transcendental (\S\ref{sec:koide-gap}). Four routes are closed: the simplest
holonomy-squared model, $m_k \propto \sin^4(\theta_0 + 2\pi k/3)$, does not reproduce the
spectrum; the structural angles of the bare sedenion triple contain no $2/9$
(Appendix~\ref{app:nb-M}); the norm-defect identity~\eqref{eq:debt-defect}, being a magnitude,
cannot fix a phase; and a coherent-state realisation of the triality frame, with the phase as
the enclosed phase-space area, cannot meet the amplitude and the phase at once.
\end{openproblem}
"""
NEW_OP = "\n".join([
    r"\begin{openproblem}[The Koide phase and amplitude]\label{op:koide-delta}",
    fill(r"""
Derive the two numbers of the triality form~\eqref{eq:z3}. The invariant targets are the phase,
$3\delta = 2/3$, the real part $\cos(2/3)$ of the cyclic product of the three off-diagonal
units, and the amplitude, $\alpha = 2\rho = \sqrt2$, the off-diagonal norm $\rho = 1/\sqrt2$ at
which the generation states are pairwise unbiased (Proposition~\ref{prop:koide-jordan}). A
derivation of the phase passes if it lands inside the measured band, $\delta = 0.222225 \pm
0.000006$ radians, with no fitted input; a derivation of the amplitude passes if it lands inside
$\alpha = 1.414209 \pm 0.000011$ on the same terms. The comparison is made with the band and
not below $10^{-6}$ radians, where the pole-mass and self-scale readings of the relation part
(\S\ref{sec:koide-gap}); no derivation is asked to say more than the data can. A route fails
before any number is checked if it ends in an algebraic value of $e^{i\delta}$ --- a root of
unity, the argument of a configuration of vectors with algebraic coordinates, the phase of a
cyclic product of algebraic octonions --- since $e^{2i/9}$ is transcendental, or if its output
is a relation among running masses at a common scale, since the relation holds among pole
masses (\S\ref{sec:koide-gap}). Nine routes are closed: the holonomy-squared model $m_k \propto
\sin^4(\theta_0 + 2\pi k/3)$; the structural angles of the bare sedenion triple
(Appendix~\ref{app:nb-M}); any single octonionic direction, by $G_2$-transitivity; the
norm-defect identity~\eqref{eq:debt-defect}, a magnitude; the natural-angle families of the
pre-registered scan; a compact flat torus; any construction with algebraic $e^{i\delta}$; the
coherent-state realisation of the triality frame; and a relation among running masses at a
common scale. What survives is a phase that is the exponential of a rational number along a
non-compact flat direction, and an amplitude that makes three states mutually unbiased; the
mechanism that produces either is the problem.
"""),
    r"\end{openproblem}",
])

# 4. the summary paragraph
OLD_SUM = r"""
Owed, and recorded as the named problems above: the derivation of $\delta = 2/9$ from the Hopf
holonomy (Open Problem~\ref{op:koide-delta}, the key open calculation); the associator--geodesic
"""
NEW_SUM = r"""
Owed, and recorded as the named problems above: the derivation of the Koide amplitude and phase
(Open Problem~\ref{op:koide-delta}, frozen with its bands, its ceiling and its closed routes);
the associator--geodesic
""".strip()

# 5. the closing paragraph of sec:koide-gap
ANCHOR_TORUS_END = r"""
of $1.361$ rather than $\sqrt2$. We record the shape of the derivation as a constraint, the
model as a closed route, and the earlier suggestion of a torus as superseded.
"""
P_WHICH = fill(r"""
Which masses. The relation is among pole masses. Under one-loop QED running to any common
scale $\mu$, every mass ratio acquires the factor $(m_j/m_k)^{3\alpha_{\mathrm{em}}/2\pi}$,
independent of $\mu$, and the parameters move to $K = 2/3 + 1.2\times10^{-3}$, $\alpha =
\sqrt2 + 2.5\times10^{-3}$ and $\delta = 2/9 - 1.1\times10^{-3}$, each more than a hundred and
seventy standard deviations from the data. A relation imposed on Yukawa couplings at the
matching scale would therefore fail at the pole unless something cancels the logarithm, which
is the problem Sumino's family gauge symmetry was built to solve
\autocite{sumino2009family,sumino2009origin}. A relation among pole masses has no such problem:
they are scheme-independent observables, and a framework with one dimensional scale and ratios
fixed by a scale-free geometry can only be making a statement about them. To one loop the
same relation holds for the masses at their own scales, $\bar m_k(\bar m_k)$, since
$m_k/\bar m_k(\bar m_k) = 1 + \alpha_{\mathrm{em}}/\pi$ is the same for all three. The two
readings part only at two loops, through the lighter leptons in each lepton's self-energy: with
the physical $\alpha_{\mathrm{em}}$, $m_k/\bar m_k(\bar m_k)$ differs between generations by
$(\alpha_{\mathrm{em}}/\pi)^2\sum_{l<k}\bigl[\tfrac23\ln(m_k/m_l) - \tfrac{71}{96} -
\tfrac{\pi^2}{12}\bigr]$ \autocite{melnikovvanritbergen2000threeloop}, which moves $\delta$ by
$1.4\times10^{-6}$ radians, a fifth of the present band. The claim $\delta = 2/9$ is thus free
of scheme to about $10^{-6}$ radians and no further, which is the ceiling written into Open
Problem~\ref{op:koide-delta}; separating the two readings would need the tau mass to
$\pm0.007$ MeV.
""")


def main():
    with open(MASSES, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (MASSES, HEADER.strip()))
    text = replace_once(text, OLD_HDR, NEW_HDR)
    text = replace_once(text, OLD_GAP, NEW_GAP)
    text = replace_once(text, OLD_OP, NEW_OP)
    text = replace_once(text, OLD_SUM, NEW_SUM)
    pat = re.compile(ws(ANCHOR_TORUS_END.strip()))
    if len(pat.findall(text)) != 1:
        sys.exit("REFUSING: torus-paragraph anchor not unique")
    m = pat.search(text)
    text = text[:m.end()] + "\n\n" + P_WHICH + text[m.end():]
    for lab in (r"\label{op:koide-delta}", r"\label{prop:koide-jordan}", r"\label{sec:koide-gap}"):
        if text.count(lab) != 1:
            sys.exit("REFUSING: label %s occurs %d times" % (lab, text.count(lab)))
    for key in ("sumino2009family", "sumino2009origin", "melnikovvanritbergen2000threeloop"):
        if text.count(key) != 1:
            sys.exit("REFUSING: key %s cited %d times, expected 1" % (key, text.count(key)))
    shutil.copy(MASSES, MASSES + "." + STAMP + ".bak")
    with open(MASSES, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak); three citation keys await import: do not build"
          % (MASSES, MASSES, STAMP))


if __name__ == "__main__":
    main()
