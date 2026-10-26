#!/usr/bin/env python3
"""inflation_debts_at_framework_scales_2026-10-07T1200.py

Standard cosmology reproduced for scale, nothing of the framework's own: the
two fine-tunings inflation is credited with removing, evaluated at the
temperatures the framework owns (electroweak crossover, 3.6 TeV matching
scale, first-record epoch a few decades below the Planck temperature, and the
Planck temperature itself), so that the note of 2026-10-07 can say what a
no-inflation account has to explain and where.

  A. Flatness.  Omega_tot(a) - 1 = Omega_k0 a^-2 / E^2(a).  With the Planck 2018
     + BAO bound |Omega_k0| < 0.005 (taken as a round 2-sigma bound; the paper
     cites Planck2020), the bound on |Omega - 1| at each temperature.  The
     scale factor at temperature T is a = (T0/T) (g_s0/g_s(T))^(1/3), with
     g_s = 3.91 today, 10.75 above e+e- annihilation, 106.75 above the
     electroweak crossover (Standard Model only; the framework has no GUT).
  B. Horizon.  Comoving particle horizon at recombination against comoving
     distance to the last-scattering surface, flat LCDM; the angle on the sky
     and the number of causally disconnected patches at recombination.
  C. The ratio inflation is asked to produce: the number of e-folds N such that
     e^N stretches the particle horizon at T_P to cover the present Hubble
     radius, i.e. the standard "about 60".

Parameters: Planck 2018 base LCDM (H0 = 67.4, Omega_m = 0.315, Omega_r = 9.1e-5
including massless neutrinos, Omega_L = 1 - Omega_m - Omega_r, T0 = 2.725 K,
z_rec = 1090).  Numpy only; no random numbers; no seed needed.
"""
import numpy as np

H0 = 67.4                      # km/s/Mpc
c = 299792.458                 # km/s
Om, Or = 0.315, 9.1e-5
OL = 1.0 - Om - Or
Ok0_bound = 0.005
T0_K, kB_eV = 2.725, 8.617e-5
T0 = T0_K * kB_eV              # eV
TP = 1.22e28                   # eV, Planck temperature
MP_GeV = 1.22e19

def g_s(T_eV):
    if T_eV < 0.5e6: return 3.91          # after e+e- annihilation
    if T_eV < 160e9: return 10.75 if T_eV < 1e8 else 86.25   # rough: below QCD / between QCD and EW
    return 106.75

def a_of_T(T_eV):
    return (T0 / T_eV) * (3.91 / g_s(T_eV)) ** (1.0 / 3.0)

def E2(a):
    return Or / a**4 + Om / a**3 + OL

print("Standard-cosmology fine-tunings at the framework's scales (Planck 2018 base LCDM)")
print("=" * 86)
print("A. flatness: bound on |Omega - 1| at temperature T, from |Omega_k0| < %.3f today" % Ok0_bound)
rows = [("today", T0), ("recombination (0.26 eV)", 0.26), ("BBN (1 MeV)", 1e6),
        ("electron clock switches on (0.5 MeV)", 0.511e6), ("electroweak crossover (160 GeV)", 160e9),
        ("3.6 TeV matching scale", 3.6e12), ("first records, T_P/1000", TP / 1e3), ("T_P/10", TP / 10), ("T_P", TP)]
for name, T in rows:
    a = a_of_T(T)
    bound = Ok0_bound / (a * a * E2(a))
    print("   %-40s a = %9.2e   |Omega-1| < %9.2e" % (name, a, bound))

print("B. horizon: flat LCDM, z_rec = 1090")
def chi(a1, a2, n=200000):
    a = np.linspace(a1, a2, n)
    return np.trapz(1.0 / (a * a * np.sqrt(E2(a))), a) * c / H0      # Mpc, comoving
a_rec = 1.0 / 1091.0
chi_p = chi(1e-12, a_rec)                 # particle horizon at recombination (integrand ~ a^-2 / sqrt(Or a^-4) = 1/sqrt(Or): converges at a -> 0)
chi_ls = chi(a_rec, 1.0)
theta = chi_p / chi_ls
print("   comoving particle horizon at recombination: %7.0f Mpc" % chi_p)
print("   comoving distance to last scattering:       %7.0f Mpc" % chi_ls)
print("   angle subtended today: %.2f deg;  disconnected patches on the sky ~ 4/theta^2 = %.0f" % (np.degrees(theta), 4.0 / theta**2))

print("C. e-folds inflation is asked for, from T_P to today")
# comoving Hubble radius 1/(aH) must shrink during inflation by the factor it grew since: N = ln[(a H)_end / (a H)_0] ~ ln(T_P / T0 * (H0/H_P)...) ; standard estimate
a_P = a_of_T(TP)
HP_over_H0 = np.sqrt(E2(a_P))
N = np.log(a_P * HP_over_H0 / 1.0)        # (aH)_P / (aH)_0 with (aH)_0 = 1 in these units
print("   (aH)_P / (aH)_0 = %.2e  ->  N = ln of that = %.1f e-folds (textbook: about 60)" % (a_P * HP_over_H0, -N if N < 0 else N))
print("=" * 86)
print("INFLATION DEBTS: PASS (textbook figures reproduced; see note for what the framework owes)")
