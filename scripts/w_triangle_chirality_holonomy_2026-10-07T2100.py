#!/usr/bin/env python3
"""w_triangle_chirality_holonomy_2026-10-07T2100.py

JS, 2026-10-07: "GHZ does not have pairs of fibrations, but the W case does
have 3 pairs, the quaternionic subalgebras of a triple."  The chirality of
section 9 (det T < 0, partial transpose negative) applied to the three edges
of the three-qubit register, where each pair is a MIXED two-qubit state and
the pure-state Hopf map is not available, but the correlation matrix and the
partial transpose are.

  A. Canonical W and GHZ: for each edge XY the correlation matrix
     T_ij = Tr(rho_XY sigma_i (x) sigma_j), its determinant (sign = chirality
     of the map from X's axis to Y's conditional Bloch vector), Wootters's
     concurrence, the smallest eigenvalue of the partial transpose, and the
     Z_2 holonomy sign(det T_AB det T_BC det T_CA) round the triangle.
     Single-qubit marginal spectra and the three-tangle for the class.
  B. Local unitaries: det T, C, holonomy invariant (300 random SU(2)^3).
  C. Random SLOCC images (GL(2,C)^3, normalised): how far the dichotomy
     survives off the canonical orbit.  Reported, not assumed.
  D. The frustration as holonomy: a handedness bit chi_X in {L,R} per sphere
     with chi_X != chi_Y on every improper edge has no solution on K_3; the
     obstruction is exactly the product of the three signs.

Seed 20261007; numpy only.
"""
import itertools

import numpy as np

rng = np.random.default_rng(20261007)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
S = (sx, sy, sz); I2 = np.eye(2)
YY = np.kron(sy, sy)


def ket(*bits):
    v = np.zeros(8, complex); v[int("".join(map(str, bits)), 2)] = 1; return v


W = (ket(1, 0, 0) + ket(0, 1, 0) + ket(0, 0, 1)) / np.sqrt(3)
GHZ = (ket(0, 0, 0) + ket(1, 1, 1)) / np.sqrt(2)
PAIRS = {"AB": 2, "BC": 0, "CA": 1}          # pair -> qubit traced out


def reduced_pair(psi, trace_out):
    t = psi.reshape(2, 2, 2)
    rho3 = np.einsum("abc,def->abcdef", t, t.conj())
    if trace_out == 2: r = np.einsum("abcdec->abde", rho3); return r.reshape(4, 4)
    if trace_out == 0: r = np.einsum("abcaef->bcef", rho3); return r.reshape(4, 4)
    # trace out B: keep (C, A) so that the pair reads "CA"
    r = np.einsum("abcdbf->cafd", rho3); return r.reshape(4, 4)


def corr(rho):
    return np.array([[np.real(np.trace(rho @ np.kron(si, sj))) for sj in S] for si in S])


def concurrence(rho):
    R = rho @ YY @ rho.conj() @ YY
    lam = np.sqrt(np.abs(np.sort(np.linalg.eigvals(R).real)[::-1]))
    return max(0.0, lam[0] - lam[1] - lam[2] - lam[3])


def min_pt(rho):
    g = rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    return np.linalg.eigvalsh(g).min()


def three_tangle(psi):
    a = psi.reshape(2, 2, 2)
    d1 = (a[0,0,0]*a[1,1,1])**2 + (a[0,0,1]*a[1,1,0])**2 + (a[0,1,0]*a[1,0,1])**2 + (a[1,0,0]*a[0,1,1])**2
    d2 = (a[0,0,0]*a[1,1,1]*a[0,1,1]*a[1,0,0] + a[0,0,0]*a[1,1,1]*a[1,0,1]*a[0,1,0] + a[0,0,0]*a[1,1,1]*a[1,1,0]*a[0,0,1]
          + a[0,1,1]*a[1,0,0]*a[1,0,1]*a[0,1,0] + a[0,1,1]*a[1,0,0]*a[1,1,0]*a[0,0,1] + a[1,0,1]*a[0,1,0]*a[1,1,0]*a[0,0,1])
    d3 = a[0,0,0]*a[1,1,0]*a[1,0,1]*a[0,1,1] + a[1,1,1]*a[0,0,1]*a[0,1,0]*a[1,0,0]
    return 4 * abs(d1 - 2 * d2 + 4 * d3)


def marginal_spectrum(psi, q):
    t = psi.reshape(2, 2, 2); t = np.moveaxis(t, q, 0).reshape(2, 4)
    return np.sort(np.linalg.eigvalsh(t @ t.conj().T))[::-1]


def edges(psi):
    out = {}
    for name, tr in PAIRS.items():
        rho = reduced_pair(psi, tr); T = corr(rho)
        out[name] = (np.linalg.det(T), concurrence(rho), min_pt(rho), np.round(np.diag(T), 4))
    return out


def holonomy(e):
    p = np.prod([v[0] for v in e.values()])
    return 0 if abs(p) < 1e-12 else int(np.sign(p))


def su2():
    q = rng.standard_normal(4); q /= np.linalg.norm(q)
    return np.array([[q[0] + 1j * q[1], -q[2] + 1j * q[3]], [q[2] + 1j * q[3], q[0] - 1j * q[1]]])


def gl2():
    return rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))


def local(psi, Ms):
    v = np.kron(np.kron(Ms[0], Ms[1]), Ms[2]) @ psi
    return v / np.linalg.norm(v)


print("W triangle chirality and holonomy, seed 20261007")
print("=" * 88)
print("A. canonical representatives")
for name, psi in (("W", W), ("GHZ", GHZ)):
    e = edges(psi)
    print("   %-3s three-tangle %.3f, marginal spectrum %s" % (name, three_tangle(psi), np.round(marginal_spectrum(psi, 0), 4)))
    for k, (d, C, m, diag) in e.items():
        print("       edge %s: diag T = %s  det T = %+.4f  C = %.4f  min eig(rho^Gamma) = %+.4f" % (k, diag, d, C, m))
    print("       Z_2 holonomy sign(det T_AB det T_BC det T_CA) = %+d" % holonomy(e))
print("   W edge exactly: det T = -4/27 = %.4f; min eig(rho^Gamma) = (1 - sqrt5)/6 = %.4f" % (-4 / 27, (1 - np.sqrt(5)) / 6))

print("B. local unitaries (300 random SU(2)^3): invariance of det T, C, and holonomy")
for name, psi in (("W", W), ("GHZ", GHZ)):
    e0 = edges(psi); worst = 0.0; hol = set()
    for _ in range(300):
        e = edges(local(psi, [su2() for _ in range(3)]))
        worst = max(worst, max(abs(e[k][0] - e0[k][0]) + abs(e[k][1] - e0[k][1]) for k in e))
        hol.add(holonomy(e))
    print("   %-3s max change in (det T, C) over edges: %.1e; holonomies seen: %s" % (name, worst, sorted(hol)))

print("C. random SLOCC images (300 random GL(2,C)^3, normalised): off the canonical orbit")
for name, psi in (("W", W), ("GHZ", GHZ)):
    hol = {}; signs = {"all three edges improper (det<0)": 0, "some edge det>0": 0, "some edge det=0": 0}
    negs = 0; taus = []
    for _ in range(300):
        p = local(psi, [gl2() for _ in range(3)]); e = edges(p); taus.append(three_tangle(p))
        h = holonomy(e); hol[h] = hol.get(h, 0) + 1
        ds = [v[0] for v in e.values()]
        if all(d < -1e-12 for d in ds): signs["all three edges improper (det<0)"] += 1
        elif any(d > 1e-12 for d in ds): signs["some edge det>0"] += 1
        else: signs["some edge det=0"] += 1
        negs += all(v[2] < -1e-9 for v in e.values())
    print("   %-3s three-tangle range [%.3f, %.3f]; holonomy counts %s; %s; all three partial transposes negative: %d/300"
          % (name, min(taus), max(taus), dict(sorted(hol.items())), signs, negs))

print("D. the frustration as a Z_2 holonomy")
sol = [c for c in itertools.product("LR", repeat=3) if c[0] != c[1] and c[1] != c[2] and c[2] != c[0]]
print("   handedness assignments chi in {L,R}^3 with chi_X != chi_Y on all three edges: %d  (K_3 not two-colourable)" % len(sol))
print("   obstruction = product of edge signs: W gives (-1)^3 = -1 (frustrated); GHZ gives 0 (no constraint on any edge)")
print("=" * 88)
eW, eG = edges(W), edges(GHZ)
ok = (all(abs(v[0] + 4 / 27) < 1e-12 and abs(v[1] - 2 / 3) < 1e-12 for v in eW.values()) and holonomy(eW) == -1
      and all(abs(v[0]) < 1e-12 and v[1] < 1e-12 and v[2] > -1e-12 for v in eG.values()) and holonomy(eG) == 0 and len(sol) == 0)
print("W TRIANGLE: %s" % ("PASS" if ok else "FAIL"))
