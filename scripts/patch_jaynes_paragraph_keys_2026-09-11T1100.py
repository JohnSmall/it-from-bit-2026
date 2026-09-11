#!/usr/bin/env python3
"""Resolve the placeholders in orphans/jaynes_paragraph_2026-07-19.tex.

Three substitutions, each recorded rather than guessed:

  jaynes1990probability -> Jaynes_89_a
      The sibling appendix, appendix_jaynes_fibration_2026-07-19.tex, records
      this in its 2026-08-23 key reconciliation and names this very file:
      "The sibling insert jaynes_paragraph_2026-07-19.tex needs the single swap
      jaynes1990probability -> Jaynes_89_a". The appendix got the swap; this
      file did not. Jaynes_89_a is "Probability in Quantum Theory", 1990 --
      the same paper the placeholder key describes, despite the key's "_89_".

  sec:hopf   -> sec:hopf-bloch          (MAP-LABEL, John, 2026-09-11)
  sec:fanout -> sec:fanout-boundary     (MAP-LABEL, John, 2026-09-11)
      The file's own header flagged these as placeholders to be adjusted to
      the master file's labels. Paper 1 has five sec:hopf-* labels and two
      sec:fanout-*, so which one was meant is an authorial decision, not a
      lookup. The third placeholder the header names, sec:born, had already
      been resolved to sec:born-invariance.

This only makes the file consistent; it does not place it in the paper.
"""

import re
import shutil
import sys

DATE = "2026-09-11"
SCRIPT = "scripts/patch_jaynes_paragraph_keys_2026-09-11T1100.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
FILE = "orphans/jaynes_paragraph_2026-07-19.tex"

SUBS = [
    (r"\autocite{jaynes1990probability}", r"\autocite{Jaynes_89_a}", 1),
    (r"\S\ref{sec:hopf}", r"\S\ref{sec:hopf-bloch}", None),
    (r"\ref{sec:hopf}", r"\ref{sec:hopf-bloch}", None),
    (r"\S\ref{sec:fanout}", r"\S\ref{sec:fanout-boundary}", None),
    (r"\ref{sec:fanout}", r"\ref{sec:fanout-boundary}", None),
]


def main():
    t = open(FILE, encoding="utf-8").read()
    if HEADER.strip() in t:
        sys.exit("REFUSING: %s already patched by %s" % (FILE, SCRIPT))

    body = re.sub(r"(?m)^\s*%.*$", "", t)
    for bad in ("sec:hopf}", "sec:fanout}"):
        pass

    done = []
    for old, new, expect in SUBS:
        n = t.count(old)
        if expect is not None and n != expect:
            sys.exit("REFUSING: %r occurs %d times, expected %d" % (old, n, expect))
        if n:
            t = t.replace(old, new)
            done.append((old, new, n))

    # no bare placeholder may survive outside a comment
    body = re.sub(r"(?m)^\s*%.*$", "", t)
    for bad in (r"\ref{sec:hopf}", r"\ref{sec:fanout}", "jaynes1990probability"):
        if bad in body:
            sys.exit("REFUSING: placeholder %r still present in the body" % bad)

    shutil.copy2(FILE, FILE + ".bak")
    open(FILE, "w", encoding="utf-8").write(HEADER + t)
    for old, new, n in done:
        print("  %-34s -> %-38s x%d" % (old, new, n))
    print("wrote %s (backup %s.bak)" % (FILE, FILE))


if __name__ == "__main__":
    main()
