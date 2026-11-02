#!/usr/bin/env python3
"""Bump the title-page version of Paper 1 from 0.5 to 0.6 (2026-10-31T1619).

The maintainer re-dated the paper by hand on 2026-10-31 (\\date{16 September
2026} to \\date{31 October 2026}) and asked for the version to move with it.
0.6 is the next draft increment, not a release: the DRAFT watermark, the
work-in-progress note and the reserved DOI in the colophon are untouched, and
settling them together with the number remains step 4 of the Zenodo release
sequence in notes/todo.md. Per README, the title-page number and the arXiv
revision are kept equal; the Zenodo ordinal floats.

Anchor matched whitespace-insensitively, exactly once. A dated .bak is
written, an "% EDITED" header prepended, and the header makes the script
refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-10-31"
SCRIPT = "scripts/patch_version_0_6_2026-10-31T1619.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/main.tex"
BAK = DEST + ".2026-10-31T1619.bak"

OLD = r"""\large\normalfont Version 0.5}"""
NEW = r"""\large\normalfont Version 0.6}"""


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))
    if "Version 0.6" in text:
        sys.exit("REFUSING: Version 0.6 is already present")
    pat = re.compile(ws(OLD))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: the version line matched %d times, expected 1" % n)
    text = pat.sub(lambda _m: NEW, text, count=1)
    if "Version 0.5" in text:
        sys.exit("REFUSING: a Version 0.5 survives")
    shutil.copy2(DEST, BAK)
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("bumped the title-page version to 0.6 in %s" % DEST)


if __name__ == "__main__":
    main()
