#!/usr/bin/env python3
"""patch_zd_defect_antecedents_2026-09-27T0900.py

paper1/appendices/appendix_zd_structure_2026-09-01.tex: after the proof sketch of
Proposition prop:zd-defect, one paragraph naming the antecedents of the
norm-defect identity, following the ChatGPT prior-work review of 2026-09-25
(knowledge/other_sources/openai/sedenion_prior_work.tex) and the Fable session's
second-order checks of 2026-09-27 (knowledge/sessions/chatgpt_sedenion_prior_work_review_2026-09-27T0900.md).
Morita's Section 5 could not be read (paywalled): that citation is
VERIFY-SUPPORT and the sentence says "in another notation", which is the
review's translation, not ours. NOT RUN until JS rules; `--check` verifies.
"""
import re, shutil, sys
from pathlib import Path

DATE = "2026-09-27"; SCRIPT = Path(__file__).name; STAMP = "2026-09-27T0900"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/appendices/appendix_zd_structure_2026-09-01.tex"

def ws(s): return r"\s+".join(re.escape(t) for t in s.split())

ANCHOR = r"its equality case, the calibration bound of calibrated geometry. \end{proof}"
ADD = r"""

The identity is not new, and the appendix does not present it as such. Morita's cross-term
expansion of a sedenion product norm is the same identity in another notation
\autocite{Morita2014QuasiAssociativity}; Moreno's block form of the squared multiplication
operator, with the associator as its off-diagonal entry, is its operator counterpart
\autocite{Moreno2005Constructing}; the range statement is the spectrum $\{0, 1, 2\}$ that Biss,
Christensen, Dugger and Isaksen obtain for the positive operator $L_{\bar x}L_{x}/\lvert x\rvert^{2}$
on a zero-divisor configuration \autocite{BissEtAl2009Eigentheory}; and the identification of the
associator's dual with the coassociative calibration is Harvey and Lawson's
\autocite{harvey1982calibrated}. What is the framework's is the reading of the defect as the
settlement of the associator-debt, \S\ref{sec:masses}."""

def main():
    text = TARGET.read_text()
    if HEADER in text: sys.exit("refusing to run twice")
    hits = list(re.finditer(ws(ANCHOR), text))
    if len(hits) != 1: sys.exit("anchor matched %d times" % len(hits))
    m = hits[0]
    new = text[:m.end()] + ADD + text[m.end():]
    print("verified: %s" % TARGET.relative_to(ROOT))
    if CHECK: print("--check: nothing written"); return
    shutil.copyfile(TARGET, TARGET.with_name(TARGET.name + "." + STAMP + ".bak"))
    TARGET.write_text(HEADER + new); print("patched")

if __name__ == "__main__": main()
