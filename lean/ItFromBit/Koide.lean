/-
Paper 1, `prop:koide` (The Koide ratio from the doubling norm), masses_section_2026-06-08.tex.

Statement in the paper: for square-root masses of the `ℤ₃` form `eq:z3`,
  `√m_k = M (1 + α cos(δ + 2πk/3))`, k = 0, 1, 2,
the Koide ratio `eq:koide`, `(Σ m_k) / (Σ √m_k)²`, equals `(1 + α²/2)/3` independently of `M`
and `δ`; with `α² = 2` it is `2/3`.

What is formalised: the whole proposition, as a trigonometric identity over `ℝ`. The two
ingredients are `Σ_k cos(δ + 2πk/3) = 0` and `Σ_k cos²(δ + 2πk/3) = 3/2`, proved from the addition
formulae and the values of `cos`, `sin` at `π/3` and `π`. `M ≠ 0` is needed, since at `M = 0` the
ratio is `0/0`.
-/
import Mathlib

open Real

namespace ItFromBit

/-- `eq:z3`: the three triality images of one quantity. -/
noncomputable def sqrtMass (M α δ : ℝ) (k : Fin 3) : ℝ :=
  M * (1 + α * cos (δ + 2 * π * (k : ℝ) / 3))

/-- `eq:koide` for three masses given by their square roots. -/
noncomputable def koideRatio (s : Fin 3 → ℝ) : ℝ :=
  (∑ k, (s k) ^ 2) / (∑ k, s k) ^ 2

lemma cos_two_pi_div_three : cos (2 * π / 3) = -1 / 2 := by
  have : 2 * π / 3 = π - π / 3 := by ring
  rw [this, cos_pi_sub, cos_pi_div_three]; norm_num

lemma sin_two_pi_div_three : sin (2 * π / 3) = √3 / 2 := by
  have : 2 * π / 3 = π - π / 3 := by ring
  rw [this, sin_pi_sub, sin_pi_div_three]

lemma cos_four_pi_div_three : cos (4 * π / 3) = -1 / 2 := by
  have : 4 * π / 3 = π / 3 + π := by ring
  rw [this, cos_add_pi, cos_pi_div_three]; norm_num

lemma sin_four_pi_div_three : sin (4 * π / 3) = -(√3 / 2) := by
  have : 4 * π / 3 = π / 3 + π := by ring
  rw [this, sin_add_pi, sin_pi_div_three]

/-- The three phases spaced by `2π/3` have cosines summing to zero. -/
lemma sum_cos_third_turn (δ : ℝ) :
    cos δ + cos (δ + 2 * π / 3) + cos (δ + 4 * π / 3) = 0 := by
  rw [cos_add, cos_add, cos_two_pi_div_three, sin_two_pi_div_three,
    cos_four_pi_div_three, sin_four_pi_div_three]
  ring

/-- ... and squared cosines summing to `3/2`. -/
lemma sum_cos_sq_third_turn (δ : ℝ) :
    cos δ ^ 2 + cos (δ + 2 * π / 3) ^ 2 + cos (δ + 4 * π / 3) ^ 2 = 3 / 2 := by
  rw [cos_add, cos_add, cos_two_pi_div_three, sin_two_pi_div_three,
    cos_four_pi_div_three, sin_four_pi_div_three]
  have h3 : (√3 : ℝ) ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hδ := sin_sq_add_cos_sq δ
  nlinarith [h3, hδ]

/-- `prop:koide`, first clause: the ratio is `(1 + α²/2)/3`, independent of `M` and `δ`. -/
theorem koide_ratio_eq (M α δ : ℝ) (hM : M ≠ 0) :
    koideRatio (sqrtMass M α δ) = (1 + α ^ 2 / 2) / 3 := by
  unfold koideRatio sqrtMass
  rw [Fin.sum_univ_three, Fin.sum_univ_three]
  simp only [Fin.val_zero, Fin.val_one, Fin.val_two, Nat.cast_zero, Nat.cast_one, Nat.cast_ofNat]
  have e1 : δ + 2 * π * 0 / 3 = δ := by ring
  have e2 : δ + 2 * π * 1 / 3 = δ + 2 * π / 3 := by ring
  have e3 : δ + 2 * π * 2 / 3 = δ + 4 * π / 3 := by ring
  rw [e1, e2, e3]
  have hs := sum_cos_third_turn δ
  have hq := sum_cos_sq_third_turn δ
  have hden : (M * (1 + α * cos δ) + M * (1 + α * cos (δ + 2 * π / 3))
      + M * (1 + α * cos (δ + 4 * π / 3))) = 3 * M := by linear_combination M * α * hs
  rw [hden]
  have hnum : (M * (1 + α * cos δ)) ^ 2 + (M * (1 + α * cos (δ + 2 * π / 3))) ^ 2
      + (M * (1 + α * cos (δ + 4 * π / 3))) ^ 2 = 3 * M ^ 2 * (1 + α ^ 2 / 2) := by
    linear_combination (2 * M ^ 2 * α) * hs + (M ^ 2 * α ^ 2) * hq
  rw [hnum]
  field_simp

/-- `prop:koide`, second clause: the doubling norm `α = √2` gives the Koide value `2/3`. -/
theorem koide_two_thirds (M δ : ℝ) (hM : M ≠ 0) :
    koideRatio (sqrtMass M (√2) δ) = 2 / 3 := by
  rw [koide_ratio_eq M _ δ hM, Real.sq_sqrt (by norm_num)]
  norm_num

end ItFromBit
