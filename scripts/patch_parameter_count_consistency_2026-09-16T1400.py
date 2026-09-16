#!/usr/bin/env python3
"""Make the free-parameter count consistent across paper 1.

JS, 2026-09-16: one section must not claim one free parameter while another counts three.

The inventory (every count statement in paper1/, read in context):

Dimensional. The masses section (its "dimensional-parameter count" paragraph) and the boson
section's op:vev are the honest statements: structurally the framework admits exactly one
dimensional input, v, because the observer cannot fix the absolute scale from inside; as
calculated, v fixes the bosons, the top (y_t = 1) and hence the up-quark sector, while the
lepton and down-quark sectors each carry a scale set by their heaviest member -- three in
all (op:sector-scales) -- and the matching scale and the QCD scale are further dimensional
quantities not yet derived from v. The headline snippet, the predictions section and the
summary (twice) say "v the single dimensional input" with no caveat: the structural claim
presented as the current count. That is the inconsistency.

Dimensionless. The 2026-09-11 patch made "no fitted dimensionless parameters (one, the Koide
phase, matched rather than derived)" uniform. But the quark subsection says the exponent 3/2
in alpha^2 = 2 + 2|Q|^(3/2) is "fixed empirically to within one per cent" and
op:colour-correction asks to derive it: a second rational number matched to data, of exactly
the Koide phase's kind, omitted from every headline count. The neutrino sector adds no
parameter (theta_nu is predicted, the 0.6 degree figure is a discrepancy; its scale is the
matching scale).

Canonical statement, used below: no fitted dimensionless parameters; two rational numbers
matched rather than derived, the Koide phase 2/9 (op:koide-delta) and the quark exponent 3/2
(op:colour-correction); alpha = sqrt2 identified; v the one dimensional input the framework
admits structurally, with the lepton and down-quark sector scales still set by hand
(op:sector-scales).

Six files, one header each, one run only; already-patched files are skipped.

paper1/headline_results_snippet_2026-07-07.tex   the lead sentence
paper1/predictions_section_2026-06-13.tex        the "count of adjustable constants" sentence
paper1/summary_section_2026-07-07.tex            two sentences
paper1/masses_section_2026-06-08.tex             "no free dimensionless" -> "no fitted" (lepton
                                                 showcase); the 3/2 named as the second matched
                                                 number where it is introduced
paper1/boson_masses_section_2026-06-08.tex       "one free dimensional scale" gains the
                                                 as-calculated caveat
paper1/appendices/appendix_hardware_fez_2026-07-10.tex
                                                 "with no free parameter" -> "with no parameter
                                                 beyond the matched Koide phase"
Left alone: main.tex 84 and 124 and what_is_a_quantum_state.tex 10 ("some free parameters"),
which claim nothing countable.

Anchors are matched whitespace-insensitively and must match exactly once; edited prose
paragraphs are re-filled to 96 columns where they hold no structure. A dated .bak is written
per file and a "% EDITED" header is prepended.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-16"
STAMP = "2026-09-16T1400"
SCRIPT = "scripts/patch_parameter_count_consistency_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

HEAD = "paper1/headline_results_snippet_2026-07-07.tex"
PRED = "paper1/predictions_section_2026-06-13.tex"
SUMM = "paper1/summary_section_2026-07-07.tex"
MASS = "paper1/masses_section_2026-06-08.tex"
BOSON = "paper1/boson_masses_section_2026-06-08.tex"
FEZ = "paper1/appendices/appendix_hardware_fez_2026-07-10.tex"


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
                                     "\\section", "\\label", "\\paragraph")):
            sys.exit("REFUSING: paragraph to re-fill contains structure:\n  %s" % line)
    return text[:start] + fill(para) + text[end:]


OLD_HEAD = r"""
From the chain summarised above, with no fitted dimensionless parameters (one, the Koide phase,
is matched rather than derived) and the electroweak vacuum value $v$ as the single dimensional
input, the framework returns --- among a spectrum in which eight of the nine charged-fermion
masses land within about one per cent of observation --- the following headline results.
"""
NEW_HEAD = fill(r"""
From the chain summarised above, with no fitted dimensionless parameters --- two rational
numbers, the Koide phase $2/9$ and the quark exponent $3/2$, are matched rather than derived
(Open Problems~\ref{op:koide-delta} and~\ref{op:colour-correction}) --- and with the electroweak
vacuum value $v$ as the one dimensional input the framework admits structurally, the lepton and
down-quark sector scales being still set by hand (Open Problem~\ref{op:sector-scales}), the
framework returns --- among a spectrum in which eight of the nine charged-fermion masses land
within about one per cent of observation --- the following headline results.
""")

OLD_PRED = r"""
adjustable constants behind them: no fitted dimensionless parameters --- the one dimensionless
number set by hand, the Koide phase $\delta_0 = 2/9$, is matched rather than derived (Open
Problem~\ref{op:koide-delta}) --- with $v$ the single dimensional input. The forward predictions
"""
NEW_PRED = r"""
adjustable constants behind them: no fitted dimensionless parameters --- the two dimensionless
numbers set by hand, the Koide phase $\delta_0 = 2/9$ (Open Problem~\ref{op:koide-delta}) and the
quark exponent $3/2$ (Open Problem~\ref{op:colour-correction}), are matched rather than derived
--- with $v$ the one dimensional input the framework admits structurally, the lepton and
down-quark sector scales being still set by hand (Open Problem~\ref{op:sector-scales}). The
forward predictions
""".strip()

OLD_SUMM_A = r"""
claim is the record it produces: a Standard Model with no fitted dimensionless parameters (one,
the Koide phase, matched rather than derived), the electroweak vacuum value $v$ its single
dimensional input, and a list of numbered problems where the chain is not yet closed. This
"""
NEW_SUMM_A = r"""
claim is the record it produces: a Standard Model with no fitted dimensionless parameters (two
rational numbers, the Koide phase and the quark exponent, matched rather than derived), the
electroweak vacuum value $v$ the one dimensional input it admits structurally, two sector scales
still set by hand, and a list of numbered problems where the chain is not yet closed. This
""".strip()

OLD_SUMM_B = r"""
The numbers, at their honest weights. Postdictive, with no fitted dimensionless parameters and
$v$ the single dimensional input: $\sin^{2}\theta_{W} = \tfrac14$ at tree level, running to
"""
NEW_SUMM_B = r"""
The numbers, at their honest weights. Postdictive, with no fitted dimensionless parameters, two
matched, and $v$ the one dimensional input the framework admits, two sector scales still set by
hand: $\sin^{2}\theta_{W} = \tfrac14$ at tree level, running to
""".strip()

OLD_MASS_A = r"""
which are the clean showcase, reproduced from a single dimensional scale and no free dimensionless
parameters; and the quarks, which require two structural modifications --- one to the amplitude, one
to the phase --- and succeed for eight of the nine charged fermions, with the one failure flagged
plainly.
"""
NEW_MASS_A = r"""
which are the clean showcase, reproduced from a single dimensional scale and no fitted
dimensionless parameters; and the quarks, which require two structural modifications --- one to
the amplitude, one to the phase, the first carrying the paper's second matched number --- and
succeed for eight of the nine charged fermions, with the one failure flagged plainly.
""".strip()

OLD_MASS_B = r"""
the coefficient being the doubling norm squared and the power $3/2$ fixed empirically to within one
per cent; the framework reads $|Q|^{3/2} = |Q|\cdot\sqrt{|Q|}$ as winding number times its
"""
NEW_MASS_B = r"""
the coefficient being the doubling norm squared and the power $3/2$ fixed empirically to within one
per cent --- the second of the paper's two matched dimensionless numbers, beside the Koide phase,
and counted with it wherever the paper counts ---; the framework reads $|Q|^{3/2} = |Q|\cdot\sqrt{|Q|}$
as winding number times its
""".strip()

OLD_BOSON = r"""
the associator, ratios from the triality angle and the dilution rule, and one free dimensional scale.
"""
NEW_BOSON = r"""
the associator, ratios from the triality angle and the dilution rule, and, structurally, one free
dimensional scale --- as calculated, three sector scales, of which $y_t = 1$ ties one to $v$
(Open Problem~\ref{op:sector-scales}).
""".strip()

OLD_FEZ = r"""
framework derives one number here with no free parameter, $\lambda = \sin\tfrac29$, and with it
"""
NEW_FEZ = r"""
framework derives one number here with no parameter beyond the matched Koide phase,
$\lambda = \sin\tfrac29$, and with it
""".strip()


def patch(path, fn, must_contain):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        print("already patched, skipping: %s" % path)
        return
    text = fn(text)
    for s in must_contain:
        if s not in text:
            sys.exit("REFUSING: %s lacks %r after the edit" % (path, s))
    shutil.copy(path, path + "." + STAMP + ".bak")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak)" % (path, path, STAMP))


def main():
    patch(HEAD, lambda t: replace_once(t, OLD_HEAD, NEW_HEAD), [r"\ref{op:sector-scales}"])
    patch(PRED, lambda t: refill_paragraph_at(replace_once(t, OLD_PRED, NEW_PRED), "quark exponent $3/2$"),
          [r"\ref{op:colour-correction}"])
    patch(SUMM, lambda t: refill_paragraph_at(refill_paragraph_at(
        replace_once(replace_once(t, OLD_SUMM_A, NEW_SUMM_A), OLD_SUMM_B, NEW_SUMM_B),
        "still set by hand, and a list"), "matched, and $v$ the one dimensional input"),
          ["set by hand"])
    # The eq:quarkalpha paragraph holds an equation block without blank lines, so it is not
    # re-filled; the replacement there is pre-wrapped.
    patch(MASS, lambda t: refill_paragraph_at(
        replace_once(replace_once(t, OLD_MASS_A, NEW_MASS_A), OLD_MASS_B, NEW_MASS_B),
        "second matched number ---"),
          ["second of the paper's two matched dimensionless numbers"])
    patch(BOSON, lambda t: refill_paragraph_at(replace_once(t, OLD_BOSON, NEW_BOSON), "as calculated, three sector scales"),
          [r"\ref{op:sector-scales}"])
    patch(FEZ, lambda t: refill_paragraph_at(replace_once(t, OLD_FEZ, NEW_FEZ), "beyond the matched Koide phase"),
          ["beyond the matched Koide phase"])


if __name__ == "__main__":
    main()
