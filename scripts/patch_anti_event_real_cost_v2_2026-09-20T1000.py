#!/usr/bin/env python3
"""patch_anti_event_real_cost_v2_2026-09-20T1000.py

Paper 1 v2, plan item 1 (notes/paper1_v2_complex_cost_revision_plan_2026-09-18T1000.md):
the promissory note at the first "free". In paper1/what_is_a_quantum_state.tex,
sec:fanout-boundary, "without thermodynamic cost" (twice) becomes "without real
cost", and one sentence says the step from nothing to kT ln 2 at the first copy
is a placeholder replaced by the rotation of the redundancy ladder once the
amplitudes are complex. Prerequisite of item 2's script, which cites this
wording. JS, 2026-09-20: "go ahead and make the edits".

Sentinel-gated: anchor must match exactly once (whitespace-insensitive), .bak
written, "% EDITED" header added, refuses to run twice.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-20"
SCRIPT = Path(__file__).name
STAMP = "2026-09-20T1000"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/what_is_a_quantum_state.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


ANCHOR = (r"Before FANOUT no classical records exist and therefore Landauer's Principle doesn't apply, "
          r"information can be erased without thermodynamic cost. An \enquote{anti-event} erases information "
          r"without thermodynamic cost. By analogy with Burgin's proof reader, before a text has been copied "
          r"and published widely, correcting a mistake has no cost. After publication, post FANOUT, changing "
          r"something is very costly.")
REPL = r"""Before FANOUT no classical records exist and therefore Landauer's Principle doesn't apply:
information can be erased without real cost. An \enquote{anti-event} erases information without
real cost. By analogy with Burgin's proof reader, before a text has been copied and published
widely, correcting a mistake has no cost. After publication, post FANOUT, changing something is
very costly. The step from nothing to $kT\ln 2$ at the first copy is a placeholder: once the
amplitudes are complex (\S\ref{sec:complex-amplitudes}) the cost before FANOUT is a phase, and the
redundancy ladder of \S\ref{sec:wf-redundancy} replaces the step by a rotation, paid by degrees as
the copies accumulate."""


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    hits = list(re.finditer(ws(ANCHOR), text))
    if len(hits) != 1:
        sys.exit("anchor matched %d times, expected 1" % len(hits))
    m = hits[0]
    new = text[: m.start()] + REPL + text[m.end():]
    for s in ["without real cost. An", "replaces the step by a rotation"]:
        if s not in new:
            sys.exit("post-check failed: %r" % s)
    if "without thermodynamic cost" in new[m.start(): m.start() + len(REPL) + 50]:
        sys.exit("post-check failed: old wording survives in the patched region")
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s)" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
