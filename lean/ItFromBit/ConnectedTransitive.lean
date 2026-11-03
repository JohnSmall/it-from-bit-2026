/-
Paper 1, `prop:connected-transitive` (Continuity from a connected state space),
continuity_section_2026-07-04.tex; the same argument is
`prop:continuity-review-connected` in appendix_continuity_self_reference_2026-10-18T2119.tex.

The proof: closedness makes `G` a compact Lie group with finitely many components (Lie theory,
cited); `G₀` is normal of finite index; each `G₀`-orbit is compact hence closed; `G` transitive and
`G₀` normal make the cosets permute the orbits transitively, so there are finitely many; a finite
partition of a connected space into closed sets has one block; so `G₀` is transitive, and a path in
`G₀` from the identity supplies the continuous transformation.

What is formalised, with the Lie-theoretic inputs as hypotheses:
 * `const_of_finite_closed_fibres`: a map from a preconnected space to a finite type with closed
   fibres is constant (the "finite partition into closed sets" step).
 * `finite_orbits_of_transitive`: if `G` acts transitively and `N ⊴ G` has finite index, `N` has
   finitely many orbits (the coset-permutation step, with `N` in place of `G₀`).
 * `transitive_of_connected`: the proposition's conclusion that `N` is transitive, from
   `P` preconnected, `N`-orbits closed, `G` transitive, `[G : N] < ∞`.
Not formalised: that a closed subgroup of a compact matrix group has finitely many components,
that `G₀`-orbits are closed (compactness of `G₀`), and that `G₀` is path-connected. Those are the
hypotheses `Finite (G ⧸ N)`, `hclosed`, and the final path, respectively.
-/
import Mathlib

open MulAction Set

namespace ItFromBit

/-- A map from a preconnected space to a finite type, all of whose fibres are closed, is constant.
Each fibre is then also open, being the complement of a finite union of closed fibres. -/
theorem const_of_finite_closed_fibres {P ι : Type*} [TopologicalSpace P] [PreconnectedSpace P]
    [Finite ι] (f : P → ι) (hf : ∀ i, IsClosed (f ⁻¹' {i})) (x y : P) : f x = f y := by
  let _ : TopologicalSpace ι := ⊥
  have : DiscreteTopology ι := ⟨rfl⟩
  have hcont : Continuous f := by
    rw [continuous_iff_isClosed]
    intro s _
    have : f ⁻¹' s = ⋃ i ∈ s, f ⁻¹' {i} := by ext; simp
    rw [this]
    exact (Set.toFinite s).isClosed_biUnion (fun i _ => hf i)
  exact PreconnectedSpace.constant inferInstance hcont

/-- If a group `N` acts on a preconnected space with finitely many orbits, all closed, then there
is exactly one orbit. -/
theorem mem_orbit_of_finite_closed_orbits {N P : Type*} [Group N] [MulAction N P]
    [TopologicalSpace P] [PreconnectedSpace P] [Finite (orbitRel.Quotient N P)]
    (hclosed : ∀ x : P, IsClosed (orbit N x)) (x y : P) : y ∈ orbit N x := by
  let f : P → orbitRel.Quotient N P := fun p => Quotient.mk'' p
  have hf : ∀ q, IsClosed (f ⁻¹' {q}) := by
    intro q
    induction q using Quotient.inductionOn' with
    | h z =>
      have : f ⁻¹' {Quotient.mk'' z} = orbit N z := by
        ext p
        simp only [f, mem_preimage, mem_singleton_iff, Quotient.eq'']
        exact MulAction.orbitRel_apply
      rw [this]; exact hclosed z
  have h := const_of_finite_closed_fibres f hf y x
  exact MulAction.orbitRel_apply.mp (Quotient.eq''.mp h)

/-- If `G` acts transitively on `P` and `N ⊴ G` has finite index, then `N` has finitely many
orbits on `P`: the cosets of `N` permute them transitively. -/
theorem finite_orbits_of_transitive {G P : Type*} [Group G] [MulAction G P] (N : Subgroup G)
    [N.Normal] [Finite (G ⧸ N)] (htrans : ∀ x y : P, ∃ g : G, g • x = y) (x₀ : P) :
    Finite (orbitRel.Quotient N P) := by
  have wd : ∀ a b : G, QuotientGroup.leftRel N a b →
      (Quotient.mk'' (a • x₀) : orbitRel.Quotient N P) = Quotient.mk'' (b • x₀) := by
    intro a b hab
    rw [QuotientGroup.leftRel_apply] at hab
    apply Quotient.sound'
    rw [MulAction.orbitRel_apply]
    -- the element a * b⁻¹ = (b * (a⁻¹ * b) * b⁻¹)⁻¹ lies in N by normality
    have hn : a * b⁻¹ ∈ N := by
      have := (Subgroup.Normal.conj_mem ‹N.Normal› _ hab b)
      have h2 : (b * (a⁻¹ * b) * b⁻¹)⁻¹ = a * b⁻¹ := by group
      rw [← h2]; exact N.inv_mem this
    refine ⟨⟨a * b⁻¹, hn⟩, ?_⟩
    change (a * b⁻¹) • b • x₀ = a • x₀
    rw [← mul_smul, inv_mul_cancel_right]
  let f : G ⧸ N → orbitRel.Quotient N P := Quotient.lift (fun g => Quotient.mk'' (g • x₀)) wd
  refine Finite.of_surjective f ?_
  intro q
  induction q using Quotient.inductionOn' with
  | h y =>
    obtain ⟨g, hg⟩ := htrans x₀ y
    exact ⟨QuotientGroup.mk g, by simp [f, hg]⟩

/-- `prop:connected-transitive`, the core: with `P` preconnected, `G` transitive, `N ⊴ G` of
finite index and every `N`-orbit closed, `N` itself is transitive. Applied to `N = G₀`. -/
theorem transitive_of_connected {G P : Type*} [Group G] [MulAction G P] (N : Subgroup G)
    [N.Normal] [Finite (G ⧸ N)] [TopologicalSpace P] [PreconnectedSpace P]
    (htrans : ∀ x y : P, ∃ g : G, g • x = y) (hclosed : ∀ x : P, IsClosed (orbit N x))
    (x y : P) : ∃ n : N, n • x = y := by
  have := finite_orbits_of_transitive N htrans x
  exact mem_orbit_of_finite_closed_orbits hclosed x y

end ItFromBit
