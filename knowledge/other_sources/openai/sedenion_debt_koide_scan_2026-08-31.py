"""
sedenion_debt_koide_scan_2026-08-31.py
Does the zero-divisor / norm-defect geometry touch fermion masses?  Explicit encodings.
Convention A as in sedenion_zero_divisor_scan_2026-08-31.py.  PASS/FAIL per check.
"""
import numpy as np, itertools, sys
rng = np.random.default_rng(831)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def cd(a, b):
    n = len(a)
    if n == 1: return a * b
    h = n // 2; p, q = a[:h], a[h:]; r, s = b[:h], b[h:]
    return np.concatenate([cd(p, r) - cd(conj(s), q), cd(s, p) + cd(q, conj(r))])
def unit(i, n=16):
    v = np.zeros(n); v[i] = 1.0; return v
def nrm2(x): return float(x @ x)
def assoc(x, y, z): return cd(cd(x, y), z) - cd(x, cd(y, z))
def imag_oct():
    v = rng.normal(size=8); v[0] = 0; return v
def emb(o): return np.concatenate([o, np.zeros(8)])
def tagunit(theta):                       # lambda = exp(theta e8) in the tag plane
    l = np.zeros(16); l[0], l[8] = np.cos(theta), np.sin(theta); return l
def rot(o, theta):                        # imaginary octonion o  ->  o.lambda  (its rotated copy)
    return cd(emb(o), tagunit(theta))
def phi(p, q, r): return float(cd(p, q) @ r)   # associative 3-form on Im O
def orthonormal_triple():
    p, q, r = imag_oct(), imag_oct(), imag_oct()
    p /= np.linalg.norm(p); q -= (q @ p) * p; q /= np.linalg.norm(q)
    r -= (r @ p) * p + (r @ q) * q; r /= np.linalg.norm(r); return p, q, r
def report(name, ok):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}"); return ok
allok = True

# ---- (1) generation degeneracy of the bare norm defect: Delta(z.lambda, w) = Delta(z, w) for ALL lambda in U(1)_ell
err = 0.0
for _ in range(100):
    x, y = imag_oct(), imag_oct(); w = rng.normal(size=16)
    z = np.concatenate([x, y]); th = rng.uniform(0, 2 * np.pi)
    zl = cd(z, tagunit(th))
    D0 = nrm2(cd(z, w)) - nrm2(z) * nrm2(w); D1 = nrm2(cd(zl, w)) - nrm2(zl) * nrm2(w)
    err = max(err, abs(D0 - D1))
allok &= report(f"norm defect against a fixed frame is U(1)_ell-invariant (hence psi-degenerate): max dev {err:.1e}", err < 1e-9)

# ---- (2) the product-norm ratio |zw|/(|z||w|) lies in [0, sqrt2]; both ends on the coassociative locus
x, y, u, v = unit(3, 8), unit(2, 8), unit(6, 8), unit(7, 8)     # {2,3,6,7} coassociative (complement of line {1,4,5})
zd  = np.concatenate([x, y]); w_minus = np.concatenate([u, -v]); w_plus = np.concatenate([u, v])
r_min = np.sqrt(nrm2(cd(zd, w_minus)) / (nrm2(zd) * nrm2(w_minus)))
r_max = np.sqrt(nrm2(cd(zd, w_plus)) / (nrm2(zd) * nrm2(w_plus)))
r_rand = max(np.sqrt(nrm2(cd(a, b)) / (nrm2(a) * nrm2(b))) for a, b in
             ((rng.normal(size=16), rng.normal(size=16)) for _ in range(20000)))
allok &= report(f"ratio = {r_min:.3f} (zero divisor) and {r_max:.4f} (= sqrt2, same plane, flipped orientation); "
                f"random max {r_rand:.4f} <= sqrt2", abs(r_min) < 1e-12 and abs(r_max - np.sqrt(2)) < 1e-12 and r_rand <= np.sqrt(2) + 1e-12)

# ---- (3) octonion associator norm on an orthonormal triple: |[p,q,r]|^2 = 4 (1 - phi^2)
err = 0.0
for _ in range(100):
    p, q, r = orthonormal_triple()
    err = max(err, abs(nrm2(assoc(p, q, r)) - 4 * (1 - phi(p, q, r) ** 2)))
allok &= report(f"|[p,q,r]|^2 = 4(1 - phi^2) on orthonormal imaginary triples: max dev {err:.1e}", err < 1e-9)

# ---- (4) THE ROTATED ASSOCIATOR:  [p.l, q.l, r.l]_S = [p,q,r]_O . l  -  2 phi(p,q,r) sin(3 theta) e8,  l = exp(theta e8)
err = 0.0; tagpart_on_halvings = 0.0
for _ in range(100):
    p, q, r = orthonormal_triple(); th = rng.uniform(0, 2 * np.pi)
    lhs = assoc(rot(p, th), rot(q, th), rot(r, th))
    rhs = cd(emb(assoc(p, q, r)), tagunit(th)) - 2 * phi(p, q, r) * np.sin(3 * th) * unit(8)
    err = max(err, np.linalg.norm(lhs - rhs))
    for k in range(6):   # on the halvings (theta = k pi/3) the tag component vanishes
        tagpart_on_halvings = max(tagpart_on_halvings, abs(assoc(rot(p, k*np.pi/3), rot(q, k*np.pi/3), rot(r, k*np.pi/3))[8]))
allok &= report(f"rotated-associator identity: max dev {err:.1e}; tag component on the six halving angles {tagpart_on_halvings:.1e}",
                err < 1e-9 and tagpart_on_halvings < 1e-9)

# ---- (5) debt anatomy: orbit part (rotates with psi) vs tag part (psi-fixed); ratio of norms
#          |orbit| / |tag| = sqrt(1 - phi^2) / (|phi| |sin 3theta|)
err = 0.0
for _ in range(100):
    p, q, r = orthonormal_triple(); th = rng.uniform(0.1, 0.9)
    D = assoc(rot(p, th), rot(q, th), rot(r, th))
    orbit = np.linalg.norm(np.concatenate([D[1:8], D[9:16]])); tag = abs(D[8])
    err = max(err, abs(orbit / tag - np.sqrt(1 - phi(p, q, r) ** 2) / (abs(phi(p, q, r)) * abs(np.sin(3 * th)))))
allok &= report(f"|orbit debt|/|tag debt| = sqrt(1-phi^2)/(|phi| |sin 3theta|): max dev {err:.1e}", err < 1e-8)

# ---- (6) Koide numerology.  Frame f reading the debt with equal weight on the orbit plane and the tag line;
#          sqrt(m_k) := <f, D_k>, D_k the debt of the k-th psi-copy.  Then Sum m / (Sum sqrt m)^2 = 1/3 + A^2/(6U^2),
#          A/U = sqrt(1-phi^2)/(|phi| |sin3theta|).  Koide 2/3  <=>  A/U = sqrt2.  At theta = pi/6: <=> phi^2 = 1/3.
def koide_ratio(p, q, r, th, frame_azimuth):
    sm = []
    for k in range(3):
        D = assoc(rot(p, th + 2*np.pi*k/3), rot(q, th + 2*np.pi*k/3), rot(r, th + 2*np.pi*k/3))
        orb = np.concatenate([D[1:8], D[9:16]]); n_orb = np.linalg.norm(orb)
        # orbit plane spanned by A0 = [p,q,r].l and A0.e8 ; frame at azimuth 'frame_azimuth' in that plane, |f_P| = |f_ell| = 1/sqrt2
        A0 = cd(emb(assoc(p, q, r)), tagunit(th)); A1 = cd(A0, unit(8)); A0 /= np.linalg.norm(A0); A1 /= np.linalg.norm(A1)
        f = (np.cos(frame_azimuth) * A0 + np.sin(frame_azimuth) * A1) / np.sqrt(2) + unit(8) / np.sqrt(2)
        sm.append(float(f @ D))
    sm = np.array(sm); m = sm ** 2
    return m.sum() / sm.sum() ** 2, sm
p, q = unit(1, 8), unit(2, 8)
r = (unit(3, 8) + unit(5, 8) + unit(6, 8)) / np.sqrt(3)         # orthonormal, phi(p,q,r)^2 = 1/3
K13 = [koide_ratio(p, q, r, np.pi / 6, az)[0] for az in rng.uniform(0, 2*np.pi, 20)]
p2, q2, r2 = orthonormal_triple()
Kgen = koide_ratio(p2, q2, r2, np.pi / 6, 0.3)[0]
allok &= report(f"phi^2 = 1/3, theta = pi/6, equal-weight frame: Koide ratio = {np.mean(K13):.6f} for every frame azimuth (spread {np.ptp(K13):.1e}); "
                f"generic triple (phi^2 = {phi(p2,q2,r2)**2:.3f}): {Kgen:.4f}", np.allclose(K13, 2/3))
K, sm = koide_ratio(p, q, r, np.pi / 6, 2/9)
print(f"      sample at frame azimuth delta = 2/9: sqrt(m_k) proportional to {np.round(sm / sm.max(), 4)}, "
      f"m ratios {np.round((sm**2) / (sm**2).max(), 5)}  (Koide-parametrised e/mu/tau: 1 + sqrt2 cos(2/9 + 2 pi k/3))")
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED"); sys.exit(0 if allok else 1)
