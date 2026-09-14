#!/usr/bin/env python3
"""Make the "Spacetime dimensionality" headline say what the spacetime section argues, and
make the spacetime section name the Bloch sphere where it uses it.

JS, 2026-09-12: the headline item spoke of state reduction on the Bloch sphere and Lorentz
boosts forcing d = 3, while the spacetime section never mentions the Bloch sphere. The
section gets the count from Adams' parallelisable spheres plus the associativity filter
(sec:three-dimensions, with a general-relativistic route from mutual acceleration), and the
Lorentz group separately from the computability split fixing C^2 (sec:lorentz, "the qubit
density operators fill the future cone"). The headline's Kaluza--Klein sentence said the
opposite of the section ("misdiagnoses it as spatial"; no metric) and its "six internal
dimensions of SU(3) x SU(2) x U(1)" was wrong on its face.

Two files, one header each, one run only.

paper1/main.tex
  1. The "Spacetime dimensionality" item is replaced: the two routes to the count as the
     section gives them; the Lorentz group from C^2 with the density operators as the
     future cone and the pure states as its celestial sphere; S^7 as filter, no metric,
     the Kaluza--Klein remark as the section makes it; op:three-dimensions named.
paper1/spacetime_from_non-computability.tex
  2. One sentence inserted in sec:lorentz after "the qubit density operators fill the
     future cone" (after the Mueller citations): the Bloch ball as the unit-trace slice of
     the cone, the Bloch sphere as its celestial sphere with the Moebius action of
     SL(2,C), state reduction and boosts as one operation in two charts. Inserted as its
     own lines; the surrounding paragraph is NOT re-filled because it contains a
     "%"-continued line ("Euclidean-and-three%") that re-filling would corrupt.

Every anchor is matched whitespace-insensitively and must match exactly once; the headline
replacement is pre-filled to 96 columns. A dated .bak is written per file, a "% EDITED"
header is prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-12"
STAMP = "2026-09-12T1400"
SCRIPT = "scripts/patch_spacetime_bloch_headline_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

MAIN = "paper1/main.tex"
SPACE = "paper1/spacetime_from_non-computability.tex"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def fill(s):
    return textwrap.fill(" ".join(s.split()), width=WIDTH,
                         break_long_words=False, break_on_hyphens=False)


def replace_once(text, anchor, replacement):
    pat = re.compile(ws(anchor.strip()))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1:\n  %s" % (n, anchor.strip()[:70]))
    m = pat.search(text)
    return text[:m.start()] + replacement + text[m.end():]


# ---------------------------------------------------------------- main.tex
OLD_ITEM = r"""
\item \textbf{Spacetime dimensionality.} By recognising spacelike separation to be an analog of
non-computable separation between computational states we find that the requirement that state
reduction on the Bloch sphere be consistent with Lorentz boosts demands
$\mathrm{Spin}(1,d) \cong SL(2,\mathbb{A})$ for a normed division algebra~$\mathbb{A}$. The
computability split selects $\mathbb{A} = \mathbb{C}$, giving
$SL(2,\mathbb{C}) = \mathrm{Spin}(1,3)$ and thus $d = 3$ spatial dimensions. The six internal
dimensions of $SU(3) \times SU(2) \times U(1)$ account for the reduction from $d = 9$ (the
octonionic case) to $d = 3$, reproducing the Kaluza--Klein dimensional decomposition
$9+1 = (3+1) + 2 + 4$ with a structural explanation. But note that those extra dimensions cannot
admit a metric structure.
"""
NEW_ITEM = fill(r"""
\item \textbf{Spacetime dimensionality.} Spacelike separation is read as non-computable
separation between computational states. The closed timelike curves that define it need
consistent parallel transport around a loop, so the sphere of directions must be parallelisable,
one of $S^1$, $S^3$, $S^7$ \autocite{adams1960hopf}; information arriving with a causal history
must compose as a group, which excludes the non-associative $S^7$, and the abelian $S^1$ cannot
carry the structure alone, so space has exactly three dimensions
(Section~\ref{sec:three-dimensions}; a general-relativistic route from mutual acceleration
reaches the same count). The Lorentz group follows separately: the computability split fixes
the state space as $\mathbb{C}^2$, whose Hermitian operators are $\mathbb{R}^{1,3}$ with the
density operators filling the future cone and the pure states, the Bloch sphere, forming its
celestial sphere, so that $SL(2,\mathbb{C}) \cong \mathrm{Spin}(1,3)$ acts on measurement as it
acts on the cone (Section~\ref{sec:lorentz}). $S^7$ contributes no geometry and admits no
metric; it contributes the strong interaction as a filter on what may be exchanged, which is
why gauge symmetry has so often been mistaken for compactified extra dimensions. Dimension
three as a theorem is Open Problem~\ref{op:three-dimensions}.
""")

# ---------------------------------------------------------------- spacetime section
OLD_LORENTZ = r"""
from the relativity of simultaneity \autocite{GarnerMuellerDahlsten2017}. The
$SL(2,\mathbb{A})$ correspondence is rigorous; its identification with
"""
NEW_LORENTZ = (r"from the relativity of simultaneity \autocite{GarnerMuellerDahlsten2017}." + "\n"
               + fill(r"""
In these coordinates the Bloch ball is the unit-trace slice of the cone and the Bloch sphere
its boundary rays, the celestial sphere on which $SL(2,\mathbb{C})$ acts by M\"obius
transformations; state reduction sends a point of the ball to a point of the sphere, and a
boost sends the sphere to itself, which is what lets the two be one operation in two charts.
""") + "\n"
               + r"The $SL(2,\mathbb{A})$ correspondence is rigorous; its identification with")


def patch(path, edits, must_contain):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (path, HEADER.strip()))
    for old, new in edits:
        text = replace_once(text, old, new)
    for s in must_contain:
        if s not in text:
            sys.exit("REFUSING: %s lacks %r after the edit" % (path, s))
    shutil.copy(path, path + "." + STAMP + ".bak")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak)" % (path, path, STAMP))


def main():
    patch(MAIN, [(OLD_ITEM, NEW_ITEM)],
          [r"\ref{sec:three-dimensions}", r"\ref{sec:lorentz}", r"\ref{op:three-dimensions}"])
    patch(SPACE, [(OLD_LORENTZ, NEW_LORENTZ)],
          ["Euclidean-and-three%", "celestial sphere on which"])


if __name__ == "__main__":
    main()
