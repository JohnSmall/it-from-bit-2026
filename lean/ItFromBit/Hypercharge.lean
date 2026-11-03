/-
Paper 1, `prop:hypercharge` (Hypercharge spectrum), quantum_numbers_section_2026-06-08.tex.

Statement in the paper: tracelessness of the hypercharge generator over
`𝕆 = ℂ ⊕ ℂ³`, i.e. `1·y_ℂ + 3·y_ℂ³ = 0`, fixes the ratio `y_ℂ : y_ℂ³ = -3 : 1`; normalising by the
electron's charge, `y_ℂ = -1`, gives `y_ℂ³ = 1/3`.

What is formalised: the arithmetic. The physical content (Schur's lemma forcing the generator to be
diagonal on the split, and tracelessness itself) is the hypothesis `eq:trace`; the proposition is
then linear arithmetic in two unknowns, and `linarith` closes it. This is recorded for completeness
and to be honest that nothing deeper is being checked here.
-/
import Mathlib

namespace ItFromBit

/-- The trace condition `eq:trace` over `ℂ ⊕ ℂ³` fixes the ratio `-3 : 1`. -/
theorem hypercharge_ratio (yC yC3 : ℚ) (htrace : 1 * yC + 3 * yC3 = 0) :
    yC = -3 * yC3 := by
  linarith

/-- With the lepton hypercharge normalised to `-1`, the quark doublet hypercharge is `1/3`. -/
theorem hypercharge_values (yC yC3 : ℚ) (htrace : 1 * yC + 3 * yC3 = 0) (helectron : yC = -1) :
    yC3 = 1 / 3 := by
  linarith

/-- Electric charge `Q = T₃ + Y/2` on the four members of the doublets then comes out in thirds:
the up quark at `2/3`, the down quark at `-1/3`, the neutrino at `0`, the electron at `-1`. -/
theorem charges_in_thirds (yC yC3 : ℚ) (htrace : 1 * yC + 3 * yC3 = 0) (helectron : yC = -1) :
    (1/2 : ℚ) + yC3 / 2 = 2/3 ∧ (-1/2 : ℚ) + yC3 / 2 = -1/3 ∧
    (1/2 : ℚ) + yC / 2 = 0 ∧ (-1/2 : ℚ) + yC / 2 = -1 := by
  have h := hypercharge_values yC yC3 htrace helectron
  subst h; subst helectron; norm_num

end ItFromBit
