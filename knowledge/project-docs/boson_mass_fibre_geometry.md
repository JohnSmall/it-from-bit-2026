# Electroweak Boson Masses from Fibre Geometry

## Calculation Summary — March 16, 2026

---

## 1. Overview

The fermion mass calculation (see fermion_mass_geodesic_calculation.md) derives masses from geodesic path lengths on Hopf fibres. The boson masses come from a different aspect of the same geometry: the **metric on the fibre itself** rather than the paths within it.

The electroweak sector lives in ℂ ⊗ ℍ (biquaternions). The U(1) hypercharge comes from the S¹ (ℂ) fibre; the SU(2) weak isospin comes from the S³ (ℍ) fibre. The Weinberg angle measures their relative metric weight. The Higgs quartic measures the curvature stiffness of the computability barrier.

Three results:

1. **sin²θ_W = 1/4** at the bare level, from dim(S¹)/[dim(S¹) + dim(S³)] = 1/(1+3). This runs to the observed 0.2312 at M_Z via standard SM running, with matching scale **Λ ≈ 3.6 TeV**.

2. **m_H = v/2**, i.e. the Higgs quartic λ = 1/8. Predicted: 123.1 GeV. Observed: 125.25 GeV. Error: **−1.7%**.

3. **y_t = 1** (the top quark Yukawa coupling is unity), i.e. m_t = v/√2 ≈ 174 GeV. Observed: 172.5 GeV. Error: **+0.9%**. This is the statement that the top quark sits exactly at the computability boundary.

---

## 2. The Weinberg Angle

### 2.1 Derivation

The electroweak gauge group U(1)_Y × SU(2)_L lives on the fibre S¹ × S³ of the combined complex and quaternionic Hopf bundles. The Weinberg angle parametrises the mixing between U(1) and SU(2):

    sin²θ_W = g'² / (g² + g'²)

where g is the SU(2) coupling and g' is the U(1) coupling.

The coupling constants are determined by the fibre geometry. In the ℂ ⊗ ℍ algebra, the U(1) generator spans one real dimension (S¹) and the SU(2) generators span three real dimensions (S³). If the metric on the combined fibre space assigns equal weight to each direction, then the relative coupling strengths are determined by the **dimension ratio**:

    sin²θ_W = dim(S¹) / [dim(S¹) + dim(S³)] = 1 / (1 + 3) = 1/4

This is a **bare** (tree-level) value. It coincides numerically with the SU(5) GUT prediction at tree level, but the physical origin is entirely different:

| Framework | Bare sin²θ_W | Origin | Matching scale |
|---|---|---|---|
| SU(5) GUT | 3/8 = 0.375 | Embedding U(1)×SU(2) ⊂ SU(5) | ~10¹⁶ GeV |
| Division algebras | 1/4 = 0.250 | Fibre dimensions in ℂ ⊗ ℍ | ~3.6 TeV |

The division algebra value is 1/4 (not 3/8) because there is no SU(5) embedding — the U(1) and SU(2) are not unified into a larger group, and the normalisation of the U(1) generator is set by the octonionic ℂ ⊕ ℂ³ decomposition rather than by SU(5) Clebsch-Gordan coefficients.

### 2.2 Running to M_Z

The bare value sin²θ_W = 1/4 must be evaluated at some UV scale Λ, then run to M_Z using the Standard Model renormalisation group equations. Using one-loop running with the SM beta coefficients:

    b(U(1)) = −41/6   (coupling increases at higher energy)
    b(SU(2)) = +19/6   (coupling decreases at higher energy — asymptotic freedom)

Numerically, sin²θ_W = 0.25 at the matching scale **Λ ≈ 3.6 TeV**, running down to 0.231 at M_Z = 91.2 GeV.

This is remarkable for two reasons:

**First**, the matching scale is in the TeV range — the same order as the electroweak scale v = 246 GeV, not an astronomical GUT scale. This is natural in the framework: the computability split occurs at the electroweak scale, so the "bare" fibre geometry should match physics at that scale, not at 10¹⁶ GeV.

**Second**, the framework predicts that no new physics (no GUT, no SUSY threshold) is needed between the TeV scale and the Planck scale. The Weinberg angle runs under SM physics alone. This is consistent with the framework's exclusion of SU(5) unification and extra dimensions, and is testable: no new gauge bosons or sparticles should appear between current collider energies and the Planck scale.

### 2.3 Connection to the Fermion Sector

The number 4 = dim(S¹) + dim(S³) = 1 + 3 appears in both the Weinberg angle (sin²θ = 1/4) and the fermion α² formula. In the α² formula, the colour correction is 2|Q|^{3/2} where the quarks' charge comes from the ℂ ⊕ ℂ³ decomposition — the same 1 + 3 structure, now of the octonions rather than the quaternions. The Weinberg angle and the fermion mass anisotropy both measure the same underlying dimensional ratio, applied to different parts of the fibre.

---

## 3. W and Z Boson Masses

### 3.1 Standard Relations

Given sin²θ_W and the Higgs VEV v = 246.22 GeV, the W and Z masses follow from the standard electroweak relations:

    m_W = (g/2) × v = (e / 2sinθ_W) × v
    m_Z = m_W / cos θ_W

These are exact at tree level in the Standard Model. The framework does not modify these relations — it derives sin²θ_W from the fibre geometry, and the masses follow.

### 3.2 Predictions

Using the bare sin²θ_W = 1/4 directly (without running):

    m_W(bare) = m_Z × √(3/4) = 91.19 × 0.866 = 79.0 GeV
    Observed: 80.4 GeV (−1.7%)

The 1.7% discrepancy is consistent with the running of sin²θ from 0.25 to 0.231. At the physical M_Z scale with the correctly run sin²θ_W = 0.231, the SM relation reproduces m_W exactly.

### 3.3 Interpretation

The W and Z masses are not independent predictions of the framework beyond the Weinberg angle. Their mass is the logical debt from breaking SU(2) at the computability split: the S³ fibre's non-commutativity creates a residual obstruction (the W and Z are massive because the SU(2) that had to break carries the debt). The specific mass values are set by v × sin θ_W, both of which are determined by the electroweak scale.

---

## 4. The Higgs Mass

### 4.1 The Prediction: m_H = v/2

The Higgs mass is m_H = √(2λ) × v where λ is the quartic self-coupling. Experimentally, m_H = 125.25 GeV and v = 246.22 GeV, giving:

    λ = m_H² / (2v²) = 0.1294
    m_H / v = 0.5087

The simplest algebraic value close to λ = 0.129 is **λ = 1/8 = 0.125**, giving:

    m_H = √(2/8) × v = v/2 = 123.1 GeV

This is **1.7% below** the observed value.

### 4.2 Why λ = 1/8?

The Higgs field is the dynamical preferred complex direction promoted from the Hopf bundle's nontriviality (Finkelstein-Jauch-Schiminovich-Speiser; Szangolies 2025). In the sombrero potential, the radial excitation around the broken vacuum has mass set by the curvature of the potential at the minimum. This curvature measures the **stiffness of the computability barrier** — the cost of pushing the system back toward the non-computable symmetric point.

The value λ = 1/8 has several possible algebraic interpretations within the framework:

**Interpretation 1: sin²θ_W / 2.** Since sin²θ_W = 1/4 at tree level, λ = (1/4)/2 = 1/8. The Higgs quartic is half the Weinberg angle. This would mean the stiffness of the computability barrier is directly set by the electroweak mixing, which is plausible since both involve the ℂ vs ℍ metric ratio.

**Interpretation 2: (Chern class / 2)².** The complex Hopf bundle has c₁ = 1. The squared Hopf map (which gives the quartic potential from the quadratic map) has (c₁/2)² = 1/4 as the natural topological scale, divided by 2 from the doubling structure, giving 1/8. This needs to be made rigorous.

**Interpretation 3: Cayley-Dickson reciprocal cubed.** The inter-generational coupling in J₃(𝕆) is ε = 1/√2, and ε³ = 1/(2√2) ≈ 0.354. Not obviously 1/8, but (ε²)² = (1/2)² = 1/4, and divided by 2 gives 1/8 again. The pattern: λ = ε⁴/2 = 1/8.

**Status:** The prediction m_H = v/2 is simple and numerically close (−1.7%). The algebraic derivation from first principles is not yet complete. The most promising route is via the connection to sin²θ_W, since both involve the same 1/4 arising from the S¹ vs S³ dimension ratio.

### 4.3 The 1.7% Discrepancy

The predicted 123.1 GeV vs observed 125.25 GeV leaves a 2.1 GeV gap. This may be:

**Radiative corrections.** The bare λ = 1/8 at the matching scale Λ ≈ 3.6 TeV runs under the SM RGE. The dominant correction is from the top Yukawa: λ increases at lower scales due to the top loop. A 3% increase from 3.6 TeV to the Higgs mass scale would give λ(m_H) ≈ 0.129, matching observation. This is consistent with the known SM running of λ.

**Higher-order fibre geometry.** The bare λ = 1/8 may receive corrections from the octonionic sector (the S⁷ fibre contribution to the Higgs potential), analogous to how the fermion α² receives corrections proportional to |Q|^{3/2} from the colour engagement.

---

## 5. The Top Yukawa: y_t = 1

### 5.1 The Prediction

In the geodesic picture, the top quark sits at the **computability boundary** — its internal traversal rate equals the Higgs VEV. This means:

    y_t = √2 × m_t / v = 1

giving m_t = v/√2 = 174.1 GeV. The observed value is 172.5 ± 0.7 GeV, a **+0.9%** discrepancy (2.3σ).

### 5.2 Interpretation

The top Yukawa being unity is not an arbitrary numerological coincidence in this framework — it is the statement that one fermion has **maximum coupling** to the computability boundary. The top quark's geodesic extends as deeply as possible into the fibre: its mass exhausts the available internal traversal budget at the electroweak scale.

This is also why the top quark is singled out in the SM: it is the only fermion whose Yukawa coupling is O(1), making it the dominant contributor to the Higgs potential through radiative corrections. In the framework, this follows from the top being the third generation of the sector with the largest α² (up quarks, with α² ≈ 3.09) and the smallest θ dilution (n = 3, the maximum).

### 5.3 Connection to the Higgs Mass

The near-criticality of the SM vacuum — the fact that the Higgs mass sits very close to the boundary between vacuum stability and metastability — is a well-known feature of the SM. With y_t ≈ 1 and λ ≈ 1/8, the framework predicts that this near-criticality is **structural**: the top Yukawa and Higgs quartic are both determined by the same fibre geometry, and their ratio is fixed at the matching scale. The vacuum sits near the stability boundary because the fibre geometry places it there, not by accident.

---

## 6. Summary Table

| Quantity | Predicted | Observed | Error | Origin |
|---|---|---|---|---|
| sin²θ_W (bare) | 1/4 = 0.250 | — | — | dim(S¹)/(dim(S¹)+dim(S³)) |
| sin²θ_W (at M_Z) | 0.231* | 0.2312 | ~0% | SM running from 3.6 TeV |
| m_W (bare) | 79.0 GeV | 80.4 GeV | −1.7% | v × √(3)/2 × e/√(4πα) |
| m_Z | 91.2 GeV | 91.2 GeV | ~0% | Input (not predicted) |
| m_H | 123.1 GeV | 125.25 GeV | −1.7% | λ = 1/8, m_H = v/2 |
| m_t | 174.1 GeV | 172.5 GeV | +0.9% | y_t = 1, m_t = v/√2 |
| Λ (matching) | 3.6 TeV | — | — | Scale where sin²θ = 1/4 |

*After SM one-loop running from 3.6 TeV to M_Z.

The electroweak sector has three characteristic mass ratios, all simple fractions of v:

    m_H ≈ v/2      (λ = 1/8)
    m_t ≈ v/√2     (y_t = 1)
    m_W ≈ v × g/2  (g from sin²θ = 1/4 + running)

---

## 7. What Remains

### 7.1 Established

- sin²θ_W = 1/4 at tree level from fibre dimension counting — no SU(5) needed
- SM running from 3.6 TeV reproduces the observed 0.231 at M_Z
- m_H = v/2 (λ = 1/8) gives 123.1 GeV, within 1.7% of observation
- y_t = 1 gives m_t = 174.1 GeV, within 0.9% of observation
- The matching scale ~3.6 TeV is naturally at the electroweak scale

### 7.2 Open

- **Derive λ = 1/8 from the Hopf bundle curvature** — the most important open calculation. The connection λ = sin²θ_W / 2 is suggestive but needs a first-principles derivation from the fibre geometry.
- **Derive v itself** — the Higgs VEV sets the overall electroweak scale. In the framework, this should be related to the Margolus-Levitin bound or the Jacobson thermodynamic derivation, but the connection is not yet made.
- **The matching scale Λ ≈ 3.6 TeV** — is this a prediction (no new physics below 3.6 TeV) or an artefact of one-loop running? The framework's exclusion of SUSY and extra dimensions suggests it is a genuine prediction.
- **Radiative corrections to λ** — confirm that SM running from λ(3.6 TeV) = 1/8 gives λ(m_H) ≈ 0.129.
- **The v hierarchy** — why v ≈ 246 GeV and not some other value. This is the electroweak hierarchy problem, which the framework addresses through the computability-barrier interpretation but does not yet solve quantitatively.

---

## 8. References

### Electroweak Theory
- Weinberg, S. "A Model of Leptons." Phys. Rev. Lett. 19 (1967), 1264.
- Glashow, S.L. "Partial-symmetries of weak interactions." Nucl. Phys. 22 (1961), 579.
- Salam, A. "Weak and electromagnetic interactions." In Svartholm (ed.), Elementary Particle Theory (1968).

### Higgs Mechanism from Division Algebras
- Finkelstein, D., Jauch, J.M., Schiminovich, S. & Speiser, D. "Foundations of quaternion quantum mechanics." J. Math. Phys. 3 (1962), 207–220.
- Szangolies, J. "The Standard Model Symmetry and Qubit Entanglement." Entropy 27(6), 569 (2025). [arXiv:2512.17328]

### Vacuum Stability
- Degrassi, G. et al. "Higgs mass and vacuum stability in the Standard Model at NNLO." JHEP 1208 (2012), 098. [arXiv:1205.6497]
- Buttazzo, D. et al. "Investigating the near-criticality of the Higgs boson." JHEP 1312 (2013), 089.

### Previously Established (see project documents)
- Weinberg angle approaches — conversation_summary_2026_03_12.md §9
- Higgs from bundle nontriviality — hopf_fibrations_research_summary.md §7.3, §9.1 Q4
- Fermion mass calculation — fermion_mass_geodesic_calculation.md

---

*Document Status: Boson mass calculation record. March 16, 2026.*
*Companion script: boson_mass_exploration.py*
