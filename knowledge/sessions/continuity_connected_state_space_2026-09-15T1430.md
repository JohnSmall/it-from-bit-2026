# Session note: continuity from a connected state space

Date: 2026-09-15T1430. Session: Claude Code (Fable 5.1), `it_from_bit_fable_5_1`.
Subject: op:limit-realisability, the one arrow the reconstruction chain owes
(self-reference -> negative probability -> complex amplitudes -> reversible
continuity -> L^2 metric -> Hopf fibrations). Thinking session with a paper
patch; ledger entries proposed at the end, for the Opus session to apply.

## The question, as JS put it

JS thought the problem had been settled in an earlier conversation. A review
of the corpus (this session, earlier) found it refined, not settled: the
2026-07-04 section asks for two premises about transformations, divisibility
and closedness; the 2026-07-17 ledger and appendix decomposed the arrow into
P1 (descriptive closure), P2' (divisibility, with a stage-lattice lemma
meant to reduce it to "no records") and P3 (transitivity); the 2026-08-04
fourteen-step chain, recovered from Claude web by JS, restates the same gaps
(Step 9 divisibility open, Step 10 substrate open, Step 6 half-open). None
of the three is in the paper except the first. JS then stated the stakes:
without reversible continuity the L^2 metric is unjustified and with it the
Hopf structure, so "complex probability amplitudes imply reversible
continuity" must be shown.

## The argument

Labels are proposals; JS applies them.

### 1. What the premises can and cannot carry

**STRUCTURAL (argument).** Self-reference is a diagonal phenomenon and lives
in discrete settings; Cantor, Goedel and Turing need no continuum. Complex
amplitudes are an algebraic fact. Hardy's fifth axiom is topological. The
passage needs a topology (real scalars), closure and something that kills
the component group; the premises supply none directly.

**STRUCTURAL (countermodel, corrected from the previous message).** Qubit
stabiliser mechanics has complex amplitudes and is contextual (Mermin--Peres
lives inside it), its reversible transformations form a finite group (the
Clifford group), and Hardy A5 fails in it. Spekkens's toy theory is the real
version, credences rationed by the knowledge-balance principle. I first read
the foil as showing that the missing premise is a transformation (the T
gate, the fourth root of the sign flip, which the Clifford group lacks: the
phase gate S has no Clifford square root). That is true but is a symptom.
Both foils have FINITELY MANY PURE STATES, with outcome probabilities in
{0, 1/2, 1}. They do not have "complex probability amplitudes" in the
framework's sense; they have a finite set of them. What they lack is a
continuum of values, and once that is seen the divisibility premise is
unnecessary.

### 2. The proposition that does the work

**STRUCTURAL (textbook; now prop:connected-transitive in the paper).** Let
the pure states form a connected space P and let the reversible
transformations form a closed group G acting transitively on P. Closedness
in the compact automorphism group of the state body makes G a compact Lie
group with finitely many components (Cartan; Broecker--tom Dieck), so G_0 is
a closed normal subgroup of finite index and is path-connected. G_0-orbits
are compact, hence closed; the cosets of G_0 permute them transitively
(G_0 g x = g G_0 x by normality, and G is transitive), so there are finitely
many; a finite partition of P into closed sets is a partition into open
sets; P connected gives one orbit, so G_0 is transitive; a path in G_0 from
the identity to the g carrying x to y is a continuous reversible
transformation from x to y. That is Hardy's fifth axiom. No n-th roots, no
dyadic tower, no stage lattice. Divisibility then FOLLOWS (the exponential
map of a compact connected Lie group is surjective), so it is a consequence,
not a route.

### 3. What "complex amplitudes imply continuity" means, exactly

**STRUCTURAL.** With the Born rule the pure states are the unit vectors of
C^K modulo phase, CP^(K-1), connected for K >= 2 -- provided every unit
vector is a state. So the implication holds in this form: if the amplitudes
fill their continuum, no pure state is privileged, and the available
transformations are closed under limits, then reversible continuity
follows; then Banach--Lamperti gives the L^2 metric and the Hopf fibrations
stand. Real amplitudes would do for this step (RP^(K-1) is connected); the
complex field is bought separately, as the August chain already says.

### 4. The three premises, and their status

- **Value continuum (OPEN; the one genuine input).** Every real number in
  [0,1] is an attainable credence, so the amplitudes fill C^K. This is the
  07-17 appendix's op:quantised, "is self-referential ignorance quantised or
  divisible?", not its op:stage-lattice. Framework-native candidate route: a
  rationing rule (a minimal unit of self-ignorance) is a stable, copyable
  description of the observer's own epistemic state, a record predating any
  FANOUT, which the third face excludes. Not a proof. FAIL test, of the kind
  that served the Koide phase: an argument whose premises are all satisfied
  by Spekkens's toy theory (or the stabiliser fragment) cannot prove it.
- **Closure (a stance, now stated as one).** The operational completion: a
  limit no experiment can certify absent is admitted. Needed, since a
  transitive group that is not closed can be totally disconnected in the
  subspace topology (R with the discrete topology acts transitively on R).
  The 07-04 text derives it from "the description would refer to a
  transformation that does not exist"; that is not a contradiction, since a
  computable Cauchy sequence of rationals can have a non-computable limit
  (Specker): describable limits need not be realisable. The same founding
  premise admits a constructive reading; the framework takes the operational
  one, Hardy's own; the paper now says so in one sentence.
- **Homogeneity (FRAMEWORK, as before).** No privileged pure state, from
  inside/outside equivalence; a proper closed invariant set of pure states
  would define a superselection observable, a record. Already the paper's
  P3 argument.

### 5. What is retired, and why the earlier arguments failed

- **Step 6 "package deal"** (2026-08-04): analytic continuation defines
  (-1)^t for every t; it does not make each an available operation; the
  stabiliser world buys the flip and its square root and stops. Definability
  is not availability. Retired as an argument for divisibility; harmless as
  a remark about values.
- **Step 9 / stage-lattice lemma** (2026-07-17, 2026-08-04): "no
  distinguished step" is a negation, divisibility an existence claim; the
  lemma's "record" would have to condemn a finite Clifford group while
  acquitting the finite dimension K and the state-body shape. Retired as
  unnecessary: divisibility follows from the conclusion.
- **thm:conditional / prop:divisible-closed**: still true, still in the
  paper; no longer the load-bearing route. The Lagrange paragraph's closing
  claim that "the whole question compresses to those two premises" was
  false as of today and is replaced.

## What was changed in the paper

`scripts/patch_continuity_connected_state_space_2026-09-15T1430.py`, one
run (two invocations: the first stopped at the L^2 file's re-fill guard,
the script was made to skip already-patched files and to leave that one
paragraph un-refilled, and the second invocation completed). Backups
`.2026-09-15T1430.bak` on all four files.

- `paper1/continuity_section_2026-07-04.tex`: the opening now says "one
  premise about values"; after the Lagrange paragraph, prop:connected-
  transitive with proof and the paragraph on the two foils; the subsection
  "The two premises, and what they mean" is now "The premises, and what
  they mean", names the three premises, retires divisibility, keeps the
  limit-realisability text and adds the closedness-as-stance sentence;
  op:limit-realisability restated as "The value continuum from
  self-reference" (label kept; cross-referenced from four files) with the
  three premises, the one open, the candidate route, PASS and FAIL.
- `paper1/L2_metric_global_phase_section_2026_06_07.tex`,
  `paper1/summary_section_2026-07-07.tex`,
  `paper1/derivation_of_the_quantum_postulates.tex`: the sentences calling
  the problem "two premises, divisibility and closedness" re-pointed to the
  one open premise. (The postulates file's re-fill joined the
  `\paragraph{Postulate 1 ...}` command to its text on one line; no effect on
  the output.)

Labels and keys used were checked to exist: prop:divisible-closed,
prop:f1-dictionary, sec:fanout-boundary, sec:self-reference;
spekkens2007toy, broeckertomdieck1985compact. Not built (JS's rule); not
committed.

Atticked at JS's instruction, same session, renamed in place in
`knowledge/project-docs/` per the house rule (nothing deleted), each with a
one-line SUPERSEDED header pointing here, and the project-docs INDEX updated
(the 07-17 line rewritten; the two 08-04 files, which post-date the export,
listed under "Added after the export" together with the 08-04 markdown
record, which is kept as history):

- `attic_appendix_continuity_open_problems_2026-07-17.tex.superseded`
  (tracked; git mv)
- `attic_section_selfref_to_l2_chain_2026-08-04T1720.tex.superseded` (new)
- `attic_refs_selfref_to_l2_chain_2026-08-04.bib.superseded` (new; never
  imported)

`knowledge/open_problems.md` lines 11 and 20 still name the old path of the
07-17 appendix in its list of formal open-problem documents; that file is
append-only, so the path is left for the Opus session to supersede with the
dated entry proposed below rather than edited here.

## Second edit, T1525: the fossil subsection in what_is_a_quantum_state.tex

JS: the subsection "Reversible continuity" (sec:reversible-continuity, lines
546--560) predates sec:continuity and needs removing or re-pointing. It
contradicted the section twice: the diagonal "fills the gaps in Q to give R
and hence continuity" (sec:continuity says the diagonal presupposes the
completed line), and "reversible continuity is a consequence of
self-reference" (now conditional on one open premise). Its label is
referenced from main.tex's introduction and from an earlier sentence in the
same file, so it was rewritten as a pointer, label kept:
`scripts/patch_reversible_continuity_fossil_2026-09-15T1525.py`, backups
`.2026-09-15T1525.bak` on both files.

- The subsection now states the recordless reversible regime, Hardy's
  axiom and what it affords (the TRUE/FALSE superposition), sends the
  question to sec:continuity, corrects the diagonal reading, and states the
  honest status with op:limit-realisability.
- The earlier sentence promised to "expand on" quaternionic and octonionic
  amplitudes "when discussing reversible continuity", which the subsection
  never did; it now says continuity fixes the metric and not the field and
  points to sec:continuity.
- main.tex's introduction said "this forces reversible continuity"; it now
  says the paper takes it up and that sec:continuity reduces it to a single
  open premise about values. Bare \ref kept to match that paragraph (its
  style pass is a separate todo of the other session's).

Not built; not committed.

## Third edit, T1540: the premise declared once; the statistical route to L^2

JS asked whether the complex values, reached by analytic continuation of the
logarithm, imply the value continuum. Answer, STRUCTURAL: they consume it.
Analytic continuation is an operation on a function on a connected domain;
its value at a negative entry is unique only because credences range over
such a domain. With finitely many attainable credences (the stabiliser
fragment's {0, 1/2, 1}; the toy theory), "-log p" would be one of infinitely
many rules agreeing on the attained points and its extension a convention.
So the framework's one continuity input is made at the Shannon step and is
consumed three times: at the continuation (complex amplitudes), at
prop:connected-transitive (reversible continuity), and at Cencov (the
simplex as a manifold). It is also what the corpus called Layer 1, "why R
before C": the same premise, with Khrennikov's p-adics as its foil in the
way the epistricted theories are.

Caution recorded: the continuation by itself yields only the sign as a phase
(e^{-s} with s = -log|p| - i pi is just the signed entry p). The continuous
phase theta in the paper's S = -ln|p| - i theta is a further appeal to the
same premise (ignorance in all degrees), and the square-root magnitude comes
from the Born rule or the Fisher--Rao coordinate, not from the continuation.
Not changed in the paper beyond the declared-premise sentence; worth JS's
eye when sec:complex-amplitudes is next revised.

JS then asked whether the step to the L^2 metric can be justified. Yes,
conditionally on that one declared premise, by two routes sharing only it:
(a) reversible continuity and Banach--Lamperti (value continuum + closure +
homogeneity); (b) Cencov's theorem plus a lemma, STRUCTURAL: the
Fubini--Study metric is the only metric on CP^(K-1) restricting to
Fisher--Rao on the positive real orthant of every orthonormal basis (proof:
every tangent direction phi at psi lies along the real curve
cos t psi + sin t phi in the orthant of a basis containing psi and phi; i phi
is reached by the basis containing i phi). This is Wootters's 1981
statistical distance in another guise. Route (b) needs coarse-graining
invariance and the equal standing of bases, not closure or a transformation
group. Hardy's K = N^2 counting is not a premise-independent third leg: it
uses A5 to exclude the classical r = 1 and again for the Bloch ball; the L^2
section's own wording ("two roads from continuity") was already right, the
postulates section's "independent route" was not.

`scripts/patch_value_continuum_declared_cencov_2026-09-15T1540.py`, backups
`.2026-09-15T1540.bak` on four files:
- `what_is_a_quantum_state.tex`: the declared premise after the continuation
  sentence (credences take every value in [0,1]; not rationed as in the
  epistricted theories, spekkens2007toy cited), why the continuation needs
  it, where it is consumed, op:limit-realisability named.
- `continuity_section_2026-07-04.tex`: op:limit-realisability gains the
  sentence that the premise is the Shannon step's, consumed three times.
- `L2_metric_global_phase_section_2026_06_07.tex`: status paragraph updated;
  Hardy's-route paragraph says both roads start from continuity and a third
  starts earlier; new sec:cencov-route with Cencov (cited to
  bengtsson2006geometry, the one source for it in the bibliography),
  lem:every-basis with proof, and the two-legs status paragraph.
- `derivation_of_the_quantum_postulates.tex`: "an independent route" ->
  "a second route from the same continuity premise", the statistical route
  named; "the independent isometry and counting arguments" -> "the isometry
  and counting arguments and ... the statistical route".
Not built; not committed.

Additional ledger proposals from this edit:
- results_ledger, **STRUCTURAL**: the complex amplitudes reached by analytic
  continuation consume the value continuum rather than imply it; the
  framework's one continuity input is declared at the Shannon step and
  consumed at the continuation, at prop:connected-transitive and at Cencov;
  it is the corpus's Layer 1 under another name.
- results_ledger, **STRUCTURAL**: the every-basis lemma (lem:every-basis);
  with Cencov's theorem it gives the L^2 metric from the value continuum,
  coarse-graining invariance and the equal standing of bases, with no
  transformation group.
- results_ledger, **CANDIDATE**: the L^2 metric, and with it the Hopf
  fibrations and everything downstream, are derived conditionally on the
  one declared premise by two routes that share only it; their status is
  "a premise every physicist grants, not yet derived from self-reference".
- invalid_routes: treating Hardy's K = N^2 counting as a route to the
  quadratic norm independent of the continuity premise (it uses A5 twice).
- References for the other session to verify and batch: Cencov 1982 (AMS
  translation of the 1972 Russian, "Statistical Decision Rules and Optimal
  Inference"); Wootters 1981, Phys. Rev. D 23, 357; optionally Campbell 1986
  or Ay--Jost--Le--Schwachhoefer 2015 for the general form of Cencov's
  theorem. The patch cites only bengtsson2006geometry, already in the bib.

## Proposed ledger entries

### results_ledger.md, dated 2026-09-15

- **STRUCTURAL** Continuity from a connected state space: if the pure
  states form a connected space and the reversible transformations form a
  closed group acting transitively on them, the identity component is
  already transitive and Hardy's fifth axiom holds (prop:connected-
  transitive). Divisibility of the group is a consequence, not a premise.
  Textbook mathematics (Cartan, finiteness of components, orbits of a
  normal subgroup); the framework's contribution is only its use.
- **STRUCTURAL** The two standing foils, qubit stabiliser mechanics and
  Spekkens's toy theory, have finitely many pure states with outcome
  probabilities in {0, 1/2, 1} and finite transformation groups; Hardy A5
  fails in both; both have complex (resp. real) amplitudes and the first is
  contextual. So "complex amplitudes imply continuity" is false unless the
  amplitudes are taken to fill their continuum, and the missing premise is
  one of values, not of transformations. The phase gate's lack of a
  Clifford square root is a symptom.
- **CANDIDATE** The framework's reading of the one open premise: self-
  referential ignorance is not rationed (every credence in [0,1] is
  attainable), because a rationing rule would be a copyable description of
  the observer's own epistemic state, a record before any FANOUT.
- Recorded, not labelled: closedness of the transformation group is the
  framework's adopted operational stance, not a theorem; the constructive
  reading of the founding premise (Specker) is the road not taken, and the
  paper now says so.

### invalid_routes.md, dated 2026-09-15

- Deriving divisibility of the transformation group from "no distinguished
  step" (07-04 candidate route; 07-17 P2' and op:stage-lattice; 08-04
  Step 9): retired as unnecessary rather than refuted -- divisibility
  follows from continuity, so no derivation of it is needed; and as an
  argument it never distinguished a finite Clifford group (to be excluded)
  from the finite dimension K (to be kept).
- The "package deal" of the 08-04 Step 6 (analytic continuation of the
  logarithm makes every phase available): conflates definability with
  availability; the stabiliser fragment defines all phases and uses four.
  Not an argument for continuity.
- Any argument for continuity whose premises are all satisfied by
  Spekkens's toy theory or by the stabiliser fragment of quantum theory:
  fails before it is checked, both being consistent with finitely many
  pure states.

### open_problems.md, dated 2026-09-15

- **OPEN** op:limit-realisability, restated: derive from self-referential
  closure that the embedded observer's credences fill [0,1], so that the
  pure states are all of CP^(K-1). PASS: a derivation of the connected
  state space from premises the toy theory does not satisfy. FAIL: every
  premise holds in the toy theory or the stabiliser fragment. Supersedes the
  07-04 statement (two premises about transformations) and the 07-17
  op:stage-lattice; op:fdp of 07-17 becomes the stance recorded above
  rather than a problem; op:quantised of 07-17 is this problem in its
  framework form; op:transitivity of 07-17 stands as the homogeneity
  argument to be written out.
- The 07-17 appendix (`appendix_continuity_open_problems_2026-07-17.tex`)
  and the 08-04 chain (`section_selfref_to_l2_chain_2026-08-04T1720.tex`)
  in project-docs are partly superseded by this: their divisibility
  material should not be spliced as it stands; their Specker, dyadic-tower
  and value-continuity material remains good. JS's editorial call whether
  either is spliced, with the other session doing the splice.

## References the other session may add (verified data needed first)

- Specker 1949, "Nicht konstruktiv beweisbare Saetze der Analysis",
  J. Symbolic Logic 14, 145--158, for the computable sequence with a
  non-computable limit; the paper's new sentence states the fact without
  a citation.
- Gottesman 1998, "The Heisenberg representation of quantum computers",
  arXiv:quant-ph/9807006, for the stabiliser fragment; the paper names the
  fragment without a citation. Spekkens 2016 (quasi-quantisation,
  epistricted theories) likewise optional; the toy theory is cited.
All from memory: VERIFY before batching.

## Not done

- No computation: the propositions are textbook and the countermodel facts
  standard. A seed-locked check that S has no Clifford square root and that
  arbitrary single-qubit rotations with CNOT generate the unitary group was
  offered and not needed for the paper's text.
- The homogeneity argument (sector = record) is still asserted, not proved
  (07-17 op:transitivity).
- The value-continuum premise: the candidate route is stated; no proof
  attempted.
