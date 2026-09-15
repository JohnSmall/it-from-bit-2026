#!/usr/bin/env python3
"""Continuity from a connected state space: the theorem that removes divisibility, and the
restated open problem.

Companion to knowledge/sessions/continuity_connected_state_space_2026-09-15T1430.md. JS,
2026-09-15: the chain negative probability -> complex amplitudes -> L^2 metric -> Hopf
fibrations passes through reversible continuity (Hardy's fifth axiom), so the paper must say
what "complex probability amplitudes imply reversible continuity" rests on. The finding: with
the pure states a connected space, a closed transitive transformation group already has its
identity component transitive, so Hardy A5 follows with no divisibility premise; the residue
is one premise about values (the amplitudes fill their continuum, i.e. self-referential
ignorance is not rationed), plus closure as an adopted stance and homogeneity as argued.

Four files, one header each, one run only.

paper1/continuity_section_2026-07-04.tex
  1. Opening paragraph: "two sharply posed lemma-premises" becomes "one premise about values".
  2. After the Lagrange paragraph that followed prop:divisible-closed: its closing sentence no
     longer says the question compresses to divisibility and closedness; a new
     Proposition (prop:connected-transitive) with proof is inserted, followed by a paragraph
     on what the proposition relocates and on the two foils (the stabiliser fragment of
     quantum theory; Spekkens's toy theory), both with finitely many pure states.
  3. \\subsection{The two premises, and what they mean} becomes "The premises, and what they
     mean"; its opening, which gave divisibility a candidate derivation, now names the three
     premises of the new proposition, retires divisibility, and keeps the closedness text;
     one sentence at the paragraph's end records closedness as an adopted stance.
  4. op:limit-realisability is restated (label kept: it is cross-referenced from four files):
     title "The value continuum from self-reference"; the three premises; the single open
     one, with the candidate route (a rationing rule is a record); PASS and FAIL clauses with
     the toy theory and the stabiliser fragment as the test; divisibility retired.
paper1/L2_metric_global_phase_section_2026_06_07.tex, paper1/summary_section_2026-07-07.tex,
paper1/derivation_of_the_quantum_postulates.tex
  5. The sentences that describe the open problem as "two premises, divisibility and
     closedness" are re-pointed to the one open premise.

Every anchor is matched whitespace-insensitively and must match exactly once; edited prose
paragraphs are re-filled to 96 columns. A dated .bak is written per file, a "% EDITED" header
is prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-15"
STAMP = "2026-09-15T1430"
SCRIPT = "scripts/patch_continuity_connected_state_space_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

CONT = "paper1/continuity_section_2026-07-04.tex"
L2 = "paper1/L2_metric_global_phase_section_2026_06_07.tex"
SUMM = "paper1/summary_section_2026-07-07.tex"
POST = "paper1/derivation_of_the_quantum_postulates.tex"


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


def refill_paragraph_at(text, marker):
    i = text.index(marker)
    start = text.rfind("\n\n", 0, i) + 2
    end = text.find("\n\n", i)
    para = text[start:end]
    for line in para.splitlines():
        if line.lstrip().startswith(("\\begin", "\\end", "\\item", "%", "\\subsection",
                                     "\\section", "\\label")):
            sys.exit("REFUSING: paragraph to re-fill contains structure:\n  %s" % line)
    return text[:start] + fill(para) + text[end:]


# ------------------------------------------------------------------ continuity section
OLD_INTRO = r"""
derivation is not a postulate but two sharply posed lemma-premises, stated as an open problem at the
end of the section with nothing hidden in them.
"""
NEW_INTRO = r"""
derivation is not a postulate about transformations but one premise about values, stated as an open
problem at the end of the section with nothing hidden in it.
""".strip()

OLD_LAGRANGE_END = r"""
Every route to a discrete transformation group
therefore passes through a failure of divisibility or a failure of closedness: the whole question
compresses to those two premises, and to nothing else.
"""
NEW_LAGRANGE_END = ("Every route to a discrete transformation group therefore passes through a failure of "
                    "divisibility or a failure of closedness. Divisibility, however, asks for more than the "
                    "conclusion needs, and the next proposition removes it.")

PROP = "\n".join([
    r"\begin{proposition}[Continuity from a connected state space]\label{prop:connected-transitive}",
    fill(r"""
Let the pure states of a finite-dimensional system form a connected space $P$, and let the group
$G$ of reversible transformations of the pre-measurement regime be topologically closed and act
transitively on $P$. Then the identity component $G_0$ already acts transitively on $P$, and a
continuous reversible transformation connects any two pure states: Hardy's fifth axiom holds, with
no divisibility assumed.
"""),
    r"\end{proposition}",
    "",
    r"\begin{proof}",
    fill(r"""
As in Proposition~\ref{prop:divisible-closed}, closedness makes $G$ a compact Lie group with
finitely many connected components \autocite{broeckertomdieck1985compact}, so $G_0$ is a closed
normal subgroup of finite index and is path-connected. Each $G_0$-orbit in $P$ is the continuous
image of a compact group, hence compact, hence closed. Since $G$ is transitive and $G_0$ is normal,
the $G_0$-orbit of $gx$ is $g$ applied to the $G_0$-orbit of $x$, so the cosets of $G_0$ permute the
orbits transitively and there are finitely many of them. A finite partition of $P$ into closed sets
is a partition into open sets; $P$ is connected; so there is one orbit and $G_0$ is transitive. Given
pure states $x$ and $y$, choose $g \in G_0$ with $gx = y$ and a continuous path $g_t$ in $G_0$ from
the identity to $g$; then $g_t x$ is a continuous reversible transformation from $x$ to $y$.
"""),
    r"\end{proof}",
])

P_FOILS = fill(r"""
The proposition relocates the premise. Divisibility was asked for because a transformation group
could be infinite and discrete; but a group acting transitively on a continuum cannot be countable,
and a closed group acting transitively on a connected space cannot be disconnected in the way that
matters, so what the argument needs from the regime is not the availability of $n$-th roots but the
connectedness of the state space itself. That is a statement about values: that the pure states are
all the unit vectors of $\mathbb{C}^{K}$ up to phase, the space $\mathbb{CP}^{K-1}$, connected for
$K \ge 2$, and hence that the amplitudes of \S\ref{sec:self-reference} fill their continuum. The
two standing foils show the premise doing its work. The stabiliser fragment of quantum theory has
complex amplitudes and is contextual, yet it has finitely many pure states, its outcome
probabilities take only the values $0$, $\tfrac12$ and $1$, and its reversible transformations form
a finite group, the Clifford group, so Hardy's fifth axiom fails in it; Spekkens's toy theory
\autocite{spekkens2007toy} is the same with real amplitudes, its ignorance rationed by a
knowledge-balance principle. Neither has a connected state space, and neither is a model of the
regime described here, whose credences take every value. Divisibility, which both also lack --- the
phase gate has no square root in the Clifford group --- is a symptom of the discreteness, not its
cause.
""")

OLD_PREMISES_HEAD = r"""
\subsection{The two premises, and what they mean}

Divisibility has a candidate derivation whose status we flag plainly as owed rather than proved:
with no basis selected there is no distinguished step, so a reversible transformation of the regime
should be realisable in $n$ equal describable stages for every $n$ --- an $n$-th root for every $n$.
Closedness is the deeper premise, and it is where the section's title is earned.
"""
NEW_PREMISES_HEAD = (r"\subsection{The premises, and what they mean}" + "\n\n" + r"""
Three premises carry Proposition~\ref{prop:connected-transitive}. Transitivity is the regime's
homogeneity: inside/outside equivalence leaves no pure state privileged, and a proper closed
invariant set of pure states would define a superselection observable, a classical record predating
any \textsc{fanout} (\S\ref{sec:fanout-boundary}). Connectedness of the state space is a premise
about values --- that self-referential ignorance is not rationed --- and it is the one that remains
open; it is stated at the end of the section. Divisibility, which an earlier version of this section
asked for, is not needed: it follows from the conclusion, every element of a compact connected Lie
group having roots of every order, and its candidate derivation from ``no distinguished step'' is
retired with it. Closedness is the deeper premise conceptually, and it is where the section's title
is earned.
""".strip())

OLD_CLOSURE_END = r"""
Continuity is the topological face of
the founding non-computability.
"""
NEW_CLOSURE_END = r"""
Continuity is the topological face of the founding non-computability. We record closedness, all the
same, as the framework's adopted stance rather than as a theorem: the same founding premise admits
a constructive reading on which only describable limits exist --- a computable Cauchy sequence of
rationals can have a non-computable limit, and the two readings part exactly there --- and the
stance taken here is the operational one, that a limit no experiment can certify absent is
admitted, which Hardy's own axioms take for granted.
""".strip()

OLD_OP = r"""
\begin{openproblem}[Limit-realisability from self-reference]\label{op:limit-realisability}
Derive, from the self-referential closure of \S\ref{sec:self-reference}, the two premises of
Proposition~\ref{prop:divisible-closed}: that the reversible-transformation group of the
pre-measurement regime is divisible --- the candidate route being that no selected basis leaves no
distinguished step, so that every transformation is realisable in $n$ equal describable stages for
every $n$ (with ``no selected basis'' now the exact statement that no classical structure has
committed, Proposition~\ref{prop:f1-dictionary}) --- and that it is topologically closed --- the
candidate route being that a Cauchy sequence of available transformations whose convergence the
system can itself describe must have its limit available, on pain of the description referring to a
transformation that does not exist, a failure of exactly the fixed-point closure that
Proposition~\ref{prop:inside-outside} formalises. With
both premises, continuity follows by the proposition and everything downstream is Hardy's theorem,
cited; the finite, countable and disconnected escapes are closed unconditionally above. What is open
is exactly the two derivations named, and nothing wider.
\end{openproblem}
"""
NEW_OP = "\n".join([
    r"\begin{openproblem}[The value continuum from self-reference]\label{op:limit-realisability}",
    fill(r"""
Proposition~\ref{prop:connected-transitive} reduces Hardy's fifth axiom to three premises: that the
pure states of the pre-measurement regime form a connected space, that its reversible
transformations act transitively on them, and that they form a closed group. Transitivity is argued
above from the absence of records; closedness is the framework's adopted stance, the operational
completion. What remains open is the first. Derive, from the self-referential closure of
\S\ref{sec:self-reference}, that self-referential ignorance is not rationed: that the embedded
observer's credence in a proposition about itself can take every value in $[0,1]$, so that the
amplitudes of \S\ref{sec:self-reference} fill $\mathbb{C}^{K}$ and the pure states are all of
$\mathbb{CP}^{K-1}$. The candidate route is that a rationing rule --- a minimal unit of
self-ignorance, as in the knowledge-balance principle of the epistricted theories --- is a stable,
copyable description of the observer's own epistemic state, a record predating any
\textsc{fanout}, of exactly the kind the third face of the regime excludes (with ``no selected
basis'' the exact statement that no classical structure has committed,
Proposition~\ref{prop:f1-dictionary}). A derivation passes if it yields the connected state space
from premises that Spekkens's toy theory \autocite{spekkens2007toy} does not also satisfy; it fails
before any detail is checked if every premise it uses holds in that theory or in the stabiliser
fragment of quantum theory, since both are consistent and both have finitely many pure states.
Divisibility of the transformation group, asked for in an earlier version of this problem, is no
longer required: it is a consequence of the conclusion, not a route to it. With the one premise,
continuity follows by the proposition and everything downstream is Hardy's theorem, cited; the
finite, countable and disconnected escapes are closed unconditionally above.
"""),
    r"\end{openproblem}",
])

# ------------------------------------------------------------------ cross-references
OLD_L2 = r"""
conditionally, on the two premises priced as Open Problem~\ref{op:limit-realisability}. Assuming
those premises can be proved, everything below inherits the derivation; we carry that status,
and do not upgrade it.
"""
NEW_L2 = r"""
conditionally, on the premises priced as Open Problem~\ref{op:limit-realisability}, of which one, the
value continuum, remains open. Assuming that premise can be proved, everything below inherits the
derivation; we carry that status, and do not upgrade it.
""".strip()

OLD_SUMM = r"the two premises of continuity (Open Problem~\ref{op:limit-realisability}), the functor of the"
NEW_SUMM = r"the value continuum behind continuity (Open Problem~\ref{op:limit-realisability}), the functor of the"

OLD_POST = r"""
--- now priced exactly: two premises, divisibility and closedness,
Open Problem~\ref{op:limit-realisability}, with everything downstream of them proved
(\S\ref{sec:continuity}). Until they are closed, continuity enters as a principle, and the weight
"""
NEW_POST = r"""
--- now priced exactly: one open premise, that the pure states form a connected continuum,
Open Problem~\ref{op:limit-realisability}, with everything downstream of it proved
(\S\ref{sec:continuity}). Until it is closed, continuity enters as a principle, and the weight
""".strip()


def patch(path, fn, must_contain):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        print("already patched, skipping: %s" % path)
        return
    text = fn(text)
    for s in must_contain:
        if s not in text:
            sys.exit("REFUSING: %s lacks %r after the edit" % (path, s))
    shutil.copy(path, path + "." + STAMP + ".bak")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak)" % (path, path, STAMP))


def edit_continuity(text):
    text = replace_once(text, OLD_INTRO, NEW_INTRO)
    text = refill_paragraph_at(text, "one premise about values")
    text = replace_once(text, OLD_LAGRANGE_END, NEW_LAGRANGE_END + "\n\n" + PROP + "\n\n" + P_FOILS)
    text = refill_paragraph_at(text, "the next proposition removes it.")
    text = replace_once(text, OLD_PREMISES_HEAD, NEW_PREMISES_HEAD)
    text = replace_once(text, OLD_CLOSURE_END, NEW_CLOSURE_END)
    text = refill_paragraph_at(text, "Three premises carry Proposition")
    text = replace_once(text, OLD_OP, NEW_OP)
    for lab in (r"\label{prop:connected-transitive}", r"\label{op:limit-realisability}",
                r"\label{prop:divisible-closed}"):
        if text.count(lab) != 1:
            sys.exit("REFUSING: %s occurs %d times" % (lab, text.count(lab)))
    return text


def edit_l2(text):
    # Not re-filled: the paragraph follows its \section line without a blank line.
    return replace_once(text, OLD_L2, NEW_L2)


def edit_summ(text):
    return replace_once(text, OLD_SUMM, NEW_SUMM)


def edit_post(text):
    text = replace_once(text, OLD_POST, NEW_POST)
    return refill_paragraph_at(text, "one open premise, that the pure states")


def main():
    patch(CONT, edit_continuity, ["prop:connected-transitive", "spekkens2007toy", "Clifford group"])
    patch(L2, edit_l2, ["value continuum, remains open"])
    patch(SUMM, edit_summ, ["the value continuum behind continuity"])
    patch(POST, edit_post, ["one open premise, that the pure states"])


if __name__ == "__main__":
    main()
