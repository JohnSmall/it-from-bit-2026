#!/usr/bin/env python3
"""twistor_chirality_filatov_2026-10-07T1900.py

JS, 2026-10-07: twistors are chiral; "twistor factorisation of the
quaternionic Hopf map" recalls Filatov and Auzinsh's two-Bloch-sphere picture
of a Bell state with one sphere the inversion of the other.  Checks, in
Convention A quaternions (q = a + b j, a, b complex; e1 = i, e2 = j):

  A. Chirality of Spin(4) = Sp(1)_L x Sp(1)_R on H = R^4: the three left
     multiplications L_i, L_j, L_k are (anti-)self-dual 2-forms of one sign
     and the three right multiplications of the other sign, for the
     orientation (1, i, j, k).  The twistor fibre, the sphere of complex
     structures compatible with an orientation, is one chirality.
  B. On H^2 = two qubits (standard complex structure = left i): the right
     Sp(1) is the unitary local group of qubit 2; the left Sp(1) is generated
     by the global phase (left i) and the antiunitary spin flip of qubit 2
     (left j = (1 (x) -i sigma_y K) exactly).  So the two chiralities of the
     Hopf fibration are "unitary local group" and "phase plus spin flip".
  C. The left Hopf map h_L(q1,q2) = (2 conj(q1) q2, |q1|^2 - |q2|^2) is
     invariant under left Sp(1), hence descends to the standard projective
     two-qubit space; the right map h_R descends to the projective space of
     the partially conjugated psi' = (alpha, conj beta, gamma, conj delta);
     and h_R(psi') equals h_L(psi) up to a fixed rotation of S^4.  The two
     twistor chiralities are exchanged by conjugating one qubit.
  D. Filatov's inversion: for a pure two-qubit state with correlation matrix
     T_ij = <sigma_i (x) sigma_j>, det T = -C^2 (C the concurrence): the map
     from qubit 1's measurement axis to qubit 2's conditional Bloch vector
     is orientation-reversing for every entangled pure state, and for a Bell
     state it is a reflection or an inversion of the sphere.  For the
     singlet T = -1 exactly: the second sphere is the inversion of the first.
     The spin flip of part B acts on the Bloch vector as r -> -r, the same
     inversion.
  E. The same in Hopf terms: the spin flip of qubit 2 (left j) is NOT in the
     right Sp(1); being antiunitary it also conjugates qubit 1, so on the
     right Hopf base it reflects qubit 1's Bloch vector in the y axis and
     conjugates the concurrence phase, while on qubit 2's own sphere it is
     the inversion r -> -r.
  F. Filatov's constraint is the Peres--Horodecki criterion in disguise: the
     partial transpose on qubit 2 reverses the chirality, det T -> +C^2, and
     the result has eigenvalue -C/2 < 0 for every entangled pure state; the
     same-handed tensor T = +1 is not a state at all, the inverted one is the
     singlet.

Seed 20261007; numpy only.
"""
import itertools

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


E = np.eye(4)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
S = (sx, sy, sz)


def L(q):  return np.array([cd(q, E[k]) for k in range(4)]).T     # left multiplication matrix
def R(q):  return np.array([cd(E[k], q) for k in range(4)]).T     # right multiplication matrix


def quat(a, b):   return np.array([a.real, a.imag, b.real, b.imag])   # a + b j
def cplx(q):      return q[0] + 1j * q[1], q[2] + 1j * q[3]
def to_psi(q1, q2): return np.array([*cplx(q1), *cplx(q2)])
def to_q(psi):    return quat(psi[0], psi[1]), quat(psi[2], psi[3])
def hR(q1, q2):   return np.concatenate((2 * cd(q1, conj(q2)), [q1 @ q1 - q2 @ q2]))
def hL(q1, q2):   return np.concatenate((2 * cd(conj(q1), q2), [q1 @ q1 - q2 @ q2]))
def pconj(v):     return np.array([v[0], np.conj(v[1]), v[2], np.conj(v[3])])


print("Twistor chirality and Filatov's inversion, Convention A, seed 20261007")
print("=" * 80)

# --- A: Hodge duality of the six multiplication 2-forms
eps = np.zeros((4, 4, 4, 4))
for p in itertools.permutations(range(4)):
    eps[p] = np.linalg.det(np.eye(4)[list(p)])


def hodge(w):
    return 0.5 * np.einsum("abcd,cd->ab", eps, w)


print("A. chirality of Spin(4): left and right multiplications as (anti-)self-dual 2-forms, orientation (1,i,j,k)")
for name, M in (("left", L), ("right", R)):
    signs = []
    for k in (1, 2, 3):
        w = M(E[k]); assert np.allclose(w, -w.T)
        hw = hodge(w)
        signs.append(int(np.sign(np.sum(hw * w))) if np.allclose(hw, w) or np.allclose(hw, -w) else 0)
    print("   %-5s multiplications by i, j, k: *w = %+d w  (all three)" % (name, signs[0]) if len(set(signs)) == 1 and signs[0] != 0 else "   %s: FAIL %s" % (name, signs))
sl = int(np.sign(np.sum(hodge(L(E[1])) * L(E[1])))); sr = int(np.sign(np.sum(hodge(R(E[1])) * R(E[1]))))
print("   opposite chiralities: %s" % ("yes" if sl == -sr else "no"))

# --- B: the two Sp(1)'s in qubit language
print("B. the two Sp(1) actions on H^2 = two qubits")
eRU, eLphase, eLflip = 0.0, 0.0, 0.0
for _ in range(300):
    psi = unit(rng.standard_normal(4) + 1j * rng.standard_normal(4)); q1, q2 = to_q(psi)
    g = rq(); u, v = cplx(g)
    U = np.array([[u, -np.conj(v)], [v, np.conj(u)]])
    out = to_psi(cd(q1, g), cd(q2, g))
    eRU = max(eRU, min(np.linalg.norm(out - np.kron(np.eye(2), U) @ psi), np.linalg.norm(out - np.kron(np.eye(2), U.T) @ psi)))
    t = rng.uniform(0, 2 * np.pi); ph = np.cos(t) * E[0] + np.sin(t) * E[1]
    eLphase = max(eLphase, np.linalg.norm(to_psi(cd(ph, q1), cd(ph, q2)) - np.exp(1j * t) * psi))
    flip = to_psi(cd(E[2], q1), cd(E[2], q2))
    eLflip = max(eLflip, np.linalg.norm(flip - np.kron(np.eye(2), -1j * sy) @ psi.conj()))
print("   right Sp(1) = (1 (x) U) psi, U in SU(2), unitary on qubit 2:              max err %.1e" % eRU)
print("   left  e^{i t} = global phase e^{i t} psi:                                  max err %.1e" % eLphase)
print("   left  j = (1 (x) (-i sigma_y K)) psi, the antiunitary spin flip of qubit 2: max err %.1e" % eLflip)

# --- C: the two Hopf maps and partial conjugation
print("C. the two Hopf maps")
eLinv, eRdesc, eLdesc, eSwap = 0.0, 0.0, 0.0, 0.0
Rot = None
for _ in range(300):
    psi = unit(rng.standard_normal(4) + 1j * rng.standard_normal(4)); q1, q2 = to_q(psi)
    g = rq(); t = rng.uniform(0, 2 * np.pi)
    eLinv = max(eLinv, np.linalg.norm(hL(cd(g, q1), cd(g, q2)) - hL(q1, q2)))
    eLdesc = max(eLdesc, np.linalg.norm(hL(*to_q(np.exp(1j * t) * psi)) - hL(q1, q2)))           # global phase
    eRdesc = max(eRdesc, np.linalg.norm(hR(*to_q(np.exp(1j * t) * psi)) - hR(q1, q2)))           # should NOT vanish
    a, b = hL(q1, q2), hR(*to_q(pconj(psi)))
    # predicted relation: b = (conj of a's complex part, -conj of a's j part, same real)
    pred = np.array([a[0], -a[1], -a[2], a[3], a[4]])
    eSwap = max(eSwap, np.linalg.norm(b - pred))
print("   h_L invariant under left Sp(1):                                   %.1e" % eLinv)
print("   h_L constant on global-phase orbits (descends to the two-qubit CP^3): %.1e" % eLdesc)
print("   h_R moved by the global phase (max over sample):                   %.3f  (it descends to CP^3 of psi' instead)" % eRdesc)
print("   h_R(psi') = D h_L(psi) with D = diag(1,-1,-1,1,1), det D = +1 (a rotation of S^4): max err %.1e" % eSwap)

# --- D: Filatov's inversion, det T = -C^2
print("D. correlation matrix T_ij = <sigma_i (x) sigma_j>: det T = -C^2")
eDet = 0.0
for _ in range(300):
    psi = unit(rng.standard_normal(4) + 1j * rng.standard_normal(4))
    T = np.array([[np.real(np.vdot(psi, np.kron(si, sj) @ psi)) for sj in S] for si in S])
    C = 2 * abs(psi[0] * psi[3] - psi[1] * psi[2])
    eDet = max(eDet, abs(np.linalg.det(T) + C * C))
print("   random pure states, max |det T + C^2|:                               %.1e" % eDet)
bells = {"Phi+": np.array([1, 0, 0, 1]) / np.sqrt(2), "Phi-": np.array([1, 0, 0, -1]) / np.sqrt(2),
         "Psi+": np.array([0, 1, 1, 0]) / np.sqrt(2), "Psi-": np.array([0, 1, -1, 0]) / np.sqrt(2)}
for name, psi in bells.items():
    T = np.array([[np.real(np.vdot(psi, np.kron(si, sj) @ psi)) for sj in S] for si in S])
    print("   %-4s T = diag%s  det %+d  (second sphere = %s of the first)" % (name, tuple(int(round(x)) for x in np.diag(T)), int(round(np.linalg.det(T))),
          "inversion" if np.allclose(T, -np.eye(3)) else "reflection in one axis after a rotation"))
# spin flip on the Bloch vector
eFlip = 0.0
for _ in range(100):
    p = unit(rng.standard_normal(2) + 1j * rng.standard_normal(2)); r = np.real([np.vdot(p, s @ p) for s in S])
    pf = -1j * sy @ p.conj(); rf = np.real([np.vdot(pf, s @ pf) for s in S])
    eFlip = max(eFlip, np.linalg.norm(rf + r))
print("   the spin flip -i sigma_y K sends the Bloch vector r -> -r (inversion):      max err %.1e" % eFlip)

# --- E: the spin flip on the Hopf base
print("E. the spin flip of qubit 2 (left j, antiunitary) on the right Hopf base (r_1, C e^{i phi}, r_z)")
eBase = 0.0
for _ in range(300):
    psi = unit(rng.standard_normal(4) + 1j * rng.standard_normal(4)); q1, q2 = to_q(psi)
    a = hR(q1, q2); b = hR(cd(E[2], q1), cd(E[2], q2))
    # base coordinates (r_x, -r_y, Re C e^{i phi}, Im C e^{i phi}, r_z); conjugation of 2 q1 conj(q2) by j
    # negates the i and k components: r_y -> -r_y (qubit 1 sees only the K), phi -> -phi
    pred = np.array([a[0], -a[1], a[2], -a[3], a[4]])
    eBase = max(eBase, np.linalg.norm(b - pred))
print("   qubit 1: r_y -> -r_y (the K alone, a reflection); concurrence phase phi -> -phi; qubit 2: r -> -r:  max err %.1e" % eBase)

# --- F: Filatov's constraint is the partial-transpose criterion
print("F. the opposite chirality is the partial transpose, and it is not a state")
ePT, eNeg = 0.0, 0.0
for _ in range(300):
    psi = unit(rng.standard_normal(4) + 1j * rng.standard_normal(4))
    rho = np.outer(psi, psi.conj()); C = 2 * abs(psi[0] * psi[3] - psi[1] * psi[2])
    rhoG = rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)        # partial transpose on qubit 2
    TG = np.array([[np.real(np.trace(rhoG @ np.kron(si, sj))) for sj in S] for si in S])
    ePT = max(ePT, abs(np.linalg.det(TG) - C * C))
    eNeg = max(eNeg, abs(np.linalg.eigvalsh(rhoG).min() + C / 2))
print("   det T^Gamma = +C^2 (chirality reversed):                                    max err %.1e" % ePT)
print("   min eigenvalue of rho^Gamma = -C/2 (negative for every entangled pure state): max err %.1e" % eNeg)
Tplus = (np.eye(4) + sum(np.kron(s, s) for s in S)) / 4
print("   the 'same-handed' tensor T = +1 (second sphere a copy of the first): min eigenvalue %.2f, not a state" % np.linalg.eigvalsh(Tplus).min())
Tminus = (np.eye(4) - sum(np.kron(s, s) for s in S)) / 4
print("   the inverted tensor T = -1 (the singlet):                            min eigenvalue %.2f, a state" % np.linalg.eigvalsh(Tminus).min())
print("=" * 80)
ok = (sl == -sr and sl != 0 and eRU < 1e-12 and eLphase < 1e-12 and eLflip < 1e-12 and eLinv < 1e-12 and eLdesc < 1e-12
      and eRdesc > 0.1 and eSwap < 1e-12 and eDet < 1e-12 and eFlip < 1e-12 and eBase < 1e-12
      and ePT < 1e-12 and eNeg < 1e-12 and np.linalg.eigvalsh(Tplus).min() < -0.1)
print("TWISTOR CHIRALITY / FILATOV: %s" % ("PASS" if ok else "FAIL"))
