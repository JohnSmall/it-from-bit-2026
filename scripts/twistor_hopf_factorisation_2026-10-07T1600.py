#!/usr/bin/env python3
"""twistor_hopf_factorisation_2026-10-07T1600.py

Twistor space and the Hopf maps, for the session note of 2026-10-07.  All in
Convention A Cayley--Dickson; quaternion q = (a, b) means a + b j with a, b
complex (e1 = i, e2 = j, e1 e2 = e3); octonions likewise from pairs of
quaternions.  Seed 20261007; numpy only.

  A. Quaternionic Hopf map h_H(q1,q2) = (2 q1 conj(q2), |q1|^2 - |q2|^2) on
     S^7 in H^2 lands on S^4 and is invariant under the RIGHT action of
     Sp(1) (exact), hence under its U(1) = {e^{i theta}} (exact), so it
     factors through S^7/U(1) = CP^3: that quotient map CP^3 -> S^4 is the
     twistor fibration (Atiyah--Hitchin--Singer).  LEFT multiplication by
     e^{i theta} is NOT in the fibre: it rotates the base's j-component by
     2 theta.
  B. Two-qubit dictionary (Mosseri--Dandoloff conventions, q1 = alpha + beta j,
     q2 = gamma + delta j for psi = alpha|00> + beta|01> + gamma|10> + delta|11>):
     base point = (2 rho_1[0,1], 2 (beta gamma - alpha delta), rho_1[0,0]-rho_1[1,1]),
     i.e. qubit 1's reduced Bloch vector r (length sqrt(1 - C^2)) and the
     complex concurrence, |r|^2 + C^2 = 1.  The right Sp(1) action is the
     local SU(2) of qubit 2; its U(1) is qubit 2's local Z-phase, not the
     global phase of psi: it is the global phase of the partially conjugated
     vector psi' = (alpha, conj beta, gamma, conj delta), the coordinates of
     H^2 for the right-i complex structure.  So the twistor CP^3 is the
     projective space of psi', and the twistor fibre Sp(1)/U(1) = S^2 is
     qubit 2's local orbit mod that phase: Jacobian rank 2 (rank 3 mod the
     global phase of psi).
  C. The twistor fibre as the sphere of complex structures: q -> q e1 conj(q)
     is the Hopf map S^3 -> S^2 onto the unit imaginary quaternions, each of
     which squares to -1 and acts orthogonally: a complex structure on H.
  D. The octonionic Hopf map h_O on S^15 does NOT factor through the complex
     Hopf map: h_O(a e^{e_k t}, b e^{e_k t}) != h_O(a, b) for every unit
     imaginary e_k, right or left, except when a, b, e_k lie in one
     quaternionic subalgebra.  No twistor space at the octonionic rung by
     this route.
  E. The ladder of spheres of complex structures: unit spheres of Im C, Im H,
     Im O are S^0, S^2, S^6 with stabilisers of a point {1}, U(1) in Sp(1),
     SU(3) in G2 (dimension 8, from the colour script of 2026-09-27).
"""
import numpy as np

rng = np.random.default_rng(20261007)


def conj(x):
    y = np.array(x, copy=True); y[1:] = -y[1:]; return y


def cd(x, y):
    n = x.size
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate((cd(a, c) - cd(conj(d), b), cd(d, a) + cd(b, conj(c))))


def unit(v):
    return v / np.linalg.norm(v)


def rq(n=4):
    return unit(rng.standard_normal(n))


def exp_unit(e, t):                       # e^{e t} for a unit imaginary e
    out = np.zeros_like(e); out[0] = np.cos(t); return out + np.sin(t) * e


def hopf(q1, q2):                         # works for H and O
    return np.concatenate((2 * cd(q1, conj(q2)), [q1 @ q1 - q2 @ q2]))


def quat_from_c(a, b):                    # a + b j, a,b complex -> (Re a, Im a, Re b, Im b)
    return np.array([a.real, a.imag, b.real, b.imag])


def c_from_quat(q):
    return q[0] + 1j * q[1], q[2] + 1j * q[3]


E4 = np.eye(4); E8 = np.eye(8)
print("Twistor space and the Hopf maps, Convention A, seed 20261007")
print("=" * 78)

# --- A
print("A. quaternionic Hopf map: right Sp(1) is the fibre, right U(1) inside it, left U(1) is not")
eS4, eR, eU, lL = 0.0, 0.0, 0.0, []
for _ in range(300):
    q = rq(8); q1, q2 = q[:4], q[4:]
    h = hopf(q1, q2); eS4 = max(eS4, abs(np.linalg.norm(h) - 1))
    g = rq(4); t = rng.uniform(0, 2 * np.pi)
    eR = max(eR, np.linalg.norm(hopf(cd(q1, g), cd(q2, g)) - h))
    u = exp_unit(E4[1], t)
    eU = max(eU, np.linalg.norm(hopf(cd(q1, u), cd(q2, u)) - h))
    hl = hopf(cd(u, q1), cd(u, q2))
    # j-component (indices 2,3 of the quaternion part) should rotate by 2t; (1, i) part fixed
    z, w = h[2] + 1j * h[3], hl[2] + 1j * hl[3]
    lL.append((abs(hl[0] - h[0]) + abs(hl[1] - h[1]) + abs(hl[4] - h[4]), abs(w - z * np.exp(2j * t))))
lL = np.array(lL)
print("   lands on S^4 (max | |h|-1 |):                       %.1e" % eS4)
print("   invariant under right Sp(1):                        %.1e" % eR)
print("   invariant under right U(1) = e^{i t}:               %.1e   -> descends to S^7/U(1) = CP^3" % eU)
print("   left e^{i t}: (1,i,real) parts fixed %.1e, j-part rotated by exactly 2t (err %.1e): NOT in the fibre"
      % (lL[:, 0].max(), lL[:, 1].max()))

# --- B
print("B. two-qubit dictionary")
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
eBase, eSep, eLU, ranks = 0.0, 0.0, 0.0, []
for _ in range(300):
    psi = unit(rng.standard_normal(4) + 1j * rng.standard_normal(4))
    al, be, ga, de = psi
    q1, q2 = quat_from_c(al, be), quat_from_c(ga, de)
    h = hopf(q1, q2)
    M = psi.reshape(2, 2); rho1 = M @ M.conj().T
    r = np.real([np.trace(rho1 @ s) for s in (sx, sy, sz)])
    C = 2 * abs(al * de - be * ga)
    conc = 2 * (be * ga - al * de)
    pred = np.array([r[0], -r[1], conc.real, conc.imag, r[2]])
    eBase = max(eBase, np.linalg.norm(h - pred), abs(r @ r + C * C - 1))
    # separable: C = 0 and base in the S^2 of unit Bloch vectors
    p1 = unit(rng.standard_normal(2) + 1j * rng.standard_normal(2)); p2 = unit(rng.standard_normal(2) + 1j * rng.standard_normal(2))
    sep = np.kron(p1, p2); hs = hopf(quat_from_c(sep[0], sep[1]), quat_from_c(sep[2], sep[3]))
    eSep = max(eSep, abs(hs[2]) + abs(hs[3]), abs(np.linalg.norm(hs[[0, 1, 4]]) - 1))
    # right Sp(1) = local SU(2) on qubit 2: (q1 g, q2 g) against (1 (x) U) psi
    g = rq(4); u, v = c_from_quat(g)                 # g = u + v j
    q1g, q2g = cd(q1, g), cd(q2, g)
    psi_g = np.array([*c_from_quat(q1g), *c_from_quat(q2g)])
    U = np.array([[u, -np.conj(v)], [v, np.conj(u)]])  # candidate; fit by least squares which U reproduces the map
    cand = np.kron(np.eye(2), U) @ psi
    cand2 = np.kron(np.eye(2), U.T) @ psi
    eLU = max(eLU, min(np.linalg.norm(psi_g - cand), np.linalg.norm(psi_g - cand2)))
    # fibre dimension: Jacobian of g -> projector over the 3 tangent directions of Sp(1) at 1,
    # (i) mod the global phase of psi, (ii) mod the right U(1), which is the global phase of the
    # partially conjugated vector psi' = (alpha, conj beta, gamma, conj delta) (right-i structure)
    def pconj(v): return np.array([v[0], np.conj(v[1]), v[2], np.conj(v[3])])
    P0 = np.outer(psi, psi.conj()); Q0 = np.outer(pconj(psi), pconj(psi).conj()); cols, colsq = [], []
    for k in (1, 2, 3):
        eps = 1e-6; ge = exp_unit(E4[k], eps)
        pe = np.array([*c_from_quat(cd(q1, ge)), *c_from_quat(cd(q2, ge))])
        cols.append(((np.outer(pe, pe.conj()) - P0) / eps).ravel())
        colsq.append(((np.outer(pconj(pe), pconj(pe).conj()) - Q0) / eps).ravel())
    ranks.append((np.linalg.matrix_rank(np.array(cols).T, tol=1e-3), np.linalg.matrix_rank(np.array(colsq).T, tol=1e-3)))
    # and: the right U(1) orbit of psi is exactly a global phase of psi'
    t = rng.uniform(0, 2 * np.pi); ue = exp_unit(E4[1], t)
    pu = np.array([*c_from_quat(cd(q1, ue)), *c_from_quat(cd(q2, ue))])
    eLU = max(eLU, np.linalg.norm(pconj(pu) - np.exp(1j * t) * pconj(psi)))
print("   base = (qubit-1 Bloch vector r, complex concurrence), |r|^2 + C^2 = 1:  max err %.1e" % eBase)
print("   separable states: C = 0 and the base lies on the unit-Bloch S^2 in S^4:  max err %.1e" % eSep)
print("   right Sp(1) on (q1,q2) equals a local SU(2) on qubit 2 (1 (x) U):       max err %.1e" % eLU)
print("   right U(1) orbit of psi = global phase of psi' = (alpha, conj beta, gamma, conj delta): max err %.1e" % eLU)
print("   Sp(1)-orbit dimension mod global phase of psi: %s; mod right U(1) (= phase of psi'): %s  -> twistor fibre S^2"
      % (sorted(set(r[0] for r in ranks)), sorted(set(r[1] for r in ranks))))

# --- C
print("C. the twistor fibre as the sphere of complex structures on H")
eH, eJ = 0.0, 0.0
for _ in range(300):
    g = rq(4); t = rng.uniform(0, 2 * np.pi)
    n = cd(cd(g, E4[1]), conj(g))
    eH = max(eH, abs(n[0]), abs(np.linalg.norm(n) - 1), np.linalg.norm(cd(cd(cd(g, exp_unit(E4[1], t)), E4[1]), conj(cd(g, exp_unit(E4[1], t)))) - n))
    J = np.array([cd(n, E4[k]) for k in range(4)]).T
    eJ = max(eJ, np.linalg.norm(J @ J + np.eye(4)), np.linalg.norm(J.T @ J - np.eye(4)))
print("   g -> g e1 conj(g): unit imaginary, invariant under g -> g e^{e1 t} (Hopf S^3 -> S^2): max err %.1e" % eH)
print("   each image n gives J = L_n with J^2 = -1, J orthogonal (a complex structure):         max err %.1e" % eJ)

# --- D
print("D. octonionic Hopf map: no factorisation through the complex Hopf map")
eS8 = 0.0; dev_right = np.zeros(7); dev_left = np.zeros(7); dev_sub = 0.0
for _ in range(300):
    o = rq(16); a, b = o[:8], o[8:]
    h = hopf(a, b); eS8 = max(eS8, abs(np.linalg.norm(h) - 1))
    t = rng.uniform(0.3, 2.8)
    for k in range(1, 8):
        u = exp_unit(E8[k], t)
        dev_right[k - 1] = max(dev_right[k - 1], np.linalg.norm(hopf(cd(a, u), cd(b, u)) - h))
        dev_left[k - 1] = max(dev_left[k - 1], np.linalg.norm(hopf(cd(u, a), cd(u, b)) - h))
    # a, b in the quaternionic subalgebra span{1, e1, e2, e3}, u = e^{e1 t}: associative, invariant
    a4 = np.concatenate((rq(4), np.zeros(4))); b4 = np.concatenate((rq(4), np.zeros(4))); s = np.sqrt(0.5)
    u = exp_unit(E8[1], t)
    dev_sub = max(dev_sub, np.linalg.norm(hopf(cd(s * a4, u), cd(s * b4, u)) - hopf(s * a4, s * b4)))
print("   lands on S^8 (max | |h|-1 |):                                   %.1e" % eS8)
print("   right e^{e_k t}, k=1..7, max |h(a u, b u) - h(a, b)|:            %s" % np.round(dev_right, 3))
print("   left  e^{e_k t}, k=1..7, max |h(u a, u b) - h(a, b)|:            %s" % np.round(dev_left, 3))
print("   same, with a, b, e_1 in one quaternionic subalgebra:             %.1e  (associative: invariant)" % dev_sub)

# --- E
print("E. the ladder of spheres of complex structures")
for name, d, stab, sdim in (("Im C", 1, "{1}", 0), ("Im H", 3, "U(1) in Sp(1)", 1), ("Im O", 7, "SU(3) in G2", 8)):
    print("   unit sphere of %s: S^%d ; stabiliser of a point %-14s dim %d ; check dim(group) - dim(stab) = %d"
          % (name, d - 1, stab, sdim, {1: 0, 3: 3 - 1, 7: 14 - 8}[d]))
print("=" * 78)
ok = (eS4 < 1e-12 and eR < 1e-12 and eU < 1e-12 and lL[:, 1].max() < 1e-12 and eBase < 1e-12 and eSep < 1e-12
      and eLU < 1e-12 and set(r[0] for r in ranks) == {3} and set(r[1] for r in ranks) == {2} and eH < 1e-12 and eJ < 1e-12 and eS8 < 1e-12
      and dev_right.min() > 1e-2 and dev_left.min() > 1e-2 and dev_sub < 1e-12)
print("TWISTOR HOPF: %s" % ("PASS" if ok else "FAIL"))
