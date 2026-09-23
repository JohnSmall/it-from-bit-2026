#!/usr/bin/env python3
"""two_columns_renyi_check_2026-09-18T1200.py

Numerical checks for the note
knowledge/project-docs/two_columns_shannon_thermodynamics_action_2026-09-18T1200.md
("The two columns: Shannon, thermodynamics and action").

Part A  The complex surprisal of a negative weight on the principal branch of
        the logarithm, and the 2 pi i ambiguity when two anti-events compose.
Part B  One environment fragment of overlap lambda = cos(phi) between its two
        conditional states, for a balanced branch: the decoherence exponent
        -ln|lambda| (the real part of the complex cost) against the fragment's
        von Neumann entropy h((1+|lambda|)/2) in nats (the Landauer quantity),
        and the Renyi-1/2 divergence -2 ln F between the two conditional states.
Part C  R equal fragments: the sum of local fragment entropies, the joint
        environment entropy h((1+|lambda|^R)/2), and the decoherence exponent
        -R ln|lambda|.
Part D  The Koide ratio as exp(-H_{1/2}) of the mass fractions (PDG 2024
        central values as in the 2026-09-11 scripts).

Deterministic: no random draws. Seed 20260918 set for the record. No hidden
state. Entropies in nats throughout.
"""
import math
import random

import numpy as np

random.seed(20260918)
np.random.seed(20260918)


def h(x):
    """Binary entropy in nats."""
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log(x) - (1.0 - x) * math.log(1.0 - x)


print("=== Part A: complex surprisal of a negative weight (principal branch) ===")
p = 0.3
s = -np.log(np.complex128(-p))
print("weight -0.3: surprisal -ln(-0.3) = %.6f %+.6f i   (real part -ln 0.3 = %.6f, imaginary part -pi = %.6f)"
      % (s.real, s.imag, -math.log(p), -math.pi))
q = 0.5
s1 = -np.log(np.complex128(-p)) - np.log(np.complex128(-q))
s2 = -np.log(np.complex128((-p) * (-q)))
print("two anti-events -0.3 and -0.5: sum of surprisals = %.6f %+.6f i ; surprisal of the product = %.6f %+.6f i"
      % (s1.real, s1.imag, s2.real, s2.imag))
print("difference = %.6f i ; |difference| = 2 pi ? %s" % ((s1 - s2).imag, abs(abs((s1 - s2).imag) - 2 * math.pi) < 1e-12))

print()
print("=== Part B: one fragment, overlap lambda = cos(phi), balanced branch ===")
print("%8s %10s %14s %16s %10s %12s" % ("phi", "lambda", "-ln|lambda|", "h((1+lam)/2)", "ratio", "D_1/2=-2lnF"))
for phi in [0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.2, 1.4, 1.5, 1.55]:
    lam = math.cos(phi)
    dec = -math.log(lam)
    ent = h((1.0 + lam) / 2.0)
    print("%8.3f %10.6f %14.6f %16.6f %10.4f %12.6f" % (phi, lam, dec, ent, dec / ent, 2.0 * dec))
phi = 0.05
lam = math.cos(phi)
eps = (1.0 - lam) / 2.0
print("small phi = 0.05: -ln cos phi = %.6e vs phi^2/2 = %.6e ; h((1+lam)/2) = %.6e vs eps(1 - ln eps) = %.6e with eps = %.6e"
      % (-math.log(lam), phi ** 2 / 2, h((1 + lam) / 2), eps * (1 - math.log(eps)), eps))
print("limits: lambda -> 1: both -> 0 ; lambda -> 0: -ln|lambda| -> infinity, h -> ln 2 = %.6f" % math.log(2))

print()
print("=== Part C: R equal fragments at phi = 0.3 (lambda = %.6f) ===" % math.cos(0.3))
lam = math.cos(0.3)
print("%6s %12s %16s %16s %16s" % ("R", "|Lambda|", "sum local ent", "joint ent", "-R ln|lambda|"))
for R in [1, 2, 4, 8, 16, 32, 64, 128, 256]:
    Lam = lam ** R
    print("%6d %12.6e %16.6f %16.6f %16.6f" % (R, Lam, R * h((1 + lam) / 2), h((1 + Lam) / 2), -R * math.log(lam)))
print("joint entropy is bounded by ln 2 = %.6f ; the local sum and the decoherence exponent grow linearly in R" % math.log(2))

print()
print("=== Part D: the Koide ratio as a Renyi-1/2 entropy (PDG 2024 central values, MeV) ===")
m = {"e": 0.51099895069, "mu": 105.6583755, "tau": 1776.93}
M = sum(m.values())
K = M / sum(math.sqrt(v) for v in m.values()) ** 2
pfrac = [v / M for v in m.values()]
H_half = 2.0 * math.log(sum(math.sqrt(x) for x in pfrac))
H_one = -sum(x * math.log(x) for x in pfrac)
print("K = sum m / (sum sqrt m)^2 = %.8f ; 2/3 = %.8f" % (K, 2.0 / 3.0))
print("H_1/2(mass fractions) = %.8f nats ; ln(3/2) = %.8f ; exp(-H_1/2) = %.8f ; K - exp(-H_1/2) = %.1e"
      % (H_half, math.log(1.5), math.exp(-H_half), K - math.exp(-H_half)))
print("effective number of generations at order 1/2: exp(H_1/2) = %.6f ; at order 1 (Shannon): exp(H_1) = %.6f ; range [1, 3]"
      % (math.exp(H_half), math.exp(H_one)))
