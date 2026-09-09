#!/usr/bin/env python3
"""Collapse three duplicate citation keys onto their surviving counterparts.

Each pair below cites one and the same work under two keys, so the
bibliography currently prints these three works twice.  The survivor in
each case carries the better metadata:

  Coecke2010TheEntanglement       -> coeckekissinger2010compositional
      survivor is a proper @inproceedings (ICALP 2010) with a DOI; the
      loser is a Mendeley @article mis-typed as an LNCS journal.
  borsten_2009                    -> borsten2009blackholes
      identical DOI; survivor carries full author names, not initials.
  brukner_2000_shannon            -> bruknerzeilinger2001shannon
      identical DOI, so the year difference is preprint vs published.
      2001 is correct for Phys. Rev. A 63, 022113; the loser also has a
      malformed page range (022113--022111, end before start).

Anchors are matched whitespace-insensitively and each must match exactly
once.  A .bak is written before any change, an "% EDITED" header is
prepended, and the presence of that header makes the script refuse to
run a second time.
"""

import re
import shutil
import sys

DATE = "2026-09-09"
HEADER = "% EDITED " + DATE + " scripts/patch_duplicate_citekeys_2026-09-09T1630.py\n"

# (file, anchor, old key, new key) -- anchor must be unique within the file
EDITS = [
    ("main.tex",
     r"\autocite{Coecke2010TheEntanglement}",
     "Coecke2010TheEntanglement", "coeckekissinger2010compositional"),
    ("main.tex",
     r"\autocite{borsten_2009}",
     "borsten_2009", "borsten2009blackholes"),
    ("what_is_a_quantum_state.tex",
     r"clearly explained in \autocite{brukner_2000_shannon}",
     "brukner_2000_shannon", "bruknerzeilinger2001shannon"),
    ("what_is_a_quantum_state.tex",
     r"contrary to Brukner and Zeilinger \autocite{brukner_2000_shannon}",
     "brukner_2000_shannon", "bruknerzeilinger2001shannon"),
]


def ws_insensitive(anchor):
    """Regex matching anchor with any run of whitespace for each space."""
    return r"\s+".join(re.escape(p) for p in anchor.split())


def main():
    files = []
    for f, _, _, _ in EDITS:
        if f not in files:
            files.append(f)

    # refuse to run twice
    for f in files:
        with open(f, encoding="utf-8") as fh:
            if fh.readline().startswith("% EDITED"):
                sys.exit("REFUSING: %s already carries an %% EDITED header" % f)

    # verify every anchor matches exactly once before touching anything
    text = {f: open(f, encoding="utf-8").read() for f in files}
    orig = dict(text)
    for f, anchor, old, new in EDITS:
        n = len(re.findall(ws_insensitive(anchor), text[f]))
        if n != 1:
            sys.exit("REFUSING: anchor in %s matched %d times, expected 1:\n  %s"
                     % (f, n, anchor))
        if old not in anchor:
            sys.exit("REFUSING: key %s absent from its own anchor" % old)
    print("all %d anchors matched exactly once" % len(EDITS))

    # apply
    counts = {}
    for f, anchor, old, new in EDITS:
        pat = re.compile(ws_insensitive(anchor))
        m = pat.search(text[f])
        span = m.group(0)
        if old not in span:
            sys.exit("REFUSING: key %s not inside matched span in %s" % (old, f))
        text[f] = text[f][:m.start()] + span.replace(old, new) + text[f][m.end():]
        counts[(f, old, new)] = counts.get((f, old, new), 0) + 1
        print("  %s: %s -> %s" % (f, old, new))

    for f in files:
        # These files already carry pre-existing non-ASCII (e.g. "Godel" with
        # an umlaut, curly quotes) contrary to the pure-ASCII rule.  That is
        # not this script's to rewrite, so assert only that the edit itself
        # introduces no new non-ASCII rather than that the file is clean.
        before = sum(1 for c in orig[f] if ord(c) > 127)
        after = sum(1 for c in text[f] if ord(c) > 127)
        if after != before:
            sys.exit("REFUSING: %s non-ASCII count changed %d -> %d"
                     % (f, before, after))
        shutil.copy2(f, f + ".bak")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(HEADER + text[f])
        print("wrote %s (backup %s.bak)" % (f, f))

    for f, old, new in sorted(counts):
        print("replaced %s -> %s in %s (%d occurrence(s))"
              % (old, new, f, counts[(f, old, new)]))


if __name__ == "__main__":
    main()
