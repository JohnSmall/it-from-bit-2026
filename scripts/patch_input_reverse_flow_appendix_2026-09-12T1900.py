#!/usr/bin/env python3
"""Input the reverse-flow appendix into main.tex.

`appendix_reverse_flow_2026-07-23.tex` -- "The dictionary read in reverse:
Standard-Model facts as conjecture generators in multipartite entanglement
theory" -- was filed on 2026-09-12 but nothing pulled it in, so none of its
thirteen subsections reached the document.

It goes last in the appendix block. Its own preamble explains why that is safe:
it defines only `app:reverse-flow` and its own subsection labels, uses no
`\\ref` into the main text at all, and deliberately avoids the openproblem
environment because its content is invitations rather than results, nothing
above a fenced RHYME. So it has no ordering dependency on the appendices before
it, and placing it last keeps the graded material together and the speculative
material at the end.

The Jaynes appendix is currently last; this anchors on it.

Anchor matched whitespace-insensitively, exactly once. A .bak is written, an
"% EDITED" header prepended, and the header makes the script refuse to run
twice.

BUILD DEPENDENCY: the appendix cites 24 keys, 22 of which are absent from
references.bib and are supplied by bib/reverse_flow_refs_2026-07-23.bib. Import
that batch and re-export before building, or biber reports 22 undefined
citations from this file alone.
"""

import re
import shutil
import sys

DATE = "2026-09-12"
SCRIPT = "scripts/patch_input_reverse_flow_appendix_2026-09-12T1900.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/main.tex"

ANCHOR = r"\input{appendices/appendix_jaynes_fibration_2026-07-19}"
ADDED = r"\input{appendices/appendix_reverse_flow_2026-07-23}"


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))
    if "appendix_reverse_flow" in text:
        sys.exit("REFUSING: the appendix is already input")

    pat = re.compile(r"\s+".join(re.escape(p) for p in ANCHOR.split()))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % n)
    m = pat.search(text)

    # match the anchor's own indentation
    line_start = text.rfind("\n", 0, m.start()) + 1
    indent = text[line_start:m.start()]

    n_inputs = text.count(r"\input{")
    text = text[:m.end()] + "\n" + indent + ADDED + text[m.end():]
    if text.count(r"\input{") != n_inputs + 1:
        sys.exit("REFUSING: input count did not rise by exactly one")

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("input the reverse-flow appendix into %s" % DEST)


if __name__ == "__main__":
    main()
