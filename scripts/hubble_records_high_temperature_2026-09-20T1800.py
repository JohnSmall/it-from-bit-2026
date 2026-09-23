#!/usr/bin/env python3
"""hubble_records_high_temperature_2026-09-20T1800.py

Numbers for knowledge/project-docs/gravity_planck_scale_high_temperature_2026-09-20T1800.md.

Part A  How many records the Hubble horizon holds at temperature T in the
        radiation era: N_H = pi (L_H/l_P)^2 with L_H = 1/H and H = 1.66 g*^(1/2)
        T^2/M_P (natural units, non-reduced Planck mass; Kolb--Turner form,
        order of magnitude); and the ratio T/M_P, which is the size of the
        thermal (volume) correction to the horizon's area entropy relative to
        the area term for a Hubble-size patch. Also the temperature at which
        N_H = 1.
Part B  The record's size against the framework's dimensional input: the
        Planck length in units of the electroweak Compton length hbar c/v, and
        the corresponding hierarchy M_P/v.

Constants: hbar c = 197.3269804 MeV fm (CODATA 2018), M_P = 1.220890e19 GeV
(CODATA 2018), v = 246.22 GeV (PDG). Deterministic; seed 20260920 set for the
record.
"""
import math
import random

random.seed(20260920)

MP = 1.220890e19        # GeV
v = 246.22              # GeV
hbarc = 197.3269804e-18  # GeV m
lP = hbarc / MP         # m

print("=== Part A: records on the Hubble horizon, radiation era ===")
print("l_P = %.4e m ; N_H(T) = pi M_P^4 / (1.66^2 g* T^4)" % lP)
print("%-24s %12s %6s %14s %12s" % ("epoch", "T (GeV)", "g*", "N_H", "T/M_P"))
for name, T, gs in [("QCD crossover", 0.155, 61.75), ("electroweak crossover", 160.0, 106.75),
                    ("matching scale 3.6 TeV", 3600.0, 106.75), ("Planck", MP, 106.75)]:
    NH = math.pi * MP ** 4 / (1.66 ** 2 * gs * T ** 4)
    print("%-24s %12.3e %6.2f %14.3e %12.3e" % (name, T, gs, NH, T / MP))
T1 = MP * (math.pi / (1.66 ** 2 * 106.75)) ** 0.25
print("N_H = 1 at T = %.3f M_P (g* = 106.75) ; the thermal correction T/M_P is then of order one" % (T1 / MP))
print("present de Sitter horizon, for comparison: S ~ 1e122 records (Gibbons--Hawking), not computed here")

print()
print("=== Part B: the record's size against the electroweak scale ===")
lv = hbarc / v
print("electroweak Compton length hbar c / v = %.4e m ; l_P / (hbar c/v) = v/M_P = %.3e ; M_P / v = %.3e" % (lv, v / MP, MP / v))
print("one Planck area in units of the electroweak area: (v/M_P)^2 = %.3e" % ((v / MP) ** 2))
