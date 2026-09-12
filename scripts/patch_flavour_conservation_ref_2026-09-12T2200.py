#!/usr/bin/env python3
"""Resolve sec:flavour-conservation, the last undefined label in paper 1.

The sedenion section refers to "the no-force propositions of
\\S\\ref{sec:flavour-conservation}". That label is defined nowhere: the
2026-08-12 flavour splice it names went into the paper without a section label
of its own. The section's own preamble anticipates exactly this and says what
to do:

    MAP-LABELs (NOT confirmed in project knowledge; substitute real
    labels or delete the clause):
      sec:flavour-conservation -- the 2026-08-12 flavour splice
                                  (no-force propositions). Use prop:fcnc /
                                  prop:neutral-blind if the splice has no
                                  section label of its own.

Both propositions exist, in the interactions section:
  prop:fcnc          "No tree-level FCNC"
  prop:neutral-blind "Neutral compositions are generation-blind"

and the second is what the sentence goes on to paraphrase -- "there it is shown
that a neutral gate has no qubit to act on that would carry the generation".

So the clause is substituted rather than deleted: it points at the section that
holds them, and names both propositions, which is more precise than the
unresolved label ever was.

Anchor matched whitespace-insensitively, exactly once. A .bak is written, an
"% EDITED" header prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-12"
SCRIPT = "scripts/patch_flavour_conservation_ref_2026-09-12T2200.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/sedenions_generations_section_2026-08-27.tex"

OLD = r"the no-force propositions of \S\ref{sec:flavour-conservation},"
NEW = (r"the no-force propositions of \S\ref{sec:interactions}, "
       r"Propositions~\ref{prop:fcnc} and~\ref{prop:neutral-blind},")


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))

    pat = re.compile(ws(OLD))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % n)

    text = pat.sub(lambda _m: NEW, text, count=1)

    body = "\n".join(ln.split("%")[0] if not ln.lstrip().startswith("%") else ""
                     for ln in text.split("\n"))
    if "sec:flavour-conservation" in body:
        sys.exit("REFUSING: a live reference to the dead label survives")
    for lab in ("prop:fcnc", "prop:neutral-blind", "sec:interactions"):
        if ("ref{%s}" % lab) not in body:
            sys.exit("REFUSING: %s did not land" % lab)

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("substituted the flavour-conservation clause in %s" % DEST)


if __name__ == "__main__":
    main()
