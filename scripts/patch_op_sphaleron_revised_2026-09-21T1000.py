#!/usr/bin/env python3
"""patch_op_sphaleron_revised_2026-09-21T1000.py

Paper 1, absent-gate subsection: revise Open Problem op:sphaleron and the
sentence that motivates it, after JS asked (2026-09-21) whether the problem
needs changing. NOT RUN until JS rules; `--check` verifies the anchors.

Three changes.
1. Correction. The minted text identified the sphaleron with "a change in the
   ladder number of the whole register (Lemma lem:winding-number)". The lemma's
   ladder number is the relative winding of the colour circle's spinor lift and
   equals three times the electric charge, which the sphaleron conserves. The
   sphaleron's winding is the SU(2)_L vacuum's Chern--Simons number, a property
   of the gauge configuration, for which the dictionary has as yet no object.
   The sentence and PASS (i) are restated accordingly, and a FAIL is added for
   the conflation itself.
2. Sharpening. Uniqueness (PASS ii) needs neutrality under the trace direction
   (hypercharge) as well as colour (the G2 stabiliser) and S3; the earlier text
   named only G2 and S3.
3. Sharpening. A FAIL for a dictionary whose lawful gates admit the
   two-register conversion of the text, and PASS (iv) made computable with the
   charge operators on the register (the gauge-respecting circuits promised for
   the subsequent paper). The title changes from "global ladder step" to
   "collective class change".

Sentinel-gated; .bak; "% EDITED" header; refuses to run twice.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-21"
SCRIPT = Path(__file__).name
STAMP = "2026-09-21T1000"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/interactions_circuits_section_2026-06-08.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


def replace_once(text, anchor, repl, label):
    hits = list(re.finditer(ws(anchor), text))
    if len(hits) != 1:
        sys.exit("%s: anchor matched %d times" % (label, len(hits)))
    m = hits[0]
    return text[: m.start()] + repl + text[m.end():]


A1 = (r"and that the non-perturbative conversion is a change in the ladder number of the whole register "
      r"(Lemma~\ref{lem:winding-number}) rather than a gate on one.")
R1 = (r"and that the non-perturbative conversion is driven by a unit change in the weak vacuum's winding,"
      "\n" r"the Chern--Simons number of the $SU(2)_{L}$ configuration, felt by every doublet register at"
      "\n" r"once, rather than by a gate on one. That winding is not the ladder number of"
      "\n" r"Lemma~\ref{lem:winding-number}, which is the colour circle's winding and counts electric charge"
      "\n" r"in thirds; the sphaleron conserves electric charge, and the dictionary has as yet no object"
      "\n" r"carrying the weak vacuum's winding.")

A2 = r"""\begin{openproblem}[The sphaleron as a global ladder step]\label{op:sphaleron}
Exhibit the twelve-register operation in the dictionary as a change of the whole register's ladder
number by one, with one class change per doublet register; show that it is the unique $G_{2}$- and
$S_{3}$-invariant such operation, hence $\epsilon(qqq)\ell$ in each generation; show that it acts on
the left-handed doublet sector only; and show that the copy-additive count it conserves is $B-L$
with the charge assignments of \S\ref{sec:charges}. PASS: all four. FAIL: a dictionary in
which no global ladder change exists, which would forbid the sphaleron and contradict the Standard
Model, to be owned as a prediction; or one in which a single-register conversion exists, which would
predict proton decay. The rate, $8\pi^{2}/g^{2}$, is not part of the problem.
\end{openproblem}"""
R2 = r"""\begin{openproblem}[The sphaleron as a collective class change]\label{op:sphaleron}
Identify the object in the dictionary that carries the weak vacuum's winding, the Chern--Simons
number of the $SU(2)_{L}$ configuration, distinct from the charge winding of
Lemma~\ref{lem:winding-number}, and exhibit the twelve-register operation as its unit change, with
one class change per doublet register and the charge winding conserved; show that the operation is
the unique one invariant under colour (the $G_{2}$ stabiliser of the core split), neutral under the
trace direction, and symmetric under the $S_{3}$ of generations, hence $\epsilon(qqq)\ell$ in each
generation; show that it acts on the left-handed doublet sector only; and show, by computation with
the charge operators written on the register, that the copy-additive count it conserves is $B-L$
with the charge assignments of \S\ref{sec:charges}, while the two-register conversion of the text
fails colour and hypercharge. PASS: all four. FAIL: a dictionary in which no carrier of the weak
vacuum's winding exists, which would forbid the sphaleron and contradict the Standard Model, to be
owned as a prediction; one in which a single-register conversion exists, which would predict proton
decay; one whose lawful gates admit the two-register conversion; or an identification of the
sphaleron with the charge winding, which the sphaleron conserves. The rate, $8\pi^{2}/g^{2}$, is
not part of the problem.
\end{openproblem}"""


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    new = replace_once(text, A1, R1, "motivating sentence")
    new = replace_once(new, A2, R2, "open problem")
    for s in ["collective class change", "carries the weak vacuum's winding", "neutral under the\ntrace direction"]:
        if s not in new:
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
