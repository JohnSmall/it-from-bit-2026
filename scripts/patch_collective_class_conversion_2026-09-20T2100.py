#!/usr/bin/env python3
"""patch_collective_class_conversion_2026-09-20T2100.py

Paper 1: re-scope "baryon and lepton number conservation is class conservation"
to its single-register (perturbative) meaning and add the collective exception.
JS, 2026-09-20: "This needs to be noted in paper 1 and that the relationship
between conversions between classes becomes possible with several copies might
be related to the sphaleron anomaly."

Two files, three edits:
  1. paper1/interactions_circuits_section_2026-06-08.tex, sec:absent-gate: the
     sentence gains "at every order in perturbation theory" and "on a single
     register"; after the "One precision" paragraph a new paragraph states the
     't Hooft vertex, the multi-copy SLOCC conversions with the explicit
     two-copy constructions (GHZ x GHZ -> W at 3/32, W x W -> GHZ at 2/9, three
     colour copies to one W at 3/64), B-L as the copy-additive count, the
     candidate reading of the vertex's fermion content, and Open Problem
     op:sphaleron with PASS/FAIL.
  2. paper1/predictions_section_2026-06-13.tex: "gets for free" becomes "gets for
     free at every order in perturbation theory", with the non-perturbative
     exception named and pointed at sec:absent-gate.

Argument and computation: knowledge/project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md,
scripts/multicopy_slocc_conversion_2026-09-20T2100.py. New citation keys
thooft1976symmetry, kuzminrubakovshaposhnikov1985anomalous,
chitambarduanshi2008tripartite are in bib/sphaleron_slocc_refs_2026-09-20T2100.bib
(VERIFY-CITE; undefined until imported and re-exported). Sentinel-gated;
`--check` verifies anchors without writing.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-20"
SCRIPT = Path(__file__).name
STAMP = "2026-09-20T2100"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


def replace_once(text, anchor, repl, label):
    hits = list(re.finditer(ws(anchor), text))
    if len(hits) != 1:
        sys.exit("%s: anchor matched %d times" % (label, len(hits)))
    m = hits[0]
    return text[: m.start()] + repl + text[m.end():]


INTER = ROOT / "paper1/interactions_circuits_section_2026-06-08.tex"
A1 = (r"Baryon and lepton number conservation \emph{is} class conservation: ignoring the SLOCC "
      r"restriction is physics-speak for positing a leptoquark, the $X$ and $Y$ bosons of $SU(5)$ are "
      r"exactly the missing GHZ--W gates, and the framework's structural exclusion of the $SU(5)$ embedding "
      r"is its standing claim of proton stability (\S\ref{sec:predictions}).")
R1 = (r"Baryon and lepton number conservation, at every order in perturbation theory, \emph{is} class"
      "\n" r"conservation: ignoring the SLOCC restriction on a single register is physics-speak for positing a"
      "\n" r"leptoquark, the $X$ and $Y$ bosons of $SU(5)$ are exactly the missing GHZ--W gates, and the"
      "\n" r"framework's structural exclusion of the $SU(5)$ embedding is its standing claim of proton"
      "\n" r"stability (\S\ref{sec:predictions}). The non-perturbative exception is collective, and is taken"
      "\n" r"up below.")
A2 = (r"class-closed. The gap between what mathematics allows and what the dictionary stocks is exactly "
      r"where a conservation law lives.")
R2 = A2 + r"""

The single-register scope of that statement matters, because the Standard Model itself violates
$B+L$ non-perturbatively. A unit change in the winding of the $SU(2)_{L}$ gauge field removes one
fermion from every left-handed doublet, twelve at once: a colour-singlet triple of quarks and one
lepton in each generation, $\epsilon_{abc}\,q^{a}q^{b}q^{c}\,\ell$ over all three generations, with
$\Delta B = \Delta L = 3$ and $B-L$ conserved \autocite{thooft1976symmetry}. The rate is
$e^{-4\pi/\alpha_{W}} \approx 10^{-161}$ today and unsuppressed above the electroweak crossover
\autocite{kuzminrubakovshaposhnikov1985anomalous}. This process is not a gate, and it does not
contradict class conservation: the SLOCC classes are invariants of one register under local
invertible operations, and the sphaleron is collective, non-local and changes the number of
registers. With several copies the classes are inter-convertible by local stochastic operations,
which is the content of the tensor-rank theory of tripartite entanglement
\autocite{chitambarduanshi2008tripartite}, and the conversions are explicit. Two GHZ registers
convert to one W register: each party sends its two qubits $\lvert01\rangle, \lvert10\rangle,
\lvert11\rangle$ to the corresponding factor of $\lvert001\rangle + \lvert010\rangle +
\lvert100\rangle$ and annihilates $\lvert00\rangle$, with success probability $3/32$. Two W
registers convert to one GHZ register by the partial isometries $A = \lvert1\rangle\langle00\rvert +
\lvert0\rangle\langle11\rvert$, $B = \lvert1\rangle\langle01\rvert + \lvert0\rangle\langle00\rvert$,
$C = \lvert1\rangle\langle10\rvert + \lvert0\rangle\langle00\rvert$, with success probability
$2/9$. Three GHZ registers, one from each colour copy, convert to one W register with probability
$3/64$. Each is verified exactly and realised as a postselected circuit
(\texttt{scripts/multicopy\_slocc\_conversion\_2026-09-20T2100.py} and its Qiskit companion). One
copy suffices in neither direction, by tensor rank one way and by the three-tangle the other. What a
collective conversion conserves is the count additive over registers, one third per GHZ register
minus one per W register, which is $B-L$, the three supplied by colour. We record as a candidate
reading, not a derivation, that the fermion content of the 't~Hooft vertex is what this
framework's symmetries select for a collective class change: one register from each of the three
colour copies of the core split, the same in every generation by the $S_{3}$ of
\S\ref{sec:generations}, on the left-handed doublet sector alone; and that the non-perturbative
conversion is a change in the ladder number of the whole register (Lemma~\ref{lem:winding-number})
rather than a gate on one. The multi-copy inter-convertibility of the classes is then the
kinematic room the anomaly occupies, the winding change being what selects, out of every
collective conversion the mathematics permits, the one nature performs.

\begin{openproblem}[The sphaleron as a global ladder step]\label{op:sphaleron}
Exhibit the twelve-register operation in the dictionary as a change of the whole register's ladder
number by one, with one class change per doublet register; show that it is the unique $G_{2}$- and
$S_{3}$-invariant such operation, hence $\epsilon(qqq)\ell$ in each generation; show that it acts on
the left-handed doublet sector only; and show that the copy-additive count it conserves is $B-L$
with the charge assignments of \S\ref{sec:charges}. PASS: all four. FAIL: a dictionary in
which no global ladder change exists, which would forbid the sphaleron and contradict the Standard
Model, to be owned as a prediction; or one in which a single-register conversion exists, which would
predict proton decay. The rate, $8\pi^{2}/g^{2}$, is not part of the problem.
\end{openproblem}"""

PRED = ROOT / "paper1/predictions_section_2026-06-13.tex"
A3 = (r"This is consistent with the continued non-observation of proton decay, which the framework gets "
      r"for free rather than by tuning, and it is a standing null:")
R3 = (r"This is consistent with the continued non-observation of proton"
      "\n" r"decay, which the framework gets for free at every order in perturbation theory rather than by"
      "\n" r"tuning --- the Standard Model's non-perturbative $B+L$ violation, a collective operation outside"
      "\n" r"the gate set that conserves $B-L$, is not excluded (\S\ref{sec:absent-gate}) --- and it is a"
      "\n" r"standing null:")

EDITS = [
    (INTER, [(A1, R1, "interactions: re-scope"), (A2, R2, "interactions: collective paragraph")],
     ["label{op:sphaleron}", "chitambarduanshi2008tripartite", "at every order in perturbation theory, \\emph{is}"]),
    (PRED, [(A3, R3, "predictions: re-scope")], ["at every order in perturbation theory rather than", "sec:absent-gate"]),
]


def main():
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
        print("--check: nothing written")
        return
    for path, new in staged:
        bak = path.with_name(path.name + "." + STAMP + ".bak")
        shutil.copyfile(path, bak)
        path.write_text(HEADER + new)
        print("patched: %s (backup %s)" % (path.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
