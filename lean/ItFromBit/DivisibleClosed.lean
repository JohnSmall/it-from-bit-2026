/-
Paper 1, `prop:divisible-closed` (Divisible and closed implies connected),
continuity_section_2026-07-04.tex.

The proof has two parts. (1) Lie theory, cited to Bröcker–tom Dieck: a closed subgroup of a
compact matrix group is a compact Lie group with finitely many components, so `G/G₀` is finite.
(2) Lagrange: the quotient of a divisible group is divisible, and a nontrivial finite group is
never divisible, so `G/G₀` is trivial and `G = G₀`.

What is formalised: part (2) in full, with the identity component replaced by an arbitrary normal
subgroup `N` of finite index. Part (1) is not in Mathlib (no structure theory of compact Lie
groups) and is left as the hypothesis `Finite (G ⧸ N)`.
-/
import Mathlib

namespace ItFromBit

/-- A group is divisible (multiplicatively) if every element has an `n`-th root for every
`n ≥ 1`. -/
def Divisible (G : Type*) [Group G] : Prop :=
  ∀ (g : G) (n : ℕ), 0 < n → ∃ r : G, r ^ n = g

/-- Lagrange's one line: a finite divisible group is trivial. With `|H| = m`, every `h` has an
`m`-th root `r`, and `r ^ m = 1`, so `h = 1`. -/
theorem Divisible.subsingleton_of_finite {H : Type*} [Group H] [Finite H]
    (hdiv : Divisible H) : Subsingleton H := by
  cases nonempty_fintype H
  refine ⟨fun a b => ?_⟩
  have key : ∀ h : H, h = 1 := by
    intro h
    obtain ⟨r, hr⟩ := hdiv h (Fintype.card H) Fintype.card_pos
    rw [← hr, pow_card_eq_one]
  rw [key a, key b]

/-- The image of a divisible group under a surjective homomorphism is divisible. -/
theorem Divisible.of_surjective {G H : Type*} [Group G] [Group H] (f : G →* H)
    (hf : Function.Surjective f) (hdiv : Divisible G) : Divisible H := by
  intro h n hn
  obtain ⟨g, rfl⟩ := hf h
  obtain ⟨r, hr⟩ := hdiv g n hn
  exact ⟨f r, by rw [← map_pow, hr]⟩

/-- `prop:divisible-closed`, the group-theoretic core: a divisible group has no proper normal
subgroup of finite index. Applied to `N = G₀`, this is "`G/G₀` is trivial, so `G` is connected". -/
theorem Divisible.normal_finiteIndex_eq_top {G : Type*} [Group G] (N : Subgroup G) [N.Normal]
    [Finite (G ⧸ N)] (hdiv : Divisible G) : N = ⊤ := by
  have hq : Divisible (G ⧸ N) :=
    hdiv.of_surjective (QuotientGroup.mk' N) (QuotientGroup.mk'_surjective N)
  have := hq.subsingleton_of_finite
  ext g
  simp only [Subgroup.mem_top, iff_true]
  rw [← QuotientGroup.eq_one_iff]
  exact Subsingleton.elim _ _

/-- The remark following the proposition: a nontrivial finite group is never divisible. -/
theorem not_divisible_of_finite_nontrivial {H : Type*} [Group H] [Finite H] [Nontrivial H] :
    ¬ Divisible H := fun h =>
  not_subsingleton H h.subsingleton_of_finite

end ItFromBit
