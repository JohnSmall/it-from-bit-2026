# Continuity of reversible transformations from self-reference

Discussion draft, 18 October 2026. Status labels in this draft are proposals
for John Small's review; they do not amend the manuscript or ledgers.
**STRUCTURAL** identifies established mathematical facts and conditional
arguments; **CANDIDATE** identifies a proposed physical interpretation;
**RHYME** identifies an analogy; **OPEN** identifies a problem with stated
criteria for resolution. Each status label applies to the passage that
follows it, until the next status label or heading.

## The question for discussion

**OPEN.** Can the physical limitations on an observer's complete
self-description explain why any two pure states can be connected by a
continuous family of physically available reversible transformations? The
observer, its memory, the production of its predictions, and its subsequent
use of those predictions must all belong to the physical system being
described. The sought result must precede the Born rule and the Hilbert-space
metric. If self-reference cannot supply it, what additional physical
principle is needed?

**CANDIDATE.** The proposed starting insight is that making a self-record is
itself an intervention in the state being recorded. The unresolved step is
to turn the resulting limitation on records into a positive constraint on
which states and transformations nature must admit. The attempts below have
not supplied that step. Some contain false implications; others remain
useful conditional arguments with an unproved physical premise.

## What must be derived, and in what order

**STRUCTURAL.** The target is Hardy's fifth axiom, from *Quantum Theory From
Five Reasonable Axioms* (2001): continuous reversible accessibility between
any two pure states. It is stronger than the continuity of each individual
transformation as a mathematical map. Write $P$ for the physically
admissible pure states and $G$ for the allowed reversible transformations.
The target is

$$
\forall x,y\in P\quad \exists\ g:[0,1]\longrightarrow G
\quad\text{continuous},\qquad g(0)=e,\quad g(1)x=y.
$$

Here the path parameter labels transformations; it need not already be a
physical time coordinate. The requirement concerns availability of the
whole path, including its intermediate transformations. Continuity is the
target; differentiability is not an initial premise.
[Hardy, axiom 5](https://arxiv.org/pdf/quant-ph/0101012).

**CANDIDATE.** For this investigation, the framework's earlier argument for
complex amplitudes is taken as a conditional starting point. Its status is
not upgraded here. The intended dependency is

$$
\text{self-reference and complex amplitudes}
\ \longrightarrow\ \text{continuous reversible accessibility}
\ \longrightarrow\ L^2
\ \longrightarrow\ (S^1\to S^3\to S^2)
\ \longrightarrow\ \text{Born probabilities}.
$$

The downstream arrows retain their own premises. In particular, selecting
an $L^2$ norm requires assumptions about the representation of states and
the transformations preserving it; continuity alone is not asserted to
derive the whole chain. The [manuscript's metric section](../../paper1/L2_metric_global_phase_section_2026_06_07.tex)
places continuity upstream of its norm and Hopf constructions. Neither the
Born rule nor an already normalised Hilbert sphere can therefore justify
continuity at this step.

**STRUCTURAL.** A topology can be specified without a Born rule. In a
finite-dimensional operational description, a state is determined by a
finite list of probabilities for specified measurement outcomes. Convergence
means convergence of those probabilities. Pure states are the extreme
points of the admitted convex preparation set, not automatically all rays
of a vector space. This supplies a language in which to ask about
connectedness; it does not assume that the pure states are connected.
[Hardy, sections 1 and 6](https://arxiv.org/pdf/quant-ph/0101012).

## The physical starting point needs careful scope

**STRUCTURAL.** If an observer writes a new record into its memory, its
total physical state changes. Schematically,
$s\xrightarrow{\mathrm{write}\ r}s_r$.
It does not follow that the record is false: it can correctly describe a
past state, a partial property, or even a predictable consequence of the
writing. The stronger obstruction concerns a universally successful
predictor whose predictions can themselves enter the behaviour predicted.
Popper explicitly includes calculation and the physical production of
predictions in his analysis, and establishes limitations in a classical
setting. Thus the obstruction alone cannot distinguish quantum theory from
classical theories.
[Popper, *Indeterminism in Quantum Physics and in Classical Physics*, Part I,
pp. 118–119](https://cqi.inf.usi.ch/qic/popper-indet.pdf).

**CANDIDATE.** FANOUT denotes the formation of an accessible, copyable
outcome record. The proposed pre-FANOUT regime lacks a committed outcome
record for the interaction in question. Turning this into a statement that
no preferred basis or invariant distinction exists is additional work. In
particular, the impossibility of a complete self-record must not be replaced
by the stronger assertion that no record of any property can exist.
This is the issue behind the manuscript's [five proposed descriptions of
the pre-measurement regime](../../paper1/continuity_section_2026-07-04.tex).

**RHYME.** The liar and truth-teller suggest a distinction between
inconsistent Boolean self-assignment and consistent but underdetermined
self-assignment. This motivates the comparison of pre-FANOUT paradox with
post-FANOUT hypodox. It does not specify a topology, a transformation law,
or the probability of the record selected. The comparison with information
in a closed timelike loop has the same limited role.
[Earlier paradox discussion](liar_hypodox_fanout_2026-10-16T1100.md),
[CTC discussion](hypodox_ctc_fanout_2026-10-16T0900.md).

**STRUCTURAL.** Failure to predict an outcome from information available
to the observer does not establish that the outcome has no physical
antecedents. That inference would confuse a limitation on prediction with
a claim about causation; it supplies no continuity argument.

## Attempts and the reasons they are insufficient

### 1. Complex amplitudes provide a continuum

**STRUCTURAL.** A continuous scalar field permits continuous families of
vectors and matrices, but does not make all those vectors preparable or all
those matrices physically available. The complex stabiliser fragment is a
direct test: its single-qubit pure states are the six rays represented by
$(1,0),(0,1),(1,\pm1),(1,\pm i)$, and its Clifford transformations have
24 distinct actions on rays. It uses complex amplitudes and reversible
linear maps, but supplies no continuous path between distinct pure states.
[Backens, sections 2.1 and 5](https://arxiv.org/pdf/1307.7025).

**STRUCTURAL.** Spekkens's toy bit was an earlier warning about finite
state sets, but is not itself a complex-amplitude model. The stabiliser
example addresses that objection. Both are tests of particular proposed
implications; neither has thereby been checked against a fully specified
model of the self-describing observer.
[Spekkens, sections III.A and III.C](https://arxiv.org/pdf/quant-ph/0401052),
[connected-state-space discussion](continuity_connected_state_space_2026-09-15T1430.md).

### 2. Probability normalisation forces unitarity, hence continuity

**STRUCTURAL.** For an exhaustive measurement, normalisation says
$\sum_i p(i\mid s,M)=1$. These are real outcome probabilities. Identifying
them with $|a_i|^2$ already supplies the quadratic rule that this
programme intends to obtain later. The [probability-conservation attempt](continuity_probability_conservation_2026-10-10T1000.md),
section 2, explicitly makes that identification as its third premise. Its
calculation is conditional on that premise and cannot establish the earlier
continuity step.

**STRUCTURAL.** Even granting a quadratic norm and complex-linear dynamics,
norm preservation gives $U^\dagger U=I$, not the physical availability of
every element of $U(n)$. A finite subgroup still preserves the norm.
Moreover, a linear map being continuous is distinct from a continuous path
of allowed maps connecting it to the identity. Both gaps remain after the
normalisation calculation.

### 3. No record means no preferred basis, so bases connect smoothly

**STRUCTURAL.** This compresses three unproved implications. Absence of a
particular record does not exclude a restriction in the laws. Symmetry
between admitted bases does not imply that every mathematical basis is
admitted. Transitivity between admitted states does not imply continuous
transitivity: a finite group can move any member of a finite set to any
other. A passive change of coordinates is also distinct from a physical
operation. The stabiliser example treats its three Pauli bases symmetrically
while restricting the family of bases. The [continuity section](../../paper1/continuity_section_2026-07-04.tex)
already distinguishes its proposition that continuity forbids a privileged
finite basis from the unproved converse.

**STRUCTURAL.** An invariant mathematical partition is not automatically a
readable classical record. To use that claim, one must construct an allowed
measurement that distinguishes its parts and an allowed procedure that
copies the result. Merely naming the parts does not supply either operation.

### 4. No thermodynamic cost means reversible evolution

**STRUCTURAL.** Logical invertibility, absence of heat dissipation, and
thermodynamic reversibility are different conditions. Landauer reasoning
tracks information transferred to other degrees of freedom; it does not
derive microscopic reversible laws from zero heat. Copying classical data
into a blank register can itself be implemented reversibly. Consequently,
a cost assigned to FANOUT cannot by itself prove that all pre-FANOUT
operations possess physically available inverses, still less that these
inverses belong to continuous paths.
[Bennett, discussion of Landauer's principle and copying](https://arxiv.org/pdf/physics/0210005).

### 5. Excluding superpositions would cause nonlinear dynamics and signalling

**STRUCTURAL.** The first implication is false. The linear reversible
matrix $S=\operatorname{diag}(1,i)$ preserves the six stabiliser rays;
restricting the state set does not make this matrix nonlinear. A restriction
to standard quantum preparations, operations and measurements also cannot
create a signalling protocol unavailable in the full theory. This is a
counterexample to the implication, using known quantum theory, not an input
to the proposed reconstruction.
[Backens, section 2.1](https://arxiv.org/pdf/1307.7025).

**STRUCTURAL.** The theorem of Simon, Bužek and Gisin derives linear,
completely positive density-matrix dynamics using Hilbert-space states,
the usual trace probability rule, and no signalling. It cannot be moved
upstream of the metric and Born rule without replacing those premises.
An operational no-signalling condition could be imposed independently, but
by itself does not eliminate the restricted subtheory above.
[Simon, Bužek and Gisin, assumptions and argument](https://arxiv.org/pdf/quant-ph/0102125).

### 6. Diagonalisation or inexhaustible self-ignorance supplies continuity

**STRUCTURAL.** Diagonalisation establishes a failure of exhaustive
representation under specified assumptions. Cardinality and computability
do not determine connectedness. For example, the space of infinite binary
sequences is uncountable but totally disconnected: any two distinct
sequences differ at a coordinate whose two values separate them into disjoint
open-and-closed sets. Even an uncountable set of possibilities therefore
need not contain a nonconstant continuous path. Likewise, density in a
larger mathematical space does not establish that the missing limits are
physically admitted. The [September review](continuity_connected_state_space_2026-09-15T1430.md)
already separated diagonalisation from the physical assumption of
limit-realisability.

**STRUCTURAL.** A continuum of outcome probabilities is also insufficient.
A classical bit admits every probability $p\in[0,1]$ through mixtures
while retaining just two pure states. Thus the move from unrestricted
credences to a connected pure-state space needs its own argument.

**STRUCTURAL.** Analytic continuation of a logarithm also requires a
specified domain and regularity; it does not prove that physical amplitudes
occupy that domain. The [September review](continuity_connected_state_space_2026-09-15T1430.md)
records that the Shannon/logarithm route consumes a value-continuum premise.
Accepting the complex-amplitude construction conditionally does not turn
that earlier use of a continuum into a derivation of connected pure states.

### 7. Different observers' pure and mixed descriptions imply a larger pure space

**STRUCTURAL.** The Bell example must distinguish conditioning from taking
a subsystem. After Alice measures her half of
$(|00\rangle+|11\rangle)/\sqrt2$ in the computational basis and learns
the result, she assigns Bob the corresponding conditional pure state.
Bob, without the result, assigns his qubit $I/2$. A pure description of
the combined system does not make Bob's local state pure. These standard
quantum facts clarify the example; they cannot supply pre-Born premises.
[The manuscript's friend/Wigner comparison](../../paper1/wigners_friend_in_the_hopf_picture_2026-06-13.tex).

**STRUCTURAL.** Hilbert-space purification says that every mixed state is
the marginal of a pure state of a larger system. Its usual construction
already uses the Hilbert structure. Operational purification can instead
be postulated before that structure, as in Chiribella, D'Ariano and
Perinotti's programme; their quantum reconstruction also uses other
informational axioms. Purification has not here been derived from the
physical impossibility of complete self-description.
[Purification principle](https://arxiv.org/abs/0908.1583),
[reconstruction and its stated axioms](https://arxiv.org/abs/1011.6451).

### 8. No distinguished step implies arbitrary subdivision of transformations

**STRUCTURAL.** Under the finite-dimensional compact-group assumptions in
the appendix, divisibility of $G$, meaning that every element has an
$n$-th root for every positive integer $n$, implies connectedness.
The gap is physical: absence of a distinguished step does not establish
the availability of all those roots. Moreover, a formal root of a matrix
need not be an allowed operation. The [September revision](continuity_connected_state_space_2026-09-15T1430.md)
retired this as the necessary route, retaining the conditional theorem.

### 9. A connected state space and enough symmetry give continuous reversibility

**STRUCTURAL.** This conditional route works: for a closed group of
reversible affine transformations of a finite-dimensional compact convex
state body, transitivity on a connected pure-state space implies that the
identity component already acts transitively. The appendix gives the
argument. What remains is the physical derivation of connectedness, with
transitivity and closedness also declared rather than silently inferred.
[Manuscript proposition `prop:connected-transitive`](../../paper1/continuity_section_2026-07-04.tex).

**STRUCTURAL.** Assuming all complex directions are physical would supply
the missing connected space, even before choosing an $L^2$ norm: the unit
sphere of any norm on $\mathbb C^n$ is connected, by radial rescaling of
an ordinary sphere. But a complex representation does not establish this
admissibility assumption. Nor does closure under limits establish
connectedness; finite state sets and finite transformation groups are
already closed. These observations identify the missing premise rather
than derive it.

### 10. Self-consistency forces pure fixed points of every transformation

**STRUCTURAL.** The [fixed-point attempt](value_continuum_fixed_point_route_2026-10-10T1500.md)
introduces

$$
\tag{F}
\forall g\in G\quad\exists x\in P:\ gx=x.
$$

With compact Lie structure, transitivity and at least two pure states,
this forces a connected, positive-dimensional pure-state space; the
appendix supplies the proof. It is a useful reduction of the target.

**OPEN.** The missing derivation is from physical self-reference to **pure**
fixed points. A classical bit-flip already has a consistent mixed state,
the equal mixture, without a pure fixed point. Lawvere's theorem requires
a suitable representation/evaluation structure and a surjectivity
hypothesis; identifying the situation as self-referential does not verify
those hypotheses or locate the resulting fixed point in the pure states.
The route passes only if these physical and mathematical requirements are
established without admitting the full Hilbert space in advance. It fails
if consistency supplies only mixed states or if the representation
hypothesis is assumed rather than justified.
[Yanofsky's exposition of the diagonal and fixed-point theorems](https://arxiv.org/html/math/0305282).

## What the missing physical insight could concern

**CANDIDATE.** The common gap is a relation between two different things:
the information an embedded observer cannot record, and the alternative
physical processes the theory must allow. An obstruction to a universally
correct record says what cannot be completed. Continuous reversibility
asserts the existence of an entire family of processes. A physical
principle must explain that existence.

**CANDIDATE.** A promising place to seek it is the complete act of
self-description: the target, the memory that describes it, the physical
encoding of the description, and the feedback that uses it. Adding the
memory changes the target; redescribing the enlarged target introduces
another physical act. The significant issue may be what information remains
in relations among these parts when a complete internal record is
unavailable. This suggests investigating a constraint on information,
disturbance and recoverable correlations. It does not yet establish that
those correlations are phases, that they form a continuum, or that their
transformations are reversible.

**CANDIDATE.** One possible intermediate result would link an obstruction
to continuous reversible access with an internally available, repeatably
readable distinction. If such a link followed from the complete observer
model, the absence of the relevant record could constrain the allowed
decomposition of pure states. The link cannot be assumed: attempt 3 above
explains why a partition alone supplies no measurement. The stabiliser and
toy models are useful tests of any proposed link.

**CANDIDATE.** A second direction is to ask whether the same physical
analysis forces an operational purification or reversible-dilation
principle. That would connect record limitations to positive statements
about larger systems. It would still require an audit of the remaining
reconstruction assumptions. The substantive missing insight would be the
reason that self-reference enforces such a principle, not its reformulation
in Hilbert-space notation.

## Proposed OPEN problem

**OPEN — Physical self-description and continuous reversible accessibility.**
This is a proposed sharpening of the manuscript's `op:limit-realisability`,
not a claim that it has been solved.

**Setting.** Work with finite-dimensional operational state spaces. Declare
the assumptions that preparations form a compact convex set $\Omega$,
that a finite collection of measurement probabilities separates states,
and that deterministic reversible operations act affinely. Set
$P=\operatorname{ext}(\Omega)$. Take complex amplitudes only with the
algebraic and compositional properties actually obtained from the earlier
self-reference argument; do not add full superposition admissibility.

**First task: specify the physical premise.** Give an operational condition
$\mathcal R$ expressing the limitation on self-description. Include
observer, memory, production of records, and feedback in the same theory.
Specify which prediction tasks admit a diagonal response and which partial
or retrospective records remain possible. Distinguish closure of the
*physical model* under adding observers from possession by an observer of
an exhaustive *internal representation*. The former must not silently be
treated as the latter. Where increasing memory is needed, use a family of
finite systems rather than a finite register with unlimited capacity.

**Narrow mathematical task.** Initially grant that the allowed reversible
group $G$ is closed and transitive on $P$, explicitly as additional
premises. Determine whether $\mathcal R$, together with the declared
complex-amplitude structure, forces $P$ to be connected, or equivalently
under these assumptions forces $G_0$ to act transitively. A derivation of
(F) would be one sufficient route, but is not required.

**Full physical task.** Explain whether closedness, transitivity and the
availability of inverses also follow from the observer analysis. If any
remain independent postulates, identify them. A solution to the narrow
task must not be described as deriving continuous reversibility from
self-reference alone.

**PASS, affirmative resolution.** State $\mathcal R$ in independently
meaningful operational terms and prove the target for every model of the
declared premises. Establish the available paths or the sufficient
connectedness result, and identify the precise premise violated by the
finite counterexamples. Merely constructing one connected model does not
establish necessity.

**PASS, negative resolution.** Construct a model satisfying the same
explicit premises, including the physical observer and its prediction and
record procedures, whose pure states fail the target. For the narrow task,
the countermodel must retain closedness and transitivity. It must satisfy
the substantive complex-amplitude requirements, not just encode classical
labels with complex coordinates. Such a model would establish that a
further physical principle is necessary.

**FAIL as a derivation.** Import the Born rule, an $L^2$ sphere, all
projective rays, all unitary transformations, continuous control, or
arbitrary physical roots as an unstated premise; infer pure-state
connectedness merely from continuously variable probabilities; or claim
that a toy model violates $\mathcal R$ without defining and testing it.
A premise that simply rephrases connectedness also fails the explanatory
aim even if the subsequent mathematics is correct.

## Questions to put to advisers

**OPEN.** Which operational formulation of an embedded observer's
self-description captures the physical effect of producing and using its
own records, while allowing ordinary partial knowledge? Can it distinguish
the proposed pre-FANOUT regime from a discrete theory that has diagonal
limits on prediction?

**OPEN.** Is there a theorem connecting that formulation to connected pure
states, pure fixed-point consistency, or operational purification? If so,
which independent assumptions carry the topological content?

**OPEN.** If a countermodel exists, what is the weakest additional physical
condition that excludes it? A precise independence result would be as useful
here as an affirmative derivation.

## Mathematical appendix: what the conditional arguments establish

**STRUCTURAL — Common hypotheses.** Let $\Omega$ be a compact convex set
spanning a finite-dimensional affine space, and let $G$ be a closed
subgroup of its affine automorphisms. Its automorphism group is compact:
the centroid provides a common fixed point, and inscribed and circumscribed
balls bound the matrices and their inverses. Thus $G$ is a compact matrix
Lie group. Its identity component $G_0$ is path-connected and has finite
index. These are the hypotheses used below; arbitrary compact groups are
not being assumed to be Lie groups. Euclidean coordinates used to bound
matrices here are auxiliary; they do not identify physical normalisation
or probabilities with a quadratic norm.
[The manuscript's two group propositions](../../paper1/continuity_section_2026-07-04.tex).

**STRUCTURAL — Connected pure states.** Suppose $G$ acts transitively
on $P$. The $G_0$-orbits partition $P$ into finitely many sets,
since $G/G_0$ is finite. Each orbit is compact and hence closed, so each
is also open relative to this finite partition. If $P$ is connected,
there is one orbit. Path-connectedness of $G_0$ then gives the target
path for each pair of pure states. The whole group $G$ need not be
connected. This is the proof of `prop:connected-transitive`.

**STRUCTURAL — Divisibility.** If $G$ is divisible, then its finite
quotient $G/G_0$ is divisible. A finite group of order $m$ has
$h^m=e$ for every element, so it cannot have an $m$-th root of any
nonidentity element. The quotient must be trivial. Hence $G$ is
connected, and transitivity supplies the target. This proves the conditional
claim; it does not derive divisibility from a physical absence of records.

**STRUCTURAL — Pure fixed points.** Add transitivity, $|P|\ge2$, and
(F). The finite group induced on the $G_0$-orbits acts transitively.
If there were more than one orbit, that permutation group would contain
an element moving every orbit: by the orbit-counting lemma, its average
number of fixed points is one, while its identity fixes more than one.
Any lift to $G$ would then fix no point of $P$, contradicting (F).
Therefore $P$ is one $G_0$-orbit and is connected. As a nontrivial
homogeneous space of a compact Lie group it has positive dimension.
This is the conditional fixed-point argument of the
[10 October note](value_continuum_fixed_point_route_2026-10-10T1500.md).

**STRUCTURAL — What mixed fixed points do not establish.** Averaging any
state over a compact group gives an invariant state of $\Omega$, which
may be mixed. Thus consistency in the convex state space is much weaker
than (F). A physical reason to insist on an admissible pure fixed point
is precisely what the fixed-point route still owes.

## Repository provenance

This discussion consolidates the conversation of 18 October with the
following working sources. Earlier assertions are recorded here as attempts,
not silently adopted as premises.

| Source | Contribution to the present question |
| --- | --- |
| [Continuity section](../../paper1/continuity_section_2026-07-04.tex) | Conditional group arguments and the existing `op:limit-realisability`. |
| [Connected-state-space revision, 15 September](continuity_connected_state_space_2026-09-15T1430.md) | Retirement of the necessity of divisibility; limits of diagonal and value-continuum arguments. |
| [Probability-conservation attempt, 10 October](continuity_probability_conservation_2026-10-10T1000.md) | Normalisation route and its absolute-square premise. |
| [Fixed-point attempt, 10 October](value_continuum_fixed_point_route_2026-10-10T1500.md) | Condition (F), its group-theoretic consequence and the missing physical premise. |
| [Paradox/hypodox discussion, 16 October](liar_hypodox_fanout_2026-10-16T1100.md) | Fixed-point motivation and record formation. |
| [Quantum-state section](../../paper1/what_is_a_quantum_state.tex) | Popper's observer and the proposed complex-amplitude starting point. |
| [Metric section](../../paper1/L2_metric_global_phase_section_2026_06_07.tex) | Intended order of continuity, norm, Hopf geometry and Born probabilities. |
