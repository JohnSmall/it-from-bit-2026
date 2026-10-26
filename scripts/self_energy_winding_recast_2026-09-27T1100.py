#!/usr/bin/env python3
"""self_energy_winding_recast_2026-09-27T1100.py

The proposed op:parallelisable-renormalisable, attempted. Question: can the
one-loop electron self-energy be recast as a closed computational path, a sum
over windings on a compact fibre with a bounded phase, so that its ultraviolet
divergence is removed without a cutoff put in by hand? PASS: the recasting
gives a finite result reproducing the renormalised finite part. FAIL: the
recasting leaves the momentum measure and its divergence untouched, or needs
a cutoff by hand.

Part A  Baseline. The one-loop mass shift with a Euclidean momentum cutoff
        Lambda, Feynman gauge, photon mass zero, on shell:
        delta m / m = (alpha/2 pi) int_0^1 (2 - x) ln(Lambda^2/Delta(x)) dx,
        Delta(x) = (1 - x)^2 m^2. Closed form:
        delta m / m = (3 alpha/4 pi) ln(Lambda^2/m^2) + 5 alpha/4 pi.
        Numerical quadrature against the closed form; slope 3 alpha/4 pi.
Part B  Recasting 1: the loop as a closed path in time. Euclidean time on a
        circle of circumference beta turns the k_0 integral into a winding sum
        over Matsubara frequencies. Scalar analogue with the same log
        divergence, I(Lambda) = int d^4k/(k^2 + m^2)^2 over |k| < Lambda,
        continuous versus winding-sum, same four-dimensional cutoff region.
        Test: is the ln Lambda growth removed, reduced, or unchanged?
Part C  Recasting 2: the phase bounded modulo 2 pi. Stated, not computed: the
        loop's weight is already a bounded phase; the divergence is the count
        of modes, not the range of the phase.
Part D  Recasting 3: a compact momentum space, S^3 of radius Lambda, the
        radius fixed by the framework's own scales (the 3.6 TeV matching
        scale; the Planck grain). Finite numbers, and whether they predict.
Part E  The finite one-loop quantity that needs none of this: the Schwinger
        term alpha/2 pi.

Constants: alpha = 1/137.035999 (from memory, CODATA-grade), m_e = 0.511 MeV,
M_P = 1.221e19 GeV. Deterministic; seed 20260927 set for the record.
"""
import math
import random

import numpy as np

random.seed(20260927)
np.random.seed(20260927)

alpha = 1.0 / 137.035999
m_e = 0.51099895e-3     # GeV
M_P = 1.220890e19       # GeV
LAM_FRAMEWORK = 3.6e3   # GeV


def dm_over_m_quad(Lam, m=1.0, n=200001):
    x = np.linspace(0.0, 1.0, n)[:-1] + 0.5 / n     # midpoints, avoid x = 1
    integrand = (2 - x) * np.log(Lam ** 2 / ((1 - x) ** 2 * m ** 2))
    return alpha / (2 * math.pi) * integrand.mean()


def dm_over_m_closed(Lam, m=1.0):
    return 3 * alpha / (4 * math.pi) * math.log(Lam ** 2 / m ** 2) + 5 * alpha / (4 * math.pi)


print("=== Part A: baseline, the one-loop mass shift with a Euclidean cutoff (m = 1) ===")
print("%10s %14s %14s" % ("Lambda/m", "quadrature", "closed form"))
prev = None
for Lam in [1e1, 1e2, 1e3, 1e4, 1e5]:
    q, c = dm_over_m_quad(Lam), dm_over_m_closed(Lam)
    print("%10.0e %14.8f %14.8f" % (Lam, q, c))
    if prev is not None:
        slope = (c - prev) / math.log(100.0)   # per unit of ln Lambda^2 (Lambda up by 10)
    prev = c
print("slope per unit ln(Lambda^2): %.8f ; 3 alpha/4 pi = %.8f ; logarithmic divergence confirmed" % (slope, 3 * alpha / (4 * math.pi)))

print()
print("=== Part B: the loop as a closed path in time (winding sum) against the continuous loop ===")


def I_cont(Lam, m=1.0):
    return math.pi ** 2 * (math.log(1 + Lam ** 2 / m ** 2) - Lam ** 2 / (Lam ** 2 + m ** 2))


def shell(K, a2):
    """int_0^K 4 pi k^2 dk / (k^2 + a2)^2 in closed form."""
    a = math.sqrt(a2)
    return 4 * math.pi * (math.atan(K / a) / (2 * a) - K / (2 * (K ** 2 + a2)))


def I_wind(Lam, beta, m=1.0):
    total = 0.0
    nmax = int(Lam * beta / (2 * math.pi))
    for n in range(-nmax, nmax + 1):
        w = 2 * math.pi * n / beta
        if w * w >= Lam * Lam:
            continue
        K = math.sqrt(Lam * Lam - w * w)
        total += shell(K, w * w + m * m)
    return (2 * math.pi / beta) * total


print("%10s %12s" % ("Lambda/m", "continuous") + "".join("%16s" % ("beta m = %g" % b) for b in [1.0, 5.0, 20.0]))
rows = {}
for Lam in [1e1, 1e2, 1e3, 1e4]:
    vals = [I_wind(Lam, b) for b in [1.0, 5.0, 20.0]]
    rows[Lam] = (I_cont(Lam), vals)
    print("%10.0e %12.5f" % (Lam, I_cont(Lam)) + "".join("%16.5f" % v for v in vals))
print("differences winding minus continuous (should converge to a finite, beta-dependent constant):")
for Lam in [1e1, 1e2, 1e3, 1e4]:
    c, vals = rows[Lam]
    print("%10.0e " % Lam + "".join("%16.5f" % (v - c) for v in vals))
c3, c4 = rows[1e3][0], rows[1e4][0]
print("slope per unit ln(Lambda^2), continuous: %.5f ; winding (beta m = 5): %.5f ; pi^2 = %.5f"
      % ((c4 - c3) / math.log(100.0), (rows[1e4][1][1] - rows[1e3][1][1]) / math.log(100.0), math.pi ** 2))
print("VERDICT B: the winding sum discretises the loop frequency and adds a finite thermal part; the logarithmic divergence is unchanged. FAIL.")

print()
print("=== Part C: the phase bounded modulo 2 pi ===")
print("In Minkowski signature the loop weight exp(i S) is already of modulus one for every mode; reducing S modulo 2 pi is the identity on it.")
print("The divergence is the integral of the modulus over the modes, i.e. the number of modes, not the range of the phase. No computation changes this. FAIL by inspection.")

print()
print("=== Part D: a compact momentum space, radius fixed by the framework's own scales (electron) ===")
for name, Lam in [("matching scale 3.6 TeV", LAM_FRAMEWORK), ("Planck grain", M_P)]:
    r = dm_over_m_closed(Lam, m_e)
    print("%-24s delta m / m = %.4f (finite)" % (name, r))
print("finite, but not a prediction: the shift is absorbed into the measured mass, and every cutoff-independent observable is unchanged by the choice. A cutoff put in by hand. FAIL by the problem's own criterion.")

print()
print("=== Part E: the finite one-loop quantity ===")
print("Schwinger term a_e = alpha/2 pi = %.9f ; ultraviolet finite with no recasting; the target for any framework-native vertex computation" % (alpha / (2 * math.pi)))
