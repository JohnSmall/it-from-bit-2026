# The Classification Ledger and the D4 Arena

**Session document, 2026-08-16.** JS's observation, verbatim in spirit: the tower's progression
-- structure at the fourth wire, nothing at the fifth -- must be reflected in the classifications
of n-qubit entanglement for n > 2. Verdict of the session: exact, and theorem-grade on both
sides, with the crossover at the same wire; moreover both the last type-complete rung (three
qubits) and the label rung (four qubits) live inside the single Lie algebra whose diagram
symmetry is the triality S3 the sedenion doubling promotes. That identification supplies
Conjecture 1 of the fourth-qubit document with the arena it has lacked. Status vocabulary
throughout: established / structural / candidate / conjecture / RHYME / open. Spine material for
the follow-up paper; nothing here touches Paper 1.

## 0. Scope and non-claims (recorded)

- This note is state-side. The flavour-conservation splice and its REV (the no-force
  propositions, the Klein grading, op:graded-dynamics) are untouched by everything below: the
  arena concerns moduli of states, not connections or currents.
- Two moduli spaces are now in play this week and they are DIFFERENT OBJECTS: the CP^2 of
  octonion copies through the core (constructor note 2026-08-12, copies-through-the-spine) and
  the Cartan quotient h / W(D4) of the four-qubit grading (this note). Relation: open. Do not
  conflate them in spine text.
- Several citations below are from memory; the whole batch is refs-first gated (section 10).

## 1. The classification ledger (established)

- n = 2: one entangled SLOCC class (Bell). A list of length one.
- n = 3: Dur-Vidal-Cirac -- six orbits in total, two genuinely tripartite (GHZ and W).
  Finitely many; the classification is a list. (Key in library; VERIFY-KEY at refs-first.)
- n = 4: Verstraete-Dehaene-De Moor-Verschelde -- nine families, but the generic family
  G_abcd carries continuous complex parameters: infinitely many inequivalent states. The
  classification stops being a list and becomes a moduli space.
- n >= 5: the moduli dimension grows exponentially (2^n - 1 - 3n) and the invariant theory is
  wild; the five-qubit invariant ring is already not free (Luque-Thibon 2006).

Types at two and three wires, moduli at four, wilderness after: the tower's own rhythm --
forces, then copies-with-mixing, then hosting.

## 2. The engine, entanglement side (established arithmetic)

The SLOCC group SL(2,C)^n has complex dimension 3n; the projective state space has dimension
2^n - 1. The ledger:

    n      dim group (3n)    dim space (2^n - 1)
    2          6                    3
    3          9                    7
    4         12                   15
    5         15                   31

At n = 3 the group still dominates: C^2 (x) C^2 (x) C^2 is a prehomogeneous space, the GHZ
orbit is dense, Cayley's 2x2x2 hyperdeterminant (degree 4) is the relative invariant, and
finiteness of the classification follows. At n = 4 the group is smaller than the space for the
first time: at least 15 - 12 = 3 continuous projective invariants MUST appear -- exactly
Verstraete's count (four generators on the linear space, three ratios projectively). Linear
symmetry supply against exponential structure, crossover between the third and fourth wire.

Same address as Adams: the entanglement fibrations the paper already inhabits -- S7 -> S4
(Mosseri-Dandoloff, two qubits), S15 -> S8 (Bernevig-Chen, three qubits) -- exist exactly on the
finite-classification rungs, and Adams removes S31 -> S16 exactly where the moduli switch on.
Two theorems, one wall.

## 3. Type and state, restated with proofs attached (structural)

Coecke-Kissinger: no new entanglement primitive exists at four wires. The monogamy document:
the four-qubit constraints decompose into the two- and three-qubit ones. So the continuous
parameters that appear at n = 4 cannot be new TYPES; the invariant theory is reporting a
continuous family of inequivalent ways to RELATE the wires using only the old primitives. A
continuous, SLOCC-inequivalent relation between a register and a tag wire is a mixing structure
in invariant-theoretic clothing. The corpus slogan thereby acquires a proof-shaped restatement:

    finite orbit list  = type regime (n <= 3);
    onset of moduli    = state regime (n = 4);

and the first moduli in the history of the tower appear on the wire that carries the generation
label. Status: the two inputs are established; the reading is structural.

## 4. The D4 identification: both rungs inside one algebra (established mathematics)

The headline. The four-qubit state space is not merely analysed by Lie theory; it IS a graded
piece of a Lie algebra, and so is the three-qubit space -- the SAME Lie algebra, D4 = so(8),
the unique simple diagram whose symmetry group is S3.

**(a) The Z2-grading houses four qubits.**

    so(8) = sl(2)^4 (+) (2,2,2,2),    dimensions 12 + 16 = 28.

(Real form so(4,4) in the black-hole/qubit literature.) Four-qubit SLOCC classification is
Vinberg theta-group theory for this grading: the Cartan subspace h in the (2,2,2,2) piece has
dimension 4; Verstraete's generic parameters a, b, c, d are coordinates on h; the little Weyl
group is W(D4); the ring of SLOCC invariants is FREE on generators of degrees 2, 4, 4, 6
(Luque-Thibon 2003) -- precisely the Weyl invariant degrees of D4 (for D_n: 2, 4, ..., 2n-2;
n). The nilpotent-orbit side gives the family classification (Chterental-Djokovic; Borsten-
Dahanayake-Duff-Marrani-Rubens 2010: 31 real classes, 9 complex families).

**(b) The five-grading houses three qubits.**

    so(8) = 1 (+) (2,2,2) (+) (sl(2)^3 (+) C) (+) (2,2,2) (+) 1,
            dimensions 1 + 8 + 10 + 8 + 1 = 28.

This is the Freudenthal-triple-system grading; the FTS rank stratification 1, 2, 3, 4 is
exactly separable / biseparable / W / GHZ (Borsten-Dahanayake-Duff-Ebrahim-Rubens 2009). So the
last type-complete rung and the label rung are the two canonical gradings of one algebra.

**(c) Triality acts, and the Klein group reappears.** Under sl(2)_A (+) sl(2)_B (+) sl(2)_C
(+) sl(2)_D inside so(8), the three eight-dimensional representations decompose as

    8_v = (2,2,1,1) (+) (1,1,2,2),
    8_s = (2,1,2,1) (+) (1,2,1,2),
    8_c = (2,1,1,2) (+) (1,2,2,1):

the three 8's are the three ways of PAIRING the four legs, {AB|CD}, {AC|BD}, {AD|BC}. Triality
permutes the pairings; the natural map S4 -> S3 (wire permutations to pairing permutations) has
kernel exactly the Klein four-group V4 of double transpositions, S4 / V4 = S3 = Aut(V4). The
same pair (V4, S3 = Aut(V4)) that organises the sedenion side -- sectors graded by K = Z2 x Z2,
generations permuted by S3 = Aut(K) -- organises the Lie side: a three-element set canonically
built from a four-element structure, with the Klein group as the silent kernel. Recorded as a
RHYME with a candidate shape; its precise statement is checklist item 2, and the naive full-S4
equivariance is the WRONG ask, because the register's wires are rung-broken (the fourth wire is
a tag, not a symmetric leg). Both S3's are literally Spin(8) triality -- the sedenion S3 by the
promotion theorem (mechanism document, section 1), the diagram S3 by definition -- so the
candidate is that they are ONE action seen twice, and proving that is Conjecture 3(a) below.

## 5. Five wires: no host (established by the arithmetic here; one clause refs-gated)

For (sl(2)^5, (2,2,2,2,2)) to repeat the pattern, a simple graded Lie algebra would need it as
(g_0, g_1). Dimension arithmetic closes every shape:

- Z2-graded: dim g = 15 + 32 = 47. No simple Lie algebra has dimension 47.
- 3-graded: dim g = 32 + 16 + 32 = 80. The only simple algebra of dimension 80 is sl(9), whose
  3-gradings have g_0 = sl(p) (+) sl(q) (+) C (p + q = 9), never sl(2)^5.
- 5-graded (FTS shape): dim g = 1 + 32 + 16 + 32 + 1 = 82. No simple algebra has dimension 82.

And on the Vinberg/Kac side, (2,2,2,2,2) appears on no theta-representation list (Kac 1980;
VERIFY at refs-first). After D4 there is no Lie-theoretic host; the classification goes wild
independently of the tower. "Nothing more at five" holds in invariant theory on its own.

## 6. Conjecture 3 -- the Cartan arena (CANDIDATE; numbering continues the fourth-qubit doc)

**Statement.** The physical mixing data of the four-wire register live on h / W(D4), the Cartan
quotient of the Z2-grading of D4, with the generation S3 acting on h through triality. CKM and
PMNS parameters are coordinates on this quotient; generation rebasings act by the diagram
symmetry; and the AME-deficit geometry of Conjecture 1 becomes computable in the degree-
{2, 4, 4, 6} invariants.

**Clause (a) -- the map, with the Cabibbo rung as gate.** Construct the explicit map from the
framework's four-wire states (tag coupled within the leptonic ninth) to points of h / W(D4),
architecture-respecting (rung-broken S4), such that the register's generation S3 descends to
the triality action. PASS: the executed Cabibbo circuit (R_y(2 * 2/9); Paper 1, hardware-
confirmed) lands as a computable coordinate with lambda = sin(2/9) recovered. FAIL: the
register S3 does not descend to triality, or the Cabibbo point has no finite image.

**Clause (b) -- Higuchi-Sudbery re-derived in the arena.** Express the all-marginals-maximally-
mixed condition in the four invariant generators. PASS: the conditions are shown incompatible
-- AME(4,2) nonexistence reproved inside the grading -- yielding a quantitative deficit
function on h whose minimum locus bounds the mixing angles (the standing target of Conjecture
1). FAIL: the conditions admit a common zero (which would contradict the theorem and hence
expose an error in the map, a useful failure).

**Parameter count (RHYME only, flagged).** Four complex Cartan coordinates against the CKM's
four real parameters (three angles, one phase). Real against complex, no map yet; recorded as a
rhyme, not a derivation. PMNS Majorana phases, if physical, need structure beyond h --
plausibly the sterile / S3-invariant sector; open.

## 7. Risk items (honesty ledger)

1. Real forms matter: the black-hole literature works in so(4,4); which real form the
   framework's register selects (and what the physical orbits are) is unaudited. Checklist 5.
2. The rung-broken S4: any equivariance statement must be formulated for the architecture's
   actual symmetry, not the naive wire-permutation group. Overclaiming here would poison
   clause (a).
3. Memory-sourced citations throughout; nothing enters spine text before the refs-first gate.
4. The CP^2 of copies and h / W(D4) are distinct moduli; the temptation to identify them is
   noted and resisted until a theorem does it.

## 8. Checklist (ordered)

1. Refs-first: verify the batch of section 10 (companion RIS delivered this session); confirm
   the in-library keys (Dur-Vidal-Cirac, Mosseri-Dandoloff, Bernevig-Chen, Coecke-Kissinger).
2. Write the pairing-degree bridge precisely: the architecture-respecting subgroup of S4, its
   image in S3, and the candidate bijection {wire pairings} <-> {nontrivial Klein degrees};
   PASS/FAIL as an equivariance check on the C^16 = C (x) S identification.
3. Clause (a) on the Cabibbo rung only: one angle, one coordinate, lambda = sin(2/9) in or out.
4. Clause (b): the marginal conditions in the degree-{2,4,4,6} generators; attempt the
   incompatibility proof; extract the deficit function.
5. Real-form audit (risk 1).
6. Only then: spine text for the follow-up paper (this note's sections 1-5 are its skeleton),
   and the one-line relation update in the fourth-qubit document pointing Conjecture 1 here.

## 9. Relations

Fourth-qubit doc 2026-07-06: Conjectures 1 and 2; this note supplies Conjecture 1's arena and
continues the numbering. Mechanism doc 2026-07-10: sections 1-2 (the promotion theorem; the
Klein grading -- now echoed as the V4 kernel of S4 -> S3). Flavour splice 2026-08-12 + REV
2026-08-15: unaffected (state-side note); op:graded-dynamics clauses (a)/(b) live upstream of
everything here. Constructor note 2026-08-12 (CP^2 of copies): distinct moduli, relation open
(section 0). Monogamy document: the four-qubit ring impossibility and constraint decomposition
(input to section 3). Paper 1: the dictionary section (Dur-Vidal-Cirac, Mosseri-Dandoloff,
Bernevig-Chen, Coecke-Kissinger already cited there), sec:budget-converse (the leptonic ninth),
op:cabibbo (clause (a)'s gate).

## 10. Refs-first batch (ALL VERIFY-CITE; companion RIS: refs_d4_arena_2026-08-16T0522.ris)

- verstraete2002fourqubit -- Verstraete, Dehaene, De Moor, Verschelde, "Four qubits can be
  entangled in nine different ways", Phys. Rev. A 65, 052112 (2002).
- luquethibon2003 -- Luque, Thibon, "Polynomial invariants of four qubits", Phys. Rev. A 67,
  042303 (2003). [Degrees 2, 4, 4, 6.]
- luquethibon2006 -- Luque, Thibon, "Algebraic invariants of five qubits", J. Phys. A 39, 371
  (2006). [Non-free ring; section 1's n >= 5 clause.]
- borsten2009freudenthal -- Borsten, Dahanayake, Duff, Ebrahim, Rubens, "Freudenthal triple
  classification of three-qubit entanglement", Phys. Rev. A 80, 032326 (2009).
- borsten2010fourqubit -- Borsten, Dahanayake, Duff, Marrani, Rubens, "Four-qubit entanglement
  classification from string theory", Phys. Rev. Lett. 105, 100507 (2010).
- levay2006 -- Levay, "On the geometry of four-qubit invariants", J. Phys. A 39, 9533 (2006).
- chterentaldjokovic2007 -- Chterental, Djokovic, "Normal forms and tensor ranks of pure states
  of four qubits", in Linear Algebra Research Advances (Nova Science, 2007); arXiv:quant-ph/
  0612184.
- vinberg1976 -- Vinberg, "The Weyl group of a graded Lie algebra", Math. USSR-Izv. 10, 463
  (1976).
- kac1980 -- Kac, "Some remarks on nilpotent orbits", J. Algebra 64, 190 (1980). [The theta-
  representation clause of section 5.]
