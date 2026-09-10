# The Metric Identification: Space of Computations = Spacetime of GR

**Session document, 2026-07-07.** Seeds the central identification of Paper 2 (the dynamical
layer). Prompted by JS's observation: GR defines the metric via energy--momentum; the framework
defines it via computable/non-computable step counts; Toffoli and Margolus identify energy with
computation; therefore the two metric definitions may be one. Verdict of the session: they are,
with a precise shape. Status vocabulary as ever: proved / structural / candidate / owed / open.

## 0. Provenance (added 2026-07-07)

The imaginary-units convention dates to JS's CASYS paper (Small, 2006, small_2006): p. 14 carries
counting non-causal steps in imaginary numbers, the parallelisable-spheres step, AND the
open-problem flag on its proof — op:comp-metric's direct ancestor, twenty years old. The paper now
says so at the convention's first statement. Verified from the OCR sidecars inside the project's
zip bundle (the bundles are machine-readable after all; earlier verdict corrected).

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
UPGRADED 2026-07-07 (JS found arXiv:2510.24491, Dorau & Much, PRL 2026): the Jacobson leg is now
PAVED with modular-theoretic rigour — relative entropy (Araki--Uhlmann) between vacuum and coherent
excitations on a bifurcate Killing horizon = energy flux; assume S = A/4G hbar; semiclassical
Einstein equations follow. THE INTERFACE: their hypothesis is our conjecture's conclusion. Paper 2
no longer defends Jacobson's heuristics; it supplies Dorau--Much's two inputs — the entropy--area
law (from counting: native A = -S, coefficient triple-routed) and the local horizon/modular
structure (op:comp-metric's job, now with a precise target and a quality bar: the network's wedge
structure must eventually meet modular-theory standards). Their coherent-state scope = our locked
(high-R) regime; the low-R complement stays the framework's nascent-geometry territory. Their
reference trail (Longo 2019; Hollands; Casini--Grillo--Pontello; Alonso-Serrano et al.) is Paper
2's cognate bibliography ready-made. Key: doraumuch2026relative (RIS delivered).

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

## 3b. The four-constant junction: graded FANOUT as the mechanism under Jacobson
(Added 2026-07-07, JS's synthesis: graded FANOUT + measurement-creates-relations => the creation
of spacetime relations is graded and thermodynamically locked => c, hbar, G, k_B link.)

**One event, four invoices.** A graded-FANOUT locking (copy fires -> Zurek redundancy ->
Landauer-paid permanence) IS the creation of a spacetime relation, billed in four currencies at
once: a step (c: one bit of relation per causal step), an orthogonalising transition (hbar:
Margolus--Levitin rate pricing), a paid bill (k_B: Landauer k_B T ln 2 per locked bit — k_B joins
the quartet as the bits<->thermodynamic-entropy exchange, natively 1), and an area increment (G:
one bit-pair, 4 ln 2 l_P^2). The four constants are the four exchange rates from one native ledger
(steps, bits) into human units; they "link" because they were never four things.

**The junction identity.** One locking at Unruh temperature:
  dQ / T  =  k_B ln 2 . dN_bits  =  (k_B c^3 / 4 G hbar) . dA
— each equality one exchange rate. Fed to Jacobson's Clausius relation, hbar and k_B CANCEL,
leaving Einstein's equations in G and c alone: the quantum and thermal constants are scaffolding
conversions that drop out of the geometric law. SELF-CHECK RULE for all Paper-2/3 derivations: no
final geometric equation of the framework's may contain hbar or k_B.

**What R-grading adds to Jacobson: a nascent regime.** Low-R relations are tentative spacetime —
the WF reconciliation's phase recovery acquires a geometric reading (Wigner undoing the friend's
record = un-forming a relation before its Landauer bill is paid); high-R relations lock and
spacetime grows by one event. Sequential growth: direct conversation with Rideout--Sorkin causal-set
growth dynamics (the Dowker lineage, second entrance — the first was co-events in the FANOUT
section). Candidate reading: superposed geometry = low-R relational structure (the pre-locking
stretch of the existing ladder), quantum gravity's regime without new formalism. Status: the
relational thesis at its structural flags; permanence is FAPP (the WF register, kept).

**Relative entropy as the nascent regime's currency (via Dorau--Much's toolkit).** Araki--Uhlmann
relative entropy is defined for any state pair, basis-free, and monotone under channels — so the
R-grading becomes a data-processing statement (each copy step a channel; monotonicity IS the
irreversibility grading) and the Landauer bill is what its modern proofs already are, a
relative-entropy inequality. The graded-FANOUT locking, rephrased: relative entropy of the record
to its erased counterpart, flowing one way.

**The coefficient, triple-routed.** The O(1) owed (bits per bit-pair, lambda/l_P) now has three
independent routes: the CTC-quantum pricing, the Bekenstein normalisation, and NEW — the
Landauer--Unruh energy audit (energy of one locking at the recorder's Unruh T, demanded consistent
with the area increment). Over-determination available before drafting begins.

## 3c. The ontology gap in Dorau--Much, and its dissolution
(Added 2026-07-07, JS's criticism: they use the non-dynamical, ontic spacetime of QFT/SR as the
arena and derive the dynamical, relational, epistemic spacetime of GR — apparently without
noticing.)

**The gap, sharpened.** Modular theory is background-ANCHORED at every joint: relative entropy
needs a vacuum; the vacuum needs a wedge algebra; the wedge needs a bifurcate Killing horizon; the
flow needs the boost field. All live on a fixed, per-solution non-dynamical arena. The output —
the semiclassical Einstein equations — retroactively contradicts the ontological status of the
inputs. Their rigour makes the anchoring MORE visible than Jacobson's heuristics did.

**Their available defence, and its limit.** Self-consistency/bootstrap: only local flatness is
assumed, which the derived theory's own equivalence principle guarantees. Answers the technical
circularity; does NOT answer the ontic/epistemic cut — the local patch is still treated as
ontically given.

**The dissolution (the framework's, at structural status).** The fixed background IS the
post-FANOUT description: the arena as recorded, locked, shared at high R — epistemic-made-rigid
(Di Biagio--Rovelli stable facts, applied to the stage). The dynamical relational layer is the
nascent locking of §3b. Relocated, Dorau--Much's theorem is the INSIDE VIEW deriving the law its
own arena must satisfy — Lawvere's shape, IOEP — non-circular once the two-level (F1) vocabulary
is supplied. Corollary 1: semiclassicality (⟨T⟩ not T-hat) is the exact law of the locked regime,
not an approximation — their coherent-state scope was the theorem announcing its own domain.
Corollary 2: local flatness = locally uniform locking — a second derivation-shaped reading of the
equivalence principle, beside ML-blindness.

**Consequence for the pitch.** The interface upgrades from "we supply their inputs" to "we supply
their ONTOLOGY": Paper 2 offers the account under which their derivation does not consume what it
produces. Leipzig conversation shape: the criticism is the opener, the dissolution is the gift.
FLAG: the dissolution is a structural reading until op:comp-metric delivers the record-side chart
and wedge structure from the network — the gap is named and its filling proposed, not yet filled.

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
6. The Landauer--Unruh route to the coefficient: energy audit of one locking, cross-checked
   against routes one and two; if the three agree, the coefficient is over-determined.
7. Formalise the nascent regime: low-R relational structure as superposed geometry; state what
   the WF reconciliation's phase recovery means geometrically, at candidate status.
8. Add Rideout--Sorkin sequential growth to the cognate map beside Lloyd and Jacobson; state the
   framework's differentiator (the identity of the growth event: a FANOUT crossing its redundancy
   threshold).
9. Write the two-level relocation of Dorau--Much as a short section: the ontology gap, the
   bootstrap defence and its limit, the post-FANOUT reading of the fixed background,
   semiclassicality as the locked regime's exact law, uniform-locking as the equivalence
   principle's second face. This is Paper 2's philosophical spine and its opening claim on the
   Leipzig programme.

## 7. Relations

Paper-1 anchors: op:comp-metric (the gate), op:three-dimensions, the Unruh derivation, the
Jacobson subsection and entropic-gravity paragraph (sec:jacobson), the one-bit-per-curve pricing,
toffoli_2003. The spacetime section's closing already defers "the deepest to a second paper" —
this document is that deferral's first payment. Suite position: Paper 2's opening movement; the
FANOUT-as-causal-dressing programme is its second.
