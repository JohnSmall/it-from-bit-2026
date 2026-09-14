#!/usr/bin/env python3
"""Shorten the "Spacetime dimensionality" headline item to a teaser with pointers.

JS, 2026-09-12: the item rewritten at T1400 was correct but too long; the headline list
should name a few results with pointers to where they are derived, enough to entice the
reader, not half a derivation. One file, one header, one run only.

paper1/main.tex: the T1400 item is replaced by three lines that say what is suggested
(three dimensions of space, and the internal degrees of freedom so often mistaken for
hidden ones, understood through non-computable distance) and point at
sec:three-dimensions, sec:lorentz and op:three-dimensions.

The anchor is matched whitespace-insensitively and must match exactly once; the
replacement is pre-filled to 96 columns. A dated .bak is written, a "% EDITED" header is
prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-12"
STAMP = "2026-09-12T1415"
SCRIPT = "scripts/patch_spacetime_headline_short_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

MAIN = "paper1/main.tex"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def fill(s):
    return textwrap.fill(" ".join(s.split()), width=WIDTH,
                         break_long_words=False, break_on_hyphens=False)


OLD_ITEM = r"""
\item \textbf{Spacetime dimensionality.} Spacelike separation is read as non-computable
separation between computational states. The closed timelike curves that define it need
consistent parallel transport around a loop, so the sphere of directions must be parallelisable,
one of $S^1$, $S^3$, $S^7$ \autocite{adams1960hopf}; information arriving with a causal history
must compose as a group, which excludes the non-associative $S^7$, and the abelian $S^1$ cannot
carry the structure alone, so space has exactly three dimensions
(Section~\ref{sec:three-dimensions}; a general-relativistic route from mutual acceleration
reaches the same count). The Lorentz group follows separately: the computability split fixes the
state space as $\mathbb{C}^2$, whose Hermitian operators are $\mathbb{R}^{1,3}$ with the density
operators filling the future cone and the pure states, the Bloch sphere, forming its celestial
sphere, so that $SL(2,\mathbb{C}) \cong \mathrm{Spin}(1,3)$ acts on measurement as it acts on
the cone (Section~\ref{sec:lorentz}). $S^7$ contributes no geometry and admits no metric; it
contributes the strong interaction as a filter on what may be exchanged, which is why gauge
symmetry has so often been mistaken for compactified extra dimensions. Dimension three as a
theorem is Open Problem~\ref{op:three-dimensions}.
"""
NEW_ITEM = fill(r"""
\item \textbf{Spacetime dimensionality.} We suggest a way to understand the three dimensions
of space, and the internal degrees of freedom so often mistaken for hidden ones, in terms of
non-computable distance: the count comes from which spheres can serve as rulers
(Section~\ref{sec:three-dimensions}), the Lorentz group from the qubit's own geometry
(Section~\ref{sec:lorentz}), and dimension three as a theorem is Open
Problem~\ref{op:three-dimensions}.
""")


def main():
    with open(MAIN, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (MAIN, HEADER.strip()))
    pat = re.compile(ws(OLD_ITEM.strip()))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1" % n)
    m = pat.search(text)
    text = text[:m.start()] + NEW_ITEM + text[m.end():]
    for lab in (r"\ref{sec:three-dimensions}", r"\ref{sec:lorentz}", r"\ref{op:three-dimensions}"):
        if lab not in text:
            sys.exit("REFUSING: %s missing after the edit" % lab)
    shutil.copy(MAIN, MAIN + "." + STAMP + ".bak")
    with open(MAIN, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak)" % (MAIN, MAIN, STAMP))


if __name__ == "__main__":
    main()
