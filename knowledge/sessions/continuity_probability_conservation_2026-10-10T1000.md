# Review of the continuity section: where conservation of probability comes from (2026-10-10)

Session 2026-10-10, Fable 5.1. JS: "Review the continuity section and
consider the requirement that measured probability must sum to 1 and
therefore probability must be conserved." The whole of
`paper1/continuity_section_2026-07-04.tex` read, with the passages it leans
on: `sec:reversible-continuity-l2` (the L^2 section), Postulates 3 and 5
(`derivation_of_the_quantum_postulates.tex`), `sec:born-cost-ledger`
(`what_is_a_quantum_state.tex`), and the Born-rule paragraph of
`sec:self-reference`. Script
`scripts/probability_conservation_vs_renormalisation_2026-10-10T1000.py`
(standard quantum mechanics, seed 20261010, PASS), stdout in section 7.

## 0. The answer in brief

JS's requirement is right, and the paper already uses it as the cut from
$GL(n,\mathbb{C})$ to $U(n)$ in three places, but it never says where the
requirement comes from, and the continuity section attributes the cut to
the wrong thing. The section says "the cut from $GL(n,\mathbb{C})$ down to
the unitary group is the conserved quadratic form, and continuity is what
entitles the theory to make it". Continuity cannot make that cut:
$GL(n,\mathbb{C})$ is itself connected, and a continuous reversible path
between any two pure states exists inside it. What makes the cut is
conservation of probability, as JS says, and the paper's own ingredients
supply it from the record side: a FANOUT writes exactly one outcome, it
could occur at any operation count, and the outcome weights are the
closed-loop squares $|\psi_{i}|^{2}$ of the cost-ledger derivation, not
ratios of them; so the dynamics must carry the unit sphere to itself at
every step, and a linear map that preserves a sphere is an isometry of its
norm, which for the quadratic norm means unitary. Continuity's job is then
what the section's own propositions already make it: that the isometry
group be connected and transitive, so that superpositions are reached (and
through Lamperti, that the conserved norm be the quadratic one if one
starts from the $p$-norms). Two consequences. The continuity section's "why
the cut matters" paragraph needs one correction (patch drafted, unrun).
And the paper gains a third route to the $L^{2}$ metric, from
conservation rather than from continuity or from Čencov, which closes a
small circularity the present text has: every current route reads
normalisation off the $L^{2}$ sphere that continuity delivered, so
"probability sums to one" is at present a consequence of the metric
rather than a premise about records. The conservation route makes it a
premise about records, which is where the framework wants it.

## 1. What the three passages currently say

- *The L^2 section* (`sec:reversible-continuity-l2`): "Operationally a
  reversible transformation of states is a symmetry of the state manifold,
  hence norm-preserving; the demand is that such symmetries form a
  connected group acting transitively." Then Lamperti: for $p\neq2$ the
  isometries are generalised permutations, so only $p=2$ admits a connected
  transitive isometry group. Closing: "Bare reversibility on the amplitude
  space buys only $GL(n,\mathbb{C})$; what carves the unitary group out of
  it is preservation of the quadratic form, and reversibility of the
  resulting maps is then a corollary." Norm preservation is assumed here,
  in the clause "a symmetry of the state manifold, hence norm-preserving",
  which is circular as stated: the state manifold is defined as the unit
  sphere of the norm, so its symmetries preserve the norm by definition,
  and the question is why the dynamics must be a symmetry of the state
  manifold at all. That is JS's question.
- *Postulate 5*: "Conservation of probability is preservation of the $L^{2}$
  inner product, and the inner-product-preserving linear maps are the
  unitaries... Reversibility is here a corollary, not a premise." Right,
  and consistent with the L^2 section; conservation is again taken as
  given.
- *The continuity section*, "Why the cut matters physically": "The cut from
  $GL(n,\mathbb{C})$ down to the unitary group is the conserved quadratic
  form, and continuity is what entitles the theory to make it: with the
  fifth axiom in hand, Hardy's theorem delivers the complex Hilbert space,
  the quadratic norm and the unitary group in one stroke." The first
  clause is right, the second is not: continuity does not entitle the
  cut. What is true is that Hardy's theorem, with all five axioms,
  delivers the unitary group; but Hardy's first four axioms contain the
  probability structure (states as normalised probability lists,
  transformations that do not increase total probability), so in that
  route conservation is imported from Hardy, not derived. The paragraph
  conflates "continuity selects the quadratic norm among norms" (Lamperti,
  true) with "continuity cuts $GL$ to $U$" (false).

And one more place, which shows the circularity: `sec:born-cost-ledger`
derives the square $\psi\psi^{*}$ as the closed loop and then says "with
the normalisation of \S\ref{sec:l2-metric-fibre} it is a probability". So
even the cost route borrows $\sum|\psi_{i}|^{2}=1$ from the L^2 section,
where it came from continuity. Nowhere does the paper derive
normalisation from the record side.

## 2. The conservation route [CANDIDATE; the pieces are the paper's own]

Four of the paper's ingredients, in order:

1. *Exactly one outcome.* A FANOUT writes one record from an exhaustive,
   exclusive set of outcomes (`sec:fanout-boundary`); so at any FANOUT,
   $\sum_{i}p_{i}=1$. This is what "measured probability must sum to 1"
   means in the framework: it is the statement that a record is one
   outcome, a real-column fact.
2. *At any time.* A FANOUT could occur at any operation count; the observer
   is the standing counterfactual possibility of one (observer note,
   2026-10-08, section 5). So the state must be normalised at every
   operation count, not only when a measurement happens.
3. *The weights are absolute squares.* The cost-ledger route gives
   $p_{i}=\psi_{i}\psi_{i}^{*}$, a polynomial in the amplitudes, the closed
   loop of the history and its return leg. It is not the ratio
   $|\psi_{i}|^{2}/\sum_{j}|\psi_{j}|^{2}$: a ratio is not a polynomial, and
   the analyticity declared at `sec:complex-amplitudes`, the same clause
   that excludes $|\psi|$, excludes it. (This is where Aaronson's
   renormalised theory is cut off: it is normalised at every measurement
   by construction and is not norm-preserving, and it signals; script part
   A shows a renormalised invertible map on one qubit of an entangled pair
   changing the other qubit's reduced state by order one, while a unitary
   never does.)
4. *Linearity.* The dynamics is linear on the amplitudes, inherited from
   the additive continued measure (`sec:self-reference`; the L^2 section
   says the same).

Then: a linear map that carries the unit sphere $\sum_{i}|\psi_{i}|^{2}=1$
to itself preserves the quadratic norm on all vectors (homogeneity), so it
is an isometry of $\ell^{2}$, and the linear isometries of $\ell^{2}$ are the
unitaries (script part B: no random invertible map keeps the norm on six
random states, every unitary does, and a non-unitary perturbation of
relative size $10^{-3}$ changes the norm of a random state by $2\times10^{-3}$).
Conservation of probability is unitarity, derived from records and the
closed-loop Born rule, with no appeal to continuity. And since the
conserved norm is the quadratic one by step 3, the $L^{2}$ metric follows
too: a third route to the metric, from conservation, after the
Lamperti and Čencov routes.

The same statement in the paper's anti-event language, which may be the
cleaner one for the text: "every event is undoable" (the second face of
the regime) with the undoing done by the event's anti-event, the time
reverse, which for a process is $U^{\dagger}$ (reverse the order, conjugate
the amplitudes, the dagger of the categorical calculus the paper already
uses). Undoable by the anti-event is $U^{\dagger}U=1$, which is unitarity;
undoable by *some* map is only invertibility, $GL(n,\mathbb{C})$. Script
part D: for a random invertible map the inverse exists but the time
reverse does not undo it, $|G^{\dagger}G-1|\approx23$, and the closed loop
$\langle\psi|\psi\rangle$ is not conserved. So the Born rule and unitarity
are one closed-loop statement at two levels: for a state, the loop out
along the history and back along the return leg has weight
$\psi\psi^{*}$; for a process, the loop out along $U$ and back along
$U^{\dagger}$ is the identity. The second is conservation of the first.
This needs the identification of the anti-event of a process with its
dagger, which the paper's anti-event identity states for events and
weights and not yet for processes: a one-sentence extension, CANDIDATE.

## 3. What continuity is then for

Exactly what the section's propositions prove: that the group of
transformations be connected and act transitively on the pure states
(`prop:connected-transitive`), so that a basis state is carried to a
superposition by a continuous path. Conservation alone would be satisfied
by any subgroup of $U(n)$, including the Clifford group of the stabiliser
fragment the section uses as its foil, which conserves probability and
has finitely many pure states. Continuity rules that out. And if one
starts, as the L^2 section does, from the family of $p$-norms without the
Born rule, continuity also selects $p=2$ by Lamperti (script part C: a
random unitary changes the $p$-norm of a random vector by order $10^{-1}$
for $p=1,3,4$ and by $10^{-16}$ for $p=2$). So the honest division of
labour is: conservation cuts $GL$ to the isometries of the norm the
probabilities are read from; the closed-loop Born rule says that norm is
quadratic; continuity says the isometry group is all of $U(n)$ and not a
discrete subgroup. The section's title, "Continuity is not an axiom",
survives untouched; what changes is one paragraph's claim about what
continuity does.

## 4. Fences

- Step 2 (normalised at every operation count) rests on the counterfactual
  reading of the observer, which is CANDIDATE (2026-10-08). Without it one
  has normalisation at actual FANOUTs only, and a dynamics that leaves the
  sphere between them and returns to it is not excluded by step 1 alone.
  Linearity plus "at every actual FANOUT" with FANOUTs dense enough closes
  the gap in practice; the clean statement needs step 2.
- Step 4 (linearity) is inherited, not derived here; it is the same
  inheritance the L^2 section declares.
- The dagger extension of the anti-event identity is a reading; the paper
  should state it as one.
- Nothing here changes the open problem `op:limit-realisability` (the
  value continuum), which is about connectedness of the state space, not
  about conservation.

## 5. Proposed wording

Patch drafted, unrun, anchor-checked, JS to rule:
`scripts/patch_continuity_cut_conservation_2026-10-10T1100.py`, one edit in
`paper1/continuity_section_2026-07-04.tex` replacing the two sentences "The
cut from $GL(n,\mathbb{C})$ down to the unitary group is the conserved
quadratic form, and continuity is what entitles the theory to make it:
with the fifth axiom in hand, Hardy's theorem delivers ... cited here, not
re-proved" with a statement of the division of labour: conservation makes
the cut, from exactly-one-outcome at any operation count and the
closed-loop squares (backward reference to `sec:born-cost-ledger`, which
precedes this section in `main.tex`), with the renormalised alternative
excluded by analyticity and named as Aaronson's signalling theory;
continuity selects the norm and makes the isometry group connected
(forward reference to `sec:reversible-continuity-l2`); Hardy's theorem
cited as before.

Two further wording items, not patched: in the L^2 section, replace "a
symmetry of the state manifold, hence norm-preserving" with the premise
stated (the dynamics must carry normalised states to normalised states
because a record is one outcome and could be written at any step); in
Postulate 5, after "Conservation of probability is preservation of the
$L^{2}$ inner product", one clause giving its origin, exactly one outcome
per FANOUT at any operation count, and one clause for the anti-event
form, $U^{\dagger}U=1$ as the closed loop of a process. And in
`sec:born-cost-ledger`, "with the normalisation of \S\ref{sec:l2-metric-fibre}
it is a probability" could become "with the normalisation that a record is
one outcome, it is a probability", removing the borrowed step.

## 6. Proposed ledger entries

- **CANDIDATE** Conservation of probability is derived from the record
  side: a FANOUT writes exactly one outcome, could occur at any operation
  count, and its weights are the closed-loop squares, so the dynamics
  preserves the unit sphere and, being linear, is unitary. Equivalently,
  every process is undone by its anti-event, $U^{\dagger}U=1$. This cuts
  $GL(n,\mathbb{C})$ to $U(n)$ without continuity and is a third route to
  the $L^{2}$ metric.
- *Precision owed:* the continuity section's "continuity is what entitles
  the theory to make [the cut]" is wrong as stated, since
  $GL(n,\mathbb{C})$ is connected; continuity selects the norm and the
  connectedness of the isometry group. Patch drafted.
- **STRUCTURAL** (textbook, script): the renormalised invertible dynamics
  is normalised at every measurement, not norm-preserving, and signals;
  linear sphere-preserving maps are isometries; the $p$-norm isometries
  for $p\neq2$ are generalised permutations.

## 7. Exact stdout of `scripts/probability_conservation_vs_renormalisation_2026-10-10T1000.py`

```
Probability conservation versus renormalisation, seed 20261010
====================================================================================
A. renormalised invertible map on qubit 2 changes qubit 1's reduced state: max 1.137 (signalling)
   unitary map on qubit 2 changes qubit 1's reduced state:                 max 9.0e-16 (no signalling)
B. linear maps that keep sum|psi_i|^2 = 1 on normalised states are unitary
   random GL(3,C) maps keeping the norm on six random states: 0 of 2000 (generic maps do not)
   random U(3) maps: all keep it (max |norm-1| 4.4e-16), and |U^dagger U - 1| max 1.2e-15
   a non-unitary perturbation of size 1e-03 of a unitary changes the norm of a random state by 2.2e-03: not conserved
C. isometries of the p-norm: a random rotation (p=2 isometry) changes |v|_p for p != 2
   p = 1: max change of the p-norm under a random unitary: 2.7e-01
   p = 2: max change of the p-norm under a random unitary: 3.3e-16
   p = 3: max change of the p-norm under a random unitary: 1.4e-01
   p = 4: max change of the p-norm under a random unitary: 1.4e-01
D. undoable by the inverse versus undoable by the time reverse
   unitary:    |U^dagger U - 1| = 7.2e-16   (the time reverse undoes it)
   invertible: |G^-1 G - 1| = 3.2e-15 but |G^dagger G - 1| = 22.86  (the inverse undoes it, the time reverse does not)
   closed loop <psi|psi> after U: 1.000000000000 ; after G: 4.104345
====================================================================================
CONSERVATION: PASS
```


## 8. Does this clear op:limit-realisability? No, and what it does instead (added 2026-10-10T1300)

JS: "Does this clear up the open problem op:limit-realisability?" No. The
open problem asks for the value continuum: that the pure states of the
regime are all of $\mathbb{CP}^{K-1}$, a connected space, derived from
self-referential closure, with the FAIL criterion that a derivation
fails before any detail is checked if every premise it uses also holds in
Spekkens's toy theory or the stabiliser fragment. The conservation route
fails that test at once, by design: its premises are one outcome per
FANOUT, the closed-loop squares, linearity and $U^{\dagger}U=1$, and the
stabiliser fragment satisfies all four while having six pure states and a
transformation group of 24 elements of orders 1 to 4 (script part A). The
route fixes the ambient group $U(n)$ and the norm; it says nothing about
which subgroup of $U(n)$ the regime realises or whether its orbits are
continua. That is exactly the division of labour section 3 drew:
conservation cuts, continuity connects, and the value continuum is
continuity's premise, not conservation's.

What it does instead is tidy the problem's statement. The problem lists
three premises (connected $P$, transitive $G$, closed $G$) for "the group
of reversible transformations"; the conservation route makes that group a
subgroup of $U(n)$ from the record side, so "reversible" in the problem
can read "unitary", with nothing else changed.

And one observation, which sharpens where the gap is without closing it.
By the section's own Baire and compact-Lie arguments, a closed group
containing a single element of infinite projective order has positive
dimension, and its orbits are continua. The foils have no such element:
every Clifford element returns to the identity within four steps. So the
open problem could be restated as "derive that the regime contains one
transformation of infinite projective order", a weaker-looking demand
than "derive that $P=\mathbb{CP}^{K-1}$", though not equivalent to it (a
positive-dimensional orbit need not fill $\mathbb{CP}^{K-1}$; transitivity
must still be argued, as the problem does from the absence of records).
The framework has exactly one witness that such an element exists, and
it is empirical rather than derived: the Koide phase $\delta=2/9$ rad, a
rational number of radians and hence an irrational fraction of a turn,
whose exponential is transcendental by Lindemann--Weierstrass (ledger,
2026-09-11). A rotation by $\delta$ about any axis is never projectively
the identity (script part B: the closest approach in a million steps is
at $n=103993$, a convergent of $\pi$, off the identity by $2\times10^{-11}$
and off an integer multiple of $9\pi$ by $7\times10^{-7}$). So the measured
charged-lepton spectrum is a witness that the regime's group is not
finite, and with closedness that its state space contains a continuum.
That is RHYME-level for the open problem, because the witness lives in
the mass sector and the problem wants a derivation from closure at the
single-qubit rung; but it is a fact worth one sentence in the problem's
text: the foils are not merely consistent toy theories, they are theories
in which no physical phase is an irrational fraction of a turn, and the
framework's own matched number is such a phase.

`op:limit-realisability` stays OPEN. Script
`scripts/value_continuum_infinite_order_2026-10-10T1300.py`, no randomness.

### Exact stdout

```
Value continuum and infinite order
======================================================================
A. one-qubit Clifford group mod phases: 24 elements; element orders [1, 2, 3, 4]; orbit of |0>: 6 states
   every Clifford element conserves probability (max |U^dagger U - 1| = 6.4e-16)
B. rotation by the Koide phase delta = 2/9 rad: closest projective approach in n <= 10^6 is n = 103993, |tr U^n| - 2 = -2.14e-11, n/(9 pi) off an integer by 6.8e-07
   (U^n = 1 projectively iff n/(9 pi) is an integer; never, pi being irrational)
   a closed group containing it is a compact Lie group of positive dimension; its orbit of |0> is a continuum (the z-circle)
======================================================================
INFINITE ORDER: PASS
```
