# Lean proofs: directory created, triage of Paper 1's stated results

Session note, 2026-11-03, Fable 5.1 with JS (maintainer). JS: "check some of the theorems we've
stated by writing lean proofs. Create a directory to hold Lean proofs and evaluate which theorems
are easily verified in Lean."

## What was set up

- `elan` installed user-locally (`~/.elan`, no sudo); Lean 4.35.0; Mathlib pinned at tag
  `v4.35.0` (the latest stable tag on 2026-11-03; master was on a 4.36 release candidate).
- New directory `lean/` with `lakefile.toml`, `lean-toolchain`, root module `ItFromBit.lean`,
  nine proof files under `ItFromBit/`, `Audit.lean` (axiom printout) and `README.md` carrying the
  triage table. `lean/.lake/` (Mathlib checkout and build, about 7 GB) is gitignored; one line
  added to `.gitignore`.
- Full build: `lake build` → `Build completed successfully (9057 jobs)`, no errors, no `sorry`
  (`grep -c sorry ItFromBit/*.lean` is 0 in every file).

Axiom audit (`lake env lean Audit.lean`), exact output:

```
'ItFromBit.no_tree_level_fcnc' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.hypercharge_values' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.koide_ratio_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.koide_two_thirds' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.inside_outside_fixed_point' does not depend on any axioms
'ItFromBit.no_point_surjection_to_bool' does not depend on any axioms
'ItFromBit.Divisible.normal_finiteIndex_eq_top' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.no_continuous_motion_among_privileged' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.transitive_of_connected' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.outer_eq_iff_phase' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.rho1_W' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.rho12_W' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## What was checked, and what each check does and does not say

Paper 1 has 41 theorem-like environments (theorem, proposition, lemma, corollary). Nine files
cover twelve of them, in full or in their mathematical core. The split, statement by statement, is
in `lean/README.md`; the points worth recording here are the ones that bear on status labels.

1. **Formalised in full** (the statement as printed is a theorem of Mathlib-plus-these-files):
   `prop:fcnc`, `prop:hypercharge`, `prop:koide`, `prop:basis-discreteness`. Note what "in full"
   means for the first two: `prop:fcnc` is `Vᴴ(c·1)V = c·1`, and `prop:hypercharge` is
   `y + 3y' = 0, y = -1 ⇒ y' = 1/3`. The machine confirms they are correct and also that they are
   one-line facts; neither carries weight beyond its premise. `prop:koide` is a genuine
   trigonometric identity (`Σ cos = 0`, `Σ cos² = 3/2` on a third-turn) and the proof in the paper
   is exactly what Lean needed.

2. **Mathematical core formalised, cited theory as hypothesis:** `prop:divisible-closed`,
   `prop:connected-transitive` (and the two appendix restatements). The Lie-theoretic step
   (closed subgroup of a compact matrix group has finitely many components) is not in Mathlib and
   enters as `Finite (G ⧸ N)`; closedness of `G₀`-orbits enters as a hypothesis. Everything the
   paper's proofs do *after* citing Bröcker--tom Dieck is now machine-checked, including the
   coset-permutation count of orbits, which the paper states in one sentence.

3. **Formalised with the setting simplified:** `prop:inside-outside` is Lawvere's theorem in
   Set rather than in a dagger-compact category. Lean confirms the diagonal construction yields a
   fixed point of any endomap; the involution hypothesis is not used for existence (recorded in
   the file as an unused argument). Worth noting for the paper: the proposition's content is
   exactly Lawvere's theorem, and the "involution" and "richness" clauses add nothing to the
   fixed-point claim. `prop:invariant-ring` (i) is done for `ℂⁿ`; (ii) is invariant theory and was
   not attempted.

4. **Canonical instance only:** `prop:w-doublet` and `app:cor:bell` are checked for the canonical
   `|W⟩` and `|GHZ⟩`; the local-unitary covariance `ρ₁(Uψ) = U₁ρ₁U₁†` that extends them to the
   orbit is standard and was not formalised.

## Triage of the remaining 29

Feasible next, in rough order of value per effort: the complex specialisation of
`prop:koide-jordan` (3×3 Hermitian characteristic cubic plus `cos 3θ`); a concrete
Cayley--Dickson construction of `𝕆` and `𝕊` over `Fin 8`/`Fin 16`, which would unlock
`prop:zd-defect` (polynomial identity), `prop:zd-census` (decidable), and the Hopf-map lemmas
`lem:cproj`, `app:lem:base`, `app:lem:ceiling`; and the finite matrix checks `prop:trace-blind`,
`prop:neutral-blind`. Not feasible in current Mathlib: Lamperti, the every-basis lemma, Hopf-bundle
nontriviality, Hurwitz/Adams termination, `prop:gsm`, the `G₂` zero-divisor propositions, and
Jordan's derangement theorem (`prop:continuity-review-fixed-points`). Full list with reasons in
`lean/README.md`.

## Proposals for JS

- No status-label changes proposed. Nothing checked was in doubt; the four full formalisations
  confirm statements already labelled or treated as elementary.
- Consider adding `lean/` to the layout list in `README.md` and a sentence in CLAUDE.md on when a
  Lean check is expected (suggested rule: any new proposition whose proof is finite algebra or
  elementary topology gets a file here before it is labelled ESTABLISHED).
- `prop:inside-outside`: the Lean file makes visible that the involution hypothesis is idle. If
  the paper wants `σ² = id` to do work, the proposition should say what (e.g. that the fixed point
  is also a fixed point of the outside-of-inside composite), or the clause should be presented as
  interpretation rather than hypothesis.

## Files

- `lean/` (new): `lakefile.toml`, `lean-toolchain`, `ItFromBit.lean`, `Audit.lean`, `README.md`,
  `ItFromBit/{Fcnc,Hypercharge,Koide,Lawvere,DivisibleClosed,BasisDiscreteness,
  ConnectedTransitive,InvariantRing,ThreeQubitMarginals}.lean`
- `.gitignore`: one entry, `lean/.lake/`
- This note. No `.tex`, `.bib` or ledger changes. Nothing committed.

## Same day, later: the GHZ/W appendix (`paper1/appendices/appendix_ghz_w_proofs_2026-06-11.tex`)

JS asked whether the appendix's proofs are checkable in Lean and, if so, to check them and add
them to `lean/`. They are, almost entirely. Five new files, all compiled with no `sorry`:

- `Octonions.lean`: `𝕆` as `Fin 8 → ℝ` with a multiplication table generated mechanically from
  the seven Fano triples of `eq:fano-lines` (Cayley--Dickson Convention A, the paper's own
  convention). Checked: `e₁e₇ = e₆`, `e₆e₇ = −e₁`, the `J = L_{e₁}` action of `eq:Jaction`
  including `J(e₆) = −e₇`, `J² = −1`, and the composition identity `eq:composition`
  `|ab|² = |a|²|b|²` as a polynomial identity in 16 real variables (`ring` closes it).
- `HopfProjection.lean`: the embedding `eq:embedding` with its `−y₃e₇` sign, the Hopf map
  `𝐡 = o₁ō₂`, `π_ℂ`. `lem:cproj` is proved in full: `π_ℂ(𝐡) = conj⟨o₁,o₂⟩`; `app:cor:cproj`
  follows (`π_ℂ(𝐡) = 0 ⇔ ⟨o₁,o₂⟩ = 0`), and `|𝐡|² = |o₁|²|o₂|²`.
- `Branches.lean`: the three cuts of a three-qubit state as pairs of two-qubit branches, the local
  unitary action `U₁ ⊗ U₂ ⊗ U₃` via Mathlib's Kronecker product, and `eq:general-ip`: the
  branches after the action are `U`-mixtures of the branches before, so if the original branches
  are orthogonal and of equal norm the mixed ones are orthogonal for every unitary `U`. This is
  the whole of the GHZ forward direction once the canonical branches are computed.
- `Ceiling.lean`: `app:lem:base` (`x₉ = r_z`, `2π_ℂ(𝐡) = r_x − i r_y`, `r² + |w|² = 1`) and
  `app:lem:ceiling` in full: the `ℂ`-fraction is `≤ r²` for every unitary on the cut, and the
  bound is attained. The proof differs from the appendix's in one respect: rather than quoting
  the Bloch-vector rotation picture, it shows `r²` is unitarily invariant through the trace and
  determinant of the `2×2` Gram matrix of the branches (`r² = (tr ρ)² − 4 det ρ`), and reaches
  `x₉ = 0` by a real rotation and the intermediate value theorem. Same content, no appeal to
  `SU(2) → SO(3)`.
- `GhzW.lean`: `|GHZ⟩`, `|W⟩`, the tilted states; `prop:ghz` forward for all three splits;
  `app:cor:s5` (`x₉ = 0`, `π_ℂ = 0`, `|w|² = 1` on the orbit); `app:thm:char` (i)⇔(ii) and
  (iii)⇒(i); `prop:w-access` with the exact formula `⟨o₁,o₂⟩ = conj(U₀₀)U₁₀/3` and the ceiling
  `1/9`, attained; `app:cor:instances` for GHZ, W and the tilted family.

Not formalised, with reasons:

- `app:thm:char` (ii)⇒(iii): the appendix cites the Acín et al. canonical form; no Mathlib
  support, and it is cited theory, not the paper's own argument.
- The "measure zero" wording in `prop:w-access`: the vanishing locus `U₀₀U₁₀ = 0` is formalised
  exactly; that a proper algebraic subset of `U(2)` has Haar measure zero is not.
- The "sweeps out `S⁵`" sentence in `app:cor:s5`: the appendix states it as an observation and
  so does the Lean file header.

Two things the formalisation turned up, neither a fault in the appendix:

1. The Lean statement of `prop:w-access` is for a general unitary `U` rather than the appendix's
   `SU(2)` form `[[a, b], [−b̄, ā]]`: `⟨o₁,o₂⟩ = conj(U₀₀)U₁₀/3`. With `U₀₀ = a`, `U₁₀ = −b̄`
   this is the appendix's `−āb̄/3` exactly. (My first draft carried the appendix's minus sign
   over to the general form, and `linear_combination` reported a residual of `(2/3)·hrel`; the
   slip was mine, not the appendix's. Recorded because the residual is a useful diagnostic.)
2. The ceiling lemma does not need the Bloch-sphere rotation picture; the Gram-matrix invariants
   suffice. That is a simplification the appendix could adopt, not a correction.

### Build time, and a false alarm

The first full build of `GhzW.lean` took 48 minutes, which looked like a pathological proof.
Profiling by halves showed every tactic in the file completes in under two seconds. Timing the
file alone with Lean's profiler gave the answer: importing Mathlib took 239 s of a 279 s run,
with 3.45 GB resident and 680k page faults; elaboration of the whole file took 0.6 s. The
machine has 16 GB and a virtual machine was holding 6.4 GB, so a parallel `lake build` had been
paging. The proofs are fine; the README now says to build with memory free. Nothing in the Lean
files was changed for speed. Three `norm_num` calls that the linter reported as unused were
removed.

### Final build and audit (exact output below)

(The first full `lake build` of the library failed at the final import with a name clash,
`ItFromBit.GHZ` being defined in both `ThreeQubitMarginals.lean` and `GhzW.lean`; every file had
compiled. The normalised state in `GhzW.lean` is now `ghz3`. Second build below.)

```
warning: ItFromBit/ThreeQubitMarginals.lean:45:68: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
warning: ItFromBit/ThreeQubitMarginals.lean:45:68: Unused tactic linter: `<;>` should be replaced with `;` or be removed.
warning: ItFromBit/ThreeQubitMarginals.lean:50:68: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
warning: ItFromBit/ThreeQubitMarginals.lean:50:68: Unused tactic linter: `<;>` should be replaced with `;` or be removed.
✔ [9060/9062] Built ItFromBit.GhzW (118s)
✔ [9061/9062] Built ItFromBit (115s)
Build completed successfully (9062 jobs).
BUILD_EXIT=0
SORRY_GREP_DONE
'ItFromBit.no_tree_level_fcnc' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.hypercharge_values' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.koide_ratio_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.koide_two_thirds' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.inside_outside_fixed_point' does not depend on any axioms
'ItFromBit.no_point_surjection_to_bool' does not depend on any axioms
'ItFromBit.Divisible.normal_finiteIndex_eq_top' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.no_continuous_motion_among_privileged' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.transitive_of_connected' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.outer_eq_iff_phase' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.rho1_W' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.rho12_W' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.Oct.normSq_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.cproj' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.cproj_eq_zero_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.piC_vanishes_of_maximally_mixed' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.rSq_add_wSq' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.ceiling' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.ghz_forward' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.char_i_iff_ii' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.char_iii_to_i' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.ghz_colour_equator' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.w_ceiling' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.w_ip_eq_zero_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'ItFromBit.tilted_rSq' depends on axioms: [propext, Classical.choice, Quot.sound]
AUDIT_EXIT=0
```

Timings: `GhzW.lean` 118 s and the library root 115 s, each almost entirely Mathlib import on a
machine with about 20 MB free; the two `ThreeQubitMarginals` warnings are style lints on a
`<;>` and were left alone rather than risk another rebuild.

## Files (appendix batch)

- `lean/ItFromBit/{Octonions,HopfProjection,Branches,Ceiling,GhzW}.lean` (new);
  `lean/ItFromBit.lean` (five imports added); `lean/Audit.lean` (thirteen `#print axioms` lines
  added); `lean/README.md` (seven table rows, feasible/not-feasible lists revised, memory note
  in the build section). The octonion multiplication table was generated by a short Python
  loop over the seven Fano triples and pasted in; it is checked in Lean by the four octonion
  theorems, not trusted.
- This note. No `.tex`, `.bib` or ledger changes. Nothing committed.
