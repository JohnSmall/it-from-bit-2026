#!/usr/bin/env python3
"""Resolve the VERIFY-KEY placeholder \\autocite{hurwitz1898}.

masses_section_2026-06-08.tex cites Hurwitz's 1898 theorem under the key
hurwitz1898, which has no entry in self-ref-2026.bib.  The library's
existing key for that same paper is hurwitz1898composition (Ueber die
Composition der quadratischen Formen..., cited in five other files).  The
file itself carries the instruction at lines 148-150:

    %%   VERIFY-KEY: replace \\autocite{hurwitz1898} below with the
    %%   library's existing Hurwitz key before compiling.

That VERIFY-KEY comment is deliberately left in place as history.

The bare string "autocite{hurwitz1898}" occurs twice in the file -- once
inside that comment, once as the live citation -- so the anchor is the
surrounding prose of the live one, which is unique.  The comment is not
touched.

Note the file already carries an "% EDITED 2026-07-12" header from an
earlier pass, so the run-twice guard keys on this script's own header
line rather than on any % EDITED line.
"""

import re
import shutil
import sys

DATE = "2026-09-09"
SCRIPT = "scripts/patch_hurwitz_citekey_2026-09-09T1640.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

FILE = "masses_section_2026-06-08.tex"
ANCHOR = (r"tower \autocite{hurwitz1898}, the norm of a product first "
          r"fails to factorise")
OLD = "hurwitz1898"
NEW = "hurwitz1898composition"


def ws_insensitive(anchor):
    return r"\s+".join(re.escape(p) for p in anchor.split())


def main():
    orig = open(FILE, encoding="utf-8").read()

    if HEADER.strip() in orig:
        sys.exit("REFUSING: %s already patched by %s" % (FILE, SCRIPT))

    pat = re.compile(ws_insensitive(ANCHOR))
    hits = pat.findall(orig)
    if len(hits) != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % len(hits))
    print("anchor matched exactly once")

    m = pat.search(orig)
    span = m.group(0)
    if OLD not in span:
        sys.exit("REFUSING: key %s not inside matched span" % OLD)
    # replace the whole braced key, not the substring, so hurwitz1898composition
    # elsewhere could never be mangled into hurwitz1898compositioncomposition
    new_span = span.replace("{" + OLD + "}", "{" + NEW + "}")
    if new_span == span:
        sys.exit("REFUSING: no braced key {%s} in matched span" % OLD)
    text = orig[:m.start()] + new_span + orig[m.end():]

    before = sum(1 for c in orig if ord(c) > 127)
    after = sum(1 for c in text if ord(c) > 127)
    if after != before:
        sys.exit("REFUSING: non-ASCII count changed %d -> %d" % (before, after))

    # the VERIFY-KEY comment must survive untouched
    if orig.count("VERIFY-KEY") != text.count("VERIFY-KEY"):
        sys.exit("REFUSING: VERIFY-KEY comment was altered")

    shutil.copy2(FILE, FILE + ".bak")
    with open(FILE, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("wrote %s (backup %s.bak)" % (FILE, FILE))
    print("replaced {%s} -> {%s} (1 occurrence, live citation only)" % (OLD, NEW))


if __name__ == "__main__":
    main()
