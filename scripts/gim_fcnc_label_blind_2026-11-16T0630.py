#!/usr/bin/env python3
"""GIM and flavour-changing neutral currents on the generation label.

Session note: knowledge/sessions/gim_fcnc_label_blind_2026-11-16T0630.md

Part A (structure, exact linear algebra on the 3-dim generation label space):
  A1  tree level: V^dag (c 1) V = c 1; the three-quark world of 1970 fails
      because T_3 is not proportional to 1 on (d', s'); charge always is.
  A2  loop level: offdiag(V^dag F(D) V) depends only on differences of F and
      is bounded by half the spread of F.
  A3  weak-basis form: the loop insertion is F(H_u) seen from the down mass
      basis; flavour change <=> [H_u, H_d] != 0.
  A4  the paper's circulant mass forms in a common label basis commute, so
      they give V = permutation: no mixing, no loop FCNC, no CP violation.
  A5  Jarlskog: det[H_u, H_d] = 2 i J prod(mass-squared differences).
  A6  the all-ones matrix J is a polynomial in the Koide circulant, i.e. a
      function of the mass operator (a Higgs-like, not a gauge-like, coupling).
Part B (numbers, PDG 2024 inputs; one-loop leading-order estimates only):
  B1  cos(2/9), sin(2/9) against |V_ud|, |V_us|; first-row unitarity.
  B2  size of the GIM suppression: K mixing with and without the cancellation.
  B3  B_s -> mu mu from the top-loop function, against Bobeth et al. 2014.
  B4  floors: t -> c Z scaling and mu -> e gamma.

Pure numpy, fixed seed, no hidden state.  Final line: PASS or FAIL.
"""
import math
import numpy as np

SEED = 20261116
rng = np.random.default_rng(SEED)
np.set_printoptions(precision=5, suppress=True, linewidth=120)
results = []


def check(name, ok, detail=""):
    results.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def haar_unitary(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def offdiag(a):
    return a - np.diag(np.diag(a))


def ckm(s12, s13, s23, delta):
    c12, c13, c23 = (math.sqrt(1 - s * s) for s in (s12, s13, s23))
    e = np.exp(1j * delta)
    return np.array([
        [c12 * c13, s12 * c13, s13 / e],
        [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])


def circulant(alpha2, delta):
    """Paper eq. (z3) as a matrix: unit diagonal, off-diagonals (alpha/2) e^{+-i delta}."""
    rho = math.sqrt(alpha2) / 2
    C = np.roll(np.eye(3), 1, axis=0)
    u = np.exp(1j * delta)
    return np.eye(3) + rho * (u * C + np.conj(u) * C.T)


print(f"seed {SEED}")
print("\n== A1  tree level ==")
V = haar_unitary(3)
dev = np.abs(V.conj().T @ (0.37 * np.eye(3)) @ V - 0.37 * np.eye(3)).max()
check("V^dag (c 1) V = c 1 for a Haar V", dev < 1e-14, f"max deviation {dev:.1e}")
thC = math.asin(0.22431)
R = np.array([[math.cos(thC), math.sin(thC)], [-math.sin(thC), math.cos(thC)]])
T3_1970 = np.diag([-0.5, 0.0])      # d' in a doublet with u; s' a singlet (no charm)
T3_gim = np.diag([-0.5, -0.5])      # charm completes the second doublet
Q = np.diag([-1 / 3, -1 / 3])
a = (R.T @ T3_1970 @ R)[0, 1]
print(f"    three-quark world: (d,s) entry of T_3 in the mass basis = {a:+.5f} = -sin cos / 2 = {-math.sin(thC)*math.cos(thC)/2:+.5f}")
check("without charm the Z has a tree-level s-d coupling of order sin(theta_C)/2", abs(abs(a) - math.sin(thC) * math.cos(thC) / 2) < 1e-15 and abs(a) > 0.1)
check("with charm T_3 is proportional to 1 and the coupling vanishes", abs((R.T @ T3_gim @ R)[0, 1]) < 1e-16)
check("the charge (photon) part is diagonal with or without charm", abs((R.T @ Q @ R)[0, 1]) < 1e-16)

print("\n== A2  loop level: only differences of F survive, bounded by half the spread ==")
worst_shift, worst_ratio = 0.0, 0.0
for _ in range(2000):
    V = haar_unitary(3)
    F = rng.normal(size=3) * 10 ** rng.uniform(-3, 3)
    c = rng.normal() * 100
    A = V.conj().T @ np.diag(F) @ V
    B = V.conj().T @ np.diag(F + c) @ V
    scale = max(1.0, abs(c), np.abs(F).max())
    worst_shift = max(worst_shift, np.abs(offdiag(A) - offdiag(B)).max() / scale)
    spread = F.max() - F.min()
    worst_ratio = max(worst_ratio, np.abs(offdiag(A)).max() / (spread / 2))
check("offdiag(V^dag F V) is unchanged by F -> F + c (2000 Haar draws)", worst_shift < 1e-12, f"max relative change {worst_shift:.1e}")
check("|entry| <= (max F - min F)/2 in every draw", worst_ratio <= 1 + 1e-12, f"largest ratio {worst_ratio:.4f}")
V2 = np.array([[1, 1], [-1, 1]]) / math.sqrt(2)
sat = abs((V2.T @ np.diag([0.0, 1.0]) @ V2)[0, 1])
check("the bound is attained by maximal two-generation mixing", abs(sat - 0.5) < 1e-15, f"entry {sat:.3f} at spread 1")
check("degenerate masses (F constant) give exactly zero", np.abs(offdiag(V.conj().T @ np.diag([2.0, 2.0, 2.0]) @ V)).max() < 1e-14)

print("\n== A3  weak-basis form: the loop insertion is F(H_u); flavour change <=> [H_u, H_d] != 0 ==")
Uu, Ud = haar_unitary(3), haar_unitary(3)
mu2 = np.array([1.0, 30.0, 900.0]); md2 = np.array([2.0, 7.0, 400.0])
Hu = Uu @ np.diag(mu2) @ Uu.conj().T
Hd = Ud @ np.diag(md2) @ Ud.conj().T
Vr = Uu.conj().T @ Ud
F = np.log1p(mu2)
lhs = Vr.conj().T @ np.diag(F) @ Vr
w, P = np.linalg.eigh(Hu)
rhs = Ud.conj().T @ (P @ np.diag(np.log1p(w)) @ P.conj().T) @ Ud
check("V^dag F(D_u) V = U_d^dag F(H_u) U_d", np.abs(lhs - rhs).max() < 1e-11, f"max deviation {np.abs(lhs-rhs).max():.1e}")
comm = Hu @ Hd - Hd @ Hu
check("generic H_u, H_d do not commute and the loop insertion is off-diagonal", np.linalg.norm(comm) > 1 and np.abs(offdiag(lhs)).max() > 1e-3)
Hd_aligned = Uu @ np.diag(md2) @ Uu.conj().T
Va = Uu.conj().T @ Uu
check("commuting H_u, H_d give V = 1 and no off-diagonal insertion", np.linalg.norm(Hu @ Hd_aligned - Hd_aligned @ Hu) < 1e-9 and np.abs(offdiag(Va)).max() < 1e-14)

print("\n== A4  the paper's circulant mass forms in one label basis ==")
Xl = circulant(2.0, 2 / 9)
Xd = circulant(2 + 2 * (1 / 3) ** 1.5, 1 / 9)
Xu = circulant(2 + 2 * (2 / 3) ** 1.5, 2 / 27)
for nm, X in (("leptons", Xl), ("down", Xd), ("up", Xu)):
    ev = np.sort(np.linalg.eigvalsh(X))
    print(f"    {nm:8s} sqrt-mass eigenvalues {ev}  squared ratios to heaviest {(ev[:2]/ev[2])**2}")
cn = np.linalg.norm(Xu @ Xd - Xd @ Xu)
check("[X_u, X_d] = 0 for the paper's up and down circulants", cn < 1e-14, f"norm {cn:.1e}")
wu, Pu = np.linalg.eigh(Xu @ Xu); wd, Pd = np.linalg.eigh(Xd @ Xd)
Vc = np.abs(Pu.conj().T @ Pd)
print("    |V| from the two circulants:\n" + "\n".join("      " + str(r) for r in Vc))
check("the resulting |V| is a permutation matrix: no mixing", np.abs(np.sort(Vc.ravel())[::-1][:3] - 1).max() < 1e-12 and np.sort(Vc.ravel())[:6].max() < 1e-12)
Xd_shift = circulant(2 + 2 * (1 / 3) ** 1.5, 1 / 9 + 2 * math.pi / 3)
check("a relative triality shift of 2 pi/3 only relabels: still commuting", np.linalg.norm(Xu @ Xd_shift - Xd_shift @ Xu) < 1e-14)
Sperm = np.eye(3)[[1, 0, 2]]
Xd_perm = Sperm @ Xd @ Sperm.T
cperm = np.linalg.norm(Xu @ Xd_perm - Xd_perm @ Xu)
wp, Pp = np.linalg.eigh(Xd_perm @ Xd_perm)
Vp = np.abs(Pu.conj().T @ Pp)
print(f"    S_3 transposition applied to the down frame: commutator norm {cperm:.1e}; |V| =\n" + "\n".join("      " + str(r) for r in Vp))
check("an odd S_3 relabelling of one frame also keeps the circulant form (S_3 normalises Z_3): still commuting", cperm < 1e-14, f"norm {cperm:.1e}")
check("and |V| is again a permutation: no element of the component group produces a mixing angle",
      np.abs(np.sort(Vp.ravel())[::-1][:3] - 1).max() < 1e-12 and np.sort(Vp.ravel())[:6].max() < 1e-12)
worst = 0.0
for sig in ([0, 1, 2], [1, 2, 0], [2, 0, 1], [1, 0, 2], [0, 2, 1], [2, 1, 0]):
    Sg = np.eye(3)[sig]
    worst = max(worst, np.linalg.norm(Xu @ (Sg @ Xd @ Sg.T) - (Sg @ Xd @ Sg.T) @ Xu))
check("all six elements of S_3: [X_u, g X_d g^-1] = 0", worst < 1e-14, f"largest norm {worst:.1e}")
Vpdg = ckm(0.22501, 0.003732, 0.04183, 1.147)
F3 = np.exp(2j * np.pi * np.outer(np.arange(3), np.arange(3)) / 3) / math.sqrt(3)
Rframe = F3 @ Vpdg @ F3.conj().T
check("V = F^dag R F: the measured CKM is the relative unitary R of two cyclic frames (R is unitary, not a permutation)",
      np.abs(Rframe @ Rframe.conj().T - np.eye(3)).max() < 1e-14 and np.abs(np.abs(Rframe) - np.eye(3)).max() > 0.05,
      f"max | |R| - 1 | = {np.abs(np.abs(Rframe)-np.eye(3)).max():.3f}")

print("\n== A5  Jarlskog commutator ==")
mu = np.array([0.00216, 1.27, 162.5]); md = np.array([0.00470, 0.0935, 4.18])   # GeV, PDG 2024 MS-bar
Hu = np.diag(mu ** 2).astype(complex)
Hd = Vpdg @ np.diag(md ** 2) @ Vpdg.conj().T
Cm = Hu @ Hd - Hd @ Hu
Jv = (Vpdg[0, 1] * Vpdg[1, 2] * np.conj(Vpdg[0, 2]) * np.conj(Vpdg[1, 1])).imag
prod = 1.0
for m in (mu ** 2, md ** 2):
    prod *= (m[1] - m[0]) * (m[2] - m[0]) * (m[2] - m[1])
lhsJ = np.linalg.det(Cm)
print(f"    J from the PDG 2024 angles and phase: {Jv:.3e} (PDG quotes 3.12e-5)")
print(f"    det[H_u, H_d] = {lhsJ.imag:.4e} i ; 2 J prod = {2*Jv*prod:.4e}")
check("J reproduces the PDG value within its error", abs(Jv - 3.12e-5) < 0.13e-5)
check("|det[H_u, H_d]| = 2 J prod(m_u^2 diffs) prod(m_d^2 diffs)", abs(abs(lhsJ.imag) - 2 * Jv * prod) / (2 * Jv * prod) < 1e-6 and abs(lhsJ.real) < 1e-6 * abs(lhsJ.imag))

print("\n== A6  the all-ones matrix is a function of the Koide circulant ==")
wl, Pl = np.linalg.eigh(Xl)
Jones = np.ones((3, 3))
k = int(np.argmax(np.abs(Pl.conj().T @ np.ones(3))))
lam = wl
poly = np.eye(3, dtype=complex)
for j in range(3):
    if j != k:
        poly = poly @ (Xl - lam[j] * np.eye(3)) / (lam[k] - lam[j])
check("J = 3 P_tau = 3 (X - m_e)(X - m_mu) / ((m_tau - m_e)(m_tau - m_mu)) in sqrt-mass units", np.abs(3 * poly - Jones).max() < 1e-13 and k == 2,
      f"max deviation {np.abs(3*poly-Jones).max():.1e}; eigenvalue index {k} (largest)")
check("so a 1 + b J commutes with X_l: aligned, no lepton flavour violation", np.linalg.norm((0.3 * np.eye(3) + 0.2 * Jones) @ Xl - Xl @ (0.3 * np.eye(3) + 0.2 * Jones)) < 1e-14)

print("\n== B1  the Cabibbo identification and first-row unitarity (PDG 2024) ==")
c, s = math.cos(2 / 9), math.sin(2 / 9)
for nm, th, val, err, src in (("|V_ud|", c, 0.97367, 0.00032, "direct"), ("|V_ud|", c, 0.97435, 0.00016, "SM fit"),
                              ("|V_us|", s, 0.22431, 0.00085, "direct"), ("|V_us|", s, 0.22501, 0.00068, "SM fit")):
    print(f"    {nm} = {th:.5f} from 2/9 ; PDG {src} {val:.5f} +/- {err:.5f} ; {100*(th-val)/val:+.2f} % ; {(th-val)/err:+.1f} sigma")
thfit = math.asin(0.22501)
print(f"    fitted theta_12 = {thfit:.5f} rad against 2/9 = {2/9:.5f}: {100*(2/9-thfit)/thfit:+.2f} %")
check("2/9 is within 2.5 per cent of the Cabibbo angle", abs(2 / 9 - thfit) / thfit < 0.025)
check("but outside the measurement by more than four sigma on each element", abs(c - 0.97367) / 0.00032 > 4 and abs(s - 0.22431) / 0.00085 > 4)
row, rerr = 0.9984, 0.0007
print(f"    first row: |V_ud|^2 + |V_us|^2 + |V_ub|^2 = {row} +/- {rerr} ; framework (exactly three generations) 1 ; pull {(row-1)/rerr:+.1f} sigma")
check("first-row unitarity deficit is between 2 and 3 sigma", 2 < abs(row - 1) / rerr < 3)

print("\n== B2  how much GIM suppresses: K mixing ==")
GF, MW = 1.1663788e-5, 80.3692
fK, BK, mK = 0.1557, 0.75, 0.497611
xc, xt = (1.27 / MW) ** 2, (162.5 / MW) ** 2


def S0(x):
    return x * (4 - 11 * x + x * x) / (4 * (1 - x) ** 2) - 1.5 * x ** 3 * math.log(x) / (1 - x) ** 3


lam_c = 0.22431 * 0.97349
pref = GF ** 2 / (6 * math.pi ** 2) * fK ** 2 * BK * mK * MW ** 2 * lam_c ** 2
dmk_exp = 3.484e-15
print(f"    x_c = m_c^2/M_W^2 = {xc:.3e} ; S0(x_c) = {S0(xc):.3e} ; S0(x_t) = {S0(xt):.3f}")
print(f"    Delta M_K, charm box, no QCD correction: {pref*S0(xc):.2e} GeV ; measured {dmk_exp:.3e} GeV ; ratio {pref*S0(xc)/dmk_exp:.2f}")
print(f"    same box with the cancellation switched off (loop function 1): {pref:.2e} GeV ; ratio to measured {pref/dmk_exp:.0f}")
check("S0(x_c) = x_c to leading order: the amplitude is a mass difference", abs(S0(xc) / xc - 1) < 0.01)
check("the charm box gives Delta M_K within a factor three (Gaillard and Lee)", 1 / 3 < pref * S0(xc) / dmk_exp < 3)
check("without the cancellation K mixing would be over a thousand times too large", pref / dmk_exp > 1000)

print("\n== B3  B_s -> mu mu from the top loop ==")


def Y0(x):
    return x / 8 * ((x - 4) / (x - 1) + 3 * x * math.log(x) / (x - 1) ** 2)


alpha, sw2 = 1 / 127.95, 0.23122
fBs, mBs, mmu = 0.2303, 5.36693, 0.1056584
tau = 1.520e-12 / 6.582119569e-25
VtbVts = 0.999118 * 0.04110
Y = 1.0113 * Y0((163.5 / MW) ** 2)
br = tau * GF ** 2 / math.pi * (alpha / (4 * math.pi * sw2)) ** 2 * fBs ** 2 * mmu ** 2 * mBs * math.sqrt(1 - 4 * mmu ** 2 / mBs ** 2) * VtbVts ** 2 * Y ** 2
br_avg = br / (1 - 0.064)
print(f"    Y = {Y:.3f} ; prompt BR = {br:.2e} ; time-integrated (y_s = 0.064) = {br_avg:.2e} ; Bobeth et al. 2014: (3.65 +/- 0.23)e-9")
check("leading-order top-loop estimate within 15 per cent of the full SM prediction", abs(br_avg / 3.65e-9 - 1) < 0.15, f"ratio {br_avg/3.65e-9:.2f}")
check("helicity and loop suppression: BR below 1e-8", br_avg < 1e-8)

print("\n== B4  floors ==")
mb, Vcb = 4.18, 0.0411
scale = Vcb ** 2 * (mb / MW) ** 4 * (alpha / (4 * math.pi * sw2)) ** 2
print(f"    t -> c Z scaling |V_cb|^2 (m_b/M_W)^4 (alpha/(4 pi s_W^2))^2 = {scale:.1e} (full calculation: about 1e-14) ; ATLAS 2023 limit 1.3e-4")
check("the scaling estimate is within two orders of 1e-14 and ten orders below the limit", 1e-16 < scale < 1e-12 and 1.3e-4 / scale > 1e8)
dm21, dm31 = 7.41e-5, 2.51e-3                 # eV^2
s12l, s13l, s23l = math.sqrt(0.307), math.sqrt(0.0220), math.sqrt(0.55)
U = ckm(s12l, s13l, s23l, 0.0)
amp = (np.conj(U[1, 1]) * U[0, 1] * dm21 + np.conj(U[1, 2]) * U[0, 2] * dm31) / (MW * 1e9) ** 2
br_meg = 3 * (1 / 137.036) / (32 * math.pi) * abs(amp) ** 2
print(f"    mu -> e gamma with m_1 = 0, normal ordering: BR = {br_meg:.1e} ; MEG II 2025 limit 1.5e-13 ; gap {math.log10(1.5e-13/br_meg):.0f} orders")
check("the leptonic GIM floor is below 1e-50", br_meg < 1e-50)
theta2 = 0.05e-9 / 3600.0
print(f"    seesaw mixing of a 3.6 TeV sterile with 0.05 eV: theta^2 = {theta2:.1e} (non-unitarity of the 3x3 lepton matrix)")
check("sterile-induced non-unitarity is below 1e-12", theta2 < 1e-12)

n_ok = sum(results)
print(f"\n{n_ok}/{len(results)} checks passed")
print("GIM FCNC LABEL BLIND: " + ("PASS" if all(results) else "FAIL"))
