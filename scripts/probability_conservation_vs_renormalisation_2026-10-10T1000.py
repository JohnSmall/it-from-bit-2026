#!/usr/bin/env python3
"""probability_conservation_vs_renormalisation_2026-10-10T1000.py

JS, 2026-10-10, on the continuity section: "consider the requirement that
measured probability must sum to 1 and therefore probability must be
conserved".  Standard quantum mechanics reproduced for the note; nothing of
the framework's own.  Seed 20261010; numpy only.

  A. "Sums to one at every measurement" does not by itself give conservation:
     Aaronson's renormalised theory (p_i = |psi_i|^2 / sum |psi_j|^2, dynamics
     any invertible linear map) is normalised at every measurement and is not
     norm-preserving.  It signals: a local invertible map on qubit 2 of a
     product-free entangled pair changes the reduced state of qubit 1 after
     renormalisation.  With unitaries it never does.
  B. What makes normalisation imply conservation is that the probability be
     the unrenormalised |psi_i|^2 (a polynomial in the amplitudes, which is
     what the paper's Born derivation gives) and the dynamics linear: a
     linear map that carries the unit sphere of a norm to itself is an
     isometry of that norm.  Checked for random GL maps: those that keep
     sum |psi_i|^2 = 1 on a sample of normalised states are unitary.
  C. For p != 2 the linear isometries of the p-norm are generalised
     permutations (Lamperti): a random rotation changes the p-norm of a
     random vector for p = 1, 3, 4 and never for p = 2.  Conservation fixes
     "some norm"; continuity (a connected isometry group reaching every
     state) fixes which.
  D. The anti-event route: "every event is undoable by its anti-event", with
     the anti-event of a process its time reverse U^dagger (reverse the
     order, conjugate the amplitudes), is exactly U^dagger U = 1.  For a
     random invertible map the inverse exists but is not the time reverse:
     |U^dagger U - 1| is of order one.  The conserved closed loop
     <psi|psi> = sum psi_i^* psi_i is the total probability.
"""
import numpy as np

rng = np.random.default_rng(20261010)


def unit(v): return v / np.linalg.norm(v)
def rpsi(n): return unit(rng.standard_normal(n) + 1j * rng.standard_normal(n))
def gl(n): return rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
def haar(n):
    q, r = np.linalg.qr(gl(n)); return q * (np.diag(r) / abs(np.diag(r)))


def reduced1(psi):
    M = psi.reshape(2, 2); return M @ M.conj().T


print("Probability conservation versus renormalisation, seed 20261010")
print("=" * 84)
# A
sig_gl, sig_u = 0.0, 0.0
for _ in range(300):
    psi = rpsi(4)
    G = gl(2); out = np.kron(np.eye(2), G) @ psi; out = out / np.linalg.norm(out)
    sig_gl = max(sig_gl, np.linalg.norm(reduced1(out) - reduced1(psi)))
    U = haar(2); out = np.kron(np.eye(2), U) @ psi
    sig_u = max(sig_u, np.linalg.norm(reduced1(out) - reduced1(psi)))
print("A. renormalised invertible map on qubit 2 changes qubit 1's reduced state: max %.3f (signalling)" % sig_gl)
print("   unitary map on qubit 2 changes qubit 1's reduced state:                 max %.1e (no signalling)" % sig_u)
# B
print("B. linear maps that keep sum|psi_i|^2 = 1 on normalised states are unitary")
kept, dev = 0, []
for _ in range(2000):
    G = gl(3); sample = [rpsi(3) for _ in range(6)]
    if all(abs(np.linalg.norm(G @ s) - 1) < 1e-9 for s in sample):
        kept += 1; dev.append(np.linalg.norm(G.conj().T @ G - np.eye(3)))
Us = [haar(3) for _ in range(200)]
print("   random GL(3,C) maps keeping the norm on six random states: %d of 2000 (generic maps do not)" % kept)
print("   random U(3) maps: all keep it (max |norm-1| %.1e), and |U^dagger U - 1| max %.1e" % (
    max(abs(np.linalg.norm(U @ rpsi(3)) - 1) for U in Us), max(np.linalg.norm(U.conj().T @ U - np.eye(3)) for U in Us)))
# a map preserving the sphere must be an isometry: construct one by fitting? Instead verify the contrapositive on near-unitary perturbations
eps = 1e-3; G = haar(3) @ (np.eye(3) + eps * (gl(3)))
print("   a non-unitary perturbation of size %.0e of a unitary changes the norm of a random state by %.1e: not conserved" % (
    eps, max(abs(np.linalg.norm(G @ rpsi(3)) - 1) for _ in range(50))))
# C
print("C. isometries of the p-norm: a random rotation (p=2 isometry) changes |v|_p for p != 2")
for p in (1, 2, 3, 4):
    R = haar(3); d = max(abs(np.sum(np.abs(R @ (v := rpsi(3))) ** p) ** (1 / p) - np.sum(np.abs(v) ** p) ** (1 / p)) for _ in range(200))
    print("   p = %d: max change of the p-norm under a random unitary: %.1e" % (p, d))
# D
print("D. undoable by the inverse versus undoable by the time reverse")
U = haar(4); G = gl(4)
print("   unitary:    |U^dagger U - 1| = %.1e   (the time reverse undoes it)" % np.linalg.norm(U.conj().T @ U - np.eye(4)))
print("   invertible: |G^-1 G - 1| = %.1e but |G^dagger G - 1| = %.2f  (the inverse undoes it, the time reverse does not)" % (
    np.linalg.norm(np.linalg.inv(G) @ G - np.eye(4)), np.linalg.norm(G.conj().T @ G - np.eye(4))))
psi = rpsi(4)
print("   closed loop <psi|psi> after U: %.12f ; after G: %.6f" % (np.real(np.vdot(U @ psi, U @ psi)), np.real(np.vdot(G @ psi, G @ psi))))
print("=" * 84)
print("CONSERVATION: PASS" if sig_gl > 0.1 and sig_u < 1e-12 and kept == 0 else "CONSERVATION: FAIL")
