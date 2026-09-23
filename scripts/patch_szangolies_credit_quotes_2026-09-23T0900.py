#!/usr/bin/env python3
"""patch_szangolies_credit_quotes_2026-09-23T0900.py

Paper 1: two further quotations from Szangolies, "The Standard Model Symmetry
and Qubit Entanglement" (arXiv:2512.17328, key szangolies2025standardmodel),
with the credit JS asked for on 2026-09-23: "he has to be given due credit for
being the first to suggest that approach." Both passages were verified verbatim
against the arXiv v1 PDF (pdftotext, 2026-09-23); the locators are section
numbers, which survive versions, not page numbers.

1. paper1/sedenions_generations_section_2026-08-27.tex, after "The connection is
   established enough to belong in the main text rather than a sequel.": his
   Sec. IV.E "Further Development" passage on the sedenions, four qubits and
   the S_3 generations (his [67]-[70] are pinillaluthra2009hopf,
   gresnigtgourlayvarma2023three, gourlaygresnigt2024algebraic,
   tangtang2023unified, all in the bibliography), and a paragraph saying what
   this section takes from it and where it departs.
2. paper1/interactions_circuits_section_2026-06-08.tex, after "Putting these
   together turns a Feynman diagram into a quantum circuit on the internal
   qubit registers.": his Sec. VI "Quantum Simulation of Gauge Fields" proposal,
   credited as the first suggestion of running the correspondence on quantum
   hardware.

Sentinel-gated: each anchor matches exactly once (whitespace-insensitive), a
.bak is written per file, "% EDITED" header added, refuses to run twice;
`--check` verifies without writing.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-23"
SCRIPT = Path(__file__).name
STAMP = "2026-09-23T0900"
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


SED = ROOT / "paper1/sedenions_generations_section_2026-08-27.tex"
A1 = r"same algebra. The connection is established enough to belong in the main text rather than a sequel."
R1 = A1 + r"""

The step itself was first pointed at by Szangolies, whose entanglement--spacetime correspondence
this paper takes as its starting point (\S\ref{sec:hopf-justification}). Closing his octonionic
construction, he wrote:
\begin{quotation}
Moving to four qubits, it is then tempting to appeal to the next algebra in the Cayley--Dickson
sequence, the sedenions $\mathbb{S}$. Of course, because of the existence of zero divisors, the Hopf
map cannot be defined in a straightforward way. Hence, a fully analogous continuation of the
sequence above does not seem feasible---which indeed may be an indication of the apparent relevance
of this case in nature.

Nevertheless, it has been proposed that the sedenions could be utilized to quantify four-qubit
entanglement in a similar way, with a single four-qubit state being a point on $S^{31}$
\autocite{pinillaluthra2009hopf}. Furthermore, the discrete $S_{3}$ automorphism of $\mathbb{S}$ has
been argued to yield a natural realization of the triple-generational structure of the Standard
Model \autocite{gresnigtgourlayvarma2023three,gourlaygresnigt2024algebraic,tangtang2023unified},
providing essentially three copies of the octonion algebra.

Hence, while, as expected, no essentially new phenomenology (e.g.\ fifth forces) becomes apparent
through enlarging the model, it seems nevertheless possible to capture further relevant structure
of the Standard Model, such as most notably the generational structure.
\hfill \autocite[\S IV.E]{szangolies2025standardmodel}
\end{quotation}
Three things in that passage are taken up here, and one is departed from. The zero divisors that
stop the Hopf sequence are, in this section, the reason the tower ends where it does, and the
``apparent relevance of this case in nature'' is given its content as the boundary of the fourth
rung. The $S_{3}$ of the doubling is the family label, as he says. The expectation of no new
phenomenology becomes, through the derivation count of the notebook record
(Appendix~\ref{app:nb-T}), a statement at citation grade: no further connected symmetry at any
rung. The departure is in what the $S_{3}$ permutes. ``Three copies of the octonion algebra''
through the shared core are, by direct computation, permuted inside $G_{2}$ and are colour; the
triple the doubling's $S_{3}$ does permute is the three halvings of the sedenions, and that is the
triple this section reads as the generations. The priority for the step, and for the reading of
the finite factor as the generational structure, is his and the line of work he cites."""

INTER = ROOT / "paper1/interactions_circuits_section_2026-06-08.tex"
A2 = r"Putting these together turns a Feynman diagram into a quantum circuit on the internal qubit registers."
R2 = A2 + r"""

That this correspondence should be run on quantum hardware was proposed by Szangolies, in the
paper that supplies the correspondence itself:
\begin{quotation}
Given that the above model starts out from the correspondence between the symmetries of few-qubit
systems and relativistic spacetimes, and from there, recovers the standard model gauge symmetries
via a `dimensional reduction' that corresponds to fixing a given tensor-product structure, it seems
natural to utilize it as a means of simulating these systems on present-day quantum computing
hardware. Here, we will only give a brief outline the application of this correspondence to the
narrow task of simulating gauge fields.
\hfill \autocite[\S VI]{szangolies2025standardmodel}
\end{quotation}
His outline builds the field strength from a two-qubit spinor after von Weizs\"acker; the circuits
of this section are built instead on the three-qubit fermion registers and the dictionary's gates,
and they simulate vertices rather than fields. The suggestion that the correspondence is
executable, and that present-day hardware is the place to execute it, is his, and the notebooks of
Appendix~\ref{app:notebook-record} are its continuation by a different construction. What such
circuits can and cannot yet carry is stated at \S\ref{sec:absent-gate}."""

EDITS = [(SED, [(A1, R1, "sedenions: quotation and credit")], ["\\S IV.E]{szangolies2025standardmodel}", "The priority for the step"]),
         (INTER, [(A2, R2, "interactions: quotation and credit")], ["\\S VI]{szangolies2025standardmodel}", "is his, and the notebooks"])]


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
        print("verified: %s" % path.relative_to(ROOT))
    if CHECK:
        print("--check: nothing written"); return
    for path, new in staged:
        bak = path.with_name(path.name + "." + STAMP + ".bak")
        shutil.copyfile(path, bak)
        path.write_text(HEADER + new)
        print("patched: %s (backup %s)" % (path.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
