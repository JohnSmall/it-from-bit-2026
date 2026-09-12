# Constructor check, 2026-08-12: octonion subalgebras of S through the core H.
# Convention (corpus, app:setup): (a,b)(c,d) = (ac - conj(d)b, da + b conj(c));
# conj(e_i) = e_i if i==0 else -e_i. Exact integer arithmetic throughout.
from fractions import Fraction
from itertools import product
import random
random.seed(20260812)

def mul_unit(a, b, n):
    """Product e_a * e_b at Cayley-Dickson level n (dim 2^n). Returns (sign, index)."""
    if n == 0:
        return (1, 0)
    h = 1 << (n - 1)
    ah, al = divmod(a, h); bh, bl = divmod(b, h)
    if ah == 0 and bh == 0:                      # (p,0)(r,0) = (pr,0)
        s, i = mul_unit(al, bl, n - 1); return (s, i)
    if ah == 0 and bh == 1:                      # (p,0)(0,t) = (0, t p)
        s, i = mul_unit(bl, al, n - 1); return (s, i + h)
    if ah == 1 and bh == 0:                      # (0,q)(r,0) = (0, q conj(r))
        s, i = mul_unit(al, bl, n - 1)
        if bl != 0: s = -s
        return (s, i + h)
    s, i = mul_unit(bl, al, n - 1)               # (0,q)(0,t) = (-conj(t) q, 0)
    s = -s
    if bl != 0: s = -s
    return (s, i)

N = 4; DIM = 16
TAB = [[mul_unit(a, b, N) for b in range(DIM)] for a in range(DIM)]

def mul_vec(x, y):
    z = [Fraction(0)] * DIM
    for a in range(DIM):
        if x[a] == 0: continue
        for b in range(DIM):
            if y[b] == 0: continue
            s, i = TAB[a][b]
            z[i] += s * x[a] * y[b]
    return z

def basis_vec(i, c=1):
    v = [Fraction(0)] * DIM; v[i] = Fraction(c); return v

def norm2(x): return sum(c * c for c in x)

def rank_and_basis(vecs):
    """Exact row reduction over Q; returns basis rows."""
    rows = [list(v) for v in vecs]; basis = []; piv = []
    for r in rows:
        r = r[:]
        for b, p in zip(basis, piv):
            if r[p] != 0:
                f = r[p] / b[p]
                r = [ri - f * bi for ri, bi in zip(r, b)]
        nz = [j for j, c in enumerate(r) if c != 0]
        if nz:
            basis.append(r); piv.append(nz[0])
    return basis

def subalgebra_closure(gens, cap=DIM):
    basis = rank_and_basis(gens)
    while True:
        new = list(basis)
        for x in basis:
            for y in basis:
                new.append(mul_vec(x, y))
        nb = rank_and_basis(new)
        if len(nb) == len(basis) or len(nb) >= cap:
            return nb
        basis = nb

def comp_check(basis, trials=400):
    """Exact N(xy) == N(x)N(y) on random integer combinations; also det-nonzero probes."""
    d = len(basis)
    for _ in range(trials):
        cx = [random.randint(-3, 3) for _ in range(d)]
        cy = [random.randint(-3, 3) for _ in range(d)]
        x = [sum(Fraction(cx[k]) * basis[k][j] for k in range(d)) for j in range(DIM)]
        y = [sum(Fraction(cy[k]) * basis[k][j] for k in range(d)) for j in range(DIM)]
        if norm2(mul_vec(x, y)) != norm2(x) * norm2(y):
            return False
    return True

# PASS 1: reproduce eq:fano-lines exactly (all positive cyclic).
fano = [(1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5)]
ok = all(mul_unit(i,j,3) == (1,k) for (i,j,k) in fano)
print("PASS 1 (Fano lines, corpus orientation):", "PASS" if ok else "FAIL")

# PASS 2: Klein grading table V_iV_i in H, V_iV_j in V_k.
sector = lambda a: a % 4
ok = True
for a in range(1, DIM):
    for b in range(1, DIM):
        s, i = TAB[a][b]
        if sector(i) != (sector(a) ^ sector(b)): ok = False
print("PASS 2 (Klein grading, all 256 products):", "PASS" if ok else "FAIL")

H = [basis_vec(i) for i in (0, 4, 8, 12)]

# PASS 3: exactly three unit-spanned 8-dim subalgebras contain H; test which of the
# 15 hyperplane subalgebras of F_2^4 are composition (octonion) algebras.
print("PASS 3 (hyperplane scan): phi-mask : contains H : closure dim : composition")
count_through_H = 0
for mask in range(1, 16):
    idxs = [a for a in range(16) if bin(a & mask).count("1") % 2 == 0]
    contains_H = all(i in idxs for i in (0, 4, 8, 12))
    B = subalgebra_closure([basis_vec(i) for i in idxs])
    comp = comp_check(B, trials=150)
    if contains_H: count_through_H += 1
    print(f"  mask {mask:2d} : {str(contains_H):5s} : dim {len(B):2d} : {comp}")
print("  unit-spanned 8-dim subalgebras containing H:", count_through_H, "(expect 3)")

# TEST A: DIAGONAL core-doubling, same tag, cross-sector: w = e1 + e2.
for label, w in [("A1: w = e1+e2 (same-tag, cross-sector)", [ (1,1), (2,1) ]),
                 ("A2: w = 3e1+4e2 (asymmetric mix)",        [ (1,3), (2,4) ]),
                 ("A3: w = e1+e2+e3 (all three sectors)",    [ (1,1), (2,1), (3,1) ]),
                 ("B : w = e1+e10 (tag-flipped, ZD-shaped)", [ (1,1), (10,1) ]),
                 ("C : w = e1+e6+e11 (mixed tags/sectors)",  [ (1,1), (6,1), (11,1) ])]:
    wv = [Fraction(0)] * DIM
    for i, c in w: wv[i] = Fraction(c)
    B = subalgebra_closure(H + [wv])
    line = f"TEST {label}: closure dim {len(B)}"
    if len(B) == 8:
        line += f" ; composition (400 exact samples): {comp_check(B)}"
    print(line)

# SECOND BATTERY (2026-08-12): map the family. Analytic reading under test:
# D_w = H + Hw is an octonion copy iff w lies in the J-complex 3-space
# C^3 = span{e1,e5, e2,e6, e3,e7} of the ell = e4 computability split of O_CD,
# extended H-coherently (single H-multiplier per line). Then D_w depends only on
# the complex line [w] in CP^2; O_1, O_2, O_3 are the coordinate points; the
# Stab(e4) SU(3) inside the diagonal G2 sweeps the family.
def D_of(wspec):
    wv = [Fraction(0)] * DIM
    for i, c in wspec: wv[i] = Fraction(c)
    return subalgebra_closure(H + [wv])

def same_span(B1, B2):
    return len(rank_and_basis(B1 + B2)) == len(B1) == len(B2)

tests = [
 ("e5+e6      (= e4-multiple of e1+e2; predict 8, same D as A1)", [(5,1),(6,1)]),
 ("e9+e10     (= e8-multiple of e1+e2; predict 8, same D as A1)", [(9,1),(10,1)]),
 ("e13+e14    (= e12-multiple;        predict 8, same D as A1)", [(13,1),(14,1)]),
 ("e1+e6      (point of C^3, mixed planes; predict 8)",          [(1,1),(6,1)]),
 ("e1+e5+e2   (point of C^3, J-phase on line 1; predict 8)",     [(1,1),(5,1),(2,1)]),
 ("e1+e2+e13  (incoherent H-multipliers; predict 16)",           [(1,1),(2,1),(13,1)]),
 ("e1+2e6+3e3 (generic C^3 point; predict 8)",                   [(1,1),(6,2),(3,3)]),
]
DA1 = D_of([(1,1),(2,1)])
print("SECOND BATTERY (family map; D_A1 = closure of H,{e1+e2}):")
for label, spec in tests:
    B = D_of(spec)
    line = f"  {label}: dim {len(B)}"
    if len(B) == 8:
        line += f" ; composition: {comp_check(B, 300)} ; equals D_A1: {same_span(B, DA1)}"
    print(line)

# Coordinate points really are the graded copies:
O1 = subalgebra_closure([basis_vec(i) for i in (0,4,8,12,1,5,9,13)])
print("  [w]=[e1] gives O1:", same_span(D_of([(1,1)]), O1))
# Distinct lines give distinct copies (O1 vs D_A1 vs democratic):
Dd = D_of([(1,1),(2,1),(3,1)])
print("  D_A1 distinct from O1:", not same_span(DA1, O1),
      "; democratic distinct from both:", (not same_span(Dd, O1)) and (not same_span(Dd, DA1)))
