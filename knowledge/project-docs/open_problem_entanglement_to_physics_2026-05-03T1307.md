# Open Problem: The Dual Direction — Outstanding Problems in Entanglement Classification via the Particle-Physics Dictionary

## Statement

**Conjecture (Bidirectional dictionary).** The structural correspondence between multipartite entanglement classes and particle-physics composites — established empirically by the Imperial College "black holes and qubits" programme and given a self-referential foundation by the present framework — runs in both directions. Outstanding problems in n-qubit entanglement classification admit derivations through the dictionary that import constraints from gauge invariance, confinement, the Hopf fibration tower, and the termination of normed division algebras at 𝕆, supplying structural reasons currently absent from the quantum-information literature where such results are typically established by case-by-case analysis of polynomial invariants or U-duality orbits.

## Background

### The forward direction is established

The connection between entanglement classification and particle physics has been developed extensively over fifteen years by the Imperial College group (Borsten, Duff, Hughes, Marrani, Rubens) together with Ferrara, Lévay, and others, under the heading *black holes and qubits*. Key results include:

- **Three qubits ↔ STU black holes (Duff 2007).** The Cayley hyperdeterminant Det(a_{ABC}) classifying three-qubit entanglement coincides with the Bekenstein–Hawking entropy formula for N = 2 STU black holes. The shared symmetry is [SL(2)]³.

- **Seven qubits ↔ N = 8 black holes (Duff & Ferrara 2007).** The tripartite entanglement of seven qubits arranged on the Fano plane carries an E₇ structure, with Cartan's quartic invariant J₄ playing the role of both the entanglement measure and the black hole entropy.

- **Three qutrits ↔ D = 5 N = 8 black holes (Duff & Ferrara 2007).** The bipartite entanglement of three qutrits is governed by E₆ and Cartan's cubic invariant J₃.

- **Four qubits via U-duality (Borsten, Dahanayake, Duff, Marrani, Rubens 2010).** The classification of four-qubit SLOCC orbits is recovered from timelike reduction of string theory D = 4 → D = 3, yielding 31 entanglement families that reduce to 9 up to permutation of the qubits — agreeing with the Verstraete–Dehaene–De Moor–Verschelde classification.

- **Magic supergravities and the division algebra ladder.** The R, C, H, O magic supergravities in D = 4 and D = 5 produce parallel structures with symmetries Sp(6), SU(3,3), SO*(12), E₇₍₋₂₅₎ and SL(3,R), SL(3,C), SL(3,H), SL(3,O) respectively, exhibiting the same division-algebra organisation that the present framework derives from self-reference.

That the connection is real and structural is no longer a controversial claim. It has a literature and a sustained research programme.

### The unexplained "why"

What the Imperial-group literature explicitly does not provide is an explanation of *why* these correspondences exist. Duff and Ferrara (2007), in the conclusion of "E₆ and the bipartite entanglement of three qutrits," state plainly:

> *Our analogy between black holes and quantum information remains, for the moment, just that. We know of no physics connecting them.*

The same paper records a private communication from Murat Gunaydin suggesting that the appearance of octonions and split octonions in the magic supergravities "implies a connection to quaternionic and/or octonionic quantum mechanics" — a pointer that has not been systematically developed in the intervening two decades.

The present framework supplies the missing connection: both halves of the dictionary are downstream of the same self-referential constraint that singles out the normed division algebras (ℝ, ℂ, ℍ, 𝕆), and the Hopf fibration tower these algebras support. The framework's Cayley-Dickson qubits — A as ℂ-qubit, B as ℍ-qubit, C as 𝕆-qubit — realise the Gunaydin pointer concretely, with the layered structure derived rather than imposed.

### The dual direction is open

While the forward direction (use entanglement classification to organise particle-physics composites) has been worked extensively in both literatures, the dual direction — use particle-physics constraints to *solve* outstanding problems in entanglement classification — has not been systematically pursued. Yet the asymmetry between what is technically hard on each side is suggestive: results that require lengthy case-by-case analysis on the QI side often correspond to one-line topological observations on the particle-physics side, and vice versa.

This document proposes the dual direction as a research programme, with a concrete worked example (AME(4,2) non-existence) demonstrating that the programme has content.

## Precise Formulation

**Dual-direction problem.** Identify outstanding problems in multipartite entanglement classification that admit derivations through the framework's particle-physics dictionary. For each such problem, the resolution should:

(D1) State the QI question intrinsically (in the language of SLOCC orbits, Frobenius algebras, polynomial invariants, or topological monotones).

(D2) Translate via the dictionary into a particle-physics statement (about gauge invariance, confinement, Hopf bundle topology, division-algebra termination, or composite-particle representation theory).

(D3) Resolve the particle-physics statement using tools standard in that domain.

(D4) Translate the resolution back to the QI side and verify it agrees with whatever is independently known.

A successful resolution provides a *structural* proof — typically much shorter than the original QI proof — and exposes the underlying reason for the result in a form unavailable from the QI side alone.

### Candidate sub-problems

Concrete instances where the dual direction appears tractable:

**(P1) AME(4,2) non-existence.** Higuchi & Sudbery (2000) proved that no four-qubit pure state has all two-qubit reductions maximally mixed. The proof works through polynomial invariants of the SLOCC group. Treated as a worked example below.

**(P2) The Verstraete count of 9 four-qubit SLOCC families.** Borsten et al. (2010) recovered this count via U-duality but required string-theoretic machinery (timelike reduction, E₇ orbit structure). The framework should recover the count from Frobenius spider tree composition under sedenion-zero-divisor topological obstruction, without invoking string theory.

**(P3) Generators of the SLOCC invariant ring for n ≥ 4.** Empirically the ring has a complicated structure with no canonical generating set in the QI literature. The conjecture is that these generators are the entanglement projection of a hadronic invariant ring (Casimir invariants of the gauge groups acting on composite states), and that the SU(3) × SU(2) × U(1) representation theory fixes their count and structure.

**(P4) The generic-vs-degenerate distinction within Verstraete families.** The continuous parameters within each four-qubit family (e.g. a, b, c, d in G_{abcd}) should map to coupling constants in the hadronic interpretation, with degenerate orbits corresponding to bound-state composites and generic orbits to scattering states.

**(P5) Higher AME existence (AME(n,d)).** A systematic catalogue of which AME(n,d) states exist and which do not, derived structurally from the framework's monogamy and topological-obstruction theorems.

## Partial Evidence: AME(4,2) as Worked Example

This section establishes that the dual direction has content by treating one case in full.

### The QI statement

A pure state |ψ⟩ of n qudits of local dimension d is *absolutely maximally entangled* (AME) if every reduced density matrix on ⌊n/2⌋ parties is maximally mixed. The state |ψ⟩ is AME(n,d). For n = 4, d = 2, the requirement is that every two-qubit reduction equals I/4.

Higuchi and Sudbery (2000) proved that AME(4,2) does not exist. The proof uses polynomial invariants of SU(2)⁴ × S₄ and shows that the constraints imposed by maximal mixing on all C(4,2) = 6 pairs cannot be simultaneously satisfied. The argument is technical and offers no obvious geometric reason for the non-existence.

### Translation

By the framework's entanglement–composite dictionary, "every two-qubit reduction maximally mixed" is the requirement that every pair among the four constituents be maximally entangled. In W-class language, this is a complete-graph K₄ topology on four vertices: every pair carries concurrence 1, every two-vertex marginal saturates the entanglement bound.

### Resolution

The framework's monogamy theorem (`monogamy_hopf_theorem.md`) establishes the equivalence:

1. The normed division algebras terminate at 𝕆 (dimension 8).
2. The Hopf fibrations terminate at S⁷ → S¹⁵ → S⁸.
3. Self-consistent W-type democratic entanglement transfer is impossible for four or more qubits in a ring topology.

The K₄ AME configuration is precisely the n = 4 ring case that statement (3) forbids: the sedenion zero-divisor obstruction prevents the Hopf-bundle structure required for a closed four-cycle of W-type entanglement to be consistently defined. Equivalently, the configuration would require two non-zero W-type composition paths (A→B→C and A→D→C) whose combined effect is zero net entanglement transfer between A and C — a zero divisor in the entanglement composition algebra. Such elements exist in the sedenions but cannot support a Hopf fibration, and so cannot support a consistent quantum state.

The non-existence of AME(4,2) is therefore the same theorem as the non-existence of a fourth normed division algebra: a one-line topological obstruction.

### Verification

The translation back to the QI side is direct. The K₄ structure is exactly the constraint Higuchi and Sudbery proved unsatisfiable. Their polynomial-invariant argument is a coordinate proof of the same fact for which the framework provides a coordinate-free reason.

This worked example demonstrates (D1)–(D4) explicitly and establishes that the dual direction generates structural proofs at least as short as the corresponding QI proofs are technical.

## Resolution Criteria

The open problem is resolved by any of:

**(A) A systematic catalogue.** A collection of QI classification problems for which the dual direction supplies clean, structurally illuminating proofs — at minimum AME(4,2), with extensions to AME(n,d) for varying parameters and to the Verstraete count of 9 four-qubit families.

**(B) A boundary result.** A characterisation of which QI questions translate cleanly through the dictionary and which do not, with the boundary itself carrying structural meaning (e.g., perhaps only questions about *existence* and *count* translate, while questions about specific *amplitudes* or *moduli* do not).

**(C) A no-go result.** A demonstration that the dual direction is empty beyond AME(4,2) — that the worked example is an isolated coincidence rather than the first instance of a programme. This would itself be informative, suggesting that the dictionary is genuinely asymmetric.

Outcome (A) is the target. Outcomes (B) and (C) are intermediate but still useful: they sharpen the framework's claims about *how much* of the QI–physics correspondence is structural.

## Significance

A successful programme along these lines would have three consequences.

First, it would supply the structural "why" that the Imperial-group literature has explicitly identified as missing for nearly two decades. The black-hole/qubit correspondence would no longer be a "quirky coincidence" (Duff's phrasing) but a corollary of the division-algebra termination forced by self-reference.

Second, it would establish the QI-classification ↔ particle-physics correspondence as a working dictionary rather than a shared mathematical formalism. Problems hard in one domain become tractable when translated into the other, and the translation is constructive in both directions.

Third, it would provide independent corroboration of the framework's central architecture. The same tower of normed division algebras that explains the Standard Model gauge group, the three generations, and the absence of SU(5) unification would also explain the structure of multipartite entanglement classification — a domain entirely independent of any of the framework's particle-physics inputs. Convergence of independent mathematical fields on the same termination point at 𝕆 is the framework's signature pattern; this would be a further instance.

## Suggested Approach

The most direct route appears to be:

1. **Write up AME(4,2) in full** as a self-contained note. The argument is essentially complete in `monogamy_hopf_theorem.md`; what is needed is a presentation that makes the equivalence with Higuchi–Sudbery explicit and accessible to QI readers without prior exposure to the framework's full architecture. This document alone establishes the programme has content.

2. **Extend to AME(n,d) systematically.** Determine which existence/non-existence results follow from monogamy and which require additional structure. Compare with the existing QI catalogue (Helwig–Cui 2013 and successors).

3. **Attempt the Verstraete count.** Decompose the 9 four-qubit families as Frobenius spider trees subject to the sedenion zero-divisor obstruction, and check whether the count emerges naturally. A successful derivation would provide a non-string-theoretic alternative to Borsten et al. 2010 — and, more importantly, would explain why the count is 9 in terms of the framework's underlying topology.

4. **Approach the SLOCC invariant ring** via the Casimir-invariant correspondence. The hypothesis is that QI invariant generators are Casimirs of the gauge group acting on the composite-state representation; this can be tested at small n where both sides are known.

These steps are sequenced from least to most ambitious. The first is largely a writing exercise; the last is a substantial research project.

## Natural Audience

Three groups are uniquely well-positioned to engage with this programme.

**Anthony Sudbery (York).** Sudbery proved the AME(4,2) non-existence (with Higuchi 2000), has worked extensively on quaternionic quantum mechanics and division algebras, and is acknowledged in Duff–Ferrara (2007) for useful conversations on the black-hole/qubit correspondence. He has both halves of the dictionary in his head already.

**The Imperial College group (Borsten, Duff, Hughes, Marrani).** They have explicitly identified the gap that this programme addresses. Hughes in particular has pursued the magic-pyramid and double-copy structures that connect division algebras to gauge theory, providing further entry points.

**Péter Lévay (Budapest).** Lévay's work on Hopf fibrations, entanglement geometry, and the Fano plane structure of seven-qubit entanglement sits closest to the framework's geometric core. He is the natural partner for the Hopf-side of the dual translation.

More broadly, the quantum-information classification community (Verstraete, Dür, Cirac, Coecke, Kissinger, Heunen) and the categorical-quantum-mechanics community would have an interest in any successful demonstration that their classification problems admit clean derivations from a structurally independent source.

## References

### Black-hole/qubit programme
- Duff, M.J. "String triality, black hole entropy and Cayley's hyperdeterminant." Phys. Rev. D 76, 025017 (2007). [arXiv:hep-th/0601134]
- Duff, M.J. & Ferrara, S. "E₇ and the tripartite entanglement of seven qubits." Phys. Rev. D 76, 025018 (2007). [arXiv:quant-ph/0609227]
- Duff, M.J. & Ferrara, S. "E₆ and the bipartite entanglement of three qutrits." Phys. Rev. D 76, 124023 (2007). [arXiv:0704.0507]
- Borsten, L., Dahanayake, D., Duff, M.J., Marrani, A. & Rubens, W. "Four-qubit entanglement from string theory." Phys. Rev. Lett. 105, 100507 (2010). [arXiv:1005.4915]
- Borsten, L., Duff, M.J. & Lévay, P. "The black-hole/qubit correspondence: an up-to-date review." Class. Quant. Grav. 29, 224008 (2012). [arXiv:1206.3166]
- Lévay, P. "Stringy black holes and the geometry of entanglement." Phys. Rev. D 74, 024030 (2006). [arXiv:hep-th/0603136]

### Entanglement classification
- Higuchi, A. & Sudbery, A. "How entangled can two couples get?" Phys. Lett. A 273, 213–217 (2000). [arXiv:quant-ph/0005013]
- Verstraete, F., Dehaene, J., De Moor, B. & Verschelde, H. "Four qubits can be entangled in nine different ways." Phys. Rev. A 65, 052112 (2002). [arXiv:quant-ph/0109033]
- Dür, W., Vidal, G. & Cirac, J.I. "Three qubits can be entangled in two inequivalent ways." Phys. Rev. A 62, 062314 (2000). [arXiv:quant-ph/0005115]
- Coffman, V., Kundu, J. & Wootters, W.K. "Distributed entanglement." Phys. Rev. A 61, 052306 (2000). [arXiv:quant-ph/9907047]
- Helwig, W. & Cui, W. "Absolutely maximally entangled states: existence and applications." (2013). [arXiv:1306.2536]

### Hopf-fibration entanglement geometry
- Mosseri, R. & Dandoloff, R. "Geometry of entangled states, Bloch spheres and Hopf fibrations." J. Phys. A 34, 10243 (2001). [arXiv:quant-ph/0108137]
- Bernevig, B.A. & Chen, H.-D. "Geometry of the 3-Qubit State, Entanglement and Division Algebras." J. Phys. A 37, 3069 (2004). [arXiv:quant-ph/0302081]
- Pinilla, L. & Luthra, M. "Hopf Fibration and Quantum Entanglement in Qubit Systems." (2009). [arXiv:0904.4925]

### Categorical quantum mechanics
- Coecke, B. & Kissinger, A. "The Compositional Structure of Multipartite Quantum Entanglement." ICALP 2010, LNCS 6199. [arXiv:1002.2540]

### Division algebras and exceptional structures
- Adams, J.F. "On the non-existence of elements of Hopf invariant one." Ann. Math. 72, 20–104 (1960).
- Baez, J. "The Octonions." Bull. Amer. Math. Soc. 39, 145–205 (2002). [arXiv:math/0105155]

### Internal framework documents
- `monogamy_hopf_theorem.md` — equivalence of division-algebra termination, Hopf fibration termination, and W-type ring impossibility for n ≥ 4.
- `open_problem_hopf_frobenius.md` — companion problem on whether Adams' theorem implies Coecke–Kissinger compositional completeness as a topological corollary.
- `g2_roots_ghz_w_quark_lepton_v2_2026-04-30T0604.md` — entanglement-class ↔ Standard-Model dictionary in mature form.

---

*Document created: 2026-05-03T13:07 UTC. Status: Open problem proposed for Paper 1.*
