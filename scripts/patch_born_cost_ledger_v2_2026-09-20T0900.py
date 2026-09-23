#!/usr/bin/env python3
"""patch_born_cost_ledger_v2_2026-09-20T0900.py

Paper 1 v2, plan item 2a (notes/paper1_v2_complex_cost_revision_plan_2026-09-18T1000.md):
the Born rule from the cost ledger, and the back-references from the two
existing Born-rule routes. Drafted by the Fable session 2026-09-20 at JS's
instruction ("integrate this derivation into the additions we're going to do
for complex temperature pre-FANOUT, and refer back to it in the section where
we derive the Born rule via the Hopf route. Both routes work for a single
qubit unlike Gleason's Theorem"). Argument and status in
knowledge/project-docs/two_columns_shannon_thermodynamics_action_2026-09-18T1200.md
section 2a.

Three files:
  1. paper1/what_is_a_quantum_state.tex: a new subsection
     "The cost of a record, and why it is a square" (label sec:born-cost-ledger)
     inserted before "Scale and dimension of limits to information", i.e. at
     the end of the complex-amplitudes discussion and before either later
     Born-rule section, so that both can refer back.
  2. paper1/self_reference_section_2026-07-04.tex (sec:born-rule): "polynomial"
     and the analyticity clause; a back-reference and the single-qubit remark.
  3. paper1/derivation_of_the_quantum_postulates.tex (sec:born-invariance):
     the same wording fix; "two independent routes" becomes three.

Intended for the v2 branch; runs on whatever branch is checked out. Sentinel-
gated: every anchor must match exactly once (whitespace-insensitive), a .bak
is written per file, an "% EDITED" header is added, and a file already
carrying this script's header is refused. `--check` verifies the anchors and
prints the insertions without writing anything.

Forward references introduced: sec:l2-metric-fibre, sec:wf-redundancy,
app:fanout-boundary, sec:born-rule, sec:born-invariance (all exist in v1);
the new label sec:born-cost-ledger is referenced from files 2 and 3, so all
three edits must land together. Cites Landauer_1961 (in the bibliography).
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-20"
SCRIPT = Path(__file__).name
STAMP = "2026-09-20T0900"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv

ROOT = Path(__file__).resolve().parents[1]


def ws(s):
    """Whitespace-insensitive regex for an exact anchor."""
    return r"\s+".join(re.escape(tok) for tok in s.split())


def find_once(text, anchor, label):
    pat = re.compile(ws(anchor))
    hits = list(pat.finditer(text))
    if len(hits) != 1:
        sys.exit("%s: anchor matched %d times, expected 1:\n  %s" % (label, len(hits), anchor[:80]))
    return hits[0]


def replace_once(text, anchor, replacement, label):
    m = find_once(text, anchor, label)
    return text[: m.start()] + replacement + text[m.end():]


# ---------------------------------------------------------------- file 1
WHAT_IS = ROOT / "paper1/what_is_a_quantum_state.tex"
ANCHOR_1 = r"\subsection{Scale and dimension of limits to information }"
NEW_SUBSECTION = r"""\subsection{The cost of a record, and why it is a square}
\label{sec:born-cost-ledger}

The log now takes negative and complex arguments, so a surprisal can be assigned to an amplitude
and not only to a probability. On the principal branch it is
\[
-\ln\psi \;=\; -\ln|\psi| \;-\; i\arg\psi ,
\]
additive under composition as Shannon's measure must be --- the additivity that fixed the field
above fixes it for both parts at once --- and defined only modulo $2\pi i$, the ambiguity of the
continued log being the phase the observer cannot fix (\S\ref{sec:l2-metric-fibre}). An anti-event,
a negative weight $-p$, has surprisal $-\ln p - i\pi$: the same real part as its event and an
imaginary part of half a turn. Before \textsc{fanout} nothing is erased, and the imaginary part is
the whole of what the anti-event costs; that is the sense in which \S\ref{sec:fanout-boundary}
says it erases without real cost. The complex cost is developed, and its real part paid, in
\S\ref{sec:wf-redundancy} and Appendix~\ref{app:fanout-boundary}.

The record is different in kind, and the difference is the Born rule. A record is a copy
(\S\ref{sec:fanout-boundary}), and a copy is a correlation between the system and its fragment:
its weight carries one factor for each party, the fragment's factor being the amplitude read
back, the return leg, the conjugate. Erasing a record costs heat \autocite{Landauer_1961}, so a
record's surprisal is real, and it adds over independent records; a real, additive, phase-blind
function of an amplitude is $-\alpha\ln|\psi|$ for some exponent $\alpha$, and the loop fixes the
exponent as the number of its legs. The weight of the closed loop, out along the history and back
along its return, is $\psi\psi^{*}$, and with the normalisation of \S\ref{sec:l2-metric-fibre} it
is a probability:
\[
p \;=\; |\psi|^{2}.
\]
The two legs contribute equal and opposite imaginary parts, so the loop carries no phase. That is
why a probability is blind to the fibre, and why thermodynamics, which deals in probabilities,
never sees the imaginary part of the cost: a record is a loop of zero net period, and on the
complex temperature of Appendix~\ref{app:fanout-boundary} the loop's temperature is real. A loop
that fails to close, one history paired with the return leg of another, is an off-diagonal
element of the density matrix; it keeps a phase, and it is what redundancy removes
(\S\ref{sec:wf-redundancy}).

This is the same quadratic that \S\ref{sec:born-rule} derives from fibre privacy and
\S\ref{sec:born-invariance} from $U(1)$-invariance on the Hopf fibre, reached from the cost side.
The routes share the premise that records are fibre-blind; the cost route adds the multiplicative
form and reads the exponent as a count of legs, and it closes a gap the other two leave open,
since $|\psi|$ is also fibre-blind and of degree one and is excluded there only by the
analyticity declared above. None of the three needs the lattice of projections on which
Gleason's theorem rests, so all three hold for a single qubit, where Gleason is silent. The
argument is structural rather than a theorem in the strict sense, and is flagged as such.

"""

# ---------------------------------------------------------------- file 2
SELF_REF = ROOT / "paper1/self_reference_section_2026-07-04.tex"
ANCHOR_2A = r"The lowest-degree invariant of a complex amplitude is the quadratic $|\psi|^{2}$, and normalisation fixes the coefficient:"
REPL_2A = r"""The lowest-degree polynomial invariant
of a complex amplitude is the quadratic $|\psi|^{2}$ --- the non-polynomial invariant $|\psi|$,
of degree one, is excluded by the analyticity declared at \S\ref{sec:complex-amplitudes} --- and
normalisation fixes the coefficient:"""
ANCHOR_2B = r"the Born rule as the cheapest invariant the fibre permits. The derivation is the framework's own;"
REPL_2B = r"""the Born rule as the cheapest invariant the fibre permits. The same square is reached from the
cost side in \S\ref{sec:born-cost-ledger}, where a record is the closed loop of a history and its
return leg and the exponent is the number of legs; neither route uses the lattice of projections
that Gleason's theorem needs, and both hold for a single qubit. The derivation is the framework's
own;"""

# ---------------------------------------------------------------- file 3
POSTULATES = ROOT / "paper1/derivation_of_the_quantum_postulates.tex"
ANCHOR_3A = r"There is no $U(1)$-invariant of degree one; the lowest-degree invariant is quadratic, so the probability must be $p=\lvert\psi\rvert^{2}$."
REPL_3A = r"""There is no polynomial $U(1)$-invariant of degree one,
and the non-polynomial $\lvert\psi\rvert$ is excluded by the analyticity declared at
\S\ref{sec:complex-amplitudes}; the lowest-degree polynomial invariant is quadratic, so the
probability must be $p=\lvert\psi\rvert^{2}$."""
ANCHOR_3B = r"is given at \S\ref{sec:born-rule}: two independent routes to one rule, the over-determination this framework treats as evidence."
REPL_3B = r"""is
given at \S\ref{sec:born-rule}, and the cost-ledger derivation --- the record as the closed loop of
a history and its return leg, the exponent the number of legs --- at \S\ref{sec:born-cost-ledger}:
three routes to one rule, each holding for a single qubit, the over-determination this framework
treats as evidence."""

EDITS = [
    (WHAT_IS, [(ANCHOR_1, NEW_SUBSECTION + ANCHOR_1, "what_is: insert sec:born-cost-ledger")],
     ["label{sec:born-cost-ledger}", "loop of zero net period"]),
    (SELF_REF, [(ANCHOR_2A, REPL_2A, "self_ref: polynomial"), (ANCHOR_2B, REPL_2B, "self_ref: back-reference")],
     ["sec:born-cost-ledger", "non-polynomial invariant"]),
    (POSTULATES, [(ANCHOR_3A, REPL_3A, "postulates: polynomial"), (ANCHOR_3B, REPL_3B, "postulates: three routes")],
     ["three routes to one rule", "sec:born-cost-ledger"]),
]


def main():
    # verify everything before writing anything
    staged = []
    for path, edits, must in EDITS:
        text = path.read_text()
        if HEADER in text:
            sys.exit("%s already carries %s; refusing to run twice" % (path.name, SCRIPT))
        new = text
        for anchor, repl, label in edits:
            new = replace_once(new, anchor, repl, label)
        for s in must:
            if s not in new:
                sys.exit("%s: post-check failed, missing %r" % (path.name, s))
        staged.append((path, new))
        print("verified: %s (%d edit%s)" % (path.relative_to(ROOT), len(edits), "" if len(edits) == 1 else "s"))
    if CHECK:
        print("--check: nothing written. Insertion for %s:\n" % WHAT_IS.name)
        print(NEW_SUBSECTION)
        return
    for path, new in staged:
        bak = path.with_name(path.name + "." + STAMP + ".bak")
        shutil.copyfile(path, bak)
        path.write_text(HEADER + new)
        print("patched: %s (backup %s)" % (path.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
