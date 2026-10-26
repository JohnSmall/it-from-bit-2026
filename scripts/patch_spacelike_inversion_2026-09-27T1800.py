#!/usr/bin/env python3
"""patch_spacelike_inversion_2026-09-27T1800.py

paper1/spacetime_from_non-computability.tex. JS, 2026-09-27: "people who are
used to thinking that tachyonic anti-telephony is an afterthought of the
standard spacetime metric might miss the inversion and then get confused when
we dismiss octonionic spacetime." Three edits.

1. sec:comp-distance, after the paragraph that ends "...motivated by
   reproducing what nature does, not proved.": two paragraphs stating the
   inversion in plain terms (the antitelephone as a corollary there, the
   antitelephone loops as the definition here) and then, in JS's picture
   (2026-09-27, revised the same evening), many observers with antitelephones
   to each other: the network is consistent only if relays compose
   associatively, two links always do (Artin), three do only inside a
   quaternionic subalgebra (Harvey--Lawson associative 3-planes), so the
   largest consistent network in S^7 is an S^3 and space has three
   directions; and the forward warning that S^7 is set aside below for that
   reason and not because R^8 lacks a metric or Spin(9,1) fails to exist.
   Numerical check: scripts/antitelephone_network_associativity_2026-09-27T1900.py
   (PASS). Cites benfordbooknewcomb1970tachyonic, tolman1917theory (batch
   written, metadata verified, VERIFY-SUPPORT, undefined until imported),
   conway_2003 and harvey1982calibrated (in the library, VERIFY-SUPPORT for
   the passages, flagged in a %% comment) and baez2002octonions.
2. sec:three-dimensions: "forbids a metric outright" becomes "forbids a metric
   built from the sphere's own composition law outright".
3. Same paragraph, after "no geodesic structure exists.": one parenthesis
   saying what is untouched.

Sentinel-gated; anchors match once; .bak; "% EDITED" header; refuses twice;
`--check` verifies only.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-27"
SCRIPT = Path(__file__).name
STAMP = "2026-09-27T1800"
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


A1 = r"identification is motivated by reproducing what nature does, not proved."
R1 = A1 + r"""

%% VERIFY-SUPPORT 2026-09-27: conway_2003 is cited below for "any two octonions
%% generate an associative subalgebra" (Artin's theorem; a Moufang loop is
%% diassociative) and harvey1982calibrated for "a three-plane in Im O is
%% associative iff the associator of a basis vanishes, and the associative
%% three-planes are the imaginary parts of the quaternionic subalgebras"
%% (Harvey--Lawson, ch. IV). Neither passage was read in the session that wrote
%% this; both statements are checked numerically in Convention A by
%% scripts/antitelephone_network_associativity_2026-09-27T1900.py (PASS).
A reader used to the standard order of ideas should pause here, because the order has been
inverted, and the inversion is used below. In special relativity the tachyonic antitelephone is a
corollary: a signal faster than light, composed with a boost, would arrive before it was sent and
close a timelike loop, therefore there is no such signal \autocite{tolman1917theory,
benfordbooknewcomb1970tachyonic}. The metric comes first and the impossible telephone is a check
on it. Here the telephone comes first. Two observers are spacelike separated when an antitelephone
between them would close a loop; the loops such telephones would close, and carry nothing round,
are what spacelike separation is, their number is the distance, and the metric is read off from
them. Nothing is lost, since the corollary returns as a tautology: an antitelephone that carried
a record would close a causal loop, and its two ends would not have been spacelike after all.

What is gained is a definite meaning for a spatial dimension. Picture many observers, each holding
an antitelephone to each of the others. A message relayed from one observer to another through a
third composes two transports round two loops, and the network is consistent only if every relay
composes to a single transport whatever the bracketing of the relaying: a spatial dimension is a
family of loops whose transports compose associatively, which is a group law on a parallelisable
sphere. That is a condition a family of loops can fail, and \S\ref{sec:three-dimensions} shows
that the loops of the seventh sphere fail it. Two antitelephones always compose, because any two
octonions generate an associative subalgebra \autocite{conway_2003}; three compose only when their
imaginary parts lie in one quaternionic subalgebra, which is what the associative three-planes of
Harvey and Lawson are \autocite{harvey1982calibrated}, and a third link outside that subalgebra is
seen by the network exactly through its component outside it. The largest consistent network of
antitelephones inside $S^{7}$ is therefore an $S^{3}$, and there are three spatial directions.
When the seventh sphere is set aside there as a ruler, which is the octonionic spacetime of the
division-algebra literature, the claim is not that $\mathbb{R}^{8}$ has no metric, nor that the
ten-dimensional Minkowski space of $SL(2,\mathbb{O}) \cong \mathrm{Spin}(9,1)$ fails to exist
\autocite{baez2002octonions}; it is that the octonionic directions are not loops on which
antitelephones compose, and so are algebra rather than distance. In the standard order that
sentence has no content; in this one it is the reason space has three dimensions."""

A2 = r"The same non-associativity forbids a metric outright: path composition $d(A,C)$ through $B$ depends on the bracketing,"
R2 = r"""The same non-associativity
forbids a metric built from the sphere's own composition law outright: path
composition $d(A,C)$ through $B$ depends on the bracketing,"""

A3 = r"no geodesic structure exists. Since the abelian $S^{1}$ alone cannot carry"
R3 = r"""no geodesic structure exists. (What is untouched should be said: the Euclidean metric of
$\mathbb{R}^{8}$, and the ten-dimensional spacetime that $SL(2,\mathbb{O})$ furnishes, are metrics
of the ordinary kind; what fails is a ruler made of antitelephone loops, which is what a spatial
dimension is in this section, as \S\ref{sec:comp-distance} set out. Nor is the failure total:
relays between any two links compose, and among three they compose exactly when the links lie in
one quaternionic subalgebra, so the largest consistent network inside $S^{7}$ is an $S^{3}$
\autocite{conway_2003,harvey1982calibrated}.) Since the abelian $S^{1}$ alone cannot carry"""


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    new = replace_once(text, A1, R1, "inversion paragraph")
    new = replace_once(new, A2, R2, "metric clause")
    new = replace_once(new, A3, R3, "untouched parenthesis")
    for s in ["the order has been\ninverted", "built from the sphere's own composition law", "a ruler made of antitelephone loops", "Picture many observers"]:
        if new.count(s) != 1:
            sys.exit("post-check failed: %r" % s)
    print("verified: %s (3 edits)" % TARGET.relative_to(ROOT))
    if CHECK:
        print("--check: nothing written"); return
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s)" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
