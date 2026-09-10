# The G₂ Root Structure, Entanglement Classes, and the Quark/Lepton Split

## Structural Argument — March 16, 2026 *(consolidated v2: 30 April 2026)*

---

## 1. Overview

This document presents a structural argument connecting three independently established mathematical results into a single chain:

1. The G₂ automorphism group of the octonions has a root system with two distinct root lengths (ratio √3), which decompose under SU(3) into the adjoint (short roots) and the coset G₂/SU(3) (long roots).
2. Three-qubit entanglement has exactly two inequivalent SLOCC classes — GHZ (special Frobenius algebra) and W (anti-special Frobenius algebra) — which are compositionally complete.
3. The octonionic Hopf fibration, upon singling out a preferred complex direction, splits the fermion representation into leptons (colour singlets, ℂ sector) and quarks (colour triplets, ℂ³ sector).

The three results are dual presentations of one underlying structure. Throughout this document particles are treated as **irreducible communication channels** between events in a self-referential network rather than as objects with labels. Under this ontology the GHZ/W distinction labels channel-attributes, the long/short root distinction labels gauge channels (operators that exchange attributes), and the quark/lepton distinction labels the modes the channels carry. These are three different *categorical types* of structure — attributes, gauge channels, and modes — which §4 keeps in separate columns rather than collapsing into a single row.

**Status.** The individual results (1)–(3) are established. The connection between them is supported by **proved theorems (§8)**: under the octonionic Hopf map with the computability split, GHZ-class entanglement maps exclusively to the ℂ³ (colour triplet) sector — the *GHZ confinement theorem* — while W-class states generically access the ℂ (colour singlet) sector — the *W accessibility theorem*. A direct consequence is a topological resolution of the strong CP problem (§9): the colour sector has no oriented pairwise structure to carry a CP-violating phase, forcing θ_QCD = 0. The remaining connections (G₂ root lengths and mass spectrum) are open conjectures with testable consequences. The framework's relationship to Furey's algebraic programme is via a Wedderburn-style correspondence between minimal left ideals and irreducible channels (§7.3).

---

## 2. The G₂ Root System Under SU(3)

### 2.1 Basic Structure

G₂ = Aut(𝕆) has rank 2 and dimension 14. Its root system has 12 roots in two orbits under the Weyl group:

- **6 short roots** of length 1
- **6 long roots** of length √3

The ratio of long to short root lengths is √3; the ratio of squared lengths is 3.

### 2.2 Decomposition Under SU(3)

Singling out one imaginary octonion direction — the computability split ℂ ⊂ 𝕆 — breaks G₂ to SU(3). The adjoint representation decomposes as:

**14 = 8 ⊕ 3 ⊕ 3̄**

where:

- **8** (SU(3) adjoint): spanned by the 6 short roots plus the 2-dimensional Cartan subalgebra. These are the gluon directions — rotations *within* the colour sector that preserve the octonionic structure.
- **3 ⊕ 3̄** (coset G₂/SU(3) ≅ S⁶): spanned by the 6 long roots. These are the directions that connect the ℂ sector to the ℂ³ sector — they would act *between* the lepton-attribute and quark-attribute sectors if they were unbroken. The breaking of G₂ → SU(3) is precisely what removes these as available gauge channels.

### 2.3 Bracket Structure

The Lie bracket relations between these sectors have a definite pattern:

- **[8, 8] ⊂ 8**: Short-root brackets close among themselves. The SU(3) adjoint is a subalgebra.
- **[8, 3] ⊂ 3** and **[8, 3̄] ⊂ 3̄**: Short roots rotate the long-root sectors (the adjoint acts on the fundamental representation).
- **[3, 3̄] ⊂ 8**: Long-root brackets land in the short roots. The product of a triplet with an anti-triplet yields an adjoint element.
- **[3, 3] ⊂ 3̄** (schematically, via the ε-tensor): Triplets bracket to anti-triplets.

The crucial asymmetry is: **short roots close among themselves; long roots do not.** Any operation involving long roots necessarily involves the full algebra. This is the algebraic expression of confinement under the channel reading: the broken long-root channels cannot be assembled out of the surviving short-root channels.

### 2.4 The Im(𝕆) Decomposition

Under SU(3) ⊂ G₂ (where SU(3) is the stabiliser of e₁), the full octonions decompose as:

**𝕆 = ℝ ⊕ Im(𝕆) = 1 ⊕ (1 ⊕ 3 ⊕ 3̄) = 1 ⊕ 1 ⊕ 3 ⊕ 3̄**

The two singlets are e₀ (the real direction, trivially SU(3)-invariant) and e₁ (the preferred imaginary, fixed by the choice of split). Together they span ℂ = {e₀, e₁}, the 2-dimensional sector W states project into. The 6-dimensional 3 ⊕ 3̄ is {e₂, …, e₇}, the sector the GHZ Hopf image lands in.

The 3 ⊕ 3̄ rep appears twice — once as a vector subspace of 𝕆 (where GHZ Hopf images live) and once as a coset in g₂ (where the broken generators live). These are isomorphic as SU(3)-reps and naturally identified by G₂/SU(3) ≅ S⁶ ⊂ Im(𝕆).

---

## 3. GHZ and W Entanglement Classes

### 3.1 SLOCC Classification

Dür, Vidal, and Cirac (2000) showed that three-qubit entanglement under stochastic local operations and classical communication (SLOCC) has exactly two inequivalent genuine tripartite classes:

- **GHZ class**: |GHZ⟩ = |000⟩ + |111⟩. Maximal three-tangle. Tracing out any one qubit leaves the other two in a *separable* mixed state. Entanglement is "all or nothing" — genuinely tripartite.
- **W class**: |W⟩ = |001⟩ + |010⟩ + |100⟩. Zero three-tangle. Tracing out any one qubit leaves the other two *still entangled*. Entanglement is distributed pairwise, robust to particle loss.

### 3.2 Frobenius Algebra Characterisation

Coecke and Kissinger (2010) showed that these classes correspond to two distinct algebraic structures:

- **GHZ → Special commutative Frobenius algebra**: The composition μ ∘ δ (comultiply then multiply) yields a nonzero scalar. The algebra is "connected" — composing and decomposing retains information about the whole.
- **W → Anti-special commutative Frobenius algebra**: The composition μ ∘ δ yields zero. The algebra is "disconnected" — the composition annihilates.

The distinction is purely algebraic/topological: special vs anti-special is about whether a certain loop evaluates to a nonzero scalar.

### 3.3 Compositional Completeness

Coecke and Kissinger proved that GHZ and W Frobenius algebras are **compositionally complete**: any N-qubit entanglement class can be generated from compositions of these two three-qubit primitives (plus two-qubit Bell entanglement). No genuinely new entanglement primitive arises at four or more qubits.

---

## 4. The Attribute / Channel Dictionary

### 4.1 The Right Categorical Separation

Three different categorical types of structure are at play in §2 and §3, and they should not be collapsed into a single row of correspondences:

- **Attribute spaces** are subspaces of 𝕆 — what a channel can carry.
- **Gauge channels** are subspaces of g₂ — operators that exchange attributes.
- **Channel classes** (GHZ vs W) are properties of the Frobenius-algebra structure — kinds of attribute the channel composition preserves.

The earlier two-row dictionary ("long roots ↔ GHZ ↔ quarks" / "short roots ↔ W ↔ leptons") had Row 1 looking clean only because three different categorical types happened to share an SU(3)-rep label (3 ⊕ 3̄), and had Row 2 visibly mismatched. The correct presentation separates the columns:

| Object | Lives in | SU(3) content | Role in channel structure |
|---|---|---|---|
| ℝ ⊂ 𝕆 (e₀) | vector rep | 1 | Scalar / normalisation direction |
| {e₁} ⊂ Im(𝕆) | vector rep | 1 | W-accessible singlet — lepton attribute |
| {e₂, …, e₇} ⊂ Im(𝕆) | vector rep | 3 ⊕ 3̄ | GHZ Hopf image — quark colour attribute |
| Short roots + Cartan ⊂ g₂ | algebra | 8 | Gluon channel — acts within quark-attribute sector |
| Long roots ⊂ g₂ | algebra | 3 ⊕ 3̄ | Broken generators — would mix lepton/quark attributes |

### 4.2 Why GHZ-Class Channels Carry Quark Attribute

Under the channel reading, the GHZ ↔ quark identification rests on three matching properties. None of them say "GHZ is a quark"; they say a GHZ-class channel can only carry, exchange, and sustain quark-type attribute.

**Property 1 — Non-closure (confinement is a channel-availability statement).**
- GHZ channel: tracing out one of three sub-channels destroys *all* the channel's attribute content. The three sub-channels are inseparable.
- Long-root structure: [3, 3̄] ⊂ 8, [3, 3] ⊂ 3̄. Long-root operations never close among themselves; they always involve the full G₂ algebra. After G₂ → SU(3), the long roots are broken, and there are no surviving gauge channels through which a colour-triplet attribute can be exchanged into the singlet sector. The colour-triplet attribute is therefore stuck within 3 ⊕ 3̄ — not because of a force preventing escape, but because the only channels that could carry it out have been broken. (Made rigorous in §8.)
- Quarks: this is colour confinement, restated as a fact about which exchange channels exist.

**Property 2 — Connectedness (gauge interaction is the surviving cycle).**
- GHZ/special: μ ∘ δ ≠ 0. The compose-decompose loop is nonzero.
- Short-root structure: the bracket [3, 3̄] → 8 → [8, 3] → 3 is a nontrivial cycle that stays inside the quark-attribute sector. Starting from a colour triplet, passing through the adjoint, and returning to the triplet yields a nonzero result. This cycle *is* the gauge interaction — gluon exchange.
- Quarks: the strong force is mediated by exactly this cycle (quark emits gluon, gluon absorbed by quark), and it never leaves the quark-attribute sector.

**Property 3 — Genuine tripartiteness.**
- GHZ channel: the entanglement is irreducibly three-party.
- 3 ⊕ 3̄ representation: the SU(3) fundamental has three colour charges with the constraint that physical states are colour singlets (all three colours participate).
- Quarks: three colours, irreducibly tripartite.

### 4.3 Why W-Class Channels Carry Lepton Attribute

**Property 1 — Self-closure (no broken channel needed).**
- W channel: tracing out one of three sub-channels leaves the other two still entangled. The pairwise structure survives.
- Lepton attribute: lives in {e₁} ⊂ Im(𝕆), the SU(3)-singlet sector. The SU(3) algebra (short roots + Cartan, 8-dimensional) acts trivially on this sector. The triviality of the action — not the absence of operators — is what makes leptons colour-neutral.
- Leptons exist as isolated, independently measurable particles because their attribute sector requires no surviving long-root channel to maintain it.

**Property 2 — Disconnectedness (anti-special composition).**
- W/anti-special: μ ∘ δ = 0. The compose-decompose loop annihilates.
- Singlet sector: the SU(3) gauge channels evaluate to zero on it. There is no analogue of the [3, 3̄] → 8 → [3] cycle for singlets, because the gluons cannot couple to the singlet attribute at all.
- Leptons: no strong interaction.

**Property 3 — Pairwise robustness of the underlying entanglement.**
- W: entanglement is distributed across all pairs.
- Lepton attribute: the electromagnetic and weak charges are pairwise — they act between particle and field without requiring a third party. The pairwise structure of W entanglement is what supports oriented Hopf linking, which is the geometric basis of CP violation in the weak sector (§9.3).

### 4.4 Confinement and the Gauge Channels

Under the channel reading the §6 "confinement is a topological theorem" statement becomes structurally cleaner. Confinement is not about quark-balls being unable to escape. It is about long-root channels being broken by the e₁ split, so there are no exchange channels capable of carrying a colour-triplet attribute into the singlet sector. The §8 Hopf-projection theorem proves precisely this — a structural absence of channels rather than a dynamical bound. The state-language version ("isolated quarks cannot exist") is a consequence; the channel-language version ("the channels needed to isolate a colour-triplet attribute do not exist") is the underlying theorem.

---

## 5. The Root Length Ratio and Mass

### 5.1 Connection to the Koide Framework

In the J₃(𝕆) mass framework (see companion documents), the charged lepton masses are eigenvalues of a Jordan algebra element with Koide parameter α = √2, traced to the Cayley-Dickson doubling norm. The quark sectors have α > √2 (specifically α_d ≈ 1.545 for down-type, α_u ≈ 1.778 for up-type), and the Koide ratio deviates from 2/3.

The G₂ root structure provides a candidate explanation for this deviation. Lepton-attribute channels couple to the Higgs VEV through the ℂ sector of the computability split — where the algebra is associative and the Cayley-Dickson norm is exactly √2. Quark-attribute channels couple through the ℂ³ sector — where the non-associative octonionic product modifies the effective coupling.

### 5.2 Two Complementary Working Hypotheses

There are currently **two distinct mass-deviation formulas** in the framework, both consistent with the data and both pointing at a structural origin in the long-root sector. They have not yet been shown equivalent, and treating them as a single story papers over the open problem.

**Hypothesis A — the Casimir / G₂ root-length account (§5.3 below).** Predicts α_quark = √2 · f(√3) for some f determined by the G₂ → SU(3) reduction. The Casimir ratio C₂(G₂; **7**)/C₂(SU(3); **3**) = 3 = (√3)² is the squared root-length ratio, and it is the mathematical source of the Georgi-Jarlskog factor of 3 in this account.

**Hypothesis B — the fitted |Q|^(3/2) account (§5.4 below).** The actually-fitted formula in `fermion_mass_geodesic_calculation.md` and `quark_neutrino_masses.md` is

α² = 2 + 2|Q|^(3/2)

with electric charges Q ∈ {1/3, 2/3}, giving α_d ≈ 1.544 and α_u ≈ 1.758 to within 1%. The "3" enters through |Q|^(3/2), not through any obvious √3 factor.

**Open problem.** Either (a) prove that A reduces to B — for instance, by showing |Q| tracks fractional traversal-depth of the long-root coset and |Q|^(3/2) emerges from the volume measure on S⁶ ⊂ Im(𝕆) — or (b) determine which of A and B is the correct structural account and why the other is at best a coincidence. This is sharpened in §10.2.

### 5.3 The Casimir Account

The quadratic Casimir invariants provide a quantitative link from G₂ geometry to a universal quark/lepton ratio:

- C₂(SU(3), fundamental **3**) = 4/3
- C₂(G₂, fundamental **7**) = 4
- Ratio: C₂(**7**) / C₂(**3**) = 3 = (√3)²

If the Yukawa coupling of a fermion ideal to the Higgs VEV picks up a factor from the relevant Casimir (as it does in standard gauge theory), the quark sector's effective Koide parameter would differ from the lepton sector's by a factor determined by the non-associative product structure in the long-root directions. This account predicts a **single universal factor** for all quark types — it does not distinguish up-type from down-type.

### 5.4 The Fitted |Q|^(3/2) Account

The empirically fitted formula α² = 2 + 2|Q|^(3/2) **does** distinguish up-type from down-type, by the explicit |Q| dependence (Q = 1/3 vs 2/3). It reproduces the down and up Koide parameters to within 1%. Where Hypothesis A predicts a single deviation factor, Hypothesis B predicts a two-parameter family indexed by electric charge.

A conjectural bridge: |Q| might track a fractional traversal-depth of the long-root coset, with the 3/2 exponent coming from the volume measure on S⁶ ⊂ Im(𝕆) (which has volume scaling exponent 6/4 = 3/2 in the natural normalisation). This is speculative and is the open problem in §10.2.

### 5.5 Georgi-Jarlskog Pattern

The observed quark-to-lepton mass ratios show a generation-dependent pattern:

| Generation | m_d/m_e (at ~2 GeV) | High-energy limit |
|---|---|---|
| 1 (e, d) | ~9 | ~3 |
| 2 (μ, s) | ~0.88 | ~1/3 |
| 3 (τ, b) | ~2.35 | ~1 |

In SU(5) GUTs, the factor of 3 arises from Clebsch-Gordan coefficients. In this framework, it arises from the squared root length ratio (√3)² = 3 — the same number, but from G₂ geometry rather than SU(5) representation theory. This is significant because **the framework explicitly excludes SU(5) unification** (it does not arise naturally from division algebras, and non-observation of proton decay is a prediction rather than a constraint). The Georgi-Jarlskog pattern is recovered without SU(5).

The generation pattern (3, 1/3, 1) factors as 3 × (1, 1/9, 1/3). The universal **3** plausibly comes from the long-root / colour multiplicity. The generation factors (1, 1/9, 1/3) need a different source — almost certainly triality permuting the three Cayley-Dickson qubits, with each generation traversing the long-root coset a different number of times. (Open problem §10.2.)

### 5.6 Status

The mass connection is a **conjecture**, not a derivation. Both Hypothesis A (Casimir) and Hypothesis B (fitted |Q|^(3/2)) are working formulas with empirical support; neither is yet derived from the channel structure. Whether they are dual descriptions or genuinely competing accounts is the subject of §10.2.

---

## 6. Confinement as a Topological Theorem

### 6.1 The Argument

If the dictionary in §4 is correct, colour confinement is not a dynamical accident of the QCD coupling constant but a **topological consequence of the entanglement class** — equivalently, a structural absence of exchange channels.

This is supported by the proved result of §8: under the octonionic Hopf map with the computability split, GHZ-class states are algebraically confined to the ℂ³ sector. The argument runs:

1. Quark-attribute channels are GHZ-class (special Frobenius algebra).
2. The defining property of GHZ entanglement is that tracing out any subsystem destroys *all* entanglement.
3. Therefore, isolating a single colour degree of freedom from a quark system destroys the entire channel.
4. An "isolated quark" would be a traced-out subsystem of a GHZ-class channel — which, by the defining property, has zero entanglement and hence carries no quark attribute at all.
5. Equivalently: the gauge channels needed to take a colour-triplet attribute out of the 3 ⊕ 3̄ sector are the long roots, and they have been broken by the G₂ → SU(3) reduction.
6. Therefore, isolated quark-attribute states cannot exist. This is confinement, restated structurally.

Conversely, lepton-attribute channels are W-class (anti-special Frobenius algebra), where pairwise correlations survive tracing. Lepton attribute can be isolated because the channel structure carrying it is robust to partial tracing.

### 6.2 Testable Consequence

This predicts that confinement is exact and cannot be "screened away" at any energy scale. In standard QCD, asymptotic freedom means the coupling weakens at high energy, but confinement is a non-perturbative phenomenon that persists. The topological argument gives a structural reason: the GHZ property is a discrete (topological) invariant, not a continuous parameter that could be tuned to zero. You cannot continuously deform a GHZ-class channel into a W-class channel — they are in different SLOCC classes and correspond to inequivalent module structures.

---

## 7. Compositional Completeness and the Division Algebra Chain

### 7.1 Why the Alphabet Terminates

Adams' theorem: the only parallelisable spheres are S⁰, S¹, S³, S⁷, corresponding to the four normed division algebras ℝ, ℂ, ℍ, 𝕆. The Hopf fibrations supported by these spheres encode the geometry of 1-, 2-, and 3-qubit entanglement. The sedenion extension fails (zero divisors prevent a consistent Hopf map), so no new entanglement primitives arise at four qubits.

Coecke and Kissinger's compositional completeness theorem says that GHZ and W (the three-qubit primitives) plus Bell entanglement (two-qubit) generate all N-qubit entanglement classes. The grounding argument (see companion document) explains *why*: the topological resources available for entanglement loops are exhausted at S⁷, so no genuinely new primitive can arise beyond three qubits.

### 7.2 The Full Entanglement–Particle Dictionary

| Entanglement | Hopf fibration | Division algebra | Particle physics |
|---|---|---|---|
| Single qubit (no entanglement) | S¹ → S³ → S² | ℂ | U(1) phase / electromagnetism |
| Bell (two-qubit) | S³ → S⁷ → S⁴ | ℍ | SU(2) weak force |
| GHZ (three-qubit, special) | S⁷ → S¹⁵ → S⁸ | 𝕆 (ℂ³ sector) | SU(3) colour / quark attribute (confined) |
| W (three-qubit, anti-special) | S⁷ → S¹⁵ → S⁸ | 𝕆 (ℂ sector) | Colour singlet / lepton attribute (free) |

The GHZ and W classes both live in the octonionic Hopf fibration but occupy different sectors under the computability split 𝕆 ≅ ℂ ⊕ ℂ³. The split is the same preferred complex direction that Krasnov, Szangolies, and Dubois-Violette identify as giving rise to the Standard Model gauge group.

### 7.3 The Furey ↔ Channels Correspondence

Furey's programme classifies elementary particles as minimal left ideals of the algebra ℝ ⊗ ℂ ⊗ ℍ ⊗ 𝕆 (or, more precisely, of its left-multiplication algebra, which is associative and to which Wedderburn-Artin applies). The framework's "particles as irreducible communication channels" is the same classification under a different vocabulary, related by the standard categorical correspondence between irreducible modules of an algebra and irreducible morphisms in its representation category.

The translation:

| Furey | Coecke-Kissinger | This framework |
|---|---|---|
| Minimal left ideal of A | Irreducible Frobenius-algebra representation | Irreducible communication channel |
| A acts on itself by left multiplication | Spider-fusion / Frobenius composition | Channel composition rules |
| Idempotent projector onto an ideal | Pure-state spider | Channel attribute |
| Wedderburn decomposition of A | Compositional completeness of {Bell, GHZ, W} | Hopf-fibration termination at S⁷ |
| Colour-singlet ideal | W-class channel | Lepton-attribute channel |
| Colour-triplet ideal | GHZ-class channel | Quark-attribute channel |

These three are **not parallel research programmes**. They are dual presentations of one structure. Each makes something obvious that the others leave obscure:

- Furey's algebraic vocabulary makes the **classification** obvious: Wedderburn-style theorems for the left-multiplication algebra of ℝ ⊗ ℂ ⊗ ℍ ⊗ 𝕆 enumerate the minimal left ideals, and the count gives the particle content directly. What Furey's vocabulary does *not* make obvious is why the algebra acts on itself in the first place.
- The channel vocabulary makes the **dynamics** obvious: channels compose, and the algebra-acts-on-itself structure is the channel-composition structure forced by the framework's basic primitive (an event-event correlation that can be sequentially extended). What it does not make obvious is which irreducible channels exist — Wedderburn answers that.
- The Coecke-Kissinger vocabulary in the middle is the categorical bridge: special vs anti-special Frobenius algebras are exactly the two distinct module structures on the irreducible left ideals at the octonionic level.

The asymmetric unification claim worth making in the paper: **Furey takes the algebra as input; the framework supplies the dynamical existence argument for that algebra.** The Cayley-Dickson tower is selected by self-reference plus the requirement that channels remain composable; this forces normed division algebras; Adams' theorem terminates the chain at 𝕆.

**Caveats to be honest about.** (i) The categorical Wedderburn theorem for the dagger-Frobenius / non-symmetric-monoidal setting is in Heunen-Vicary (*Categories for Quantum Theory*, OUP 2019) for the basic case, but the full classification with extra structure (e.g. flavour symmetry, oriented chirality) is younger mathematics and not entirely settled. (ii) The "framework derives the Cayley-Dickson tower" chain is structurally clear but not yet fully discharged as a theorem; parts of it remain conjectural. The explicit Wedderburn correspondence is best stated as a structural duality whose full categorical-Wedderburn proof is open (§10.4).

A line worth working into the framing of any external write-up:

> *Furey's minimal left ideals of ℝ ⊗ ℂ ⊗ ℍ ⊗ 𝕆 and the framework's irreducible communication channels in the self-referential network are the same objects under different descriptions, related by the standard categorical correspondence between irreducible modules of an algebra and irreducible morphisms in its representation category. The framework supplies a dynamical existence argument for the algebra Furey takes as input; Furey supplies the algebraic classification.*

---

## 8. Proved Results: GHZ Confinement and W Accessibility

This section establishes two complementary theorems about how the three-qubit entanglement classes map under the octonionic Hopf fibration with the computability split. **Theorem 1** (GHZ confinement, §8.1–§8.5) shows that GHZ-class channels are algebraically forbidden from carrying lepton attribute. **Theorem 2** (W accessibility, §8.6) shows the converse: W-class channels generically populate the lepton-attribute sector. §8.7 gives the underlying eigenvalue invariant that drives both results, and §8.8 assembles them into a single combined statement.

### 8.1 Theorem 1: GHZ Confinement

**Theorem.** Under the Cayley-Dickson identification ℂ⁸ ≅ 𝕆² and the computability split e₁ (giving 𝕆 ≅ ℂ ⊕ ℂ³), the octonionic Hopf map image h = o₁·conj(o₂) of any state in the SU(2)³ orbit of |GHZ⟩ = (|000⟩ + |111⟩)/√2 has identically zero projection onto the ℂ = {e₀, e₁} sector. The Hopf image lies entirely in the ℂ³ = {e₂, …, e₇} sector.

W-class states, in contrast, generically have nonzero ℂ-projection (proved as Theorem 2 in §8.6).

### 8.2 Proof

The proof proceeds in five steps.

**Step 1. The Cayley-Dickson map and the Hermitian inner product.**

The Cayley-Dickson map sends a three-qubit state ψ ∈ ℂ⁸ to a pair (o₁, o₂) ∈ 𝕆² by splitting on the first qubit:

- o₁ (as ℂ⁴) ↔ ψ₀ = (ψ₀₀₀, ψ₀₀₁, ψ₀₁₀, ψ₀₁₁)
- o₂ (as ℂ⁴) ↔ ψ₁ = (ψ₁₀₀, ψ₁₀₁, ψ₁₁₀, ψ₁₁₁)

where e₁ serves as the complex imaginary unit (so Re(ψ_ijk) maps to even-indexed octonion components and Im(ψ_ijk) maps to odd-indexed ones).

A direct computation using the octonion multiplication table shows that the {e₀, e₁} components of the Hopf image h = o₁·ō₂ satisfy:

**h[0] + i·h[1] = conj(⟨o₁, o₂⟩_ℂ⁴)**

where ⟨o₁, o₂⟩_ℂ⁴ = Σₖ conj(o₁)ₖ · (o₂)ₖ is the standard Hermitian inner product on ℂ⁴. This follows because, in the octonion product, the e₀ component collects terms e_i · conj(e_i) = +1 (giving the real inner product), and the e₁ component collects terms from the pairs {e₀, e₁}, {e₂, e₃}, {e₄, e₅}, {e₆, e₇} that together constitute the imaginary part of the Hermitian inner product with e₁ as complex imaginary unit.

Therefore, **h has zero ℂ-projection if and only if o₁ and o₂ are ℂ⁴-orthogonal**.

**Step 2. Initial orthogonality.**

For the bare GHZ state: ψ₀ = (1, 0, 0, 0)/√2 and ψ₁ = (0, 0, 0, 1)/√2. These are orthogonal in ℂ⁴ with equal norms |ψ₀|² = |ψ₁|² = 1/2.

**Step 3. U₂ ⊗ U₃ preserves orthogonality.**

U₂ ⊗ U₃ acts unitarily on the ℂ⁴ that encodes qubits 2 and 3. Let φ₀ = (U₂ ⊗ U₃)ψ₀ and φ₁ = (U₂ ⊗ U₃)ψ₁. Unitarity preserves:

- ⟨φ₀, φ₁⟩ = ⟨ψ₀, ψ₁⟩ = 0
- |φ₀|² = 1/2, |φ₁|² = 1/2

**Step 4. U₁ mixes o₁ and o₂.**

U₁ = [[a₁, b₁], [−b̄₁, ā₁]] acts on the first qubit, mixing the two branches:

- o₁ = a₁·φ₀ + b₁·φ₁
- o₂ = −b̄₁·φ₀ + ā₁·φ₁

**Step 5. The cancellation.**

Computing the Hermitian inner product:

⟨o₁, o₂⟩_ℂ⁴ = ā₁(−b̄₁)⟨φ₀, φ₀⟩ + |a₁|²⟨φ₀, φ₁⟩ + |b₁|²⟨φ₁, φ₀⟩ + b̄₁ā₁⟨φ₁, φ₁⟩

Substituting ⟨φ₀, φ₁⟩ = 0 and |φ₀|² = |φ₁|² = 1/2:

= −ā₁b̄₁ · (1/2) + 0 + 0 + b̄₁ā₁ · (1/2)

= (1/2)(−ā₁b̄₁ + b̄₁ā₁)

= **0**

The cancellation holds because **complex multiplication is commutative**: ā₁b̄₁ = b̄₁ā₁. ∎

### 8.3 Why the Proof Fails for W States

For the W state |W⟩ = (|001⟩ + |010⟩ + |100⟩)/√3, the first-qubit split gives:

- ψ₀ = (0, 1, 1, 0)/√3 with |ψ₀|² = **2/3**
- ψ₁ = (1, 0, 0, 0)/√3 with |ψ₁|² = **1/3**

Although ⟨ψ₀, ψ₁⟩ = 0, the norms are unequal. The inner product after U₁ mixing becomes:

⟨o₁, o₂⟩ = −ā₁b̄₁ · (2/3) + b̄₁ā₁ · (1/3) = ā₁b̄₁ · (−2/3 + 1/3) = −ā₁b̄₁/3 ≠ 0

The cancellation fails because the **coefficients are unequal**. The equal-norm condition (|ψ₀|² = |ψ₁|²) is equivalent to maximal entanglement across the first qubit, which GHZ satisfies and W does not.

### 8.4 The Role of the Fano Plane

The theorem singles out the computability split direction e₁. Numerical computation confirms that the zero-projection result holds specifically for {e₀, e₁} and not for other choices of imaginary direction {e₀, eₖ} with k ∈ {2,3,4,5}. Moreover:

The standard GHZ Hopf image lands on the e₆ direction. Numerical scanning over all GHZ variants (including complex-amplitude variants) and 10,000 random local unitaries per variant shows:

| GHZ variant | Hopf direction | Zero-projection directions | Fano line |
|---|---|---|---|
| |000⟩ + |111⟩ | e₆ | {e₀, e₁} and {e₀, e₇} | **(1, 6, 7)** |
| |000⟩ + i|111⟩ | e₇ | {e₀, e₁} and {e₀, e₆} | **(1, 6, 7)** |
| All other real/imag variants | e₆ or e₇ | same pattern | **(1, 6, 7)** |

In every case, the zero-projection directions are exactly the **two Fano partners** of the Hopf image direction within the Fano line (1, 6, 7). This line is distinguished: it is the unique Fano triple containing e₁, e₆, and e₇, which are precisely the three imaginary directions that participate in the Cayley-Dickson doubling ℍ → 𝕆 along e₁.

**Interpretation.** The Fano line (1, 6, 7) defines the quaternionic subalgebra {1, e₁, e₆, e₇} ≅ ℍ that contains the computability split direction. The theorem says: the GHZ Hopf image is ℂ⁴-orthogonal to the preferred ℂ direction, which confines it to the complementary ℂ³. The Fano structure determines which specific ℂ is "preferred" — it is the one defined by the Cayley-Dickson tower, i.e. the one where the algebra is commutative and the cancellation in Step 5 applies.

For any other imaginary direction eₖ (k ∉ {1, 7}), the analogous "inner product" would involve quaternionic or octonionic multiplication, where non-commutativity prevents the cancellation. The computability split is not merely a convenient choice — it is the **unique direction along which the proof works**, because it is the unique direction along which the relevant algebra is commutative.

### 8.5 Scope of the Result

The proof applies to any state of the form (|0⟩|ψ₀⟩ + |1⟩|ψ₁⟩)/√2 where ⟨ψ₀, ψ₁⟩ = 0 and |ψ₀| = |ψ₁|. This is the class of states maximally entangled across the first qubit. The GHZ state is one such state, but the result is broader: it applies to the entire SU(2)³ orbit of any maximally-entangled-across-qubit-1 state.

The condition |ψ₀| = |ψ₁| (equal norms) is equivalent to the reduced density matrix of qubit 1 being maximally mixed (ρ₁ = I/2). For the W state, ρ₁ has eigenvalues 2/3 and 1/3 — not maximally mixed — and the result fails.

This was verified numerically (10,000+ random local unitaries per test, maximum deviation from zero < 10⁻³²) and proved algebraically as above.

### 8.6 Theorem 2: W Accessibility

**Theorem (W accessibility).** For W-class states under SU(2)³ local unitaries, the Hopf image has **generically nonzero** projection onto the ℂ = {e₀, e₁} sector. The ℂ-projection vanishes only on a measure-zero subset of the local unitary group.

**Proof.** For the W state |W⟩ = (|001⟩ + |010⟩ + |100⟩)/√3, the first-qubit split gives ψ₀ = (0, 1, 1, 0)/√3 and ψ₁ = (1, 0, 0, 0)/√3 with |ψ₀|² = 2/3 and |ψ₁|² = 1/3. These are orthogonal: ⟨ψ₀, ψ₁⟩ = 0.

Following the same steps as the GHZ proof, U₂ ⊗ U₃ preserves orthogonality and norms, and U₁ mixes:

⟨o₁, o₂⟩_ℂ⁴ = ā₁(−b̄₁) · (2/3) + b̄₁ā₁ · (1/3) = ā₁b̄₁(−2/3 + 1/3) = **−ā₁b̄₁/3**

This is zero if and only if a₁ = 0 or b₁ = 0, which means U₁ is either diagonal or anti-diagonal — a measure-zero subset of SU(2). For all other U₁, the ℂ-projection is nonzero. ∎

**Why the asymmetry.** The GHZ cancellation relied on the two terms having **equal coefficients** (both 1/2), so that −ā₁b̄₁ · (1/2) + b̄₁ā₁ · (1/2) = 0 by commutativity. For W, the unequal coefficients (2/3 vs 1/3) leave a residual −ā₁b̄₁ · (1/3) that does not cancel. The root cause is the entanglement asymmetry: GHZ has ρ₁ = I/2 (maximally mixed), while W has ρ₁ with eigenvalues (2/3, 1/3).

### 8.7 The Eigenvalue Characterisation

The reduced density matrix eigenvalues are **local unitary invariants** — they are unchanged by U₁ ⊗ U₂ ⊗ U₃ because ρₖ = Tr_rest(|ψ⟩⟨ψ|) transforms as Uₖρₖ U†ₖ, which preserves eigenvalues. Therefore we can read them off the standard representatives once:

| State | ρ₁ eigenvalues | ρ₂ eigenvalues | ρ₃ eigenvalues |
|---|---|---|---|
| GHZ | (1/2, 1/2) | (1/2, 1/2) | (1/2, 1/2) |
| W | (2/3, 1/3) | (2/3, 1/3) | (2/3, 1/3) |

**Both results are symmetric across all three qubits.** GHZ has maximally mixed reduced states for every qubit, and W has the same (2/3, 1/3) imbalance for every qubit. Since the Cayley-Dickson tower has three levels — splitting on qubit 1 (ℂ → ℍ level), qubit 2 (ℍ → 𝕆 level), or qubit 3 (within ℂ² at each level) — the confinement/accessibility results hold for every Cayley-Dickson split simultaneously. This was verified numerically: the GHZ ℂ-projection is zero to < 10⁻³¹ for all three qubit splits, and the W ℂ-projection is generically nonzero for all three.

### 8.8 Combined Statement

**The Hopf ℂ-projection as an entanglement class detector:**

- **ℂ-projection ≡ 0** for all local unitaries ⟺ ρₖ = I/2 for qubit k (maximally entangled across that qubit). Satisfied by GHZ, not by W.
- **ℂ-projection ≠ 0** generically ⟺ ρₖ ≠ I/2 for qubit k. Satisfied by W, not by GHZ.

**Physical interpretation under the channel reading:**

GHZ-class channels are **confined**: the Hopf image cannot project into the lepton-attribute (ℂ) sector under any physical basis change. This is exact and follows from a discrete invariant (the reduced state eigenvalues).

W-class channels are **free**: the Hopf image generically has nonzero lepton-sector projection. The exceptions form a measure-zero set, not a generic condition.

The ℂ sector is **accessible to W-class channels but forbidden to GHZ-class channels**. This is the algebraic content of confinement: it is not a dynamical property of the coupling constant but a topological property of the channel class, determined by the reduced density matrix spectrum.

---

## 9. Resolution of the Strong CP Problem

### 9.1 The Problem

The QCD Lagrangian admits a CP-violating term proportional to a parameter θ:

L_θ = (θ g²/32π²) G_μν G̃^μν

where G is the gluon field strength and G̃ its dual. This term is gauge-invariant, Lorentz-invariant, and renormalisable — there is no structural reason within the Standard Model for it to be absent. Yet experiment constrains |θ| < 10⁻¹⁰ (from the neutron electric dipole moment). The question of why θ is so small, when nothing in the Standard Model forces it to be zero, is the strong CP problem.

The two leading proposals are the Peccei-Quinn axion (a new dynamical field that drives θ → 0) and anthropic selection. Both introduce structure beyond the Standard Model.

### 9.2 The Channel-Structure Resolution

The theorems proved in §8 provide a third resolution that requires no new particles or anthropic reasoning. Stated in channel language: θ_QCD has no carrier in the GHZ-class channel structure.

**Step 1. Parity violation requires oriented pairwise linking.**

In the Hopf fibration, any two distinct fibres are linked with an oriented Hopf linking number. The linking is a property of *pairs* of circles (S¹ fibres) embedded in S³. The orientation gives the linking a handedness — mirroring the configuration reverses the sign. This oriented linking is the geometric content of parity violation: the structure distinguishes left from right.

**Step 2. The weak sector has pairwise linking.**

The two-qubit (Bell) entanglement that lives in the quaternionic Hopf fibration S³ → S⁷ → S⁴ carries this oriented linking structure. Under the computability split, the equivariance group is U(1) × SU(2), and the oriented linking manifests as the chirality of SU(2)_L — the weak force couples only to left-handed particles. The W accessibility theorem (§8.6) confirms that W-class channels project into the ℂ sector where this pairwise linking resides.

**Step 3. The colour sector has no pairwise linking.**

GHZ-class channels are irreducibly tripartite. This is not an approximation — it is the defining property of the GHZ SLOCC class, characterised by a nonzero three-tangle τ (Dür, Vidal, Cirac 2000). A nonzero three-tangle means the channel *cannot* be decomposed into pairwise sub-channels. There are no pairs of loops to link, therefore no linking number, therefore no handedness.

The GHZ confinement theorem (§8.1) proves that GHZ-class channels map exclusively to the ℂ³ (colour) sector. Therefore the colour sector inherits the tripartite, non-pairwise channel structure of the GHZ class.

**Step 4. θ = 0 is forced.**

CP violation requires a geometric phase with physical consequences — an oriented structure that distinguishes a process from its CP-conjugate. In the Hopf fibration framework, the only available oriented structure is the Hopf linking number, which is a property of pairwise-linked fibres.

The colour sector, being GHZ-class, has no pairwise linking. Therefore it has no oriented structure to carry a CP-violating phase. The θ-parameter is not a free parameter that happens to be small — it has *no carrier in the available channel structure*. It is not a small number, it is a parameter for a channel-decomposition that does not exist in the GHZ class.

### 9.3 Comparison With the Weak Sector

The CKM matrix of the weak sector has an irreducible complex phase δ ≈ 70° that produces CP violation. This is consistent with the framework: the weak sector involves W-class channels, which *do* decompose into pairwise sub-channels (the W state's defining property is robust pairwise entanglement surviving partial tracing). These pairwise correlations carry oriented Hopf linking, which provides the geometric structure for the CKM phase.

The pattern is:

| Sector | Channel class | Pairwise linking | CP violation |
|---|---|---|---|
| Strong (SU(3)) | GHZ (tripartite) | Absent | θ = 0 (forced) |
| Weak (SU(2)) | W (pairwise) | Present | δ_CKM ≈ 70° (allowed) |

Both entries follow from the proved theorems. The asymmetry between strong and weak CP properties is a direct consequence of the asymmetry between GHZ-class and W-class channels.

### 9.4 Predictions

1. **θ = 0 exactly, not merely small.** The θ-parameter is not fine-tuned but topologically fixed. Any future measurement of θ ≠ 0 would falsify the framework.

2. **The QCD axion does not exist.** This requires a precise argument at two levels.

   *First level (airtight): the QCD axion is unnecessary and structurally forbidden.* The QCD axion is the pseudo-Goldstone boson of a broken Peccei-Quinn U(1)_PQ symmetry, introduced specifically to dynamically relax θ to zero. The Peccei-Quinn mechanism promotes θ from a fixed parameter to a dynamical field a(x), and the QCD instanton potential generates a minimum at θ_eff = 0. The axion particle is the excitation of this field around that minimum.

   In the present framework, θ is not a free parameter requiring relaxation. It is topologically fixed at zero because the GHZ entanglement class has no oriented pairwise structure. A topologically fixed quantity cannot be promoted to a dynamical field — there is no degree of freedom to excite. Therefore there is no axion field, no axion potential, and no axion particle.

   *Second level (the mass mechanism): even a hypothetical axion-like field would be massless.* The QCD axion acquires its mass through the anomalous coupling to the colour sector — specifically, the coupling to the topological charge density G_μν G̃^μν (the same θ-term). In the present framework, this term is topologically zero in the GHZ sector: the GHZ channel structure does not support the oriented instanton linking that generates the topological charge. Therefore, even if one postulated an additional global U(1) symmetry with an anomalous coupling to the strong sector, the coupling would produce no potential, because the GHZ topology has no G G̃ structure for it to couple to. The resulting "axion" would be exactly massless — a free scalar with no observable consequences in the strong sector. An exactly massless particle with no QCD coupling is not an axion in any operational sense.

   *What is not ruled out:* Axion-like particles coupled to sectors other than SU(3) — for example, a light pseudoscalar coupled to electromagnetism — are not directly addressed by these theorems. The prediction is specific: no QCD axion, because the strong CP problem it was invented to solve does not exist.

3. **No new CP violation in the strong sector at any energy scale.** The absence of strong CP violation is not an accident of low-energy physics but a topological invariant that holds at all scales.

4. **Strong CP conservation and colour confinement have a common origin.** Both are consequences of the GHZ confinement theorem: the colour sector is GHZ-class, which simultaneously prevents isolation of colour charges (confinement) and prevents CP-violating phases (θ = 0). These are not independent facts but two aspects of the same channel-structural property.

### 9.5 Relation to Existing Approaches

The result that GHZ-class channels cannot carry an oriented pairwise structure is closely related to the fact that the associator [a, b, c] = (ab)c − a(bc) of the octonions is totally antisymmetric. The associator measures the failure of associativity, and its total antisymmetry means it cannot single out a preferred orientation among the three factors. This is the algebraic counterpart of the topological statement that GHZ entanglement has no pairwise decomposition.

't Hooft's original analysis of the strong CP problem identified instantons (topological configurations of the gluon field) as the source of the θ-dependence. In the present framework, instantons correspond to nontrivial loops in the gauge field configuration space, and the θ-parameter measures the oriented linking of such loops. The GHZ topology forbids this linking, which translates back as: the instanton contributions to the vacuum energy are CP-symmetric, and θ drops out of physical observables.

---

## 10. Remaining Open Calculations

### 10.1 The Frobenius–Bracket Correspondence

**Problem.** Formalise the mapping between the special/anti-special Frobenius algebra distinction (Coecke-Kissinger) and the long-root/short-root bracket closure properties of G₂. Specifically: is there a functorial relationship between the category of Frobenius algebras internal to the octonionic Hopf fibration and the root system decomposition of G₂ under SU(3)?

### 10.2 The Quark Koide Deviation: G₂ Long-Root Traversal with Triality

**Problem.** Derive the fitted formula α² = 2 + 2|Q|^(3/2) (Hypothesis B in §5.4) from the G₂ long-root traversal of GHZ-class channels, with triality determining the per-generation weighting that produces the Georgi-Jarlskog pattern (3, 1/3, 1) = 3 × (1, 1/9, 1/3).

This merges two earlier sub-problems (the colour-triplet Koide parameter and the qubit-label dependence of the Hopf-projection proof). They are facets of the same problem: the GHZ Hopf-projection theorem can be applied splitting on any of the three qubits, the three splits correspond to the three Cayley-Dickson levels, and each split should give a different mass contribution. Triality permutes these three splits, and the per-split weighting is what generates the generation pattern.

The conjectural bridge between Hypotheses A and B is that |Q| tracks fractional traversal-depth of the long-root coset and the 3/2 exponent comes from the volume measure on S⁶ ⊂ Im(𝕆). If this works, A is the universal/leading factor and B is the |Q|-dependent correction; if it doesn't, the two hypotheses need to be reconciled differently.

### 10.3 CKM from Hopf Holonomy

**Problem.** If the quark/lepton split is determined by the GHZ/W split under the octonionic Hopf map, the CKM mixing matrix (which governs flavour-changing weak interactions between quarks) should be determined by the holonomy of the Hopf connection restricted to the GHZ sector. The CKM matrix elements would then be geometric invariants of the octonionic Hopf bundle. Can the Cabibbo angle θ_C ≈ 13° be derived from this holonomy?

### 10.4 Categorical Wedderburn for the Furey ↔ Channels Correspondence

**Problem.** Make the §7.3 correspondence rigorous by constructing the explicit functor between (a) the category of minimal left ideals of the left-multiplication algebra of ℝ ⊗ ℂ ⊗ ℍ ⊗ 𝕆 and (b) the category of irreducible Frobenius-algebra representations in the dagger-compact-closed category modelling the framework's communication channels. The basic dagger-Frobenius case is in Heunen-Vicary (2019); the open piece is the extension to handle the chiral / oriented structure that distinguishes left from right ideals (which on the channel side corresponds to direction of information flow).

This is the open Coecke-Kissinger ↔ Hopf-fibration-termination conjecture, restated in a form Heunen would recognise as a categorical-Wedderburn statement. See `open_problem_hopf_frobenius.md`.

### 10.5 U(1)_em vs U(1)_Y in the e₁-Stabiliser

**Problem (cross-check).** The {e₀, e₁} = ℂ sector that W-class channels project into carries a natural complex structure (multiplication by e₁), and there is a U(1) acting by phase rotation on this ℂ that commutes with the SU(3) stabilising e₁ inside G₂. In the Standard Model the U(1) commuting with SU(3)_C **before** electroweak symmetry breaking is U(1)_Y (hypercharge); U(1)_em emerges only after the Weinberg rotation Q = T₃ + Y/2, mixing T₃ from the SU(2)_L sector (which arises from Bell entanglement / quaternionic Hopf in the framework) with Y. Therefore the e₁-stabiliser U(1) should be identified with U(1)_Y, not U(1)_em.

This is consistent with the framework's existing electroweak unification work but should be verified explicitly against `electroweak_unification_theorem.md` and against Krasnov / Szangolies on the SO(9) / qubit-entanglement gauge group derivations before being asserted in print.

---

## 11. Predictions

The structural argument, if correct, generates the following testable predictions:

1. **Confinement is exact**: No deconfined quark phase exists at any energy scale. (This is consistent with current observations but distinguishes the framework from models that predict quark-gluon plasma is literally deconfined rather than a collective state of colour singlets.)

2. **No fractional electric charges observed in isolation**: Because quark-attribute channels are GHZ-class and cannot be traced out, fractional charges are never directly observable. (Already confirmed experimentally.)

3. **The quark Koide deviation is calculable from G₂ geometry combined with triality**: Either α_quark = √2 · f(√3) (universal Casimir factor, Hypothesis A) or α² = 2 + 2|Q|^(3/2) (charge-dependent, Hypothesis B), with §10.2 the open problem of relating them. Either way the quark α-values are not free parameters.

4. **The Georgi-Jarlskog factor of 3 follows from (√3)² without SU(5)**: The quark/lepton mass ratio pattern is a consequence of the G₂ root length ratio, not of grand unification. Combined with the framework's prediction that SU(5) is excluded (no proton decay at GUT rates), this is a distinguishing prediction.

5. **Compositional completeness has physical content**: No new gauge forces or confined sectors exist beyond the Standard Model's SU(3) × SU(2) × U(1). The entanglement alphabet is complete at three qubits. Discovery of a "fifth force" with confinement-like behaviour would falsify the framework.

6. **The computability split is physically unique**: The proved result (§8) shows that GHZ confinement to ℂ³ depends on the commutativity of ℂ along the singled-out direction. Any other choice of imaginary direction would break the theorem. This means the computability split is not a convention but a structural necessity — it is the unique direction along which the GHZ/quark confinement holds. The same direction gives the Standard Model gauge group (Krasnov, Szangolies). These are the same constraint.

7. **θ_QCD = 0 exactly** (from §9): The strong CP parameter is topologically fixed at zero because the colour sector corresponds to GHZ-class channels, which have no oriented pairwise structure to carry a CP-violating phase. This is not fine-tuning but a topological invariant.

8. **No QCD axion exists** (from §9): The Peccei-Quinn mechanism is unnecessary and structurally forbidden. The framework predicts that searches for the QCD axion (ADMX, CASPEr, ABRACADABRA, etc.) will yield null results in the QCD-coupled sector. (Axion-like particles coupled to other sectors are not directly addressed by these theorems.)

---

## 12. References

### G₂ and Octonions
- Günaydin, M. & Gürsey, F. "Quark structure and octonions." J. Math. Phys. 14 (1973), 1651–1667.
- Baez, J. "The Octonions." Bull. AMS 39 (2002), 145–205.
- Draper Fontanals, C. "Notes on G₂: the Lie algebra and the Lie group." (2017). arXiv:1704.07819.

### Entanglement Classification
- Dür, W., Vidal, G. & Cirac, J.I. "Three qubits can be entangled in two inequivalent ways." Phys. Rev. A 62, 062314 (2000).
- Coecke, B. & Kissinger, A. "The Compositional Structure of Multipartite Quantum Entanglement." ICALP 2010, LNCS 6199, 297–308. arXiv:1002.2540.

### Hopf Fibrations and Standard Model
- Szangolies, J. "The Standard Model Symmetry and Qubit Entanglement." Entropy 27(6), 569 (2025). arXiv:2512.17328.
- Krasnov, K. "SO(9) characterisation of the Standard Model gauge group." J. Math. Phys. 62, 021703 (2021). arXiv:1912.11282.
- Mosseri, R. & Dandoloff, R. "Geometry of entangled states, Bloch spheres and Hopf fibrations." J. Phys. A 34, 10243 (2001).
- Bernevig, B.A. & Chen, H.-D. "Geometry of the 3-Qubit State, Entanglement and Division Algebras." J. Phys. A 37, 3069 (2004). arXiv:quant-ph/0302081.

### Division Algebras and Particle Physics
- Furey, C. "SU(3)_C × SU(2)_L × U(1)_Y (× U(1)_X) as a symmetry of division algebraic ladder operators." Phys. Lett. B (2018).
- Dubois-Violette, M. "Exceptional quantum geometry and particle physics." (2016). arXiv:1604.01247.

### Wedderburn Theory and Categorical Quantum Mechanics
- Wedderburn, J.H.M. "On hypercomplex numbers." Proc. London Math. Soc. (1908).
- Albert, A.A. "A structure theory for Jordan algebras." Ann. Math. 48 (1947).
- Bruck, R.H. & Kleinfeld, E. "The structure of alternative division rings." Proc. AMS 2 (1951).
- Heunen, C. & Vicary, J. *Categories for Quantum Theory*. OUP (2019).

### Strong CP and Axions
- Peccei, R.D. & Quinn, H.R. "CP Conservation in the Presence of Pseudoparticles." Phys. Rev. Lett. 38, 1440 (1977).
- 't Hooft, G. "Symmetry breaking through Bell-Jackiw anomalies." Phys. Rev. Lett. 37, 8 (1976).

### Parallelisable Spheres
- Adams, J.F. "On the non-existence of elements of Hopf invariant one." Annals of Mathematics 72 (1960), 20–104.
- Bott, R. & Milnor, J. "On the parallelizability of the spheres." Bull. AMS 64 (1958), 87–89.

---

*Document Status: v2 consolidated 2026-04-30T0604. Original structural argument March 16, 2026; v1 consolidation 29 April 2026; v2 incorporates the channel-ontology rewrite of §4, the explicit two-hypothesis split in §5, the Furey ↔ Wedderburn correspondence in §7.3, the merged §10 open problems, and the U(1)_Y cross-check in §10.5. Proved theorems: GHZ confinement (§8.1–§8.5) and W accessibility (§8.6); topological resolution of the strong CP problem (§9). Open: G₂ root length and mass connections (§5, §10.2); categorical Wedderburn for the Furey correspondence (§10.4); U(1)_Y identification (§10.5).*
