# Open Problem: Compositional Completeness as a Corollary of Adams' Theorem

## Statement

**Conjecture (Hopf–Frobenius correspondence).** There exists a structure-preserving map from the chain of Hopf fibrations over parallelisable spheres to the Frobenius algebras of categorical quantum mechanics, such that Adams' theorem on the non-existence of Hopf fibrations beyond the octonionic case implies the Coecke–Kissinger compositional completeness theorem as a topological corollary.

## Background

Two independent results in quantum information theory arrive at the same conclusion by different routes.

**Result 1 (Algebraic).** Coecke and Kissinger (2010) proved that the GHZ and W entanglement classes — realised as commutative special and anti-special Frobenius algebras in the category FdHilb — are *compositionally complete*: any N-qubit entanglement class under SLOCC can be generated from compositions of these three-qubit primitives together with two-qubit entanglement and product states. The proof proceeds through the classification of Frobenius algebras and the spider theorem for connected diagrams.

**Result 2 (Topological).** The geometry of multi-qubit entanglement maps onto the Hopf fibrations associated with the normed division algebras (Mosseri & Dandoloff 2001, Bernevig & Chen 2004):

| Qubits | Division algebra | Hopf fibration | Entanglement content |
|--------|-----------------|----------------|---------------------|
| 1 | ℂ | S¹ → S³ → S² | Global phase (none) |
| 2 | ℍ | S³ → S⁷ → S⁴ | One entanglement parameter |
| 3 | 𝕆 | S⁷ → S¹⁵ → S⁸ | GHZ/W classes |

Adams (1962) proved that no Hopf fibration exists beyond the octonionic case, because the normed division algebras terminate at 𝕆 (equivalently: only S⁰, S¹, S³, S⁷ are parallelisable). This means no fundamentally new entanglement geometry appears at four or more qubits.

Neither community appears to have recognised the other's result as bearing on the same question. Coecke and Kissinger make no reference to Hopf fibrations or division algebras. The Hopf fibration literature on entanglement (Mosseri, Bernevig, Lévay, Pinilla & Luthra) does not reference compositional completeness or Frobenius algebras.

## Precise Formulation

Define the following objects:

- Let **Hopf** be the category whose objects are the three Hopf fibrations S^(2^k - 1) → S^(2^(k+1) - 1) → S^(2^k) for k = 1, 2, 3 (corresponding to ℂ, ℍ, 𝕆), with morphisms given by bundle maps respecting the fibration structure.

- Let **Frob**(FdHilb) be the category of Frobenius algebras on ℂ² in FdHilb, with the two distinguished classes: commutative special (GHZ-type, classified by orthonormal bases) and anti-special (W-type).

**Problem.** Construct a functor F: **Hopf** → **Frob**(FdHilb), or prove that no such functor exists, satisfying:

(F1) F maps the complex Hopf fibration (k = 1) to the single-qubit Frobenius algebra structure (classical basis choice = point on S²).

(F2) F maps the quaternionic Hopf fibration (k = 2) to the interaction structure of two Frobenius algebras on a two-qubit system, with the SU(2) fibre encoding the entanglement that survives the classical quotient.

(F3) F maps the octonionic Hopf fibration (k = 3) to the GHZ/W pair of Frobenius algebras on a three-qubit system, with the GHZ class corresponding to the full S⁷ fibre (non-associative, all-or-nothing) and the W class corresponding to the associative quaternionic subalgebra within 𝕆.

(F4) The composition of Frobenius algebras (the operation by which Coecke–Kissinger build N-qubit representatives) corresponds, under F, to a well-defined geometric operation on Hopf bundles or their compositions.

If F exists and satisfies (F1)–(F4), then compositional completeness follows from Adams' theorem: there is no fourth Hopf fibration to supply a fourth primitive, so GHZ and W (plus lower-order structures) must generate everything.

## Partial Evidence

**At one qubit.** The commutative special Frobenius algebras on ℂ² are classified by orthonormal bases of ℂ², i.e., by points on S² = ℂP¹. The first Hopf fibration has S² as its base space. The Hopf fibre S¹ encodes the global phase — precisely the U(1) freedom that the Frobenius algebra quotients out when it "copies" (i.e., classicalises) a basis state. The spider theorem — that connected GHZ diagrams collapse to a single spider — corresponds to the fact that the base S² is a well-defined manifold: composing projections onto a classical basis is idempotent.

**At two qubits.** The SU(2) fibre of the quaternionic Hopf fibration encodes the entanglement that cannot be removed by local operations. Lévay (2004) proved that the natural connection on this bundle is the SU(2) Yang–Mills instanton. The interaction between two Frobenius algebras in the categorical picture captures the same content: the part of the two-qubit state that is not reducible to a product of single-qubit classical structures.

**At three qubits.** The octonionic Hopf fibration's S⁷ fibre encodes the three-qubit entanglement. The GHZ/W split (Dür, Vidal & Cirac 2000) maps naturally onto the algebraic structure of the octonions: GHZ is genuinely tripartite (non-associative — requiring the full octonionic structure), while W is pairwise-robust (its entanglement can be understood within the associative quaternionic subalgebra ℍ ⊂ 𝕆). This mirrors the Frobenius algebra classification, where GHZ-type spiders are commutative special and W-type are anti-special.

**The spider theorem and sections.** A possible route to the proof: show that the spider theorem (connected GHZ diagrams collapse) is equivalent to the existence of a global section of the corresponding Hopf bundle restricted to the base. The complex Hopf bundle is non-trivial (π₁(S¹) ≠ 0), but a chosen basis defines a local section, and the Frobenius algebra precisely encodes this section structure. The spider collapse would then be the algebraic expression of "projection onto a section."

## Resolution Criteria

The problem is resolved by either:

**(A) Construction of F.** An explicit functor satisfying (F1)–(F4), from which compositional completeness follows as: "Adams' theorem ⟹ no fourth object in **Hopf** ⟹ F produces no fourth Frobenius primitive ⟹ GHZ + W + lower-order structures generate all N-qubit classes." This would replace the Coecke–Kissinger algebraic proof with a topological necessity argument.

**(B) A no-go result.** A proof that no such F can exist — that the Frobenius algebra composition and the Hopf bundle composition are fundamentally different operations that happen to agree at low qubit number. This would establish that the algebraic and geometric classifications are independent results whose agreement demands separate explanation.

**(C) A weaker correspondence.** An equivalence at the level of classification (the two frameworks identify the same entanglement classes at 1, 2, 3 qubits) without a functorial relationship on compositions. This would be intermediate: the two results illuminate each other but neither implies the other.

## Significance

If resolution (A) holds, it has three consequences:

1. **Compositional completeness is explained, not merely proved.** The Coecke–Kissinger result becomes a corollary of the division algebra structure of quantum mechanics, rather than an independent algebraic fact.

2. **Spider diagrams acquire topological semantics.** In any framework where fundamental particles arise from division algebra structure via Hopf fibrations, the GHZ/W spider diagrams used to represent those particles would be the *unique* diagrammatic language forced by the topology — not a convenient notation but the only one available.

3. **The bridge is bidirectional.** Problems stated in the categorical language (compositions of Frobenius algebras) could be translated into topological language (operations on Hopf bundles) and vice versa, potentially making hard problems in one domain tractable in the other.

If resolution (B) holds, the independence of the two results becomes a structural fact requiring its own explanation, and the question shifts to: *why do two unrelated mathematical frameworks agree on the classification of quantum entanglement?*

## Suggested Approach

The most direct route to resolution appears to be:

1. Establish (F1) explicitly by showing that the Frobenius algebra axioms on ℂ² encode precisely the section/fibre decomposition of the complex Hopf bundle. This is likely the easiest step and may already be implicit in existing work on classical structures in categorical QM.

2. Establish (F2) by connecting Lévay's instanton result to the two-Frobenius-algebra interaction laws. The SU(2) connection on S⁷ → S⁴ should correspond to the complementarity conditions between two Frobenius algebras (mutual unbias, Hopf law).

3. Attempt (F3) and (F4) together, since the three-qubit case is where non-associativity enters and where the composition question becomes non-trivial. The key test: does composing octonionic Hopf maps (in whatever sense is geometrically natural) reproduce the same N-qubit class representatives that Coecke–Kissinger construct by composing GHZ/W spiders?

## Natural Audience

This problem sits at the intersection of categorical quantum mechanics (Coecke, Kissinger, Heunen, Vicary), quantum information geometry (Mosseri, Lévay, Bernevig), and division algebra approaches to physics (Furey, Krasnov, Dubois-Violette). A resolution would connect communities that have been working in parallel on closely related structures.

## References

- Adams, J.F. "On the non-existence of elements of Hopf invariant one." Ann. Math. 72, 20–104 (1960).
- Bernevig, B.A. & Chen, H.-D. "Geometry of the 3-Qubit State, Entanglement and Division Algebras." J. Phys. A 37, 3069 (2004). [quant-ph/0302081]
- Coecke, B. & Kissinger, A. "The Compositional Structure of Multipartite Quantum Entanglement." ICALP 2010, LNCS 6199. [arXiv:1002.2540]
- Dür, W., Vidal, G. & Cirac, J.I. "Three qubits can be entangled in two inequivalent ways." Phys. Rev. A 62, 062314 (2000).
- Lévay, P. "The geometry of entanglement: metrics, connections and the geometric phase." J. Phys. A 37, 1821 (2004). [quant-ph/0306115]
- Mosseri, R. & Dandoloff, R. "Geometry of entangled states, Bloch spheres and Hopf fibrations." J. Phys. A 34, 10243 (2001). [quant-ph/0108137]
- Pinilla, L. & Luthra, M. "Hopf Fibration and Quantum Entanglement in Qubit Systems." (2009). [arXiv:0904.4925]
