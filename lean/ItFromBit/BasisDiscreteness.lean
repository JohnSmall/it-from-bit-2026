/-
Paper 1, `prop:basis-discreteness` (Continuity forbids a selected basis),
continuity_section_2026-07-04.tex.

Statement in the paper: a privileged finite set of pure states is carried to itself by every
respecting reversible map, which therefore permutes it; a continuous family of such maps induces a
continuous path in a finite discrete set, which is constant; so no continuous family connects two
distinct distinguished states.

What is formalised: both halves. (1) A bijection of the state space that maps a finite set into
itself restricts to a permutation of it. (2) A continuous family (parametrised by any preconnected
space, in particular a path on `[0,1]`) of points of a T₁ state space that stays inside a finite set
is constant. Nothing about quantum states is used: the argument is topological, as the paper's
proof says.
-/
import Mathlib

open Set

namespace ItFromBit

/-- A bijection carrying a finite set into itself permutes it. -/
theorem bijective_mapsTo_finite_surjOn {X : Type*} (S : Set X) (hS : S.Finite)
    (g : X → X) (hg : Function.Injective g) (hmaps : MapsTo g S S) : SurjOn g S S := by
  have := hS.to_subtype
  have hinj : Function.Injective (hmaps.restrict g S S) :=
    fun a b h => Subtype.ext (hg (congrArg Subtype.val h))
  have hsurj := Finite.surjective_of_injective hinj
  intro y hy
  obtain ⟨⟨x, hx⟩, hxy⟩ := hsurj ⟨y, hy⟩
  exact ⟨x, hx, congrArg Subtype.val hxy⟩

/-- A continuous family of points of a T₁ space, indexed by a preconnected space and confined to a
finite set, is constant. -/
theorem continuous_into_finite_set_const {T X : Type*} [TopologicalSpace T] [PreconnectedSpace T]
    [TopologicalSpace X] [T1Space X] (S : Set X) (hS : S.Finite) (f : T → X) (hf : Continuous f)
    (hfS : ∀ t, f t ∈ S) (t₁ t₂ : T) : f t₁ = f t₂ := by
  have := hS.to_subtype
  let g : T → S := fun t => ⟨f t, hfS t⟩
  have hg : Continuous g := hf.subtype_mk hfS
  exact congrArg Subtype.val (PreconnectedSpace.constant inferInstance hg (x := t₁) (y := t₂))

/-- `prop:basis-discreteness`: a continuous path of transformations respecting a privileged
finite set `S` of pure states cannot carry a distinguished state to a different one. The path is
`γ : [0,1] → (X → X)` with `t ↦ γ t x` continuous for the state `x ∈ S`. -/
theorem no_continuous_motion_among_privileged {X : Type*} [TopologicalSpace X] [T1Space X]
    (S : Set X) (hS : S.Finite) (γ : unitInterval → X → X)
    (hresp : ∀ t, MapsTo (γ t) S S) (x : X) (hx : x ∈ S)
    (hcont : Continuous fun t => γ t x) (t : unitInterval) :
    γ t x = γ 0 x :=
  continuous_into_finite_set_const S hS (fun t => γ t x) hcont (fun t => hresp t hx) t 0

end ItFromBit
