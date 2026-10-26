#!/usr/bin/env python3
"""antitelephone_network_associativity_2026-09-27T1900.py

JS, 2026-09-27: many agents sending messages to each other by tachyonic
antitelephones requires composing transports (rotations) on a parallelisable
sphere, and that cannot be done consistently on S^7.  This script checks the
statements the revised spacetime paragraph makes, in Convention A octonions:

  A. Two antitelephone links always compose consistently: the subalgebra two
     octonions generate is associative (Artin; a Moufang loop is
     diassociative).  Max associator over all ordered triples of words of
     length <= 3 in x, y and their conjugates (16 words, all ordered triples).
  B. Three generic links do not: |(xy)z - x(yz)| for random unit links.
  C. Three links in one quaternionic subalgebra H = span{1,a,b,ab} do.
  D. Harvey--Lawson: for imaginary x,y,z the associative calibration
     phi(x,y,z) = <x, yz> obeys phi^2 + c |[x,y,z]|^2 = |x ^ y ^ z|^2 with a
     constant c; equality phi = vol (associative 3-plane) iff the associator
     vanishes.  The constant is fitted and reported.
  E. Maximality: with x, y in H and z anywhere, [x,y,z] = [x,y,z_perp] and
     |[x,y,z]| = 2 |Im x ^ Im y| |z_perp|, so the network's inconsistency
     measures exactly the part of the third link outside the quaternionic
     subalgebra.  A consistent network is confined to an S^3.
  F. Rotations: L_x L_y is a rotation of R^8 (SO(8) is a group) but is not
     L_{xy}, nor L_w for any w; on the quaternions L_x L_y = L_{xy} exactly.
  G. Control: quaternion rung, all associators vanish.

Convention A; seed 20260927; numpy only.  No hidden state.
"""
import itertools

import numpy as np

rng = np.random.default_rng(20260927)
N = 2000


def conj(x):
    y = np.array(x, copy=True); y[1:] = -y[1:]; return y


def cd(x, y):
    n = x.size
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate((cd(a, c) - cd(conj(d), b), cd(d, a) + cd(b, conj(c))))


def assoc(x, y, z):
    return cd(cd(x, y), z) - cd(x, cd(y, z))


def unit(v):
    return v / np.linalg.norm(v)


def rand_unit(n):
    return unit(rng.standard_normal(n))


def rand_imag_unit(n):
    v = rng.standard_normal(n); v[0] = 0.0; return unit(v)


def vol3(u, v, w):
    G = np.array([[u @ u, u @ v, u @ w], [v @ u, v @ v, v @ w], [w @ u, w @ v, w @ w]])
    return np.sqrt(max(np.linalg.det(G), 0.0))


def phi(u, v, w):                      # associative 3-form on Im O
    return u @ cd(v, w)


def left_mult(x):
    n = x.size
    return np.array([cd(x, np.eye(n)[j]) for j in range(n)]).T   # column j = x e_j


def quaternion_subalgebra():
    """Random quaternionic subalgebra of O: orthonormal imaginary a, b, c = ab."""
    a = rand_imag_unit(8)
    b = rng.standard_normal(8); b[0] = 0.0; b -= (b @ a) * a; b = unit(b)
    c = cd(a, b)
    one = np.eye(8)[0]
    return one, a, b, c


def in_H(one, a, b, c):
    co = rng.standard_normal(4)
    return unit(co[0] * one + co[1] * a + co[2] * b + co[3] * c)


print("Antitelephone network associativity, Convention A octonions, seed 20260927")
print("=" * 78)

# --- A
print("A. two links always compose (diassociativity)")
worst = 0.0
for _ in range(10):
    x, y = rand_unit(8), rand_unit(8)
    gens = [x, y, conj(x), conj(y)]
    words = list(gens)
    words = words + [cd(u, v) for u in words for v in gens]          # length 2
    words = words + [cd(u, v) for u in words[4:] for v in gens[:2]]  # some of length 3
    words = words[:16]
    for u, v, w in itertools.product(words, repeat=3):
        worst = max(worst, np.linalg.norm(assoc(u, v, w)))
print("   max |[u,v,w]| over words in two random links (10 pairs, 16 words each):  %.3e" % worst)

# --- B
print("B. three generic links: relay discrepancy |(xy)z - x(yz)|, unit links")
d = np.array([np.linalg.norm(assoc(rand_unit(8), rand_unit(8), rand_unit(8))) for _ in range(N)])
print("   N=%d  min %.4f  median %.4f  max %.4f  (zero would be consistent)" % (N, d.min(), np.median(d), d.max()))

# --- C
print("C. three links inside one quaternionic subalgebra")
worst_assoc, worst_closure = 0.0, 0.0
for _ in range(200):
    one, a, b, c = quaternion_subalgebra()
    worst_closure = max(worst_closure,
                        np.linalg.norm(cd(b, c) - a), np.linalg.norm(cd(c, a) - b),
                        abs(c[0]), abs(c @ a), abs(c @ b), abs(np.linalg.norm(c) - 1))
    x, y, z = (in_H(one, a, b, c) for _ in range(3))
    worst_assoc = max(worst_assoc, np.linalg.norm(assoc(x, y, z)))
print("   closure of span{1,a,b,ab} as quaternions (bc=a, ca=b, c imaginary unit): %.3e" % worst_closure)
print("   max |[x,y,z]| for x,y,z in H (200 subalgebras):                       %.3e" % worst_assoc)

# --- D
print("D. Harvey--Lawson calibration identity on Im O")
ratios, cfit = [], []
for _ in range(N):
    u, v, w = (rand_imag_unit(8) for _ in range(3))
    V, P, A = vol3(u, v, w), phi(u, v, w), np.linalg.norm(assoc(u, v, w))
    ratios.append(abs(P) / V)
    cfit.append((V * V - P * P) / (A * A))
ratios, cfit = np.array(ratios), np.array(cfit)
print("   random imaginary triples: max |phi|/vol = %.6f  (< 1: none associative)" % ratios.max())
print("   fitted c = (vol^2 - phi^2)/|[u,v,w]|^2: min %.15f  max %.15f" % (cfit.min(), cfit.max()))
worst_q = 0.0
for _ in range(200):
    one, a, b, c = quaternion_subalgebra()
    u, v, w = (in_H(one, a, b, c) for _ in range(3))
    u, v, w = (t - t[0] * one for t in (u, v, w))          # imaginary parts
    worst_q = max(worst_q, abs(abs(phi(u, v, w)) - vol3(u, v, w)))
print("   quaternionic triples: max | |phi| - vol | = %.3e  (calibration saturated)" % worst_q)

# --- E
print("E. maximality: two links in H, third link anywhere")
worst_lin, worst_norm, min_assoc = 0.0, 0.0, np.inf
for _ in range(N):
    one, a, b, c = quaternion_subalgebra()
    x, y = in_H(one, a, b, c), in_H(one, a, b, c)
    z = rand_unit(8)
    zH = sum((z @ e) * e for e in (one, a, b, c))
    zp = z - zH
    A = assoc(x, y, z)
    worst_lin = max(worst_lin, np.linalg.norm(A - assoc(x, y, zp)))
    xi, yi = x - x[0] * one, y - y[0] * one
    pred = 2.0 * np.sqrt(max((xi @ xi) * (yi @ yi) - (xi @ yi) ** 2, 0.0)) * np.linalg.norm(zp)
    worst_norm = max(worst_norm, abs(np.linalg.norm(A) - pred))
    min_assoc = min(min_assoc, np.linalg.norm(A) / np.linalg.norm(zp))
print("   max |[x,y,z] - [x,y,z_perp]|:                         %.3e" % worst_lin)
print("   max | |[x,y,z]| - 2 |Im x ^ Im y| |z_perp| |:            %.3e" % worst_norm)
print("   min |[x,y,z]| / |z_perp| over N=%d:                    %.4f  (> 0: every escape from H is seen)" % (N, min_assoc))

# --- F
print("F. rotations: relay L_x L_y against a single link")
dev_gen, dev_H, orth = 0.0, np.inf, 0.0
for _ in range(200):
    x, y = rand_unit(8), rand_unit(8)
    M = left_mult(x) @ left_mult(y)
    orth = max(orth, np.linalg.norm(M.T @ M - np.eye(8)))
    dev_gen = max(dev_gen, np.linalg.norm(M - left_mult(cd(x, y))))
    # best single link w: L_w is determined by its first column w = M e_0 = x(y e_0) = xy
    one, a, b, c = quaternion_subalgebra()
    xq, yq = in_H(one, a, b, c), in_H(one, a, b, c)
    Mq = left_mult(xq) @ left_mult(yq)
    dev_H = min(dev_H, np.linalg.norm(Mq - left_mult(cd(xq, yq))))
print("   L_x L_y orthogonal (max |M^T M - 1|):                  %.3e  (a rotation of R^8)" % orth)
print("   max |L_x L_y - L_{xy}|, generic octonion links:         %.4f  (not any single link)" % dev_gen)
print("   min |L_x L_y - L_{xy}|, both links in one H, on all R^8: %.4f  (fails off H)" % dev_H)
worst4 = 0.0
for _ in range(200):
    x, y = rand_unit(4), rand_unit(4)
    worst4 = max(worst4, np.linalg.norm(left_mult(x) @ left_mult(y) - left_mult(cd(x, y))))
print("   max |L_x L_y - L_{xy}| on the quaternions (S^3):         %.3e" % worst4)

# --- G
print("G. control: quaternion rung")
w4 = max(np.linalg.norm(assoc(rand_unit(4), rand_unit(4), rand_unit(4))) for _ in range(N))
print("   max |[x,y,z]| over N=%d random unit quaternions:        %.3e" % (N, w4))

print("=" * 78)
ok = (worst < 1e-12 and d.min() > 1e-3 and worst_assoc < 1e-12 and ratios.max() < 1
      and cfit.max() - cfit.min() < 1e-9 and worst_q < 1e-12 and worst_lin < 1e-12
      and worst_norm < 1e-12 and min_assoc > 1e-3 and dev_gen > 1e-3 and dev_H > 1e-3
      and worst4 < 1e-12 and w4 < 1e-12)
print("ANTITELEPHONE NETWORK: %s" % ("PASS" if ok else "FAIL"))
