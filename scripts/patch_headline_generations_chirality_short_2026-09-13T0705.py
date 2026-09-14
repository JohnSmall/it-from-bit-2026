#!/usr/bin/env python3
"""Shorten the "Three generations" and "Chirality" headline items to the teaser register.

JS, 2026-09-12/13: the headline list should name a few results with pointers to where
they are derived, enough to entice the reader, not half a derivation. The two items
written by patch_sedenion_fossils_headline_2026-09-12T1345.py were correct but ten to
twelve lines each. One file, one header, one run only.

paper1/main.tex: each item becomes three or four lines, pointing at
sec:sedenions-generations, sec:generations and op:chirality. The body-text sources they
summarise are unchanged.

Anchors are matched whitespace-insensitively and must match exactly once; replacements
are pre-filled to 96 columns. A dated .bak is written, a "% EDITED" header is prepended,
and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-13"
STAMP = "2026-09-13T0705"
SCRIPT = "scripts/patch_headline_generations_chirality_short_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

MAIN = "paper1/main.tex"


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


OLD_GEN = r"""
\item \textbf{Three generations.} Doubling the octonions to the sedenions leaves the identity
component of the automorphism group where it was, $\mathrm{Aut}(\mathbb{S})_0 = G_2$, and adds
exactly one finite factor, $\mathrm{Aut}(\mathbb{S}) \cong G_2 \times S_3$
\autocite{brown1967generalized}. That $S_3$ permutes the three octonion halvings $\mathbb{O}$,
$\psi\mathbb{O}$, $\psi^2\mathbb{O}$ that share the doubling unit, and the generations are that
orbit: three because the factor is $S_3$, a family label and never a fourth force because a
component group carries no Lie algebra, and no fifth rung because the fibrations that host
forces stop at the octonions (Section~\ref{sec:sedenions-generations}). The register's
frustrated-pair count of Section~\ref{sec:generations} reaches the same three plus a sterile
class and is read as the shadow of this orbit.
"""
NEW_GEN = fill(r"""
\item \textbf{Three generations.} Doubling the octonions to the sedenions adds exactly one
finite factor to the automorphism group, $\mathrm{Aut}(\mathbb{S}) \cong G_2 \times S_3$, and
the generations are its orbit: three of them, a family label and never a fourth force
(Section~\ref{sec:sedenions-generations}).
""")

OLD_CHI = r"""
\item \textbf{Chirality.} Handedness enters at the register, not through the algebra's
multiplication. Each Bloch sphere's coordinate frame carries a handedness, and the Filatov
representation forces opposite handedness on an entangled pair \autocite{filatov2024towards}; on
three spheres the pairwise constraints cannot all hold, since $K_3$ is not two-colourable, and
the eight handedness assignments fall into three chiral classes and one a-chiral class. In each
chiral class the pair left frustrated has two resolutions, and those are the weak-isospin
doublet: the weak force is the switch between them, so it acts on one handedness only,
left-handed doublets and right-handed singlets, while the a-chiral class, having no
opposite-handed pair, is blind to it (Section~\ref{sec:generations}). Which handedness the
doublet takes is not yet derived (Open Problem~\ref{op:chirality}), and the three-qubit
extension of Filatov's result is the assumption the count rests on (Open
Problem~\ref{op:filatov-extension}).
"""
NEW_CHI = fill(r"""
\item \textbf{Chirality.} Handedness enters at the register: entangled spheres must carry
opposite handedness, three cannot all comply, and the weak force is the switch between the two
ways of resolving the frustrated pair, which is why it sees one handedness only
(Section~\ref{sec:generations}; which handedness, Open Problem~\ref{op:chirality}).
""")


def main():
    with open(MAIN, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (MAIN, HEADER.strip()))
    text = replace_once(text, OLD_GEN, NEW_GEN)
    text = replace_once(text, OLD_CHI, NEW_CHI)
    for lab in (r"\ref{sec:sedenions-generations}", r"\ref{sec:generations}", r"\ref{op:chirality}"):
        if lab not in text:
            sys.exit("REFUSING: %s missing after the edit" % lab)
    shutil.copy(MAIN, MAIN + "." + STAMP + ".bak")
    with open(MAIN, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak)" % (MAIN, MAIN, STAMP))


if __name__ == "__main__":
    main()
