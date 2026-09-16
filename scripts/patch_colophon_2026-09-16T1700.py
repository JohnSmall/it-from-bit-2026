#!/usr/bin/env python3
"""Give the paper a colophon, and a fixed date instead of \\today.

Two problems this fixes.

`\\date{\\today}` stamps the build date, so every rebuild produces a
differently dated PDF and no copy in circulation can say what produced it. A
preprint needs a date that belongs to the version, not to the machine that
last compiled it.

And nothing in the paper says where the source, the computations or the
working record live. The introduction mentions the Zenodo archive in passing
and cites it, but a reader who has only the PDF -- which is how most readers
will have it -- has no line that tells them which version they hold and where
to find everything behind it.

The colophon goes immediately after \\maketitle, beneath the existing
work-in-progress note. It does not repeat the version or the date: the title
block already carries both, and saying them twice on one page reads as an
oversight rather than as emphasis.

Version is left at 0.5, as the title already declares: the paper is
pre-submission and the DRAFT watermark is still on. When it is tagged and
submitted, this block and the title both want the new number, and the DOI
wants to become the concept DOI.

DOI NOTE: 10.5281/zenodo.22755871 is the *reserved version* DOI, which points
at one deposit. Zenodo mints the *concept* DOI -- the one that always resolves
to the latest version -- only on first publication. When it exists it should
replace this one both here and in the `small2026itfrombit` bibliography entry,
because both places are pointing at a living record rather than a snapshot.

Anchors matched whitespace-insensitively, each exactly once. A .bak is
written, an "% EDITED" header prepended, and the header makes the script
refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-16"
SCRIPT = "scripts/patch_colophon_2026-09-16T1700.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/main.tex"

OLD_DATE = r"\date{\today}"
NEW_DATE = r"\date{16 September 2026}"

OLD_BLOCK = r"""\begin{center}
\itshape This is a work in progress and will be updated frequently.
\end{center}"""

NEW_BLOCK = r"""\begin{center}
\itshape This is a work in progress and will be updated frequently.
\end{center}

\begin{center}\small
The source of this paper, every computation behind it, and the complete
working record --- including the routes that failed --- are archived at\\
\href{https://doi.org/10.5281/zenodo.22755871}{\texttt{doi:10.5281/zenodo.22755871}}
\quad$\cdot$\quad
\href{https://github.com/JohnSmall/it-from-bit-2026}{\texttt{github.com/JohnSmall/it-from-bit-2026}}
\end{center}"""


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))
    if "the complete\nworking record" in text:
        sys.exit("REFUSING: the colophon is already present")

    if text.count(OLD_DATE) != 1:
        sys.exit("REFUSING: \\date{\\today} occurs %d times, expected 1" % text.count(OLD_DATE))
    text = text.replace(OLD_DATE, NEW_DATE, 1)

    pat = re.compile(ws(OLD_BLOCK))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: the work-in-progress block matched %d times, expected 1" % n)
    text = pat.sub(lambda _m: NEW_BLOCK, text, count=1)

    if r"\today" in text:
        sys.exit("REFUSING: a \\today survives")
    if text.count(r"\begin{center}") != text.count(r"\end{center}"):
        sys.exit("REFUSING: center environments are unbalanced")
    # twice by design: once in the href target, once in the displayed text
    if text.count("10.5281/zenodo.22755871") != 2:
        sys.exit("REFUSING: the DOI appears %d times, expected 2"
                 % text.count("10.5281/zenodo.22755871"))
    if text.count("github.com/JohnSmall/it-from-bit-2026") < 2:
        sys.exit("REFUSING: the repository link did not land")

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("added the colophon and fixed the date in %s" % DEST)


if __name__ == "__main__":
    main()
