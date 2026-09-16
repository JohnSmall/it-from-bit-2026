#!/usr/bin/env python3
"""Two typos in the Thomson's Lamp passage.

`what_is_a_quantum_state.tex` describes the lamp being toggled:

    after the first minute we toggle if off, then half a minute
    later we toggle in on, ...

"if" and "in" are both "it". The third toggle in the same sentence already
reads "we toggle it off", which is the pattern the other two were meant to
follow.

Each anchor carries enough surrounding words to be unique, and each must match
exactly once. A .bak is written, an "% EDITED" header prepended, and the header
makes the script refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-16"
SCRIPT = "scripts/patch_thomson_lamp_typos_2026-09-16T1600.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/what_is_a_quantum_state.tex"

EDITS = [
    ("after the first minute we toggle if off",
     "after the first minute we toggle it off"),
    ("later we toggle in on",
     "later we toggle it on"),
]


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))

    before = len(text.split())
    for old, new in EDITS:
        pat = re.compile(ws(old))
        n = len(pat.findall(text))
        if n != 1:
            sys.exit("REFUSING: anchor matched %d times, expected 1:\n  %s" % (n, old))
        text = pat.sub(lambda _m, r=new: r, text, count=1)

    if len(text.split()) != before:
        sys.exit("REFUSING: the word count changed; this patch only swaps two words")
    for _, new in EDITS:
        if text.count(new) != 1:
            sys.exit("REFUSING: %r landed %d times" % (new, text.count(new)))

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("fixed %d typos in %s" % (len(EDITS), DEST))


if __name__ == "__main__":
    main()
