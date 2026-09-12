#!/usr/bin/env python3
"""Input the zero-divisor structure appendix, and honour its dependency note.

`appendix_zd_structure_2026-09-01.tex` is the tex consumer of the refs-first
batch `zd_structure_refs_2026-08-31.{ris,bib}`; it cites all five of that
batch's keys and no others that are absent. All seven labels it mints were
checked against the live tree and none collides. Its only cross-references are
`sec:masses` and `sec:generations`, both of which exist.

Two edits.

(1) main.tex: input it after the reverse-flow appendix, so the two appendices
    added on 2026-09-12 sit in the order their material was drafted.

(2) The appendix's own preamble records a dependency and says what to do about
    it:

      DEPENDENCY NOTE: eq:zd-defect intentionally restates the identity that
        the bridge splice mints as eq:debt-defect in sec:masses; an appendix
        should be self-contained. If both land, add after eq:zd-defect:
        "(quoted in \\S\\ref{sec:masses} as Eq.~\\eqref{eq:debt-defect})".

    Both have landed --- `eq:debt-defect` went into the masses section with the
    bridge splice on 2026-09-10 --- so the sentence is added as instructed,
    verbatim. Without it the paper states one identity twice with no signpost
    between the two statements.

Anchors matched whitespace-insensitively, each exactly once. A .bak is written
per file, an "% EDITED" header prepended, and the header makes the script
refuse to run twice.

BUILD DEPENDENCY: import `bib/zd_structure_refs_2026-08-31.bib` and re-export,
or biber reports five undefined citations from this file.
"""

import re
import shutil
import sys

DATE = "2026-09-12"
SCRIPT = "scripts/patch_input_zd_appendix_2026-09-12T2000.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
MAIN = "paper1/main.tex"
APP = "paper1/appendices/appendix_zd_structure_2026-09-01.tex"

ANCHOR = r"\input{appendices/appendix_reverse_flow_2026-07-23}"
ADDED = r"\input{appendices/appendix_zd_structure_2026-09-01}"
CROSSREF = r" (quoted in \S\ref{sec:masses} as Eq.~\eqref{eq:debt-defect})"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    texts = {}
    for path in (MAIN, APP):
        t = open(path, encoding="utf-8").read()
        if HEADER.strip() in t:
            sys.exit("REFUSING: %s already patched by %s" % (path, SCRIPT))
        texts[path] = t

    # (1) the input line
    if "appendix_zd_structure" in texts[MAIN]:
        sys.exit("REFUSING: the appendix is already input")
    pat = re.compile(ws(ANCHOR))
    if len(pat.findall(texts[MAIN])) != 1:
        sys.exit("REFUSING: the reverse-flow input line is not unique")
    m = pat.search(texts[MAIN])
    line_start = texts[MAIN].rfind("\n", 0, m.start()) + 1
    indent = texts[MAIN][line_start:m.start()]
    n_inputs = texts[MAIN].count(r"\input{")
    texts[MAIN] = texts[MAIN][:m.end()] + "\n" + indent + ADDED + texts[MAIN][m.end():]
    if texts[MAIN].count(r"\input{") != n_inputs + 1:
        sys.exit("REFUSING: input count did not rise by exactly one")

    # (2) the cross-reference the appendix's preamble asks for. Guard against
    # the instruction's own text in the preamble comment by stripping comments
    # before testing for idempotence.
    t = texts[APP]
    body = "\n".join(ln.split("%")[0] if not ln.lstrip().startswith("%") else ""
                     for ln in t.split("\n"))
    if "eq:debt-defect" in body:
        sys.exit("REFUSING: the cross-reference is already in the body")
    if len(re.findall(r"\\label\{eq:zd-defect\}", t)) != 1:
        sys.exit("REFUSING: eq:zd-defect is not defined exactly once")
    # It lands on the sentence that states what the right-hand side is, which is
    # the sentence immediately after the display.
    SENT = "evaluated on the four components."
    pat2 = re.compile(ws(SENT))
    if len(pat2.findall(t)) != 1:
        sys.exit("REFUSING: the anchor sentence matched %d times, expected 1"
                 % len(pat2.findall(t)))
    m2 = pat2.search(t)
    texts[APP] = t[:m2.end() - 1] + CROSSREF + "." + t[m2.end():]

    for path, t in texts.items():
        shutil.copy2(path, path + ".bak")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(HEADER + t)
        print("patched %s" % path)


if __name__ == "__main__":
    main()
