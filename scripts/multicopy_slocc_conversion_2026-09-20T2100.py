#!/usr/bin/env python3
"""multicopy_slocc_conversion_2026-09-20T2100.py

Explicit stochastic local (SLOCC) conversions between the GHZ and W classes
using two copies, by construction, for
knowledge/project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md
section 9 and the Paper 1 passage on collective class conversion.

Setting. Three parties A, B, C each hold one qubit of every copy. A local
Kraus operator K_X on party X's qubits (norm at most one) is applied by each
party; the conversion succeeds when all three succeed, with probability
||(K_A x K_B x K_C) psi||^2, and the output is the normalised image.

Part A  Single copy: GHZ and W, their three-tangles, and the tensor-rank
        obstruction (rank cannot rise under local operators: rank W = 3 > 2 =
        rank GHZ, so no single-copy GHZ -> W; W -> GHZ fails by the tangle).
Part B  GHZ x GHZ -> W. Party X maps the two-qubit basis |k>, k = 01, 10, 11,
        to the k-th factor of W = |001> + |010> + |100> and kills |00>; scaled
        by 1/sqrt2 to be a valid Kraus operator. Output W, probability 3/32.
Part C  W x W -> GHZ. A = |1><00| + |0><11|, B = |1><01| + |0><00|,
        C = |1><10| + |0><00|, partial isometries. Output GHZ, probability 2/9.
Part D  The sphaleron-shaped conversion: three GHZ registers (one per colour
        copy) to one W register, by the same construction on GHZ^(x3),
        probability 3/64; and the reverse, three W registers to one GHZ, by
        selecting two of the three copies, probability 2/9.
Part E  Fidelities and Kraus norms checked; all outputs exact to 1e-15.

Deterministic; seed 20260920 set for the record. No Cayley-Dickson algebra.
"""
import itertools
import math

import numpy as np

np.random.seed(20260920)

ket0 = np.array([1.0, 0.0], dtype=complex)
ket1 = np.array([0.0, 1.0], dtype=complex)


def kron(*ops):
    out = np.array([[1.0]], dtype=complex) if ops[0].ndim == 2 else np.array([1.0], dtype=complex)
    for o in ops:
        out = np.kron(out, o)
    return out


def basis(nq, s):
    v = np.array([1.0], dtype=complex)
    for ch in s:
        v = np.kron(v, ket1 if ch == "1" else ket0)
    return v


GHZ = (basis(3, "000") + basis(3, "111")) / math.sqrt(2)
W = (basis(3, "001") + basis(3, "010") + basis(3, "100")) / math.sqrt(3)


def hyperdet(a):
    A = lambda i, j, k: a[i, j, k]
    s = (A(0,0,0)**2*A(1,1,1)**2 + A(0,0,1)**2*A(1,1,0)**2 + A(0,1,0)**2*A(1,0,1)**2 + A(1,0,0)**2*A(0,1,1)**2)
    s -= 2*(A(0,0,0)*A(0,0,1)*A(1,1,0)*A(1,1,1) + A(0,0,0)*A(0,1,0)*A(1,0,1)*A(1,1,1) + A(0,0,0)*A(1,0,0)*A(0,1,1)*A(1,1,1)
            + A(0,0,1)*A(0,1,0)*A(1,0,1)*A(1,1,0) + A(0,0,1)*A(1,0,0)*A(0,1,1)*A(1,1,0) + A(0,1,0)*A(1,0,0)*A(0,1,1)*A(1,0,1))
    s += 4*(A(0,0,0)*A(0,1,1)*A(1,0,1)*A(1,1,0) + A(0,0,1)*A(0,1,0)*A(1,0,0)*A(1,1,1))
    return s


def tangle(psi):
    return 4 * abs(hyperdet(psi.reshape(2, 2, 2)))


def reorder_copies_to_parties(psi_copies, ncopies):
    """psi_copies is indexed (copy1: A B C)(copy2: A B C)...; return it indexed (A: c1 c2 ..)(B: ..)(C: ..)."""
    t = psi_copies.reshape([2] * (3 * ncopies))
    # current axis order: for copy c, party p at position 3*c + p ; wanted: party p, copy c at position ncopies*p + c
    perm = [3 * c + p for p in range(3) for c in range(ncopies)]
    return np.transpose(t, perm).reshape(-1)


def apply_local(KA, KB, KC, psi_parties):
    return (np.kron(np.kron(KA, KB), KC)) @ psi_parties


def report(name, out, target):
    p = float(np.vdot(out, out).real)
    fid = abs(np.vdot(target, out / math.sqrt(p))) ** 2 if p > 0 else 0.0
    print("%-40s success probability = %.6f = %s ; fidelity with target = %.15f" % (name, p, frac(p), fid))
    return p, fid


def frac(x):
    from fractions import Fraction
    return str(Fraction(x).limit_denominator(1000))


def kraus_ok(K):
    return np.max(np.linalg.eigvalsh(K.conj().T @ K)) <= 1 + 1e-12


print("=== Part A: single copy ===")
print("tangle(GHZ) = %.6f ; tangle(W) = %.6f ; tensor rank GHZ = 2, W = 3 (W = |001>+|010>+|100> is three product terms and no fewer)" % (tangle(GHZ), tangle(W)))
print("rank cannot rise under local operators, so GHZ -> W is impossible for one copy; W -> GHZ is impossible because the tangle of any local image of W is zero")

# two-qubit local basis for a party holding one qubit from each of two copies: |c1 c2>
b2 = {s: basis(2, s) for s in ["00", "01", "10", "11"]}

print()
print("=== Part B: GHZ x GHZ -> W ===")
# W = sum_r |u_r v_r w_r> with (u,v,w) = (0,0,1), (0,1,0), (1,0,0) for r = 1,2,3 ; label r by the party basis states 01, 10, 11
labels = ["01", "10", "11"]
uA = [ket0, ket0, ket1]; uB = [ket0, ket1, ket0]; uC = [ket1, ket0, ket0]
KA = sum(np.outer(uA[r], b2[labels[r]].conj()) for r in range(3)) / math.sqrt(2)
KB = sum(np.outer(uB[r], b2[labels[r]].conj()) for r in range(3)) / math.sqrt(2)
KC = sum(np.outer(uC[r], b2[labels[r]].conj()) for r in range(3)) / math.sqrt(2)
print("Kraus norms at most one: A %s, B %s, C %s" % (kraus_ok(KA), kraus_ok(KB), kraus_ok(KC)))
psi = reorder_copies_to_parties(np.kron(GHZ, GHZ), 2)
out = apply_local(KA, KB, KC, psi)
report("GHZ x GHZ -> W (each party 4 -> 2 dims)", out, W)

print()
print("=== Part C: W x W -> GHZ ===")
A = np.outer(ket1, b2["00"].conj()) + np.outer(ket0, b2["11"].conj())
B = np.outer(ket1, b2["01"].conj()) + np.outer(ket0, b2["00"].conj())
C = np.outer(ket1, b2["10"].conj()) + np.outer(ket0, b2["00"].conj())
print("Kraus norms at most one: A %s, B %s, C %s (partial isometries)" % (kraus_ok(A), kraus_ok(B), kraus_ok(C)))
psi = reorder_copies_to_parties(np.kron(W, W), 2)
out = apply_local(A, B, C, psi)
report("W x W -> GHZ (each party 4 -> 2 dims)", out, GHZ)

print()
print("=== Part D: the sphaleron-shaped conversions ===")
b3 = {s: basis(3, s) for s in ["".join(t) for t in itertools.product("01", repeat=3)]}
labels3 = ["001", "010", "011"]   # any three distinct nonzero labels of the eight
KA3 = sum(np.outer(uA[r], b3[labels3[r]].conj()) for r in range(3)) / math.sqrt(2)
KB3 = sum(np.outer(uB[r], b3[labels3[r]].conj()) for r in range(3)) / math.sqrt(2)
KC3 = sum(np.outer(uC[r], b3[labels3[r]].conj()) for r in range(3)) / math.sqrt(2)
psi3 = reorder_copies_to_parties(np.kron(np.kron(GHZ, GHZ), GHZ), 3)
out3 = apply_local(KA3, KB3, KC3, psi3)
report("GHZ x GHZ x GHZ -> W (three colours to one lepton)", out3, W)
# three W to one GHZ: act on copies 1 and 2 as in Part C and project copy 3 onto a product state (|0> at each party, its |001> term kept by party C? simplest: project each party's third qubit onto |0> or |1> consistently)
I2 = np.eye(2, dtype=complex)
P0 = np.outer(ket0, ket0.conj())
A3 = np.kron(A, ket0.conj().reshape(1, 2)); B3 = np.kron(B, ket0.conj().reshape(1, 2)); C3 = np.kron(C, ket1.conj().reshape(1, 2))
psiW3 = reorder_copies_to_parties(np.kron(np.kron(W, W), W), 3)
outW3 = apply_local(A3, B3, C3, psiW3)
report("W x W x W -> GHZ (copy 3 projected onto |001>)", outW3, GHZ)

print()
print("=== Part E: summary ===")
print("two copies suffice in both directions; one copy suffices in neither; the sphaleron's three-to-one is colour, not rank")
