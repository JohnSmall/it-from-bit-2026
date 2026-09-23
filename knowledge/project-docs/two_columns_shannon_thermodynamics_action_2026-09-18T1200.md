# The two columns: Shannon, thermodynamics and action

Date: 2026-09-18T1200. Written by the Fable session at JS's prompt: "It's
interesting that thinking about anti-events pre-FANOUT brings Shannon entropy
and thermodynamics together. Think about the relationships." Companion to
`complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md` (sections 1--4e,
"the note" below) and to the v2 plan
`notes/paper1_v2_complex_cost_revision_plan_2026-09-18T1000.md`. The
computation is `scripts/two_columns_renyi_check_2026-09-18T1200.py`; its exact
stdout is section 12.

Labels are proposals; JS applies them. Every reference not already in
`paper1/references.bib` was from memory; all were verified against Crossref
on 2026-09-20 and batched, and section 9 records what changed. Verified
means the bibliographic record, not the argument: no body listed there has
been read, so every characterisation of what a paper says is still this
document's own.

## 0. The answer in brief

Shannon's surprisal $-\ln p$ and Clausius's entropy $\delta Q/T$ were already
one quantity before this framework: Jaynes made thermodynamic entropy the
Shannon entropy of the maximum-entropy distribution, and Landauer priced a nat
of erased information at $k_{B}T$ of heat. What the anti-event adds is a
second column. Plugging a negative weight into the log, which is the paper's
Shannon step (sec:complex-amplitudes), gives a surprisal with an imaginary
part, and the imaginary part of the surprisal of an amplitude is its phase,
which is the action in units of $\hbar$. So the framework's complex cost is
the complex surprisal of an amplitude,

$$-\ln\psi \;=\; \tfrac12\,(-\ln p)\;-\;i\,S/\hbar ,\qquad p = |\psi|^{2},$$

real column half the Shannon surprisal of the outcome, imaginary column the
action. Thermodynamics is the real column read through Landauer's constant
$k_{B}T$; dynamics is the imaginary column read through $\hbar$; and the paper
already deduces, from the scale at which self-reference bites, that the
inside quantity "must have the dimension of action" (its subsection "Scale and
dimension of limits to information"). The two constants are the exchange
rates of one currency, nats, on the two sides of the FANOUT boundary: $\hbar$
belongs to the inside (self-reference, phase, reversible), $k_{B}T$ to the
outside (records, heat, irreversible). An anti-event is a surprisal of
$i\pi$: half a turn of phase, an action of $\pi\hbar$, which is the half
Compton period of section 4a of the note. The rest of this document says what
follows, what the computation shows about the real column (it is two
quantities, not one), and what the framework must cite.

## 1. Where each ingredient enters the paper's chain

The chain in `what_is_a_quantum_state.tex` runs: self-reference forces
negative weights (Burgin's anti-events, the contextuality equivalence);
"we must use Shannon Information Theory and ... plug a negative value into the
log function", which needs analytic continuation and yields complex
amplitudes (sec:complex-amplitudes, with the declared value-continuum
premise); commutativity of addition of information excludes the quaternions;
FANOUT is where records begin and Landauer's cost is paid (sec:fanout-boundary,
"An anti-event erases information without thermodynamic cost", the sentence v2
corrects); and the "Scale and dimension" subsection deduces that the
inside limit has the dimension of action. So Shannon enters at the surprisal
of a single outcome, not as an average; thermodynamics enters at the record;
and action enters as the dimension of the inside scale. The complex cost of
the note joins the three: the surprisal is complex, its real part is what
records make thermodynamic, its imaginary part is what the inside scale
measures.

## 2. The complex surprisal [STRUCTURAL as arithmetic; CANDIDATE as the reading]

For a weight $w$, real or complex, the surprisal is $-\ln w$ on a chosen
branch. For an amplitude, $-\ln\psi = -\ln|\psi| - i\arg\psi$. Three facts,
all elementary, carry the whole reading.

*Additivity.* Amplitudes compose by multiplication, so complex surprisals add
along a path and across independent factors, exactly as Shannon's do across
independent events. That is the property the paper uses to exclude the
quaternions, and it holds for both columns at once: the real parts add and
the phases add.

*The half, corrected 2026-09-20 after JS's objection.* Since $p = \psi\psi^{*}$,
adding the surprisal of $\psi$ to that of $\psi^{*}$ is the Born rule and
nothing more: the "cancellation of phases" is a tautology at that point.
Physically the conjugate is the return leg of a closed loop,
$p = \langle\psi|U^{\dagger}|a\rangle\langle a|U|\psi\rangle$, forward under $U$
and back under $U^{\dagger}$ (the Schwinger--Keldysh contour; "time-reverse"
is exact only for time-symmetric dynamics), and a loop of that kind carries
no net phase by construction. The content is in the pair that does not close:
the density-matrix element $\rho(x, x') = \psi(x)\psi^{*}(x')$, a history
paired with the return leg of a different one, whose surprisal has real part
$-\ln|\psi(x)\psi(x')|$ and imaginary part the relative phase. On the
diagonal the loop closes and Shannon's surprisal of a probability results,
which is where thermodynamics lives; off the diagonal the imaginary column
lives. The complex cost of the note is the surprisal of exactly such a pair,
the fragments' overlap $\Lambda$ being Feynman--Vernon's $F[x, x']$, equal to
one on the diagonal and less than one in modulus, with a phase, off it. A
record is what forces the pair to close: FANOUT is the process by which only
closed loops survive, einselection said at the level of surprisals. Two
consequences. Pairing by multiplication (amplitude times conjugate) kills the
phase; pairing by addition (amplitude plus conjugate) keeps its real part,
$2|\cdot|\cos\Phi$: spectra, built by addition, see phases, and purities,
built by multiplication, do not (the blindness of section 7 and the session
note of 2026-09-19). And the factor one half at the surprisal level is the
factor four between the Fisher and Fubini--Study metrics on the real slice
(Wootters 1981, `wooters_1981`), the same Jacobian $dp = 2\sqrt p\,d\sqrt p$
once and squared: a consistency check, not a result.

*The branch.* $-\ln(-p) = -\ln p - i\pi$ on the principal branch (Part A of
the stdout). An anti-event carries the same real surprisal as its event and
an imaginary surprisal of $\pi$. Two anti-events compose to a positive
weight, and the sum of their surprisals differs from the surprisal of their
product by $2\pi i$ (Part A): the complex surprisal is defined modulo $2\pi
i$, and the ambiguity is the global phase. This is the point at which the
paper's declared premise (the value continuum, so that the surprisal is an
analytic function) and the Jaynes appendix's "phase as self-ignorance" meet:
analytic continuation of the log to negative arguments cannot be done without
choosing a branch, the branch is unobservable, and that unobservability is
the fibre.

## 2a. Is this the Born rule? (added 2026-09-20)

JS: "by thinking through the consequences of applying the Landauer principle
to the pre-FANOUT regime but allowing $T$ to be complex ... we've
rediscovered the Born rule". Verdict: not rediscovered; re-derived along the
route the paper already has (sec:born-rule, "the Born rule from fibre
privacy"), with one gain, that the route's tacit premise gets a name.

*What the chain gives without assumption.* A record's cost must be real and
must add over independent records (Landauer, and the additivity that fixed
the base field). A real, multiplicative, phase-blind function of a complex
amplitude is $|\psi|^{\alpha}$ for some $\alpha > 0$; nothing in Landauer, or
in a complex temperature, fixes $\alpha$. Applied to a single history the
chain gives $e^{-\mathrm{Re}\,C} = |\psi|$, exponent one, which is the wrong
rule. So the square is not in the chain.

*Where the square is.* In the closed loop: the record's weight is the product
of the forward leg and the return leg, $\psi\psi^{*}$ (section 2, "the half").
The paper's two routes say "the lowest-degree $U(1)$-invariant is quadratic".
That is true of polynomial invariants and false of invariants in general:
$|\psi| = (\psi\psi^{*})^{1/2}$ is $U(1)$-invariant and homogeneous of degree
one. What excludes it is analyticity: $|\psi|^{\alpha}$ is analytic in
$(\psi, \bar\psi)$ at the origin only for even $\alpha$, and the minimal
non-trivial case is two. The framework declared analyticity at the Shannon
step (the value-continuum premise, "so that the surprisal is an analytic
function on a continuum"); so the Born square follows from three premises the
paper already holds, fibre-blindness of records, analyticity, and minimality,
and the complex-cost chain's contribution is to show that the single-leg
weight $|\psi|$ is exactly what analyticity excludes (its surprisal has the
log's branch point). ESTABLISHED as arithmetic: $|\psi|$ is a $U(1)$-invariant
of degree one, so the sentences "there is no $U(1)$-invariant of degree one"
(sec:born-invariance) and "the lowest-degree invariant of a complex amplitude
is the quadratic" (sec:born-rule) need the word "polynomial" and the
analyticity premise named. This is a wording weakness in v1 a referee could
raise, and the fix is one clause in each place.

*The Hawking reading [CANDIDATE].* On the closed loop the two legs contribute
$+it/\hbar$ and $-it/\hbar$ to the complex inverse temperature and cancel: a
record is a loop of zero net period, Hawking's complex temperature is real on
it, and its cost is Landauer's. A loop that fails to close, $\rho(x, x')$,
keeps a net imaginary part. This is a consistent reading of the Born rule in
the cost ledger, and it is a reading, not a derivation: it borrows the two
legs from the record's structure as a correlation between system and copy,
which is Zurek's envariance setting (system entangled with its fragment) and
the diagonal of the decoherence functional, $p(h) = D(h, h)$.

*Aaronson's two norms [RHYME].* The pre-FANOUT weight is linear in the
amplitude, a complex "one-norm" object that is not a probability; the record
is the two-norm. Aaronson's argument that only the one-norm and the two-norm
admit non-trivial norm-preserving linear evolution says there is nothing in
between: the exponent is sharp even where the visibility is graded.

*To cite when this is written up (verified 2026-09-20 against Crossref and
the arXiv API; batched in `bib/two_columns_action_refs_2026-09-20T2200.bib`,
except Aaronson, which is in the library already but under a faulty entry --
see that file's closing comment):* Zurek,
"Probabilities from entanglement, Born's rule from envariance", Phys. Rev. A
71, 052105 (2005); Gell-Mann and Hartle 1990 for $D(h,h)$; Masanes, Galley
and Müller, "The measurement postulates of quantum mechanics are
operationally redundant", Nat. Commun. 10, 1361 (2019); Aaronson, "Is quantum
mechanics an island in theoryspace?", quant-ph/0401062 (2004); Aharonov and
Reznik, Phys. Rev. A 65, 052116 (2002).

*Proposed for the ledgers.* CANDIDATE: the Born rule read as the closed loop
of the complex-cost ledger (two legs, zero net period, real temperature).
ESTABLISHED (arithmetic): the $|\psi|$ loophole in the paper's "lowest-degree
invariant" wording, closed by the analyticity premise already declared. No
new derivation; no open problem minted, since the exponent's dependence on
a composition or analyticity premise is a known result (Aaronson;
Masanes--Galley--Müller) and the framework holds such a premise.

*Status 2026-09-20.* JS ruled the derivation into v2 with back-references from
the Hopf route; drafted and applied the same day as sec:born-cost-ledger
(`scripts/patch_born_cost_ledger_v2_2026-09-20T0900.py`, with item 1's
`patch_anti_event_real_cost_v2_2026-09-20T1000.py` as prerequisite), on the
main working tree, uncommitted and unbuilt. Record in
`sessions/born_cost_ledger_patch_2026-09-20T1000.md`.

## 3. Two constants, one currency [CANDIDATE]

A nat of real surprisal becomes heat at $k_{B}T$ per nat: Landauer for a bit,
$k_{B}T\ln 2$; Clausius in general, $\delta Q = T\,dS$ with $S = k_{B}H$
(Jaynes). A nat of imaginary surprisal, one radian of phase, becomes action
at $\hbar$ per nat: $S_{\rm dyn} = \hbar\,\arg\psi$. The Wick rotation is the
statement that these are two readings of one complex number, the complex
inverse temperature $\beta_{c} = \beta + it/\hbar$, since $e^{-\beta H}$ and
$e^{-iHt/\hbar}$ are the two faces of $e^{-\beta_{c}H}$. In nats,

$$C \;=\; \frac{Q}{k_{B}T} \;+\; i\,\frac{S_{\rm dyn}}{\hbar},$$

which is the complex cost of the note with its units made explicit. The
Boltzmann exponent $\hbar\omega/k_{B}T$ is the ratio of the two exchange
rates for one period of a mode; the Unruh and Hawking temperatures are the
case in which one full turn of the imaginary column, $2\pi$, is set equal to
one $\beta$ of the real column by a horizon. That last is a RHYME here, to be
made or broken in Paper 2, where the horizon is the FANOUT boundary; the
Euclidean-periodicity derivation is standard physics, and the framework does
not yet own the step from "records declared inaccessible" to "period $2\pi$".

*What it costs to undo an anti-event.* Before a record, an anti-event is a
relative phase $\pi$ and is undone by another: a $\pi$-pulse, an energy
difference $\Delta E$ applied for a time $\pi\hbar/\Delta E$, an action
$\pi\hbar$, dissipating nothing. Margolus and Levitin bound the time to reach
an orthogonal state from below by $\pi\hbar/2E$ (mean energy above the
ground state), so producing or undoing an anti-event costs at least an action
$\pi\hbar/2$: this is the imaginary column's Landauer bound, a floor on
action as Landauer's is a floor on heat, with $\hbar$ where Landauer has
$k_{B}T$ (Margolus and Levitin 1998, verified 2026-09-20; body not read, so
the $\pi\hbar/2$ floor is attributed to them here without being checked
against them). After the records exist,
undoing means either collecting every fragment and uncomputing, or erasing
them, at $k_{B}T$ per nat of what they hold. Pre-FANOUT the price of an
anti-event is time at a given energy; post-FANOUT it is heat at a given
temperature. The graded boundary of section 4b is the rotation from the one
price to the other, with angle $1/\sqrt{R}$.

*Which constant belongs to which side.* Temperature is a property of the
records' side: it is defined by the environment that holds the fragments, and
the framework has no temperature before it has an environment. The action
scale is a property of the inside: the paper deduces it from self-reference,
and Rovelli postulates it. So the two constants are not on an equal footing
in the framework: $\hbar$ is the framework's, $k_{B}T$ is the bath's, and
the FANOUT boundary is where the bath begins. The one dimensional input of
the framework (op:sector-scales) sets the imaginary column's rate for a
particle, the mass; a temperature sets the real column's rate for its
records, the width in the case of decay being the framework's own example
(note section 4d).

## 4. Two laws of two logical types [STRUCTURAL; the pairing CANDIDATE]

The real column obeys an inequality: records accumulate, entropy does not
decrease, Landauer is a lower bound. The imaginary column obeys a congruence:
a phase transported around a closed loop must return to itself modulo
$2\pi$, which is single-valuedness, Bohr--Sommerfeld quantisation, the
integrality of a Chern number, and the reason the global phase is a gauge
freedom (note section 4c). Two consequences follow for the framework's
accounting. First, there is no second law for the imaginary column and no
expectation value of it in the ordinary sense: an average of phases over a
distribution is not a phase, and the "quantropy" of Baez and Pollard (the
complex analogue of entropy for path-integral weights, with $1/i\hbar$ in the
place of $\beta$) is stationary, not maximal (Baez and Pollard, "Quantropy",
Entropy 17(2), 772--789 (2015), verified 2026-09-20; body not read, so
"stationary, not maximal" is this document's reading of their construction
and not a quotation). The framework's
version of the same fact is the computation of the 2026-09-18 session note:
$\mathrm{Re}\,C$ grows as $R$ and $\mathbb{E}|\mathrm{Im}\,C|$ only as
$\sqrt{R}$, the phases of independent fragments cancelling. Second, the
framework should keep its cost at the level of surprisals (one history, one
record) and take expectations only where the weights are real, at the record.
A complex "entropy" of a state is not needed and is not well defined; the
von Neumann entropy of a density matrix is real. The complexification lives
on histories and transitions, which is where the anti-event lives, and where
Hartle's extended probabilities and the Kirkwood--Dirac quasi-probabilities
live (section 9).

## 5. The real column is two quantities, not one [ESTABLISHED as computation; the reading CANDIDATE]

This is the substantive finding of the session, and it corrects a looseness
in the note and in the 2026-09-18 session note.

The real part of the complex cost is $\mathrm{Re}\,C = -\sum_{k}\ln|\lambda_{k}|$,
the decoherence exponent: the log of the fidelity between the two conditional
environment states, which is the Rényi divergence of order one half,
$D_{1/2} = -2\ln F$, per fragment. It measures how invisible the phase has
become. The Landauer quantity is different: the von Neumann entropy the
fragment actually carries, which for a balanced branch and overlap
$|\lambda|$ is $h\!\left((1+|\lambda|)/2\right)$ in nats. Part B of the
stdout tabulates both for $\lambda = \cos\phi$. They vanish together at
$\lambda = 1$ and are monotone together, but they are not proportional: the
ratio runs from $0.24$ at $\phi = 0.05$ to $5.6$ at $\phi = 1.55$, the small-$\phi$
behaviours are $\phi^{2}/2$ against $\epsilon(1-\ln\epsilon)$ with
$\epsilon = \phi^{2}/4$, and at $\lambda \to 0$ the decoherence exponent
diverges while the entropy saturates at $\ln 2$. A perfectly distinguishing
fragment is infinitely invisible and costs one bit to erase.

Part C adds the second distinction. For $R$ equal fragments the joint
environment entropy $h((1+|\lambda|^{R})/2)$ is bounded by $\ln 2$ and
reaches it (0.693147 at $R = 256$); the sum of the local fragment entropies
grows linearly in $R$ (27.39 at $R = 256$); the decoherence exponent grows
linearly too (11.70 at $R = 256$), with a different slope. So there are three
real quantities where the note spoke of one. The joint entropy is the record:
one bit, whatever the redundancy, and the global Landauer cost of resetting
the environment is at most $k_{B}T\ln 2$. The local sum is the redundancy
priced in heat: what an observer who meets the fragments one at a time and
erases each pays, linear in $R$. The decoherence exponent is the invisibility
of the phase, linear in $R$, and is the real part of the complex cost.

What this does to the earlier wording. "Landauer recovered at the plateau"
(session note, item 5 of the v2 plan) is right for the joint entropy and must
say so: the plateau is where the one-bit record is complete. "The real cost
accumulates as redundancy" is right for the local sum and for the decoherence
exponent, and must say which; the two are proportional to $R$ with slopes
$h((1+|\lambda|)/2)$ and $-\ln|\lambda|$, and only the first is heat.
"A perfect record costs infinitely much" (note section 4e, the rhyme on
Guryanova, Friis and Huber) must be fenced: the divergence is in the
decoherence exponent, not in the erasure cost, which is a bit; whether their
infinite resource cost is of the first kind (perfect orthogonality of a
pointer needs infinite energy or time, an action) or of the second is a
question to settle by reading them. And op:complex-cost item (i), "show the
real part reduces to Landauer for a thermal environment", is mis-stated as it
stands: the real part of $C$ is a fidelity, not an entropy, and it reduces to
nothing thermodynamic by itself. The corrected PASS criterion is in section
10.

Why the two real quantities are related at all, and where they agree. The
decoherence exponent is an amplitude-level quantity, order one half in the
Rényi family; the von Neumann entropy is a probability-level quantity, order
one. Single-shot thermodynamics prices erasure with a failure probability by
the max-entropy, which is the Rényi entropy of order one half of the state,
$2\ln\sum\sqrt{p_{i}}$, the log of a sum of amplitudes, and recovers the von
Neumann entropy only in the limit of many independent copies, by the
asymptotic equipartition property (Dahlsten, Renner, Rieper and Vedral 2011;
Faist, Dupuis, Oppenheim and Renner 2015; both verified 2026-09-20 against
Crossref, neither body read). That is the
right statement of "Landauer at the plateau": the amplitude-level cost is the
single-shot one, and the Shannon--Landauer form is its many-fragment limit.
The framework's cost is single-shot by construction, one history at a time,
which is why its real part is a fidelity.

## 6. The second-order form: Fisher plus Berry [STRUCTURAL as mathematics; CANDIDATE as reading]

The paper reaches the $L^{2}$ metric from the value continuum by two routes,
Hardy's continuity and Čencov's theorem with the every-basis lemma
(sec:cencov-route). Čencov's route uses the Fisher information, the curvature
of the real surprisal. The complexification of the surprisal has a
second-order shadow that is standard: the quantum geometric tensor
$Q_{ij} = g_{ij} + \tfrac{i}{2}F_{ij}$, whose real part is the Fubini--Study
metric (the Fisher metric, up to the factor four, on the real slice) and whose
imaginary part is the Berry curvature (Provost and Vallee 1980, verified
2026-09-20, Commun. Math. Phys. 76(3), 289--301, body not read; Berry 1984,
already in the library as `berry1984quantal` and checked correct; the Bargmann invariant to Berry phase relation is Mukunda and
Simon 1993, `mukundaQuantumKinematicApproach1993`). So the two columns at
first order (surprisal: real Shannon, imaginary action) become at second
order (curvature: real Fisher, imaginary Berry). The Koide phase
$3\delta$ is a Bargmann invariant (prop:koide-jordan), an imaginary-column
object; the masses are norms, real-column objects; and section 4a's "scale
from real cost, ratios from imaginary cost" is the first-order version of
"norms from the metric, phases from the curvature". Nothing here derives
$\delta$; it places it.

## 7. A rhyme, fenced: the Koide ratio as a Rényi-1/2 entropy [RHYME]

With $p_{k} = m_{k}/\sum m$ the mass fractions, the Rényi entropy of order one
half is $H_{1/2} = 2\ln\sum_{k}\sqrt{p_{k}} = \ln\big((\sum\sqrt{m})^{2}/\sum
m\big) = -\ln K$. So $K = e^{-H_{1/2}}$ identically, and the Koide relation
$K = 2/3$ says $H_{1/2} = \ln(3/2)$: the effective number of generations at
Rényi order one half is $3/2$, the geometric midpoint of the range $[1, 3]$
in the sense $e^{H}$. Part D of the stdout: $H_{1/2} = 0.40546841$ against
$\ln(3/2) = 0.40546511$ on PDG 2024 central values, the identity holding to
$10^{-16}$. This is arithmetic, and it says nothing that $K = 2/3$ did not
say. Its only interest is that order one half is the amplitude level of
section 5, the same level at which the fit-free reading of the Koide data
($p_{k} = \sqrt{m_{k}}/\sum\sqrt{m}$, the 2026-09-11 sessions) already works.
Keep out of the paper; do not add to the closed-routes list, since it is not
a route. Expanded 2026-09-19 in `sessions/koide_renyi_half_2026-09-19T1100.md`:
four equivalent forms (Foot's 45 degrees, negativity 1/4, purity 2/3 of the
democratic mixture of the generation states, the power sums), and the one
new fact, that the order-one-half entropy is blind to the phase, which enters
the spectrum first at cubic order through the Bargmann invariant.

## 8. What is not claimed, and the pushback

*Not new.* "Action is imaginary entropy" and "inverse temperature is imaginary
time" are the Wick rotation and are textbook; Baez and Pollard formalised the
complex-weight entropy as quantropy; Caticha's entropic dynamics derives the
Schrödinger equation from Shannon inference with the phase as a drift
potential; the decoherence functional of Gell-Mann and Hartle is
$\prod\lambda_{k}$ for two histories, so the complex cost is $-\ln D(h, h')$
and the framework did not invent it; and Hartle's extended probabilities are
negative weights for histories that have not decohered, which are usable
("settleable") only when records exist. That last is the nearest published
statement to "an anti-event before FANOUT", and the framework must cite it and
say what it adds. What it adds, on this session's reading, is threefold: the
origin of the negative weights in self-reference rather than in a choice of
coarse graining; the grading, the rotation angle $1/\sqrt{R}$ being physical
(the records) rather than formal (the contour); and the two identifications,
mass as the imaginary rate and width as the real rate (note sections 4a and
4d). None of the three is established by the arithmetic of section 2.

*Temperature is borrowed.* Every conversion of the real column into heat
needs a bath. The framework supplies nats; the bath supplies $T$. A claim of
the form "the framework predicts a heat" is empty until the bath is
specified; the framework's own real-column rate is the width, which is a
rate of records, not a heat.

*The half is a choice of bookkeeping.* Whether "the cost of a record" is
counted per amplitude (the fidelity, order one half) or per probability (the
entropy, order one) changes numbers by more than a factor of two (Part B),
and v2 must say which it means at each occurrence. The recommendation: the
complex cost stays amplitude-level, as it must (it has a phase); heat is
computed from the fragment entropies; the two are related by the single-shot
to asymptotic limit and nowhere identified.

*No complex entropy of a state.* Section 4. A reviewer who reads "complex
thermodynamic cost" as "complex entropy" will object correctly; the phrase
in v2 should be "the complex surprisal of a history" or "the complex cost of
a copy", never the entropy of anything.

## 9. Literature to position against (verified 2026-09-20)

*Verification, 2026-09-20 (Opus session).* Everything named below that was not
already in the library is batched, verified against Crossref by DOI, in
`bib/two_columns_action_refs_2026-09-20T2200.bib`; the corrections are listed
in that file's header and in each entry's note, and are almost all page ranges
where a first page had been given from memory. Three things this list got
wrong or short. Goldstein and Page's title is longer than the short form used
here. Connes and Rovelli's title continues past "relation". And Berry 1984 is
already in the library as `berry1984quantal`, so it is not batched. One item
could not be found: Mandelstam and Tamm 1945 has no Crossref or INSPIRE
record. One item in the library is faulty: `Aaronson2004h` carries the island
paper's title and eprint with the DOI, journal and volume of Aaronson's
"Quantum computing and hidden variables", a different paper; see the comment
block at the foot of the batch. None of the bodies below has been read except
where an entry's note says so, so every characterisation of what a paper
argues is still this document's own and not checked.

- Hartle, "Quantum mechanics with extended probabilities", Phys. Rev. A 78,
  012108 (2008): negative probabilities for non-decoherent histories,
  settleable only with records. Goldstein and Page, "Linearly positive
  histories", Phys. Rev. Lett. 74, 3715 (1995), the linear-positivity
  condition Hartle relaxes. Gell-Mann and Hartle 1990 (in Zurek, ed.,
  *Complexity, Entropy and the Physics of Information*) for the decoherence
  functional.
- Baez and Pollard, "Quantropy", Entropy 17, 772 (2015), arXiv:1311.0813.
- Caticha, "Entropic dynamics, time and quantum theory", J. Phys. A 44,
  225303 (2011). The library has `caticha_a_2006` ("From objective
  amplitudes to Bayesian probabilities"), which is the Born-rule paper, not
  the dynamics one.
- Mückenheim et al., "A review of extended probabilities", Phys. Rep. 133,
  337 (1986): in the library (the Mückenheim, Ludwig, Dewdney ... Bartlett,
  Jaynes entry); the paper cites it already for negative probability.
- Arvidsson-Shukur et al., the Kirkwood--Dirac review, `arvidssonshukur2024kirkwood`,
  in the library: complex quasi-probabilities on histories, and their
  "entropies".
- Margolus and Levitin, "The maximum speed of dynamical evolution", Physica D
  120, 188 (1998). Mandelstam and Tamm 1945 for the energy-spread form.
- Dahlsten, Renner, Rieper and Vedral, "Inadequacy of von Neumann entropy for
  characterizing extractable work", New J. Phys. 13, 053015 (2011); del Rio
  et al. 2011 (already in the v2 list); Faist, Dupuis, Oppenheim and Renner,
  "The minimal work cost of information processing", Nat. Commun. 6, 7669
  (2015); Tomamichel, Colbeck and Renner for the asymptotic equipartition
  property (IEEE Trans. Inf. Theory 55, 5840 (2009)).
- Provost and Vallee, "Riemannian structure on manifolds of quantum states",
  Commun. Math. Phys. 76, 289 (1980); Berry 1984 (Proc. R. Soc. A 392, 45);
  Mukunda and Simon 1993, in the library.
- Wootters 1981 (`wooters_1981`, in the library) for the factor four.
- Connes and Rovelli, "Von Neumann algebra automorphisms and time--thermodynamics
  relation", Class. Quantum Grav. 11, 2899 (1994), for the thermal-time
  reading of $\beta_{c}$, if Paper 2 wants it.
- Unruh 1976 (Phys. Rev. D 14, 870) and Hawking 1975 for the $2\pi$ rhyme;
  `Hawking1995QuantumCurves` is in the library for the complex temperature.

## 10. What changes in the v2 plan and in op:complex-cost

- Item 2 (the anti-event's cost at the complex-amplitude step) states the
  complex surprisal of section 2, the half, and the branch, in three
  sentences, and cites Hartle 2008 and Baez--Pollard 2015 (once verified) so
  the reader knows the object is not new and what is.
- Item 5 (the cost of a copy) distinguishes the three real quantities of
  section 5 by name: the record (joint entropy, one bit), the redundancy
  priced in heat (local sum), and the invisibility of the phase (the
  decoherence exponent, the real part of $C$). "Landauer at the plateau" is
  said of the first.
- Item 6 (Hawking's rotation) adds Margolus--Levitin as the imaginary
  column's floor beside Landauer's on the real column, one sentence.
- Item 10, op:complex-cost, criterion (i) is restated: PASS is to show that
  for a thermal environment of $R$ fragments the local fragment-entropy sum
  reproduces Landauer's heat per record and the joint entropy saturates at
  the record's size, while $\mathrm{Re}\,C$ is the decoherence exponent and
  is bounded below by the single-shot (max-entropy) cost; FAIL is any text
  that equates $\mathrm{Re}\,C$ with a heat.
- New item 12: the Jaynes appendix gains one paragraph saying that the
  complex inverse temperature $\beta_{c} = \beta + it/\hbar$ is Jaynes's
  multiplier continued to the complex plane, with the real part inference
  and the imaginary part dynamics, and that "time is operation count" is the
  statement that the imaginary multiplier counts composition steps. Label
  CANDIDATE. Item 13, optional: one sentence in sec:cencov-route naming the
  quantum geometric tensor as the second-order form of the two columns
  (section 6).
- The seven-passage checklist of the plan gains the word "entropy": no
  sentence in v2 may call the complex cost an entropy.

## 11. Proposed ledger entries

- **STRUCTURAL** (arithmetic) The complex surprisal of an amplitude is half
  the Shannon surprisal of its outcome minus $i$ times the action in units
  of $\hbar$; an anti-event contributes $i\pi$; the surprisal is defined
  modulo $2\pi i$. (Part A.)
- **ESTABLISHED** (computation) For a balanced branch and fragment overlap
  $|\lambda|$, the decoherence exponent $-\ln|\lambda|$ and the fragment
  entropy $h((1+|\lambda|)/2)$ are not proportional (ratio 0.24 to 5.6 over
  $\phi \in [0.05, 1.55]$), the former diverging and the latter saturating at
  $\ln 2$ as $|\lambda| \to 0$; for $R$ equal fragments the joint entropy is
  bounded by $\ln 2$ while the local sum and the exponent are linear in $R$.
  (Parts B and C.)
- **CANDIDATE** The two columns of the complex cost convert to physical
  quantities through $k_{B}T$ (heat, the records' side) and $\hbar$ (action,
  the inside), jointly the complex inverse temperature; pre-FANOUT the price
  of an anti-event is action, post-FANOUT it is heat; Margolus--Levitin and
  Landauer are the floors on the two columns.
- **CANDIDATE** The real part of the complex cost is a fidelity (Rényi order
  one half), not an entropy; Landauer's form is its many-fragment limit via
  the single-shot to asymptotic passage. Supersedes, in wording only, the
  session note's "Landauer recovered at the plateau".
- **RHYME** $K = e^{-H_{1/2}}$ of the mass fractions; Koide is $H_{1/2} =
  \ln(3/2)$. (Part D.) Not a route.
- **RHYME** One full turn of the imaginary column set equal to one $\beta$
  of the real column is the Unruh--Hawking temperature; for Paper 2.
- **open_problems** op:complex-cost, criterion (i) restated as in section 10.
- **invalid_routes** none.

## 12. Exact stdout of `scripts/two_columns_renyi_check_2026-09-18T1200.py`

```
=== Part A: complex surprisal of a negative weight (principal branch) ===
weight -0.3: surprisal -ln(-0.3) = 1.203973 -3.141593 i   (real part -ln 0.3 = 1.203973, imaginary part -pi = -3.141593)
two anti-events -0.3 and -0.5: sum of surprisals = 1.897120 -6.283185 i ; surprisal of the product = 1.897120 -0.000000 i
difference = -6.283185 i ; |difference| = 2 pi ? True

=== Part B: one fragment, overlap lambda = cos(phi), balanced branch ===
     phi     lambda    -ln|lambda|     h((1+lam)/2)      ratio  D_1/2=-2lnF
   0.050   0.998750       0.001251         0.005235     0.2389     0.002501
   0.100   0.995004       0.005008         0.017463     0.2868     0.010017
   0.200   0.980067       0.020135         0.055849     0.3605     0.040270
   0.300   0.955336       0.045692         0.106980     0.4271     0.091383
   0.500   0.877583       0.130584         0.230280     0.5671     0.261168
   0.800   0.696707       0.361391         0.425555     0.8492     0.722781
   1.000   0.540302       0.615626         0.539094     1.1420     1.231253
   1.200   0.362358       1.015123         0.625978     1.6217     2.030247
   1.400   0.169967       1.772150         0.678632     2.6114     3.544300
   1.500   0.070737       2.648784         0.690643     3.8352     5.297567
   1.550   0.020795       3.873051         0.692931     5.5894     7.746102
small phi = 0.05: -ln cos phi = 1.250521e-03 vs phi^2/2 = 1.250000e-03 ; h((1+lam)/2) = 5.234943e-03 vs eps(1 - ln eps) = 5.235139e-03 with eps = 6.248698e-04
limits: lambda -> 1: both -> 0 ; lambda -> 0: -ln|lambda| -> infinity, h -> ln 2 = 0.693147

=== Part C: R equal fragments at phi = 0.3 (lambda = 0.955336) ===
     R     |Lambda|    sum local ent        joint ent    -R ln|lambda|
     1 9.553365e-01         0.106980         0.106980         0.045692
     2 9.126678e-01         0.213960         0.179425         0.091383
     4 8.329625e-01         0.427921         0.287280         0.182767
     8 6.938266e-01         0.855841         0.428026         0.365533
    16 4.813953e-01         1.711683         0.572326         0.731066
    32 2.317414e-01         3.423366         0.666049         1.462133
    64 5.370410e-02         6.846731         0.691704         2.924266
   128 2.884130e-03        13.693463         0.693143         5.848532
   256 8.318206e-06        27.386925         0.693147        11.697064
joint entropy is bounded by ln 2 = 0.693147 ; the local sum and the decoherence exponent grow linearly in R

=== Part D: the Koide ratio as a Renyi-1/2 entropy (PDG 2024 central values, MeV) ===
K = sum m / (sum sqrt m)^2 = 0.66666446 ; 2/3 = 0.66666667
H_1/2(mass fractions) = 0.40546841 nats ; ln(3/2) = 0.40546511 ; exp(-H_1/2) = 0.66666446 ; K - exp(-H_1/2) = -1.1e-16
effective number of generations at order 1/2: exp(H_1/2) = 1.500005 ; at order 1 (Shannon): exp(H_1) = 1.244343 ; range [1, 3]
```
