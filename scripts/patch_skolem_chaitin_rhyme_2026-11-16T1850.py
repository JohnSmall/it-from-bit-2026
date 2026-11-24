#!/usr/bin/env python3
"""patch_skolem_chaitin_rhyme_2026-11-16T1850.py

paper1/what_is_a_quantum_state.tex, end of sec:measuring-non-computability:
one paragraph recording the rhyme between Skolem's paradox and Chaitin's
point that an unprovable proposition becomes provable when information is
added to the axioms.  JS's instruction of 2026-11-16: add it, as a rhyme for
mathematicians and logicians to work on, without committing to any reading of
Skolem's work, and say that it becomes relevant in Paper 2.  Session note:
knowledge/sessions/skolem_chaitin_rhyme_2026-11-16T1850.md.  Five new keys in
bib/skolem_rhyme_refs_2026-11-16T1850.bib (undefined until imported).
`--check` verifies the anchor and writes nothing.
"""
import re, shutil, sys
from pathlib import Path

DATE = "2026-11-16"; SCRIPT = Path(__file__).name; STAMP = "2026-11-16T1850"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/what_is_a_quantum_state.tex"

def ws(s): return r"\s+".join(re.escape(t) for t in s.split())

ANCHOR = r"""In \ref{sec:measuring-non-computability} I'll make use of that to
suggest a space of computations."""
ADD = r"""

% BEGIN skolem-chaitin-rhyme 2026-11-16
There is a rhyme here with an older result in logic, and I record it as a rhyme and no more. The
L\"owenheim--Skolem theorem gives any first-order theory in a countable language that has an
infinite model a countable one, so set theory, which proves that uncountable sets exist, has a
model in which every set is countable when counted from outside
\autocite{skolem1922remarks}. Nothing contradictory follows: the model lacks the enumeration that
the outside view supplies, and each is right by its own lights. Set beside Chaitin's observation
the two look alike. A model in which a theory's own consistency statement fails contains an object
that it takes for a proof and that from outside is no finite proof at all, just as Skolem's model
contains a set that it takes to be uncountable; and by G\"odel's completeness theorem a
proposition is unprovable from a set of axioms exactly when some model of those axioms makes it
false, so that adding an axiom and discarding models are one act. In both cases what the inside
lacks is supplied only from an outside that sees more, and that outside is in its turn the inside
of another; on the side of proof this is the progression of theories studied by Turing and by
Feferman \autocite{turing1939systems,feferman1962transfinite}. The two also differ, and in the
respect that matters most to this section. Adding first-order axioms moves the boundary of the
provable, but every consistent extension still has its countable models, so a distance counted in
added information does not carry over from the one case to the other without an argument; and the
reading of Chaitin's theorem as a measure of the information in a set of axioms is itself disputed
\autocite{raatikainen1998interpreting}. What Skolem's result means for the foundations of
mathematics has been argued over for a century \autocite{bays2025skolem}, and nothing in this
paper takes a side in that argument; only the theorem is used, in \S\ref{sec:continuity}, where it
is the reason the completion cannot be derived. I leave the rhyme to logicians and mathematicians
as a question worth their attention. It will matter in the second paper, where the inside and the
outside carry more of the weight and the proposal of \S\ref{sec:comp-distance}, that to measure a
spatial distance is to measure the information that must be added to make two events causally
connected, is developed in full.
% END skolem-chaitin-rhyme 2026-11-16"""

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
