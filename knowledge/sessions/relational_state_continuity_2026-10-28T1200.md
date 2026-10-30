# A state is a relation, and so is a transformation: what relationalism does to Hardy's fifth axiom (2026-10-28T1200)

Session 2026-10-28, Fable 5.1, first session on the laptop. JS: "a state
vector assumes it is a real state that can be measured, when in fact only
its relationship to another entity can be measured. Think about this and
how it might affect the issue of continuous transformation between pure
states." Read against `paper1/continuity_section_2026-07-04.tex`, the
2026-10-18 review of the ten routes
(`continuity_from_self_reference_open_problem_2026-10-18T1811.md`), the
fixed-point route of 2026-10-10T1500, the observer definition of
2026-10-08T1500, and blocks B2, B3 and B5 of the July continuity ledger.
Script `scripts/relational_transformations_fixed_points_2026-10-28T1200.py`
(seed 20261028, PASS), stdout in section 8. No TeX on this machine yet;
nothing compiled.

## 0. The answer in brief

Taken for states alone, JS's point is already in the paper (the global
phase as self-referential ignorance; Postulate 4's "gauge-invariant
relational content"; the counterfactual observer of 2026-10-08), and it
does not touch continuity: the stabiliser fragment and the toy theory are
relational in that sense and finite. The tempting next step, that a state
relative to a frame becomes every state once the frame is allowed to turn,
is circular, since it needs the continuous group of frame rotations that
is the conclusion (section 1).

What does bear on continuity is applying the same point to
*transformations*. A transformation is no more an absolute than a state
is: a rotation is a rotation about something, a unitary is diagonal in
something, and in the paper's calculus that "something" has an exact
name. A classical structure is an observer's record basis (2026-10-08),
and the reversible maps a classical structure generates are its *phases*,
the maps diagonal in it (Coecke and Duncan's phase group). So "the
transformation is relative to an observer" means "the transformation is a
phase of that observer's structure", and a transformation that is a phase
of no admissible structure is an absolute transformation, relative to an
observer the theory does not contain. The relational premise for
transformations is therefore

> **(I)** every admissible reversible transformation of the pre-measurement
> regime is a phase of some admissible classical structure.

A phase of a structure fixes the structure's copyable states, which are
admissible pure states. So (I) implies the fixed-point premise (F) of
2026-10-10, and (F) with transitivity and closedness gives a connected
positive-dimensional state space by the Jordan-derangement theorem of that
note, and Hardy's fifth axiom by `prop:connected-transitive`. Three things
follow that were not in hand on 2026-10-18.

1. The foils fail (I) in a form one can compute, and it is exactly their
   failure of (F): of the 24 one-qubit Clifford elements, the 10 that are
   phases of X, Y or Z are precisely the 10 that fix a stabiliser state,
   element by element; the 14 derangements are the 14 absolute
   transformations. The composite of two admissible phases, a Z-phase then
   an X-phase, is a phase of no admissible structure: it is the order-three
   rotation about (1,1,1)/sqrt 3, whose structure is the F magic state.
   The fragment admits a two-step protocol relative to an observer it does
   not admit (script parts A and B).
2. (I) is not a new kind of premise. It is the inside/outside principle
   applied to dynamics, and it has the same Lawvere shape as the closedness
   the paper already adopts: closedness says the regime's own description
   may not refer to a transformation that does not exist; (I) says the
   regime's own transformations may not be relative to an observer that
   does not exist. The open problem shrinks from "an adopted stance plus an
   open premise" to "one adopted stance, stated for limits and for
   generators". It does not close; section 6 says exactly what is adopted.
3. (I) bears on the field at the single-qubit rung. The rebit violates
   it: every non-trivial rotation of the real projective line moves every
   real state, and the fixed points it lacks are (1, +-i)/sqrt 2, the
   states the rebit does not have. Real quantum theory satisfies (F) in
   odd dimension and violates it generically in even dimension; complex
   quantum theory satisfies it always (script parts C and D). This
   corrects a fence in the 2026-10-10 note, which said real quantum
   theory's RP^{K-1} satisfies (F) with SO(K): only for odd K. The complex
   structure is what gives every rotation an observer, which is the
   2026-10-08 biconditional (observer = selection of i) seen from the
   dynamics side.

## 1. The reading that is circular, logged so it is not retried

The fragment's six states are stabiliser states *relative to a Pauli
frame*. If frames have no absolute orientation, one is tempted to say the
theory must admit the images of its states under every reorientation of
the frame, and the union of the conjugated fragments over SU(2) is all of
CP^1. That argument needs the continuous group of frame reorientations as
an input, and the existence of that group is the conclusion sought. The
toy theory shows the gap directly: its frame group is S_4, finite, the
union over frames is the same six epistemic states, and the theory is
perfectly relational in the frame sense. Relationalism about *states*
leaves the finiteness of the frame group untouched. Closed; of a piece
with the "no preferred basis" route (2026-10-18, attempt 3), which the
passive/active distinction blocks. Relationalism does dissolve that
distinction (turning the frame and turning the system are the same
relation change), but the dissolved distinction only relocates the
question to the frame group.

## 2. Transformations as relations, in the paper's own objects [STRUCTURAL pieces, CANDIDATE assembly]

1. A classical structure (dagger-special commutative Frobenius algebra)
   is an orthonormal basis (Coecke, Pavlovic, Vicary; cited in the paper),
   and in the paper's reading it is an observer's committed record basis
   (`prop:f1-dictionary`; the 2026-10-08 definition of observer).
   STRUCTURAL and CANDIDATE respectively, as before.
2. The phase group of a classical structure is the group of unitaries
   diagonal in its basis (Coecke and Duncan; the "phased spiders" of the
   ZX-calculus the paper already uses). In Hilb on C^K it is U(1)^K
   modulo the global phase. STRUCTURAL; the reference is in the ZX
   literature the paper cites through Coecke--Kissinger, and the exact key
   for the phase-group paper is owed (VERIFY-CITE if the paper quotes it).
3. Every unitary on C^K is a phase of the structure given by its
   eigenbasis. STRUCTURAL (spectral theorem). Conversely, in the
   fragment, the structures are X, Y and Z and the phase groups are Z_4
   each (part A: 4 + 4 + 4 - 2 = 10 elements, the identity shared).
4. A state is measurable only as its relation to a reference: the overlap
   table with the reference's basis, and the relative phases through a
   third reference. The paper has this as the gauge-invariant relational
   content (Postulate 4) and the global phase as self-ignorance. The same
   sentence for a transformation: it is measurable only by the relations
   it changes, and it is *about* a structure, the one it is a phase of.
   The relational premise (I) says that structure is in the theory.

Assembled: (I) is "no absolute transformations", the twin of "no absolute
states", with "relative to" given the exact form "phase of". CANDIDATE.

## 3. (I) implies (F), and (F) implies the continuum [STRUCTURAL]

A phase of a structure multiplies each copyable state of the structure by
a scalar, so it fixes each of them projectively; the copyable states of an
admissible structure are admissible pure states; hence every admissible
transformation fixes an admissible pure state, which is (F). The theorem of
2026-10-10T1500 then gives, with transitivity and closedness and at least
two pure states, that P is a connected manifold of positive dimension, and
`prop:connected-transitive` gives Hardy's fifth axiom.

For one qubit the conclusion is all of CP^1, not merely a connected subset:
the connected positive-dimensional homogeneous spaces of closed subgroups
of SO(3) are S^2 and circles, and a circle fails (F), every non-trivial
rotation of it moving every point. Part C is this fact on the real
projective line, which is the same circle.

For a qubit (I) and (F) coincide: a transformation fixing psi is a
rotation about psi's axis, hence a phase of the structure {psi, psi-perp},
admissible when psi is (part A confirms the coincidence element by element
on the Clifford group). In higher dimension (I) is stronger than (F),
asking for a whole fixed basis rather than one fixed state. The theorem
needs only (F); (I) is what gives (F) a physical reading.

## 4. Why the foils fail, verified [ESTABLISHED by script; the reading CANDIDATE]

- Part A. The 10 Clifford elements that are phases of an admissible
  structure are exactly the 10 that fix a stabiliser state; the 14 others
  are exactly the 14 derangements of 2026-10-10. Element by element,
  True. So in the fragment, "absolute transformation" and "transformation
  with no fixed admissible state" are the same set.
- Part B. S_Z(pi/2) followed by S_X(pi/2), each a phase of an admissible
  structure, composes to a projective order-three element whose
  eigenstates have Bloch axis (0.5774, 0.5774, 0.5774) and overlap
  1/sqrt 3 with every Pauli axis: a phase of no admissible structure,
  fixing no stabiliser state. The fragment is relationally open: two
  admissible relative steps compose to a step relative to an observer the
  theory lacks, and that observer's record states are the magic states.
  This is the sentence the 2026-10-10 note reached for ("the fragment is
  not self-referentially closed") with the closure now named: closure of
  the set of structures under the eigenbases of the group the structures
  generate.
- The toy theory: its transformations are postulated permutations; the
  phase group of the epistemic basis {12|34} is the permutations fixing
  both blocks, Z_2 x Z_2, and the three-cycles and four-cycles are phases
  of no epistemic basis. Not computed here; the derangement count of 14
  was computed on 2026-10-10.

So (I) passes the open problem's FAIL test: both foils violate it. And
(I) is not a rephrasing of connectedness: it is a condition on (P, G)
checkable one transformation at a time, and it holds or fails in finite
theories where connectedness is not even in question.

## 5. The field [STRUCTURAL fact; CANDIDATE reading; one correction]

Parts C and D. The rebit's transformation group SO(2) on RP^1 violates
(F): for theta = pi/4, pi/2, 2pi/3 the largest overlap |<v|Rv>| over 3601
real directions is 0.707, 0.000, 0.500, never 1. The eigenvectors are
(1, +-i)/sqrt 2, which the rebit does not contain. In dimension n, random
SO(n) elements have a real eigenvector 1000/1000 times for n = 3 and 5 and
0/1000 times for n = 4; random unitaries always have one.

Correction owed to the 2026-10-10T1500 note, section 5, first fence:
"for larger K real quantum theory's RP^{K-1} also satisfies (F) with
SO(K)" holds for odd K only; for even K, and in particular for the rebit,
(F) fails. The consequence is that at the single-qubit rung, where the
open problem is posed, (I) and (F) exclude the real field as well as the
finite foils, and the complex field is the one in which every
transformation has an observer. This is the 2026-10-08 biconditional
(a system is an observer iff it carries a committed complex direction)
read from the dynamics side: a rotation needs an axis to be about, the
axis is a committed direction, and a committed direction is a complex
structure. The field is still pinned by additivity at the Shannon step,
as the paper says; this is a second, independent reason, and it is local
to even dimension, so it does not replace the first. CANDIDATE reading;
the RHYME "no C, no observer for the rotation" should stay fenced until
written against `sec:fanout-direction`.

## 6. What (I) is, honestly, and what remains open

(I) is not derived here. It is adopted, and the claim is that it is the
*same* adoption the paper already makes for closedness, not a second one.
Closedness (limit-realisability): a Cauchy sequence of available
transformations whose convergence the system can describe has its limit
available, else the description refers to what does not exist. (I): a
transformation the regime performs is a phase of some structure, and that
structure is available, else the transformation is relative to an observer
that does not exist. Both are "the regime contains what its own
descriptions refer to", the Lawvere shape the paper names. The honest
statement of the open problem after today is then one of two, JS to
choose:

- *Adopt.* State the operational completion as one stance with two
  clauses, limits and generators, and record that with it the value
  continuum is a theorem (section 3) rather than a premise. The debt is
  then one adopted stance, named, with the foils as the theories that
  refuse it. `op:limit-realisability` would be restated as "derive the
  completion stance from self-referential closure", which is where the
  2026-10-10 Lawvere programme (point-surjectivity of self-description)
  was already pointing.
- *Derive.* Keep (I) as the target: show from the inside/outside
  involution (`prop:inside-outside`) that the generator of every admissible
  transformation is an admissible system. The step still missing is the
  one the 2026-10-18 note called the full physical task: that "nothing
  acts on the regime from outside" is the same premise as "every
  transformation is a phase of an inside structure", rather than a
  stronger one.

Fences.

- Transitivity is still from no-records and closedness is still adopted;
  the theorem consumes both. Nothing here touches them.
- "Phase of a structure" presupposes the calculus (dagger-compact,
  classical structures). That is the paper's setting from
  `sec:hopf-justification` on; the premise is stated inside it, not
  inside Hilbert space, and asserts only that a structure exists in the
  theory.
- In higher dimension (I) asks more than (F); if a derivation delivers
  only (F), the theorem still fires.
- Finite dimension throughout, as before (the shift has no eigenvector).
- Degenerate phases fix a subspace; it contains pure states; (F) holds.
- The Coecke--Duncan phase-group reference is not in the paper's
  bibliography under that name as far as this session checked; VERIFY-CITE
  before the paper says "phase group".

## 7. Proposed text and ledger entries (JS to apply or decline)

- **ESTABLISHED** (computed) In the one-qubit Clifford group modulo
  phases, the elements that are phases of an admissible classical
  structure (diagonal in X, Y or Z) are exactly the elements that fix a
  stabiliser state, 10 of 24; the remaining 14 are the derangements of
  2026-10-10. The composite of a Z-phase and an X-phase of order four is
  of projective order three with eigenstate axis (1,1,1)/sqrt 3, a phase
  of no admissible structure.
- **STRUCTURAL** Real quantum theory on RP^{K-1} with SO(K) satisfies the
  fixed-point premise (F) iff K is odd; the rebit violates it; complex
  quantum theory satisfies it in every finite dimension. *Supersedes in
  part* the first fence of section 5 of
  `value_continuum_fixed_point_route_2026-10-10T1500.md`.
- **CANDIDATE** Relationalism for transformations: every admissible
  reversible transformation of the regime is a phase of some admissible
  classical structure (I). It implies (F); with transitivity and
  closedness the state space is a connected positive-dimensional manifold,
  all of CP^1 for a qubit, and Hardy's fifth axiom follows. Both foils
  violate (I) outright.
- **CANDIDATE** (I) and closedness are one adopted stance, the regime
  containing what its own descriptions refer to, for generators and for
  limits respectively. `op:limit-realisability` restated: derive that
  stance from self-referential closure, or adopt it and record the value
  continuum as its theorem.
- **RHYME** The complex structure is what gives every rotation an
  observer; the rebit's rotations are about an axis the rebit does not
  contain.
- *Closed route, for invalid_routes.md:* relationalism about states, via
  the union of a finite state set over all frame reorientations, is
  circular (section 1).
- No patch; the open problem's text and the continuity section are JS's
  to change. If adopted, the natural place is the paragraph of
  `sec:continuity` beginning "Closedness is the deeper premise
  conceptually", with (I) as its second clause, and one sentence in
  `op:limit-realisability` after the (F) restatement proposed on
  2026-10-10.

## 8. Exact stdout of `scripts/relational_transformations_fixed_points_2026-10-28T1200.py`

Run with numpy 2.5.4 in a scratch virtual environment (the repository's
`.venv` is not yet rebuilt on this machine).

```
Relational transformations and pure fixed points, seed 20261028
======================================================================================
A. Clifford mod phases: 24 elements; stabiliser states: 6
   elements that are a phase of X, Y or Z (diagonal in an admissible basis): 10  (per basis {'X': 4, 'Y': 4, 'Z': 4}, identity shared)
   elements fixing some stabiliser state: 10; derangements: 14
   'phase of an admissible structure' == 'fixes an admissible state' element by element: True
B. composite S_Z(pi/2) S_X(pi/2): projective order 3; eigenstate Bloch axis (+0.5774, +0.5774, +0.5774), |axis_k| = 1/sqrt3 = 0.5774
   |<eig|P|eig>| for P = X, Y, Z: X 0.5774, Y 0.5774, Z 0.5774  (a stabiliser state would give one 1 and two 0)
   phase of X, Y or Z: False; fixes a stabiliser state: False
C. rebit: SO(2) acting on the real projective line RP^1
   theta = 0.7854: max over 3601 real directions of |<v|Rv>| = 0.707107 < 1 (no fixed point); eigenvalues 0.707+0.707j, 0.707-0.707j, eigenvectors (1, +-i)/sqrt2 -- outside the rebit
   theta = 1.5708: max over 3601 real directions of |<v|Rv>| = 0.000000 < 1 (no fixed point); eigenvalues 0.000+1.000j, 0.000-1.000j, eigenvectors (1, +-i)/sqrt2 -- outside the rebit
   theta = 2.0944: max over 3601 real directions of |<v|Rv>| = 0.500000 < 1 (no fixed point); eigenvalues -0.500+0.866j, -0.500-0.866j, eigenvectors (1, +-i)/sqrt2 -- outside the rebit
D. real quantum theory: random SO(n) elements with a real eigenvector (a fixed point of RP^(n-1)):
   SO(3): 1000/1000   SO(4): 0/1000   SO(5): 1000/1000   (even n: generically none; odd n: always)
   complex: random U(2) with an eigenvector 1000/1000, U(4) 1000/1000 (always; the fundamental theorem of algebra)
======================================================================================
RELATIONAL FIXED POINTS: PASS
```

## 9. The other entity is the observer itself (added 2026-10-28T1500)

JS: "In the context of a self-referential observer the state is both the
observer and the observed, the 'other entity' is itself. The potential to
make an observation creates an observer-observed relationship, or
alternatively speaking of 'an observer' implies the potential to make an
observation. So we can think of an observer counter-factually making a
self-observation." Script
`scripts/self_observation_closure_2026-10-28T1500.py` (seed 20261028,
PASS), stdout at the end of this section.

### 9.0 What changes [CANDIDATE]

In section 2 the structure a transformation is relative to was "some
observer T". With the observer self-referential there is no T outside it:
the structure is O's own. (I) then reads: every transformation of the
regime is a phase of one of O's own record bases. The fixed point it
supplies is O's *counterfactual self-observation*: the state O would find
itself in if it fired its copy in that basis, and which the transformation
leaves alone. Fired, the copy is a record, the real column, a FANOUT.
Held, it is a fixed point of the dynamics, the imaginary column. The two
columns of 2026-09-18 are the two fates of one copy map. Thomson's lamp is
the paper's own instance: the self-consistent value (1+i)/2 is the lamp's
counterfactual self-observation under the toggle, the state the toggle
would confirm, admitted as a state because the lamp is both the toggled
and the toggler.

### 9.1 Lawvere, read as self-observation [CANDIDATE; the setup still owed]

The fixed point in Lawvere's proof is phi(a_0)(a_0): the self-description
evaluated on itself, which is a self-observation in JS's sense and nothing
else. Point-surjectivity, Lawvere's hypothesis, says the potential of
self-observation is complete: every way the observer could be described
from its register is a way it can describe itself. That is the
inside/outside principle in the observer's own terms, and by the
2026-10-08 definition it is what "observer" means. The proof uses the
*existence* of the self-description map, never its application, which is
why "counterfactual" is the right word: in the paper's calculus the
diagonal exists only on the classical part, as the copy map of a
structure, and the counterfactual self-observation is that copy map held
unfired. The categorical setup owed on 2026-10-10 (section 4, items 1 to
3) is unchanged but sharper: A is the copyable states of O's structure, the
diagonal is O's copy map unfired, the fixed point is the self-consistent
state, and the lamp principle is what admits it to P.

### 9.2 The clock reading [CANDIDATE]

An observer relative to whom g is a phase is one whose self-record is
stationary under g while its phase advances: a clock. So (F) says every
transformation of the regime is evolution relative to some internal clock,
and the fragment's dynamics has none: the order-three gate is applied from
outside, by a circuit. This answers block B2 of the July ledger ("why does
nature's pre-FANOUT gate set generate densely rather than close
finitely?"): a gate set is an external agent, nature has no external
agent, its transformations are each relative to an internal observer, and
that observer's stationary states are states of nature. Fence, important:
"internally generated" must be read as "diagonal in an admissible basis",
not as "of the form exp(-iHt)", or continuity is presupposed. (I) as stated
presupposes no one-parameter group; the fragment's phase groups are Z_4.

### 9.3 What the self-observation closure generates [ESTABLISHED by script; STRUCTURAL facts]

Apply the lamp principle uniformly, admitting the self-consistent fixed
point of every transformation, together with transitivity.

- Without transitivity it stops. Adjoining the fixed points of the
  Clifford group to the six stabiliser states gives 26 states, and a
  second pass gives 26 again; the set is Clifford-invariant (part C). This
  is the 2026-10-10 result, recomputed.
- Transitivity requires a transformation carrying |0> to an F state. The
  F axis has polar angle arccos(1/sqrt 3) = 0.304087 pi. By Niven's
  theorem, if theta is a rational multiple of pi then 2 cos theta is an
  algebraic integer; 2/sqrt 3 is a root of 3x^2 - 4, not monic, so
  theta/pi is irrational and the rotation has infinite projective order
  (part A: closest return in a million steps is 1e-11 off, never zero).
  With closedness the group contains a U(1) and the orbit is a continuum.
  This is a *structural* witness of infinite order, where the
  2026-10-10T1300 addendum had only the empirical Koide phase.
- The H states sit at pi/4, so carrying |0> to one is the T gate, of
  finite order eight; but Clifford with T is dense in SU(2) (Boykin,
  Mor, Pulver, Roychowdhury and Vatan 1999; Nielsen and Chuang, both
  VERIFY-CITE for the paper), and part B shows the enumerated orbit of
  |0> approaching a seeded random point of the sphere as the word length
  grows. With closedness, all of SU(2) and P = CP^1.

So the self-observation closure of the stabiliser fragment, under
transitivity and closedness, is quantum theory on the qubit. The
epistricted theories are, in one sentence, the theories that refuse the
self-consistent fixed points of their own transformations: block B5's
"load-bearing difference", located.

### 9.4 The step that is still adopted, now with its physical content [CANDIDATE]

An observer is defined by the potential of self-observation. A
transformation under which no admissible state is self-consistent is one
under which no observer persists: every potential self-record is
disturbed. If every transformation of the regime is one that some observer
survives, because transformations are relative to observers (I) and the
observer is inside (inside/outside), then (F). This is the same adopted
stance as section 6, with its physical content named: *the observer
survives its own dynamics*. The step from "observer is inside" and
"observer is the potential of self-observation" to "every transformation
is a phase of the observer's structure" is not a theorem here; it is the
place where the derivation would have to be done, and it is the
point-surjectivity step of 9.1 in physical dress.

### 9.5 Labels proposed for this section

- **STRUCTURAL** The angle between a stabiliser axis and an F magic axis is
  an irrational fraction of a turn (Niven); the rotation joining them has
  infinite projective order; Clifford with T is dense in SU(2) (cited).
- **ESTABLISHED** (computed) Fixed-point closure of the fragment without
  transitivity is finite (26 states, invariant); with transitivity it is
  dense.
- **CANDIDATE** (F) is the counterfactual self-observation; every
  transformation of the regime is evolution relative to an internal clock;
  the lamp principle is (F)-closure and generates quantum theory from the
  fragment under transitivity and closedness.
- **RHYME** The fired copy is a record, the unfired copy is a fixed point:
  the two columns as the two fates of one copy map.

### 9.6 Exact stdout of `scripts/self_observation_closure_2026-10-28T1500.py`

```
Self-observation closure of the stabiliser fragment, seed 20261028
======================================================================================
A. F-state polar angle theta = arccos(1/sqrt3) = 0.955317 rad = 0.304087 pi; 2cos(theta) = 1.154701 = 2/sqrt3, root of 3x^2 - 4: not an algebraic integer, so theta/pi is irrational
   rotation by theta about y: closest projective return in n <= 10^6 is n = 278585, ||tr U^n| - 2| = 9.86e-12 (never 0)
   image of |0>: Bloch (+0.8165, +0.0000, +0.5774), z-component 1/sqrt3
B. Clifford alone: 24 projective elements (closed). Clifford + T: reached the cap of 3000 distinct elements
   distance from a seeded random Bloch point to the nearest orbit point of |0>, by number of elements enumerated:
   100: 0.4665; 500: 0.2100; 1000: 0.1065; 2000: 0.0873; 3000: 0.0873  (decreasing: dense)
C. fixed-point closure without transitivity: 6 -> 26 -> 26 states; Clifford images outside the set: 0  (finite and invariant; transitivity is what forces the rotation of part A or B)
======================================================================================
SELF-OBSERVATION CLOSURE: PASS
```

## 10. Rational transformations: where closedness is indispensable (added 2026-10-28T1800)

JS: "suppose the infinitesimally small transformation was in the set of
rationals, would Hardy's derivation still apply?" Hardy's paper read today
from the arXiv PDF (quant-ph/0101012; text extracted to the scratchpad).
Script `scripts/rational_unitary_fixed_points_2026-10-28T1800.py` (no
randomness, PASS), stdout at the end.

### 10.1 Hardy as written: no [STRUCTURAL]

Hardy glosses "continuous" in section 7 as "made up from many small
transformations only infinitesimally different from the identity" and
states at once that the reversible transformations "will form a compact
Lie group". He uses the Lie structure three times: Appendix 3 (a compact
Lie group has an orthogonal real representation, which is what makes
reversible transformations rotations), section 8.6 (the Lie dimension
cannot be one, so the pure states of a qubit fill a two-surface, the
sphere), and the antipode argument of A3.4. A countable group of
rational transformations is not a Lie group, has no generators, and its
pure-state orbit is totally disconnected, so Axiom 5 in Hardy's reading is
false for it. What survives under the weaker reading "arbitrarily small
reversible steps, any two pure states joined by a chain of them": K = N is
still excluded, since permutations are never close to the identity, and
K = N^2 follows by simplicity; the Born rule and the sphere equation are
algebraic and hold for the rational points. What does not survive without
a closure step: the Lie group, hence Hamiltonians, Stone's theorem and the
Schroedinger equation.

### 10.2 The rational theory is a consistent dense subtheory [STRUCTURAL]

Quantum theory over the Gaussian rationals Q(i): states are the Q(i)-points
of the unit sphere of C^K, transformations the unitaries with Q(i) entries,
probabilities rational. It satisfies Hardy's Axioms 1 to 4 and the weak
Axiom 5 (the rational points of SU(2) are dense), has superposition,
entanglement and Bell violation, and is closed under composition,
subspaces and tensor products. Three things it lacks. (i) Lie structure,
as above. (ii) The Tsirelson bound: the CHSH value of Q(i) data is
rational, so 2 sqrt 2 is approached and never attained. (iii) The
fixed-point premise (F): the unitary
U = [[1/2 + i/2, (1+i)/2], [-(1-i)/2, 1/2 - i/2]] has entries in Q(i),
trace 1 and determinant 1, so its eigenvalues are exp(+-i pi/3) and its
eigenvectors involve sqrt 3, outside Q(i)^2. It fixes no admissible state
(script). Closing under fixed points, the lamp principle, extends the
field: iterated, to the algebraic numbers.

### 10.3 The algebraic theory: (F) without the continuum [STRUCTURAL; the reading CANDIDATE]

Quantum theory over the algebraic numbers (amplitudes in the algebraic
closure of Q intersected with C) satisfies (F), since eigenvectors of
algebraic matrices are algebraic; it is transitive on its pure states; it
has arbitrarily small transformations and elements of infinite projective
order (the rotation of section 9.3 is algebraic); and it is countable and
totally disconnected. So it is a countermodel to "(F) and transitivity
give the continuum" *without closedness*, exactly as the theorem of
2026-10-10 requires: that theorem assumes a closed, hence compact Lie,
group. Three nested theories now mark the three premises:

| theory | finite foils | algebraic | closure (quantum theory) |
| --- | --- | --- | --- |
| (F) holds | no | yes | yes |
| infinite order | no | yes | yes |
| connected | no | no | yes |
| separated from the next by | (F) with transitivity | closedness | --- |

Closedness is therefore not a technicality to be discharged by density
arguments (block B9's "operationally indistinguishable"): it is the one
premise that separates the algebraic theory from quantum theory, and
nothing operational at finite precision can tell them apart. The paper's
own sentence, "Hardy's fifth axiom is the demand that the transformation
group contain its non-computable limits", is exactly right and can be
sharpened to "its transcendental limits".

### 10.4 The framework's time is discrete, and the Koide phase is the witness [CANDIDATE]

In the framework time is operation count, an integer. A theory with a
discrete clock and an algebraic gate set never leaves the algebraic theory:
no product of algebraic gates has a transcendental entry. So the framework
does not get Hardy's Lie structure from its own dynamics; it gets it only
from the closure stance. The one place the framework needs a transcendental
is the Koide phase: if delta = 2/9 rad exactly, cos(delta) is
transcendental by Lindemann, and the transformation carrying that phase is
in no algebraic theory (results ledger, 2026-09-11, STRUCTURAL, now read
from the dynamics side). The charged-lepton spectrum is thus not only a
witness of infinite order (2026-10-10T1300) but a witness of the closure
itself: the only empirical evidence in the framework that nature's
transformation group is the compact Lie group and not its countable
algebraic subgroup. This also gives the 2026-09-11 CONJECTURE ("a rational
number of radians is the signature of flat geometry with rational
periods") a second reading: a rational number of radians is the signature
of a transformation outside the algebraic theory, so op:koide-delta and
op:limit-realisability are coupled, and a derivation of delta from
algebraic data fails before any detail is checked, as the ledger already
says.

### 10.5 Labels proposed

- **STRUCTURAL** Hardy's derivation uses the compact Lie structure of the
  reversible group in Appendix 3 and section 8.6; with a countable dense
  group of transformations K = N^2 and the Born rule survive and the Lie
  structure does not.
- **STRUCTURAL** Quantum theory over Q(i) violates (F) (explicit unitary,
  eigenvalues exp(+-i pi/3)); quantum theory over the algebraic numbers
  satisfies (F), transitivity and infinite order, and is totally
  disconnected. Closedness is the premise that separates it from quantum
  theory.
- **CANDIDATE** With time an operation count, the framework's dynamics is
  algebraic unless a gate carries a transcendental phase; the Koide phase
  2/9 rad is the framework's witness that nature's group is the closure.
  Couples op:koide-delta to op:limit-realisability.
- *Correction to section 9.4 of this note:* "the lamp principle generates
  quantum theory from the fragment" holds with closedness; without it the
  lamp principle generates the algebraic theory.

### 10.6 Exact stdout of `scripts/rational_unitary_fixed_points_2026-10-28T1800.py`

```
unitary: True  trace (1+0j)  det (1+0j)
eigenvalues: [0.5+0.866025j 0.5-0.866025j]  = exp(+-i pi/3): True
projective order: 3
eigenvector 0, normalised to first component 1: second component = 0.366025+0.366025j; |second|^2 = 0.267949 (eigenvector 0: 2 - sqrt3, off by -5.6e-17; eigenvector 1: 2 + sqrt3)
eigenvector 1, normalised to first component 1: second component = -1.366025-1.366025j; |second|^2 = 3.732051 (eigenvector 0: 2 - sqrt3, off by 3.5e+00; eigenvector 1: 2 + sqrt3)
cos(2/9) = 0.9754100853894475  (transcendental by Lindemann; a rotation by 2/9 rad is outside the algebraic theory)
RATIONAL UNITARY: PASS
```

### 10.7 Correction to 10.4: the Koide phase is a commitment, not a witness, and not a step (added 2026-10-28T1900)

JS: "Why does the Koide phase enter into a derivation of closure? I think
of the Koide phase as something to do with lepton masses." It does not
enter the derivation. Closedness is adopted in the paper and nothing in
sections 9 or 10 derives it; 10.4 overstated the phase's role, and this
subsection replaces it.

*How a mass number is a phase of a transformation.* By
prop:koide-jordan (ledger 2026-09-11, STRUCTURAL), 3 delta is the
Bargmann invariant of the three generation states: the phase picked up
around the loop psi_1 -> psi_2 -> psi_3 -> psi_1, a holonomy, which is a
product of the transformations carrying one generation state to the
next. So the Koide phase is a phase of a transformation of the regime,
and whether such a phase can be transcendental is the closure question of
10.3. That is the only reason it appeared.

*Why it is not evidence.* A number matched to five figures cannot
certify transcendence: an algebraic number lies within any measured band.
10.3 says this itself, that nothing operational at finite precision
separates the algebraic theory from its closure. So the Koide phase is
not a witness of closure, and "the only empirical witness" in 10.4 is
withdrawn.

*What it is.* A commitment. The paper matches delta to 2/9 rad exactly,
and the ledger records that then exp(i delta) is transcendental. A
framework that asserts delta = 2/9 exactly asserts a holonomy outside the
algebraic theory, and so has already taken the operational reading of
closedness rather than the constructive one; the two readings part at
exactly this number. That is a consistency statement about the
framework's own assertions, RHYME-level for op:limit-realisability, and it
cuts the other way too: a derivation of delta from algebraic data (a root
of unity, a finite group, a polygon with algebraic vertices) would force
delta transcendental-or-zero and is already on the FAIL list of
op:koide-delta. The coupling of the two open problems is this and no
more.

*Labels.* The CANDIDATE of 10.5, third bullet, is withdrawn and replaced
by: **RHYME** the framework's exact 2/9 rad is a holonomy outside the
algebraic theory, so the framework is committed to the operational
reading of closedness; the coupling to op:koide-delta is through
prop:koide-jordan and the FAIL clause already in the ledger.

## 11. Why closure cannot be derived, and what to do instead (added 2026-10-28T2000)

JS: "all of our suggested routes apply equally to rational probabilities as
to irrational probabilities and therefore form a disconnected set ... If we
add the requirement for closure then we can get to continuous
transformations between pure states. But how do we justify closure?"

### 11.1 The diagnosis, sharpened [STRUCTURAL]

Every route in the 2026-10-18 review, and the fixed-point route of
2026-10-10 and sections 2 to 9 above, is a condition that holds in the
algebraic theory of 10.3. That is not an accident of the routes. Any
collection of principles each of which is a first-order statement about
states, transformations and probabilities has, if it has an infinite
model, a countable one (Loewenheim--Skolem); and a countable subset of
CP^{K-1} is totally disconnected. So no such collection can imply
connectedness. Hardy's Axiom 5 escapes only because it is second-order:
it quantifies over paths. Closedness is second-order in the same way: it
quantifies over all Cauchy sequences. The routes failed because they were
first-order, and no first-order route can succeed.

### 11.2 The founding non-computability does not escape either [STRUCTURAL; closes a route]

One might hope the paper's founding move, that self-reference forces
non-computable amplitudes, breaks the symmetry: the algebraic numbers are
all computable, so a non-computable amplitude is outside the algebraic
theory. It is, but not outside every countable theory. The arithmetical
complex numbers (those whose digit sets are definable in first-order
arithmetic) form a countable algebraically closed field containing
non-computable numbers; eigenvectors of arithmetical unitaries are
arithmetical, so (F) holds; limits of arithmetical Cauchy sequences are
arithmetical, so the theory is closed under every limit it can itself
describe; and it is finitely stated and totally disconnected. The same
holds at every level of the definable hierarchy. Limit-realisability in
the paper's own words, "a Cauchy sequence of available transformations
whose convergence the system can itself describe must have its limit
available", is satisfied by each of these countable theories, because
"can itself describe" picks out countably many sequences. The Specker
bridge of the July ledger (a computable bounded increasing sequence of
rationals with non-computable supremum) shows the computable theory is
not limit-closed; it lands in the next countable field, not in the
continuum. So: *closure cannot be derived from non-computability, nor
from self-describable limits, nor from any first-order principle*. Logged
as a closed route.

The constructivist's point, which the paper already concedes, is the same
fact from the other side: a physically realisable sequence of
preparations is finitely specified, so the realisable Cauchy sequences
are countable and their limits form a countable set. The full completion
closes under sequences no one can specify. Closure is adopted, or it is
nothing; the only question is what the adoption costs and what it buys.

### 11.3 What closure buys: nothing empirical [STRUCTURAL]

The algebraic theory and its closure agree on every finite-precision
prediction: every measured number is matched by an algebraic one, the
Tsirelson value 2 sqrt 2 is algebraic and attained, K = N^2 and the Born
rule are theorems of both, and the invariants of the dense group are the
invariants of its closure. What the closure adds is the Lie structure:
generators, Hamiltonians, Stone's theorem, the Schroedinger equation. In
a framework whose time is an operation count these are representations of
a discrete dynamics, not its content. Hardy's own gloss of "continuous",
"made up from many small transformations", is at finite precision a
statement of density, and density is what an experiment can see.

### 11.4 Two honest positions [CANDIDATE; JS to choose]

**A. Completion as definition; density as the theorem.** A state is what
a sequence of preparations that converges at every finite precision
converges to: the completion of the preparation classes under the
finite-precision metric. This is a definition, the same one that makes a
length a real number rather than a rational one, and it is where every
reconstruction, Hardy's Axiom 1 included, puts the continuum (the July
ledger's B4 and B7 saw this). It has no empirical content, so a referee
cannot say continuity has been assumed; what has been defined in is
exactly the part no experiment can contest. The empirical content of
Hardy's Axiom 5 is then density, and density is derived: (I) with
transitivity gives (F), (F) with transitivity gives an element of
infinite order (sections 3 and 9.3), and the orbit of an infinite-order
element is dense in a positive-dimensional compact group. The section's
title stands with its claim restated: Hardy's fifth axiom is a definition
plus a theorem, not an axiom. The paper's sentence "Hardy's fifth axiom is
the demand that the transformation group contain its non-computable
limits" would become "contain its limits; once it does, almost all of
them are non-computable", since non-computability is a property of the
completed continuum, not the reason for it. `op:limit-realisability`
splits: the value-continuum clause dissolves into density plus the
definition; the remaining OPEN is to derive (I) from self-referential
closure, which is first-order and so may be derivable.

**B. The continuum is emergent.** Take "It from Bit" literally: the
fundamental regime is the algebraic (or computable) theory, countable and
dense, with a discrete operation count and no Hamiltonian; the continuum
is what emerges at the FANOUT boundary, as Paper 2 already says of
spacetime. Then Paper 1 should not claim Hardy's axiom at all, only
density, and the amplitude continuum is inherited from the emergent
one. This is coherent with the framework's discrete time, and it is
radical: the Schroedinger equation becomes an effective description. It
also sits well with the paper's Thomson's-lamp paragraph, where the
record side is not limit-closed and the amplitude side is; on reading B
the amplitude side is limit-closed only in the emergent description.

Either way the paper stops owing a derivation of closure, because none is
possible, and says so with the reason (11.1). The remaining debt is (I).

### 11.5 Proposed entries

- **STRUCTURAL** No collection of first-order principles about states,
  transformations and probabilities implies a connected pure-state space
  (Loewenheim--Skolem); the arithmetical complex numbers give a countable
  model satisfying (F), transitivity, non-computable amplitudes and
  closure under all self-describable limits. Closedness is second-order
  and is adopted, not derived.
- *invalid_routes.md:* deriving closure from the founding
  non-computability, from limit-realisability of self-describable
  sequences, or from any first-order principle (the arithmetical model).
  Subsumes the Specker bridge of the July ledger as a route to closure.
- **CANDIDATE** Position A above: completion is a definition with no
  empirical content; density is the empirical content of Hardy's Axiom 5
  and is derived from (I) and transitivity. `op:limit-realisability`
  restated accordingly, with (I) the remaining OPEN item.
- **CANDIDATE** Position B as the alternative, to be ruled on against
  Paper 2's emergence of the continuum.

### 11.6 Not derivable is not ungrounded (added 2026-10-28T2100)

JS: "the statement that a derivation of closure is not possible suggests
that closure itself is ungrounded." It does not, and the distinction
matters for how the paper states its stance.

*The model case.* Dedekind completeness is not derivable from the
ordered-field axioms (Q satisfies them all), and no one holds that the real
line is ungrounded. It is grounded by two things: categoricity, there
being exactly one complete ordered field, so that completeness is the one
extension that leaves no further choice; and role, that it is what makes
limits exist. A second-order principle is grounded in that way or not at
all. Closedness is a principle of that type, and its grounding has the
same two parts, with a third that is the framework's own.

*Grounding (i): self-reference says no level suffices* [CANDIDATE, the
founding move]. Every observer is a finite system with a definite
descriptive power, a level in the definability hierarchy of 11.2. The
founding move says the observer's own state exceeds its own level; the
inside/outside principle says this is not a defect of one perspective but
a law, so it holds of every observer at every level. Hence the state
space is not the countable model at any level: each such model is the
view of an observer of bounded resources, and the regime is the view of
none of them.

*Grounding (ii): the completion is the unique level-independent
structure* [STRUCTURAL]. The completion of a dense set under the
finite-precision metric is unique up to isometry, contains every level,
and depends on none. Any other candidate, a particular level or a
particular transfinite stage, is a choice, and the choice is an
additional law, "amplitudes are arithmetical", with no ground and no
test. The completion posits no such law. By the ordinary scientific
standard of not asserting an undetectable restriction, the completion is
the least committal option, not the most.

*Grounding (iii): a chosen level is a datum the regime does not carry*
[RHYME until written against sec:fanout-boundary]. A level is an integer
or an ordinal that would have to be written somewhere; the regime before
any record carries no such datum. This is the no-record face of the
regime said of the field; it is suggestive, and the 2026-10-18 objection
that a mathematical restriction is not a readable record applies to it,
which is why it is fenced as RHYME and the weight is carried by (ii).

*What would be ungrounded.* The reverse assertion: that the state space is
some specific countable field. That is the claim that needs a derivation
it cannot have, since no experiment and no principle picks the level. The
burden falls on the restriction, not on the completion.

*What this is not.* It is not a derivation, and the paper should not call
it one. "Closedness is adopted" stays; what changes is that the adoption
is shown to be grounded, by (i) and (ii), and the ungrounded alternative
is named. The honest sentence for the paper: continuity is a
second-order principle, grounded as every completeness principle is
grounded, by the uniqueness of the completion and by the framework's own
result that no observer's descriptive level captures the regime; its
empirical content is density, which is derived.

- **CANDIDATE** Closedness is grounded, not derived: (i) self-reference
  with inside/outside equivalence gives that no definability level
  captures the regime; (ii) the completion is the unique level-independent
  structure and the least committal; a specific countable field is the
  ungrounded assertion. Proposed as the paper's stated ground for
  limit-realisability, replacing "adopted stance" with "adopted on these
  grounds".

## 12. Is self-referential ignorance enough? Where the continuum actually enters (added 2026-10-29T0900)

JS: the paper's thesis is that every axiomatisation rich enough for
quantum mechanics smuggles in self-reference in some disguise, Hardy's
continuity among them, since it permits the superposition of true and
false that is the liar's fixed point; so explicit self-reference should
derive continuity without a further axiom; but we found closure had to be
added; so self-referential ignorance on its own seems not enough.

### 12.1 Hardy's "continuous" is two things, and only one of them is quantum [STRUCTURAL]

Hardy's Axiom 5 asserts that the pure states are joined by continuous
paths. Sections 10 and 11 split that into (a) the pure states are
infinite and dense, with fixed points for every transformation, and (b)
the state space is complete. The algebraic theory has (a) and not (b),
and it is fully quantum: K = N^2, the Born rule, superposition,
entanglement, Bell violation at the Tsirelson value, the fixed point of
every transformation. So the quantum/classical difference lives entirely
in (a). Part (b) is not a quantum axiom in disguise; it is the real-number
convention of all probability theory, and Hardy adopts it before Axiom 5
is stated: Axiom 1 makes probabilities real numbers (limits of relative
frequencies), and Axioms 1 to 4 already give classical probability
theory whose mixtures fill a real simplex. The continuum is in Hardy's
classical theory; what "continuous" in Axiom 5 adds, given Axiom 1, is
that the *pure* states are dense in a connected set rather than finitely
many. Given the real convention, density of pure states is connectedness
of their closure.

### 12.2 The liar's fixed point is in the smallest theory [STRUCTURAL]

The lamp's self-consistent value (1 + i)/2 is a Gaussian rational, and
the corresponding state, equal weights with a quarter-turn phase, is a
stabiliser state, the Y eigenstate. The single liar therefore does not
even leave the stabiliser fragment. What leaves it is self-reference
applied to every protocol: the fixed point of a Z-phase followed by an
X-phase is a magic state (section 9.3), and closing under all such fixed
points with transitivity gives density. So the self-referential content
of Axiom 5 is (F) for composite transformations, the observer surviving
every protocol, not the liar alone. That content is what sections 2 to 9
derive, conditionally on (I).

### 12.3 Where the framework's continuum enters [STRUCTURAL about the paper; the reading CANDIDATE]

The paper does not start from Hardy's Axiom 1. Its continuum enters at
the Shannon step, where credences are declared to range over a connected
domain so that the continuation of the logarithm is unique
(`sec:complex-amplitudes`; the paper says "declared once there, consumed
at the continuation, here"). That is the same declaration classical
probability makes. Cox's theorem, which the Jaynes appendix leans on,
needs it too: Halpern showed the theorem fails on finite domains and the
repair is a density assumption on plausibility values (Halpern 1999,
Paris 1994, both VERIFY-CITE), after which the values are completed to
the reals by the same convention. So classical and quantum probability
have the same shape, density plus completion, and the completion is
common to both. The classical density is of credences; the quantum
density is of pure states; and the second is what self-reference
supplies.

So "we have to introduce closure to get continuity" is misdescribed. The
framework introduced it at the Shannon step, in the classical part, as
every probability theory does; nothing quantum hides in it, since the
algebraic theory is as quantum as the closure; and the quantum part of
Hardy's axiom, density of pure states, is derived from self-reference,
conditionally on (I). The thesis survives in its correct scope:
self-referential ignorance deduces the quantum formalism *from classical
probability*; it does not deduce the real numbers, and nothing does.

### 12.4 What is honestly left

- (I), every admissible transformation a phase of an admissible
  structure, from self-referential closure: OPEN, first-order, so a
  derivation is possible in principle (section 11.4).
- The completion convention: adopted on the grounds of 11.6, shared with
  classical probability, carrying no quantum content. The paper should say
  this in `sec:continuity` and in `op:limit-realisability`, and should
  move the sentence about non-computable limits accordingly.
- Retrocausality as disguised self-reference: untouched by any of this;
  the anti-event identity lives in the algebraic theory as much as in the
  closure.

### 12.5 Proposed entries

- **STRUCTURAL** Hardy's fifth axiom is density of pure states plus the
  completion already present in his Axiom 1; the algebraic theory shows
  the quantum/classical difference lies wholly in the density.
- **STRUCTURAL** The liar's fixed point (1+i)/2 is Gaussian rational and
  its state is a stabiliser state; the self-referential content that
  exceeds the finite foils is the fixed point of composite protocols.
- **CANDIDATE** The framework's continuum enters at the Shannon step as
  the classical credence continuum (Cox with Halpern's density repair),
  not as a quantum axiom; self-reference supplies the density of pure
  states, which is the quantum content of Hardy's axiom. Restates the
  claim of `sec:continuity` in its defensible scope.

## 13. Premise (I) stated in full (added 2026-10-29T1000)

JS asked for the statement expanded. This is the definition the OPEN
item of 12.4 refers to.

*Setting.* A theory of the pre-measurement regime specifies three sets:
the admissible pure states P, the admissible classical structures
(observers' record bases) B, and the admissible reversible transformations
G. In the paper's calculus a classical structure is a dagger-special
commutative Frobenius algebra, equivalently an orthonormal basis
(Coecke, Pavlovic, Vicary), equivalently, by the 2026-10-08 definition, an
observer: a committed direction with its section, the copy map that a
FANOUT in that basis would fire. Its copyable states are the basis
vectors; for a qubit, the two poles of an axis.

*Phase.* The phases of a classical structure are the reversible maps the
structure itself generates: in the ZX-calculus, the spiders of that colour
carrying a phase; concretely, the unitaries diagonal in the structure's
basis, multiplying the k-th basis vector by exp(i alpha_k). Coecke and
Duncan call the set of them the phase group of the structure. A phase
leaves every copyable state of the structure where it is and moves only
the relative phases between them, the data the structure's record would
not carry. Equivalently: the phases of a structure are exactly the
reversible maps that commute with its copy map up to the phase itself,
the maps a FANOUT in that basis cannot see.

*(I).* For every g in G there is a structure b in B such that g is a
phase of b. In words: every admissible transformation is diagonal in some
admissible observer's record basis; no transformation of the regime is
relative to an observer the regime does not contain; there are no absolute
transformations, as there are no absolute states.

*Readings, all the same statement.* (1) Relational: a transformation is a
change of relation, and it is "about" the observer whose relation to the
system it preserves. (2) Implementer: what performs g has an axis, the
axis is a committed direction, a committed direction is a structure, and
that structure is in the theory. (3) Clock: the observer relative to whom
g is a phase has a stationary self-record and an advancing phase; (I) says
every transformation is evolution relative to an internal clock. (4)
Self-observation (section 9): b's copyable states are the counterfactual
self-observations that g leaves alone.

*What it implies.* A phase of b fixes b's copyable states, which are in P;
so every g fixes an admissible pure state, (F). With transitivity and at
least two pure states, (F) gives an element of infinite projective order
and a dense orbit (Jordan's derangement theorem for the finite case;
sections 3 and 9.3); with the completion convention of section 12, a
connected P and Hardy's Axiom 5.

*What it does not assume.* No one-parameter group, no generator, no
Hamiltonian: the phase group of a structure in a finite theory is finite
(Z_4 for each Pauli basis in the stabiliser fragment). No Hilbert space:
"phase of a structure" is defined in the calculus. No connectedness: (I)
is a condition checkable one transformation at a time in a finite theory.

*Who satisfies it.* Quantum theory over any field closed under taking
eigenvectors: every unitary is a phase of its eigenbasis (spectral
theorem), so complex quantum theory, the algebraic theory, the
arithmetical theory. Who violates it: the stabiliser fragment (14 of 24
elements, exactly the derangements; the composite of two admissible
phases is a phase of nothing admissible), Spekkens's toy theory (its
three-cycles are phases of no epistemic basis), the rebit and real
quantum theory in even dimension (a rotation of the real plane has no
real axis), and quantum theory over Q(i) (the unitary of section 10.2).

*In dimension above two* (I) is stronger than (F): it asks that the fixed
points of g form a whole admissible basis, not that one of them exist.
Degenerate phases fix a subspace; its pure states are still fixed, so
(F) follows in every dimension.

*What a derivation would have to show.* That the paper's inside/outside
involution (`prop:inside-outside`) entails that the generator of every
admissible transformation is an admissible system, i.e. that "nothing acts
on the regime from outside" is the same statement as "every transformation
is a phase of an inside structure" and not a stronger one. The relational
twin, "no absolute states", is already the paper's position (the global
phase as self-ignorance; Postulate 4); (I) asks the paper to say the same
of transformations. First-order; so, unlike closure, derivable in
principle.

## 14. The inside/outside tower yields (I) (added 2026-10-29T1200)

JS, in Popper's terms: C cannot predict its future interaction with E,
since that needs complete knowledge of its own state; C+ can have complete
knowledge of C and E together and so can predict; but C+ cannot predict
its own interaction with C+E. Wigner's friend likewise: WF cannot predict
its interaction with S, W can know WF+S completely, W cannot predict its
own interaction with WF+S. The restriction: inside and outside views must
agree on anything both can measure. "This restriction is important."

### 14.1 What the agreement condition fixes, and what it does not [STRUCTURAL]

Agreement on shared measurables is the statement that WF's record basis
is a structure W can see: W measuring WF's register in that basis finds
WF's outcome, because the record-forming map is the copy map of a
classical structure (Coecke, Pavlovic, Vicary). So the condition makes
every inside record basis an outside-admissible structure, the same B at
every level. W's conjugate measurement, which erases WF's record, is not
something WF can measure, so no agreement is owed there; outcome and
relation are complementary observables of WF+S. All of this holds in the
stabiliser fragment, which is a consistent subtheory, so agreement alone
does not exclude the finite foils. What excludes them is the second half
of JS's statement: that the outside *can have complete knowledge* of the
inside, read together with what "time" is in the paper.

### 14.2 The derivation sketch [CANDIDATE; the pieces labelled]

Premises.

- **T1** (JS, the tower; purification in CDP's language, flagged on
  2026-10-18 as a direction): C+ can have complete knowledge of C+E. In
  the paper's terms, complete knowledge is a potential record: the state
  of C+E is a copyable state of some structure C+ carries, and by
  inside/outside equivalence C+'s structures are the theory's.
- **T2** (paper, `sec:space-of-computations`): time is operation count,
  internal to the system that operates. C's count is C's own; C+ does not
  share it, and reading it would be a FANOUT on C.
- **T3** (the regime): before any FANOUT, C's count is not classically
  recorded anywhere, so C+'s description of C+E is pure, not a mixture
  over counts.

Argument. Let g be the transformation C performs on E per operation (a
protocol, possibly composite). By T2, C+'s complete knowledge of C+E
cannot depend on C's count k: whatever structure holds the state must hold
it at every k. By T3 the state is pure, so C+'s count-independent complete
description is a pure state of (C's clock) + E that is stationary under
"advance the clock and apply g". The stationary states of that map are the
Fourier modes of the clock tensored with the eigenvectors of g, and
nothing else (Page and Wootters; the history state
sum_k |k> (x) g^k psi is stationary with eigenvalue lambda exactly when
psi lies in g's lambda-eigenspace). So C+ has a structure in which g acts
by phases: g is a phase of an admissible structure. That is (I).

Equivalently, in the paper's vocabulary: the outside's ignorance of the
inside's count is not a classical unknown (that would be a record, T3) and
not shared knowledge (T2), so it is a phase, and the structure in which
it is a phase is the eigenbasis of the inside's dynamics. The paper says
the global phase is the observer's self-ignorance of its own
computational state; the tower says the relative phase in the eigenbasis
is the outside's ignorance of the inside's computational count, which by
inside/outside equivalence is the same statement one level up. This is
the clock reading of 9.2, now derived from the tower rather than read
into it.

### 14.3 How the fragment breaks it [STRUCTURAL]

Take C = WF running the protocol "Z-phase then X-phase", of projective
order three, on a qubit S. Its eigenvectors are the F magic states (section
9.3), not in the fragment. So no pure stationary description of
clock + S exists in the fragment, and W's knowledge of S under WF's
protocol is either count-dependent (W shares WF's clock, against T2) or a
mixture over the count mod 3 (the count is a classical record, against
T3). The fragment is therefore a theory in which the inside's time is
classical before any FANOUT: it violates the regime's definition at
exactly the transformations where it violates (I). The same holds for the
toy theory's three-cycles, for the rebit's rotations and for the
Gaussian-rational unitary of 10.2.

### 14.4 What is still owed, exactly

- T1 is purification. Chiribella, D'Ariano and Perinotti take it as an
  axiom; here it is JS's tower premise, that the outside view exists and
  is complete. Whether it follows from `prop:inside-outside` or is the
  framework's form of that principle should be said in the paper. It is
  the one premise in the sketch that a reconstruction programme would
  recognise as an axiom.
- T3 is the regime's definition and T2 the paper's time doctrine; neither
  is new.
- The Page--Wootters step is standard (Page and Wootters 1983, VERIFY-CITE
  for the key; the paper's Jacobson and spacetime sections may already
  cite it).
- With (I) in hand: (F), infinite order, density (sections 3 and 9.3); the
  completion is the classical convention of section 12. The chain from
  self-referential ignorance to Hardy's Axiom 5 then has one axiom-shaped
  premise, T1, and it is the one JS stated.

### 14.5 Proposed entries

- **CANDIDATE** (I) follows from three premises: the outside can have
  complete knowledge of the inside (T1, purification as the existence of
  the outside view), time is operation count internal to the operator
  (T2), and the count is not classically recorded before FANOUT (T3). The
  outside's count-independent pure description of clock + system is
  stationary, and stationary states exist iff the inside's transformation
  has admissible eigenvectors (Page--Wootters). Supersedes the
  "adopted" status of (I) in sections 6 and 9.4 if accepted.
- **STRUCTURAL** In the stabiliser fragment the order-three protocol has
  no pure stationary clock + system description, so the fragment makes
  the inside's count classical before any FANOUT.
- **RHYME** The relative phase in the eigenbasis of the inside's dynamics
  is the outside's ignorance of the inside's computational count; the
  paper's "global phase as self-ignorance of one's own computational
  state" is the same sentence one level down.

## 15. The accounting closes on the paper's own premise (added 2026-10-29T1400)

JS: "The fundamental premise of the paper is that self-reference is
fundamental, but is experienced as a non-self-referential sequence of
events, and that the two things together, self-reference experienced as
non-self-reference, completely constrain the form of natural laws. The
inside/outside view is the axiom-shaped premise."

Checked against `sec:self-reference` ("One principle, and a theorem").
The paper's single commitment is that the category of descriptions
contains a self-representing object (self-reference foundational, stated
as Lawvere's point-surjectivity). The inside/outside involution sigma
exchanges the inside presentation (participant-indexed, the observer part
of the system) and the outside presentation (base-times-fibre over a
classical parameter space); sigma^2 = id is "a coherence requirement: the
outside view of the inside view of a thing is the thing"; physical law is
Fix(sigma); and the paper lists what it assumes: "the setting itself and
the existence of sigma as a genuine involution".

The three premises of section 14 map onto this without remainder.

- T1, the outside can have complete knowledge of the inside, is the
  existence of sigma as a genuine involution: the outside presentation is
  a presentation of the same object, nothing lost between the two views.
  Were the outside view a mixture, going out and back would lose
  information and sigma would not square to the identity. So T1 is not
  purification imported from CDP; it is the paper's coherence requirement,
  and CDP's purification axiom is what that requirement looks like from
  inside a reconstruction programme that lacks sigma.
- T2 and T3, time as internal operation count and no record before
  FANOUT, are the content of "experienced as a non-self-referential
  sequence of events": the inside presentation is a sequence, its index
  is the count, and its events are the records.
- "The two together" is sigma itself, and (I) is a property of
  Fix(sigma): a transformation that is a phase of no inside structure has
  no stationary outside presentation, so it is not invariant under the
  exchange of views and is not a law.

The accounting for Hardy's fifth axiom is then: the paper's one
commitment, the existence of sigma, and the completion convention of
section 12 that classical probability shares. Nothing else. The sentence
in 14.4 calling T1 "the one premise a reconstruction programme would
recognise as an axiom" stands, with the gloss that the paper has already
named it as its assumption.

*Proposed restatement of `op:limit-realisability`.* The value-continuum
clause is dissolved: density of pure states follows from (I) with
transitivity, and the completion is the classical credence continuum
declared at the Shannon step. What remains OPEN, with PASS/FAIL: make the
derivation of (I) in section 14 rigorous inside Fix(sigma). PASS: a proof
that every endomap in Fix(sigma) is a phase of a classical structure in
Fix(sigma), from the self-representing object, sigma, and the
operation-count reading of the inside presentation. FAIL: any step that
holds in the stabiliser fragment, the toy theory, the rebit or the
Gaussian-rational theory, all of which violate (I) and all of which make
the inside's count classical before any FANOUT (14.3).

*Proposed restatement of the claim of `sec:continuity`.* Hardy's fifth
axiom is density of pure states plus the completion. The completion is
the classical continuum, adopted on the grounds of 11.6 and carrying no
quantum content. The density is derived from self-reference experienced
as a sequence: every transformation the inside performs must have a
stationary outside presentation, hence an admissible eigenbasis, hence a
fixed point; fixed points with transitivity give infinite order and
density. Continuity is not an axiom: its quantum content is a theorem of
the paper's one commitment and its coherence requirement, and its
non-quantum content is the real line.

## 16. Patch applied (2026-10-29T1500)

JS: "I accept the proposed changes to the paper. Go ahead and make the
changes." Applied by `scripts/patch_continuity_tower_premise_2026-10-29T1500.py`.

Exact stdout, exit status 0:

```
patched paper1/continuity_section_2026-07-04.tex  backup: paper1/continuity_section_2026-07-04.tex.2026-10-29T1500.bak
patched paper1/L2_metric_global_phase_section_2026_06_07.tex  backup: paper1/L2_metric_global_phase_section_2026_06_07.tex.2026-10-29T1500.bak
patched paper1/what_is_a_quantum_state.tex  backup: paper1/what_is_a_quantum_state.tex.2026-10-29T1500.bak
patched paper1/derivation_of_the_quantum_postulates.tex  backup: paper1/derivation_of_the_quantum_postulates.tex.2026-10-29T1500.bak
patched paper1/self_reference_section_2026-07-04.tex  backup: paper1/self_reference_section_2026-07-04.tex.2026-10-29T1500.bak
patched paper1/summary_section_2026-07-07.tex  backup: paper1/summary_section_2026-07-07.tex.2026-10-29T1500.bak
patched paper1/main.tex  backup: paper1/main.tex.2026-10-29T1500.bak
continuity section: 5 edits; cross-references: 7 edits in 6 files
new citation keys (batch bib/continuity_tower_refs_2026-10-29T1500.bib, import owed): pagewootters1983evolution, coeckeduncan2011interacting
PATCH: PASS
```

Second run refused with exit status 1:
`REFUSING: paper1/continuity_section_2026-07-04.tex already carries the EDITED header for this script`.

What changed. In `sec:continuity`: the opening paragraph (one premise
about transformations; the completion named as the real line); a closing
sentence on the foils paragraph; the "premises" subsection's value-premise
and closedness text replaced by three paragraphs (the density/completion
split with the algebraic theory as the foil; the completion as the
classical convention with its grounds, the Cantor and Turing sentences
kept and the non-computable sentence corrected; density from the tower
with premise (I), its three-premise derivation sketch via Page--Wootters,
its consequences and the foils); `op:limit-realisability` restated under
the title "Every transformation a phase of an inside structure", label
kept, PASS/FAIL as in section 15; the closing accounting sentence. In six
other files the sentences describing the open problem as a premise about
values are re-pointed. Divisibility's retirement is kept. The "Why the cut
matters physically" paragraph, flagged on 2026-10-10 with its own drafted
patch, is untouched and still owed.

Sanity checks on the edited section, no TeX on this machine: braces
balanced (107/107), proposition 3/3, proof 3/3, openproblem 1/1, inline
maths delimiters even, every `\autocite` key present in `references.bib`
except the two new ones, which the batch supplies.

Compile status: NOT RUN. TeX Live is not yet installed on the laptop. The
build must be run after installation; the two new keys will report
undefined until the batch is imported and the bibliography re-exported,
which is expected. VERIFY-SUPPORT stands on both new citations in the text.

Ledger entries: still proposals (sections 7, 9.5, 10.5, 11.5, 12.5, 14.5,
15); the maintainer writes them. Nothing committed.
