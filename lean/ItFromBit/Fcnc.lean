/-
Paper 1, `prop:fcnc` (No tree-level FCNC), interactions_circuits_section_2026-06-08.tex.

Statement in the paper: a neutral-current coupling is proportional to the identity in the
generation index, `D = c • 1`; in the mass basis it becomes `Vᴴ D V`, and `Vᴴ (c • 1) V = c • 1`,
so the off-diagonal (flavour-changing) entries vanish.

What is formalised: exactly that matrix identity, for any unitary `V` over `ℂ` indexed by any
finite type, and the vanishing of the off-diagonal entries. The physical premise (that a neutral
current is proportional to the identity in generation space) is the hypothesis `D = c • 1`.
-/
import Mathlib

open Matrix

namespace ItFromBit

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Conjugating a scalar matrix by a unitary returns the scalar matrix. -/
theorem conj_scalar_by_unitary (V : Matrix.unitaryGroup n ℂ) (c : ℂ) :
    star (V : Matrix n n ℂ) * (c • (1 : Matrix n n ℂ)) * (V : Matrix n n ℂ) = c • 1 := by
  rw [Matrix.mul_smul, Matrix.mul_one, Matrix.smul_mul, Matrix.UnitaryGroup.star_mul_self]

/-- `prop:fcnc`: the flavour-changing entries of a neutral current are zero in every basis
related to the weak basis by a unitary (CKM) rotation. -/
theorem no_tree_level_fcnc (V : Matrix.unitaryGroup n ℂ) (D : Matrix n n ℂ) (c : ℂ)
    (hD : D = c • 1) {i j : n} (hij : i ≠ j) :
    (star (V : Matrix n n ℂ) * D * (V : Matrix n n ℂ)) i j = 0 := by
  rw [hD, conj_scalar_by_unitary, Matrix.smul_apply, Matrix.one_apply_ne hij, smul_zero]

end ItFromBit
