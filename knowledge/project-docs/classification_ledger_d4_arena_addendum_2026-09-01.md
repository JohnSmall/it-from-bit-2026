# Addendum to the Classification Ledger and the D4 Arena: the sedenion S3 on the arena

**Addendum, 2026-09-01**, to `classification_ledger_d4_arena_2026-08-16T0522.md`. Section
numbering continues the ledger (sections 0-10 there; 11 onward here). Status vocabulary as in
the ledger: established / structural / candidate / conjecture / RHYME / open. Nothing here
touches Paper 1. Feeds: ledger section 0 (the moduli-objects caution), 4(c) (triality and the
Klein kernel), 6 (Conjecture 3, clause (a)), 7 (risk items), 8 (checklist items 2 and 3), and,
outside the ledger, op:hopf-frobenius and the monogamy document's bridge point (C).

Inputs: the zero-divisor arc (session note `session_note_zero_divisor_arc_2026-08-31.md`, three
scripts) and the arena probe `arena_psi_probe_2026-08-31.py`. Reproduction: the probe was run on
the second environment on 2026-09-01 with seed-locked values bit-identical (arena deviation 5.429;
sterile-overlap sequence 1.28e-01, 7.50e-02, 1.79e-02), last-digit float noise only. Everything
labelled "established" below is double-verified unless stated.

Indexing convention of the probe: C^16 = C (x) S with k = 8 q1 + 4 q2 + 2 q3 + q4, so the TAG is
wire 1 and the register is wires 2-4. The ledger's prose calls the tag "the fourth wire"; the two
are a relabelling and nothing below depends on it. Algebra convention A as in the arc scripts.

## 11. The sedenion S3 at gate level (established)

The arc's closed form on the algebra side is psi = identity on the tag plane <1, e8>, right
multiplication by omega = exp(2 pi e8 / 3) on its 14-dimensional complement; tau = e8-flip;
<psi, tau> = S3, psi commuting with the diagonal G2. Read on the four-wire register these are:

  tau = Z on the tag wire  (local; det -1, i.e. SLOCC up to the global phase of iZ in SL(2)).

  psi = R_tag + (I - R_tag) P_sterile,

where R_tag is the real rotation by a third of a turn on the tag wire (an element of SU(2), hence
SLOCC-local) and P_sterile projects onto the sterile plane

  span{ |t, 000>_reg : t = 0, 1 }  =  the tag plane <1, e8>  =  Fix(psi).

In words: psi is a third-turn rotation of the tag controlled on the register being away from its
vacuum. The generation step is a context-conditioned gate by construction; the cp-context note's
"frozen context" reading gets a literal circuit. psi^3 = 1 on states and on invariants.

## 12. The sterile-support theorem (established)

On states with no sterile-plane overlap (z_{|0,000>} = z_{|1,000>} = 0), psi coincides with
R_tag (x) 1, a local SU(2) gate, and is therefore trivial on h / W(D4). Dialling the overlap to
zero sends the arena motion monotonically to zero (probe: 1.28e-01, 7.50e-02, 1.79e-02, 0 for
overlap weights 1, 1/2, 1/10, 0). tau is trivial on the arena for every state.

Statement for the ledger: within the sedenion S3, the Z2 is invisible to h / W(D4) everywhere,
and the Z3 is visible only through the state's sterile component. Whatever the generation step
does to mixing moduli, it does through the sterile line -- the same sector the ledger's
parameter-count remark reserved for Majorana-phase structure (section 6) and the cp-context note
assigned to CP.

## 13. Non-descent, and what it does to clause (a) (computed, established as a negative)

(i) Naive pushforward does not descend. Two SLOCC-equivalent states map under psi to different
arena points (probe: same invariant multiset in, different multisets out). So "apply psi" is not a
map on h / W(D4).

(ii) On a generic G_abcd the motion is outside W(F4). The probe's invariant map works in squared
coordinates (eig(B B^T) = {a^2, b^2, c^2, d^2}, self-calibrated at the pairing 12|34 with the
magic basis, exactly SL(2)^4-invariant). On squares W(D4) collapses to permutations, and W(F4)
acts through exactly three cosets of W(B4): the identity; the reflection in the short root
(1/2)(1,-1,-1,-1) -- this is the half-Hadamard H4 (trace 2, a single reflection); and H4
composed with one coordinate sign flip, which lies in the third coset because H4 conjugates a
coordinate flip to a reflection in a (1/2)(+-1,+-1,+-1,+-1) root, outside W(B4). The probe's
sign sweep covered all three. The negative is therefore complete: psi's arena motion is not any
element of W(F4), in particular not the triality coset. Standard root data (Bourbaki, Planche
VIII); no new reference minted.

(iii) Consequence for Conjecture 3(a). The ledger already says the naive full-S4 equivariance is
the wrong ask; this is the state-side proof of it, together with the identification of the only
channel a genuine descent can use. Clause (a) is sharpened, not replaced:

  Clause (a'), the sterile-channel gate. The architecture map Phi must exhibit the Cabibbo
  coordinate as a function of the state's tag-plane component -- the within-the-ninth coupling
  -- and that coordinate must vanish when the sterile component is removed.
  PASS: the executed Cabibbo point (R_y(2 * 2/9)) is recovered AND removing the sterile
  component of the source state sends its arena image to the triality-fixed locus.
  FAIL: a construction in which the Cabibbo coordinate survives removal of the sterile
  component. (Any such construction contradicts section 12 for every psi-based generation step,
  so a FAIL here diagnoses the map, not the theorem.)

(iv) Consistency with the promotion theorem (structural reading). Triality is an OUTER
automorphism of Spin(8): it permutes the three 8's rather than acting inside one fixed
representation, so no fixed unitary on C^16 can realise it as a global intertwiner. The promotion
theorem (sedenion S3 = triality, algebra level) and the non-descent (state level) are the same
statement seen from two sides, not a tension. The arc's recurring motif holds a third time: psi
coincides with an official action only on a locus (the colour centre on the zero-divisor locus;
a local SU(2) off the sterile plane) and carries a localised correction elsewhere, and the
corrections are where the physics sits.

## 14. The rung-broken S4 and the pairing S3 (established; input to checklist item 2)

The architecture-respecting subgroup of S4 is the stabiliser of the tag wire, Stab(tag) = S3 on
the register wires. Its intersection with the Klein kernel V4 of S4 -> S3 (pairings) is trivial,
because every double transposition moves the tag. Hence Stab(tag) maps ISOMORPHICALLY onto the
pairing S3 = diagram triality: the rung-broken S4 is exactly triality, with the Klein group as
precisely the tag-moving part. This discharges the first half of checklist item 2 (the
architecture-respecting subgroup and its image in S3).

A concrete, convention-bound observation for the second half (the bijection with the Klein
degrees), recorded as candidate: in the probe's indexing the G--G Klein grading is literally the
basis value of register wires 3 and 4 -- core (0,0), V_1 (0,1), V_2 (1,0), V_3 (1,1) -- with the
tag and register wire 2 free inside each block; and the arc's identification V_i = colour line i
(x) tag makes wire 2 the carrier of the selected complex direction j = e4. Under a change of CD
indexing these wire labels move; the invariant content is that both the pairings and the
nontrivial degrees are S3-torsors, and the bijection between them is still checklist item 2's job.
Do not read the wire labels as physics.

## 15. Update to section 0: three moduli objects, not two (structural; relation open)

Alongside the CP^2 of octonion copies (constructor note 2026-08-12) and h / W(D4), the arc puts a
third object in play: the projectivised zero-divisor locus G2/U(2), the twistor space of
S^6 = G2/SU(3), fibred over the selected directions with CP^2 fibres of colour rays. Candidate
identification: the twistor CP^2 with the copies CP^2. Relation open; the section-0 caution is
extended from two objects to three. Do not conflate in spine text.

## 16. The crossover twinning, and the non-claim about nine (structural)

The arena's first continuous moduli (a, b, c, d) and the algebra's first continuous invariants --
the sedenion norm defect, which is the coassociative 4-form on the octonion components, and phi
-- arrive on the same wire. That is the arc's contribution to "four qubits can be entangled in
nine ways": the crossover is the same crossover, and the algebra side now has explicit twins for
the state-side moduli. On the nine families individually the arc claims nothing: they are the
Jordan strata of B B^T, and no sedenion object corresponds to them one by one. Dead-route
prophylaxis: do not attempt a families-to-sedenion-objects map.

## 17. The Coecke--Kissinger face (candidate; feeds op:hopf-frobenius, monogamy bridge (C))

The monogamy document's bridge point (C) -- "the sedenion zero divisors prevent a consistent
fibration" -- is now quantitative: the failure is the coassociative 4-form and the failure locus
is the colour geometry over the selected direction. The failure mode is the point for
op:hopf-frobenius: special means the loop is the identity, and the arc's invertibility result
(z invertible while L_z has a 4-dimensional kernel) says the loop degenerates on the zero-divisor
locus. The fourth level produces no third Frobenius species -- which would have been a new
particle type -- but a degeneracy locus of the existing special structure: moduli, not type. This
is the categorical face of the ledger's list-to-moduli crossover.

Two further readings, candidate, with the checked ingredients named: the Klein grading
V_i V_j in V_k is the basis-copying (group-like, GHZ-type) shadow of colour-line bookkeeping,
and |zw|^2 = 4 |h(x,u)|^2 is its faithfulness failure; and psi is itself a C--K diagram, a
register copy-dot on the FANOUT basis controlling a tag rotation, so the generation symmetry
requires no fourth primitive, consistent with completeness. No Frobenius structure on S has been
constructed or checked against the C--K axioms; these are readings.

## 18. Risk items added (honesty ledger, continuing section 7)

5. Squared coordinates coarsen h / W(D4) to h / W(B4): sign data is lost. The negatives of
   section 13 are unaffected; any POSITIVE descent claim will need the finer coordinates.
6. The positive characterisation of psi's action on the arena -- what it IS, as opposed to what
   it is not -- is open. Section 12 fixes the support; the functional form is not derived.
7. The probe works over C; the real-form audit (ledger risk 1) is still owed and applies here.
8. Tag-in-pair: the pairing lock 12|34 places the tag inside a pair. The negatives are
   coordinate-free by the coset argument; a reader checking the positive side should run the
   other two pairings.

## 19. Checklist updates (continuing section 8)

- Item 2 (pairing-degree bridge): first half discharged by section 14 (Stab(tag) = S3 maps
  isomorphically onto the pairing S3; V4 is the tag-moving part). Second half remains: the
  bijection with the Klein degrees; section 14's wire-label observation is an input, not an
  answer.
- Item 3 (clause (a) on the Cabibbo rung): gated additionally by clause (a') of section 13.
- New item 3b: characterise psi's arena action positively (risk 6), in the finer coordinates
  (risk 5), across all three pairings (risk 8).
- Reproduction: `sedenion_zero_divisor_scan_2026-08-31.py` is the only script of the arc not yet
  echoed on the second environment.

## 20. Relations

Ledger sections 0, 4(c), 6, 7, 8 as listed in the header. Session note of the arc
(2026-08-31): sections 2.1, 2.4, 2.6, 2.7 supply the algebra-side inputs to 11, 15, 17.
Mechanism document 2026-07-10, section 1 (promotion theorem): section 13(iv). Constructor note
2026-08-12 (CP^2 of copies): section 15. cp-context note 2026-08-16T0639: sections 11 and 12.
Fourth-qubit document 2026-07-06, Conjecture 2: untouched here, but section 12's asymmetry --
generation stepping acts on moduli only through the sterile component -- is the natural place
for its lepton/quark coupling asymmetry to be re-examined. op:hopf-frobenius and the monogamy
document, bridge point (C): section 17.
