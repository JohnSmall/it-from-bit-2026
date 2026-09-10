# Research Summary: Computability, Spacetime, and Division Algebras

## Conversation Date: March 12, 2026

## Overview

This conversation extended the negative probability / self-reference framework into spacetime structure, computational distance metrics, and the division algebra foundations of the Standard Model. The central thesis developed here is that spacetime geometry emerges from the structure of computability and non-computability, constrained by the parallelisable spheres S¹ and S³.

---

## 1. Toffoli's "What is the Lagrangian Counting?"

Toffoli (Int. J. Theor. Phys. 42, 2003) asked what the Lagrangian is counting in the least-action principle. Variational principles in physics usually have combinatorial origins (thermodynamics counts microstates, evolution counts reproductive success), but the action principle has resisted such reduction. Feynman's path integral has the right combinatorial spirit but the objects being "counted" remain elusive.

**Connection to our framework**: The path integral sums over paths weighted by complex phases e^{iS/ℏ}. In our framework, this complex weighting is necessary because a self-referential system (where the observer is part of the observed) cannot count its own paths with purely real measures. The imaginary component represents "information debt" — the Lagrangian counts computational paths, but the count is complex-valued because complete self-knowledge is impossible.

**Key related work**: A follow-up paper on the Yang-Mills Lagrangian reinterprets the action integral as a quantum "macroprogram" whose Lagrangian density is the classical limit of a quantum "microprogram." The integration superposes these elementary microprograms. Toffoli's "Action, or the Fungibility of Computation" (1998) connects action directly to "amount of computation."

**Important**: The Margolus-Levitin theorem (co-authored by Levitin and Toffoli) establishes that a quantum system of energy E needs at least time h/4E to evolve to an orthogonal state, giving ~6×10³³ operations/second/joule as the maximum computational rate of physical matter.

---

## 2. Information-Theoretic Distance to Non-Computability

Three established frameworks measure "distance" to non-computable states:

### 2a. Chaitin's Information-Theoretic Incompleteness
A formal system with n bits of axioms can determine at most n+c bits of the halting probability Ω. The "distance" to a non-computable statement is literally the information gap — the number of additional axiom-bits needed. The probability that a true sentence of length n is provable tends to zero as n → ∞.

### 2b. Proof-Theoretic Ordinals (Ordinal Analysis)
Ordinal analysis assigns ordinals to theories as a measure of strength. PA has ordinal ε₀ (Gentzen). Goodstein's theorem is unprovable in PA but provable in stronger systems (Kirby-Paris, 1982). The ordinal gap between theories measures the "distance" between what they can prove. The natural axiomatic theories are pre-well-ordered by consistency strength.

### 2c. Arithmetic Hierarchy
The Σ₁, Π₁, Σ₂, ... hierarchy with Turing jumps gives a third notion of distance — the number of oracle jumps needed.

### Novel contribution from our framework
All three existing approaches use real-valued distance. Our framework proposes complex-valued distance:
- **|ΔS_real|** = information gap (Chaitin bits / ordinal gap)  
- **|ΔS_imaginary|** = degree of self-referential entanglement preventing computation

---

## 3. The Axiom of Choice, Supertasks, and CTCs

### Key argument chain:
1. Well-ordering requires the Axiom of Choice (AC)
2. AC implicitly performs a supertask (uncountably many selections)
3. Supertasks exceed computability bounds
4. Therefore AC smuggles non-computable operations into any theory using it

This explains paradoxes like Banach-Tarski: supertasks create information from nowhere.

### Laraudogoitia's Beautiful Supertask (Mind, 1996)
Demonstrated systems where energy is not conserved, particles are created ex nihilo, and spontaneous self-excitation occurs — all from infinite particle systems with elastic collisions. Time-reversal of these systems produces creation from nothing.

### Closed Timelike Curves (CTCs)
Aaronson & Watrous showed CTCs make quantum and classical computing equivalent (both PSPACE). CTCs solve NP-complete problems without the computational work — information appears from the self-consistency requirement. Deutsch's model: Nature "finds" a fixed point, solving hard problems for free.

### Unification
Supertasks, AC, and CTCs are the same phenomenon viewed differently — mechanisms for creating or destroying information by exceeding computability bounds.

---

## 4. Fundamental Constants as Causality Protection

The four fundamental constants each block a different route to non-computability:

- **c (speed of light)** — prevents spatial closure (CTCs via superluminal travel). The spatial causality protector.
- **ℏ (Planck's constant)** — prevents temporal compression (supertasks via infinite computational speed). Via Margolus-Levitin theorem.
- **G (gravitational constant)** — prevents informational singularity (infinite density → horizon). Via Bekenstein bound.
- **k_B (Boltzmann constant)** — prevents entropic reversal (time-reversed computation). Via Landauer's principle.

Together they form a joint causality protection system. If any bound is exceeded, self-reference, supertasks, or information from nowhere become possible.

---

## 5. Jacobson's Thermodynamic Spacetime

Jacobson (Phys. Rev. Lett. 75, 1995) derived the Einstein equation from δQ = TdS applied to all local Rindler causal horizons. The Einstein equation is an equation of state, not a fundamental dynamical law. This suggests spacetime geometry is emergent from informational constraints, not fundamental. The constants c, G, ℏ, k_B describe computational boundaries that *generate* spacetime rather than describing it.

---

## 6. Parallelisable Spheres and Spatial Dimensionality

### Core argument:
- Self-referential loops require consistent information flow → parallelisability
- Adams' theorem: only S¹, S³, S⁷ are parallelisable
- S⁷ excluded because octonions are non-associative → unit octonions form a Moufang loop, not a group → cannot define consistent distance metric → information not preserved
- This leaves S¹ and S³ as the only structures for non-computable spaces

### Spacetime dimensionality:
- S¹ (ℂ): one-dimensional self-referential structure. When causality prevents closure → one temporal dimension
- S³ (ℍ): three-dimensional non-commutative self-referential structure. When causality prevents closure → three spatial dimensions
- Therefore spacetime is necessarily 3+1 dimensional

### Spatial infinity:
Non-computability is unbounded (arithmetic hierarchy extends indefinitely, proof-theoretic ordinals have no ceiling). If spatial distance corresponds to computational distance, space must be infinite.

---

## 7. Biquaternions ℂ ⊗ ℍ and the Lorentz Group

### Established mathematics:
The biquaternion algebra ℂ ⊗ ℍ (complexified quaternions) is isomorphic to M₂(ℂ) and to the even part of the spacetime algebra. The unit quasi-sphere provides a representation of the Lorentz group. Key result: Re(p̄q) = p₀q₀ - p₁q₁ - p₂q₂ - p₃q₃ gives the Lorentz metric directly.

SL(2,ℂ) — the double cover of the Lorentz group — is the group of unit-norm biquaternions. Historical development: Hamilton (1844), Silberstein (1912), Conway (1911), Lanczos (1949).

All seven Lorentz representations used in particle physics (scalars, four-vectors, Weyl spinors, Majorana spinors, Dirac spinors, electromagnetic field tensor) can be constructed as invariant subspaces within the biquaternions.

### Interpretation in our framework:
- ℍ provides the four-dimensional arena (three imaginary + one real direction)
- ℂ provides the computability split — introduces the algebraic structure distinguishing one direction (timelike/computable) from three (spacelike/non-computable)
- Without ℂ: positive-definite Euclidean metric (+,+,+,+). With ℂ: Lorentz signature (+,-,-,-)
- The signature difference reflects the algebraic difference between commutative (ℂ, S¹) and non-commutative (ℍ, S³) self-reference

---

## 8. Electroweak Chirality from Biquaternion Structure

### Key observation:
U(1) × SU(2) (electroweak gauge group) has the same algebraic structure as ℂ ⊗ ℍ (Lorentz group). The electroweak interaction is the only force that violates parity (couples only to left-handed particles).

### Proposed explanation:
If the internal symmetry group and spacetime symmetry group share the same algebra, chirality is a consequence of the embedding, not an arbitrary postulate. The ℂ factor creates an inherently chiral split (complex conjugation distinguishes z from z̄). When this acts on spinors, it distinguishes left-handed from right-handed. Since electroweak SU(2) is the same algebraic object as spatial SU(2) in the Lorentz group, it inherits chirality.

**Chirality = the spinorial manifestation of the computability/non-computability distinction.**

### Why SU(3) doesn't violate parity:
SU(3) is associated with octonionic structure, which is external to the ℂ ⊗ ℍ spacetime algebra (excluded on associativity grounds). It doesn't participate in the computability split and has no mechanism to distinguish left from right.

---

## 9. The Weinberg Angle as a Derivable Quantity

### Status:
The Weinberg angle θ_W (sin²θ_W ≈ 0.231 experimentally) parametrises the mixing of U(1)_Y and SU(2)_L. In the Standard Model it's a free parameter. The framework predicts it should be derivable from the biquaternion embedding.

### Key constraint:
SU(5) GUT is excluded because it doesn't arise naturally from division algebras. This is a prediction: no grand unification via SU(5), consistent with non-observation of proton decay. Therefore the sin²θ_W = 1/4 value from SU(5) cannot be used as a starting point.

### Approaches to derivation:
1. Geometric: the angle at which U(1)_Y embeds within ℂ ⊗ ℍ relative to SU(2)_L, fixed by compatibility with Lorentz structure
2. Information-theoretic: relative information capacity of ℂ vs ℍ phase spaces
3. Algebraic: compatibility condition requiring internal symmetry generators to commute with / transform covariantly under Lorentz generators within the same biquaternion algebra

### Note from literature:
One Cl(6)-based model predicts bare sin²θ_W = 0.25, possibly requiring RG running to match experiment. But this needs careful analysis independent of GUT assumptions.

---

## 10. Octonions and SU(3): Singling Out One Direction

### Established results:
- Günaydin & Gürsey (1973): SU(3)_c structure for quarks within octonions, obtained by fixing one imaginary octonion direction. The automorphism group G₂ breaks to SU(3).
- Furey: Complex octonions ℂ ⊗ 𝕆 generate Cl(6). Left multiplication chains of at most 6 octonions (since "seven rights make a left") give the Clifford algebra. SU(3) generators partition Cl(6) into triplets and singlets matching three generations.
- The singling out of one imaginary octonion is essential to the construction.

### Our framework's explanation:
S⁷ can't exist as a free-standing non-computable space (non-associativity). But a single self-referential loop (one unit octonion) is equivalent to S¹, which IS permitted. The singled-out octonion maps onto the ℂ computability split. The remaining 6 directions generate the associative Cl(6), producing SU(3).

This gives a *reason* for the singling out: it's the complex direction providing the computability split. There's only one such direction because there's only one S¹, one time dimension, one computability axis.

---

## 11. Exclusion of Extra Spatial Dimensions

### Hard prediction:
Three spatial dimensions is a theorem in this framework, not a contingent fact. It follows from S³ being the only higher parallelisable sphere with group structure. This directly contradicts:
- String theory (requires 10 or 11 dimensions)
- Kaluza-Klein theories (5+ dimensions)
- Large extra dimension models (ADD)

The framework says extra structure of particle physics comes from octonionic algebra projected as gauge symmetry, NOT from extra spatial dimensions.

### Additional predictions:
- No SU(5) grand unification
- No proton decay at GUT rates
- Spatially infinite universe
- Three spatial dimensions at all energy scales (no dimensional reduction at Planck scale)

---

## 12. CP Violation and Relationalism

### The objection:
CP violation in B mesons implies T violation (via CPT theorem), suggesting a preferred time direction, which would seem to require substantivalist spacetime.

### Counter-argument from our framework:
CP violation arises from the CKM matrix's irreducible complex phase δ. In our framework, this phase encodes complementarity between flavour and mass bases — it's a property of the relationship between observables, not of spacetime. The phase creates informational asymmetry (different imaginary information debt for forward vs reverse transitions), which *constitutes* the arrow of time rather than presupposing it.

Without CP violation (δ = 0): all transition amplitudes real, perfect T symmetry — not because spacetime has no preferred direction, but because no informational asymmetry exists to constitute one.

CP violation is contextual information asymmetry, supporting the relationalist view.

---

## 13. Key Open Questions for Future Research

1. **Weinberg angle derivation** from biquaternion embedding compatibility conditions
2. **Formal complex distance metric** between computable and non-computable states, using division algebra structure
3. **Mapping between proof-theoretic ordinals** and physical quantities (Margolus-Levitin / Bekenstein / Jacobson)
4. **Precise mechanism** by which octonionic non-associativity projects into SU(3) gauge symmetry via the computability split
5. **Whether chirality is fully derivable** from the ℂ ⊗ ℍ embedding
6. **Connection between Toffoli's action-computation equivalence** and the entanglement → geometry correspondence (Van Raamsdonk / ER=EPR)
7. **Three generations**: whether the octonionic → Cl(6) → three-generation structure has a computability interpretation

---

## Key References

### Computation and Action
- Toffoli, "What is the Lagrangian Counting?" Int. J. Theor. Phys. 42 (2003)
- Toffoli, "Action, or the Fungibility of Computation" in Feynman and Computation (1998)
- Margolus & Levitin, "The maximum speed of dynamical evolution" Physica D 120 (1998)

### Information-Theoretic Incompleteness
- Chaitin, "Information-Theoretic Limitations of Formal Systems" JACM (1974)
- Chaitin, "Information-Theoretic Incompleteness" World Scientific (1992)
- Kirby & Paris, "Accessible Independence Results for Peano Arithmetic" Bull. LMS 14 (1982)

### Supertasks
- Laraudogoitia, "A Beautiful Supertask" Mind 105 (1996)
- Laraudogoitia, "Infinity Machines and Creation Ex Nihilo" Synthese 115 (1998)

### CTCs and Computation
- Aaronson & Watrous, "Closed timelike curves make quantum and classical computing equivalent" Proc. Roy. Soc. A 465 (2009)
- Deutsch, "Quantum mechanics near closed timelike lines" Phys. Rev. D 44 (1991)

### Spacetime from Information
- Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State" Phys. Rev. Lett. 75 (1995)
- Van Raamsdonk, "Building up spacetime with quantum entanglement" Gen. Relativ. Gravit. 42 (2010)
- Maldacena & Susskind, "Cool horizons for entangled black holes" (2013) [ER=EPR]
- Ryu & Takayanagi, "Holographic derivation of entanglement entropy from AdS/CFT" Phys. Rev. Lett. 96 (2006)

### Division Algebras and Standard Model
- Furey, "SU(3)_C × SU(2)_L × U(1)_Y (× U(1)_X) as a symmetry of division algebraic ladder operators" Phys. Lett. B (2018)
- Furey, "Generations: three prints, in colour" JHEP 10 (2014)
- Furey & Hughes, "One generation of standard model Weyl representations as a single copy of ℝ⊗ℂ⊗ℍ⊗𝕆" Phys. Lett. B (2022)
- Günaydin & Gürsey, "Quark structure and octonions" J. Math. Phys. 14 (1973)
- Dixon, "Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics" (1994)
- Boyle & Farnsworth, "Non-Commutative Geometry, Non-Associative Geometry and the Standard Model of Particle Physics" (2014)
- Dubois-Violette & Todorov (various papers on exceptional Jordan algebra and Standard Model)

### Biquaternions and Lorentz Group
- Silberstein, "Quaternionic form of relativity" Phil. Mag. 23 (1912)
- Lanczos, "The Variational Principles of Mechanics" (1949), pp. 304-312
- Lambek, "In Praise of Quaternions" (2013)
- Sangwine, Ell & Le Bihan, "Fundamental representations and algebraic properties of biquaternions" Adv. Appl. Clifford Alg. (2010)
- Lasenby, "Some recent results for SU(3) and octonions within the geometric algebra approach" Math. Meth. Appl. Sci. (2022)

### Ordinal Analysis
- Gentzen, consistency proof of PA using ε₀-induction (1936)
- Rathjen, "Goodstein's Theorem Revisited" in Gentzen's Centenary (2015)
- Walsh, "Characterizations of ordinal analysis" (2022)

---

## Status of the Programme

**Solid structural results** (requiring formal proof):
- Parallelisability → S¹, S³ (S⁷ excluded) → 3+1 dimensions
- ℂ ⊗ ℍ → Lorentz metric and signature
- Fundamental constants as joint causality protection
- Exclusion of extra spatial dimensions
- Exclusion of SU(5) GUT

**Well-posed open questions**:
- Weinberg angle from biquaternion structure
- Chirality from embedding
- Complex distance metric formalization
- Octonionic projection mechanism for SU(3)
- Three-generation structure

**Bold predictions**:
- No extra spatial dimensions (ever)
- No SU(5) unification / no proton decay at GUT rates
- Spatially infinite universe
- CP violation is contextual, not evidence for substantivalist spacetime
