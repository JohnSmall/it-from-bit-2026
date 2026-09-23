#!/usr/bin/env python3
"""koide_renyi_profile_2026-09-19T1100.py

The Koide ratio as an entropy, expanded. With mass fractions p_k = m_k / sum m
and the amplitude-level distribution q_k = sqrt(m_k) / sum sqrt(m):

  K = sum m / (sum sqrt m)^2 = sum_k q_k^2 = exp(-H_2(q)) = exp(-H_{1/2}(p)),

so K = 2/3 is H_{1/2}(p) = ln(3/2) = ln 3 - ln 2, one bit below the maximum.
Equivalent forms checked here:
  (a) the fidelity (Bhattacharyya) of p with the uniform distribution is
      F^2 = (1/3)(sum sqrt p)^2 = 1/(3K) = 1/2: the square-root-mass vector is
      at 45 degrees to the democratic direction (Foot's angle);
  (b) the pure bipartite state with Schmidt coefficients sqrt(p_k) has
      negativity N = ((sum sqrt p)^2 - 1)/2 = 1/4, since exp(H_{1/2}) = 1 + 2N;
  (c) q is the spectrum of the equal mixture rho = (1/3) sum_k |psi_k><psi_k| of
      three generation states with Gram matrix G (unit diagonal, off-diagonal
      modulus 1/sqrt2, Bargmann phase Phi = 3 delta), and K = Tr rho^2 is its
      purity; tr G^2 = 6 fixes K = 2/3 with no reference to the phase;
  (d) the power sums of q: sum q = 1, sum q^2 = K depends on alpha only, and
      sum q^3 = (1/27)(3 + (9/2) alpha^2 + (3/4) alpha^3 cos 3 delta) is where
      the invariant phase first appears; so H_{1/2}(p) is blind to delta, while
      H_1(p) and H_{3/2}(p) are not.

Part A  the identities on PDG 2024 central values.
Part B  the Z3 form at alpha = sqrt2 for several delta: which entropies move.
Part C  an explicit Gram matrix of three mutually unbiased states with Bargmann
        phase 3 delta: eigenvalues against the triality form, tr G^2, tr G^3.

Deterministic; seed 20260919 set for the record. No Cayley-Dickson algebra.
"""
import math

import numpy as np

np.random.seed(20260919)
SQRT2 = math.sqrt(2.0)


def renyi(p, a):
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    if abs(a - 1.0) < 1e-12:
        return float(-np.sum(p * np.log(p)))
    return float(np.log(np.sum(p ** a)) / (1.0 - a))


def profile(m):
    m = np.asarray(m, dtype=float)
    p = m / m.sum()
    q = np.sqrt(m) / np.sqrt(m).sum()
    K = m.sum() / np.sqrt(m).sum() ** 2
    return p, q, K


print("=== Part A: PDG 2024 central values (MeV) ===")
m = np.array([0.51099895069, 105.6583755, 1776.93])
p, q, K = profile(m)
print("K = %.8f ; sum q^2 = %.8f ; exp(-H_1/2(p)) = %.8f ; exp(-H_2(q)) = %.8f"
      % (K, np.sum(q ** 2), math.exp(-renyi(p, 0.5)), math.exp(-renyi(q, 2.0))))
print("H_1/2(p) = %.8f ; ln(3/2) = %.8f ; difference = %.2e nats" % (renyi(p, 0.5), math.log(1.5), renyi(p, 0.5) - math.log(1.5)))
F2 = (np.sqrt(p).sum() ** 2) / 3.0
print("(a) fidelity^2 with uniform = (1/3)(sum sqrt p)^2 = %.8f ; 1/(3K) = %.8f ; angle to (1,1,1) = %.6f deg (45 at K = 2/3)"
      % (F2, 1.0 / (3 * K), math.degrees(math.acos(math.sqrt(F2)))))
N = (np.sqrt(p).sum() ** 2 - 1.0) / 2.0
print("(b) negativity of the Schmidt state = %.8f ; 1 + 2N = %.8f = exp(H_1/2) = %.8f" % (N, 1 + 2 * N, math.exp(renyi(p, 0.5))))
print("effective numbers: exp(H_1/2(p)) = %.6f ; exp(H_1(p)) = %.6f ; exp(H_3/2(p)) = %.6f ; exp(H_2(q)) = %.6f"
      % (math.exp(renyi(p, 0.5)), math.exp(renyi(p, 1.0)), math.exp(renyi(p, 1.5)), math.exp(renyi(q, 2.0))))
print("harmonic mean of 1 and 3 = %.6f ; arithmetic mean of 1/3 and 1 = %.6f = K at Koide" % (2 * 1 * 3 / (1 + 3), (1 / 3 + 1) / 2))

print()
print("=== Part B: Z3 form sqrt(m_k) = 1 + alpha cos(delta + 2 pi k/3), alpha = sqrt2 ===")
print("%8s %12s %12s %12s %12s %14s %14s" % ("delta", "K", "H_1/2(p)", "H_1(p)", "H_3/2(p)", "sum q^3", "formula"))
for delta in [-0.15, 0.0, 0.1, 2.0 / 9.0, 0.25, math.pi / 12]:  # positivity needs |3 delta| <= pi/4, i.e. |delta| <= pi/12 = 0.2618
    r = np.array([1 + SQRT2 * math.cos(delta + 2 * math.pi * k / 3) for k in range(3)])
    if np.any(r <= 0):
        print("%8.4f  (a root is non-positive; skipped)" % delta)
        continue
    mm = r ** 2
    p, q, K = profile(mm)
    s3 = float(np.sum(q ** 3))
    formula = (3 + 4.5 * SQRT2 ** 2 + 0.75 * SQRT2 ** 3 * math.cos(3 * delta)) / 27.0
    print("%8.4f %12.8f %12.8f %12.8f %12.8f %14.8f %14.8f" % (delta, K, renyi(p, 0.5), renyi(p, 1.0), renyi(p, 1.5), s3, formula))
print("H_1/2(p) is constant at ln(3/2) = %.8f across delta; H_1 and H_3/2 move; sum q^3 carries cos(3 delta)" % math.log(1.5))
print("sum q^2 = (1 + alpha^2/2)/3 in general: alpha = 1.0 gives %.6f, alpha = sqrt2 gives %.6f, alpha = 2 gives %.6f"
      % ((1 + 0.5) / 3, (1 + 1.0) / 3, (1 + 2.0) / 3))

print()
print("=== Part C: Gram matrix of three mutually unbiased states with Bargmann phase Phi = 3 delta, delta = 2/9 ===")
delta = 2.0 / 9.0
Phi = 3 * delta
# unit diagonal, off-diagonal modulus 1/sqrt2, phases chosen so that arg(G12 G23 G31) = Phi
G = np.array([[1.0, np.exp(1j * Phi) / SQRT2, 1.0 / SQRT2],
              [np.exp(-1j * Phi) / SQRT2, 1.0, 1.0 / SQRT2],
              [1.0 / SQRT2, 1.0 / SQRT2, 1.0]], dtype=complex)
ev = np.sort(np.linalg.eigvalsh(G))
tri = np.sort(np.array([1 + SQRT2 * math.cos((Phi + 2 * math.pi * k) / 3) for k in range(3)]))
print("eigenvalues of G      : " + " ".join("%.8f" % x for x in ev))
print("triality form         : " + " ".join("%.8f" % x for x in tri))
print("max |difference| = %.1e ; Bargmann phase arg(G12 G23 G31) = %.8f = 3 delta = %.8f" % (np.max(np.abs(ev - tri)), np.angle(G[0, 1] * G[1, 2] * G[2, 0]), Phi))
tr2 = float(np.trace(G @ G).real)
tr3 = float(np.trace(G @ G @ G).real)
print("tr G = %.6f ; tr G^2 = %.6f (= 3 + 6 x 1/2, phase-free) ; K = tr G^2 / (tr G)^2 = %.8f" % (float(np.trace(G).real), tr2, tr2 / 9))
print("tr G^3 = %.8f ; 12 + (3 sqrt2 / 2) cos(3 delta) = %.8f" % (tr3, 12 + 1.5 * SQRT2 * math.cos(Phi)))
rho = G / 3.0
print("(c) purity of the equal mixture, Tr rho^2 = %.8f ; spectrum of rho = q_k: " % float(np.trace(rho @ rho).real)
      + " ".join("%.6f" % x for x in np.sort(np.linalg.eigvalsh(rho))) + " ; q from the triality form: "
      + " ".join("%.6f" % x for x in np.sort(tri / tri.sum())))
