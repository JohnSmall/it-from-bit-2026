#!/usr/bin/env python3
"""w_orbit_cfrac_check_2026-09-23T1100.py

Numerical check of Proposition prop:w-access (paper1/entanglement_classes_and_gauge_groups):
on the local-unitary orbit of W the C-fraction of the octonionic Hopf image,
C_frac = |<o1,o2>|^2 / (|o1|^2 |o2|^2) with o1, o2 the two first-qubit branches
(Lemma lem:cproj and the composition identity |h|^2 = |o1|^2 |o2|^2), is
generically nonzero, vanishes only when the first-qubit unitary is diagonal or
anti-diagonal, and has supremum 1/9, attained at |a|^2 = 1/2; closed form
C_frac = p(1-p)/((1+p)(2-p)), p = |a|^2 (appendix app:w-proof, eq. wcfrac).
Also: internal unitaries on qubits 2 and 3 leave C_frac unchanged, and the
same holds under each of the three qubit splits by the symmetry of W.

Seed 20260923; 20000 Haar-random local unitaries per split. numpy only.
"""
import math

import numpy as np

rng = np.random.default_rng(20260923)


def haar_u2():
    z = (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r) / np.abs(np.diag(r))
    return q * d


def cfrac(psi, split):
    t = psi.reshape(2, 2, 2)
    t = np.moveaxis(t, split, 0).reshape(2, 4)
    o1, o2 = t[0], t[1]
    return abs(np.vdot(o1, o2)) ** 2 / (np.vdot(o1, o1).real * np.vdot(o2, o2).real)


W = np.zeros(8, dtype=complex)
for lab in ["001", "010", "100"]:
    W[int(lab, 2)] = 1 / math.sqrt(3)

print("=== W orbit: C-fraction under random local unitaries, 20000 samples per split ===")
for split in range(3):
    vals = []
    for _ in range(20000):
        U = np.kron(np.kron(haar_u2(), haar_u2()), haar_u2())
        vals.append(cfrac(U @ W, split))
    vals = np.array(vals)
    print("split on qubit %d: max C_frac = %.6f (1/9 = %.6f) ; fraction of samples with C_frac < 1e-6: %.5f ; mean %.5f"
          % (split, vals.max(), 1 / 9, np.mean(vals < 1e-6), vals.mean()))

print()
print("=== closed form against direct computation, first-qubit unitary only ===")
print("%8s %12s %12s" % ("p=|a|^2", "direct", "p(1-p)/((1+p)(2-p))"))
for p in [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]:
    a = math.sqrt(p); b = math.sqrt(1 - p) * np.exp(1j * 0.7)
    U1 = np.array([[a, b], [-np.conj(b), np.conj(a)]])
    psi = np.kron(np.kron(U1, np.eye(2)), np.eye(2)) @ W
    print("%8.2f %12.6f %12.6f" % (p, cfrac(psi, 0), p * (1 - p) / ((1 + p) * (2 - p))))
print("supremum 1/9 at p = 1/2; zero exactly at p = 0 and p = 1 (diagonal or anti-diagonal U_1)")
print()
print("=== internal unitaries alone (qubits 2, 3) leave the bare W at C_frac = 0 ===")
vals = [cfrac(np.kron(np.kron(np.eye(2), haar_u2()), haar_u2()) @ W, 0) for _ in range(2000)]
print("max over 2000 samples: %.2e" % max(vals))
