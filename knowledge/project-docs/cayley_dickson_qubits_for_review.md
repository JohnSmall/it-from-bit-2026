# Qubits across Cayley-Dickson sectors: framework summary for external review

## Purpose

This document describes a specific construction — three qubits, each valued in a different normed division algebra — used in a framework that derives Standard Model content from self-referential foundations. It is written for an external reviewer (human or LLM) with working knowledge of quantum information, Lie theory, and particle physics. The goal is critical engagement, not summary. Open problems and contestable claims are flagged explicitly.

---

## 1. The construction

Three qubits, drawn from successive levels of the Cayley-Dickson construction:

- **A-qubit** over ℂ (complex numbers)
- **B-qubit** over ℍ (quaternions)
- **C-qubit** over 𝕆 (octonions)

Each is a two-state system, but the "two states" in each case are valued in a different normed division algebra. The triple (A, B, C) is the minimal system on which the claimed Standard Model particle content arises.

## 2. Why these three, and only these three

Three termination theorems converge on the same dimensional cap:

1. **Hurwitz (1898).** The normed division algebras are exactly ℝ, ℂ, ℍ, 𝕆.
2. **Adams (1960).** The parallelisable spheres are exactly S⁰, S¹, S³, S⁷.
3. **Coecke-Kissinger (2017).** Compositional completeness of finite-dim QM is achieved at tripartite GHZ/W entanglement species; no new species appear above three parties.

ℝ is excluded as a physical qubit base on independent grounds (Müller: real-Solomonoff induction cannot reproduce Bell violations). 𝕆 is terminal — sedenions lose the norm and introduce zero divisors. What remains is three qubits over {ℂ, ℍ, 𝕆}.

**Contestable claim:** The three terminations are not independent facts. The framework conjectures (Hopf-Frobenius conjecture, open) that Adams' theorem implies Coecke-Kissinger completeness as a topological corollary.

---

## 3. The three qubits in detail

### 3.1 A-qubit: ℂ-qubit (standard)

- Hilbert space: ℂ²
- State space: S³ (unit sphere)
- Hopf fibration: S³ → S² with fibre S¹ = U(1)
- Automorphism: U(2) = (U(1) × SU(2)) / ℤ₂
- Algebraic properties: commutative, associative, normed
- Information-theoretic: no-cloning in the usual quantum sense, but FANOUT on the computational basis is well-defined

**Physical role assigned:** U(1) phase; global-phase degree of freedom that underwrites the Born-rule derivation (global phase = observer's private self-referential ignorance, unable to be communicated via FANOUT, so observables must be U(1)-invariant).

### 3.2 B-qubit: ℍ-qubit

- Hilbert space: ℍ² (right-module over ℍ)
- State space: S⁷
- Hopf fibration: S⁷ → S⁴ with fibre S³ = SU(2)
- Automorphism: Sp(2) ≅ Spin(5)
- Algebraic properties: non-commutative (ab ≠ ba), associative

**Physical role assigned:** Weak isospin SU(2). Left/right quaternion multiplication corresponds to the two possible actions; the re-bracketing dynamics (W±) live here. Bell-class entanglement is naturally housed in this layer because Bell pairs span a 2-dimensional subspace supporting SU(2).

**Standard objection to address:** Adler and others have raised well-known issues with ℍ-QM as a fundamental theory (tensor product ambiguity, composite-system difficulties). The framework's response: ℍ is not the base of physical QM; it is the internal algebra of one of three qubits in a ℂ-based outer Hilbert space. The framework does not assert ℍ-QM as a replacement for ℂ-QM.

### 3.3 C-qubit: 𝕆-qubit

- State space: S¹⁵
- Hopf fibration: S¹⁵ → S⁸ with fibre S⁷
- "Automorphism": G₂ (14-dim exceptional Lie group, Aut(𝕆))
- Algebraic properties: non-commutative, **non-associative**; associator [a,b,c] = (ab)c − a(bc) is non-zero

**Caveat on "Hilbert space":** Because 𝕆 is non-associative, 𝕆² is not a Hilbert space in the ordinary sense. It is a normed module with inner product. The framework treats the C-qubit as a geometric object (S¹⁵ with Hopf structure) rather than a quantum system in the Dirac/von Neumann sense.

**Physical role assigned:**

- Colour SU(3) as the stabiliser of a preferred ℂ ⊂ 𝕆 inside G₂
- The associator [a,b,c] carries mass: mass = associator debt, with units [L⁻¹] in natural units
- Non-associativity breaks Spin(8) triality, which forces a specific spinor vs co-spinor assignment — i.e. chirality
- Fano plane orientation is the discrete chirality at the algebraic level

---

## 4. How the three qubits combine

On the tensor system A ⊗ B ⊗ C, the Dür-Vidal-Cirac SLOCC classification gives six entanglement classes: fully product, three biseparable, GHZ-class, W-class. The framework maps these to Standard Model sectors:

| Entanglement class | Standard Model sector |
|---|---|
| Fully product | Higgs |
| Bell-class (biseparable, bipartite) | Gauge bosons |
| GHZ-class (tripartite, diagonal, global correlation) | Quarks (colour triplets) |
| W-class (tripartite, off-diagonal, distributed correlation) | Leptons |

**Key structural claims (some proved, some flagged):**

1. **Proved (framework internal):** GHZ-class states map exclusively into the ℂ³ colour sector under the octonionic Hopf map, for all local unitaries. This forces θ_QCD = 0 topologically: GHZ has no oriented pairwise linking structure to carry a CP-violating phase, so the QCD axion is structurally forbidden.

2. **Proved (framework internal):** W-class states generically access the lepton sector (ℂ-valued, not ℂ³-valued).

3. **Claimed, derived:** Three generations arise from triality on the octonionic Hopf fibration. K₃ topological obstruction (K₃ is not 2-colourable) gives four resolution classes: three fermion generations + one sterile a-chiral state (dark matter candidate).

4. **Claimed, falsifiable:** GHZ-class states must be confined (no free colour); W-class states must be deconfined. This is asserted to follow from the monogamy/frustration asymmetry between the two classes, not postulated separately.

---

## 5. What each algebra contributes, at a glance

| Sector | Algebra | New structure | Physical role |
|---|---|---|---|
| A | ℂ | Norm, complex structure | U(1), global phase, Born rule |
| B | ℍ | Non-commutativity | SU(2), isospin, re-bracketing dynamics |
| C | 𝕆 | Non-associativity | SU(3), mass (associator), chirality (triality breaking) |

The progression ℂ → ℍ → 𝕆 is read as: commutative/associative → non-commutative/associative → non-commutative/non-associative. Each step loses a symmetry, and each lost symmetry is identified with a physical content:

- Losing commutativity ⇒ gauge-rotation content (SU(2))
- Losing associativity ⇒ mass and chirality

---

## 6. Claims a critical reviewer should stress-test

These are the places where the framework is strongest or weakest, depending on how the reviewer reads them. I list them with the framework's position stated, so the reviewer can push back.

**Q1. Is A/B/C really three distinct qubits or one composite state over a Cayley-Dickson tower?**
*Framework position:* Each is independently a two-state system; the algebra each is valued in determines what gauge structure it carries. The tensor structure is genuine tripartite, not a disguise for a single higher-dimensional space.

**Q2. Does treating ℍ and 𝕆 as "internal" algebras evade the standard objections to ℍ-QM and 𝕆-QM?**
*Framework position:* Yes, because ℂ remains the base of the physical Hilbert space; ℍ and 𝕆 appear as internal algebras for specific qubits, not as alternative foundations. This is the same move that lets Baez-Huerta use 𝕆 in Standard-Model-like constructions without claiming 𝕆-QM.

**Q3. Why three qubits specifically?**
*Framework position:* Forced by (i) three non-trivial Cayley-Dickson levels above ℝ, (ii) genuine tripartite entanglement (Dür-Vidal-Cirac) being the minimal case where GHZ and W are SLOCC-inequivalent, (iii) Coecke-Kissinger completeness at three parties.

**Q4. Is "mass = associator debt" dimensionally and physically coherent?**
*Framework position:* [a,b,c] has units [L⁻¹] in natural units when a, b, c are taken as wavenumber-valued octonion components. The claim is that mass as the information needed to specify a bracketing order is dimensionally forced, not tuned.

**Q5. Does selecting a preferred ℂ ⊂ 𝕆 (to get SU(3) ⊂ G₂) introduce a preferred direction that breaks gauge invariance observably?**
*Framework position:* The selection is the computability split itself, not an ad-hoc choice. The Moufang-loop "seven rights make a left" mechanism provides a non-arbitrary preferred direction. This is where the framework claims to resolve Furey's preferred-complex-direction problem.

**Q6. Does the GHZ/W-to-quark/lepton mapping survive alternative SLOCC-compatible assignments?**
*Framework position:* The mapping is fixed by: (a) GHZ = copyable/Frobenius structure (confinement), (b) W = non-copyable/anti-Frobenius (deconfinement), (c) the explicit theorem that GHZ ↦ ℂ³ and W ↦ ℂ under the octonionic Hopf map.

---

## 7. Open problems (framework-flagged, not rhetorical)

1. **Hopf-Frobenius conjecture.** Does Adams' theorem on parallelisable spheres imply Coecke-Kissinger compositional completeness as a topological corollary? (Heunen flagged as well-positioned to resolve.)

2. **Qutrit geometry conjecture.** Does a set of eight geometric properties P₁–P₈ hold jointly iff the system is underwritten by a normed division algebra?

3. **Torsionful Dirac operator spectrum on parallelised S⁷.** The eigenvalues would determine all 13 Yukawa couplings from the single gate specification. This is flagged as potentially the most significant open calculation in the framework.

4. **Chirality fixed-point.** Explicitly: what is the minimal relational structure that encodes W-type frustration, distinguishes orientation, couples to spinors, and forces global chirality? Framework conjecture: the octonionic Hopf fibration S¹⁵ → S⁸ with its orientation selected by the computability split.

---

## 8. Specific questions for the reviewing LLM

1. Does the three-qubit construction over (ℂ, ℍ, 𝕆) avoid the standard objections to quaternionic and octonionic quantum mechanics by virtue of being internal rather than fundamental? If not, why not?

2. Is the mapping {product, Bell, GHZ, W} ↔ {Higgs, gauge bosons, quarks, leptons} natural or ad hoc? What alternative mappings are consistent with the Dür-Vidal-Cirac SLOCC classification, and what would distinguish them?

3. Is "mass = associator debt" dimensionally and physically coherent as stated? Can you find a route by which the dimensional assignment fails?

4. What would falsify the claim that GHZ-class states map exclusively to the ℂ³ colour sector under the octonionic Hopf map?

5. Does restricting to a preferred ℂ ⊂ 𝕆 (to yield SU(3) ⊂ G₂) introduce a symmetry-breaking that should be observable, e.g. in CP violation measurements, or is the restriction physically inert in the way the framework claims?

6. Is the analogy GHZ:classical-Frobenius :: W:anti-Frobenius a genuine structural correspondence between Coecke-Kissinger categorical QM and the confinement/deconfinement distinction, or is it a suggestive coincidence?

7. Which of the three termination theorems (Hurwitz, Adams, Coecke-Kissinger) is, in your view, the most independent of the other two, and why?

---

*End of document. Please respond with critical engagement rather than summary; the framework's authors are seeking to identify weaknesses, not confirmation.*
