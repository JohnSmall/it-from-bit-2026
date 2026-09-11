#!/usr/bin/env python3
"""Append the loops/renormalisability prospects to sec:spacetime-open-problems.

orphans/loops_renormalizability_prospects_2026-06-13.tex is a drop-in pair of
\\paragraph blocks for the "Open problems and prospects" subsection of
spacetime_from_non-computability.tex. None of its 44 substantive lines was in
that file, so nothing is being duplicated. Both cross-references
(sec:three-dimensions, sec:entanglement-classes) resolve and its only citation,
adams1960hopf, is already in the bibliography.

PLACEMENT. The orphan's header says "after the existing prospect paragraphs
(e.g. after 'Expansion and acceleration.')". Those are no longer the same
place: a seventh paragraph, "The $S^{7}$ sector as internal structure.", has
been added since the orphan was drafted on 2026-06-13. Per John, the new
prospects go after that one, at the end of the prospects and before the
\\medskip that closes the subsection.

QUOTING. The orphan uses TeX's ``...'' quoting. Both papers now quote with
\\enquote{} from csquotes, so the two instances are converted. The comma after
"select them too" is moved outside the closing quote: the quoted phrase is a
coined slogan, not quoted speech, and the papers are set to British English,
where punctuation not belonging to the quotation sits outside it.

NOT DONE, needs John. The \\medskip summary that closes the subsection
enumerates the prospects by name and now under-counts: it lists CP violation
and baryogenesis, inflation, expansion, and the $S^{7}$ sector, but not these
two. Its own header flagged this ("Adjust the \\medskip summary if needed").
Rewriting that sentence is an editorial judgement about which prospects to
name, so it is left alone.

Anchors are matched whitespace-insensitively and must match exactly once.
A .bak is written, an "% EDITED" header prepended, and this script's own
header makes it refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-11"
SCRIPT = "scripts/patch_splice_loops_prospects_2026-09-11T0900.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

DEST = "paper1/spacetime_from_non-computability.tex"
SRC = "orphans/loops_renormalizability_prospects_2026-06-13.tex"

ANCHOR = ("add real spatial dimensions to carry the same structure.")
NEXT = r"\medskip"

QUOTES = [
    ("``closed paths in spacetime select the parallelisable spheres''",
     r"\enquote{closed paths in spacetime select the parallelisable spheres}"),
    ("``closed paths in interactions select them too,''",
     r"\enquote{closed paths in interactions select them too},"),
]


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    dest = open(DEST, encoding="utf-8").read()
    src = open(SRC, encoding="utf-8").read()

    if HEADER.strip() in dest:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))

    body = src[src.index(r"\paragraph{Loops"):].rstrip()
    body = re.sub(r"\n%\s*=+\s*$", "", body).rstrip()
    if body.lstrip().startswith("%"):
        sys.exit("REFUSING: extracted body starts with a comment")

    # the second quotation spans a line break in the source, so match
    # whitespace-flexibly rather than literally
    for old, new in QUOTES:
        pat_q = re.compile(ws(old))
        n = len(pat_q.findall(body))
        if n != 1:
            sys.exit("REFUSING: quote %r occurs %d times, expected 1" % (old[:34], n))
        body = pat_q.sub(lambda _m, r=new: r, body)
    if "``" in body or "''" in body:
        sys.exit("REFUSING: TeX-style quotes survive in the body")

    pat = re.compile(ws(ANCHOR))
    if len(pat.findall(dest)) != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % len(pat.findall(dest)))
    m = pat.search(dest)
    tail = dest[m.end():]
    if NEXT not in tail[:400]:
        sys.exit("REFUSING: the \\medskip close does not follow the anchor as expected")

    new_dest = dest[:m.end()] + "\n\n" + body + "\n" + dest[m.end():]

    for label in ("Loops, supertasks", "Does parallelisability determine"):
        if new_dest.count(label) != 1:
            sys.exit("REFUSING: %r appears %d times after splice" % (label, new_dest.count(label)))
    if sum(1 for c in new_dest if ord(c) > 127) != sum(1 for c in dest if ord(c) > 127) + \
       sum(1 for c in body if ord(c) > 127):
        sys.exit("REFUSING: unexpected change in non-ASCII content")

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + new_dest)
    print("spliced 2 prospect paragraphs into %s" % DEST)
    print("  lines %d -> %d" % (dest.count("\n") + 1, new_dest.count("\n") + 1))
    print("  quotes converted to \\enquote{}: %d" % len(QUOTES))


if __name__ == "__main__":
    main()
