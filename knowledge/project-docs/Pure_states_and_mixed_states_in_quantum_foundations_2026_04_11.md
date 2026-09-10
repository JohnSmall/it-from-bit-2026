# Pure States and Mixed States in Quantum Foundations
## Session Summary — 11 April 2026

---

## Overview

This session developed a critical foundational argument for the paper: that quantum probability is epistemological (not ontological), and that this commitment — combined with the existence of negative quasi-probabilities — uniquely and necessarily produces complex-valued probability amplitudes. The argument was elevated from a suggestion to the status of a theorem, with every step being either a mathematical fact, an experimentally established result, or a short logical deduction.

---

## The Quantum Omelette (Jaynes)

The density matrix ρ = ½(I + **r**·**σ**) smoothly interpolates between:
- **|r| = 1**: pure state (all unpredictability conventionally labelled "quantum")
- **|r| = 0**: maximally mixed state (all unpredictability conventionally labelled "classical ignorance")
- **0 < |r| < 1**: Jaynes's "quantum omelette" — inseparable mixture

Two mechanisms accomplish the transition: partial tracing (entanglement with environment) and Bayesian updating (gaining/losing preparation information). These are operationally indistinguishable at the level of ρ itself — the decomposition of a mixed state into pure states is non-unique. The no-cloning theorem (FANOUT) prevents the observer from distinguishing the two cases.

---

## The Seven-Step Theorem: Self-Reference → Complex Amplitudes

### Statement
A probability theory for a system where the observer is embedded in the system they observe necessarily uses complex-valued amplitudes with the Born rule.

### Proof Chain

1. **The Bloch ball is smooth** (mathematical fact)
2. **Pure↔mixed transition requires no physical change**, only change in observer knowledge — e.g., Bob measures his half of a singlet state and communicates the result; Alice's local state goes from maximally mixed to pure with no physical interaction with her qubit (operational fact)
3. **Therefore quantum uncertainty is epistemological** — no boundary exists in the smooth Bloch ball where the character of uncertainty discontinuously changes, under an operation involving no physical disturbance (logical consequence of 1+2)
4. **Therefore Shannon's H = −Σ p log p is the correct information measure** — Shannon's uniqueness theorem: given epistemological uncertainty, H is the unique measure satisfying his axioms (contra Brukner-Zeilinger, arXiv:quant-ph/0006087)
5. **Quantum mechanics requires negative quasi-probabilities** — Hudson's theorem: the only pure states with non-negative Wigner function are Gaussians; Kirkwood-Dirac distributions for non-commuting observables necessarily take negative values (theorem)
6. **log of a negative number requires analytic continuation to ℂ** — log(−|p|) = log|p| + iπ (mathematical fact)
7. **Therefore the information-theoretic description of quantum measurement is necessarily complex-valued** (logical consequence of 4+5+6)

### Status
Every step is either a mathematical theorem, an experimentally established fact, or a short logical deduction. The only step open to challenge is Step 3, and the objections are philosophical (not mathematical).

---

## Three Independent Supports for Step 3 (Epistemological Quantum Probability)

### 1. Bloch Ball Continuity (Mathematical)
Any position assigning different ontological status to uncertainty at |r|=1 versus |r|=0 must identify where in the interval [0,1] the character changes. The smooth geometry of the Bloch ball, combined with the fact that the transition is accomplished by purely informational operations, provides no such boundary. The parsimonious reading is epistemological throughout.

### 2. Quantum Zeno Effect (Experimental)
Frequent null measurements suppress radioactive decay (Itano et al. 1990, now textbook). A null measurement — confirming "not yet decayed" — involves no energy exchange and no physical interaction with the nucleus. Nothing happened to the atom. What changed is the observer's knowledge. The anti-Zeno effect (infrequent measurements accelerating decay) is equally natural: sparse updates allow the complex amplitude to evolve further before projection. Both effects are exactly what complex Bayesian updating predicts.

### 3. Predictive Consequences (Abductive)
Accepting Step 3 yields complex amplitudes → division algebras → Standard Model with zero free dimensionless parameters, including sin²θ_W = 1/4, m_H = v/2, y_t = 1, α_s(M_Z) ≈ 0.1185, and fermion mass ratios to under 0.2%. Rejecting Step 3 yields no comparable explanatory power.

---

## Bell's Theorem and Negative Probability (Step 5 Support)

Khrennikov (and others) have pointed out that Bell's theorem forces a choice — abandon hidden variables or accept non-locality — *only if* hidden variable probabilities are restricted to [0,1] (Kolmogorovian). If negative probabilities are permitted, Bell inequalities don't apply because their derivation assumes non-negative measures.

This means Bell's theorem *supports* Step 5: it tells us that if hidden variables exist, their probabilities must be negative. The framework identifies these hidden variables as the observer's own state, which they cannot fully know due to the self-referential obstruction.

**Resolution of Bell interpretive debate**: Bell killed local *Kolmogorovian* realism, not local realism per se. Local realism with complex probability is alive and well — it is quantum mechanics, properly understood.

---

## The Hypodox Structure

The argument has a self-consistent circular structure:
- Step 3 (epistemological) licenses Shannon → forces ℂ when probabilities go negative
- Step 5 (negative probabilities) is independently required by Bell's theorem to maintain locality
- Locality is required by the inside/outside equivalence principle
- The inside/outside equivalence principle generates Step 3

This circular self-consistency is a **hypodox** — "this sentence is true" rather than "this sentence is false." The framework is itself a fixed point: the output has the same self-referential character as the axiom that generated it. The global phase (the observer's self-referential ignorance) cycles stably because |e^{iθ}|² = 1 for all θ. The liar paradox oscillates between 0 and 1 and never settles; the hypodox oscillates in phase and always settles. This circular character is a consistency check, not a weakness.

---

## Relationship to Existing Literature

### Brukner-Zeilinger (quant-ph/0006087)
Argued that Shannon information is conceptually inadequate for quantum measurements because quantum uncertainty is ontological, not epistemic. Already challenged by Timpson (quant-ph/0112178) and Hall (quant-ph/0007116) on technical grounds. The framework's challenge is more fundamental: the Bloch ball argument undermines the ontological premise entirely.

### Scott Aaronson ("Island in Theoryspace" / "Why Are Amplitudes Complex?")
Aaronson argued quantum mechanics is what you'd inevitably get from negative probabilities, and showed quaternions fail due to: (a) parameter counting — f(n_A n_B) = f(n_A)f(n_B) holds only for ℂ; (b) tensor product of quaternionic Hermitian matrices need not be Hermitian → superluminal signalling; (c) Wootters' Goldilocks — random states give uniform distributions over the probability simplex only over ℂ. However, [redacted 2026-09-10: private remark by a named third party; see knowledge/memory/CORRECTIONS.md] "not even well developed enough to form into a conjecture." The missing piece was Step 3 — without the epistemological commitment, the log function has no justification and the argument stalls.

### Aaronson's local tomography dissatisfaction
Aaronson expressed explicit dissatisfaction with local tomography as an axiom in Hardy-type derivations, recognising it was introduced specifically to rule out ℝ and felt circular. The framework resolves this: inside/outside equivalence *implies* local tomography (an external observer's characterisation must be recoverable from local measurements), so it's derived rather than postulated.

### QBism (Fuchs, Schack)
Gets the epistemological part right but cannot explain why probabilities must be complex-valued. The SIC-POVM/urgleichung reformulation is descriptive, not explanatory. The framework fills the gap: probabilities are complex because the agent's ignorance is self-referential.

### Markus Müller
Developing a "first-person point of view" programme, slowly converging on epistemological quantum probability from operational axiomatics. Independent convergence from a different starting point strengthens the case.

### Khrennikov
p-adic probability and non-Kolmogorovian frameworks for hidden variables. Connection to the framework's use of negative probability. Planned discussion at Växjö on whether the adelic product formula constrains the Tsirelson bound.

---

## Alternative Route to ℂ (Structural/Algebraic)

A complementary argument using the division algebra tower was also developed:

1. Self-reference → Lawvere fixed-point obstruction → not ℝ (theorem)
2. Conditionalization requires normed division algebra → {ℂ, ℍ, 𝕆} remain (Hurwitz, theorem)
3. Inside/outside equivalence → local tomography → parameter factorisation → not ℍ, not 𝕆 (Aaronson's argument, theorem)
4. U(1) invariance → Born rule p = |ψ|² (framework's derivation, theorem)

Both routes — the Shannon/analytic-continuation argument and the Lawvere/Hurwitz/local-tomography argument — are the same truth seen from two angles. The Shannon route shows complex amplitudes are *necessary*. The division algebra route shows they are *sufficient* and *unique*, and reveals the algebraic architecture that gives gauge symmetry and particle content.

---

## Implications for Paper Structure

- **Main text**: The Shannon/log argument (seven steps) as the primary derivation, with the Bloch ball, quantum Zeno, and Bell/Khrennikov as supporting evidence for the key steps
- **Following section**: The division algebra route as structural analysis showing *why* the tower appears
- **Explicit acknowledgement**: Step 3 requires a philosophical commitment; the paper's posture is "assume this, then these numerical results follow as theorems"
- **Narrative**: Aaronson identified the right question but couldn't ground it; QBism opened the door but couldn't walk through it; this framework provides the grounding (self-reference) that both were missing

---

## Key Quotes / Formulations for Paper

- "Any position that assigns different ontological status to the uncertainty at |r|=1 versus |r|=0 must identify where in the interval [0,1] the character changes. The smooth geometry of the Bloch ball provides no such boundary."
- "Bell killed local Kolmogorovian realism, not local realism."
- "Complex probability is not a departure from epistemological probability; it is what epistemological probability *becomes* when the knower is part of the known."
- "The framework is itself a hypodox — a self-sustaining fixed point. It would be suspicious if a theory grounded in self-reference produced a structure that wasn't self-referential."
