# The Dynamics Companion: Reversibility, FANOUT, and the Route to Unitarity

**Research note — 2026-05-20T14:30**

**Status.** Working note. Intended as the *dynamics* counterpart to
`fanout_logic_measure_correspondence_theorem_v2_2026-05-17.md`. Where that theorem
treats FANOUT as the boundary for **logic** (anhomomorphism) and **measure**
(signedness), this note treats FANOUT as the boundary for **dynamics**: how the
framework reaches unitary evolution, which premise actually does the work, and where
the field ℂ comes from. Companion target: the QM-derivation section of Paper 1.

**Origin.** A six-step conversation (20 May 2026). Each step either tightened an
argument or repaired a tempting but invalid one. The corrections are kept in the
record below because they are instructive — the invalid versions are exactly the
ones a careful referee would attack.

---

## 1. The pre/post-FANOUT dynamical dichotomy

FANOUT is already established in the framework as the epistemological/ontological
boundary: the clonability of information is the operational criterion separating
private (non-clonable, phase-carrying) from public (clonable, communicable). This
note adds the dynamical reading.

**Post-FANOUT.** In the Coecke–Kissinger vocabulary, FANOUT is the SCFA
comultiplication, the COPY map δ: H → H⊗H. Its precise character is sharper than
"stochastic": δ is an **isometry but not a unitary** — δ†δ = I but δδ† is a
projector ≠ I. It is not square. It has a left inverse (δ†) but no two-sided
inverse, and that non-surjectivity *is* the irreversibility. The stochastic matrix
appears one step later: trace out the copy (the environmental record), and the
marginal dynamics on the surviving register is a stochastic/Markov map, generically
non-invertible.

So the dichotomy is:

- **FANOUT itself** = isometric embedding into a larger space (no two-sided inverse).
- **Effective post-FANOUT dynamics** = stochastic matrix on the classical record.
- **Pre-FANOUT dynamics** = reversible. The target of this note.

---

## 2. The invalid shortcut: "reversible → invertible → unitary"

The tempting chain is: pre-FANOUT events are reversible; reversible means
invertible; invertible probability-preserving maps are unitary. **The last step is
invalid as stated**, and Paper 1 must not use it.

Reversible = invertible = possessing a two-sided inverse. On a complex vector space
that delivers the **full general linear group GL(n, ℂ)** — n² complex dimensions.
U(n) sits inside GL(n, ℂ) as a real form of *half* that dimension. "Complex +
reversible" lands in GL(n, ℂ) and stops; it does not reach U(n). A complex shear, or
simply ψ ↦ 2ψ, is reversible and complex-linear and not remotely unitary.

Two further facts pin the gap down:

1. **Staying classical gives only permutations.** If one remains in the classical
   probability simplex (ℓ¹, non-negative, sums to 1) and demands reversibility, the
   only maps are the **permutation matrices** — a discrete group, not the continuous
   U(n). (A stochastic matrix whose inverse is also stochastic is a permutation.)
   Reversibility on classical probabilities buys permutations, full stop.

2. **What carves U(n) out of GL(n, ℂ) is preservation of the Hermitian quadratic
   form** Σ|ψᵢ|² = 1. Invertible + ℓ²-isometry = unitary; Wigner's theorem makes
   this tight (continuous, reversible, transition-probability-preserving → unitary).

**Conclusion.** Reversibility supplies "the isometry has a two-sided inverse"; it
does not supply "isometry." The load-bearing premise for unitarity is preservation
of the quadratic form. Reversibility is, in fact, a **corollary** of that premise,
not a co-premise: a norm-preserving linear map on a finite-dimensional space is
injective, hence bijective, hence invertible, with norm-preserving inverse. Putting
"complex + reversible" together does not reach unitary; putting "complex +
norm-preserving" together does, and hands you reversibility for free.

A note on negative probability specifically: a signed quasi-probability is still
*linearly* normalised (Σpᵢ = 1 with some pᵢ < 0). So negative probability is
compatible with, and at most yields, conservation of the *linear* functional. The
*quadratic* form is a separate fact. Negative probability is the thing that *forces
the bridge* from ℓ¹ to ℓ²; it is not the thing that fixes the metric on the far
side.

---

## 3. The five-way pre-FANOUT equivalence

The pre-FANOUT regime can be characterised five equivalent ways. These are not five
premises to be combined; they are one regime under five descriptions.

1. **Negative probability is available** (anti-events have negative probability).
2. **Anti-events / reversibility hold** (events are undoable).
3. **No classical record exists.**
4. **No preferred basis is selected.**
5. **Hardy's continuity axiom holds** (a continuous reversible transformation
   between any two pure states).

FANOUT is the single event that fails all five at once: it writes the record,
selects the basis, kills the anti-events, discretises the transformation group, and
switches off negative probability. One boundary, five readings — the dynamical
analogue of the 17 May theorem's "one boundary, several readings" for logic and
measure.

The identification 4 ⇔ 5 is doing real work and is proved below (§4); 1 ⇔ 2 is the
anti-event identity already in the framework.

---

## 4. Leg 2: basis-blind coherence, and the Hardy identification

### 4.1 Dutch-book coherence is post-FANOUT

An earlier draft attributed the quadratic conserved form to "coherence." This needs
care, because ordinary Dutch-book coherence is itself a **post-FANOUT** notion: the
sure-loss argument bites at *settlement* — a ticket is shown to a bookmaker, a
proposition's truth value is read off a record, gains are summed. Every operative
noun (ticket, record, reading-off, summing) is post-FANOUT. Standard Dutch-book
coherence therefore delivers only Σpᵢ = 1 on classical outcomes — the *linear*, ℓ¹
normalisation. It does not, by itself, deliver the quadratic form.

### 4.2 The repair: basis-blind coherence is quadratic

Pre-FANOUT there is no preferred basis — FANOUT is the operation that *selects* the
basis (the SCFA that fires picks it; cf. `observable_bundling_at_measurement.md`).
So the pre-FANOUT agent does not know which basis the eventual record will be
written in. The only coherence demand even *statable* pre-FANOUT is: **whichever
basis FANOUT turns out to select, the resulting record must sum to 1.**

Demanding Σpᵢ = 1 *in every orthonormal basis simultaneously* is not a weak ℓ¹
condition. The quadratic form Σ|ψᵢ|² is the unique functional that is
basis-independent and reduces to Σpᵢ = 1 in each basis. **The quadratic form is
Dutch-book coherence with the basis-quantifier moved out front.** It is not an
intrinsic pre-FANOUT bet-settlement (there is no bookmaker there); it is the
*basis-independent envelope* of post-FANOUT coherence.

This makes Postulate 3 (Born, the quadratic U(1)-invariant) and Postulate 5
(unitary) visibly the same object: unitarity is the symmetry group of the Born form.

### 4.3 "No preferred basis" is Hardy's continuity axiom

A *preferred basis* is a distinguished finite set of pure states (the simplex
vertices). If a basis is selected, the only structure-preserving reversible maps are
permutations of those distinguished points — a discrete group, no continuity.
Contrapositive: continuous reversibility ⇒ no basis selected. The converse runs too:
if no finite set of pure states is privileged, the reversible transformations cannot
be pinned to permuting a finite set, so the pure-state space must be homogeneous
under them — a continuous group. Hence:

> **No preferred basis ⇔ Hardy continuity.** The selection of a basis is exactly
> the collapse of a continuous transformation group to a discrete one.

This is more than terminology. It converts leg 2 from an argument the framework must
prove into a **citation**. Hardy (2003, quant-ph/0101012) already showed that
continuity, plus his other mild axioms, yields the complex Hilbert space with the
quadratic norm and the unitary group. So the framework's job shrinks to one thing:
**deriving Hardy's continuity axiom from self-reference**, via
negative probability → anti-events → reversibility-without-a-selected-basis →
continuity. Everything downstream — quadratic form, U(n), Born rule — is then
Hardy's theorem, cited rather than re-proved.

Caveat for the paper: Hardy needs continuity *plus* the subspace/composition axioms.
Confirm those are independently satisfied or derived in the framework (the
Cayley–Dickson composition story plausibly covers tensor structure) rather than
assumed to come along free.

---

## 5. Aaronson, "Is Quantum Mechanics an Island in Theoryspace?"

Source verified by direct read: Aaronson, *Is Quantum Mechanics An Island In
Theoryspace?* (quant-ph/0401062; Växjö proceedings — acknowledgments thank
Khrennikov for inclusion and Fuchs for instigation). Three results bear on the
dependency graph.

### 5.1 Section 2 — the 2-norm is uniquely special

**The 2-norm is the only p-norm that permits nontrivial norm-preserving linear
maps.** For every p ≠ 2 the only norm-preserving linear transformations are
generalised diagonal matrices (permutations composed with diagonal rescalings) —
no rich group. The 1-norm is **not** a co-equal special point; it looks special only
under nonnegativity. Stochastic matrices preserve the 1-norm of *nonnegative*
vectors; over *all* vectors (negative entries allowed) the only 1-norm-preserving
linear maps are the **permutation matrices**.

That last fact is the negative-probability argument, sitting inside Section 2 — with
the honest caveat that **Aaronson does not frame the paper this way**. The paper is a
p-norm survey. The snappy "QM is probability theory with minus signs" line is from
*Quantum Computing Since Democritus* and is a heuristic, not a theorem. What is a
theorem, and is in the island paper: allow probability vectors to carry minus signs
(quasi-probabilities), keep dynamics linear, and the 1-norm dies — permutations only,
no interference. The unique p-norm giving signed vectors a rich linear dynamics is
p = 2, whose norm-preserving maps are orthogonal/unitary. For Paper 1: cite the
theorem; supply the negativity framing as our own reading.

### 5.2 Section 2–3 — the keystone: GL(n, ℂ) is physically pathological

Aaronson's "option (ii)" — map |ψ⟩ to A|ψ⟩ for *any invertible A* — is precisely
**GL(n, ℂ) as a dynamics**: reversibility with no norm constraint. This is exactly
the object §2 above identified as the gap. Aaronson proves what it costs: arbitrary
invertible matrices permit **superluminal signalling**, allow **distinguishing
non-orthogonal states**, and let a quantum computer solve **PP-complete problems**
in polynomial time (PP sits above NP).

> **Keystone.** Reversibility alone = GL(n, ℂ) = Aaronson's option (ii) =
> superluminal signalling + PP. *Pathological.*
> Reversibility + 2-norm preservation = U(n). *Healthy.*

This upgrades §2's "you need an extra premise" from a logical nicety to a **physical
necessity**. Leg 2 — the conserved quadratic form — is the thing standing between
the theory and superluminal signalling. It is not an aesthetic axiom.

### 5.3 Section 4 — ℂ over ℝ, but silent on ℍ

Aaronson's independent ℝ-vs-ℂ argument is the **square-root property**: for
continuous time evolution every U must have a V with V² = U. Real QM fails this —
orthogonal matrices of determinant −1 (the phase flip, the swap) have no real square
root of the same dimension. Complex QM has it; **so does quaternionic QM** (every
quaternion has a square root). Aaronson is explicit, twice, that the argument forces
ℂ over ℝ but says **nothing about ℂ versus ℍ**.

### 5.4 Three routes to legs 2–3

Legs 2–3 (quadratic form; unitarity) are now over-determined:

- **Hardy** — continuity → 2-norm geometry.
- **Aaronson §2** — linear + norm-preserving + nontrivial → p = 2 + unitary.
- **Aaronson §3** — the alternative (drop norm preservation) is causally and
  computationally pathological.

Over-determination is exactly what Paper 1 wants here.

---

## 6. Brukner–Zeilinger: the two-strand response

Brukner & Zeilinger, *Conceptual inadequacy of the Shannon information in quantum
measurements* (quant-ph/0006087), argue Shannon information is inadequate for QM.
The paper has two separable strands; the framework must answer both.

### 6.1 Conceptual strand — defeated by relocating ignorance

B-Z's conceptual claim: a measurement reveals no pre-existing value, so the observer
is ignorant of nothing, so Shannon "information gain" does not apply. The mechanism
of this argument is the weak point: **B-Z tacitly assume the only thing an observer
can be ignorant of is a property of the system.** Bell and Kochen–Specker then forbid
pre-existing system properties, and B-Z conclude there is no ignorance at all.

The framework's reply is *not* "there is a hidden system value" — that walks into
Bell/KS/PBR. It is that B-Z **enumerated the loci of ignorance incompletely**. There
is a second locus: the observer's own state. Ignorance of it is real, is irreducible
by Turing/self-reference, and is untouched by Bell/KS/PBR because those theorems
constrain *system* hidden variables, not the observer's self-model. (This is the same
reason PBR misses the framework: the relevant hidden variable is the observer's, not
the system's — the framework sits outside the Harrigan–Spekkens classification.)

Shannon's precondition — uncertainty as ignorance of a definite-but-unknown fact —
is thereby restored, with the fact relocated. Note one does not even need a
pre-existing *outcome*: the operational pure↔mixed argument (no physical change when
a remote result arrives) already shows the uncertainty behaves like ignorance.
Shannon's uniqueness theorem then forces −log p.

### 6.2 Technical strand — absorbed as the Born rule

Independently of the objective-randomness claim, B-Z argue the *basis-invariant*
information measure of a qubit is **quadratic** (summed over mutually unbiased
bases), because Shannon entropy is basis-dependent. This is interpretation-free, so
§6.1 does not touch it.

The framework should not defeat this strand — it should **absorb** it. B-Z's
quadratic invariant is the squared Bloch radius, and that *is* the Born rule: the
degree-2 U(1)-invariant already derived from the Hopf argument. So the position is
clean: B-Z are right that the basis-blind measure is quadratic — that is Born,
pre-FANOUT, ℓ². Shannon's −log p is the basis-fixed measure — post-FANOUT, on the
classical record, ℓ¹. **Not rivals; the pre- and post-FANOUT measures.** B-Z
conflated "invariant measure of the state" with "information the observer gains";
those differ precisely because the gain is basis-relative (which record got made)
while the state's invariant is basis-blind.

---

## 7. The quaternion-logarithm exclusion (native replacement for leg 1b)

### 7.1 Statement and repair

What ties negative probability to *complex* probability is Shannon: negative
probability forces −log p, and log of a negative number forces analytic continuation
to ℂ. A natural further question is whether log also excludes the quaternions.

The naive form — "log fails for quaternions" — is **too strong**. The quaternion
logarithm exists perfectly well: log q = ln|q| + ûφ for q = |q|e^{ûφ}. What fails is
not its existence but its **homomorphism property**: exp(p+q) = exp(p)exp(q) holds
for quaternions **iff p and q commute** (exactly as e^{A+B} = e^A e^B needs
[A,B] = 0 for matrices). So log(ab) = log(a) + log(b) genuinely breaks for
non-commuting quaternions — but the correct name for the breakage is "log is not a
homomorphism," not "log does not exist."

### 7.2 Why this matters: the homomorphism *is* Shannon additivity

The homomorphism property is not incidental — it is the whole reason log is the
right tool. Shannon's additivity axiom (information from independent events adds),
I(p₁p₂) = I(p₁) + I(p₂), is precisely the statement that I is a homomorphism from
(composition, ×) to (information, +). "S = −log p turns multiplicative Bayesian
updating into additive information updating" is that homomorphism, named.

### 7.3 The exclusion argument

Split a quaternion amplitude into modulus and phase.

- **Modulus.** |q₁q₂| = |q₁||q₂| holds in *all four* division algebras — this is
  Hurwitz. So ln|q| is additive everywhere. The modulus is never the problem.
- **Phase.** ℂ's phase group is U(1), abelian: log linearises it, and the −iθ term
  in S = −log|p| − iθ is a genuine additive information term. ℍ's "phase" is the
  **non-abelian** S³ ≅ SU(2): log does not linearise it (non-zero commutator, BCH),
  so the phase part of quaternionic "information" is **not additive**, and
  S = −log|p| − iθ has no consistent quaternionic analogue.

> **Proposition (to be written rigorously).** Shannon-additivity of *phase
> information* forces the amplitude algebra's phase group to be abelian — hence
> U(1) — hence the amplitude field is ℂ.

This excludes 𝕆 as well (non-commutative *and* non-associative). It is therefore a
**framework-native replacement** for the previously-imported parameter-counting
exclusion (leg 1b, f(n) = n², Caves–Fuchs–Schack / Hardy). The framework now has
three independent routes to "ℂ not ℍ" for the amplitude field:

1. **1a** — analytic continuation of log through the negative axis → *at least* ℂ.
2. **1b (imported)** — parameter count f(n) = n² → not ℍ.
3. **1c (native)** — Shannon-additivity of phase → abelian phase → U(1) → ℂ.

Route 1c is the one to lead with: it runs entirely through the information-theoretic
backbone the framework already commits to.

### 7.4 Honest flags

- The pieces (modulus/phase split; exp-additivity iff commuting; multiplicativity of
  the quaternion norm; non-abelian S³) are solid textbook facts. The **assembly**
  into an exclusion theorem is a clean new argument that must be written out.
- The rigorous write-up must state *why an adequate information measure must be
  sensitive to the non-commutative part* rather than legitimately blind to it. The
  cleanest hinge: independent-subsystem composition is **symmetric** (it cannot
  matter which subsystem is listed first), so ℍ's order-dependent product is already
  pathological at the amplitude level; the Shannon-additivity statement is that same
  fact seen through log. The argument is robust under that reformulation — reassuring
  — but the framing should be chosen deliberately.
- This argument concerns the **amplitude field** only. It leaves untouched the roles
  of ℍ and 𝕆 as Cayley–Dickson qubit / gauge structure elsewhere in the framework.
  State this explicitly to pre-empt confusion.

---

## 8. The assembled dependency graph

For the QM-derivation section of Paper 1:

```
self-reference
   │
   ▼
negative probability  ──────────────┐
   │                                │
   │ (anti-events)                  │ (analytic continuation: log of −|p|)
   ▼                                ▼
reversibility-without-            field is at least ℂ        [leg 1a]
a-selected-basis                     │
   │                                 │  + Shannon-additivity of phase
   │ = Hardy continuity   [leg 2]     │    → abelian phase → U(1)   [leg 1c, native]
   ▼                                 │  ( replaces imported f(n)=n²  [leg 1b] )
Hardy's reconstruction               ▼
   │                              field is ℂ (not ℍ, not 𝕆)
   ▼
complex Hilbert space, quadratic (Born) form, U(n)   [legs 2–3]
   │
   │  legs 2–3 over-determined:
   │   • Hardy continuity
   │   • Aaronson §2 (only p=2 has a nontrivial norm-preserving linear group)
   │   • Aaronson §3 (drop norm preservation → superluminal signalling + PP)
   ▼
unitary evolution.  Reversibility is a COROLLARY, not a premise.
```

Keystone, stated once more for the paper: **reversibility alone = GL(n, ℂ) =
Aaronson option (ii) = superluminal signalling + PP.** The cut from GL(n, ℂ) down to
U(n) is the conserved quadratic form, and that cut is what makes the theory causal.

---

## 9. Settled / new / open

**Settled (each independently established in cited literature):**

- FANOUT / COPY as the SCFA comultiplication; an isometry, not a unitary
  (Coecke–Kissinger).
- Reversible stochastic maps = permutation matrices; reversible-but-not-norm-
  preserving complex-linear maps = GL(n, ℂ).
- Wigner's theorem: continuous reversible probability-preserving symmetry → unitary.
- Hardy (2003): continuity + mild axioms → complex Hilbert space, quadratic norm,
  U(n).
- Aaronson (island paper): 2-norm uniquely admits nontrivial norm-preserving linear
  maps; arbitrary invertible matrices → superluminal signalling + PP; square-root
  property → ℂ over ℝ, silent on ℍ.
- Quaternion log exists; exp(p+q) = exp(p)exp(q) iff [p,q] = 0; quaternion norm
  multiplicative (Hurwitz); S³ ≅ SU(2) non-abelian.
- Brukner–Zeilinger: Shannon entropy basis-dependent; quadratic invariant over MUBs.

**New from this note:**

- The dynamical reading of the FANOUT boundary: isometry (FANOUT) → stochastic
  (record), versus unitary (pre-FANOUT) — completing the trio with the 17 May
  theorem's logic and measure readings.
- The explicit correction of "reversible → invertible → unitary": reversibility is a
  *corollary* of norm preservation, not a co-premise.
- Leg 2 restated as **basis-blind coherence** — the quadratic form as Dutch-book
  coherence with the basis-quantifier moved out front — and its identification with
  Hardy's continuity axiom (no preferred basis ⇔ continuity).
- The five-way pre-FANOUT equivalence.
- The keystone identification: reversibility-alone = GL(n, ℂ) = Aaronson option (ii)
  = superluminal signalling + PP — making leg 2 a physical necessity.
- The two-strand Brukner–Zeilinger response: conceptual strand defeated by relocating
  ignorance to the observer's own state; technical strand absorbed as the Born rule.
- The **quaternion-logarithm exclusion** (leg 1c): Shannon-additivity of phase forces
  an abelian phase group, excluding ℍ and 𝕆 as the amplitude field — a native
  replacement for the imported parameter count.

**Open:**

- Rigorous proof that self-reference *delivers* Hardy's continuity axiom (the single
  arrow the framework still owes). The chain via anti-events is plausible but not
  written down.
- Confirm Hardy's subspace/composition axioms are independently satisfied or derived,
  not assumed free with continuity.
- Rigorous write-up of the leg-1c proposition, including the precise faithfulness
  condition on the information measure (why I must be sensitive to the
  non-commutative part) and the choice between the amplitude-level framing
  (independence is symmetric) and the information-level framing (additivity is a
  homomorphism).
- Whether the Lawvere–Yanofsky diagonal analysis delivers leg 2 *intrinsically*
  pre-FANOUT, rather than via the basis-quantifier route. The basis-quantifier
  argument is the solid one and suffices for Paper 1; the diagonal-intrinsic version
  is a stronger, still-unproved claim.

---

## 10. For Paper 1

Recommended placement: this material is the dynamics half of the QM-derivation
section, paired with the Born-rule (Hopf) and FANOUT-boundary material already
drafted. Three rhetorical points carry the section:

1. State the dependency graph (§8) explicitly, with reversibility marked as a
   corollary. A careful reader (Khrennikov) will otherwise spot reversibility doing
   no work and the quadratic norm slipped in unannounced.
2. Use the keystone (§5.2) as the section's hinge: it converts an abstract logical
   gap into a concrete physical one (superluminal signalling), which is far more
   persuasive than an axiom.
3. Lead the field-selection argument with leg 1c (§7), the native one; mention 1a and
   1b as concurring. Note that the island paper is itself a Växjö proceedings paper —
   a natural citation for the framework's primary venue.
