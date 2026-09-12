#!/usr/bin/env python3
"""Point the zero-divisor appendix at the Gunaydin key the library already uses.

`bib/zd_structure_refs_2026-08-31.bib` supplies `gunaydin1973quark` for
Gunaydin and Gursey, "Quark structure and octonions". The library already holds
that work, under `gunaydingursey1974quark`, and the duplicate check matched them
on DOI 10.1063/1.1666240 -- the same paper, so importing the batch entry would
have created a duplicate.

The other six duplicates found in the same check were resolved the other way,
by re-pinning the library item to the key the paper wants, because none of their
existing keys was cited anywhere. This one is different: `gunaydingursey1974quark`
is already cited in two files and already exported into `references.bib`, so
re-pinning it would break those citations. The citing appendix moves instead.

(The existing key names 1974 while the item's date field is 1973, which the
journal reference supports -- J. Math. Phys. 14. The key is only a label, so it
is left alone rather than churned; renaming it would be a third way to break the
two standing citations.)

Anchor matched whitespace-insensitively, exactly once. A .bak is written, an
"% EDITED" header prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-12"
SCRIPT = "scripts/patch_gunaydin_citekey_2026-09-12T2100.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/appendices/appendix_zd_structure_2026-09-01.tex"
OLD = "gunaydin1973quark"
NEW = "gunaydingursey1974quark"


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))

    body = "\n".join(ln.split("%")[0] if not ln.lstrip().startswith("%") else ""
                     for ln in text.split("\n"))
    n = len(re.findall(r"\b%s\b" % re.escape(OLD), body))
    if n != 1:
        sys.exit("REFUSING: %s occurs %d times outside comments, expected 1" % (OLD, n))
    if re.search(r"\b%s\b" % re.escape(NEW), body):
        sys.exit("REFUSING: %s is already cited here" % NEW)

    # replace only the live occurrence, leaving the preamble's record intact
    out, done = [], False
    for line in text.split("\n"):
        if not done and not line.lstrip().startswith("%"):
            code, sep, comment = line.partition("%")
            if re.search(r"\b%s\b" % re.escape(OLD), code):
                code = re.sub(r"\b%s\b" % re.escape(OLD), NEW, code)
                line = code + sep + comment
                done = True
        out.append(line)
    if not done:
        sys.exit("REFUSING: no live occurrence was replaced")
    text = "\n".join(out)

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("re-pointed %s -> %s in %s" % (OLD, NEW, DEST))


if __name__ == "__main__":
    main()
