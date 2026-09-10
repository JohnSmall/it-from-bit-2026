# Research Prompt: Extending the Two-Sphere Handedness Theorem to Three Qubits

**For:** Stanislav Filatov.
**From:** John Smith's "It from Bit" research programme (Växjö).
**Use:** read directly, or paste to an LLM assistant as a working brief. It is self-contained.

## 0. Why you, and what is being asked

Your result with Auzinsh — that a pure entangled two-qubit state, drawn as a pair of Bloch
spheres, forces the two spheres' coordinate frames to be **opposite-handed** — has become a
foundation stone of a larger programme: it is the mechanism by which that programme derives the
three fermion generations, the weak-isospin doublet, and a fourth, sterile channel. The programme's
papers currently carry the tripartite extension of your theorem as an **explicitly stated open
assumption**, flagged as the foundational open problem of their generation sector — and it is
reserved, deliberately, for you. This document states the problem precisely, hands over everything
the programme has established that bears on it, is honest about where the difficulty lives, and
sketches candidate routes without presuming your approach. A theorem, a theorem-with-restricted-
scope, or a clean counterexample would all be major contributions; the papers will cite whichever
you find.

## 1. The problem, in two parts

**Part A (the pairwise-entangled case).** Let |ψ⟩ be a pure three-qubit state in which all three
pairs are entangled (the W class is the canonical case). Conjecture: in a faithful
three-sphere-plus-fibre representation of |ψ⟩, **each entangled pair independently imposes your
handedness constraint** — the two spheres of every entangled pair must carry opposite-handed
frames. Since the triangle K₃ is not two-colourable, the three constraints cannot all be
satisfied: the representation is *frustrated*, and the inequivalent ways of resolving the
frustration are what the programme reads as physical structure. What is needed is the theorem
behind "each entangled pair independently": that each pair of a tripartite state carries its own
quaternionic Hopf structure, so that the two-sphere constraint applies edge by edge.

**Part B (the companion, harder and stranger).** The GHZ class has **no pairwise entanglement at
all** — every two-qubit reduced state is separable — yet the programme needs the same
resolution-class structure to govern GHZ-type registers too. Part B asks: in what precise sense
does a genuinely tripartite (GHZ-type) state constrain the relative handedness of its three
spheres, when no edge is entangled? This may require reformulating what "the constraint" *is*: the
GHZ correlations are perfect pairwise in the computational basis (classically correlated, not
entangled), and the entanglement is irreducibly three-way. An answer that treats Part B as a
different theorem with a different mechanism is entirely acceptable; an answer showing Parts A and
B are one theorem in a tripartite representation would be beautiful.

## 2. Where the difficulty genuinely lives

Your two-sphere theorem concerns **pure** two-qubit states. Inside a tripartite state, the pairwise
reduced states are **mixed**. For the canonical W state, each pair's reduced state is

  ρ_pair = (2/3) |Ψ⁺⟩⟨Ψ⁺| + (1/3) |00⟩⟨00|,

rank 2, with concurrence 2/3. So the extension is *not* a corollary of the pure-state theorem
applied to marginals — the marginal is not a pure state, and the two-sphere representation of a
mixed state is not the one your theorem addresses. Any honest route must do one of three things:
extend the handedness theorem to (a class of) mixed states; or define the per-sphere frames through
the **pure tripartite object itself** rather than through marginals; or show the constraint is a
property of a genuinely three-body representation from which pairwise handedness is *read off*, not
inherited. This is the crux, and it is why the programme flagged the extension as open rather than
claiming it.

## 3. What is established (all checkable; several machine-verified)

- **Your theorem** (pure two-qubit, opposite-handed frames), which the programme reads as a
  topological fact about the quaternionic Hopf fibration S⁷ → S⁴ with fibre S³ — the fibre carrying
  the relative-frame data.
- **Canonical states and their invariants.** W = (|001⟩+|010⟩+|100⟩)/√3: every single-qubit
  reduced state has spectrum (2/3, 1/3); every pairwise concurrence equals 2/3; the three-tangle
  τ₃ = 0. GHZ = (|000⟩+|111⟩)/√2: every pairwise concurrence is 0; τ₃ = 1; every single-qubit
  marginal is maximally mixed.
- **The combinatorics downstream of Part A** (rigorous once Part A is granted): with one binary
  handedness label per sphere and an "opposite on every edge" demand, the 8 assignments satisfy
  either 0 or 2 of the three constraints — never 1 or 3 (a parity fact of the odd cycle). The six
  2-satisfying assignments fall into three classes by the position of the odd vertex; the two
  0-satisfying assignments (all-same) form a fourth class; the global flip pairs assignments as
  state/conjugate. Three classes + one: the programme's three generations and its sterile channel.
- **The three-qubit Hopf geometry exists and is class-sensitive.** The 15-sphere of three-qubit
  states carries the octonionic Hopf fibration S¹⁵ → S⁸ with fibre S⁷, and under the induced map
  built on the split 𝕆 = ℂ ⊕ ℂ³, canonical GHZ states land on the ℂ³ side and canonical W states
  reach the ℂ side — proved and numerically verified within the programme. Any tripartite
  representation you build can be checked against, or founded on, this structure.
- **A relevant frustration echo.** Realising an "unlike-oriented" edge as the two-qubit singlet and
  contracting a closed three-edge network with the natural copy fusion, exactly the even-flip
  patterns transmit and all odd patterns annihilate — the contraction enforces the K₃ cycle parity
  by itself. This is a network-level shadow of the same odd-cycle structure Part A concerns, and it
  is executable in a dozen lines of NumPy if a sanity target is wanted.

## 4. Literature you will want on the desk

Mosseri & Dandoloff, *Geometry of entangled states, Bloch spheres and Hopf fibrations*,
J. Phys. A **34**, 10243 (2001) — the S⁷ representation of two qubits your theorem lives beside.
Mosseri's follow-up on the three-qubit case and S¹⁵. Bernevig & Chen, *Geometry of the three-qubit
state, entanglement and division algebras*, J. Phys. A **36**, 8325 (2003) — the octonionic
S¹⁵ → S⁸ treatment, sensitive to exactly the GHZ/W distinction Part B turns on. Coffman, Kundu &
Wootters on the three-tangle and monogamy, for the invariants quoted above. And, of course, your
own two-sphere paper with Auzinsh, whose proof technique is the natural thing to try to transplant.

## 5. Candidate routes (offered, not prescribed)

**Route 1 — the tripartite representation.** Generalise the two-qubit two-sphere-plus-fibre picture
to three qubits directly, via the iterated/octonionic Hopf structure (Mosseri; Bernevig–Chen):
define the three spheres and their frames from the pure state, then *prove* the edge-handedness
relations as properties of the representation — pairwise handedness read off, never inherited from
mixed marginals. This is the programme's guess at the natural home of both parts, since the
representation is already known to separate GHZ from W.

**Route 2 — a mixed-state handedness theorem.** Extend your theorem from pure states to the class
of rank-2 two-qubit mixed states that arise as marginals of pure tripartite states (the W marginal
above is the canonical target). A plausible shape: nonzero concurrence forces opposite handedness,
with the constraint degrading gracefully — perhaps vanishing exactly with the concurrence, which
would automatically explain why GHZ (concurrence 0 on every edge) needs Part B's different
mechanism.

**Route 3 — purification.** The third qubit *is* the purifier of each pair. Define the pair's
sphere frames conditionally — via the steered ensembles the third qubit induces — and prove
handedness ensemble-wise. This route makes the tripartite nature of the constraint explicit from
the start.

**Route 4 — holonomy formulation.** Express handedness as an orientation of S³-fibre transport,
and the three-edge demand as a cocycle condition on the triangle; frustration is then a nontrivial
ℤ₂ holonomy — one circuit returns a flip, two circuits return the identity. This is the
formulation the programme would ultimately like to *interpret* (it connects the K₃ structure to
double covers and spin), but no route is presumed: whatever proves the theorem defines the object.

## 6. What counts as success

Any of the following would resolve the open problem as posed and be recorded with attribution:
a proof of Part A (with Part B separately addressed, even if only scoped); a proof with an explicit
domain of validity narrower than "all pairwise-entangled tripartite states" (the programme would
then know exactly which registers the generation machinery governs); or a counterexample — a
pairwise-entangled tripartite state admitting a faithful representation with a consistent
handedness assignment — which would force a sharp revision and would be *equally* valuable, since
the downstream combinatorics would then need a different foundation and the sooner that is known
the better. Partial results welcome: even the mixed-state two-sphere question (Route 2) standing
alone is a publishable theorem about your own representation.

## 7. Practical notes

Numerics are encouraged alongside proof: the canonical states, their invariants, and the network
parity fact of §3 give sharp targets that a short NumPy or Qiskit script can check, and the
programme's experience is that planted assertions catch wiring errors and occasionally catch
discoveries. The problem is yours within the programme — it is stated in the papers as open,
without an attempted solution, precisely so that the first proof is yours to publish; the
programme's role afterwards is to cite it and build on it. Questions, partial results, or "this
route is dead" reports are all welcome by email at any stage — dead routes are recorded so nobody
retries them, which is itself a contribution.
