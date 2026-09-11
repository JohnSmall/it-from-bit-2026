#!/usr/bin/env python3
"""Re-point the eight citations of patch_koide_citations_jordan_sense_2026-09-11T2000.py
to the keys Better BibTeX actually exported.

The RIS batch bib/koide_bargmann_jordan_refs_2026-09-11T2000.ris (written to ris/, since
renamed bib/) carried author+year+keyword keys in its ID fields; Zotero's RIS importer has
no citation-key field and discarded them, so Better BibTeX generated formula keys
(auth.lower + shorttitle(3, 3) + year). references.bib now holds the entries under the
right-hand names below, so the .tex must cite those. Batches are .bib from now on, whose
entry keys BBT keeps and pins (bib/README.md); this situation should not recur.

One file, one header, one run only. Each old key must occur exactly the number of times
recorded here (springerveldkamp2000octonions is cited twice, in the proposition and its
proof); the script refuses otherwise. A dated .bak is written and a "% EDITED" header is
prepended, which makes the script refuse to run twice.
"""

import shutil
import sys

DATE = "2026-09-11"
STAMP = "2026-09-11T2100"
SCRIPT = "scripts/patch_koide_citation_keys_bbt_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

MASSES = "paper1/masses_section_2026-06-08.tex"

# old key -> (new key, expected occurrences in the .tex)
KEYS = {
    "bargmann1964wigner":            ("bargmannNoteWignersTheorem1964", 1),
    "mukundasimon1993kinematic":     ("mukundaQuantumKinematicApproach1993", 1),
    "pancharatnam1956interference":  ("pancharatnamGeneralizedTheoryInterference1956", 1),
    "woottersfields1989unbiased":    ("woottersOptimalStatedeterminationMutually1989", 1),
    "durt2010unbiased":              ("durtMutuallyUnbiasedBases2010", 1),
    "baker1975transcendental":       ("bakerTranscendentalNumberTheory1975", 1),
    "springerveldkamp2000octonions": ("springerOctonionsJordanAlgebras2000", 2),
    "draymanogue1999eigenvalue":     ("drayExceptionalJordanEigenvalue1999", 1),
}


def main():
    with open(MASSES, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (MASSES, HEADER.strip()))
    for old, (new, n) in KEYS.items():
        c = text.count(old)
        if c != n:
            sys.exit("REFUSING: key %s occurs %d times, expected %d" % (old, c, n))
        if new in text:
            sys.exit("REFUSING: new key %s already present" % new)
    for old, (new, _) in KEYS.items():
        text = text.replace(old, new)
    shutil.copy(MASSES, MASSES + "." + STAMP + ".bak")
    with open(MASSES, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s: %d keys re-pointed (backup %s.%s.bak)" % (MASSES, len(KEYS), MASSES, STAMP))


if __name__ == "__main__":
    main()
