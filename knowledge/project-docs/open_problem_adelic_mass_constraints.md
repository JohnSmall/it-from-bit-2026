# Open Problem: Adelic Constraints on Particle Masses from Division Algebra Structure

## Statement

**Conjecture (Adelic mass consistency).** The fermion mass ratios derived from octonionic geometry in the Archimedean completion ℝ are subject to non-trivial constraints from the non-Archimedean (p-adic) completions ℚ_p via the adelic product formula. These constraints have never been examined.

More broadly: the division algebra chain ℝ → ℂ → ℍ → 𝕆 and the associated parallelisable spheres S¹, S³, S⁷ have been studied exclusively over ℝ. But Ostrowski's theorem guarantees that for every algebraic or rational quantity determined by this structure, there exists a p-adic counterpart for each prime p, and the adelic product formula ∏_v |x|_v = 1 locks these together. The physical consequences of this locking — particularly for mass ratios, coupling constants, and the computability split — constitute an unexplored domain.

## Background

### The two completions of the rationals

Ostrowski's theorem (1918) classifies all non-trivial absolute values on ℚ: up to equivalence, they are the usual absolute value |·|_∞ (Archimedean) and the p-adic absolute values |·|_p for each prime p (non-Archimedean). Completing ℚ with respect to these yields ℝ and ℚ_p respectively. These are the *only* completions.

The adelic ring 𝔸_ℚ = ℝ × ∏'_p ℚ_p (restricted product) unifies all completions into a single object. The product formula

∏_{v} |x|_v = 1

valid for all x ∈ ℚ×, expresses the fact that the Archimedean and non-Archimedean information about a rational number are not independent — they are complementary.

### Division algebras and the Archimedean sector

The framework derives particle physics from the division algebra chain ℝ → ℂ → ℍ → 𝕆, which terminates by three independent theorems (Adams, Hurwitz, Coecke–Kissinger). This entire construction lives in the Archimedean completion. The key results — Bott periodicity, the Hopf fibrations, the parallelisability of S¹, S³, S⁷, and the mass formulas derived from octonionic geometry — are all proved over ℝ or ℂ.

### p-Adic quantum mechanics

Khrennikov, Volovich, Dragovich and collaborators have developed p-adic and adelic quantum mechanics over several decades. Key results include:

- Negative probabilities are well-defined within p-adic probability theory in the frequency interpretation (Khrennikov 1995), providing an alternative to the complex amplitude route.
- p-Adic path integrals and spectral theory have been constructed for quadratic Lagrangians (Vladimirov & Volovich 1989).
- The adelic harmonic oscillator is related to the Riemann zeta function (Dragovich 1995).
- p-Adic models predict correlations between particles in interference experiments that differ from standard quantum mechanics (Khrennikov 2009).

### The gap

These two programmes — division algebra particle physics and p-adic quantum mechanics — have developed in complete isolation. No one has asked:

1. What happens to the Hurwitz theorem, Adams' theorem, or the parallelisability of spheres over ℚ_p?
2. What p-adic constraints does the adelic product formula impose on division-algebra-derived mass ratios?
3. Whether the ultrametric (tree-like) structure of p-adic spaces has a structural relationship to the binary tree of Cayley–Dickson doublings.

## The Connection to Non-Computability

The framework identifies the computability split ℂ ⊂ 𝕆 as the Higgs mechanism — a Wick rotation from computable to non-computable content. There is a natural parallel with the Archimedean/non-Archimedean split:

- **Archimedean completion (ℝ):** Information extends to the right of the decimal point. Truncation gives computable approximations that converge. This is the sector where measurements live and where the division algebra chain operates.

- **Non-Archimedean completion (ℚ_p):** Information extends to the left. A generic p-adic number has infinitely many digits to the left, and fully specifying it requires completion of an infinite process — a supertask. The p-adic completion is literally the number system you get when you allow supertasks to complete.

In the framework's language: the Archimedean sector houses the computable content (Rule 𝒜 — no supertasks); the non-Archimedean sector houses the non-computable content (where supertasks have completed). The adelic product formula then becomes a consistency condition between the computable and non-computable sectors — precisely the kind of constraint the framework predicts should exist at the QM/GR interface.

## Specific Open Problems

### Problem 1: Adelic product formula applied to mass ratios

The framework derives fermion mass ratios as algebraic functions of octonionic geometric invariants, with zero free parameters. These ratios are algebraic numbers (roots of polynomials with rational coefficients). For any such ratio r ∈ ℚ̄, the product formula constrains the p-adic absolute values:

|r|_∞ · ∏_p |r|_p = 1.

**Question.** Do the p-adic valuations of the predicted mass ratios exhibit any structure — for instance, are they constrained to be p-adic integers (|r|_p ≤ 1) for all but finitely many primes, and if so, which primes are exceptional? Do the exceptional primes have any relationship to the dimensions of the division algebras (1, 2, 4, 8) or the structure constants of the octonion algebra?

This question is well-posed and computationally checkable given explicit mass ratio formulas.

### Problem 2: Division algebra theorems over ℚ_p

The three theorems that terminate the division algebra chain are proved over ℝ:

- **Hurwitz (1898):** The only normed division algebras over ℝ are ℝ, ℂ, ℍ, 𝕆.
- **Adams (1960):** Only S⁰, S¹, S³, S⁷ are parallelisable.
- **Coecke–Kissinger (2010):** GHZ and W are compositionally complete.

**Question.** What are the analogues of these theorems over ℚ_p? Specifically:

(a) Do normed division algebras over ℚ_p terminate at the same point? The Cayley–Dickson construction can be performed over any field — over ℚ_p, the resulting algebras may have different properties (e.g., the sedenions might fail to be a division algebra for different reasons, or might fail at a different stage for certain primes).

(b) The statement "S^n is parallelisable" depends on the topology of the sphere, which is defined over ℝ. Is there a p-adic analogue of parallelisability (perhaps via Berkovich spaces or rigid analytic geometry) and if so, does it terminate at the same dimensions?

(c) Adams' theorem uses real Bott periodicity (period 8 in KO-theory). Algebraic K-theory provides p-adic analogues of Bott periodicity. Do these p-adic periodicities carry physical information — for instance, do they constrain the number of generations or the structure of flavour mixing?

### Problem 3: Ultrametric trees and the Cayley–Dickson construction

The p-adic integers ℤ_p have a natural tree structure: the p-ary tree, where each node branches into p children corresponding to the p possible digits at that level. The Cayley–Dickson construction is a binary tree: each doubling ℝ → ℂ → ℍ → 𝕆 → 𝕊 adds one level of branching.

**Question.** Is there a precise categorical or algebraic relationship between:

(a) The 2-adic tree (the tree structure of ℤ₂), which branches binarily, and the Cayley–Dickson doubling tree, which also branches binarily?

(b) The Moufang loop structure of the unit octonions and the structure of the 2-adic integers as a profinite group?

(c) The "Seven Rights Can Make a Left" property of the octonionic Moufang loop (which encodes the 480 valid multiplication tables) and the 2-adic valuation of the relevant combinatorial numbers?

The prime p = 2 is distinguished here because the Cayley–Dickson construction doubles dimensions (multiplies by 2), and Bott periodicity has period 8 = 2³.

### Problem 4: p-Adic negative probability and the self-referential framework

Khrennikov showed that p-adic probability provides a rigorous frequency interpretation of negative probabilities. The framework derives negative probabilities from self-reference via the Lawvere–Yanofsky diagonal structure, leading to complex probability amplitudes.

**Question.** Are these two routes to negative probability — complex amplitudes (Archimedean) and p-adic probabilities (non-Archimedean) — related by the adelic product formula? Specifically:

(a) If a quasi-probability distribution takes negative values in the Wigner function representation (Archimedean), what are the constraints on its p-adic counterpart imposed by the product formula?

(b) Can the Born rule derivation from the Hopf fibration (global phase = self-referential ignorance → U(1) invariance → p = |ψ|²) be replicated in the p-adic setting, and if so, what replaces the Hopf fibration?

(c) The framework's FANOUT criterion (clonability of information as the boundary between epistemological and ontological) operates in the Archimedean sector. Is there a p-adic FANOUT criterion, and does it identify the same boundary?

### Problem 5: The distinguished role of specific primes

**Question.** Do the primes p = 2, 3, 5, 7 play a distinguished role in p-adic quantum mechanics when applied to the division algebra framework?

Motivation: The parallelisable spheres have dimensions 1, 3, 7, which are Mersenne numbers 2^k − 1 for k = 1, 2, 3, and the division algebras have dimensions 1, 2, 4, 8 = 2^k for k = 0, 1, 2, 3. The primes dividing these dimensions and their nearest neighbours are exactly {2, 3, 5, 7}. Whether this is numerology or structure is an open question, but it is at least well-posed: one can examine whether ℚ₂, ℚ₃, ℚ₅, ℚ₇ exhibit different algebraic properties when the Cayley–Dickson construction is performed over them.

## Why This Has Not Been Considered Before

The division algebra programme in particle physics (Dixon, Furey, Krasnov, Dubois-Violette, Boyle, Szangolies) works exclusively over ℝ and ℂ. The p-adic physics programme (Khrennikov, Volovich, Dragovich, Zelenov) works with p-adic analogues of standard quantum mechanics without reference to division algebras or parallelisable spheres. The two communities attend different conferences, cite different literatures, and frame their questions differently.

The bridge between them requires a framework that simultaneously:

1. Takes the division algebra chain as fundamental to particle physics;
2. Takes non-computability as fundamental to quantum mechanics;
3. Recognises that the Archimedean/non-Archimedean split maps onto the computable/non-computable split.

The self-referential framework satisfies all three conditions, making this connection natural within it and invisible from either side independently.

## Resolution Criteria

The problems above range from computationally checkable (Problem 1 — apply the product formula to explicit mass ratios) to structurally deep (Problem 3 — categorical relationship between two tree structures). Minimal progress would consist of:

**(A)** Computing the p-adic valuations of the framework's predicted mass ratios and identifying any structure in the results.

**(B)** Performing the Cayley–Dickson construction explicitly over ℚ₂ and determining at which stage it ceases to produce a division algebra, and whether the failure mode differs from the real case.

**(C)** Determining whether the adelic harmonic oscillator (which connects to the Riemann zeta function) has any relationship to the framework's mass formulas when the oscillator frequencies are identified with the Zitterbewegung frequencies of fermions.

Any of these would constitute the first result connecting division algebra particle physics to p-adic analysis.

## Significance

If the adelic product formula imposes non-trivial constraints on division-algebra-derived mass ratios, this would:

1. Provide an independent cross-check on mass predictions from a completely different mathematical direction.
2. Connect the framework's computability arguments to the rigorous p-adic probability theory developed by Khrennikov and collaborators.
3. Open a large new domain of open problems at the intersection of number theory, quantum foundations, and particle physics — one that has been invisible because the prerequisite bridge between the two programmes did not exist.

The key observation for the community is simply this: **the adelic product formula applied to geometrically-determined mass ratios implies non-trivial p-adic constraints that have never been examined.**

## References

- Adams, J.F. "On the non-existence of elements of Hopf invariant one." Ann. Math. 72, 20–104 (1960).
- Dragovich, B. "Adelic harmonic oscillator." Int. J. Mod. Phys. A10, 2349 (1995).
- Dragovich, B. "Adeles in mathematical physics." arXiv:0707.3876 (2007).
- Hurwitz, A. "Über die Composition der quadratischen Formen von belibig vielen Variablen." Nachr. Ges. Wiss. Göttingen, 309–316 (1898).
- Khrennikov, A.Yu. "p-Adic description of Dirac's hypothetical world with negative probabilities." Int. J. Theor. Phys. 34, 2423–2434 (1995).
- Khrennikov, A.Yu. "Interpretations of probability and their p-adic extensions." Theory Probab. Appl. 46(2), 256–273 (2002).
- Khrennikov, A.Yu. "p-Adic probability prediction of correlations between particles in interference experiments." arXiv:0906.0509 (2009).
- Khrennikov, A.Yu. "Interference of probabilities and number field structure of quantum models." Ann. Phys. (Leipzig) 12, 575–585 (2003).
- Ostrowski, A. "Über einige Lösungen der Funktionalgleichung φ(x)·φ(y) = φ(xy)." Acta Math. 41, 271–284 (1918).
- Vladimirov, V.S. & Volovich, I.V. "p-Adic quantum mechanics." Comm. Math. Phys. 123, 659–676 (1989).
- Vladimirov, V.S., Volovich, I.V. & Zelenov, E.I. *p-Adic Numbers in Mathematical Physics.* World Scientific, Singapore (1994).
- Volovich, I.V. "p-Adic string." Class. Quantum Grav. 4, 83–87 (1987).

## Natural Audience

This problem would be of particular interest to Andrei Khrennikov (Linnaeus/Växjö — p-adic probability and quantum foundations), Branko Dragovich (Belgrade — adelic quantum mechanics), Cohl Furey (Humboldt — division algebra particle physics), and Tim Palmer (Oxford — Invariant Set Theory, which independently uses p-adic-like structures in its non-computable dynamics). The Växjö quantum foundations conference — where both the p-adic probability programme and the self-referential framework have been presented — is a natural venue for initiating this cross-pollination.
