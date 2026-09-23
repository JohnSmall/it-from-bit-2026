#!/usr/bin/env python3
"""patch_circuit_scope_statement_2026-09-21T0900.py

Paper 1, absent-gate subsection, the collective-class-conversion paragraph
added 2026-09-20T2100: state honestly what the two-copy conversion circuits can
and cannot do, and that circuits respecting the gauge symmetries and
conservation laws are in preparation for a subsequent paper. JS, 2026-09-21:
"honestly state what the circuits can do, and what they can't do, and say that
we're working on circuits that respect gauge symmetries and conservation laws
and will publish in a subsequent paper."

One file, one edit. Sentinel-gated: anchor matches exactly once
(whitespace-insensitive), .bak written, "% EDITED" header added, refuses to run
twice. `--check` verifies without writing.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-21"
SCRIPT = Path(__file__).name
STAMP = "2026-09-21T0900"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/interactions_circuits_section_2026-06-08.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


ANCHOR = (r"Each is verified exactly and realised as a postselected circuit "
          r"(\texttt{scripts/multicopy\_slocc\_conversion\_2026-09-20T2100.py} and its Qiskit companion). "
          r"One copy suffices in neither direction, by tensor rank one way and by the three-tangle the other.")
REPL = r"""Each is verified exactly and realised as a postselected circuit
(\texttt{scripts/multicopy\_slocc\_conversion\_2026-09-20T2100.py} and its Qiskit companion). One
copy suffices in neither direction, by tensor rank one way and by the three-tangle the other. What
these circuits can and cannot do should be stated plainly. They act on bare qubits and carry the
entanglement class and the phases, nothing more: no charge operator is defined on their registers,
and their gate set is not restricted to operations that conserve one, which is why they can perform
a conversion, two quarks to one lepton, that colour and hypercharge forbid. They establish the
kinematic room and only that. In this framework the charges are functions of the register's
octonionic image, hypercharge the trace direction and colour the occupied line
(\S\ref{sec:charges}), so a circuit can in principle carry them, at the price of writing the charge
operators on the register and restricting the gates to those that commute with them, which is the
circuit form of the dictionary's class-closure. Circuits of that kind, respecting the gauge
symmetries and the conservation laws, are in preparation and will be reported in a subsequent
paper; nothing in the present section rests on them."""


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    hits = list(re.finditer(ws(ANCHOR), text))
    if len(hits) != 1:
        sys.exit("anchor matched %d times" % len(hits))
    m = hits[0]
    new = text[: m.start()] + REPL + text[m.end():]
    for s in ["establish the\nkinematic room and only that", "reported in a subsequent\npaper"]:
        if s not in new:
            sys.exit("post-check failed: %r" % s)
    print("verified: %s (1 edit)" % TARGET.relative_to(ROOT))
    if CHECK:
        print("--check: nothing written"); return
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s)" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
