# Building Quantum Circuits for Particle Interactions — A Hands-On Manual

**Who this is for.** Anyone who wants to try these circuits, especially using an LLM to write the
Qiskit code. Read *From Hopf Fibrations to Quantum Circuits — Context* first: it explains why the
circuits look the way they do. Then paste both documents to your LLM and build from §5 onward.
Everything here runs on a laptop with `qiskit` installed; no quantum hardware is required for any
result in this manual, and every computation comes with its expected answer so you can tell
immediately whether your code is right.

## 1. Ground rules (for you and your LLM)

1. **These circuits compute structure, not dynamics.** They give selection rules, conservation
   laws, entanglement bookkeeping and interference structure. They do **not** give rates,
   cross-sections, propagators, loop corrections, running couplings, or anything like the
   electron's magnetic moment — and the framework claims no deviation from standard QED on any such
   quantity. If your LLM starts adding Hamiltonians, "time evolution", or decay rates, stop it.
2. **Hand-derive first, then run.** Every expected output below was computed on paper before it was
   coded. Have your LLM state the expected result before executing, and plant assertions that fail
   loudly. Twice in this project a code/derivation disagreement caught a wiring bug — and once it
   caught a *discovery* (see §9). Both times the assertion did the work.
3. **Respect status.** Some claims are theorems, some are structural identifications, some are open
   problems (the context document flags each). A result your code produces is "verified for the
   encoded case", never "proved", unless a proof exists.
4. **Simulator first.** Statevector simulation is exact and free; hardware adds noise and queues.
   Every expected number below is a statevector fact; the hardware figures quoted are calibration
   points from real runs, not requirements.

## 2. Encoding conventions

- **One fermion = three wires**: qubit A (hypercharge), qubit B (weak isospin), qubit C (colour).
  Particles created mid-process enter as fresh wires initialised to |0⟩. Time runs left to right.
- **Circuit amplitudes are internal-structure factors**: the gauge/generation part of a process
  amplitude, with no propagator or phase-space factors (those belong to a layer these circuits do
  not model).
- **Qubit ordering:** Qiskit is little-endian (qubit 0 is the rightmost bit of a basis label).
  Fix a convention at the top of every notebook, print a one-qubit smoke test, and never trust
  positional bookkeeping after a contraction — see §9.

Canonical states (unnormalised):
GHZ = |000⟩+|111⟩; W = |001⟩+|010⟩+|100⟩; Bell Φ⁺ = |00⟩+|11⟩; singlet Ψ⁻ = |01⟩−|10⟩;
product = |000⟩. Compute on these canonical states — the framework's invariants are sharp exactly
there.

## 3. The gate dictionary

| Boson | Acts on | Gate |
|---|---|---|
| photon γ | A (and B, via Q) | phase e^{iφQ}, with Q = T₃ + ½Y |
| Z | A–B jointly | phase e^{iθ(¾T₃ − ⅛Y)} (tree value of the mixing angle) |
| W± | B | X (isospin raise/lower); two-generation form: X ⊗ R_y(2·(2/9)) on a generation qubit |
| gluon | C | SU(3) rotation (single-qubit stand-in: any local unitary on C) |
| Higgs | doublet ↔ singlet | chirality-flip connector within one generation |

**Z-phase anchors** — the θ-coefficient per species. If your Z gate does not reproduce this table,
the gate is wrong, not the table (these equal the textbook T₃ − Q sin²θ_W at sin²θ_W = ¼):

| species | T₃ | Y | ¾T₃ − ⅛Y |
|---|---|---|---|
| ν | +½ | −1 | **+½** |
| e | −½ | −1 | **−¼** |
| u | +½ | +⅓ | **+⅓** |
| d | −½ | +⅓ | **−5/12** |

**A free sanity check, guaranteed by theorem:** every neutral gate above is either diagonal in the
computational basis (γ, Z) or a single-qubit unitary (gluon). Consequently *no composition of
neutral gates can change a register's entanglement class* — GHZ stays GHZ, W stays W, product stays
product. If a neutral-gates-only run changes a class or moves the three-tangle off its class value,
you have a wiring bug with certainty.

**Coupling normalisations:** the electroweak *ratio* is fixed (g′/g = 1/√3) and the Higgs gate's
strengths are the Yukawa couplings, but overall normalisations are an open problem — which is why
the circuits compare structures and ratios, never absolute rates.

## 4. Fusion: the one non-unitary move

Hadron vertices use the "copy fusion" μ: |xy⟩ ↦ δ_xy |x⟩ — two wires in, one out, keeping only the
agreeing components. This is a **post-selected isometry, not a unitary**. On a statevector, apply
the 2→1 tensor and renormalise, **reporting the pre-normalisation norm² as the success
probability**; on hardware, implement as CNOT + measure + post-select. The success probabilities
are physics, not bugs: the fully closed baryon triangle fuses at exactly **1/4**; a single vertex
fusion at exactly **1/2**. A "fidelity 1" with the wrong success weight means the wiring is wrong.

Closed-triangle wiring (labels matter): three Bell edges AB = (a1,b1), BC = (b2,c1), CA = (c2,a2);
vertices fuse A:(a2,a1), B:(b1,b2), C:(c1,c2).

## 5. Starter code patterns

Pure-Python statevector route — exact, no hardware, no account needed. Give these to your LLM as
the house style:

```python
import numpy as np

B  = np.array([1,0,0,1], complex)/np.sqrt(2)      # |Phi+>
Bm = np.array([0,1,-1,0], complex)/np.sqrt(2)     # |Psi->
GHZ = np.zeros(8, complex); GHZ[0] = GHZ[7] = 1/np.sqrt(2)
W   = np.zeros(8, complex); W[[1,2,4]] = 1/np.sqrt(3)

mu = np.zeros((2,2,2)); mu[0,0,0] = 1; mu[1,1,1] = 1   # copy fusion

class Net:                                          # label-tracked tensor network
    def __init__(s, vec, labels): s.t = vec.reshape([2]*len(labels)); s.lab = list(labels)
    def fuse(s, a, b, new):                         # fuse wires a,b -> new (post-selected!)
        ia, ib = s.lab.index(a), s.lab.index(b)
        s.t = np.tensordot(mu, np.moveaxis(s.t, [ia, ib], [0, 1]), axes=([0,1],[0,1]))
        s.lab = [new] + [x for x in s.lab if x not in (a, b)]
        return s
    def vec(s, order):
        return np.moveaxis(s.t, [s.lab.index(l) for l in order], range(len(order))).reshape(-1)

def rho(psi, keep, n):                              # reduced density matrix
    psi = psi.reshape([2]*n); ax = [i for i in range(n) if i not in keep]
    r = np.tensordot(psi, psi.conj(), axes=(ax, ax))
    return r.reshape(2**len(keep), 2**len(keep))
```

Qiskit route for circuit-shaped work (still exact, still local):

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace

qc = QuantumCircuit(3)
qc.h(0); qc.cx(0, 1); qc.cx(1, 2)                  # GHZ
psi = Statevector(qc)
```

Optional-hardware guard, so notebooks never die at an authentication cell:

```python
RUN_HARDWARE = False
if RUN_HARDWARE:
    try:
        from qiskit_ibm_runtime import QiskitRuntimeService
        service = QiskitRuntimeService()
    except Exception as e:
        print(f"hardware unavailable ({e}); continuing on local simulation")
        RUN_HARDWARE = False
```

## 6. Computations and their expected results

Reproduce these in order; each takes minutes. If your result disagrees, suspect wiring before
physics — every row is hand-derived and machine-verified, and the flagged rows were also run on IBM
Heron-class hardware (June 2026).

| Computation | Expected result |
|---|---|
| Beta decay (active quark: X on B; W → lepton Bell pair on fresh wires) | output supported on exactly two basis states; either lepton wire's reduced state maximally mixed; charge, colour, B and L conserved by wiring alone |
| GHZ ∘ GHZ (copy fusion of two GHZ₃ nodes) | fidelity with GHZ₄ = **1.000000** |
| W ∘ W | fidelity with W₄ = **0.000000** |
| W triangle (three W nodes closed) | fidelity with W₃ = **0.75** — does not close |
| Baryon triangle (three Bell edges, three fusions) | output **exactly GHZ₃**, success **1/4** (hardware: populations 0.925, parity +0.837, two-setting fidelity ≈ 0.88) |
| One vertex fused only | **exactly GHZ₃ ⊗ Bell**, success **1/2** |
| Meson (two-edge loop) | closes onto the **canonical Bell pair** |
| Two-gluon open network | returns a **Bell pair**, not a copy structure |
| Two-generation W gate: X ⊗ R_y(2·2/9) | \|V_ud\| = cos(2/9) = 0.97541 (**+0.11%** vs measured); \|V_us\| = sin(2/9) = 0.22040 (**−1.74%**) |
| GHZ–W interference (mix a small W amplitude into GHZ; track the Bloch radius of a cut) | response is **first order** in the admixture (a 2% amplitude moves the invariant ~**17×** more than incoherent mixing) and **phase-rigid** |

## 7. Two richer projects

**(a) The confinement budget, and an exact trade-off.** Show that the colour singlet (canonical
GHZ₃) has three-tangle τ₃ = 1 with both pairwise tangles exactly zero; then couple one qubit to an
external qubit D and watch confinement resist. Reference family:
|ψ(θ)⟩ = [cos θ·𝟙 + i sin θ·(X_{q1} ⊗ X_D)] (GHZ ⊗ |0⟩_D), for θ ∈ [0, π/4].
Expected: the GHZ fidelity of the triple falls as F = cos²θ from 1 to 1/2 while the entanglement
entropy of D rises from 0 to 1 — monotone lockstep, and in fact **exact**:
**S_D = H₂(F)**, the binary entropy of the fidelity, to machine precision.
*Witness warning:* the pairwise concurrence between q1 and D is the wrong witness (the environment
decoheres it to ~0 throughout, and at θ = π/2 the coupling is merely a local unitary). Use the cut
entropy S_D, on θ ∈ [0, π/4].

**(b) Glueball orientation classes.** Build the three-edge triangle but let each edge be either
Φ⁺ (aligned) or Ψ⁻ (flipped), giving 8 edge patterns; contract with the plain copy fusion at all
three vertices. Expected: patterns with an **even** number of flips transmit at probability **1/4**
each; all odd patterns **annihilate** (the fusion enforces the triangle's cycle parity by itself,
and the four even patterns are exactly the ones a consistent vertex orientation can produce). The
four transmitted outputs are **mutually orthogonal** GHZ-type pair states, and the map is
geometric: all-aligned → |000⟩+|111⟩; one aligned edge → the pair state with the qubit **opposite
that edge** flipped (aligned AB → flip C; aligned BC → flip A; aligned CA → flip B). Bonus checks:
any odd pattern transmits (at 1/4) if you first apply a single Y "antipode" to one leg of **any**
edge — position-free; and with explicit Gell-Mann matrices, verify the colour-side identity
Tr(TᵃTᵇTᶜ) ± Tr(TᵃTᶜTᵇ) = ½d^{abc}, ½if^{abc} — the two three-gluon couplings of QCD as the even
and odd parts of one trace read in its two cyclic orders.

**(c) The absent gate (species conservation as a missing unitary).** GHZ and W are
SLOCC-inequivalent, but a single global unitary — a quarter rotation in their two-dimensional span,
or constructively (W-preparation) ∘ (GHZ-preparation)⁻¹ — converts them exactly and reversibly.
Build it and verify: fidelity 1 in both directions; the ledger flip (τ₃: 1 ↔ 0; pairwise tangles:
0 ↔ 4/9; one-to-rest: 1 ↔ 8/9; single-qubit marginals: I/2 ↔ spectrum (2/3, 1/3)); and that τ₃ > 0
at every interior point of the rotation — the W class sits on the boundary of the GHZ orbit's
closure. The converter is non-Clifford and needs entangling gates among all three qubits. On
hardware: prepare GHZ (H + two CNOTs), apply the compiled converter, read the W signatures
(population on {001, 010, 100} summing to 1, plus a coherence witness). Physics reading, for
context: in the particle dictionary of the companion document this gate is a quark↔lepton
(leptoquark) vertex, and no force in the framework stocks it — building it in a laboratory is a
demonstration of exactly the operation whose absence in nature is baryon and lepton number
conservation.

## 8. What these circuits can and cannot do

**Can:** selection rules; conservation laws by wiring (charge via Q = T₃ + ½Y, colour, baryon and
lepton number); entanglement-class bookkeeping before and after any gate sequence; interference
structure; fusion and contraction results with their success probabilities; per-cent-level *ratio*
tests such as the Cabibbo comparison.

**Cannot (do not attempt, do not let your LLM imply):** numerical rates or cross-sections;
propagators, phase space, loop integrals, renormalisation, coupling running; the anomalous magnetic
moment or any dynamical QED/QCD quantity; absolute masses in physical units (one scale in the
framework is a free parameter by design); anything that would require converting a network length
into MeV. When a request crosses the line, the correct answer is that the line exists.

## 9. Debug playbook

- **Track labels through every contraction.** A positional (`moveaxis`-index) fusion once
  contracted the wrong pair of legs — and the final check *still passed*, because GHZ is
  permutation-symmetric; only an intermediate check exposed it. Use the label-tracked `Net` pattern
  of §5 and verify intermediate states, not just endpoints.
- **Plant assertions, and read failures before "fixing" them.** An assertion that "every
  transmitted output is GHZ" failed — and the failure was the *discovery* that the four classes
  transmit to four orthogonal states. A failing assertion is information.
- **Right witness, right range.** See project (a): concurrence versus cut entropy, and parameter
  values where a coupling degenerates into a local unitary.
- **Account for success probability.** Post-selected fusions carry physical weights (1/4, 1/2); a
  renormalised state with an unexamined pre-norm is a silent error.
- **Endianness.** One-qubit smoke test before any multi-register run.
- **Global phases** are never observable and never bugs; relative phases within a register are.

## 10. Numerical anchor sheet

δ = 2/9 rad ≈ 12.73°; cos(2/9) = 0.97541; sin(2/9) = 0.22040. Koide phase dilution: δ/n with
n = 1, 2, 3 for leptons, down-type, up-type. α² = 2 (leptons), 2.3849 (down), 3.0887 (up).
sin²θ_W = ¼ (tree) → 0.2312 (MS-bar at M_Z) → 0.22305 (on-shell); mass-ratio chain
0.8660 → 0.8768 → 0.88145. v = 246.220 GeV; v/2 = 123.11; v/√2 = 174.10; matching scale ≈ 3.6 TeV.
Fusion successes: 1/4 (full triangle), 1/2 (one vertex). Class transmission: 1/4 each.
Z-phase coefficients: +½ (ν), −¼ (e), +⅓ (u), −5/12 (d).

---
The open problems are real and stated openly in the context document; these circuits are the
handles the framework offers for gripping them. If a run of yours disagrees with §6 or §7, the
smart money is on wiring — and if, after honest checking, it still disagrees, that is exactly the
kind of information the whole approach exists to surface.
