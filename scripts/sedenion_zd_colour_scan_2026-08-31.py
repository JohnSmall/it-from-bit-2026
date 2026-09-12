"""
sedenion_zd_colour_scan_2026-08-31.py
The zero-divisor <-> SU(3) colour dictionary, as explicit encodings.
Convention A (as in sedenion_zero_divisor_scan_2026-08-31.py): (a,b)(c,d) = (ac - conj(d)b, da + b conj(c));
e4 = octonion doubling unit, e8 = tag.  Colour: fix a unit imaginary j; SU(3) = Stab_{G2}(j) built here from
first principles as {D in Der(O): Dj = 0} exponentiated (no basis conventions assumed).  PASS/FAIL per check.
"""
import numpy as np, itertools, sys
from scipy.linalg import expm
rng = np.random.default_rng(20260831)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def cd(a, b):
    n = len(a)
    if n == 1: return a * b
    h = n // 2; p, q = a[:h], a[h:]; r, s = b[:h], b[h:]
    return np.concatenate([cd(p, r) - cd(conj(s), q), cd(s, p) + cd(q, conj(r))])
def unit(i, n=16):
    v = np.zeros(n); v[i] = 1.0; return v
def u8(i): return unit(i, 8)
def nrm2(x): return float(x @ x)
def imag_oct():
    v = rng.normal(size=8); v[0] = 0; return v
def emb(o): return np.concatenate([o, np.zeros(8)])
def tagunit(th):
    l = np.zeros(16); l[0], l[8] = np.cos(th), np.sin(th); return l
def kerdim(z):
    M = np.column_stack([cd(z, unit(k)) for k in range(16)])
    return 16 - np.linalg.matrix_rank(M, tol=1e-9)
def report(name, ok):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}"); return ok
allok = True

def rand_dir():
    j = imag_oct(); return j / np.linalg.norm(j)
def colour_basis(j):                       # orthonormal complex basis (u_a, j u_a) of C^3_j
    B = []
    while len(B) < 3:
        u = imag_oct(); u -= (u @ j) * j
        for b in B: u -= (u @ b[0]) * b[0] + (u @ b[1]) * b[1]
        n = np.linalg.norm(u)
        if n < 1e-6: continue
        u /= n; B.append((u, cd(j, u)))
    return B
def zd_of(x, j):     return np.concatenate([x, cd(j, x)])   # colour vector, tag-doubled
def antizd_of(u, j): return np.concatenate([u, cd(u, j)])   # anti-colour (direction -j)

# ---- (1) j = xy makes span(x,y) a complex line: jx = y, jy = -x; z = x + (jx) ell has ker dim 4
ok = True
for _ in range(40):
    x = rand_dir(); y = imag_oct(); y -= (y @ x) * x; y /= np.linalg.norm(y)
    j = cd(x, y)
    ok &= np.allclose(cd(j, x), y) and np.allclose(cd(j, y), -x) and abs(nrm2(j) - 1) < 1e-12
    ok &= kerdim(np.concatenate([x, y])) == 4
allok &= report("j = xy: L_j rotates span(x,y) (jx = y, jy = -x); z = x + (jx) ell has ker dim 4", ok)

# ---- (2) unit ZDs over a fixed j = the colour 5-sphere; direction recovery x(jx) = j
ok = True
for _ in range(40):
    j = rand_dir(); B = colour_basis(j)
    c = rng.normal(size=6); c /= np.linalg.norm(c)
    x = sum(c[2*a] * B[a][0] + c[2*a+1] * B[a][1] for a in range(3))
    ok &= kerdim(zd_of(x, j)) == 4 and np.allclose(cd(x, cd(j, x)), j)
allok &= report("unit ZDs with direction j <-> unit colour vectors x in C^3_j (an S^5); x(jx) = j", ok)

# ---- (3) SU(3) = Stab_{G2}(j), from first principles: Der(O) is 14-dim, {Dj = 0} is 8-dim,
#          exponentials are automorphisms fixing j, and their colour matrices are special unitary
def liftD(m):
    def f(v):
        out = np.zeros(8); out[1:] = m @ v[1:]; return out
    return f
eqs = [(i, jj) for i in range(1, 8) for jj in range(i + 1, 8)]
A = np.zeros((len(eqs) * 8, 49))
for col in range(49):
    a, b = divmod(col, 7); m = np.zeros((7, 7)); m[a, b] = 1; f = liftD(m)
    for r, (i, jj) in enumerate(eqs):
        A[r*8:(r+1)*8, col] = f(cd(u8(i), u8(jj))) - cd(f(u8(i)), u8(jj)) - cd(u8(i), f(u8(jj)))
sv, Vt = np.linalg.svd(A)[1], np.linalg.svd(A)[2]
dim_g2 = int(np.sum(sv < 1e-9 * sv[0])); G2b = Vt[-dim_g2:].T
C = np.column_stack([G2b[:, k].reshape(7, 7)[:, 3] for k in range(dim_g2)])   # D e4 column
W = np.linalg.svd(C)[2][np.linalg.matrix_rank(C, tol=1e-9):].T
su3 = [ (G2b @ W[:, k]).reshape(7, 7) for k in range(W.shape[1]) ]
j4 = u8(4); Bstd = [(u8(a), cd(j4, u8(a))) for a in (1, 2, 3)]
def gexp(coef, t=1.0):
    E = expm(t * sum(c * m for c, m in zip(coef, su3)))
    def fO(v):
        out = v.copy() * 0; out[0] = v[0]; out[1:] = E @ v[1:]; return out
    return fO
def colour_matrix(fO):
    M = np.zeros((3, 3), dtype=complex)
    for a in range(3):
        gv = fO(Bstd[a][0])
        for b in range(3): M[b, a] = complex(gv @ Bstd[b][0], gv @ Bstd[b][1])
    return M
ok = dim_g2 == 14 and len(su3) == 8
fO = gexp(rng.normal(size=8))
ok &= all(np.linalg.norm(fO(cd(p, q)) - cd(fO(p), fO(q))) < 1e-8 for p, q in
          [(rng.normal(size=8), rng.normal(size=8)) for _ in range(30)])
M = colour_matrix(fO)
ok &= np.allclose(fO(j4), j4) and np.allclose(M.conj().T @ M, np.eye(3), atol=1e-8) and abs(np.linalg.det(M) - 1) < 1e-8
allok &= report(f"dim Der(O) = {dim_g2} (g2); dim{{Dj=0}} = {len(su3)} (su3); exp = automorphism fixing j; "
                "colour matrix special unitary", ok)

# ---- (4) tag circle = colour phase; psi restricted to the ZD locus = the CENTRE of colour SU(3)
def central(j, th):                                   # v -> cos(th) v + sin(th) j v on j-perp, fix j (basis-free)
    def fS(z):
        def fo(v):
            vj = (v @ j) * j; w = v - vj
            return vj + np.cos(th) * w + np.sin(th) * cd(j, w)
        return np.concatenate([fo(z[:8]), fo(z[8:])])
    return fS
def psi(z):
    t = np.zeros(16); t[0], t[8] = z[0], z[8]
    return t + cd(z - t, tagunit(2 * np.pi / 3))
j = rand_dir(); B = colour_basis(j); x = B[1][0]; z = zd_of(x, j)
c_p, c_m = central(j, 2 * np.pi / 3), central(j, -2 * np.pi / 3)
on_zd  = min(np.linalg.norm(psi(z) - c_p(z)), np.linalg.norm(psi(z) - c_m(z)))
off_zd = min(np.linalg.norm(psi(emb(j)) - c_p(emb(j))), np.linalg.norm(psi(emb(j)) - c_m(emb(j))))
th = rng.uniform(0, 2 * np.pi)
phase_dev = np.linalg.norm(cd(z, tagunit(th)) - zd_of(np.cos(th) * x - np.sin(th) * cd(j, x), j))
allok &= report(f"tag phase on a ZD = colour phase of x (dev {phase_dev:.1e}); psi = central colour Z3 ON the ZD "
                f"locus (dev {on_zd:.1e}) but NOT off it (dev {off_zd:.2f})",
                phase_dev < 1e-9 and on_zd < 1e-9 and off_zd > 0.5)

# ---- (5) products = the SU(3)-invariant pairings: colour x anti-colour -> CORE singlet; |zw|^2 = 4|h(x,u)|^2
ok = True
for _ in range(50):
    jj = rand_dir(); Bc = colour_basis(jj)
    cx = rng.normal(size=6); cx /= np.linalg.norm(cx); cu = rng.normal(size=6); cu /= np.linalg.norm(cu)
    x = sum(cx[2*a]*Bc[a][0] + cx[2*a+1]*Bc[a][1] for a in range(3))
    u = sum(cu[2*a]*Bc[a][0] + cu[2*a+1]*Bc[a][1] for a in range(3))
    z, w = zd_of(x, jj), antizd_of(u, jj)
    h = complex(x @ u, cd(jj, x) @ u)
    P = cd(z, w)
    Cc = np.column_stack([unit(0), emb(jj), unit(8), np.concatenate([np.zeros(8), jj])])
    ok &= np.linalg.norm(P - Cc @ (Cc.T @ P)) < 1e-9 and abs(nrm2(P) - 4 * abs(h) ** 2) < 1e-9
allok &= report("colour x anti-colour lands in the core <1, j, ell, j ell>; |zw|^2 = 4|h(x,u)|^2 (ZD <=> singlet = 0)", ok)

# ---- (6) the fibre of Moreno's Z = G2 -> S^6 is colour SU(3): su(3)_j maps ZD pairs over j to ZD pairs
#          over j consistently with the dictionary, and its orbit through a pair is the full 8-dim fibre
x1, U1 = Bstd[0][0], Bstd[1][0]
z1, w1 = zd_of(x1, j4), antizd_of(U1, j4)
assert np.linalg.norm(cd(z1, w1)) < 1e-9
fO = gexp(rng.normal(size=8))
fS = lambda zz: np.concatenate([fO(zz[:8]), fO(zz[8:])])
img_z, img_w = fS(z1), fS(w1)
ok = (np.linalg.norm(cd(img_z, img_w)) < 1e-9
      and np.allclose(img_z, zd_of(fO(x1), j4), atol=1e-9)
      and np.allclose(img_w, antizd_of(fO(U1), j4), atol=1e-9))
T = np.column_stack([np.concatenate([liftD(m)(z1[:8]), liftD(m)(z1[8:]), liftD(m)(w1[:8]), liftD(m)(w1[8:])]) for m in su3])
rk = np.linalg.matrix_rank(T, tol=1e-9)
allok &= report(f"su(3)_j closes on ZD pairs over j, matches the dictionary, and its orbit map has rank {rk} "
                "= dim of the fibre (14 - 6 = 8): the fibre of Z = G2 over S^6 is colour SU(3)", ok and rk == 8)

# ---- (7) ZDs are invertible elements with information-losing channels
z = zd_of(Bstd[2][0], j4); w = antizd_of(Bstd[0][0], j4)
assert np.linalg.norm(cd(z, w)) < 1e-9
zinv = -z / nrm2(z)
ok = (np.allclose(cd(z, z), -nrm2(z) * unit(0)) and np.allclose(cd(zinv, z), unit(0))
      and np.allclose(cd(z, zinv), unit(0)) and np.linalg.norm(cd(zinv, cd(z, w))) < 1e-9 and np.linalg.norm(w) > 1)
allok &= report("z^2 = -|z|^2: every ZD is invertible (two-sided), yet z^{-1}(zw) = 0 =/= w -- the loss sits in the channel, not the element", ok)

# ---- (8) the Gillard-Gresnigt blocks are the colour lines of the selected direction j = e4
ok = all(abs(abs(float(cd(j4, u8(i)) @ u8(i + 4))) - 1) < 1e-12 for i in (1, 2, 3))
def blk(i): return [i, i + 4, i + 8, i + 12]
coreidx = [0, 4, 8, 12]
def outside(P, idxs): return np.linalg.norm(P[[k for k in range(16) if k not in idxs]])
for i, jb, k in [(1, 2, 3), (2, 3, 1), (3, 1, 2)]:
    for _ in range(15):
        a = np.zeros(16); b = np.zeros(16); c = np.zeros(16)
        a[blk(i)] = rng.normal(size=4); b[blk(i)] = rng.normal(size=4); c[blk(jb)] = rng.normal(size=4)
        ok &= outside(cd(a, b), coreidx) < 1e-9 and outside(cd(a, c), blk(k)) < 1e-9
allok &= report("G-G blocks V_i = colour line i (x) tag (L_{e4} e_i ~ e_{i+4}); V_iV_i -> core (singlet channel), "
                "V_iV_j -> V_k (epsilon: 3x3 -> 3bar)", ok)

print("\nALL PASS" if allok else "\nSOME CHECKS FAILED"); sys.exit(0 if allok else 1)
