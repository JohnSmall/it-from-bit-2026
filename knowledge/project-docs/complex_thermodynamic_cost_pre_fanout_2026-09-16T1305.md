# Deletion before FANOUT has a complex thermodynamic cost

Date: 2026-09-16T1305. Written by the Fable session at JS's request, from an
idea JS recorded in `paper1/conclusions_section.tex` (subsection "Updates")
on the day paper 1 v1 went to Zenodo:

> While doing the final preparations for release I realised there's a
> mistake in the idea that deletion post-FANOUT has a thermodynamic cost
> and pre-FANOUT it doesn't. I think deletion pre-FANOUT has a complex
> thermodynamic cost. I'll be exploring this idea, but it's too late to
> make the cut for this version.

This document records the idea, what the paper currently says against it,
what the corpus already holds that bears on it, what "complex cost" can
mean, what would follow, and what a well-formed open problem for paper 1
v2 would look like. Nothing here is a result. Labels are proposals.

## 1. What paper 1 v1 says, and where

The published version asserts a clean split: erasure is free before FANOUT
and costs $k T \ln 2$ per bit after it. The passages to revise in v2:

- `paper1/what_is_a_quantum_state.tex` 438--441: "Before FANOUT no
  classical records exist and therefore Landauer's Principle doesn't apply,
  information can be erased without thermodynamic cost. An anti-event
  erases information without thermodynamic cost."
- `paper1/what_is_a_quantum_state.tex` 560 (the pointer subsection
  "Reversible continuity", rewritten 2026-09-15): "In the pre-FANOUT regime
  erasing information has no thermodynamic cost, everything is reversible".
- `paper1/appendices/fanout_boundary_section_2026-07-06.tex` 160--165: the
  Landauer bill "falls due at amplification"; "pre-firing there is nothing
  to pay for, because there is nothing that counts as a record to erase."
- `paper1/wigners_friend_in_the_hopf_picture_2026-06-13.tex` 265--269: "The
  single relational copy is unitary and free ... The relative fact is
  thermodynamically free; the objective fact is what costs $kT \ln 2$."
- `paper1/appendices/appendix_jaynes_fibration_2026-07-19.tex` 322: the
  record side "irreversible and carries Landauer's toll".
- `paper1/derivation_of_the_quantum_postulates.tex` 143: Landauer costs
  "accrue with redundancy".
- The atticked August chain, Steps 7 and 8 (`attic_section_selfref_to_l2_
  chain_2026-08-04T1720.tex.superseded`): "before FANOUT nothing has been
  written anywhere, so nothing can require erasing, so no transformation can
  be charged."

None of these is false as a statement about *real* heat. What JS's remark
changes is the claim that the cost is *zero*: on the reading below it is not
zero but imaginary, and the split is between the real and imaginary parts of
one quantity, not between a cost and no cost.

## 2. What the corpus already holds

The idea is not new in kind; it is the thermodynamic face of a chain the
project already wrote down and fenced.

- **2026-07-26, imaginary temperature** (`session_summary_ctc_supertask_
  imaginary_temperature_2026-07-26.md`, section 4; Hawking gr-qc/9502017
  read in full that session). Hawking's closed-timelike-curve systems are "a
  particle coupled to a heat bath where the only difference is that the
  temperature of the heat bath is imaginary". At $1/T = i a$ the Gibbs
  weights become unimodular phases $e^{-i a E_n}$, a complex
  quasi-probability distribution summing to one; every functional built on
  them ($\ln Z$, $S = E/T + \ln Z$) goes complex. Hawking keeps a small
  positive real part in $1/T$ when rotating toward the real axis, and that
  residual real part is what damps the divergences. The session's "honest
  chain": imaginary temperature $\Rightarrow$ complex, ledger-valued
  information on the loop $\Rightarrow$ real coherence loss at the record;
  "the imaginary part is paid at the cut". RHYME 2's fourth clause:
  $\mathrm{Im}(1/T)$ is the loop.
- **The anti-event identity** (`sec:self-reference`; the August chain Step
  4): the surprisal of a negative entry is $-\log|p| - i\pi$; the imaginary
  part of information is the ledger line for the sign; an anti-event
  carries surprisal $i\pi$.
- **The self-reference/CTC identification** (2026-07-25/26 sessions): the
  pre-FANOUT loop of self-reference is read as a closed timelike curve, so
  Hawking's imaginary-temperature bath is the framework's own environment
  for the pre-record regime, not an analogy imported from outside.

Put those three together and JS's remark is what they imply for Landauer.

## 3. What "complex thermodynamic cost" can mean

Three readings, in increasing framework-specificity. They agree.

**(a) Complex temperature [CANDIDATE].** Landauer's bound per bit is
$k T \ln 2$, i.e. $(\ln 2)/\beta$ with $\beta = 1/kT$. Continue $\beta$ into
the complex plane, as the 07-26 chain does: $\beta = \beta_r + i\beta_i$.
The cost $C = (\ln 2)/\beta$ is then complex, with a real part that is
dissipated work and an imaginary part that is a phase, an action in units
of $\hbar$. On the imaginary axis, Hawking's pure CTC bath, unitary
evolution as periodicity in real time, $C$ is purely imaginary: no heat, a
phase. Giving $\beta$ a real part, Hawking's damping term, the record side,
gives $C$ a real part: Landauer's bill. FANOUT, on this reading, is the
rotation of $1/T$ from the imaginary axis toward the real axis, and
Landauer's $k T \ln 2$ is the real part of the analytically continued cost
at the boundary. The damping detail is a check the reading passes: the
regime with no real cost is also the regime with no damping, the winding
divergence of the 07-26 note.

**(b) Framework-native, through the surprisal [CANDIDATE].** Landauer's
bound is $kT$ per nat of entropy handed to the environment. Pre-FANOUT the
bookkeeper's entries are signed and their surprisal complex; an anti-event
carries $s = i\pi$. Price it at $kT$ per nat and the anti-event costs
$i\pi kT$: purely imaginary, a phase of $\pi$, which is exactly the sign
flip it performs. A fractional anti-event, rotation by $\theta$, costs
$i\theta kT$. Unitarity is then the conservation of the imaginary cost
(phase information is moved, never destroyed), and FANOUT is the event
that converts imaginary cost into real cost: decoherence is the phase
becoming entropy, the imaginary part becoming heat. The general
pre-FANOUT step has a complex cost whose real part is zero; the general
post-FANOUT step has a complex cost whose imaginary part has been paid at
the cut and whose real part is at least $k T \ln 2$ per bit.

**(c) The established neighbour [STRUCTURAL; VERIFY-CITE].** Landauer's
principle with quantum side information: del Rio, \AA berg, Renner,
Dahlsten and Vedral (Nature 474, 61, 2011, as recalled) show the work cost
of erasing a system $A$ given a memory $B$ is $k T \ln 2 \cdot S(A|B)$, the
conditional entropy, which is negative when $A$ and $B$ are entangled, so
erasure can *yield* work. Before a classical record exists, correlations
are quantum, and "free" erasure is really erasure at negative, recoverable
cost. The framework's complex cost would be the generalisation of that
negative conditional entropy to the signed-probability ledger: real and
negative in del Rio et al.'s setting, complex once the ledger carries
phases. Reeb and Wolf (New J. Phys. 16, 103011, 2014, as recalled) give the
tight finite-size form of Landauer's bound and are the reference for its
exact statement. Neither was read this session.

## 4. What would follow

- **The phase is the cost.** The framework already reads the imaginary
  part of the surprisal as the phase of the amplitude. Reading (b) says
  the same quantity is the thermodynamic cost of the operation that
  produced it. That is a unification, not an addition: one ledger, whose
  imaginary column is both "phase" and "cost", and whose real column is
  entropy. It would replace every "free" in section 1 by "costs a phase".
- **A thermodynamic form of the value-continuum premise [CANDIDATE
  bridge].** Landauer's real cost is quantised, $k T \ln 2$ per bit. Is
  the imaginary cost quantised? In the stabiliser fragment and the toy
  theory the available phases are fourth roots of unity, so imaginary
  costs come in units of $i\pi kT/2$: rationed. The value continuum of
  `op:limit-realisability`, that self-referential ignorance is not
  rationed, is then the statement that the imaginary cost of an anti-event
  has stages of every size. That gives the open premise a thermodynamic
  reading and possibly a route: a rationed imaginary cost would be a
  standard, a stable copyable unit, a record before any FANOUT.
- **Hawking's damping as the boundary's signature.** The record-side real
  part of $1/T$ both pays Landauer's bill and regularises the loop. If v2
  makes reading (a) precise, the boundary acquires a quantitative marker:
  the ratio of the real to the imaginary part of $\beta$.
- **A rhyme to keep fenced.** The Koide work of 2026-09-11 concluded that
  the phase $\delta = 2/9$ must be the exponential of a rational number, an
  action in units of $\hbar$ along a flat direction. On reading (b) an
  action in units of $\hbar$ is an imaginary cost in units of $kT$. That
  makes $\delta$ a cost, which is suggestive and nothing more. RHYME.

## 4a. Imaginary cost and particle mass (added later the same day)

JS asked whether the imaginary cost of an anti-event is related to particle
mass. It is, in three layers of decreasing standing.

**Mass is the rate of imaginary cost [STRUCTURAL, standard physics].** A
particle of mass $m$ at rest has amplitude $e^{-imc^{2}t/\hbar}$: its phase
advances at the Compton frequency $mc^{2}/\hbar$ (de Broglie's internal
clock; Schroedinger's Zitterbewegung; measured directly by the Compton-clock
experiment of Mueller's group, Science 2013, VERIFY-CITE). In the language
of this note the phase is the imaginary cost, so a massive particle at rest
accrues imaginary cost at a rate fixed by its mass, and every half Compton
period the amplitude changes sign: one anti-event per half period. On
reading (b) an anti-event costs $i\pi kT$; on Hawking's imaginary axis,
$kT = 1/(ia)$, that cost is real and equals $\pi\hbar/a$; setting it to
$mc^{2}$ gives $a = \pi\hbar/mc^{2}$, half the Compton period. So: mass is
the imaginary cost of an anti-event divided by the period of the loop on
which it occurs, and a massless particle is one that performs no anti-events
in any rest frame, having none. Check for v2: whether the framework's reason
for $m_{1} = 0$ (the massless neutrino, CANDIDATE in the results ledger)
matches "no anti-events".

**The free parameter as the clock period [CANDIDATE].** A phase is
dimensionless; turning it into a mass needs a period. The framework's one
free dimensional parameter is a scale the observer cannot fix from inside.
On this reading it is the period of the loop, and the structural claim
"ratios from inside, scale not" becomes "imaginary costs around loops are
counted from inside, the tick length is not". Consistency, not a result.

**Scale from real cost, ratios from imaginary cost [CANDIDATE].** The Koide
form writes the mass roots as $1 + \sqrt2\cos((\Phi + 2\pi k)/3)$, the real
parts of thirds of the loop phase $\Phi = 3\delta$, which the 2026-09-11
sessions identified as the Bargmann invariant of the generation triple: the
phase accumulated around the closed loop through the three generations. In
cost language the mass ratios are set by the imaginary cost around the
generation loop, $2/3$ of a nat, and the mass scale by the real cost paid at
closure, the norm defect's territory. The picture separates cleanly and it
re-expresses op:koide-delta without solving it: derive the imaginary cost of
the generation loop. That the number is a rational number of nats is what
the transcendence result of 2026-09-11 demanded (an exponentiated
rational), and a cost is a natural thing to be rational in nats.

**Near-miss closed [computed from the 2026-09-11 fit].** Landauer's real
unit is $\ln 2$ nats per bit. $3\delta = 0.6666743 \pm 0.0000188$ rad
against $\ln 2 = 0.693147$: excluded by about 1400 sigma; $\delta$ against
$(\ln 2)/3 = 0.231049$: likewise. The loop's imaginary cost is not "a bit".
The rhyme $3\delta = K$ gains a thermodynamic phrasing and no more. RHYME.

**Fences specific to this section.** (i) The Wick ambiguity: real cost per
unit imaginary time and imaginary cost per unit real time have the same
coefficient, the mass, so the framework must say which axis the FANOUT
boundary sits on before "the cost of an anti-event" is a definite quantity;
section 3(a) puts the boundary at the rotation between them. (ii) The
norm-defect identity fixes the object and not the spectrum, and the cost
reading cannot do better on its own: it relabels the same phase. (iii) The
temptation to read mass ratios off costs directly is the numerology the
closed-routes list already guards against; the value here is the
separation of scale from ratios and the dimensional reading of the free
parameter, not a formula.

References for this section (all from memory; verify before citing): de
Broglie 1924 (thesis) for the internal clock; Lan, Kuan, Estey, English,
Brown, Hohensee and Mueller, "A clock directly linking time to a particle's
mass", Science 339 (2013) 554, for the Compton clock.

## 5. Fences

- Complex temperature is not negative temperature; the 07-26 note's fence
  stands, and a referee will reach for negative temperature first.
- $e^{-iaH}/Z$ is not a density matrix, and the record never receives an
  imaginary entropy: the exterior sees real decoherence entropy (Hawking's
  own result). Any version of the idea in which the imaginary cost shows
  up as heat, or in which the record's entropy goes complex, contradicts
  the chain the project already has. The claim has to stay: the ledger is
  complex, the record is real, the imaginary part is paid at the cut.
- Landauer's principle is a statement about erasure into an environment at
  a real temperature. Pre-FANOUT the only "environment" available is the
  loop itself, at imaginary temperature. The reading therefore stands or
  falls with the self-reference/CTC identification, which is CANDIDATE.
- "Cost" pre-FANOUT is not an operational quantity in the usual sense;
  nothing can be paid until there is a record. The imaginary cost is a
  bookkeeping entry whose only observable consequence is the interference
  it later produces, which is also why it is conserved.

## 6. A well-formed open problem for v2

**op:complex-cost (proposed, OPEN).** Define the complex cost $C$ of an
operation in the pre-FANOUT regime such that (i) $\mathrm{Re}\,C = 0$ and
$\mathrm{Im}\,C$ is the accumulated phase, in units of $kT$ or
equivalently the action in units of $\hbar$, for every unitary step; (ii)
$\mathrm{Im}\,C$ is conserved under unitary evolution; (iii) at FANOUT the
imaginary part is converted to a real part with $\mathrm{Re}\,C \ge k T
\ln 2$ per bit written, Landauer's bound recovered as the real part of the
analytically continued cost. PASS: a definition meeting (i)--(iii) that
reduces to del Rio et al.'s $k T \ln 2 \cdot S(A|B)$ when the ledger is
real and to Landauer when the memory is classical. FAIL: any definition in
which the record receives an imaginary entropy, or in which
$\mathrm{Im}\,C$ is not conserved under unitary evolution, or which
distinguishes "free" from "costs a phase" by anything other than the
FANOUT boundary.

**A computation worth running first** (seed-locked, for the next version):
a single qubit; $Z(\beta) = \mathrm{tr}\, e^{-\beta H}$ continued to complex
$\beta$; the "free energy" $-(1/\beta)\ln Z$ and its real and imaginary
parts along the imaginary axis and along Hawking's tilted axis; erasure by
a unitary (pre) against erasure by measure-and-reset (post), with the
change in the complex free energy in each case. The prediction of reading
(a) is that the unitary erasure changes only the imaginary part and the
reset changes the real part by at least $k T \ln 2$.

## 7. References to verify before any of this is cited

- Hawking, gr-qc/9502017: in references.bib as `Hawking1995QuantumCurves`
  (read in full by the 2026-07-26 session); citable now.
- del Rio, \AA berg, Renner, Dahlsten, Vedral, "The thermodynamic meaning
  of negative entropy", Nature 474 (2011) 61, from memory.
- Reeb and Wolf, "An improved Landauer principle with finite-size
  corrections", New J. Phys. 16 (2014) 103011, from memory.
- Landauer 1961 is in the bibliography (Landauer_1961); Bennett 1973 is not.

## 8. Status

Idea: JS, 2026-09-16, recorded in v1's conclusions as too late for that
version. This document: the reading and the proposed open problem, labelled
CANDIDATE and OPEN throughout, with one STRUCTURAL neighbour to verify. No
paper text changed. For v2: the seven passages of section 1, the open
problem of section 6, and the computation.
