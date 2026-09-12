#!/usr/bin/env python3
"""Notebook M's angle inventory, re-run on the psi-orbit triple.

WHY. Notebook M (2026-07-10) scanned eighteen structural angles of the sedenion
triple for delta_0 = 2/9 and found none. Notebook T (2026-08-27) then showed M
had scanned the WRONG triple: Brown's S_3 stabilises each octonion copy
core (+) V_i, which are cycled instead by a lifted G_2 element and are colour
structure. The triple Brown's S_3 actually permutes is the three halvings
O, psi(O), psi^2(O), and the generations are that psi-orbit. So M's verdict
closes the colour-triple frame and says nothing about the generation frame.
This re-runs the inventory on the correct triple.

CONSTRUCTIONS, both taken from the notebooks rather than reinvented:
  Cayley-Dickson convention A, (a,b)(c,d) = (ac - d*b, da + bc*), as in
  notebook M. Brown's maps as in notebook T:
      psi(a, b) = ( [a + 3a* + sqrt3 (b - b*)]/4,
                    [b + 3b* - sqrt3 (a - a*)]/4 )
      eps(a, b) = (a, -b)
  The halvings are H_k = psi^k(O), O = span(e0..e7), all doubled by e8.

PRE-REGISTERED BASKET, declared before any computation, all entries reported:

  P1  relative phase under psi: |arg <x, psi x>_s| for the four vectors
      x in {e1, (e0+e1)/sqrt2, uniform over Im(O), uniform over O} and the
      three imaginary units s in {e8, e4, e12}. e8 is the principled choice:
      Fix(psi) = span{e0, e8}, so e8 is the ONLY imaginary unit psi fixes and
      the only one giving a psi-equivariant complex structure. e4 and e12 are
      carried for comparability with M's basket and are flagged unprincipled.
                                                                    (12 angles)
  P2  the frame misalignment: the principal angles between Im(H_0) and
      Im(H_1), the imaginary parts of two halvings, reported as the distinct
      values with multiplicities. This is the direct "angle between generation
      frames", the quantity M's T1 was reaching for on the wrong triple.
  P3  the cross-halving leakage: arcsin of the operator norm of
      Pi_1 L_z Pi_0, with Pi_k the orthogonal projector onto Im(H_k) and z the
      canonical zero divisor of notebook M, z = (e_a + sigma(e8 e_a))/sqrt2
      rebuilt here with psi in place of sigma: z = (x + psi(e8 x))/sqrt2.
                                                                    (4 angles)
  P4  principled dimension ratios: dim Fix(psi)/dim S, dim C/dim O,
      pairwise-intersection/halving.

HIT CRITERION, unchanged from M: |theta - 2/9| < 0.003 AND a principled
construction. Anything else is a miss and says so. Reference set for near-miss
reporting is M's: {2/9, 1/9, 2/7, pi/9, 2pi/9, sin(2/9)}.

No seed is needed: every quantity is exact linear algebra on fixed bases.
"""

import numpy as np

np.set_printoptions(precision=6, suppress=True)
DIM = 16
SQ3 = np.sqrt(3.0)
DELTA0 = 2.0 / 9.0
E = np.eye(DIM)


def cd_conj(x):
    y = x.copy()
    y[1:] = -y[1:]
    return y


def cd_mult(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b = x[:h], x[h:]
    c, d = y[:h], y[h:]
    return np.concatenate([cd_mult(a, c) - cd_mult(cd_conj(d), b),
                           cd_mult(d, a) + cd_mult(b, cd_conj(c))])


def u(i):
    return E[i].copy()


def L(a):
    return np.column_stack([cd_mult(a, u(j)) for j in range(DIM)])


def psi_vec(x):
    h = DIM // 2
    a, b = x[:h], x[h:]
    ac, bc = cd_conj(a), cd_conj(b)
    return np.concatenate([(a + 3 * ac + SQ3 * (b - bc)) / 4.0,
                           (b + 3 * bc - SQ3 * (a - ac)) / 4.0])


PSI = np.column_stack([psi_vec(E[i]) for i in range(DIM)])
EPS = np.diag([1.0] * 8 + [-1.0] * 8)


def is_automorphism(M):
    w = 0.0
    for i in range(DIM):
        for j in range(DIM):
            w = max(w, np.max(np.abs(M @ cd_mult(u(i), u(j))
                                     - cd_mult(M @ u(i), M @ u(j)))))
    return w


def proj(cols):
    Q, _ = np.linalg.qr(cols)
    return Q @ Q.T


print("== psi-orbit angle inventory (notebook M's basket, notebook T's triple) ==")

# ---- structural checks, so the re-run stands on its own -------------------
w = is_automorphism(PSI)
print(f"(A) psi is an automorphism of S: worst violation {w:.2e}")
print(f"(A) psi^3 = I: {np.allclose(np.linalg.matrix_power(PSI, 3), np.eye(DIM))}"
      f"; eps^2 = I: {np.allclose(EPS @ EPS, np.eye(DIM))}"
      f"; eps psi = psi^2 eps: "
      f"{np.allclose(EPS @ PSI, np.linalg.matrix_power(PSI, 2) @ EPS)}")
fix = np.linalg.svd(PSI - np.eye(DIM))[2][np.linalg.matrix_rank(PSI - np.eye(DIM), tol=1e-9):]
onaxis = [f"e{i}" for i in range(DIM)
          if np.linalg.norm(fix @ E[i]) > 0.9]
print(f"(A) dim Fix(psi) = {fix.shape[0]}; basis units it contains: {onaxis}")

O = np.column_stack([E[i] for i in range(8)])
H = [O, PSI @ O, PSI @ PSI @ O]
ImH = [np.column_stack([h[:, i] for i in range(1, 8)]) for h in H]
print(f"(A) the three halvings are 8-dimensional subalgebras, pairwise "
      f"intersection dim "
      f"{DIM - np.linalg.matrix_rank(np.vstack([np.eye(DIM) - proj(H[0]), np.eye(DIM) - proj(H[1])]), tol=1e-9)}")

angles = []

# ---- P1 : relative phase under psi ---------------------------------------
def carg(x, s):
    re = float(x @ (PSI @ x))
    im = float(x @ (L(u(s)) @ (PSI @ x)))
    return abs(np.arctan2(im, re))


xs = {"e1": u(1),
      "(e0+e1)/sqrt2": (u(0) + u(1)) / np.sqrt(2),
      "uniform-Im(O)": sum(u(i) for i in range(1, 8)) / np.sqrt(7),
      "uniform-O": sum(u(i) for i in range(8)) / np.sqrt(8)}
for xn, x in xs.items():
    for s in (8, 4, 12):
        tag = "principled" if s == 8 else "comparability"
        angles.append((f"P1 x={xn:14s} s=e{s:<2d} [{tag}]", carg(x, s), s == 8))

# ---- P2 : principal angles between Im(H_0) and Im(H_1) --------------------
Q0, _ = np.linalg.qr(ImH[0])
Q1, _ = np.linalg.qr(ImH[1])
sv = np.clip(np.linalg.svd(Q0.T @ Q1, compute_uv=False), -1.0, 1.0)
pa = np.arccos(sv)
seen = []
for th in pa:
    for s in seen:
        if abs(s[0] - th) < 1e-9:
            s[1] += 1
            break
    else:
        seen.append([th, 1])
for th, mult in seen:
    angles.append((f"P2 principal angle Im(H0),Im(H1)  x{mult} [principled]", th, True))

# ---- P3 : cross-halving leakage ------------------------------------------
Pi0, Pi1 = proj(ImH[0]), proj(ImH[1])
for a in (1, 2, 3, 5):
    x = u(a)
    z = (x + PSI @ cd_mult(u(8), x)) / np.sqrt(2)
    nz = np.linalg.norm(z)
    zt = z / nz if nz > 1e-12 else z
    th = float(np.arcsin(min(1.0, np.linalg.norm(Pi1 @ L(zt) @ Pi0, 2))))
    angles.append((f"P3 leakage z from e{a} [principled]", th, True))

# ---- P4 : dimension ratios -----------------------------------------------
angles.append(("P4 dim Fix(psi)/dim S = 2/16 [principled]", 2 / 16, True))
angles.append(("P4 dim C / dim O = 2/8    [principled]", 2 / 8, True))
angles.append(("P4 pairwise intersection / halving = 1/8 [principled]", 1 / 8, True))

# ---- report ---------------------------------------------------------------
refs = {"2/9": 2 / 9, "1/9": 1 / 9, "2/7": 2 / 7, "pi/9": np.pi / 9,
        "2pi/9": 2 * np.pi / 9, "sin(2/9)": np.sin(2 / 9)}
print(f"\n== the inventory against delta_0 = 2/9 = {DELTA0:.6f} ==")
hits = 0
for name, th, principled in angles:
    k = min(refs, key=lambda r: abs(refs[r] - th))
    hit = abs(th - DELTA0) < 0.003 and principled
    hits += hit
    # Is the value a rational multiple of pi with a small denominator? That is
    # the signature a discrete symmetry leaves, and 2/9 rad is not one.
    extra = "  (= 0 exactly)" if abs(th) < 1e-12 else ""
    if not extra:
        from fractions import Fraction
        f = Fraction(th / np.pi).limit_denominator(24)
        if abs(float(f) * np.pi - th) < 1e-12:
            lab = ("pi" if f == 1 else
                   f"{f.numerator}pi/{f.denominator}" if f.numerator != 1
                   else f"pi/{f.denominator}")
            extra = f"  (= {lab} exactly, to {abs(float(f)*np.pi - th):.1e})"
    print(f"  {name:52s} = {th:.6f}  nearest: {k} ({refs[k]:.5f})"
          + ("   <-- 2/9 HIT" if hit else "") + extra)
print(f"\ncomparisons: {len(angles)}; principled: {sum(1 for _,_,p in angles if p)};"
      f" hits on 2/9 within 0.003: {hits}")
