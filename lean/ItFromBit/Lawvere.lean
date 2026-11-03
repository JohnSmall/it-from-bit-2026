/-
Paper 1, `prop:inside-outside` (Inside/outside fixed point), self_reference_section_2026-07-04.tex.

Statement in the paper: if the category of descriptions contains a self-representing object
(a weakly point-surjective `φ : A → Yᴬ`) and `σ` is the inside/outside involution, then
`Fix(σ)` is non-empty. The proof is Lawvere's diagonal construction applied to `σ`.

What is formalised: Lawvere's fixed-point theorem in its set-theoretic form (functions between
types, point-surjectivity as surjectivity onto `A → Y`), the proposition as its specialisation to
an involution, and the contrast the paper draws: on the two-element type, negation has no fixed
point, so no `A → (A → Bool)` is point-surjective (Cantor). The categorical setting (dagger
compact closure, weak point-surjectivity in a cartesian closed category) is not formalised; what
is checked is that the diagonal argument the proof invokes does produce a fixed point.
-/
import Mathlib

namespace ItFromBit

/-- Lawvere's fixed-point theorem, set-theoretic form: if `φ : A → (A → Y)` is point-surjective
then every endomap of `Y` has a fixed point. -/
theorem lawvere_fixed_point {A Y : Type*} (φ : A → A → Y)
    (hφ : ∀ g : A → Y, ∃ a, φ a = g) (σ : Y → Y) : ∃ y, σ y = y := by
  obtain ⟨a, ha⟩ := hφ (fun a => σ (φ a a))
  exact ⟨φ a a, (congrFun ha a).symm⟩

/-- `prop:inside-outside`: an involution on a self-representing type has a fixed point. The
involution hypothesis is not needed for existence; it is carried to match the paper's statement. -/
theorem inside_outside_fixed_point {A Y : Type*} (φ : A → A → Y)
    (hφ : ∀ g : A → Y, ∃ a, φ a = g) (σ : Y → Y) (_hσ : Function.Involutive σ) :
    (Function.fixedPoints σ).Nonempty :=
  lawvere_fixed_point φ hφ σ

/-- The paper's contrast: Boolean negation has no fixed point, so the same construction applied
to negation refutes point-surjectivity. This is Cantor's theorem in Lawvere's form. -/
theorem no_point_surjection_to_bool {A : Type*} (φ : A → A → Bool) :
    ¬ ∀ g : A → Bool, ∃ a, φ a = g := by
  intro h
  obtain ⟨b, hb⟩ := lawvere_fixed_point φ h not
  exact Bool.not_ne_self b hb

end ItFromBit
