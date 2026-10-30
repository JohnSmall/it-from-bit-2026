#!/usr/bin/env python3
"""One-loop SM running of alpha', alpha_2, alpha_3 from M_Z (PDG 2024 MSbar inputs).
Question: does the fibre-dimension rule g'^2 : g^2 : g_s^2 = 1 : 3 : 8 hold at the
3.6 TeV matching scale where sin^2(theta_W) = 1/4 is attained?  No randomness."""
import math
MZ, MT = 91.1876, 172.57
alpha_inv, s2w, a3 = 127.951, 0.23121, 0.1180        # alpha(M_Z) MSbar, sin^2 theta_W MSbar, alpha_s(M_Z)
a = 1 / alpha_inv
ap_inv = (1 - s2w) / a      # 1/alpha'  (g' unnormalised, not GUT-normalised)
a2_inv = s2w / a            # 1/alpha_2
a3_inv = 1 / a3
bY, b2 = -41/6, 19/6        # SM one-loop: d(1/alpha)/dln(mu) = b/(2 pi)
def b3(mu): return 23/3 if mu < MT else 7.0
def run(mu):
    L = math.log(mu / MZ)
    ap = ap_inv + bY / (2*math.pi) * L
    a2 = a2_inv + b2 / (2*math.pi) * L
    if mu <= MT:
        a3i = a3_inv + (23/3) / (2*math.pi) * L
    else:
        a3i = a3_inv + (23/3) / (2*math.pi) * math.log(MT/MZ) + 7.0 / (2*math.pi) * math.log(mu/MT)
    return 1/ap, 1/a2, 1/a3i
for mu in (MZ, 500, 1000, 2000, 3600, 5000, 10000):
    ap, a2, a3_ = run(mu)
    print(f"mu = {mu:7.1f} GeV  sin2W = {ap/(ap+a2):.4f}  a2/a' = {a2/ap:.3f}  a3/a' = {a3_/ap:.3f}  a3/a2 = {a3_/a2:.3f}")
# scale where sin2W = 1/4, and where a3/a2 = 8/3, and where a3/a' = 8
def bisect(f, lo, hi):
    for _ in range(200):
        mid = math.sqrt(lo*hi)
        if f(lo) * f(mid) <= 0: hi = mid
        else: lo = mid
    return mid
m1 = bisect(lambda m: run(m)[0]/(run(m)[0]+run(m)[1]) - 0.25, 200, 1e5)
m2 = bisect(lambda m: run(m)[2]/run(m)[1] - 8/3, 100, 1e5)
m3 = bisect(lambda m: run(m)[2]/run(m)[0] - 8.0, 100, 1e5)
print(f"sin2W = 1/4 at mu = {m1:.0f} GeV;  a3/a2 = 8/3 at mu = {m2:.0f} GeV;  a3/a' = 8 at mu = {m3:.0f} GeV")
