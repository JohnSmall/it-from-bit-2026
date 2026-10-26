#!/usr/bin/env python3
"""complexified_vs_complex_structure_2026-09-27T1400.py

JS (2026-09-27): "we always use complexified quaternions, complexified
octonions and complexified sedenions. Is that correct?" Two facts that decide
the wording.

Part A  Dimensions. The n-qubit Hilbert space C^(2^n) has the complex
        dimension of C (x) A_n (the complexification of the n-th Cayley-Dickson
        algebra) and the real dimension of A_(n+1) (the next algebra, viewed
        with a complex structure). Adding a qubit is one doubling either way.
Part B  Complexification destroys the division property. In C (x) H and
        C (x) O, with the Cayley-Dickson product extended C-bilinearly and the
        C-bilinear norm N(x) = sum x_i^2 (not the Hermitian norm), the element
        x = 1 + i e_1 has N(x) = 0 and x xbar = 0: a zero divisor. The real
        algebras H and O have none (norm composition holds exactly); the real
        sedenions S do (the corpus's zero divisors).
Part C  The framework's identification is the other one: C^4 = O as a real
        8-space with the complex structure "left multiplication by e_1"
        (lem:cproj), so the octonionic norm composition used in the paper is
        the real algebra's, and the complex amplitude's Hermitian norm is the
        real Euclidean norm of the same 8-vector. Checked on random states.

Convention A throughout: (a,b)(c,d) = (ac - conj(d) b, da + b conj(c)).
Seed 20260927. numpy only.
"""
import math

import numpy as np

rng = np.random.default_rng(20260927)


def conj(x):
    y = np.array(x, copy=True); y[1:] = -y[1:]; return y


def cd(x, y):
    n = x.size
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate((cd(a, c) - cd(conj(d), b), cd(d, a) + cd(b, conj(c))))


def N_bilinear(x):
    return np.sum(x * x)          # C-bilinear norm, no complex conjugation of coefficients


print("=== Part A: dimensions ===")
print("%6s %14s %20s %22s" % ("qubits", "dim_C C^(2^n)", "dim_C C(x)A_n", "dim_R A_(n+1)/2"))
for n in range(1, 5):
    print("%6d %14d %20d %22d" % (n, 2 ** n, 2 ** n, 2 ** (n + 1) // 2))
print("adding a qubit doubles the space; so does one Cayley--Dickson step, in either reading")

print()
print("=== Part B: complexification has zero divisors, the real algebras up to O do not ===")
for name, dim in [("C (x) H", 4), ("C (x) O", 8)]:
    x = np.zeros(dim, dtype=complex); x[0] = 1.0; x[1] = 1j     # 1 + i e_1
    xb = conj(x)
    print("%-8s x = 1 + i e_1: N(x) = %s ; x xbar = %s ; x nonzero, xbar nonzero -> zero divisor"
          % (name, N_bilinear(x), np.allclose(cd(x, xb), 0)))
for name, dim in [("H (real)", 4), ("O (real)", 8), ("S (real)", 16)]:
    worst = 0.0
    for _ in range(2000):
        x = rng.normal(size=dim); y = rng.normal(size=dim)
        worst = max(worst, abs(N_bilinear(cd(x, y)) - N_bilinear(x) * N_bilinear(y)) / (N_bilinear(x) * N_bilinear(y)))
    print("%-8s worst relative norm-composition defect over 2000 random pairs: %.2e" % (name, worst))
e = np.eye(16)
z = (e[1] + e[10]) / math.sqrt(2); w = (e[4] - e[15]) / math.sqrt(2)
print("S (real) an explicit zero divisor pair from the corpus scans: |zw| = %.3e" % np.linalg.norm(cd(z, w)))

print()
print("=== Part C: C^4 as the real octonions with the e_1 complex structure ===")
e8 = np.eye(8)
L1 = np.array([cd(e8[1], e8[k]) for k in range(8)]).T      # matrix of left multiplication by e_1
print("L_{e_1}^2 = -I: %s" % np.allclose(L1 @ L1, -np.eye(8)))
# invariant 2-planes: e_a paired with e_1 e_a (a in the orbit representatives)
pairs, used = [], set()
for a in range(8):
    if a in used:
        continue
    img = cd(e8[1], e8[a]); b = int(np.argmax(np.abs(img))); s = int(np.sign(img[b]))
    pairs.append((a, b, s)); used.update([a, b])
print("e_1 e_a = s e_b on the pairs (a, b, s):", pairs)


def to_octonion(psi):
    """psi_k = u_k + i v_k on the k-th plane (e_a, e_b): u e_a + v (e_1 e_a) = u e_a + v s e_b."""
    o = np.zeros(8)
    for k, (a, b, s) in enumerate(pairs):
        o[a] += psi[k].real; o[b] += s * psi[k].imag
    return o


worst_norm, worst_i = 0.0, 0.0
for _ in range(1000):
    psi = rng.normal(size=4) + 1j * rng.normal(size=4)
    o = to_octonion(psi)
    worst_norm = max(worst_norm, abs(np.vdot(psi, psi).real - N_bilinear(o)))
    worst_i = max(worst_i, np.max(np.abs(to_octonion(1j * psi) - cd(e8[1], o))))
print("Hermitian norm of psi equals the real octonionic norm of its 8-vector: worst |difference| = %.1e" % worst_norm)
print("multiplying psi by i equals left multiplication of its 8-vector by e_1: worst |difference| = %.1e" % worst_i)
print("so the paper's octonions are the REAL algebra carrying the amplitude's complex structure (e_1 with its sign bookkeeping), not the complexification")
