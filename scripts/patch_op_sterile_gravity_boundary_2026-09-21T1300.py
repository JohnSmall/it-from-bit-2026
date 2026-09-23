#!/usr/bin/env python3
"""patch_op_sterile_gravity_boundary_2026-09-21T1300.py

Paper 1: restate Open Problem op:sterile-gravity as a boundary with PASS/FAIL,
and name the boundary in the spacetime section's deferred dark-matter
paragraph. JS, 2026-09-21: "this can be marked as a genuine boundary where the
framework might fail to be able to make any predictions and therefore needs
more work to understand." NOT RUN until JS rules; `--check` verifies anchors.
Argument: knowledge/project-docs/boundary_gravity_of_unrecorded_matter_2026-09-21T1300.md.
Sentinel-gated; .bak; "% EDITED" header; refuses to run twice.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-21"
SCRIPT = Path(__file__).name
STAMP = "2026-09-21T1300"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


def replace_once(text, anchor, repl, label):
    hits = list(re.finditer(ws(anchor), text))
    if len(hits) != 1:
        sys.exit("%s: anchor matched %d times" % (label, len(hits)))
    m = hits[0]
    return text[: m.start()] + repl + text[m.end():]


ZOO = ROOT / "paper1/particle_zoo_section_2026-06-08.tex"
A1 = r"""\begin{openproblem}[The sterile channel and relational gravity]\label{op:sterile-gravity}
Reconcile the gravitational participation of a gauge-sterile massive channel with the framework's
identification of gravity with measurement. Since whatever affects the causal structure must, on that
identification, be measurable, a channel that couples to no gauge force must nonetheless enter the
relational network by some route if it is to gravitate. Candidate directions, none here endorsed: that
the channel possesses a measurable but non-gauge interaction, which the framework would then have to
exhibit; that its mass --- its associator-geodesic length (Open Problem~\ref{op:associator-geodesic})
--- itself constitutes its relational participation, perhaps as a self-relation, which would connect
to the open Majorana reading and to the self-referential character of the framework as a whole; or
that the channel is a pre-spatial object that never acquires a distinct spacetime location, in which
case its cosmological gravitational effects must be accounted for without one. The resolution bears
directly on the nature of mass, of the sterile sector, and of dark matter, and we flag it as a
tension the framework's identification of gravity with measurement makes unavoidable.
 The spacetime section's dark-matter prospect names the same condition from the
metric side --- participation in loop-counting prior to, and independent of, gauge participation
(\S\ref{sec:space-of-computations}) --- and the two statements are one problem.
\end{openproblem}"""
R1 = r"""\begin{openproblem}[The sterile channel and relational gravity: a boundary]\label{op:sterile-gravity}
Reconcile the gravitational participation of matter that engages no gauge force with the framework's
identification of gravity with the bookkeeping of records. Whatever affects the causal structure
must, on that identification, be recorded, so a channel that couples to no gauge force must enter the
relational network by some route if it is to gravitate. Three routes are on the table, and they are
not the same physics. First, a non-gauge interaction that writes records: the a-chiral channel's
Yukawa is such a gate, and with a seesaw-size coupling at $3.6$~TeV it thermalises the channel at
$T \sim M$ and decays it within $10^{-15}$~s, so that channel is recorded at birth and at death and
is not dark matter, while a stable relic needs a coupling small enough to leave no record after its
production; the sphaleron is not such a route, since it touches no singlet. Second, the tick-rate
itself: the channel's mass as its relational participation, a self-relation
(Open Problem~\ref{op:associator-geodesic}), on which anything with a worldline gravitates whether
or not it is recorded; this is the spacetime section's reading, participation in loop-counting
prior to and independent of gauge participation (\S\ref{sec:space-of-computations}), and it makes
gravity a pre-\textsc{fanout} phenomenon. Third, energy--momentum as a conserved charge, so that the
record written at production persists by conservation, and between events the source has no
location: unrecorded matter gravitates as a delocalised source at the resolution of its records,
which keeps gravity post-\textsc{fanout} and matches the smoothness of dark-matter haloes. The
second and third agree on everything that exists and differ on which side of the boundary gravity
reads, and the framework has not chosen; until it has, what gravitates is not a prediction of the
framework but an assumption borrowed from general relativity, and dark matter is the case in which
that shows. PASS: the count-density dictionary of the second paper states which side it counts,
reproduces the coupling to $\langle T_{\mu\nu}\rangle$ for recorded matter, reproduces the
dark-matter fraction and the smoothness of haloes, and gives the one sentence both papers can
carry. FAIL: a dictionary on which only gauge-recorded matter counts, refuted by the dark-matter
fraction; or the two papers left answering differently; or no dictionary, in which case this is the
boundary at which the framework makes no prediction about dark matter, and it says so. The
resolution bears directly on the nature of mass, of the sterile sector, and of dark matter, and we
mark it as the boundary the identification of gravity with records makes unavoidable.
\end{openproblem}"""

ST = ROOT / "paper1/spacetime_from_non-computability.tex"
A2 = (r"If gravity is the bookkeeping of the interaction network and dark matter interacts only "
      r"gravitationally, how does it participate in a network it does not exchange information with?")
R2 = (r"If gravity is the bookkeeping of the interaction network and dark matter interacts only"
      "\n" r"gravitationally, how does it participate in a network it does not exchange information with?"
      "\n" r"This is a genuine boundary of the programme, at which it may make no prediction, and Open"
      "\n" r"Problem~\ref{op:sterile-gravity} states it with the criteria that would close it.")


EDITS = [(ZOO, [(A1, R1, "zoo: op:sterile-gravity")], ["a boundary]", "PASS: the count-density dictionary"]),
         (ST, [(A2, R2, "spacetime: boundary sentence")], ["genuine boundary of the programme"])]


def main():
    staged = []
    for path, edits, must in EDITS:
        text = path.read_text()
        if HEADER in text:
            sys.exit("%s already carries %s; refusing to run twice" % (path.name, SCRIPT))
        new = text
        for anchor, repl, label in edits:
            new = replace_once(new, anchor, repl, label)
        for s in must:
            if s not in new:
                sys.exit("%s: post-check failed, missing %r" % (path.name, s))
        staged.append((path, new))
        print("verified: %s" % path.relative_to(ROOT))
    if CHECK:
        print("--check: nothing written"); return
    for path, new in staged:
        bak = path.with_name(path.name + "." + STAMP + ".bak")
        shutil.copyfile(path, bak)
        path.write_text(HEADER + new)
        print("patched: %s (backup %s)" % (path.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
