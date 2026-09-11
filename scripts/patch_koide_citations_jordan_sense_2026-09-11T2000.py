#!/usr/bin/env python3
"""Citations for the Bargmann-invariant material, and "eigenvalues in the Jordan sense".

Companion to bib/koide_bargmann_jordan_refs_2026-09-11T2000.ris (written to ris/, since
renamed bib/), whose eight ID-field keys are cited below, and to
knowledge/sessions/koide_flat_direction_2026-09-11T1900.md. The keys were expected to
exist in references.bib after the RIS batch was imported into Zotero and the .bib
re-exported by Better BibTeX. They did not: Zotero's RIS importer discards the ID, so
BBT generated formula keys and patch_koide_citation_keys_bbt_2026-09-11T2100.py
re-points the citations. Reference batches are .bib from now on (bib/README.md).

One file, one header, one run only.

paper1/masses_section_2026-06-08.tex, all inside sec:koide-gap as spliced on
2026-09-11T1930:
  1. prop:koide-jordan: "the eigenvalues of X" becomes "the eigenvalues of X in the
     Jordan sense --- the roots of its characteristic cubic, which are the
     coefficients of its decomposition into orthogonal primitive idempotents", with
     springerveldkamp2000octonions and draymanogue1999eigenvalue. For octonionic
     Hermitian matrices the naive eigenvalue equation has solutions outside the
     cubic's roots, so the sense has to be said.
  2. The proof cites springerveldkamp2000octonions for the bracketing-independence
     of the real part of a triple product.
  3. The reading paragraph cites woottersfields1989unbiased and durt2010unbiased for
     "mutually unbiased", bargmann1964wigner for the invariant, and
     pancharatnam1956interference with mukundasimon1993kinematic for its reading as
     the geometric phase of the geodesic triangle (one clause added).
  4. The transcendence paragraph cites baker1975transcendental, ch. 1, for
     Lindemann--Weierstrass.

Every anchor is the whole paragraph or environment body it replaces, matched
whitespace-insensitively and required to match exactly once; replacements are
pre-filled to 96 columns. A dated .bak is written, a "% EDITED" header is prepended,
and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-11"
STAMP = "2026-09-11T2000"
SCRIPT = "scripts/patch_koide_citations_jordan_sense_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

MASSES = "paper1/masses_section_2026-06-08.tex"
KEYS = ["bargmann1964wigner", "mukundasimon1993kinematic", "pancharatnam1956interference",
        "woottersfields1989unbiased", "durt2010unbiased", "baker1975transcendental",
        "springerveldkamp2000octonions", "draymanogue1999eigenvalue"]


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


# 1. proposition body
OLD_PROP = r"""
Let $X \in J_3(\mathbb{O})$ have unit diagonal and off-diagonal entries $x_1, x_2, x_3$ of a
common norm $\rho$, and write $x_i = \rho u_i$ with $u_i$ unit octonions and
$\operatorname{Re}(u_1u_2u_3) = \cos\Phi$. Then the eigenvalues of $X$ are $1 +
2\rho\cos\bigl((\Phi + 2\pi k)/3\bigr)$, $k = 0, 1, 2$: the form~\eqref{eq:z3} with $\alpha =
2\rho$ and $3\delta = \Phi$. The phase is well defined although the octonions are not
associative, and for $\rho = 1/\sqrt2$ it satisfies $|\Phi| \le \pi/4$, with equality exactly
when one eigenvalue vanishes.
"""
NEW_PROP = fill(r"""
Let $X \in J_3(\mathbb{O})$ have unit diagonal and off-diagonal entries $x_1, x_2, x_3$ of a
common norm $\rho$, and write $x_i = \rho u_i$ with $u_i$ unit octonions and
$\operatorname{Re}(u_1u_2u_3) = \cos\Phi$. Then the eigenvalues of $X$ in the Jordan sense ---
the roots of its characteristic cubic, which are the coefficients of its decomposition into
orthogonal primitive idempotents \autocite{springerveldkamp2000octonions,draymanogue1999eigenvalue}
--- are $1 + 2\rho\cos\bigl((\Phi + 2\pi k)/3\bigr)$, $k = 0, 1, 2$: the form~\eqref{eq:z3}
with $\alpha = 2\rho$ and $3\delta = \Phi$. The phase is well defined although the octonions
are not associative, and for $\rho = 1/\sqrt2$ it satisfies $|\Phi| \le \pi/4$, with equality
exactly when one eigenvalue vanishes.
""")

# 2. proof body
OLD_PROOF = r"""
The characteristic cubic of $X$ is $\lambda^3 - (\operatorname{tr}X)\lambda^2 + S(X)\lambda -
N(X)$ with $\operatorname{tr}X = 3$, $S(X) = 3 - 3\rho^2$ and cubic norm $N(X) = 1 - 3\rho^2 +
2\rho^3\cos\Phi$ \autocite{baez2002octonions}. Substituting $\lambda = 1 + 2\rho c$ reduces it
to $4c^3 - 3c = \cos\Phi$, whose roots are $c = \cos\bigl((\Phi + 2\pi k)/3\bigr)$. The real
part of a triple product is the same for either bracketing in any composition algebra, which is
what makes $\Phi$ well defined. For $\rho = 1/\sqrt2$ the smallest eigenvalue is $1 +
\sqrt2\cos\bigl((|\Phi| + 2\pi)/3\bigr)$, which is non-negative exactly when $|\Phi| \le \pi/4$.
"""
NEW_PROOF = fill(r"""
The characteristic cubic of $X$ is $\lambda^3 - (\operatorname{tr}X)\lambda^2 + S(X)\lambda -
N(X)$ with $\operatorname{tr}X = 3$, $S(X) = 3 - 3\rho^2$ and cubic norm $N(X) = 1 - 3\rho^2 +
2\rho^3\cos\Phi$ \autocite{baez2002octonions}. Substituting $\lambda = 1 + 2\rho c$ reduces it
to $4c^3 - 3c = \cos\Phi$, whose roots are $c = \cos\bigl((\Phi + 2\pi k)/3\bigr)$. The real
part of a triple product is the same for either bracketing in any composition algebra
\autocite{springerveldkamp2000octonions}, which is what makes $\Phi$ well defined. For $\rho =
1/\sqrt2$ the smallest eigenvalue is $1 + \sqrt2\cos\bigl((|\Phi| + 2\pi)/3\bigr)$, which is
non-negative exactly when $|\Phi| \le \pi/4$.
""")

# 3. reading paragraph
OLD_READ = r"""
The proposition says what the two numbers are inside the framework's own construction. The
amplitude $\alpha = \sqrt2$ is the statement that the off-diagonal entries have squared norm one
half; read through the Gram matrix of three generation states, whose entries are the overlaps
$\langle\psi_j|\psi_k\rangle$, it says that each pair is mutually unbiased,
$|\langle\psi_j|\psi_k\rangle|^2 = \tfrac12$, and the Koide ratio then follows exactly as in
Proposition~\ref{prop:koide}. The phase is the Bargmann invariant of the triple, the argument of
the cyclic product of the three overlaps, which is the one continuous invariant three states
possess beyond their overlaps; its octonionic form is the real part of the cyclic product of the
three off-diagonal units. The measured $3\delta = 0.6667$ sits at $0.85$ of the positivity bound
$\pi/4$, and to first order the electron's square-root mass is one third of the shortfall,
$\sqrt{m_e}/M \simeq (\pi/4 - 3\delta)/3$, accurate to two per cent. So the question ``why
$2/9$'' is, precisely, ``why does the cyclic product of the three off-diagonal units have real
part $\cos(2/3)$''. The number to derive is the $\mathbb{Z}_3$-invariant $3\delta = 2/3$, and it
is worth recording that this is also the value of the Koide ratio: the invariant phase, in
radians, equals $\operatorname{tr}X^2/(\operatorname{tr}X)^2$. We have no mechanism that makes a
phase equal a trace ratio and record the equality as a rhyme.
"""
NEW_READ = fill(r"""
The proposition says what the two numbers are inside the framework's own construction. The
amplitude $\alpha = \sqrt2$ is the statement that the off-diagonal entries have squared norm one
half; read through the Gram matrix of three generation states, whose entries are the overlaps
$\langle\psi_j|\psi_k\rangle$, it says that each pair is mutually unbiased,
$|\langle\psi_j|\psi_k\rangle|^2 = \tfrac12$ \autocite{woottersfields1989unbiased,durt2010unbiased},
and the Koide ratio then follows exactly as in Proposition~\ref{prop:koide}. The phase is the
Bargmann invariant of the triple \autocite{bargmann1964wigner}, the argument of the cyclic
product of the three overlaps, which is the one continuous invariant three states possess
beyond their overlaps and is the geometric phase of the geodesic triangle through them
\autocite{pancharatnam1956interference,mukundasimon1993kinematic}; its octonionic form is the
real part of the cyclic product of the three off-diagonal units. The measured $3\delta = 0.6667$
sits at $0.85$ of the positivity bound $\pi/4$, and to first order the electron's square-root
mass is one third of the shortfall, $\sqrt{m_e}/M \simeq (\pi/4 - 3\delta)/3$, accurate to two
per cent. So the question ``why $2/9$'' is, precisely, ``why does the cyclic product of the
three off-diagonal units have real part $\cos(2/3)$''. The number to derive is the
$\mathbb{Z}_3$-invariant $3\delta = 2/3$, and it is worth recording that this is also the value
of the Koide ratio: the invariant phase, in radians, equals
$\operatorname{tr}X^2/(\operatorname{tr}X)^2$. We have no mechanism that makes a phase equal a
trace ratio and record the equality as a rhyme.
""")

# 4. transcendence paragraph: one sentence
OLD_LW = r"""
What kind of number it must be. If $\delta = 2/9$ exactly then $e^{i\delta}$ is transcendental,
by the Lindemann--Weierstrass theorem: $e^{a}$ is transcendental for every non-zero algebraic
$a$. The consequences are sharp.
"""
NEW_LW = r"""
What kind of number it must be. If $\delta = 2/9$ exactly then $e^{i\delta}$ is transcendental,
by the Lindemann--Weierstrass theorem \autocite[ch.~1]{baker1975transcendental}: $e^{a}$ is
transcendental for every non-zero algebraic $a$. The consequences are sharp.
""".strip()


def refill_paragraph_at(text, marker):
    """Re-fill the blank-line-delimited prose paragraph containing `marker`."""
    i = text.index(marker)
    start = text.rfind("\n\n", 0, i) + 2
    end = text.find("\n\n", i)
    para = text[start:end]
    for line in para.splitlines():
        if line.lstrip().startswith(("\\begin", "\\end", "\\item", "%", "\\subsection",
                                     "\\section", "\\label")):
            sys.exit("REFUSING: paragraph to re-fill contains structure:\n  %s" % line)
    return text[:start] + fill(para) + text[end:]


def main():
    with open(MASSES, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (MASSES, HEADER.strip()))
    text = replace_once(text, OLD_PROP, NEW_PROP)
    text = replace_once(text, OLD_PROOF, NEW_PROOF)
    text = replace_once(text, OLD_READ, NEW_READ)
    text = replace_once(text, OLD_LW, NEW_LW)
    text = refill_paragraph_at(text, r"\autocite[ch.~1]{baker1975transcendental}")
    for k in KEYS:
        if text.count(k) < 1:
            sys.exit("REFUSING: key %s not cited after the edit" % k)
    shutil.copy(MASSES, MASSES + "." + STAMP + ".bak")
    with open(MASSES, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak); %d keys cited, bib not yet re-exported: do not build"
          % (MASSES, MASSES, STAMP, len(KEYS)))


if __name__ == "__main__":
    main()
