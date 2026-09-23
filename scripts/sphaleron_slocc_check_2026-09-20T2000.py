#!/usr/bin/env python3
"""sphaleron_slocc_check_2026-09-20T2000.py

Checks for knowledge/project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md
("Sphalerons and the GHZ/W split: a collective conversion, not a breakdown of SLOCC").

Part A  The single-register SLOCC invariant the paper uses and the one it does
        not: the one-qubit reduced spectrum (1/2,1/2) on GHZ and (2/3,1/3) on W
        (a local-unitary invariant), and the three-tangle, four times the modulus
        of Cayley's hyperdeterminant, equal to 1 on GHZ and 0 on W (the SLOCC
        class invariant); the tangle on the deformed state a|000> + b|111>.
Part B  GHZ-class states approach W as a limit (border rank two):
        (|0> + e|1>)^(x3) - |000> is a rank-two combination of product states whose
        normalised form has overlap with W tending to one as e -> 0. The reverse
        limit does not exist (tensor rank cannot rise under SLOCC). Single-copy
        statements only; the sphaleron is collective.
Part C  The 't Hooft vertex counting: one fermion per left-handed SU(2) doublet
        per unit change of winding; 3 colours x 3 generations quark doublets + 3
        lepton doublets = 12; per generation epsilon_abc q^a q^b q^c l; Delta B,
        Delta L, Delta(B-L).
Part D  The two columns of the rate: the zero-temperature instanton weight
        exp(-4 pi/alpha_W) (an action, imaginary column) and the high-temperature
        activation over the sphaleron barrier E_sph ~ 9 TeV (heat, real column),
        with alpha_W = alpha_em(M_Z)/sin^2 theta_W.

Deterministic; seed 20260920 set for the record. No Cayley-Dickson algebra.
"""
import itertools
import math
import random

import numpy as np

random.seed(20260920)
np.random.seed(20260920)


def hyperdet(a):
    """Cayley's hyperdeterminant of a 2x2x2 tensor a[i][j][k]."""
    A = lambda i, j, k: a[i, j, k]
    s = (A(0,0,0)**2 * A(1,1,1)**2 + A(0,0,1)**2 * A(1,1,0)**2
         + A(0,1,0)**2 * A(1,0,1)**2 + A(1,0,0)**2 * A(0,1,1)**2)
    s -= 2 * (A(0,0,0)*A(0,0,1)*A(1,1,0)*A(1,1,1) + A(0,0,0)*A(0,1,0)*A(1,0,1)*A(1,1,1)
              + A(0,0,0)*A(1,0,0)*A(0,1,1)*A(1,1,1) + A(0,0,1)*A(0,1,0)*A(1,0,1)*A(1,1,0)
              + A(0,0,1)*A(1,0,0)*A(0,1,1)*A(1,1,0) + A(0,1,0)*A(1,0,0)*A(0,1,1)*A(1,0,1))
    s += 4 * (A(0,0,0)*A(0,1,1)*A(1,0,1)*A(1,1,0) + A(0,0,1)*A(0,1,0)*A(1,0,0)*A(1,1,1))
    return s


def tangle(psi):
    return 4 * abs(hyperdet(psi.reshape(2, 2, 2)))


def reduced_spectrum(psi):
    m = psi.reshape(2, 4)
    return np.sort(np.linalg.eigvalsh(m @ m.conj().T))[::-1]


ket = lambda s: np.array([1.0 if format(i, "03b") == s else 0.0 for i in range(8)], dtype=complex)
GHZ = (ket("000") + ket("111")) / math.sqrt(2)
W = (ket("001") + ket("010") + ket("100")) / math.sqrt(3)

print("=== Part A: single-register invariants ===")
for name, psi in [("GHZ", GHZ), ("W", W)]:
    print("%-4s reduced spectrum (%.6f, %.6f) ; three-tangle = %.6f" % ((name,) + tuple(reduced_spectrum(psi)) + (tangle(psi),)))
for a in [0.6, 0.8, 0.95]:
    b = math.sqrt(1 - a * a)
    psi = a * ket("000") + b * ket("111")
    print("a|000>+b|111>, a = %.2f: spectrum (%.4f, %.4f) ; tangle = %.6f = 4 a^2 b^2 = %.6f" % ((a,) + tuple(reduced_spectrum(psi)) + (tangle(psi), 4 * a * a * b * b)))

print()
print("=== Part B: W as a limit of GHZ-class (rank-two) states ===")
for e in [0.5, 0.1, 0.01, 0.001]:
    v = np.array([1.0, e], dtype=complex)
    prod = np.kron(np.kron(v, v), v)
    chi = (prod - ket("000")) / e
    chi_n = chi / np.linalg.norm(chi)
    print("e = %.3f: |<W|chi_e>|^2 = %.8f ; tangle(chi_e) = %.3e" % (e, abs(np.vdot(W, chi_n)) ** 2, tangle(chi_n)))
print("the overlap tends to one while the tangle tends to zero: the W class is on the boundary of the GHZ class, not inside it")

print()
print("=== Part C: the 't Hooft vertex ===")
colours, gens = 3, 3
quark_doublets = colours * gens
lepton_doublets = gens
print("left-handed doublets: %d quark (3 colours x 3 generations) + %d lepton = %d ; one fermion each per unit winding"
      % (quark_doublets, lepton_doublets, quark_doublets + lepton_doublets))
dB = quark_doublets * (1.0 / 3.0)
dL = lepton_doublets * 1.0
print("Delta B = %d x 1/3 = %.0f ; Delta L = %d x 1 = %.0f ; Delta(B - L) = %.0f ; Delta(B + L) = %.0f" % (quark_doublets, dB, lepton_doublets, dL, dB - dL, dB + dL))
print("per generation: epsilon_abc q^a q^b q^c l, one quark from each colour copy and one lepton: three GHZ registers to one W register")

print()
print("=== Part D: the two columns of the rate ===")
alpha_em_MZ = 1.0 / 127.95
sin2 = 0.2312
alpha_W = alpha_em_MZ / sin2
S_inst = 4 * math.pi / alpha_W
print("alpha_W = alpha_em(M_Z)/sin^2 theta_W = %.5f ; instanton action 4 pi/alpha_W = %.1f ; weight exp(-4 pi/alpha_W) = 10^%.1f (T = 0, action column)"
      % (alpha_W, S_inst, -S_inst / math.log(10)))
E_sph_GeV = 9.0e3
for T in [1.0, 10.0, 100.0, 160.0]:
    print("k_B T = %6.0f GeV: activation factor exp(-E_sph/k_B T) = 10^%.1f  (E_sph = 9 TeV, heat column; the barrier itself falls with v(T) and vanishes above the crossover)"
          % (T, -E_sph_GeV / T / math.log(10)))
