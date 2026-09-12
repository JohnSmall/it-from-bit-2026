#!/usr/bin/env python3
# =====================================================================
#  NOTEBOOK M -- The explicit triple, its S3, and the leakage angle
#  (sedenion programme, checklist items 1-2 executed; the up-quark
#  candidate's derivation-or-refutation run). 2026-07-10.
#
#  QUESTION ON TRIAL: does a canonical, parameter-free angle of the
#  {O_i, zero-divisor} geometry equal delta0 = 2/9 rad = 0.22222 --
#  the recorded up-quark admixture candidate -- or not?
#
#  PRE-REGISTERED ANGLE BASKET (declared before computation; all
#  reported; comparisons counted):
#    T1  arg< psi, sigma psi >_C for psi in {e1, (e0+e1)/sqrt2,
#        uniform-V1, uniform-(H+V1)}; complex structure from a core
#        selected unit s in {e4, e8, e12}          (12 angles)
#    T2  the ZD leakage angle arcsin ||P_for L_z P_1|| for the
#        canonical cross unit z = (e_a + sigma(e_a))/sqrt2, a in V1
#        basis                                      (4 angles)
#    T3  principled dimension ratios only: kernel-dim/16, dim C/dim O
#  Reference set for near-miss reporting: {2/9, 1/9, 2/7, pi/9,
#  2pi/9, sin(2/9)}. A HIT = |theta - 2/9| < 0.003 AND a principled
#  construction; anything else is a MISS and says so.
#
#  STRUCTURAL CHECKS (PASS/FAIL): (A) exactly three octonion
#  subalgebras of S contain the core H = <e0,e4,e8,e12>: H (+) V_i,
#  V1 = <e1,e5,e9,e13>, V2 = <e2,e6,e10,e14>, V3 = <e3,e7,e11,e15>;
#  the grading V_i V_i c H, V_i V_j c V_k. (B) sigma (order 3) and
#  tau (involution) constructed and verified multiplicative on all
#  256 basis pairs: S3 <= Aut(S) by hand (Brown-consistent). (C) the
#  canonical cross units are zero divisors. Angles (D) are REPORTED.
# =====================================================================
import numpy as np, sys
from itertools import product

ok_all = True
def report(msg, ok):
    global ok_all
    print(("PASS " if ok else "FAIL ") + msg); ok_all &= ok

def cd_conj(x):
    y = x.copy(); y[1:] = -y[1:]; return y
def cd_mult(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2
    a, b = x[:h], x[h:]; c, d = y[:h], y[h:]
    return np.concatenate([cd_mult(a, c) - cd_mult(cd_conj(d), b),
                           cd_mult(d, a) + cd_mult(b, cd_conj(c))])
DIM = 16
E = np.eye(DIM)
def u(i): return E[i].copy()
def L(a): return np.column_stack([cd_mult(a, u(j)) for j in range(DIM)])
MT = np.zeros((16, 16, 16))
for i in range(16):
    for j in range(16):
        MT[i, j] = cd_mult(u(i), u(j))

print("== NOTEBOOK M: the triple, the S3, the angle ==")
CORE = [0, 4, 8, 12]
V = {1: [1, 5, 9, 13], 2: [2, 6, 10, 14], 3: [3, 7, 11, 15]}

def closed_in(idx):
    S = set(idx)
    for i in idx:
        for j in idx:
            supp = set(np.nonzero(np.abs(MT[i, j]) > 1e-12)[0])
            if not supp.issubset(S): return False
    return True
def composition_on(idx, trials=60):
    rng = np.random.default_rng(11)
    for _ in range(trials):
        x = np.zeros(DIM); y = np.zeros(DIM)
        x[idx] = rng.normal(size=len(idx)); y[idx] = rng.normal(size=len(idx))
        if abs(np.linalg.norm(cd_mult(x, y)) -
               np.linalg.norm(x) * np.linalg.norm(y)) > 1e-9: return False
    return True
okA1 = all(closed_in(CORE + V[i]) and composition_on(CORE + V[i]) for i in (1, 2, 3))
report("(A1) H(+)V_i closed and norm-multiplicative for i = 1,2,3: three "
       "octonion copies, explicit", okA1)

hits = set()
for k in range(16):
    if k in CORE: continue
    span = set(CORE)
    for c in CORE:
        span |= set(np.nonzero(np.abs(MT[c, k]) > 1e-12)[0])
    for i in (1, 2, 3):
        if span == set(CORE + V[i]): hits.add(i)
report(f"(A2) every core-doubling H + H.e_k lands in one of the three "
       f"(copies hit: {sorted(hits)}) -- the triple exhaustive over "
       f"core-doublings", hits == {1, 2, 3})

def sector_of(vec):
    supp = set(np.nonzero(np.abs(vec) > 1e-12)[0])
    for name, idx in [("H", CORE), ("V1", V[1]), ("V2", V[2]), ("V3", V[3])]:
        if supp.issubset(set(idx)): return name
    return "MIXED"
grade_ok = True
for i in (1, 2, 3):
    for j in (1, 2, 3):
        secs = {sector_of(MT[a, b]) for a in V[i] for b in V[j]}
        want = {"H"} if i == j else {f"V{6 - i - j}"}
        grade_ok &= secs == want
report("(A3) the grading holds: V_i V_i c H and V_i V_j c V_k (cyclic) -- "
       "the S3 is a grading of the algebra itself", grade_ok)

def build_auto(images):
    phi = {0: u(0)}
    for g, im in images.items(): phi[g] = im.copy()
    def img(k):
        if k in phi: return phi[k]
        for i in list(phi.keys()):
            for j in list(phi.keys()):
                v = MT[i, j]
                nz = np.nonzero(np.abs(v) > 1e-12)[0]
                if len(nz) == 1 and nz[0] == k:
                    phi[k] = v[k] * cd_mult(phi[i], phi[j]); return phi[k]
        return None
    for k in range(16):
        if img(k) is None: return None
    M = np.column_stack([phi[k] for k in range(16)])
    if not np.allclose(M.T @ M, np.eye(16), atol=1e-9): return None
    for i in range(16):
        for j in range(16):
            if not np.allclose(M @ MT[i, j], cd_mult(M @ u(i), M @ u(j)),
                               atol=1e-9): return None
    return M

# generators {e4, e8, e1, e2} reach all sectors (e3-sector = V1.V2 products);
# sigma may rotate the core's imaginary units among themselves
core_maps = []
for (a, b) in [(4,8),(4,12),(8,4),(8,12),(12,4),(12,8)]:
    for sa in (1,-1):
        for sb in (1,-1):
            core_maps.append({4: sa*u(a), 8: sb*u(b)})
sigma = None
for cm in core_maps:
    for s12 in (1,-1):
        for s23 in (1,-1):
            cand = build_auto({**cm, 1: s12*u(2), 2: s23*u(3)})
            if cand is not None and np.allclose(
                    np.linalg.matrix_power(cand, 3), np.eye(16), atol=1e-8):
                sigma = cand; break
        if sigma is not None: break
    if sigma is not None: break
report("(B1) sigma: order-3 automorphism fixing the core sector, cycling "
       "V1 -> V2 -> V3, multiplicative on all 256 pairs", sigma is not None)

tau = None
for cm in core_maps:
    for s1 in (1,-1):
        for s2 in (1,-1):
            cand = build_auto({**cm, 1: s1*u(1), 2: s2*u(3)})
            if cand is not None and np.allclose(cand @ cand, np.eye(16), atol=1e-8) \
               and sector_of(cand @ u(2)) == "V3":
                tau = cand; break
        if tau is not None: break
    if tau is not None: break
report("(B2) tau: involutive automorphism swapping V2 <-> V3 -- with sigma, "
       "S3 <= Aut(S) exhibited by hand (Brown-consistent)", tau is not None)

# DISCOVERED CORRECTION (first run): (e_a + sigma e_a) is an ISOMETRY --
# the true zero-divisor diagonal pairs a generation step WITH a doubling
# step: z = (a + sigma(e8 . a))/sqrt2. Cross-generation degeneracy needs
# BOTH an S3 move AND a tag-half flip: the mixing sector is literally
# (tag flip) x (generation step) -- the fourth qubit inside the algebra.
zd = []
if sigma is not None:
    for a in V[1]:
        da = cd_mult(u(8), u(a))                    # the doubling step
        w = sigma @ da                              # then the generation step
        b = int(np.argmax(np.abs(w)))
        z = (u(a) + np.sign(w[b]) * u(b)) / np.sqrt(2)
        smin = np.linalg.svd(L(z), compute_uv=False)[-1]
        zd.append((a, b, z, smin))
okC = bool(zd) and all(sv < 1e-10 for *_, sv in zd)
report(f"(C) the true zero-divisor diagonals z = (e_a + sigma(e8 e_a))/sqrt2, "
       f"every a in V1 (min sv: {[f'{sv:.1e}' for *_, sv in zd]}) -- mixing = "
       f"(tag flip) x (generation step)", okC)

print("\n== (D) the pre-registered angle inventory vs delta0 = 2/9 = 0.222222 ==")
DELTA0 = 2 / 9
refs = {"2/9": 2/9, "1/9": 1/9, "2/7": 2/7, "pi/9": np.pi/9,
        "2pi/9": 2*np.pi/9, "sin(2/9)": np.sin(2/9)}
def nearest(th):
    k = min(refs, key=lambda r: abs(refs[r] - th)); return k, refs[k]
angles = []
if sigma is not None:
    def carg(psi, s):
        re = float(psi @ (sigma @ psi))
        im = float(psi @ (L(u(s)) @ (sigma @ psi)))
        return np.arctan2(im, re)
    psis = {"e1": u(1), "(e0+e1)/sqrt2": (u(0)+u(1))/np.sqrt(2),
            "uniform-V1": sum(u(a) for a in V[1]) / 2,
            "uniform-H+V1": sum(u(a) for a in CORE + V[1]) / np.sqrt(8)}
    for pn, psi in psis.items():
        for s in (4, 8, 12):
            angles.append((f"T1 psi={pn:14s} s=e{s}", abs(carg(psi, s))))
    Pfor = np.zeros((16, 16))
    for a in V[2] + V[3]: Pfor[a, a] = 1
    P1 = np.zeros((16, 16))
    for a in V[1]: P1[a, a] = 1
    for a, b, z, _ in zd:
        th = float(np.arcsin(min(1.0, np.linalg.norm(Pfor @ L(z) @ P1, 2))))
        angles.append((f"T2 z=(e{a}+e{b})/sqrt2 leakage", th))
    kdim = int(np.sum(np.linalg.svd(L(zd[0][2]), compute_uv=False) < 1e-10))
    angles.append((f"T3 kernel ratio {kdim}/16", kdim / 16))
    angles.append(("T3 dim C / dim O = 2/8", 2 / 8))
n_hits = 0
for name, th in angles:
    k, v = nearest(th)
    hit = abs(th - DELTA0) < 0.003
    n_hits += hit
    print(f"  {name:44s} = {th:.5f}   nearest: {k} ({v:.5f})"
          + ("   <-- 2/9 HIT" if hit else ""))
print(f"\ncomparisons: {len(angles)}; hits on 2/9 within 0.003: {n_hits}")
print("angle inventory is a REPORT; a miss constrains where delta0 must come")
print("from and is recorded as such.")
print("\nSTRUCTURAL CHECKS:", "ALL PASS" if ok_all else "SOME FAILED")
if not ok_all:
    sys.exit(1)
