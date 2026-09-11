#!/usr/bin/env python3
"""Resolve the undefined section references in paper 1.

The build has carried thirteen "Reference ... undefined" warnings for months;
they render as "??" in the PDF, all but three of them in the introduction's
"Paper structure" paragraph. Two are outright typos (sec:Kioid,
sec:negative_probaility) and the rest name labels that were never created or
that were renamed. Each target below was matched by reading the heading the
sentence describes, not by guessing at the name.

Resolved to labels that already exist:

  sec:negative_probaility -> sec:complex-amplitudes-2
      \\subsection{The price is negative probability}, self_reference_section,
      which main.tex inputs immediately after what_is_a_quantum_state -- so it
      is also where the narrative order puts it.
  sec:self-ignorance      -> sec:fibre-self-ignorance
      \\subsection{The fibre as self-referential ignorance}, L2_metric section.
  sec:quantum_number      -> sec:charges
      \\section{Quantum Numbers}.
  sec:particle_zoo        -> sec:generations
      \\section{The Particle Zoo}.
  sec:quantum_circuits    -> sec:interactions
      \\section{Interactions as Quantum Circuits}.
  sec:sedenions-generations -> sec:sedenion-announcement  (three occurrences)
      \\subsection{The extra wire: how a deeper mechanism announced itself},
      particle_zoo, which is where the sedenion generation label is derived.

Given a label, the heading being unlabelled:

  sec:achirality_qcd    -> sec:achirality-qcd
      \\subsection{Why the colour force is not chiral}, particle_zoo.
  sec:Kioid             -> sec:koide
      \\subsection{Charged leptons: the Koide relation}, masses.
  sec:weak_mixing_angle -> sec:weak-mixing-angle
      \\subsection{The weak mixing angle and the $W$/$Z$ mass ratio},
      boson_masses.

NOT touched, and left undefined deliberately: sec:sedenions-mixing, one
occurrence in wigners_friend. The sentence says that section "reads that phase
--- through the paper's negativity--contextuality chain --- as this wire's
contextual cargo". Two sections could be meant, the masses section's
\\subsection{Mass eigenstates versus weak eigenstates} and the interactions
section's provenance paragraph on the sedenion route to the full CKM, and
choosing between them is an editorial call, not a typo fix.

New labels are hyphenated, the majority house style. Anchors are matched
whitespace-insensitively and each must match the expected number of times. A
.bak is written per file, an "% EDITED" header prepended, and the header makes
the script refuse to run twice.

This patch is static: it only renames references and adds labels. It cannot be
verified without a build, which is JS's to authorise.
"""

import re
import shutil
import sys

DATE = "2026-09-11"
SCRIPT = "scripts/patch_undefined_section_refs_2026-09-11T2030.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"

MAIN = "paper1/main.tex"
WF = "paper1/wigners_friend_in_the_hopf_picture_2026-06-13.tex"
ZOO = "paper1/particle_zoo_section_2026-06-08.tex"
MASSES = "paper1/masses_section_2026-06-08.tex"
BOSON = "paper1/boson_masses_section_2026-06-08.tex"

# old label -> (new label, file, expected occurrences)
RETARGET = [
    ("sec:negative_probaility", "sec:complex-amplitudes-2", MAIN, 1),
    ("sec:self-ignorance", "sec:fibre-self-ignorance", MAIN, 1),
    ("sec:achirality_qcd", "sec:achirality-qcd", MAIN, 1),
    ("sec:quantum_number", "sec:charges", MAIN, 1),
    ("sec:Kioid", "sec:koide", MAIN, 1),
    ("sec:weak_mixing_angle", "sec:weak-mixing-angle", MAIN, 1),
    ("sec:particle_zoo", "sec:generations", MAIN, 1),
    ("sec:quantum_circuits", "sec:interactions", MAIN, 1),
    ("sec:sedenions-generations", "sec:sedenion-announcement", WF, 3),
]

# heading to label -> (file, heading, new label)
ADD_LABEL = [
    (ZOO, r"\subsection{Why the colour force is not chiral}", "sec:achirality-qcd"),
    (MASSES, r"\subsection{Charged leptons: the Koide relation}", "sec:koide"),
    (BOSON,
     r"\subsection{The weak mixing angle and the \texorpdfstring{$W$/$Z$}{W/Z} mass ratio}",
     "sec:weak-mixing-angle"),
]


def load(path, cache={}):
    if path not in cache:
        text = open(path, encoding="utf-8").read()
        if HEADER.strip() in text:
            sys.exit("REFUSING: %s already patched by %s" % (path, SCRIPT))
        cache[path] = text
    return cache[path]


def main():
    files = {p: load(p) for p in {MAIN, WF, ZOO, MASSES, BOSON}}

    # --- add the three labels first, so every retarget has somewhere to land
    for path, heading, label in ADD_LABEL:
        text = files[path]
        if ("\\label{%s}" % label) in text:
            sys.exit("REFUSING: %s already defined in %s" % (label, path))
        pat = re.compile(r"\s+".join(re.escape(p) for p in heading.split()))
        n = len(pat.findall(text))
        if n != 1:
            sys.exit("REFUSING: heading matched %d times in %s:\n  %s" % (n, path, heading))
        m = pat.search(text)
        files[path] = text[:m.end()] + "\n\\label{%s}" % label + text[m.end():]

    # --- retarget the references
    for old, new, path, expected in RETARGET:
        text = files[path]
        pat = re.compile(r"\\ref\{%s\}" % re.escape(old))
        n = len(pat.findall(text))
        if n != expected:
            sys.exit("REFUSING: \\ref{%s} occurs %d times in %s, expected %d"
                     % (old, n, path, expected))
        files[path] = pat.sub(r"\\ref{%s}" % new, text)

    # --- every target must now resolve somewhere in the paper
    everything = "".join(open(p, encoding="utf-8").read()
                         for p in ["paper1/main.tex"] + sorted(
                             __import__("glob").glob("paper1/*.tex")
                             + __import__("glob").glob("paper1/appendices/*.tex"))
                         if "attic" not in p)
    everything += "".join(files.values())
    for _, new, _, _ in RETARGET:
        if ("\\label{%s}" % new) not in everything:
            sys.exit("REFUSING: target label %s is not defined anywhere" % new)
    for old, _, path, _ in RETARGET:
        if ("ref{%s}" % old) in files[path]:
            sys.exit("REFUSING: %s survives in %s" % (old, path))

    for path, text in files.items():
        shutil.copy2(path, path + ".bak")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(HEADER + text)
        print("patched %s" % path)


if __name__ == "__main__":
    main()
