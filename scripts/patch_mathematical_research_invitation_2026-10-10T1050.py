#!/usr/bin/env python3
"""Make the pure-mathematics research invitation explicit after the Deutsch quote.

Requested by JS, 2026-10-10. One whitespace-insensitive, sentinel-gated splice;
exclusive .bak, dated EDITED header, and refusal to run twice. --check is read-only.
The conjectured connection receives no status upgrade or ledger entry.
"""

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-10-10T1050"
TARGET = ROOT / "paper1/what_is_a_quantum_state.tex"
BACKUP = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
HEADER = "% EDITED 2026-10-10 scripts/" + Path(__file__).name + "\n"
BEGIN = "% BEGIN mathematical_research_invitation_" + STAMP
END = "% END mathematical_research_invitation_" + STAMP

OLD = r"""However logicians have not used $\sqrt{not}$ in their discussions of self-referential logic.
This is quite understandable since the postulates of quantum mechanics are an ad-hoc collection
without explanation other than the fact that they work and we can calculate numbers which match
experiment. Which isn't good enough for mathematicians who want a well founded explanation.
Hence Deutsch's suggestion that logicians could use the logical states enabled by quantum
mechanics has certainly not been adopted by people working in and around the fields of
self-referential logic and inconsistent mathematics. Although we're in a strange land where
people are using quantum computation, which involves imaginary truth values, yet logicians have
not taken to using them in their exploration of self-referential paradoxes and hypodoxes."""

NEW = r"""Deutsch's suggestion connects the present enquiry with Mortensen's programme of inconsistent
mathematics, which studies mathematical theories in logics that tolerate contradictions without
making every proposition provable \autocite{mortensen1995inconsistent}. There is also work directly
extending Spencer-Brown's imaginary logical values: Kauffman and Collings develop a four-valued
calculus with a square root of negation \autocite{kauffmancollings2019bf}. These provide
mathematical starting points for asking whether quantum superposition can supply a semantics for
self-referential expressions that admit no consistent Boolean assignment.

The proposed connection is that the obstruction identified by Lawvere and Yanofsky may motivate
both an extension of logical values and the complex amplitudes used in physics. A mathematical
derivation along these lines would give superposition a foundation in the structure of
self-reference, strengthening Deutsch's appeal to physically realised operations. Quantum
structures can already be studied axiomatically; the additional gain would be an explanation of
why such structures arise. Establishing the correspondence between superposition and the states
used in inconsistent mathematics remains part of this enquiry.

Completing this route could therefore open further work on self-reference, nonclassical semantics
and computation, with significance for pure mathematics independent of its applications to
quantum foundations. Here it is offered as an invitation to mathematicians. The present paper
develops the physically motivated route through self-referential ignorance and Shannon
information; it leaves the proposed mathematical connection for further work. Its conditional
argument from reversible continuity to the $p=2$ norm
(\S\ref{sec:reversible-continuity-l2}) can be assessed on its stated premises without completing
that wider programme."""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()

    original = TARGET.read_bytes()
    text = original.decode("utf-8")
    if HEADER in text or BEGIN in text or END in text or BACKUP.exists():
        raise SystemExit("Refusing to run twice: edit sentinel or backup already exists.")

    pattern = r"\s+".join(re.escape(token) for token in OLD.split())
    matches = list(re.finditer(pattern, text))
    if len(matches) != 1:
        raise SystemExit(f"Expected one paragraph anchor; found {len(matches)}.")
    match = matches[0]
    replacement = BEGIN + "\n" + NEW + "\n" + END
    updated = HEADER + text[:match.start()] + replacement + text[match.end():]
    if updated.count(BEGIN) != 1 or updated.count(END) != 1:
        raise SystemExit("Expected exactly one BEGIN/END sentinel pair.")

    norm_section = ROOT / "paper1/L2_metric_global_phase_section_2026_06_07.tex"
    label = r"\label{sec:reversible-continuity-l2}"
    if norm_section.read_text(encoding="utf-8").count(label) != 1:
        raise SystemExit("The norm-section label is missing or duplicated.")
    batch = ROOT / "bib/mathematical_research_refs_2026-10-10T1050.bib"
    keys = re.findall(r"^@\w+\{([^,]+),", batch.read_text(encoding="utf-8"), re.M)
    cited = re.findall(r"\\autocite\{([^}]+)\}", NEW)
    if any(keys.count(key) != 1 for key in cited):
        raise SystemExit("A new citation is missing or duplicated in the dated batch.")

    print("verified: one whitespace-insensitive paragraph anchor")
    print("verified: one BEGIN/END pair and existing norm-section label")
    print("verified: both new citation keys occur once in the dated batch")
    if args.check:
        print("--check: nothing written")
        return

    if TARGET.read_bytes() != original:
        raise SystemExit("Target changed during preparation; refusing to overwrite it.")
    with BACKUP.open("xb") as backup:
        backup.write(original)
    TARGET.write_bytes(updated.encode("utf-8"))
    print("patched: " + str(TARGET.relative_to(ROOT)))
    print("backup: " + str(BACKUP.relative_to(ROOT)))


if __name__ == "__main__":
    main()
