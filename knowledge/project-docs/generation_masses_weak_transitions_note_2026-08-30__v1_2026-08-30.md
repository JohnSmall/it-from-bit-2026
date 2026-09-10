# Generation Masses and Weak Transitions under the psi-Orbit (2026-08-30)

Session note. JS asked how the sedenion mechanism (generations = the psi-orbit of the three
octonion halvings; Aut(S) = G2 x S3 a DIRECT product) squares with (Q1) the generations having
different masses -- an exact automorphism naively forces degeneracy -- and (Q2) the weak force
inducing transitions between generations, when flavour is supposed to be conserved and
ungauged. The corpus contains every ingredient of the answer (masses section: prop:koide,
eq:z3, the mass-vs-weak-eigenstates subsection, op:koide-delta, op:cabibbo, op:sector-scales,
op:colour-correction; interactions section: prop:fcnc, prop:neutral-blind, the beta-decay
circuit; sedenion section 2026-08-27/30; fourth-qubit doc Conjecture 2), but the connective
tissue was unwritten and the mass machinery's grounding language ("J3(O) triality", "the three
off-diagonal entries") predates the two-triples correction. This note assembles the account at
its recorded statuses; nothing is upgraded; the genuinely new identifications are marked NEW
(candidate).

## 1. Q1 -- an exact S3 and unequal masses: equivariance, not invariance

An exact symmetry of the ALGEBRA forces degeneracy only in observables INVARIANT under it.
Mass is not such an observable. Mass is associator debt read against the FANOUT frame -- the
selected complex direction and its reading context -- and psi does not fix the frame: notebook
T established Fix(psi) = span{1, u} exactly, so psi fixes the real axis and the tag direction
only and rotates every other direction, the selected one included, by a third of a turn into
its doubled partner. The three generations are therefore three EXACT psi-copies of one
structure held at three orientations relative to the frame; the debt is orientation-dependent;
three orientations, three masses. Nothing breaks. The mass functional was never S3-invariant,
only S3-EQUIVARIANT: applying psi permutes the masses without changing the set.

The symmetry's exact content then sits precisely where the framework's formula has exactness:

- exactly three (the order of psi) -- established;
- exact 120-degree spacing: the cos(2 pi k / 3) of eq:z3 IS the orbit -- the ansatz's Z3 is
  the psi-orbit's projection (NEW grounding, candidate; the standing J3(O)-triality grounding
  is untouched and the two should be stitched, not swapped);
- hence the Koide ratio 2/3 EXACT and delta-independent (prop:koide, from alpha = sqrt2
  alone). NEW identification (candidate): **the Koide relation is what survives of the S3 in
  the mass sector** -- the invariant of the orbit. Degeneracy was never the symmetry's
  prediction; the 2/3 was. A broken symmetry would generically spoil it; an exact symmetry
  with a frame-referenced observable protects it;
- identical gauge quantum numbers across generations (the direct product: psi commutes with
  G2) -- established.

The empirical pattern -- generations identical in every gauge respect, differing only in the
frame-referenced quantities, mass and mixing -- is thus the SIGNATURE of an exact family
symmetry plus a frame-referenced debt, not evidence against one. (NEW framing, candidate.)

Component reading of eq:z3 under the psi-orbit (NEW, candidate): the "1" is the projection on
the psi-fixed line <1, u> -- the same invariant line the sterile class occupies; the rotating
cosine is the component in the (a, au) planes psi turns; alpha = sqrt2 is the doubling norm
|1 + u|, the diagonal of the halving (consistent with the section's existing derivation of
alpha); delta is the frame's offset from the orbit's reference orientation, and its matched
value 2/9 = dim C / dim(O + R) reads as exactly that -- the preferred plane against the
frame's nine-dimensional ambient. delta remains MATCHED, not derived: op:koide-delta is
unchanged and remains the mass sector's central open calculation. Sector structure (alpha^2 =
2 + 2|Q|^{3/2} x colour; dilution delta/n) = sector-dependent frame coupling; op:sector-scales
and op:colour-correction open as recorded; op:up-quark's cross-halving pricing carries its
owed notebook re-run (corrections ledger item 4).

Picture (for prose use): three identical clock hands at exact 120 degrees; mass is the shadow
each casts on a wall set at angle delta to the face. Identical hands, exact spacing, wildly
different shadows; turning the face a third of a turn permutes the shadows without changing
the set; and the one exact relation among the shadows -- the 2/3 -- is the trace of the exact
spacing.

## 2. Q2 -- why the weak force "changes generation": a blind gate across two frames

Layered, each layer at its recorded status:

1. The weak force cannot COUPLE to generation: the family factor is the component group, no
   Lie algebra, no charge (established; direct product; the splice's "no qubit to act on").
2. Because every gauge gate is generation-blind, it is the identity on the family index --
   diagonal in EVERY generation basis. For neutral currents that is the whole story:
   V^dag (c 1) V = c 1 (prop:fcnc) -- GIM FORCED, not arranged; strengthened at vertex level
   by prop:neutral-blind; loop-level processes proceed through charged pairs exactly as
   observed; the no-mediator floor is the falsifiable content.
3. The charged current differs not by seeing the tag -- it does not -- but by changing the
   REGISTER: the W flips the B-qubit (the executed beta-decay circuit: one X on B; "the W
   changes the bracketing"). It changes what the fermion IS (its doublet slot) and hence the
   debt structure it carries, while never touching the family label.
4. "Generation," as measured, is the mass basis -- the debt-diagonalising basis -- and the
   debt is frame-referenced PER SECTOR (sector-dependent alpha and dilution), so the up-type
   and down-type mass bases are two different alignments of one family space against the
   shared weak (doublet) basis.
5. A tag-blind B-flip therefore connects two differently aligned bases; the bookkeeping of
   one against the other is a unitary, V = U_u^dag U_d -- the CKM -- with unitarity (hence
   GIM again, hence the loop floor) automatic from blindness.
6. Plain statement: the W does not induce generation transitions; it induces SECTOR
   transitions, and generation-change is the bookkeeping shadow of a blind gate crossing two
   frames. What every vertex conserves is the family-space label (neutral by
   prop:neutral-blind; charged by locality on B); what a sector flip cannot conserve is the
   sector-relative mass label, because "which mass eigenstate" is not a frame-independent
   fact across the flip.
7. One geometry, two shadows: the first mismatch angle sits at the SAME 2/9 that offsets the
   masses (Cabibbo ~ delta, suggestive + executed at the per-cent level; op:cabibbo). The
   hierarchy and the mixing are both frame-offset readings of the one orbit. Amplitude seat:
   the cross-halving / zero-divisor sector (the planes psi rotates); mixing obligatory by
   no-AME(4,2); near-diagonality (quarks) vs large mixing (leptons) is the open frame-vs-
   state coupling question (fourth-qubit Conjecture 2; re-runs owed post-correction).

## 3. Offered stitches (JS's call; nothing patched)

(a) One sentence in the masses section re-grounding eq:z3's Z3 on the psi-orbit alongside the
J3(O) reading, with a pointer to rem:two-triples. (b) One clarifying paragraph candidate for
the sedenion section's summary or mixing subsection carrying the equivariance point and the
"Koide 2/3 = the surviving S3" identification, at candidate status. (c) The clock-hands
image, if wanted, belongs beside prop:koide.

## 4. Status ledger

Established/structural: direct product; Fix(psi) = <1,u> (notebook T); prop:koide (2/3 from
alpha = sqrt2); prop:fcnc; prop:neutral-blind; mass-vs-weak-basis mismatch = CKM. Executed:
Cabibbo circuit (per-cent); beta-decay circuit (hardware). Matched: delta = 2/9
(op:koide-delta). NEW today (candidate): the equivariance resolution as stated; eq:z3's
component reading on the psi-orbit; Koide-2/3-as-orbit-invariant; the signature framing;
"sector transitions, not generation transitions" as the charged-current statement. Open, as
recorded: op:koide-delta, op:cabibbo, op:sector-scales, op:colour-correction, op:up-quark
(+ owed notebook re-runs per the corrections ledger).
