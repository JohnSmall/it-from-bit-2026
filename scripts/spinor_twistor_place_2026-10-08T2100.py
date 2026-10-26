#!/usr/bin/env python3
"""spinor_twistor_place_2026-10-08T2100.py

JS, 2026-10-08: "a twistor is a spinor plus a place"; in the framework a place
is created when a relation is formed (pre-FANOUT the state is isolated, once
connected it acquires a location).  Is the twistor the connected object?

The two-qubit geometry answers this precisely, and this script checks it.
Write the two-qubit amplitudes as a 2x2 matrix A (rows qubit 1, columns
qubit 2).  Then rho_1 = A A^dagger, and 2 rho_1 = p^0 + p.sigma is a future
4-vector (the paper's "density operators fill the future cone").

  A. Minkowski norm: p^2 = (p^0)^2 - |p|^2 = 4 det(rho_1) = 4 |det A|^2 = C^2
     for a normalised pure pair (C the concurrence).  Separable <=> p null
     (on the cone: a light ray, no rest frame).  Entangled <=> p timelike
     (inside the cone: a rest frame exists).  Maximally entangled <=> p at
     rest, p = (1, 0).  The relation IS the mass; the mass IS the rest frame.
  B. Local invertible maps on qubit 1 (SLOCC, det M = 1) act on p as Lorentz
     transformations, p -> Lambda p, with det A invariant: the "mass" is the
     SL(2,C) invariant of the unnormalised pair.  Local SU(2) on qubit 1 is a
     rotation of p (and the local group of qubit 2 does nothing to p at all).
  C. Dictionary with the Hopf base (twistor note section 4) and Chin--Lee's
     momentum bispinor: base point (r, C e^{i phi}) = (p/p^0, mu) with
     |r|^2 + C^2 = 1; the twistor fibre over the base point is qubit 2's
     local orbit, which leaves p untouched.
  D. The stages, as numbers: a lone qubit (one spinor) has a null p and no
     relation coordinate; a pair with C = 0 is still null (the twistor: a
     spinor with a ray but no place); a pair with C > 0 is timelike, has a
     rest frame, and its place coordinate C e^{i phi} is the record of the
     relation.  Quantitatively: rapidity to the rest frame = artanh(|r|),
     infinite for a separable pair.

Seed 20261008; numpy only.
"""
import numpy as np

rng = np.random.default_rng(20261008)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
S = (sx, sy, sz)


def unit(v): return v / np.linalg.norm(v)
def rpsi(): return unit(rng.standard_normal(4) + 1j * rng.standard_normal(4))
def four(A):
    rho = A @ A.conj().T
    return np.real(np.array([np.trace(rho)] + [np.trace(rho @ s) for s in S]))   # 2 rho_1 = p^0 + p.sigma
def msq(p): return p[0] ** 2 - p[1:] @ p[1:]
def conc(psi): return 2 * abs(psi[0] * psi[3] - psi[1] * psi[2])
def sl2c():
    M = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)); return M / np.sqrt(np.linalg.det(M))
def su2():
    q = unit(rng.standard_normal(4)); return np.array([[q[0] + 1j * q[1], -q[2] + 1j * q[3]], [q[2] + 1j * q[3], q[0] - 1j * q[1]]])


eta = np.diag([1.0, -1, -1, -1])
print("Spinor, twistor, place: the two-qubit 4-vector, seed 20261008")
print("=" * 82)
# A
eA = 0.0
for _ in range(300):
    psi = rpsi(); A = psi.reshape(2, 2); p = four(A)
    eA = max(eA, abs(msq(p) - conc(psi) ** 2), abs(msq(p) - 4 * abs(np.linalg.det(A)) ** 2), abs(p[0] - 1))
sep = np.kron(unit(rng.standard_normal(2) + 1j * rng.standard_normal(2)), unit(rng.standard_normal(2) + 1j * rng.standard_normal(2)))
bell = np.array([1, 0, 0, 1]) / np.sqrt(2)
print("A. p^2 = C^2 = 4|det A|^2, p^0 = 1 (normalised):                  max err %.1e" % eA)
print("   separable pair: p^2 = %.1e (null, on the cone)    Bell pair: p = %s (at rest)" % (msq(four(sep.reshape(2, 2))), np.round(four(bell.reshape(2, 2)), 12)))
# B
eB, eRot, eInv, eQ2 = 0.0, 0.0, 0.0, 0.0
for _ in range(300):
    psi = rpsi(); A = psi.reshape(2, 2); p = four(A)
    M = sl2c(); Ap = M @ A; pp = four(Ap)
    # Lorentz: p' = Lambda p with Lambda from M; check the invariant and that Lambda is in SO(1,3) via p'^2 = p^2
    eB = max(eB, abs(msq(pp) - msq(p)))
    eInv = max(eInv, abs(np.linalg.det(Ap) - np.linalg.det(A)))
    # reconstruct Lambda column by column from M acting on the Pauli basis and check Lambda^T eta Lambda = eta
    basis = [np.eye(2, dtype=complex), sx, sy, sz]
    Lam = np.array([[np.real(np.trace(basis[a] @ M @ basis[b] @ M.conj().T)) / 2 for b in range(4)] for a in range(4)])
    eB = max(eB, np.linalg.norm(Lam.T @ eta @ Lam - eta), np.linalg.norm(Lam @ p - pp))
    U = su2(); pr = four(U @ A); eRot = max(eRot, abs(pr[0] - p[0]), abs(np.linalg.norm(pr[1:]) - np.linalg.norm(p[1:])))
    V = su2(); eQ2 = max(eQ2, np.linalg.norm(four(A @ V.T) - p))
print("B. local SL(2,C) on qubit 1 = Lorentz on p (Lambda^T eta Lambda = eta, Lambda p = p'): max err %.1e; det A invariant %.1e" % (eB, eInv))
print("   local SU(2) on qubit 1 = rotation (p^0, |p| fixed): %.1e; local SU(2) on qubit 2 leaves p alone: %.1e" % (eRot, eQ2))
# C
eC = 0.0
for _ in range(300):
    psi = rpsi(); A = psi.reshape(2, 2); p = four(A); C = conc(psi)
    r = p[1:] / p[0]
    eC = max(eC, abs(r @ r + C * C - 1))
print("C. base point (r, C e^{i phi}) = (p/p^0, mu): |r|^2 + C^2 = 1:        max err %.1e   (Chin--Lee's |p|^2 + |mu|^2 = 1)" % eC)
# D
print("D. the stages")
for name, psi in (("separable (twistor: null ray, no place)", sep), ("C = 0.3", None), ("C = 0.9", None), ("Bell (at rest: a place)", bell)):
    if psi is None:
        c = float(name.split("= ")[1]); th = np.arcsin(c) / 2
        psi = np.array([np.cos(th), 0, 0, np.sin(th)]); psi = psi * np.exp(1j * rng.uniform(0, 2 * np.pi))
        U = np.kron(su2(), su2()); psi = U @ psi
    p = four(psi.reshape(2, 2)); r = np.linalg.norm(p[1:]) / p[0]; C = conc(psi)
    rap = np.inf if r >= 1 - 1e-12 else np.arctanh(r)
    print("   %-42s C = %.3f   p^2 = %.3f   |r| = %.3f   rapidity to rest frame = %s" % (name, C, msq(p), r, "inf" if rap == np.inf else "%.3f" % rap))
print("=" * 82)
print("SPINOR TWISTOR PLACE: %s" % ("PASS" if eA < 1e-12 and eB < 1e-10 and eInv < 1e-12 and eRot < 1e-12 and eQ2 < 1e-12 and eC < 1e-12 else "FAIL"))
