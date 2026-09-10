# F1 established: the one-qubit dictionary of the Hopf-fibration–Frobenius correspondence

**Session document, 2026-07-03.** The first condition (F1) of `op:hopf-frobenius` (the
Hopf-fibration–Frobenius correspondence, posed in `sec:hopf-compositional` of Paper 1) is
established: a precise bijection between classical structures on a qubit and section data of the
complex Hopf bundle, equivariant for the natural symmetries, with the record-level collapse and the
spider reading worked out. Every finitely-checkable claim is verified by executed code
(`f1_verification_2026-07-03.py`). One plausible stronger claim was tested, found false, and is
recorded as a dead route. Literature checked 2026-07-03; the field is clear, with three anchors to
cite and one two-month-old near neighbour that turns out to be the complementary projection.

**Status flags.** Lemma parts (a)–(d): proved (short proofs below; (a) rests on the
Coecke–Pavlovic–Vicary classification, the rest is direct computation). The framework reading
(fibre-choice as the germ of the paper's U(1) content): structural. The dead route (topological
no-cloning): refuted, recorded. F2–F4 of the correspondence: open, unchanged.

---

## 1. The Lemma

Throughout, H = ℂ², π : S³ → S² is the complex Hopf fibration (S³ the unit vectors of ℂ², S² = ℂP¹
the rays, π the ray map), and a **†-SCFA** is a dagger special commutative Frobenius algebra (δ, ε)
on H in **FdHilb** — a *classical structure*. A **lifted skeleton** is a pair (P, s): an unordered
antipodal pair P = {p, p̄} ⊂ S² (equivalently, an unordered pair of orthogonal rays in ℂ²) together
with a section s : P → S³ of π over P (a choice of unit-vector lift of each point).

**Lemma (F1 dictionary).**

**(a) Bijection.** †-SCFAs on ℂ² correspond bijectively to lifted skeletons. Under the
correspondence the copyable states of (δ, ε) — the non-zero x with δ(x) = x ⊗ x — are exactly the
image s(P) = {v₀, v₁}; conversely a lifted skeleton determines the structure by
δ(vᵢ) = vᵢ ⊗ vᵢ, ε(vᵢ) = 1. The correspondence records the lifts faithfully: if x is copyable then
e^{iθ}x is copyable only for θ = 0, and bases differing only by phases yield distinct structures on
the same ℂ² (verified: checks 1–2).

**(b) Equivariance.** The bijection intertwines the natural U(2)-actions: on structures by
transport, δ ↦ δ_U = (U ⊗ U) δ U†, and on lifted skeletons by the action of U on S³ (which covers
the induced rotation of S²). Copyables of δ_U are {Uv₀, Uv₁} (verified: check 3). The centre acts
non-trivially: U = e^{iα}·id fixes every skeleton and every point of the base, yet moves the
structure, δ ↦ e^{iα}δ, copyables ↦ e^{iα}vᵢ (verified: check 4). Consequently the action of U(2)
on *ordered* lifted skeletons is simply transitive: **the space of ordered classical structures on a
qubit is a U(2)-torsor** — the classical structures are, as a space, the gauge group itself.

**(c) Record-level collapse.** The channel induced by a structure,
Δ_δ(ρ) = δ†(ρ ⊗ I)δ, equals dephasing in the skeleton, Δ(ρ) = Σᵢ Pᵢ ρ Pᵢ with Pᵢ the ray
projectors, and therefore depends on P alone: distinct structures over one skeleton induce the
identical channel (verified: check 5). The section freedom over a fixed skeleton — a torsor for
Map(P, U(1)) ≅ U(1) × U(1), every phase pair giving a valid and distinct structure (verified: check
6) — is thus exactly the data absent from every classical record. **The base carries the
classical index; the section carries the quantum re-embedding; the fibre freedom is gauge at the
classical level.**

**(d) Specialness and the spider reading.** μδ = id (specialness) holds for every structure
constructed (verified throughout), and Δ² = Δ: classicising is idempotent, projection onto the
skeleton stays on the skeleton. Copying, δ, broadcasts the skeleton index *by means of* the chosen
lifts: what is copied is a specific vector — section data — not a ray.

## 1a. Refinement, same day: the fibre torsor decomposes — and Popper's 1950 anchor

A precision audit prompted by the Popper connection (below) sharpens part (c)'s scope. What check 5
verifies is that the induced *classical record* — the dephasing channel Δ — is section-independent.
The copier's *coherent* action is not: for lifts differing by phases (θ₀, θ₁),
δ′(α|0⟩ + β|1⟩) = e^{iθ₀}(α|00⟩ + e^{i(θ₁−θ₀)} β|11⟩), so the torsor Map(P, U(1)) splits as
U(1)_diag × U(1)_rel. The **diagonal** phase is a global scalar on the isometry — gauge for every
observer, absolutely. The **relative** phase never appears in the copier's own classical record but
is carried by the coherent copy state, accessible only to an observer who treats the copier itself
coherently (calibrated process tomography): in the Wigner's-friend anatomy, exactly the from-above
access that promotion describes. Wording in the Lemma and in the paper's proposition accordingly
tightened from "invisible at the density level" to "absent from the classical record the structure
induces"; the stronger reading would be false, and the falsifying computation is the displayed
state. (Check 5 covered arbitrary (θ₀, θ₁) for the record channel, so nothing executed changes;
only the prose scope does.)

**Popper's 1950 anchor.** Popper argued that a predictor C embedded in the world has inferior
knowledge of itself because it cannot impart self-information without, by that very act, rendering
it out of date — "making this information obsolete" (*Indeterminism in Quantum Physics and in
Classical Physics*, BJPS vol. 1, Parts I–II, 1950 — canonical cite keys `Popper1950a`/`Popper1950b`, already in the project bibliography; the quoted passage's page to be pinned from JS's
annotated copy). Part (c) is that obstruction made structural rather than temporal, and localised:
the datum C cannot put into its own record is not its state wholesale but exactly its fibre
commitment — the diagonal part private to every observer forever, the relative part accessible only
from above. When `sec:self-reference` is drafted, its lineage should open here: 1950 predates the
modern epistemic-horizon literature by half a century.


## 2. Proofs

**(a).** The Coecke–Pavlovic–Vicary theorem: †-SCFAs on a finite-dimensional H correspond to
orthonormal bases, the basis being recovered as the set of copyables. An orthonormal basis of ℂ² is
precisely two orthogonal rays with a chosen unit representative of each; orthogonality of rays in ℂ²
is antipodality on the Bloch sphere (|⟨v₀|v₁⟩|² = (1 + n̂₀·n̂₁)/2); and a choice of unit
representative over each ray is a section of π over the corresponding base points. Phase-pinning:
δ(e^{iθ}x) = e^{iθ} x⊗x while (e^{iθ}x)⊗(e^{iθ}x) = e^{2iθ} x⊗x, equal only at θ = 0. ∎

**(b).** δ_U(Ux) = (U⊗U)δ(x) for any x, so x copyable for δ iff Ux copyable for δ_U; the action on
copyable sets is v ↦ Uv, i.e. the action of U on S³, covering the base rotation. Centre: with
U = e^{iα}id, (U⊗U)δU† = e^{2iα}δ e^{-iα} = e^{iα}δ. Simple transitivity on ordered lifted
skeletons: an ordered orthonormal basis with phases is the column data of a unitary matrix, on which
U(2) acts simply transitively by left multiplication. ∎

**(c).** δ†(ρ⊗I)δ = Σᵢⱼ vᵢ ⟨vᵢ|ρ|vⱼ⟩⟨vᵢ|vⱼ⟩ vⱼ† = Σᵢ ⟨vᵢ|ρ|vᵢ⟩ vᵢvᵢ†, which depends only on the
projectors vᵢvᵢ†, i.e. on the rays. The set of structures over a fixed skeleton is
{(e^{iθ₀}v₀, e^{iθ₁}v₁)}, a free transitive Map(P,U(1))-space. ∎

**(d).** μδ = Σᵢⱼ vᵢ vᵢ†vⱼ (vᵢ⊗vᵢ)†(vⱼ⊗vⱼ) … reduces by orthonormality to Σᵢ vᵢvᵢ† = id;
Δ² = Δ by the projector algebra. ∎

## 3. Verification record

`f1_verification_2026-07-03.py`, executed 2026-07-03, all checks pass:
(1) copyables of the computational-basis structure are |0⟩, |1⟩ and *not* e^{iθ}|0⟩;
(2) the rephased basis yields δ′ ≠ δ with the rephased vectors as its copyables, both structures
satisfying specialness, coassociativity and cocommutativity;
(3) five random U(2) transports: valid structures, copyables {Uv₀, Uv₁}, old basis not copyable;
(4) centre: δ_{e^{iα}id} = e^{iα}δ, copyables e^{iα}vᵢ;
(5) five random density matrices: Δ_δ = skeleton dephasing = Δ_δ′ for distinct structures over one
skeleton;
(6) six phase pairs over a fixed skeleton: all valid, pairwise distinct structures.

## 4. What this does not show (dead route, recorded)

It is tempting to read the non-triviality of the Hopf bundle (Chern class 1, no global section) as a
topological derivation of no-cloning. **This fails, and should not be retried in this form.** The
finiteness of the copyable set is linear-algebraic — copyables are linearly independent, hence at
most dim H of them — and local sections of the bundle exist, so nothing topological forbids a
continuum of copyables; linearity does. The categorical locus of structural no-cloning is
*non-naturality* (Abramsky; Abramsky–Heunen): there is no natural family of diagonals in a compact
closed category. At k = 1 the Chern class does no work. The first place the bundle's global
topology can genuinely bite is k = 2 — see §6.

## 5. Literature triangulation (checked 2026-07-03)

Three anchors, one near neighbour; no collision with the dictionary as stated.

**Coecke–Pavlovic–Vicary** (existing key `coeckepavlovicvicary2013orthogonal`): the classification
†-SCFAs ↔ orthonormal bases. Algebraic; no bundle language. Part (a) rests on it.

**Abramsky–Heunen** (arXiv:1011.6123, "H*-algebras and nonunital Frobenius algebras"): frames
Frobenius structures as the algebraic account of observables and records structural no-cloning as
non-naturality — the correct home of the fact the dead route sought in topology. Cite if F1 enters
the paper.

**Mosseri–Dandoloff / Bernevig–Chen** (existing keys): the fibration side; states and phases
geometrically, no Frobenius structures. The mutual silence noted in `sec:hopf-compositional` stands.

**Burton–Anwar, "Meromorphic Quantum Computing" (arXiv:2605.06251, May 2026, Quantinuum).** The
near neighbour, and the complementary projection rather than a collision. They projectivise:
functorially and lax-monoidally pass to the base ℙ¹ = Riemann sphere, deliberately forgetting the
fibre (global phase is, in their words, "annoying fluff on the carpet"), and re-derive the
arithmetic GHZ/W-calculus there. F1 shows the classical structures live in exactly the data their
functor forgets: the Frobenius data pins lifts into the total space, and the projectively-invisible
centre of U(2) moves classical structures (check 4). The two readings compose rather than compete:
their projectivisation functor is a candidate right leg of a consistency triangle
**Hopf → Frob → ℙ**, in which our F followed by their projectivisation should recover base data ---
a concrete compatibility condition available to constrain F2–F4. (Their paper is two months old;
the mutual-silence observation in the paper's subsection is, happily, already dated on the base
side --- worth a clause when citing.)

## 6. What F1 buys, and the next bounded question

F1 discharges the first condition of `op:hopf-frobenius` and upgrades the problem from invitation to
invitation-with-downpayment: the route exists, its first step is walked, and it already produced a
correction to folklore (lift-selection, not base-projection) plus the torsor identity (ordered
classical structures on a qubit = U(2)). For the framework specifically, part (c) gives the paper's
own split a one-qubit germ: base = classical record, fibre choice = U(1) freedom absent from
every classical record — the private-phase reading the A-register carries, now with a theorem-shaped
statement behind it.

**The next bounded question is F2's first check, and it is where topology first has teeth.** The
quaternionic bundle S⁷ → S⁴ is classified by its clutching map S³ → SU(2) of degree one; on the
categorical side, a *pair* of interacting classical structures is governed by strong
complementarity (the Hopf law — Heinz Hopf's name again, on the third structure in the story).
Conjecture to test: the clutching data is the geometric shadow of strong complementarity — the
degree-one map standing to the bialgebra interaction as the section data of F1 stands to a single
Frobenius structure. Bounded first computation: express the complementarity conditions for a
mutually unbiased pair of ℂ²-structures in the S⁷ coordinates of Mosseri–Dandoloff and identify
what bundle datum they constrain. Not attempted here.

## 7. Placement options for Paper 1 (decision: John's)

**(A)** A Proposition plus two sentences in `sec:hopf-compositional`, after the partial-evidence
paragraph: state parts (a)–(c) compactly as "the first of the four conditions is established", cite
CPV (existing), Abramsky–Heunen and Burton–Anwar (two new RIS), and point the reader here/to the
repo for proofs and the executable check. Cost: ~12 lines and two RIS entries. Benefit: the open
problem ships with its first condition proved, which is the strongest possible form of the
invitation.

**(B)** Repo note only (`scripts/` + this document); the paper's problem ships as posed.

Recommendation: (A) — the downpayment is cheap and real. But it adds scope days into a
done-beats-perfect push, so the call is John's.

## References (RIS deferred to the placement decision)

Coecke, Pavlovic, Vicary — existing key `coeckekissinger…/coeckepavlovicvicary2013orthogonal`.
Abramsky, Heunen — arXiv:1011.6123. Burton, Anwar — arXiv:2605.06251. Mosseri–Dandoloff,
Bernevig–Chen, Coecke–Kissinger 2010 — existing keys.
