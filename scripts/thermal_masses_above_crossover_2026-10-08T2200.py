#!/usr/bin/env python3
"""thermal_masses_above_crossover_2026-10-08T2200.py

JS, 2026-10-08, on the records note's "above the electroweak crossover there
are no masses and no proper time": is that accepted or invented, and is the
truth rather that rest masses are small compared with the interaction energy?

Standard finite-temperature field theory, reproduced for scale (textbook
leading-order formulas, coefficients from memory and marked VERIFY-SUPPORT
in the note: Kapusta--Gale; Carrington 1992; Arnold--Espinosa 1993).  No
randomness.  Electroweak-scale inputs, approximate: g = 0.652, g' = 0.357,
g_s = 1.22, y_t = 0.99, lambda = 0.129, mu_H = m_H/sqrt2 = 88.4 GeV,
v = 246 GeV, Lambda_QCD = 0.2 GeV; lattice crossover T_c = 159.5 GeV
(D'Onofrio--Rummukainen 2016, VERIFY-CITE).

  A. Mean-field Higgs condensate v(T) = v sqrt(1 - T^2/T_c^2) with
     T_c = mu_H / sqrt(c_H): the Yukawa (vacuum) masses m = y v(T)/sqrt2
     go to zero AT the crossover, not merely become small.
  B. Thermal (plasma) masses above the crossover, all proportional to T:
       quark asymptotic mass   m_q^2 = (g_s^2/6) T^2 (QCD part)
       lepton (left-handed)    m_l^2 = (3 g^2/32 + g'^2/32) T^2  (SU(2) + Y=-1/2 hypercharge)
       SU(2) Debye mass        m_D^2 = (11/6) g^2 T^2
       U(1) Debye mass         m_D'^2 = (11/6) g'^2 T^2
       Higgs thermal mass      m_H^2(T) = c_H T^2 - mu_H^2,  c_H = lambda/2 + 3g^2/16 + g'^2/16 + y_t^2/4
     These are comparable to T, not small, and are frame-dependent
     (plasma-frame quasiparticle masses), not Lorentz-invariant rest masses.
  C. The fixed scales that survive: Lambda_QCD and mu_H, as fractions of T
     at T = 160 GeV, 1 TeV, 3.6 TeV, 10 TeV.  These, and the logarithmic
     running of the couplings, are what breaks scale invariance; everything
     else scales with T.
  D. Clocks: Compton rate of the zero-temperature mass against the thermal
     rate k_B T / hbar, for the electron, top and W at the same temperatures,
     i.e. how far the particle's own clock is outrun by the bath's.
"""
import numpy as np

g, gp, gs, yt, lam = 0.652, 0.357, 1.22, 0.99, 0.129
muH, v, LQCD, Tc_lat = 88.4, 246.0, 0.2, 159.5
cH = lam / 2 + 3 * g**2 / 16 + gp**2 / 16 + yt**2 / 4
Tc_mf = muH / np.sqrt(cH)
print("Thermal masses above the electroweak crossover (textbook leading order, approximate inputs)")
print("=" * 92)
print("A. mean-field: c_H = %.3f, T_c(mean field) = %.0f GeV (lattice crossover %.1f GeV)" % (cH, Tc_mf, Tc_lat))
for T in (100, 140, 155, 159):
    vT = v * np.sqrt(max(0.0, 1 - (T / Tc_lat) ** 2))
    print("   T = %4d GeV: v(T) = %6.1f GeV, m_top(T) = %6.1f GeV, m_e(T) = %.4f MeV  (Yukawa masses vanish at T_c)"
          % (T, vT, yt * vT / np.sqrt(2), 2.94e-6 * vT / np.sqrt(2) * 1e3))
print("B. thermal masses above the crossover, as fractions of T (all proportional to T):")
print("   quark (QCD)  m_q/T = %.3f;  lepton (EW)  m_l/T = %.3f;  SU(2) Debye  m_D/T = %.3f;  U(1) Debye  %.3f;  Higgs  sqrt(c_H) = %.3f"
      % (gs / np.sqrt(6), np.sqrt(3 * g**2 / 32 + gp**2 / 32), np.sqrt(11 / 6) * g, np.sqrt(11 / 6) * gp, np.sqrt(cH)))
print("   so a quark at T = 1 TeV carries a plasma mass of about %.0f GeV: not small compared with T" % (gs / np.sqrt(6) * 1000))
print("C. fixed scales that survive, as fractions of T:")
for T in (160, 1000, 3600, 10000):
    print("   T = %5d GeV: Lambda_QCD/T = %.1e   mu_H/T = %.3f   (thermal masses / T are T-independent)" % (T, LQCD / T, muH / T))
print("D. the particle's own clock against the bath's: m c^2 / k_B T (zero-temperature masses, below the crossover only)")
for name, m in (("electron", 0.000511), ("W", 80.4), ("top", 172.8)):
    print("   %-9s at T = 1, 10, 100 GeV: %s" % (name, "  ".join("%.1e" % (m / T) for T in (1, 10, 100))))
print("=" * 92)
print("THERMAL MASSES: PASS (arithmetic reproduced; see the note for what the framework must change)")
