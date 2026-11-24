# Qutrits in the Hopf picture: the colour equator, its phase circle, and the singlet as a quaternion triple

Fable session, 2026-11-07T1600. Script
`scripts/qutrit_hopf_picture_2026-11-07T1600.py` (PASS, stdout in section
14). Bibliography batch `bib/qutrit_hopf_refs_2026-11-07T1610.bib`.
Follows this morning's `confinement_budget_flux_tube_2026-11-07T1130.md`,
whose fence (the SU(3) singlet is three qutrits, the register is three
qubits) prompted the question.

JS's question: "tell me about qutrits in the Hopf fibration picture."

## 0. The answer in five lines

1. A qutrit has no Hopf fibration. Its phase bundle S^1 -> S^5 -> CP^2 has
   the complex projective plane as base, not a sphere, and Adams's theorem
   leaves S^1, S^3 and S^7 as the only fibres of spheres by spheres and the
   only parallelisable spheres; S^5 is neither. Its Bloch body is not a
   ball (script F): a pure state has Bloch radius 1 but its antipode has
   eigenvalue -1/3 and is not a state; the fraction of directions at a
   given radius that are states is 1 inside radius 1/2 and 0.68, 0.09,
   0.0025, 0 at radii 0.55, 0.7, 0.9, 1; three orthogonal pure states sit
   at the corners of an equilateral triangle (pairwise inner product
   -1/2), not at antipodes. The qudit-degeneration document already lists
   this as P_1 to P_8; the qutrit is not a register of the tower.
2. Where the qutrit lives is the colour sector of the three-qubit Hopf
   base, and the paper already has the geometry under another name. The
   appendix's lemma "the base is Bloch + colour" gives r^2 + |w|^2 = 1 with
   w the colour component of the Hopf image; script A confirms it on 2000
   random states and adds the one line the lemma does not say: |w|^2 =
   4 det rho_1 = the one-tangle of the split qubit (deviation 6e-16). So
   S^8 is the join S^2 * S^5 of the record Bloch sphere and the qutrit's
   sphere, and the colour equator S^5 of the appendix's corollary, the
   locus the GHZ orbit covers, is the unit sphere of C^3: the qutrit's
   phase sphere, reached exactly when the budget is exhausted (r_1 = 0).
   GHZ maps to -e_6, a unit colour vector; W to colour radius sqrt(8/9).
3. The qutrit's own fibration S^1 -> S^5 -> CP^2 has as fibre left
   multiplication by the record circle exp(theta e_1): that is the quantum
   global phase of a branch, it preserves C^3 and acts there as the scalar
   exp(i theta), and its automorphism subgroup is the centre Z_3 of SU(3)
   (script B, continuing this morning's Part D). The colour qutrit's state
   space CP^2 is the colour equator modulo the record phase, with the
   round metric of S^5 descending to Fubini--Study. One fence: the Hopf
   image is a function of the state vector, not of the ray; the global
   phase of the three-qubit state moves the colour direction in general
   (overlap as low as 0.04 between a state and its rephasing), rotating it
   by exp(2 i theta) on the coloured-GHZ family |0>|00> + |1>|c>, whose
   colour vector is exactly -c. The invariant content of the colour vector
   is its radius, which is the paper's confinement statement.
4. Colour SU(3) acts on the register as an entangling unitary of the two
   internal qubits (script C). Exponentiating the e_1-stabiliser of g_2
   gives, on each branch C^4 = C + C^3, a unitary that fixes the record
   amplitude |00> and lies in SU(3) (det 1 to 1e-14) on the complementary
   qutrit {|01>, |10>, |11>}; it has operator-Schmidt rank 4 across the two
   internal qubits and sends |01> to a state of concurrence 0.40 to 0.87;
   and the Hopf colour vector transforms in the fundamental. So the colour
   qutrit is the internal two-qubit space with the record direction
   removed, the "qutrit, or two qubits" of the interactions section made
   exact, and colour rotations are not local operations on the register.
   Local unitaries on the internal qubits preserve the colour radius and do
   not act on the colour direction as a function of the base point at all.
5. The three-quark singlet is the octonionic 3-form with the record-line
   associator as its phase (script D, exact to 1e-14 on 300 triples):
   epsilon(v_1, v_2, v_3) = det[v_1 v_2 v_3] = <v_1, v_2 v_3> +
   (i/2) <e_1, [v_1, v_2, v_3]>, the real part the associative calibration
   phi and the imaginary part the coassociative calibration *phi(e_1, .,
   ., .). A unitary colour frame closes under octonion multiplication up
   to the phase of its determinant, v_1 v_2 = e^(-i alpha) v_3, and an
   SU(3) frame spans with e_0 a quaternion subalgebra: a colour singlet is
   a copy of H inside the colour C^3, the special Lagrangian 3-planes of
   Harvey and Lawson. That is the same condition the spacetime section
   imposes for three links to compose. The meson singlet is pi_C(conj(w) v).
   Two qutrits add one more fence to the ball picture: the CGLMP maximum
   is 2.8729 at the maximally entangled state and 2.9149 at gamma = 0.7923
   (script E), so the "unique centre" argument for Tsirelson is qubit-only.

## 1. What the corpus says

- `paper1/entanglement_classes_and_gauge_groups_2026-06-08.tex` lines
  156--180: the identification psi -> (o_1, o_2) by the first-qubit split,
  the Hopf map h = o_1 conj(o_2), the split O = C + C^3 with C^3 "the
  colour-triplet sector carrying the 3 + 3-bar of the SU(3)", lemma
  `lem:cproj` (pi_C(h) is the conjugate Hermitian inner product of the
  branches), the composition identity, and "e_1 is the unique imaginary
  direction whose Fano pairing of the basis units coincides with the
  pairing of real and imaginary parts in the qubit amplitudes". Lines
  184--221, `prop:ghz` (the GHZ orbit's image lies in C^3, characterised by
  maximally mixed marginals) and `prop:w-access` (sup C_frac = 1/9). Lines
  360--366: "The base S^8 decomposes as (Bloch vector of the split qubit)
  + (colour sector C^3), and the canonical GHZ orbit maps onto the unit
  sphere of the colour sector --- the equatorial S^5 in S^8".
- `paper1/appendices/appendix_ghz_w_proofs_2026-06-11.tex`: the table
  (Fano lines (1,2,3), (1,4,5), (1,7,6), ...), J = L_{e_1} with J(e_6) =
  -e_7, the embedding eq:embedding with the forced sign on the last block,
  lemma `app:lem:base` (x_9 = r_z, 2 pi_C(h) = r_x - i r_y, r^2 + |w|^2 =
  1), the ceiling lemma, corollary `app:cor:s5` (the colour equator), and
  the W orbit on a colour five-sphere of radius sqrt(8/9) times a Bloch
  two-sphere of radius 1/3.
- `knowledge/project-docs/open_problem_qudit_degeneration.md` (March
  2026): the eight properties P_1 to P_8 that hold for the qubit and fail
  for d >= 3, with the division-algebra axiom conjecturally responsible
  for each; P_4 and P_5 are Adams; "the particle-native encoding (three
  binary Cayley-Dickson qubits per fermion) avoids qudits entirely".
- `paper1/interactions_circuits_section_2026-06-08.tex` line 339: "a
  generation register --- a qutrit, or two qubits encoding the triality
  sector"; line 439: "no current device offers a qutrit".
- `paper1/quantum_numbers_section_2026-06-08.tex` lines 236--249: the Z_3
  centre of colour inside the Z_6 quotient.
- `paper1/masses_section_2026-06-08.tex` lines 190--200: the norm defect
  "is, up to normalisation, the coassociative calibration" (Harvey and
  Lawson; Bryant), zero divisors at the calibration bound.
- `paper1/spacetime_from_non-computability.tex` lines 168--194,
  `sec:three-dimensions`: "among three [links] they compose exactly when
  the links lie in one quaternionic subalgebra, so the largest consistent
  network inside S^7 is an S^3" (Conway; Harvey and Lawson).
- `paper1/monogamy_aside_2026-06-07.tex`: tau_A = 1 - r_A^2 = 4 det rho_A.
- This morning's note, section 6: the SU(3) singlet epsilon has pairwise
  negativity 1/3 while GHZ_3 has separable pairs; the budget's robust
  clause is r^2 = 0.

## 2. The qutrit has no Hopf fibration (script F)

The pure states of a qutrit form CP^2, real dimension 4, and the phase
bundle S^1 -> S^5 -> CP^2 is a principal U(1) bundle whose base is not a
sphere (its second and fourth Betti numbers are both 1). Hopf's fibrations
(1931; 1935) are S^1 -> S^3 -> S^2, S^3 -> S^7 -> S^4 and S^7 -> S^15 ->
S^8, and Adams (1960; 1962) closed the list: no further sphere fibres
spheres by spheres, and only S^0, S^1, S^3, S^7 are parallelisable. The
qutrit's S^5 is not parallelisable and its base is not a sphere, which is
why the qudit-degeneration document's P_4 and P_5 fail at d = 3.

The Bloch body (Kimura 2003; Kimura and Kossakowski 2005; Goyal et al.
2016; Eltschka et al. 2021). In the normalisation rho = (I + sqrt3
n.lambda)/3 a pure state has |n| = 1 (checked on 200 random pure states,
with rho recovered from n). The antipode -n has smallest eigenvalue
exactly -1/3 and is not a state. Random directions at radius 0.4 and 0.5
are states with probability 1 (the inscribed ball has radius 1/2); at
0.55, 0.7, 0.9 the fraction is 0.6835, 0.0925, 0.0025; at radius 1 it is
0 (the pure states are a measure-zero CP^2 on the sphere). The Bloch
vectors of three orthogonal pure states have Gram matrix (3/2) I - 1/2:
pairwise inner product -1/2, an equilateral triangle, not antipodal pairs
(P_7).

None of this is new; it is recorded so that the next section can say
precisely where the qutrit does appear.

## 3. Where the qutrit lives: the colour equator of the three-qubit base (script A)

With the paper's table and embedding (the script re-derives e_1 e_2 = e_3,
e_1 e_4 = e_5, e_1 e_7 = e_6 and e_2 e_4 = e_6 from the Cayley--Dickson
recursion), on 2000 random three-qubit states:

- |o_1 conj(o_2)|^2 = |o_1|^2 |o_2|^2 (composition), and pi_C(h) is the
  conjugate of sum conj(psi_{0k}) psi_{1k} (lemma `lem:cproj`), both to
  1e-12.
- (z, 2 Re pi_C, -2 Im pi_C) is the first qubit's Bloch vector (r_z, r_x,
  r_y), lemma `app:lem:base`.
- The colour radius squared, 4 |pi_{C^3}(h)|^2, equals 4 det rho_1 = 1 -
  r_1^2, the one-tangle of the split qubit, to 6e-16. The appendix writes
  this as r^2 + |w|^2 = 1; the monogamy aside writes tau = 1 - r^2; the
  two together are the sentence "the colour radius is the budget".
- The base point (z, 2 pi_C, 2 pi_{C^3}) has unit norm: S^8 = {(b, v) in
  R^3 + C^3 : |b|^2 + |v|^2 = 1}, the join S^2 * S^5.

Canonical states: GHZ has z = 0, pi_C = 0 and colour vector exactly -e_6,
a unit vector on the third colour line; W has z = 1/3, pi_C = 0 and colour
radius sqrt(8/9) = 0.942809; |000> has colour radius 0 and Bloch radius 1.

The reading. The three-qubit Hopf base fibres over the closed Bloch ball
of the split qubit with fibre a five-sphere of radius sqrt(1 - r^2),
shrinking to a point on the ball's surface (product states) and full-size
at the centre (budget exhausted). The full-size fibre is the colour
equator S^5 of the appendix, and it is the unit sphere of the colour C^3:
the total space of the qutrit's own phase bundle. A qutrit, in the Hopf
picture, is what the three-qubit register looks like from the base when
the split qubit has nothing of its own left: the GHZ locus.

## 4. The phase circle and CP^2 (script B)

The record circle exp(theta e_1), acting by left multiplication, is the
quantum global phase of a branch (embed(e^{i theta} c) = exp(theta e_1)
embed(c), 200 random cases), preserves the colour C^3 and acts there as
the scalar e^{i theta} in the block pairing (200 random colour vectors).
Its automorphism subgroup is the centre Z_3 (residual 0 at the cube roots
of unity, above 0.1 at pi/2 and at 1 radian), as this morning. So the
qutrit's phase fibration S^1 -> S^5 -> CP^2 is, inside the octonions, the
record line's U(1) acting on the colour equator, and CP^2 = S^5 / U(1)_rec
with the Fubini--Study metric as the quotient of the round metric (the
standard Hopf construction of CP^n; no check needed). The colour qutrit's
state space is the colour equator with the record phase quotiented out,
and the only part of that phase that is an octonion automorphism is the
centre.

The fence. Under the global phase psi -> e^{i theta} psi of the
three-qubit state, z and pi_C are invariant (they are rho_1) but the
colour vector is not: over 300 random states and phases the overlap
|<v, v'>|/|v||v'| falls as low as 0.0429, and v' is neither v nor
e^{+-2 i theta} v in general (maximum deviations 0.99, 0.92, 0.87). On the
coloured-GHZ family |0>|00> + |1>|c> the colour vector is exactly -c and
the global phase rotates it by e^{2 i theta}, so there the direction in
CP^2 is phase-invariant (overlap 1.000000). This is the three-qubit form
of a fact already present for two qubits, where the concurrence
coordinate of the S^4 base rotates by e^{2 i theta} (Mosseri and Dandoloff
2001): the Hopf map is a map on S^15, not on CP^7, and the base is a
function of the vector. The paper uses only the colour radius (prop:ghz,
the ceiling lemma), which is a function of rho_1; anything that uses the
colour direction as a property of a state must say which representative,
or stay on the coloured-GHZ family.

## 5. Colour SU(3) on the register (script C)

Exponentiating random elements of the eight-dimensional e_1-stabiliser of
Der(O) (three trials; automorphism residual 5e-13, commutator with J
3e-13) gives on each branch C^4 = C + C^3 a 4 x 4 unitary (residual 5e-13)
that fixes the record amplitude (the first basis vector, both as column
and row) and whose 3 x 3 block has determinant 1 to 1e-14. Its
operator-Schmidt rank across the two internal qubits is 4 (a local
unitary has rank 1), and it sends |01> to a state of concurrence 0.7565,
0.8732, 0.3967 in the three trials. The Hopf image transforms
equivariantly, h' = g(h), with z and pi_C fixed and the colour vector
rotated by the 3 x 3 block, on 50 random states per trial.

So the colour SU(3) of the framework, the stabiliser of e_1 in G_2, acts
on the three-qubit register as 1 (x) U_g with U_g = diag(1, U_3) in the
basis {|00>, |01>, |10>, |11>} of the two internal qubits. The colour
qutrit of a quark is the span of |01>, |10>, |11>: the internal two-qubit
space with the record direction |00> removed, which is what C^4 = C + C^3
says once the embedding is fixed. The interactions section's "a qutrit, or
two qubits encoding the triality sector" is, for colour, exact and not a
choice: the qutrit is the two qubits minus one direction. And a colour
rotation is an entangling gate on the two internal qubits, never a local
one.

The contrast, reported not assumed: for one fixed local unitary U_2 (x) U_3
on the internal qubits applied to both branches, the colour radius is
preserved to 3e-16 (it is the one-tangle) but the best linear fit v' = M v
has residual 0.49, and the best linear fit on the whole base point (z, 2h)
has residual 0.98; a Haar unitary on C^4 gives 0.28 and 0.56. The colour
direction of the transformed state is not a function of the base point of
the original. This is why the GHZ orbit covers the whole equator (the
paper's "maps onto"): local unitaries move the colour direction freely and
non-linearly while keeping the radius at 1.

## 6. The singlet as a quaternion triple (script D)

For colour vectors v_1, v_2, v_3 in C^3 = span(e_2, ..., e_7), with det
the complex determinant of the 3 x 3 matrix of their block coordinates,
fitting and then checking on 300 random triples:

    Re det = <v_1, v_2 v_3>                      (coefficient 1.000000, residual 1e-14)
    Im det = (1/2) <e_1, [v_1, v_2, v_3]>         (coefficient 0.500000, residual 7e-15)
           = <e_1, (v_1 v_2) v_3> = -<e_1, v_1 (v_2 v_3)>.

The real part is the associative 3-form phi(a, b, c) = <a, bc> of Harvey
and Lawson; the imaginary part is the coassociative 4-form *phi(a, b, c,
d) = (1/2) <a, [b, c, d]> with the record unit in the first slot. In the
C^3 model of the octonions this is the statement that phi restricted to
R + C^3 is e^1 wedge omega + Re Omega and *phi contracted with e_1 is Im
Omega, where Omega is the holomorphic volume form of C^3 and the
determinant is Omega(v_1, v_2, v_3). The script also confirms the model's
product rule: pi_C(v w) = -conj<v, w>_C and colour(v w) = conj(v x w) (the
conjugate cross product), and the meson singlet <v, w>_C = pi_C(conj(w)
v), the conjugate pattern of lemma `lem:cproj`. The associator of three
colour vectors has zero real part and non-zero e_1 and colour parts.

Consequences for frames. For a unitary colour frame F = [v_1 v_2 v_3]
with det F = e^{i alpha}: v_1 v_2 = e^{-i alpha} v_3 and cyclically
(closure up to the phase of the determinant), phi(v_1, v_2, v_3) = cos
alpha and (1/2) <e_1, [v_1, v_2, v_3]> = sin alpha (five random frames;
three printed). For an SU(3) frame, alpha = 0, the four vectors e_0, v_1,
v_2, v_3 span a subalgebra closed under multiplication: a quaternion
subalgebra of O. By Harvey and Lawson the associative 3-planes of Im O are
exactly the imaginary parts of quaternion subalgebras, and the ones lying
inside C^3 = e_1^perp are the special Lagrangian planes, SU(3)/SO(3).

So the SU(3) colour singlet of three quarks, as a frame, is a copy of H
inside the colour C^3; the phase of a U(3) frame's determinant measures
how far it is from one, with phi = cos alpha the associative calibration
and the coassociative calibration *phi(e_1, ., ., .) = sin alpha the tilt.
Two readings follow, with labels.

- The spacetime section's condition for three links to compose, "exactly
  when the links lie in one quaternionic subalgebra", is the same
  condition as the colour singlet's: a consistent three-link network and
  a colour-singlet baryon are both associative triples in O, one chosen
  inside Im H as the S^3 of relays, one inside the colour C^3. The
  asymptotic-freedom document's remark that N_c = d - 1 = 3 "both arise
  from dim_C C^3" now has a sharper form: both are the number of
  imaginary units of a quaternion subalgebra. CANDIDATE for the identity
  of conditions; the reading that it explains anything is RHYME until a
  mechanism says why the same triple serves twice.
- The imaginary part of the singlet is the coassociative calibration with
  the record unit in the first slot, and the masses section identifies the
  coassociative calibration with the norm defect that settles the
  associator debt. So the phase of a baryon's colour frame is a
  coassociative quantity of exactly the kind the mass map is built from:
  Im epsilon(q_1, q_2, q_3) = *phi(e_1, q_1, q_2, q_3). Whether this gives
  the baryon binding a handle is not computed here. CONJECTURE, flagged
  for `op:confinement-energy-locus` and `op:baryon-contact`.

This also closes this morning's fence from the other side. The singlet's
pairwise negativity 1/3 is, in frame language, the statement that two
colours of a quaternion triple fix the third (v_1 v_2 = v_3); the
antisymmetric Werner marginal is the marginal of "the third is the product
of the first two". GHZ_3, whose pairs are separable, carries no such
product rule between its parties. The budget argument's robust clause,
r = 0 for every party, is what the two share.

## 7. Two qutrits: the ball argument is qubit-only (script E)

With the standard CGLMP settings (Collins et al. 2002), the family
(|00> + gamma|11> + |22>)/sqrt(2 + gamma^2) gives I_3 = 2.872934 at gamma
= 1, matching 4/(6 sqrt3 - 9), and a maximum of 2.914854 at gamma =
0.79229 (grid plus golden section), the result of Acín, Durt, Gisin and
Latorre 2002. The maximally entangled two-qutrit state does not maximise
the Bell violation. The monogamy aside derives the Tsirelson bound and
monogamy together from the unique centre of the Bloch ball; for a qutrit
the state space has a unique centre (I/3) but is not a ball, and the
extremal correlation does not sit at the state whose marginals are at the
centre. The ball argument is a qubit argument, which is consistent with
the qudit-degeneration document's thesis and should be one of its listed
degeneracies.

## 8. What I think

The qutrit's place in the framework is exact and slightly surprising. It
is not a register, because it has no fibration and no ball; it is the
shape of the three-qubit base seen from a split qubit that has spent its
budget. Its unit sphere is the colour equator the paper already names, its
phase circle is the record line's U(1), its projective space is that
equator modulo that phase, and its symmetry group acts on the register as
an entangling gate on the two internal qubits that leaves the record
direction alone. "Colour is a qutrit" and "the register is three qubits"
are the same sentence read from base and from total space.

The singlet result is the one I would carry forward. That the SU(3)
singlet is a quaternion subalgebra, with the record-line associator as its
phase, is a theorem (Harvey and Lawson on associative planes inside C^3),
and it puts the baryon vertex epsilon(qqq), which the paper already uses,
into the same calibrated geometry the masses section uses for the
associator debt. It also explains this morning's pairwise negativity
without apology: two colours of a baryon determine the third because they
multiply to it. What it does not do is say why the three spatial links
and the three colours should be the same kind of triple; that is a rhyme
until something forces it.

The two fences matter for future writing. The colour direction on the
Hopf base is vector data, not ray data; the paper is safe because it uses
only the radius, and any new use of the direction must say so. And the
unique-centre argument for Tsirelson does not survive the passage to
qutrits, which the framework should state as a feature of its qubit
foundation rather than discover later as an objection.

## 9. Second-order findings for JS's ruling

(a) `knowledge/project-docs/open_problem_qudit_degeneration.md`: add a
ninth degeneracy, "the maximal Bell violation is not at the maximally
entangled state (CGLMP; Acín et al. 2002), because the state space is not
a ball and the centre argument of the monogamy aside is qubit-specific".
Script E reproduces the numbers. CANDIDATE.

(b) `paper1/entanglement_classes_and_gauge_groups_2026-06-08.tex`, the
"base decomposes" paragraph (line 360): one sentence that the colour
equator is the unit sphere of the colour qutrit, fibred over CP^2 by the
record circle, and that the colour SU(3) acts on the register as
diag(1, SU(3)) on the two internal qubits, an entangling gate that fixes
the record amplitude. STRUCTURAL for the mathematics (script C);
CANDIDATE for the wording.

(c) `paper1/interactions_circuits_section_2026-06-08.tex` line 339, "a
qutrit, or two qubits": for colour the qutrit is exactly the two internal
qubits minus the record direction; the sentence is about the generation
register, where the triality is an S_3 label rather than a C^3, so a
parenthesis distinguishing the two "qutrits" (colour: continuous, C^3;
generation: a three-element set) would prevent a conflation. CANDIDATE.

(d) A proposition for the confinement section beside `op:baryon-contact`:
epsilon(v_1, v_2, v_3) = phi(v_1, v_2, v_3) + i *phi(e_1, v_1, v_2, v_3);
an SU(3) colour frame spans a quaternion subalgebra; a unitary frame
closes up to the phase of its determinant. STRUCTURAL (Harvey--Lawson),
verified in script D. Its reading against the masses section's
coassociative calibration is CONJECTURE and should be labelled so.

(e) The identity of conditions between `sec:three-dimensions` ("one
quaternionic subalgebra") and the colour singlet: a one-line cross-
reference in either place, labelled RHYME. No mechanism offered.

(f) The vector-versus-ray fence of section 4 as a footnote to
`lem:cproj` or `app:lem:base`: the base is a function of the vector; the
results used are functions of rho_1 and are safe. CANDIDATE.

(g) The glossary already tolerates two Z_3's (this morning's 9(c)); it now
also has two "qutrits". One sentence in the quantum-numbers or
generations section would keep colour's C^3 apart from the generations'
three-element set.

## 10. Prior work and ownership

- Hopf fibrations and qubit entanglement: Mosseri and Dandoloff 2001 (two
  qubits; the base S^4 as Bloch vector plus complex concurrence);
  Bernevig and Chen 2003 (three qubits; S^15 -> S^8). The join reading
  and the identification of the colour equator with the qutrit's phase
  sphere are this session's framing of the paper's own lemma.
- The qutrit's geometry: Kimura 2003; Kimura and Kossakowski 2005; Goyal
  et al. 2016; Eltschka et al. 2021; Bengtsson and Życzkowski 2006. Not
  the framework's.
- Adams 1960, 1962 and Hopf 1931, 1935 for the fibrations and
  parallelisability. Not the framework's.
- The C^3 model of the octonions with the conjugate cross product and the
  decomposition phi = e^1 wedge omega + Re Omega: Harvey and Lawson 1982;
  Bryant 1987; Baez 2002. The identity det = phi + i *phi(e_1, ...) is a
  restatement; the frame-closure corollary is elementary. The reading of
  the SU(3) singlet as a quaternion subalgebra inside the colour sector,
  and of its phase as the record-line associator, is this session's.
- The colour SU(3) as diag(1, SU(3)) on C^4 = C + C^3 is immediate from the
  paper's own embedding; that it is an entangling gate on the two internal
  qubits is this session's observation.
- CGLMP and the non-maximally-entangled maximum: Collins et al. 2002;
  Acín, Durt, Gisin and Latorre 2002. Not the framework's.
- Three-qutrit SLOCC classes: Nurmiev 2000; not two classes; not used
  beyond the remark.

## 11. Fences

- Everything in sections 3 to 6 is in the paper's own conventions (the
  table, J = L_{e_1}, the embedding with the sign on the last block). A
  different Fano orientation would move signs, not statements.
- The colour direction on the base is vector data (section 4). No result
  here uses it as a ray property except on the coloured-GHZ family.
- Script C's "not a function of the base point" is a least-squares
  statement on 400 samples with one fixed unitary each; it is a report,
  not a theorem, and the theorem-grade part is the SU(3) equivariance.
- Section 6's reading of Im epsilon as a coassociative quantity is a
  formal identity; nothing is said about the baryon mass.
- Section 7 computes one family of two-qutrit states with the standard
  settings; the global maximum of I_3 over all states and settings is not
  computed (Acín et al. report it on this family).
- Section 2's fractions are Monte Carlo (4000 directions per radius).
- No claim about generations: the "triality" register is an S_3 label and
  is only mentioned to keep the two qutrits apart.

## 12. Proposed ledger entries

- **STRUCTURAL** The three-qubit Hopf base is the join S^2 * S^5 of the
  split qubit's Bloch sphere and the colour five-sphere, with colour
  radius squared equal to the one-tangle 4 det rho_1 = 1 - r_1^2 (the
  appendix's r^2 + |w|^2 = 1 read with the monogamy aside). Script A.
- **STRUCTURAL** The colour equator S^5 is the unit sphere of the colour
  qutrit; left multiplication by the record circle exp(theta e_1) is the
  branch's global phase, the scalar e^{i theta} on C^3, and the fibre of
  the qutrit's bundle S^5 -> CP^2; its automorphism subgroup is the centre
  Z_3. Script B.
- **STRUCTURAL** exp(su(3)_{e_1}) acts on each branch C^4 = C + C^3 as a
  unitary fixing the record amplitude and lying in SU(3) on the
  complementary qutrit; it is entangling across the two internal qubits
  (operator-Schmidt rank 4); the Hopf colour vector transforms in the
  fundamental. Script C.
- **STRUCTURAL** det[v_1 v_2 v_3] = <v_1, v_2 v_3> + (i/2) <e_1, [v_1, v_2,
  v_3]> for colour vectors; pi_C(v w) = -conj<v, w>_C and colour(v w) =
  conj(v x w); a unitary frame closes up to the phase of its determinant;
  an SU(3) frame spans with e_0 a quaternion subalgebra. Script D;
  Harvey--Lawson for the calibration identities.
- **ESTABLISHED** The finite checks of scripts A to F, PASS, 0 FAIL,
  including the CGLMP values 2.872934 and 2.914854 at gamma = 0.79229.
- **CANDIDATE** The colour qutrit of a quark is the two internal qubits
  with the record direction removed, and colour rotations are entangling
  gates on them; "a qutrit, or two qubits" is exact for colour.
- **CANDIDATE** The qudit-degeneration document's ninth property: the
  maximal Bell violation leaves the maximally entangled state at d = 3,
  because the centre argument needs a ball.
- **RHYME** The colour singlet and the spacetime section's three composing
  links are both associative triples in O.
- **CONJECTURE** Im epsilon(q_1, q_2, q_3) = *phi(e_1, q_1, q_2, q_3) ties
  the baryon vertex to the coassociative calibration of the mass map;
  nothing computed.
- *Fence, recorded not labelled:* the Hopf base is a function of the
  state vector, not of the ray; the paper's uses are functions of rho_1.

## 13. Files

- `scripts/qutrit_hopf_picture_2026-11-07T1600.py` (new; PASS, 0 FAIL;
  seed 20261107; pure numpy; the paper's conventions; three fixes during
  the session: a missing factor 2 in the coloured-GHZ check, the
  conjugation side of the meson identity, and the local-unitary check
  converted from an assertion to a report after it failed).
- `knowledge/sessions/qutrit_hopf_picture_2026-11-07T1600.md` (this note).
- `bib/qutrit_hopf_refs_2026-11-07T1610.bib` (9 keys, all
  Crossref-verified; no VERIFY-CITE; VERIFY-SUPPORT on every body).
- `notes/todo.md`: section "2026-11-07: qutrits in the Hopf picture (Fable
  session, afternoon)" appended.
- Nothing in the paper patched; nothing built; nothing committed.

## 14. Exact stdout of `scripts/qutrit_hopf_picture_2026-11-07T1600.py`

```
  [ok  ] the paper's table: e_1 e_2 = e_3, e_1 e_4 = e_5, e_1 e_7 = e_6 (so J e_6 = -e_7), e_2 e_4 = e_6
  [ok  ] J = L_{e_1} squares to -1 on O
=== Part A: the Hopf base is (Bloch vector) + (colour C^3) with colour radius^2 = one-tangle ===
  [ok  ] composition identity |o_1 conj(o_2)|^2 = |o_1|^2 |o_2|^2 on 2000 random states
  [ok  ] lemma cproj: pi_C(h) = conj <psi_0, psi_1> (antilinear in the first slot)
  [ok  ] (z, 2 Re pi_C, -2 Im pi_C) is the first qubit's Bloch vector (r_z, r_x, r_y)
  [ok  ] colour radius squared 4|pi_{C^3}(h)|^2 = 4 det rho_1 = 1 - r_1^2 = the one-tangle  (max deviation 5.6e-16)
  [ok  ] base point lies on S^8: z^2 + |Bloch_xy|^2 + colour^2 = 1
  state          z  |2 pi_C|  colour radius  colour vector 2 pi_{C^3}(h) as C^3
  GHZ       0.0000    0.0000       1.000000  [ 0.+0.j  0.+0.j -1.+0.j]
  W         0.3333    0.0000       0.942809  [0.6667+0.j 0.6667+0.j 0.    +0.j]
  |000>     1.0000    0.0000       0.000000  [0.+0.j 0.+0.j 0.+0.j]
  [ok  ] GHZ: z = 0, pi_C = 0, unit colour vector (-e_6, the third colour line)
  [ok  ] W: z = 1/3, pi_C = 0, colour radius sqrt(8/9)
  [ok  ] product: colour radius 0, Bloch radius 1
  so S^8 = { (Bloch vector b, colour vector v) : |b|^2 + |v|^2 = 1 } = the join S^2 * S^5;
  the qutrit's sphere S^5 (unit colour vectors) is the budget-exhausted equator, r_1 = 0.

=== Part B: the qutrit's phase fibration S^1 -> S^5 -> CP^2 and the record circle ===
  [ok  ] left multiplication by exp(theta e_1) is the quantum global phase of a branch
  [ok  ] it preserves the colour C^3 and acts there as the scalar exp(i theta): the qutrit's phase circle
  [ok  ] the phase circle's automorphism subgroup is the centre Z_3 (residual 0 at the cube roots, > 0.1 elsewhere)
  global phase psi -> exp(i theta) psi on the Hopf image (random states):
    max |v' - v| = 0.994; max |v' - e^(2i theta) v| = 0.919; max |v' - e^(-2i theta) v| = 0.865
    min over samples of |<v, v'>|/(|v||v'|) = 0.0429  (1 would mean the colour direction in CP^2 is phase-invariant)
  [ok  ] coloured GHZ |0>|00> + |1>|c>: colour vector = -c exactly, and the global phase rotates it by e^(2i theta)
    on that family the colour direction in CP^2 is phase-invariant: min |<v,v'>|/|v||v'| = 1.000000
  reading: the Hopf base is a function of the vector, not of the ray (as for two qubits, where the
  concurrence coordinate rotates by e^(2i theta)); the LU-invariant content of the colour vector is its radius.

=== Part C: colour SU(3) acts on the register as an entangling unitary of the two internal qubits ===
  [ok  ] dim Der(O) = 14 and dim Stab(e_1) = 8
  trial   aut res    [g,J]  unitary  fixes rec         det U3  op-Schmidt  C(U|01>)  v'=U3 v
      0   5.0e-13  3.0e-13  4.7e-13       True +1.000000+1.4e-14j           4    0.7565     True
      1   6.7e-13  1.3e-13  8.5e-13       True +1.000000-2.0e-14j           4    0.8732     True
      2   4.9e-13  2.5e-13  5.4e-13       True +1.000000-1.4e-14j           4    0.3967     True
  [ok  ] exp(su(3)_{e_1}) acts on each branch as a unitary fixing the record amplitude, in SU(3) on the qutrit |00>^perp, entangling across the two internal qubits, and the Hopf colour vector transforms in the fundamental
  the induced action on the Hopf image, for ONE fixed unitary applied to both branches (reported, not assumed):
    U_2 x U_3 local on the internal qubits: colour radius preserved to 2.8e-16; best linear fit v' = M v has max residual 0.49; best linear fit on the whole base point (z, 2h) has max residual 0.98
    -> the colour vector's direction is not a function of the base point under this unitary; only its radius is invariant
    Haar U(4) on the internal qubits: colour radius preserved to 2.2e-16; best linear fit v' = M v has max residual 0.28; best linear fit on the whole base point (z, 2h) has max residual 0.56
    -> the colour vector's direction is not a function of the base point under this unitary; only its radius is invariant
  [ok  ] local unitaries on the internal qubits preserve the colour radius (the one-tangle) but do not act linearly on the colour vector

=== Part D: the three-quark singlet is the octonionic 3-form plus the record component of the associator ===
  Re det = alpha <v1, v2 v3>:            alpha = +1.000000, max residual 1.2e-14
  Im det = beta  e_1 . [v1, v2, v3]:      beta  = +0.500000, max residual 7.1e-15
  Im det = beta' e_1 . ((v1 v2) v3):      beta' = +1.000000, max residual 7.1e-15
  Im det = beta'' e_1 . (v1 (v2 v3)):     beta''= -1.000000, max residual 8.9e-15
  [ok  ] epsilon(v1,v2,v3) = (+1.0) <v1, v2 v3> + i (+0.5) e_1.[v1,v2,v3] exactly on 300 random triples
  support of the associator of three colour vectors, max |component| by basis unit: [ 0.    33.393 22.373 20.861 45.231 22.279 18.966 21.626]
  [ok  ] meson singlet <v, w>_C = pi_C(conj(w) v), the conjugate pattern of lemma cproj
  [ok  ] for colours v, w: pi_C(v w) = -conj<v,w>_C and colour(v w) = conj(v x w): the octonions are C + C^3 with the conjugate cross product
  unitary colour frames F = [v1 v2 v3], det F = e^(i alpha): closure v1 v2 = e^(-i alpha) v3 and Re det = phi
    frame 0: alpha = -1.3217; closure True; phi = +0.246563 = cos alpha; e_1.[v1,v2,v3]/2 = -0.969127 = sin alpha
    frame 1: alpha = -1.0817; closure True; phi = +0.469803 = cos alpha; e_1.[v1,v2,v3]/2 = -0.882771 = sin alpha
    frame 2: alpha = -1.5808; closure True; phi = -0.009976 = cos alpha; e_1.[v1,v2,v3]/2 = -0.999950 = sin alpha
  [ok  ] a unitary colour frame closes under octonion multiplication up to the phase of its determinant; det = 1 iff the triple is a quaternionic (associative) triple
  [ok  ] an SU(3) frame (det 1) spans, with e_0, a quaternion subalgebra of O: the colour singlet is a copy of H

=== Part E: two qutrits -- the CGLMP maximum is not at the maximally entangled state ===
  I_3 at the maximally entangled state (gamma = 1): 2.872934   (local bound 2; 4/(6 sqrt3 - 9) = 2.872934)
  I_3 maximised over the family (|00> + gamma|11> + |22>): 2.914854 at gamma = 0.79229
  [ok  ] CGLMP: 2.8729 at gamma = 1 with the standard settings
  [ok  ] the maximum over the family exceeds the maximally entangled value and sits at gamma != 1 (about 0.79)

=== Part F: the qutrit's Bloch body is not a ball ===
  [ok  ] pure qutrit states have Bloch radius 1 in the normalisation rho = (I + sqrt3 n.lambda)/3
  [ok  ] the antipode -n of a pure state is not a state: its smallest eigenvalue is -1/3
   radius  fraction of random directions that are states
     0.40                                         1.0000
     0.50                                         1.0000
     0.55                                         0.6663
     0.70                                         0.0938
     0.90                                         0.0008
     1.00                                         0.0000
  Gram matrix of the Bloch vectors of three orthogonal pure states:
 [[ 1.  -0.5 -0.5]
 [-0.5  1.  -0.5]
 [-0.5 -0.5  1. ]]
  [ok  ] three orthogonal pure states form an equilateral triangle (pairwise inner product -1/2), not antipodes (-1)

QUTRIT HOPF PICTURE: PASS
```

## 15. Ruling and application (2026-11-07T1700)

JS, 2026-11-07: "I accept all your recommendations in section 9." All
seven findings (a)--(g) applied by
`scripts/patch_qutrit_hopf_rulings_2026-11-07T1700.py` (sentinel-gated;
anchors matched once each on `--check`; `.bak` beside every target;
`% EDITED` header; refuses to run twice). Targets:

- (a) `knowledge/project-docs/open_problem_qudit_degeneration.md`: P_9
  (maximal Bell violation at maximal entanglement; holds at d = 2, fails
  at d = 3 by CGLMP), a P_9 row in the Part A table (candidate: follows
  from P_1 and P_7), and a references block for Collins et al. 2002 and
  Acín et al. 2002. Part B's "P_1--P_8" left as it stands.
- (b) `paper1/entanglement_classes_and_gauge_groups_2026-06-08.tex`: one
  paragraph after "tilted off it into the single-qubit Bloch directions"
  (the colour qutrit's address; the record circle as its phase bundle;
  colour SU(3) as diag(1, U_3), entangling, fixing |00>; no fibration, no
  ball; the colour radius as the only state property). Cites
  `adams1960hopf` (in references.bib) and `kimura2003bloch` (in the
  2026-11-07T1610 batch only: undefined until import, as expected).
- (c) `paper1/interactions_circuits_section_2026-06-08.tex`: the
  parenthesis at "a qutrit, or two qubits".
- (d) `paper1/confinement_section_2026-06-13.tex`: Proposition
  `prop:singlet-quaternion` with a proof sketch, after
  `op:confinement-energy-locus` (`op:baryon-contact` is no longer in the
  paper; it survives only in knowledge/open_problems.md). Equation
  `eq:singlet-calibration`. Three remarks after it: the singlet's pair is
  the antisymmetric Werner state, so "every pairwise correlation zero" is
  about the register's GHZ_3 and the shared form of the budget argument is
  r^2 = 0 (fact, from this note's section 6; the morning note's wider
  reading of the paper's pairwise clause is still for ruling); the
  identity of conditions with `sec:three-dimensions` as a rhyme; the
  coassociative reading as a conjecture with nothing computed.
  `harvey1982calibrated` cited for the associative-plane theorem:
  VERIFY-SUPPORT, see below.
- (e) `paper1/spacetime_from_non-computability.tex`: one sentence after
  the Conway/Harvey--Lawson parenthesis in `sec:three-dimensions`,
  pointing to `prop:singlet-quaternion`, "recorded as a rhyme".
- (f) `paper1/appendices/appendix_ghz_w_proofs_2026-06-11.tex`: a remark
  after the proof of `app:lem:base` (vector, not ray; the invariants the
  lemmas use are functions of rho; the coloured-GHZ rotation by
  e^{2 i theta}).
- (g) `paper1/quantum_numbers_section_2026-06-08.tex`: one paragraph after
  the Z_6 paragraph keeping the continuous colour qutrit apart from the
  generations' three-element set; the colour triality of that paragraph
  assigned to the first, the generations' triality to the second. (The
  morning note's 9(c) on the two Z_3's is not applied here.)

Static checks on the inserted LaTeX: brace balance 0; `$` parity even;
one each of proposition, proof, remark and equation environments opened
and closed; every `\ref` target exists; citations resolve to
references.bib except `kimura2003bloch` (batch); no non-ASCII characters.
Not built (JS co-ordinates builds); a build is wanted. Not committed.

Verification. Acín, Durt, Gisin and Latorre 2002 read today against the
arXiv v2 text (quant-ph/0111143): settings Eq. (3) (phi_1 = 0,
phi_2 = pi j/3, phi'_1 = pi j/6, phi'_2 = -pi j/6, then U_FT and U_FT*);
maximally entangled value 4(2 sqrt3 + 3)/9 ~ 2.8729 (Sec. II); Bell
operator Eq. (8) with largest eigenvalue 1 + sqrt(11/3) ~ 2.9149 and
eigenvector (|00> + gamma|11> + |22>)/sqrt(2 + gamma^2), gamma =
(sqrt11 - sqrt3)/2 ~ 0.7923 (Eq. (9)); the numerical search over all von
Neumann settings and states finds no larger value; POVMs not excluded
(Sec. V). Closed forms agree with script E's 2.872934 and 2.914854 at
0.79229 (4/(6 sqrt3 - 9) = 4(2 sqrt3 + 3)/9). VERIFY-SUPPORT discharged
for `acindurtgisinlatorre2002quantum`; journal pagination not checked.
Harvey and Lawson 1982 could not be fetched (Project Euclid serves a bot
challenge; Springer redirects to a login), so the associative-plane
theorem cited in `prop:singlet-quaternion` stays VERIFY-SUPPORT, as does
the same citation in `sec:three-dimensions`, which the paper already
carried.

Ledger: section 12's entries now follow from the accepted findings and are
ready for JS (or the Opus session at JS's instruction) to write into the
ledgers; nothing written here.
