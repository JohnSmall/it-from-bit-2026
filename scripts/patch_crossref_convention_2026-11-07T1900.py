#!/usr/bin/env python3
"""Normalise Paper 1's internal cross-reference convention.

Three changes, all in paper1/:

  A. "Section~\\ref{sec:...}" -> "\\S\\ref{sec:...}"  (22 sites in 4 files),
     against 548 existing "\\S\\ref{sec:...}".  The section sign is the
     paper's majority form; "Section" spelled out is the minority.

  B. Bare "\\ref{sec:...}" / "\\ref{app:...}" with no qualifier in front
     (22 sites) gain one.  These currently print as a naked number, e.g.
     "a question 'What is a quantum state' 2".  Bracketed where the
     reference is an appended pointer, unbracketed where it is part of the
     sentence's grammar ("in \\S4.2", "of \\S4.2").

  C. One unbalanced bracket, main.tex:257.

NOT touched: "\\ref{sec:somthing}" at what_is_a_quantum_state.tex:605, whose
label does not exist; theorem-like environments (Proposition~, Lemma~,
Problem~, Remark~, Corollary~, Table~), which are already consistent; and
the 12 "\\S\\ref{app:jaynes:*}" in the Jaynes appendix, which point at
subsections within that appendix and so are correctly a section sign.

Asserts every anchor matches exactly the expected number of times, writes a
.bak, stamps an "% EDITED" header, and refuses to run twice.
Usage: patch_crossref_convention_2026-11-07T1900.py [--check]
"""

import re
import shutil
import sys
from pathlib import Path

DATE = "2026-11-07"
STAMP = f"% EDITED {DATE}: internal cross-reference convention normalised " \
        f"(scripts/patch_crossref_convention_{DATE}T1900.py)\n"
ROOT = Path(__file__).resolve().parent.parent / "paper1"

# --- A: uniform substitution, with the exact count expected per file -------
UNIFORM = {
    "main.tex": 9,
    "derivation_of_the_quantum_postulates.tex": 4,
    "spacetime_from_non-computability.tex": 5,
    "wigners_friend_in_the_hopf_picture_2026-06-13.tex": 4,
}
UNIFORM_OLD = r"Section~\ref{sec:"
UNIFORM_NEW = r"\S\ref{sec:"

# --- B and C: per-site splices, (old, new) ---------------------------------
SITES = {
    "main.tex": [
        # C: the unbalanced bracket (applied after A has run on this file)
        (r"and the Tsirelson bound (\S\ref{sec:tsirelson} follow",
         r"and the Tsirelson bound (\S\ref{sec:tsirelson}) follow"),
        # B: the Paper structure paragraph
        (r"quantum state} \ref{sec:what_is_a_quantum_state},",
         r"quantum state} (\S\ref{sec:what_is_a_quantum_state}),"),
        (r"self-reference \ref{sec:popper}, from that",
         r"self-reference (\S\ref{sec:popper}), from that"),
        (r"\ref{sec:complex-amplitudes-2} and that the probability",
         r"(\S\ref{sec:complex-amplitudes-2}) and that the probability"),
        (r"information \ref{sec:fibre-self-ignorance} from that",
         r"information (\S\ref{sec:fibre-self-ignorance}) from that"),
        (r"probability amplitudes \ref{sec:complex-amplitudes}. Once",
         r"probability amplitudes (\S\ref{sec:complex-amplitudes}). Once"),
        (r"\ref{sec:reversible-continuity}, which \ref{sec:continuity} reduces",
         r"(\S\ref{sec:reversible-continuity}), which \S\ref{sec:continuity} reduces"),
        (r"\ref{sec:reversible-continuity-l2}. We also note",
         r"(\S\ref{sec:reversible-continuity-l2}). We also note"),
        (r"\ref{sec:space-of-computations}. We find",
         r"(\S\ref{sec:space-of-computations}). We find"),
        (r"Hopf fibration picture \ref{sec:wf-friend}, which leads",
         r"Hopf fibration picture (\S\ref{sec:wf-friend}), which leads"),
        (r"postulates in \ref{sec:postulates}. That in turn",
         r"postulates in \S\ref{sec:postulates}. That in turn"),
        (r"particle interactions \ref{sec:hopf-justification}, which compels",
         r"particle interactions (\S\ref{sec:hopf-justification}), which compels"),
        (r"particle physics \ref{sec:division-algebras}. Then",
         r"particle physics (\S\ref{sec:division-algebras}). Then"),
        (r"interesting result \ref{sec:achirality-qcd}. Once",
         r"interesting result (\S\ref{sec:achirality-qcd}). Once"),
        (r"quantum numbers in \ref{sec:charges} and",
         r"quantum numbers in \S\ref{sec:charges} and"),
        (r"Kiode relations \ref{sec:koide} as well",
         r"Kiode relations (\S\ref{sec:koide}) as well"),
        (r"\ref{sec:weak-mixing-angle}. We then move on",
         r"(\S\ref{sec:weak-mixing-angle}). We then move on"),
        (r"multi-particle entanglement \ref{sec:generations}.",
         r"multi-particle entanglement (\S\ref{sec:generations})."),
        (r"awkward misses \ref{sec:masses}. Since",
         r"awkward misses (\S\ref{sec:masses}). Since"),
        (r"do in \ref{sec:interactions}.",
         r"do in \S\ref{sec:interactions}."),
    ],
    "what_is_a_quantum_state.tex": [
        ('is in the\n' + r"appendices \ref{app:fanout-boundary}",
         'is in\n' + r"Appendix~\ref{app:fanout-boundary}."),
        (r"In \ref{sec:measuring-non-computability} I'll",
         r"In \S\ref{sec:measuring-non-computability} I'll"),
    ],
    "entanglement_classes_and_gauge_groups_2026-06-08.tex": [
        (r"which we pick up in \ref{sec:interactions}",
         r"which we pick up in \S\ref{sec:interactions}"),
    ],
}

check = "--check" in sys.argv
fail = []
plan = []

for name in sorted(set(UNIFORM) | set(SITES)):
    path = ROOT / name
    if not path.exists():
        fail.append(f"{name}: missing")
        continue
    text = path.read_text(encoding="utf-8")
    if text.startswith("% EDITED") and f"cross-reference convention" in text.split("\n")[0]:
        fail.append(f"{name}: already patched by this script -- refusing")
        continue
    new = text

    if name in UNIFORM:
        want = UNIFORM[name]
        got = new.count(UNIFORM_OLD)
        if got != want:
            fail.append(f"{name}: expected {want} 'Section~\\ref{{sec:', found {got}")
        else:
            new = new.replace(UNIFORM_OLD, UNIFORM_NEW)
            plan.append(f"{name}: A  {want} x 'Section~\\ref{{sec:' -> '\\S\\ref{{sec:'")

    for old, repl in SITES.get(name, []):
        n = new.count(old)
        if n != 1:
            fail.append(f"{name}: anchor matched {n} times, need 1: {old[:62]!r}")
            continue
        new = new.replace(old, repl)
        plan.append(f"{name}: B  {old.strip()[:66]!r}")

    if fail:
        continue
    if new == text:
        fail.append(f"{name}: nothing changed")
        continue
    if not check:
        shutil.copy2(path, path.with_suffix(path.suffix + f".bak-{DATE}"))
        path.write_text(STAMP + new, encoding="utf-8")

if fail:
    print("REFUSED -- no file written\n")
    for f in fail:
        print("  " + f)
    sys.exit(1)

print(("DRY RUN -- would apply" if check else "APPLIED") + f" {len(plan)} edits\n")
for p in plan:
    print("  " + p)

# post-check: the only bare section/appendix ref left must be sec:somthing
if not check:
    bare = re.compile(r"(?<!\\S)(?<![~A-Za-z])\\ref\{(?:sec|app):([^}]*)\}")
    left = []
    for f in sorted(ROOT.rglob("*.tex")):
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            if line.lstrip().startswith("%"):
                continue
            for m in bare.finditer(line):
                if m.group(1) != "somthing":
                    left.append(f"{f.relative_to(ROOT)}:{i}: {m.group(0)}")
    print(f"\npost-check: {len(left)} unqualified refs remain "
          f"(expected 0 besides sec:somthing)")
    for l in left:
        print("  " + l)
