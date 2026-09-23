#!/usr/bin/env python3
"""sterile_records_early_universe_2026-09-21T1200.py

Do the framework's ~3.6 TeV sterile neutrinos interact, and when? For
knowledge/project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md
section 20. Type-I seesaw estimates, coefficients standard (VERIFY-CITE):
  Yukawa from the seesaw:      h^2 ~ M m_3 / v^2, v = 174 GeV
  decay width of the sterile:  Gamma_N = h^2 M / (8 pi)
  Hubble rate, radiation era:  H(T) = 1.66 g*^(1/2) T^2 / M_P
  washout parameter:           K = Gamma_N / H(T = M)  (K > 1: the steriles thermalise)
  cosmic time at T:            t ~ 2.42 g*^(-1/2) (T/MeV)^-2 s

Part A  Yukawa, width, lifetime: the steriles decay promptly.
Part B  K at T = M: whether the Yukawa gate brings them into equilibrium.
Part C  Cosmic time of the sterile epoch against the clock ladder.

Deterministic; seed 20260921 set for the record.
"""
import math
import random

random.seed(20260921)

v = 174.0
M = 3.6e3
m3 = 0.050e-9
MP = 1.220890e19
gstar = 106.75
hbar_GeVs = 6.582119569e-25

h2 = M * m3 / v ** 2
Gamma = h2 * M / (8 * math.pi)
tau = hbar_GeVs / Gamma
print("=== Part A: the Yukawa gate and the decay ===")
print("seesaw Yukawa squared h^2 ~ %.2e ; mixing angle squared theta^2 ~ m_3/M = %.2e" % (h2, m3 / M))
print("width Gamma_N = %.2e GeV ; lifetime %.1e s : the framework's steriles decay promptly and are not dark matter" % (Gamma, tau))

H = 1.66 * math.sqrt(gstar) * M ** 2 / MP
K = Gamma / H
print()
print("=== Part B: equilibrium at T = M ===")
print("H(T = %.1f TeV) = %.2e GeV ; K = Gamma_N / H = %.0f" % (M / 1e3, H, K))
print("K >> 1: the steriles thermalise through the Yukawa gate (strong washout); they interact copiously at T ~ M and form records then")

print()
print("=== Part C: when ===")
for name, T_MeV in [("sterile epoch, T = M", M * 1e3), ("top/Higgs threshold", 172.57e3), ("electroweak crossover", 160e3)]:
    t = 2.42 / math.sqrt(gstar) * T_MeV ** -2
    print("%-24s T = %8.3e GeV ; t ~ %.1e s" % (name, T_MeV / 1e3, t))
print("the steriles' records are written at ~1e-13 s, before the clocks of the top and Higgs switch on at ~1e-11 s")
