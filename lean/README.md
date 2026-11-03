# lean/ --- machine-checked versions of Paper 1's stated results

Lean 4 proofs, checked against Mathlib, of those theorem-like statements in `paper1/` whose
content is finite algebra, elementary topology or a diagonal argument. Each file's header says
which proposition it covers, what exactly is formalised, and what is left as a hypothesis. The
point is not to re-prove Mathlib; it is to pin down, statement by statement, which part of each
proposition is mathematics that a machine can check and which part is physics or cited theory.

## Building

Toolchain and Mathlib are pinned: `lean-toolchain` (Lean 4.35.0) and `lakefile.toml`
(Mathlib `v4.35.0`). Install `elan` once (user-local, no sudo), then

```
cd lean
lake exe cache get     # downloads Mathlib's prebuilt .olean files, ~7 GB, once
lake build             # builds ItFromBit; "Build completed successfully" and no "error:" lines
lake env lean Audit.lean   # prints the axioms each main theorem depends on
```

Memory matters more than CPU. Importing Mathlib maps about 3.5 GB; on a 16 GB machine with a
virtual machine or browser holding several GB, a single file can spend four minutes paging in the
import and under a second elaborating (measured 2026-11-03: `GhzW.lean` 239 s import, 0.6 s
elaboration). Run `lake build` with nothing else heavy open, and prefer `lake build -j1` if memory
is tight; a parallel build of several files under memory pressure took 48 minutes for one file.

`.lake/` is gitignored. A clean build means every theorem in `ItFromBit/*.lean` type-checks with
no `sorry`; the audit should show only `propext`, `Classical.choice`, `Quot.sound` (Lean's standard
axioms) or none.

## What is formalised (status 2026-11-03, appendix batch added the same day)

| Paper label | Source | File | What the Lean proof covers |
|---|---|---|---|
| `prop:fcnc` | interactions_circuits | `Fcnc.lean` | Whole statement: `Vᴴ(c·1)V = c·1` for unitary `V`; off-diagonal entries vanish. |
| `prop:hypercharge` | quantum_numbers | `Hypercharge.lean` | Whole statement, which is linear arithmetic once `eq:trace` is assumed; charges in thirds as a corollary. |
| `prop:koide` | masses | `Koide.lean` | Whole statement: Koide ratio `= (1 + α²/2)/3` for the `ℤ₃` form, `2/3` at `α = √2`. |
| `prop:inside-outside` | self_reference | `Lawvere.lean` | Lawvere's fixed-point theorem (set-theoretic form) and its application to an involution; the Bool contrast (Cantor). Categorical setting not formalised. |
| `prop:basis-discreteness` | continuity | `BasisDiscreteness.lean` | Whole statement: a bijection preserving a finite set permutes it; a continuous family confined to a finite subset of a T₁ space is constant. |
| `prop:divisible-closed` | continuity | `DivisibleClosed.lean` | The Lagrange core: a divisible group has no proper normal subgroup of finite index. Lie-theoretic input (`G/G₀` finite) is a hypothesis. Also covers `prop:continuity-review-divisible`. |
| `prop:connected-transitive`, `prop:continuity-review-connected` | continuity, continuity appendix | `ConnectedTransitive.lean` | Finite closed partition of a preconnected space is trivial; finite-index normal subgroup of a transitive group has finitely many orbits; hence `G₀` transitive. Closedness of `G₀`-orbits and finiteness of `G/G₀` are hypotheses. |
| `prop:invariant-ring` (i) | jaynes appendix | `InvariantRing.lean` | Equal outer products iff equal up to a unit-modulus scalar. Part (ii) (invariant theory) not attempted. |
| `prop:w-doublet`, `app:cor:bell`, `app:cor:instances` (i),(ii) in part | entanglement_classes, ghz_w appendix | `ThreeQubitMarginals.lean` | Canonical W marginals `diag(2/3, 1/3)` (qubits 1 and 3), GHZ marginal `½·1`, two-qubit W marginal `⅔|Ψ⁺⟩⟨Ψ⁺| + ⅓|00⟩⟨00|`. Local-unitary covariance of the partial trace not formalised. |
| `eq:fano-lines`, `eq:composition`, `eq:Jaction` | ghz_w appendix §app:setup | `Octonions.lean` | Concrete octonions on `Fin 8` from the seven Fano triples (table generated mechanically); `e₁e₇ = e₆`, `e₆e₇ = −e₁`; `J = L_{e₁}` acts as stated and `J² = −1`; the composition identity `|ab|² = |a|²|b|²` as a polynomial identity. |
| `lem:cproj`, `app:cor:cproj` | ghz_w appendix | `HopfProjection.lean` | Whole statement: with the embedding `eq:embedding`, `π_ℂ(o₁ ō₂) = conj⟨o₁,o₂⟩`; vanishes iff the two branches are orthogonal; `|𝐡|² = |o₁|²|o₂|²`. |
| `app:lem:base` | ghz_w appendix | `Ceiling.lean` | `x₉ = r_z`, `2π_ℂ(𝐡) = r_x − i r_y`, `r² + |w|² = 1` on a normalised cut. The `eq:general-ip` branch mixing and its orthogonality consequence are in `Branches.lean`. |
| `app:lem:ceiling` | ghz_w appendix | `Ceiling.lean` | Whole statement: the `ℂ`-fraction is `≤ r²` for every unitary on the cut (`r²` is unitarily invariant via trace and determinant of the 2×2 Gram matrix), with equality attained by a real rotation that zeroes `x₉` (intermediate value theorem). |
| `prop:ghz` (forward), `app:cor:s5` | ghz_w appendix §app:ghz-proof | `GhzW.lean` | Forward direction: `π_ℂ(𝐡) = 0` for every local unitary and all three splits of `|GHZ⟩`; on the orbit `x₉ = 0`, `π_ℂ = 0`, `|w|² = 1`. The "sweeps out `S⁵`" sentence is not formalised (the appendix also only observes it). |
| `app:thm:char` | ghz_w appendix | `GhzW.lean` | (i)⇔(ii) for a cut: `ℂ`-fraction vanishing for every unitary iff the marginal is maximally mixed; (iii)⇒(i). Not formalised: (ii)⇒(iii), which cites the Acín et al. canonical form. |
| `prop:w-access`, `app:cor:instances` | ghz_w appendix §app:w-proof | `GhzW.lean` | `⟨o₁,o₂⟩ = conj(U₀₀)U₁₀/3` on the W orbit, so the `ℂ`-sector is reached iff `U₀₀U₁₀ ≠ 0`; ceiling `1/9`, attained; `r = 0` for GHZ, `r² = 1/9` for W, `r = |α|² − |β|²` for the tilted states. The "measure zero" wording is not formalised; the locus `U₀₀U₁₀ = 0` is. |

## Triage of the rest

Feasible with moderate effort, not yet done:

- `prop:koide-jordan`, complex specialisation: characteristic cubic of the 3×3 Hermitian matrix
  with unit diagonal and off-diagonals of common modulus `ρ`, roots `1 + 2ρ cos((Φ+2πk)/3)` via
  `Real.cos_three_mul`. The octonionic statement needs `J₃(𝕆)`, which Mathlib lacks.
- `prop:zd-defect`, `prop:zd-census`: need the sedenions as a concrete 16-dimensional algebra
  (a multiplication table over `Fin 16`, extending `Octonions.lean` by one Cayley--Dickson
  step). The norm-defect identity is then a polynomial identity in 32 variables, and the census
  is a decidable finite check. Heavy but mechanical.
- `prop:neutral-blind`, `prop:trace-blind`, `prop:energy-locus`: finite matrix checks already
  verified numerically in the code release; formalisable as explicit linear algebra but long.
- `app:thm:char` (ii)⇒(iii): the Acín et al. canonical form for three qubits; substantial.
- `prop:f1-dictionary`: classification of dagger-special commutative Frobenius algebras on `ℂ²`;
  the orthonormal-basis theorem behind it is not in Mathlib.

Not feasible in current Mathlib (missing theory), or not mathematics:

- `prop:lamperti` (Banach--Lamperti), `lem:every-basis` (Riemannian geometry of `ℂPⁿ`),
  `prop:no-section` (nontriviality of the Hopf bundle, Chern classes), `prop:termination`
  (Hurwitz and Adams), `prop:gsm` (Spin(9) stabiliser computation), `prop:iterated-hopf`
  (nested fibrations), `prop:continuity-review-fixed-points` (Jordan's derangement theorem plus
  Lie theory), `prop:zd-locus`, `prop:zd-aut`, `prop:zd-colour` (`G₂` structure).
- `lem:winding-number`, `prop:fanout-correspondence`: framework-specific operators; not
  attempted. `prop:w-access` (measure-zero clause): measure theory on `U(2)`; the vanishing locus
  itself is formalised.

## Conventions

One file per paper statement or closely related group; the file header names the label and the
source `.tex`. Hypotheses that stand in for cited theory are named and listed in the header. No
`sorry` is committed. Nothing in this directory is cited by the paper; it is a check, not a source.
