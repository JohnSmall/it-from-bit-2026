#!/usr/bin/env python3
"""
three_papers_lfu_angular_2026-11-07T2000.py

Session note: knowledge/sessions/three_papers_lfu_angular_2026-11-07T2000.md

Three papers JS sent on 2026-11-07, read against the framework's
generation-label propositions (prop:fcnc, prop:neutral-blind,
sec:sedenions-flavour-not-force):
  - LHCb, angular analysis of B0 -> K*0 e+ e-, JHEP 06 (2025) 140
    (arXiv:2502.10291): the Q_i lepton-universality observables.
  - LHCb, comprehensive analysis of B0 -> K*0 mu+ mu-, PRL 137 (2026) 021802
    (arXiv:2512.18053): the universal C_9 deficit, lepton-mass effects.
  - Mir, Alda and Penaranda, EPS-HEP 2025 proceedings (arXiv:2510.17742):
    new physics on a single generation in the interaction basis, a rank-one
    flavour projector lambda, fitted to R_D(*), R_J/psi, B -> K nu nubar.

Part A, structure (derivations, no data):
  A1  prop:fcnc's identity V^dag (c 1) V = c 1 against the Mir-Alda-Penaranda
      projector lambda(alpha, beta), which conjugation does not preserve; the
      lepton-sector entry that would be lepton-flavour violation.
  A2  The commutant of the S_3 permutation action on the label space C^3 is
      span{1, J}, J the all-ones matrix: dimension two.
  A3  The S_3 average of the projector is a democratic coupling a 1 + b J.
  A4  In the complex circulant representative of the Koide form (unit diagonal,
      off-diagonal rho e^{i Phi/3}, rho = 1/sqrt2, Phi = 3 delta = 2/3), J
      commutes with the mass matrix, so a 1 + b J is diagonal in the mass
      basis; the b-term falls on the k = 0 Fourier mode, which is the heaviest
      generation.
Part B, data against the framework's prediction (the SM's for every lepton-
universality observable):
  B1  LHCb Q_i in 1.1-6 GeV^2 against zero; the lepton-mass scale 4 m^2/q^2
      that is the framework's actual non-zero prediction.
  B2  The four headline inputs of Mir et al. Table 1 against the SM, with and
      without the HFLAV R_D-R_D* correlation.

Fixed seed, numpy only, no hidden state.  Final line: PASS or FAIL.
"""
import itertools
import math

import numpy as np

SEED = 20261107
rng = np.random.default_rng(SEED)
np.set_printoptions(precision=4, suppress=True, linewidth=100)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def haar_unitary(n):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))


def chi2_sf_even(x, k):
    """Survival function of chi^2 with an even number k of degrees of freedom."""
    assert k % 2 == 0
    return math.exp(-x / 2) * sum((x / 2) ** i / math.factorial(i) for i in range(k // 2))


def sigma_from_p(p):
    """Two-sided Gaussian sigma for tail probability p, by bisection on erfc."""
    lo, hi = 0.0, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if math.erfc(mid / math.sqrt(2)) > p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def offdiag_norm(m):
    return np.linalg.norm(m - np.diag(np.diag(m)))


def perm_matrix(sigma):
    p = np.zeros((3, 3))
    for i, j in enumerate(sigma):
        p[i, j] = 1.0
    return p


def map_projector(alpha, beta):
    """Mir-Alda-Penaranda eq. (2): rank-one projector onto (alpha, beta, 1)."""
    v = np.array([alpha, beta, 1.0], dtype=complex)
    return np.outer(v, v.conj()) / (np.vdot(v, v).real)


ONE = np.eye(3)
J = np.ones((3, 3))

print("THREE PAPERS, LEPTON UNIVERSALITY AND THE ANGULAR OBSERVABLES  (seed %d)" % SEED)

# ---------------------------------------------------------------- Part A
print("\nPART A: structure")
print("\nA1  prop:fcnc versus the Mir-Alda-Penaranda projector")
V = haar_unitary(3)
c = 0.37
dev = np.max(np.abs(V.conj().T @ (c * ONE) @ V - c * ONE))
check("V^dag (c 1) V = c 1 for a Haar-random unitary V", dev < 1e-12, f"max deviation {dev:.1e}")

beta_q = 0.64  # Scenario III best fit, their Table 2
lam = map_projector(0.0, beta_q)
check("lambda(0, 0.64) is Hermitian", np.max(np.abs(lam - lam.conj().T)) < 1e-12)
check("lambda(0, 0.64) is idempotent", np.max(np.abs(lam @ lam - lam)) < 1e-12)
check("tr lambda = 1", abs(np.trace(lam).real - 1) < 1e-12)
sb = lam[1, 2].real
check("s-b entry = beta/(1+beta^2)", abs(sb - beta_q / (1 + beta_q**2)) < 1e-12, f"{sb:.5f}")
lamV = V.conj().T @ lam @ V
print(f"    off-diagonal norm of lambda: {offdiag_norm(lam):.4f}; after conjugation by V: {offdiag_norm(lamV):.4f}")
check("a rank-one projector on the label is not conjugation-invariant",
      np.max(np.abs(lamV - lam)) > 0.05, f"max change {np.max(np.abs(lamV - lam)):.3f}")
for beta_l in (0.0, 0.02):
    ll = map_projector(0.0, beta_l)
    print(f"    lepton projector beta_l = {beta_l:.2f}: tau-mu entry {ll[1, 2].real:.4f} "
          f"(their fit: beta_l = 0.00 +/- 0.02, lepton mixing consistent with zero)")
check("beta_l = 0 gives the pure third-generation projector (aligned, no LFV)",
      np.max(np.abs(map_projector(0.0, 0.0) - np.diag([0, 0, 1.0]))) < 1e-12)

print("\nA2  commutant of the S_3 permutation action on C^3")
perms = [perm_matrix(s) for s in itertools.permutations(range(3))]
cols = []
for a in range(3):
    for b in range(3):
        E = np.zeros((3, 3))
        E[a, b] = 1.0
        cols.append(np.concatenate([(E @ P - P @ E).ravel() for P in perms]))
M = np.array(cols).T  # 54 x 9
s = np.linalg.svd(M, compute_uv=False)
nullity = int(np.sum(s < 1e-10))
check("commutant has dimension 2", nullity == 2, f"singular values {np.round(s, 4)}")
check("1 commutes with every permutation", max(np.max(np.abs(ONE @ P - P @ ONE)) for P in perms) < 1e-12)
check("J commutes with every permutation", max(np.max(np.abs(J @ P - P @ J)) for P in perms) < 1e-12)
_, _, vh = np.linalg.svd(M)
basis = vh[-2:].reshape(2, 3, 3)
X = rng.standard_normal(2) @ basis.reshape(2, 9)
coeff, *_ = np.linalg.lstsq(np.column_stack([ONE.ravel(), J.ravel()]), X, rcond=None)
resid = np.linalg.norm(X - coeff[0] * ONE.ravel() - coeff[1] * J.ravel())
check("a random commutant element lies in span{1, J}", resid < 1e-10, f"residual {resid:.1e}")

print("\nA3  S_3 average of the projector lambda(0, 0.64)")
lam_bar = sum(P @ lam @ P.T for P in perms) / 6
S_entries = lam.sum().real
b = (S_entries - 1) / 6
a = 1 / 3 - b
check("S_3 average equals a 1 + b J with b = (sum of entries - 1)/6, a = 1/3 - b",
      np.max(np.abs(lam_bar - (a * ONE + b * J))) < 1e-12, f"a = {a:.4f}, b = {b:.4f}")
ev = np.sort(np.linalg.eigvalsh(lam_bar))
print(f"    eigenvalues of the average: {ev}  (a + 3b = {a + 3*b:.4f} on (1,1,1)/sqrt3, a twice)")
check("the average is non-universal (b != 0) but equivariant", abs(b) > 1e-3)

print("\nA4  the democratic term in the Koide mass basis (complex circulant representative)")
rho = 1 / math.sqrt(2)
Phi = 2 / 3
u = np.exp(1j * Phi / 3)
C = np.roll(np.eye(3), 1, axis=1)  # cyclic shift
Xk = np.eye(3, dtype=complex) + rho * (u * C + np.conj(u) * C.T)
check("Koide circulant is Hermitian", np.max(np.abs(Xk - Xk.conj().T)) < 1e-12)
w, vecs = np.linalg.eigh(Xk)
formula = np.array([1 + 2 * rho * math.cos((Phi + 2 * math.pi * k) / 3) for k in range(3)])
check("eigenvalues are 1 + 2 rho cos((Phi + 2 pi k)/3)",
      np.max(np.abs(np.sort(w) - np.sort(formula))) < 1e-12, f"{np.sort(formula)}")
check("J commutes with the Koide circulant", np.max(np.abs(Xk @ J - J @ Xk)) < 1e-12)
e0 = np.ones(3) / math.sqrt(3)
overlap = abs(np.vdot(vecs[:, -1], e0))
check("the largest eigenvalue's eigenvector is (1,1,1)/sqrt3, the k = 0 mode",
      abs(overlap - 1) < 1e-12, f"|overlap| = {overlap:.6f}")
which = {0: "tau", 1: "electron", 2: "muon"}
order = np.argsort(-formula)
print("    k = 0, 1, 2 -> sqrt-mass values", np.round(formula, 4),
      "-> generations", [which[k] for k in range(3)])
m_ratio = (formula / formula[0]) ** 2
print(f"    squared ratios to the k = 0 mode: {m_ratio}  (m_e/m_tau = {m_ratio[1]:.2e}, m_mu/m_tau = {m_ratio[2]:.4f})")
check("k = 0 is the heaviest generation", order[0] == 0)
D_mass = vecs.conj().T @ (a * ONE + b * J) @ vecs
check("a 1 + b J is diagonal in the mass basis", offdiag_norm(D_mass) < 1e-12,
      f"diag = {np.round(np.diag(D_mass).real, 4)}")
tau_idx = int(np.argmax(w))
check("its non-universal part sits on the tau alone",
      abs(D_mass[tau_idx, tau_idx].real - (a + 3 * b)) < 1e-12
      and all(abs(D_mass[i, i].real - a) < 1e-12 for i in range(3) if i != tau_idx))

# ---------------------------------------------------------------- Part B
print("\nPART B: data against the framework's prediction (= the SM's)")
print("\nB1  LHCb B0 -> K*0 e+e- (JHEP 06 (2025) 140), Table 4: Q_i = P_i(mu) - P_i(e), 1.1 < q^2 < 6.0 GeV^2")
Q = [  # name, value, stat, syst
    ("Q_FL", 0.12, 0.05, 0.05), ("Q_1", -0.10, 0.26, 0.25), ("Q_4", -0.07, 0.17, 0.13),
    ("Q_5", 0.05, 0.13, 0.11), ("Q_2", 0.07, 0.10, 0.12), ("Q_6", -0.05, 0.14, 0.10),
    ("Q_8", -0.28, 0.17, 0.14), ("Q_3", 0.22, 0.14, 0.11),
]
chi2_q = 0.0
worst = 0.0
for name, val, st, sy in Q:
    tot = math.hypot(st, sy)
    pull = val / tot
    chi2_q += pull**2
    worst = max(worst, abs(pull))
    print(f"    {name:5s} = {val:+.2f} +/- {tot:.3f}   pull from zero {pull:+.2f} sigma")
p_q = chi2_sf_even(chi2_q, len(Q))
print(f"    chi^2 = {chi2_q:.2f} for {len(Q)} observables (correlations neglected), p = {p_q:.2f}")
check("every Q_i is within 2 sigma of universality", worst < 2.0, f"largest |pull| {worst:.2f}")
check("the Q_i set is consistent with Q_i = 0", p_q > 0.05, f"p = {p_q:.2f}")
m_mu, m_e = 0.1056583755, 0.00051099895  # GeV, PDG 2024
print("    the framework's non-zero prediction is the lepton-mass term; its scale 4 m^2/q^2:")
for q2 in (1.1, 2.5, 4.0, 6.0):
    print(f"      q^2 = {q2:3.1f} GeV^2: muons {4*m_mu**2/q2*100:5.2f} %, electrons {4*m_e**2/q2:.1e}")
check("muon-mass scale is below one per cent by q^2 = 6 GeV^2", 4 * m_mu**2 / 6.0 < 0.01)
avg = 4 * m_mu**2 * math.log(6.0 / 1.1) / (6.0 - 1.1)  # flat average over the bin
smallest = min(math.hypot(st, sy) for _, _, st, sy in Q)
print(f"    bin-averaged muon-mass scale over 1.1-6 GeV^2: {avg*100:.2f} %; smallest Q_i error {smallest:.3f} (Q_FL); ratio {smallest/avg:.1f}")
check("bin-averaged muon-mass scale is below every Q_i error", avg < smallest, f"ratio {smallest/avg:.1f}")
check("but within a factor ten of the Q_FL error: the mass term matters for the next F_L test", smallest / avg < 10)

print("\nB2  Mir, Alda and Penaranda Table 1 inputs against the SM (the framework predicts the SM value)")
T = [  # name, exp, sigma_exp, sm, sigma_sm
    ("R_D", 0.342, 0.026, 0.299, 0.004), ("R_D*", 0.287, 0.012, 0.257, 0.005),
    ("R_J/psi", 0.52, 0.20, 0.258, 0.004), ("BR(B+->K+nunu) x 1e5", 2.3, 0.7, 0.429, 0.021),
]
pulls = []
for name, ex, sx, sm, ssm in T:
    tot = math.hypot(sx, ssm)
    pulls.append((ex - sm) / tot)
    print(f"    {name:22s} exp {ex:.3f} +/- {sx:.3f}, SM {sm:.3f} +/- {ssm:.3f}: pull {pulls[-1]:+.2f} sigma")
chi2_u = sum(p**2 for p in pulls)
p_u = chi2_sf_even(chi2_u, 4)
print(f"    uncorrelated: chi^2 = {chi2_u:.2f}/4, p = {p_u:.1e}, {sigma_from_p(p_u):.2f} sigma")
rho_dd = -0.39  # HFLAV 2023 experimental correlation of R_D and R_D*
cov = np.diag([math.hypot(sx, ssm) ** 2 for _, _, sx, _, ssm in T])
cov[0, 1] = cov[1, 0] = rho_dd * T[0][2] * T[1][2]
d = np.array([ex - sm for _, ex, _, sm, _ in T])
chi2_c = float(d @ np.linalg.solve(cov, d))
p_c = chi2_sf_even(chi2_c, 4)
print(f"    with rho(R_D, R_D*) = {rho_dd}: chi^2 = {chi2_c:.2f}/4, p = {p_c:.1e}, {sigma_from_p(p_c):.2f} sigma")
d2 = d[:2]
chi2_dd = float(d2 @ np.linalg.solve(cov[:2, :2], d2))
print(f"    R_D, R_D* pair alone: chi^2 = {chi2_dd:.2f}/2, {sigma_from_p(chi2_sf_even(chi2_dd, 2)):.2f} sigma")
check("no single headline input exceeds 3 sigma", max(abs(p) for p in pulls) < 3.0,
      f"largest {max(abs(p) for p in pulls):.2f} sigma (B+ -> K+ nu nubar)")
check("the four together stand against the SM at about 3 sigma", 2.5 < sigma_from_p(p_c) < 4.0,
      f"{sigma_from_p(p_c):.2f} sigma")
print("    (their global pull of 6.25 sigma, Delta chi^2 = 46.66 for three parameters over the full")
print("     smelli observable set, is a model-comparison statistic and is not reproduced here)")

# ---------------------------------------------------------------- summary
print("\nSUMMARY")
n_fail = sum(1 for _, ok in CHECKS if not ok)
for name, ok in CHECKS:
    if not ok:
        print("  FAILED:", name)
print(f"  {len(CHECKS) - n_fail}/{len(CHECKS)} checks passed")
print("THREE PAPERS LFU ANGULAR: " + ("PASS" if n_fail == 0 else "FAIL"))
