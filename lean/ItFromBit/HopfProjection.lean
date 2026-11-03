/-
Paper 1, `lem:cproj` (The ℂ-projection is a Hermitian inner product), stated in
entanglement_classes_and_gauge_groups_2026-06-08.tex and proved in
appendix_ghz_w_proofs_2026-06-11.tex §app:setup, with `app:cor:cproj`.

The embedding `eq:embedding` sends four complex amplitudes `c₀, …, c₃` to
`x₀e₀ + y₀e₁ + x₁e₂ + y₁e₃ + x₂e₄ + y₂e₅ + x₃e₆ − y₃e₇`, the sign on `e₇` forced by `J e₆ = −e₇`.
The Hopf map's octonionic part is `𝐡 = o₁ ō₂`, and `π_ℂ(𝐡) = h₀ + i h₁`.

What is formalised: that the embedding is ℂ-linear for `J = L_{e₁}` (`embed (i•c) = J (embed c)`);
the lemma itself, `π_ℂ(𝐡) = conj ⟨o₁, o₂⟩` with `⟨·,·⟩` conjugate-linear in the first slot; the
vanishing criterion; `|embed c|² = Σ|cₖ|²`; and the corollary `|𝐡|² = |o₁|²|o₂|²`. The four
amplitudes are indexed by `Fin 2 × Fin 2`, the second and third qubit, so the same file serves the
three-qubit branches directly. Everything is a polynomial identity closed by `ring` after expansion.
-/
import ItFromBit.Octonions

open ComplexConjugate

namespace ItFromBit

/-- Two-qubit amplitudes, indexed by (qubit 2, qubit 3). -/
abbrev Q2 := Fin 2 × Fin 2

/-- `eq:embedding`, with block `k = 2b + c` for amplitude index `(b, c)`. -/
def embed (c : Q2 → ℂ) : Oct :=
  ![(c (0,0)).re, (c (0,0)).im, (c (0,1)).re, (c (0,1)).im,
    (c (1,0)).re, (c (1,0)).im, (c (1,1)).re, -(c (1,1)).im]

/-- `𝐡 = o₁ ō₂`. -/
def hopfH (o₁ o₂ : Oct) : Oct := Oct.mul o₁ (Oct.conj o₂)

/-- `π_ℂ(𝐡) = h₀ + i h₁`. -/
def piC (h : Oct) : ℂ := ⟨h 0, h 1⟩

/-- `⟨c, d⟩ = Σ conj(cₖ) dₖ`, conjugate-linear in the first argument. -/
def herm (c d : Q2 → ℂ) : ℂ := ∑ k, conj (c k) * d k

lemma herm_expand (c d : Q2 → ℂ) :
    herm c d = conj (c (0,0)) * d (0,0) + conj (c (0,1)) * d (0,1)
      + conj (c (1,0)) * d (1,0) + conj (c (1,1)) * d (1,1) := by
  simp [herm, Fintype.sum_prod_type, Fin.sum_univ_two]; ring

/-- The embedding is ℂ-linear: multiplication by `i` on the amplitudes is `J` on `𝕆`. -/
theorem embed_I_smul (c : Q2 → ℂ) : embed (Complex.I • c) = Oct.J (embed c) := by
  ext k
  fin_cases k <;> simp [embed, Oct.J, Oct.mul, Oct.e, Fin.sum_univ_eight, Oct.mulTable]

/-- `|embed c|² = Σ |cₖ|²`. -/
theorem normSq_embed (c : Q2 → ℂ) : Oct.normSq (embed c) = ∑ k, Complex.normSq (c k) := by
  simp [Oct.normSq, embed, Fin.sum_univ_eight, Fintype.sum_prod_type, Fin.sum_univ_two,
    Complex.normSq_apply]
  ring

/-- `lem:cproj`: `π_ℂ(o₁ ō₂) = conj ⟨o₁, o₂⟩`. -/
theorem cproj (c d : Q2 → ℂ) : piC (hopfH (embed c) (embed d)) = conj (herm c d) := by
  rw [herm_expand]
  apply Complex.ext <;>
    simp [piC, hopfH, Oct.mul, Oct.conj, embed, Fin.sum_univ_eight, Oct.mulTable] <;> ring

/-- `lem:cproj`, second clause: the projection vanishes iff the branches are orthogonal. -/
theorem cproj_eq_zero_iff (c d : Q2 → ℂ) :
    piC (hopfH (embed c) (embed d)) = 0 ↔ herm c d = 0 := by
  rw [cproj]; exact map_eq_zero_iff _ (RingHom.injective _)

/-- `app:cor:cproj`: `|𝐡|² = |o₁|² |o₂|²`, from `eq:composition` and `|ō| = |o|`. -/
theorem normSq_hopfH (o₁ o₂ : Oct) :
    Oct.normSq (hopfH o₁ o₂) = Oct.normSq o₁ * Oct.normSq o₂ := by
  rw [hopfH, Oct.normSq_mul, Oct.normSq_conj]

end ItFromBit
