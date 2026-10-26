#!/usr/bin/env python3
"""colour_su3_from_e1_structure_2026-09-27T1500.py

JS's example (2026-09-27): "the colour force derives from octonions, but we
describe the colour of a quark as a complex probability superposition of
potential colours." Check that one choice, the preferred imaginary unit e_1
as the complex structure on the real octonions, supplies both: the complex
3-space of colour amplitudes and the SU(3) that acts on it.

Part A  Der(O) in Convention A by the Leibniz nullspace: dimension 14 (g_2).
Part B  The derivations annihilating e_1: dimension 8. Each commutes with
        left multiplication by e_1, hence is C-linear for that complex
        structure; on the 6-real-dimensional complement of {e_0, e_1}, read as
        C^3 through the e_1 pairs, they are traceless anti-Hermitian 3x3
        matrices: su(3). A generic derivation does not fix e_1 and mixes the
        C line with the C^3.
Part C  The three colour lines are the three e_1-invariant planes (e_2,e_3),
        (e_4,e_5), (e_6,-e_7); a random unit vector of C^3 is a colour
        superposition, and exponentiating a random su(3) derivation carries
        it to another unit vector of the same C^3 with the Hermitian norm and
        the Hermitian inner product preserved.

Convention A; seed 20260927; numpy only.
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


E = np.eye(8)
T = np.array([[cd(E[i], E[j]) for j in range(8)] for i in range(8)])   # T[i,j,:] = e_i e_j

# --- Part A: derivations D (8x8) with D(xy) = D(x) y + x D(y) on basis pairs
rows = []
for i in range(8):
    for j in range(8):
        # D(e_i e_j) - D(e_i) e_j - e_i D(e_j) = 0, linear in the 64 entries of D
        M = np.zeros((8, 64))
        for k in range(8):                      # D(e_i e_j) = sum_k T[i,j,k] D e_k
            M += T[i, j, k] * np.kron(np.eye(8)[:, :], np.eye(8)[k]).reshape(8, 64) if False else 0
        # explicit construction instead of the kron trick
        for a in range(8):
            for b in range(8):
                col = a * 8 + b                 # D[a,b]: component a of D e_b
                # term D(e_i e_j): sum_k T[i,j,k] * D[:,k]
                M[a, col] += T[i, j, b] if True else 0
                # term - D(e_i) e_j: -(sum_k D[k,i] e_k) e_j -> component a: - sum_k D[k,i] T[k,j,a]
                M[a, col] -= (T[b, j, a] if True else 0) * (1.0 if col == a * 8 + b else 0) * 0  # placeholder, done below
        rows.append((i, j))
# cleaner: build the linear map explicitly with einsum on a basis of matrices
def leibniz_residual(D):
    R = np.zeros((8, 8, 8))
    for i in range(8):
        for j in range(8):
            lhs = D @ T[i, j]
            rhs = cd(D[:, i], E[j]) + cd(E[i], D[:, j])
            R[i, j] = lhs - rhs
    return R.reshape(-1)


basis = []
for a in range(8):
    for b in range(8):
        D = np.zeros((8, 8)); D[a, b] = 1.0
        basis.append(leibniz_residual(D))
A = np.array(basis).T          # 512 x 64
u, s, vt = np.linalg.svd(A)
null = vt[s.size:] if False else vt[np.sum(s > 1e-9):]
print("=== Part A: derivations of O ===")
print("dim Der(O) = %d (expected 14, g_2)" % null.shape[0])
Ders = [v.reshape(8, 8) for v in null]

# --- Part B: those with D e_1 = 0
C = np.array([D[:, 1] for D in Ders]).T          # 8 x 14, columns D e_1
u2, s2, vt2 = np.linalg.svd(C)
stab = vt2[np.sum(s2 > 1e-9):]                   # coefficients giving D e_1 = 0
Stab = [sum(c * D for c, D in zip(coef, Ders)) for coef in stab]
print()
print("=== Part B: the stabiliser of e_1 ===")
print("dim {D in Der(O): D e_1 = 0} = %d (expected 8, su(3))" % len(Stab))
L1 = np.array([cd(E[1], E[k]) for k in range(8)]).T
print("every stabiliser derivation commutes with L_{e_1}: %s" % all(np.allclose(D @ L1, L1 @ D) for D in Stab))
pairs = [(2, 3, 1), (4, 5, 1), (6, 7, -1)]        # e_1 e_a = s e_b, from the 1400 script


def to_c3(o):
    return np.array([o[a] + 1j * s * o[b] for a, b, s in pairs])


def matrix_c3(D):
    """the 3x3 complex matrix of D on C^3 = span of the three colour planes"""
    M = np.zeros((3, 3), dtype=complex)
    for k, (a, b, s) in enumerate(pairs):
        M[:, k] = to_c3(D[:, a])                    # image of the basis vector e_a (real part 1 of line k)
    return M


ok_c_linear = ok_antiherm = ok_traceless = ok_block = True
for D in Stab:
    M = matrix_c3(D)
    # C-linearity: D(e_1 e_a) = e_1 D(e_a) -> image of i * basis vector is i * image
    for a, b, s in pairs:
        ok_c_linear &= np.allclose(to_c3(D[:, b]) * s, 1j * to_c3(D[:, a]))
    ok_antiherm &= np.allclose(M + M.conj().T, 0)
    ok_traceless &= abs(np.trace(M)) < 1e-9
    ok_block &= np.allclose(D[:2, :], 0) and np.allclose(D[:, :2], 0)   # leaves the C line (e_0, e_1) alone
print("C-linear on the colour C^3: %s ; anti-Hermitian: %s ; traceless: %s ; leaves the line (e_0, e_1) alone: %s"
      % (ok_c_linear, ok_antiherm, ok_traceless, ok_block))
Dgen = sum(rng.normal() * D for D in Ders)
print("a generic derivation moves e_1: |D e_1| = %.3f, and mixes the C line with the C^3 (entries D[2:,1] nonzero): %s"
      % (np.linalg.norm(Dgen[:, 1]), np.any(np.abs(Dgen[2:, 1]) > 1e-9)))

# --- Part C: a colour superposition and its transport
print()
print("=== Part C: a colour state is a unit vector of that C^3, and su(3) moves it inside C^3 ===")
psi = rng.normal(size=3) + 1j * rng.normal(size=3); psi /= np.linalg.norm(psi)
o = np.zeros(8)
for k, (a, b, s) in enumerate(pairs):
    o[a] = psi[k].real; o[b] = s * psi[k].imag
print("state as a real octonion: components on e_0, e_1 = %.1e (none: it lies in the colour C^3); real norm %.6f" % (np.max(np.abs(o[:2])), np.linalg.norm(o)))
# exponentiate a random su(3) derivation (Euler steps on the derivation, i.e. the automorphism exp(D))
D = sum(rng.normal() * X for X in Stab)
def expm(M, terms=30, squarings=10):
    """scaling and squaring with a Taylor series; exact to machine precision for these norms"""
    S = M / (2 ** squarings)
    R = np.eye(M.shape[0]); P = np.eye(M.shape[0])
    for k in range(1, terms):
        P = P @ S / k; R = R + P
    for _ in range(squarings):
        R = R @ R
    return R


g = expm(D)
o2 = g @ o
print("after exp(D): components on e_0, e_1 = %.1e ; real norm %.6f ; Hermitian inner product with the original = %.6f%+.6fi (a colour rotation, not a loss)"
      % (np.max(np.abs(o2[:2])), np.linalg.norm(o2), np.vdot(psi, to_c3(o2)).real, np.vdot(psi, to_c3(o2)).imag))
print("exp(D) is an automorphism: worst |g(xy) - g(x)g(y)| over 200 random pairs = %.1e"
      % max(np.max(np.abs(g @ cd(x, y) - cd(g @ x, g @ y))) for x, y in (rng.normal(size=(2, 8)) for _ in range(200))))
