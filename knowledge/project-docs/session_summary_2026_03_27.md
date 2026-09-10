# Session Summary — 27 March 2026

## Deriving the Postulates of Quantum Mechanics from Self-Reference

### Overview

This session systematically addressed whether the framework can derive all six standard postulates of quantum mechanics from the self-referential starting point, rather than merely reinterpreting them. The conclusion is that it can — each postulate is either logically forced or has a unique solution, with the complex numbers being the only non-trivial input and everything else following as the unique consistent probability theory built on ℂ.

A new derivation of the Born rule from the Hopf fibration was developed, which appears to be novel in the literature. The FANOUT criterion — previously present in John's thinking since the 2007 MSc dissertation but omitted from recent posters — was identified as the precise operational boundary between epistemological and ontological information, and was shown to do substantial work in grounding the measurement postulate, explaining decoherence, and pre-empting the standard QBism objection about inter-subjective agreement.

---

## 1. The Six Postulates — Derivation Summary

### Postulate 1: States are vectors in a complex Hilbert space

**Status: Derived.**

Self-reference → observer must assign probability to own internal state → negative probability → Shannon information requires log of negative values → analytic continuation to complex plane → complex probability amplitudes.

The Hilbert space structure (inner product) encodes distinguishability between states of knowledge. Two epistemological states are orthogonal when perfectly distinguishable; the inner product ⟨φ|ψ⟩ measures overlap between states of knowledge. Completeness (closure under limits) is a consistency requirement: limits of convergent sequences of knowledge states must themselves be valid knowledge states.

### Postulate 2: Observables are Hermitian operators

**Status: Trivially forced.**

Given a complex state space (derived above) and the requirement that measurement outcomes must be real numbers (a measurement result is a classical fact — communicable, distributable via FANOUT — and communication happens in the real-valued classical channel), the operators representing measurements must be Hermitian. This is the unique condition guaranteeing real eigenvalues on a complex vector space. No freedom exists here.

### Postulate 3: The Born rule p = |ψ|²

**Status: Derived. Three independent routes; the Hopf route is new and strongest.**

See §2 below for the full Hopf derivation.

### Postulate 4: State vector reduction (measurement update)

**Status: Derived.**

Both the real and complex components of the state are epistemological — properties of the observer's knowledge, not of the system. "Collapse" is Bayesian updating: the observer gains information (the measurement result) and updates their state of knowledge. The apparent discontinuity is the same as opening an envelope and learning the result of a coin flip.

What the framework adds beyond standard QBism: the *reason* the pre-measurement state had complex amplitudes is that the observer couldn't fully know their own state. After measurement, that particular self-referential loop has been closed (at the cost of opening new ones, per the C → C⁺ → C⁺⁺ chain).

The FANOUT criterion (§3) makes this precise rather than philosophical: measurement is the specific operation that converts non-clonable (private, epistemological, complex) information into clonable (public, ontological, real) information.

### Postulate 5: Unitary time evolution (Schrödinger equation)

**Status: Derived.**

Probability conservation (the observer must always be in *some* state of knowledge) + complex Hilbert space → time evolution must preserve the inner product → unitarity. Stone's theorem then gives U(t) = e^{−iHt} for some Hermitian H, which is the Schrödinger equation.

Deeper grounding from the CASYS paper: Rule 𝒜 (no supertasks) requires a global time parameter and gives ℏ. Unitarity is the mathematical expression of Rule 𝒜 — the global reference frame of time must preserve total information content. If it didn't, a supertask could extract or destroy information, violating the no-supertask constraint.

**Critical implication for quantum gravity:** Unitarity requires a global time parameter — a universal "in the future" that all observers agree on. Special relativity provides this (Minkowski spacetime has global causal structure). General relativity does not (no preferred foliation, possible CTCs). This is the deep reason canonical quantum gravity fails: the Wheeler-DeWitt equation H|ψ⟩ = 0 is what you get when you try to write the Schrödinger equation without preferred time — it says nothing ever happens. See §5 below.

### Postulate 6: Tensor product composition

**Status: Derived.**

The Cayley-Dickson construction (ℝ → ℂ → ℍ → 𝕆) is a tensor-product-like operation — dimensions multiply, not add. This multiplicative composition is forced by the requirement that the combined system can represent *all possible correlations* including entangled ones. The direct sum would only give product states. The tensor product is the minimal space accommodating entanglement.

Categorical argument: the tensor product is the unique monoidal product making the category of Hilbert spaces compact closed (Coecke-Kissinger compositional completeness), which is the categorical expression of entanglement and teleportation.

### Open gap: Separability

The one remaining piece is why the Hilbert space is separable (has a countable basis). Conjectured to follow from the computability constraint: a non-separable Hilbert space would require uncountably many distinguishable states, needing non-computable labels to index them. The causality protection system should forbid this. Not yet made explicit.

---

## 2. The Born Rule from the Hopf Fibration — New Derivation

### The argument

**Setup.** A normalised qubit state (α, β) ∈ ℂ² with |α|² + |β|² = 1 lives on S³. The global phase is unobservable: (α, β) and (e^{iθ}α, e^{iθ}β) are physically indistinguishable. So physically distinct states are the quotient S³/U(1) = ℂP¹ ≅ S². The Hopf map is the projection S³ → S².

**The key question.** What is the lowest-degree polynomial in (α, β, α*, β*) that's invariant under the U(1) fibre action?

**Degree 1 is impossible.** A general monomial α^a β^b (α*)^c (β*)^d transforms under (α, β) → (e^{iθ}α, e^{iθ}β) as:

e^{i(a+b−c−d)θ} × α^a β^b (α*)^c (β*)^d

Invariance requires a + b = c + d. At degree 1 (a + b + c + d = 1), this has no solutions. **There are no U(1)-invariant polynomials of degree 1.** Linearity is ruled out by the topology of the fibre.

**Degree 2 works.** At degree 2 with a + b = c + d = 1, the invariant monomials are: |α|², |β|², αβ*, α*β. On S³ (with |α|² + |β|² = 1) these give three independent real quantities:

- |α|² − |β|² (ranges from −1 to +1)
- 2Re(αβ*)
- 2Im(αβ*)

These are exactly the Bloch sphere coordinates on S². The Born rule probability p₀ = |α|² is the simplest U(1)-invariant monomial. It's degree 2 — **squared** — because degree 1 invariants don't exist.

**Generalisation.** For n-dimensional Hilbert space: state space is S^{2n−1}, fibre is U(1), quotient is ℂP^{n−1}. The same argument applies: U(1)-invariant polynomials require equal holomorphic and anti-holomorphic degree, so minimum degree is 2, and p_k = |ψ_k|² is the unique lowest-degree invariant probability assignment.

### What the argument assumes

Only two things:

1. The state space is a complex vector space (derived from self-reference → negative probability → analytic continuation).
2. The global phase is unobservable (forced because the global phase is the S¹ fibre — the observer's private self-referential ignorance — which cannot be FANOUTed).

It does **not** assume: linearity of quantum mechanics, anything about measurement or dynamics, any dimension restriction (works for a single qubit, unlike Gleason), any decision-theoretic or frequency-limit framework.

### The full logical chain (paper version)

The observer cannot fully know their own state (self-reference). This forces complex probability amplitudes (analytic continuation of Shannon information). The imaginary component represents information the observer lacks about themselves. Because they lack it, they cannot communicate it (no FANOUT on information you don't possess). Because it cannot be communicated, it cannot enter any measurement result. Therefore observables must be invariant under the global phase. Therefore the minimum-degree map from amplitudes to probabilities is quadratic. Therefore p = |ψ|².

### Advantages over existing Born rule derivations

- **Versus Gleason:** Works for dimension 2 (single qubit). Three lines of algebra versus a notoriously intricate proof. Gives a physical *reason* for squaring, not just uniqueness.
- **Versus Deutsch-Wallace:** No decision-theoretic assumptions. Doesn't depend on rationality axioms.
- **Versus Zurek (envariance):** No decoherence assumptions. Doesn't require environment.
- **Versus Hartle (frequency):** No infinite-ensemble limit. Works for a single system.

The argument is purely structural: given complex amplitudes with a private phase, the quadratic rule is the unique lowest-order extraction of public probabilities.

### Literature status

The geometric correspondence between the Hopf map and quantum state space is established (Mosseri & Dandoloff 2001, Urbantke, others). The claim that the Born rule's quadratic form is *topologically forced* by U(1) invariance of the fibre — specifically, that degree-1 invariants don't exist — does not appear to have been stated as a derivation in the literature. The pieces (Hopf map, U(1) invariance, classification of invariant polynomials) are all known; their assembly into this specific argument appears to be new. **Treat cautiously; verify against literature before claiming novelty in the paper.**

### Paper strategy

Present the Hopf derivation as the Born rule argument. Do not mention alternative derivations (Gleason, Deutsch-Wallace, Zurek, Hartle, etc.) — this avoids pulling the reader into a comparison debate and keeps the narrative flowing from self-reference to the Standard Model.

---

## 3. FANOUT as the Epistemological/Ontological Boundary

### The criterion

The ability to copy information (FANOUT) is the precise operational criterion distinguishing:

- **Epistemological** (private): non-clonable, complex, phase-carrying, observer-dependent
- **Ontological** (public): clonable, real, communicable, observer-independent

A measurement result can be written down, spoken, transmitted as bits. The moment it enters the classical channel it can be copied — FANOUT is free on classical data. Once distributed to multiple observers, it's operationally indistinguishable from an objective fact. The epistemological becomes effectively ontological through clonability.

The complex phase represents the observer's ignorance about their own state. They don't have this information, so they cannot copy it. **The no-cloning theorem gets a conceptual explanation prior to linearity and unitarity: you can't clone the phase because the phase is what the observer doesn't know about themselves, and you can't share what you don't have.**

### Connection to Hopf fibration

- Base space S² = space of measurement outcomes = the clonable part
- Fibre S¹ = global phase = the non-clonable part (observer's self-referential ignorance)
- Hopf projection S³ → S² = map from full quantum state to what can be cloned and shared

Measurement *is* the Hopf map. What it discards (the fibre) is precisely the non-communicable self-referential component.

### Connection to categorical quantum mechanics

In the ZX-calculus (Coecke-Kissinger):
- **Special Frobenius algebra** supports copying (FANOUT) → classical data, GHZ-type entanglement
- **Anti-special Frobenius algebra** does not support copying → complementary observables, W-type entanglement

The framework already maps GHZ → quarks and W → leptons. So the algebraic structure of "information that can be shared" (special Frobenius) is the same structure that characterises colour confinement. Confinement is the price of classicality: the GHZ structure that enables copying ensures coloured constituents can never be isolated.

### Measurement as FANOUT

Measurement is the specific operation that converts non-clonable information into clonable information — the transition from private to public. This is irreversible: once the phase is projected out by making the result public, it can't be recovered (the phase was the observer's self-referential ignorance, now replaced by a shared definite fact).

**Decoherence follows for free.** When a quantum system interacts with a large environment, information about the system gets copied (FANOUT) into many environmental degrees of freedom. The "classical" part (real, clonable) distributes consistently. The phase information doesn't survive because each environmental subsystem has its *own* self-referential ignorance, and these are all different. The complex phases — being observer-relative — don't add up coherently across different observers. They average to zero. Decoherence is the washing out of the private epistemological component when many independent observers each get their own classical copy.

### Resolution of the measurement problem

"When does collapse happen?" becomes "When does FANOUT happen?" — an operational question with a definite answer: when the measurement result becomes available for copying, i.e., when it enters a classical channel. The boundary is precisely the FANOUT boundary = the boundary between special and anti-special Frobenius algebras = the boundary between GHZ-class and W-class entanglement. No vague macroscopic/microscopic boundary needed.

### Strategic importance for the paper

Without FANOUT, the epistemological-to-ontological transition looks hand-wavy, and critics will say "this is just QBism." With FANOUT, it's operationally precise: the classical/quantum boundary is the clonability boundary. This pre-empts the standard inter-subjective agreement objection against QBism: objectivity *emerges* from clonability. You don't postulate it.

**Note:** The FANOUT criterion dates to John's 2007 MSc dissertation. It was omitted from the Växjö posters (2022-2025). Must be included in the paper.

---

## 4. Teleportation Analysis

### Standard teleportation in the framework's language

Three operationally distinct steps, each handling a different kind of information:

1. **Entangled pair establishes shared private context.** A correlation between Alice's and Bob's self-referential structures that neither can individually read out. This is a pre-existing alignment of their private epistemological frames.

2. **Bell measurement extracts relative phase as classical bits.** Alice's Bell measurement has four outcomes decomposing into two binary questions: is there a bit flip? Is there a phase flip? These encode the *relative* phase between the unknown state and Alice's half of the pair. Crucially, this is relative phase — not absolute phase. Relative phase between two quantum states is classical information that can be extracted, communicated, and copied. Absolute phase remains private.

3. **Bob's correction aligns his private frame.** The two classical bits are a coordinate transformation label: "your reference frame is related to the one in which the original state was defined by Pauli rotation number n." Bob rotates his own private frame into alignment with Alice's original one.

### Key insight: Bell measurement reveals phase *difference*

The Bell measurement extracts the phase difference between the unknown state and the shared reference frame established by the Bell pair. This maps onto the framework's three-level hierarchy:

- **Absolute phase:** Private, non-communicable. The S¹ fibre, gauge freedom, epistemological component projected out by the Hopf map.
- **Relative phase:** Extractable as classical information. What interference experiments and Bell measurements access.
- **Measurement outcomes (base space S²):** Fully public and clonable. Ontological facts.

### Why teleportation requires both channels

The entangled pair alone gives shared private context but no way to align it with a specific measurement outcome. The classical channel alone gives public information but no private context to apply it to. You need both because the protocol converts between private and public information, requiring a bridge between the two domains.

### Why teleportation supports the epistemological interpretation

If the complex phase were an intrinsic ontic property, it would be mysterious that it can be "moved" between physical systems by purely informational means (a shared correlation plus two classical bits). If the phase is a *relationship between observer and observed* — a property of the epistemic frame — then of course it can be transferred by transferring the frame. You're not moving a thing; you're telling someone how to hold the map.

### Reference frame alignment — hidden requirements

Teleportation protocols assume Alice and Bob share a reference frame (agreed Z direction, agreed handedness). This is never discussed in textbook treatments but represents substantial shared classical information.

**Z direction alignment:** Nearby observers can point at the same wall. As separation increases, increasingly remote objects are needed. Cosmologically separated observers need the entire visible sky (CMB dipole, distant quasars). This is Mach's principle arriving through quantum information theory — the local definition of "which way is Z" depends on distant matter.

**Handedness alignment:** This is a discrete choice (right-hand vs left-hand rule) that cannot be established by triangulation. The *only* physical process distinguishing left from right is the weak interaction (parity violation). Without the weak force, handedness would be purely conventional, and this part of the teleportation protocol would require prior co-location.

In the framework, weak force chirality is derived from the self-consistency of the biquaternion embedding (the parity-symmetric phase produces two decoupled spacetimes, which is relationally inconsistent). So the ability of separated observers to agree on handedness — a prerequisite for teleportation — depends on the same self-consistency requirement that gives rise to the weak force.

### Reference frame alignment cost as spatial distance

**Key observation (to be developed further):** The amount of classical information required to align two reference frames increases with separation. This looks like an information-theoretic definition of spatial distance: distance = minimum classical communication cost of frame alignment, measured in bits.

This fits with the framework's treatment of space as the computable causal structure of the relational network. It gives a concrete operational meaning to c as the bound on how fast shared objectivity can be established.

Another author has recently published on this idea — John is looking up the reference. Whether they come at it from a similar direction or from holographic/operational quantum gravity considerations matters for how to engage with it in the paper.

---

## 5. The Problem of Time — Rule 𝒜 / Rule ℬ Analysis

### The obstruction

Quantum mechanics requires a global time parameter for unitary evolution: U(t) = e^{−iHt} requires t to mean the same thing everywhere. This is derived in the framework — probability conservation on a complex Hilbert space forces unitarity, which forces a global "in the future."

Special relativity provides this: Minkowski spacetime has global causal structure. Different inertial observers disagree about *how much* time, but agree on *which comes first* for timelike-separated events.

General relativity does not provide this: no preferred foliation; possible CTCs; "state at time t" is observer-dependent.

### Rule 𝒜 vs Rule ℬ decomposition

- **Rule 𝒜** (no supertasks): Requires global time parameter. Gives ℏ. Makes QM possible. A *global* rule.
- **Rule ℬ** (no causal loops): Requires only local causal structure. Gives c. Gives light cones. Does *not* require global time ordering.

General relativity respects Rule ℬ but not Rule 𝒜 (local light cones but no global time). Quantum mechanics respects Rule 𝒜 but struggles with Rule ℬ's local-only character (wants a global "now" for the Hilbert space).

### The ontological-epistemological split

- **GR** treats spacetime epistemologically (hole argument: spacetime points have no intrinsic identity).
- **SR** treats spacetime ontologically (Minkowski spacetime is a fixed background).
- **QM** inherits SR's ontological treatment because it needs a global time parameter.

Canonical quantum gravity fails because it tries to make epistemological (GR) spacetime play the role of ontological (QM) time. The Wheeler-DeWitt equation H|ψ⟩ = 0 is the Schrödinger equation without preferred time — it says nothing ever happens.

### The framework's resolution

Any successful quantum gravity theory must be purely epistemological — deriving *both* the global time ordering (QM needs) and local causal structure (GR needs) from the self-referential computational structure. Time as computation does this: the global tick is completion of one minimal irreversible computational loop (Rule 𝒜), and local causal structure emerges from finite propagation speed through the network (Rule ℬ). Neither is ontological background.

The "problem of time" is an artefact of mixing ontological and epistemological descriptions.

---

## 6. Popescu-Rohrlich and the Tsirelson Bound

### The question

Quantum correlations violate Bell inequalities up to the Tsirelson bound 2√2, but no-signalling alone permits violations up to 4 (PR boxes). What constrains quantum correlations beyond no-signalling?

### The Hopf geometry answer

The two-qubit state space is S⁷ (unit sphere in ℂ⁴). The CHSH operator's maximum eigenvalue is 2√2, determined by the operator norm on ℂ⁴, which is determined by the division algebra norm of ℂ. A PR box would require correlations exceeding this geometry — it would require a state space not arising from any normed division algebra.

The Tsirelson bound is a geometric consequence of the Hopf fibration structure, which is forced by self-reference. It's not an empirical fact requiring an additional principle — it's a theorem about what the Hopf geometry permits.

Alternative theories (generalised probabilistic theories) with stronger-than-quantum correlations have state spaces that are not Hilbert spaces over ℂ. The framework says these are unavailable because they can't consistently represent self-referential knowledge. Once you have ℂ, the Tsirelson bound comes free.

### Paper strategy

Mention briefly in the main text (one or two sentences). Defer full derivation to an appendix or the second paper. Signals the framework's scope without breaking narrative flow. The Popescu-Rohrlich question is well-known enough in the quantum foundations community that even a brief mention will catch attention.

---

## 7. Logical Structure of the Paper's QM Derivation Section

The recommended arc for the paper:

1. Self-reference → observer must assign probability to own state → negative probability
2. Negative probability + epistemological character → Shannon information → analytic continuation → complex amplitudes (**Postulate 1: complex Hilbert space**)
3. Complex phase = observer's self-referential ignorance → private, non-clonable (FANOUT criterion)
4. Measurement results must be communicable → real-valued → **Postulate 2: Hermitian observables**
5. Probabilities must be U(1)-invariant → minimum degree 2 → **Postulate 3: Born rule** (Hopf derivation, half a page)
6. Both real and complex components epistemological → measurement updates knowledge → **Postulate 4: state reduction** (Bayesian updating; FANOUT converts private to public)
7. Probability conservation → inner product preservation → **Postulate 5: unitary evolution** → Schrödinger equation via Stone's theorem
8. Cayley-Dickson doubling → multiplicative composition → **Postulate 6: tensor product**
9. Brief mention: Tsirelson bound follows from Hopf geometry → resolves Popescu-Rohrlich (pointer to appendix)

Each step follows from the previous by a single logical move. Total length: perhaps 3-4 pages.

---

## 8. Items for Follow-Up

- **Look up the author** working on information-theoretic definition of spatial distance (reference frame alignment cost). Engage with their work in the paper.
- **Read Coecke & Kissinger** *Picturing Quantum Processes* (2017) properly — specifically the Frobenius algebra / spider diagram formalism and its relation to FANOUT / classical-quantum boundary.
- **Verify Born rule Hopf argument novelty** against literature before claiming it in the paper. Check Mosseri & Dandoloff (2001), Urbantke, and related differential geometry literature for whether the "degree-1 invariants don't exist" point has been made explicitly.
- **Separability of Hilbert space**: Make the computability argument explicit — can a non-separable Hilbert space arise from a computable self-referential structure?
- **FANOUT in the paper**: Must be included prominently. Dates to 2007 dissertation. Pre-empts the QBism inter-subjective agreement objection.

---

*Session: 27 March 2026. Topics: QM postulates derivation, Born rule from Hopf map, FANOUT criterion, teleportation analysis, reference frame alignment, problem of time, Tsirelson bound.*
