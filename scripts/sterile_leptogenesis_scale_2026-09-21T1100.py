#!/usr/bin/env python3
"""sterile_leptogenesis_scale_2026-09-21T1100.py

Order-of-magnitude check for knowledge/project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md
section 18: can the sphaleron route turn the framework's two ~3.6 TeV sterile
neutrinos into the baryon asymmetry (leptogenesis), and what does it require?

Standard formulae, coefficients from memory (VERIFY-CITE before quoting):
  Davidson--Ibarra bound on the CP asymmetry of the lightest sterile in a
  hierarchical type-I seesaw:  |eps_1| <= 3 M_1 (m_3 - m_1) / (16 pi v^2), v = 174 GeV
  (the vev normalisation of the seesaw literature).
  Baryon-to-photon ratio from leptogenesis with sphaleron conversion:
  eta_B ~ 0.96e-2 * eps_1 * kappa  (Buchmueller, Di Bari, Pluemacher; g* = 106.75),
  kappa the washout efficiency, 1e-2 to 1e-1 typical.
  Resonant enhancement for two nearly degenerate steriles: eps up to ~ 1/2 at
  Delta M ~ Gamma/2; the gain over the hierarchical value scales as M / Delta M.
  Sphaleron conversion: B = (28/79)(B - L) in the SM with one Higgs doublet.

Part A  The hierarchical bound at M = 3.6 TeV against the asymmetry needed.
Part B  The degeneracy the resonant route then requires, Delta M / M.
Part C  The framework's neutrino sector as the two-sterile (minimal) seesaw:
        m_1 = 0 exactly, one Majorana phase, the FGY structure.

Deterministic; seed 20260921 set for the record.
"""
import math
import random

random.seed(20260921)

v = 174.0            # GeV, seesaw-literature normalisation (v/sqrt2 of 246)
M = 3.6e3            # GeV, the framework's sterile scale
m3 = 0.050e-9        # GeV, heaviest active neutrino, normal ordering, m1 = 0
eta_B = 6.1e-10      # observed baryon-to-photon ratio (Planck; from memory)

eps_DI = 3 * M * m3 / (16 * math.pi * v ** 2)
print("=== Part A: hierarchical leptogenesis at the framework's sterile scale ===")
print("Davidson--Ibarra bound at M = %.1f TeV, m_3 = %.3f eV: |eps_1| <= %.3e" % (M / 1e3, m3 * 1e9, eps_DI))
for kappa in [1e-1, 1e-2]:
    eps_needed = eta_B / (0.96e-2 * kappa)
    print("kappa = %.0e: eps needed = %.2e ; shortfall factor = %.1e" % (kappa, eps_needed, eps_needed / eps_DI))
print("hierarchical thermal leptogenesis fails at 3.6 TeV by six to seven orders of magnitude (the Davidson--Ibarra bound wants M >~ 1e9 GeV)")

print()
print("=== Part B: the resonant route, two nearly degenerate steriles ===")
for kappa in [1e-1, 1e-2]:
    eps_needed = eta_B / (0.96e-2 * kappa)
    gain = eps_needed / eps_DI
    print("kappa = %.0e: enhancement needed ~ %.1e, so Delta M / M ~ %.1e" % (kappa, gain, 1.0 / gain))
print("i.e. the two 3.6 TeV steriles must be degenerate to about one part in 1e6 to 1e7 for the sphaleron route to supply the observed asymmetry")
print("sphaleron conversion factor B/(B-L) = 28/79 = %.3f" % (28 / 79))

print()
print("=== Part C: the framework's neutrino sector as the minimal two-sterile seesaw ===")
print("two right-handed (sterile) neutrinos, active mass matrix of rank 2: m_1 = 0 exactly; one Majorana phase; one Dirac phase")
print("this is the Frampton--Glashow--Yanagida structure, in which the sign of the baryon asymmetry is fixed by the low-energy CP phase")
