# Session note: the zero-divisor arc (structure, masses, colour)

Date: 2026-08-31
Scope: three sessions in one thread. (1) zero divisors as structure rather than
obstruction; (2) whether that structure touches fermion masses; (3) the zero-divisor
<-> SU(3) colour dictionary.
Scripts (delivered to outputs, all checks PASS):
  - sedenion_zero_divisor_scan_2026-08-31.py      (locus, norm defect, census, psi)
  - sedenion_debt_koide_scan_2026-08-31.py        (degeneracy, rotated associator, Koide)
  - sedenion_zd_colour_scan_2026-08-31.py         (colour dictionary, derivation-built su(3))
Reproduction ledger: scripts 2 and 3 echoed back from the second environment,
seed-locked values bit-identical, deviations last-digit float noise only (different
BLAS). Script 1 delivered but NOT yet echoed; full double-verification of the arc
awaits that run.
Convention: A throughout: (a,b)(c,d) = (ac - conj(d) b, da + b conj(c)); e4 = octonion
doubling unit; e8 = tag (the u of Fix(psi) = span{1, u}). The XOR index structure is
convention-independent; signs, and which of +/- j is the annihilator direction, are not.

## 1. Question and verdict

Question posed: zero divisors have been treated negatively (they block the fourth
division algebra and the fourth Hopf fibration); does their presence carry positive
structural information about S and the three generations?

Verdict: yes, and the structure is all G2. The zero divisors are not noise on top of
S; they are the colour geometry of the selected direction, doubled through the tag.
They contribute nothing to the generation HIERARCHY (that is now a theorem, not a
scan result), but they fix where the hierarchy cannot live, they supply the two-term
shape of the Koide reading, and they identify the mixing seat with colour geometry.

## 2. Established results (STRUCTURAL / exact; machine-verified as noted)

### 2.1 The locus

Unit zero divisors are exactly z = x + y ell with x, y in Im O orthonormal; nothing
else has a kernel. The locus is V_{7,2} = G2/SU(2); the set of unit ZD PAIRS is a
single G2-orbit, a G2-torsor (Moreno 1998, moreno1998zerodivisors). Every annihilator
is exactly 4-dimensional (Biss--Dugger--Isaksen 2008, biss2008annihilators: max
annihilator dim 2^n - 4n + 4, = 4 at n = 4):

  Ann(x + y ell) = { u + (u j) ell : u in H_{x,y}-perp },   j = x y,

and the annihilator's own direction is -j (convention A). Consequence: every ZD is
gauge-equivalent to every other; the bare cross-halving vertex carries no G2-invariant
angle. This is the structural reason for the Notebook M verdict (T2 = pi/4, leakage
maximal and generation-blind; the suppression sits in the dressing).

### 2.2 Norm defect and coassociativity

Exact identity (checked to 1e-13 on both environments):

  |(a,b)(c,d)|^2 - |(a,b)|^2 |(c,d)|^2 = 2 <a, [c,b,d]>,

proportional to the coassociative 4-form (*phi) on the four octonion components. A
zero-divisor pair is the calibration bound saturated: the four imaginary components
span a coassociative 4-plane (phi restricted to it vanishes) with |a| = |b|,
|c| = |d|. The product-norm ratio |zw|/(|z||w|) ranges over [0, sqrt2]; BOTH extremes
sit on the coassociative locus, opposite orientations. So sqrt2 is the sedenion's
maximal amplification, the mirror image of the ZD bound 0.

### 2.3 PG(3,2) census

15 imaginary units = points of PG(3,2); 35 lines = quaternion subalgebras; 15 planes,
of which 8 are octonion (O and the seven doubles H_L + H_L ell) and 7 quasi-octonion,
Q_L = H_L + (H_L-perp) ell, the planes carrying the zero divisors (Cawagas 2004,
cawagas2004sedenion; de Marrais's seven box-kites partitioning the 42 assessors,
demarrais2000assessors). Lines sorted by the division count of their three planes:

  7 lines through the tag e8 : (3, 0)
  7 Fano lines inside O      : (2, 1)
  21 mixed lines             : (1, 2)

Consequences. (a) The only quaternion cores whose three 8-dim extensions are all
division algebras are those containing the tag, <1, j, ell, j ell>, a G2/SU(3) = S^6
family indexed by the selected direction j. (b) A register-internal triple cannot be
permuted by any automorphism (automorphisms preserve zero divisors): the wire on
which triality acts HAS to be the tag -- derived, no longer asserted. (c) The three
extensions of <1, j, ell, j ell> are the Cayley--Dickson doubles of the three Fano
lines through j: O_i = CD(H_{L_i}, ell), the line_i <-> O_i correspondence at algebra
level.

### 2.4 psi and the halvings

Closed form: psi = identity on <1, e8>, right multiplication by omega = exp(2 pi e8/3)
on the 14-dim complement. It is an automorphism iff omega^3 = 1 (exp(i pi/4) fails),
commutes with the diagonal G2, tau psi tau = psi^{-1}, Fix(psi) = span{1, e8}. The
halvings O omega^k have parallel components and are ZD-free; the ZD cone is the
maximally cross-halving locus (components orthogonal). The ZD locus is invariant
under the WHOLE tag circle U(1)_ell, of which only the Z3 survives as automorphisms:
the mixing seat has an accidental U(1) the algebra lacks.

### 2.5 Mass-side identities

Degeneracy theorem: the norm defect of a state against a fixed frame satisfies
Delta(z lambda, w) = Delta(z, w) for every lambda in U(1)_ell, because (*phi) is
alternating in the rotated pair. Any mass term built from the bare defect is exactly
generation-degenerate.

On orthonormal imaginary triples: |[p,q,r]|^2 = 4 (1 - phi(p,q,r)^2).

Rotated-associator identity (lambda = exp(theta e8)):

  [p lambda, q lambda, r lambda]_S = [p,q,r]_O lambda - 2 phi(p,q,r) sin(3 theta) e8.

The debt of an off-halving triple splits into an orbit part (psi rotates it) and a
tag part along e8 (psi-fixed, hence generation-universal), vanishing exactly on the
six halving angles: generation number is conserved exactly where the tag debt
vanishes. Ratio of norms:

  |orbit| / |tag| = sqrt(1 - phi^2) / (|phi| |sin 3 theta|).

### 2.6 The colour dictionary

With j = x y: j x = y, j y = -x, so span(x, y) is a complex line for L_j and
z = x + (j x) ell. Every unit x in C^3_j gives a zero divisor this way and x (j x) = j
recovers the direction: the fibration V_{7,2} -> S^6 = G2/SU(3) has fibre the S^5 of
unit colour vectors. A unit zero divisor IS a unit colour vector, doubled through the
tag.

Tag phase on a ZD = colour phase of x. psi restricted to the ZD locus coincides with
the central Z3 of SU(3)_j; off the locus they differ, and the deviation on the
direction itself has the closed form sqrt3 = |omega - 1| (the 120-degree chord). The
generation Z3 (component group, outside G2) and the colour centre Z3 (inside G2) are
globally distinct groups that agree exactly on the mixing seat: intertwiner-shaped,
which is what the shadow statement needs.

Anti-colour = tag-doubling with -j. For z colour and w anti-colour, zw lands entirely
in the core <1, j, ell, j ell> with |zw|^2 = 4 |h(x,u)|^2, h the hermitian overlap;
the 8 of 3 (x) 3bar has nowhere to live in the algebra and is killed. A zero-divisor
pair is a colour--anticolour pair with vanishing singlet contraction; the annihilator
is the perpendicular anti-colour C^2 (hence dimension 4). The epsilon channel
3 (x) 3 -> 3bar is the grading theorem verbatim: V_i V_i in H is the singlet channel,
V_i V_j in V_k is epsilon, because the G--G blocks are the three colour lines of the
selected direction tensored with the tag (L_{e4} e_i ~ e_{i+4}). Sharpens
rem:two-triples: the V-triple is the COLOUR triple; the halvings are the GENERATION
triple.

Moreno factorised: a ZD pair over j is an orthonormal colour 2-frame (third ray
forced), i.e. an SU(3) element. Built from first principles in the script
({D in Der(O) : D j = 0}: dims 14 -> 8; exponentials are automorphisms; colour
matrices special unitary; orbit map through a pair has rank 8 = the fibre dimension):
the fibre of Z = G2 over S^6 is colour SU(3) itself. Mod phases the locus is the
twistor space G2/U(2) -> S^6 with CP^2 fibres; the full pair set fibres through the
flag manifold G2/T^2. SU(3) = Stab_{G2}(j) and the C^3 split: Gunaydin--Gursey 1973
(gunaydin1973quark).

### 2.7 Invertibility

z^2 = -|z|^2: every zero divisor is a two-sided invertible element, yet L_z has a
4-dim kernel and z^{-1}(z w) = 0 =/= w. In S, irreversibility detaches from the
element and attaches to the channel: an invertible operation that destroys
information. Candidate housing: Paper 3 (FANOUT / Landauer sections).

## 3. Candidate items (grades unchanged this session)

- Koide two-term reading: sqrt(m_k) = <f, D_k> with the "1" = tag-line debt (the
  psi-fixed line, the sterile line) and the "alpha cos" = orbit debt. Closed forms
  for the equal-weight frame: U = -sqrt2 phi sin(3 theta), A = sqrt2 sqrt(1 - phi^2);
  Koide ratio = 1/3 + (A/U)^2 / 6, equal to 2/3 iff A/U = sqrt2, which at
  theta = pi/6 with equal tag/orbit weighting is phi^2 = 1/3. Three assumptions
  carried explicitly: (i) linear frame reading; (ii) theta = pi/6; (iii) equal
  weighting |f_P| = |f_ell|. Verified numerically that the ratio is 2/3 for every
  frame azimuth under (i)-(iii); the azimuth is the Koide delta, matched not derived.
- phi^2 = 1/3 <-> the W-state per-branch weight 1/3: lead only.
- alpha = sqrt2 as the sedenion amplification bound: RHYME.
- GHZ states live on the colour equator, hence arrive with a canonical zero divisor
  attached; W-class states sit off the equator and get none. Candidate relevance to
  quark-small vs lepton-large mixing (fourth-qubit Conjecture 2 territory).
- |zw|^2 = 4 |h|^2 as the seat of the colour factor in alpha^2 (op:colour-correction
  adjacency).

## 4. Closed routes (logged so they are not retried)

- delta0 from the bare zero-divisor vertex: CLOSED. The pair set is a single G2-orbit
  and the locus is U(1)_ell-invariant; no gauge-invariant angle exists there. (The
  Notebook M empirical verdict, now structural.)
- Generation triple on a register-internal core: CLOSED. The census gives (2,1) or
  (1,2) for every line not through the tag, and automorphisms preserve zero divisors.
- Mass functionals built from product norms or the bare norm defect alone: CLOSED.
  Exactly degenerate across the psi-orbit (Section 2.5 theorem).

## 5. Standing PASS/FAIL (labels to mint if promoted to the open-problems file)

1. Dressed-vertex phi^2 (checklist 3b). Build the debt triple from the dressed lepton
   state on C (x) S; evaluate phi^2. PASS: phi^2 = 1/3, discharging alpha = sqrt2 as
   an input. FAIL: anything else; the two-term shape survives, the coefficient
   returns to unexplained.
2. Dressed leakage vs delta0. Evaluate the dressed vertex along psi_lambda(z),
   lambda in U(1)_ell. Constant in lambda: FAIL (the angle is not there).
   Z3-periodic, non-constant: PASS (delta0 lives in the U(1)_ell -> Z3 breaking the
   dressing induces).
3. Reproduction completion: run sedenion_zero_divisor_scan_2026-08-31.py on the
   second environment and echo. PASS: all checks pass with seed-locked values
   matching. (Scripts 2 and 3 already double-verified.)

## 6. Incidental verifications and literature (2026-08-31 web pass)

- Eakin--Sathaye venue settled: Journal of Algebra 129 (1990), 263-278 (concordant
  across BDI's Eigentheory reference list and arXiv:1010.2156). A circulating variant
  citing Journal of Pure and Applied Algebra 129, 263-280 is WRONG (JPAA vol. 129 is
  ~1998). Clears the standing VERIFY-CITE on the venue; the S3-vs-Z2 CONTENT question
  remains with Notebook T.
- de Marrais describes Moreno's G2 result as "homomorphic"; the precise statement
  should be quoted from Moreno directly, not from de Marrais.
- Incidental find, possibly new to the library: arXiv:2306.13098, "Three generations
  of colored fermions with S3 family symmetry from Cayley-Dickson sedenions"
  (Gresnigt-adjacent; cites Gunaydin--Gursey). Not added to the batch; flag for a
  read and a priority/overlap assessment against the halvings picture.
- Companion reference if wanted later: Gunaydin & Gursey, Quark statistics and
  octonions, Phys. Rev. D 9 (1974), 3387-3391.

## 7. Files and housing

Delivered this session: the three scripts above, this note, and
zd_structure_refs_2026-08-31.ris (five entries, all web-verified, dedupe flags in
N1). Repo placement is yours; remember the Project knowledge panel sync trigger after
committing. Housing suggestions, yours to adjudicate: Sections 2.1-2.4 and 2.6 to the
sedenion/generations appendix; 2.5 and 3 to the mass-formula discussion alongside
eq:z3; 2.7 to Paper 3; Section 4 into the open-problems file's closed-routes log; the
census lemma (no S3 on register-internal triples) into Notebook T's preamble.
