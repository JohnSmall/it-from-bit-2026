# Correction: Root-Length Labelling in the G₂ / GHZ / W Documents

## Status note — 2026-06-08

This note corrects a labelling error in `g2_roots_ghz_w_quark_lepton_2026-04-29_0550.md`
and its consolidation `g2_roots_ghz_w_quark_lepton_v2_2026-04-30T0604.md`. Both documents
assign the **short** roots of G₂ to the colour SU(3) adjoint (the gluons) and the **long**
roots to the coset 3 ⊕ 3̄. This is backwards. The correct assignment is

> **colour SU(3) adjoint (gluons) = long roots; coset 3 ⊕ 3̄ (quark triplet ℂ³) = short roots.**

Only the length labels are wrong. Every representation-theoretic and physical statement in
those documents — the 14 = 8 ⊕ 3 ⊕ 3̄ split, the coset = ℂ³ = GHZ sector, the non-closure ⇒
confinement argument, θ_QCD = 0, and the Casimir ratio 3 — survives the swap intact, and §5
reads *more* coherently afterwards (the quark sector then sits on the genuinely non-associative
directions, which is where the coupling deviation should come from). The proof in §2.2a below is
the referee-proof anchor; later mass and coupling calculations should cite it rather than the
original §2.

The replacement text for §2 and the one-sentence fix to §5.1 follow.

---

## 2. The G₂ Root System Under SU(3) *(corrected)*

### 2.1 Basic structure

G₂ = Aut(𝕆) has rank 2 and dimension 14. Its root system has 12 roots in two Weyl orbits:

- **6 short roots**, normalised to length 1;
- **6 long roots**, of length √3.

The ratio of long to short length is √3; the ratio of squared lengths is 3.

### 2.2 Decomposition under SU(3)

Singling out one imaginary octonion direction — the computability split ℂ ⊂ 𝕆, equivalently a
choice of point on S⁶ = G₂/SU(3) — breaks G₂ to SU(3). The adjoint decomposes as

**14 = 8 ⊕ 3 ⊕ 3̄**

where:

- **8** (SU(3) adjoint): the **6 long roots** together with the 2-dimensional Cartan subalgebra.
  These are the gluon directions — the transformations that *leave the chosen imaginary unit
  invariant* and rotate the remaining six imaginaries among themselves. They form the closed
  colour su(3).
- **3 ⊕ 3̄** (coset G₂/SU(3) ≅ S⁶): the **6 short roots**. These are the broken directions,
  the tangent space to S⁶ at the chosen point — the transformations that *move* the chosen
  imaginary unit. The colour-triplet sector ℂ³ ⊂ Im(𝕆), into which GHZ-class Hopf images land,
  lives here.

The intuition is geometric. Measurement fixes a point p ∈ S⁶; the generators that stabilise p
are the long roots (the surviving gauge symmetry, colour), and the generators tangent to S⁶ at p
are the short roots (the broken, recorded directions). The long/short dichotomy is exactly the
gauge/broken — equivalently stabiliser/tangent, or fibre/base — dichotomy induced by the choice.

### 2.2a Proof of the assignment

Take simple roots α (short) and β (long) with the standard G₂ angle of 150°, normalised so that

  ⟨α,α⟩ = 1,  ⟨β,β⟩ = 3,  ⟨α,β⟩ = |α||β|cos150° = √3·(−√3/2) = −3/2.

The six positive roots and their squared lengths ⟨γ,γ⟩ are:

| root γ      | ⟨γ,γ⟩ | length | class |
|-------------|-------|--------|-------|
| α           | 1     | 1      | short |
| α + β       | 1     | 1      | short |
| 2α + β      | 1     | 1      | short |
| β           | 3     | √3     | long  |
| 3α + β      | 3     | √3     | long  |
| 3α + 2β     | 3     | √3     | long  |

(For example ⟨2α+β, 2α+β⟩ = 4⟨α,α⟩ + 4⟨α,β⟩ + ⟨β,β⟩ = 4 − 6 + 3 = 1, short; and
⟨3α+2β, 3α+2β⟩ = 9⟨α,α⟩ + 12⟨α,β⟩ + 4⟨β,β⟩ = 9 − 18 + 12 = 3, long.)

So the short roots are ±α, ±(α+β), ±(2α+β) and the long roots are ±β, ±(3α+β), ±(3α+2β).

**(i) The short roots do not form a subsystem.** α and 2α+β are both short, and their sum
α + (2α+β) = 3α+β is a root — but a *long* one. A set of roots that is not closed under the
addition of roots within it cannot be the root system of a subalgebra. Hence there is no su(3)
spanned by the short roots.

**(ii) The long roots form an A₂.** β and 3α+β are long, and β + (3α+β) = 3α+2β is again long;
the six long roots {±β, ±(3α+β), ±(3α+2β)} are mutually at 60°/120° and of equal length, i.e.
an A₂ root system, with simple roots β and 3α+β and highest root 3α+2β. The long roots therefore
span su(3). This is the *unique* A₂ subsystem of G₂, so the colour SU(3) can only be the long-root
subalgebra. Its adjoint 8 = (6 long roots) ⊕ (2 Cartan).

**(iii) The coset is the short roots, and carries ℂ³.** The 7-dimensional fundamental
representation of G₂ has weight set {six short roots} ∪ {0} (Fulton–Harris; Baez, *The Octonions*,
§4.1). Identifying **7** ≅ Im(𝕆), the choice of imaginary unit fixes the zero-weight direction
(the lepton singlet **1**), and the orthogonal complement ℂ³ = span{e₂,…,e₇} carries the six
short roots, splitting as **3** ⊕ **3̄** under the long-root SU(3). Thus the quark triplet sits on
the short roots and the gluons on the long roots. ∎

### 2.3 Bracket structure *(corrected labels)*

The bracket relations are unchanged in content; only the length labels attached to them move.
Writing **8** for the long-root adjoint and **3 ⊕ 3̄** for the short-root coset:

- **[8, 8] ⊂ 8** — the long roots plus the Cartan close: the adjoint is the colour su(3) subalgebra.
- **[8, 3] ⊂ 3** and **[8, 3̄] ⊂ 3̄** — the adjoint (long roots) acts on the coset (short roots):
  gluons rotate the colour-triplet directions.
- **[3, 3̄] ⊂ 8** — a short root plus the negative of another short root lands in the adjoint;
  concretely two short roots can sum to a long root, e.g. α + (2α+β) = 3α+β.
- **[3, 3] ⊂ 3̄** — short ⊗ short can also be short, e.g. α + (α+β) = 2α+β (the ε-tensor part).

The crucial asymmetry, corrected: **the long roots close (they are su(3)); the short roots do
not.** A sum of two short roots can be long or short, but the short roots never form a closed
subsystem isolated from the rest of G₂. This non-closure of the short roots is the algebraic
statement of confinement: the colour-triplet (short-root, coset) directions cannot be assembled
into a self-contained subalgebra — you cannot isolate a single colour direction.

### 2.4 The Im(𝕆) decomposition

Under SU(3) ⊂ G₂ (the stabiliser of e₁), the full octonions decompose as

**𝕆 = ℝ ⊕ Im(𝕆) = 1 ⊕ (1 ⊕ 3 ⊕ 3̄) = 1 ⊕ 1 ⊕ 3 ⊕ 3̄.**

The two singlets are e₀ (the real direction, trivially SU(3)-invariant) and e₁ (the chosen
imaginary, the fixed zero-weight direction); together they span ℂ = {e₀, e₁}, the sector W states
project into. The 6-dimensional **3 ⊕ 3̄** is {e₂,…,e₇} = ℂ³, the **short-root** sector, where the
GHZ Hopf image lands. The same **3 ⊕ 3̄** appears twice — once as a vector subspace of 𝕆 (the
short-root weights of the **7**) and once as a coset in g₂ (the short-root generators) — and the
two are identified by G₂/SU(3) ≅ S⁶ ⊂ Im(𝕆). This subsection was already correct in v2; the only
addition is the explicit identification of the {e₂,…,e₇} sector with the short roots.

---

## 5.1 Connection to the Koide framework *(corrected sentence)*

Replace the two sentences beginning "Leptons couple to the Higgs VEV…" with:

> Leptons couple to the Higgs VEV through the ℂ sector of the computability split — the singlet
> (zero-weight) direction fixed by the choice of e₁, surrounded by the associative long-root core
> (the closed colour su(3)), where the Cayley–Dickson norm is exactly √2. Quarks couple through
> the ℂ³ sector — the short-root coset, the genuinely non-associative directions (the short roots
> fail to close into a subalgebra), where the non-associative octonionic product modifies the
> effective coupling.

The §5.2 Casimir account is unaffected: C₂(**7**)/C₂(**3**) = 4 / (4/3) = 3 = (√3)² is independent
of which orbit is called "long," so the factor of 3 entering the quark/lepton ratio and the
Georgi–Jarlskog pattern stands exactly as written. The fitted |Q|^{3/2} account (§5.4) and the
open problem of reconciling it with the Casimir account (§10.2) are likewise unchanged.

---

## What changes and what does not

**Changes (labels only):** every occurrence of "short roots = SU(3) adjoint / gluons" becomes
"long roots," and "long roots = coset / 3 ⊕ 3̄ / quark ℂ³" becomes "short roots," in §2.2, §2.3,
the §4 dictionary table (first column), and the §5.1 prose.

**Does not change:**
- The decomposition 14 = 8 ⊕ 3 ⊕ 3̄ and 7 = 1 ⊕ 3 ⊕ 3̄.
- The coset = ℂ³ = GHZ sector identification, and the GHZ confinement / W accessibility theorems (§8).
- The non-closure ⇒ confinement argument (it is the short roots that fail to close; the conclusion is the same).
- θ_QCD = 0 (§9): topological, independent of root-length labels.
- The Casimir ratio 3 = (√3)² and the entire §5 mass conjecture (which reads more coherently, the quark deviation now sitting on the non-associative short-root coset).

**Separate, still outstanding:** the §4 dictionary's second row, "short roots ↔ W ↔ leptons," is a
category error independent of this correction — flagged already in
`session_summary_g2_channels_furey_wedderburn_2026-04-30_0543.md`, §1.3 — because roots are
operators (gluons) and the lepton singlet is a *state* those operators act on trivially. That fix
(operators vs states) and this fix (long vs short) are independent; both are needed before the
dictionary is clean.

---

## For later calculations

The reference facts to carry forward:

- Measurement of an imaginary unit = choice of p ∈ S⁶ = G₂/SU(3); the short-root coset is T_pS⁶
  (the recorded / broken data), the long-root su(3) is the stabiliser (the surviving colour gauge).
- Quark triplet ℂ³ ↔ short roots ↔ non-associative coset; gluons ↔ long roots ↔ associative
  closed su(3).
- Squared length ratio = C₂(**7**)/C₂(**3**) = 3; this is the label-independent number feeding the
  quark/lepton mass-ratio conjecture.

*References for §2.2a: J. Baez, "The Octonions," Bull. Amer. Math. Soc. 39 (2002) 145, §4.1;
W. Fulton and J. Harris, Representation Theory, §22.3 (the 7 of G₂ and its short-root weights).*
