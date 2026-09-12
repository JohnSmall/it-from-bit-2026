"""
sedenion_zero_divisor_scan.py  (2026-08-31)
Explicit encodings for the zero-divisor structure of the sedenions S.
Cayley-Dickson convention A: (a,b)(c,d) = (ac - conj(d) b, d a + b conj(c)).
Index convention: e_i e_j = +/- e_{i XOR j}  (e_4 = octonion doubling unit, e_8 = tag).
PASS/FAIL printed per check.
"""
import numpy as np, itertools, sys
rng = np.random.default_rng(20260831)

def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def cd(a, b):
    n = len(a)
    if n == 1: return a * b
    h = n // 2
    p, q = a[:h], a[h:]; r, s = b[:h], b[h:]
    return np.concatenate([cd(p, r) - cd(conj(s), q), cd(s, p) + cd(q, conj(r))])
def unit(i, n=16):
    v = np.zeros(n); v[i] = 1.0; return v
def nrm2(x): return float(x @ x)
def assoc(x, y, z): return cd(cd(x, y), z) - cd(x, cd(y, z))
def imag_oct(): 
    v = rng.normal(size=8); v[0] = 0; return v
def emb(o):  # octonion -> sedenion, first half
    return np.concatenate([o, np.zeros(8)])
def embl(o): # octonion*ell -> second half
    return np.concatenate([np.zeros(8), o])
def left_mult_matrix(z):
    return np.column_stack([cd(z, unit(j)) for j in range(16)])
def report(name, ok):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    return ok

allok = True
print("Octonion table in this convention (e_i e_j = s e_k, i<j, both imaginary):")
lines = set()
for i in range(1, 8):
    for j in range(i + 1, 8):
        p = cd(unit(i, 8), unit(j, 8)); k = int(np.argmax(np.abs(p)))
        lines.add(frozenset((i, j, k)))
print("  Fano lines:", sorted(sorted(l) for l in lines))

# ---- (1) norm-defect identity  |(a,b)(c,d)|^2 - |(a,b)|^2|(c,d)|^2 = 2 <a,[c,b,d]>
err = 0.0
for _ in range(200):
    a, b, c, d = (rng.normal(size=8) for _ in range(4))
    A = np.concatenate([a, b]); B = np.concatenate([c, d])
    lhs = nrm2(cd(A, B)) - nrm2(A) * nrm2(B)
    rhs = 2 * float(a @ assoc(c, b, d))
    err = max(err, abs(lhs - rhs))
allok &= report(f"norm-defect identity, max |lhs-rhs| = {err:.2e}", err < 1e-9)

# ---- (2) zero divisors: z = x + y ell, x,y imaginary orthonormal  ->  kernel dim 4 exactly
dims = set(); dims_bad = set()
for _ in range(50):
    x = imag_oct(); x /= np.linalg.norm(x)
    y = imag_oct(); y -= (y @ x) * x; y /= np.linalg.norm(y)
    z = np.concatenate([x, y])
    dims.add(16 - np.linalg.matrix_rank(left_mult_matrix(z), tol=1e-9))
    w = np.concatenate([x, 0.7 * y + 0.3 * x])      # not orthonormal
    dims_bad.add(16 - np.linalg.matrix_rank(left_mult_matrix(w), tol=1e-9))
allok &= report(f"orthonormal imaginary pair -> ker L_z dims {dims}; non-orthonormal -> {dims_bad}",
                dims == {4} and dims_bad == {0})

# ---- (3) annihilator structure: Ann(x + y ell) = { u + (u j) ell : u in H_{x,y}^perp }, j = x y
def ann_check():
    x = imag_oct(); x /= np.linalg.norm(x)
    y = imag_oct(); y -= (y @ x) * x; y /= np.linalg.norm(y)
    j = cd(x, y)
    z = np.concatenate([x, y])
    M = left_mult_matrix(z)
    # basis of H^perp: imaginary, orthogonal to x, y, j
    Q, _ = np.linalg.qr(np.column_stack([unit(0, 8), x, y, j]))
    P = np.eye(8) - Q @ Q.T
    U = np.linalg.svd(P)[0][:, :4]                 # 4 orthonormal vectors spanning H^perp
    res = 0.0; dirs = []
    for k in range(4):
        u = U[:, k]; v = cd(u, j)
        w = np.concatenate([u, v]); res = max(res, np.linalg.norm(M @ w))
        dirs.append(float(cd(u, v) @ j))          # direction of the annihilator vs j
    return res, dirs
res, dirs = ann_check()
allok &= report(f"Ann(z) = {{u + (uj)ell}}: max |z w| = {res:.2e}; annihilator direction (uv).j = {np.round(dirs,6)}",
                res < 1e-9 and np.allclose(dirs, -1))

# ---- (4) coassociativity: the 3-form phi vanishes on the 4-plane <a,b,c,d> of a zero-divisor pair
def phi(x, y, z): return float(cd(x, y) @ z)      # phi(x,y,z) = <xy, z> on imaginaries
x = imag_oct(); x /= np.linalg.norm(x)
y = imag_oct(); y -= (y @ x) * x; y /= np.linalg.norm(y)
j = cd(x, y); u = imag_oct(); 
for vv in (x, y, j): u -= (u @ vv) * vv
u /= np.linalg.norm(u); v = cd(u, j)
comps = [x, y, u, v]
assert np.linalg.norm(cd(np.concatenate([x, y]), np.concatenate([u, v]))) < 1e-9
phimax = max(abs(phi(*t)) for t in itertools.combinations(comps, 3))
allok &= report(f"phi restricted to span(a,b,c,d) of a ZD pair vanishes: max|phi| = {phimax:.2e}", phimax < 1e-9)

# ---- (5) PG(3,2) census: 35 lines, 15 planes; planes octonion vs quasi-octonion
pts = list(range(1, 16))
lines_pg = sorted({frozenset((i, j, i ^ j)) for i in pts for j in pts if i != j})
planes = sorted({frozenset({i, j, k, i ^ j, i ^ k, j ^ k, i ^ j ^ k})
                 for i, j, k in itertools.combinations(pts, 3) if i ^ j != k}, key=sorted)
def plane_is_division(pl):
    idx = [0] + sorted(pl)
    for _ in range(40):
        a = np.zeros(16); b = np.zeros(16)
        a[idx] = rng.normal(size=8); b[idx] = rng.normal(size=8)
        if abs(nrm2(cd(a, b)) - nrm2(a) * nrm2(b)) > 1e-9: return False
    return True
div = {pl: plane_is_division(pl) for pl in planes}
n_oct = sum(div.values()); n_quasi = len(planes) - n_oct
allok &= report(f"{len(lines_pg)} lines, {len(planes)} planes: {n_oct} octonion + {n_quasi} quasi-octonion",
                len(lines_pg) == 35 and len(planes) == 15 and n_oct == 8 and n_quasi == 7)
census = {}
for L in lines_pg:
    through = [pl for pl in planes if L <= pl]
    typ = (sum(div[pl] for pl in through), sum(not div[pl] for pl in through))
    kind = "through tag e8" if 8 in L else ("inside O" if max(L) < 8 else "mixed")
    census.setdefault((kind, typ), 0); census[(kind, typ)] += 1
for k in sorted(census): print(f"   lines {k[0]:<15} -> (octonion, quasi) planes through = {k[1]} : {census[k]} lines")
allok &= report("census: 7 tag lines (3,0); 7 register lines (2,1); 21 mixed lines (1,2)",
                census == {("through tag e8", (3, 0)): 7, ("inside O", (2, 1)): 7, ("mixed", (1, 2)): 21})

# ---- (6) the generation automorphism psi = 1 on the tag plane <1,e8>, right-multiplication by
#          omega = exp(2 pi e8/3) on its 14-dim complement Im(O) (+) Im(O) ell.  Automorphism iff omega^3 = 1.
def psi_lam(lam):
    def f(z):
        t = np.zeros(16); t[0], t[8] = z[0], z[8]
        return t + cd(z - t, lam)
    return f
def is_aut(f, trials=60):
    for _ in range(trials):
        a = rng.normal(size=16); b = rng.normal(size=16)
        if np.linalg.norm(f(cd(a, b)) - cd(f(a), f(b))) > 1e-9: return False
    return True
omega = np.zeros(16); omega[0] = -0.5; omega[8] = np.sqrt(3) / 2
lam45 = np.zeros(16); lam45[0] = np.cos(np.pi / 4); lam45[8] = np.sin(np.pi / 4)
psi = psi_lam(omega); tau = lambda z: np.concatenate([z[:8], -z[8:]])
allok &= report("psi = 1 (+) R_omega is an automorphism; the same with exp(i pi/4) is not; tau is",
                is_aut(psi) and not is_aut(psi_lam(lam45)) and is_aut(tau))
fixdim = 16 - np.linalg.matrix_rank(np.column_stack([psi(unit(k)) - unit(k) for k in range(16)]), tol=1e-9)
allok &= report(f"Fix(psi) has dimension {fixdim} (= span{{1, e8}}); psi^3 = 1: "
                f"{np.linalg.norm(psi(psi(psi(z:=rng.normal(size=16)))) - z) < 1e-9}", fixdim == 2)
allok &= report("tau psi tau = psi^{-1}  (<psi, tau> = S3)",
                np.linalg.norm(tau(psi(tau(z))) - psi_lam(conj(omega))(z)) < 1e-9)
# psi commutes with the diagonal G2: check against the automorphism of O induced by the Fano-line
# rotation e1->e2->e3->e1 extended by e4 fixed, i.e. the order-3 element of Aut(H_{123}) lifted to O and to S
perm = {1: 2, 2: 3, 3: 1, 4: 4, 5: 6, 6: 7, 7: 5}   # e5=e1e4 -> e2e4=e6 -> e3e4=e7 -> e5
def g_diag(z):
    out = np.zeros(16)
    for i in range(16):
        base, tag = i & 7, i & 8
        out[(perm[base] if base else 0) | tag] += z[i]
    return out
# fix signs by construction: verify g is an automorphism first
allok &= report("g = diagonal lift of the Fano rotation (e1 e2 e3) is an automorphism of S", is_aut(g_diag))
allok &= report("psi commutes with g (direct product G2 x S3 witnessed on one non-trivial g)",
                np.linalg.norm(psi(g_diag(z)) - g_diag(psi(z))) < 1e-9)
# ---- (7) ZD locus is invariant under the whole tag circle U(1)_ell, halvings O.omega^k are ZD-free
zd_inv = True
for _ in range(30):
    x = imag_oct(); x /= np.linalg.norm(x)
    y = imag_oct(); y -= (y @ x) * x; y /= np.linalg.norm(y)
    z = np.concatenate([x, y]); lam = np.zeros(16); th = rng.uniform(0, 2*np.pi)
    lam[0], lam[8] = np.cos(th), np.sin(th)
    zd_inv &= (16 - np.linalg.matrix_rank(left_mult_matrix(psi_lam(lam)(z)), tol=1e-9)) == 4
halv_free = all((16 - np.linalg.matrix_rank(left_mult_matrix(psi_lam(lam)(emb(rng.normal(size=8)))), tol=1e-9)) == 0
                for lam in (unit(0), omega, cd(omega, omega)))
allok &= report("ZD locus invariant under all of U(1)_ell; the three halvings O, O.omega, O.omega^2 contain no ZDs",
                zd_inv and halv_free)

print("\nALL PASS" if allok else "\nSOME CHECKS FAILED"); sys.exit(0 if allok else 1)
