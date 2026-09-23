#!/usr/bin/env python3
"""landauer_temperature_fanout_2026-09-20T1200.py

Numbers for knowledge/project-docs/landauer_temperature_fanout_energy_2026-09-20T1200.md
("What the temperature in Landauer's equation does to the energy cost of FANOUT").

Part A  The four cells of Q = Delta S / beta_c with beta_c = beta + i t/hbar: real
        entropy at real inverse temperature (Landauer heat), imaginary entropy at
        imaginary inverse temperature (Planck energy), and the two mixed cells
        (imaginary energies). Checked symbolically by evaluating the complex
        quotient, and for the electron: an anti-event (Delta S = i pi) over half a
        Compton period returns m_e c^2.
Part B  The crossover between the two columns, hbar / (k_B T) (the thermal time),
        and Landauer's energy per bit, at laboratory temperatures and at the Unruh
        temperature of one g.
Part C  The temperature at which the thermal column's rate equals a particle's
        Compton rate, k_B T = m c^2, for the electron, muon and proton.

Constants: h, k_B, e exact (SI 2019); m c^2 values CODATA 2018 / PDG. No random
draws; seed 20260920 set for the record.
"""
import math
import random

random.seed(20260920)

h = 6.62607015e-34          # J s, exact
hbar = h / (2 * math.pi)
kB = 1.380649e-23           # J/K, exact
eV = 1.602176634e-19        # J, exact
c = 299792458.0             # m/s, exact
g = 9.80665                 # m/s^2, standard gravity
me_c2 = 0.51099895000e6 * eV
mmu_c2 = 105.6583755e6 * eV
mp_c2 = 938.27208816e6 * eV

print("=== Part A: Q = Delta S / beta_c, beta_c = beta + i t/hbar ===")
beta = 1.0 / (kB * 300.0)
t = 1e-12
for name, dS, bc in [
    ("real S, real beta   (Landauer)", complex(math.log(2), 0), complex(beta, 0)),
    ("imag S, imag beta   (Planck)  ", complex(0, math.pi), complex(0, t / hbar)),
    ("real S, imag beta   (a width) ", complex(math.log(2), 0), complex(0, t / hbar)),
    ("imag S, real beta   (Matsubara)", complex(0, 2 * math.pi), complex(beta, 0)),
]:
    Q = dS / bc
    print("%s : Q = %+.4e %+.4e i J  (%+.4e %+.4e i eV)" % (name, Q.real, Q.imag, Q.real / eV, Q.imag / eV))
print("Landauer cell at 300 K: k_B T ln 2 = %.4e eV ; Planck cell: pi hbar / t = %.4e eV for t = %.0e s"
      % (kB * 300 * math.log(2) / eV, math.pi * hbar / t / eV, t))
t_half = math.pi * hbar / me_c2
Q_e = complex(0, math.pi) / complex(0, t_half / hbar)
print("electron: anti-event (Delta S = i pi) over half a Compton period t = %.4e s gives Q = %.6f MeV (m_e c^2 = %.6f MeV)"
      % (t_half, Q_e.real / eV / 1e6, me_c2 / eV / 1e6))
print("fermionic Matsubara check: Delta S = i pi per thermal period beta hbar gives Q = pi k_B T = hbar omega_0 with omega_0 = pi k_B T / hbar")

print()
print("=== Part B: thermal time hbar/(k_B T) and Landauer's energy per bit ===")
T_U = hbar * g / (2 * math.pi * c * kB)
print("%-28s %12s %14s %16s" % ("bath", "T (K)", "hbar/k_B T (s)", "k_B T ln2 (eV)"))
for name, T in [("room", 300.0), ("liquid helium", 4.2), ("dilution fridge", 0.015),
                ("Unruh at one g", T_U)]:
    print("%-28s %12.3e %14.3e %16.3e" % (name, T, hbar / (kB * T), kB * T * math.log(2) / eV))
print("Unruh temperature at one g: %.3e K ; its thermal time %.3e s = %.1f years" % (T_U, hbar / (kB * T_U), hbar / (kB * T_U) / 3.15576e7))

print()
print("=== Part C: k_B T = m c^2, the temperature at which the thermal rate equals the Compton rate ===")
for name, mc2 in [("electron", me_c2), ("muon", mmu_c2), ("proton", mp_c2)]:
    print("%-9s m c^2 = %10.4f MeV ; T = %.3e K ; Compton period h/(m c^2) = %.3e s" % (name, mc2 / eV / 1e6, mc2 / kB, h / mc2))
