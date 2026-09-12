#!/usr/bin/env python3
"""The QED-correction problem for the Koide phase delta = 2/9.

Companion to knowledge/sessions/koide_qed_corrections_2026-09-11T2200.md. Inputs and
conventions as in koide_delta_fit_and_angle_scan_2026-09-11T1600.py: the Z3 form
sqrt(m_k) = M (1 + alpha cos(delta + 2 pi k/3)), k = 0, 1, 2 = tau, e, mu, PDG 2024 pole
masses, fit-free extraction via the discrete Fourier transform of p_k = sqrt(m_k)/sum.

Part A  One-loop QED running to a common MS-bar scale mu:
        mbar_k(mu) = m_k [1 - (a/pi)(1 + (3/4) ln(mu^2/m_k^2))], a = alpha_em, m_k pole.
        The generation-dependent part is (3a/2pi) ln m_k, so all ratios at a common scale
        are mu-independent at this order and equal (m_j/m_k)^(1 + 3a/2pi). The Koide
        parameters at any common scale therefore differ from their pole values by fixed
        amounts, computed here at several mu. At mu = m_k (each mass at its own scale) the
        factor 1 + a/pi is universal and the pole-mass Koide parameters are recovered.
Part B  Sensitivities: d(K, alpha, delta)/d ln m_k at the physical point, by finite
        differences with an analytic check, so that any per-generation relative shift can
        be turned into a shift of delta.
Part C  Two-loop pole/self-scale ratio. With the MS-bar coupling of each lepton's own
        effective theory, m_pole/mbar(mbar) = 1 + a + a^2 [c0 - d3 N_L], N_L the number of
        lighter leptons (0, 1, 2 for e, mu, tau) and d3 = 71/96 + pi^2/12 = 1.5621 (Melnikov
        and van Ritbergen, hep-ph/9912391, eq. 10, whose QCD form -1.0414 N_L is eq. 13;
        verified 2026-09-11). Those couplings differ between generations, so the comparison
        is made with the single physical alpha(0): the running of alpha between the light
        masses then enters at the same order and the generation-dependent coefficient per
        lighter lepton becomes (2/3) ln(m_k/m_l) - d3. c0 is universal and drops out of
        ratios; light-mass corrections are O(m_l/m_k) and negligible. This is the only
        generation-dependent difference between "exact at the pole" and "exact at self-scale
        MS-bar", so it is where the two readings fork; its size in sigma is the result.
Part D  The one-loop-invariant combinations: ratios of differences of log masses are
        exactly invariant under m -> C m^(1+eps); recorded for the record.

No hidden state: every input is a literal below. No randomness.
"""
import cmath
import math

# PDG 2024 charged-lepton pole masses, MeV (central, one-sigma).
PDG = {"e": (0.51099895069, 0.00000000016),
       "mu": (105.6583755, 0.0000023),
       "tau": (1776.93, 0.09)}
ALPHA_EM = 1.0 / 137.035999            # fine-structure constant at zero momentum
A_PI = ALPHA_EM / math.pi
SQRT2 = math.sqrt(2.0)
W = cmath.exp(-2j * math.pi / 3)
# Band on delta and alpha from the 1600/1900 Monte Carlo (PDG 2024, tau-limited).
SIG_DELTA = 0.00000626
SIG_ALPHA = 0.0000108
SIG_K = None  # computed below from the tau band by linear propagation

me, mmu, mtau = PDG["e"][0], PDG["mu"][0], PDG["tau"][0]

print("koide_qed_corrections_2026-09-11T2200.py  (deterministic; alpha_em = 1/137.035999)")


def koide_params(mt, me_, mm):
    """(K, alpha, delta, p) from three masses, fit-free, k = tau, e, mu."""
    r = [math.sqrt(mt), math.sqrt(me_), math.sqrt(mm)]
    s = sum(r)
    p = [x / s for x in r]
    b = sum(p[k] * W ** k for k in range(3))
    return sum(x * x for x in p), 2 * abs(b), cmath.phase(b) % (2 * math.pi / 3), p


K0, al0, de0, p0 = koide_params(mtau, me, mmu)
# sigma_K from the tau band: dK/dln m_tau = p_tau (p_tau - K)
SIG_K = abs(p0[0] * (p0[0] - K0)) * PDG["tau"][1] / mtau
print("pole values: K = %.8f, alpha = %.7f, delta = %.8f rad; sigma_K (tau band) = %.2e, "
      "sigma_alpha = %.1e, sigma_delta = %.2e" % (K0, al0, de0, SIG_K, SIG_ALPHA, SIG_DELTA))


def report(label, K, al, de):
    print("%-44s K-2/3 = %+.3e (%+7.1f sig)  alpha-sqrt2 = %+.3e (%+7.1f sig)  "
          "delta-2/9 = %+.3e rad (%+7.1f sig)"
          % (label, K - 2 / 3, (K - 2 / 3) / SIG_K, al - SQRT2, (al - SQRT2) / SIG_ALPHA,
             de - 2 / 9, (de - 2 / 9) / SIG_DELTA))


# ----------------------------------------------------------------------------- Part A
print("--- Part A: one-loop QED running of the pole masses to a common MS-bar scale mu")
report("pole masses (data)", K0, al0, de0)


def mbar(m, mu):
    return m * (1.0 - A_PI * (1.0 + 0.75 * math.log(mu * mu / (m * m))))


def mbar_power(m, mu):
    """Resummed one-loop form: (1 - a/pi) (m/mu)^(3a/2pi) m; same to O(a^2)."""
    return m * (1.0 - A_PI) * (m / mu) ** (1.5 * A_PI)


for name, mu in (("mu = m_e", me), ("mu = m_mu", mmu), ("mu = m_tau", mtau),
                 ("mu = M_Z = 91187.6 MeV", 91187.6), ("mu = 3.6 TeV (matching scale)", 3.6e6)):
    K, al, de, _ = koide_params(mbar(mtau, mu), mbar(me, mu), mbar(mmu, mu))
    report("common scale, linearised, " + name, K, al, de)
K, al, de, _ = koide_params(mbar_power(mtau, mtau), mbar_power(me, mtau), mbar_power(mmu, mtau))
report("common scale, power-law form, mu = m_tau", K, al, de)
# Self-scale: each mass at its own scale, mbar_k(m_k) = m_k (1 - a/pi): universal.
K, al, de, _ = koide_params(mbar(mtau, mtau), mbar(me, me), mbar(mmu, mmu))
report("self-scale mbar_k(m_k) (universal factor)", K, al, de)
# The reverse: if (sqrt2, 2/9) were exact at a common scale, the pole values would be
Kc, alc, dec, _ = koide_params(mbar(mtau, mtau), mbar(me, mtau), mbar(mmu, mtau))
print("if exact at a common scale, pole values would be: K = 2/3 %+.3e, alpha = sqrt2 %+.3e, "
      "delta = 2/9 %+.3e rad, i.e. %+.0f, %+.0f, %+.0f sigma from the data"
      % (-(Kc - K0), -(alc - al0), -(dec - de0),
         -(Kc - K0) / SIG_K, -(alc - al0) / SIG_ALPHA, -(dec - de0) / SIG_DELTA))
print("exponent of the one-loop distortion m -> m^(1+eps): eps = 3a/2pi = %.5e" % (1.5 * A_PI))


# ----------------------------------------------------------------------------- Part B
print("--- Part B: sensitivities d(K, alpha, delta)/d ln m_k at the physical point")
h = 1e-6
sens = {}
for k, name in ((0, "tau"), (1, "e"), (2, "mu")):
    ms = [mtau, me, mmu]
    up = ms[:]; up[k] *= math.exp(h)
    dn = ms[:]; dn[k] *= math.exp(-h)
    Ku, alu, deu, _ = koide_params(*up)
    Kd, ald, ded, _ = koide_params(*dn)
    dK, dal, dde = (Ku - Kd) / (2 * h), (alu - ald) / (2 * h), (deu - ded) / (2 * h)
    sens[name] = (dK, dal, dde)
    print("  d/d ln m_%-3s: dK = %+.5f (analytic p_k(p_k-K) = %+.5f)  dalpha = %+.5f  ddelta = %+.5f rad"
          % (name, dK, p0[k] * (p0[k] - K0), dal, dde))
print("  check: sum over k of each derivative (a common rescaling changes nothing): "
      "%+.1e %+.1e %+.1e" % tuple(sum(sens[n][i] for n in sens) for i in range(3)))


# ----------------------------------------------------------------------------- Part C
print("--- Part C: two-loop pole/self-scale ratio, generation dependence through the lighter leptons")
# Melnikov & van Ritbergen, hep-ph/9912391, eq. (10): mbar(M)/M = 1 - C_F a + C_F a^2 (C_F d1 + C_A d2
# + T_R N_L d3 + T_R N_H d4) with d3 = 71/96 + pi^2/12, a = alpha_MSbar(M)/pi in the theory with
# N_L massless light flavours; their eq. (13) gives the QCD numbers 13.4434 - 1.0414 N_L for
# M/mbar(mbar). Inverting and converting to mu = mbar adds nothing N_L-dependent, so for QED
# (C_F = T_R = 1, C_A = 0): M/mbar(mbar) = 1 + a + a^2 (c0 - d3 N_L), a the MS-bar coupling at the
# lepton's own scale in its own effective theory. That coupling differs between generations;
# with the single physical alpha(0), alpha_MSbar(m_k)/pi = a0 [1 + (a0/3) sum_{l<k} ln(m_k^2/m_l^2)],
# so the generation-dependent two-loop coefficient with a common a0 is, per lighter lepton l,
#   (2/3) ln(m_k/m_l) - (71/96 + pi^2/12).
# Light-mass corrections are O(m_l/m_k) times a constant of order one and are shown below.
d3 = 71.0 / 96.0 + math.pi ** 2 / 12.0
print("  d3 = 71/96 + pi^2/12 = %.4f (verified: Melnikov-van Ritbergen eq. 10); (a0/pi)^2 = %.3e"
      % (d3, A_PI ** 2))
masses = {"e": me, "mu": mmu, "tau": mtau}
lighter = {"e": [], "mu": ["e"], "tau": ["e", "mu"]}
coef = {k: sum((2.0 / 3.0) * math.log(masses[k] / masses[l]) - d3 for l in lighter[k]) for k in masses}
coef_ms = {k: -d3 * len(lighter[k]) for k in masses}
shift = {k: A_PI ** 2 * coef[k] for k in masses}
shift_ms = {k: A_PI ** 2 * coef_ms[k] for k in masses}
for k in ("e", "mu", "tau"):
    print("  %-3s lighter leptons %-9s: two-loop coefficient %+.4f (common alpha(0)); relative shift of "
          "m_pole/mbar(mbar) = %+.3e   [MS-bar coupling at own scale: %+.4f, %+.3e]"
          % (k, ",".join(lighter[k]) or "none", coef[k], shift[k], coef_ms[k], shift_ms[k]))
lm = {"mu": d3 * (me / mmu), "tau": d3 * (me / mtau + mmu / mtau)}
print("  light-mass corrections ~ d3 (m_l/m_k) (a0/pi)^2: mu %.1e, tau %.1e  -- negligible"
      % (lm["mu"] * A_PI ** 2, lm["tau"] * A_PI ** 2))
# If the relation is exact for self-scale MS-bar masses, the pole masses carry the shifts
# above and the pole-mass Koide parameters move by:
dK = sum(sens[n][0] * shift[n] for n in shift)
dal = sum(sens[n][1] * shift[n] for n in shift)
dde = sum(sens[n][2] * shift[n] for n in shift)
print("  exact at self-scale  =>  at the pole: K = 2/3 %+.3e (%+.2f sig), alpha = sqrt2 %+.3e (%+.2f sig), "
      "delta = 2/9 %+.3e rad (%+.2f sig)" % (dK, dK / SIG_K, dal, dal / SIG_ALPHA, dde, dde / SIG_DELTA))
print("  data minus each hypothesis, delta: pole-exact %+.2f sig, self-scale-exact %+.2f sig; "
      "alpha: %+.2f sig, %+.2f sig"
      % ((de0 - 2 / 9) / SIG_DELTA, (de0 - 2 / 9 - dde) / SIG_DELTA,
         (al0 - SQRT2) / SIG_ALPHA, (al0 - SQRT2 - dal) / SIG_ALPHA))
# Tau precision needed to separate the two at 3 sigma in delta:
need = abs(dde) / 3.0
print("  to separate the two readings at 3 sigma in delta the band must shrink to %.2e rad, "
      "i.e. m_tau to +/- %.3f MeV (now +/- %.2f)" % (need, PDG["tau"][1] * need / SIG_DELTA, PDG["tau"][1]))
# Three-loop order of magnitude: (a/pi)^3 x O(10) x n_l
print("  three-loop n_l terms: (a/pi)^3 x O(10) = %.0e relative -- below the band by 10^3" % (A_PI ** 3 * 10))


# ----------------------------------------------------------------------------- Part D
print("--- Part D: combinations exactly invariant under m -> C m^(1+eps)")
L = {n: math.log(m) for n, m in (("tau", mtau), ("mu", mmu), ("e", me))}
r = (L["tau"] - L["mu"]) / (L["mu"] - L["e"])
print("  (ln m_tau - ln m_mu)/(ln m_mu - ln m_e) = %.6f; invariant under the one-loop running, "
      "unlike K, alpha, delta" % r)
# and under the two-loop n_l shifts it moves by
rr = (L["tau"] + shift["tau"] - L["mu"] - shift["mu"]) / (L["mu"] + shift["mu"] - L["e"])
print("  under the two-loop n_l shifts it moves by %+.1e (relative %+.1e)" % (rr - r, (rr - r) / r))
print("done.")
