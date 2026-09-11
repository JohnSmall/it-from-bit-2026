#!/usr/bin/env python3
"""Koide phase: what the data fix, and whether 2/9 rad is a natural angle.

Companion to knowledge/sessions/koide_delta_gap_2026-09-11T1600.md.

Part 1 inverts the Z3 triality form sqrt(m_k) = M (1 + alpha cos(delta + 2 pi k/3))
exactly on the three charged-lepton masses (three masses, three parameters), then
propagates the PDG uncertainties by a seed-locked Monte Carlo to put an error bar on
delta and alpha. Generation assignment k = 0, 1, 2 = tau, e, mu, the assignment the
paper's delta = 2/9 selects (cos(2/9) is the largest of the three cosines).

Part 2 asks whether any "natural" angle -- a rational multiple of pi, an inverse
trigonometric function of a simple rational or surd, or the Berry phase of a symmetric
spherical cap -- lies inside the experimental band around the fitted delta. The families
are fixed here, before the scan, so the search is pre-registered rather than post hoc.

No hidden state: every input is a literal below. Seed fixed for the Monte Carlo only.
"""
import math
import random
from fractions import Fraction

SEED = 20260911
random.seed(SEED)

# PDG 2024 charged-lepton pole masses, MeV (central, one-sigma).
PDG = {
    "e":   (0.51099895069, 0.00000000016),
    "mu":  (105.6583755,   0.0000023),
    "tau": (1776.93,       0.09),
}
# PDG 2022 tau, used as a sensitivity check (the tau is what limits delta).
TAU_2022 = (1776.86, 0.12)

TWO_NINTHS = 2.0 / 9.0
SQRT2 = math.sqrt(2.0)


def fit(me, mmu, mtau):
    """Exact inversion of the Z3 form. Returns (M, alpha, delta) with alpha > 0,
    delta reduced to [0, 2 pi/3): k = 0 -> tau, 1 -> e, 2 -> mu."""
    r = [math.sqrt(mtau), math.sqrt(me), math.sqrt(mmu)]
    M = sum(r) / 3.0
    s = [x / M - 1.0 for x in r]              # s_k = alpha cos(delta + 2 pi k/3)
    a_cos = s[0]
    a_sin = (s[2] - s[1]) / math.sqrt(3.0)    # from the k = 1, 2 difference
    alpha = math.hypot(a_cos, a_sin)
    delta = math.atan2(a_sin, a_cos) % (2.0 * math.pi / 3.0)
    return M, alpha, delta


def predict(M, alpha, delta):
    return [(M * (1.0 + alpha * math.cos(delta + 2.0 * math.pi * k / 3.0))) ** 2
            for k in range(3)]                # [tau, e, mu]


def koide(me, mmu, mtau):
    return (me + mmu + mtau) / (math.sqrt(me) + math.sqrt(mmu) + math.sqrt(mtau)) ** 2


def part1(label, tau):
    me, mmu = PDG["e"][0], PDG["mu"][0]
    M, alpha, delta = fit(me, mmu, tau[0])
    # Seed-locked Monte Carlo over the PDG bands.
    N = 200000
    ds, As = [], []
    for _ in range(N):
        e_ = random.gauss(*PDG["e"])
        mu_ = random.gauss(*PDG["mu"])
        t_ = random.gauss(*tau)
        _, a_, d_ = fit(e_, mu_, t_)
        ds.append(d_)
        As.append(a_)
    dmean = sum(ds) / N
    dsig = math.sqrt(sum((x - dmean) ** 2 for x in ds) / (N - 1))
    amean = sum(As) / N
    asig = math.sqrt(sum((x - amean) ** 2 for x in As) / (N - 1))
    print(f"--- Part 1 [{label}]: exact inversion + MC error propagation (N={N}, seed={SEED})")
    print(f"inputs  m_e = {me} MeV, m_mu = {mmu} MeV, m_tau = {tau[0]} +/- {tau[1]} MeV")
    print(f"Koide ratio from data          = {koide(me, mmu, tau[0]):.8f}   (2/3 = {2/3:.8f}; "
          f"deviation {koide(me, mmu, tau[0]) - 2/3:+.2e})")
    print(f"M (scale)                      = {M:.6f} sqrt(MeV)")
    print(f"alpha (fitted)                 = {alpha:.7f} +/- {asig:.7f}   "
          f"(sqrt2 = {SQRT2:.7f}; shift {(alpha / SQRT2 - 1) * 100:+.4f}%, "
          f"{(alpha - SQRT2) / asig:+.2f} sigma)")
    print(f"delta (fitted)                 = {delta:.8f} +/- {dsig:.8f} rad")
    print(f"2/9                            = {TWO_NINTHS:.8f} rad")
    print(f"  2/9 - delta_fit              = {TWO_NINTHS - delta:+.8f} rad "
          f"= {(TWO_NINTHS - delta) / dsig:+.2f} sigma = {(TWO_NINTHS / delta - 1) * 100:+.4f}%")
    print(f"  relative width of the band   = {dsig / delta:.2e}  "
          f"(constrains ~{-math.log10(dsig / delta):.1f} significant figures of delta)")
    # The paper's construction: alpha = sqrt2, delta = 2/9, M from the tau mass alone.
    Mt = math.sqrt(tau[0]) / (1.0 + SQRT2 * math.cos(TWO_NINTHS))
    pt, pe, pmu = predict(Mt, SQRT2, TWO_NINTHS)
    print(f"paper construction (alpha=sqrt2, delta=2/9, M from tau):")
    print(f"  m_e  predicted = {pe:.6f} MeV   error {(pe / me - 1) * 100:+.4f}%")
    print(f"  m_mu predicted = {pmu:.4f} MeV   error {(pmu / mmu - 1) * 100:+.4f}%")
    print(f"  m_tau          = {pt:.2f} MeV   (scale)")
    return delta, dsig


def part2(delta, dsig, nsig=3.0):
    lo, hi = delta - nsig * dsig, delta + nsig * dsig
    print(f"--- Part 2: pre-registered natural-angle scan, band = delta_fit +/- {nsig:g} sigma "
          f"= [{lo:.8f}, {hi:.8f}] rad")
    print(f"2/9 rad = {math.degrees(TWO_NINTHS):.5f} deg = 1/{2 * math.pi / TWO_NINTHS:.4f} turn; "
          f"2/9 of a turn would be {2 * math.pi * TWO_NINTHS:.5f} rad")

    def report(name, cands):
        # cands: list of (value, description). Every family lives in (0, pi/2], so the
        # number of chance hits expected in the band is (count) x (band width)/(pi/2);
        # a family with expectation near 1 cannot distinguish a hit from noise.
        inside = [(v, d) for v, d in cands if lo <= v <= hi]
        best = min(cands, key=lambda c: abs(c[0] - delta))
        expect = len(cands) * (hi - lo) / (math.pi / 2)
        print(f"{name}: {len(cands)} candidates, {len(inside)} inside the band "
              f"(chance expectation {expect:.2f}); "
              f"nearest {best[1]} = {best[0]:.6f} rad at {abs(best[0] - delta) / dsig:.0f} sigma")
        for v, d in inside[:10]:
            print(f"    IN BAND: {d} = {v:.8f}")

    # (a) rational multiples of pi, p/q in lowest terms, q <= 400
    seen, cands = set(), []
    for q in range(1, 401):
        for p in range(1, q):
            f = Fraction(p, q)
            if f in seen or f > Fraction(1, 2):
                continue
            seen.add(f)
            cands.append((math.pi * p / q, f"{f.numerator}pi/{f.denominator}"))
    report("(a) rational multiples of pi (q<=400)", cands)
    small = [c for c in cands if Fraction(c[1].split("pi/")[0]).denominator == 1
             and int(c[1].split("pi/")[1]) <= 60]
    report("(a') rational multiples of pi, small denominators (q<=60)", small)

    # (b) acos / asin / atan of rationals p/q, q <= 100
    seen, cands = set(), []
    for q in range(1, 101):
        for p in range(0, q + 1):
            f = Fraction(p, q)
            if f in seen:
                continue
            seen.add(f)
            x = float(f)
            cands.append((math.acos(x), f"acos({f})"))
            cands.append((math.asin(x), f"asin({f})"))
            cands.append((math.atan(x), f"atan({f})"))
            if f.denominator != 1 or f.numerator > 1:
                cands.append((math.atan(1 / x) if x else math.pi / 2, f"atan({1/f})"))
    report("(b) acos/asin/atan of rationals (q<=100)", cands)

    # (c) acos / asin / atan of surds sqrt(p/q), q <= 100
    seen, cands = set(), []
    for q in range(1, 101):
        for p in range(1, 4 * q + 1):
            f = Fraction(p, q)
            if f in seen:
                continue
            seen.add(f)
            x = math.sqrt(float(f))
            if x <= 1.0:
                cands.append((math.acos(x), f"acos(sqrt({f}))"))
                cands.append((math.asin(x), f"asin(sqrt({f}))"))
            cands.append((math.atan(x), f"atan(sqrt({f}))"))
    report("(c) acos/asin/atan of surds sqrt(p/q) (q<=100)", cands)

    # (d) Berry phase of a symmetric cap on S2 of half-angle theta = p pi/q:
    #     gamma = Omega/2 = pi (1 - cos theta)
    seen, cands = set(), []
    for q in range(1, 201):
        for p in range(1, q + 1):
            f = Fraction(p, q)
            if f in seen:
                continue
            seen.add(f)
            th = math.pi * p / q
            cands.append((math.pi * (1 - math.cos(th)), f"cap Berry phase, half-angle {f}pi"))
    report("(d) cap Berry phases pi(1-cos(p pi/q)) (q<=200)", cands)

    # (e) the dimension-ratio reading taken literally as a fraction of a turn
    v = 2 * math.pi * TWO_NINTHS
    print(f"(e) 2pi x (2/9) = {v:.6f} rad, {abs(v - delta) / dsig:.0f} sigma from delta_fit")


if __name__ == "__main__":
    print(f"koide_delta_fit_and_angle_scan_2026-09-11T1600.py  seed={SEED}")
    d24, s24 = part1("PDG 2024", PDG["tau"])
    d22, s22 = part1("PDG 2022 tau, sensitivity", TAU_2022)
    print(f"shift of delta_fit between tau values = {d22 - d24:+.8f} rad "
          f"({(d22 - d24) / s24:+.2f} sigma_2024)")
    part2(d24, s24)
