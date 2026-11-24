#!/usr/bin/env python3
"""qutrit_hopf_picture_2026-11-07T1600.py

JS (2026-11-07): "tell me about qutrits in the Hopf fibration picture."

Finite checks for the companion note
knowledge/sessions/qutrit_hopf_picture_2026-11-07T1600.md.  Conventions are
the paper's own (appendix_ghz_w_proofs_2026-06-11.tex, app:setup):
Cayley--Dickson (a,b)(c,d) = (ac - conj(d) b, da + b conj(c)), e_1 the
preferred unit, J = L_{e_1}, the embedding c_k = x_k + i y_k ->
x_k e_{2k} + y_k J(e_{2k}) with J(e_6) = -e_7, the Hopf map
h(o_1, o_2) = (2 o_1 conj(o_2), |o_1|^2 - |o_2|^2).

Part A  The base S^8 is (Bloch vector of the split qubit) + (colour C^3)
        with the colour radius squared equal to the one-tangle:
        4 |pi_{C^3}(h)|^2 = 4 det rho_1 = 1 - r_1^2.  GHZ -> unit colour
        vector; W -> colour radius sqrt(8/9), Bloch radius 1/3; product ->
        colour 0.  So S^8 is the join S^2 * S^5 and the qutrit's sphere
        S^5 is the budget-exhausted equator.
Part B  The qutrit's own phase fibration S^1 -> S^5 -> CP^2: the fibre is
        left multiplication by the record circle exp(theta e_1), which is
        the quantum global phase of a branch and the scalar exp(i theta) on
        the colour C^3; its automorphism subgroup is the centre Z_3.  How
        the global phase of the three-qubit state moves the colour vector
        (reported, not assumed).
Part C  Colour SU(3) on the register: an element of the e_1-stabiliser of
        G_2 acts on each branch C^4 as a unitary fixing the record
        amplitude and lying in SU(3) on the complementary qutrit; the Hopf
        image's colour vector transforms in the fundamental; the unitary is
        entangling on the two internal qubits.  Local unitaries on the two
        internal qubits act on the colour vector by a real-linear map that
        is not complex-linear (reported).
Part D  The three-quark singlet epsilon(v_1, v_2, v_3) = det[v_1 v_2 v_3] on
        colour vectors is the octonionic associative 3-form <v_1, v_2 v_3>
        plus i times a record-line component of the associator: the exact
        coefficients are fitted over random triples and then checked to
        1e-12.  The meson singlet is the C-part of conj(v) w.
Part E  Two qutrits: the CGLMP inequality's maximal violation is not at the
        maximally entangled state (Acin, Durt, Gisin and Latorre 2002):
        2.8729 at gamma = 1, maximum about 2.9149 near gamma = 0.79.
Part F  The qutrit's Bloch body is not a ball: pure states have |n| = 1 but
        -n is not a state; the fraction of directions that are states falls
        from 1 inside radius 1/2 to 0 at radius 1; three orthogonal pure
        states form an equilateral triangle, not antipodes.

Pure numpy; seed 20261107.  Exact stdout is pasted into the session note.
"""
import itertools
import math

import numpy as np

rng = np.random.default_rng(20261107)
np.set_printoptions(precision=6, suppress=True, linewidth=120)
FAILS = []


def check(name, cond, detail=""):
    tag = "ok  " if cond else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILS.append(name)


# --------------------------------------------------------------------------
# octonions, Convention A (the paper's table)
# --------------------------------------------------------------------------
def conj_o(x):
    y = np.array(x, copy=True); y[1:] = -y[1:]; return y


def cd(x, y):
    n = x.size
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate((cd(a, c) - cd(conj_o(d), b), cd(d, a) + cd(b, conj_o(c))))


E8 = np.eye(8)
T = np.array([[cd(E8[i], E8[j]) for j in range(8)] for i in range(8)])
J = T[1].T.copy()                                   # J[a,b] = component a of e_1 e_b
check("the paper's table: e_1 e_2 = e_3, e_1 e_4 = e_5, e_1 e_7 = e_6 (so J e_6 = -e_7), e_2 e_4 = e_6",
      np.allclose(T[1, 2], E8[3]) and np.allclose(T[1, 4], E8[5]) and np.allclose(T[1, 7], E8[6]) and np.allclose(T[2, 4], E8[6]))
check("J = L_{e_1} squares to -1 on O", np.allclose(J @ J, -np.eye(8)))
BLOCKS = [(0, 1, 1), (2, 3, 1), (4, 5, 1), (6, 7, -1)]          # c_k -> x e_a + s y e_b


def embed(c4):
    o = np.zeros(8)
    for k, (a, b, s) in enumerate(BLOCKS):
        o[a] = c4[k].real; o[b] = s * c4[k].imag
    return o


def unembed(o):
    return np.array([o[a] + 1j * s * o[b] for a, b, s in BLOCKS])


def colour_c3(o):
    """the colour C^3 part of an octonion, as a complex 3-vector in the block pairing"""
    return unembed(o)[1:]


def hopf(psi):
    o1, o2 = embed(psi[:4]), embed(psi[4:])
    hh = cd(o1, conj_o(o2))
    z = float(o1 @ o1 - o2 @ o2)
    return o1, o2, hh, z


def rand_state(n):
    v = rng.normal(size=n) + 1j * rng.normal(size=n)
    return v / np.linalg.norm(v)


def rho_first(psi):
    M = psi.reshape(2, 4)
    return M @ M.conj().T


def haar_unitary(n):
    Z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / math.sqrt(2)
    Q, R = np.linalg.qr(Z)
    return Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))


# ==========================================================================
print("=== Part A: the Hopf base is (Bloch vector) + (colour C^3) with colour radius^2 = one-tangle ===")
# ==========================================================================
ok_comp = ok_lemma = ok_bloch = ok_tangle = ok_sphere = True
worst = 0.0
for _ in range(2000):
    psi = rand_state(8)
    o1, o2, hh, z = hopf(psi)
    c, d = psi[:4], psi[4:]
    piC = hh[0] + 1j * hh[1]
    ok_comp &= abs(hh @ hh - (o1 @ o1) * (o2 @ o2)) < 1e-12
    ok_lemma &= abs(piC - np.conj(np.vdot(c, d))) < 1e-12          # lemma cproj: conj of sum conj(c_k) d_k
    rho = rho_first(psi)
    rz = (rho[0, 0] - rho[1, 1]).real
    rx, ry = 2 * rho[0, 1].real, -2 * rho[0, 1].imag               # rho_01 = (r_x - i r_y)/2
    ok_bloch &= abs(z - rz) < 1e-12 and abs(2 * piC.real - rx) < 1e-12 and abs(-2 * piC.imag - ry) < 1e-12
    r2 = rx * rx + ry * ry + rz * rz
    colour2 = 4 * float(hh[2:] @ hh[2:])
    tau = 4 * np.linalg.det(rho).real
    ok_tangle &= abs(colour2 - tau) < 1e-12 and abs(colour2 - (1 - r2)) < 1e-12
    ok_sphere &= abs(z * z + 4 * abs(piC) ** 2 + colour2 - 1) < 1e-12
    worst = max(worst, abs(colour2 - tau))
check("composition identity |o_1 conj(o_2)|^2 = |o_1|^2 |o_2|^2 on 2000 random states", ok_comp)
check("lemma cproj: pi_C(h) = conj <psi_0, psi_1> (antilinear in the first slot)", ok_lemma)
check("(z, 2 Re pi_C, -2 Im pi_C) is the first qubit's Bloch vector (r_z, r_x, r_y)", ok_bloch)
check("colour radius squared 4|pi_{C^3}(h)|^2 = 4 det rho_1 = 1 - r_1^2 = the one-tangle", ok_tangle, f"max deviation {worst:.1e}")
check("base point lies on S^8: z^2 + |Bloch_xy|^2 + colour^2 = 1", ok_sphere)


def ket(bits):
    v = np.zeros(8, complex); v[int(bits, 2)] = 1; return v


GHZ = (ket("000") + ket("111")) / math.sqrt(2)
W = (ket("001") + ket("010") + ket("100")) / math.sqrt(3)
PROD = ket("000")
print(f"  {'state':8s} {'z':>7s} {'|2 pi_C|':>9s} {'colour radius':>14s}  colour vector 2 pi_{{C^3}}(h) as C^3")
for name, psi in [("GHZ", GHZ), ("W", W), ("|000>", PROD)]:
    o1, o2, hh, z = hopf(psi)
    print(f"  {name:8s} {z:7.4f} {2 * abs(hh[0] + 1j * hh[1]):9.4f} {2 * np.linalg.norm(hh[2:]):14.6f}  {np.round(2 * colour_c3(hh), 4)}")
_, _, hG, zG = hopf(GHZ); _, _, hW, zW = hopf(W); _, _, hP, zP = hopf(PROD)
check("GHZ: z = 0, pi_C = 0, unit colour vector (-e_6, the third colour line)",
      abs(zG) < 1e-12 and abs(hG[0]) + abs(hG[1]) < 1e-12 and np.allclose(2 * hG[2:], -E8[6][2:]))
check("W: z = 1/3, pi_C = 0, colour radius sqrt(8/9)",
      abs(zW - 1 / 3) < 1e-12 and abs(hW[0]) + abs(hW[1]) < 1e-12 and abs(4 * (hW[2:] @ hW[2:]) - 8 / 9) < 1e-12)
check("product: colour radius 0, Bloch radius 1", np.linalg.norm(hP[2:]) < 1e-12 and abs(zP - 1) < 1e-12)
print("  so S^8 = { (Bloch vector b, colour vector v) : |b|^2 + |v|^2 = 1 } = the join S^2 * S^5;")
print("  the qutrit's sphere S^5 (unit colour vectors) is the budget-exhausted equator, r_1 = 0.")

# ==========================================================================
print()
print("=== Part B: the qutrit's phase fibration S^1 -> S^5 -> CP^2 and the record circle ===")
# ==========================================================================


def rec_phase(theta):
    """left multiplication by exp(theta e_1) as an 8x8 real matrix"""
    return math.cos(theta) * np.eye(8) + math.sin(theta) * J


ok_phase = ok_scalar = ok_inside = True
for _ in range(200):
    th = rng.uniform(0, 2 * math.pi)
    c4 = rand_state(4)
    ok_phase &= np.allclose(embed(np.exp(1j * th) * c4), rec_phase(th) @ embed(c4))
    v = np.zeros(8); v[2:] = rng.normal(size=6)
    pv = rec_phase(th) @ v
    ok_inside &= abs(pv[0]) + abs(pv[1]) < 1e-12
    ok_scalar &= np.allclose(colour_c3(pv), np.exp(1j * th) * colour_c3(v))
check("left multiplication by exp(theta e_1) is the quantum global phase of a branch", ok_phase)
check("it preserves the colour C^3 and acts there as the scalar exp(i theta): the qutrit's phase circle", ok_inside and ok_scalar)


def aut_residual(P):
    return max(np.linalg.norm(P @ T[i, j] - cd(P @ E8[i], P @ E8[j])) for i in range(8) for j in range(8))


def colour_phase(theta):
    P = np.eye(8); P[2:, 2:] = rec_phase(theta)[2:, 2:]; return P


res = {th: aut_residual(colour_phase(th)) for th in (0.0, 2 * math.pi / 3, 4 * math.pi / 3, math.pi / 2, 1.0)}
check("the phase circle's automorphism subgroup is the centre Z_3 (residual 0 at the cube roots, > 0.1 elsewhere)",
      max(res[0.0], res[2 * math.pi / 3], res[4 * math.pi / 3]) < 1e-12 and min(res[math.pi / 2], res[1.0]) > 0.1)

# how the global phase of the three-qubit state moves the colour vector
print("  global phase psi -> exp(i theta) psi on the Hopf image (random states):")
dev_same = dev_plus = dev_minus = 0.0
proj_min = 1.0
for _ in range(300):
    psi = rand_state(8); th = rng.uniform(0, 2 * math.pi)
    _, _, h0, z0 = hopf(psi); _, _, h1, z1 = hopf(np.exp(1j * th) * psi)
    v0, v1 = colour_c3(h0), colour_c3(h1)
    dev_same = max(dev_same, np.linalg.norm(v1 - v0))
    dev_plus = max(dev_plus, np.linalg.norm(v1 - np.exp(2j * th) * v0))
    dev_minus = max(dev_minus, np.linalg.norm(v1 - np.exp(-2j * th) * v0))
    proj_min = min(proj_min, abs(np.vdot(v0, v1)) / (np.linalg.norm(v0) * np.linalg.norm(v1)))
print(f"    max |v' - v| = {dev_same:.3f}; max |v' - e^(2i theta) v| = {dev_plus:.3f}; max |v' - e^(-2i theta) v| = {dev_minus:.3f}")
print(f"    min over samples of |<v, v'>|/(|v||v'|) = {proj_min:.4f}  (1 would mean the colour direction in CP^2 is phase-invariant)")
# the coloured-GHZ family |0>|00> + |1>|c>
ok_cg = True; proj_cg = 1.0
for _ in range(100):
    cvec = rand_state(3); th = rng.uniform(0, 2 * math.pi)
    psi = np.zeros(8, complex); psi[0] = 1 / math.sqrt(2); psi[5:8] = cvec / math.sqrt(2)
    _, _, h0, _ = hopf(psi); _, _, h1, _ = hopf(np.exp(1j * th) * psi)
    v0, v1 = 2 * colour_c3(h0), 2 * colour_c3(h1)
    ok_cg &= np.allclose(v0, -cvec) and np.allclose(v1, np.exp(2j * th) * v0)
    proj_cg = min(proj_cg, abs(np.vdot(v0, v1)) / (np.linalg.norm(v0) * np.linalg.norm(v1)))
check("coloured GHZ |0>|00> + |1>|c>: colour vector = -c exactly, and the global phase rotates it by e^(2i theta)", ok_cg)
print(f"    on that family the colour direction in CP^2 is phase-invariant: min |<v,v'>|/|v||v'| = {proj_cg:.6f}")
print("  reading: the Hopf base is a function of the vector, not of the ray (as for two qubits, where the")
print("  concurrence coordinate rotates by e^(2i theta)); the LU-invariant content of the colour vector is its radius.")

# ==========================================================================
print()
print("=== Part C: colour SU(3) acts on the register as an entangling unitary of the two internal qubits ===")
# ==========================================================================


def derivations():
    rows = []
    for i in range(8):
        for j in range(8):
            M = np.zeros((8, 64))
            for a in range(8):
                for b in range(8):
                    col = a * 8 + b
                    M[a, col] += T[i, j, b]
                    if b == i:
                        M[:, col] -= T[a, j, :]
                    if b == j:
                        M[:, col] -= T[i, a, :]
            rows.append(M)
    Mfull = np.vstack(rows)
    u, sv, vt = np.linalg.svd(Mfull)
    nullity = int((sv < 1e-10).sum()) + (64 - sv.size)
    return [v.reshape(8, 8) for v in vt[64 - nullity:]]


Ders = derivations()
C1 = np.array([D[:, 1] for D in Ders]).T
u2, s2, vt2 = np.linalg.svd(C1)
nul2 = len(Ders) - int((s2 > 1e-10).sum())
Stab = [sum(c * D for c, D in zip(vt2[len(Ders) - nul2 + i], Ders)) for i in range(nul2)]
check("dim Der(O) = 14 and dim Stab(e_1) = 8", len(Ders) == 14 and len(Stab) == 8)


def expm(M, squarings=12, terms=30):
    S = M / (2 ** squarings)
    R = np.eye(M.shape[0]); term = np.eye(M.shape[0])
    for k in range(1, terms):
        term = term @ S / k; R = R + term
    for _ in range(squarings):
        R = R @ R
    return R


def complex_matrix(g):
    """the 4x4 complex matrix of a J-commuting real-linear map g on O = C^4 (block pairing)"""
    return np.array([unembed(g @ embed(np.eye(4)[k])) for k in range(4)]).T


def op_schmidt_rank(U4):
    """operator-Schmidt rank of a 4x4 operator across the two-qubit cut"""
    R = U4.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4)
    return int((np.linalg.svd(R, compute_uv=False) > 1e-9).sum())


def concurrence_pure2(v):
    m = v.reshape(2, 2)
    return 2 * abs(np.linalg.det(m))


hdr = ["trial", "aut res", "[g,J]", "unitary", "fixes rec", "det U3", "op-Schmidt", "C(U|01>)", "v'=U3 v"]
print("  " + " ".join(f"{h:>{w}s}" for h, w in zip(hdr, (5, 9, 8, 8, 10, 14, 11, 9, 8))))
ok_C = True
for t in range(3):
    D = sum(rng.normal() * X for X in Stab)
    g = expm(D)
    res_aut = aut_residual(g)
    commJ = np.linalg.norm(g @ J - J @ g)
    Ug = complex_matrix(g)
    unit = np.linalg.norm(Ug @ Ug.conj().T - np.eye(4))
    fixes = np.allclose(Ug[:, 0], np.eye(4)[0]) and np.allclose(Ug[0, :], np.eye(4)[0])
    U3 = Ug[1:, 1:]
    det3 = np.linalg.det(U3)
    rank = op_schmidt_rank(Ug)
    conc = concurrence_pure2(Ug @ np.array([0, 1, 0, 0], complex))
    # equivariance of the Hopf colour vector
    ok_eq = True
    for _ in range(50):
        psi = rand_state(8)
        psi_g = np.concatenate((Ug @ psi[:4], Ug @ psi[4:]))
        _, _, h0, z0 = hopf(psi); _, _, h1, z1 = hopf(psi_g)
        ok_eq &= np.allclose(h1, g @ h0) and abs(z1 - z0) < 1e-12 and np.allclose(colour_c3(h1), U3 @ colour_c3(h0))
    print(f"  {t:5d} {res_aut:9.1e} {commJ:8.1e} {unit:8.1e} {str(fixes):>10s} {det3.real:+.6f}{det3.imag:+.1e}j {rank:11d} {conc:9.4f} {str(ok_eq):>8s}")
    ok_C &= res_aut < 1e-10 and commJ < 1e-10 and unit < 1e-10 and fixes and abs(det3 - 1) < 1e-10 and rank > 1 and conc > 1e-3 and ok_eq
check("exp(su(3)_{e_1}) acts on each branch as a unitary fixing the record amplitude, in SU(3) on the qutrit |00>^perp,"
      " entangling across the two internal qubits, and the Hopf colour vector transforms in the fundamental", ok_C)

# contrast: local unitaries on the internal qubits, and a Haar unitary on C^4


def induced_map_fit(U, nsamp=400):
    X, Y, X9, Y9 = [], [], [], []
    for _ in range(nsamp):
        psi = rand_state(8)
        psi2 = np.concatenate((U @ psi[:4], U @ psi[4:]))
        _, _, h0, z0 = hopf(psi); _, _, h1, z1 = hopf(psi2)
        X.append(h0[2:]); Y.append(h1[2:])
        X9.append(np.concatenate(([z0], 2 * h0))); Y9.append(np.concatenate(([z1], 2 * h1)))
    return np.array(X), np.array(Y), np.array(X9), np.array(Y9)


print("  the induced action on the Hopf image, for ONE fixed unitary applied to both branches (reported, not assumed):")
for label, U in [("U_2 x U_3 local on the internal qubits", np.kron(haar_unitary(2), haar_unitary(2))),
                 ("Haar U(4) on the internal qubits", haar_unitary(4))]:
    X, Y, X9, Y9 = induced_map_fit(U)
    M = np.linalg.lstsq(X, Y, rcond=None)[0].T
    pred_err = np.max(np.abs(Y - X @ M.T))
    M9 = np.linalg.lstsq(X9, Y9, rcond=None)[0].T
    pred9 = np.max(np.abs(Y9 - X9 @ M9.T))
    norm_pres = np.max(np.abs(np.linalg.norm(Y, axis=1) - np.linalg.norm(X, axis=1)))
    print(f"    {label}: colour radius preserved to {norm_pres:.1e}; best linear fit v' = M v has max residual {pred_err:.2f};"
          f" best linear fit on the whole base point (z, 2h) has max residual {pred9:.2f}")
    print("    -> the colour vector's direction is not a function of the base point under this unitary; only its radius is invariant")
check("local unitaries on the internal qubits preserve the colour radius (the one-tangle) but do not act linearly on the colour vector",
      norm_pres < 1e-9 and pred_err > 1e-3)

# ==========================================================================
print()
print("=== Part D: the three-quark singlet is the octonionic 3-form plus the record component of the associator ===")
# ==========================================================================


def rand_colour():
    v = np.zeros(8); v[2:] = rng.normal(size=6); return v


rows_fit, dets = [], []
for _ in range(300):
    v1, v2, v3 = rand_colour(), rand_colour(), rand_colour()
    detC = np.linalg.det(np.array([colour_c3(v1), colour_c3(v2), colour_c3(v3)]).T)
    phi = float(v1 @ cd(v2, v3))                                      # associative 3-form <v1, v2 v3>
    assoc = cd(cd(v1, v2), v3) - cd(v1, cd(v2, v3))
    a1 = float(assoc[1])                                              # record-line component of the associator
    b1 = float(cd(cd(v1, v2), v3)[1])                                 # e_1 component of (v1 v2) v3
    c1 = float(cd(v1, cd(v2, v3))[1])                                 # e_1 component of v1 (v2 v3)
    rows_fit.append([phi, a1, b1, c1]); dets.append(detC)
A = np.array(rows_fit); dets = np.array(dets)
coef_re = np.linalg.lstsq(A[:, :1], dets.real, rcond=None)[0]
coef_im_assoc = np.linalg.lstsq(A[:, 1:2], dets.imag, rcond=None)[0]
coef_im_b = np.linalg.lstsq(A[:, 2:3], dets.imag, rcond=None)[0]
coef_im_c = np.linalg.lstsq(A[:, 3:4], dets.imag, rcond=None)[0]
print(f"  Re det = alpha <v1, v2 v3>:            alpha = {coef_re[0]:+.6f}, max residual {np.max(np.abs(dets.real - A[:, 0] * coef_re[0])):.1e}")
print(f"  Im det = beta  e_1 . [v1, v2, v3]:      beta  = {coef_im_assoc[0]:+.6f}, max residual {np.max(np.abs(dets.imag - A[:, 1] * coef_im_assoc[0])):.1e}")
print(f"  Im det = beta' e_1 . ((v1 v2) v3):      beta' = {coef_im_b[0]:+.6f}, max residual {np.max(np.abs(dets.imag - A[:, 2] * coef_im_b[0])):.1e}")
print(f"  Im det = beta'' e_1 . (v1 (v2 v3)):     beta''= {coef_im_c[0]:+.6f}, max residual {np.max(np.abs(dets.imag - A[:, 3] * coef_im_c[0])):.1e}")
alpha = round(coef_re[0] * 2) / 2
beta = round(coef_im_assoc[0] * 2) / 2
ok_D = (np.max(np.abs(dets.real - A[:, 0] * alpha)) < 1e-12 and np.max(np.abs(dets.imag - A[:, 1] * beta)) < 1e-12)
check(f"epsilon(v1,v2,v3) = ({alpha:+.1f}) <v1, v2 v3> + i ({beta:+.1f}) e_1.[v1,v2,v3] exactly on 300 random triples", ok_D)
# the associator of three colour vectors has no colour component? report its support
supp = np.zeros(8)
for _ in range(100):
    v1, v2, v3 = rand_colour(), rand_colour(), rand_colour()
    supp = np.maximum(supp, np.abs(cd(cd(v1, v2), v3) - cd(v1, cd(v2, v3))))
print("  support of the associator of three colour vectors, max |component| by basis unit:", np.round(supp, 3))
# meson: the Hermitian inner product as the C-part of conj(v) w
ok_meson = True
for _ in range(200):
    v, w = rand_colour(), rand_colour()
    hp = np.vdot(colour_c3(v), colour_c3(w))                          # sum conj(v_k) w_k
    cw = cd(conj_o(w), v)
    ok_meson &= abs((cw[0] + 1j * cw[1]) - hp) < 1e-12
check("meson singlet <v, w>_C = pi_C(conj(w) v), the conjugate pattern of lemma cproj", ok_meson)
# the octonion product of two colours: C-part and colour part
ok_cross = True
for _ in range(200):
    v, w = rand_colour(), rand_colour()
    vw = cd(v, w)
    cv, cw_ = colour_c3(v), colour_c3(w)
    ok_cross &= abs((vw[0] + 1j * vw[1]) + np.conj(np.vdot(cv, cw_))) < 1e-12          # pi_C(v w) = -conj <v, w>_C
    ok_cross &= np.allclose(colour_c3(vw), np.conj(np.cross(cv, cw_)))                  # colour(v w) = conj(v x w)
check("for colours v, w: pi_C(v w) = -conj<v,w>_C and colour(v w) = conj(v x w): the octonions are C + C^3 with the conjugate cross product", ok_cross)
# unitary colour frames: closure under multiplication and the phase of the singlet
print("  unitary colour frames F = [v1 v2 v3], det F = e^(i alpha): closure v1 v2 = e^(-i alpha) v3 and Re det = phi")
ok_frame = True
for t in range(5):
    F = haar_unitary(3)
    alpha = np.angle(np.linalg.det(F))
    vs = []
    for k in range(3):
        o = np.zeros(8)
        for j, (a, b, sg) in enumerate(BLOCKS[1:]):
            o[a] = F[j, k].real; o[b] = sg * F[j, k].imag
        vs.append(o)
    v1, v2, v3 = vs
    c12 = colour_c3(cd(v1, v2)); c23 = colour_c3(cd(v2, v3)); c31 = colour_c3(cd(v3, v1))
    closure = (np.allclose(c12, np.exp(-1j * alpha) * F[:, 2]) and np.allclose(c23, np.exp(-1j * alpha) * F[:, 0])
               and np.allclose(c31, np.exp(-1j * alpha) * F[:, 1]))
    phi = float(v1 @ cd(v2, v3)); assoc1 = float((cd(cd(v1, v2), v3) - cd(v1, cd(v2, v3)))[1])
    ok_frame &= closure and abs(phi - math.cos(alpha)) < 1e-12 and abs(assoc1 / 2 - math.sin(alpha)) < 1e-12
    if t < 3:
        print(f"    frame {t}: alpha = {alpha:+.4f}; closure {closure}; phi = {phi:+.6f} = cos alpha; e_1.[v1,v2,v3]/2 = {assoc1 / 2:+.6f} = sin alpha")
check("a unitary colour frame closes under octonion multiplication up to the phase of its determinant; det = 1 iff the triple is a quaternionic (associative) triple",
      ok_frame)
# the SU(3) singlet frame IS a quaternionic subalgebra: 1, v1, v2, v3 closed
F = haar_unitary(3); F = F / np.linalg.det(F) ** (1 / 3)
vs = []
for k in range(3):
    o = np.zeros(8)
    for j, (a, b, sg) in enumerate(BLOCKS[1:]):
        o[a] = F[j, k].real; o[b] = sg * F[j, k].imag
    vs.append(o)
basis = np.array([E8[0]] + vs)
closed = True
for x in basis:
    for y in basis:
        coeffs = np.linalg.lstsq(basis.T, cd(x, y), rcond=None)[0]
        closed &= np.allclose(basis.T @ coeffs, cd(x, y))
check("an SU(3) frame (det 1) spans, with e_0, a quaternion subalgebra of O: the colour singlet is a copy of H",
      closed and abs(np.linalg.det(F) - 1) < 1e-12)

# ==========================================================================
print()
print("=== Part E: two qutrits -- the CGLMP maximum is not at the maximally entangled state ===")
# ==========================================================================
w3 = np.exp(2j * np.pi / 3)


def basis_A(alpha):
    return np.array([[np.exp(2j * np.pi * j * (k + alpha) / 3) / math.sqrt(3) for j in range(3)] for k in range(3)])  # rows: |k>


def basis_B(beta):
    return np.array([[np.exp(2j * np.pi * j * (-l + beta) / 3) / math.sqrt(3) for j in range(3)] for l in range(3)])


A1, A2 = basis_A(0.0), basis_A(0.5)
B1, B2 = basis_B(0.25), basis_B(-0.25)


def joint(psi2, BA, BB):
    P = np.zeros((3, 3))
    for k in range(3):
        for l in range(3):
            P[k, l] = abs(np.kron(BA[k], BB[l]).conj() @ psi2) ** 2
    return P


def P_eq(P, shift):
    """P(A = B + shift mod 3)"""
    return sum(P[(l + shift) % 3, l] for l in range(3))


def I3(psi2):
    P11, P12, P21, P22 = joint(psi2, A1, B1), joint(psi2, A1, B2), joint(psi2, A2, B1), joint(psi2, A2, B2)
    plus = P_eq(P11, 0) + P_eq(P21, -1) + P_eq(P22, 0) + P_eq(P12, 0)
    minus = P_eq(P11, -1) + P_eq(P21, 0) + P_eq(P22, -1) + P_eq(P12, 1)
    return plus - minus


def psi_gamma(g):
    v = np.zeros(9, complex); v[0] = 1; v[4] = g; v[8] = 1
    return v / np.linalg.norm(v)


I_me = I3(psi_gamma(1.0))
gs = np.linspace(0.3, 1.5, 1201)
vals = np.array([I3(psi_gamma(g)) for g in gs])
g_best = gs[np.argmax(vals)]
# refine by golden section around the grid maximum
lo, hi = g_best - 0.002, g_best + 0.002
for _ in range(60):
    m1 = hi - 0.618034 * (hi - lo); m2 = lo + 0.618034 * (hi - lo)
    if I3(psi_gamma(m1)) < I3(psi_gamma(m2)):
        lo = m1
    else:
        hi = m2
g_opt = (lo + hi) / 2; I_opt = I3(psi_gamma(g_opt))
print(f"  I_3 at the maximally entangled state (gamma = 1): {I_me:.6f}   (local bound 2; 4/(6 sqrt3 - 9) = {4 / (6 * math.sqrt(3) - 9):.6f})")
print(f"  I_3 maximised over the family (|00> + gamma|11> + |22>): {I_opt:.6f} at gamma = {g_opt:.5f}")
check("CGLMP: 2.8729 at gamma = 1 with the standard settings", abs(I_me - 4 / (6 * math.sqrt(3) - 9)) < 1e-9)
check("the maximum over the family exceeds the maximally entangled value and sits at gamma != 1 (about 0.79)",
      I_opt > I_me + 0.03 and abs(g_opt - 0.79) < 0.02)
# the qubit contrast: CHSH is maximal at the maximally entangled state (stated, standard)

# ==========================================================================
print()
print("=== Part F: the qutrit's Bloch body is not a ball ===")
# ==========================================================================
GM = [np.array(m, complex) for m in [
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], np.diag([1, 1, -2]) / math.sqrt(3)]]


def rho_of_n(n):
    return (np.eye(3) + math.sqrt(3) * sum(ni * L for ni, L in zip(n, GM))) / 3


def n_of_rho(rho):
    return np.array([np.trace(rho @ L).real for L in GM]) * math.sqrt(3) / 2


ok_pure = True; mins = []
for _ in range(200):
    psi = rand_state(3); rho = np.outer(psi, psi.conj()); n = n_of_rho(rho)
    ok_pure &= abs(np.linalg.norm(n) - 1) < 1e-12 and np.allclose(rho_of_n(n), rho)
    mins.append(np.linalg.eigvalsh(rho_of_n(-n)).min())
check("pure qutrit states have Bloch radius 1 in the normalisation rho = (I + sqrt3 n.lambda)/3", ok_pure)
check("the antipode -n of a pure state is not a state: its smallest eigenvalue is -1/3", max(abs(m + 1 / 3) for m in mins) < 1e-12)
print(f"  {'radius':>7s} {'fraction of random directions that are states':>46s}")
for rad in (0.4, 0.5, 0.55, 0.7, 0.9, 1.0):
    cnt = 0; N = 4000
    for _ in range(N):
        n = rng.normal(size=8); n *= rad / np.linalg.norm(n)
        cnt += np.linalg.eigvalsh(rho_of_n(n)).min() >= -1e-12
    print(f"  {rad:7.2f} {cnt / N:46.4f}")
# orthogonal triple
ns = [n_of_rho(np.outer(e, e.conj())) for e in np.eye(3, dtype=complex)]
gram = np.array([[a @ b for b in ns] for a in ns])
print("  Gram matrix of the Bloch vectors of three orthogonal pure states:\n", np.round(gram, 4))
check("three orthogonal pure states form an equilateral triangle (pairwise inner product -1/2), not antipodes (-1)",
      np.allclose(gram, 1.5 * np.eye(3) - 0.5))

print()
if FAILS:
    print(f"QUTRIT HOPF PICTURE: FAIL ({len(FAILS)}): " + "; ".join(FAILS))
else:
    print("QUTRIT HOPF PICTURE: PASS")
