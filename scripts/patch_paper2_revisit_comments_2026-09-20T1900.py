#!/usr/bin/env python3
"""patch_paper2_revisit_comments_2026-09-20T1900.py

Comment-only patch to paper2/paper2_main_2026-07-07.tex: beside the four
places the 2026-09-16 to 20 complex-cost thread answers or bears on, add a
"% REVISIT" comment pointing at the hub note
knowledge/project-docs/paper2_revisit_complex_cost_thread_2026-09-20T1900.md.
JS, 2026-09-20: "Make sure this conversation is to be revisited when we work
on paper 2." No typeset text changes.

Sentinel-gated: each anchor must match exactly once (whitespace-insensitive),
a .bak is written, an "% EDITED" header is added, and the script refuses to
run twice.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-20"
SCRIPT = Path(__file__).name
STAMP = "2026-09-20T1900"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper2/paper2_main_2026-07-07.tex"
HUB = "knowledge/project-docs/paper2_revisit_complex_cost_thread_2026-09-20T1900.md"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


EDITS = [
    (r"% TODO: one paragraph engaging the equation-of-state moral's history (Jacobson's",
     "% REVISIT (2026-09-20): a draft of this paragraph, in register, is in\n"
     "%   knowledge/project-docs/jacobson_non_equilibrium_spacetime_2026-09-20T1600.md\n"
     "%   section 7 (Jacobson's caveats; non-equilibrium spacetime as the graded FANOUT\n"
     "%   of a horizon; Eling--Guedens--Jacobson, Chirco--Liberati, Padmanabhan to\n"
     "%   inherit; op:p2-nonequilibrium to mint). Hub: " + HUB + "\n",
     "jacobson TODO"),
    (r"% TODO: Oreshkov--Costa--Brukner engagement paragraph; mint keys at drafting.",
     "% REVISIT (2026-09-20): basis for this section and this paragraph in\n"
     "%   knowledge/project-docs/indefinite_causal_order_fanout_2026-09-19T0900.md\n"
     "%   (duration is a phase, order is a record; the graded switch as the toy proof\n"
     "%   of the theorem target, table in Part B; the Rubino witness as a record of\n"
     "%   Lambda; op:ico-threshold). Hub: " + HUB + "\n",
     "oreshkov TODO"),
    (r"\begin{openproblem}[The Newtonian limit]\label{op:p2-newton}",
     "% REVISIT (2026-09-20): this route (clocks slowed by load) is a below-electroweak-\n"
     "%   crossover statement: above it the framework has no clocks and the conformal\n"
     "%   factor has no record. See knowledge/project-docs/\n"
     "%   gravity_planck_scale_high_temperature_2026-09-20T1800.md section 4.\n",
     "newton openproblem"),
    (r"\section{Gravity lives in the post-\fanout{} regime}",
     "% REVISIT (2026-09-20): the temperature in Landauer and the four-constant\n"
     "%   junction (landauer_temperature_fanout_energy_2026-09-20T1200.md sec. 4);\n"
     "%   records and causal structure at high temperature, the area law as capacity,\n"
     "%   the singularity as the failure of records\n"
     "%   (records_causal_structure_high_temperature_2026-09-20T1400.md); where the\n"
     "%   equation of state fails and what the Planck scale is\n"
     "%   (gravity_planck_scale_high_temperature_2026-09-20T1800.md). Hub: " + HUB + "\n",
     "gravity section"),
]


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    new = text
    for anchor, comment, label in EDITS:
        hits = list(re.finditer(ws(anchor), new))
        if len(hits) != 1:
            sys.exit("%s: anchor matched %d times" % (label, len(hits)))
        m = hits[0]
        # insert the comment block on the line before the anchor
        line_start = new.rfind("\n", 0, m.start()) + 1
        new = new[:line_start] + comment + new[line_start:]
    if new.count("% REVISIT (2026-09-20)") != 4:
        sys.exit("post-check failed: expected four REVISIT comments")
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s); four REVISIT comments added, no typeset text changed" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
