#!/usr/bin/env python3
"""The Koide phase along the flat direction: invariant form, Gram-matrix reading,
octonionic realisation, and two closed models.

Companion to knowledge/sessions/koide_flat_direction_2026-09-11T1900.md. Inputs and
conventions follow scripts/koide_delta_fit_and_angle_scan_2026-09-11T1600.py: the Z3
form sqrt(m_k) = M (1 + alpha cos(delta + 2 pi k/3)), generation assignment
k = 0, 1, 2 = tau, e, mu, PDG 2024 pole masses, seed 20260911 for the Monte Carlo.

Part A  Fit-free extraction. With p_k = sqrt(m_k) / sum_j sqrt(m_j) the Koide ratio is
        K = sum_k p_k^2 and the Z3 form is the discrete Fourier transform of p:
        b = sum_k p_k exp(-2 pi i k/3) = (alpha/2) exp(i delta). Only 3 delta is
        Z3-invariant; the coincidence "delta = 2/9" is invariantly "3 delta = 2/3 = K".
Part B  Gram-matrix realisation. Any three unit vectors with pairwise |<psi_j|psi_k>|^2 = 1/2
        (mutually unbiased) and Bargmann phase Phi = arg(<0|1><1|2><2|0>) have Gram
        eigenvalues 1 + sqrt2 cos((Phi + 2 pi k)/3): the Koide spectrum with alpha = sqrt2
        forced and 3 delta = Phi. Positivity bounds |Phi| <= pi/4, equality iff one
        massless generation. Verified by explicit construction and diagonalisation.
Part C  J3(O) realisation, Cayley-Dickson Convention A. The democratic element (unit
        diagonal, off-diagonal octonions of norm 1/sqrt2) has the same spectrum with
        cos(3 delta) = sqrt2 Re(x1 x2 x3) x 2 ... i.e. 2 Re(u1 u2 u3) / sqrt2 for unit u_i.
        Checked: Re((xy)z) = Re(x(yz)) on random octonions (the phase is well defined
        despite non-associativity); spectrum depends on Phi only, not on directions.
Part D  Coherent-state model (three coherent states on an equilateral triangle, mass
        roots = Gram eigenvalues, Pancharatnam phase = twice the enclosed area). One
        parameter, two targets: closed both ways.
Part E  Near-miss 108 p_e p_mu p_tau = 4 det G vs 2/9, and the chance expectation of a
        simple fraction landing in the band.

No hidden state: every input is a literal below. Seeds fixed for the Monte Carlo and
for the random octonions only.
"""
import cmath
import math
import random
from fractions import Fraction

import numpy as np

SEED = 20260911
random.seed(SEED)
RNG = np.random.RandomState(SEED)

# PDG 2024 charged-lepton pole masses, MeV (central, one-sigma).
PDG = {
    "e":   (0.51099895069, 0.00000000016),
    "mu":  (105.6583755,   0.0000023),
    "tau": (1776.93,       0.09),
}
SQRT2 = math.sqrt(2.0)
TWO_NINTHS = 2.0 / 9.0
TWO_THIRDS = 2.0 / 3.0
W = cmath.exp(-2j * math.pi / 3)           # DFT kernel, k = 0, 1, 2 = tau, e, mu

print("koide_flat_direction_gram_2026-09-11T1900.py  seed=%d" % SEED)


# ----------------------------------------------------------------------------- Part A
def roots_normalised(me, mmu, mtau):
    r = [math.sqrt(mtau), math.sqrt(me), math.sqrt(mmu)]      # k = 0, 1, 2
    s = sum(r)
    return [x / s for x in r], s


def dft_fit(me, mmu, mtau):
    """Fit-free: alpha = 2|b|, delta = arg b, b = sum_k p_k w^k."""
    p, s = roots_normalised(me, mmu, mtau)
    b = sum(p[k] * W ** k for k in range(3))
    return s / 3.0, 2.0 * abs(b), cmath.phase(b) % (2.0 * math.pi / 3.0), p, b


def koide_roots(alpha, delta):
    return [1.0 + alpha * math.cos(delta + 2.0 * math.pi * k / 3.0) for k in range(3)]


def masses_from(M, lam):
    return [(M * l) ** 2 for l in lam]       # [tau, e, mu]


me, mmu, mtau = PDG["e"][0], PDG["mu"][0], PDG["tau"][0]
M, alpha, delta, p, b = dft_fit(me, mmu, mtau)
K = sum(x * x for x in p)
print("--- Part A: fit-free extraction from PDG 2024 (tau %.2f +/- %.2f MeV)" % PDG["tau"])
print("p = sqrt(m)/sum sqrt(m)  [tau, e, mu] = %.8f  %.8f  %.8f   (sum = %.15f)"
      % (p[0], p[1], p[2], sum(p)))
print("K = sum p^2              = %.8f   (2/3 = %.8f; K - 2/3 = %+.2e)" % (K, TWO_THIRDS, K - TWO_THIRDS))
print("b = sum p_k w^k          = %.8f %+.8fi" % (b.real, b.imag))
print("|b|^2                    = %.8f   (identity (3K-1)/2 = %.8f; 1/2 at K = 2/3)"
      % (abs(b) ** 2, (3 * K - 1) / 2))
print("alpha = 2|b|             = %.7f   (sqrt2 = %.7f)" % (alpha, SQRT2))
print("delta = arg b            = %.8f rad   (2/9 = %.8f)" % (delta, TWO_NINTHS))
# Monte Carlo over the PDG bands, same seed and draw order as the 1600 script.
N = 200000
ds, As = [], []
for _ in range(N):
    e_ = random.gauss(*PDG["e"])
    mu_ = random.gauss(*PDG["mu"])
    t_ = random.gauss(*PDG["tau"])
    _, a_, d_, _, _ = dft_fit(e_, mu_, t_)
    ds.append(d_)
    As.append(a_)
dmean = sum(ds) / N
dsig = math.sqrt(sum((x - dmean) ** 2 for x in ds) / (N - 1))
amean = sum(As) / N
asig = math.sqrt(sum((x - amean) ** 2 for x in As) / (N - 1))
Phi, Phisig = 3.0 * delta, 3.0 * dsig
print("MC (N=%d): delta = %.8f +/- %.8f rad, alpha = %.7f +/- %.7f" % (N, delta, dsig, alpha, asig))
print("Z3-invariant phase 3 delta = %.7f +/- %.7f rad" % (Phi, Phisig))
print("  2/3 - 3 delta            = %+.7f rad = %+.2f sigma" % (TWO_THIRDS - Phi, (TWO_THIRDS - Phi) / Phisig))
print("  K   - 3 delta            = %+.7f rad = %+.2f sigma   (the invariant coincidence: 3 delta = K)"
      % (K - Phi, (K - Phi) / Phisig))
print("  bound pi/4 = %.7f; 3 delta / (pi/4) = %.6f; shortfall pi/4 - 3 delta = %.7f rad"
      % (math.pi / 4, Phi / (math.pi / 4), math.pi / 4 - Phi))
print("  delta as a fraction of the Z3 step 2 pi/3: %.7f  (irrational: 1/(3 pi) = %.7f under the 2/9 hypothesis)"
      % (delta / (2 * math.pi / 3), 1 / (3 * math.pi)))
# Sensitivity: the tau mass as listed around 2006, 1776.99 +/- 0.29 MeV (symmetrised; quoted
# from memory, VERIFY against the PDG 2006 lepton table). Same seed, fresh draws.
TAU_OLD = (1776.99, 0.29)
random.seed(SEED)
ds_old = []
for _ in range(N):
    e_ = random.gauss(*PDG["e"])
    mu_ = random.gauss(*PDG["mu"])
    t_ = random.gauss(*TAU_OLD)
    ds_old.append(dft_fit(e_, mu_, t_)[2])
d_old = dft_fit(me, mmu, TAU_OLD[0])[2]
dm_old = sum(ds_old) / N
ds_old_sig = math.sqrt(sum((x - dm_old) ** 2 for x in ds_old) / (N - 1))
print("older tau %.2f +/- %.2f MeV (VERIFY): delta = %.8f +/- %.8f rad; 2/9 at %+.2f sigma; "
      "band since narrowed by x%.1f and 2/9 is at %+.2f sigma of the 2024 band"
      % (TAU_OLD[0], TAU_OLD[1], d_old, ds_old_sig, (TWO_NINTHS - d_old) / ds_old_sig,
         ds_old_sig / dsig, (TWO_NINTHS - delta) / dsig))


# ----------------------------------------------------------------------------- Part B
def unbiased_triple(Phi):
    """Three unit vectors in C^3 with pairwise |overlap|^2 = 1/2 and Bargmann phase Phi.
    psi0 = e0, psi1 = (e0 + e1)/sqrt2, psi2 = (e0 + b e1 + c e2)/sqrt2 with
    |b|^2 = 3 - 2 sqrt2 cos Phi, 2 Re b = 1 - |b|^2, c = sqrt(1 - |b|^2) real."""
    bb = 3.0 - 2.0 * SQRT2 * math.cos(Phi)
    re = (1.0 - bb) / 2.0
    im = math.sqrt(max(bb - re * re, 0.0)) * (1 if Phi >= 0 else -1)
    c = math.sqrt(max(1.0 - bb, 0.0))
    psi = np.array([[1, 0, 0],
                    [1 / SQRT2, 1 / SQRT2, 0],
                    [1 / SQRT2, (re + 1j * im) / SQRT2, c / SQRT2]], dtype=complex)
    return psi


def gram(psi):
    return psi.conj() @ psi.T                # G_jk = <psi_j|psi_k>


def bargmann(G):
    return cmath.phase(G[0, 1] * G[1, 2] * G[2, 0])


print("--- Part B: Gram matrix of three mutually unbiased unit vectors in C^3")
for label, Ph in (("Phi = 2/3 exactly", TWO_THIRDS), ("Phi = 3 delta_fit", Phi)):
    psi = unbiased_triple(Ph)
    G = gram(psi)
    ov = [abs(G[j, k]) ** 2 for j, k in ((0, 1), (1, 2), (2, 0))]
    lam = np.sort(np.linalg.eigvalsh(G))[::-1]            # descending: tau, mu, e
    lam_cf = sorted(koide_roots(SQRT2, Ph / 3.0), reverse=True)
    Mt = math.sqrt(mtau) / lam[0]
    mt, mm, me_ = masses_from(Mt, lam)
    print("[%s]  pairwise |overlap|^2 = %.12f %.12f %.12f;  Bargmann phase = %.10f (target %.10f)"
          % (label, ov[0], ov[1], ov[2], bargmann(G), Ph))
    print("  Gram eigenvalues        = %.10f %.10f %.10f" % tuple(lam))
    print("  1+sqrt2 cos((Phi+2pik)/3)= %.10f %.10f %.10f   max|diff| = %.1e"
          % (lam_cf[0], lam_cf[1], lam_cf[2], max(abs(x - y) for x, y in zip(lam, lam_cf))))
    print("  normalised p from data  = %.10f %.10f %.10f   (= eigenvalues/3 when Phi = 3 delta_fit)"
          % (p[0], p[2], p[1]))
    print("  M from tau = %.6f sqrt(MeV): m_mu = %.4f MeV (%+.4f%%), m_e = %.6f MeV (%+.4f%%)"
          % (Mt, mm, (mm / mmu - 1) * 100, me_, (me_ / me - 1) * 100))
    print("  det G = %.8f;  (sqrt2 cos Phi - 1)/2 = %.8f;  108 p_e p_mu p_tau (data) = %.8f"
          % (np.linalg.det(G).real, (SQRT2 * math.cos(Ph) - 1) / 2, 108 * p[0] * p[1] * p[2]))
G4 = gram(unbiased_triple(math.pi / 4))
print("[Phi = pi/4]  eigenvalues = %s  -> rank 2, one massless generation; third component c = %.3e"
      % (np.array2string(np.sort(np.linalg.eigvalsh(G4)), precision=10), abs(unbiased_triple(math.pi / 4)[2, 2])))
# Random unitary rotation of the triple: the spectrum and the Bargmann phase are invariant.
Z = RNG.randn(3, 3) + 1j * RNG.randn(3, 3)
U, _ = np.linalg.qr(Z)
psiU = unbiased_triple(TWO_THIRDS) @ U.T
GU = gram(psiU)
print("random U(3) rotation: max|G' - G| = %.1e, Bargmann phase %.10f" % (np.max(np.abs(GU - gram(unbiased_triple(TWO_THIRDS)))), bargmann(GU)))


# ----------------------------------------------------------------------------- Part C
def cd_mul(x, y):
    """Cayley-Dickson Convention A: (a,b)(c,d) = (ac - conj(d) b, d a + b conj(c))."""
    n = len(x)
    if n == 1:
        return np.array([x[0] * y[0]])
    h = n // 2
    a, bq = x[:h], x[h:]
    c, d = y[:h], y[h:]
    return np.concatenate((cd_mul(a, c) - cd_mul(cd_conj(d), bq),
                           cd_mul(d, a) + cd_mul(bq, cd_conj(c))))


def cd_conj(x):
    y = -x.copy()
    y[0] = x[0]
    return y


def unit(v):
    return v / np.linalg.norm(v)


def oct_exp(theta, n):
    """exp(theta n) for a unit imaginary octonion n."""
    e0 = np.zeros(8); e0[0] = 1.0
    return math.cos(theta) * e0 + math.sin(theta) * n


def j3o_cubic(x1, x2, x3, a=1.0, bdiag=1.0, c=1.0):
    """Invariants of the J3(O) element [[a, x3, x2*],[x3*, b, x1],[x2, x1*, c]] (Baez 2002, 3.4):
    tr, S = ab+bc+ca - sum|x|^2, N = abc - a|x1|^2 - b|x2|^2 - c|x3|^2 + 2 Re(x1 x2 x3)."""
    n1, n2, n3 = (np.dot(x, x) for x in (x1, x2, x3))
    re123 = cd_mul(cd_mul(x1, x2), x3)[0]
    return a + bdiag + c, a * bdiag + bdiag * c + c * a - n1 - n2 - n3, \
        a * bdiag * c - a * n1 - bdiag * n2 - c * n3 + 2 * re123


print("--- Part C: J3(O) democratic element, Convention A octonions")
E = np.eye(8)
# Sanity: e_i^2 = -1, e1 e2 = e3, norm multiplicative, alternative, non-associative.
sq_ok = all(np.allclose(cd_mul(E[i], E[i]), -E[0]) for i in range(1, 8))
e1e2 = cd_mul(E[1], E[2])
xs = [unit(RNG.randn(8)) for _ in range(3)]
x, y, z = xs
norm_def = abs(np.linalg.norm(cd_mul(x, y)) - 1.0)
alt = np.max(np.abs(cd_mul(x, cd_mul(x, y)) - cd_mul(cd_mul(x, x), y)))
assoc = np.max(np.abs(cd_mul(cd_mul(x, y), z) - cd_mul(x, cd_mul(y, z))))
re_assoc = abs(cd_mul(cd_mul(x, y), z)[0] - cd_mul(x, cd_mul(y, z))[0])
print("e_i^2 = -1 for i=1..7: %s;  e1 e2 = e%d;  |xy|-1 = %.1e;  alternativity %.1e;  "
      "associator %.3f (non-zero);  Re((xy)z) - Re(x(yz)) = %.1e"
      % (sq_ok, int(np.argmax(e1e2)), norm_def, alt, assoc, re_assoc))
# (i) coplanar triple: x1 = x2 = x3 = exp(delta e1)/sqrt2, delta = 2/9.
u = oct_exp(TWO_NINTHS, E[1])
tr, S, Ncub = j3o_cubic(u / SQRT2, u / SQRT2, u / SQRT2)
lam_c = np.sort(np.roots([1.0, -tr, S, -Ncub]).real)[::-1]
lam_k = sorted(koide_roots(SQRT2, TWO_NINTHS), reverse=True)
print("(i) x1=x2=x3=exp((2/9) e1)/sqrt2: tr=%.6f S=%.6f N=%.10f; cubic roots %.10f %.10f %.10f; "
      "Koide roots max|diff| = %.1e" % (tr, S, Ncub, lam_c[0], lam_c[1], lam_c[2],
                                       max(abs(a - b_) for a, b_ in zip(lam_c, lam_k))))
# (ii) generic triple: random unit u1, u2; u3 = cos(Phi) conj(u1 u2) + sin(Phi) n, n orthogonal
# to conj(u1 u2), so that Re((u1 u2) u3) = cos(Phi) with Phi = 2/3, directions otherwise random.
u1, u2 = unit(RNG.randn(8)), unit(RNG.randn(8))
w = cd_conj(cd_mul(u1, u2))
nvec = RNG.randn(8); nvec -= np.dot(nvec, w) * w; nvec = unit(nvec)
u3 = math.cos(TWO_THIRDS) * w + math.sin(TWO_THIRDS) * nvec
re_a = cd_mul(cd_mul(u1, u2), u3)[0]
re_b = cd_mul(u1, cd_mul(u2, u3))[0]
tr, S, Ncub = j3o_cubic(u1 / SQRT2, u2 / SQRT2, u3 / SQRT2)
lam_c = np.sort(np.roots([1.0, -tr, S, -Ncub]).real)[::-1]
print("(ii) random directions, |u3| = %.12f: Re((u1u2)u3) = %.10f, Re(u1(u2u3)) = %.10f, cos(2/3) = %.10f"
      % (np.linalg.norm(u3), re_a, re_b, math.cos(TWO_THIRDS)))
print("     cubic roots %.10f %.10f %.10f; Koide roots max|diff| = %.1e  (spectrum depends on Phi only)"
      % (lam_c[0], lam_c[1], lam_c[2], max(abs(a - b_) for a, b_ in zip(lam_c, lam_k))))
# The associator of the generic triple is not zero: the phase is defined without associativity.
print("     associator [(u1u2)u3 - u1(u2u3)] norm = %.4f" % np.linalg.norm(cd_mul(cd_mul(u1, u2), u3) - cd_mul(u1, cd_mul(u2, u3))))


# ----------------------------------------------------------------------------- Part D
print("--- Part D: coherent-state model, alpha_k = r exp(2 pi i k/3), G_jk = <alpha_j|alpha_k>")
def coherent_gram(r2):
    al = [math.sqrt(r2) * cmath.exp(2j * math.pi * k / 3) for k in range(3)]
    G = np.array([[cmath.exp(-abs(a) ** 2 / 2 - abs(bb) ** 2 / 2 + a.conjugate() * bb) for bb in al] for a in al])
    return G
# Closure 1: overlap magnitude fixed to 1/sqrt2 (alpha = sqrt2 exactly).
r2 = math.log(2.0) / 3.0
G = coherent_gram(r2)
Ph1 = bargmann(G)
lam = np.sort(np.linalg.eigvalsh(G))[::-1]
Mt = math.sqrt(mtau) / lam[0]
mt, mm, me_ = masses_from(Mt, lam)
print("closure 1: r^2 = ln2/3 = %.6f -> |overlap|^2 = %.6f, Phi = (sqrt3/2) ln 2 = %.6f rad "
      "(target 2/3: %+.4f rad = %+.0f sigma); delta = %.6f" % (r2, abs(G[0, 1]) ** 2, Ph1, Ph1 - TWO_THIRDS, (Ph1 - TWO_THIRDS) / Phisig, Ph1 / 3))
print("           masses with M from tau: m_mu = %.3f MeV (%+.2f%%), m_e = %.5f MeV (%+.1f%%)"
      % (mm, (mm / mmu - 1) * 100, me_, (me_ / me - 1) * 100))
# Closure 2: Bargmann phase fixed to 2/3 (twice the triangle area = 2/3, area = 1/3).
r2 = TWO_THIRDS / (3 * math.sqrt(3) / 2)
G = coherent_gram(r2)
al2 = 2 * abs(G[0, 1])
lam = np.sort(np.linalg.eigvalsh(G))[::-1]
Mt = math.sqrt(mtau) / lam[0]
mt, mm, me_ = masses_from(Mt, lam)
print("closure 2: Phi = %.10f, triangle area = %.6f, r^2 = 4/(9 sqrt3) = %.6f -> alpha = 2 e^{-3r^2/2} = %.6f "
      "(sqrt2: %+.4f = %+.0f sigma), K = %.6f" % (bargmann(G), 3 * math.sqrt(3) / 4 * r2, r2, al2, al2 - SQRT2, (al2 - SQRT2) / asig, (1 + al2 ** 2 / 2) / 3))
print("           masses with M from tau: m_mu = %.3f MeV (%+.2f%%), m_e = %.5f MeV (%+.1f%%)"
      % (mm, (mm / mmu - 1) * 100, me_, (me_ / me - 1) * 100))


# ----------------------------------------------------------------------------- Part E
print("--- Part E: near-miss and chance expectation")
nm_data = 108 * p[0] * p[1] * p[2]
nm_hyp = 2 * SQRT2 * math.cos(TWO_THIRDS) - 2
nm_sig = 2 * SQRT2 * math.sin(Phi) * Phisig
print("108 p_e p_mu p_tau = 4 det G: data %.8f, under 3 delta = 2/3 exactly %.8f; 2/9 = %.8f; "
      "excess over 2/9 = %+.2e (%+.3f%%, %+.0f sigma). Not a coincidence worth pursuing."
      % (nm_data, nm_hyp, TWO_NINTHS, nm_hyp - TWO_NINTHS, (nm_hyp / TWO_NINTHS - 1) * 100, (nm_data - TWO_NINTHS) / nm_sig))
fr = sorted({Fraction(pp, q) for q in range(1, 10) for pp in range(1, q * 3) if Fraction(pp, q) < 2 * math.pi / 3})
band = 6 * dsig
expect = len(fr) * band / (2 * math.pi / 3)
print("reduced fractions p/q with q <= 9 in [0, 2 pi/3): %d; 6-sigma band width %.2e rad; "
      "chance expectation of one landing = %.2e" % (len(fr), band, expect))
print("done.")
