# Paradox, hypodox and the FANOUT boundary (2026-10-16T1100)

JS: "think about the nature of logical paradoxes such as 'The set of all sets
that are not members of themselves' or 'This statement is false', and
hypodoxes 'This statement is true', and pre-FANOUT, post-FANOUT states."

Fable session, thinking only. Script
`scripts/liar_hypodox_fanout_2026-10-16T1100.py` (seed 20261016, numpy only,
PASS; exact stdout in section 11). Reference batch
`bib/liar_hypodox_refs_2026-10-16T1200.bib` (16 keys; VERIFY-CITE and
VERIFY-SUPPORT items listed in its header). Nothing in the paper is patched.
Labels below are proposals; JS applies them. Companion notes:
`continuity_probability_conservation_2026-10-10T1000.md` and
`value_continuum_fixed_point_route_2026-10-10T1500.md` (premise (F)).

## 0. The answer in brief

A self-referential sentence "S has the value g(S)" is a fixed-point equation
v = g(v) on the value space. On the classical bit there are four endomaps g.
The two constants are grounded sentences, one fixed point each. The identity
is the Truth-teller, "this statement is true": two fixed points, nothing to
choose between them, Eldridge-Smith's hypodox, underdetermined. Negation is
the Liar: no fixed point, overdetermined. The paper already uses Lawvere's
theorem, that a self-representing object forces every endomap to have a
fixed point, and already says that the diagonal the theorem uses is the copy
map, which is FANOUT. What follows from putting the hypodox beside the
paradox is this.

*Pre-FANOUT* no structure is committed, there is no diagonal (Abramsky's
cloning-collapse theorem: a uniform one would make every endomorphism a
scalar), and the diagonal argument cannot run. What remains of the sentence
is the eigenvector equation on rays, and over the complex numbers every
endomap has a solution. Both ungrounded sentences have consistent states:
every ray solves the Truth-teller's equation, the two rays |+> and |-> solve
the Liar's. Neither is a record. This is Kripke's minimal fixed point, where
both sentences are gapped.

*Post-FANOUT in the record basis Z* the Truth-teller takes whichever value
the record writes and is consistent with it, since both values are fixed
points; the Liar has no record, dephasing its states gives the value 1/2,
Kleene's gap and not a value. A measurement outcome is a resolved hypodox:
true because it was written, undetermined before the writing. Wheeler's "it
from bit" is the resolution of hypodoxes.

*The Liar's consistent states are records in the complementary structure X*,
where the Liar operator acts as a truth-teller with a sign, X|+> = +|+> and
X|-> = -|->. Paradox and hypodox are exchanged by complementarity. The Liar
anticommutes with the record, XZ = -ZX, which the ledger already holds as
strong complementarity; the hypodox commutes with every record. The sign
that is "clearly visible" in "this statement is false" is the value of the
complementary record, a relative phase between the two Z-amplitudes, fibre
data in the sense of prop:f1-dictionary. It is not a negative probability.

*The Liar forces no negativity.* Its fixed states are stabiliser states,
vertices of the octahedron that is Spekkens's toy theory's state space,
non-negative in every Wootters Wigner convention and in the Kirkwood--Dirac
distribution over (Z, X); the toy theory resolves the Liar in exactly the
same way, its Z-flip fixing the two X-states, with no sign anywhere.
Negativity first appears at the fixed points of the Hadamard, the involution
that exchanges the record structure with the Liar's: Fix(H) is the pair of
H-type magic states with Bloch vector (1,0,+-1)/sqrt2, outside the
octahedron, Wigner minimum (1 - sqrt2)/4 in the convention that sees it. H
permutes the six stabiliser states with no fixed point (last week's script),
so a theory closed under the fixed points of its own exchange of inside and
outside must contain states no epistemically restricted model has. The
three-cycle of the three structures, the product of half a hypodox and half
a Liar, sqrtZ sqrtX, has the T-type magic states as fixed points, and every
order-3 Clifford element fixes only magic states. So the paper's
"self-referential paradoxes <=> negative probability" is right about the
regime and wrong about the example: the price of self-reference is charged
not at the Liar but at the exchange of record and complement, which is the
paper's own sigma, and at the composition of roots, which is continuity.

## 1. What the paper says now

- `paper1/self_reference_section_2026-07-04.tex`, proof of
  prop:inside-outside: "Where the same construction applied to Boolean
  negation yields paradox --- negation has no fixed point on a two-element
  type, so the conclusion explodes the premises --- the inside/outside
  involution is an honest involution on a rich type, and the conclusion is a
  constructive fixed point rather than a contradiction." Then: "Physical law
  is the structure carried by Fix(sigma)."
- Same file, sec:complex-amplitudes-2: "negativity is not a permissible
  convenience but the first price of self-referential closure, and it is
  charged exactly and only in the pre-record regime".
- `paper1/what_is_a_quantum_state.tex` (the FANOUT subsection, after the
  Popper quotation): "Hence self-referential paradoxes <=> negative
  probabilty." And earlier, after Spekkens and Abramsky: "So we get
  self-reference <=> contextuality <=> negative probability", followed by
  the paper's own complaint that "in the architypical case 'This sentence is
  false', the negation is clearly visible and totally obvious" and yet
  nothing explains negative probability.
- Same file, sec:reversible-continuity: reversible continuity "is what lets
  a superposition of |TRUE> and |FALSE> represent the classically
  inadmissible states of the paradoxes of self-reference".
- `paper1/appendices/fanout_boundary_section_2026-07-06.tex`: "The copy map
  *is* the diagonal Delta: A -> A x A, and Lawvere's fixed-point theorem ...
  is precisely a statement about what follows when a diagonal exists. The
  absence of a natural diagonal in the quantum category is therefore the
  categorical face of the self-reference obstruction." And
  prop:fanout-correspondence (b): "Pre-firing --- whenever rho has a
  non-zero off-diagonal element in B --- any tomographically complete
  quasi-probability representation respecting B is signed".

The hypodox appears nowhere in the paper. Every self-referential example is
the Liar.

## 2. Self-reference as a fixed-point equation [STRUCTURAL]

On the bit, v = g(v) with g one of the four maps {0,1} -> {0,1}. Script
part A: the constants have one fixed point each (grounded: the value is set
by the non-semantic facts), the identity has two (the Truth-teller), negation
none (the Liar). Eldridge-Smith coined "hypodox" for the Truth-teller's kind
(2007; "a paradox is incompatibly overdetermined, a hypodox is
underdetermined", 2019), conjectured that every paradox has a hypodoxical
dual, and credits Mackie (1973) with the first list of Truth-teller
counterparts. Kripke's construction (1975) adds the gap value 1/2 and takes
the minimal fixed point of the truth predicate: there both ungrounded
sentences are gapped (script: the Liar's only Kleene fixed point is 1/2,
the Truth-teller's are 0, 1/2 and 1). The Liar has a value in no fixed
point, which is Kripke's definition of paradoxical; the Truth-teller has a
value in some fixed points and none in the minimal one, ungrounded but not
paradoxical [VERIFY-SUPPORT: quoted from memory of the paper, not re-read
today]. Russell's set {x : x not in x} is the Liar with membership for
truth, R in R <=> R not in R; the co-Russell set {x : x in x} is the
Truth-teller, C in C <=> C in C (Sujan 2024; Eldridge-Smith 2023).

## 3. The diagonal is FANOUT: where the argument can run [STRUCTURAL, with the paper's reading]

Lawvere (1969): in a cartesian closed category, if phi: A -> Y^A is
point-surjective then every g: Y -> Y has a fixed point; the proof forms
a |-> g(phi(a)(a)), which needs the diagonal A -> A x A. The contrapositive
is the diagonal argument, and Yanofsky (2003) shows Cantor, Russell, Godel,
Tarski and Turing are instances. The appendix already identifies the diagonal
with the copy map. Abramsky's cloning-collapse theorem (2009, Theorem 11)
gives the quantum side its exact form: a compact category with uniform
cloning, a monoidal natural Delta_A: A -> A (x) A that is coassociative and
cocommutative, has every endomorphism a scalar multiple of the identity,
f = Tr(f) id_A; uniform deleting alone makes it a preorder (Proposition 15).
Script part E at one qubit: the space of linear Delta: C^2 -> C^2 (x) C^2
with Delta U = (U (x) U) Delta for all unitaries is {0}; the copy map of a
basis is natural for the permutation of that basis and fails for a phase
gate (residual 0.686) and for the scalar -1 (residual 2.83), which is the
fibre statement in the proof of prop:f1-dictionary.

So the diagonal argument has a domain: the copyable states of a committed
structure, the post-FANOUT states. Pre-FANOUT there is no diagonal to run it
with, and what survives of "S has the value g(S)" is the equation on rays,
g psi ~ psi, whose solutions are eigenvectors; over C every endomap has one.
That is premise (F) of the 2026-10-10 note, now seen for what it is:
Lawvere's conclusion holding pre-FANOUT on the base CP^1, where it fails on
the bit (the Liar) and, section 6, on the rebit (the quarter-turn).

Fence: Roberts (2023) shows Lawvere's theorem survives dropping weakening
and exchange; the abstract is silent on contraction, which is copying. If a
diagonal argument can be run without contraction, "no diagonal, no paradox"
needs qualifying. The paper must be read before the sentence is used.

## 4. The three readings of one equation [CANDIDATE]

Script part B. Record basis Z, Liar operator X, hypodox operator 1.

1. *Pre-FANOUT.* X has fixed rays |+> and |->, eigenvalues +1 and -1; both
   give Z-probabilities (1/2, 1/2), the value of part A's Kleene fixed point.
   Neither is Z-copyable (residuals 0.765 and 1.414). The identity fixes
   every ray. Both sentences are consistent and neither has a value: the
   regime "where there is no definite unknown to be ignorant of"
   (sec:born-rule).
2. *Post-FANOUT in Z.* Firing F_Z on |+-> gives the maximally mixed state:
   the Liar's record is the gap. Firing on any state gives a Z-record; the
   Truth-teller is consistent with it whichever way it falls, and the Born
   rule is the weight of the two resolutions. In Kripke's terms, choosing a
   non-minimal fixed point is choosing a value for each hypodox; a classical
   structure writes its own copyables and nothing else.
3. *Post-FANOUT in X.* |+-> are the copyables of X (residuals 1e-16), and
   X|+-> = +-|+->: the Liar operator is a signed truth-teller for the
   complementary structure. "Pre-FANOUT with respect to Z" and "post-FANOUT
   with respect to X" are the same state. The Liar relative to a record is
   what the complementary record looks like from this one.

Reading: a measurement outcome is a resolved hypodox, and the paradox is the
appearance, in one structure, of a record kept in the other. This is the
dictionary's prop:f1-dictionary said in logical words, and it is the sense
in which the paper's "superposition of |TRUE> and |FALSE> represents the
classically inadmissible states" is right: the superposition is admissible,
as a record, one structure over.

## 5. Paradox and hypodox exchanged by complementarity, with a sign [finite check ESTABLISHED; reading CANDIDATE]

X anticommutes with Z and 1 commutes with it (script). On the Bloch sphere
every self-referential endomap is a rotation about an axis n, and its fixed
rays are +-n. Axis z: fixes the records; the phase gate S = sqrtZ is "this
statement is true, with a quarter-turn", a hypodox with fibre data. Axis x
or y: fixes the complementary records, Liar type. Generic axis: fixes states
that are records of no stabiliser structure, section 6. The sign in the
Liar's -1 eigenvalue is the sign in the anticommutator XZ = -ZX, and the
ledger's STRUCTURAL entry that strong complementarity is anticommutation is
what makes "paradox = anticommutes with the record, hypodox = commutes" a
statement about classical structures rather than about one operator.

## 6. Negativity: the Liar does not force it; the exchange does [second-order finding; CANDIDATE]

(a) The Liar's fixed states have Kirkwood--Dirac distribution over (Z, X)
with entries 0 and 1/2, and Wootters Wigner function non-negative in all
eight sign conventions (script B). Their Bloch vectors have |n|_1 = 1: they
are vertices of the stabiliser octahedron, the toy theory's state space. The
toy theory's Z-flip, the permutation (13)(24) of its four ontic states,
fixes its two X-states and nothing else: the Liar is resolved inside a
noncontextual, epistemically restricted classical theory, with no sign.
The paper's two "<=> negative probability" sentences use the Liar as the
example; it is the one self-referential sentence that does not pay.

(b) Script C: for a rotation about n, the minimum over the eight conventions
of the Wigner function of its fixed state is exactly (1 - |n|_1)/4 (checked
on 200 random axes), negative iff n is off the three record axes. Script F:
the group generated mod phases by the Liar X, the signed truth-teller Z and
the involution H that exchanges their structures has eight elements, the
rebit's Clifford group. The three Paulis fix stabiliser states; the two
quarter-turns HX and XH fix the y-records; the two Hadamard-type involutions
fix the H-type magic states, |n|_1 = sqrt2, Wigner minimum -0.1036.
Fix(H) = (1,0,+-1)/sqrt2. H is real, so this is already true of the rebit.
Last week's script showed H permutes the six stabiliser states without a
fixed point; the toy theory's involutions all fix an epistemic state (its
derangements are the 3- and 4-cycles), so the two groups, though both S_4,
act inequivalently on their six states, and the toy theory never meets the
Hadamard's demand. A regime closed under the fixed points of the exchange of
record and complement, premise (F) applied to the exchange, contains states
outside every epistemically restricted model. At one qubit the exchange of
the record structure with its complement is the natural shadow of the
paper's sigma, and Fix(sigma), which prop:inside-outside says carries
physical law, is magic.

(c) The quarter-turn HX, the Liar composed with the exchange, has no real
fixed ray (eigenvalues e^{+-i pi/4}) and fixes |y+-> over C: the third
classical structure is the price of resolving that composite, and the rebit
cannot pay it. With the third structure, sqrtZ sqrtX, half a hypodox after
half a Liar, is of projective order 3 and fixes the T-type magic states,
|n|_1 = sqrt3, Wigner minimum -0.1830; the full Clifford group has 24
elements, 8 of order 3, each fixing only magic states. Roots are
continuity's gift (2026-10-10: divisibility follows from connectedness), so
the order is: Liar and hypodox give two complementary structures; the
exchange gives negativity; the composite with the exchange gives C; roots
and composition give the three-cycle and the second magic family.

(d) Two senses of "negative" are conflated in the paper's sentences: a sign
on an amplitude (the Liar's -1, the complementary record's value, a bit in
the toy theory) and a signed quasi-probability (outside the stabiliser
polytope, Spekkens's contextuality). The first is what "this statement is
false" shows. The second is what the chain self-reference -> negative
probability needs, and it arrives with the exchange, not with the Liar.

(e) prop:fanout-correspondence (b) overclaims. Read per state, "whenever rho
has a non-zero off-diagonal element in B, any tomographically complete
quasi-probability representation respecting B is signed" is false for
rho = |-><-|, B = Z: the Wootters function is tomographically complete, its
p-marginal is the Z-distribution, and it is non-negative. Spekkens's theorem
is about an operational theory, every preparation and measurement at once,
not about one state. The per-state pre-firing signature is non-copyability
in B, which (a) and script B exhibit; negativity is a property of the state
space the regime admits, and it begins at Fix(H). Clause (c) of the
proposition, that the two signatures vanish together at firing, inherits
the correction. For JS.

## 7. Russell, Godel, Henkin and Lob: provability as record [RHYME]

Naive comprehension, every predicate on sets is a set, is Lawvere's
point-surjective self-representation; Russell is its contrapositive with
negation, the co-Russell set the same construction with the identity, no
contradiction and no determination (Sujan derives a contradiction from the
co-Russell set with the fixed-point theorem of naive set theory, so the line
is not sharp there). In FANOUT terms comprehension is universal copying,
"every description is a record", which is cartesian; the quantum category
refuses it and offers one copy map per structure, so Russell's construction
runs on each structure's copyables and nowhere else.

Provability is the existence of a proof, a copyable object in a fixed
structure. The Godel sentence "no record of G exists" is the Liar with
record for truth, and it is not a contradiction because provability is
partial: G is true and unrecorded, a state definite in some structure and
uncopyable in this one. The Henkin sentence "a record of H exists" is the
hypodox of provability, and Lob (1955) proves it: H is provable. The
record-hypodox is settled by the structure itself, where the truth-hypodox
is settled by nothing. Tarski, no truth predicate, is no universal copy;
Godel, a provability predicate that is incomplete, is each structure copying
its basis and missing the rest; adding G as an axiom is committing the
complementary structure, at the price of the old records and with a new
unrecordable state. This is a rhyme: provability logic has the Lob axiom and
nothing in the framework has been shown to satisfy it. Dourdent's "quantum
Godelian hunch" (2020, in the library, not cited), Liar cycles and the
"emergence of time from self-contradiction", is the 2005 chain's hunch in
another hand; JS may want it beside small_2006 in the lineage paragraph.

## 8. Prior work and ownership

Lawvere 1969 and Yanofsky 2003 (the paper's); Abramsky 2009, the cloning
collapse; Abramsky and Zvesper 2015, interactive diagonalisation; Roberts
2023, substructural Lawvere; Abramsky et al. 2015, Liar cycles as
contextuality, which the paper cites and script D reproduces: the 4-cycle
with one negation has no global assignment and the one with two negations
has two, a hypodox cycle; the PR box satisfies all four edges where any
deterministic assignment satisfies at most three, and has a signed global
section with least weight -1/16 (Abramsky and Brandenburger). Eldridge-Smith
2007, 2019, 2023, Billon 2018 and Mackie 1973 on hypodoxes; Sujan 2024 on
co-Russell; Kripke 1975; Lob 1955. Szangolies 2020, in the library and
cited, applies Lawvere to measurement contexts; the state in his title is
|+>, the Liar's +1 fixed point, the resolution without the sign. Aerts,
Broekaert and Smets 1999 and 2006 model the Liar as a quantum state evolving
unitarily between readings, with a cognitive reading; Sassoli de Bianchi
2026 reconstructs it and finds the two-sentence Liar state entangled where
the non-paradoxical configurations are separable; Cheimarios and Cheimariou
2025 build a circuit stabilising the Liar's fixed point. None of these pairs
the hypodox with the paradox as the identity and negation endomaps, none
observes that the Liar's resolution lies inside the toy theory, and none
places the first negativity at the fixed points of the exchange of record
and complement. Two searches; claimed as the framework's with that caveat.

## 9. Fences

- One qubit throughout. H is the exchange of the record structure with its
  complement at one qubit; the paper's sigma is the inside/outside exchange
  of total space against base-times-fibre, and the identification is a
  reading, CANDIDATE at best, with op:sigma-functor's debt unchanged.
- Qubit Wigner negativity is convention-dependent; the invariant statement
  is "outside the stabiliser octahedron", equivalently |n|_1 > 1, and the
  script reports both.
- Lawvere's hypothesis, a point-surjective self-representation, is not
  instantiated here any more than last week; items 1 to 3 of the
  2026-10-10 note stand.
- Kripke's classification of the Truth-teller is from memory
  (VERIFY-SUPPORT). Roberts 2023 must be read for contraction. The Lob
  paragraph is a rhyme and is labelled one.
- "Self-reference forces negativity" now rests on (F) applied to the
  exchange involution; (F) is a premise. What the note shows is where the
  premise first bites, not that it holds.
- No statement about the second-order Liar ("this sentence is not true" in
  three-valued logic, the revenge Liar) is made; its natural counterpart is
  the three-cycle, and that is a guess.

## 10. Proposed wording and ledger entries (for JS)

Wording, `what_is_a_quantum_state.tex`, in place of "Hence self-referential
paradoxes <=> negative probabilty": "The negation visible in 'this
statement is false' is the value of a complementary record, a sign on an
amplitude; a signed probability is forced not by the Liar, whose consistent
states are stabiliser states, but by closure under the fixed points of the
exchange of record and complement, whose consistent states no
epistemically restricted model contains (Appendix, FANOUT boundary;
session note 2026-10-16)." The "self-reference <=> contextuality <=>
negative probability" sentence to be split into the two senses of section
6(d). Appendix prop:fanout-correspondence (b) to be restated at the level
of the operational theory with non-copyability as the per-state signature.

Ledger proposals:

- **ESTABLISHED** (finite check, script PASS) On C^2 with record basis Z the
  Liar endomap X has fixed rays |+->, the copyables of X, with
  Kirkwood--Dirac distribution over (Z,X) and Wootters Wigner function
  non-negative in every convention; the minimum over conventions of the
  Wigner function of the fixed state of a rotation about n is (1 - |n|_1)/4;
  the Hadamard's fixed states have |n|_1 = sqrt2 and every order-3 Clifford
  element's fixed states have |n|_1 = sqrt3; no linear map C^2 -> C^2 (x)
  C^2 is natural under U(2).
- **STRUCTURAL** Abramsky's cloning-collapse theorem; Kripke's grounded /
  paradoxical / ungrounded-not-paradoxical trichotomy; Eldridge-Smith's
  hypodox as the underdetermined dual of a paradox.
- **CANDIDATE** The three readings of section 4; paradox and hypodox
  exchanged by complementarity with the sign in the anticommutator;
  negativity first at Fix(H), the exchange of record and complement, and
  not at the Liar.
- **RHYME** Provability as record, Godel as the Liar of records, Henkin as
  its hypodox settled by Lob; Kripke's non-minimal fixed points as records.
- *Retraction proposed:* "self-referential paradoxes <=> negative
  probability" as it stands, and prop:fanout-correspondence (b) as a
  per-state claim. Recorded as a correction, not a claim.

## 11. Exact stdout of `scripts/liar_hypodox_fanout_2026-10-16T1100.py`

```
Liar, hypodox and FANOUT
======================================================================
A. classical endomaps of {0,1} and their fixed points
   const 0              fixed points on {0,1}: [0]
   const 1              fixed points on {0,1}: [1]
   id  (truth-teller)   fixed points on {0,1}: [0, 1]
   NOT (Liar)           fixed points on {0,1}: []
   ok   truth-teller has two fixed points (underdetermined), Liar none (overdetermined)
   id  (truth-teller)   fixed points on {0,1/2,1}: [0, 0.5, 1]
   NOT (Liar)           fixed points on {0,1/2,1}: [0.5]
   ok   Liar's only Kleene fixed point is 1/2 (ungrounded, no classical value)
B. qubit with record basis Z; Liar operator X, hypodox operator 1
   eigenvalues of X: [-1.  1.]; |+> = [0.7071+0.j 0.7071+0.j], |-> = [ 0.7071-0.j -0.7071+0.j]
   Z-probabilities of |+>, |->: [0.5 0.5], [0.5 0.5]
   ok   both Liar fixed rays are the value 1/2 in Z (part A's fixed point)
   Z-copy residual of |+>, |->: 0.765, 1.414 ; X-copy residual: 1.1e-16, 1.1e-16
   ok   Liar fixed rays are not Z-copyable but are X-copyable (records in the complementary structure)
   <+|X|+> = +1, <-|X|-> = -1 : the Liar acts on its own fixed records as a signed truth-teller
   ok   Liar anticommutes with the record (XZ = -ZX); hypodox commutes
   Kirkwood--Dirac of |-> in (Z,X):
      [[ 0.   0.5]
       [-0.   0.5]]
   ok   KD distribution of the Liar's fixed state is non-negative
   Wootters Wigner minimum over conventions, |->: 0.0000 ; |+>: 0.0000
   ok   Liar fixed state has no Wigner negativity in any convention: the -1 is a sign on an amplitude, not a signed probability
C. which self-referential endomaps force negativity: rotation about axis n
   Liar  X            axis x        fixed Bloch vectors [-1.  0.  0.], [ 1.  0. -0.] ; |n|_1 = 1.000 ; min Wigner = -0.0000, +0.0000
   phase hypodox      axis z        fixed Bloch vectors [0. 0. 1.], [ 0.  0. -1.] ; |n|_1 = 1.000 ; min Wigner = +0.0000, +0.0000
   order-3 Clifford   axis (1,1,1)  fixed Bloch vectors [0.577 0.577 0.577], [-0.577 -0.577 -0.577] ; |n|_1 = 1.732 ; min Wigner = -0.1830, -0.1830
   generic            axis random   fixed Bloch vectors [-0.799  0.602  0.002], [ 0.799 -0.602 -0.002] ; |n|_1 = 1.402 ; min Wigner = -0.1005, -0.1005
   ok   Liar and phase-hypodox fixed states are stabiliser states (inside the octahedron)
   ok   order-3 Clifford and generic self-reference fix magic states (outside it, Wigner-negative)
   ok   min_conventions W(fixed state) = (1 - |n|_1)/4 for 200 random axes: negative iff n is off the three record axes
   ok   the axis-(1,1,1) rotation by 2pi/3 cycles the three classical structures X -> Y -> Z -> X: a three-valued Liar
D. Liar cycles and the PR box
   4-cycle, one negation (Liar cycle): 0 global assignments; two negations (hypodox cycle): 2 -> [(0, 0, 0, 1), (1, 1, 1, 0)]
   ok   odd cycle is a paradox (0 sections), even cycle a hypodox (2 sections)
   PR box: a deterministic global assignment satisfies at most 3 of the 4 edges
   ok   no non-negative global section: the PR box satisfies all 4 with probability one
   signed global section (least-norm): residual 3.5e-16, min weight -0.0625, max weight +0.1875, sum 1.0000
   ok   a signed global section exists and is genuinely signed (Abramsky--Brandenburger)
E. no natural diagonal on C^2
   dim of {Delta : Delta U = (U x U) Delta for 8 Haar U}: 0 (smallest singular value 3.09e+00)
   ok   no linear map C^2 -> C^2 x C^2 is natural under U(2): no diagonal, so no diagonal argument, pre-FANOUT
   copy map of Z: naturality residual under the basis swap X: 0.0e+00 ; under a phase gate: 0.686 ; under the scalar -1: 2.828
   ok   the record's copy map is natural for its own permutations only; phases and the scalar -1 break it (the fibre)
F. composition: what the Liar, the hypodox and their square roots generate
   <X, Z, H> mod phases: 8 elements, orders [1, 2, 4]
   ok   Liar + signed truth-teller + their exchange: 8 elements (the rebit's Clifford group), none of order 3
      1 element(s) of order 1 with fixed-state |n|_1 = 1.000000 (Wigner minimum +0.0000)
      3 element(s) of order 2 with fixed-state |n|_1 = 1.000000 (Wigner minimum +0.0000)
      2 element(s) of order 2 with fixed-state |n|_1 = 1.414214 (Wigner minimum -0.1036)
      2 element(s) of order 4 with fixed-state |n|_1 = 1.000000 (Wigner minimum +0.0000)
   ok   Paulis fix stabiliser states; the two Hadamard-type involutions fix H-type magic states (|n|_1 = sqrt2, negative); quarter-turns fix stabiliser states
   Fix(H) = [0.707 0.    0.707], [-0.707  0.    -0.707] : the fixed points of the exchange of record and Liar structures are magic
   quarter-turn HX: real eigenvalues [0.707+0.707j 0.707-0.707j] -> no real fixed ray; complex fixed Bloch vectors [0. 1. 0.], [ 0. -1.  0.]
   ok   the quarter-turn has no fixed ray over R and fixes the y-records over C: the third classical structure
   S sqrtX = sqrtZ sqrtX: projective order 3, fixed-state |n|_1 = 1.7321, 1.7321, min Wigner -0.1830
   ok   half a hypodox composed with half a Liar is the three-cycle; its fixed states are magic (|n|_1 = sqrt3)
   <X, Z, H, S> mod phases: 24 elements, 8 of order 3, min |n|_1 over their fixed states 1.7321
   ok   the full Clifford group: every order-3 element fixes only magic states
======================================================================
LIAR HYPODOX FANOUT: PASS
```
