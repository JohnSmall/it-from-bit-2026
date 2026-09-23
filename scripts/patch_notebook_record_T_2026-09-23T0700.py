#!/usr/bin/env python3
"""patch_notebook_record_T_2026-09-23T0700.py

Paper 1, appendix_notebook_record_2026-07-11.tex: add the entry for notebook T
(trigintaduonion automorphisms, 2026-08-27, re-run 2026-09-23). The sedenion
section and the Wigner's-friend section both say "the fifth and sixth rungs are
checked directly in the notebook record (Appendix app:notebook-record)", and the
appendix had no such entry. JS, 2026-09-23: "update any tex file that needs to
be updated with this information." Written in the appendix's fixed template
(Provenance, Claim, Design, Verified outputs, Hardware record, Status,
Consistency) from notebooks/notebook_T_trigintaduonion_automorphisms_2026-08-27.md
and the two captured runs. Appended after the last entry (Notebook O).

Sentinel-gated: anchor (the file's final sentence) matches exactly once,
.bak written, "% EDITED" header added, refuses to run twice.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-23"
SCRIPT = Path(__file__).name
STAMP = "2026-09-23T0700"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/appendices/appendix_notebook_record_2026-07-11.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


ANCHOR = (r"op:associator-geodesic. The $K_{3}$ bridge to the generations gives the obstruction independent "
          r"standing in the $K_{3}$-versus-$S_{3}$ decision.")
ENTRY = r"""

\subsection{Notebook T: trigintaduonion automorphisms --- the fifth rung}
\label{app:nb-T}

\emph{Provenance.} \texttt{notebook\_T\_trigintaduonion\_automorphisms\_2026-08-27} (.py, with a
markdown record and a captured run); created 27 August 2026 in the sedenion session that
corrected the generation mechanism; pure numpy, no circuit, no hardware content and none owed.
Re-run unchanged on 23 September 2026 (Python 3.10.12, numpy 1.21.5, three minutes eleven
seconds): the captured output is byte-identical to the original and is retained beside it. It
settles the ledger item ``extend the Cayley--Dickson constructor to the trigintaduonions to decide
the $\mathbb{Z}/2$-versus-$S_{3}$ branch by construction'', closed 23 September 2026.

\emph{Claim.} The automorphism increment of the Cayley--Dickson tower beyond the octonions, which
\S\ref{sec:generations} and \S\ref{sec:wigners-friend} use in the form ``each further doubling
adds exactly one finite $S_{3}$ and no continuous symmetry, ever''. Three parts. Part A, the
branch: Brown's doubling involution $\epsilon(a + bu) = a - bu$ and his order-three map
$\psi(a + bu) = [a + 3a^{*} + \sqrt3(b - b^{*})]/4 + [b + 3b^{*} - \sqrt3(a - a^{*})]/4\,u$ are
exact algebra automorphisms of $A_{n}$ at rungs $n = 3, 4, 5, 6$; $\psi^{3} = 1$,
$\epsilon^{2} = 1$, $\epsilon\psi = \psi^{2}\epsilon$, so they generate $S_{3}$; $\psi$ mixes the
two halves and is not a lift; the new $S_{3}$ at rung $n$ commutes with the lifted $S_{3}$ from
rung $n - 1$ and the lifted $\psi$ is a distinct element, a direct product; and the derivation
algebra, the Lie algebra of the identity component, has dimension $0, 3, 14, 14, 14$ at
$n = 1, \dots, 5$. Over $\mathbb{R}$ the Eakin--Sathaye branch is therefore $S_{3}$ at every rung
from the fourth, the $\mathbb{Z}/2$ branch being the general-field case in which $\psi$'s
$\sqrt3$ is unavailable, and the identity component is $\mathfrak{g}_{2}$ from the octonions
onward: the fifth rung is repetitive, not silent. Part B, the two triples: Brown's $S_{3}$
stabilises the quaternionic core and each of the three octonion copies through it setwise; the
map that cycles those copies is a lifted $G_{2}$ element, the colour-line three-cycle, fixing the
core pointwise; so the core triple is colour structure one rung up. Part C, the triple $\psi$ does
permute: the three octonion halvings $\mathbb{O}, \psi\mathbb{O}, \psi^{2}\mathbb{O}$ of the
sedenions, pairwise and triply intersecting in $\mathbb{R}$, each regenerating the sedenions with
the fixed doubling unit, and each fixed pointwise by one of the three involutions
$\epsilon\psi^{k}$; the doubling's $S_{3}$ permutes the halvings, at relative orientations
$0$, $120$ and $240$ degrees, which is the generation triple of \S\ref{sec:generations}.

\emph{Design.} The corpus recursion $(a,b)(c,d) = (ac - \bar d b,\ da + b\bar c)$ with
$\overline{(a,b)} = (\bar a, -b)$ on $\mathbb{R}^{2^{n}}$, the doubling unit of rung $n$ at index
$2^{n-1}$; automorphism checks on every pair of basis units (up to $64 \times 64$ at rung six);
derivations by the eigenvalue count of the normal matrix of the Leibniz system; subspace
statements by rank and by stacked orthogonal complements. Tolerance $10^{-10}$.

\emph{Verified outputs.} Every Part A, B and C check returns true at both runs, worst
automorphism residual $1.1 \times 10^{-16}$; $\dim\mathrm{Der}(A_{n}) = 0, 3, 14, 14, 14$;
$\mathrm{Fix}(\psi_{4}) = \mathrm{span}\{e_{0}, e_{8}\}$ of dimension two; the halvings' pairwise
and triple intersections of dimension one; final line \texttt{NOTEBOOK T: PASS}.

\emph{Hardware record.} Numerics only.

\emph{Status.} Part A confirms external results by computation: Brown's equality
$\mathrm{Aut}(A_{n-1}) \times S_{3} = \mathrm{Aut}(A_{n})$ for $n = 4, 5, 6$ is cited, not
computed, the notebook verifying the inclusion, the direct-product structure and the derivation
count \autocite{brown1967generalized,eakinsathaye1990automorphisms,schafer1954cayleydickson}.
Parts B and C are exact algebra, machine-verified. The physical identifications riding on Part C,
generation as the discrete orientation of the link against its copy and the repeated higher-rung
factor as what the redundancy ladder consumes, are CANDIDATE and RHYME respectively, flagged
where used.

\emph{Consistency.} Part B is the reason the corpus's earlier reading of the core triple as the
generations was retired: the copies are cycled inside $G_{2}$, the Klein grading of notebook M is
the colour grading, and the correct generation triple is the halvings. Notebook M's structural
results stand as colour-side statements; the generation-side scan on the $\psi$-orbit is owed
before M's maximal-mixing verdict and notebook N's pre-registered dressing hypothesis carry over.
The direct product is the structural reason for the untriplicated gauge sector, consonant with
the Gresnigt line's later construction of the generations as the $\psi$-orbit. The no-new-force
statement of \S\ref{sec:generations} and the fifth-wire passage of \S\ref{sec:wigners-friend}
rest on Part A and its two runs."""


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    hits = list(re.finditer(ws(ANCHOR), text))
    if len(hits) != 1:
        sys.exit("anchor matched %d times" % len(hits))
    m = hits[0]
    new = text[: m.end()] + ENTRY + text[m.end():]
    if "label{app:nb-T}" not in new or new.count("NOTEBOOK T: PASS") != 1:
        sys.exit("post-check failed")
    print("verified: %s (1 entry appended)" % TARGET.relative_to(ROOT))
    if CHECK:
        print("--check: nothing written"); return
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s)" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
