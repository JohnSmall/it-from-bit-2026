#!/usr/bin/env python3
"""Graded FANOUT as the rotation of a complex cost: a branching-state toy model.

Companion to knowledge/sessions/graded_fanout_complex_cost_2026-09-18T0830.md and to
knowledge/project-docs/complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md.

Model. A system qubit S in a|0> + b|1> is copied into R environment fragments, one qubit
each, by controlled operations: fragment k goes to |eps0> = |0> if S is |0>, and to
|eps1_k> = exp(i theta_k) (cos(phi) |0> + sin(phi) |1>) if S is |1>. The global state is the
branching state a |0>|0...0> + b |1> (x)_k |eps1_k>, and everything is closed-form:

  overlap        lam_k = <eps0|eps1_k> = exp(i theta_k) cos(phi)
  coherence      rho_S(0,1) = a b* prod_k conj(lam_k)      (Zurek's decoherence factor)
  complex cost   C_R = - sum_k ln lam_k = R gamma - i sum_k theta_k,   gamma = -ln cos(phi)
  entropies      every reduced state of a branching state is a mixture of two pure states
                 with weights |a|^2, |b|^2 and overlap mu = prod over the traced-out
                 fragments' complement ... (see mix_entropy), so the mutual information
                 I(S:F) of S with a fragment set F of f qubits is closed-form too (the
                 quantum-Darwinism plateau).

Claims tested.
  1. Re C_R grows linearly in R (the real cost accumulates); with independent fragment
     phases Im C_R is a random walk ~ sqrt(R), so arg C_R -> 0 like 1/sqrt(R): the cost
     rotates from the imaginary axis (a single phase-only interaction) to the real axis
     (many records). With identical phases Im C_R = R theta and no rotation occurs.
  2. phi = 0 (no distinguishability, |lam| = 1): the cost is purely imaginary for any R and
     S's entropy stays zero: the pre-FANOUT limit. Any phi > 0 already has a real part at
     R = 1: the boundary is graded, not sharp.
  3. S's entropy saturates at the Landauer value H(|a|^2) while Re C_R keeps growing:
     the surplus is redundancy. I(S:F_f) reaches the plateau H_S at small f (Zurek).
  4. Caldeira--Leggett: the noise kernel carries coth(beta omega/2); at imaginary
     beta = i a, coth(i x) = -i cot(x), so the noise (real-cost) kernel becomes a phase.
     Numerical identity check.
  5. Validation: the closed forms agree with an explicit state-vector computation at R = 4.

Seed 20260918; fixed inputs; no hidden state.
"""
import cmath
import math

import numpy as np

SEED = 20260918
rng = np.random.RandomState(SEED)

A = 1 / math.sqrt(2)          # |0> amplitude
B = 1 / math.sqrt(2)          # |1> amplitude (maximal coherence: Landauer bound ln 2)
PHI = 0.30                    # fragment distinguishability angle: |lam| = cos(phi)
SIGMA = 0.50                  # spread of the fragment phases (Gaussian, radians)
LN2 = math.log(2.0)


def h2(p):
    """Binary entropy in nats."""
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log(p) - (1 - p) * math.log(1 - p)


def mix_entropy(mu_abs):
    """Entropy (nats) of |a|^2 |x><x| + |b|^2 |y><y| with |<x|y>| = mu_abs."""
    d = math.sqrt(max(0.0, (A * A - B * B) ** 2 + 4 * A * A * B * B * mu_abs ** 2))
    return h2((1 + d) / 2)


def entropy_S(D_abs):
    """Entropy of rho_S with off-diagonal a b* D."""
    return mix_entropy(D_abs)


def fragment_state(theta):
    return cmath.exp(1j * theta) * np.array([math.cos(PHI), math.sin(PHI)], dtype=complex)


def branching_state(thetas):
    """Explicit global state vector a|0>|0..0> + b|1>(x)|eps1_k>, S first."""
    R = len(thetas)
    zero_env = np.zeros(2 ** R, dtype=complex); zero_env[0] = 1.0
    one_env = np.array([1.0 + 0j])
    for th in thetas:
        one_env = np.kron(one_env, fragment_state(th))
    psi = np.concatenate((A * zero_env, B * one_env))
    return psi


def vn_entropy(rho):
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-14]
    return float(-(w * np.log(w)).sum())


def reduced(psi, keep, n):
    """Reduced density matrix on qubits `keep` (list of indices, 0 = S) of an n-qubit pure state."""
    psi = psi.reshape([2] * n)
    trace_out = [q for q in range(n) if q not in keep]
    perm = keep + trace_out
    t = np.transpose(psi, perm).reshape(2 ** len(keep), 2 ** len(trace_out))
    return t @ t.conj().T


print("graded_fanout_complex_cost_2026-09-18T0830.py  seed=%d  a=b=1/sqrt2  phi=%.2f  sigma=%.2f"
      % (SEED, PHI, SIGMA))
gamma = -math.log(math.cos(PHI))
print("per-copy real cost gamma = -ln cos(phi) = %.6f nat;  |lam| = %.6f" % (gamma, math.cos(PHI)))

# ------------------------------------------------------------------ 5. validation at R = 4
print("--- validation: closed forms against an explicit state vector, R = 4")
th4 = rng.normal(0.0, SIGMA, size=4)
psi = branching_state(th4)
n = 5
rhoS = reduced(psi, [0], n)
D = np.prod([cmath.exp(-1j * t) * math.cos(PHI) for t in th4])
print("  rho_S(0,1) explicit = %.6f%+.6fi ; closed form a b* prod conj(lam) = %.6f%+.6fi"
      % (rhoS[0, 1].real, rhoS[0, 1].imag, (A * B * D).real, (A * B * D).imag))
print("  S(rho_S) explicit = %.6f ; closed form = %.6f" % (vn_entropy(rhoS), entropy_S(abs(D))))
F = [1, 2]
rest = [3, 4]
rhoF = reduced(psi, F, n); rhoSF = reduced(psi, [0] + F, n)
I_explicit = vn_entropy(rhoS) + vn_entropy(rhoF) - vn_entropy(rhoSF)
muF = math.cos(PHI) ** len(F); muR = math.cos(PHI) ** len(rest)
I_closed = entropy_S(abs(D)) + mix_entropy(muF) - mix_entropy(muR)
print("  I(S:F) for F = fragments 1,2: explicit = %.6f ; closed form = %.6f" % (I_explicit, I_closed))

# ------------------------------------------------------------------ 1, 3. the rotation
print("--- the cost with R copies: independent phases (theta_k ~ N(0, sigma)) vs identical phases")
print("  %4s %10s %10s %9s %10s %11s %11s %9s" % ("R", "Re C", "Im C(rand)", "arg(rand)", "|D_R|", "S(rho_S)/ln2", "Im C(same)", "arg(same)"))
Rs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 1024]
thetas_all = rng.normal(0.0, SIGMA, size=max(Rs))
for R in Rs:
    re = R * gamma
    im_rand = -thetas_all[:R].sum()
    im_same = -R * SIGMA
    Dabs = math.cos(PHI) ** R
    print("  %4d %10.4f %10.4f %9.4f %10.3e %11.4f %11.3f %9.4f"
          % (R, re, im_rand, math.atan2(im_rand, re), Dabs, entropy_S(Dabs) / LN2, im_same,
             math.atan2(im_same, re)))
# ensemble statement of the random walk
trials = 2000
ratios = []
for R in (16, 64, 256, 1024):
    ims = np.array([abs(rng.normal(0.0, SIGMA, size=R).sum()) for _ in range(trials)])
    ratios.append((R, ims.mean(), SIGMA * math.sqrt(2 * R / math.pi), ims.mean() / (R * gamma)))
print("  E|Im C| over %d trials vs sigma sqrt(2R/pi); and E|Im C| / Re C:" % trials)
for R, m, pred, ratio in ratios:
    print("    R=%4d  E|Im C| = %.3f  (predicted %.3f)   E|Im C|/Re C = %.4f  (~ 1/sqrt(R))" % (R, m, pred, ratio))

# ------------------------------------------------------------------ 2. the pre-FANOUT limit
print("--- phi = 0 (no distinguishability): cost purely imaginary, entropy zero, any R")
for R in (1, 10, 1000):
    print("  R=%4d  Re C = %.1f  Im C = %.3f  S(rho_S) = %.1f" % (R, -R * math.log(1.0), -thetas_all[:R].sum(), entropy_S(1.0)))
print("--- a single copy with phi > 0 already has a real part: the boundary is graded")
for phi in (0.05, 0.1, 0.3, 0.6, 1.0, 1.4):
    g = -math.log(math.cos(phi))
    print("  phi=%.2f  |lam|=%.4f  Re C_1 = %.5f nat  S(rho_S)/ln2 after one copy = %.5f"
          % (phi, math.cos(phi), g, entropy_S(math.cos(phi)) / LN2))

# ------------------------------------------------------------------ 3. the Darwinism plateau
R = 24
print("--- quantum-Darwinism plateau at R = %d: I(S:F_f)/H_S against fragment size f" % R)
HS = entropy_S(math.cos(PHI) ** R)
row = []
for f in (1, 2, 3, 4, 6, 8, 12, 16, 20, 23, 24):
    I = entropy_S(math.cos(PHI) ** R) + mix_entropy(math.cos(PHI) ** f) - mix_entropy(math.cos(PHI) ** (R - f))
    row.append("f=%d:%.3f" % (f, I / HS))
print("  H_S/ln2 = %.4f ;  " % (HS / LN2) + "  ".join(row))
print("  (the phase information needs f -> R: I(S:F) exceeds H_S only when nearly all fragments are held)")

# ------------------------------------------------------------------ 4. Caldeira-Leggett at imaginary beta
print("--- coth(i x) = -i cot(x): the thermal noise kernel becomes a phase at imaginary temperature")
for x in (0.3, 1.0, 2.0):
    lhs = 1 / cmath.tanh(1j * x)
    rhs = -1j / math.tan(x)
    print("  x=%.1f  coth(ix) = %.6f%+.6fi   -i cot(x) = %.6f%+.6fi   |diff| = %.1e"
          % (x, lhs.real, lhs.imag, rhs.real, rhs.imag, abs(lhs - rhs)))
print("done.")
