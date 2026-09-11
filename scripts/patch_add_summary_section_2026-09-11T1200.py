#!/usr/bin/env python3
"""Add the Summary of Results section to main.tex, after predictions.

summary_section_2026-07-07.tex collects the paper's results by stratum and
closes with sec:what-remains, the suite index. None of its 136 substantive
lines was anywhere in Paper 1, all 52 of its cross-references resolve, and
neither sec:summary nor sec:what-remains collides with an existing label.

PLACEMENT, per John and matching the file's own recommendation: between
\\input{predictions_section_2026-06-13} and the Open Problems list, so the
prose closes before the formal index and the index is the paper's last word
before the appendices.

The file's recommendation also lists \\input{conclusions_section} between the
two. That file does not exist: its header records the Conclusions as John's to
write, in his own voice, with a placeholder comment marking the seam. The
\\input line is therefore NOT added, and a comment is left in main.tex at the
point where it belongs.

Anchors matched whitespace-insensitively, each exactly once. A .bak is
written, an "% EDITED" header prepended, and this script's own header makes it
refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-11"
SCRIPT = "scripts/patch_add_summary_section_2026-09-11T1200.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/main.tex"

ANCHOR = r"\input{predictions_section_2026-06-13}"
FOLLOWS = r"\renewcommand{\listtheoremname}{Open Problems}"
ADDED = (r"\input{summary_section_2026-07-07}"
         "\n% TODO(JS): \\input{conclusions_section} belongs here, in your own voice,"
         "\n% between the summary of results and the Open Problems index.")


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    dest = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in dest:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))
    if "summary_section_2026-07-07" in dest:
        sys.exit("REFUSING: main.tex already inputs the summary section")

    for needle, label in ((ANCHOR, "predictions input"), (FOLLOWS, "Open Problems list")):
        if len(re.findall(ws(needle), dest)) != 1:
            sys.exit("REFUSING: %s matched %d times, expected 1"
                     % (label, len(re.findall(ws(needle), dest))))

    m = re.search(ws(ANCHOR), dest)
    tail = dest[m.end():]
    if not re.match(r"\s*" + ws(FOLLOWS), tail):
        sys.exit("REFUSING: the Open Problems list does not immediately follow predictions")

    new = dest[:m.end()] + "\n" + ADDED + dest[m.end():]

    if new.count(r"\input{summary_section_2026-07-07}") != 1:
        sys.exit("REFUSING: summary input appears %d times"
                 % new.count(r"\input{summary_section_2026-07-07}"))

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + new)
    print("added the summary section to %s" % DEST)


if __name__ == "__main__":
    main()
