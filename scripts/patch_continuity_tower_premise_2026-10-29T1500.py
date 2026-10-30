#!/usr/bin/env python3
"""Continuity: the completion named as the classical convention, density derived from the
inside/outside tower, and op:limit-realisability restated.

Companion to knowledge/sessions/relational_state_continuity_2026-10-28T1200.md (sections 10 to
15). JS, 2026-10-29: "I accept the proposed changes to the paper." The finding: Hardy's fifth
axiom is density of pure states plus completion. The completion is the real-number convention
of every probability theory, declared at the Shannon step and carrying no quantum content (the
algebraic theory has everything quantum and is not complete); it is adopted on stated grounds,
not derived, because no first-order principle can give it. The density is derived, in outline,
from the paper's own premise: every transformation the inside performs must have a stationary
outside presentation (the inside/outside involution as a genuine involution, time as internal
operation count, no record before FANOUT), hence an admissible eigenbasis, hence a fixed point;
fixed points with transitivity give infinite order and density. The remaining open item is the
rigour of that derivation inside Fix(sigma).

Eight files, one header each, one run only.

paper1/continuity_section_2026-07-04.tex
  1. Opening paragraph: "one premise about values" becomes one premise about transformations,
     with the completion named.
  2. The foils paragraph after prop:connected-transitive gains a closing sentence.
  3. "The premises, and what they mean": the value-premise and closedness text is replaced by
     three paragraphs: the split of connectedness into density and completion; the completion
     as the classical convention, with its grounds; the density from the tower, with the
     premise (I), its derivation sketch and its consequences.
  4. op:limit-realisability restated (label kept: it is cross-referenced from six files);
     new title.
  5. The closing accounting sentence.
paper1/L2_metric_global_phase_section_2026_06_07.tex, paper1/what_is_a_quantum_state.tex,
paper1/derivation_of_the_quantum_postulates.tex, paper1/self_reference_section_2026-07-04.tex,
paper1/summary_section_2026-07-07.tex, paper1/main.tex
  6. The sentences describing the open problem as a premise about values are re-pointed.

Citations: existing keys only, except pagewootters1983evolution and coeckeduncan2011interacting,
batched in bib/continuity_tower_refs_2026-10-29T1500.bib (Crossref-verified; VERIFY-SUPPORT in
the text until read). Until the batch is imported the build reports them undefined; expected.

Every anchor is matched whitespace-insensitively and must match exactly once; edited prose is
filled to 96 columns. A dated .bak is written per file, a "% EDITED" header is prepended, and
the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-10-29"
STAMP = "2026-10-29T1500"
SCRIPT = "scripts/patch_continuity_tower_premise_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

CONT = "paper1/continuity_section_2026-07-04.tex"
L2 = "paper1/L2_metric_global_phase_section_2026_06_07.tex"
WIQS = "paper1/what_is_a_quantum_state.tex"
POST = "paper1/derivation_of_the_quantum_postulates.tex"
SELF = "paper1/self_reference_section_2026-07-04.tex"
SUMM = "paper1/summary_section_2026-07-07.tex"
MAIN = "paper1/main.tex"
FILES = [CONT, L2, WIQS, POST, SELF, SUMM, MAIN]


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


# ------------------------------------------------------------------ 1. continuity: intro
OLD_INTRO = r"""
Continuity is the fifth face of the pre-measurement regime that
self-reference forces, and what stands between the framework and a full derivation is not a
postulate about transformations but one premise about values, stated as an open problem at the
end of the section with nothing hidden in it.
"""
NEW_INTRO = fill(r"""
Continuity is the fifth face of the pre-measurement regime that self-reference forces, and
what stands between the framework and a full derivation is not a postulate about values but one
premise about transformations --- that every transformation the inside performs has a
stationary outside presentation --- derived in outline below from the inside/outside involution
of \S\ref{sec:self-reference} and stated as an open problem at the end of the section with
nothing hidden in it. The continuum itself, the completion that every probability theory
adopts, is named for what it is: the real line, shared with classical probability and carrying
no quantum content.
""")

# ------------------------------------------------------------------ 2. continuity: foils
OLD_FOILS_END = r"""
Divisibility, which both also lack --- the phase gate has no square root in the
Clifford group --- is a symptom of the discreteness, not its cause.
"""
NEW_FOILS_END = fill(r"""
Divisibility, which both also lack --- the phase gate has no square root in the Clifford group
--- is a symptom of the discreteness, not its cause. What both lack can be said exactly, and the
next subsection says it: each contains a transformation that fixes no state it admits.
""")

# ------------------------------------------------------------------ 3. continuity: premises
OLD_PREMISES = r"""
Connectedness of the state space is
a premise about values --- that self-referential ignorance is not rationed --- and it is the one
that remains open; it is stated at the end of the section. Divisibility, which an earlier
version of this section asked for, is not needed: it follows from the conclusion, every element
of a compact connected Lie group having roots of every order, and its candidate derivation from
``no distinguished step'' is retired with it. Closedness is the deeper premise conceptually, and
it is where the section's title is earned. Closedness is limit-realisability: a Cauchy sequence
of available transformations whose convergence the system can itself describe must have its
limit available, for otherwise the system's own description refers to a transformation that does
not exist, and self-referential closure fails --- a demand of exactly Lawvere's fixed-point
shape \autocite{Lawvere_1969,Yanofsky2003}. What limit-realisability adds to the line is worth
stating exactly, because it is the corrected form of a natural intuition. Cantor's diagonal
\autocite{cantor1891diagonal} does not build the continuum; its output is an infinite decimal
--- a Cauchy sequence of rationals --- which exists \emph{as a point} only because the line is
complete. The diagonal presupposes limit-realisability and then shows that the completed line
outruns every internal listing. And the character of the completion is the framework's own: the
computable reals are countable \autocite{Turing_1937}, hence of measure zero, so the completed
continuum is non-computable almost everywhere. Hardy's fifth axiom, on this reading, is the
demand that the transformation group contain its \emph{non-computable} limits. Continuity is the
topological face of the founding non-computability. We record closedness, all the same, as the
framework's adopted stance rather than as a theorem: the same founding premise admits a
constructive reading on which only describable limits exist --- a computable Cauchy sequence of
rationals can have a non-computable limit, and the two readings part exactly there --- and the
stance taken here is the operational one, that a limit no experiment can certify absent is
admitted, which Hardy's own axioms take for granted.
"""

P_SPLIT = fill(r"""
Connectedness of the state space is two statements, and only one of them is quantum. The
first is that the pure states are infinite and dense, with a fixed point for every
transformation; the second is that the state space is complete. Quantum theory over the
algebraic numbers --- amplitudes in the algebraic closure of $\mathbb{Q}$ within $\mathbb{C}$
--- has the first without the second: it has $K = N^{2}$, the Born rule, superposition,
entanglement and Bell violation at the Tsirelson value, every unitary has an algebraic
eigenvector, and it is countable and totally disconnected. So the whole quantum content of
Hardy's axiom lies in the density, and the completion is the real-number convention of every
probability theory. Hardy adopts it before his fifth axiom is stated, in the first, which makes
probabilities real numbers and gives his classical theory a real simplex of mixtures; this
framework adopts it at the Shannon step, where credences are declared to range over a connected
domain so that the continuation of the logarithm is unique (\S\ref{sec:complex-amplitudes}).
Given that convention, density of the pure states is connectedness of their closure. Divisibility,
which an earlier version of this section asked for, is not needed: it follows from the
conclusion, every element of a compact connected Lie group having roots of every order.
""")

P_COMPLETION = fill(r"""
Closedness is the completion, limit-realisability: a Cauchy sequence of available
transformations has its limit available. It cannot be derived, and the reason should be stated
rather than hidden. Any collection of first-order principles about states, transformations and
probabilities that has an infinite model has a countable one, and a countable subset of
$\mathbb{CP}^{K-1}$ is totally disconnected; the founding non-computability does not escape
this, since the arithmetical complex numbers form a countable algebraically closed field
containing non-computable numbers and closed under every limit it can itself describe. Hardy's
axiom and closedness are second-order, quantifying over paths and over sequences, and a
second-order principle is grounded as Dedekind completeness is grounded or not at all. The
grounds are these. The completion of a dense set under the finite-precision metric is unique
and depends on no choice, whereas any countable alternative is a choice of definability level,
an extra law with no ground and no test; and the framework's own result is that no observer's
descriptive level captures the regime, since by \S\ref{sec:self-reference} every observer's
state exceeds its own level and the inside/outside principle makes that a law rather than a
perspective. The burden therefore falls on any restriction, not on the completion, which is the
least committal option and carries no quantum content. What limit-realisability adds to the
line is still worth stating exactly, because it is the corrected form of a natural intuition.
Cantor's diagonal \autocite{cantor1891diagonal} does not build the continuum; its output is an
infinite decimal --- a Cauchy sequence of rationals --- which exists \emph{as a point} only
because the line is complete. The diagonal presupposes limit-realisability and then shows that
the completed line outruns every internal listing. And the character of the completion is the
framework's own: the computable reals are countable \autocite{Turing_1937}, hence of measure
zero, so once the transformation group contains its limits almost all of them are
non-computable. Non-computability is a property of the completed continuum, not the reason for
it. The constructive reading, on which only describable limits exist, remains consistent; it
is the countable theory above, and the two readings differ in nothing an experiment can
certify.
""")

P_DENSITY = fill(r"""
Density is where the section's title is earned, and it is derived from the paper's own premise.
Write $(\mathrm{I})$ for the statement that every admissible transformation of the regime is a
phase of some admissible classical structure: diagonal, that is, in the record basis of some
observer the regime contains, a phased spider of that basis in the calculus of
\S\ref{sec:hopf-justification} \autocite{coeckeduncan2011interacting} (VERIFY-SUPPORT). It says
of transformations what the global phase of \S\ref{sec:self-reference} says of states: there
are no absolute ones. It follows from three things the paper already holds. The inside/outside
involution is a genuine involution, so the outside presentation of the inside is a presentation
of the same object with nothing lost: the outside can have complete knowledge of the inside,
a potential record, the joint state lying in a structure the outside carries. Time is operation
count, internal to the system that operates (\S\ref{sec:space-of-computations}), so the outside
does not share the inside's count. And before any \textsc{fanout} that count is not classically
recorded, so the outside's description is pure. Let $g$ be the transformation the inside
performs per operation. The outside's complete knowledge cannot depend on the inside's count,
and it is pure, so it is a pure state of the inside's clock and system that is stationary under
``advance the clock and apply $g$''; the stationary states of that map are clock Fourier modes
tensored with eigenvectors of $g$ and nothing else \autocite{pagewootters1983evolution}
(VERIFY-SUPPORT). So the outside holds a structure in which $g$ acts by phases, which is
$(\mathrm{I})$; and the relative phase in that structure is the outside's ignorance of the
inside's computational count, the same ignorance the global phase records one level down. The
consequences are a theorem. A phase of a structure fixes the structure's copyable states, so
every admissible transformation fixes an admissible pure state; a finite transitive action has
an element moving every point (Jordan), so the pure states are infinite; the transformation
carrying a stabiliser state to the fixed point of the composite of a $Z$-phase and an $X$-phase
turns through $\arccos(1/\sqrt{3})$, an irrational fraction of a turn, so the group has an
element of infinite projective order and its orbits are dense. With the completion,
Proposition~\ref{prop:connected-transitive} fires and Hardy's fifth axiom holds. The two foils
fail $(\mathrm{I})$ exactly where they fail continuity: fourteen of the twenty-four Clifford
operations are phases of no Pauli basis and fix no stabiliser state, their fixed points being
the magic states; the toy theory's three-cycles are phases of no epistemic basis; and in each
the outside's knowledge of the inside under the order-three protocol is either count-dependent
or a mixture over the count, so each makes the inside's time classical before any record
exists. The derivation of $(\mathrm{I})$ is an outline, not a proof, and it is what the open
problem below asks for.
""")

NEW_PREMISES = P_SPLIT + "\n\n" + P_COMPLETION + "\n\n" + P_DENSITY

# ------------------------------------------------------------------ 4. continuity: open problem
OLD_OP_BEGIN = r"""
\begin{openproblem}[The value continuum from self-reference]\label{op:limit-realisability}
"""
OLD_OP_END = r"""
theorem, cited; the finite, countable and disconnected escapes are closed unconditionally above.
\end{openproblem}
"""
NEW_OP = "\n".join([
    r"\begin{openproblem}[Every transformation a phase of an inside structure]\label{op:limit-realisability}",
    fill(r"""
Proposition~\ref{prop:connected-transitive} reduces Hardy's fifth axiom to three premises:
connectedness of the pure states, transitivity, and closedness. Transitivity is argued above
from the absence of records. Closedness is the completion, adopted on the grounds stated above
and carrying no quantum content. Connectedness is density plus that completion, and density
follows, by Jordan's theorem and the infinite-order argument, from $(\mathrm{I})$: that every
admissible transformation of the regime is a phase of some admissible classical structure. What
remains open is the rigour of the derivation of $(\mathrm{I})$ from the paper's premise. Derive,
inside the fixed-point locus $\mathrm{Fix}(\sigma)$ of Proposition~\ref{prop:inside-outside},
that every endomap is a phase of a classical structure in $\mathrm{Fix}(\sigma)$, from the
self-representing object, the involution $\sigma$ as a genuine involution, and the reading of
the inside presentation as a sequence indexed by operation count with no record before
\textsc{fanout}. The outline above does this with the stationary-state construction of Page and
Wootters; a derivation passes if it makes that outline a theorem of the calculus, with the
outside's count-independent complete description shown to exist and to be pure from the
involution alone. It fails before any detail is checked if every premise it uses holds in the
stabiliser fragment of quantum theory, in Spekkens's toy theory \autocite{spekkens2007toy}, in
the real qubit, or in quantum theory over the Gaussian rationals, all of which violate
$(\mathrm{I})$ outright and all of which make the inside's operation count classical before any
record exists. It also fails if it imports the completion as a premise about transformations:
the completion is the real line and has no derivation, and a derivation of $(\mathrm{I})$ must
hold in the countable algebraic theory, where $(\mathrm{I})$ is true and continuity is not.
"""),
    r"\end{openproblem}",
])

# ------------------------------------------------------------------ 5. continuity: accounting
OLD_ACCOUNT = r"""
The accounting, in one sentence: the axiom that every reconstruction programme pays is, in this
framework, a debt with a stated invoice --- two derivations, both of Lawvere's shape, both posed. And
"""
NEW_ACCOUNT = fill(r"""
The accounting, in one sentence: the axiom that every reconstruction programme pays is, in this
framework, one derivation posed, of Lawvere's shape --- that every endomap of the fixed-point
locus is a phase of a classical structure in it --- and one convention named, the completion,
which classical probability pays too. And
""")

# ------------------------------------------------------------------ 6. cross-references
XREFS = [
    (L2,
     r"""
on the premises priced as Open Problem~\ref{op:limit-realisability}, of which one, the
value continuum, remains open. That premise is the one the Shannon step declares
(\S\ref{sec:complex-amplitudes}), and
""",
     fill(r"""
on the premises priced as Open Problem~\ref{op:limit-realisability}, of which one, that every
transformation of the regime is a phase of an inside structure, remains open; the continuum
itself is the completion the Shannon step declares (\S\ref{sec:complex-amplitudes}), the
classical convention, and
""")),
    (L2,
     r"""
derived from a premise every physicist
grants and the framework has not yet derived from self-reference (Open
Problem~\ref{op:limit-realisability}).
""",
     fill(r"""
derived from the completion every physicist grants, which carries no quantum content, and from
one premise about transformations that the framework derives in outline and has not yet proved
(Open Problem~\ref{op:limit-realisability}).
""")),
    (WIQS,
     r"""
reduces, by a theorem, to a single premise about values --- that self-referential ignorance is
not rationed --- stated as Open Problem~\ref{op:limit-realisability}.
""",
     fill(r"""
reduces, by a theorem, to the completion, which is the real line of every probability theory,
and to a single premise about transformations --- that every transformation the inside performs
has a stationary outside presentation --- stated as Open Problem~\ref{op:limit-realisability}.
""")),
    (POST,
     r"""
one open premise, that the pure states form a connected continuum, Open
Problem~\ref{op:limit-realisability}, with everything downstream of it proved
""",
     fill(r"""
one open premise, that every transformation of the regime is a phase of an inside structure,
Open Problem~\ref{op:limit-realisability}, with everything downstream of it proved
""")),
    (SELF,
     r"""
the two premises of
continuity (Open Problem~\ref{op:limit-realisability}, in \S\ref{sec:continuity});
""",
     fill(r"""
the remaining premise of continuity (Open Problem~\ref{op:limit-realisability}, in
\S\ref{sec:continuity});
""")),
    (SUMM,
     r"""
the value continuum behind continuity (Open Problem~\ref{op:limit-realisability}),
""",
     fill(r"""
the transformation premise behind continuity (Open Problem~\ref{op:limit-realisability}),
""")),
    (MAIN,
     r"""
which \ref{sec:continuity} reduces to a single open premise
about values, and once that is settled it leads to the L2 metric
""",
     fill(r"""
which \ref{sec:continuity} reduces to a single open premise about transformations, and once
that is settled it leads to the L2 metric
""")),
]


def main():
    texts = {}
    for f in FILES:
        with open(f, encoding="utf-8") as fh:
            texts[f] = fh.read()
        if SCRIPT in texts[f]:
            sys.exit("REFUSING: %s already carries the EDITED header for this script" % f)

    t = texts[CONT]
    t = replace_once(t, OLD_INTRO, NEW_INTRO)
    t = replace_once(t, OLD_FOILS_END, NEW_FOILS_END)
    t = replace_once(t, OLD_PREMISES, NEW_PREMISES)
    # the open problem: anchor on its first and last lines, replace everything between
    pb = re.compile(ws(OLD_OP_BEGIN.strip()))
    pe = re.compile(ws(OLD_OP_END.strip()))
    if len(pb.findall(t)) != 1 or len(pe.findall(t)) != 1:
        sys.exit("REFUSING: open-problem anchors did not match exactly once")
    mb, me = pb.search(t), pe.search(t)
    if me.start() < mb.end():
        sys.exit("REFUSING: open-problem anchors out of order")
    t = t[:mb.start()] + NEW_OP + t[me.end():]
    t = replace_once(t, OLD_ACCOUNT, NEW_ACCOUNT)
    texts[CONT] = t

    for f, old, new in XREFS:
        texts[f] = replace_once(texts[f], old, new)

    for f in FILES:
        shutil.copy(f, f + "." + STAMP + ".bak")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(HEADER + texts[f])
        print("patched", f, " backup:", f + "." + STAMP + ".bak")

    print("continuity section: 5 edits; cross-references: %d edits in %d files" % (len(XREFS), len(FILES) - 1))
    print("new citation keys (batch bib/continuity_tower_refs_2026-10-29T1500.bib, import owed):"
          " pagewootters1983evolution, coeckeduncan2011interacting")
    print("PATCH: PASS")


if __name__ == "__main__":
    main()
