/-
Paper 1, appendix_ghz_w_proofs_2026-06-11.tex §app:ghz-proof and §app:w-proof:
`prop:ghz` (GHZ confinement, forward direction), `app:cor:s5` (colour equator),
`app:thm:char` (Characterisation of the GHZ orbit), `prop:w-access` (W accessibility),
`app:cor:instances`.

What is formalised:
 * the canonical `|GHZ⟩` and `|W⟩`, normalised, and the tilted states `α|000⟩ + β|111⟩`;
 * `prop:ghz` forward: under every local unitary `U₁ ⊗ U₂ ⊗ U₃` and each of the three splits, the
   `ℂ`-projection of the Hopf image of `|GHZ⟩` vanishes (`ghz_forward`);
 * `app:cor:s5`: on the GHZ orbit `x₉ = 0`, `π_ℂ(𝐡) = 0`, `|w|² = 1` for the first split;
 * `app:thm:char` (i)⇔(ii) for a cut: the `ℂ`-fraction vanishes for every first-qubit unitary
   and every internal unitary iff the cut's marginal is maximally mixed; and (iii)⇒(i);
 * `prop:w-access`: on the W orbit (first split) `⟨o₁,o₂⟩ = conj(U₀₀) U₁₀ / 3`, so it vanishes iff
   `U₀₀ U₁₀ = 0`; the ceiling is `1/9`, attained;
 * `app:cor:instances`: `r = 0` for GHZ, `r² = 1/9` for W, `r = |α|² − |β|²` for the tilted states.
Not formalised: (ii)⇒(iii), which rests on the Acín et al. canonical form (cited), and the
"measure zero" phrasing of the W vanishing locus (the locus itself, `U₀₀U₁₀ = 0`, is formalised).
-/
import ItFromBit.Ceiling

open Matrix ComplexConjugate Real
open scoped Kronecker

namespace ItFromBit

/-- `(1/√2 : ℂ)` and `(1/√3 : ℂ)` with their squares. -/
noncomputable def s2 : ℂ := ((Real.sqrt 2)⁻¹ : ℝ)
noncomputable def s3 : ℂ := ((Real.sqrt 3)⁻¹ : ℝ)

lemma conj_s2 : conj s2 = s2 := by simp [s2]
lemma conj_s3 : conj s3 = s3 := by simp [s3]
lemma s2_mul_s2 : s2 * s2 = 1 / 2 := by
  simp only [s2]; rw [← Complex.ofReal_mul, ← mul_inv, Real.mul_self_sqrt (by norm_num)]; push_cast; ring
lemma s3_mul_s3 : s3 * s3 = 1 / 3 := by
  simp only [s3]; rw [← Complex.ofReal_mul, ← mul_inv, Real.mul_self_sqrt (by norm_num)]; push_cast; ring
lemma normSq_s2 : Complex.normSq s2 = 1 / 2 := by
  simp only [s2, Complex.normSq_ofReal]; rw [← mul_inv, Real.mul_self_sqrt (by norm_num)]; norm_num
lemma normSq_s3 : Complex.normSq s3 = 1 / 3 := by
  simp only [s3, Complex.normSq_ofReal]; rw [← mul_inv, Real.mul_self_sqrt (by norm_num)]; norm_num

/-- `|GHZ⟩ = (|000⟩ + |111⟩)/√2` on `Q3` (named `ghz3` to avoid `ThreeQubitMarginals.GHZ`). -/
noncomputable def ghz3 : Q3 → ℂ := fun q =>
  if (q.1 = 0 ∧ q.2.1 = 0 ∧ q.2.2 = 0) ∨ (q.1 = 1 ∧ q.2.1 = 1 ∧ q.2.2 = 1) then s2 else 0

/-- `|W⟩ = (|100⟩ + |010⟩ + |001⟩)/√3`. -/
noncomputable def Wst : Q3 → ℂ := fun q =>
  if (q.1 = 1 ∧ q.2.1 = 0 ∧ q.2.2 = 0) ∨ (q.1 = 0 ∧ q.2.1 = 1 ∧ q.2.2 = 0)
    ∨ (q.1 = 0 ∧ q.2.1 = 0 ∧ q.2.2 = 1) then s3 else 0

/-- The tilted states `α|000⟩ + β|111⟩`. -/
def tilted (α β : ℂ) : Q3 → ℂ := fun q =>
  if q.1 = 0 ∧ q.2.1 = 0 ∧ q.2.2 = 0 then α else if q.1 = 1 ∧ q.2.1 = 1 ∧ q.2.2 = 1 then β else 0

/-! ### Branch data of the canonical states -/

theorem ghz_br1_orth : ip (br1 ghz3 0) (br1 ghz3 1) = 0 := by
  simp [ip, dotProduct, br1, ghz3, Fintype.sum_prod_type, Fin.sum_univ_two]
theorem ghz_br1_nrm : nrm (br1 ghz3 0) = 1 / 2 ∧ nrm (br1 ghz3 1) = 1 / 2 := by
  constructor <;> simp [nrm, br1, ghz3, Fintype.sum_prod_type, Fin.sum_univ_two, normSq_s2]
theorem ghz_br2_orth : ip (br2 ghz3 0) (br2 ghz3 1) = 0 := by
  simp [ip, dotProduct, br2, ghz3, Fintype.sum_prod_type, Fin.sum_univ_two]
theorem ghz_br2_nrm : nrm (br2 ghz3 0) = 1 / 2 ∧ nrm (br2 ghz3 1) = 1 / 2 := by
  constructor <;> simp [nrm, br2, ghz3, Fintype.sum_prod_type, Fin.sum_univ_two, normSq_s2]
theorem ghz_br3_orth : ip (br3 ghz3 0) (br3 ghz3 1) = 0 := by
  simp [ip, dotProduct, br3, ghz3, Fintype.sum_prod_type, Fin.sum_univ_two]
theorem ghz_br3_nrm : nrm (br3 ghz3 0) = 1 / 2 ∧ nrm (br3 ghz3 1) = 1 / 2 := by
  constructor <;> simp [nrm, br3, ghz3, Fintype.sum_prod_type, Fin.sum_univ_two, normSq_s2]

theorem w_br1_orth : ip (br1 Wst 0) (br1 Wst 1) = 0 := by
  simp [ip, dotProduct, br1, Wst, Fintype.sum_prod_type, Fin.sum_univ_two]
theorem w_br1_nrm : nrm (br1 Wst 0) = 2 / 3 ∧ nrm (br1 Wst 1) = 1 / 3 := by
  constructor <;> simp [nrm, br1, Wst, Fintype.sum_prod_type, Fin.sum_univ_two, normSq_s3]
  norm_num

theorem tilted_br1_orth (α β : ℂ) : ip (br1 (tilted α β) 0) (br1 (tilted α β) 1) = 0 := by
  simp [ip, dotProduct, br1, tilted, Fintype.sum_prod_type, Fin.sum_univ_two]
theorem tilted_br1_nrm (α β : ℂ) :
    nrm (br1 (tilted α β) 0) = Complex.normSq α ∧ nrm (br1 (tilted α β) 1) = Complex.normSq β := by
  constructor <;> simp [nrm, br1, tilted, Fintype.sum_prod_type, Fin.sum_univ_two]

/-! ### The ghz3 forward direction, all three splits -/

/-- Unitarity data for a local unitary. -/
structure LU where
  U₁ : Matrix (Fin 2) (Fin 2) ℂ
  U₂ : Matrix (Fin 2) (Fin 2) ℂ
  U₃ : Matrix (Fin 2) (Fin 2) ℂ
  h₁ : U₁ ∈ Matrix.unitaryGroup (Fin 2) ℂ
  h₂ : U₂ ∈ Matrix.unitaryGroup (Fin 2) ℂ
  h₃ : U₃ ∈ Matrix.unitaryGroup (Fin 2) ℂ

/-- A split's `ℂ`-projection after a local unitary, for a state whose branches along that split
are orthogonal with equal norms, vanishes. Stated for the first split; `br2_act`, `br3_act` give
the other two by the same lemma. -/
theorem piC_br1_act_eq_zero (L : LU) (ψ : Q3 → ℂ)
    (horth : ip (br1 ψ 0) (br1 ψ 1) = 0) (hnorm : nrm (br1 ψ 0) = nrm (br1 ψ 1)) :
    piC (hopf (br1 (act L.U₁ L.U₂ L.U₃ ψ) 0) (br1 (act L.U₁ L.U₂ L.U₃ ψ) 1)) = 0 := by
  rw [hopf, br1_act, br1_act]
  exact piC_vanishes_of_maximally_mixed L.U₁ (Matrix.mem_unitaryGroup_iff.mp L.h₁) _
    (kron_star_mul_self _ _ (Matrix.mem_unitaryGroup_iff'.mp L.h₂)
      (Matrix.mem_unitaryGroup_iff'.mp L.h₃)) (br1 ψ) horth
    (by rw [ip_self, ip_self, hnorm])

theorem piC_br2_act_eq_zero (L : LU) (ψ : Q3 → ℂ)
    (horth : ip (br2 ψ 0) (br2 ψ 1) = 0) (hnorm : nrm (br2 ψ 0) = nrm (br2 ψ 1)) :
    piC (hopf (br2 (act L.U₁ L.U₂ L.U₃ ψ) 0) (br2 (act L.U₁ L.U₂ L.U₃ ψ) 1)) = 0 := by
  rw [hopf, br2_act, br2_act]
  exact piC_vanishes_of_maximally_mixed L.U₂ (Matrix.mem_unitaryGroup_iff.mp L.h₂) _
    (kron_star_mul_self _ _ (Matrix.mem_unitaryGroup_iff'.mp L.h₁)
      (Matrix.mem_unitaryGroup_iff'.mp L.h₃)) (br2 ψ) horth
    (by rw [ip_self, ip_self, hnorm])

theorem piC_br3_act_eq_zero (L : LU) (ψ : Q3 → ℂ)
    (horth : ip (br3 ψ 0) (br3 ψ 1) = 0) (hnorm : nrm (br3 ψ 0) = nrm (br3 ψ 1)) :
    piC (hopf (br3 (act L.U₁ L.U₂ L.U₃ ψ) 0) (br3 (act L.U₁ L.U₂ L.U₃ ψ) 1)) = 0 := by
  rw [hopf, br3_act, br3_act]
  exact piC_vanishes_of_maximally_mixed L.U₃ (Matrix.mem_unitaryGroup_iff.mp L.h₃) _
    (kron_star_mul_self _ _ (Matrix.mem_unitaryGroup_iff'.mp L.h₁)
      (Matrix.mem_unitaryGroup_iff'.mp L.h₂)) (br3 ψ) horth
    (by rw [ip_self, ip_self, hnorm])

/-- `prop:ghz`, forward direction: on the whole local-unitary orbit of `|ghz3⟩` the
`ℂ`-projection vanishes under each of the three splits. -/
theorem ghz_forward (L : LU) :
    piC (hopf (br1 (act L.U₁ L.U₂ L.U₃ ghz3) 0) (br1 (act L.U₁ L.U₂ L.U₃ ghz3) 1)) = 0 ∧
    piC (hopf (br2 (act L.U₁ L.U₂ L.U₃ ghz3) 0) (br2 (act L.U₁ L.U₂ L.U₃ ghz3) 1)) = 0 ∧
    piC (hopf (br3 (act L.U₁ L.U₂ L.U₃ ghz3) 0) (br3 (act L.U₁ L.U₂ L.U₃ ghz3) 1)) = 0 :=
  ⟨piC_br1_act_eq_zero L ghz3 ghz_br1_orth (by rw [ghz_br1_nrm.1, ghz_br1_nrm.2]),
   piC_br2_act_eq_zero L ghz3 ghz_br2_orth (by rw [ghz_br2_nrm.1, ghz_br2_nrm.2]),
   piC_br3_act_eq_zero L ghz3 ghz_br3_orth (by rw [ghz_br3_nrm.1, ghz_br3_nrm.2])⟩

/-- Composition of local unitaries: `(iii) ⇒ (i)` needs that the orbit of an orbit point is the
orbit. -/
theorem act_act (L M : LU) (ψ : Q3 → ℂ) :
    act L.U₁ L.U₂ L.U₃ (act M.U₁ M.U₂ M.U₃ ψ)
      = act (L.U₁ * M.U₁) (L.U₂ * M.U₂) (L.U₃ * M.U₃) ψ := by
  simp only [act, mulVec_mulVec, mul_kronecker_mul]

/-- `app:thm:char`, (iii) ⇒ (i), first split (the other two are identical): every state on the
ghz3 orbit has vanishing `ℂ`-projection under every further local unitary. -/
theorem char_iii_to_i (M L : LU) :
    piC (hopf (br1 (act L.U₁ L.U₂ L.U₃ (act M.U₁ M.U₂ M.U₃ ghz3)) 0)
              (br1 (act L.U₁ L.U₂ L.U₃ (act M.U₁ M.U₂ M.U₃ ghz3)) 1)) = 0 := by
  rw [act_act]
  exact (ghz_forward ⟨_, _, _, Submonoid.mul_mem _ L.h₁ M.h₁, Submonoid.mul_mem _ L.h₂ M.h₂,
    Submonoid.mul_mem _ L.h₃ M.h₃⟩).1

/-! ### The characterisation (i) ⇔ (ii) for a cut -/

/-- "Maximally mixed" for the cut: branches orthogonal with equal norm. -/
def MaxMixed (φ : Fin 2 → Q2 → ℂ) : Prop := ip (φ 0) (φ 1) = 0 ∧ nrm (φ 0) = nrm (φ 1)

theorem maxMixed_iff_rSq (φ : Fin 2 → Q2 → ℂ) : MaxMixed φ ↔ rSq (φ 0) (φ 1) = 0 := by
  rw [rSq_eq', MaxMixed, rho01]
  constructor
  · rintro ⟨h0, h1⟩
    rw [ip_swap, h0, map_zero, Complex.normSq_zero, h1]; ring
  · intro h
    have hsq : (nrm (φ 0) - nrm (φ 1)) ^ 2 = 0 := by
      nlinarith [sq_nonneg (nrm (φ 0) - nrm (φ 1)), Complex.normSq_nonneg (ip (φ 1) (φ 0))]
    have hρ : Complex.normSq (ip (φ 1) (φ 0)) = 0 := by
      nlinarith [sq_nonneg (nrm (φ 0) - nrm (φ 1)), Complex.normSq_nonneg (ip (φ 1) (φ 0))]
    refine ⟨?_, by nlinarith [hsq]⟩
    rw [ip_swap, map_eq_zero_iff _ (RingHom.injective _)]
    exact Complex.normSq_eq_zero.mp hρ

/-- `app:thm:char` (i) ⇔ (ii) for one cut: the `ℂ`-fraction vanishes for every first-qubit
unitary (internal unitaries change neither side, by `ip_mulVec`) iff the cut is maximally mixed.
Normalisation `n₀ + n₁ = 1` is assumed. -/
theorem char_i_iff_ii (φ : Fin 2 → Q2 → ℂ) (h : nrm (φ 0) + nrm (φ 1) = 1) :
    (∀ U ∈ Matrix.unitaryGroup (Fin 2) ℂ, cfrac (mix U φ 0) (mix U φ 1) = 0) ↔ MaxMixed φ := by
  rw [maxMixed_iff_rSq]
  obtain ⟨hle, t, ht⟩ := ceiling φ h
  constructor
  · intro hall
    rw [← ht, hall _ (rotU_mem t)]
  · intro h0 U hU
    have h1 := hle U hU
    rw [h0] at h1
    have h2 : 0 ≤ cfrac (mix U φ 0) (mix U φ 1) := by
      unfold cfrac; exact div_nonneg (Complex.normSq_nonneg _) (by
        unfold Oct.normSq; positivity)
    linarith

/-! ### Instances -/

/-- `app:cor:instances` (i): `r = 0` on the ghz3 cut. -/
theorem ghz_rSq : rSq (br1 ghz3 0) (br1 ghz3 1) = 0 :=
  (maxMixed_iff_rSq (br1 ghz3)).mp ⟨ghz_br1_orth, by rw [ghz_br1_nrm.1, ghz_br1_nrm.2]⟩

/-- `app:cor:s5`: on the ghz3 cut, `x₉ = 0`, `π_ℂ(𝐡) = 0` and `|w|² = 1`: the image lies on the
colour equator `S⁵`. -/
theorem ghz_colour_equator :
    x9 (br1 ghz3 0) (br1 ghz3 1) = 0 ∧ piC (hopf (br1 ghz3 0) (br1 ghz3 1)) = 0 ∧
    wSq (br1 ghz3 0) (br1 ghz3 1) = 1 := by
  refine ⟨?_, ?_, ?_⟩
  · simp only [x9, ghz_br1_nrm.1, ghz_br1_nrm.2]; ring
  · rw [piC_hopf, rho01, ip_swap, ghz_br1_orth, map_zero]
  · have := rSq_add_wSq (br1 ghz3 0) (br1 ghz3 1) (by rw [ghz_br1_nrm.1, ghz_br1_nrm.2]; norm_num)
    rw [ghz_rSq] at this; linarith

/-- `app:cor:instances` (ii): `r² = 1/9` on the W cut, so the ceiling is `1/9`, attained. -/
theorem w_rSq : rSq (br1 Wst 0) (br1 Wst 1) = 1 / 9 := by
  rw [rSq_eq', rho01, ip_swap, w_br1_orth, map_zero, Complex.normSq_zero, w_br1_nrm.1, w_br1_nrm.2]
  norm_num

/-- `prop:w-access`, the ceiling: `C_frac ≤ 1/9` on the W orbit (first split, every first-qubit
unitary), and `1/9` is attained. -/
theorem w_ceiling :
    (∀ U ∈ Matrix.unitaryGroup (Fin 2) ℂ, cfrac (mix U (br1 Wst) 0) (mix U (br1 Wst) 1) ≤ 1 / 9) ∧
    (∃ t : ℝ, cfrac (mix (rotU t) (br1 Wst) 0) (mix (rotU t) (br1 Wst) 1) = 1 / 9) := by
  have h := ceiling (br1 Wst) (by rw [w_br1_nrm.1, w_br1_nrm.2]; norm_num)
  rw [w_rSq] at h; exact h

/-- `prop:w-access`, the formula: after any first-qubit unitary the branch inner product is
`conj(U₀₀) U₁₀ / 3`, so it vanishes exactly when `U₀₀ U₁₀ = 0` (the paper's `ab = 0`). -/
theorem w_ip_formula (U : Matrix (Fin 2) (Fin 2) ℂ) (hU : U ∈ Matrix.unitaryGroup (Fin 2) ℂ) :
    ip (mix U (br1 Wst) 0) (mix U (br1 Wst) 1) = conj (U 0 0) * U 1 0 / 3 := by
  have hUU : U * star U = 1 := Matrix.mem_unitaryGroup_iff.mp hU
  have h01 : (U * star U) 1 0 = 0 := by rw [hUU]; simp
  have hrel : conj (U 0 0) * U 1 0 + conj (U 0 1) * U 1 1 = 0 := by
    simpa [Matrix.mul_apply, Fin.sum_univ_two, star_eq_conjTranspose, conjTranspose_apply,
      mul_comm] using h01
  have h10 : ip (br1 Wst 1) (br1 Wst 0) = 0 := by rw [ip_swap, w_br1_orth, map_zero]
  rw [ip_mix, w_br1_orth, h10, ip_self, ip_self, w_br1_nrm.1, w_br1_nrm.2]
  push_cast
  linear_combination (1 / 3 : ℂ) * hrel

theorem w_ip_eq_zero_iff (U : Matrix (Fin 2) (Fin 2) ℂ) (hU : U ∈ Matrix.unitaryGroup (Fin 2) ℂ) :
    ip (mix U (br1 Wst) 0) (mix U (br1 Wst) 1) = 0 ↔ U 0 0 * U 1 0 = 0 := by
  rw [w_ip_formula U hU, div_eq_zero_iff, mul_eq_zero, mul_eq_zero, map_eq_zero_iff _ (RingHom.injective _)]
  norm_num

/-- `app:cor:instances` (iii): the tilted states have `r = |α|² − |β|²` on the first cut. -/
theorem tilted_rSq (α β : ℂ) :
    rSq (br1 (tilted α β) 0) (br1 (tilted α β) 1) = (Complex.normSq α - Complex.normSq β) ^ 2 := by
  rw [rSq_eq', rho01, ip_swap, tilted_br1_orth, map_zero, Complex.normSq_zero,
    (tilted_br1_nrm α β).1, (tilted_br1_nrm α β).2]
  ring

end ItFromBit
