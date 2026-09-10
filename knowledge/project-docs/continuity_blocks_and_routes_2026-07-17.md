# Blocks and routes: self-referential ignorance ⟹ Hardy A5 — the continuity ledger

**Session document, 2026-07-17.** Upgrades `continuity_limit_realisability_2026-07-04.md` §3
(Routes A and B), respects and extends its dead-route box (§4), and decomposes the owed arrow
into named premises with named blocks. Status flags as in the corpus: RECORDED (cited by doc),
NEW-TODAY (2026-07-17), OWED, FOIL (a named counterexample the paper must answer),
VERIFY (memory-based citation to check at drafting).

---

## 0. Thesis of the day

The owed arrow — *self-referential ignorance ⟹ Hardy's continuity axiom* — is not one arrow.
It is **two completions driven by one two-step motor**:

- **Motor, step 1 — divide:** no records ⟹ no distinguished step size ⟹ every available
  transformation (in particular the anti-event −1) is realisable in n stages for every n
  (divisibility).
- **Motor, step 2 — close:** self-referential ignorance ⟹ no infinite-precision
  self-specification ⟹ the theory's objects are finite-precision description-classes ⟹ the
  theory's spaces are completions (closed under described Cauchy limits).

Run the motor on the scalars and you get **ℝ** (order-completion; supertasks select the
Archimedean fork) and **ℂ/U(1)** (root-completion; the anti-event demands √−1). Run it on the
transformation group and you get the July-4 closedness lemma's premises **exactly** —
divisible + closed — hence a compact connected Lie group, hence Hardy A5.

Slogan form: **continuity is what "no oracles" looks like in analysis.** The only known
discontinuous objects at every layer — non-measurable additive functions, wild automorphisms
of 𝕋 and ℂ, non-computable maps, unrepresentable limits — are choice-monsters or oracles: things
with no finite description. A theory whose objects are descriptions cannot contain them. Hardy's
axiom is the topological shadow of the founding premise.

Everything else in the chain is now a theorem or a citation. The residue is three named premises
(§5) — of which one is already a face of the five-way regime — plus the honesty blocks of §3.

---

## 1. What "continuity" means — the ladder

The threads in play conflate at least six distinct notions. Sorting them is half the battle.

1. **Continuity of a map** (ε–δ, topological): preimages of opens are open. A property of a
   *map*, relative to chosen topologies. Cheap in ℝ (Weierstrass monsters are continuous).
2. **Connectedness of a space**: no partition into two nonempty clopen pieces.
   **Path-connectedness**: any two points joined by a continuous path. A property of a *space*.
3. **Cauchy completeness** (uniform): every Cauchy sequence/filter converges. **Completeness
   does NOT imply connectedness**: ℚ_p and ℤ_p are complete and totally disconnected.
4. **Order-completeness + Archimedean** (Dedekind's *Stetigkeit*, the 19th-century meaning of
   "continuity of the line"): every bounded set has a supremum; no infinitesimals. For ordered
   fields this is categorical — it pins **ℝ uniquely** — and it is equivalent to connectedness
   of the order topology. Cauchy-complete + Archimedean ordered field ⟹ ℝ.
5. **Local compactness**: the ambient enabler — Cartan's closed-subgroup theorem, Baire, Haar
   measure all live here. Pontryagin/Weil: the locally compact non-discrete fields are ℝ, ℂ,
   finite extensions of ℚ_p, and 𝔽_q((t)); the *connected* ones are ℝ and ℂ alone (ℍ if skew
   fields are admitted). VERIFY exact statement at drafting.
6. **Analyticity / rigidity** (the complex notion): holomorphy ⟹ identity theorem ⟹ a germ
   determines the function on a **connected** domain; monodromy on non-simply-connected domains
   generates winding integers. Real continuity says *no gaps*; complex analyticity says
   *no freedom*.

**The group-level collapse (Hilbert's 5th problem).** For groups the ladder telescopes:
Gleason–Montgomery–Zippin–Yamabe — a locally compact group with **no small subgroups** (NSS:
some neighbourhood of the identity contains no nontrivial subgroup) is a Lie group; continuity
self-upgrades to real-analyticity. And NSS is the group-level face of the Archimedean fork:
ℤ_p *fails* NSS (the subgroups pⁿℤ_p shrink to the identity); real matrix groups satisfy it.
**Small subgroups = p-adic signature; NSS = Archimedean signature.** The Ostrowski fork of §6
reappears at the group level, unprompted.

**Foil box (keep these straight; referee-bait otherwise).**
- Complete ≠ connected: ℚ_p (also: (ℚ_p,+) is divisible, complete, totally disconnected — so
  "divisible + complete" *without a compact matrix ambient* is not enough; the July lemma's
  ambient Sym(K) ⊂ GL(K,ℝ) is load-bearing).
- Uncountable ≠ connected: Cantor set (RECORDED, July dead-route box).
- Connected ≠ path-connected: the **solenoid** — a compact connected abelian group with a dense
  path-component; A5's "continuous transformation between any two pure states" would fail there.
  Only the Lie/matrix structure (Cartan) upgrades connected to path-connected. Insurance in the
  abelian case: a compact abelian group is connected **iff** divisible (Hofmann–Morris, VERIFY).
- Countable + closed-in-compact ⟹ finite (Baire; RECORDED July corollary).

**What each thread touches (audit table).**

| Thread | Provides | Consumes |
|---|---|---|
| Superposition-represents-self-reference | motivation; fixed points on amplitude side | a scalar field with the fixed points *available* — see FOIL: superposition exists over finite fields (§9, Box 2) |
| Thomson lamp / supertasks | **Archimedean selection** (accumulation possible → ℝ at the Ostrowski fork, §6) | completeness (terminal point must *exist*) |
| Cantor diagonal | ignorance-of-the-completion: internal listings never exhaust; with Specker (§6), the completion provably contains non-computable points | a completed line for its output to live in (RECORDED dead-route box: it does not build the completion) |
| Shannon / log / analytic continuation | root-completion demand (√−1); rigidity-up-to-winding; winding integer | **connectedness** (identity theorem, monodromy need connected domains) — it is downstream of A5-type continuity, not upstream |
| Halting/Lawvere ignorance | the Finite Description Principle (P1): completion + monster-ban | Church–Turing (already committed: 2023 poster; Popper 1950 pedigree in project files) |

---

## 2. The two-layer audit — where the petitio hides

**Layer 2 (group):** the July-4 lemma runs inside Sym(K), K a compact convex body in ℝᴷ. That
ambient *presupposes real scalars* — completeness, local compactness, Archimedean order all
imported in the phrase "compact convex set." NEW-TODAY: this is the deepest circularity risk in
the current record. The lemma is fine; its *ambient* is a debt.

**Layer 1 (scalars):** why is the probability scalar field ℝ rather than ℚ, the computable
reals, a hyperreal field, or ℚ_p? Note that Hardy's A1 itself assumes relative frequencies
*tend to definite limits* — a von Mises-style limit-realisability import. And Kolmogorov's
axiom V (countable additivity) is literally called the **continuity axiom** — the one de Finetti
famously rejected as non-operational, insisting on finite additivity. So the reconstruction
literature's two real-number imports (A1's limiting frequencies, A5's continuous group) have a
common root, and the framework's P1 (below) discharges both at once — while taking a definite
side in the de Finetti debate: self-reference forces the completion de Finetti resisted.

The owed arrow therefore splits: **Layer 1** — derive ℝ (and ℂ) as the scalar completion
(§6, §4); **Layer 2** — derive closedness + divisibility + transitivity of the group over those
scalars (§5). The May record treated it as one arrow; it is two, and they use the same motor.

---

## 3. The blocks (B1–B10)

**B1. The FDP is a semantic principle, not yet a theorem.** The completion move (P1, §5) says:
theory-objects are finite-precision description-classes, and the space of such classes is
complete *by the universal property of completion*. A referee can object that completeness has
been defined in. Mitigation: state FDP as a named axiom grounded in Church–Turing/Lawvere (an
infinite-precision self-specifier would decide its own halting; RECORDED, 2023 poster), and show
it has independent nontrivial consequences (the three automatic-continuity faces, §7) — a
principle with theorem-weight output is not vacuous. Residual: honest.

**B2. Divisibility (P2′) is still OWED** — and the physical group is *finitely generated*.
Circuits generate countable, non-divisible groups (⟨one rotation⟩ ≅ ℤ). Divisibility can only
hold of the *availability structure* (every transformation realisable in n equal available
stages), not of the generated group; and closures of non-divisible groups can be anything from
U(1) (irrational rotation — good) to ℤ/3 (Clifford-like — fatal). The sharp physical question:
**why does nature's pre-FANOUT gate set generate densely rather than close finitely?** The
framework's own answer-shape: a finite closure is a distinguished finite structure = preferred-
basis-like = record-like = post-FANOUT (the 4⇔5 argument applied to the closure). The
Gottesman–Knill resonance — finite-closure gate sets (Clifford) are exactly the classically
simulable subtheories; universality = dense generation = connected closure — is suggestive but
flagged HEURISTIC. New anchor for P2′ in §4: the anti-event's n-th stages.

**B3. Transitivity is owed and was hidden.** The May 4⇔5 converse ("cannot be pinned to
permutations ⟹ homogeneous") gestures; A5 needs the identity component *transitive on pure
states*. NEW-TODAY discharge route: **a superselection sector is a pre-existing record.** If two
pure states lie on different orbits, the orbit label is a basis-free, measurement-free, absolute
distinguished fact — a classical observable commuting with everything — i.e. a record predating
FANOUT. "No classical record exists" (face 3 of the five-way regime, RECORDED May doc) therefore
already contains no-superselection, i.e. transitivity. Needs writing as an orbit argument
(orbits of a compact group are closed; a proper closed invariant distinguished set of pure
states = describable absolute = record). Status: sketched, presentable.

**B4. Layer-1 circularity (the ambient-ℝ debt).** As §2. Discharged only if the scalar story
(§6) is written as a *prior* section: FDP-completion of frequency ratios + Archimedean
selection. Until then every Layer-2 result is conditional on real scalars, and Hardy's A1 has
quietly done the work. The Khrennikov foil (p-adic probability: completions exist in which the
framework's phase cannot — ℚ_p is totally disconnected, no continuous interpolating phase, no
U(1)) must be answered explicitly, especially for Växjö.

**B5. Superposition ⇏ continuity.** FOIL: Schumacher–Westmoreland modal quantum theory —
superposition over finite fields, no continuity (and no probabilities: only modalities). FOIL:
Spekkens toy theory / epistricted theories — *ignorance-based, discrete*, one-bit knowledge
balance, transformation group finite (S₄ ≅ the stabilizer octahedron's rotations for one toy
bit). These are the strongest counterexample-pressure on the whole programme: discrete epistemic
theories exist. The load-bearing difference must be located, and it is **P2′**: their groups are
finite, hence non-divisible — their ignorance is integer-quantised (know one quadrature, lose
one bit), while pre-record self-referential ignorance is divisible (continuous phase). See Box 2
of §9, including the Chaitin-Ω sub-question.

**B6. The Shannon/log thread points the wrong way for A5.** Analytic continuation *consumes*
connectedness: the identity theorem and the monodromy theorem are statements about connected
(and simply connected) domains. The thread cannot found continuity; repositioned in §8 it
supplies the root-completion demand, rigidity-up-to-winding, and the winding integer. Additional
circularity inside it: Shannon's uniqueness axioms (and Faddeev's weakening) include a
*continuity axiom for H* — dischargeable, because the grouping axiom is a Cauchy functional
equation and **measurable solutions of Cauchy's equation are linear** (Fréchet–Sierpiński–
Banach); the non-continuous solutions are Hamel/AC monsters, banned by FDP. So entropy-
continuity comes from describability, not assumption — Route B in miniature.

**B7. Hardy's fine print.** A1 imports limiting frequencies (see §2); A2 ("simplicity") is a
minimality choice-principle referees dislike; A3 (subspaces) and A4 (composites, local
tomography) remain the RECORDED caveat — A4 claimed derived from inside/outside equivalence
(RECORDED, Pure_states doc line 87), A3 unaddressed; K per system is *finite* (Cartan and the
whole Lie apparatus need finite dimension — ∞-dim automatic continuity is a genuinely harder
world, out of scope; FDP suggests finite distinguishability per FANOUT as the physical ground).
Also: decide the reconstruction target — Hardy 2001's A5, Masanes–Müller 2011's "continuous
reversible dynamics", or CDP's purification framework — since the derived premise-set should be
matched to a specific published axiom-set for the citation to do its work.

**B8. Compact-but-not-Lie escapes.** Solenoids (connected, not path-connected) and profinite
groups would wreck A5; both are killed only by the matrix ambient (Cartan) — which is B4's debt.
Partial insurance independent of matrices: compact abelian divisible ⟹ connected
(Hofmann–Morris, VERIFY). Keep visible so the dependence is honest.

**B9. The epistemic-subject objection.** P1-completion completes the *description space*. An
ontic reader will say the physical group might "really" be the ragged dense G₀, with closure a
representational artefact. Stance answer: the framework is ignorance-based by construction
(QBist-adjacent); the description space *is* the subject matter. Sharper answer: G₀ and its
closure are operationally indistinguishable (density), and the closure is the unique
monster-free representative of the operational equivalence class; a Cauchy class *is*
finite-precision-specifiable at every precision, which is all FDP ever meant by "object."

**B10. Choice bookkeeping (DC vs AC).** The constructions used (Cauchy sequences, closure of
divisible via sequential compactness, supertask arguments) need **dependent choice** only; the
discontinuous monsters need non-measurable sets from full AC. Solovay/Shelah: in ZF+DC models
where all sets are measurable/Baire, automatic continuity is a *theorem*. So: **probability's
continuity lives in the gap between DC and AC** — physics keeps DC (sequences, supertasks) and
self-reference (via FDP) forfeits the AC-monsters. Mark choice usage explicitly in proofs or a
referee will.

---

## 4. The dyadic-tower construction (NEW-TODAY centrepiece)

Apply the motor to the single primitive **−1** (the anti-event, RECORDED as the source of
negative probability):

1. **Divide.** An un-happening with no distinguished step size must have an n-th stage for
   every n: −1 needs n-th roots. In ℝ it has none even for n = 2 — **√−1 is half an anti-event**;
   this, not calculational convenience, is why the scalars leave ℝ. The *minimal* divisible
   group containing an element of order 2 is its injective hull: the **Prüfer group ℤ(2^∞)** —
   exactly the 2ⁿ-th roots of unity, i.e. **the Thomson lamp's dyadic switching schedule read as
   phases**. The lamp's halvings 1/2, 1/4, 1/8, … and the anti-event's stage-tower are the same
   dyadic tower.
2. **Close.** ℤ(2^∞) is dense in the circle; its closure is **U(1)**.

So **U(1) = closure(divisible hull(−1))**: the phase group is precisely the two owed premises
(divisibility, closedness) made flesh, applied to the anti-event. The imaginary unit i is the
tower's 4th root; the ±i ambiguity (Galois-indistinguishable) is the winding sense — the branch
choice of log(−1) = ±iπ — the anti-event's rotation direction. Downstream, U(1)-invariance gives
the Born rule by the RECORDED corpus derivation, and Wigner's unitary/antiunitary dichotomy is
the describable remnant of ℂ's field symmetry (of ℂ's 2^𝔠 wild field automorphisms under AC,
exactly two are describable/continuous: identity and conjugation).

One level up, the same two steps applied to the available transformation set are *literally the
premise-set of the July-4 lemma* (divisible + closed in compact ⟹ connected Lie). One motor,
two layers. And at the scalar layer: ℝ is the **order-completion** (no gaps — supertasks,
limits), ℂ the **root-completion** (no missing roots — anti-events, phases); U(1) is their
intersection. *Quantum theory is what probability becomes when its scalars are completed in both
senses, and self-referential ignorance is why both completions are forced.*

---

## 5. The assembled proof skeleton (Layer 2)

Premises, each with grounding and status:

- **P1 (Finite Description Principle / no-oracle closure).** The theory's transformation object
  is the closure Ḡ = cl(G₀) of the available set in Sym(K) — because states and transformations
  are finite-precision description-classes (Church–Turing/Lawvere: infinite-precision
  self-specification would solve the specifier's own halting problem; RECORDED 2023 poster;
  Popper 1950 as classical pedigree, project PDFs). Completion is then the universal-property
  theorem, not a physical assumption. Status: sharply posed; the semantic step is B1.
  Note: on a compact Hausdorff ambient the uniformity is *unique*, so "Cauchy" is unambiguous —
  one more service the compact body performs, and one more debt of B4.
- **P2′ (No distinguished step / divisibility of availability).** Every available transformation
  is realisable in n equal available stages, for every n; records are what discretise, and
  pre-FANOUT there are none. Grounding: the anti-event tower of §4; contrapositive of "FANOUT
  discretises the group" (RECORDED May doc). Status: OWED (B2), now with an anchor.
- **P3 (No superselection).** = face 3 of the five-way regime ("no classical record"), via
  *sector = pre-existing record* (B3). Status: internal discharge, needs writing.

**Chain.** P2′ ⟹ G₀ divisible-as-availability ⟹ (sequential compactness; DC only) Ḡ divisible
[closure of a divisible set in a compact metrizable group is divisible — proved by
subconvergence of n-th roots]. P1 ⟹ Ḡ closed. July-4 lemma (Cartan + Lagrange-on-π₀) ⟹ Ḡ is a
compact **connected** Lie group. P3 ⟹ Ḡ transitive on pure states; connected ⟹ Ḡ = Ḡ₀, so the
transitive action is by the identity component ⟹ **a continuous reversible path between any two
pure states: Hardy A5.** Hardy 2001 then does everything downstream as a citation, per the
RECORDED strategy.

Weakened fallback if full P2′ resists derivation: **(No Minimal Step)** — the identity is not
isolated in G₀ (a gap around "do nothing" would be a smallest-detectable-change quantum, a
self-clock, a record). This alone gives Ḡ non-discrete, hence dim Ḡ ≥ 1 and a nontrivial
identity component — continuous paths *exist* — but leaves π₀ alive, so A5 holds only within
path-components. Full A5 needs full P2′ (or divisibility of Ḡ by another route). Record the gap
honestly.

---

## 6. Layer 1: the scalar derivation (Ostrowski fork, Accumulation Lemma, Specker bridge)

**FDP at the scalar layer.** Probability values enter as frequency ratios — finite records of
finite runs: rationals, refined without bound but never completed by any internal agent. FDP
makes the probability scalar the *completion* of ℚ. But completions of ℚ are classified —
**Ostrowski's theorem**: every nontrivial absolute value on ℚ is the real one or a p-adic one.
The fork is real: Khrennikov's programme lives on the other tine. Why the Archimedean tine?

**Meaning-of-frequency argument (primary).** Frequency-closeness is operational closeness:
|f₁ − f₂| small = proportionally few discordant trials — the order/counting uniformity. p-adic
closeness (agreement of counts mod pⁿ) has no operational meaning for frequencies. The
uniformity is fixed by what frequency *means*, and it is the order uniformity: Archimedean.

**Accumulation Lemma (NEW-TODAY, independent physical selector).** The lamp's schedule needs
|2⁻ⁿ| → 0 (switching times tₙ = 1 − 2⁻ⁿ must accumulate). Check every completion of ℚ and every
ordered-field extension: (i) real absolute value: 2⁻ⁿ → 0 ✓; (ii) ℚ_p, p odd: |2⁻ⁿ|_p = 1 for
all n — never accumulates; (iii) ℚ₂: |2⁻ⁿ|₂ = 2ⁿ → ∞ — diverges; (iv) any non-Archimedean
ordered field: an infinitesimal ε has 0 < ε < 2⁻ⁿ for all n, so 2⁻ⁿ ↛ 0 — the lamp cannot even
accumulate. **The supertask's possibility of accumulation selects the Archimedean class; adding
Cauchy completeness (P1) then pins ℝ categorically** (the unique complete Archimedean ordered
field). This cashes the supertask instinct exactly: supertasks don't merely *need* the
completion — **they perform the Ostrowski selection.** (Footnote foil: a nonstandard analyst
completes the lamp internally at a hyperfinite stage N — but that changes the task's order type
from ω; the physical task is ω-indexed. Hamkins-adjacent; see Box 3.)

Division of labour now clean: **Archimedean** (shared by ℚ and ℝ — the textbook lamp's limit
point 1 is rational, RECORDED July §5(i)) = supertasks *can* accumulate; **completeness** (ℝ
only) = every supertask's terminal point *exists*. Which supertasks need it? —

**The Specker bridge (NEW-TODAY; the jewel gets its mathematical anchor).** Specker (1949):
there is a computable, monotone, bounded sequence of rationals whose limit is not computable —
canonically σ = Σ_{n∈K} 2⁻ⁿ, K the halting set. This is **the Thomson lamp arithmetised**: a
dyadic supertask whose terminal value encodes halting information. It is the exact formal
witness for Route A's premise sentence ("a describable Cauchy sequence whose limit the internal
agent cannot realise"). Consequences: (i) the July dead-route box stands — the diagonal builds
no completion — but the *object-level* identity behind the corpus slogan is restored: **generic
supertasks ARE diagonalisations** — Specker's σ is the lamp run on the halting set, a single act
that is both a convergent supertask and an escape from the computable reals. "Same theorem"
refines to "same object," not just "same licence." (ii) The jewel (RECORDED July §4) is now a
citation: demanding the theory closed under described limits = demanding it contain Specker
limits = importing the halting problem's insolubility *into the state space as states*
(superpositions, phases) rather than as gaps. Continuity is the topological face of the founding
non-computability — **per Specker 1949**, computable analysis's founding counterexample.
Adjacent: Pour-El–Richards (computable wave-equation data, non-computable solution) — physics
already realises described limits beyond computation.

**Khrennikov foil, answered.** On the p-adic tine: no order, no accumulation for the lamp, and —
decisive for this framework — **no phase**: ℚ_p and its unit groups are totally disconnected;
there is no continuous interpolating phase flow, no U(1), no dense one-parameter winding, no
monodromy integer. The global-phase-as-self-ignorance mechanism (RECORDED) is
Archimedean-specific. p-adic probability is a consistent mathematics of a *different* premise —
worth one respectful subsection, especially at Växjö.

---

## 7. Route B dossier: continuity for free (three faces, one moral)

The July doc recorded Route B as "not attempted." NEW-TODAY: it is not one route but three, each
a developed literature, and together they corroborate P1 from independent directions.

**(a) Measure-theoretic automatic continuity.** Steinhaus/Pettis: a Baire/Haar-measurable
homomorphism between Polish groups is continuous; Christensen extends via Haar-null sets;
Rosendal's survey (BSL 2009, VERIFY) maps the modern field. The discontinuous additive monsters
all require non-measurable sets (Hamel bases). Physical grounding of measurability is the July
doc's own: transformations must yield well-defined record probabilities. FDP strengthens this:
describable ⟹ measurable, monsters unreachable. In Solovay/Shelah worlds the ban is a theorem
(B10).

**(b) Algebraic rigidity — the topology is remembered by the algebra.** **Van der Waerden
(1933):** every abstract group homomorphism from a compact *semisimple* Lie group into a compact
group is continuous; such groups have a unique compact group topology. Tsankov (2013, VERIFY):
the unitary group of separable Hilbert space has automatic continuity. So for the semisimple
bulk of quantum symmetry — SU(n) — **continuity is not extra data; derive the abstract group
(the framework's algebraic comfort zone: anti-events, composition, SCFA circuits) and the
topology follows.** The catch, and it is beautiful: tori are NOT rigid — 𝕋 has wild abstract
automorphisms under AC. **The automatic-continuity-resistant part of the symmetry group is
exactly U(1) — the phase — the part the framework says carries the self-referential ignorance.**
Division of labour: van der Waerden hands SU(n) its topology for free; the ignorance-bearing
U(1) must be carried by P1 (the completion of the dyadic tower, §4). The one piece of topology
self-reference must personally supply is the piece that encodes self-reference.

**(c) Computable-analytic.** In computable analysis (TTE, Weihrauch), **every computable
function on the reals is continuous** — "computable ⟹ continuous" is a theorem, the exact arrow
the framework owes, already proved in the neighbouring category. Scott's domain theory says the
same in semantics (computable = Scott-continuous; approximation by finite information *is* the
topology); Smyth's "topology as the theory of observable properties," Vickers, Abramsky, Escardó
develop it; Gisin's finite-information intuitionism (2019–21) is the physics-adjacent
convergence. If dynamics is computable-from-descriptions (physical Church–Turing, already
committed), its continuity is not an axiom but a corollary.

**Gleason-twice box.** The same Andrew Gleason (i) solved the NSS case of Hilbert's 5th problem
— continuity/analyticity from group structure — and (ii) proved the frame-function theorem,
whose hard analytic core is precisely *automatic continuity* (nonnegative frame functions on
ℝ³ are regular): the Born rule extracted from additivity by a continuity-for-free argument.
Route B is not exotic; the canon already runs it, twice, through one mathematician. Open check:
does the signed/bounded frame-function case (needed if pre-FANOUT weights go negative) retain
automatic regularity? Likely known via Jordan-type decomposition (Sherstnev/Dorofeev, VERIFY).

**Moral.** All three faces say: continuity is a consequence of *maps being given by data*
(measurable, abstract-algebraic, computable). The only discontinuities are oracles. Hence the
thesis sentence of §0.

**Meyer–Kent–Clifton cross-link (for the contextuality pole of the project).** Meyer (1999):
finite-precision measurement "nullifies" Kochen–Specker — KS-colourable *dense rational* subsets
exist; Kent, Clifton–Kent extended; Mermin, Appleby, Cabello replied. That debate is exactly
dense-skeleton vs completion: contextuality's obstruction lives in the completed continuum and
evaporates on describable dense subsets. The framework should say: the completion is forced
(P1), therefore contextuality is physical — and the KS obstruction is another consumer of the
same limit-realisability. This is the project-brief's requested bridge between contextuality and
the self-reference cluster, in a peer-reviewed literature.

---

## 8. The Shannon/complex-log thread, repositioned

What it cannot do: found A5 (B6 — continuation consumes connectedness). What it does, once
repositioned downstream of the dyadic tower:

1. **Demand the root-completion.** H = −Σ p log p meets negative p; log needs −1 in its domain's
   multiplicative reach; in ℝ∖{0} the components of p and −p are disconnected — the sign flip is
   a jump with no continuous story. The minimal connected repair is a path from p to −p avoiding
   0: the anti-event as a continuous rotation e^{iθ}, θ: 0 → π — which is the tower of §4 again,
   from the entropy side.
2. **Rigidity up to winding.** Once on a connected complex domain, the continuation of log is
   unique per homotopy class; the ambiguity 2πik is not noise but a **new integer observable** —
   feed to `appendix_winding_number_operator_2026-07-12.tex` (cross-refs both ways).
3. **Entropy's own continuity discharged, not assumed.** Faddeev's axioms need continuity of
   H(p, 1−p); the grouping axiom is Cauchy's functional equation; measurability (FDP) kills the
   Hamel monsters; continuity follows. Route B(a) in miniature (B6).
4. **Branch-locus prospect (NEW-TODAY, flagged speculative).** Continue H over complexified
   quasidistributions: the branch walls sit at p_i = 0 and the zeros at certainty — **the branch
   locus of the continued entropy is the classical boundary** (records form exactly where a
   probability hits 0/1). Monodromy of H around the walls = entropic image of the FANOUT
   boundary; compare the winding-number appendix. One paragraph in the paper at most, but it is
   the right home for "imaginary entropy."
5. **Modern quasiprobability home.** The Kirkwood–Dirac distribution (Kirkwood 1933, Dirac 1945)
   is the currently active complex-probability formalism; its *negativity and imaginarity* are
   studied as contextuality witnesses (Arvidsson-Shukur, Lostaglio et al., VERIFY exact papers).
   The literature review should place the framework's complex probabilities relative to KD — and
   this is a second requested contextuality bridge.

---

## 9. Corrected-instinct boxes

**Box 1 (RECORDED, July dead-route box — stands).** The diagonal is non-exhaustion, not
construction; uncountable ≠ connected. Unchanged; the Specker bridge (§6) *adds* the object-level
supertask–diagonal identity without reopening the dead route.

**Box 2 (NEW-TODAY): superposition does not imply continuity.** Schumacher–Westmoreland modal QM:
superposition over finite fields, no continuity, no probabilities. Spekkens toy/epistricted
theories: ignorance-based AND discrete — finite transformation groups, integer-quantised
ignorance. The corrected premise: *superposition + probabilistic weights + FDP* forces continuum
scalars; superposition alone is field-agnostic. The framework's separating premise is P2′
(divisibility): finite groups have no n-th roots of their anti-event beyond their order. Open
sub-question, stated honestly: **is self-referential ignorance quantised or divisible?**
Chaitin's Ω is maximally-unknowable *bit by bit* (quantised); the anti-event tower is divisible.
Proposed resolution consistent with the two-sided boundary (RECORDED July §5): recorded
ignorance is bit-quantised (Ω lives post-FANOUT, in the record algebra); pre-record ignorance is
divisible (phase). The lamp again exhibits both: continuous "when it would have halted" phase
before the record; halting bits after.

**Box 3 (NEW-TODAY): the supertask premise, final form.** Archimedean = the schedule *can*
accumulate (and selects ℝ's tine at the Ostrowski fork — Accumulation Lemma); completeness = the
terminal point *exists* (bites only for generic/Specker supertasks; the textbook lamp's limit is
rational). FOIL: Hamkins–Lewis infinite-time Turing machines complete every ω-supertask by
*convention* (the limsup rule: cells take limsup at limit ordinals — the lamp's limsup(0,1,0,1,…)
= 1, liminf = 0). ITTMs thereby formalise Benacerraf's arbitrariness: the record side has no
canonical completion, you must legislate one. The amplitude side's (1+i)/2 (RECORDED founding
resolution) is the *basis-free* completion — the one that doesn't legislate. Two ways to answer
Thomson: convention (ITTM) or superposition (QM); only the second is coordinate-free.

---

## 10. Ways forward (W1–W8)

- **W1 (structural).** Draft sec:self-reference in two layers: Layer-1 scalar subsection
  (frequency-FDP, Ostrowski fork, Accumulation Lemma with its four-case proof, Specker bridge,
  Khrennikov foil) *before* the Layer-2 group subsection — retiring B4. Modest effort, mostly
  assembly of this memo and July's.
- **W2 (the axiom).** State FDP once, formally, with Church–Turing/Lawvere grounding and its
  three theorem-consequences (completion/closedness; monster-ban/automatic continuity; finite K
  per system). This is the paper's honest residual premise; give it a name and a box. B1 becomes
  a stated axiom instead of a hidden move.
- **W3 (the hard one — P2′).** Attempt the derivation "no records ⟹ no distinguished step size
  ⟹ n-stage realisability," with the anti-event tower as the worked example and the
  Spekkens/epistricted foil as the discriminating test (write out exactly which premise S₄
  violates). Also write the weakened No-Minimal-Step fallback and its honest π₀ gap (§5).
- **W4 (transitivity memo).** The superselection-sector-as-record orbit argument (B3), one page,
  folding P3 into face 3 of the five-way regime.
- **W5 (Route B dossier).** Verify and assemble: van der Waerden 1933; Tsankov 2013; Steinhaus/
  Pettis/Christensen/Rosendal; Weihrauch TTE; Gleason-twice; signed frame functions
  (Sherstnev/Dorofeev). Write the U(1)-non-rigidity irony explicitly — it is the framework's
  best "why the phase, specifically" argument.
- **W6 (stretch — the Lawvere unification).** Lawvere 1969 (fixed points) + Lawvere 1973 (metric
  spaces as enriched categories; **Cauchy completeness = representability of limit-bimodules**)
  are one man's two halves of this problem. Conjecture to attack: in a closed category with a
  point-surjective self-describer into the amplitude object, describable limit-profunctors must
  be representable — an unrepresented limit yields a diagonalisation witness against
  point-surjectivity ("the description refers to a transformation that does not exist," made
  categorical). If this proves, Route A is a theorem and the paper has its spine.
- **W7 (literature intake for the review).** Specker 1949; Weihrauch; Pour-El–Richards; Meyer/
  Kent/Clifton–Kent + replies (contextuality bridge); Gisin 2019–21; Hamkins–Lewis 2000;
  Schumacher–Westmoreland; Spekkens 2007/2016; Kirkwood–Dirac imaginarity-contextuality corpus;
  Rosendal survey; van der Waerden; Hofmann–Morris; Ostrowski; de Finetti (finite additivity)
  vs Kolmogorov axiom V; Norton/Laraudogoitia supertasks; Montgomery–Zippin.
- **W8 (prospect).** The entropy branch-locus paragraph (§8.4) pointed at the winding-number
  appendix, and the KD-imaginarity placement — both feed the project's contextuality pole.

## 10a. Addendum (later same session): the stage-lattice reduction

Candidate lemma that would collapse the premise-set of §5: *if some available transformation g
lacks an available n-th stage, then the set of achievable stages of g forms a distinguished
discrete lattice — a preferred-basis-like invariant structure, i.e. a record — contradicting
face 3 (no classical record).* Discreteness = record is exactly the shape of the May 4⇔5
argument, applied to the stage structure instead of the state set. If this lemma holds, **P2′
(divisibility) reduces to face 3 just as P3 (transitivity) does** via the
superselection-sector-as-record argument: the pre-FANOUT regime's defining no-record property
supplies both, and the single remaining bridge from self-referential ignorance proper is
**P1/FDP (closure)**. The headline question "does self-referential ignorance ⟹ A5?" then reads:
yes, modulo (i) FDP, (ii) this lemma, (iii) the Layer-1 scalar story — all three sharply stated.
Status: statement NEW-TODAY; proof OWED.

## 11. Consequences worth recording

Limit-realisability is the common root of Hardy A1 (limiting frequencies exist) and A5
(continuous group) — the two real-number imports of the reconstruction discharge to one
principle. Downstream, once A5 delivers paths, Stone's theorem converts strong continuity of
one-parameter unitary groups into self-adjoint generators: **continuity ⟹ Hamiltonians** — the
final consumer of the arrow. And the de Finetti stance (§2) should be stated in the paper:
the framework sides with completion against finitism, *because* of self-reference — that is a
philosophical position with a pedigree on both sides, not an oversight.

## 12. Informal references (VERIFY all at drafting stage)

Hardy quant-ph/0101012 (2001 posting — RECORDED date-fix note). Specker, *Nicht konstruktiv
beweisbare Sätze der Analysis*, J. Symb. Logic 14 (1949). Weihrauch, *Computable Analysis*
(2000). Pour-El & Richards, *Computability in Analysis and Physics* (1989). Lawvere 1969
(Diagonal arguments…), Lawvere 1973 (Metric spaces, generalized logic…). Scott; Smyth; Vickers,
*Topology via Logic*; Abramsky, *Domain theory in logical form*; Escardó, synthetic topology.
Gisin, finite-information/intuitionism papers 2019–2021. Meyer PRL 83:3751 (1999); Kent (1999);
Clifton–Kent (2000); Mermin/Appleby/Cabello replies. Hamkins & Lewis, *Infinite time Turing
machines*, J. Symb. Logic 65 (2000). Schumacher & Westmoreland, *Modal quantum theory* (Found.
Phys. 2012-ish). Spekkens, PRA 75, 032110 (2007); *Quasi-quantization: classical statistical
theories with an epistemic restriction* (2016). Kirkwood (1933); Dirac, Rev. Mod. Phys. 17
(1945); Arvidsson-Shukur et al., Lostaglio et al. on Kirkwood–Dirac (2020s). van der Waerden,
Math. Z. 36 (1933). Tsankov, automatic continuity of U(ℓ²) (2013). Rosendal, BSL 15 (2009).
Steinhaus (1920); Pettis (1950); Christensen (1972). Solovay (1970); Shelah (1984). Hofmann &
Morris, *The Structure of Compact Groups* (connected ⇔ divisible, compact abelian). Ostrowski
(1916). Montgomery–Zippin (1955); Gleason (1952); Gleason, frame functions, J. Math. Mech. 6
(1957). Thomson 1954; Benacerraf 1962 (RECORDED). de Finetti on finite additivity; Kolmogorov
(1933) axiom V ("continuity"). Norton (supertasks, SEP); Laraudogoitia. Sherstnev/Dorofeev,
signed measures on projection lattices.
