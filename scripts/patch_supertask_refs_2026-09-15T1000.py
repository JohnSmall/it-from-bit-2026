#!/usr/bin/env python3
"""Cite the hypercomputation literature for the super-task claim.

`what_is_a_quantum_state.tex` carries the sentence

    Also super-tasks can exceed the bounds of a Turing machine (refs).

with `(refs)` standing in for citations that were never supplied. The claim is
that a super-task can decide what a Turing machine cannot, and three references
carry it between them:

  shagrirSupertasksAcceleratingTuring2004
      Shagrir, "Super-tasks, accelerating Turing machines and uncomputability",
      Theoretical Computer Science 317 (2004) 105-114. The claim itself, title
      for title, and it argues it through Thomson's lamp -- the example this
      paragraph has just used.
  Hamkins_2002
      Hamkins, "Infinite Time Turing Machines", Minds and Machines 12 (2002)
      521. The formal result: transfinite ordinal running time decides sets far
      beyond the arithmetical hierarchy.
  Copeland_2002
      Copeland, "Hypercomputation", Minds and Machines 12 (2002) 461. The
      survey of the field, for a reader who does not know the literature.

All three were already in the Zotero library and were added to the
`self-ref-2026-cited` collection on 2026-09-15; Shagrir's item type was
corrected from conferencePaper to journalArticle at the same time, and
Copeland's mangled issue field from a Mendeley import string to "4". The
re-export carries all three.

Not cited, deliberately: Kieu, "Quantum Hypercomputation" (same issue), whose
adiabatic claim was refuted in the subsequent literature; and Etesi and
Nemeti's Malament-Hogarth route, whose library record is too damaged to cite
without rebuilding it.

Anchor matched whitespace-insensitively, exactly once. A .bak is written, an
"% EDITED" header prepended, and the header makes the script refuse to run
twice.
"""

import re
import shutil
import sys

DATE = "2026-09-15"
SCRIPT = "scripts/patch_supertask_refs_2026-09-15T1000.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/what_is_a_quantum_state.tex"

OLD = "super-tasks can exceed the bounds of a Turing machine (refs)."
NEW = ("super-tasks can exceed the bounds of a Turing machine\n"
       "\\autocite{shagrirSupertasksAcceleratingTuring2004,Hamkins_2002,Copeland_2002}.")
KEYS = ("shagrirSupertasksAcceleratingTuring2004", "Hamkins_2002", "Copeland_2002")


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))
    for k in KEYS:
        if k in text:
            sys.exit("REFUSING: %s is already cited here" % k)

    pat = re.compile(ws(OLD))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % n)

    # the keys must exist in the bibliography this paper uses
    bib = open("paper1/references.bib", encoding="utf-8").read()
    for k in KEYS:
        if not re.search(r"^@[a-z]+\{%s," % re.escape(k), bib, re.M | re.I):
            sys.exit("REFUSING: %s is not in paper1/references.bib -- re-export first" % k)

    text = pat.sub(lambda _m: NEW, text, count=1)

    if "(refs)" in text.split("\n")[0:0] or OLD in text:
        sys.exit("REFUSING: the placeholder survives")
    for k in KEYS:
        if text.count(k) != 1:
            sys.exit("REFUSING: %s appears %d times" % (k, text.count(k)))

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("cited %d references for the super-task claim in %s" % (len(KEYS), DEST))


if __name__ == "__main__":
    main()
