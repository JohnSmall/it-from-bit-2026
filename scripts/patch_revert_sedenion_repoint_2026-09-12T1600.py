#!/usr/bin/env python3
"""Revert the sec:sedenions-generations re-point. It was wrong.

On 2026-09-11, patch_undefined_section_refs_2026-09-11T2030.py treated
sec:sedenions-generations as a label that had never been created and re-pointed
its three occurrences in wigners_friend to sec:sedenion-announcement, the zoo's
subsection. It also left sec:sedenions-mixing undefined and called the choice of
target an editorial one.

Both judgements were wrong, and for the same reason: the section that defines
those two labels, `Sedenions and the Three Generations`, existed but was not in
the repository. The references were correct as written. Worse, that section's
own preamble records that it ABSORBS sec:sedenion-announcement, which is to be
reduced to a forward pointer when it lands -- so the re-point aimed three
references at a label that is itself on its way out.

This restores the three references verbatim. sec:sedenions-mixing was never
touched and needs nothing. The other eight re-points in that patch stand: they
were genuine typos (sec:Kioid, sec:negative_probaility) or headings that really
did lack a label.

Anchors matched whitespace-insensitively, each exactly once. A .bak is written,
an "% EDITED" header prepended, and the header makes the script refuse to run
twice.
"""

import re
import shutil
import sys

DATE = "2026-09-12"
SCRIPT = "scripts/patch_revert_sedenion_repoint_2026-09-12T1600.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/wigners_friend_in_the_hopf_picture_2026-06-13.tex"

WRONG = r"\S\ref{sec:sedenion-announcement}"
RIGHT = r"\S\ref{sec:sedenions-generations}"
EXPECTED = 3


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))

    n = text.count(WRONG)
    if n != EXPECTED:
        sys.exit("REFUSING: found %d occurrences of the wrong target, expected %d"
                 % (n, EXPECTED))
    before_total = len(re.findall(r"\\S\\ref\{sec:sedenion", text))

    text = text.replace(WRONG, RIGHT)

    if text.count(WRONG):
        sys.exit("REFUSING: an occurrence survived")
    if text.count(RIGHT) != EXPECTED:
        sys.exit("REFUSING: expected %d restored references, found %d"
                 % (EXPECTED, text.count(RIGHT)))
    if len(re.findall(r"\\S\\ref\{sec:sedenion", text)) != before_total:
        sys.exit("REFUSING: the number of sedenion references changed")

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("reverted %d references in %s" % (EXPECTED, DEST))


if __name__ == "__main__":
    main()
