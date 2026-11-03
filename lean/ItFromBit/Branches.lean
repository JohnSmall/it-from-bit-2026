/-
Paper 1, appendix_ghz_w_proofs_2026-06-11.tex: the branch algebra used in §app:ghz-proof and
§app:w-proof. A three-qubit state is split on one qubit into two branches in `ℂ⁴`; a local unitary
`U₁ ⊗ U₂ ⊗ U₃` acts by the internal unitary `U₂ ⊗ U₃` on each branch followed by the first-qubit
mixing `o₁ = U₁₀₀ φ₀ + U₁₀₁ φ₁`, `o₂ = U₁₁₀ φ₀ + U₁₁₁ φ₁`.

What is formalised:
 * the inner product `ip v w = Σ conj(vₖ) wₖ` on branches and its invariance under a unitary
   matrix (`ip_mulVec`), and that the Kronecker product of unitaries is unitary;
 * the local-unitary action `act U₁ U₂ U₃` on `Fin 2 × (Fin 2 × Fin 2) → ℂ` and the three branch
   lemmas `br1_act`, `br2_act`, `br3_act`: the branches along qubit `s` of the transformed state are
   the `U_s`-mixing of the `(U_other ⊗ U_other')`-images of the branches of the original;
 * `eq:general-ip` in its `U(2)` form, and the vanishing theorem it yields: orthogonal, equal-norm
   branches stay orthogonal under every local unitary (the forward direction of `prop:ghz` for one
   split, before it is specialised to GHZ).
-/
import ItFromBit.HopfProjection

open Matrix ComplexConjugate
open scoped Kronecker

namespace ItFromBit

/-- Three-qubit index `(a, (b, c))`. -/
abbrev Q3 := Fin 2 × (Fin 2 × Fin 2)

/-- `ip v w = Σ conj(vₖ) wₖ = ⟨v, w⟩`. -/
def ip {n : Type*} [Fintype n] (v w : n → ℂ) : ℂ := star v ⬝ᵥ w

lemma ip_eq_herm (v w : Q2 → ℂ) : ip v w = herm v w := by
  simp [ip, herm, dotProduct, Pi.star_apply]

lemma ip_add_left {n : Type*} [Fintype n] (u v w : n → ℂ) : ip (u + v) w = ip u w + ip v w := by
  simp [ip, star_add, add_dotProduct]

lemma ip_add_right {n : Type*} [Fintype n] (u v w : n → ℂ) : ip u (v + w) = ip u v + ip u w := by
  simp [ip, dotProduct_add]

lemma ip_smul_left {n : Type*} [Fintype n] (c : ℂ) (v w : n → ℂ) :
    ip (c • v) w = conj c * ip v w := by
  simp [ip, star_smul, smul_dotProduct, smul_eq_mul]

lemma ip_smul_right {n : Type*} [Fintype n] (c : ℂ) (v w : n → ℂ) :
    ip v (c • w) = c * ip v w := by
  simp [ip, dotProduct_smul, smul_eq_mul]

lemma ip_swap {n : Type*} [Fintype n] (v w : n → ℂ) : ip w v = conj (ip v w) := by
  simp [ip, dotProduct, Pi.star_apply, map_sum, mul_comm]

/-- A unitary matrix preserves `ip`. -/
theorem ip_mulVec {n : Type*} [Fintype n] [DecidableEq n] (M : Matrix n n ℂ)
    (hM : star M * M = 1) (v w : n → ℂ) : ip (M *ᵥ v) (M *ᵥ w) = ip v w := by
  simp only [ip]
  rw [star_mulVec, dotProduct_mulVec, vecMul_vecMul, ← star_eq_conjTranspose, hM, vecMul_one]

/-- The Kronecker product of unitaries is unitary. -/
theorem kron_star_mul_self {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]
    (A : Matrix m m ℂ) (B : Matrix n n ℂ) (hA : star A * A = 1) (hB : star B * B = 1) :
    star (A ⊗ₖ B) * (A ⊗ₖ B) = 1 := by
  rw [star_eq_conjTranspose, conjTranspose_kronecker, ← mul_kronecker_mul,
    ← star_eq_conjTranspose, ← star_eq_conjTranspose, hA, hB, one_kronecker_one]

/-- The local-unitary action `U₁ ⊗ U₂ ⊗ U₃` on three-qubit amplitudes. -/
def act (U₁ U₂ U₃ : Matrix (Fin 2) (Fin 2) ℂ) (ψ : Q3 → ℂ) : Q3 → ℂ :=
  (U₁ ⊗ₖ (U₂ ⊗ₖ U₃)) *ᵥ ψ

/-- Branches along the first qubit. -/
def br1 (ψ : Q3 → ℂ) (a : Fin 2) : Q2 → ℂ := fun p => ψ (a, p)
/-- Branches along the second qubit (remaining amplitudes indexed by (qubit 1, qubit 3)). -/
def br2 (ψ : Q3 → ℂ) (b : Fin 2) : Q2 → ℂ := fun p => ψ (p.1, (b, p.2))
/-- Branches along the third qubit (remaining amplitudes indexed by (qubit 1, qubit 2)). -/
def br3 (ψ : Q3 → ℂ) (c : Fin 2) : Q2 → ℂ := fun p => ψ (p.1, (p.2, c))

/-- The `U(2)` mixing of two branches: `mix U φ a = Σ U a a' • φ a'`. -/
def mix (U : Matrix (Fin 2) (Fin 2) ℂ) (φ : Fin 2 → Q2 → ℂ) (a : Fin 2) : Q2 → ℂ :=
  U a 0 • φ 0 + U a 1 • φ 1

theorem br1_act (U₁ U₂ U₃ : Matrix (Fin 2) (Fin 2) ℂ) (ψ : Q3 → ℂ) (a : Fin 2) :
    br1 (act U₁ U₂ U₃ ψ) a = mix U₁ (fun a' => (U₂ ⊗ₖ U₃) *ᵥ br1 ψ a') a := by
  ext ⟨b, c⟩
  simp only [br1, act, mix, mulVec, dotProduct, kroneckerMap_apply, Fintype.sum_prod_type,
    Fin.sum_univ_two, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  ring

theorem br2_act (U₁ U₂ U₃ : Matrix (Fin 2) (Fin 2) ℂ) (ψ : Q3 → ℂ) (b : Fin 2) :
    br2 (act U₁ U₂ U₃ ψ) b = mix U₂ (fun b' => (U₁ ⊗ₖ U₃) *ᵥ br2 ψ b') b := by
  ext ⟨a, c⟩
  simp only [br2, act, mix, mulVec, dotProduct, kroneckerMap_apply, Fintype.sum_prod_type,
    Fin.sum_univ_two, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  ring

theorem br3_act (U₁ U₂ U₃ : Matrix (Fin 2) (Fin 2) ℂ) (ψ : Q3 → ℂ) (c : Fin 2) :
    br3 (act U₁ U₂ U₃ ψ) c = mix U₃ (fun c' => (U₁ ⊗ₖ U₂) *ᵥ br3 ψ c') c := by
  ext ⟨a, b⟩
  simp only [br3, act, mix, mulVec, dotProduct, kroneckerMap_apply, Fintype.sum_prod_type,
    Fin.sum_univ_two, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  ring

/-- `eq:general-ip` for a general `U ∈ U(2)`: the inner product of the mixed branches. -/
theorem ip_mix (U : Matrix (Fin 2) (Fin 2) ℂ) (φ : Fin 2 → Q2 → ℂ) :
    ip (mix U φ 0) (mix U φ 1)
      = conj (U 0 0) * U 1 0 * ip (φ 0) (φ 0) + conj (U 0 1) * U 1 1 * ip (φ 1) (φ 1)
        + conj (U 0 0) * U 1 1 * ip (φ 0) (φ 1) + conj (U 0 1) * U 1 0 * ip (φ 1) (φ 0) := by
  simp only [mix, ip_add_left, ip_add_right, ip_smul_left, ip_smul_right]
  ring

/-- Orthogonal branches of equal norm stay orthogonal under any `U(2)` mixing: the mixing
coefficient is the `(0,1)` entry of `U Uᴴ = 1`. -/
theorem ip_mix_eq_zero (U : Matrix (Fin 2) (Fin 2) ℂ) (hU : U * star U = 1)
    (φ : Fin 2 → Q2 → ℂ) (horth : ip (φ 0) (φ 1) = 0) (hnorm : ip (φ 0) (φ 0) = ip (φ 1) (φ 1)) :
    ip (mix U φ 0) (mix U φ 1) = 0 := by
  have h10 : ip (φ 1) (φ 0) = 0 := by rw [ip_swap, horth, map_zero]
  rw [ip_mix, horth, h10, ← hnorm]
  have h01 : (U * star U) 1 0 = 0 := by rw [hU]; simp
  have : conj (U 0 0) * U 1 0 + conj (U 0 1) * U 1 1 = 0 := by
    simpa [Matrix.mul_apply, Fin.sum_univ_two, star_eq_conjTranspose, conjTranspose_apply,
      mul_comm] using h01
  linear_combination ip (φ 0) (φ 0) * this

/-- The forward direction of `prop:ghz` along one split, in general form: if the two branches
are orthogonal with equal norms, then after any internal unitary `V` (with `Vᴴ V = 1`) and any
first-qubit `U` (with `U Uᴴ = 1`) the branches are still orthogonal, hence by `lem:cproj` the
`ℂ`-projection of the Hopf image vanishes. -/
theorem piC_vanishes_of_maximally_mixed (U : Matrix (Fin 2) (Fin 2) ℂ) (hU : U * star U = 1)
    (V : Matrix Q2 Q2 ℂ) (hV : star V * V = 1) (φ : Fin 2 → Q2 → ℂ)
    (horth : ip (φ 0) (φ 1) = 0) (hnorm : ip (φ 0) (φ 0) = ip (φ 1) (φ 1)) :
    piC (hopfH (embed (mix U (fun a => V *ᵥ φ a) 0)) (embed (mix U (fun a => V *ᵥ φ a) 1))) = 0 := by
  rw [cproj_eq_zero_iff, ← ip_eq_herm]
  apply ip_mix_eq_zero U hU
  · simp only [ip_mulVec V hV, horth]
  · simp only [ip_mulVec V hV, hnorm]

end ItFromBit
