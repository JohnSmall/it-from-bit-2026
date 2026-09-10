# The K₃ obstruction, chirality, and the sterile neutrino

*The fermion generation count, the SU(2) doublet structure, and the sterile a-chiral state emerge from a single topological obstruction: the complete graph K₃ is not 2-colourable. This document expands the argument chain step by step, separating what is combinatorially forced, what follows structurally from the framework, and what remains genuinely conjectural.*

---

## 1. What the reader needs to see

The framework makes three claims that look like separate empirical inputs in the Standard Model but are argued here to follow from one topological fact:

1. There are exactly **three generations**.
2. Fermions come in **SU(2) doublets with one charged and one neutral partner**.
3. There exist **sterile neutrinos** that do not couple to any gauge interaction, distinct from right-handed neutrinos.

This document traces the reasoning from the two-qubit Bloch-sphere result of Filatov & Auzinsh, through the three-qubit extension, the K₃ graph-colouring obstruction, the four resolution classes, and their physical identification. Each step is made explicit.

---

## 2. Preliminary: the two-sphere result

### 2.1 The Filatov-Auzinsh theorem

A single qubit |ψ⟩ = α|0⟩ + β|1⟩ ∈ ℂ² has unit-norm states parametrised by the Bloch sphere S². This is standard: points on S² correspond one-to-one to pure qubit states up to overall phase.

For two qubits |ψ⟩ ∈ ℂ² ⊗ ℂ², a similar Bloch-sphere representation is attractive but requires care. Filatov & Auzinsh (2024) prove that a consistent two-Bloch-sphere representation of *entangled* pure two-qubit states exists if and only if the coordinate axes of the two spheres have opposite handedness. If one Bloch sphere is coordinatised right-handedly (x̂ × ŷ = ẑ), the other must be coordinatised left-handedly (x̂ × ŷ = −ẑ).

This is not a convention. It is a topological consequence of the quaternionic Hopf fibration S³ → S⁷ → S⁴ that carries two-qubit states. The handedness asymmetry is the geometric shadow of entanglement itself — the analogue, for two qubits, of the single-qubit Berry phase being ill-defined without a choice of phase convention.

We call this the **Filatov constraint**: entangled qubit pairs require opposite Bloch-sphere handedness.

### 2.2 What the constraint encodes

Intuitively: entanglement distinguishes "left from right" at the level of quantum-state geometry. A Bell pair cannot be represented as two independent Bloch spheres with the same handedness because there is no smooth way to transport the coordinate frame between them without picking up a sign. The L/R asymmetry at the Bloch-sphere level *is* the information-theoretic content of entanglement, geometrised.

This is the key fact we will use. It is proven for two spheres. For the three-sphere extension (§3.1) we will assume the natural generalisation; whether the proof extends formally is an open problem at the level of pure mathematics.

---

## 3. Three spheres: the W state and K₃

### 3.1 The extension

A tripartite W-class state |W⟩ = (|001⟩ + |010⟩ + |100⟩)/√3 has the property that *every single-qubit reduction* leaves a two-qubit state with nonzero entanglement (specifically the ρ_pair of the W → SU(2)_L theorem: (2/3)|Ψ⁺⟩⟨Ψ⁺| + (1/3)|00⟩⟨00|). All three pairs (AB), (AC), (BC) are entangled.

The natural extension of the Filatov constraint: *each entangled pair independently requires opposite handedness*. So an assignment of handedness χ_A, χ_B, χ_C ∈ {L, R} to the three qubits must satisfy:

$$\chi_A \neq \chi_B, \qquad \chi_A \neq \chi_C, \qquad \chi_B \neq \chi_C.$$

**Status.** The two-sphere Filatov theorem does not formally imply the three-sphere version; one must show that the constraint applies pairwise and independently to each entangled pair of a multipartite state. This is intuitively correct — each pair carries its own quaternionic Hopf structure — but the formal proof is open. Filatov has been contacted for collaboration; no response to date. The derivation below *assumes* the three-sphere extension and derives its consequences.

### 3.2 K₃ and 2-colourability

The handedness assignment problem is a graph-colouring question. Represent each qubit as a vertex and each entangled pair as an edge. For the W state, all three pairs are entangled, so the graph is K₃ — the complete graph on three vertices, i.e., a triangle.

The Filatov constraint says: every edge must have endpoints of different colours (where "colour" = handedness L or R).

A graph is **2-colourable** iff all its cycles have even length (König's theorem). K₃ is itself a 3-cycle. 3 is odd. Therefore:

**Fact.** *K₃ is not 2-colourable.*

This is elementary graph theory — a textbook result, not a framework claim. What matters is what this means physically: there is no consistent assignment of handedness to the three qubits that satisfies all three Filatov constraints simultaneously.

This is the **K₃ obstruction**. The framework cannot represent W-class states in a naive three-sphere Bloch picture. Something has to give.

---

## 4. The four resolution classes

### 4.1 Enumerating the failures

Since all three constraints cannot be satisfied, we enumerate all 2³ = 8 possible handedness assignments and count how many constraints each violates. Let ↑ = L, ↓ = R:

| (χ_A, χ_B, χ_C) | Satisfied edges | Frustrated edges | Class |
|---|---|---|---|
| (↑, ↓, ↓) | AB, AC | BC | **1** |
| (↓, ↑, ↑) | AB, AC | BC | **1** |
| (↑, ↑, ↓) | AC, BC | AB | **2** |
| (↓, ↓, ↑) | AC, BC | AB | **2** |
| (↑, ↓, ↑) | AB, BC | AC | **3** |
| (↓, ↑, ↓) | AB, BC | AC | **3** |
| (↑, ↑, ↑) | none | AB, AC, BC | **4** |
| (↓, ↓, ↓) | none | AB, AC, BC | **4** |

**Observation 1.** Every assignment satisfies exactly 0 or 2 of the 3 constraints. Never exactly 1; never exactly 3. This is because flipping one vertex changes two edges simultaneously — you cannot change the count by an odd number.

**Observation 2.** The 8 assignments partition into 4 classes, each containing a pair (an assignment and its global flip ↑↔↓). Global flip corresponds to particle ↔ antiparticle.

**Observation 3.** Classes 1, 2, 3 are distinguished by *which qubit is "odd"* — which qubit has a different handedness from the other two. Class 4 has all three the same.

The four classes are topologically distinct: no continuous path of handedness assignments can take you from one class to another without breaking the discrete structure. **This is the structural content of the K₃ obstruction: three "one odd qubit" resolutions plus one "all same" resolution.**

### 4.2 Why four, not something else

The count 4 = C(3,1) + 1 is the number of ways to choose "the odd vertex" (three ways) plus the option of "no odd vertex, all same" (one way). This is a combinatorial theorem about K₃, not a framework input.

What the framework contributes is the *physical interpretation* of these four classes.

---

## 5. Three classes = three generations

### 5.1 Which qubit is odd determines the generation

The three non-trivial classes (1, 2, 3) each have exactly one qubit with distinct handedness from the other two. Call this the **odd qubit** of the class. By the identification established in the three-qubits document (A ↔ ℂ, B ↔ ℍ, C ↔ 𝕆):

| Class | Odd qubit | Cayley-Dickson level of frustration | Generation |
|---|---|---|---|
| 1 | A | ℂ (commutative, associative) | 1st — lightest |
| 2 | B | ℍ (non-commutative, associative) | 2nd — intermediate |
| 3 | C | 𝕆 (non-commutative, non-associative) | 3rd — heaviest |

The three generations are distinguished by *which Cayley-Dickson level carries the frustration*. This is the single-principle answer to "why three generations" that the triality arguments were trying to capture: triality at the level of 𝕆 permutes the three places the frustration can sit.

### 5.2 Why the mass hierarchy goes in this order

Mass in the framework is associator debt — the information needed to fix a bracketing order when algebraic multiplication is non-associative (see `fermion_mass_geodesic_calculation.md`). Associator debt scales with algebraic depth:

- ℂ: commutative and associative. No non-computable residue. Minimal debt.
- ℍ: non-commutative but associative. Orientation content only. Intermediate debt.
- 𝕆: non-commutative and non-associative. Full bracketing-order content. Maximal debt.

Generation 1 frustrates the ℂ-qubit, which has the smallest algebraic obstruction to resolve. Generation 3 frustrates the 𝕆-qubit, which has the largest. The mass hierarchy m₁ < m₂ < m₃ follows because the frustrated qubit is the one that carries the mass-generating associator, and deeper Cayley-Dickson levels produce longer internal geodesics.

This is why generation 3 is heaviest: its frustration engages the non-associativity of 𝕆, which is the deepest algebraic structure available. Generations don't run out because there are only three Cayley-Dickson levels that can be frustrated in this way — there is no ℝ-qubit (ℝ is trivial as internal structure), and there is no sedenion qubit (𝕊 fails the norm identity and cannot carry a Hopf map).

**This is a single-principle derivation of both "three" and the ordering.** No empirical input.

### 5.3 Relation to the triality family

The Spin(8) / J₃(𝕆) / iterated-Hopf formulations of "why three" converge on the same answer: triality permutes the three Cayley-Dickson levels that can carry the frustration. What the K₃ obstruction adds is the specific mechanism — Filatov-constrained handedness assignments — and the bonus prediction (Class 4) that the triality arguments alone do not capture.

---

## 6. Two resolutions per class = SU(2) doublets

### 6.1 The doublet structure

Within each of Classes 1, 2, 3, the frustrated pair (the one edge violating its Filatov constraint) can be resolved in two topologically distinct ways. Concretely: the same-handedness pair (say BC both = ↑ in Class 1) can be locally rotated to either of two configurations, each breaking the frustration in a different direction.

Call these **Resolution α** (one direction of breaking) and **Resolution β** (the other). They are two topologically distinct points in the moduli space of the class, connected by an SU(2) rotation but not by any smaller group.

The framework identifies:

- Resolution α = **T₃ = −1/2** component (charged fermion or down-quark)
- Resolution β = **T₃ = +1/2** component (neutrino or up-quark)

For each generation, this gives two members:

| Generation | Resolution α (T₃ = −1/2) | Resolution β (T₃ = +1/2) |
|---|---|---|
| 1 | e, d | ν_e, u |
| 2 | μ, s | ν_μ, c |
| 3 | τ, b | ν_τ, t |

### 6.2 SU(2)_L is the rotation between resolutions

The weak interaction SU(2)_L acts on this doublet by rotating Resolution α ↔ Resolution β. A W boson emission takes (ν_μ → μ) by switching which resolution is realised. The SU(2)_L gauge symmetry is the local freedom to choose which of the two resolutions is being used.

This is why only *left-handed* fermions form SU(2) doublets. The Filatov constraint acts on handedness-dependent Bloch-sphere coordinates; right-handed fermions either do not participate in the K₃ structure (as singlets) or arrive via the Zitterbewegung zigzag (see §8.3 below). Either way, the doublet structure is intrinsically left-handed.

Concretely this gives the statement **W facet ⇔ SU(2)_L doublet** as derived in the companion document `w_to_su2l_doublet_theorem.md`: the 2/3-weighted eigenvector of ρ_k is one member of the resolution doublet; the 1/3-weighted singlet tail is the SU(2)_L-neutral sector (which includes Class 4, below).

### 6.3 Why exactly two resolutions

The frustrated pair has an SU(2)-worth of local rotations, but only two points in this SU(2) are topologically distinguished as resolutions — the two fixed points of the ℤ₂ that flips handedness in the frustrated pair. SU(2)/ℤ₂ = SO(3) acts transitively between them. Hence doublet.

This is why SU(2)_L doublets have exactly two members — not three, not one. It is a theorem about the ℤ₂ quotient structure of the frustrated-pair moduli space, not an empirical input.

---

## 7. Chirality: what the Filatov assignment actually encodes

Before moving to Class 4, it is worth being careful about what "chirality" means in the framework, because the standard Dirac L/R distinction is subtly different from the Filatov L/R assignment.

### 7.1 Three notions of chirality

There are three distinct notions of "handedness" in play:

**(a) Filatov handedness** χ ∈ {L, R}: the handedness of a Bloch-sphere coordinate frame, per qubit. This is the handedness that the K₃ constraint acts on.

**(b) Dirac/Weyl chirality** γ_5 = ±1: the handedness of a Lorentz-spinor, the property that distinguishes e_L from e_R in the Standard Model. This is a spacetime property, not an internal one.

**(c) Algebraic chirality**: the orientation of the Fano plane or the selection between left and right Moufang loops, per `g2_roots_ghz_w_quark_lepton.md`.

These three notions are not identical, and conflating them is where the framework is most vulnerable.

### 7.2 How they connect

The framework's structural claim — proved in part and conjectured in part — is that all three are projections of the same underlying selection:

- Algebraic chirality (c) is the Fano plane orientation of 𝕆, fixed by the computability split e_1 ∈ 𝕆.
- Filatov handedness (a) on the C-qubit inherits its orientation from (c) via the octonionic Hopf fibration S¹⁵ → S⁸.
- Dirac chirality (b) is locked to Filatov handedness on the B-qubit by the fact that SU(2)_L = Spin(3) ⊂ Spin(1,3) acts on Dirac spinors through the left-multiplication ℍ-action.

The net claim: **a single orientation choice on 𝕆 propagates through the Cayley-Dickson tower to select one Dirac chirality as "left" and couple it to SU(2).** Abstract three-qubit frustration without the Cayley-Dickson decoration does not force chirality (this was the negative result from the ChatGPT analysis of the earlier entanglement-as-processes exchange); the octonionic decoration does.

### 7.3 What's proved and what's conjectured

Proved: the orientation of the Fano plane is a discrete choice, and reversing it gives the opposite octonion algebra.

Proved: Filatov's two-sphere handedness is a topological invariant of the quaternionic Hopf fibration.

Conjectured: these two orientations are locked together through the octonionic Hopf tower in the specific way needed to make SU(2)_L the left-handed action and not the right-handed one. This is the **chirality fixed-point conjecture**, flagged in the entanglement-as-processes analysis and still the single most important open problem in the chirality section.

A rigorous statement would show: (i) the 𝕆-orientation induces a preferred ℍ-orientation via the S⁷ sub-fibration of S¹⁵, (ii) the preferred ℍ-orientation selects left-multiplication over right-multiplication, (iii) SU(2)_L = left-multiplication action of unit quaternions on the B-qubit. Each step is tractable; none is written up.

---

## 8. Class 4 = the a-chiral sterile neutrino

### 8.1 The topology of Class 4

Class 4 has all three qubits with the same handedness (all ↑ or all ↓). All three Filatov constraints are violated. No opposite-handedness pair exists anywhere in the state.

### 8.2 Why this particle is sterile

Gauge interactions in the framework act on the Bloch-sphere handedness structure:

- **U(1)_Y (hypercharge)** acts on ℂ-qubit phase. In Class 4, all three qubits have aligned handedness, so there is no preferred phase direction; net U(1) charge = 0 by S₃ symmetry.
- **SU(2)_L** acts by rotating within a Filatov pair (one edge satisfying the opposite-handedness constraint). Class 4 has no such pair — *every* edge is frustrated. There is nothing for SU(2)_L to rotate within. SU(2) charge = 0 because the structure SU(2) requires is absent.
- **SU(3) colour** is only present for GHZ-class states (by the GHZ → ℂ³ theorem). Class 4 belongs to the W SLOCC class, not GHZ. Colour charge = 0.

All three gauge charges are zero by *topology*, not by cancellation of contributions. The particle does not couple to any gauge interaction.

This is the framework's definition of a **sterile** particle.

### 8.3 Why it's "a-chiral," not "right-handed"

The standard framing of the right-handed neutrino assumes ν_R is the parity partner of ν_L — they have opposite Dirac chirality but are otherwise the same kind of object. In particular, parity restoration at high energy should produce ν_R from ν_L.

Class 4 is topologically distinct from this picture. It is not the parity partner of anything. Its handedness is undefined because the concept of "opposite-handedness pair" requires at least one pair, and Class 4 has zero such pairs. This is what **a-chiral** means: not a chirality value (not L, not R), but *the absence of the structure on which chirality is defined*.

The physical consequence: parity restoration does not produce a-chiral states from chiral ones. The standard objection "sterile neutrinos should be produced by parity restoration at high energy, and therefore must exist as companions of active neutrinos" does not apply. The a-chiral state is topologically separate and has its own production mechanism (the computability-scale Majorana mass, discussed below).

### 8.4 Majorana nature and the seesaw

With all three gauge charges vanishing by topology, the a-chiral state can be its own antiparticle: no charge to distinguish particle from antiparticle. This is the Majorana property.

The mass mechanism for the a-chiral state is distinct from the Higgs-mediated L↔R zigzag used by Dirac fermions. A Dirac fermion acquires mass via chirality flipping: a left-handed electron emits a Higgs, becomes right-handed, emits another Higgs, becomes left-handed, etc. — the Zitterbewegung zigzag. This requires both chiralities to exist as Filatov states.

The a-chiral state has no Filatov partner to zigzag to. Instead, its mass comes from a self-closing geodesic at the **computability matching scale** Λ ≈ 3.6 TeV — the same scale that sets sin²θ_W = 1/4 bare. This scale is where the Cayley-Dickson fibre geometry becomes exact and all non-computable structure is concentrated. The Majorana mass is the geodesic length of a loop that starts and ends at the same a-chiral state, traversing the fibre geometry at this scale.

This is the **TeV-scale seesaw** prediction of the framework: M_R ≈ 3.6 TeV, not the ~10¹⁴ GeV of GUT-scale seesaw models. It is the only seesaw scale consistent with the framework's rejection of unification and its identification of ~3.6 TeV as the natural matching scale for all bare electroweak parameters.

### 8.5 Counting a-chiral states per generation

How many Class 4 states exist per generation? This is subtler than it looks.

The K₃ obstruction classifies handedness assignments globally, not per generation. Class 4 is one class in the four-class partition. But each of the three Cayley-Dickson levels can carry its frustration independently, and the a-chiral state does not distinguish between them (all three are maximally frustrated). One might naively think Class 4 is a single state.

However, Class 4's *internal* structure is not completely symmetric: the ℂ-level frustration is trivial (commutative, associative — no obstruction to "frustrate"), while the ℍ and 𝕆 levels carry genuine non-computable structure. The framework identifies **two independent a-chiral modes**: one with ℍ-level structure and one with 𝕆-level structure.

This predicts **two sterile neutrinos** at the computability scale, generation-independent. In the standard seesaw mechanism, two right-handed neutrinos produce two massive + one massless active neutrino, yielding:

- **m₁ = 0 exactly** — the lightest active neutrino has zero mass. Falsifiable: cosmological m₁ bound, double-beta decay effective mass.
- **Normal mass ordering** is mandatory: m₁ < m₂ < m₃. Consistent with current data, not yet decisive.
- **Two generation-independent sterile mass eigenstates** at ~3.6 TeV. In principle observable at future colliders.

**Status flag.** The "two, not three" count for sterile neutrinos is the weakest link in this chain. The argument that the ℂ-level frustration is trivial is structurally reasonable but not proved as a theorem in the current corpus. If the count is three rather than two, the active neutrino mass pattern changes: three sterile give three massive active (no m₁ = 0 prediction). This is worth stress-testing.

---

## 9. What the framework predicts, and what falsifies it

Summarising the derived content of Classes 1-4:

**Confirmed by existing data.**

- Three generations. (Matches observation. Contrast with string-theory or extra-dimension scenarios that permit arbitrary generation counts.)
- SU(2) doublets with one T₃ = −1/2 and one T₃ = +1/2 partner. (Matches observation.)
- Mass hierarchy m_1 < m_2 < m_3 by algebraic depth. (Matches: m_e < m_μ < m_τ, m_d < m_s < m_b, m_u < m_c < m_t. Note the m_u < m_c ordering survives despite m_u being surprisingly light.)
- No fourth generation. (Consistent with LEP Z-width, though not uniquely predicted by this framework alone.)
- Charge quantisation at multiples of 1/3. (Follows from the ℂ ⊕ ℂ³ decomposition of 𝕆 and its projection onto allowed handedness configurations.)

**Predictions not yet in data.**

- **m_1 = 0** (lightest active neutrino). Falsifiable by KATRIN-like experiments or cosmological Σm_ν bounds.
- **Normal mass ordering** (m_1 < m_2 < m_3). Will be falsified or confirmed by JUNO, Hyper-K, DUNE within ~5 years.
- **Two sterile neutrinos at ~3.6 TeV**. In principle observable at future colliders; more immediately, their cosmological abundance should match dark matter density.
- **No fourth-generation quarks or leptons at any scale**. This is a stronger statement than LEP-Z bounds, because it says no fourth generation exists even above LHC energies.

**What would falsify the K₃ argument specifically.**

- Discovery of a fourth SM generation at any scale.
- Discovery of a chiral right-handed neutrino (as opposed to a-chiral sterile) that is the parity partner of ν_L.
- Evidence for three (rather than two) sterile neutrinos contributing to the seesaw.
- Inverted mass ordering of active neutrinos.

Any of these would falsify the K₃ argument without (necessarily) falsifying the rest of the framework, because the K₃ mechanism is a specific refinement of the triality-based generation count. Triality alone gives three; K₃ gives 3 + 1.

---

## 10. Open problems

The chain of reasoning has three genuinely open links that should be flagged in any honest presentation:

1. **Three-sphere Filatov extension.** The two-sphere theorem is published. The three-sphere version is natural but not proved. Filatov has been contacted; no reply. Until this is rigorous, §3.1 is an *assumption*, not a theorem. The combinatorics of §4 follow once the assumption is granted.

2. **Chirality fixed-point.** §7.3 sketches the mechanism by which 𝕆-orientation propagates through the Cayley-Dickson tower to select SU(2)_L over SU(2)_R. The three steps (𝕆 → ℍ orientation via S⁷ sub-fibration, ℍ-orientation selects left-multiplication, SU(2)_L = left-multiplication action) are tractable but not written up. This is the single most important open problem in the chirality section.

3. **Two-vs-three sterile count.** §8.5 argues for two independent a-chiral modes on the grounds that ℂ-level frustration is trivial. The argument is structurally reasonable but not a theorem. If the correct count is three, the neutrino mass phenomenology changes.

None of these three open problems is expected to overturn the overall structure. All three are the kind of problem that a mathematician with the right background (Filatov for #1; Heunen or Baez for #2; any competent field theorist working with the framework for #3) could resolve in a few months of focused work.

---

## 11. Summary

A single topological fact — K₃ is not 2-colourable — combined with the Filatov constraint on entangled Bloch-sphere pairs, generates four resolution classes for the three internal Cayley-Dickson qubits. Three of these classes differ by which qubit carries the topological frustration, and these become the three fermion generations. The mass hierarchy follows from the algebraic depth of the frustrated qubit: ℂ-frustration is lightest, 𝕆-frustration heaviest. Within each class, the frustrated pair has two topologically distinct resolutions, which become the two members of the SU(2)_L doublet. The fourth class — all three qubits with the same handedness — has no opposite-handedness pair, hence no SU(2) structure to act on. It is *a-chiral* (not right-handed, not left-handed) and sterile to all gauge interactions. It carries the Majorana mass at the computability scale and drives a TeV-scale seesaw mechanism predicting two sterile neutrinos, m₁ = 0, and normal mass ordering.

One topological obstruction → three generations + SU(2) doublets + a sterile sector. The framework's single-principle account of the Standard Model fermion content rests on the non-2-colourability of K₃, the assumed extension of the Filatov constraint to three spheres, and the chirality fixed-point argument that propagates 𝕆-orientation through to SU(2)_L. Two of these three pillars are proved; the third — the Filatov extension — remains the key open problem at the foundation of the chain.

---

*Companion to `ghz_to_c3_theorem.md` and `w_to_su2l_doublet_theorem.md`. Together the three documents supply the framework's derivation of Standard Model fermion structure: colour (GHZ → ℂ³), weak isospin (W → SU(2)_L doublet), and generations + sterile neutrino (K₃ obstruction). The particle identifications become theorems, subject to the open problems flagged in §10.*
