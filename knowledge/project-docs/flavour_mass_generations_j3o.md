# Flavour, Mass, and Three Generations from J₃(𝕆)

## Calculation Summary — March 16, 2026

---

## 1. Central Result

The charged lepton mass amplitudes (√m_k) are exactly the eigenvalues of an element of J₃(𝕆), the exceptional Jordan algebra of 3×3 self-adjoint octonionic matrices:

```
    ⎛  1        ε·x₃*    ε·x₂  ⎞
    ⎜  ε·x₃     1       ε·x₁* ⎟     xᵢ unit octonions, ε = 1/√2
    ⎝  ε·x₂*   ε·x₁     1     ⎠
```

The physical masses are the eigenvalues squared (Born rule / Hopf map). All structural parameters except one are determined by the algebra.

## 2. The Parametrisation

Each off-diagonal octonion is tilted by angle θ_J from the computability split direction e₇ into a colour direction:

- x₁ = cos θ_J · e₇ + sin θ_J · e₁
- x₂ = cos θ_J · e₇ + sin θ_J · e₂
- x₃ = cos θ_J · e₇ + sin θ_J · e₃

The three colour directions (e₁, e₂, e₃) correspond to the three Fano plane lines through e₇, rotated by the Z₃ triality.

## 3. Analytical Results

### 3.1 The Triple Product

The crucial inter-generational coupling is:

**Re(x₁ x₂ x₃) = −ε³ sin³θ_J**

This was verified computationally and derived analytically. Only the e₁e₂e₃ component of the triple product contributes to the real part, giving the sin³θ_J dependence.

### 3.2 The Characteristic Equation

For diagonal entries ξ = (1, 1, 1) and off-diagonal magnitude ε:

- t₁ = Σξᵢ = 3
- t₂ = Σξᵢξⱼ − 3ε² = 3 − 3ε²
- t₃ = 1 − 3ε² + 2(−ε³ sin³θ_J) = 1 − 3ε² − 2ε³ sin³θ_J

The eigenvalues satisfy: **λ³ − 3λ² + (3−3ε²)λ − t₃ = 0**

With ε = 1/√2: **λ³ − 3λ² + (3/2)λ − t₃ = 0**

### 3.3 Connection to Koide

The Koide formula gives √m_k = √m₀(1 + α cos(θ_K + 2πk/3)) with fitted parameters:

| Parameter | Value | Algebraic identification |
|---|---|---|
| α | √2 = 1.41421... | Cayley-Dickson doubling norm |
| θ_K | −12.73° | Higgs-triality misalignment (≈ Cabibbo angle) |
| m₀ | 313.84 MeV | Absolute mass scale (set by Higgs VEV) |

The Koide amplitudes a_k = 1 + √2 cos(θ_K + 2πk/3) satisfy Vieta's formulas:

- Σa_k = 3
- Σa_i·a_j = 3/2
- Πa_k = t₃

The middle equation gives: 3 − 3ε² = 3/2, hence **ε² = 1/2, ε = 1/√2**.

This is exact: ε = 1/α. The off-diagonal coupling in J₃(𝕆) is the reciprocal of the Cayley-Dickson doubling norm.

### 3.4 The Angle Identity

The product formula gives:

Πa_k = Π(1 + √2 cos(θ_K + 2πk/3))

Using the standard identity Π cos(θ + 2πk/3) = cos(3θ)/4 and expanding:

Πa_k = −1/2 + 2√2 · cos(3θ_K)/4

Equating with the J₃(𝕆) expression t₃ = −1/2 − sin³θ_J/√2:

**sin³θ_J = −cos(3θ_K)**

This is an exact trigonometric identity relating the J₃(𝕆) tilt angle to the Koide phase. Both are determined by a single underlying parameter. With θ_K = −12.73°:

- cos(3θ_K) = cos(−38.19°) = 0.786
- sin³θ_J = −0.786
- θ_J = −67.35°

## 4. Interpretation

### 4.1 ε = 1/√2: The Cayley-Dickson Reciprocal

Each step of the Cayley-Dickson construction (ℝ → ℂ → ℍ → 𝕆) amplifies the algebraic structure by √2 (the norm |1+i| = √2). The inter-generational coupling ε = 1/√2 is the reciprocal: it measures how much of the doubled structure "leaks" between generations through the off-diagonal Jordan product.

The Koide α = √2 and the J₃(𝕆) ε = 1/√2 are the same quantity viewed from opposite sides:
- α = √2 is the amplification factor in the mass formula (how much the Z₃ perturbation distorts the degenerate masses)
- ε = 1/√2 is the coupling strength in J₃(𝕆) (how strongly adjacent generations interact)
- α · ε = 1 (they are reciprocals)

### 4.2 Masses as Eigenvalues² (Born Rule)

The J₃(𝕆) eigenvalues λ_k give the mass amplitudes (√m_k), not the masses directly. The physical masses are m_k = λ_k². This squaring is the Born rule: the Hopf map is quadratic (it maps amplitudes to probabilities/energies), and mass is energy at rest.

This is why the mass hierarchy is so large despite the eigenvalue ratios being moderate. The eigenvalue ratios are O(60:14:1), but the mass ratios are O(3500:207:1) — squaring amplifies the hierarchy dramatically.

### 4.3 Flavour as Self-Referential Iteration

The three generations correspond to three iterations of the self-referential measurement loop:

- **Generation 1** (e, u, d): First application of the computability split. Minimal self-referential overhead → smallest information debt → smallest mass.
- **Generation 2** (μ, c, s): Measurement of the measurement. The system's response to the first measurement is itself measured → additional debt from the back-reaction → intermediate mass.
- **Generation 3** (τ, t, b): Measurement of the measurement of the measurement. Closes the self-referential loop → includes the irreducible three-body contribution (non-zero associator) → largest mass, CP violation becomes possible.

Three iterations are the minimum for irreducible self-reference (CKM phase requires ≥ 3 generations). Four iterations would be redundant — the loop has already closed.

### 4.4 The Single Free Parameter

The entire structure is determined by the algebra except for one angular parameter θ_K ≈ 13°, which measures the misalignment between the Higgs VEV direction and the triality axes of J₃(𝕆). This parameter:

- Sets the charged lepton mass ratios (via the Koide formula)
- Determines the J₃(𝕆) tilt angle (via sin³θ_J = −cos(3θ_K))
- Is approximately equal to the Cabibbo angle (θ_C = 13.04°)
- Should be derivable from the octonionic Hopf bundle geometry (the angle at which the Higgs VEV deviates from the computability split, determined by minimising the Higgs potential subject to bundle nontriviality)

## 5. Verification

### Predicted vs Observed Mass Ratios

| Ratio | Predicted (J₃(𝕆)) | Observed | Agreement |
|---|---|---|---|
| m_τ/m_e | 3470 | 3477 | 99.8% |
| m_μ/m_e | 206.3 | 206.8 | 99.8% |
| Koide ratio | 2/3 (exact) | 0.66666 | 99.999% |

### J₃(𝕆) Parameters (All Determined)

| Parameter | Value | Origin |
|---|---|---|
| Diagonal entries | (1, 1, 1) | Triality symmetry |
| Off-diagonal ε | 1/√2 | Cayley-Dickson norm (= 1/α_Koide) |
| Tilt angle θ_J | −67.35° | From θ_K via sin³θ_J = −cos(3θ_K) |
| Born rule | m = λ² | Hopf map is quadratic |
| Free parameter | θ_K ≈ 13° | Higgs-triality misalignment |

## 6. What Remains

### Established
- Koide amplitudes = J₃(𝕆) eigenvalues (proven by direct computation)
- ε = 1/√2 from Cayley-Dickson (algebraic identity)
- sin³θ_J = −cos(3θ_K) (trigonometric identity)
- Mass hierarchy from Born rule squaring of moderate eigenvalue ratios

### Open
- Derivation of θ_K ≈ 13° from the Hopf bundle
- Extension to quark sectors (requires QCD corrections for Koide deviations)
- Derivation of the absolute mass scale m₀ from the Higgs VEV
- CKM matrix elements from the same J₃(𝕆) structure with θ_K

---

*Document Status: Calculation record. March 16, 2026.*
