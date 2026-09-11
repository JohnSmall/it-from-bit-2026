#!/usr/bin/env python3
"""Splice the Jaynes main-body insert into what_is_a_quantum_state.tex.

orphans/jaynes_paragraph_2026-07-19.tex answers an objection the paper
currently neither raises nor answers: the formalism already quotients out the
global phase, so has it not already deleted the subjective ingredient the
framework locates there? Its two paragraphs share no sentence with the
appendix (0 of 15) and its central moves -- the density matrix as the
invariant ring, the bundle with no section, the geometric phase surviving the
quotient, the HJW ensemble ambiguity -- appear nowhere in the main text.

PLACEMENT, per John. Immediately after the paragraph that ends
"self-reference <=> contextuality <=> negative probability", which is where
the body first asserts that the bundle admits no global section and defers to
Appendix~\\ref{app:jaynes}. That is the passage the objection bites on, and
the Jaynes omelette passage it refers back to is forty lines above in this
same file.

The cost, accepted deliberately: \\S\\ref{sec:hopf-bloch} (5.3) and
\\S\\ref{sec:born-invariance} (7) become forward references, since this file
is section 2. The alternative -- placing it after
derivation_of_the_quantum_postulates so both resolve backwards -- would put
the answer two sections after the objection.

Both paragraphs are carried over; the insert's header notes they may be merged
if the surrounding prose prefers, and they are left separate.

Anchors matched whitespace-insensitively, each exactly once. A .bak is
written, an "% EDITED" header prepended, and this script's own header makes it
refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-11"
SCRIPT = "scripts/patch_splice_jaynes_insert_2026-09-11T1130.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

DEST = "paper1/what_is_a_quantum_state.tex"
SRC = "orphans/jaynes_paragraph_2026-07-19.tex"

ANCHOR = r"So we get self-reference $\iff$ contextuality $\iff$ negative probability."
FOLLOWS = "But Spekkens' result uses quantum theory"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    dest = open(DEST, encoding="utf-8").read()
    src = open(SRC, encoding="utf-8").read()

    if HEADER.strip() in dest:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))

    body = re.sub(r"(?m)^\s*%.*$", "", src).strip()
    if not body:
        sys.exit("REFUSING: insert body is empty after stripping comments")
    for needed in (r"\S\ref{sec:hopf-bloch}", r"\S\ref{sec:fanout-boundary}",
                   r"\autocite{Jaynes_89_a}"):
        if needed not in body:
            sys.exit("REFUSING: insert lacks %r -- placeholders not resolved" % needed)
    if re.search(r"\\ref\{sec:(hopf|fanout)\}", body):
        sys.exit("REFUSING: unresolved placeholder label survives in the insert")

    pat = re.compile(ws(ANCHOR))
    n = len(pat.findall(dest))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % n)
    m = pat.search(dest)
    if FOLLOWS not in dest[m.end():m.end() + 400]:
        sys.exit("REFUSING: the expected following paragraph is not where it should be")

    new = dest[:m.end()] + "\n\n" + body + "\n" + dest[m.end():]

    if new.count("An objection now presents itself") != 1:
        sys.exit("REFUSING: insert appears %d times after splice"
                 % new.count("An objection now presents itself"))
    if new.count(ANCHOR.split("So we get")[0].strip()[:40]) < 1:
        sys.exit("REFUSING: anchor paragraph damaged")

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + new)
    print("spliced the Jaynes insert into %s" % DEST)
    print("  lines %d -> %d" % (dest.count("\n") + 1, new.count("\n") + 1))
    print("  paragraphs added: %d" % len([p for p in body.split("\n\n") if p.strip()]))


if __name__ == "__main__":
    main()
