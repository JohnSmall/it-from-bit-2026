/-
Paper 1, appendix_ghz_w_proofs_2026-06-11.tex: `app:lem:base` (The base is Bloch ⊕ colour) and
`app:lem:ceiling` (Ceiling lemma).

For a split with branches `φ₀, φ₁ ∈ ℂ⁴`, write `n₀ = |φ₀|²`, `n₁ = |φ₁|²`, `ρ₀₁ = ⟨φ₁, φ₀⟩`. The
reduced state of the cut qubit is `ρ = [[n₀, ρ₀₁], [ρ̄₀₁, n₁]]`, with Bloch vector
`r_z = n₀ − n₁`, `ρ₀₁ = (r_x − i r_y)/2`.

What is formalised:
 * `app:lem:base`: `x₉ = r_z`, `2π_ℂ(𝐡) = r_x − i r_y`, `r² = x₉² + |2π_ℂ(𝐡)|²`, and
   `r² + |w|² = 1` for a normalised state;
 * Cauchy--Schwarz for the branch inner product, by Lagrange's identity (needed for `r ≤ 1`);
 * `app:lem:ceiling`: `C_frac = (r² − x₉²)/(1 − x₉²)`, the bound `C_frac ≤ r²` for every pair of
   branches, equality when `x₉ = 0`, and attainment: an explicit real rotation of the first qubit
   reaches `x₉ = 0` (intermediate value theorem), where `C_frac = r²`;
 * invariance of `r²` under every first-qubit unitary, via `ρ ↦ U ρ Uᴴ` and the invariance of
   trace and determinant.
The paper's one-line argument "a first-qubit unitary rotates the Bloch vector freely" is replaced by
the explicit rotation and the trace/determinant invariance; nothing about `SU(2) → SO(3)` is used.
-/
import ItFromBit.Branches

open Matrix ComplexConjugate Real
open scoped Kronecker

namespace ItFromBit

/-- Squared norm of a branch, as a real number. -/
noncomputable def nrm {n : Type*} [Fintype n] (v : n → ℂ) : ℝ := ∑ k, Complex.normSq (v k)

lemma ip_self {n : Type*} [Fintype n] (v : n → ℂ) : ip v v = (nrm v : ℂ) := by
  simp [ip, nrm, dotProduct, Complex.normSq_eq_conj_mul_self, Complex.ofReal_sum]

lemma nrm_nonneg {n : Type*} [Fintype n] (v : n → ℂ) : 0 ≤ nrm v :=
  Finset.sum_nonneg fun _ _ => Complex.normSq_nonneg _

/-- Cauchy--Schwarz on `Q2 → ℂ`, by Lagrange's identity:
`|v|²|w|² − |⟨v,w⟩|² = Σ_{p<q} |v_p w_q − v_q w_p|² ≥ 0`. -/
theorem normSq_ip_le (v w : Q2 → ℂ) : Complex.normSq (ip v w) ≤ nrm v * nrm w := by
  have key : nrm v * nrm w - Complex.normSq (ip v w)
      = Complex.normSq (v (0,0) * w (0,1) - v (0,1) * w (0,0))
      + Complex.normSq (v (0,0) * w (1,0) - v (1,0) * w (0,0))
      + Complex.normSq (v (0,0) * w (1,1) - v (1,1) * w (0,0))
      + Complex.normSq (v (0,1) * w (1,0) - v (1,0) * w (0,1))
      + Complex.normSq (v (0,1) * w (1,1) - v (1,1) * w (0,1))
      + Complex.normSq (v (1,0) * w (1,1) - v (1,1) * w (1,0)) := by
    simp only [nrm, ip, dotProduct, Fintype.sum_prod_type, Fin.sum_univ_two, Pi.star_apply,
      Complex.normSq_apply, Complex.add_re, Complex.add_im, Complex.mul_re, Complex.mul_im,
      Complex.sub_re, Complex.sub_im, Complex.star_def, Complex.conj_re, Complex.conj_im]
    ring
  have : 0 ≤ nrm v * nrm w - Complex.normSq (ip v w) := by
    rw [key]
    have := Complex.normSq_nonneg
    linarith [Complex.normSq_nonneg (v (0,0) * w (0,1) - v (0,1) * w (0,0)),
      Complex.normSq_nonneg (v (0,0) * w (1,0) - v (1,0) * w (0,0)),
      Complex.normSq_nonneg (v (0,0) * w (1,1) - v (1,1) * w (0,0)),
      Complex.normSq_nonneg (v (0,1) * w (1,0) - v (1,0) * w (0,1)),
      Complex.normSq_nonneg (v (0,1) * w (1,1) - v (1,1) * w (0,1)),
      Complex.normSq_nonneg (v (1,0) * w (1,1) - v (1,1) * w (1,0))]
  linarith

/-! ### The Bloch vector of the cut -/

/-- `x₉ = |o₁|² − |o₂|²`. -/
noncomputable def x9 (φ₀ φ₁ : Q2 → ℂ) : ℝ := nrm φ₀ - nrm φ₁
/-- `ρ₀₁ = ⟨φ₁, φ₀⟩ = Σ φ₀ conj φ₁`. -/
def rho01 (φ₀ φ₁ : Q2 → ℂ) : ℂ := ip φ₁ φ₀
/-- Bloch components of the cut: `ρ₀₁ = (r_x − i r_y)/2`, `r_z = n₀ − n₁`. -/
noncomputable def rx (φ₀ φ₁ : Q2 → ℂ) : ℝ := 2 * (rho01 φ₀ φ₁).re
noncomputable def ry (φ₀ φ₁ : Q2 → ℂ) : ℝ := -2 * (rho01 φ₀ φ₁).im
noncomputable def rz (φ₀ φ₁ : Q2 → ℂ) : ℝ := nrm φ₀ - nrm φ₁
/-- `r²`. -/
noncomputable def rSq (φ₀ φ₁ : Q2 → ℂ) : ℝ := rx φ₀ φ₁ ^ 2 + ry φ₀ φ₁ ^ 2 + rz φ₀ φ₁ ^ 2
/-- The Hopf image's octonionic part for the embedded branches. -/
noncomputable def hopf (φ₀ φ₁ : Q2 → ℂ) : Oct := hopfH (embed φ₀) (embed φ₁)
/-- `|w|²`: the colour component of `2𝐡`, i.e. `|2𝐡|² − |2π_ℂ(𝐡)|²`. -/
noncomputable def wSq (φ₀ φ₁ : Q2 → ℂ) : ℝ :=
  4 * Oct.normSq (hopf φ₀ φ₁) - 4 * Complex.normSq (piC (hopf φ₀ φ₁))
/-- The `ℂ`-fraction `C_frac = |π_ℂ(𝐡)|² / |𝐡|²`. -/
noncomputable def cfrac (φ₀ φ₁ : Q2 → ℂ) : ℝ :=
  Complex.normSq (piC (hopf φ₀ φ₁)) / Oct.normSq (hopf φ₀ φ₁)

theorem piC_hopf (φ₀ φ₁ : Q2 → ℂ) : piC (hopf φ₀ φ₁) = rho01 φ₀ φ₁ := by
  rw [hopf, cproj, ← ip_eq_herm, rho01, ip_swap φ₀ φ₁]

theorem normSq_hopf (φ₀ φ₁ : Q2 → ℂ) : Oct.normSq (hopf φ₀ φ₁) = nrm φ₀ * nrm φ₁ := by
  rw [hopf, normSq_hopfH, normSq_embed, normSq_embed]; rfl

/-- `app:lem:base`, first clause: `x₉ = r_z`. -/
theorem x9_eq_rz (φ₀ φ₁ : Q2 → ℂ) : x9 φ₀ φ₁ = rz φ₀ φ₁ := rfl

/-- `app:lem:base`, second clause: `2 π_ℂ(𝐡) = r_x − i r_y`. -/
theorem two_piC_eq (φ₀ φ₁ : Q2 → ℂ) : 2 * piC (hopf φ₀ φ₁) = ⟨rx φ₀ φ₁, -ry φ₀ φ₁⟩ := by
  rw [piC_hopf]; apply Complex.ext <;> simp [rx, ry]

/-- `app:lem:base`, `eq:base-split` first identity: `r² = x₉² + |2π_ℂ(𝐡)|²`. -/
theorem rSq_eq (φ₀ φ₁ : Q2 → ℂ) :
    rSq φ₀ φ₁ = x9 φ₀ φ₁ ^ 2 + Complex.normSq (2 * piC (hopf φ₀ φ₁)) := by
  rw [two_piC_eq]; simp [rSq, x9, rz, Complex.normSq_apply]; ring

/-- `rSq = (n₀ − n₁)² + 4|ρ₀₁|²`. -/
theorem rSq_eq' (φ₀ φ₁ : Q2 → ℂ) :
    rSq φ₀ φ₁ = (nrm φ₀ - nrm φ₁) ^ 2 + 4 * Complex.normSq (rho01 φ₀ φ₁) := by
  simp [rSq, rx, ry, rz, Complex.normSq_apply]; ring

/-- `app:lem:base`, `eq:base-split` second identity: for a normalised state `r² + |w|² = 1`. -/
theorem rSq_add_wSq (φ₀ φ₁ : Q2 → ℂ) (h : nrm φ₀ + nrm φ₁ = 1) :
    rSq φ₀ φ₁ + wSq φ₀ φ₁ = 1 := by
  rw [rSq_eq, wSq, normSq_hopf]
  have : Complex.normSq (2 * piC (hopf φ₀ φ₁)) = 4 * Complex.normSq (piC (hopf φ₀ φ₁)) := by
    rw [Complex.normSq_mul]; norm_num
  rw [this, x9]
  nlinarith [h]

/-! ### The ceiling -/

/-- `app:lem:ceiling`, the formula `C_frac = (r² − x₉²)/(1 − x₉²)` for a normalised state with
`x₉² ≠ 1`. -/
theorem cfrac_formula (φ₀ φ₁ : Q2 → ℂ) (h : nrm φ₀ + nrm φ₁ = 1) (hx : x9 φ₀ φ₁ ^ 2 ≠ 1) :
    cfrac φ₀ φ₁ = (rSq φ₀ φ₁ - x9 φ₀ φ₁ ^ 2) / (1 - x9 φ₀ φ₁ ^ 2) := by
  have h4 : 4 * (nrm φ₀ * nrm φ₁) = 1 - x9 φ₀ φ₁ ^ 2 := by
    simp only [x9]; nlinarith [h]
  have hne : nrm φ₀ * nrm φ₁ ≠ 0 := by
    intro h0; apply hx; linarith
  rw [cfrac, normSq_hopf, rSq_eq, piC_hopf, Complex.normSq_mul]
  rw [div_eq_div_iff hne (sub_ne_zero.mpr (Ne.symm hx))]
  rw [← h4]; norm_num; ring

/-- `app:lem:ceiling`, the bound: `C_frac ≤ r²` for every normalised pair of branches. -/
theorem cfrac_le_rSq (φ₀ φ₁ : Q2 → ℂ) (h : nrm φ₀ + nrm φ₁ = 1) : cfrac φ₀ φ₁ ≤ rSq φ₀ φ₁ := by
  rw [cfrac, normSq_hopf, piC_hopf, rSq_eq']
  have hCS : Complex.normSq (rho01 φ₀ φ₁) ≤ nrm φ₀ * nrm φ₁ := by
    rw [rho01, mul_comm]; exact normSq_ip_le φ₁ φ₀
  have hρ := Complex.normSq_nonneg (rho01 φ₀ φ₁)
  have h0 := nrm_nonneg φ₀
  have h1 := nrm_nonneg φ₁
  rcases eq_or_lt_of_le (mul_nonneg h0 h1) with hz | hpos
  · rw [← hz, div_zero]
    exact add_nonneg (sq_nonneg _) (by linarith)
  · rw [div_le_iff₀ hpos]
    have h4 : 4 * (nrm φ₀ * nrm φ₁) = 1 - (nrm φ₀ - nrm φ₁) ^ 2 := by nlinarith [h]
    have h5 : 4 * Complex.normSq (rho01 φ₀ φ₁) * (nrm φ₀ * nrm φ₁)
        = Complex.normSq (rho01 φ₀ φ₁) * (1 - (nrm φ₀ - nrm φ₁) ^ 2) := by
      rw [← h4]; ring
    nlinarith [mul_nonneg (sq_nonneg (nrm φ₀ - nrm φ₁)) (sub_nonneg.mpr hCS), h5]

/-- ... with equality when the Bloch vector lies in the equatorial plane `x₉ = 0`. -/
theorem cfrac_eq_rSq_of_x9_eq_zero (φ₀ φ₁ : Q2 → ℂ) (h : nrm φ₀ + nrm φ₁ = 1)
    (hx : x9 φ₀ φ₁ = 0) : cfrac φ₀ φ₁ = rSq φ₀ φ₁ := by
  have h0 : nrm φ₀ = 1 / 2 := by simp only [x9] at hx; linarith
  have h1 : nrm φ₁ = 1 / 2 := by simp only [x9] at hx; linarith
  rw [cfrac, normSq_hopf, piC_hopf, rSq_eq', h0, h1]; ring

/-! ### Attainment: an explicit first-qubit rotation reaches the equator -/

/-- The real rotation `[[cos t, sin t], [−sin t, cos t]]` as a complex matrix. -/
noncomputable def rotU (t : ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(cos t : ℂ), (sin t : ℂ); -(sin t : ℂ), (cos t : ℂ)]

theorem rotU_mul_star (t : ℝ) : rotU t * star (rotU t) = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rotU, Matrix.mul_apply, Fin.sum_univ_two, star_eq_conjTranspose, conjTranspose_apply] <;>
    simp only [← Complex.cos_conj, ← Complex.sin_conj, Complex.conj_ofReal] <;>
    first | linear_combination Complex.cos_sq_add_sin_sq (t : ℂ) | linear_combination

theorem rotU_mem (t : ℝ) : rotU t ∈ Matrix.unitaryGroup (Fin 2) ℂ :=
  Matrix.mem_unitaryGroup_iff.mpr (rotU_mul_star t)

/-- The self inner product of a mixed branch. -/
theorem ip_mix_self (U : Matrix (Fin 2) (Fin 2) ℂ) (φ : Fin 2 → Q2 → ℂ) (a : Fin 2) :
    ip (mix U φ a) (mix U φ a)
      = conj (U a 0) * U a 0 * ip (φ 0) (φ 0) + conj (U a 0) * U a 1 * ip (φ 0) (φ 1)
        + conj (U a 1) * U a 0 * ip (φ 1) (φ 0) + conj (U a 1) * U a 1 * ip (φ 1) (φ 1) := by
  simp only [mix, ip_add_left, ip_add_right, ip_smul_left, ip_smul_right]
  ring

lemma rotU_00 (t : ℝ) : rotU t 0 0 = (cos t : ℂ) := by simp [rotU]
lemma rotU_01 (t : ℝ) : rotU t 0 1 = (sin t : ℂ) := by simp [rotU]
lemma rotU_10 (t : ℝ) : rotU t 1 0 = -(sin t : ℂ) := by simp [rotU]
lemma rotU_11 (t : ℝ) : rotU t 1 1 = (cos t : ℂ) := by simp [rotU]

/-- `x₉` after the rotation, as a function of the angle. -/
theorem x9_mix_rotU (t : ℝ) (φ : Fin 2 → Q2 → ℂ) :
    x9 (mix (rotU t) φ 0) (mix (rotU t) φ 1)
      = (cos t ^ 2 - sin t ^ 2) * (nrm (φ 0) - nrm (φ 1)) + 4 * cos t * sin t * (ip (φ 0) (φ 1)).re := by
  have key : ∀ a, nrm (mix (rotU t) φ a) = (ip (mix (rotU t) φ a) (mix (rotU t) φ a)).re :=
    fun a => by rw [ip_self, Complex.ofReal_re]
  have h10 : ip (φ 1) (φ 0) = conj (ip (φ 0) (φ 1)) := ip_swap _ _
  simp only [x9, key, ip_mix_self, h10, rotU_00, rotU_01, rotU_10, rotU_11]
  simp only [ip_self, Complex.add_re, Complex.mul_re, Complex.mul_im, Complex.conj_re, Complex.conj_im,
    Complex.ofReal_re, Complex.ofReal_im, Complex.neg_re, Complex.neg_im, map_neg,
    Complex.conj_ofReal]
  ring

/-- There is a first-qubit rotation taking the cut's Bloch vector into the equatorial plane. -/
theorem exists_rotU_x9_eq_zero (φ : Fin 2 → Q2 → ℂ) :
    ∃ t : ℝ, x9 (mix (rotU t) φ 0) (mix (rotU t) φ 1) = 0 := by
  let f : ℝ → ℝ := fun t =>
    (cos t ^ 2 - sin t ^ 2) * (nrm (φ 0) - nrm (φ 1)) + 4 * cos t * sin t * (ip (φ 0) (φ 1)).re
  have hf : Continuous f := by fun_prop
  have h0 : f 0 = nrm (φ 0) - nrm (φ 1) := by simp [f]
  have hπ : f (π / 2) = -(nrm (φ 0) - nrm (φ 1)) := by simp [f]
  have hmem : (0 : ℝ) ∈ Set.uIcc (f 0) (f (π / 2)) := by
    rw [h0, hπ, Set.mem_uIcc]
    rcases le_total 0 (nrm (φ 0) - nrm (φ 1)) with h | h
    · right; constructor <;> linarith
    · left; constructor <;> linarith
  obtain ⟨t, -, ht⟩ := intermediate_value_uIcc hf.continuousOn hmem
  exact ⟨t, by rw [x9_mix_rotU]; exact ht⟩

/-! ### Invariance of `r` under the first-qubit unitary -/

/-- The reduced state of the cut, `ρ a b = ⟨φ_b, φ_a⟩ = Σ φ_a conj φ_b`. -/
def rho (φ : Fin 2 → Q2 → ℂ) : Matrix (Fin 2) (Fin 2) ℂ := fun a b => ip (φ b) (φ a)

/-- `ρ ↦ U ρ Uᴴ` under the mixing `o_a = Σ U_{aa'} φ_{a'}`. -/
theorem rho_mix (U : Matrix (Fin 2) (Fin 2) ℂ) (φ : Fin 2 → Q2 → ℂ) :
    rho (mix U φ) = U * rho φ * star U := by
  ext a b
  simp only [rho, mix, ip_add_left, ip_add_right, ip_smul_left, ip_smul_right, Matrix.mul_apply,
    Fin.sum_univ_two, star_eq_conjTranspose, conjTranspose_apply, Complex.star_def]
  ring

theorem trace_rho (φ : Fin 2 → Q2 → ℂ) : Matrix.trace (rho φ) = ((nrm (φ 0) + nrm (φ 1) : ℝ) : ℂ) := by
  simp [Matrix.trace, rho, Fin.sum_univ_two, ip_self]

theorem det_rho (φ : Fin 2 → Q2 → ℂ) :
    Matrix.det (rho φ) = ((nrm (φ 0) * nrm (φ 1) - Complex.normSq (rho01 (φ 0) (φ 1)) : ℝ) : ℂ) := by
  rw [Matrix.det_fin_two]
  simp only [rho, rho01, ip_self]
  rw [ip_swap (φ 0) (φ 1), Complex.normSq_conj, ← Complex.normSq_eq_conj_mul_self]
  push_cast; ring

/-- `r² = (tr ρ)² − 4 det ρ`, so it is a unitary invariant of the cut. -/
theorem rSq_invariant (U : Matrix (Fin 2) (Fin 2) ℂ) (hU : U ∈ Matrix.unitaryGroup (Fin 2) ℂ)
    (φ : Fin 2 → Q2 → ℂ) :
    rSq (mix U φ 0) (mix U φ 1) = rSq (φ 0) (φ 1) := by
  have hUU : U * star U = 1 := Matrix.mem_unitaryGroup_iff.mp hU
  have hUU' : star U * U = 1 := Matrix.mem_unitaryGroup_iff'.mp hU
  -- trace and determinant of ρ are invariant
  have htr : Matrix.trace (rho (mix U φ)) = Matrix.trace (rho φ) := by
    rw [rho_mix, Matrix.trace_mul_cycle, hUU', Matrix.one_mul]
  have hdet : Matrix.det (rho (mix U φ)) = Matrix.det (rho φ) := by
    rw [rho_mix, Matrix.det_mul, Matrix.det_mul, mul_right_comm, ← Matrix.det_mul, hUU,
      Matrix.det_one, one_mul]
  rw [trace_rho, trace_rho] at htr
  rw [det_rho, det_rho] at hdet
  have htr' := Complex.ofReal_injective htr
  have hdet' := Complex.ofReal_injective hdet
  have hT : (nrm (mix U φ 0) + nrm (mix U φ 1)) ^ 2 = (nrm (φ 0) + nrm (φ 1)) ^ 2 := by rw [htr']
  rw [rSq_eq', rSq_eq']
  linear_combination hT - 4 * hdet'

/-- `app:lem:ceiling` assembled: over all first-qubit unitaries the `ℂ`-fraction is bounded by
the cut's `r²`, and the bound is attained by an explicit rotation. -/
theorem ceiling (φ : Fin 2 → Q2 → ℂ) (h : nrm (φ 0) + nrm (φ 1) = 1) :
    (∀ U ∈ Matrix.unitaryGroup (Fin 2) ℂ, cfrac (mix U φ 0) (mix U φ 1) ≤ rSq (φ 0) (φ 1)) ∧
    (∃ t : ℝ, cfrac (mix (rotU t) φ 0) (mix (rotU t) φ 1) = rSq (φ 0) (φ 1)) := by
  have hnorm : ∀ U ∈ Matrix.unitaryGroup (Fin 2) ℂ, nrm (mix U φ 0) + nrm (mix U φ 1) = 1 := by
    intro U hU
    have hUU' : star U * U = 1 := Matrix.mem_unitaryGroup_iff'.mp hU
    have := trace_rho (mix U φ)
    rw [rho_mix, Matrix.trace_mul_cycle, hUU', Matrix.one_mul, trace_rho] at this
    have := Complex.ofReal_injective this
    linarith
  refine ⟨fun U hU => ?_, ?_⟩
  · rw [← rSq_invariant U hU φ]; exact cfrac_le_rSq _ _ (hnorm U hU)
  · obtain ⟨t, ht⟩ := exists_rotU_x9_eq_zero φ
    refine ⟨t, ?_⟩
    rw [← rSq_invariant (rotU t) (rotU_mem t) φ]
    exact cfrac_eq_rSq_of_x9_eq_zero _ _ (hnorm _ (rotU_mem t)) ht

end ItFromBit
