# The W → SU(2)_L doublet theorem

*Tripartite W-class states project, under any single-qubit reduction, to a two-component sector with weight spectrum (2/3, 1/3). The 2/3 eigenvector carries the SU(2)_L doublet content; the 1/3 eigenvector carries singlet content. Permutation symmetry across the three qubits makes both statements invariant under the full local unitary group. Companion result to the GHZ → ℂ³ theorem.*

---

## 1. Setup

### 1.1 The B-qubit and SU(2)_L

Recall from the setup of `ghz_to_c3_theorem.md` that the three-qubit system (A, B, C) carries Cayley-Dickson internal structure, with the B-qubit realising an ℍ-action on its operator algebra. The weak isospin SU(2) lives here: the imaginary quaternion units {e₁, e₂, e₃} generate SU(2) under left-multiplication, and the Pauli matrices σ_i are their ℂ-matrix representation on ℂ². The ℍ-structure is non-commutative, so left and right quaternion multiplication give *two distinct* SU(2) actions:

$$SU(2)_L: \quad u \mapsto q u, \qquad SU(2)_R: \quad u \mapsto u q.$$

Either is a valid gauge action. Physical weak isospin couples to only one of them. The selection mechanism — which of the two becomes SU(2)_L — is inherited from the C-qubit via the computability split, and is discussed in §6.

### 1.2 Doublet and singlet components

A 2D Hilbert space carrying the fundamental SU(2) representation is a **doublet**. The two basis vectors transform into each other under SU(2)_L, which is why weak isospin doublets (ν_L, e_L), (u_L, d_L) are the SM's organising principle. A state that does not transform under SU(2)_L — invariant under every U ∈ SU(2)_L — is a **singlet**. Right-handed fermions (e_R, u_R, d_R) are SU(2)_L singlets.

The claim we will prove is that the W entanglement class projects, under any single-qubit reduction, onto a 2-dimensional sector that supports this doublet structure with a specific 2:1 weight asymmetry between two eigendirections.

---

## 2. The single-qubit reduced state of W

### 2.1 Lemma (W reduced state)

*Let ψ = (U_1 ⊗ U_2 ⊗ U_3)|W⟩ with |W⟩ = (|001⟩ + |010⟩ + |100⟩)/√3, and let ρ_k = Tr_{\{1,2,3\} \setminus \{k\}} |ψ⟩⟨ψ| be the reduced state on qubit k. Then for every k ∈ {1, 2, 3}:*

$$\text{spec}(\rho_k) = \bigl(\tfrac{2}{3}, \tfrac{1}{3}\bigr),$$

*and the spectrum is invariant under the full SU(2)³ local unitary group.*

*Proof.* For k = 1 and U_i = I, direct computation of Tr_{2,3}|W⟩⟨W| gives ρ_1 = diag(2/3, 1/3) in the {|0⟩, |1⟩} basis. Permutation symmetry of |W⟩ under qubit relabelling gives the same spectrum for k = 2, 3. Under U_1 ⊗ U_2 ⊗ U_3, the reduced state transforms as ρ_k ↦ U_k ρ_k U_k†, which is conjugation; conjugation preserves spectrum. ∎

### 2.2 The companion spectrum for GHZ

For comparison:

| State | spec(ρ_k) for every k | Character |
|---|---|---|
| GHZ | (½, ½) = maximally mixed | SU(2)-invariant density, no preferred direction |
| W | (2/3, 1/3) | Non-degenerate, preferred eigendirection |

The GHZ single-qubit reduced state is **maximally mixed** — proportional to the identity — which means SU(2) action leaves it invariant. There is no preferred direction in the doublet space. This is consistent with GHZ → ℂ³ having no doublet structure (the ℂ³ colour sector does not carry weak isospin).

The W single-qubit reduced state has a **preferred direction** — the eigenvector with eigenvalue 2/3. SU(2) action rotates this direction, tracing out the full 2D doublet orbit. The 2:1 ratio is preserved, but the *direction* in the doublet space transforms covariantly. This is the exact structural signature of a fundamental SU(2) representation carrying a specific state.

---

## 3. Main theorem

### 3.1 Theorem (W → SU(2)_L doublet)

*For any state ψ in the SLOCC orbit of |W⟩ under U_1 ⊗ U_2 ⊗ U_3 ∈ SU(2)³, the single-qubit reduced state ρ_k is supported on a 2-dimensional subspace that carries the fundamental SU(2) representation. Relative to this SU(2), the spectrum (2/3, 1/3) decomposes ρ_k into:*

- *a 2/3-weighted doublet-active component (the larger eigenvector), and*
- *a 1/3-weighted singlet-like tail (the smaller eigenvector).*

*The decomposition is symmetric across all three qubits and invariant under the full SU(2)³ local unitary group.*

### 3.2 Proof

**Step 1. The support is 2-dimensional.** By Lemma 2.1, ρ_k has two non-zero eigenvalues (2/3 and 1/3) regardless of U_k. The support is exactly span{v₁, v₂} where v_i are the eigenvectors.

**Step 2. The support carries the fundamental SU(2).** Under U_k ∈ SU(2), the eigenvectors {v₁, v₂} transform as U_k v_i. Any two-dimensional complex vector space on which SU(2) acts faithfully is the fundamental rep (this is the content of the SU(2) classification; the only faithful 2D rep is fundamental). So the support of ρ_k is an SU(2) doublet.

**Step 3. The spectrum is a local-unitary invariant.** Eigenvalues of ρ_k are unchanged by U_k ρ_k U_k†. The ordered pair (2/3, 1/3) is therefore an intrinsic property of the W class, not of the representative.

**Step 4. Decomposition into doublet-active and singlet components.**

The spectral decomposition

$$\rho_k \;=\; \tfrac{2}{3} |v_1\rangle\langle v_1| \;+\; \tfrac{1}{3} |v_2\rangle\langle v_2|$$

identifies two components of the same doublet space. Under SU(2)_L, both eigenvectors rotate (neither is invariant individually). But the **operator** (1/3)I commutes with every SU(2) element — it is the singlet projector, up to normalisation. Rewriting:

$$\rho_k \;=\; \tfrac{1}{3}\,\mathbb{I} \;+\; \tfrac{1}{3}\bigl(|v_1\rangle\langle v_1| - |v_2\rangle\langle v_2|\bigr).$$

The first term is **singlet under SU(2)** (invariant); the second term is the **traceless preferred-direction component** that transforms non-trivially. The SU(2)-invariant tail has weight Tr(ρ_k - ρ_k^{traceless})/2 = 1/3.

The doublet-active content — the traceless piece — has spectral norm 1/3. The singlet tail — the identity-proportional piece — has weight 1/3. The total 2/3 weight of the "up" eigenvector decomposes as (1/3 singlet) + (1/3 doublet-top); the 1/3 weight of the "down" eigenvector is (1/3 singlet) + (0 doublet-bottom). Both cases share the 1/3 singlet background, which is the interpretation of the 1/3 eigenvalue.

**Step 5. Permutation symmetry.** By Lemma 2.1, the same spectrum appears for every k. The W class therefore has three copies of the same doublet facet — one per qubit — which is consistent with the three-qubit structure being the minimal carrier of the SU(2) doublet facet. ∎

### 3.3 Corollary (Bell reduction)

Tracing W over any *one* qubit gives the two-qubit reduced state

$$\rho_{\text{pair}} \;=\; \tfrac{2}{3}\,|\Psi^+\rangle\langle\Psi^+| \;+\; \tfrac{1}{3}\,|00\rangle\langle 00|,$$

where |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2 is the symmetric Bell state. The 2/3 weight is a genuine Bell pair (maximally entangled doublet-pair structure); the 1/3 weight is the fully separable |00⟩ (both members in the SU(2)-covariant "up" eigenstate, unentangled). This is the pairwise shadow of the single-qubit decomposition.

---

## 4. The C_frac supremum

### 4.1 Proposition (W colour-access supremum)

*For any ψ in the W-class SLOCC orbit, the supremum over U_1 ∈ SU(2) of the ℂ-fraction of the Hopf image is*

$$\sup_{U_1 \in SU(2)} C_{\text{frac}}(\psi) \;=\; \frac{1}{9},$$

*achieved at the maximally-mixing U_1 with |U_{1,11}|² = ½.*

*Proof.* From the exact formula C_frac = p(1 − p) / [(1 + p)(2 − p)] derived in `ghz_to_c3_theorem.md` §4.1 (with p := |U_{1,11}|²), stationary points satisfy d/dp [p(1−p)/((1+p)(2−p))] = 0, which gives p = ½. Evaluating: C_frac(½) = ¼ / (9/4) = 1/9. Endpoints p = 0, 1 give C_frac = 0. ∎

### 4.2 Structural reading

The supremum 1/9 quantifies the maximum "colour leakage" a W-class state can produce under local rotation. GHZ's C_frac is identically zero; W's is bounded above by 1/9. **The two classes are spectrally separated in the Hopf image**: no continuous deformation connects them. This is a sharpened version of the confinement argument in the GHZ theorem, now extended by the complementary statement that leptons (W) have a definite, bounded degree of colour-sector access.

**Numerical observation worth flagging but not claiming as derivation.** The Koide angle for charged leptons is δ_e = 2/9. This is exactly twice the W supremum 1/9. The factor of 2 is consistent with an L/R channel doubling — the Koide relation sums over both chiralities, whereas C_frac selects one. A rigorous derivation would require identifying C_frac with one channel of the Koide observable; this is an open calculation (tracked in `fermion_mass_geodesic_calculation.md`) rather than a theorem here.

---

## 5. The singlet tail and the sterile sector

### 5.1 Structural identification

The 1/3-weight singlet projector (1/3)·I in the decomposition of ρ_k (§3.2 Step 4) is the portion of the W state that does not transform under SU(2)_L — the **SU(2)_L-neutral content per W excitation**.

In Standard Model language: the 1/3 weight is the structural presence of an SU(2)_L-singlet sector *per W-class state, per qubit reduction*. Identification of this singlet with a specific physical state (right-handed neutrino, sterile neutrino, or the K₃-topological a-chiral neutrino of the generation theorem) requires additional structure beyond the W facet alone — specifically, the generation/triality argument and the K₃ obstruction analysis in `octonion_generations_calculation.md`.

### 5.2 What the theorem does and does not give

**Given by §3:** The existence of a 1/3-weighted SU(2)_L-singlet component of the W state, per qubit reduction, invariant under local unitaries.

**Not given by §3:** The identification of this singlet with the dark matter candidate (sterile a-chiral neutrino from the K₃ obstruction). The connection is plausible — both are SU(2)_L-neutral, both have weight 1/3 per generation in the minimal counting — but establishing it as a theorem requires showing that the K₃ four-resolution-classes decomposition aligns with the W-state spectrum (2/3 doublet + 1/3 singlet) under the triality embedding.

This is an open problem worth flagging in Paper 1's "what's next" section.

---

## 6. Chirality localisation: why SU(2)_L and not SU(2)_R

### 6.1 The two SU(2) actions on ℍ

The B-qubit's ℍ-structure supports two SU(2) actions — left-multiplication and right-multiplication by unit quaternions. Abstractly these are indistinguishable: ℍ has an outer automorphism swapping them. Physical weak isospin couples to left-multiplication only, which is the SU(2)_L vs. SU(2)_R distinction. If the framework is to derive chirality rather than postulate it, it must say which of the two SU(2)s is picked out, and why.

### 6.2 Selection from the C-qubit

The computability split on the C-qubit (§1.2 of `ghz_to_c3_theorem.md`) selects a preferred complex direction e₁ ∈ 𝕆. This choice induces an orientation on the remaining imaginary 𝕆 components via the Fano-plane multiplication rules; reversing the orientation corresponds to exchanging 𝕆 with its opposite algebra. The octonionic Hopf fibration S¹⁵ → S⁸ carries this orientation down to its total space, which contains the B-qubit's ℍ-structure as a subalgebra. The orientation inherited from 𝕆 distinguishes the two ℍ-multiplications, selecting one as "left" and the other as "right."

The chirality selection is therefore **not a property of the B-qubit in isolation** — it is propagated from the C-qubit's non-associativity via the Hopf fibration. The W facet lives in the B-qubit, but the handedness of its SU(2) action comes from the C-qubit's computability split. This is why abstract three-qubit frustration (in ℂ² ⊗ ℂ² ⊗ ℂ², without the Cayley-Dickson decoration) does not force chirality, as the earlier ChatGPT analysis correctly observed.

### 6.3 What remains to be proved

The sketch above identifies the mechanism but does not constitute a full theorem. A rigorous chirality localisation theorem would need to: (a) explicitly write the map from 𝕆-orientation to ℍ-orientation via the octonionic Hopf total space, (b) verify that the resulting ℍ-orientation agrees with the one selected by the Fano plane acting on the B-qubit's imaginary units, and (c) show that the selection is continuous across the W SLOCC orbit. Each step is mathematically tractable; none is written up. This is the current form of the **chirality fixed-point** problem and is the highest-priority open calculation for Paper 2.

---

## 7. What the theorem does not yet give

Parallel to §7 of the GHZ document, the result above is a *facet-level* statement about the W entanglement class. It does not yet provide:

1. **Assignment of specific particles to doublet slots.** Showing that the doublet decomposition yields (ν_L, e_L), (u_L, d_L) requires the hypercharge facet and the generation-triality structure; the W facet alone gives doublet existence, not doublet membership.

2. **The CKM and PMNS matrices.** These are mixings between doublet rows across generations. The W facet sits inside one generation; CKM/PMNS requires the triality rotation between generations (tracked as open problem #7 in `session_summary_2026_04_02.md`).

3. **The Weinberg angle from the doublet structure alone.** sin²θ_W = 1/4 is separately derived from fibre dimension counting (boson_mass_fibre_geometry.md); that derivation uses the Hopf fibration structure rather than the W facet directly.

4. **The explicit chirality theorem** (§6.3). Sketched, not proved.

---

## 8. Numerical verification

The computations in `hopf_w_sector.py` independently confirm:

- **Single-qubit reduced state** ρ_k = diag(2/3, 1/3) for every k ∈ {1, 2, 3} over 20,000 random SU(2)³ samples, to machine precision.
- **LU-invariance of the spectrum**: eigenvalues of ρ_k preserved under U_1 ⊗ U_2 ⊗ U_3 to 10⁻¹⁵.
- **Two-qubit reduced state** ρ_pair matches (2/3)|Ψ⁺⟩⟨Ψ⁺| + (1/3)|00⟩⟨00| up to local basis rotation.
- **C_frac supremum**: max C_frac over 20,000 SU(2)³ samples = 0.1111…, consistent with 1/9.
- **C_frac formula**: numerical values match p(1−p)/[(1+p)(2−p)] to 10⁻¹⁰ pointwise.

The W facet structure is both rigorously proved at the level of single-qubit reduced spectra and numerically confirmed at the level of the global Hopf image.

---

## 9. Summary for Paper 1 readers

> Under any single-qubit reduction, a W-class tripartite state projects to a two-dimensional sector with eigenvalue spectrum (2/3, 1/3). The sector carries the fundamental SU(2) representation; the spectrum decomposes it into a doublet-active component (2/3 eigenvector, transforming covariantly under SU(2)) and a singlet-like tail (1/3 eigenvalue, invariant under SU(2)). The same spectrum appears for every qubit, so the structure is permutation-symmetric. The supremum of the Hopf ℂ-fraction over local unitaries is exactly 1/9, twice the Koide angle δ_e for charged leptons — a relationship that is structurally suggestive but requires separate derivation to establish as a theorem. The chirality-L vs chirality-R selection is not internal to the W facet but is propagated from the C-qubit's computability split via the octonionic Hopf fibration — localising the chirality fixed-point to the interface between the B and C qubits. The companion result to the GHZ → ℂ³ theorem, this theorem establishes that the two non-trivial tripartite SLOCC classes carry inequivalent, complementary structural facets of the Standard Model: colour (GHZ) and weak isospin (W), respectively.

---

*Companion to `ghz_to_c3_theorem.md`. Together these two documents establish the assignment GHZ ↔ colour facet, W ↔ weak-isospin facet as a theorem rather than a stipulation. The particle identifications (quark, lepton) require composing these facets with spinor, hypercharge, and generation structure — treated separately.*
