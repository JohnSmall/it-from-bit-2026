#!/usr/bin/env python3
"""Replace two pre-sedenion fossils in the headline list, and re-point the zoo's
"deeper reason" paragraph to match.

JS, 2026-09-12: main.tex's headline items "Three generations" (Spin(8) triality permuting
the three octonionic representations) and "Chirality" (non-associativity distinguishing left
and right multiplication) predate the sedenion section and carry the marker "wrong! to be
fixed with sedenions". Reworded in the paper's current terms, taken from
sedenions_generations_section_2026-08-27.tex (Aut(S) = G_2 x S_3, the psi-orbit of the three
octonion halvings, flavour-not-force) and particle_zoo_section_2026-06-08.tex (Filatov
handedness at the register, the K_3 obstruction, the frustrated pair as the weak doublet, the
a-chiral sterile class, op:chirality, op:filatov-extension).

The same fossil survives at length in the particle zoo's paragraph "There is a deeper reason
for the number three", which still calls the three Fano lines through the preferred direction
"the three generations" while sec:sedenions-promotion says they "are the three colour lines
of C^3 and not three generations". The paragraph is re-pointed so the paper agrees with
itself.

Two files, one header each, one run only.

paper1/main.tex
  1. The "Three generations" item: Brown's direct product, the S_3 on the three halvings,
     three / family-not-force / no fifth rung, the register count as the shadow.
  2. The "Chirality" item: handedness at the register, Filatov, K_3, the frustrated pair as
     the doublet, the a-chiral class, the two open problems.
paper1/particle_zoo_section_2026-06-08.tex
  3. The "deeper reason" paragraph: triality kept as the observation it is, the three lines
     named as colour with the sedenion section cited, the generation three located one rung
     up, the corroboration sentence kept.

Every anchor is matched whitespace-insensitively and must match exactly once; replacements
are pre-filled to 96 columns. A dated .bak is written per file, a "% EDITED" header is
prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-12"
STAMP = "2026-09-12T1345"
SCRIPT = "scripts/patch_sedenion_fossils_headline_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

MAIN = "paper1/main.tex"
ZOO = "paper1/particle_zoo_section_2026-06-08.tex"


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
OLD_GEN = r"""
\item \textbf{Three generations.} The triality automorphism of $\mathrm{Spin}(8)$, which
permutes the three eight-dimensional representations of the octonions, produces exactly three
generations of fermions. \textbf{wrong! to be fixed with sedenions}
"""
NEW_GEN = fill(r"""
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
""")

OLD_CHI = r"""
\item \textbf{Chirality.} The non-associativity of $\mathbb{O}$ distinguishes left and right
multiplication, breaking parity at the algebraic level.
  \textbf{wrong! to be fixed with sedenions}
"""
NEW_CHI = fill(r"""
\item \textbf{Chirality.} Handedness enters at the register, not through the algebra's
multiplication. Each Bloch sphere's coordinate frame carries a handedness, and the Filatov
representation forces opposite handedness on an entangled pair \autocite{filatov2024towards};
on three spheres the pairwise constraints cannot all hold, since $K_3$ is not two-colourable,
and the eight handedness assignments fall into three chiral classes and one a-chiral class. In
each chiral class the pair left frustrated has two resolutions, and those are the weak-isospin
doublet: the weak force is the switch between them, so it acts on one handedness only,
left-handed doublets and right-handed singlets, while the a-chiral class, having no
opposite-handed pair, is blind to it (Section~\ref{sec:generations}). Which handedness the
doublet takes is not yet derived (Open Problem~\ref{op:chirality}), and the three-qubit
extension of Filatov's result is the assumption the count rests on (Open
Problem~\ref{op:filatov-extension}).
""")

# ---------------------------------------------------------------- particle zoo
OLD_ZOO = r"""
There is a deeper reason for the number three, beyond the combinatorial count, and it is worth
giving because it shows the count is not an artefact of the $K_3$ device. The three-qubit state
space carries the triality of $\mathrm{Spin}(8)$, which permutes the vector and the two spinor
representations $\mathbf{8}_v, \mathbf{8}_s, \mathbf{8}_c$ \autocite{baez2002octonions}. Fixing the
preferred complex direction breaks the triality and singles out the three Fano lines through that
direction --- the lines $(1,2,3)$, $(1,4,5)$ and $(1,7,6)$ of the multiplication table fixed in
Appendix~\ref{app:setup} --- each a quaternionic subalgebra; these are the three generations.
Triality gives three; the $K_3$ obstruction refines this to three-plus-one by adding the
unfrustrated class. The same count of three generations is reached independently from the complex
sedenions and from chains of division-algebra ideals \autocite{gillardgresnigt2019three,furey2018three},
a convergence we read as corroboration rather than as part of the present derivation.
"""
NEW_ZOO = fill(r"""
There is a deeper reason for the number three, beyond the combinatorial count, though not the
one an earlier draft gave here. The three-qubit state space carries the triality of
$\mathrm{Spin}(8)$, which permutes the vector and the two spinor representations $\mathbf{8}_v,
\mathbf{8}_s, \mathbf{8}_c$ \autocite{baez2002octonions}. Fixing the preferred complex direction
breaks the triality and singles out the three Fano lines through that direction --- the lines
$(1,2,3)$, $(1,4,5)$ and $(1,7,6)$ of the multiplication table fixed in
Appendix~\ref{app:setup} --- each a quaternionic subalgebra. Those three lines are the three
colour lines of $\mathbb{C}^3$, not three generations (\S\ref{sec:sedenions-promotion}):
triality is not induced by any automorphism of the octonions, and the generation three comes
one rung up, from the $S_3$ that the doubling to the sedenions adds to the automorphism group,
acting on the three octonion halvings (\S\ref{sec:sedenions-generations}), of which the count
here is read as the shadow (\S\ref{sec:sedenions-shadow}). The same count of three is reached
independently from the complex sedenions and from chains of division-algebra ideals
\autocite{gillardgresnigt2019three,furey2018three}, a convergence we read as corroboration
rather than as part of the present derivation.
""")


def patch(path, edits, labels):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (path, HEADER.strip()))
    for old, new in edits:
        text = replace_once(text, old, new)
    for lab in labels:
        if lab not in text:
            sys.exit("REFUSING: %s does not contain %s after the edit" % (path, lab))
    if "wrong! to be fixed" in text and path == MAIN:
        sys.exit("REFUSING: a 'wrong! to be fixed' marker survives in %s" % path)
    shutil.copy(path, path + "." + STAMP + ".bak")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak)" % (path, path, STAMP))


def main():
    patch(MAIN, [(OLD_GEN, NEW_GEN), (OLD_CHI, NEW_CHI)],
          [r"\ref{sec:sedenions-generations}", r"\ref{op:chirality}", r"\ref{op:filatov-extension}"])
    patch(ZOO, [(OLD_ZOO, NEW_ZOO)],
          [r"\ref{sec:sedenions-promotion}", r"\ref{sec:sedenions-shadow}"])


if __name__ == "__main__":
    main()
