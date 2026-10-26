#!/usr/bin/env python3
"""patch_infinite_not_flat_2026-10-07T1400.py

paper1/spacetime_from_non-computability.tex, one edit, at JS's ruling of
2026-10-07: "infinite therefore flat" is wrong, since negative curvature is
infinite too; replace with "infinite therefore flat or of negative
curvature", and say that flatness is owed rather than settled
(knowledge/project-docs/inflation_horizon_infinitude_2026-10-07T1200.md,
section 4).  The fuller paragraph rewrite remains drafted and unrun as
scripts/patch_inflation_paragraph_2026-10-07T1300.py, re-anchored on the text
this patch leaves.

Sentinel-gated; anchor matches once; .bak; "% EDITED" header; refuses twice;
--check verifies only.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-10-07"
SCRIPT = Path(__file__).name
STAMP = "2026-10-07T1400"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/spacetime_from_non-computability.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


def replace_once(text, anchor, repl, label):
    hits = list(re.finditer(ws(anchor), text))
    if len(hits) != 1:
        sys.exit("%s: anchor matched %d times" % (label, len(hits)))
    m = hits[0]
    return text[: m.start()] + repl + text[m.end():]


A1 = r"""unbounded: the universe is spatially infinite, and being a network without a
boundary, naturally flat. Infinitude on its own, however, settles only flatness,
which was never inflation's principal task. The horizon problem is, and an
infinite space does nothing for it."""

R1 = r"""unbounded: the universe is spatially infinite, which leaves its spatial sections flat or of
negative curvature and excludes only the closed case. Infinitude on its own, however, does not
settle flatness, which is a fine-tuning of the Friedmann dynamics the framework has not yet
derived (Open Problem~\ref{op:comp-metric}); and flatness was in any case never inflation's
principal task. The horizon problem is, and an infinite space does nothing for it."""


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    new = replace_once(text, A1, R1, "infinite-not-flat")
    if new.count("flat or of\nnegative curvature") != 1 or "naturally flat" in new:
        sys.exit("post-check failed")
    if "\\label{op:comp-metric}" not in new:
        sys.exit("label missing: op:comp-metric")
    print("verified: %s (1 edit)" % TARGET.relative_to(ROOT))
    if CHECK:
        print("--check: nothing written"); return
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s)" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
