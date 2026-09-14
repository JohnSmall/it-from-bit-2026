#!/usr/bin/env python3
"""Cite the repository's Zenodo record in the introduction.

JS, 2026-09-14: the reserved DOI 10.5281/zenodo.22755871 is in Zotero as
small2026itfrombit (bib/zenodo_repository_ref_2026-09-14T0730.bib) and references.bib has
been re-exported. main.tex line 148 said "download from Zenodo (refs)"; the placeholder
becomes the citation. One file, one header, one run only.

paper1/conclusions_section.tex still cites the placeholder key zenodo_reference; that file
is being written in another session and is left alone here.

The anchor is matched whitespace-insensitively and must match exactly once. The paragraph
is not re-filled (a one-token change). A dated .bak is written, a "% EDITED" header is
prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-14"
STAMP = "2026-09-14T0800"
SCRIPT = "scripts/patch_zenodo_cite_main_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

MAIN = "paper1/main.tex"
OLD = r"up into an AI workbench anyone can download from Zenodo (refs). Therefore it is presented in a"
NEW = r"up into an AI workbench anyone can download from Zenodo \autocite{small2026itfrombit}. Therefore it is presented in a"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    with open(MAIN, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (MAIN, HEADER.strip()))
    pat = re.compile(ws(OLD))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % n)
    m = pat.search(text)
    text = text[:m.start()] + NEW + text[m.end():]
    if text.count("small2026itfrombit") != 1:
        sys.exit("REFUSING: key cited %d times, expected 1" % text.count("small2026itfrombit"))
    shutil.copy(MAIN, MAIN + "." + STAMP + ".bak")
    with open(MAIN, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak)" % (MAIN, MAIN, STAMP))


if __name__ == "__main__":
    main()
