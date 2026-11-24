#!/usr/bin/env python3
"""patch_skolem_yanofsky_antecedent_2026-11-21T0730.py

paper1/what_is_a_quantum_state.tex, inside the skolem-chaitin-rhyme block of
2026-11-16: one sentence crediting the antecedent.  JS's ruling of 2026-11-21:
cite it as Yanofsky, as quoted by Svozil.  Svozil, Physical (A)Causality,
Appendix A.5, pp. 174--175, read in JS's local PDF; Yanofsky 2013 itself is
not read and is named in the text only, with no key of its own.  No new
bibliography key.  `--check` verifies the anchor and writes nothing.
"""
import re, shutil, sys
from pathlib import Path

DATE = "2026-11-21"; SCRIPT = Path(__file__).name; STAMP = "2026-11-21T0730"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/what_is_a_quantum_state.tex"

def ws(s): return r"\s+".join(re.escape(t) for t in s.split())

ANCHOR = r"Set beside Chaitin's observation the two look alike."
ADD = r""" The likeness has
been remarked before: Yanofsky, as quoted by Svozil in a discussion of how common true yet
unprovable statements are, observes that it bears some similarity to the downward
L\"owenheim--Skolem theorem \autocite[174--175]{svozil_k_2018}; the relation to the inside and the
outside is not drawn there."""

def main():
    text = TARGET.read_text()
    if HEADER in text: sys.exit("refusing to run twice")
    if "% BEGIN skolem-chaitin-rhyme 2026-11-16" not in text: sys.exit("block missing")
    hits = list(re.finditer(ws(ANCHOR), text))
    if len(hits) != 1: sys.exit("anchor matched %d times" % len(hits))
    m = hits[0]
    new = text[:m.end()] + ADD + text[m.end():]
    print("verified: %s" % TARGET.relative_to(ROOT))
    if CHECK: print("--check: nothing written"); return
    shutil.copyfile(TARGET, TARGET.with_name(TARGET.name + "." + STAMP + ".bak"))
    TARGET.write_text(HEADER + new); print("patched")

if __name__ == "__main__": main()
