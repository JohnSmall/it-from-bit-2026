#!/usr/bin/env python3
"""burton_anwar_meromorphic_check_2026-10-03T1600.py

Checks on Burton and Anwar, "Meromorphic Quantum Computing", arXiv:2605.06251
(Quantinuum, 7 May 2026), for the reading note of 2026-10-03.  Their chart:
a qubit state [v0 : v1] is the point z = v0/v1 of the Riemann sphere, i.e.
|psi_z> = z|0> + |1>, so |0> is z = infinity, |1> is z = 0, |+-X> are z = +-1.

  A. Prop. 3.1: projectivising the Z-, X- and W-spiders (as 2x4 matrices on
     the Segre-embedded pair) gives wz, (wz+1)/(w+z) and w+z.  Hence the
     GHZ/W arithmetic (Coecke, Kissinger, Merry, Roy 2011) read projectively.
  B. The X-spider in the reciprocal chart is Einstein velocity addition
     (w+z)/(1+wz) = tanh(artanh w + artanh z) on the real segment; the
     Z-spider on the unit circle is phase addition.  As Moebius maps, the
     Z-monoid for fixed w is diag(w,1): rotation about the Z axis for |w|=1,
     boost along it for real w > 0.  Checked by comparing with the SL(2,C)
     action on the Bloch vector.
  C. Example 5.1 and 5.2 and 5.3 decoders rebuilt from the codes' logical
     states (not from the paper's formulas): Shor [[9,1,3]], five-qubit
     [[5,1,3]], Steane [[7,1,3]].  f(z) = <0_L|psi_z^{(x)n}> / <1_L|psi_z^{(x)n}>.
  D. Riemann--Hurwitz (Thm. 2.1 / 4.2) for the three decoders, counting the
     point at infinity.  Fixed points from r(z) = p - zq (Prop. 4.7).
  E. Klein's octahedral function E7 is invariant under the Clifford
     generators S(z) = -iz and H(z) = (z+1)/(z-1) (Prop. 2.3, one direction).
  F. Ramification separates the two classes: the n-leg Z (GHZ) spider
     projectivises to z^n, a degree-n cover branched only at the two copyable
     states with n sheets each (Riemann--Hurwitz 2(n-1)); the n-leg W spider
     projectivises to z_1 + ... + z_n, univariate nz, degree 1, unbranched.
     Built from the spider matrices, not from the formulas.

Seed 20261003; numpy only.  Exact stdout goes in the session note.
"""
import itertools

import numpy as np

rng = np.random.default_rng(20261003)
P = np.polynomial.polynomial


def moebius(M, z):
    (a, b), (c, d) = M
    return (a * z + b) / (c * z + d)


def rc():
    return complex(*rng.standard_normal(2))


print("Burton--Anwar checks, seed 20261003")
print("=" * 72)

# --- A
Zsp = np.array([[1, 0, 0, 0], [0, 0, 0, 1]], dtype=complex)
Xsp = np.array([[1, 0, 0, 1], [0, 1, 1, 0]], dtype=complex)
Wsp = np.array([[0, 1, 1, 0], [0, 0, 0, 1]], dtype=complex)
worst = {"Z: wz": 0.0, "X: (wz+1)/(w+z)": 0.0, "W: w+z": 0.0}
for _ in range(500):
    w, z = rc(), rc()
    seg = np.kron([w, 1], [z, 1])
    for name, M, expect in (("Z: wz", Zsp, w * z), ("X: (wz+1)/(w+z)", Xsp, (w * z + 1) / (w + z)), ("W: w+z", Wsp, w + z)):
        v = M @ seg
        worst[name] = max(worst[name], abs(v[0] / v[1] - expect))
print("A. spider monoids on the Riemann sphere (500 random pairs)")
for k, v in worst.items():
    print("   %-18s max error %.2e" % (k, v))

# --- B
print("B. the two charts: phase addition and velocity addition")
e_vel, e_phase = 0.0, 0.0
for _ in range(500):
    u, v = rng.uniform(-0.99, 0.99, 2)
    e_vel = max(e_vel, abs((u + v) / (1 + u * v) - np.tanh(np.arctanh(u) + np.arctanh(v))))
    a, b = rng.uniform(0, 2 * np.pi, 2)
    e_phase = max(e_phase, abs(np.exp(1j * a) * np.exp(1j * b) - np.exp(1j * (a + b))))
print("   X-spider, reciprocal chart, real segment = tanh(eta_1 + eta_2): max error %.2e" % e_vel)
print("   Z-spider, unit circle = phase addition:                        max error %.2e" % e_phase)
# Moebius map of diag(w,1) against the Bloch vector: rotation for |w|=1, boost for w>0 real
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]


def bloch(v):
    v = v / np.linalg.norm(v)
    return np.real([np.conj(v) @ s @ v for s in sig])


def state(z):
    return np.array([z, 1], complex) if np.isfinite(z) else np.array([1, 0], complex)


e_rot, e_boost = 0.0, 0.0
for _ in range(200):
    z = rc(); th = rng.uniform(0, 2 * np.pi); eta = rng.uniform(-1.5, 1.5)
    # rotation about the Bloch Z axis by angle th: diag(e^{i th/2}, e^{-i th/2}); Moebius: z -> e^{i th} z
    n0 = bloch(state(z)); n1 = bloch(state(np.exp(1j * th) * z))
    R = np.array([[np.cos(th), np.sin(th), 0], [-np.sin(th), np.cos(th), 0], [0, 0, 1]])   # by -th: the chart z = v0/v1 has n_y = -2 Im z/(1+|z|^2)
    e_rot = max(e_rot, np.linalg.norm(n1 - R @ n0))
    # boost along Z by rapidity eta: diag(e^{eta/2}, e^{-eta/2}); Moebius: z -> e^{eta} z; Bloch n_z -> (n_z + tanh eta)/(1 + n_z tanh eta)
    n2 = bloch(state(np.exp(eta) * z)); t = np.tanh(eta)
    e_boost = max(e_boost, abs(n2[2] - (n0[2] + t) / (1 + n0[2] * t)))
print("   diag(e^{i th},1) rotates the Bloch vector about Z by -th:       max error %.2e" % e_rot)
print("   diag(e^{eta},1) boosts n_z by rapidity eta (aberration law):     max error %.2e" % e_boost)

# --- C: decoders from logical states
I2 = np.eye(2); X = sig[0]; Y = sig[1]; Z = sig[2]
PAULI = {"I": I2, "X": X, "Y": Y, "Z": Z}


def op(s):
    M = np.array([[1.0 + 0j]])
    for ch in s:
        M = np.kron(M, PAULI[ch])
    return M


def logical_states(stabs, n):
    Pi = np.eye(2 ** n, dtype=complex)
    for s in stabs:
        Pi = Pi @ (np.eye(2 ** n) + op(s)) / 2
    zero = Pi[:, 0]                              # Pi |0...0>
    zero = zero / np.linalg.norm(zero)
    one = op("X" * n) @ zero
    assert abs(np.vdot(zero, one)) < 1e-12
    assert np.linalg.norm(op("Z" * n) @ zero - zero) < 1e-12, "|0_L> must be +1 of Z^n"
    return zero, one


def decoder(zero, one, n):
    def f(z):
        psi = np.array([1.0 + 0j])
        for _ in range(n):
            psi = np.kron(psi, [z, 1])
        return np.vdot(zero, psi) / np.vdot(one, psi)
    return f


codes = {
    "Shor [[9,1,3]]": (["ZZIIIIIII", "IZZIIIIII", "IIIZZIIII", "IIIIZZIII", "IIIIIIZZI", "IIIIIIIZZ",
                        "XXXXXXIII", "IIIXXXXXX"], 9,
                       (lambda z: (z ** 9 + 3 * z ** 3) / (3 * z ** 6 + 1)), [0, 0, 0, 3, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 3, 0, 0, 0]),
    "five-qubit [[5,1,3]]": (["XZZXI", "IXZZX", "XIXZZ", "ZXIXZ"], 5,
                             (lambda z: (z ** 5 - 5 * z) / (5 * z ** 4 - 1)), [0, -5, 0, 0, 0, 1], [-1, 0, 0, 0, 5]),
    "Steane [[7,1,3]]": (["IIIXXXX", "IXXIIXX", "XIXIXIX", "IIIZZZZ", "IZZIIZZ", "ZIZIZIZ"], 7,
                         (lambda z: (z ** 7 + 7 * z ** 3) / (7 * z ** 4 + 1)), [0, 0, 0, 7, 0, 0, 0, 1], [1, 0, 0, 0, 7]),
}
print("C. meromorphic decoders rebuilt from the codes' logical states")
built = {}
for name, (stabs, n, fpaper, p, q) in codes.items():
    zero, one = logical_states(stabs, n)
    f = decoder(zero, one, n)
    zs = [rc() for _ in range(50)]
    ratios = np.array([f(z) / fpaper(z) for z in zs])
    const = ratios[0]
    err = np.max(np.abs(ratios / const - 1))
    print("   %-22s f_built / f_paper = %s (constant to %.1e)" % (name, np.round(const, 6), err))
    built[name] = (p, q, n)

# --- D: Riemann--Hurwitz and fixed points
print("D. Riemann--Hurwitz sum over branch points, including infinity")
all_rh = True


def branch_data(p, q):
    """Return (degree, list of (point, multiplicity)) for f = p/q, finite branch points
    from roots of p'q - pq' (grouped), plus the point at infinity from 1/f(1/z)."""
    d = max(len(p), len(q)) - 1
    num = P.polysub(P.polymul(P.polyder(p), q), P.polymul(p, P.polyder(q)))
    roots = P.polyroots(num)
    pts = []
    for r in roots:
        for i, (pt, m) in enumerate(pts):
            if abs(pt - r) < 1e-6:
                pts[i] = (pt, m + 1); break
        else:
            pts.append((r, 1))
    finite = [(pt, m + 1) for pt, m in pts]           # order-k zero of f' -> k+1 sheets
    # at infinity: the multiplicity of infinity in its own fibre.  deg p > deg q: f(inf) = inf,
    # m = deg p - deg q; deg p < deg q: f(inf) = 0, m = deg q - deg p; equal: f(inf) = c and
    # m = d - deg(p - c q).
    dp, dq = len(np.trim_zeros(p, 'b')) - 1, len(np.trim_zeros(q, 'b')) - 1
    if dp != dq:
        m_inf = abs(dp - dq)
    else:
        c = p[dp] / q[dq]
        m_inf = d - (len(np.trim_zeros(P.polysub(p, c * q), 'b')) - 1)
    return d, finite, m_inf


for name, (p, q, n) in built.items():
    p = np.array(p, float); q = np.array(q, float)
    d, finite, m_inf = branch_data(p, q)
    s = sum(m - 1 for _, m in finite) + (m_inf - 1)
    all_rh = all_rh and (s == 2 * (d - 1))
    r = P.polysub(p, P.polymul([0, 1], q))
    fixed = P.polyroots(r)
    print("   %-22s degree %d; finite branch points %d with sheets %s; at infinity %d sheets; sum(m-1) = %d, 2(d-1) = %d %s"
          % (name, d, len(finite), sorted(set(m for _, m in finite)), m_inf, s, 2 * (d - 1), "OK" if s == 2 * (d - 1) else "FAIL"))
    print("      fixed points r(z)=0: %s" % ", ".join(sorted("%s" % np.round(x, 4) for x in fixed)))
    if name.startswith("five"):
        fixed2 = P.polyroots(P.polysub(-p, P.polymul([0, 1], q)))
        print("      same decoder followed by logical Z (the +X^5 frame built above, f -> -f): fixed points %s"
              % ", ".join(sorted("%s" % np.round(x, 4) for x in fixed2)))

# --- E: Klein's octahedral function
def E7(z):
    return 108 * z ** 4 * (z ** 4 - 1) ** 4 / (z ** 8 + 14 * z ** 4 + 1) ** 3


eS, eH = 0.0, 0.0
for _ in range(500):
    z = rc()
    eS = max(eS, abs(E7(-1j * z) - E7(z)) / (1 + abs(E7(z))))
    eH = max(eH, abs(E7((z + 1) / (z - 1)) - E7(z)) / (1 + abs(E7(z))))
print("E. Klein's E7 invariant under S(z) = -iz (rel. err %.1e) and H(z) = (z+1)/(z-1) (rel. err %.1e)" % (eS, eH))
Fst = P.polyroots([1, 0, 0, 0, 14, 0, 0, 0, 1])
hst = 1 + np.sqrt(2)
print("   E7 at a stabilizer state (z=1): %.1e; at an H-state (1+sqrt2): %.12f; at an F-state: |E7| = %.1e (pole); E7(1/z)=E7(z): %.1e"
      % (abs(E7(1.0)), E7(hst).real, abs(E7(Fst[0] * (1 + 1e-9))), abs(E7(1 / (0.3 + 0.7j)) - E7(0.3 + 0.7j))))
# --- F: ramification of the n-leg spiders
print("F. n-leg spiders: the Z (GHZ) spider is branched at the copyable states, the W spider is not")
ok_F = True
for n in (2, 3, 4, 5):
    # Z spider, n inputs, 1 output: |0><0|^{(x)n} + |1><1|^{(x)n}; W spider: |0><weight n-1 strings| + |1><1^n|
    dim = 2 ** n
    Zn = np.zeros((2, dim), complex); Wn = np.zeros((2, dim), complex)
    Zn[0, 0] = 1; Zn[1, dim - 1] = 1
    for k in range(dim):
        bits = bin(k).count("1")
        if bits == n - 1:
            Wn[0, k] = 1
    Wn[1, dim - 1] = 1
    zs = [rc() for _ in range(n)]
    seg = np.array([1.0 + 0j])
    for z in zs:
        seg = np.kron(seg, [z, 1])
    vZ, vW = Zn @ seg, Wn @ seg
    eZ = abs(vZ[0] / vZ[1] - np.prod(zs)); eW = abs(vW[0] / vW[1] - np.sum(zs))
    # univariate: z^n and n z; branch data of z^n = [0,...,0,1]/[1]
    d, finite, m_inf = branch_data(np.array([0.0] * n + [1.0]), np.array([1.0]))
    rh = sum(m - 1 for _, m in finite) + (m_inf - 1)
    dW, finW, mW = branch_data(np.array([0.0, float(n)]), np.array([1.0]))
    ok_F = ok_F and eZ < 1e-12 and eW < 1e-12 and rh == 2 * (d - 1) and dW == 1 and not finW and mW == 1
    print("   n=%d  Z -> prod z_i (err %.1e): degree %d, branch points %s + infinity with %d sheets, sum(m-1)=%d=2(d-1); "
          "W -> sum z_i (err %.1e): degree %d, no branch points" % (n, eZ, d, [(round(pt.real, 6), m) for pt, m in finite], m_inf, rh, eW, dW))
print("=" * 72)
print("BURTON--ANWAR CHECKS: PASS" if all(v < 1e-10 for v in worst.values()) and e_vel < 1e-10 and e_rot < 1e-10 and e_boost < 1e-10 and eS < 1e-8 and eH < 1e-8 and all_rh and ok_F else "BURTON--ANWAR CHECKS: FAIL")
