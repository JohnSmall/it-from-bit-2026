# The hypercharge theorem

*The Standard Model hypercharge assignments Y ∈ {−1, +1/3, −2, +4/3, −2/3, 0} for left- and right-handed fermions follow from three structural inputs: (1) the K₃ resolution determines T₃, (2) the U(1)_Y generator is traceless over 𝕆 = ℂ ⊕ ℂ³, giving Y_ℂ = −1 and Y_ℂ³ = +1/3, and (3) the Zitterbewegung zigzag preserves Q while sending T₃ → 0. The familiar "factor of 1/3" between quark and lepton hypercharges is the trace condition; the familiar sign flip is the opposite-sign of the trace contribution from ℂ versus ℂ³. Abelian anomaly cancellation falls out as the same tracelessness condition.*

---

## 1. Setup

### 1.1 What we are trying to derive

The Standard Model left-handed fermions in one generation carry the following hypercharges (Y = 2(Q − T₃) convention):

| Particle | Q | T₃ | Y |
|---|---|---|---|
| ν_L | 0 | +1/2 | −1 |
| e_L | −1 | −1/2 | −1 |
| u_L | +2/3 | +1/2 | +1/3 |
| d_L | −1/3 | −1/2 | +1/3 |

Right-handed singlets:

| Particle | Q | T₃ | Y |
|---|---|---|---|
| e_R | −1 | 0 | −2 |
| u_R | +2/3 | 0 | +4/3 |
| d_R | −1/3 | 0 | −2/3 |
| ν_R (sterile) | 0 | 0 | 0 |

These values are traditionally treated as empirical inputs. The framework derives all of them from the K₃ obstruction plus the structure of U(1)_Y on the Cayley-Dickson tower.

### 1.2 Inputs from previous theorems

From `ghz_to_c3_theorem.md`, `w_to_su2l_doublet_theorem.md`, and `k3_obstruction_chirality_sterile.md`, the following are established:

- The A-qubit (ℂ level) carries U(1)_Y.
- The B-qubit (ℍ level) carries SU(2)_L. Membership in the SU(2)_L doublet ↔ K₃ Resolution α (T₃ = −1/2) or β (T₃ = +1/2).
- The C-qubit (𝕆 level) carries SU(3)_C. GHZ-class states project into the ℂ³ colour sector; W-class states project into the ℂ singlet sector under the computability split 𝕆 = ℂ ⊕ ℂ³.
- Leptons are pure W (no GHZ) — they live in ℂ.
- Quarks are GHZ + W — they live in ℂ³, in SU(3) triplets.
- Right-handed singlets arise from the Zitterbewegung L↔R zigzag, with T₃ = 0 because they are the turnaround point outside the K₃ resolution structure.

The new content of this document is the determination of Y values and their connection to Q via the Gell-Mann-Nishijima relation.

---

## 2. U(1)_Y as a traceless operator on 𝕆

### 2.1 The centraliser condition

U(1)_Y must commute with SU(3)_C. In the G₂ stabiliser picture (`ghz_to_c3_theorem.md` §1.2), SU(3) is the subgroup of G₂ = Aut(𝕆) that fixes a preferred complex direction e₁ ∈ 𝕆, and acts as the fundamental representation on the remaining ℂ³ = span{e₂, e₃, e₄, e₅, e₆, e₇}.

A U(1) acting on 𝕆 commutes with SU(3) iff it is diagonal in the ℂ ⊕ ℂ³ decomposition — that is, it acts with a single scalar on each of the two summands:

$$Y = \begin{pmatrix} y_\mathbb{C} \, \mathbb{I}_{\mathbb{C}} & 0 \\ 0 & y_{\mathbb{C}^3} \, \mathbb{I}_{\mathbb{C}^3} \end{pmatrix}$$

where 𝕀_ℂ is the identity on the 1-complex-dimensional ℂ summand and 𝕀_ℂ³ is the identity on the 3-complex-dimensional ℂ³ summand. The two eigenvalues y_ℂ and y_ℂ³ are so far undetermined.

### 2.2 The tracelessness condition

The U(1)_Y generator must be **traceless** over 𝕆 in order to be a genuine SU(3)-commuting U(1) inside a larger structure, rather than a multiple of the identity (which would be a trivial phase and not a physical gauge symmetry).

In concrete terms: if Y had nonzero trace, then the U(1)_Y rotation of 𝕆 would include an overall phase rotation of the full state. This overall phase is the A-qubit's U(1) phase, which in the framework is the private self-referential phase (not a gauge observable, by the Born-rule argument). The gauge-observable U(1)_Y must therefore be the traceless part.

Counting real dimensions: dim_ℝ(ℂ) = 2, dim_ℝ(ℂ³) = 6. Tracelessness requires:

$$2 \, y_\mathbb{C} + 6 \, y_{\mathbb{C}^3} = 0 \qquad \Longleftrightarrow \qquad y_\mathbb{C} = -3 \, y_{\mathbb{C}^3}.$$

This is the structural origin of the "factor of 3" between quark and lepton hypercharges. Nothing else.

### 2.3 Fixing the normalisation

The overall scale of Y is a convention — it depends on how we normalise U(1)_Y relative to SU(2)_L. The standard choice sets:

$$y_\mathbb{C} = -1, \qquad y_{\mathbb{C}^3} = +\tfrac{1}{3}.$$

Any other choice rescales all Y values uniformly. The convention Y = 2(Q − T₃) with Q having the conventional {−1, 0, +2/3, −1/3} values pins down this particular normalisation.

The sign — that y_ℂ is negative and y_ℂ³ is positive — is fixed by requiring the electron to have Q = −1 rather than Q = +1. This is a single sign convention, not a framework input. Once chosen, all other signs follow.

**Claim.** The two eigenvalues (y_ℂ, y_ℂ³) = (−1, +1/3) are the *unique* eigenvalues of a SU(3)-commuting traceless U(1) on 𝕆 with the electron sign convention. They are not free parameters; they are forced by the ℂ ⊕ ℂ³ decomposition plus tracelessness.

---

## 3. Left-handed hypercharges

### 3.1 Leptons

Leptons are pure W-class: the state lives in the ℂ sector of 𝕆 (proved in `w_to_su2l_doublet_theorem.md` via the Hopf-image ℂ-projection). The U(1)_Y eigenvalue on ℂ is y_ℂ = −1.

For all left-handed leptons in any generation:

$$Y(\ell_L) \;=\; y_\mathbb{C} \;=\; -1.$$

Combined with T₃ values from the K₃ resolution:

- **Resolution β (T₃ = +1/2):** Q = T₃ + Y/2 = 1/2 + (−1/2) = 0. **Neutrino.**
- **Resolution α (T₃ = −1/2):** Q = T₃ + Y/2 = −1/2 + (−1/2) = −1. **Charged lepton.**

This gives the two members of each left-handed lepton doublet, with the correct electric charges.

### 3.2 Quarks

Quarks are GHZ + W: the GHZ facet places the state in the ℂ³ colour sector. The U(1)_Y eigenvalue on ℂ³ is y_ℂ³ = +1/3.

For all left-handed quarks in any generation:

$$Y(q_L) \;=\; y_{\mathbb{C}^3} \;=\; +\tfrac{1}{3}.$$

Combined with T₃ from the same K₃ resolution structure:

- **Resolution β (T₃ = +1/2):** Q = 1/2 + 1/6 = 2/3. **Up-type quark.**
- **Resolution α (T₃ = −1/2):** Q = −1/2 + 1/6 = −1/3. **Down-type quark.**

The charges +2/3 and −1/3 are not put in by hand. They follow from the same K₃ resolution structure that gives lepton charges 0 and −1, with the hypercharge contribution shifted from −1 to +1/3 by the sole fact that the state lives in ℂ³ rather than ℂ.

### 3.3 The lepton-quark shift

The celebrated +2/3 shift between corresponding lepton and quark charges (ν has Q = 0, u has Q = 2/3; e has Q = −1, d has Q = −1/3) is the difference (y_ℂ³ − y_ℂ)/2 = (1/3 − (−1))/2 = 2/3.

This is a single structural quantity — the gap between the U(1)_Y eigenvalues on the two summands of 𝕆 — that manifests as the universal charge shift between lepton and quark members of corresponding weak doublets. No extra input required.

---

## 4. Right-handed hypercharges via Zitterbewegung

### 4.1 The zigzag preserves Q

Right-handed singlet fermions arise from the Zitterbewegung process: a left-handed fermion emits a Higgs and becomes right-handed, emits another Higgs and becomes left-handed again, etc. This oscillation *is* the fermion mass (see `qubits_circuits_nucleon_physics.md` and the discussion in §2.7 there).

The Higgs is electrically neutral (Q_Higgs = 0). Emitting a neutral particle cannot change the electric charge of the emitter. Therefore:

$$Q(f_R) \;=\; Q(f_L).$$

### 4.2 The zigzag sets T₃ = 0

Right-handed fermions are SU(2)_L singlets — they are not in any K₃ resolution, so they have no T₃ assignment from the K₃ structure. T₃ = 0 by convention for singlets.

Structurally: the zigzag's right-handed leg is the turnaround point between two left-handed states. At the turnaround, the K₃ resolution is momentarily undefined — the state is transitioning between one resolution and (potentially) another. The SU(2)_L rotation during this transition is the Higgs VEV direction, which is SU(2)_L-breaking; the right-handed singlet carries no residual SU(2)_L structure.

### 4.3 Computing Y_R

From Y = 2(Q − T₃) with T₃ = 0:

$$Y(f_R) \;=\; 2 \, Q(f_L).$$

This gives:

| Particle | Q_L | Y_R = 2Q_L |
|---|---|---|
| e_R | −1 | **−2** |
| u_R | +2/3 | **+4/3** |
| d_R | −1/3 | **−2/3** |

All three values agree with Standard Model assignments.

### 4.4 ν_R (sterile neutrino)

The Class 4 a-chiral state (framework's identification of the "right-handed neutrino") is topologically distinct from the Zitterbewegung right-handed singlets. It does not arise from a left-handed state's zigzag — it is an independent K₃ class with no SU(2)_L Filatov pairs anywhere.

For Class 4:
- Q = 0 (no S¹ winding, as shown in `k3_obstruction_chirality_sterile.md` §8.2)
- T₃ = 0 (no frustrated-pair resolution to rotate within)
- Y = 2(Q − T₃) = 0

This gives the Standard Model's Y(ν_R) = 0, but with a topological origin that distinguishes the state from a ordinary right-handed partner of ν_L. The sterile status — no coupling to any gauge interaction — follows from Y = Q = T₃ = 0 simultaneously.

---

## 5. The complete hypercharge table

Putting the three sectors together:

### 5.1 Left-handed doublets (from K₃ Classes 1-3)

| Gen | Odd qubit | Resolution β (T₃ = +½) | Resolution α (T₃ = −½) | Y |
|---|---|---|---|---|
| 1 | A (ℂ) | ν_eL (Q = 0) | e_L (Q = −1) | −1 |
| 1 | A (ℂ) | u_L (Q = +2/3) | d_L (Q = −1/3) | +1/3 |
| 2 | B (ℍ) | ν_μL (Q = 0) | μ_L (Q = −1) | −1 |
| 2 | B (ℍ) | c_L (Q = +2/3) | s_L (Q = −1/3) | +1/3 |
| 3 | C (𝕆) | ν_τL (Q = 0) | τ_L (Q = −1) | −1 |
| 3 | C (𝕆) | t_L (Q = +2/3) | b_L (Q = −1/3) | +1/3 |

### 5.2 Right-handed singlets (from Zitterbewegung)

| Gen | Particle | Q | T₃ | Y |
|---|---|---|---|---|
| 1 | e_R | −1 | 0 | −2 |
| 1 | u_R | +2/3 | 0 | +4/3 |
| 1 | d_R | −1/3 | 0 | −2/3 |
| 2 | μ_R | −1 | 0 | −2 |
| 2 | c_R | +2/3 | 0 | +4/3 |
| 2 | s_R | −1/3 | 0 | −2/3 |
| 3 | τ_R | −1 | 0 | −2 |
| 3 | t_R | +2/3 | 0 | +4/3 |
| 3 | b_R | −1/3 | 0 | −2/3 |

### 5.3 Sterile sector (from K₃ Class 4)

| Particle | Q | T₃ | Y |
|---|---|---|---|
| ν_s (×2 modes per generation) | 0 | 0 | 0 |

All 45 Weyl fermions and 2 sterile modes per generation have hypercharges derived from four structural inputs: U(1)_Y tracelessness over 𝕆, K₃ resolution structure for T₃, Gell-Mann-Nishijima Q = T₃ + Y/2, and Zitterbewegung for right-handed singlets. Zero free parameters.

---

## 6. Anomaly cancellation

### 6.1 Why U(1)_Y tracelessness matters

The Standard Model requires gauge anomaly cancellation: Σ_L Y = 0 over all left-handed fermions in each generation, and various higher-order conditions (Σ Y³ = 0, etc.).

In the framework, the simplest of these — the abelian anomaly Σ Y = 0 — is a direct consequence of U(1)_Y tracelessness over 𝕆.

**Computation.** Per generation, the left-handed Weyl fermions are:
- 2 leptons (ν_L, e_L) at Y = −1 each.
- 2 × 3 = 6 quarks (u_L, d_L in three colours) at Y = +1/3 each.

Total:

$$\sum_L Y \;=\; 2 \times (-1) \;+\; 6 \times \tfrac{1}{3} \;=\; -2 + 2 \;=\; 0.$$

The cancellation is precisely 2 × y_ℂ + 6 × y_ℂ³ = 0, which is the tracelessness condition of §2.2 with the weights (dim_ℝ ℂ, dim_ℝ ℂ³) = (2, 6).

### 6.2 Structural reading

In the Standard Model, anomaly cancellation is a consistency condition that the particle content happens to satisfy. In the framework, it is *automatic*: the fermion content is determined by the K₃ resolution classes + Cayley-Dickson structure, and the hypercharges are determined by tracelessness over 𝕆. The same algebraic condition (tracelessness) both determines Y and forces the cancellation.

**This is the structural content of anomaly freedom.** The Standard Model looks suspicious because it happens to cancel anomalies for no obvious reason. The framework says: it cancels because the hypercharge itself is defined by the condition that makes it cancel. There is no separate freedom to get this wrong.

### 6.3 Higher anomalies

The mixed anomalies SU(2)²U(1) and SU(3)²U(1) and the gravitational anomaly require their own cancellation conditions:

- SU(2)²U(1): Σ_L,doublets Y = 0
- SU(3)²U(1): Σ_L,triplets Y = 0
- U(1)³: Σ Y³ − Σ_R Y³ = 0 (with appropriate signs)
- Gravitational: Σ_L Y − Σ_R Y = 0

Each of these should follow from a suitable tracelessness condition on Y over the relevant representation of 𝕆, ℂ³, or ℂ. Explicit verification requires writing out the full multi-generational cancellation with the right-handed contributions included.

**Status flag.** The abelian case (§6.1) is rigorous. The higher cases follow structurally from "same tracelessness, different subspaces" but I have not verified them all in detail. This is a natural completion exercise — most of an afternoon's work — but it is not written up.

---

## 7. What the derivation does and does not accomplish

### 7.1 What's genuinely derived

- The **magnitude ratio** Y_quark / Y_lepton = −1/3 is forced by the real-dimension ratio dim_ℝ(ℂ) / dim_ℝ(ℂ³) = 2/6 = 1/3 and the sign by the trace constraint.
- The **sign** of Y_lepton versus Y_quark is the same sign convention that makes the electron have Q = −1.
- The **specific values** (−1 for leptons, +1/3 for quark L-doublets, ±2/3 for R-singlets, −2 for charged lepton R-singlets) are determined by (y_ℂ, y_ℂ³) + K₃ resolution + Zitterbewegung + Gell-Mann-Nishijima.
- **Abelian anomaly cancellation** is automatic from tracelessness.
- The **sterile neutrino's Y = 0** follows from the topology of Class 4 in K₃, not from a separate assignment.

### 7.2 What's assumed rather than derived

- **U(1)_Y tracelessness over 𝕆** is the load-bearing assumption. It is motivated as "U(1)_Y must be the gauge-observable part of the phase rotation, not a global phase, and global phase is the private self-referential phase that Born-rule arguments say is unobservable." This is a plausible structural argument but not a theorem.
- The **Zitterbewegung zigzag mechanism** for right-handed singlets is adopted from the Hestenes tradition (circuit interpretation) and the framework's own fermion-mass geodesic picture. It is not re-derived here; it is used.
- **Gell-Mann-Nishijima Q = T₃ + Y/2** is a Standard Model convention. The factor of 1/2 and the specific combination are matters of how one chooses to split electroweak into SU(2) × U(1). The framework does not re-derive this choice, though the "K₃-blind direction = photon" argument of the EW-unification conversation makes it natural.

### 7.3 What's open

- **Higher-order anomaly cancellations** (§6.3) are structurally plausible but not written up.
- **The specific phase of U(1)_Y relative to SU(3) generators** — i.e., the sign of y_ℂ = −1 versus y_ℂ = +1 — is fixed by a physical convention (electron has Q = −1) rather than by the framework. One could argue it should come from the computability split's natural orientation, but this is not proved.
- **Why U(1)_Y is traceless and not identity-proportional** is the deepest assumption. The framework's motivation (global phase is observer-private, therefore gauge-observable U(1) must be traceless) is persuasive but not yet a theorem. A rigorous version would show that the gauge-boson kinetic term in the framework's derivation of gauge theory (via the Yang-Mills action from Hopf holonomy) forces the trace-free choice.

---

## 8. Comparison with the SU(5) GUT derivation

It is worth explicitly contrasting the framework's hypercharge derivation with the SU(5) derivation, since they land on the same answer from very different routes.

**SU(5).** Quarks and leptons embed in a common 5̄ + 10 representation. The U(1)_Y generator is the diagonal SU(5) generator that is traceless over 5̄ + 10 and commutes with SU(3) × SU(2). Tracelessness plus embedding gives the specific eigenvalues (−1/3 on d^c, +2/3 on u, −1/2 on lepton doublet, etc., after appropriate normalisation). The 1/3 factor comes from 5̄ having three "colour" components and two "lepton" components.

**Framework.** No SU(5) unification. The 𝕆 = ℂ ⊕ ℂ³ decomposition provides the analogous splitting into "one singlet component" and "three colour components." U(1)_Y is the SU(3)_C-commuting traceless U(1) on 𝕆. Tracelessness plus the dim_ℝ ratio 2:6 gives the 1/3 factor.

The same algebraic fact — tracelessness of the centraliser U(1) over a 1:3 complex decomposition — operates in both. The difference is the underlying structure: SU(5) is a unified gauge group with proton decay; the framework is an octonionic structure where ℂ and ℂ³ are *algebraically distinct* summands, so there are no gauge transitions between them, hence no proton decay.

**This is the framework's strongest structural selling point for hypercharge.** The 1/3 factor and the anomaly cancellation look identical to SU(5) — but without the SU(5) prediction (proton decay) that has been falsified by 10⁴⁰ years of non-observation. Krasnov's SO(9) characterisation of the Standard Model gauge group makes the same point independently: the octonionic structure reproduces the hypercharge assignments that SU(5) predicts, but with the ℤ₆ quotient and the absence of quark-lepton unifying transitions falling out automatically rather than being imposed.

---

## 9. Summary

> Hypercharge assignments for all Standard Model fermions follow from three structural conditions. First, the U(1)_Y generator must be traceless over the octonion algebra 𝕆 = ℂ ⊕ ℂ³, which forces its eigenvalues to have the form (−1, +1/3) up to an overall scale fixed by the electron's Q = −1 convention. Second, the K₃ resolution structure (from the Filatov-constrained three-qubit obstruction) determines T₃ ∈ {+1/2, −1/2} for doublet members and T₃ = 0 for singlets and the Class 4 a-chiral state. Third, the Zitterbewegung zigzag relates left-handed and right-handed components by preserving Q while sending T₃ → 0 on the right-handed leg. The Gell-Mann-Nishijima relation Q = T₃ + Y/2 then gives every Y value observed in the Standard Model, including the fractional quark charges, the sterile-neutrino Y = 0, and the conventional right-handed singlet assignments. Abelian anomaly cancellation is automatic from the same tracelessness condition that fixes the eigenvalues. No empirical input other than the electron's sign convention.

---

*Companion to `ghz_to_c3_theorem.md`, `w_to_su2l_doublet_theorem.md`, and `k3_obstruction_chirality_sterile.md`. Together, these four documents derive: colour (GHZ → ℂ³), weak isospin (W → SU(2)_L doublets), generations + sterile sector (K₃ obstruction), and hypercharge (trace condition on 𝕆). The remaining sector that is not yet fully written up is the derivation of SU(2)_L × U(1)_Y structure from a single electroweak object, which requires identifying the photon direction as the K₃-blind linear combination — tracked separately as a follow-up to the electroweak unification conversation.*
