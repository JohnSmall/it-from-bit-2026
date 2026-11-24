#!/usr/bin/env python3
"""patch_skolem_rice_tie_2026-11-21T0732.py

paper1/what_is_a_quantum_state.tex, skolem-chaitin-rhyme block: reword the
antecedent sentence added on 2026-11-21 so that the similarity Yanofsky
observes is tied to Rice's theorem, as it is in Svozil, Physical (A)Causality,
Appendix A.5, pp. 174--175 ("As Yanofsky observes this bears some similarity
to the downward Loewenheim-Skolem", directly after the reduction of Rice's
theorem to the halting problem).  JS's ruling of 2026-11-21.  A replacement,
not an insertion.  No new key.  `--check` verifies and writes nothing.
"""
import re, shutil, sys
from pathlib import Path

DATE = "2026-11-21"; SCRIPT = Path(__file__).name; STAMP = "2026-11-21T0732"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/what_is_a_quantum_state.tex"

def ws(s): return r"\s+".join(re.escape(t) for t in s.split())

OLD = r"""The likeness has
been remarked before: Yanofsky, as quoted by Svozil in a discussion of how common true yet
unprovable statements are, observes that it bears some similarity to the downward
L\"owenheim--Skolem theorem \autocite[174--175]{svozil_k_2018}; the relation to the inside and the
outside is not drawn there."""
NEW = r"""A likeness of this kind has been remarked before, for Rice's theorem, that every non-trivial
property of what a program computes is undecidable: Yanofsky, as quoted by Svozil where he reduces
that theorem to the halting problem, observes that it bears some similarity to the downward
L\"owenheim--Skolem theorem \autocite[174--175]{svozil_k_2018}; the relation to the inside and the
outside is not drawn there."""

def main():
    text = TARGET.read_text()
    if HEADER in text: sys.exit("refusing to run twice")
    hits = list(re.finditer(ws(OLD), text))
    if len(hits) != 1: sys.exit("anchor matched %d times" % len(hits))
    m = hits[0]
    new = text[:m.start()] + NEW + text[m.end():]
    print("verified: %s" % TARGET.relative_to(ROOT))
    if CHECK: print("--check: nothing written"); return
    shutil.copyfile(TARGET, TARGET.with_name(TARGET.name + "." + STAMP + ".bak"))
    TARGET.write_text(HEADER + new); print("patched")

if __name__ == "__main__": main()
