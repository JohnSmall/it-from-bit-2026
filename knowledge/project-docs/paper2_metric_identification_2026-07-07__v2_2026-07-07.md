# The Metric Identification: Space of Computations = Spacetime of GR

**Session document, 2026-07-07.** Seeds the central identification of Paper 2 (the dynamical
layer). Prompted by JS's observation: GR defines the metric via energy--momentum; the framework
defines it via computable/non-computable step counts; Toffoli and Margolus identify energy with
computation; therefore the two metric definitions may be one. Verdict of the session: they are,
with a precise shape. Status vocabulary as ever: proved / structural / candidate / owed / open.

## 1. The Rosetta line (the core of the identification)

Margolus--Levitin: a system with mean energy E above ground passes through orthogonal states at
rate at most 2E/h — energy IS the ceiling on computable steps per unit time. The spatial sibling:
momentum p gives orthogonal position-states at rate p/hbar per unit length (de Broglie, read
computationally). So, up to hbar:

  (E, p)  <-->  (computable steps per unit time, distinguishable marks per unit length)

GR: the metric is sourced by T_mu-nu. Framework: the metric is BUILT FROM counting computational
events. ML/de Broglie: the density of computational events IS T_mu-nu. **The two definitions of
the metric are the same definition in two currencies, with hbar the exchange rate.** Bonus echo:
temporal count rides E, spatial count rides p — the real/imaginary split of the comp-distance maps
onto the time/space block structure of T exactly where it should.

## 2. Two rungs

**Kinematic (one theorem away).** Framework interval <-> Lorentzian interval. Conversion factors
supplied by ML + de Broglie; the only gate on our side is op:comp-metric (genuine pseudo-metric,
derived signature). Once that lands, the dictionary above is a proposition.

**Dynamic (marked trail, tolls already paid).** Why Einstein's equations specifically: Jacobson's
equation-of-state derivation. Required inputs vs Paper-1 stock:
- Unruh temperature: DERIVED (T = hbar a / 2 pi c k_B, WF-for-accelerated-observers). In hand.
- Entropy proportional to area: the "area = negative information" conjecture (entropic-gravity
  paragraph). In hand at conjecture status.
- Local causal horizons: definable once op:comp-metric supplies causal structure. Gated.
Chain: comp-metric -> Rindler wedges in the network -> Jacobson -> Einstein equations as the
equation of state of step bookkeeping, with §1 supplying WHY the source is energy--momentum.

## 3. Two jewels (candidate theorems for Paper 2)

**Equivalence principle = ML blindness.** The ML bound is species-blind: only E enters, never the
substrate. Universality of free fall as the clock-rate theorem's indifference to what is
computing. A derivation of a postulate — exactly this programme's kind of result.

**G as the bit--area exchange rate — SHARPENED 2026-07-07 (JS's imaginary-units question).** In
native units (time in steps, space in i x bits) the three constants are the three exchange rates:
c = steps<->bits (native value 1), hbar = counts<->(E,p) (the Rosetta), and G — via
l_P^2 = G hbar / c^3 — is what remains: the physical area of ONE BIT, G = lambda^2 c^3 / hbar up
to O(1), lambda = length-per-bit. G_native = 1: Newton's constant is the unit-conversion artifact
of measuring bit-counts in square metres; gravity's weakness = the bit is small.

**The i^2 discovery.** A spacelike area is a product of two imaginary lengths:
A_native = (i N1)(i N2) = -N1 N2. Native area is NEGATIVE in bit-pairs — so the paper's
"area = negative information" conjecture is not a slogan: THE MINUS SIGN IS i^2, forced the moment
space is measured in imaginary units. Same i, second job: its first was the Minkowski signature
(op:comp-metric's "derived rather than read off"). Bekenstein--Hawking in native currency:
A_native = -S (bits), coefficient owed. PROVENANCE CORRECTED 2026-07-07 (JS's recall):
the two-way — including the converse, "ordinary holography implies the imaginary-units
convention" — appears in the Växjö 2024 and 2025 posters; the earlier "new" verdict grepped only
the .tex corpus, not the posters. The paper never carried it; it now does (restored to the
Jacobson subsection, Brillouin cited, i^2 payoff attached, honesty tail routed to op:comp-metric).
Rediscovery, not discovery.

**What "deriving G" now means.** With the dimensionful part exposed as conversion, the content is
the O(1) coefficient — bits per bit-pair, the 4 ln 2-type factor, equivalently lambda / l_P.
Candidate route: the one-bit-per-closed-curve pricing as the ledger's quantum. NEW care-flag: the
minimal loop's circumference-vs-enclosed-area bookkeeping on a network is nontrivial. HONESTY FLAG
(stands): Jacobson-type derivations fix G only relative to the entropy coefficient; earn it from
the framework's own counting or the claim is circular.

## 4. The mandatory cognate

Lloyd (2005), quantum gravity from quantum computation: geometry from a computation's causal
structure, Einstein--Regge dynamics from action-as-operations (Toffoli's move made
general-relativistic). Closest prior art; engage early. **Differentiator:** Lloyd's computation is
generic; ours is specified — derived particle content, FANOUT boundary, wire structure, Standard
Model attached. Lloyd: some computation yields a geometry. Framework: this computation yields this
universe, predictions included. Shared foundations: Toffoli action-as-computation (toffoli_2003
already in Paper 1's bibliography), Margolus--Levitin (Physica D 120, 188 (1998) — key to mint at
Paper-2 drafting).

## 5. Caution flags

1. "Computable step" must mean ORTHOGONALISING transition or ML does not bind. FANOUT's images are
   orthogonal by construction, so the framework's counted events are the right kind — make the
   definition say so explicitly.
2. The stress tensor exceeds (E, p): pressure and shear are momentum FLUX. The computational
   reading of flux-of-marks-across-a-surface is open; smells tractable (wire-crossing bookkeeping)
   but unwritten.
3. One-bit-per-closed-curve vs the Deutsch / Aaronson--Watrous CTC-computation literature:
   different claims, same objects; map the interface before a referee does.

## 6. First computations (Paper 2's early spine)

1. Formalise the (E, p) <-> count-density dictionary as a proposition conditional on
   op:comp-metric; state the hbar bookkeeping exactly.
2. The Newtonian limit: does computational-load-slows-clocks give the 1/r potential? Check against
   Lloyd's Regge construction — the first place the identification can fail quantitatively.
3. The equivalence-principle derivation drafted from ML blindness; find what extra premise (if
   any) it secretly needs.
4. The G normalisation, now sharpened: derive the O(1) coefficient lambda/l_P (bits per
   bit-pair) from the one-bit-per-closed-curve quantum, handling the minimal loop's
   circumference-vs-area bookkeeping explicitly; the dimensionful part of G is already understood
   as pure unit conversion (native A = -S).
5. The pressure/flux reading: define marks-across-a-cut and check the perfect-fluid form.

## 7. Relations

Paper-1 anchors: op:comp-metric (the gate), op:three-dimensions, the Unruh derivation, the
Jacobson subsection and entropic-gravity paragraph (sec:jacobson), the one-bit-per-curve pricing,
toffoli_2003. The spacetime section's closing already defers "the deepest to a second paper" —
this document is that deferral's first payment. Suite position: Paper 2's opening movement; the
FANOUT-as-causal-dressing programme is its second.
