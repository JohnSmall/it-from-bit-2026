#!/usr/bin/env python3
"""
patch_masses_z3_psi_orbit_2026-08-30.py

Adds, to the charged-lepton Koide paragraph of masses_section_2026-06-08.tex,
two sentences re-grounding the Z_3 of eq:z3 on the sedenion psi-orbit
ALONGSIDE the standing J_3(O)-triality reading (which is left untouched), at
CANDIDATE status, with pointers to sec:sedenions-generations,
sec:sedenions-promotion and rem:two-triples. Also prepends an EDITED record
to the file's header.

WHY (JS, 2026-08-30): the Koide machinery predates the two-triples
correction; under the corrected mechanism the three square-root masses are
the three psi-images of one quantity read against the selected direction,
and the exact 2 pi / 3 spacing of eq:z3 is the psi-orbit's projection. The
equivariance argument itself (why an exact S_3 gives unequal masses; the
Koide 2/3 as the orbit invariant) lives in the sedenion section's promotion
subsection (2026-08-30 revision), which this sentence points to.

ORDER / DEPENDENCIES: the pointers are FORWARD references (the sedenion
section is input after the mass arc), in the masses section's established
practice (it already forward-references sec:interactions). Requires the
2026-08-30 revision of sedenions_generations_section_2026-08-27.tex to be in
the tree (it defines rem:two-triples and sec:sedenions-promotion).
Independent of every other delivered patch.

Gates (any failure => no write, exit 1):
  - target exists and is pure ASCII;
  - the anchor "and $\\delta$ a phase. The amplitude is the Cayley--Dickson"
    occurs EXACTLY once (it is one line of the Koide paragraph);
  - idempotence: the phrase "the three $\\psi$-images of one quantity" absent.
Writes <target>.bak_2026-08-30 before modifying and prints the edited region.

Usage:
    python3 patch_masses_z3_psi_orbit_2026-08-30.py [masses_section_2026-06-08.tex]
"""
import shutil
import sys

ANCHOR = "and $\\delta$ a phase. The amplitude is the Cayley--Dickson"
IDEMPOTENCE_MARK = "the three $\\psi$-images of one quantity"
DEFAULT_TARGET = "masses_section_2026-06-08.tex"

INSERT = (
    "and $\\delta$ a phase.\n"
    "One rung up, the sedenions supply a carrier for this $\\mathbb{Z}_3$ that needs no Jordan\n"
    "structure: Brown's order-three automorphism $\\psi$ of\n"
    "\\S\\ref{sec:sedenions-generations} fixes only the line spanned by $1$ and the doubling unit\n"
    "and turns every other direction a third of a turn into its doubled partner, so the three\n"
    "square-root masses are equally the three $\\psi$-images of one quantity read against the\n"
    "selected direction. We take the two carriers to be one $\\mathbb{Z}_3$ seen from the Jordan\n"
    "and from the Cayley--Dickson side, and carry the identification at candidate status\n"
    "(Remark~\\ref{rem:two-triples}, and the equivariance paragraph of\n"
    "\\S\\ref{sec:sedenions-promotion}). The amplitude is the Cayley--Dickson"
)

HEADER = """% EDITED 2026-08-30 (patch_masses_z3_psi_orbit_2026-08-30.py, per JS):
%   two sentences added to the Koide paragraph re-grounding the Z_3 of
%   eq:z3 on the sedenion psi-orbit alongside the J_3(O) reading, at
%   CANDIDATE status; forward refs sec:sedenions-generations,
%   sec:sedenions-promotion, rem:two-triples (sedenion section,
%   2026-08-30 revision). The equivariance argument (exact S_3, unequal
%   masses; Koide 2/3 as the orbit invariant) lives there. No keys added.
"""


def fail(msg):
    print("FAIL: " + msg)
    sys.exit(1)


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TARGET
    try:
        with open(target, "r", encoding="ascii") as fh:
            text = fh.read()
    except FileNotFoundError:
        fail("target not found: " + target)
    except UnicodeDecodeError:
        fail("target is not pure ASCII: " + target)

    if IDEMPOTENCE_MARK in text:
        fail("already applied (idempotence mark present)")
    n = text.count(ANCHOR)
    if n != 1:
        fail("anchor found %d times (need exactly 1): %r" % (n, ANCHOR))

    patched = HEADER + text.replace(ANCHOR, INSERT, 1)

    bak = target + ".bak_2026-08-30"
    shutil.copyfile(target, bak)
    with open(target, "w", encoding="ascii") as fh:
        fh.write(patched)

    assert patched.count(IDEMPOTENCE_MARK) == 1
    lines = patched.split("\n")
    k = next(i for i, ln in enumerate(lines) if IDEMPOTENCE_MARK in ln)
    print("PASS: psi-orbit re-grounding inserted; EDITED header prepended")
    print("      target : " + target)
    print("      backup : " + bak)
    print("      edited region:")
    for ln in lines[k - 2:k + 9]:
        print("        | " + ln)
    print("REMINDER: the 2026-08-30 revision of the sedenion section must be in")
    print("          the tree (rem:two-triples, sec:sedenions-promotion);")
    print("          pdflatex x2 + biber, zero errors, before commit.")


if __name__ == "__main__":
    main()
