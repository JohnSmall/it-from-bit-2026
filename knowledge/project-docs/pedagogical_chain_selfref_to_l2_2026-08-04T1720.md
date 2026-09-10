# From self-referential ignorance to the L^2 metric: the derivation chain in fourteen steps

**Session document, 2026-08-04.** Pedagogical write-up of the chain: self-referential
ignorance -> signed (negative) probability -> complex surprisal via the continued
logarithm -> complex amplitudes -> thermodynamically free pre-FANOUT reversibility ->
divisibility -> connected transformation group -> Hardy Axiom 5 as theorem -> L^2 metric
(Banach--Lamperti), with independent confirmation via Chentsov / Fisher--Rao. Written at
expository grade: the reader is never asked to take a step on the authority of
unfamiliar mathematics, and every unproved step is named as such.

**Status discipline.** Every step carries a permanent label:

- ESTABLISHED -- the step is carried by external published literature.
- FRAMEWORK -- proved or argued in-house; original to this programme; not yet
  independently published or vetted.
- CANDIDATE -- fenced suggestion; introduced with pointers, not claimed.
- OPEN -- not provable by anyone yet, including us.

Labels are never upgraded in place; changes arrive as dated addenda.

**Companion files.** LaTeX paper section:
`section_selfref_to_l2_chain_2026-08-04T1720.tex` (same content, paper register).
Citation batch: `refs_selfref_to_l2_chain_2026-08-04.ris`. All memory-sourced
bibliographic entries are flagged VERIFY-CITE in the RIS N1 fields; only `schack2003`
(verified against arXiv and the Springer DOI this session) and the arXiv identifier
inside `hardy2001` (verified via the fetched Schack reference list) are exempt. The keys
`hardy2001` and `schack2003` REUSE the keys already present in
`claude_appendix_continuity_open_problems_2026-07-17.tex`: run a dedupe check on
Mendeley import.

**Depends on / feeds.**
`claude_continuity_blocks_and_routes_2026-07-17.md` (premises P2-prime and Layer 1; the
Spekkens foil; the divide-and-close motor);
`claude_appendix_continuity_open_problems_2026-07-17.tex` (existing hardy2001 /
schack2003 keys; reconstruction-target discussion at B7);
`fanout_logic_measure_correspondence_theorem_v2_2026-05-17.md` (Step 8);
`lawvere_inside_outside_fixed_point_theorem_2026-05-04T1806.md` (Step 1);
`research_summary_neg_prob.md` (Step 3);
`appendix_winding_number_operator_2026-07-12.tex` (the 2 pi i monodromy of Step 4).

---

## 0. The map before the journey

We start with an observer who is part of the world they describe. We show that their
ignorance about themselves is not a nuisance but a law; that accounting for it honestly
forces complex numbers into the books; that operations performed before any record
exists must be free and reversible; that free-and-reversible leaves no way to forbid
half-steps; and that a world with continuous reversible motion between states can
measure distance in only one way: the L^2 way.

---

## Step 1. A describer inside the description must have a blind spot. [ESTABLISHED]

Imagine a perfectly detailed map of a room, hung inside that room. To be complete, the
map must show the map -- which must show the map showing the map, and so on. Or
Popper's version: build a machine that predicts its own output one second from now,
then wire it to do the opposite of whatever it predicts. Whatever it predicts, it lies.
This is one argument wearing many costumes -- Cantor, Godel, Turing, and in physics
Popper's predictor and Breuer's theorem that no apparatus can perfectly measure a
system containing itself. Lawvere showed in 1969 that these are literally the same
theorem, instances of a single fixed-point schema; Yanofsky's survey makes the schema
accessible. No embedded observer can hold a complete, consistent description of a
whole that includes themselves.

Citations: cantor1891diagonal, goedel1931formal, turing1936computable,
popper1950indeterminism1, popper1950indeterminism2, breuer1995selfmeasurement,
lawvere1969diagonal, yanofsky2003universal.

## Step 2. Give the blind spot a bookkeeper: Shannon. [ESTABLISHED]

Physics cannot forbid observers from being embedded -- every observer is. So the blind
spot must be accounted for, not wished away. The accounting system for ignorance
already exists: Shannon's information theory. If you assign probability p to an
outcome, your surprise when it happens is s = -log p. Certain events (p = 1) carry no
surprise; impossible-seeming events carry unbounded surprise. Everything from here on
is careful bookkeeping with -log p.

Citation: shannon1948communication.

## Step 3. Self-ignorance breaks the ordinary books. [FRAMEWORK]

Try to keep ordinary books -- every entry a number between 0 and 1 -- about yourself.
The predictor of Step 1 returns: whatever probability the machine's books assign to
"I will output 0", the machine can read its own books and defeat the entry. A complete
self-assignment in [0,1] is exactly the kind of total self-description Step 1 forbids.
Two honest escapes exist: forbid the situation (Russell's route -- unavailable, since
the observer really is embedded), or extend the number system of the entries. The
extension: allow some internal bookkeeping entries to go negative, so long as every
entry corresponding to something actually observable remains an honest probability.

Negative quasi-probabilities have a respectable pedigree -- Wigner 1932, Dirac 1942,
Feynman 1987 -- and modern work (Abramsky--Brandenburger on the sheaf-theoretic
structure of contextuality; Spekkens on the equivalence of negativity and
contextuality) shows that negativity is precisely the impossibility of one global
consistent assignment. So negativity itself is well charted. What is NOT in any
literature is the claim made here: that self-reference is the ORIGIN of the negativity
-- that the signed entries are forced by the diagonal argument of Step 1. [redacted 2026-09-10: private remark by a named third party; see knowledge/memory/CORRECTIONS.md]

Status detail: the negativity--contextuality scaffolding is ESTABLISHED; the
self-reference origin is FRAMEWORK (structural argument, not yet a published theorem).

Citations: russell1908types, wigner1932quantum, dirac1942bakerian, feynman1987negative,
abramskybrandenburger2011sheaf, spekkens2008negativity.

## Step 4. Take the logarithm of a negative number. [ESTABLISHED mathematics; the physical identification is CANDIDATE]

The bookkeeper's rule is s = -log p. But some entries are now negative. What is
log(-1/4)? On the real line, nothing. But the logarithm extends -- analytically
continues -- beyond the real line in exactly one natural way, and every mathematics
undergraduate meets the key fact as Euler's identity: e^{i pi} = -1, hence
log(-1) = i pi. So log(-1/4) = log(1/4) + i pi, and the surprisal of a negative entry
is

    s = -log|p| - i pi :

an ordinary real surprise about the magnitude, plus an imaginary offset of exactly pi
recording the sign. The imaginary part of information is the ledger line for the sign.

One honest disclosure: the continued logarithm is many-valued -- going once around
zero adds 2 pi i -- and we choose the principal branch. That ambiguity is not a
defect; the multiples of 2 pi i become winding numbers later in the story (see
`appendix_winding_number_operator_2026-07-12.tex`).

Status detail: the mathematics (continuation, branch structure) is ESTABLISHED; the
identification of imaginary surprisal with physical phase is FRAMEWORK, held at
CANDIDATE.

## Step 5. Exponentiate back and you are holding an amplitude. [Definitional, given Step 4]

Probabilities and surprisals are inverses: p = e^{-s}. Feed in the complex surprisal
of Step 4 and out comes a complex number psi = e^{-s}, with |psi| carrying the
magnitude of the old entry and arg(psi) carrying the accumulated i pi's. Complex
amplitudes were not postulated. Self-ignorance was double-entered and the complex
numbers walked in through the arithmetic.

## Step 6. The continuation is a package deal: the whole dial comes with the switch. [ESTABLISHED mathematics; closure premise CANDIDATE, half-open]

Analytic continuation does not merely define log(-1); it defines z^t = e^{t log z} for
EVERY real t. The instant one accepts log(-1) = i pi one has accepted
(-1)^{1/2} = e^{i pi/2} = i, and (-1)^{1/3}, and (-1)^{0.1387}. You cannot buy the
sign flip without buying the entire continuous dial of phases -- the circle U(1). And
there is no halfway house: a small exercise shows no finite set of phases survives the
analytic root (the principal square root of a k-th root of unity has order 2k -- it
escapes the set). So IF the phases the formalism attains are closed under the roots
the formalism itself defines, the phase group is either trivial (the classical case,
already excluded by Step 3) or the full circle.

That italicised IF is a premise, not yet a theorem. It is a phase-group instance of
the ledger's divisibility family (P2-prime); recorded as CANDIDATE, half-open: the
mathematics is trivial, the physical premise is not.

## Step 7. What does a transformation cost? [ESTABLISHED]

Landauer, 1961: ERASING one bit of information has an unavoidable price, kT ln 2 of
heat paid to the environment. Bennett later showed the converse: logically reversible
operations -- ones that discard nothing -- can in principle be performed at zero cost.
The price tag is attached to forgetting, never to doing. This has been experimentally
confirmed (Berut et al. 2012).

Citations: landauer1961irreversibility, bennett1973logical, berut2012landauer.

## Step 8. The FANOUT boundary: before the first copy, everything is free. [FRAMEWORK]

Call FANOUT the moment information is first COPIED -- written into a record that could
in principle be read. The framework's central criterion: this copying moment, not any
mysterious collapse, is the boundary between pre-measurement and measurement (its
shadow in the external literature is the no-cloning theorem). Combine with Step 7:
before FANOUT, nothing has been written anywhere, so nothing can require erasing, so
no transformation can be charged. Pre-FANOUT transformations are thermodynamically
free -- and therefore must be reversible, because an irreversible step is precisely
one that discards a distinction, and discarding is the one thing that costs. Even the
cancelling of signed entries against each other -- which will grow up to be
interference -- is free, because cancellation pre-FANOUT erases no record: there is no
record. (Frame-relativity and grading of FANOUT are treated in
`fanout_logic_measure_correspondence_theorem_v2_2026-05-17.md` and
`dynamics_companion_fanout_unitarity_2026-05-20T1430.md`; the simple statement
suffices here.)

Status detail: Landauer / Bennett / no-cloning are ESTABLISHED; the FANOUT-boundary
framing is FRAMEWORK (proved in-house, not in the literature).

Citation: wootterszurek1982cloning.

## Step 9. Free and recordless means no step is special. [OPEN -- the central unproved step]

Aaronson's intuition: if an operation can be applied for one second, it ought to make
sense to apply it for half a second. We can now say WHY one should believe this rather
than merely find it plausible. Suppose pre-FANOUT there were a smallest permitted unit
of transformation -- a rule saying "whole steps only". Then partway through a step
there would have to be a fact of the matter about how much had been applied -- and a
fact is a distinguished mark, a record. But pre-FANOUT is precisely the regime with no
records. A minimal step size is a mark the recordless regime has nowhere to keep.
Therefore every attainable transformation should be DIVISIBLE: performable in halves,
thirds, n-ths, for every n.

Blunt honesty: this step is not yet a theorem -- ours or anyone's. Worse, there is a
standing counterexample keeping us honest: Spekkens' toy and epistricted theories are
also built on ignorance, yet their transformations form a FINITE group -- their
ignorance comes in indivisible whole bits. So "ignorance" alone does not force
divisibility; it must be shown that SELF-REFERENTIAL ignorance, arriving with the
continuous dial of Step 6 already attached, differs in kind from Spekkens' rationed
ignorance. This is the ledger's open problem P2-prime, and the Spekkens foil marks
exactly where the proof must bite (ledger W3).

Citations: aaronson2013democritus, spekkens2007toy, spekkens2016quasi.

## Step 10. A quiet companion assumption: limits of the allowed are allowed. [Closure move standard; substrate OPEN]

One more ingredient, mild-looking: if a sequence of permitted transformations
converges to some limiting transformation, no experiment could ever certify the
limit's absence -- each stage is indistinguishable from something permitted -- so
operationally the limit is permitted too. The set of attainable transformations is
therefore CLOSED. Reasonable -- but notice what it quietly leans on: talk of
"converging" presupposes that the scalars underneath form a continuum (the real
numbers) rather than, say, the rationals or the p-adics, and THAT choice is itself an
unproved layer of the programme (the ledger's Layer 1 debt; Khrennikov's p-adic
probability is the standing rival, in which no continuous dial exists at all --
Q_p is totally disconnected, no U(1)).

Citation: khrennikov1994padic.

## Step 11. Divisible + closed = a smoothly connected group. [ESTABLISHED]

Three old facts, each with a one-line moral. The Cartan--von Neumann closed subgroup
theorem: a closed set of matrices closed under multiplication and inverse is
automatically a SMOOTH object, a Lie group -- one cannot be closed and a group without
being smooth. Compact Lie groups have finitely many connected pieces. And Lagrange's
little observation: in a finite group of size m, only the identity is an m-th power --
so if an element has roots of every order (Step 9), its "which piece am I in" label
must be the identity label: divisibility forces every element into the piece
containing the identity. Conclusion: the attained transformations form a CONNECTED,
CONTINUOUS group. Every ingredient is nineteenth-to-twentieth-century mathematics; the
step is theorem-grade GIVEN Steps 9 and 10. (This is the ledger's divide-and-close
motor closing.)

Citation: lee2013smooth (textbook source for the closed subgroup theorem).

## Step 12. No state is special, so the group reaches everything: continuity of Hardy's kind. [Orbit argument ESTABLISHED; homogeneity premise FRAMEWORK]

The founding axiom -- Inside/Outside Equivalence -- says physical law cannot privilege
any particular pure state, since an embedded observer has no absolute landmark against
which to locate their own state. So the symmetry group must be able to carry any pure
state to any other: it acts TRANSITIVELY. A connected group acting transitively means:
between any two pure states there runs a continuous path of reversible
transformations. Say that in Hardy's words and it is exactly his fifth axiom -- the
one he had to POSTULATE in 2001, the one Schack's four-axiom Bayesian variant still
retains as a postulate. Here it has become a CONCLUSION, resting on the flagged steps.

Citations: hardy2001, schack2003.

## Step 13. The punchline: only one distance survives continuous motion. [ESTABLISHED -- Banach--Lamperti; the "corners are records" gloss is RHYME]

A distance between states, to mean anything, must be unchanged by the free reversible
operations -- otherwise costless, recordless motion could alter how distinguishable
two states are, and a change in distinguishability is itself a record that nothing
paid for. So the metric must be invariant under the whole connected group of Step 12.
Try the natural candidates: measure distance by adding up |differences|^p for some
power p. Picture the unit ball of each. For p = 1 it is a diamond; for p = infinity, a
box; for p = 2, a round sphere. A diamond or a box has CORNERS -- and corners are
distinguished directions, marks, exactly what the recordless regime cannot possess.
The theorem underneath the picture (Banach 1932; Lamperti 1958) says it precisely: for
every p != 2 the distance-preserving linear maps are only relabel-and-rephase --
permutations dressed with phases -- a rigid, disconnected set of moves with no
continuous path between distinct configurations. Continuous transitive motion is
flatly incompatible with every exponent except one. The sphere is the only cornerless
ball, and p = 2 is the only exponent whose symmetries can flow. Hence the L^2 metric.

Precision (recorded so nothing is oversold): A5-type continuity selects the EXPONENT,
not the field. Real L^2 passes the transformation test (SO(N) is connected and
transitive on the sphere); the field C is bought separately, by Step 6's phase
argument at the amplitude level and by local tomography at the composite level (ledger
B7). Within the bookkeeping: 2 from continuity, C from P1-type closure + composites.

Citations: banach1932operations, lamperti1958isometries.

## Step 14. Two independent roads confirm the same 2. [ESTABLISHED, modulo citation checks]

Road one, from the group directly: a connected group transitive on states, with the
phase circle of Step 6 as fibre, makes the state space complex projective space
CP^{K-1}, and such a space admits exactly ONE invariant metric up to overall scale --
the Fubini--Study metric, whose linear lift is the L^2 inner product. No choice was
available. Road two, from statistics with no groups at all: Chentsov proved that the
unique metric on classical probability distributions respecting coarse-graining is the
Fisher--Rao metric -- and in the coordinates x_k = sqrt(p_k) it IS the round L^2
metric on the sphere's positive orthant. The square root of probability is a natural
statistical coordinate even classically; Wootters showed the quantum
distinguishability distance is exactly the corresponding angle; Petz and Petz--Sudar
showed that although mixed states carry a whole family of monotone metrics, on PURE
states every member collapses to Fubini--Study. Transformation continuity SELECTS the
2; value continuity independently CONFIRMS it. What the value side can never supply is
the step from the positive orthant to the whole sphere -- the linear structure,
phases, superposition: that is entirely transformation-bought.

Citations: cencov1982statistical, rao1945information, wootters1981distance,
petz1996monotone, petzsudar1996geometries, bengtssonzyczkowski2017geometry.

---

## The honest ledger, gathered in one place

Fully load-bearing on published mathematics and physics: Steps 1, 2, 4 (the
mathematics), 7, 11, 13, 14. Proved or argued in-house but original to this programme,
hence not independently vetted: Step 3 (self-reference as the ORIGIN of negativity),
Step 8 (the FANOUT boundary), Step 12's homogeneity premise, and the physical
identifications in Steps 4--5. Genuinely OPEN, provable by no one yet: Step 9
(recordlessness forces divisibility -- the heart of the matter, with the Spekkens foil
standing guard), Step 10's substrate (why the real continuum underlies the scalars at
all), and, half-open, the closure premise inside Step 6 (mathematics trivial, physical
premise not). The chain is a genuine derivation with exactly three named gaps, each
gap a precise mathematical statement rather than a vague hope.

## Open steps, mapped to the continuity ledger

- Step 9 <-> ledger premise P2-prime (divisibility), work item W3, with the
  Spekkens/epistricted foil as the discriminating test.
- Step 10 substrate <-> ledger Layer 1 (FDP-completion + Archimedean selection;
  Khrennikov p-adic foil to be answered explicitly, especially for Vaxjo).
- Step 6 closure premise <-> phase-group instance of the P2-prime family; CANDIDATE,
  half-open.
- Step 12 homogeneity <-> Inside/Outside Equivalence; structural; the transitive-action
  orbit argument itself is theorem-grade (ledger closes A5 this way).

## Provenance note (NOT for print without permission)

The observation that the connection between self-referential paradoxes and negative
probability appears unexplored was reinforced in conversation: Samson Abramsky told
J.D.S. that he had never considered the connection. If this is to appear in the paper
(as "S. Abramsky, private communication"), his permission must be obtained first. The
companion LaTeX carries this as a commented-out footnote, disabled by default.

## Citation ledger (keys, roles, verification status)

- schack2003 -- Step 12. VERIFIED this session (arXiv + Springer DOI). Dedupe: key
  already in continuity appendix.
- hardy2001 -- Step 12. arXiv ID verified via fetched Schack reference list; e-print
  only, never journal-published. Dedupe: key already in continuity appendix.
- All remaining entries (cantor1891diagonal, goedel1931formal, turing1936computable,
  popper1950indeterminism1, popper1950indeterminism2, breuer1995selfmeasurement,
  lawvere1969diagonal, yanofsky2003universal, shannon1948communication,
  russell1908types, wigner1932quantum, dirac1942bakerian, feynman1987negative,
  abramskybrandenburger2011sheaf, spekkens2008negativity, spekkens2007toy,
  spekkens2016quasi, landauer1961irreversibility, bennett1973logical,
  berut2012landauer, wootterszurek1982cloning, aaronson2013democritus,
  khrennikov1994padic, lee2013smooth, banach1932operations, lamperti1958isometries,
  cencov1982statistical, rao1945information, wootters1981distance, petz1996monotone,
  petzsudar1996geometries, bengtssonzyczkowski2017geometry) -- sourced from model
  memory: every one carries a VERIFY-CITE flag in the RIS N1 field and must be checked
  against the publisher before the paper is finalised. spekkens2007toy additionally
  matches the entry recorded in the continuity ledger (W7), which raises confidence
  but does not discharge the flag.

*End of session document, 2026-08-04T1720.*
