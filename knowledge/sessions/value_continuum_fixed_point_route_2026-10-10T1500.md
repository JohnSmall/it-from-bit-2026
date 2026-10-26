# The chain from self-reference to reversible continuity: what remains, and a fixed-point route to it (2026-10-10T1500)

Session 2026-10-10, Fable 5.1. JS: "I still don't understand why we haven't
been able to show the full sequence self-reference implies negative
probability, which implies complex probability measure, which when coupled
with conservation of probability implies reversible continuity. What
remains to be proved?" Script
`scripts/fixed_point_route_value_continuum_2026-10-10T1500.py` (seed
20261010, PASS), stdout in section 7. The continuity section, the
self-reference section's Shannon step, `op:limit-realisability`, and this
morning's conservation note were the sources.

## 0. The answer in brief

The chain has one gap, and it is not where the sentence puts it. Every
link is in hand except that the second one, negative probability to the
complex measure, is proved on a premise: the analytic continuation of the
logarithm that turns a signed measure into a complex one is unique only
when the credences being continued range over a connected domain, and the
paper declares that premise at the Shannon step (`sec:complex-amplitudes`)
and consumes it again at the continuity step. That premise is the value
continuum, `op:limit-realisability`, and it is what remains. Conservation
does not supply it: this morning's note showed conservation fixes the
ambient group $U(n)$, and the stabiliser fragment satisfies every premise
of the chain while having six pure states. So the chain as JS states it is
valid, and what remains to be proved is its hidden premise: that
self-referential ignorance is not rationed, that the credences fill a
connected set.

Today's result is a candidate route to exactly that, of Lawvere's shape,
which is the shape the paper already uses for closedness. Replace the
continuum premise by the fixed-point premise: *every admissible
transformation of the regime fixes some admissible pure state*, which is
the conclusion of Lawvere's fixed-point theorem. Then a short theorem,
whose only ingredients are Jordan's theorem on derangements and the
section's own component argument, gives that the pure states form a
connected manifold of positive dimension, and `prop:connected-transitive`
gives Hardy's fifth axiom. The premise passes the open problem's FAIL test
where every earlier candidate failed it: the stabiliser fragment and
Spekkens's toy theory both contain transformations with no fixed state
(fourteen of twenty-four in each), and the states the stabiliser fragment
lacks for the premise are exactly the magic states. Quantum theory
satisfies it because every unitary has an eigenvector. What then remains
to be proved is one thing, narrower than before: that self-referential
closure delivers the fixed-point premise, which is Lawvere's hypothesis,
point-surjectivity of the observer's self-description, applied to the
regime's transformations, together with the principle the paper already
uses for Thomson's lamp, that the self-consistent fixed point of a
transformation is an admissible state.

## 1. The chain, link by link, with today's labels

1. *Self-reference gives a signed measure.* The embedded observer's
   self-ignorance; the anti-event with weight $-p$; `sec:self-reference`.
   The paper's own argument, CANDIDATE as it stands (it is the framework's
   founding move, argued at length, not a theorem).
2. *A signed measure continues to a complex one, and the field is $\mathbb{C}$.*
   Shannon's surprisal $-\ln p$ continued off the positive axis;
   additivity of the information measure pins $\mathbb{C}$ against
   $\mathbb{H}$ and $\mathbb{O}$ (the log of a product is a sum only in a
   commutative field). CANDIDATE, *on the declared premise* that credences
   range over a connected domain, without which the continuation is not
   unique. This is the link that carries the gap.
3. *Complex measure plus conservation gives the unitary group.* One
   outcome per FANOUT at any operation count, the closed-loop squares,
   linearity; a linear map preserving the sphere is an isometry;
   equivalently undoability by the anti-event, $U^{\dagger}U=1$. CANDIDATE,
   this morning (`continuity_probability_conservation_2026-10-10T1000.md`).
4. *Unitary group plus closedness, transitivity and a connected state
   space gives reversible continuity.* `prop:connected-transitive`, proved.
   Closedness is the adopted stance (limit-realisability); transitivity is
   argued from the absence of records; connectedness is open.

So "what remains" is the connectedness of the state space, used at links
2 and 4. It is not supplied by conservation (link 3), because every
premise of links 1 to 3 holds in the stabiliser fragment, whose credences
are $0$, $\tfrac12$ and $1$. The open problem's FAIL criterion is precisely
this observation.

## 2. The fixed-point premise and the theorem [the theorem STRUCTURAL; its use CANDIDATE]

**Premise (F).** Every admissible transformation $g\in G$ of the regime
fixes some admissible pure state: there is $\psi\in P$ with $g\psi=\psi$
projectively.

**Theorem.** Let $G$ be a closed (compact) group of transformations acting
transitively on the pure states $P$ of a finite-dimensional system, with
$|P|\ge2$. If (F) holds, then $P$ is a connected manifold of positive
dimension; with `prop:connected-transitive`, a continuous reversible
transformation connects any two pure states.

*Proof.* (i) $P$ is infinite. If $P$ were finite, $G$ would act through a
finite group transitive on at least two points, and such a group contains
an element without fixed points: by Burnside's lemma the average number of
fixed points over the group equals the number of orbits, which is one,
while the identity alone contributes $|P|\ge2$, so some element contributes
none (Jordan 1872; Serre 2003 for the modern statement). That contradicts
(F). Since $G$ is a compact Lie group acting transitively, $P=G/H$ is then a
compact manifold of positive dimension. (ii) $P$ is connected. The identity
component $G_{0}$ is normal of finite index, and its orbits are the
components of $P$: finitely many, closed, hence open, as in the proof of
`prop:connected-transitive`. The finite group $G/G_{0}$ permutes them
transitively. If there were more than one, Jordan would give a coset
moving every component, and any element of that coset would move every
point of $P$, contradicting (F). So $P$ has one component. $\square$

Two remarks. The credence $|\langle a|\psi\rangle|^{2}$ is continuous on
the connected $P$ and takes the value $1$, so its range is an interval:
self-ignorance is not rationed, which is the open problem's own phrasing.
And the proof is elementary: no Lefschetz theory, no Euler characteristic,
only the two facts the continuity section already uses plus Burnside.

## 3. The premise passes the FAIL test, and what it costs the foils [verified]

Script part A: the one-qubit Clifford group modulo phases (24 elements, the
rotation group of the octahedron) acting on the six stabiliser states has
Burnside average exactly one fixed point, and fourteen elements fix no
stabiliser state: the six Hadamard-type elements of order two and the
eight elements of order three. Every one of them has eigenvectors in
$\mathbb{CP}^{1}$; the fragment simply does not contain them. Classified in
Burton and Anwar's chart (2026-10-03), the eigenvectors of the order-two
derangements are the twelve $H$-states and those of the order-three
derangements are the eight $F$-states: the magic states. So the states the
stabiliser fragment lacks in order to satisfy (F) are exactly the states
that make quantum computation universal.

Part B: adjoining them gives 26 states on which every Clifford element has
at least two fixed points, so (F) is restored; but the Clifford group has
three orbits on them (6, 12, 8), and a proper closed invariant subset is a
superselection label, a record predating any FANOUT, which the framework's
third face excludes (the transitivity premise). So (F) and transitivity
together are what kill finiteness, as the theorem says; neither alone
does.

Part C: Spekkens's toy bit, $S_{4}$ on the six two-element subsets of the
four ontic states, likewise has fourteen derangements, the three-cycles and
the four-cycles. The toy theory violates (F) too.

Part D: in quantum theory (F) holds because every unitary of a
finite-dimensional space has an eigenvector; and it holds on the
projective space $\mathbb{CP}^{1}$, not on the sphere $S^{3}$, where a global
phase acts freely. The fixed-point property lives on the base, where the
records are, and fails along the fibre, which is the self-ignorance. That
is consistent with everything the paper says about the fibre.

## 4. What remains to be proved, stated exactly

(F) is the *conclusion* of Lawvere's fixed-point theorem: in a cartesian
closed category, if a map $\phi\colon A\to Y^{A}$ is point-surjective, then
every endomorphism of $Y$ has a fixed point. The paper already invokes
"a demand of exactly Lawvere's fixed-point shape" for closedness
(`Lawvere_1969`, `Yanofsky2003`, in the library). What remains is to show
that the regime is an instance of the hypothesis:

1. *The objects.* Say what $Y$ is (the value object: the pure states, or
   the credences they induce), what $A$ is (the observer's register of
   descriptions of itself), and what the exponential $Y^{A}$ is in the
   category the regime lives in (the dagger-compact calculus the paper
   uses is cartesian closed on its classical part and not on its quantum
   part, so the setup needs care: the fixed points are of maps on states,
   and the point-surjection is a classical-side object).
2. *Point-surjectivity.* That the embedded observer's self-description
   names every assignment $A\to Y$: this is the inside/outside equivalence
   of `sec:self-reference`, the claim that nothing about the observer is
   outside the observer's own description. It is the framework's founding
   premise, so the burden is to show it is the same premise, not a new
   one.
3. *Admissibility of the fixed point.* Lawvere gives a fixed point in $Y$;
   (F) needs it in $P$, the states the regime admits. This is the principle
   the paper already applies to Thomson's lamp: the self-consistent fixed
   point of the toggle, $P(\mathrm{on})=(1+i)/2$, is admitted as a state
   of the theory. Stated generally: the regime admits the self-consistent
   states of its own transformations. The stabiliser fragment is exactly a
   theory that refuses this (its order-three element's fixed points are
   states it does not admit), and by the contrapositive of Lawvere its
   self-description is not point-surjective: the fragment is not
   self-referentially closed. That is a sharper thing to say about the
   foils than "they are consistent toy theories", and it is the sentence
   the open problem's FAIL criterion was reaching for.

If 1 to 3 go through, the chain JS asked for closes with one premise fewer
than it has today: self-referential closure (as point-surjectivity) gives
(F); (F) with transitivity and closedness gives the connected continuum;
the continuum makes the continuation at link 2 unique and link 4 fire.
The value continuum stops being a declared premise and becomes a theorem
of closure. If they do not, (F) is still a better-posed premise than
"connected", since it is a statement about transformations the observer
can check one at a time.

## 5. Fences

- Finite dimension throughout: in infinite dimension unitaries can lack
  eigenvectors (the shift), and (F) would need restating. The paper's
  propositions are already finite-dimensional.
- Closedness stays the adopted stance and transitivity stays the
  no-records argument; the theorem consumes both.
- The theorem gives a connected positive-dimensional $P$, not
  $P=\mathbb{CP}^{K-1}$: for one qubit the two coincide (the only closed
  transitive subgroups of $PU(2)$ with (F) act on all of $S^{2}$), for
  larger $K$ real quantum theory's $\mathbb{RP}^{K-1}$ also satisfies (F)
  with $SO(K)$; the field is pinned at link 2, not here, which is the
  division of labour the $L^{2}$ section already states.
- "Magic states are what self-referential closure demands" is a reading of
  part A, RHYME until the categorical setup of section 4 is in place.
- Jordan's theorem is 1872 and standard; Serre 2003 is the reference used,
  Crossref-verified 2026-10-10 (Bull. Amer. Math. Soc. 40, 429--440).

## 6. Proposed text

- *op:limit-realisability, restated:* keep the problem as the value
  continuum but add the fixed-point route as its candidate derivation:
  "Equivalently, derive (F): that every admissible transformation of the
  regime fixes an admissible pure state. With transitivity and closedness,
  (F) implies the connected continuum (Jordan's theorem and the component
  argument of Proposition~\ref{prop:connected-transitive}). (F) is the
  conclusion of Lawvere's fixed-point theorem, so a derivation passes if
  it exhibits the regime as an instance of Lawvere's hypothesis, with the
  fixed point admitted as a state as Thomson's lamp already requires; and
  it fails if its premises hold in the stabiliser fragment or the toy
  theory, both of which violate (F) outright: fourteen of the twenty-four
  Clifford operations fix no stabiliser state, their fixed points being
  the magic states." CANDIDATE wording; the problem stays OPEN.
- *Ledger:* **STRUCTURAL** (theorem, elementary) a closed transitive group
  with the fixed-point property on at least two pure states has a
  connected positive-dimensional state space. **ESTABLISHED** (computed)
  the derangement counts and the magic-state identification in the
  Clifford group and the toy bit. **CANDIDATE** the fixed-point route to
  the value continuum.
- No patch; the open problem's text is JS's to change.

## 7. Exact stdout of `scripts/fixed_point_route_value_continuum_2026-10-10T1500.py`

```
Fixed points, derangements and the value continuum, seed 20261010
======================================================================================
A. Clifford mod phases: 24 elements on 6 stabiliser states; Burnside average of fixed points = 1.000 = number of orbits
   derangements (no fixed stabiliser state): 14 elements, of orders [2, 3]
   their fixed points in CP^1 (eigenvectors), classified: {2: ['H'], 3: ['F']}  -> the magic states
   every Clifford element fixes a point of CP^1 (has an eigenvector): True; the fragment just does not contain it
B. closing under fixed points: 26 states (6 stabiliser + 12 H + 8 F); min fixed points per element now 2; Clifford orbits on them: [6, 12, 8]
   fixed-point property restored, transitivity lost: three orbits = a superselection label, a record before FANOUT
C. toy bit: S_4 on the six 2-subsets; fixed-point counts {count: elements} = {0: 14, 2: 9, 6: 1}; derangement cycle types [(3, 1), (4,)]
D. U(2): every sampled unitary fixes a point of CP^1: True; a global phase e^{i 2.76} fixes no point of S^3: |U v - v| = 1.964
======================================================================================
FIXED POINT ROUTE: PASS
```
