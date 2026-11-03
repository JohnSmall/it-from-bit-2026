/-
Paper 1, `prop:invariant-ring` (The density matrix is a complete invariant), part (i),
appendix_jaynes_fibration_2026-07-19.tex.

Statement in the paper, part (i): two unit vectors have the same outer product
`|ψ⟩⟨ψ| = |φ⟩⟨φ|` if and only if they differ by a phase.

What is formalised: part (i) for vectors in `n → ℂ` with `n` finite, the outer product written
entrywise as `φ i * conj (φ j)`, and "phase" as a unit-modulus complex scalar. Part (ii), the
invariant-theory statement that the entries `ψ_i ψ̄_j` generate the `U(1)`-invariant polynomials
and span the invariants of minimal degree, is not formalised.
-/
import Mathlib

open Complex ComplexConjugate

namespace ItFromBit

variable {n : Type*}

/-- The outer product `|ψ⟩⟨ψ|`, entrywise. -/
def outer (ψ : n → ℂ) : Matrix n n ℂ := fun i j => ψ i * conj (ψ j)

lemma outer_smul (c : ℂ) (ψ : n → ℂ) : outer (c • ψ) = (‖c‖ ^ 2 : ℝ) • outer ψ := by
  ext i j
  simp only [outer, Pi.smul_apply, smul_eq_mul, map_mul, Matrix.smul_apply, Complex.real_smul]
  have : c * conj c = ((‖c‖ ^ 2 : ℝ) : ℂ) := by
    rw [Complex.mul_conj, Complex.normSq_eq_norm_sq]
  calc c * ψ i * (conj c * conj (ψ j)) = (c * conj c) * (ψ i * conj (ψ j)) := by ring
    _ = _ := by rw [this]

/-- A unit vector has a non-zero component. -/
lemma exists_ne_zero_of_norm_one [Fintype n] (ψ : n → ℂ) (hψ : ∑ i, ‖ψ i‖ ^ 2 = 1) : ∃ j, ψ j ≠ 0 := by
  by_contra h
  simp only [ne_eq, not_exists, not_not] at h
  simp [h] at hψ

/-- `prop:invariant-ring` (i): equal outer products if and only if equal up to a phase. -/
theorem outer_eq_iff_phase [Fintype n] (ψ φ : n → ℂ) (hψ : ∑ i, ‖ψ i‖ ^ 2 = 1) (hφ : ∑ i, ‖φ i‖ ^ 2 = 1) :
    outer φ = outer ψ ↔ ∃ c : ℂ, ‖c‖ = 1 ∧ φ = c • ψ := by
  constructor
  · intro h
    obtain ⟨j, hj⟩ := exists_ne_zero_of_norm_one ψ hψ
    have hjj : φ j * conj (φ j) = ψ j * conj (ψ j) := congrFun (congrFun h j) j
    have hφj : φ j ≠ 0 := by
      intro h0
      rw [h0, zero_mul, Complex.mul_conj] at hjj
      have := Complex.normSq_eq_zero.mp (by exact_mod_cast hjj.symm)
      exact hj this
    refine ⟨conj (ψ j) / conj (φ j), ?_, ?_⟩
    · -- |ψ j| = |φ j| from the diagonal entry
      have hn : ‖φ j‖ = ‖ψ j‖ := by
        have h1 : (Complex.normSq (φ j) : ℂ) = Complex.normSq (ψ j) := by
          rw [← Complex.mul_conj, ← Complex.mul_conj]; exact hjj
        have h2 : Complex.normSq (φ j) = Complex.normSq (ψ j) := by exact_mod_cast h1
        rw [Complex.normSq_eq_norm_sq, Complex.normSq_eq_norm_sq] at h2
        nlinarith [norm_nonneg (φ j), norm_nonneg (ψ j), h2]
      rw [norm_div, Complex.norm_conj, Complex.norm_conj, hn, div_self]
      exact norm_ne_zero_iff.mpr hj
    · funext i
      have hij : φ i * conj (φ j) = ψ i * conj (ψ j) := congrFun (congrFun h i) j
      have hcφ : conj (φ j) ≠ 0 := by
        intro h0; exact hφj (by simpa using congrArg conj h0)
      simp only [Pi.smul_apply, smul_eq_mul]
      rw [div_mul_eq_mul_div, eq_div_iff hcφ, hij]
      ring
  · rintro ⟨c, hc, rfl⟩
    rw [outer_smul, hc]
    simp

end ItFromBit
