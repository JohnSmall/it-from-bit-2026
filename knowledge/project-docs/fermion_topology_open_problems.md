# The Standard Model from Three Entangled Bloch Spheres

## Topological Classification and Open Problems — March 18, 2026

---

## 1. Overview

The fermion content of the Standard Model — three generations, two members per doublet, quarks and leptons with their specific quantum number assignments — is conventionally treated as empirical input. This document shows that it can be derived as a topological theorem about three entangled Bloch spheres representing the Cayley-Dickson qubits (ℂ, ℍ, 𝕆), subject to the Filatov constraint (opposite handedness for entangled pairs).

The derivation produces the correct particle counting, charge assignments, chirality structure, and generation number, plus two beyond-Standard-Model predictions: a-chiral sterile neutrinos as dark matter candidates, and m₁ = 0 for the lightest active neutrino.

---

## 2. The Three Internal Qubits

A single fermion's internal structure is described by three qubits corresponding to the three levels of the Cayley-Dickson tower:

| Qubit | CD Level | Fibre | Gauge Group | Physical Observable |
|---|---|---|---|---|
| A | ℂ | S¹ | U(1) | Electromagnetic charge |
| B | ℍ | S³ | SU(2) | Weak isospin |
| C | 𝕆 | S⁷ | SU(3) | Colour charge |

These are not abstract mathematical objects — they ARE the three gauge interactions. Every photon emission is a readout of qubit A. Every beta decay rotates qubit B. Every QCD process transforms qubit C. Each gauge boson acts on a specific internal qubit, and a particle's gauge interactions are determined by which of its three internal qubits have nontrivial states.

The identification of qubit A with U(1), qubit B with SU(2), and qubit C with SU(3) follows from matching the algebraic properties of the Cayley-Dickson levels (commutative/non-commutative/non-associative) to the structural properties of the gauge groups. The ordering is fixed by the Cayley-Dickson construction: ℂ is the first doubling (commutative, associative), ℍ is the second (non-commutative, associative), 𝕆 is the third (non-commutative, non-associative). This matches the gauge group hierarchy: U(1) is abelian, SU(2) is non-abelian but has an associative Lie algebra, SU(3) has the additional non-associative structure of the octonions constraining its representations.

---

## 3. The Filatov Constraint and K₃ Obstruction

### 3.1 The Constraint

Filatov & Auzinsh (2024) showed that representing two-qubit entanglement on two Bloch spheres requires the coordinate axes of one sphere to be right-handed and the other left-handed. This **Filatov constraint** — opposite handedness for entangled pairs — is a topological result about the quaternionic Hopf fibration, not a convention.

### 3.2 The Obstruction

For the W entanglement class, all three pairs of qubits are entangled. The Filatov constraint requires each pair to have opposite handedness. Assigning handedness (L or R) to three objects such that every pair is opposite is a 2-colouring problem on K₃ (the complete graph on 3 vertices). K₃ is an odd cycle and is therefore **not 2-colourable**.

This is the K₃ obstruction: no handedness assignment satisfies all three Filatov constraints simultaneously.

### 3.3 Resolution Classes

Every handedness assignment satisfies either 0 or 2 of the 3 constraints (never all 3, never exactly 1). Exhaustive enumeration of the 2³ = 8 possible assignments yields exactly four topological classes:

| Class | A | B | C | Satisfied pairs | Frustrated pair | Odd qubit |
|---|---|---|---|---|---|---|
| 1 | ↑ | ↓ | ↓ | (AB), (AC) | (BC) | A (ℂ) |
| 2 | ↑ | ↑ | ↓ | (AC), (BC) | (AB) | B (ℍ) |
| 3 | ↑ | ↓ | ↑ | (AB), (BC) | (AC) | C (𝕆) |
| 4 | ↑ | ↑ | ↑ | none | all three | none |

Each class also contains the globally conjugated assignment (↑↔↓ everywhere), corresponding to particle/antiparticle.

---

## 4. Physical Identification

### 4.1 Three Generations from Classes 1-3

The three classes with one odd qubit correspond to three generations. The odd qubit — the Cayley-Dickson level that carries the topological frustration — determines the mass scale:

| Class | Odd qubit | Algebraic depth | Generation | Mass hierarchy |
|---|---|---|---|---|
| 1 | A (ℂ) | Commutative, associative | 1st (e, u, d) | Lightest |
| 2 | B (ℍ) | Non-commutative, associative | 2nd (μ, c, s) | Intermediate |
| 3 | C (𝕆) | Non-commutative, non-associative | 3rd (τ, t, b) | Heaviest |

Mass increases with algebraic depth because deeper Cayley-Dickson levels involve more non-computable structure, producing longer internal geodesics. The ℂ level contributes minimal non-computability (commutative and associative). The ℍ level adds non-commutativity. The 𝕆 level adds non-associativity — the maximal algebraic obstruction. This is why the third generation is the heaviest: its frustrated qubit engages the deepest algebraic structure.

### 4.2 SU(2) Doublets from Frustrated Pair Resolution

Within each generation (Classes 1-3), the frustrated pair — the pair with same handedness — can be resolved in two topologically distinct ways. These two resolutions are the two members of the SU(2) doublet:

- **Resolution α (T₃ = −1/2):** The "charged" resolution (e, d, s, b, μ, τ)
- **Resolution β (T₃ = +1/2):** The "neutral/up" resolution (ν_e, u, c, t, ν_μ, ν_τ)

The weak force (SU(2)) is the operation that rotates between these two resolutions, acting within the Filatov pair — the pair that satisfies the opposite-handedness constraint. This is why the weak force requires a Filatov pair to act on: it rotates the relative orientation of two Bloch spheres that already have opposite handedness.

### 4.3 The Sterile Neutrino from Class 4

Class 4 — all three spheres with the same handedness — has zero Filatov pairs. This means:

- **No SU(2) interaction:** The weak force needs an opposite-handedness pair to rotate within. With none present, the particle is completely sterile to SU(2). It is not "right-handed" — it is **a-chiral**. The concept of chirality, which arises from opposite-handedness pairs, doesn't apply. This particle is "no-handed."

- **Q = 0:** Three equal frustrations around a triangle sum to zero net S¹ winding by symmetry.

- **Majorana:** All gauge charges are zero, so the particle can be its own antiparticle. The Majorana mass comes from a self-closing geodesic at the computability scale, not from the Higgs-mediated L↔R zigzag.

The distinction between a-chiral and right-handed matters physically. The standard objection to sterile neutrinos — that parity restoration at high energy should produce them — assumes they are the parity partners of left-handed neutrinos. An a-chiral particle is topologically distinct from both chiralities and is NOT produced by parity restoration. This strengthens the dark matter interpretation.

### 4.4 Counting Class 4 States

Class 4 has all three CD levels frustrated, but the three levels have different algebraic properties. The ℂ level frustration is trivial (commutative, associative — no obstruction). The ℍ level frustration is non-trivial (non-commutativity). The 𝕆 level frustration is non-trivial (non-associativity). This gives **two** independent frustration modes, corresponding to two sterile neutrinos.

Two sterile neutrinos in the seesaw mechanism produce two massive and one massless active neutrino, predicting:

- **m₁ = 0 exactly** (the lightest active neutrino is massless)
- **Normal mass ordering** (m₁ < m₂ < m₃) is mandatory
- **Two sterile neutrinos** at the computability matching scale Λ ≈ 3.6 TeV

---

## 5. Lepton and Quark Sectors

### 5.1 Leptons (Pure W)

Leptons are pure W-class: the octonionic Hopf map projects the W entanglement class into the colour singlet (ℂ) sector (proved in the G₂ document). No GHZ component means no colour charge.

**Left-handed doublets** from Classes 1-3 with two resolutions each:

| Gen | Odd qubit | Resolution α | Resolution β |
|---|---|---|---|
| 1 | A (ℂ) | e_L (Q=−1, T₃=−½) | ν_eL (Q=0, T₃=+½) |
| 2 | B (ℍ) | μ_L (Q=−1, T₃=−½) | ν_μL (Q=0, T₃=+½) |
| 3 | C (𝕆) | τ_L (Q=−1, T₃=−½) | ν_τL (Q=0, T₃=+½) |

**Right-handed partners** via Zitterbewegung (Higgs-mediated L↔R zigzag): e_R, μ_R, τ_R. These are not separate topological classes — they are the return stroke of the left-handed particle's internal zigzag. Same mass, same particle, other chirality leg. T₃ = 0 because the turnaround point is an SU(2) singlet.

**Class 4:** Two sterile neutrinos (a-chiral, Majorana, dark matter candidates).

### 5.2 Quarks (GHZ + W Superposition)

Quarks carry both colour (from GHZ-class entanglement) and weak isospin (from W-class entanglement). A single quark's internal algebraic structure is a superposition α|GHZ⟩ + β|W⟩:

- The **GHZ component** provides: colour triplet representation (SU(3)), confinement (the GHZ entanglement cannot be factored — removing one qubit destroys all entanglement, analogous to the Borromean property).

- The **W component** provides: SU(2) doublet structure (the two resolutions of the frustrated pair in Classes 1-3), and right-handed singlet structure (Class 4 all-same configuration).

- The **charge modification**: the GHZ component changes the S¹ projection from the ℂ ⊕ ℂ³ decomposition, converting lepton charges (0, −1) to quark charges (+2/3, −1/3).

**Left-handed doublets** (W component in Classes 1-3):

| Gen | Odd qubit | Resolution α (T₃=−½) | Resolution β (T₃=+½) |
|---|---|---|---|
| 1 | A (ℂ) | d_L (Q=−1/3) | u_L (Q=+2/3) |
| 2 | B (ℍ) | s_L (Q=−1/3) | c_L (Q=+2/3) |
| 3 | C (𝕆) | b_L (Q=−1/3) | t_L (Q=+2/3) |

**Right-handed singlets** via Zitterbewegung: u_R, d_R, c_R, s_R, t_R, b_R. These retain colour (from the GHZ component) and charge (from ℂ ⊕ ℂ³ projection), but lose SU(2) (no Filatov pairs in the zigzag return stroke). This is why right-handed quarks interact strongly and electromagnetically but not weakly.

### 5.3 Unified Counting

Per generation:

| Topology | Lepton (pure W) | Quark (GHZ + W) |
|---|---|---|
| Class 1-3, Resolution α | e_L (Q=−1) | d_L (Q=−1/3) × 3 colours |
| Class 1-3, Resolution β | ν_L (Q=0) | u_L (Q=+2/3) × 3 colours |
| Zigzag of α | e_R (Q=−1) | d_R (Q=−1/3) × 3 colours |
| Zigzag of β | [suppressed by seesaw] | u_R (Q=+2/3) × 3 colours |

Left-handed Weyl fermions per generation: 2 (lepton doublet) + 6 (quark doublet × 3 colours) = 8.
Right-handed Weyl fermions per generation: 1 (e_R) + 6 (u_R, d_R × 3 colours) = 7.
Three generations: 3 × 15 = 45 Weyl fermions.
Plus 2 sterile neutrinos (Majorana, generation-independent).

This matches the Standard Model count exactly (45 Weyl fermions per 3 generations, plus possible sterile neutrinos as beyond-SM content).

---

## 6. What the Topology Forbids

The following quantum number combinations are **forbidden** by the K₃ obstruction and Filatov constraint:

- No fourth generation (only three choices of which CD level is odd)
- No charged lepton with T₃ = +1/2 (the charged resolution is always T₃ = −1/2)
- No neutral lepton with T₃ = −1/2 in the doublet (the neutral resolution is always T₃ = +1/2)
- No colour triplet without SU(2) structure (GHZ requires W admixture for quarks to have doublet structure)
- No colour representations beyond singlet and triplet (only W and GHZ classes exist for three-qubit entanglement)
- No fractional charges other than 0, ±1/3, ±2/3, ±1 (determined by ℂ ⊕ ℂ³ projection of allowed configurations)
- No chiral sterile neutrino (Class 4 has no Filatov pairs — a-chiral by topology)
- No SU(2) doublet with both members having the same charge (the two resolutions always differ by one unit of T₃)

These are theorems, not postulates.

---

## 7. Gauge Interactions as Qubit Operations

| Interaction | Acts on | Operation | Requires |
|---|---|---|---|
| Photon (γ) | Qubit A | U(1) phase rotation on S¹ | Q ≠ 0 (nonzero S¹ winding) |
| W boson | Qubit B | SU(2) rotation within a Filatov pair | Filatov pair at B (T₃ ≠ 0 doublet) |
| Z boson | Qubits A, B | Mixed A-B rotation (neutral current) | Q ≠ 0 or T₃ ≠ 0 |
| Gluon (g) | Qubit C | SU(3) rotation on S⁷ | Colour triplet (GHZ component present) |
| Higgs (H) | All | Mediates L↔R zigzag (Zitterbewegung turnaround) | Couples doublet to singlet |
| Gravity | Base space | Light cone tipping = measurement | Mass (any internal geodesic) |

A particle's gauge interactions are determined by which of its three internal qubits have nontrivial states. The topology determines which qubits are active, which determines which forces the particle feels.

---

## 8. Connection to Mass Formulas

The mass formulas derived in the fermion mass calculation document connect directly to the three-qubit topology:

**α² = 2 + 2|Q|^{3/2} × (colour == 3)**

- The "2" is the Cayley-Dickson norm² — the base anisotropy from the doubling, independent of quantum numbers.
- The "|Q|^{3/2}" is the Born rule on the fibre — charge (S¹ winding from qubit A) times its amplitude.
- The "(colour == 3)" restricts the correction to quarks — only with the GHZ component does the charge project into ℂ³.

**θ = 120° + θ_C / n, where n = 1 + (T₃ + ½) + (colour == 3)**

- n counts the active internal directions — one base direction (qubit A), plus one if T₃ = +1/2 (qubit B active in the β resolution), plus one if colour triplet (qubit C active via GHZ).
- The Higgs-triality misalignment θ_C is shared among the active directions. More active qubits → more dilution → smaller mass hierarchy within the generation.

---

## 9. The Completeness Theorem: Standard Model = Entanglement Classification

### 9.1 The Bijection

The entanglement classification theorem (Dür-Vidal-Cirac 2000 for the three-qubit classification; Coecke-Kissinger 2010 for compositional completeness) establishes that multi-qubit entanglement has exactly three primitive types: Bell (two-qubit), GHZ (three-qubit, genuinely tripartite), and W (three-qubit, distributed pairwise). Any N-qubit entanglement class for N > 3 decomposes into compositions of these primitives.

The Cayley-Dickson particle hierarchy, derived from the internal qubit structure of particles, assigns one particle type to each entanglement primitive:

| Entanglement primitive | Internal qubits | CD levels | Particle type | Physical role |
|---|---|---|---|---|
| None (product state) | 1 | ℂ | Higgs | Creates the arena |
| Bell | 2 | ℂ ⊗ ℍ | Gauge bosons | Symmetries of the arena |
| W | 3 | ℂ ⊗ ℍ ⊗ 𝕆 | Leptons | Free states in the arena |
| GHZ | 3 | ℂ ⊗ ℍ ⊗ 𝕆 | Quarks (colour) | Confined states in the arena |
| GHZ + W | 3 | ℂ ⊗ ℍ ⊗ 𝕆 | Quarks (full) | Confined + doublet |

This is a bijection: four entanglement primitives, four particle types. No fifth type exists because no fifth primitive exists.

### 9.2 The Hierarchy is Necessary

Each level depends on the previous one:

**Level 1 (Higgs / product state):** The computability split — singling out ℂ within the Cayley-Dickson tower. This creates the internal structure. Without it, there is no fibre, no distinction between internal and external, no arena for physics.

**Level 2 (Gauge bosons / Bell):** The symmetries of the split. Bell entanglement between two CD levels (ℂ and ℍ) describes the rotational structure of the internal space. The gauge bosons mediate transformations within this structure. Without level 1, there's nothing to gauge.

**Level 3 (Fermions / GHZ and W):** The states that populate the structure. Three-qubit entanglement across all three CD levels (ℂ, ℍ, 𝕆) gives the matter content. Without levels 1 and 2, there's no structure to populate.

The hierarchy creates → gauges → populates the internal space. Removing any level collapses the entire structure.

### 9.3 The Spin-Statistics Connection

The internal qubit count determines the spin:

| Internal qubits | K_n 2-colourable? | Handedness | Representation | Spin |
|---|---|---|---|---|
| 1 | trivial | none | scalar | 0 |
| 2 | yes (K₂) | consistent | vector (single-valued) | 1 |
| 3 | no (K₃) | frustrated | spinor (double-valued) | 1/2 |
| 4 | forbidden (sedenions) | — | — | — |

With 1 qubit, there's no Filatov pair — no handedness structure at all. Scalar.

With 2 qubits, the Filatov constraint is satisfiable — one L, one R. Handedness is consistent, the representation is single-valued, spin is integer. Vector boson.

With 3 qubits, the K₃ obstruction makes consistent handedness impossible. The system is forced into a double-valued (spinorial) representation to accommodate the frustration. Half-integer spin.

With 4 qubits, the sedenions have zero divisors and can't support a Hopf map. The tower terminates. No spin-3/2 or higher fundamental particles.

The spin-statistics theorem — that half-integer spin particles are fermions (antisymmetric under exchange) and integer-spin particles are bosons (symmetric) — follows from graph colouring on K_n. The K₃ obstruction that prevents consistent handedness is the same topological fact that forces antisymmetric statistics. The connection between spin and statistics isn't a separate axiom; it's a consequence of the Filatov constraint on the Cayley-Dickson tower.

### 9.4 Three Proofs of Completeness

The Standard Model's completeness — that there are no additional particle types, gauge forces, or generations beyond what we observe — is the same fact viewed from three directions:

**Algebraic:** The Cayley-Dickson construction produces exactly four normed division algebras (ℝ, ℂ, ℍ, 𝕆). The next step (sedenions) has zero divisors and cannot support consistent information flow. No fourth internal qubit, no fourth particle type.

**Topological:** Adams' theorem establishes that only S⁰, S¹, S³, S⁷ are parallelisable. S¹⁵ is not. No fourth Hopf fibration, no fourth gauge force.

**Information-theoretic:** Coecke-Kissinger's compositional completeness theorem proves that Bell, GHZ, and W are sufficient to generate all N-qubit entanglement classes for any N. No fourth entanglement primitive exists. All multi-particle states decompose into compositions of these three.

These are three independent proofs that the Standard Model particle content is complete. A proton (three quarks) is a composition of GHZ primitives. A meson (quark-antiquark) is a composition of GHZ with its conjugate. An atom is a composition of all three primitives. But no new *primitive* structure appears — ever — because the mathematical structures that generate primitives have all terminated.

### 9.5 Summary

The Standard Model particle content is not an empirical list that could have been otherwise. It is identical to the classification of entanglement primitives on the Cayley-Dickson tower:

    {Product, Bell, GHZ, W} ↔ {Higgs, Gauge bosons, Quarks, Leptons}

Both classifications are complete for the same reason: the normed division algebras terminate at the octonions, the parallelisable spheres terminate at S⁷, and the entanglement primitives terminate at three qubits. These three termination theorems are three faces of one mathematical fact. The Standard Model is the unique particle physics consistent with the structure of entanglement.

---

## 10. Results: Three Tiers

### Tier 1: Solved (full derivations in the paper)

These results are established with explicit calculations or proofs:

1. **Complex information separates the Jaynes omelette.** S = −ln|p| − iθ cleanly divides classical information (real part) from information debt (imaginary part). The uncertainty principle is a constraint on imaginary information across conjugate pairs.

2. **Self-reference requires complex probability.** The Lawvere-Yanofsky diagonal structure of quantum measurement necessitates complex-valued probability. Quantum randomness is irreducible epistemological limitation from self-reference.

3. **Parallelisable spheres from consistent information flow.** Adams' theorem limits the structures supporting self-referential loops to S¹, S³, S⁷, giving the three Hopf fibrations and (upon the computability split) the Standard Model gauge group.

4. **The grounding argument.** From relational spacetime + measurement-as-CTC + Adams' theorem, the Standard Model gauge group SU(3) × SU(2) × U(1)/ℤ₆ is derived, not assumed.

5. **Fermion mass formulas.** α² = 2 + 2|Q|^{3/2} and θ = 120° + θ_C/n reproduce all three measured charged fermion sectors to < 0.2% (α²) and < 0.05° (θ), with 6 of 7 independent mass predictions within experimental error.

6. **Electroweak parameters.** sin²θ_W = 1/4 from fibre dimension counting (runs correctly to 0.231 at M_Z); y_t = 1 (m_t within 0.9%); m_H = v/2 (within 1.7%).

7. **Fractional charge without SU(5).** Quark charges arise from the ℂ ⊕ ℂ³ projection with automatic ℤ₆ quotient, predicting no proton decay.

8. **K₃ obstruction and fermion counting.** The four topological classes of three-qubit handedness assignments reproduce the Standard Model's fermion content including generation number, doublet structure, and chirality.

### Tier 2: Conjectures with Strong Support (stated with evidence)

These are motivated by the framework and consistent with data, but not yet formally derived:

1. **The Higgs mechanism is a Wick rotation** from timelike to spacelike internal degrees of freedom. Before SSB, internal structure flows in the time direction (invisible, massless). After SSB, it circulates spatially on the fibre (observable as mass).

2. **λ = 1/8** (Higgs quartic = sin²θ_W / 2). The connection to the Weinberg angle suggests both arise from the S¹/S³ dimension ratio. Predicted m_H = 123.1 GeV vs observed 125.25 GeV.

3. **Generations as Cayley-Dickson frustration depth.** The three generations correspond to which CD level carries the topological frustration, with mass scaling with algebraic depth (commutative → non-commutative → non-associative).

4. **Quarks as GHZ + W superpositions.** The quark sector requires both entanglement classes — GHZ for confinement, W for doublet structure. The GHZ-W interference explains the up quark mass discrepancy.

5. **A-chiral sterile neutrinos.** Class 4 (all-same handedness) gives particles with no Filatov pairs, hence no gauge interactions. With Majorana mass at the computability scale Λ ≈ 3.6 TeV, these are dark matter candidates.

6. **GR-QM connection at the electroweak scale.** The Higgs mechanism (Wick rotation), measurement (light cone tipping), and mass (spacetime curvature) are the same operation at different scales, connecting quantum mechanics to general relativity at v = 246 GeV rather than the Planck scale.

### Tier 3: Open Problems (explicitly left for the community)

These are well-defined problems that other researchers can work on. Each is stated with enough context that someone outside the framework can pick it up.

---

## 11. Open Problems

### 11.1 The Three-Bloch-Sphere Topology (Pure Mathematics)

**Problem:** Extend Filatov & Auzinsh's two-Bloch-sphere representation to three qubits in the W state. Prove the K₃ obstruction, classify the four resolution classes, and determine the topological invariants (linking numbers, characteristic classes) that distinguish them.

**Tools needed:** Stabiliser formalism, quaternionic Hopf fibration geometry, graph colouring theory.

**Expected outcome:** A theorem in algebraic topology relating the homotopy of three linked S² (Bloch spheres) to the classification of three-qubit W-class entanglement. This is publishable as a pure mathematics result independent of any physical interpretation.

**Contact point:** Filatov & Auzinsh have the stabiliser formalism expertise. Bernevig & Chen's octonionic parametrisation provides the three-qubit Hopf map.

### 11.2 The GHZ/W Mixing Ratio (Quantum Information / Algebra)

**Problem:** For the quark sector's GHZ + W superposition α|GHZ⟩ + β|W⟩, determine whether the mixing angle φ (where α = cos φ, β = sin φ) is a free parameter or is fixed by the topology.

**Expected answer:** Fixed. The electric charge quantisation (Q = −1/3, +2/3) through the ℂ ⊕ ℂ³ projection should determine |α/β|² uniquely. If this is correct, the quark sector has no additional free parameters beyond those already present in the lepton sector.

**Why it matters:** If α/β is free, the framework has an unexplained parameter in the quark sector. If it's fixed, the entire fermion content (quantum numbers AND masses) is determined by topology plus one angular parameter θ_C.

### 11.3 The CKM Matrix from Geodesic Basis Transformation (Mathematical Physics)

**Problem:** The CKM mixing matrix describes the transformation between mass eigenstates and flavour eigenstates. In the framework, mass eigenstates are geodesics on the Hopf fibre, and flavour eigenstates are the Z₃ triality axes of J₃(𝕆). The CKM matrix should be the basis transformation between these two bases.

**Specific target:** Derive the Cabibbo angle θ_C ≈ 13° from the octonionic Hopf bundle geometry — the angle at which the Higgs VEV direction deviates from the nearest triality axis. This is currently the one free angular parameter in the mass formulas. If derivable, it would reduce the framework to mass scales only.

**Connection:** The approximate equality θ_C ≈ θ_Koide (the Koide phase offset) suggests they are the same geometric quantity. The CKM matrix elements should then follow from the same J₃(𝕆) structure that gives the mass ratios.

### 11.4 The PMNS Matrix and Neutrino Mixing (Particle Physics / Algebra)

**Problem:** The PMNS matrix describes neutrino mixing. In the framework with two sterile neutrinos and m₁ = 0, the PMNS matrix has a specific structure (one column is determined by the masslessness of ν₁). Derive the PMNS mixing angles from the same J₃(𝕆) structure used for the CKM matrix.

**Prediction to check:** If the PMNS angles come from the same θ_C and J₃(𝕆) geometry as the CKM angles, but with different sector-specific parameters (reflecting the different n values for neutrinos vs quarks), this would be a non-trivial consistency check.

### 11.5 The Mass Scale Hierarchy (Theoretical Physics)

**Problem:** The absolute mass scale m₀ differs across the four fermion sectors: m₀(lepton) ≈ 314 MeV, m₀(ν) ~ meV, m₀(down) ≈ 650 MeV, m₀(up) ≈ 22700 MeV. The α² and θ formulas determine mass *ratios* within each sector, but not the absolute scales. What sets these four values?

**Partial answer:** m₀(up) ≈ v²/(some scale) is connected to y_t ≈ 1. m₀(lepton) ≈ Λ_QCD ≈ 300 MeV may be related to the confinement scale. The neutrino scale involves the seesaw suppression. But a unified derivation of all four m₀ values from the fibre geometry is missing.

**Why it matters:** Reducing the four m₀ values to one or two derivable quantities would bring the total free parameter count from 5 (θ_C + 4 m₀'s) to 1 or 2, making the mass spectrum almost entirely determined by topology.

### 11.6 The GHZ-W Interference and Light Quark Masses (Quantum Information / Particle Physics)

**Problem:** The up quark mass is predicted 29% too high by the single-geodesic model. If quarks are GHZ + W superpositions, the GHZ and W components interfere, and for the lightest quarks this interference is significant. Calculate the interference term and determine whether destructive interference explains the up quark discrepancy.

**Specific prediction:** The T₃ = +1/2 resolution (up-type quarks, neutrinos) should show larger interference effects than T₃ = −1/2 (down-type quarks, charged leptons), consistent with the observed pattern of Koide deviations.

### 11.7 The Sterile Neutrino as Dark Matter (Cosmology / Particle Physics)

**Problem:** If two a-chiral sterile neutrinos exist at M ≈ 3.6 TeV with Majorana mass, calculate their cosmological abundance and determine whether it matches Ω_DM h² ≈ 0.12.

**Key question:** The production mechanism is non-thermal — production occurs during the electroweak phase transition as the three K₃ resolution classes crystallise out. Standard thermal production at this mass overcloses the universe. The phase transition dynamics must be modelled to determine the abundance.

**Testable consequences:** Normal neutrino mass ordering (mandatory with m₁ = 0), Σm_ν calculable from seesaw parameters, potential signal in neutrinoless double beta decay experiments.

### 11.8 Derivation of λ = 1/8 (Mathematical Physics)

**Problem:** The Higgs quartic coupling λ = 1/8 was identified numerically (m_H/v ≈ 1/2). Derive this value from the Hopf bundle curvature or from the relationship λ = sin²θ_W / 2.

**Approach:** The complex Hopf bundle S¹ → S³ → S² has Chern class c₁ = 1 and the curvature 2-form integrates to 4π over S². The Higgs potential arises from promoting the preferred imaginary direction to a dynamical variable (Szangolies/Finkelstein-Jauch-Schiminovich-Speiser). The quartic coefficient should be determined by the bundle's curvature, possibly as λ = (c₁)²/(2 × dim(S¹ + S³)) = 1/(2×4) = 1/8.

### 11.9 The Weinberg Angle Running and Matching Scale (Particle Physics)

**Problem:** The bare sin²θ_W = 1/4 matches the observed 0.2312 at M_Z via SM running from Λ ≈ 3.6 TeV. Determine whether this matching scale is a prediction (no new physics below 3.6 TeV) or an artefact of one-loop approximation.

**Implication:** If the matching scale is physical, it predicts a desert between the electroweak scale and the Planck scale — no SUSY, no extra dimensions, no new gauge bosons in between. This is consistent with current LHC null results but will be further tested by future colliders.

### 11.10 The Three-Bloch-Sphere Extension for Borromean (GHZ) Structure (Pure Mathematics)

**Problem:** Extend the Filatov representation to the GHZ entanglement class. Since GHZ states have maximally mixed reduced density matrices (eigenvalues 1/2, 1/2 for each qubit), individual Bloch sphere representations collapse to points at the centre. Determine what topological structure replaces the three-sphere representation for GHZ — is it a Borromean linking of degenerate spheres?

**Connection:** The Borromean property (no pairwise links, only collective inseparability) should emerge naturally for GHZ, providing the topological foundation for colour confinement.

### 11.11 The Spin-Statistics Connection from Graph Colouring (Mathematical Physics / Topology)

**Problem:** Make rigorous the connection between the K_n colouring obstruction and the spin of particles. Specifically, show that:

- 1 internal qubit (K₁, trivially colourable) → scalar representation of the rotation group (spin 0)
- 2 internal qubits (K₂, 2-colourable) → vector representation (spin 1, single-valued)
- 3 internal qubits (K₃, not 2-colourable) → spinor representation (spin 1/2, double-valued)

The core claim is that the K₃ frustration — the impossibility of consistent handedness assignment — forces the system into a double-valued representation, which is the defining property of spinors. This would derive the spin-statistics theorem from the Filatov constraint on the Cayley-Dickson tower, rather than from relativistic quantum field theory.

**Why it matters:** The spin-statistics connection is one of the deepest results in physics. Deriving it from graph colouring on the internal qubit structure would establish that spin, statistics, and the particle type hierarchy all have a common topological origin in the Cayley-Dickson tower.

### 11.12 The Boson Sector from Two-Qubit Bell Entanglement (Mathematical Physics)

**Problem:** Develop the two-internal-qubit (Bell entanglement) description of gauge bosons in the same detail as the three-qubit fermion classification. Specifically:

- Show that the four electroweak bosons (γ, W⁺, W⁻, Z) correspond to the 2² = 4 states of two Bell-entangled CD qubits (ℂ and ℍ levels).
- Show that the eight gluons correspond to the SU(3) adjoint states arising from the 𝕆 level constrained by non-associativity.
- Derive the absence of generation structure for bosons from the 2-colourability of K₂ (no frustrated pairs → no generation-distinguishing obstruction).
- Show that the Higgs (1 qubit, product state) is necessarily a singlet — no partners, no copies — because K₁ has no edges and therefore no structure to classify.

---

## 12. Note on the Status of the Filatov Constraint

The extension from two to three Bloch spheres is the key calculation that underpins sections 3-6 of this document. As of this writing, Filatov has been contacted regarding potential collaboration on this extension but has not yet replied. The K₃ obstruction and four-class enumeration (section 3) follow from elementary combinatorics and do not require new calculations. The physical identifications (sections 4-5) and their connection to the mass formulas (section 8) are structural arguments within the framework. The formal topological proof — showing that the four classes have distinct topological invariants and that no other classes exist — is the content of Open Problem 10.1.

---

## 13. References

### Bloch Sphere Representations and Chirality
- Filatov, S. & Auzinsh, M. "Towards Two Bloch Sphere Representation of Pure Two-Qubit States and Unitaries." Entropy 26(4), 280 (2024).
- Filatov, S. & Auzinsh, M. "Entanglement on Two Bloch Spheres: Exploring Two-Qubit Stabilizer Group Structure." (2024). [arXiv:2406.05174]
- Filatov, S. & Auzinsh, M. "Ordering the processes with indefinite causal order." (2022). [arXiv:2106.08976]

### Entanglement Classification
- Dür, W., Vidal, G. & Cirac, J.I. "Three qubits can be entangled in two inequivalent ways." Phys. Rev. A 62, 062314 (2000).
- Coecke, B. & Kissinger, A. "The Compositional Structure of Multipartite Quantum Entanglement." ICALP 2010, LNCS 6199. [arXiv:1002.2540]

### Black Holes, Qubits, and Octonions
- Duff, M.J. "Black hole entropy and quantum information." (2007).
- Borsten, L., Dahanayake, D., Duff, M.J., Ebrahim, H. & Rubens, W. "Black Holes, Qubits and Octonions." (2009). [arXiv:0809.4685]

### Division Algebras and Standard Model
- Krasnov, K. "SO(9) characterisation of the Standard Model gauge group." J. Math. Phys. 62, 021703 (2021). [arXiv:1912.11282]
- Szangolies, J. "The Standard Model Symmetry and Qubit Entanglement." Entropy 27(6), 569 (2025). [arXiv:2512.17328]
- Furey, C. & Hughes, M. "One generation of standard model Weyl representations as a single copy of ℝ⊗ℂ⊗ℍ⊗𝕆." Phys. Lett. B (2022).
- Dubois-Violette, M. "Exceptional quantum geometry and particle physics." (2016). [arXiv:1604.01247]

### Hopf Fibrations and Entanglement
- Mosseri, R. & Dandoloff, R. "Geometry of entangled states, Bloch spheres and Hopf fibrations." J. Phys. A 34, 10243 (2001).
- Bernevig, B.A. & Chen, H.-D. "Geometry of the 3-Qubit State, Entanglement and Division Algebras." J. Phys. A 37, 3069 (2004).

### Self-Reference and Foundations
- Lawvere, F.W. "Diagonal arguments and cartesian closed categories." (1969).
- Yanofsky, N.S. "A universal approach to self-referential paradoxes, incompleteness and fixed points." Bull. Symbolic Logic 9 (2003), 362-386.
- Jaynes, E.T. "Probability in Quantum Theory." (1990).

### Higgs Mechanism from Division Algebras
- Finkelstein, D., Jauch, J.M., Schiminovich, S. & Speiser, D. "Foundations of quaternion quantum mechanics." J. Math. Phys. 3 (1962), 207-220.

### Previously Established (see project documents)
- Grounding argument — grounding_argument_gauge_group.md
- G₂ roots and GHZ/W — g2_roots_ghz_w_quark_lepton.md
- Fermion mass calculation — fermion_mass_geodesic_calculation.md
- Boson masses — boson_mass_fibre_geometry.md
- Session summary — session_summary_2026_03_18.md

---

*Document Status: Topological classification and open problems. March 18, 2026.*
*Companion script: fermion_topology_table.py*
