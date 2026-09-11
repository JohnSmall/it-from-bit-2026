#!/usr/bin/env python3
"""The Koide phase: what it is inside J3(O), what kind of number it must be, and why
the flat structure is not a torus.

Companion to knowledge/sessions/koide_flat_direction_2026-09-11T1900.md and the script
koide_flat_direction_gram_2026-09-11T1900.py, whose numbers are quoted below.

One file, one header, one run only.

paper1/masses_section_2026-06-08.tex
  1. op:koide-delta: the invariant target 3 delta = 2/3 is named, a FAIL clause is
     added (an algebraic value of e^{i delta} fails before any number is checked,
     since e^{2i/9} is transcendental), and the coherent-state model joins the
     closed routes ("Three routes" becomes "Four routes"). First sentence unchanged.
  2. In \\subsection{The shape of the gap} (sec:koide-gap) the closing paragraph --
     the conjecture that the connection is flat "along the fibre circle, a torus" --
     is replaced by: a proposition (prop:koide-jordan) identifying the triality form
     with the spectrum of the democratic element of J3(O), alpha = 2 rho and
     3 delta = Phi = the phase of the cyclic product of the off-diagonal units, with
     the positivity bound |Phi| <= pi/4; a paragraph reading alpha = sqrt2 as mutual
     unbiasedness and delta as the Bargmann invariant; a paragraph on the
     Lindemann--Weierstrass consequences of delta = 2/9 exactly; and a paragraph
     recording that a compact flat torus cannot carry the number, closing the
     coherent-state model, and superseding the torus suggestion.

Every anchor is matched whitespace-insensitively and must match exactly once. The
replacement blocks are pre-filled to 96 columns (breaks only at spaces). A dated .bak
is written, a "% EDITED" header is prepended, and the header makes the script refuse
to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-11"
STAMP = "2026-09-11T1930"
SCRIPT = "scripts/patch_koide_jordan_transcendence_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

MASSES = "paper1/masses_section_2026-06-08.tex"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def fill(s):
    return textwrap.fill(" ".join(s.split()), width=WIDTH,
                         break_long_words=False, break_on_hyphens=False)


def replace_once(text, anchor, replacement):
    pat = re.compile(ws(anchor))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1:\n  %s" % (n, anchor[:70]))
    m = pat.search(text)
    return text[:m.start()] + replacement + text[m.end():]


# ---------------------------------------------------------------- 1. op:koide-delta
ANCHOR_OP = r"""
Derive $\delta = 2/9$ from the holonomy of the octonionic Hopf connection. This is the single
most important open calculation in the mass sector. A derivation passes if it lands inside the
measured band, $\delta = 0.222225 \pm 0.000006$ radians, with no fitted input
(\S\ref{sec:koide-gap}). Three routes are closed: the simplest holonomy-squared model, $m_k
\propto \sin^4(\theta_0 + 2\pi k/3)$, does not reproduce the spectrum; the structural angles of
the bare sedenion triple contain no $2/9$ (Appendix~\ref{app:nb-M}); and the norm-defect
identity~\eqref{eq:debt-defect}, being a magnitude, cannot fix a phase.
"""

NEW_OP = fill(r"""
Derive $\delta = 2/9$ from the holonomy of the octonionic Hopf connection. This is the single
most important open calculation in the mass sector. A derivation passes if it lands inside the
measured band, $\delta = 0.222225 \pm 0.000006$ radians, with no fitted input; the invariant
target is $3\delta = 2/3$, the phase of the cyclic product of the three off-diagonal units
(Proposition~\ref{prop:koide-jordan}). It fails before any number is checked if it ends in an
algebraic value of $e^{i\delta}$ --- a root of unity, the argument of a configuration of
vectors with algebraic coordinates, the phase of a cyclic product of algebraic octonions ---
since $e^{2i/9}$ is transcendental (\S\ref{sec:koide-gap}). Four routes are closed: the
simplest holonomy-squared model, $m_k \propto \sin^4(\theta_0 + 2\pi k/3)$, does not
reproduce the spectrum; the structural angles of the bare sedenion triple contain no $2/9$
(Appendix~\ref{app:nb-M}); the norm-defect identity~\eqref{eq:debt-defect}, being a
magnitude, cannot fix a phase; and a coherent-state realisation of the triality frame, with
the phase as the enclosed phase-space area, cannot meet the amplitude and the phase at once.
""")

# ------------------------------------------------- 2. closing paragraph of sec:koide-gap
ANCHOR_GAP = r"""
The constraint is nonetheless informative. An angle that is a rational number of radians is an
arc-to-radius ratio, and arc-to-radius ratios come out rational where the arc is a run of unit
steps along a flat direction, not where it is a symmetric fraction of a round circle. If
$\delta$ is a holonomy at all, the connection carrying it is more likely flat along the
direction that matters --- the fibre circle, a torus --- than the round Hopf connection of Open
Problem~\ref{op:koide-delta}, and the computation to attempt is the one that specifies that flat
structure. We record this as a conjecture about where to look, not as a result.
"""

P_WHAT = fill(r"""
What the phase is. The triality form~\eqref{eq:z3} is not an ansatz laid over the Jordan
algebra; it is the spectrum of the simplest element of it.
""")

PROP = "\n".join([
    r"\begin{proposition}[The triality form as the spectrum of a democratic Jordan element]"
    r"\label{prop:koide-jordan}",
    fill(r"""
Let $X \in J_3(\mathbb{O})$ have unit diagonal and off-diagonal entries $x_1, x_2, x_3$ of a
common norm $\rho$, and write $x_i = \rho u_i$ with $u_i$ unit octonions and
$\operatorname{Re}(u_1u_2u_3) = \cos\Phi$. Then the eigenvalues of $X$ are
$1 + 2\rho\cos\bigl((\Phi + 2\pi k)/3\bigr)$, $k = 0, 1, 2$: the form~\eqref{eq:z3} with
$\alpha = 2\rho$ and $3\delta = \Phi$. The phase is well defined although the octonions are
not associative, and for $\rho = 1/\sqrt2$ it satisfies $|\Phi| \le \pi/4$, with equality
exactly when one eigenvalue vanishes.
"""),
    r"\end{proposition}",
    "",
    r"\begin{proof}",
    fill(r"""
The characteristic cubic of $X$ is $\lambda^3 - (\operatorname{tr}X)\lambda^2 + S(X)\lambda -
N(X)$ with $\operatorname{tr}X = 3$, $S(X) = 3 - 3\rho^2$ and cubic norm $N(X) = 1 - 3\rho^2 +
2\rho^3\cos\Phi$ \autocite{baez2002octonions}. Substituting $\lambda = 1 + 2\rho c$ reduces it
to $4c^3 - 3c = \cos\Phi$, whose roots are $c = \cos\bigl((\Phi + 2\pi k)/3\bigr)$. The real
part of a triple product is the same for either bracketing in any composition algebra, which is
what makes $\Phi$ well defined. For $\rho = 1/\sqrt2$ the smallest eigenvalue is $1 +
\sqrt2\cos\bigl((|\Phi| + 2\pi)/3\bigr)$, which is non-negative exactly when $|\Phi| \le
\pi/4$.
"""),
    r"\end{proof}",
])

P_READ = fill(r"""
The proposition says what the two numbers are inside the framework's own construction. The
amplitude $\alpha = \sqrt2$ is the statement that the off-diagonal entries have squared norm
one half; read through the Gram matrix of three generation states, whose entries are the
overlaps $\langle\psi_j|\psi_k\rangle$, it says that each pair is mutually unbiased,
$|\langle\psi_j|\psi_k\rangle|^2 = \tfrac12$, and the Koide ratio then follows exactly as in
Proposition~\ref{prop:koide}. The phase is the Bargmann invariant of the triple, the argument
of the cyclic product of the three overlaps, which is the one continuous invariant three states
possess beyond their overlaps; its octonionic form is the real part of the cyclic product of
the three off-diagonal units. The measured $3\delta = 0.6667$ sits at $0.85$ of the positivity
bound $\pi/4$, and to first order the electron's square-root mass is one third of the
shortfall, $\sqrt{m_e}/M \simeq (\pi/4 - 3\delta)/3$, accurate to two per cent. So the question
``why $2/9$'' is, precisely, ``why does the cyclic product of the three off-diagonal units have
real part $\cos(2/3)$''. The number to derive is the $\mathbb{Z}_3$-invariant $3\delta = 2/3$,
and it is worth recording that this is also the value of the Koide ratio: the invariant phase,
in radians, equals $\operatorname{tr}X^2/(\operatorname{tr}X)^2$. We have no mechanism that
makes a phase equal a trace ratio and record the equality as a rhyme.
""")

P_KIND = fill(r"""
What kind of number it must be. If $\delta = 2/9$ exactly then $e^{i\delta}$ is
transcendental, by the Lindemann--Weierstrass theorem: $e^{a}$ is transcendental for every
non-zero algebraic $a$. The consequences are sharp. The cyclic product $u_1u_2u_3$ cannot be an
algebraic octonion, so no construction of the three entries from the structure constants, from
roots of unity, from a finite group, or from any configuration of vectors with algebraic
coordinates can be exact; the holonomy of a round connection around a geodesic polygon with
algebraic vertices is the argument of exactly such a product and is excluded with them. Every
charged-lepton mass ratio is then a transcendental number, since each is a non-constant
rational function of $e^{i\delta}$ with algebraic coefficients. Conversely, any mechanism that
returns an algebraic value for a single mass ratio returns a $\delta$ that is zero or
transcendental, and must then explain the agreement with $2/9$ as an accident: a fraction with
denominator at most nine lands in the six-sigma band by chance about once in a thousand trials.
What survives is the class in which the phase is the exponential of a rational number --- an
action or a symplectic area in units of $\hbar$, a length along a flat direction in units of
its radius, a Lie-algebra generator with a rational coefficient. That is the precise content of
``flat rather than round''.
""")

P_TORUS = fill(r"""
Flat, but not a torus. On a compact flat torus a quantised flux makes every enclosed phase a
rational multiple of $2\pi$, which is the family the scan excludes; and a flat connection whose
holonomy is not quantised is a modulus, a free parameter that the geometry leaves open. The
flat structure carrying the phase must be non-compact in the direction that matters, and the
rational number is then most naturally an area, the product of two rational lengths in units of
$\hbar$. The one such reading we have found is a rhyme: $3\delta = 2/3 = 2\cdot(1/\sqrt3)^2$ is
the commutator phase of two orthogonal phase-space displacements of squared amplitude one third,
the equal-weight number. The obvious model built on it --- three coherent states at the vertices
of an equilateral triangle, mass roots the eigenvalues of their Gram matrix, phase twice the
enclosed area --- has one parameter and two targets and fails both ways: fixing the overlap at
$1/\sqrt2$ gives a phase of $0.600$ rather than $0.667$, and fixing the phase gives an amplitude
of $1.361$ rather than $\sqrt2$. We record the shape of the derivation as a constraint, the
model as a closed route, and the earlier suggestion of a torus as superseded.
""")

NEW_GAP = "\n\n".join([P_WHAT, PROP, P_READ, P_KIND, P_TORUS])


def main():
    with open(MASSES, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (MASSES, HEADER.strip()))
    text = replace_once(text, ANCHOR_OP.strip(), NEW_OP)
    text = replace_once(text, ANCHOR_GAP.strip(), NEW_GAP)
    for lab in (r"\label{prop:koide-jordan}", r"\label{sec:koide-gap}", r"\label{op:koide-delta}"):
        if text.count(lab) != 1:
            sys.exit("REFUSING: label %s occurs %d times after the edit" % (lab, text.count(lab)))
    shutil.copy(MASSES, MASSES + "." + STAMP + ".bak")
    with open(MASSES, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak)" % (MASSES, MASSES, STAMP))


if __name__ == "__main__":
    main()
