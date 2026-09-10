# Session Summary / Onboarding: 2026-07-25 -- loops, recursion depth, and the third route

Purpose: onboard a fresh conversation. This session opened the perturbative-QFT front, the
third of three routes to the same geometry. JS's long-standing suggestion (that the loops
and infinities of QFT might justify the Hopf fibrations ontologically, without the
epistemological detour through observer self-reference) had been parked as an invitation to
others. The success of the p-adic exercise of 2026-07-23 prompted the same treatment here:
find the good questions, price them, and hand them over. Companion documents (referenced,
not duplicated): `appendix_loop_recursion_2026-07-25T1140.tex` (the appendix,
compile-verified), `refs_loop_recursion_2026-07-25T1140.ris` (23-entry batch, Mendeley
import owed). Sits beside `appendix_padic_ctc_division_2026-07-23T0617.tex` (six of whose
labels are load-bearing cross-references), `claude_appendix_continuity_open_problems_2026-07-17.tex`
(Accumulation Lemma), and `open_problem_asymptotic_freedom.md` (engaged in the cautions
block; upgrades NOTHING).

## 1. JS's correction, which is the spine

The session's decisive move was JS's own caution: it is WRONG to identify a loop in a
Feynman diagram with a CTC and hence with self-reference. Single loops are finite in many
theories and are computed daily; the identification would be unfalsifiable and cheap. What
is interesting is loops acquiring their own loops -- the unbounded RECURSION of nested
subdivergences, driving to infinite frequency and hence to a supertask.

This correction turns out to name the object the technical literature is already built
around. Kreimer's and Connes-Kreimer's Hopf algebra exists precisely to bookkeep nested and
disjoint subdivergences; the coproduct records nesting, the antipode is the closed form of
Bogoliubov's recursive subtraction, and the relevant grading is the CORADICAL FILTRATION
(depth), not the loop number. Large-order behaviour confirms the choice: renormalons, as
opposed to instantons, are identified with graph families carrying MANY NESTED
SUBDIVERGENCES. The non-perturbative content the series cannot reach is carried by the
deep-nesting sector. STRUCTURAL.

Framing thesis for the appendix (JS's): the three routes -- epistemological self-reference,
the non-Archimedean fork, and now perturbative recursion depth -- are ways of nailing down
the carpet of non-computability in the room of computability. What matters is not that any
is right but that some are useful. All 2D maps of the globe are wrong; the question to ask
of a projection is what it is good for. Division of labour: the epistemological route is
good for the Born rule and for saying what a measurement is; the non-Archimedean route is
good for the arithmetic of the obstruction; the perturbative route is entirely on the
ontological side, touches measured quantities, and connects to a published uncomputability
theorem.

## 2. Proved this session (appendix lemmas)

(a) DEPTH LEMMA (`lem:depth`): loop number L = I - V + 1 (= the power of hbar) and coradical
depth d are INDEPENDENT gradings. At every L >= 1 there is a primitive graph (d = 1, no
divergent proper subgraph -- the zig-zag family witnesses); at every L >= 2 there is the
rainbow r_L with d = L. Hence d is not a function of L. Consequence, and the reason the
lemma is in the paper: the loop expansion is an expansion in hbar, NOT an expansion in
self-reference. Any framework claim about divergences must be graded by d and must concern
the d -> infinity limit, never an individual diagram. This is JS's caution as a theorem.

(b) ASSOCIATOR TRANSVERSALITY (`lem:transversality`): over a field of char != 2, an algebra
that is both alternative (associator alternating) and pre-Lie (associator symmetric in some
pair) has vanishing associator, hence is associative. One line. Corollary `cor:jacobi`:
pre-Lie is Lie-admissible (commutator obeys Jacobi -- the source of the name); alternative
is not, the octonion commutator algebra being the 7-dimensional simple Malcev algebra. The
two weakenings of associativity are transverse, and are distinguished by whether
antisymmetrisation lands in a Lie algebra. Stated as folklore-assumed, not claimed new; not
found in the operad literature but elementary. Its job is DISCIPLINARY: it forbids the
tempting shortcut of reading graph-insertion non-associativity as octonionic
non-associativity in perturbative dress.

(c) LOG REMARK (`rem:log-nowhere`), fenced CANDIDATE: each nesting level contributes one
power of log(Lambda/mu), so depth d appears as log^d and its tally is the plain count, which
converges at NO completion of Q (Archimedean by the Accumulation Lemma's standard; finite
places because |n|_p <= 1). Power divergences, regularised along a dyadic cutoff tower, are
doubling cascades and DO complete 2-adically (lem:doubling, eq:fanout-tally). This is the
reverse of their physical standing: the log carries beta functions, anomalous dimensions and
anomaly coefficients -- all the scheme-independent content -- while the power divergences are
legislated away. Reading offered: the divergences that carry physics are exactly those whose
supertask completes nowhere. Fenced because the identification of a regularised divergence
with a series in Q is a choice of tower, subject to the inherited BRIDGE CONDITION. The
practical instruction survives the fence: build only on logarithmic, scheme-independent data.

## 3. The loop ledger (classical, cited, not reproved) and its corollary

`thm:loop-ledger`, nine clauses: (i) Connes-Kreimer Hopf algebra, BPHZ as Birkhoff
decomposition / Riemann-Hilbert problem; (ii) Milnor-Moore, graded dual = enveloping algebra
of the insertion Lie algebra, insertion product PRE-LIE, bracket = Ihara bracket in an
explicit matrix Lie algebra (Berg-Cartier); (iii) van Suijlekom -- Ward and Slavnov-Taylor
identities generate a HOPF IDEAL, quotient Hopf algebra has gauge symmetry built in, with a
coaction on couplings and fields; (iv) Cutkosky cutting rules, discontinuity = sum over cuts,
optical theorem to all orders; (v) Feynman-Vernon / CTP -- real part of the influence action
governs dissipation, IMAGINARY PART IS THE DECOHERENCE FUNCTIONAL, rendering the coarse
variable classical; (vi) Watson-Onorati-Cubitt -- an explicit RG map, computable at each step,
convergent to correct fixed points, whose FLOW IS UNCOMPUTABLE, built on Cubitt-Perez-Garcia-Wolf
spectral-gap undecidability; (vii) deep nesting governs large-order behaviour (Dyson,
renormalons, Balduf-Panzer to 400 loops); (viii) Feynman periods are motivic, acted on in the
manner of a Galois theory, with the RG inside that structure (Connes-Marcolli, Brown's cosmic
Galois group); (ix) Adams -- Hopf invariant one exactly in dimensions 1, 2, 4, 8, corresponding
to the normed division algebras.

`cor:solved-unpredicted`: (i) and (vi) do not conflict and their conjunction IS the point. The
Hopf algebra guarantees the recursion has a closed-form solution order by order; the
uncomputability result guarantees the flow that solution generates need not be predictable
even in principle. LOCAL SOLVABILITY, GLOBAL UNPREDICTABILITY -- the carpet nailed at every
finite depth, the bump appearing in the limit. RESTRICTION stated in the same breath: (vi) is
for lattice many-body Hamiltonians, not continuum perturbative RG; the transfer is open and is
`op:qft-uncomputable`.

## 4. Fenced RHYMEs and the CANDIDATE

RHYME 1, one equation and two temperaments, again: `cor:solved-unpredicted` repeats the carry
map (divergent at infinity, contracting p-adically) and Deutsch's fixed point (exists by
compactness, delivers no construction). Resemblance in ROLE.

RHYME 2, the debt is paid at the cut: three imaginary parts with record-side readings --
Im(amplitude) = sum over on-shell intermediates (iv); Im(influence action) = decoherence
functional (v); Im(complex information) = debt incurred (framework). Fence: (iv) and (v) are
different objects, S-matrix element vs open-system influence action, and no identification
between THEM is asserted.

RHYME 3, two carpets and one room: by `lem:transversality` the ledger's non-associativity and
the loop expansion's cannot inhabit one algebra. If the routes meet, they meet in the GEOMETRY
both algebras act on. Consistent with "the algebra fixes the skeleton, the geometry carries the
measure"; offered as a constraint on future unification attempts, not as evidence.

CANDIDATE: FANOUT identified with the locus where the imaginary part of the CTP influence
action becomes large. Below threshold interference survives; above it the coarse variable is
classical and copyable. FALSIFIER: a FANOUT event with no counterpart in the imaginary part, or
a large imaginary part with no record. Posture note: this is the framework INHERITING a
mainstream object rather than proposing a new one -- the same move as the complementarity
reframe towards Khrennikov in the p-adic appendix.

## 5. Five open problems (the invitation)

`op:qft-depth` nesting depth as the supertask index: state a criterion under which the
d -> infinity limit is a supertask rather than a divergent sum, and determine whether it
selects the renormalon families rather than arbitrary ones. A negative result CLOSES the
appendix's central claim and must be reported as such.
`op:qft-brst` is the Slavnov-Taylor Hopf ideal the record-consistency condition? Positive
answer identifies BRST cohomology with the FANOUT boundary in gauge theory and makes the
quartet mechanism the cancellation mechanism.
`op:qft-decohere` what the influence-functional identification buys: exhibit one quantity it
predicts that the standard CTP treatment does not naturally suggest. House suggestion, offered
without confidence: a Landauer accounting converting Im(influence action) into a bit ledger
with a definite constant.
`op:qft-uncomputable` does the uncomputability transfer from lattice to continuum perturbative
RG, and is it the SAME obstruction? Three outcomes all informative (transfer + identification
supports one obstruction with several descriptions; transfer without identification exhibits
two and the framework must explain why; failure to transfer says the continuum is better
behaved).
`op:qft-twohopfs` the two Hopfs: NOT the name coincidence, which is worthless. The substantive
question is whether exceptional content can live in a graded connected commutative Hopf
algebra of graphs at all, given Milnor-Moore. A proof that it cannot is a good outcome and
closes a line that would otherwise invite decades of pattern-matching.

## 6. Cautions and closed routes (do not retry)

(a) A LOOP IS NOT A CTC. Closed. Only unbounded nesting depth is at issue; `lem:depth` is why.
(b) VIRTUAL PARTICLES ARE NOT STATES. No argument may be phrased as a particle traversing a
loop. The claim belongs to the effective-action fixed-point equation (Jackiw), where Gamma
appears on both sides of its own defining integral, and to the filtration of its iterative
solution. Naive form closed.
(c) RENORMALISABILITY DOES NOT DISCRIMINATE THE SM -- the GUTs are renormalisable ('t
Hooft-Veltman). "Only the SM is renormalisable" cannot succeed. The discriminating notion, if
any, is UV COMPLETENESS (asymptotic freedom, no Landau poles, vacuum stability), which belongs
with `open_problem_asymptotic_freedom.md` and is not reopened. Closed.
(d) Power divergences are scheme artefacts; nothing is built on them.
(e) GHOSTS ARE NOT QUASI-PROBABILITY NEGATIVITY. Different objects, different justifications;
category error until `op:qft-brst` settles. Note the asymmetry: the quartet mechanism removes
ghosts EXACTLY, whereas the framework's negativity is relocated, not removed.
(f) The uncomputability results are LATTICE many-body, not perturbative QFT. Citing them as
though they applied would be a misuse.
(g) BRIDGE CONDITION inherited in full from the p-adic appendix: any adelic reading of a
regularised divergence needs the quantity located in Q or a fixed number field first; the
dyadic cutoff tower is a choice, not a canonical identification.
(h) The two Hopfs share a name and a namesake and nothing written down. A nominal link is
worthless; the connection must run through H-spaces / Milnor-Moore or not at all.

## 7. Literature check performed this session (what is novel, what exists)

GAP CONFIRMED: no connection anywhere between the Connes-Kreimer renormalisation Hopf algebra
and Adams / Hopf invariant one / normed division algebras. The algebraic renormalisation
literature branches to gauge theory, ribbon graphs, Rota-Baxter algebras, deformation
quantisation, numerical integration and motivic periods, and never meets Adams. The
division-algebra programme in particle physics has never asked what its structures look like
in a coradical filtration. The two Hopfs have not been introduced.
ALREADY EXISTS, must be inherited not claimed: the pre-Lie character of graph insertion
(Berg-Cartier name it a right-symmetric non-associative algebra and give a matrix realisation);
the BRST/Hopf-ideal result (van Suijlekom); the imaginary-part-as-decoherence-functional
reading (Feynman-Vernon, Calzetta-Hu, Shaisultanov, who explicitly discusses fields being
"measured" and rendered classical); uncomputability inside an RG flow (Watson-Onorati-Cubitt,
Nat. Commun. 13, 7618 (2022), on Cubitt-Perez-Garcia-Wolf, Nature 528, 207 (2015)).
NOT FOUND, so presumed unoccupied: the supertask framing of divergences; the transversality
lemma as a stated result; the depth-vs-loop-order distinction stated for framework purposes.
DEMOTED after checking: anomalies and UV-completeness to a remark (the latter already
belongs to the asymptotic-freedom document); resurgence to a sentence, since Balduf-Panzer
shows the field moves fast enough that a posed problem would be overtaken.
OWED READING, not cited: arXiv:2607.04115, "Infrared Divergences as Itinerant Vacua" (July
2026) -- converts the IR-divergent imaginary part of the influence functional into a classical
stochastic source by a Hubbard-Stratonovich identity, claiming no prior coarse-graining or
decoherence assumption, applied to soft QED, de Sitter, soft gravitons and GRAVITATIONAL
MEMORY. Bears directly on `paper2_gravitational_memory_2026-07-12.md` INDEPENDENTLY of this
appendix. Author list not verified; do not cite until checked.

## 8. Deliverables, verification, owed actions

Appendix: pdflatex PASS x2 in an amsthm harness, zero errors, no undefined refs or citations,
seven pages, ASCII PASS, no bullets in prose (theorem-clause romanettes only, sibling
precedent). A MAIN-BODY INSERT paragraph for the conclusions sits in the header comments,
carrying the three-routes / map-projection framing.
Labels dangling BY DESIGN, all of which must be co-present: master `sec:self-reference`,
`sec:fanout-boundary`, `sec:born`, `sec:hopf` (last two = the same mapping task as the Jaynes
and p-adic appendices, now THREE deep, VERIFY); p-adic appendix `app:padic-shadow`,
`lem:doubling`, `eq:fanout-tally`, `thm:ledger`; continuity appendix `app:continuity-open`,
`lem:accumulation`. Master preamble may still need
\newtheorem{proposition}[theorem]{Proposition} (flagged previously).
RIS: 23 entries, PASS (TY/ID/ER counts match, one AU per line, keys in ID, native Unicode --
Frederic Chapoton, Perez-Garcia -- no LaTeX escape macros). DEDUPE WARNING on import:
thooft1980naturalness may already have arrived in the reverse-flow batch of 2026-07-23. Three
keys assumed EXISTING (VERIFY): adams1960, hurwitz1898, thooft1980naturalness.
OWED (JS): Mendeley import; label mapping; confirm the p-adic and continuity appendices are in
the same document; add the \input line after app:padic-shadow (it cites it); read
arXiv:2607.04115 for Paper 2 regardless of this front.

## 9. Retrievables (compact facts)

L = I - V + 1 = power of hbar. Coradical depth d = maximal chain of nested divergent
subgraphs. Primitives exist at every L; rainbow r_L has d = L. Depth d contributes log^d.
Renormalons <-> many nested subdivergences; instantons <-> factorial growth in the number of
graphs. Alternative = associator alternating (Artin: any two elements generate an associative
subalgebra). Pre-Lie = associator symmetric in a pair; Lie-admissible. Octonion commutator =
7-dim simple Malcev, not Lie. Alternative + pre-Lie => associative (char != 2). Milnor-Moore:
graded connected cocommutative Hopf algebra = enveloping algebra of its primitives; the graph
algebra is commutative, hence its dual group is pro-unipotent -- as classical as a Hopf algebra
gets. Adams: Hopf invariant one iff n in {1, 2, 4, 8}. Cutkosky: cut propagators -> on-shell
delta functions. Im(Feynman-Vernon influence action) = decoherence functional. Slavnov-Taylor
=> Hopf ideal. Watson-Onorati-Cubitt: each RG step computable, flow uncomputable.
