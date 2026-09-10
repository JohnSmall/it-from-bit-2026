# Quantum Circuits from Internal Qubits: Particle Interactions and Nucleon Physics

## Conversation Date: March 19, 2026

---

## 1. Core Idea

The framework identifies each Standard Model fermion as an entanglement pattern of three Cayley-Dickson qubits (A, B, C) corresponding to the three levels of the division algebra chain ℂ → ℍ → 𝕆. The fermion topology table (see `fermion_topology_table.py`) establishes that gauge interactions act on specific internal qubits:

| Interaction | Acts on | Operation | Constraint |
|-------------|---------|-----------|------------|
| Photon (γ) | Qubit A (ℂ) | U(1) phase rotation on S¹ | Only if Q ≠ 0 |
| W boson | Qubit B (ℍ) | SU(2) rotation on S³ within a Filatov pair | Only if T₃ ≠ 0 doublet |
| Z boson | Qubits A, B | Mixed A-B rotation (neutral current) | Determined by sin²θ_W = ¼ |
| Gluon (g) | Qubit C (𝕆) | SU(3) rotation on S⁷ | Only if colour triplet (GHZ component present) |
| Higgs (H) | All | Mediates L↔R zigzag (Zitterbewegung turnaround) | Couples doublet to singlet |
| Gravity | Base space | Light cone tipping = measurement | Acts on everything with mass |

This means every Feynman diagram has a direct translation into a quantum circuit acting on specific qubit registers. This is the entry point for a new approach to simulating particle and nuclear physics on quantum computers.

---

## 2. Particle Interactions as Quantum Circuits

### 2.1 Photon Exchange (QED vertex)

Two electrons, each represented as a 3-qubit register. The photon mediates a controlled-U(1) gate between the two A-qubits (ℂ-level), leaving B and C untouched. This is the simplest case: a correlated phase rotation on the S¹ fibres of both particles.

Circuit structure: Two 3-qubit registers (6 qubits total). Controlled phase gate between A₁ and A₂. B and C qubits are spectators.

### 2.2 W Boson Exchange (Charged Current / Beta Decay)

The canonical example is beta decay: d_L → u_L + W⁻.

In the internal qubit picture:
- d_L = Class 1a, α-resolution (T₃ = -½)
- u_L = Class 1a, β-resolution (T₃ = +½)

The W⁻ emission is an SU(2) gate on qubit B that switches the frustrated-pair resolution from α to β. The W then decays, creating a new 3-qubit system (electron) and a partially-entangled system (antineutrino).

The full neutron beta decay n → p + e⁻ + ν̄ₑ is a circuit with:
- Input: 9-qubit neutron register (three 3-qubit quarks: udd)
- Gate: SU(2) operation on one d-quark's B-qubit
- Ancilla creation: new 3-qubit registers for e⁻ and ν̄ₑ
- Output: 9-qubit proton register (uud) + 3-qubit e⁻ + 3-qubit ν̄ₑ

### 2.3 Z Boson (Neutral Current)

The Z is a mixed A-B gate — a neutral current that rotates both the ℂ-qubit and the ℍ-qubit simultaneously. The mixing angle is the Weinberg angle (sin²θ_W = ¼ at bare level in the framework).

Key observation: The Z is literally the **entangling gate between qubits A and B**, not a gate on either one alone. This gives the Weinberg angle a circuit-theoretic interpretation as a gate parameter.

### 2.4 Gluon Exchange (QCD vertex)

A gluon exchanged between two quarks applies an SU(3) rotation to the C-qubit of one quark, with a correlated inverse rotation on the other, maintaining the overall colour singlet constraint.

Critical feature: The non-associativity of the octonions manifests as **ordering constraints on the gate sequence**. Gluon operations cannot be freely commuted — this is the circuit-level expression of the non-abelian nature of QCD. If the octonionic non-associativity imposes gate-ordering constraints not visible in a naive SU(3) treatment, that would be a genuinely new prediction testable against lattice calculations.

---

## 3. Nucleon Physics as Multi-Register Quantum Computation

### 3.1 Proton (uud) = 9 qubits

Three 3-qubit registers: (A₁B₁C₁)(A₂B₂C₂)(A₃B₃C₃)

The C-qubits must form a colour singlet — a totally antisymmetric state:
(1/√6)(|rgb⟩ − |rbg⟩ + |brg⟩ − |bgr⟩ + |gbr⟩ − |grb⟩)

This is a specific GHZ-class entanglement across the three C-qubits, which **is** confinement in this language.

### 3.2 Neutron (udd) = 9 qubits

Same structure as proton, different A and B states on the third register.

### 3.3 Pion (meson, qq̄) = 6 qubits

Two 3-qubit registers. The C-qubits form a colour singlet as a 2-qubit Bell pair rather than a 3-qubit GHZ state.

### 3.4 Natural Factoring

The qubit counts factor naturally:
- 6 qubits = 2 × 3 = meson (two quarks)
- 9 qubits = 3 × 3 = baryon (three quarks)
- 18 qubits = 2 × 9 = deuteron (proton + neutron)

### 3.5 Compositional Completeness

The Coecke-Kissinger result guarantees this composition works: GHZ and W are the two primitive Frobenius algebras, and all multi-qubit entanglement classes can be built from compositions of these two primitives. Composing 3-qubit particles into hadrons, nuclei, and beyond is already licensed by the framework. The three-qubit terminus is sufficient, not limiting.

---

## 4. Comparison with Existing Approaches

The standard approach to quantum simulation of gauge theories (Zohar-Cirac-Reznik, Wiese, Bañuls et al.) starts from **lattice gauge theory** — discretising fields onto a lattice and then mapping that to qubits. It is fundamentally field-native.

The framework's approach is **particle-native**: particles already are qubit entanglement patterns, so the mapping to quantum hardware is direct rather than mediated through a lattice.

Advantages of the particle-native approach:
- Direct encoding: no lattice artefacts, no continuum limit needed
- Natural qubit budget: a proton is exactly 9 qubits, not a lattice of link variables
- Interactions are gates on identified qubits, not Trotter-decomposed Hamiltonian evolution
- Confinement is an entanglement constraint (C-qubit antisymmetry), not an emergent phenomenon from a large lattice

---

## 5. Specific Computations That Become Natural

### 5.1 Proton Structure

The 9-qubit proton state isn't just three quarks — the entanglement between the B-qubits across quarks encodes sea quarks and gluon content. Tracing out degrees of freedom from the full entangled state gives parton distribution functions from first principles. The entanglement entropy across different bipartite cuts of the 9-qubit system directly measures different aspects of proton structure.

### 5.2 Nuclear Binding

A deuteron (pn) is 18 qubits. The nuclear force between proton and neutron emerges from entanglement between their constituent quarks — pion exchange is a correlated gate sequence where a quark-antiquark pair is created and exchanged. The binding energy should relate to the entanglement entropy of the bipartite cut between the two 9-qubit registers.

### 5.3 Beta Decay (Showcase Calculation)

Start with 9 qubits in the neutron state. Apply the W-boson gate sequence to one d-quark's B-qubit. Introduce ancilla qubits for the electron and antineutrino. The final state is a 9-qubit proton register plus a 3-qubit electron and a 3-qubit antineutrino, with correct correlations enforced by the gate structure.

---

## 6. Planned Paper Structure

The paper has three acts:

**Act I — Fermions from topology**: Three Cayley-Dickson qubits with the Filatov constraint reproduce the Standard Model fermion content as a theorem. Takes the reader from basic concepts (Bloch sphere, Hopf fibrations, division algebras) to the complete fermion table. The contribution here is showing that the particle zoo is a classification theorem about entangled Bloch spheres, not an empirical list.

**Act II — Interactions as qubit operations**: Gauge interactions are operations on specific internal qubits. Every Feynman diagram translates into a quantum circuit. Photon = A-gate, W/Z = B-gate (with A-B mixing), gluon = C-gate. The Weinberg angle is a gate parameter. Non-associativity of octonions imposes circuit-ordering constraints on QCD.

**Act III — Nucleon physics as open problems**: Hadrons, nuclei, and scattering processes can be set up as multi-register quantum computations. This section presents concrete open problems for the quantum simulation community, rather than solving them. The paper's contribution is showing these problems exist in this form and are tractable with near-term quantum hardware.

### Open Problems for the Community

1. **Gluon exchange circuit**: Explicit gate decomposition for a single gluon exchange between two quarks inside a proton. Does octonionic non-associativity impose gate-ordering constraints beyond naive SU(3)? Testable against lattice QCD.

2. **Proton entanglement structure**: Compute the entanglement entropy across all bipartite cuts of the 9-qubit proton state. Do these reproduce known features of parton distribution functions?

3. **Beta decay circuit**: Full circuit implementation of n → p + e⁻ + ν̄ₑ with ancilla creation. Verify that quantum numbers are conserved by the gate structure.

4. **Confinement as entanglement monotone**: Is there an entanglement monotone on the C-qubit subsystem that characterises confinement? Does it remain constant under allowed (colour-singlet-preserving) operations?

5. **Meson spectrum from 6-qubit circuits**: Can the meson mass spectrum be reproduced from the entanglement structure of 6-qubit (qq̄) states with the geodesic mass formulas?

6. **Nuclear binding from inter-hadron entanglement**: For the deuteron (18 qubits), does the entanglement entropy of the proton-neutron bipartite cut relate to the binding energy?

7. **Non-perturbative QCD**: Can non-perturbative QCD phenomena (flux tubes, string breaking, chiral symmetry breaking) be recast as operations on the octonionic Hopf bundle topology?

8. **Comparison with lattice approach**: For processes where lattice QCD gives good results, does the particle-native encoding give equivalent answers with fewer qubits? What is the quantum advantage, if any?

---

## 7. Key Dependencies

This document builds on:
- `fermion_topology_table.py` — the complete fermion classification from three CD qubits
- `hopf_fibrations_research_summary.md` — the Hopf fibration / entanglement / Standard Model connection
- `conversation_summary_2026_03_12_session2.md` — GHZ/W classes, compositional completeness, chirality bootstrap
- `grounding_argument_gauge_group.md` — the gauge group derivation
- `fermion_topology_open_problems.md` — existing open problems list

Key external references:
- Coecke & Kissinger (2010) — compositional completeness of GHZ/W Frobenius algebras
- Szangolies (2025) — Standard Model symmetry from qubit entanglement
- Zohar, Cirac & Reznik (2015) — quantum simulation of lattice gauge theories (for comparison)
- Bañuls et al. (2020) — review of quantum simulation approaches to gauge theories

---

*Document Status: Active planning document for paper write-up. March 19, 2026.*
