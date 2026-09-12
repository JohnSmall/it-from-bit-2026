#!/usr/bin/env python3
"""Credit Brannen 2006 for the Koide phase as a number and for the complex half of the
Gram/Bargmann reading.

JS noted on 2026-09-12 that brannen2006lepton was in references.bib but uncited. The note
(https://brannenworks.com/MASSES2.pdf, dated 2 May 2006) was read in full before this patch:
eqs. (3)-(4) give the circulant form with unit diagonal, off-diagonal entries eta e^{+-i delta}
and eigenvalues mu(1 + 2 eta cos(delta + 2 n pi/3)); eqs. (7)-(9) make eta^2 = 1/2 the Koide
relation; eq. (14) fits delta_1 = 0.2222220(19) and the text says "delta_1 is close to 2/9, a
fact that went unnoticed until this author discovered it in 2005"; Sections IV-V build the
circulant from three Pauli-algebra projectors with T = sqrt((1 + cos theta)/2) their overlap
and phi "half the (oriented) area of the spherical triangle" as the phase of RGB, put T =
sqrt(1/2) and phi = 3 delta to recover the mass formula, and footnote 4 says that in the Pauli
algebra T = sqrt(1/2) forces phi = +-pi/4, incompatible with the data, so a larger algebra
is needed.

One file, one header, one run only.

paper1/masses_section_2026-06-08.tex
  1. The sentence introducing delta = 2/9 credits the coincidence to Brannen, with the
     circulant form, eta^2 = 1/2, the fitted value and the observation.
  2. The reading paragraph after prop:koide-jordan credits the complex half of the
     Gram/Bargmann reading to his Sections IV-V and names the pi/4 bound as the general
     form of his footnote.

Anchors are matched whitespace-insensitively and must match exactly once; the paragraphs
holding the edits are re-filled to 96 columns. A dated .bak is written, a "% EDITED"
header is prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-12"
STAMP = "2026-09-12T1330"
SCRIPT = "scripts/patch_koide_brannen_credit_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

MASSES = "paper1/masses_section_2026-06-08.tex"


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


def refill_paragraph_at(text, marker):
    i = text.index(marker)
    start = text.rfind("\n\n", 0, i) + 2
    end = text.find("\n\n", i)
    para = text[start:end]
    for line in para.splitlines():
        if line.lstrip().startswith(("\\begin", "\\end", "\\item", "%", "\\subsection",
                                     "\\section", "\\label")):
            sys.exit("REFUSING: paragraph to re-fill contains structure:\n  %s" % line)
    return text[:start] + fill(para) + text[end:]


# 1. the delta = 2/9 sentence
OLD_DELTA = r"""
the doubling norm. The phase is $\delta = 2/9$ in radians, the value that the measured masses
require, matched to five significant figures and carrying a natural geometric reading as
"""
NEW_DELTA = r"""
the doubling norm. The phase is $\delta = 2/9$ in radians, the value that the measured masses
require. The coincidence is Brannen's: his 2006 note writes the square-root masses as the
eigenvalues of a circulant matrix with unit diagonal and off-diagonal entries $\eta e^{\pm
i\delta}$, so that $\eta^2 = \tfrac12$ is the Koide relation, fits $\delta = 0.2222220$ to the
masses of the day, and records that it is close to $2/9$ \autocite{brannen2006lepton}. It is now
matched to five significant figures and carries a natural geometric reading as
""".strip()

# 2. the end of the reading paragraph
OLD_READ_END = r"""
$\operatorname{tr}X^2/(\operatorname{tr}X)^2$. We have no mechanism that makes a phase equal a
trace ratio and record the equality as a rhyme.
"""
NEW_READ_END = r"""
$\operatorname{tr}X^2/(\operatorname{tr}X)^2$. We have no mechanism that makes a phase equal a
trace ratio and record the equality as a rhyme. The complex half of this reading is also
Brannen's \autocite{brannen2006lepton}: in the same note he builds the circulant from three
projectors of the Pauli algebra, reads the off-diagonal norm as their overlap and $3\delta$ as
half the oriented area of the spherical triangle they span, and observes that an overlap of
$1/\sqrt2$ then forces the phase to $\pi/4$, incompatible with the data, so that a larger
algebra is needed. Proposition~\ref{prop:koide-jordan} names the algebra, and the bound
$|\Phi| \le \pi/4$ is the general form of his observation.
""".strip()


def main():
    with open(MASSES, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        sys.exit("REFUSING: %s already carries the header %r" % (MASSES, HEADER.strip()))
    text = replace_once(text, OLD_DELTA, NEW_DELTA)
    text = refill_paragraph_at(text, "The coincidence is Brannen's")
    text = replace_once(text, OLD_READ_END, NEW_READ_END)
    text = refill_paragraph_at(text, "The complex half of this reading")
    if text.count("brannen2006lepton") != 2:
        sys.exit("REFUSING: brannen2006lepton cited %d times, expected 2" % text.count("brannen2006lepton"))
    shutil.copy(MASSES, MASSES + "." + STAMP + ".bak")
    with open(MASSES, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak): brannen2006lepton cited twice" % (MASSES, MASSES, STAMP))


if __name__ == "__main__":
    main()
