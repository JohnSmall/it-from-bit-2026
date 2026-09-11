#!/usr/bin/env python3
"""The Koide phase: state the gap in full, and make the parameter count consistent.

Companion to knowledge/sessions/koide_delta_gap_2026-09-11T1600.md and the script
koide_delta_fit_and_angle_scan_2026-09-11T1600.py, whose numbers are quoted below.

Four files, one header each, one run only.

paper1/masses_section_2026-06-08.tex
  1. op:koide-delta gains the measured band as its PASS criterion and lists the
     three closed routes (sin^4 holonomy; notebook M's angle inventory, app:nb-M;
     the norm-defect identity, a magnitude). First sentence unchanged.
  2. A new \\subsection{The shape of the gap} (label sec:koide-gap) after the
     open problem: what the data fix, why the norm defect cannot fix a phase, what
     is excluded, and why a rational number of radians shapes any derivation.
  3. "the two theoretically fixed numbers alpha and delta" contradicted "matched"
     two lines later; now "alpha, which the theory fixes, and delta, which it
     matches", and "no free" becomes "no fitted".

paper1/headline_results_snippet_2026-07-07.tex, predictions_section_2026-06-13.tex,
paper1/summary_section_2026-07-07.tex
  4. "zero adjustable / zero dimensionless parameters" becomes "no fitted
     dimensionless parameters" with the matched Koide phase named, so the headline
     count agrees with the masses section's own "one genuine gap".
  5. "the Koide relation ... to about a tenth of a per cent" (predictions,
     summary) was loose by a factor of ten against the masses table (0.01%); now
     "to a hundredth of a per cent", with "matched phase" said.

Every anchor is matched whitespace-insensitively and must match exactly once. The
paragraph around each sentence-level edit is re-filled to 96 columns (breaks only at
spaces, never inside a word). A .bak is written per file, a "% EDITED" header is
prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-11"
SCRIPT = "scripts/patch_koide_gap_and_parameter_count_2026-09-11T1700.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

MASSES = "paper1/masses_section_2026-06-08.tex"
HEADLINE = "paper1/headline_results_snippet_2026-07-07.tex"
PRED = "paper1/predictions_section_2026-06-13.tex"
SUMM = "paper1/summary_section_2026-07-07.tex"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def fill(s):
    return textwrap.fill(" ".join(s.split()), width=WIDTH,
                         break_long_words=False, break_on_hyphens=False)


def replace_once(text, anchor, replacement, reflow=True):
    pat = re.compile(ws(anchor))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1:\n  %s" % (n, anchor[:70]))
    m = pat.search(text)
    text = text[:m.start()] + replacement + text[m.end():]
    if not reflow:
        return text
    # Re-fill the paragraph (blank-line delimited) that now holds the replacement.
    i = text.index(replacement)
    start = text.rfind("\n\n", 0, i) + 2
    end = text.find("\n\n", i)
    para = text[start:end]
    for line in para.splitlines():
        if line.lstrip().startswith(("\\begin", "\\end", "\\item", "%", "\\subsection",
                                     "\\section", "\\label")):
            sys.exit("REFUSING: paragraph to re-fill contains structure:\n  %s" % line)
    return text[:start] + fill(para) + text[end:]


def check_widths(block):
    for line in block.splitlines():
        if len(line) > WIDTH:
            sys.exit("REFUSING: inserted line exceeds %d columns:\n  %s" % (WIDTH, line))


# ---------------------------------------------------------------- masses section

OP_OLD = r"""Derive $\delta = 2/9$ from the holonomy of the octonionic Hopf connection. This is the single most
important open calculation in the mass sector. One route is already closed: the simplest
holonomy-squared model, $m_k \propto \sin^4(\theta_0 + 2\pi k/3)$, does not reproduce the spectrum
and is recorded as tried and failed."""

OP_NEW = r"""Derive $\delta = 2/9$ from the holonomy of the octonionic Hopf connection. This is the single most
important open calculation in the mass sector. A derivation passes if it lands inside the
measured band, $\delta = 0.222225 \pm 0.000006$ radians, with no fitted input
(\S\ref{sec:koide-gap}). Three routes are closed: the simplest holonomy-squared model,
$m_k \propto \sin^4(\theta_0 + 2\pi k/3)$, does not reproduce the spectrum; the structural
angles of the bare sedenion triple contain no $2/9$ (Appendix~\ref{app:nb-M}); and the
norm-defect identity~\eqref{eq:debt-defect}, being a magnitude, cannot fix a phase."""

QUARKS_HEAD = r"\subsection{Quarks: the colour correction}"

GAP = r"""\subsection{The shape of the gap}
\label{sec:koide-gap}

Since the phase is the one number in the charged-lepton sector that the framework matches rather
than derives, it is worth being exact about what kind of gap it is, what has been tried, and what
a derivation would have to look like. A well-posed gap is an invitation; a vague one is a hole.

What the data fix. Inverting the triality form~\eqref{eq:z3} on the three measured masses is
exact --- three masses, three parameters --- and with the PDG uncertainties propagated it returns
$\alpha = 1.41421 \pm 0.00001$, within half a standard deviation of $\sqrt2$, and
$\delta = 0.222225 \pm 0.000006$ radians, within half a standard deviation of $2/9 = 0.222222$.
The band is set almost entirely by the tau mass and fixes between four and five significant
figures of $\delta$; any candidate derivation is tested against that band and nothing looser.

Why the norm defect does not close it. The identity~\eqref{eq:debt-defect} is quartic in the
magnitudes: it says how badly the norm of a product fails to factorise and bounds the failure by
the coassociative calibration. Everything it can fix is a size --- the existence of mass, the
scale of the debt, the amplitude $\alpha$, which is itself a norm. The phase $\delta$ is not a
size but an orientation, the angle of the $\mathbb{Z}_3$ triality frame against the preferred
complex structure, and a magnitude identity has no handle on an orientation. That is the content
of the sentence that closes the bridge above: the identity fixes the object, not the spectrum. The
division of labour --- existence from the associator, ratios from the frame --- holds at the
sedenion rung exactly as at the octonion rung, and the elegance of the norm defect as an account
of mass does not carry over to the phase.

What is already excluded. Three routes are closed. The simplest holonomy-squared model fails
(Open Problem~\ref{op:koide-delta}). The bare sedenion geometry was inventoried in the up-quark
investigation (Appendix~\ref{app:nb-M}): an eighteen-comparison scan of the structural angles of
the sedenion triple --- twelve identically zero, four at exactly $\pi/4$, two ratios at exactly
$\tfrac14$ --- contains no occurrence of $2/9$. That scan was run against the up-quark leakage
angle, but it is the same number and the same geometry, and it closes the frame-orientation route
for the Koide phase as well. And the associator has a uniform magnitude on every bracketing not
forced to vanish, by $G_2$-transitivity, so no choice of octonionic direction can supply the
number either.

The shape any derivation must take. The number $2/9$ is a rational number of \emph{radians}, and
that is an unusual thing for a geometric angle to be. An angle fixed by a discrete symmetry is a
rational multiple of $\pi$; the inventory's $\pi/4$ is what such angles look like. An angle
between two vectors is an inverse trigonometric function of an algebraic number. A holonomy on a
round sphere around a loop singled out by symmetry is a rational fraction of $4\pi$, and a loop
not singled out by symmetry is a fitted input by another name. A pre-registered scan of these
families against the measured band finds no member of any of them at a simple denominator: the
nearest rational multiple of $\pi$ with denominator up to sixty lies nearly three hundred standard
deviations from the band, and the nearest inverse trigonometric value of a rational or a surd with
denominator up to a hundred lies ten away. (Pushing the denominators to four hundred eventually
produces a chance coincidence, $22\pi/311$, at exactly the rate a random search would; it carries
no information.) The dimension-ratio reading
$2/9 = \dim_{\mathbb{R}}\mathbb{C} \,/\, \dim_{\mathbb{R}}(\mathbb{O}\oplus\mathbb{R})$ meets the
same difficulty in another form. A ratio of dimensions is a pure number, and turning it into an
angle requires a unit; the natural unit of angle in a symmetric geometry is the turn, and
two-ninths of a turn is $1.396$ radians, nowhere near. The reading needs a mechanism in which one
radian is the natural unit --- in which the angle is an arc measured against its radius, two units
of arc on a radius of nine --- and until that mechanism is exhibited the reading remains what we
called it: suggestive, matched rather than derived.

The constraint is nonetheless informative. An angle that is a rational number of radians is an
arc-to-radius ratio, and arc-to-radius ratios come out rational where the arc is a run of unit
steps along a flat direction, not where it is a symmetric fraction of a round circle. If $\delta$
is a holonomy at all, the connection carrying it is more likely flat along the direction that
matters --- the fibre circle, a torus --- than the round Hopf connection of Open
Problem~\ref{op:koide-delta}, and the computation to attempt is the one that specifies that flat
structure. We record this as a conjecture about where to look, not as a result.

"""

SHOWCASE_OLD = r"""This is the showcase: three masses from one dimensional input and no free dimensionless parameters,
the dimensionless content being the two theoretically fixed numbers $\alpha=\sqrt2$ and $\delta=2/9$."""

SHOWCASE_NEW = r"""This is the showcase: three masses from one dimensional input and no fitted dimensionless parameters,
the dimensionless content being the two numbers $\alpha=\sqrt2$, which the theory fixes, and
$\delta=2/9$, which it matches."""

# ---------------------------------------------------------------- headline snippet

HEAD_OLD = r"""From the chain summarised above, with zero adjustable dimensionless parameters and the electroweak
vacuum value $v$ as the single dimensional input, the framework returns"""

HEAD_NEW = r"""From the chain summarised above, with no fitted dimensionless parameters (one, the Koide phase, is
matched rather than derived) and the electroweak vacuum value $v$ as the single dimensional input,
the framework returns"""

# ---------------------------------------------------------------- predictions

PRED_OLD_1 = r"""the Koide relation holds at $\delta_0 = 2/9$ to about a tenth of a per
cent;"""
PRED_NEW_1 = r"""the Koide relation, at the matched phase $\delta_0 = 2/9$, returns the charged-lepton masses
to a hundredth of a per cent;"""

PRED_OLD_2 = r"""constants behind them: zero dimensionless parameters, with $v$ the single dimensional input."""
PRED_NEW_2 = r"""constants behind them: no fitted dimensionless parameters --- the one dimensionless number set
by hand, the Koide phase $\delta_0 = 2/9$, is matched rather than derived
(Open Problem~\ref{op:koide-delta}) --- with $v$ the single dimensional input."""

# ---------------------------------------------------------------- summary

SUMM_OLD_1 = r"""a Standard
Model with zero adjustable dimensionless parameters, the electroweak vacuum value $v$ its single
dimensional input,"""
SUMM_NEW_1 = r"""a Standard Model with no fitted dimensionless parameters (one, the Koide phase, matched rather
than derived), the electroweak vacuum value $v$ its single dimensional input,"""

SUMM_OLD_2 = r"""Postdictive, with zero dimensionless parameters and $v$ the
single dimensional input:"""
SUMM_NEW_2 = r"""Postdictive, with no fitted dimensionless parameters and $v$ the single dimensional input:"""

SUMM_OLD_3 = r"""the Koide
relation at $\delta_{0} = \tfrac29$ to about a tenth of a per cent;"""
SUMM_NEW_3 = r"""the Koide relation at the matched phase $\delta_{0} = \tfrac29$ to a hundredth of a per cent;"""


def load(path):
    text = open(path, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (path, SCRIPT))
    return text


def save(path, text):
    shutil.copy2(path, path + ".bak")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("patched %s" % path)


def main():
    masses = load(MASSES)
    headline = load(HEADLINE)
    pred = load(PRED)
    summ = load(SUMM)

    # --- masses
    n_op = masses.count(r"\begin{openproblem}")
    if "sec:koide-gap" in masses:
        sys.exit("REFUSING: label sec:koide-gap already present")
    for lab in ("app:nb-M", "eq:debt-defect", "eq:z3", "op:koide-delta"):
        pass  # existence of these labels is checked by the build, not here
    # Fill each prose paragraph of the new subsection; leave the heading block alone.
    blocks = GAP.strip("\n").split("\n\n")
    gap = "\n\n".join(b if b.lstrip().startswith("\\") else fill(b) for b in blocks) + "\n\n"
    check_widths(gap)
    showcase = fill(SHOWCASE_NEW)
    masses = replace_once(masses, OP_OLD, fill(OP_NEW), reflow=False)
    n = len(re.findall(ws(QUARKS_HEAD), masses))
    if n != 1:
        sys.exit("REFUSING: quark subsection heading matched %d times" % n)
    masses = masses.replace(QUARKS_HEAD, gap + QUARKS_HEAD, 1)
    masses = replace_once(masses, SHOWCASE_OLD, showcase, reflow=False)
    if masses.count(r"\begin{openproblem}") != n_op:
        sys.exit("REFUSING: openproblem count changed")

    # --- headline
    headline = replace_once(headline, HEAD_OLD, HEAD_NEW)  # paragraph re-filled

    # --- predictions
    pred = replace_once(pred, PRED_OLD_1, PRED_NEW_1)
    pred = replace_once(pred, PRED_OLD_2, PRED_NEW_2)

    # --- summary
    summ = replace_once(summ, SUMM_OLD_1, SUMM_NEW_1)
    summ = replace_once(summ, SUMM_OLD_2, SUMM_NEW_2)
    summ = replace_once(summ, SUMM_OLD_3, SUMM_NEW_3)

    for path, text in ((MASSES, masses), (HEADLINE, headline), (PRED, pred), (SUMM, summ)):
        if "zero adjustable dimensionless" in text or "zero dimensionless parameters" in text:
            sys.exit("REFUSING: an unqualified zero-parameter count survives in %s" % path)
        if "tenth of a per" in text and "Koide" in text and path != MASSES:
            sys.exit("REFUSING: 'tenth of a per cent' survives in %s" % path)

    save(MASSES, masses)
    save(HEADLINE, headline)
    save(PRED, pred)
    save(SUMM, summ)


if __name__ == "__main__":
    main()
