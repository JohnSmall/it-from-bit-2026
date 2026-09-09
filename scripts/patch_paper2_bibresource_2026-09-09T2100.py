#!/usr/bin/env python3
"""Point paper 2 at its own bibliography.

paper2_main_2026-07-07.tex loaded self-ref-2026.bib, the Mendeley-derived
shared library, which was renamed to attic_self-ref-2026.bib.superseded when
paper 1 moved to references.bib.  Paper 2 therefore currently loads a file
that does not exist.

Paper 2 now has its own Zotero collection, self-ref-2026-paper2-cited (18
items, an exact match for its 18 cited keys), exported to
references_paper2.bib.  Nine of those 18 are shared with paper 1; the other
nine are paper 2's own spacetime/thermodynamics literature, imported from
ris/paper2_starter_refs_2026-07-07.ris, ris/aoki_energy_refs_2026-07-07.ris
and ris/gw_energy_refs_2026-07-07.ris.

The trailing comment is replaced along with the path: it read "shared
library; TODO(JS): confirm path", and the bibliography is now neither shared
nor unconfirmed.

Anchor matched whitespace-insensitively, must match exactly once; a .bak is
written, an "% EDITED" header prepended, and this script's own header line
makes it refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-09"
SCRIPT = "scripts/patch_paper2_bibresource_2026-09-09T2100.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

FILE = "paper2_main_2026-07-07.tex"
ANCHOR = (r"\addbibresource{self-ref-2026.bib} % shared library; "
          r"TODO(JS): confirm path")
NEW = (r"\addbibresource{references_paper2.bib} % Zotero collection "
       r"self-ref-2026-paper2-cited")


def ws_insensitive(anchor):
    return r"\s+".join(re.escape(p) for p in anchor.split())


def main():
    orig = open(FILE, encoding="utf-8").read()

    if HEADER.strip() in orig:
        sys.exit("REFUSING: %s already patched by %s" % (FILE, SCRIPT))

    pat = re.compile(ws_insensitive(ANCHOR))
    n = len(pat.findall(orig))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % n)
    print("anchor matched exactly once")

    # count only real commands: the file's header comment also mentions
    # "\addbibresource" in prose, without a brace
    ncmd = orig.count(r"\addbibresource{")
    if ncmd != 1:
        sys.exit("REFUSING: %d \\addbibresource{ commands, expected 1" % ncmd)

    text = pat.sub(lambda _: NEW, orig, count=1)
    if r"\addbibresource{references_paper2.bib}" not in text:
        sys.exit("REFUSING: replacement did not take")

    before = sum(1 for c in orig if ord(c) > 127)
    after = sum(1 for c in text if ord(c) > 127)
    if after != before:
        sys.exit("REFUSING: non-ASCII count changed %d -> %d" % (before, after))

    shutil.copy2(FILE, FILE + ".bak")
    with open(FILE, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("wrote %s (backup %s.bak)" % (FILE, FILE))
    print("  self-ref-2026.bib -> references_paper2.bib")


if __name__ == "__main__":
    main()
