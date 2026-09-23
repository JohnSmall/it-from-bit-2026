#!/usr/bin/env python3
"""qiskit_multicopy_slocc_circuit_2026-09-20T2100.py

Qiskit circuits for the two-copy GHZ/W conversions of
scripts/multicopy_slocc_conversion_2026-09-20T2100.py, as postselected local
operations (SLOCC = local unitaries + local measurements + keep the run only if
every party's flag reads 0).

Circuit 1  W x W -> GHZ. Six qubits: party A holds (a1, a2), B (b1, b2), C
           (c1, c2); W is prepared on (a1, b1, c1) and on (a2, b2, c2). Each party
           applies a permutation of its two-qubit basis and keeps the run if its
           second qubit reads 0; the output is (a1, b1, c1). Expected success 2/9.
Circuit 2  GHZ x GHZ -> W. As above plus one ancilla per party: a local unitary
           sends the kept subspace to (q2 = 0), a controlled-RY(pi/2) from q1 onto
           the ancilla supplies the 1/sqrt2 weight on the q1 = 1 branch, and the
           run is kept if q2 = 0 and the ancilla reads 0. Expected success 3/32.

Both are checked two ways: exactly, by projecting the final statevector onto
the kept flags (probability and fidelity), and by sampling on Aer with a fixed
seed, reporting the kept fraction and the output distribution in the
computational basis (GHZ: only 000 and 111; W: only 001, 010, 100).

Seed 20260920 for the sampler. Qiskit 2.5.2, qiskit-aer 0.17.2.
"""
import math
from collections import Counter

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator, Statevector
from qiskit_aer import AerSimulator

SEED = 20260920
SQ2 = math.sqrt(2.0)


def perm_unitary(mapping):
    """2-qubit unitary from a basis permutation written in (q1 q2) order, for use as
    qc.append(gate, [q1, q2]); Qiskit's little-endian order puts q1 as the low bit."""
    U = np.zeros((4, 4), dtype=complex)
    for src, dst in mapping.items():
        i = int(src[0]) + 2 * int(src[1])
        j = int(dst[0]) + 2 * int(dst[1])
        U[j, i] = 1.0
    assert np.allclose(U.conj().T @ U, np.eye(4))
    return UnitaryGate(U)


def basis_unitary(kept_pair, target_labels):
    """2-qubit unitary sending the two kept vectors (given as dicts label->amplitude in
    (q1 q2) order) to the basis states target_labels (in (q1 q2) order) and the
    orthogonal complement to states with q2 = 1."""
    def vec(d):
        v = np.zeros(4, dtype=complex)
        for lab, amp in d.items():
            v[int(lab[0]) + 2 * int(lab[1])] = amp
        return v / np.linalg.norm(v)
    ins = [vec(d) for d in kept_pair]
    # complete to an orthonormal basis (Gram--Schmidt on the standard basis)
    basis_vecs = list(ins)
    for k in range(4):
        e = np.zeros(4, dtype=complex); e[k] = 1.0
        for b in basis_vecs:
            e = e - np.vdot(b, e) * b
        if np.linalg.norm(e) > 1e-9:
            basis_vecs.append(e / np.linalg.norm(e))
    assert len(basis_vecs) == 4
    outs = []
    for lab in target_labels:
        v = np.zeros(4, dtype=complex); v[int(lab[0]) + 2 * int(lab[1])] = 1.0
        outs.append(v)
    for lab in ["01", "11"]:  # complement goes to q2 = 1
        v = np.zeros(4, dtype=complex); v[int(lab[0]) + 2 * int(lab[1])] = 1.0
        outs.append(v)
    U = sum(np.outer(o, i.conj()) for o, i in zip(outs, basis_vecs))
    assert np.allclose(U.conj().T @ U, np.eye(4))
    return UnitaryGate(U)


def prepare_w(qc, qubits):
    w = np.zeros(8, dtype=complex)
    for lab in ["001", "010", "100"]:
        w[int(lab, 2)] = 1 / math.sqrt(3)
    qc.prepare_state(Statevector(w), qubits)


def prepare_ghz(qc, qubits):
    qc.h(qubits[0]); qc.cx(qubits[0], qubits[1]); qc.cx(qubits[0], qubits[2])


def exact_check(qc, out_qubits, flag_qubits, target):
    sv = Statevector(qc).data
    n = qc.num_qubits
    t = sv.reshape([2] * n)             # axes ordered q_{n-1} ... q_0
    idx = [slice(None)] * n
    for f in flag_qubits:
        idx[n - 1 - f] = 0
    kept = t[tuple(idx)]
    # remaining axes correspond to the non-flag qubits in descending index order
    remaining = [q for q in range(n - 1, -1, -1) if q not in flag_qubits]
    prob = float(np.sum(np.abs(kept) ** 2))
    # bring output qubits to order (out[0], out[1], out[2]) as the high..low bits of a 3-qubit label
    perm = [remaining.index(q) for q in out_qubits]
    kept = np.transpose(kept, perm + [i for i in range(len(remaining)) if i not in perm]).reshape(8, -1)
    # the non-output, non-flag qubits (none here) would be traced; here kept is 8 x 1
    vec = kept[:, 0] / math.sqrt(prob)
    fid = abs(np.vdot(target, vec)) ** 2
    return prob, fid


def sample(qc, out_qubits, flag_qubits, shots=40000):
    n = qc.num_qubits
    meas = qc.copy()
    meas.measure_all()
    sim = AerSimulator(seed_simulator=SEED)
    counts = sim.run(transpile(meas, sim, seed_transpiler=SEED), shots=shots).result().get_counts()
    kept = Counter(); total_kept = 0
    for bits, c in counts.items():
        b = bits[::-1]  # b[q] is the outcome of qubit q
        if all(b[f] == "0" for f in flag_qubits):
            total_kept += c
            kept["".join(b[q] for q in out_qubits)] += c
    return total_kept / shots, {k: v / total_kept for k, v in sorted(kept.items())}


GHZ3 = np.zeros(8, dtype=complex); GHZ3[0] = GHZ3[7] = 1 / SQ2
W3 = np.zeros(8, dtype=complex)
for lab in ["001", "010", "100"]:
    W3[int(lab, 2)] = 1 / math.sqrt(3)

# ---------------------------------------------------------------- circuit 1
print("=== Circuit 1: W x W -> GHZ (postselected local permutations) ===")
a1, a2, b1, b2, c1, c2 = range(6)
qc = QuantumCircuit(6)
prepare_w(qc, [a1, b1, c1]); prepare_w(qc, [a2, b2, c2])
qc.append(perm_unitary({"11": "00", "00": "10", "01": "01", "10": "11"}), [a1, a2])   # A = |1><00| + |0><11| on the kept subspace
qc.append(perm_unitary({"00": "00", "01": "10", "10": "01", "11": "11"}), [b1, b2])   # B = |1><01| + |0><00|
# C = |1><10| + |0><00| : identity, keep c2 = 0
prob, fid = exact_check(qc, [a1, b1, c1], [a2, b2, c2], GHZ3)
print("exact: success probability = %.6f (2/9 = %.6f) ; fidelity of the kept output with GHZ = %.12f" % (prob, 2 / 9, fid))
kept_frac, dist = sample(qc, [a1, b1, c1], [a2, b2, c2])
print("Aer, 40000 shots, seed %d: kept fraction = %.4f ; output distribution on (a1 b1 c1): %s" % (SEED, kept_frac, {k: round(v, 4) for k, v in dist.items()}))
print("depth after transpile to Aer: %d" % transpile(qc, AerSimulator(), seed_transpiler=SEED).depth())

# ---------------------------------------------------------------- circuit 2
print()
print("=== Circuit 2: GHZ x GHZ -> W (postselected local unitaries with an ancilla weight) ===")
a1, a2, b1, b2, c1, c2, xa, xb, xc = range(9)
qc = QuantumCircuit(9)
prepare_ghz(qc, [a1, b1, c1]); prepare_ghz(qc, [a2, b2, c2])
# party A keeps s = (|01>+|10>)/sqrt2 -> |0>, |11> -> |1> (weight 1/sqrt2)
qc.append(basis_unitary([{"01": 1, "10": 1}, {"11": 1}], ["00", "10"]), [a1, a2])
# party B keeps (|01>+|11>)/sqrt2 -> |0>, |10> -> |1>
qc.append(basis_unitary([{"01": 1, "11": 1}, {"10": 1}], ["00", "10"]), [b1, b2])
# party C keeps (|10>+|11>)/sqrt2 -> |0>, |01> -> |1>
qc.append(basis_unitary([{"10": 1, "11": 1}, {"01": 1}], ["00", "10"]), [c1, c2])
for q, x in [(a1, xa), (b1, xb), (c1, xc)]:
    qc.cry(math.pi / 2, q, x)      # amplitude cos(pi/4) = 1/sqrt2 stays on ancilla |0> when q1 = 1
prob, fid = exact_check(qc, [a1, b1, c1], [a2, b2, c2, xa, xb, xc], W3)
print("exact: success probability = %.6f (3/32 = %.6f) ; fidelity of the kept output with W = %.12f" % (prob, 3 / 32, fid))
kept_frac, dist = sample(qc, [a1, b1, c1], [a2, b2, c2, xa, xb, xc])
print("Aer, 40000 shots, seed %d: kept fraction = %.4f ; output distribution on (a1 b1 c1): %s" % (SEED, kept_frac, {k: round(v, 4) for k, v in dist.items()}))
print("depth after transpile to Aer: %d" % transpile(qc, AerSimulator(), seed_transpiler=SEED).depth())
print()
print("both conversions are local: every gate after preparation acts within one party's qubits, and the only communication is the classical decision to keep the run")
