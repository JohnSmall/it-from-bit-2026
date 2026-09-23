#!/usr/bin/env python3
"""records_high_temperature_2026-09-20T1400.py

Numbers for knowledge/project-docs/records_causal_structure_high_temperature_2026-09-20T1400.md
("Records and causal structure at very high temperature").

Part A  Thermal time hbar/(k_B T), the chaos-bound maximal scrambling rate
        2 pi k_B T / hbar, and Landauer's energy per bit, at the QCD crossover,
        the electroweak crossover, the framework's 3.6 TeV matching scale, and
        the Planck temperature. (No grand-unification scale: the framework
        excludes grand unification, so its only scales between the electroweak
        and Planck temperatures are its own.)
Part B  The clock ladder: pair thresholds k_B T = m c^2 for e, mu, tau, W, Z,
        H, t, and the radiation-era cosmic time at which the bath falls below
        each (textbook estimate t ~ 2.42 g*^(-1/2) (T/MeV)^-2 s, with g* taken
        as 10.75 below 100 MeV and 106.75 above; order of magnitude only).
Part C  The capacity check: thermal entropy of a region of size R against the
        area bound, S_rad ~ (2 pi^2/45) g* (k_B T / hbar c)^3 R^3 versus
        S_A = pi R^2 c^3 / (hbar G) (A/4 in Planck units); the size at which
        they cross, as a function of T; and the temperatures, as fractions of
        the Planck energy, at which R* equals 1e5 thermal lengths and one.

Constants: h, k_B, e, c exact; G CODATA 2018; masses PDG. Deterministic; seed
20260920 set for the record.
"""
import math
import random

random.seed(20260920)

h = 6.62607015e-34
hbar = h / (2 * math.pi)
kB = 1.380649e-23
eV = 1.602176634e-19
c = 299792458.0
G = 6.67430e-11
lP = math.sqrt(hbar * G / c ** 3)
tP = lP / c
EP = math.sqrt(hbar * c ** 5 / G)
TP = EP / kB


def thermal_time(T):
    return hbar / (kB * T)


print("=== Part A: thermal time, chaos-bound rate, Landauer per bit ===")
print("Planck temperature %.3e K ; Planck time %.3e s ; Planck energy %.3e GeV" % (TP, tP, EP / eV / 1e9))
print("%-24s %12s %14s %16s %16s" % ("epoch", "k_B T", "hbar/k_B T (s)", "2pi k_B T/hbar", "k_B T ln2"))
for name, kT_eV in [("QCD crossover", 155e6), ("electroweak crossover", 160e9), ("matching scale 3.6 TeV", 3.6e12), ("Planck", EP / eV)]:
    T = kT_eV * eV / kB
    print("%-24s %9.3e eV %14.3e %14.3e /s %12.3e eV" % (name, kT_eV, thermal_time(T), 2 * math.pi / thermal_time(T), kT_eV * math.log(2)))
print("at the Planck temperature the thermal time is %.3f Planck times" % (thermal_time(TP) / tP))

print()
print("=== Part B: the clock ladder, pair thresholds and the cosmic time the bath falls below them ===")
masses = [("electron", 0.51099895e6), ("muon", 105.6583755e6), ("tau", 1776.93e6),
          ("W", 80.3692e9), ("Z", 91.1880e9), ("Higgs", 125.20e9), ("top", 172.57e9)]
print("%-9s %12s %12s %14s" % ("particle", "m c^2", "T = mc^2/k_B", "t_cosmic (s)"))
for name, mc2_eV in masses:
    T = mc2_eV * eV / kB
    T_MeV = mc2_eV / 1e6
    gstar = 10.75 if T_MeV < 100 else 106.75
    t_cos = 2.42 / math.sqrt(gstar) * T_MeV ** -2
    print("%-9s %9.4e eV %12.3e K %14.3e" % (name, mc2_eV, T, t_cos))

print()
print("=== Part C: thermal entropy against the area bound ===")
print("S_rad(R) = (2 pi^2/45) g* (k_B T/hbar c)^3 R^3 ; S_A(R) = pi R^2/l_P^2 ; cross at R* = (45/(2 pi g*)) (hbar c/k_B T)^3 / l_P^2")
gstar = 106.75
for name, kT_eV in [("QCD crossover", 155e6), ("electroweak crossover", 160e9), ("matching scale 3.6 TeV", 3.6e12), ("Planck", EP / eV)]:
    lam = hbar * c / (kT_eV * eV)          # thermal wavelength / (2 pi)
    Rstar = 45.0 / (2 * math.pi * gstar) * lam ** 3 / lP ** 2
    print("%-24s thermal length %.3e m ; R* = %.3e m = %.3e thermal lengths = %.3e l_P" % (name, lam, Rstar, Rstar / lam, Rstar / lP))
print("R*/lambda = (45/(2 pi g*)) (E_P/k_B T)^2 ; so R* = 1e5 lambda at k_B T = %.3e E_P and R* = lambda at k_B T = %.3f E_P"
      % (math.sqrt(45.0 / (2 * math.pi * gstar) / 1e5), math.sqrt(45.0 / (2 * math.pi * gstar))))
