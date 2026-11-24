#!/usr/bin/env python3
"""patch_qutrit_hopf_rulings_2026-11-07T1700.py

Applies the seven findings (a)--(g) of section 9 of
knowledge/sessions/qutrit_hopf_picture_2026-11-07T1600.md, all accepted by
JS on 2026-11-07 ("I accept all your recommendations in section 9").
Every statement patched in is verified by scripts/qutrit_hopf_picture_2026-11-07T1600.py
(PASS, 0 FAIL, seed 20261107), in the paper's own conventions (app:setup).

  (a) knowledge/project-docs/open_problem_qudit_degeneration.md: ninth
      property P9 (the maximal Bell violation leaves the maximally entangled
      state at d = 3; CGLMP), a row in the Part A table, two references.
      Support read against Acin, Durt, Gisin and Latorre 2002 (arXiv
      quant-ph/0111143v2 HTML, Secs. II--III, Eqs. (3), (8), (9)).
  (b) paper1/entanglement_classes_and_gauge_groups_2026-06-08.tex: after the
      "base decomposes" paragraph, one paragraph placing the colour qutrit on
      the colour equator, fibred over CP^2 by the record circle, with colour
      SU(3) acting on the register as diag(1, SU(3)) on the two internal
      qubits (entangling, fixing the record amplitude).
  (c) paper1/interactions_circuits_section_2026-06-08.tex: parenthesis
      distinguishing the generation "qutrit" (a three-element label) from the
      continuous colour C^3.
  (d) paper1/confinement_section_2026-06-13.tex: Proposition
      prop:singlet-quaternion after op:confinement-energy-locus -- the colour
      singlet as associative 3-form plus record-line associator; a unitary
      frame closes up to the phase of its determinant; an SU(3) frame spans a
      quaternion subalgebra. Harvey--Lawson is cited for the associative-plane
      theorem: VERIFY-SUPPORT (the 1982 paper could not be fetched today).
      The coassociative reading is labelled a conjecture in the text.
  (e) paper1/spacetime_from_non-computability.tex, sec:three-dimensions:
      one-sentence cross-reference to prop:singlet-quaternion, labelled a
      rhyme.
  (f) paper1/appendices/appendix_ghz_w_proofs_2026-06-11.tex: remark after
      the proof of app:lem:base -- the base is a function of the vector, not
      the ray; the results used are functions of rho_1 and are safe.
  (g) paper1/quantum_numbers_section_2026-06-08.tex: two sentences keeping the
      two "qutrits" (colour C^3; the generations' three-element set) apart.

Conventions: anchors must match exactly once (whitespace-insensitive); a .bak
is written beside each target; an `% EDITED` header is added (an HTML comment
for the Markdown file); the script refuses to run twice. `--check` verifies
the anchors and writes nothing. Citation kimura2003bloch is in
bib/qutrit_hopf_refs_2026-11-07T1610.bib and is undefined until JS imports it
(expected, per CLAUDE.md). Nothing here builds or commits.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-11-07"
STAMP = "2026-11-07T1700"
SCRIPT = Path(__file__).name
TEX_HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
MD_HEADER = "<!-- EDITED %s scripts/%s -->\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]


def ws(s):
    """Whitespace-insensitive literal pattern."""
    return r"\s+".join(re.escape(t) for t in s.split())


# ---------------------------------------------------------------------------
# (b) entanglement classes: the colour qutrit's address on the base
# ---------------------------------------------------------------------------
B_ANCHOR = r"""rows share the same fibre and are separated as disjoint loci on the base: on the colour equator, or
tilted off it into the single-qubit Bloch directions."""
B_ADD = r"""

The colour equator has a second name, and the two should be said together. The $\mathbb{C}^3$ of the
base, read as a three-level system, is a colour qutrit, and the equatorial $S^5$ is exactly its unit
sphere. Left multiplication by the record circle $\exp(\theta e_1)$ is the global phase of a branch
and acts on $\mathbb{C}^3$ as the scalar $e^{\mathrm{i}\theta}$, so the colour equator fibres over
$\mathbb{CP}^2$ by the qutrit's own phase bundle $S^1\to S^5\to\mathbb{CP}^2$, and the only part of
that circle that is an automorphism of $\mathbb{O}$ is its centre $\mathbb{Z}_3$. The colour
$SU(3)$ --- the stabiliser of $e_1$, exponentiated --- acts on each branch
$\mathbb{C}^4 = \mathbb{C}\oplus\mathbb{C}^3$ of the register as $\mathrm{diag}(1, U_3)$ with
$U_3\in SU(3)$: on the two internal qubits it fixes the record amplitude $\lvert 00\rangle$ and
rotates the span of $\lvert 01\rangle, \lvert 10\rangle, \lvert 11\rangle$, and it is an entangling
gate (operator-Schmidt rank four), never a local rotation of either qubit. So the colour qutrit of a
quark is the two internal qubits with the record direction removed. A qutrit has no Hopf fibration
of its own, since the base of $S^5\to\mathbb{CP}^2$ is not a sphere
\autocite{adams1960hopf}, and no Bloch ball \autocite{kimura2003bloch}; what it has is this address
on the three-qubit base, where the colour radius $\lvert w\rvert$ of Appendix~\ref{app:setup} is its
only state property (the colour \emph{direction} on the base is a function of the state vector, not
of the ray, Appendix~\ref{app:lem:base}). An executable verification accompanies the code release."""

# ---------------------------------------------------------------------------
# (c) interactions: which qutrit
# ---------------------------------------------------------------------------
C_ANCHOR = r"""generation register --- a qutrit, or two qubits encoding the triality sector of
\S\ref{sec:generations} --- and promote the $W$ gate"""
C_NEW = r"""generation register --- a qutrit, or two qubits encoding the triality sector of
\S\ref{sec:generations} (a qutrit in the sense of a three-element label, not the continuous colour
$\mathbb{C}^3$ of \S\ref{sec:entanglement-classes}, whose own qutrit is the colour equator) --- and
promote the $W$ gate"""

# ---------------------------------------------------------------------------
# (d) confinement: the singlet as a quaternion triple
# ---------------------------------------------------------------------------
D_ANCHOR = r"""The binding remains in either case
intrinsic and relational, the property of no vacuum medium.
\end{openproblem}"""
D_ADD = r"""

The colour singlet itself has an octonionic form that the dictionary of Appendix~\ref{app:setup}
makes exact, and it is worth stating because it joins the baryon vertex to two other places in the
paper.

\begin{proposition}[The colour singlet is a quaternion triple]\label{prop:singlet-quaternion}
Embed colour vectors $v\in\mathbb{C}^3$ in $\mathbb{O}$ by the block map~\eqref{eq:embedding} of
Appendix~\ref{app:setup}, so that $\mathbb{C}^3 = \operatorname{span}\{e_2,\dots,e_7\} = e_1^{\perp}
\cap \operatorname{Im}\mathbb{O}$ with complex structure $J = L_{e_1}$, and write
$[a,b,c] = (ab)c - a(bc)$ for the associator. Then for all colour vectors $v_1, v_2, v_3$,
\begin{equation}
  \det[v_1\; v_2\; v_3]
  \;=\; \langle v_1,\, v_2 v_3\rangle \;+\; \tfrac{\mathrm{i}}{2}\,\bigl\langle e_1,\,[v_1,v_2,v_3]\bigr\rangle ,
  \label{eq:singlet-calibration}
\end{equation}
the real part being the associative three-form $\varphi(x,y,z) = \langle xy, z\rangle$ of
Proposition~\ref{prop:zd-defect}, which on imaginary arguments equals $\langle x, yz\rangle$, and the
imaginary part the coassociative four-form with the record unit in its first slot. Consequently a
unitary colour frame closes under the octonion product up to the phase of its determinant,
$v_1 v_2 = \overline{\det[v_1\,v_2\,v_3]}\;v_3$ and cyclically, with the scalar acting through $J$;
an $SU(3)$ frame closes exactly, and together with $e_0$ spans a quaternion subalgebra of
$\mathbb{O}$. The colour-singlet baryon is therefore a copy of $\mathbb{H}$ inside the colour
$\mathbb{C}^3$: an associative three-plane, which by Harvey and Lawson's theorem is the imaginary
part of a quaternion subalgebra \autocite{harvey1982calibrated}.
\end{proposition}

\begin{proof}[Proof sketch]
Both sides of~\eqref{eq:singlet-calibration} are trilinear over $\mathbb{R}$ and totally
antisymmetric in $(v_1, v_2, v_3)$, so it suffices to check them on the basis triples of
$\{e_2,\dots,e_7\}$, where the table~\eqref{eq:fano-lines} gives each product directly; the
imaginary part follows from $\langle e_1, (v_1 v_2) v_3\rangle = -\langle e_1, v_1 (v_2 v_3)\rangle$
on colour vectors. In the $\mathbb{C}^3$ model of the octonions this is the decomposition of
$\varphi$ restricted to $\mathbb{R}\oplus\mathbb{C}^3$ into $e^{1}\wedge\omega + \operatorname{Re}
\Omega$, with $\Omega$ the holomorphic volume form whose value on a frame is its determinant. The
closure statement is~\eqref{eq:singlet-calibration} read with the product rule
$\pi_{\mathbb{C}}(vw) = -\overline{\langle v, w\rangle}$ and $\mathrm{colour}(vw) = \overline{v\times w}$
of the same model. Every identity is verified to machine precision in the code release.
\end{proof}

Three remarks fix what the proposition does and does not say. First, it closes a fence left by the
budget argument of \S\ref{sec:budget-converse}: the singlet's one-quark marginal is maximally mixed,
$r = 0$ for every party, exactly as for $\mathrm{GHZ}_3$, but its two-quark marginal is not
separable --- two colours of a quaternion triple fix the third, $v_1 v_2 = v_3$, and the pair is the
antisymmetric Werner state --- so ``every pairwise correlation zero'' is a statement about the
register's $\mathrm{GHZ}_3$ and not about the colour singlet, and the form of the budget argument the
two share is the one-to-rest saturation $r^2 = 0$. Second, the condition on the frame is
the condition of \S\ref{sec:three-dimensions} under which three relays compose: both a
colour-singlet baryon and a consistent three-link network are associative triples in $\mathbb{O}$,
one inside the colour $\mathbb{C}^3$ and one inside the $S^3$ of relays. That is a rhyme, recorded
and not built on. Third, the imaginary part of~\eqref{eq:singlet-calibration} is the coassociative
calibration with the record unit in the first slot, the same form that the norm defect of
Appendix~\ref{sec:zd-structure} and the associator-debt of \S\ref{sec:masses} are built from; that
the phase of a baryon's colour frame should therefore be a handle on its binding is a conjecture,
flagged for Open Problem~\ref{op:confinement-energy-locus}, with nothing computed."""

# ---------------------------------------------------------------------------
# (e) spacetime: the rhyme
# ---------------------------------------------------------------------------
E_ANCHOR = r"""so the largest consistent network inside $S^{7}$ is an $S^{3}$
\autocite{conway_2003,harvey1982calibrated}.)"""
E_ADD = r""" The same condition reappears, with no mechanism connecting the two, as
the colour singlet of \S\ref{sec:confinement}: an $SU(3)$ colour frame spans one quaternionic
subalgebra (Proposition~\ref{prop:singlet-quaternion}), so a consistent three-relay network and a
colour-singlet baryon are both associative triples in $\mathbb{O}$, one inside the $S^{3}$ of relays
and one inside the colour $\mathbb{C}^{3}$. We record the coincidence as a rhyme and do not build on
it."""

# ---------------------------------------------------------------------------
# (f) appendix: vector, not ray
# ---------------------------------------------------------------------------
F_ANCHOR = r"""the second identity in~\eqref{eq:base-split} is $|H|^2 = 1$ with $|2\mathbf{h}|^2 =
|2\pi_{\mathbb{C}}|^2 + |w|^2$.
\end{proof}"""
F_ADD = r"""

\begin{remark}
The base point $H(\psi)$ is a function of the state \emph{vector}, not of the ray. A global phase
$\psi\mapsto e^{\mathrm{i}\theta}\psi$ multiplies both branches by $e^{\mathrm{i}\theta}$, which the
embedding~\eqref{eq:embedding} realises as left multiplication by $\exp(\theta e_1)$; since
$\mathbb{O}$ is not commutative, $o_1\bar o_2$ is not invariant under it, and the colour direction
$w/\lvert w\rvert$ moves in general (on the coloured-GHZ family $\lvert 0\rangle\lvert 00\rangle +
\lvert 1\rangle\lvert c\rangle$ it rotates by $e^{2\mathrm{i}\theta}$). What is invariant is
everything the lemmas use: $x_9$, $\lvert\pi_{\mathbb{C}}(\mathbf{h})\rvert$ and the colour radius
$\lvert w\rvert$ are functions of the reduced state $\rho$, as the lemma shows, and the loci of
\S\ref{sec:canonical-orbits} are defined by them. No statement in this paper reads the colour
direction as a property of a ray, and none should.
\end{remark}"""

# ---------------------------------------------------------------------------
# (g) quantum numbers: two qutrits
# ---------------------------------------------------------------------------
G_ANCHOR = r"""Electric charge is then quantised in thirds, with leptons landing on
integers because they are colour singlets --- the same structural fact, read through $Q = T_3 +
\tfrac12 Y$."""
G_ADD = r"""

One word is used in two senses across the paper and should be kept apart here. The colour
$\mathbb{C}^3$ is a qutrit in the continuous sense --- a three-dimensional complex space, whose unit
sphere is the colour equator of \S\ref{sec:entanglement-classes} and on which the colour $SU(3)$
acts in the fundamental --- while the generation register of \S\ref{sec:interactions} is a qutrit
only as a three-element set, the $S_3$ label of \S\ref{sec:generations}, on which no colour
rotation acts. The colour triality locked to hypercharge above belongs to the first; the triality of
the generations belongs to the second."""

# ---------------------------------------------------------------------------
# (a) qudit degeneration document: P9
# ---------------------------------------------------------------------------
A1_ANCHOR = r"""- *Fails for d ≥ 3*: Goyal et al. (2016) showed that there exist families of two-sections and three-sections of Ω₃ that are geometrically equivalent but *not* unitarily equivalent. This is a direct consequence of SU(3) being a proper subgroup of SO(8)."""
A1_ADD = r"""

**P₉ (Maximal Bell violation at maximal entanglement).** The maximal violation of the natural two-party Bell inequality is attained by the maximally entangled state. *(Added 2026-11-07; `knowledge/sessions/qutrit_hopf_picture_2026-11-07T1600.md`, script E.)*

- *Holds for d = 2*: the CHSH expression reaches Tsirelson's bound 2√2 exactly on the maximally entangled state, whose marginal is the unique centre of the Bloch ball. The framework's monogamy aside reads the bound as that centre: the budget is spent when the marginal reaches it, and there is no point past it.
- *Fails for d = 3*: for the CGLMP inequality (Collins et al. 2002) with the standard Fourier settings, the maximally entangled state gives I₃ = 4(2√3 + 3)/9 ≈ 2.8729, while the state (|00⟩ + γ|11⟩ + |22⟩)/√(2 + γ²) with γ = (√11 − √3)/2 ≈ 0.7923 gives 1 + √(11/3) ≈ 2.9149 (Acín, Durt, Gisin & Latorre 2002, Eqs. (3), (8), (9)); their numerical search over all von Neumann settings and states finds no larger value, and POVMs are not excluded. The centre argument of the monogamy aside is therefore qubit-specific: at d = 3 the maximally mixed marginal 𝟙/3 is not the midpoint of any pair of antipodal pure states (P₇) and the Bloch body is not a ball (P₁), so moving the marginal off centre can increase the violation. Reproduced to six figures in the framework's script (2.872934 at γ = 1; 2.914854 at γ = 0.79229)."""

A2_ANCHOR = r"""| P₈ (geom = unitary) | — | Follows from P₁: if the state space is a round ball acted on transitively by the structure group, geometric and group equivalence coincide. |"""
A2_ADD = r"""
| P₉ (Bell maximum at maximal entanglement) | — | Follows from P₁ and P₇ (candidate, 2026-11-07): the Tsirelson argument needs the maximally mixed marginal to be the unique centre of a ball with pure states antipodal across it; at d = 3 neither holds, and the optimal CGLMP state is not maximally entangled. |"""

A3_ANCHOR = r"""### Hopf Fibrations and Entanglement"""
A3_ADD = r"""### Bell Inequalities for Qutrits (added 2026-11-07)
- Collins, D., Gisin, N., Linden, N., Massar, S. & Popescu, S. "Bell inequalities for arbitrarily high-dimensional systems." Phys. Rev. Lett. 88, 040404 (2002). [quant-ph/0106024]
- Acín, A., Durt, T., Gisin, N. & Latorre, J.I. "Quantum nonlocality in two three-level systems." Phys. Rev. A 65, 052325 (2002). [quant-ph/0111143] — the γ ≈ 0.7923 state, Eqs. (3), (8), (9); support read against the arXiv v2 text.

"""

EDITS = [
    # (target, header, [(kind, anchor, text), ...])  kind: 'after' inserts text after the anchor; 'replace' replaces it
    ("paper1/entanglement_classes_and_gauge_groups_2026-06-08.tex", TEX_HEADER,
     [("after", B_ANCHOR, B_ADD)]),
    ("paper1/interactions_circuits_section_2026-06-08.tex", TEX_HEADER,
     [("replace", C_ANCHOR, C_NEW)]),
    ("paper1/confinement_section_2026-06-13.tex", TEX_HEADER,
     [("after", D_ANCHOR, D_ADD)]),
    ("paper1/spacetime_from_non-computability.tex", TEX_HEADER,
     [("after", E_ANCHOR, E_ADD)]),
    ("paper1/appendices/appendix_ghz_w_proofs_2026-06-11.tex", TEX_HEADER,
     [("after", F_ANCHOR, F_ADD)]),
    ("paper1/quantum_numbers_section_2026-06-08.tex", TEX_HEADER,
     [("after", G_ANCHOR, G_ADD)]),
    ("knowledge/project-docs/open_problem_qudit_degeneration.md", MD_HEADER,
     [("after", A1_ANCHOR, A1_ADD), ("after", A2_ANCHOR, A2_ADD), ("before", A3_ANCHOR, A3_ADD)]),
]


def apply(text, edits, name):
    for kind, anchor, add in edits:
        hits = list(re.finditer(ws(anchor), text))
        if len(hits) != 1:
            sys.exit("%s: anchor matched %d times:\n%s" % (name, len(hits), anchor[:80]))
        m = hits[0]
        if kind == "after":
            text = text[:m.end()] + add + text[m.end():]
        elif kind == "before":
            text = text[:m.start()] + add + text[m.start():]
        elif kind == "replace":
            text = text[:m.start()] + add + text[m.end():]
        else:
            sys.exit("unknown edit kind " + kind)
    return text


def main():
    plans = []
    for rel, header, edits in EDITS:
        target = ROOT / rel
        text = target.read_text()
        if header.strip() in text:
            sys.exit("%s: refusing to run twice" % rel)
        if rel.endswith(".md"):
            # header goes after the title line, so the file still starts with its heading
            first_nl = text.index("\n") + 1
            new = text[:first_nl] + MD_HEADER + apply(text[first_nl:], edits, rel)
        else:
            new = header + apply(text, edits, rel)
        plans.append((target, new))
        print("verified: %s (%d edit%s)" % (rel, len(edits), "" if len(edits) == 1 else "s"))
    if CHECK:
        print("--check: nothing written")
        return
    for target, new in plans:
        shutil.copyfile(target, target.with_name(target.name + "." + STAMP + ".bak"))
        target.write_text(new)
        print("patched: %s" % target.relative_to(ROOT))


if __name__ == "__main__":
    main()
