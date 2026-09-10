# Glueballs in the ZX-Calculus / Quantum Circuit Picture

**Date:** 2026-05-03

## 1. Setup

In the framework, a gluon is a Bell-class entanglement on the C-qubit (octonionic) level. The eight gluon types correspond to the eight SU(3) generators acting on the colour triplet. In a typical Feynman process the gluon is the Bell pair connecting one quark's C-qubit to another's — it lives *between* two fermion registers, never on its own.

Gluon action is captured by the long-root coset structure of G₂: the cycle [3, 3̄] → 8 → 3 (quark emits gluon, gluon absorbed by quark) is the gauge interaction. That cycle never closes inside the adjoint alone — which is exactly where glueballs become interesting.

## 2. The Structural Problem

Glueballs are pure gluon bound states with no valence quarks. In framework language: a network of Bell pairs on C-qubits with no external fermion registers to terminate on. The network has to close on itself.

Two readings, both worth keeping:

**(a) Gluons carry the C-qubits themselves.** Each gluon, considered as a propagating particle, carries a colour-anticolour pair — two C-qubits in a Bell-class entanglement, with content in the adjoint 8. A glueball is a network of these Bell pairs joined so the *outer* endpoints contract to a singlet.

**(b) Glueballs require self-FANOUT.** Quarks produce classical colour records because GHZ is special Frobenius (has FANOUT). Gluons individually cannot — Bell pairs are not SCFAs in the colour sector. For a glueball to be a real, classically detectable bound state, the gluon network must *generate* SCFA structure through its closure topology. You're asking the network's geometry to do what a quark trio does for free.

## 3. ZX Diagrams

### 3.1 Two-gluon glueball (J^PC = 0++ candidate)

Four C-qubits as two Bell pairs, four external wires contracted pairwise into a singlet — a "bubble":

```
   ┌─── Bell ───┐
   │            │
 [ g₁ ]      [ g₂ ]
   │            │
   └─── Bell ───┘
```

By the spider theorem this collapses to a scalar amplitude; the SU(3) trace structure (singlet projector) makes it non-trivial. Lattice QCD identifies this as the lightest glueball at ~1.7 GeV.

### 3.2 Three-gluon glueball (K₃ topology)

```
        [g₁]
        /  \
       /    \
     [g₃]──[g₂]
```

Three gluons connected as a triangle — three C-qubit Bell pairs joined by SU(3) structure constants. **The topology is K₃: the same complete graph on three vertices that is not 2-colourable** — the obstruction that generates three fermion generations.

A structural prediction drops out: **three-gluon glueballs should inherit a triality structure from the same K₃ obstruction.** The four resolution classes of K₃ (three "frustrated pair" classes + all-same) become four C-parity / channel classes for ggg glueballs. Standard QCD knows about two singlet couplings (d^abc symmetric, f^abc antisymmetric) — the framework predicts more structure than that. Worth checking against lattice spectra.

## 4. Proposed Calculation

Encode an n-gluon glueball as a 2n-qubit C-register in Qiskit:
- Each gluon as a Bell pair on two C-qubits
- Outer endpoints projected onto the SU(3) singlet via a Frobenius structure
- Network closed according to the chosen topology

Observables:
1. **Closed-network amplitude** (the scalar the diagram collapses to) — glueball decay constant
2. **Topology class** of the closure — predicts J^PC
3. **Mass from internal entanglement geometry** — same machinery as meson masses, but on C-only registers, no A/B activity

The lightest glueball mass should come out as the geodesic length of the simplest closed C-Bell network. Mesons use 6-qubit (qq̄) entanglement; glueballs use 4-qubit (gg) C-only entanglement — structurally simpler but living entirely in the long-root coset.

## 5. Status of the Claims

**Solid.**
- Gluons as Bell pairs on C-qubits
- Glueballs as closed C-only Bell-pair networks
- The requirement that the network's topology supply its own singlet closure
- 2-gluon glueball as the simplest closed loop

**Plausible but needs work.**
- K₃ → triality inheritance for ggg glueballs. The structural parallel is suggestive but the SU(3) projection may wash it out — needs verification.

**Speculative.**
- The lightest glueball mass can be predicted from the same geodesic-length machinery as mesons. Plausible because the C-qubit geometry is the same, but the absence of A/B activity changes the relevant fibre.

## 6. Why This Matters for the Paper

If the geodesic-length formula on C-only Bell networks predicts m(0++) ≈ 1.7 GeV using the same single dimensional parameter that fixes the rest of the spectrum, that is a clean zero-dimensionless-parameter postdiction in a sector lattice QCD has worked hard to nail down.

It also extends the entanglement-class ↔ particle dictionary into the gauge-only sector. The current dictionary covers fermions (GHZ + W) and Higgs (product state); gauge bosons appear as Bell-pair *channels* between fermion registers. Glueballs are the test case for whether the framework can describe gauge-boson *bound states* — composites built from the Bell-pair channel itself, with no fermion content.

## 7. Connection to Existing Open Problems

- **Meson exchange from colour singlet constraint** (qubits_circuits_nucleon_physics.md, Open Problem 6): the same machinery — what closed networks can be passed between hadrons — applies here. Glueballs are the simpler test case (no quark content to track).
- **Frobenius–Bracket correspondence** (g2_roots_ghz_w_quark_lepton_v2): glueballs are a direct probe of long-root coset closure properties. A successful glueball calculation would be evidence for the broader functorial conjecture.
- **Hopf–Frobenius functor** (open_problem_hopf_frobenius.md): glueballs sit in the C-qubit-only sector, so any geometric statement about them lifts cleanly to a statement about the octonionic Hopf bundle restricted to its fibre structure.

## 8. Next Steps

1. Write out the explicit ZX diagram for the 2-gluon glueball with the SU(3) singlet projector spelled out as a Frobenius spider on the colour indices.
2. Implement the 4-qubit Qiskit circuit, compute the closed-network amplitude, check it's non-zero and SU(3)-singlet.
3. Apply the geodesic-length mass formula to the 4-qubit closed network and compare to lattice QCD m(0++) ≈ 1.7 GeV.
4. If (3) works, repeat for the 6-qubit ggg case and use the K₃ topology classes to predict J^PC for the next glueball multiplet.

---

*End of summary.*
