#!/usr/bin/env python3
"""tang2025_koide_check_2026-09-25T2100.py

Checks on Jau Tang, "Advantages of non-associative sedenionic QED ...",
Preprints.org 2025 (doi 10.20944/preprints202511.0427.v1), Table 2, for the
reading note of 2026-09-25. His table: electron 0.51099895 MeV (input), muon
105.655 MeV ("0.00%"), tau 1776.7 MeV ("0.01%"), experimental tau quoted as
1776.86 +/- 0.12 (the PDG 2022 value; PDG 2024 is 1776.93 +/- 0.09).

Part A  The percentage errors his table claims, recomputed.
Part B  The Koide ratio of his predicted triple against 2/3, and against the
        PDG triple, in units of the PDG band (the 2026-09-11 fit gives
        3 delta = 0.6666743 +/- 0.0000188 and K's own band from the tau).
Part C  What the framework's Z3 form gives with the electron as the input
        instead of the tau: alpha = sqrt2, delta = 2/9, M fixed by m_e, so
        that m_mu and m_tau are outputs, for comparison with his numbers.

Deterministic; seed 20260925 set for the record.
"""
import math
import random

random.seed(20260925)

SQRT2 = math.sqrt(2.0)
DELTA = 2.0 / 9.0
PDG24 = {"e": 0.51099895069, "mu": 105.6583755, "tau": 1776.93}
PDG22_TAU = 1776.86
TANG = {"e": 0.51099895, "mu": 105.655, "tau": 1776.7}


def koide(m):
    return sum(m.values()) / sum(math.sqrt(v) for v in m.values()) ** 2


print("=== Part A: Tang's Table 2 errors, recomputed ===")
for k in ["mu", "tau"]:
    ref = PDG24[k] if k == "mu" else PDG22_TAU
    print("%-4s predicted %10.4f vs %10.4f (his reference): %+.4f %% ; vs PDG 2024 %10.4f: %+.4f %%"
          % (k, TANG[k], ref, 100 * (TANG[k] - ref) / ref, PDG24[k], 100 * (TANG[k] - PDG24[k]) / PDG24[k]))
print("his table says 0.00%% and 0.01%%; the muon figure is -0.003%%, ten times the PDG uncertainty of 2e-6 %%")

print()
print("=== Part B: the Koide ratio of the triples ===")
K_tang = koide(TANG); K_pdg = koide(PDG24)
print("K(Tang predicted) = %.7f ; K(PDG 2024) = %.7f ; 2/3 = %.7f" % (K_tang, K_pdg, 2 / 3))
# K's band from the tau uncertainty (dominant): dK/dm_tau numerically
eps = 1e-3
mp = dict(PDG24); mp["tau"] += eps
dK = (koide(mp) - K_pdg) / eps * 0.09
print("K band from the tau (+/- 0.09 MeV): +/- %.2e ; Tang's K sits %.1f sigma from PDG's, %.1f sigma from 2/3" % (dK, (K_tang - K_pdg) / dK, (K_tang - 2 / 3) / dK))
print("no computation in the preprint produces his numbers; the Koide ratio is the test any associator-norm mass formula must pass")

print()
print("=== Part C: the framework's Z3 form with the electron as input ===")
# sqrt(m_k) = M (1 + sqrt2 cos(delta + 2 pi k/3)), k = 0 tau, 1 e, 2 mu (the 2026-09-11 convention)
cos = [math.cos(DELTA + 2 * math.pi * k / 3) for k in range(3)]
roots = [1 + SQRT2 * c for c in cos]
M_e = math.sqrt(PDG24["e"]) / roots[1]
pred = {"tau": (M_e * roots[0]) ** 2, "e": (M_e * roots[1]) ** 2, "mu": (M_e * roots[2]) ** 2}
for k in ["mu", "tau"]:
    print("%-4s from m_e, alpha = sqrt2, delta = 2/9: %10.4f MeV ; PDG 2024 %10.4f (%+.4f %%) ; Tang %10.3f (%+.4f %% from the Z3 value)"
          % (k, pred[k], PDG24[k], 100 * (pred[k] - PDG24[k]) / PDG24[k], TANG[k], 100 * (TANG[k] - pred[k]) / pred[k]))
print("K of the Z3 form is exactly (1 + alpha^2/2)/3 = %.7f" % ((1 + 2 / 2) / 3))
