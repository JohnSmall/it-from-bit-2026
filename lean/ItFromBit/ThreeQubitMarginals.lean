/-
Paper 1, concrete three-qubit computations:
 * `prop:w-doublet` (W carries the SU(2) doublet), entanglement_classes_and_gauge_groups: each
   single-qubit marginal of the canonical W state has spectrum `(2/3, 1/3)`, whereas the GHZ
   marginal is `½·1`.
 * `app:cor:bell` (Bipartite shadow), appendix_ghz_w_proofs: tracing one qubit from `|W⟩` leaves
   `⅔ |Ψ⁺⟩⟨Ψ⁺| + ⅓ |00⟩⟨00|`.

What is formalised: the partial traces of `|W⟩` and `|GHZ⟩` as explicit matrix identities. To keep
the arithmetic rational the vectors are written unnormalised (entries 0 and 1) and the
normalisation `1/‖ψ‖²` (`1/3` for W, `1/2` for GHZ and Ψ⁺) is applied to the reduced matrix, which
is the same thing. The reduced state of the first qubit of W is `diag(2/3, 1/3)`; the third qubit
is checked too, the second follows by the same computation. The extension to the whole
local-unitary orbit uses only `ρ₁(U₁⊗U₂⊗U₃ ψ) = U₁ ρ₁(ψ) U₁†`, which is not formalised here.
-/
import Mathlib

open Complex ComplexConjugate Matrix

namespace ItFromBit

/-- `|100⟩ + |010⟩ + |001⟩`, the W state before normalisation (‖·‖² = 3). -/
def W (a b c : Fin 2) : ℂ :=
  if (a = 1 ∧ b = 0 ∧ c = 0) ∨ (a = 0 ∧ b = 1 ∧ c = 0) ∨ (a = 0 ∧ b = 0 ∧ c = 1) then 1 else 0

/-- `|000⟩ + |111⟩`, the GHZ state before normalisation (‖·‖² = 2). -/
def GHZ (a b c : Fin 2) : ℂ :=
  if (a = 0 ∧ b = 0 ∧ c = 0) ∨ (a = 1 ∧ b = 1 ∧ c = 1) then 1 else 0

/-- Reduced state of the first qubit: trace over the second and third. -/
def rho1 (ψ : Fin 2 → Fin 2 → Fin 2 → ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  fun a a' => ∑ b, ∑ c, ψ a b c * conj (ψ a' b c)

/-- Reduced state of the third qubit. -/
def rho3 (ψ : Fin 2 → Fin 2 → Fin 2 → ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  fun c c' => ∑ a, ∑ b, ψ a b c * conj (ψ a b c')

/-- Reduced state of the first two qubits, indexed by pairs: trace over the third. -/
def rho12 (ψ : Fin 2 → Fin 2 → Fin 2 → ℂ) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  fun p q => ∑ c, ψ p.1 p.2 c * conj (ψ q.1 q.2 c)

/-- `prop:w-doublet`, first qubit: the normalised W marginal is `diag(2/3, 1/3)`. -/
theorem rho1_W : (1 / 3 : ℂ) • rho1 W = !![(2 / 3 : ℂ), 0; 0, 1 / 3] := by
  ext a a'
  fin_cases a <;> fin_cases a' <;> simp [rho1, W, Fin.sum_univ_two] <;> norm_num

/-- ... and the same for the third qubit. -/
theorem rho3_W : (1 / 3 : ℂ) • rho3 W = !![(2 / 3 : ℂ), 0; 0, 1 / 3] := by
  ext c c'
  fin_cases c <;> fin_cases c' <;> simp [rho3, W, Fin.sum_univ_two] <;> norm_num

/-- The normalised GHZ marginal is maximally mixed: no direction is singled out. -/
theorem rho1_GHZ : (1 / 2 : ℂ) • rho1 GHZ = (1 / 2 : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  ext a a'
  fin_cases a <;> fin_cases a' <;> simp [rho1, GHZ, Fin.sum_univ_two]

/-- `|01⟩ + |10⟩`, the Bell state Ψ⁺ before normalisation (‖·‖² = 2). -/
def PsiPlus (p : Fin 2 × Fin 2) : ℂ :=
  if (p.1 = 0 ∧ p.2 = 1) ∨ (p.1 = 1 ∧ p.2 = 0) then 1 else 0

/-- `|00⟩`. -/
def Ket00 (p : Fin 2 × Fin 2) : ℂ := if p.1 = 0 ∧ p.2 = 0 then 1 else 0

/-- `app:cor:bell`: tracing the third qubit from the normalised `|W⟩` gives
`⅔ |Ψ⁺⟩⟨Ψ⁺| + ⅓ |00⟩⟨00|`, with `|Ψ⁺⟩⟨Ψ⁺|` the normalised projector `½ (PsiPlus ⊗ PsiPlus*)`. -/
theorem rho12_W :
    (1 / 3 : ℂ) • rho12 W
      = (2 / 3 : ℂ) • ((1 / 2 : ℂ) • Matrix.vecMulVec PsiPlus (fun q => conj (PsiPlus q)))
        + (1 / 3 : ℂ) • Matrix.vecMulVec Ket00 (fun q => conj (Ket00 q)) := by
  ext ⟨a, b⟩ ⟨a', b'⟩
  fin_cases a <;> fin_cases b <;> fin_cases a' <;> fin_cases b' <;>
    simp [rho12, W, PsiPlus, Ket00, Matrix.vecMulVec] <;> norm_num

end ItFromBit
