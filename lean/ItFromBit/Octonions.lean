/-
Paper 1, appendix_ghz_w_proofs_2026-06-11.tex, §app:setup: the octonions with the multiplication
table `eq:fano-lines` and the composition identity `eq:composition`.

The paper fixes the table by seven ordered triples, `(i,j,k)` meaning `eᵢeⱼ = eₖ`, `eⱼeₖ = eᵢ`,
`eₖeᵢ = eⱼ`:
  (1,2,3), (1,4,5), (1,7,6), (2,4,6), (2,5,7), (3,4,7), (3,6,5),
with `e₀ = 1`, `eᵢ² = -1`, and antisymmetry off the diagonal. `mulTable` below is exactly that
table, generated mechanically from the seven triples (scripts in the session note of 2026-11-03).

What is formalised: the algebra `𝕆 = Fin 8 → ℝ` with this product, conjugation and norm; the
spot checks the paper calls out (`e₁e₇ = e₆`, `e₆e₇ = -e₁`, the action `eq:Jaction` of
`J = L_{e₁}`); and the composition identity `|ab|² = |a|²|b|²`, which is the "single structural
fact used throughout". The identity is a polynomial identity in sixteen real variables and is
closed by `ring` after the sums are expanded.
-/
import Mathlib

namespace ItFromBit

/-- The octonions as `ℝ⁸` with basis `e₀, …, e₇`. -/
abbrev Oct := Fin 8 → ℝ

namespace Oct

/-- `mulTable i j = (s, k)` means `eᵢ eⱼ = s • eₖ`. Row `i`, column `j`. -/
def mulTable : Fin 8 → Fin 8 → ℤ × Fin 8 :=
  ![
    ![(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
    ![(1, 1), (-1, 0), (1, 3), (-1, 2), (1, 5), (-1, 4), (-1, 7), (1, 6)],
    ![(1, 2), (-1, 3), (-1, 0), (1, 1), (1, 6), (1, 7), (-1, 4), (-1, 5)],
    ![(1, 3), (1, 2), (-1, 1), (-1, 0), (1, 7), (-1, 6), (1, 5), (-1, 4)],
    ![(1, 4), (-1, 5), (-1, 6), (-1, 7), (-1, 0), (1, 1), (1, 2), (1, 3)],
    ![(1, 5), (1, 4), (-1, 7), (1, 6), (-1, 1), (-1, 0), (-1, 3), (1, 2)],
    ![(1, 6), (1, 7), (1, 4), (-1, 5), (-1, 2), (1, 3), (-1, 0), (-1, 1)],
    ![(1, 7), (-1, 6), (1, 5), (1, 4), (-1, 3), (-1, 2), (1, 1), (-1, 0)]
  ]

/-- Basis vector `eᵢ`. -/
def e (i : Fin 8) : Oct := Pi.single i 1

/-- Octonion product: bilinear extension of the table. -/
def mul (a b : Oct) : Oct := fun k =>
  ∑ i, ∑ j, a i * b j * (if (mulTable i j).2 = k then ((mulTable i j).1 : ℝ) else 0)

instance : Mul Oct := ⟨mul⟩

/-- Conjugation `ō = x₀ - Σ xᵢ eᵢ`. -/
def conj (a : Oct) : Oct := fun k => if k = 0 then a 0 else -a k

/-- Squared norm `|o|² = Σ xₖ²`. -/
def normSq (a : Oct) : ℝ := ∑ k, a k ^ 2

/-- Left multiplication by `e₁`, the complex structure `J` of the appendix. -/
def J (a : Oct) : Oct := mul (e 1) a

/-- Expand an octonion into its eight coordinates. -/
lemma mul_apply (a b : Oct) (k : Fin 8) :
    mul a b k = ∑ i, ∑ j, a i * b j * (if (mulTable i j).2 = k then ((mulTable i j).1 : ℝ) else 0) :=
  rfl

/-- The table as stated in the paper: `e₁ e₇ = e₆` (the reversed line `(1,7,6)`). -/
theorem e1_mul_e7 : mul (e 1) (e 7) = e 6 := by
  ext k; fin_cases k <;> simp [mul, e, Fin.sum_univ_eight, mulTable]

/-- ... hence `e₆ e₇ = -e₁`. -/
theorem e6_mul_e7 : mul (e 6) (e 7) = -e 1 := by
  ext k; fin_cases k <;> simp [mul, e, Fin.sum_univ_eight, mulTable]

/-- `eq:Jaction`: `J e₀ = e₁`, `J e₂ = e₃`, `J e₄ = e₅`, `J e₆ = -e₇`. -/
theorem J_action : J (e 0) = e 1 ∧ J (e 2) = e 3 ∧ J (e 4) = e 5 ∧ J (e 6) = -e 7 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> ext k <;> fin_cases k <;> simp [J, mul, e, Fin.sum_univ_eight, mulTable]

/-- `J² = -1`. -/
theorem J_J (a : Oct) : J (J a) = -a := by
  ext k; fin_cases k <;> simp [J, mul, e, Fin.sum_univ_eight, mulTable]

/-- `|ō|² = |o|²`. -/
theorem normSq_conj (a : Oct) : normSq (conj a) = normSq a := by
  simp [normSq, conj, Fin.sum_univ_eight]

/-- `eq:composition`: `|ab|² = |a|² |b|²`. -/
theorem normSq_mul (a b : Oct) : normSq (mul a b) = normSq a * normSq b := by
  simp only [normSq, mul, Fin.sum_univ_eight, mulTable]
  simp
  ring

end Oct

end ItFromBit
