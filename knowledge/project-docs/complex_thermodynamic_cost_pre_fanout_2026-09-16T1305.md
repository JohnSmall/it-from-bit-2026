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

**(c) The established neighbour [STRUCTURAL; reference verified 2026-09-20,
body not read].** Landauer's principle with quantum side information: del
Rio, \AA berg, Renner, Dahlsten and Vedral, "The thermodynamic meaning of
negative entropy", Nature 474(7349), 61--63 (2011), doi 10.1038/nature10123 show the work cost
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
experiment of Mueller's group, Science 2013, verified 2026-09-20 against
Crossref 10.1126/science.1230767 for the bibliographic record only; the
experiment's own interpretation is still unread, and the Compton-clock
reading of it was contested when it appeared). In the language
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

## 4b. Graded FANOUT as the rotation of the cost (added 2026-09-18)

JS's second thought on the idea: it is more elegant than a sharp cut at
FANOUT where thermodynamics suddenly applies, and it fits the graded FANOUT
of the Wigner's-friend section, a record being many copies rather than one
event, with the real part of the cost accumulating over copies and the
phase parts cancelling; and it fits Hawking's complex temperature and
Zurek's quantum Darwinism. A toy model
(`scripts/graded_fanout_complex_cost_2026-09-18T0830.py`, argument and
exact output in `sessions/graded_fanout_complex_cost_2026-09-18T0830.md`)
confirms the intuition in a precise form and adds two things it lacked.

- **The cost is a standard object [STRUCTURAL].** For a system copied into
  $R$ fragments the coherence is $ab^{*}\prod_k\overline{\lambda_k}$,
  $\lambda_k$ the fragment overlap (Zurek's decoherence factor), and the
  cost is $C_R = -\sum_k\ln\lambda_k$: real part the accumulated
  distinguishability (the record), imaginary part the accumulated phase.
  It is $i$ times the Feynman--Vernon influence action; the 07-26 note's
  RHYME-2 clause (v) is an identity.
- **The rotation [STRUCTURAL, computed].** $\mathrm{Re}\,C_R = R\gamma$;
  with independent fragment phases $\mathrm{Im}\,C_R$ is a random walk
  ($E|\mathrm{Im}| = \sigma\sqrt{2R/\pi}$), so the angle of the cost from the
  real axis falls as $1/\sqrt{R}$: from the imaginary axis (a phase-only
  interaction) to the real axis (many records). The phases do not cancel
  in the global state; they fail to add coherently.
- **Not sharp even at $R = 1$.** Any fragment with $|\lambda| < 1$ already
  has a real cost; pre-FANOUT is exactly $|\lambda| = 1$. The Wigner's-
  friend "single relational copy is free" becomes "costs $\gamma_1 -
  i\theta_1$, the real part small but not zero".
- **Independence is required.** Identical fragment phases (a coherent,
  replica environment) never rotate the cost; the phase stays recoverable
  and recurrences occur. Independence of witnesses is Zurek's condition
  and must enter the framework's definition of a record.
- **Zurek.** The system's entropy saturates at the Landauer value while the
  real cost grows as redundancy, the $R$ of the ladder; the mutual
  information with a fragment set reaches the plateau $H_S$ early and
  exceeds it only when nearly all fragments are held. The imaginary part is
  "paid at the cut" in this exact sense: conserved globally, available
  locally to no one.
- **Hawking [CANDIDATE; the identity STRUCTURAL].** At imaginary inverse
  temperature the Caldeira--Leggett noise kernel's $\coth(\beta\omega/2)$
  becomes $-i\cot$: the bath's real cost is a phase, the pre-FANOUT regime.
  Hawking's hand-inserted real part of $1/T$, which damps the divergences,
  is here $\sum_k\ln(1/|\lambda_k|)$, and the angle is $1/\sqrt{R}$: the
  framework derives the rotation he put in.

Fences carried over from the session note: the model is pure dephasing
(coherence loss in nats, heat only with a thermal environment and $kT$);
the CTC identification is CANDIDATE; finite-$R$ recurrences are the same
fact as Hawking's damping. The open problem of section 6 is refined there:
general couplings with energy exchange; the phase-recoverability bound
$\prod_{k\notin F}|\lambda_k| \to 1$; the fragment-sum form of Hawking's
real part; FAIL if a replica environment pays a real cost.

## 4c. Motion in space as change of phase (added 2026-09-18)

JS: extending the complex cost into the spacetime section means that
movement in space becomes changes in phase.

**Established.** Momentum generates translation as energy generates time
evolution: a displacement $\Delta x$ multiplies a momentum eigenstate by
$e^{-ip\Delta x/\hbar}$; the phase along a worldline is the action
$S/\hbar = \int(p\cdot dx - E\,dt)/\hbar$. Section 4a's "mass is the rate of
imaginary cost per proper time" and today's "momentum is the rate per
distance" are the two components of one Lorentz scalar, the action; the
split is frame-dependent, the value is not (de Broglie 1924, the harmony
of phases; the thesis was defended in 1924 but the text with a DOI is its
publication in Annales de Physique, series 10, volume 3, pages 22--128,
dated 1925, verified 2026-09-20 --- decide which is meant before importing,
because the batch carries the published version and the two should not both
be imported). The real part, entropy from records, is also
invariant: the complex cost is a scalar and the Lorentz group of
sec:lorentz acts on its decomposition.

**Framework reading [CANDIDATE].** Pre-FANOUT, motion is phase
accumulation: free propagation, reversible, no real cost. Post-FANOUT,
motion is a track of records, each scattering a copy with a real cost, and
the classical trajectory is the redundant record: Mott's 1929 cloud-chamber
problem answered by quantum Darwinism with position as the pointer basis
(Mott 1929, "The wave mechanics of $\alpha$-ray tracks", Proc. R. Soc. A
126(800), 79--84, and Joos and Zeh 1985, Z. Phys. B 59(2), 223--243, for the
localisation rate; both verified 2026-09-20 against Crossref, neither body
read, so the localisation rate is not checked. Note that Crossref's record
of Mott's title is corrupt, carrying U+221D where the alpha belongs). The
grading is the monitoring rate times the per-scatter distinguishability,
$\sum_k\ln(1/|\lambda_k|)$ over scattering events. Paper 2 material (the
Newtonian limit, op:p2-newton); one forward pointer in Paper 1 v2 from the
redundancy-ladder resolution.

**Consequence [CANDIDATE].** The spacetime section defines spacelike
distance through closed loops on which information is transported
consistently. In cost language, consistency around a closed loop is
single-valuedness of the amplitude: the imaginary cost around the loop is
a multiple of $2\pi$, i.e. $\oint p\cdot dx = 2\pi n\hbar$, Bohr--Sommerfeld.
Hawking's imaginary-temperature sum over windings is the same condition
from the loop's side. And it matches the Koide result from the other side:
$3\delta = 2/3$ is not a multiple of $2\pi$, so the generation phase is an
open-path action on a non-compact direction, not a closed-loop holonomy,
as the transcendence analysis of 2026-09-11 demanded. Closed loops
quantise, open paths do not.

**Fences.** The phase--motion identification is de Broglie's; the framework
supplies only the boundary reading. Distance counted in bits through loops
against a continuous phase per bit rests on the value continuum of
op:limit-realisability, the one declared premise. The Wick angle that
rotates the cost (FANOUT) is not the rapidity that rotates $E$ into $p$;
different rotations of different pairs; a rhyme, one sentence at most.

## 4d. Identifying "mass is associator debt" with "mass is the rate of imaginary cost" (added 2026-09-18)

JS: the two accounts must be identified. The paper's definitions
(sec:masses "What mass is: associator-debt"; the debt-to-defect bridge,
eq:debt-defect; the Higgs subsection of the boson section) supply what is
needed, and the paper's own sentence already has the two faces: "the
associator prices the debt at issuance, where the octonion norm still
balances the books; the sedenion norm defect is where it settles."

**The identification [CANDIDATE].** The associator debt is the complex
cost per composition step. Read at issuance it is the imaginary column: an
obligation carried as phase, the "information cost of specifying a
bracketing that the algebra leaves ambiguous" (the paper's definition),
in nats per step. Read at settlement it is the real column: the norm
deficit of a product, eq:debt-defect, where a composition actually fails
to conserve the norm. The paper says mass is the debt and that the
associator "carries an inverse length in natural units, as a mass must";
a debt per step with the dimensions of inverse length is a rate, and with
time as operation count (the spacetime section) the step is a tick of
proper time. So "mass is associator debt" and "mass is the rate of
imaginary cost per unit proper time" are one statement read at the two
ends of the same ledger line: the debt issued at each composition is the
phase the state accrues per tick, and the Compton clock is the associator
ticking. The magnitude of the debt per step is fixed where it settles, at
the mediated composition through the preferred direction, the Yukawa
vertex with the vacuum value as the magnitude of the selection: that is
the paper's own account of $m_f = y_f v/\sqrt2$, now read as "the size of
the per-step obligation is set at the vertex, and between vertices it
accrues as phase". Under a Wick rotation the two columns are one
coefficient: $e^{-m\tau_E}$ along Euclidean time, $e^{-imt}$ along real
time, $e^{-mr}$ along a spacelike separation (the Compton wavelength as
the debt's range).

**What the identification buys.**

- *Why mass is a constant [STRUCTURAL, given the ledger].* The associator
  has uniform magnitude on every bracketing not forced to vanish
  ($G_2$-transitivity; the fact that closed the Koide-phase route). A
  uniform debt per step is a constant phase rate: a clock, not a drift. The
  same uniformity that forbids the associator from setting the hierarchy is
  what makes each mass a well-defined number.
- *The complex mass [STRUCTURAL as standard physics; CANDIDATE as
  reading].* An unstable particle's amplitude goes as $e^{-i(m - i\Gamma/2)t}$:
  the complex pole. In cost language this is the complex cost rate: $m$ the
  imaginary accrual, $\Gamma/2$ the real settlement rate, the rate at which
  the debt is paid into records, the decay products being the records. A
  stable particle is one whose debt is never settled as norm loss because no
  record channel exists (the electron: nothing lighter to decay into), so
  its cost is purely imaginary and its clock ticks forever. The width is a
  separate number, set by the available channels, not by the defect.
- *Scale and ratios, again.* The debt's magnitude (real column, settled at
  the vertex) sets the scale; the frame's phase structure around the
  generation loop (imaginary column, the Bargmann invariant $3\delta$) sets
  the ratios. This is the paper's division of labour, associator for
  existence and triality angle for ratios, restated in one currency.
- *A route for op:associator-geodesic [CANDIDATE].* The geodesic proxy
  used in the operational mass calculations computes an accrued quantity
  along a path; the definition is a per-step debt. They agree if the
  proxy's length is the number of composition steps and the accrued
  quantity is the action, steps times per-step debt. The length that mass
  multiplies is the worldline's proper time, not an internal geodesic on
  $S^7$, which is why the retraction of the internal-geodesic picture
  (invalid_routes, March) stands and this does not reopen it.
- *The top at the boundary [RHYME].* The paper places the top where "its
  internal traversal rate equals the Higgs vacuum value", $y_t = 1$. In
  cost language: the largest possible debt per step, the calibration bound
  at which the sedenion zero divisors sit. Whether $m_t = v/\sqrt2$ is
  literally the saturating debt is not shown; recorded as a rhyme.

**Decay channels as records [STRUCTURAL as standard physics; the reading
CANDIDATE].** JS: "so the possible decay channels are the possible records
that can be created?" Yes, with one sharpening: a channel is a record only
if the products reach a continuum of final states and cannot re-form the
parent. Fermi's golden rule takes its irreversibility entirely from that
continuum; a "decay" into one discrete state is a Rabi oscillation,
reversible, a phase. The density of final states is the record's
redundancy. So the possible records are the *open* channels, kinematics and
conservation laws deciding which are open, and stability is the absence of
any admissible record of the parent's disappearance (the electron: charge
conservation and nothing lighter charged). The exact form is the optical
theorem: the self-energy is complex, its imaginary part the total rate into
open channels (settlement, the width, the real cost rate), its real part the
mass shift (the phase rate); a channel contributes to the imaginary part only
above threshold, i.e. only once a record can be written, and below threshold
only to the mass. The complex pole $m - i\Gamma/2$ has its two columns filled
by exactly this rule. Confirming cases: neutrino flavour oscillation (no
continuum, no record, purely imaginary) and virtual emission-and-reabsorption
in a loop (renormalises the mass, writes nothing).

**Fences.** This identifies two accounts of one coefficient; it derives no
mass. The step-is-a-tick equation rests on "time is operation count",
which is the framework's premise, and on the register's composition steps
being timelike ticks for a particle at rest. The real column at the vertex
is a coupling, not an entropy: norm conservation holds for the full
process, and the debt is only "settled" as actual norm loss in a decay,
where the products are the records. Do not read the norm defect as
decoherence.

## 4e. Clocks that pay: the thermodynamic cost of timekeeping (added 2026-09-18)

JS supplied Pearson, Guryanova, Erker, Laird, Briggs, Huber and Ares,
"Measuring the thermodynamic cost of timekeeping", Phys. Rev. X 11, 021029
(2021), read in full. It is relevant, and more sharply than "clocks cost
entropy": it supplies the vocabulary that separates the two columns of the
complex cost inside a clock, a theorem giving the exchange rate between
them, and the empirical anchor for the real column that the Compton-clock
experiment supplies for the imaginary one.

**What the paper establishes [STRUCTURAL, read].** A clock is a clockwork
plus a register (their Fig. 1): the clockwork consumes a resource and
produces a periodic signal; the register identifies ticks in it and counts
them. Accuracy is $N = (t_{\rm tick}/\Delta t_{\rm tick})^{2}$, the number
of ticks before the accumulated timing error reaches one tick. For the
autonomous quantum clock of Erker et al. (2017), $N_{Q} = \Delta S_{\rm
tick}/2k_{B}$; for their classical thermomechanical clock (a silicon
nitride membrane driven by white noise, read by an rf cavity, the ticks
being upward zero crossings of the demodulated signal) the best achievable
accuracy is $N_{C} = 2\pi^{2}(T_{c}/T_{N})\,\Delta S_{\rm tick}/k_{B}$,
with $\Delta S_{\rm tick}$ the entropy created per tick in the readout
circuit and $T_{N}$ the noise temperature of the electronics. The measured
$N$ is linear in $\Delta S_{\rm tick}$ over an order of magnitude, at about
$N_{C}/10$ (their tick identification is not optimal), and saturates when
the membrane goes nonlinear. Two things in the paper matter here. First,
the derivation of $N_{C}$ (their Appendix B) is a phase-estimation problem:
each tick is the estimate of the oscillator's phase $\phi_{n}$ from a
non-overlapping segment of a noisy record, $N = 4\pi^{2}/\langle\delta
\phi_{n}^{2}\rangle$, the least-squares error is $\delta\phi^{2} \propto$
noise over signal energy per cycle, and the entropy per tick is the signal
energy per cycle dissipated in the cold resistor divided by $T_{c}$.
Combining their eqs. (1), (3) and (B1), the bound reads
$\langle\delta\phi^{2}\rangle\,\Delta S_{\rm tick} = 2k_{B}T_{N}/T_{c}$:
the clockwork's phase can be written into the register only at a fixed
price in entropy per unit of phase precision. Second, they separate a clock
from a stopwatch: a clock must identify ticks as they occur, whereas a
device that reads a finished record retroactively gives elapsed time on
interrogation and no continuous reference; and "any system that acts as a
register is expected to consume work, as it would inevitably require to
perform measurements of irreversible events" (their Sec. V, citing
Guryanova, Friis and Huber 2020).

**The mapping [CANDIDATE].** Clockwork and register are the two columns.
The clockwork's phase is the imaginary column: it accrues freely, costs
nothing real, and is unobservable until registered. The register is
FANOUT: each tick is a record, and the entropy per tick is the real cost
of that record. Their theorem is then the exchange rate between the
columns, and the experiment is the demonstration that the real column is
paid per record and only per record: they themselves set aside the
clockwork's own dissipation (the white-noise drive) as not the fundamental
cost, and the entropy that bounds accuracy is the entropy per registered
tick. In this vocabulary section 4a reads: a massive particle at rest is
clockwork without a register. Its phase advances at $mc^{2}/\hbar$, one
clockwork cycle per Compton period, and nothing is written; the "anti-event
per half period" of section 4a is a clockwork event, not a tick. The
Compton-clock experiment (Lan et al. 2013) is a register attached to that
clockwork: the interferometer reads the accrued phase, the apparatus pays
Pearson et al.'s price per tick, the particle pays nothing. This answers an
objection the mass reading invites. If mass is a clock rate and clocks
dissipate in proportion to accuracy, a particle at rest should dissipate.
It does not, because the entropy is per registered tick and a stable
particle registers none. The unstable particle registers exactly one, the
decay, with the width as the real cost rate (section 4d). Since an
exponentially distributed interval has standard deviation equal to its
mean, a decaying particle read as a clock has accuracy $N = 1$ exactly
[ESTABLISHED, trivial]: one tick, one record, no timekeeping. That this is
"the least a record can do" is a RHYME.

**The scaling law is the same [STRUCTURAL as statistics; CANDIDATE as
identification].** Pearson et al.'s bound has the form (phase error)$^{2}
\times$ (real cost per tick) $=$ constant. The graded-FANOUT model of
section 4b has, from the closed forms recorded in the 2026-09-18 session
note ($\mathrm{Re}\,C = R\gamma$, $\mathbb{E}|\mathrm{Im}\,C| =
\sigma\sqrt{2R/\pi}$), rotation angle $r \approx \sigma\sqrt{2/\pi}/(\gamma
\sqrt{R})$ and hence $r^{2}\,\mathrm{Re}\,C = 2\sigma^{2}/(\pi\gamma)$,
independent of $R$: (residual phase)$^{2} \times$ (real cost) $=$ constant.
This follows by algebra from the recorded closed forms and was not run
separately. Both are the central-limit statement that $R$ independent
fragments fix a phase to $1/\sqrt{R}$ and cost $R$. The objects differ:
their $\delta\phi$ is the estimation error of a classical oscillator phase
from $R$ samples; our $r$ is the argument of the complex cost, the residual
phase of the fragment sum. The correspondence is in the exchange rate, not
in the identity of the phases, and that is the claim to keep: a register of
$R$ fragments buys phase precision linearly in real cost, in both accounts.

**A perfect record costs infinitely much [RHYME; source read 2026-09-20, and
it does not say this in the currency assumed here].** The cost
of a copy is $-\ln\lambda_{k}$; its real part $-\ln|\lambda_{k}|$ diverges
as the fragment becomes perfectly distinguishing, $|\lambda_{k}| \to 0$.
Guryanova, Friis and Huber, "Ideal projective measurements have infinite
resource costs", Quantum 4, 222 (2020), cited by Pearson et al. as the
reason a register must consume work, states the same direction for
measurements. Read in full 2026-09-20, and it holds as its title says, but
not in the currency this note assumes: see the verification paragraph added
at the end of this section. If it holds as its title says, the graded boundary
of section 4b is the finite-resource version of their statement, and v1's
"Landauer at the first copy" is doubly too sharp: a first copy is neither
free nor a complete record. Fence added 2026-09-18T1200: the divergence is
in the decoherence exponent, the invisibility of the phase; the erasure cost
of a perfectly distinguishing fragment is one bit, not infinite (two-columns
note, section 5, Part B). Whether their infinite cost is an action (to make
the pointer orthogonal) or a heat is what reading them must settle.

**Motion [RHYME].** Section 4c makes the phase rate of a moving particle
$p\cdot dx$ and the track its register. A cloud-chamber track is a clock in
Pearson et al.'s sense, one tick per droplet, its momentum read from the
curvature at a precision priced by the number of droplets. Not pursued.

**A lesson for the record's basis.** Pearson et al. show (their Sec. V and
Fig. 4) that the precision extracted from one and the same voltage record
depends on which observable is registered: the energy flux has the opposite
dependence on drive power from the tick interval. Accuracy is a property of
the register's observable, not of the clockwork. In the framework's terms a
record is basis-dependent, which is what the every-basis lemma and the
blind-spot clause (item 4 of the v2 plan) say: what is written, and so what
is paid, depends on which fragment observable is declared the record.

**Fences.** (i) The experiment is classical: a thermal oscillator, a
classical phase, an oscilloscope. It measures the real column and says
nothing about a quantum phase or an imaginary cost; the anchor for the
imaginary column remains Lan et al. (ii) The factor of ten between $N$ and
$N_{C}$ and the nonlinear saturation mean the relation is an upper bound
on accuracy, not an equality; the correspondence is with the bound's form.
(iii) Their entropy is heat over a bath temperature; the framework's real
cost is a log-overlap in nats. The two agree at the plateau only under the
Landauer identification already assumed in section 4b, which
op:complex-cost is to prove. (iv) The thermodynamic uncertainty relations
they compare against (Barato and Seifert 2016) bound precision by entropy
production for Markovian steady states; the graded-FANOUT exchange rate,
when the fragments form a Markovian register, must not beat them. That is a
check to add to op:complex-cost, not a result.

**For v2.** Item 7 of the revision plan cites Pearson et al. beside Lan et
al.: the one for the register's price, the other for the clockwork's rate.
Item 10 (op:complex-cost) gains a PASS sub-criterion: the model's exchange
rate must reduce to a phase--entropy relation of Pearson et al.'s form for
a register of $R$ fragments, and must respect the thermodynamic uncertainty
relation. Item 5 cites Guryanova et al. once verified. The wording "one
anti-event per half period" in item 7 becomes "one clockwork cycle per half
period; nothing is registered".

References for this section: Pearson et al. read (pp. 1--12 and 16--18;
Phys. Rev. X 11, 021029 (2021), DOI 10.1103/PhysRevX.11.021029). Taken from
its reference list and not read: Erker et al., Phys. Rev. X 7, 031022
(2017); Barato and Seifert, Phys. Rev. X 6, 041053 (2016); Milburn,
Contemp. Phys. 61, 69 (2020); Schwarzhans et al., Phys. Rev. X 11, 011046
(2021); Guryanova, Friis and Huber, Quantum 4, 222 (2020). Batch:
`bib/clock_thermodynamics_refs_2026-09-18T1100.bib`.

**Verified 2026-09-20 (Opus session).** Every entry in the batch was checked
against Crossref and the batch corrected in place; the bibliographic
corrections are listed in its header and are additions, not errors. Guryanova,
Friis and Huber was read in full, because item 5 turns on what kind of cost
theirs is. **It is an energy cost paid in finite time, and it is not an entropy
cost.** Their Appendix A.IV.3: measurement procedures that reduce the rank "use
either infinite energy $E$, take infinite time $t$ (an infinite sequence of
finite interaction range operations) or are infinitely complex (infinite
interaction range operations)". Their section 6 makes the trade explicit:
"Within our cooling paradigm, the energy cost for reaching the ground state in
finite time is infinite. Other paradigms allow cooling to the ground state
using finite energy, but require infinite time." The Discussion's summary is
"ideal finite-time projective measurements have an infinite cost". Entropy
enters only in the appendix, where the thermal pointer state minimises energy
at fixed entropy and maximises entropy at fixed energy, which is how the work
cost is bounded from below; the third law is the *reason* for the divergence,
not the coin it is paid in.

Two consequences for item 5, neither fatal and both needing a decision.

First, the currencies do not line up as this section assumes. The cost of a
copy here is $-\ln\lambda_{k}$, and it is its *real* part, the entropy-like
part, that diverges as $|\lambda_{k}| \to 0$. Guryanova et al.'s divergence
is in the energy--time pair. So they cannot be cited as stating "the same
direction" for the same quantity; they state the same direction for a
different one. That the diverging pair is energy and time is the shape of an
action, which is suggestive given section 4d, but they never form the product
and never use the word, so the identification would be the framework's own
step and would need its own label. RHYME is the right level as the heading
already has it.

Second, their divergence is conditional and their approximation is cheap. It
holds "unless pure states are freely available", which the framework should
not quietly assume it has; and "ideal measurements can be approximated by
non-ideal, unbiased ones to arbitrary precision at finite energy cost". The
infinity sits in the last step to *perfect* correlation, not in making a good
record. This strengthens rather than weakens the fence already added at
2026-09-18T1200: a first copy is neither free nor complete, and a nearly
complete one is not expensive either.

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
- Pearson, Guryanova, Erker, Laird, Briggs, Huber and Ares, Phys. Rev. X 11,
  021029 (2021): read 2026-09-18; batched as `pearson2021timekeeping` in
  `bib/clock_thermodynamics_refs_2026-09-18T1100.bib`, citable once imported.
- From Pearson et al.'s reference list, in the same batch, all verified
  2026-09-20 against Crossref: Erker et al. 2017 (`erker2017autonomous`),
  Barato and Seifert 2016 (`baratoseifert2016brownian`), Milburn 2020
  (`milburn2020thermodynamics`), Schwarzhans et al. 2021
  (`schwarzhans2021clockworks`), Guryanova, Friis and Huber 2020
  (`guryanova2020projective`, read in full). Lan et al. 2013
  (`lan2013compton`) was in the batch from memory and is now verified
  against Crossref 10.1126/science.1230767. Every field remembered was
  right; the corrections were additions only, and are listed in the batch
  header. Only Pearson et al. and Guryanova et al. have been read; the other
  five are cited on Pearson et al.'s characterisation of them, which is
  recorded in each entry's note.

## 8. Status

Idea: JS, 2026-09-16, recorded in v1's conclusions as too late for that
version. This document: the reading and the proposed open problem, labelled
CANDIDATE and OPEN throughout, with one STRUCTURAL neighbour to verify. No
paper text changed. For v2: the seven passages of section 1, the open
problem of section 6, and the computation.

2026-09-18: JS ruled that sections 4a--4d "need to be in paper 1 (version
2)". The revision plan, eleven insertions with target passages, drafts,
labels, dependencies, references to batch and the order of work, is
`notes/paper1_v2_complex_cost_revision_plan_2026-09-18T1000.md`; the
computation is notebook S.

2026-09-18, later: section 4e added after reading Pearson et al. (2021),
supplied by JS. It changes no label above; it supplies the clockwork/register
vocabulary, the exchange-rate reading of the accuracy--entropy relation, and
three amendments to the v2 plan (items 5, 7 and 10), recorded there.

2026-09-18, later still: the relationships between Shannon surprisal,
thermodynamic entropy and action that the anti-event brings together are in
`two_columns_shannon_thermodynamics_action_2026-09-18T1200.md`, with a
computation. It sharpens one thing here: the real part of the complex cost is
a fidelity (the decoherence exponent), not an entropy; the Landauer quantity is
the fragment entropy, and the two are neither equal nor proportional. Read
"real cost" in sections 3, 4b and 4d as the decoherence exponent, and "heat"
as the fragment entropies times k_B T, until v2 fixes the wording (plan items 5
and 10).

2026-09-19: indefinite causal order placed on the same ladder in
`indefinite_causal_order_fanout_2026-09-19T0900.md`: the quantum switch
separates operation count (a phase, definite on both branches) from order (a
record); graded FANOUT of the control multiplies the order-interference by the
same Lambda as the phase. For Paper 2's causal-order section; one open
problem proposed (op:ico-threshold).

2026-09-20: the first two v2 insertions are in the paper text (main working
tree, uncommitted, unbuilt): item 1, "without real cost" with the placeholder
sentence at the first mention; item 2, the subsection sec:born-cost-ledger,
the Born rule as the closed loop of the cost ledger, with back-references
from both existing Born-rule sections and the |psi| loophole closed. Section
1's checklist of "free" passages: the first is done. Record in
`sessions/born_cost_ledger_patch_2026-09-20T1000.md`.

2026-09-20, later: the temperature in Landauer's equation, and the energy cost
of FANOUT, in `landauer_temperature_fanout_energy_2026-09-20T1200.md`: T is
the payer's, the framework fixes only the entropy; with complex beta the
equation has four corners (Landauer, Planck, width, Matsubara) and FANOUT is
the rotation between the two real ones; the thermal time is the crossover;
at a horizon T is fixed by Unruh and cancels (Paper 2's four-constant
junction). Amends v2 plan items 6, 7 and 10.

2026-09-20, later still: records and causal structure at very high
temperature, in `records_causal_structure_high_temperature_2026-09-20T1400.md`:
definiteness and memory scale oppositely with T; the thermal time as the
causal structure's resolution; conserved charges as the surviving records
and the sphaleron check on Paper 1's baryon-number sentence (op:sphaleron,
proposed); no clocks above the electroweak crossover; the area law as record
capacity and the singularity as the failure of records. For Paper 2.
