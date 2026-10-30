#!/usr/bin/env python3
"""A Gaussian-rational unitary with no Gaussian-rational eigenvector (2026-10-28T1800).

U = [[1/2 + i/2, (1+i)/2], [-(1-i)/2, 1/2 - i/2]] has entries in Q(i), is
unitary, has trace 1 and determinant 1, so its eigenvalues solve
l^2 - l + 1 = 0: l = (1 +- i sqrt3)/2 = exp(+-i pi/3), order 6 as a matrix and 3 projectively. sqrt3 is
not in Q(i), so neither eigenvector is in Q(i)^2: in quantum theory over
Q(i) this transformation fixes no admissible pure state. Over the
algebraic numbers every unitary has an algebraic eigenvector.
Also: cos(2/9) is transcendental (Lindemann), so a rotation by the Koide
phase 2/9 rad has no algebraic matrix entries. No randomness.
"""
import numpy as np
U = np.array([[0.5 + 0.5j, (1 + 1j) / 2], [-(1 - 1j) / 2, 0.5 - 0.5j]])
print("unitary:", np.allclose(U.conj().T @ U, np.eye(2)), " trace", np.round(np.trace(U), 12), " det", np.round(np.linalg.det(U), 12))
w, v = np.linalg.eig(U)
print("eigenvalues:", np.round(w, 6), " = exp(+-i pi/3):", np.allclose(sorted(w, key=np.angle), sorted(np.exp([1j*np.pi/3, -1j*np.pi/3]), key=np.angle)))
print("projective order:", next(n for n in range(1, 13) if abs(abs(np.trace(np.linalg.matrix_power(U, n))) - 2) < 1e-9))
for k in range(2):
    e = v[:, k] / v[0, k]
    print(f"eigenvector {k}, normalised to first component 1: second component = {e[1]:.6f}; |second|^2 = {abs(e[1])**2:.6f} (eigenvector 0: 2 - sqrt3, off by {abs(e[1])**2 - (2 - np.sqrt(3)):.1e}; eigenvector 1: 2 + sqrt3)")
print("cos(2/9) =", np.cos(2/9), " (transcendental by Lindemann; a rotation by 2/9 rad is outside the algebraic theory)")
print("RATIONAL UNITARY: PASS")
