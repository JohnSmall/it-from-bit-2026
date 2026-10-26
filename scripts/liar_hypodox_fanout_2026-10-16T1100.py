#!/usr/bin/env python3
"""liar_hypodox_fanout_2026-10-16T1100.py

JS, 2026-10-16: think about logical paradoxes ("the set of all sets that are
not members of themselves", "this statement is false"), hypodoxes ("this
statement is true"), and pre-FANOUT / post-FANOUT states.

A self-referential sentence "S has the value g(S)" is a fixed-point equation
v = g(v) on the value space.  Lawvere's theorem says a self-representing
object forces every endomap g to have a fixed point; the diagonal it uses
is the copy map, which in the paper is FANOUT (appendix app:fanout-boundary).
This script checks the finite parts of the reading that follows:

  A. Classical values {0,1}: the four endomaps.  Constants are grounded
     (one fixed point), the identity is the truth-teller / hypodox (two
     fixed points, underdetermined), NOT is the Liar / paradox (none,
     overdetermined).  Kleene's third value 1/2 (Kripke's minimal fixed
     point) gives both ungrounded sentences the value 1/2; the extra fixed
     points above it are {0,1} for the truth-teller and none for the Liar.
  B. Qubit, record basis Z.  The Liar operator X and the hypodox operator 1.
     Fixed rays of X: |+>, |-> (eigenvalues +1, -1); both are maximal
     Z-superpositions, not Z-copyable, but X-copyable: the Liar's consistent
     state is a record in the complementary classical structure, where the
     Liar operator acts as a (signed) truth-teller.  X anticommutes with Z;
     1 commutes with everything.  The Liar's sign is the -1 eigenvalue, a
     sign on an amplitude: the Kirkwood--Dirac distribution of |-> in (Z,X)
     and its Wootters Wigner function are non-negative in every convention.
  C. Which self-referential endomaps force negativity.  For a rotation about
     Bloch axis n the fixed rays are +-n.  The minimum of the Wootters Wigner
     function of the fixed state over the eight sign conventions is
     (1 - |n|_1)/4, negative iff n is not a Pauli axis: the Liar (axis x) and
     the phase-hypodox (axis z) fix stabiliser states, inside the toy-theory
     octahedron; the order-3 Clifford element (axis (1,1,1)/sqrt3) and a
     generic axis fix magic states outside it.
  D. Liar cycles.  The 4-cycle with an odd number of negations has no global
     assignment, the even one has two.  The PR box (the odd cycle with
     probability one on each edge) has no non-negative global section, each
     deterministic assignment satisfying at most three of its four edges, but
     has a signed one (Abramsky--Brandenburger).
  E. No natural diagonal.  The space of linear Delta: C^2 -> C^2 (x) C^2
     with Delta U = (U (x) U) Delta for all U in U(2) is {0}; the copy map
     of a basis is natural for the permutation of that basis and not for a
     phase gate, nor for the scalar -1 (prop:f1-dictionary's fibre).
  F. Composition.  The group generated mod phases by the Liar X, its signed
     truth-teller Z and the involution H that exchanges their structures has
     8 elements (the rebit's Clifford group) and no element of order 3.  The
     Paulis fix stabiliser states; the two Hadamard-type involutions fix the
     H-type magic states, |n|_1 = sqrt2, Wigner minimum (1 - sqrt2)/4: the
     fixed points of the exchange of record and Liar structures are the
     first states outside the toy theory.  The quarter-turns HX, XH have no
     real fixed ray but fix |y+-> over C, the third classical structure.
     The square roots S = sqrt Z and sqrt X = HSH (half a hypodox, half a
     Liar) compose to an element of order 3 whose fixed states are the
     T-type magic states, |n|_1 = sqrt3.  With S the group is the full
     Clifford group, 24 elements, 8 of order 3, each fixing only magic
     states.
Seed 20261016; numpy only.
"""
import itertools

import numpy as np

rng = np.random.default_rng(20261016)
np.set_printoptions(precision=4, suppress=True)

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
ok = True


def check(cond, msg):
    global ok
    ok = ok and bool(cond)
    print(("   ok  " if cond else "   FAIL") + " " + msg)


print("Liar, hypodox and FANOUT")
print("=" * 70)

# ---------------------------------------------------------------- A
print("A. classical endomaps of {0,1} and their fixed points")
maps = {"const 0": lambda v: 0, "const 1": lambda v: 1,
        "id  (truth-teller)": lambda v: v, "NOT (Liar)": lambda v: 1 - v}
fp2 = {}
for name, g in maps.items():
    fp2[name] = [v for v in (0, 1) if g(v) == v]
    print("   %-20s fixed points on {0,1}: %s" % (name, fp2[name]))
check(fp2["id  (truth-teller)"] == [0, 1] and fp2["NOT (Liar)"] == [],
      "truth-teller has two fixed points (underdetermined), Liar none (overdetermined)")
# Kleene: values {0, 1/2, 1}, NOT v = 1 - v, id v = v
for name, g in [("id  (truth-teller)", lambda v: v), ("NOT (Liar)", lambda v: 1 - v)]:
    fp3 = [v for v in (0, 0.5, 1) if g(v) == v]
    print("   %-20s fixed points on {0,1/2,1}: %s" % (name, fp3))
check(0.5 in [v for v in (0, 0.5, 1) if 1 - v == v], "Liar's only Kleene fixed point is 1/2 (ungrounded, no classical value)")

# ---------------------------------------------------------------- B
print("B. qubit with record basis Z; Liar operator X, hypodox operator 1")
w, v = np.linalg.eigh(X)
plus = v[:, 1] if w[1] > 0 else v[:, 0]
minus = v[:, 0] if w[0] < 0 else v[:, 1]
plus = plus / plus[0]; plus /= np.linalg.norm(plus)
minus = minus / minus[0]; minus /= np.linalg.norm(minus)
print("   eigenvalues of X: %s; |+> = %s, |-> = %s" % (np.round(w, 6), np.round(plus, 4), np.round(minus, 4)))
pz = lambda s: np.abs(s) ** 2
print("   Z-probabilities of |+>, |->: %s, %s" % (pz(plus), pz(minus)))
check(np.allclose(pz(plus), 0.5) and np.allclose(pz(minus), 0.5), "both Liar fixed rays are the value 1/2 in Z (part A's fixed point)")


def copy_map(basis):
    """delta|b_i> = |b_i>|b_i> for the orthonormal columns of basis."""
    d = np.zeros((4, 2), dtype=complex)
    for i in range(2):
        b = basis[:, i]
        d += np.outer(np.kron(b, b), b.conj())
    return d


dZ = copy_map(I2)
dX = copy_map(np.column_stack([plus, minus]))
resZ = [np.linalg.norm(dZ @ s - np.kron(s, s)) for s in (plus, minus)]
resX = [np.linalg.norm(dX @ s - np.kron(s, s)) for s in (plus, minus)]
print("   Z-copy residual of |+>, |->: %.3f, %.3f ; X-copy residual: %.1e, %.1e" % (resZ[0], resZ[1], resX[0], resX[1]))
check(min(resZ) > 0.5 and max(resX) < 1e-12, "Liar fixed rays are not Z-copyable but are X-copyable (records in the complementary structure)")
print("   <+|X|+> = %+.0f, <-|X|-> = %+.0f : the Liar acts on its own fixed records as a signed truth-teller" % ((plus.conj() @ X @ plus).real, (minus.conj() @ X @ minus).real))
check(np.allclose(X @ Z + Z @ X, 0) and np.allclose(I2 @ Z - Z @ I2, 0), "Liar anticommutes with the record (XZ = -ZX); hypodox commutes")
# Kirkwood--Dirac in (Z, X) for |->
KD = np.array([[(I2[:, z].conj() @ xb) * (xb.conj() @ minus) * (minus.conj() @ I2[:, z]) for xb in (plus, minus)] for z in range(2)])
print("   Kirkwood--Dirac of |-> in (Z,X):\n      %s" % str(KD.real).replace("\n", "\n      "))
check(np.all(KD.real >= -1e-12) and np.allclose(KD.imag, 0), "KD distribution of the Liar's fixed state is non-negative")


def wigner_min(bloch):
    """Minimum over the eight Wootters sign conventions of the qubit Wigner function
    W(q,p) = (1 + s_z z + s_x x + s_y y)/4, the convention fixing which sign triples occur."""
    x, y, z = bloch
    vals = [(1 + sz * z + sx * x + sy * y) / 4 for sz in (1, -1) for sx in (1, -1) for sy in (1, -1)]
    return min(vals)


bloch = lambda s: np.array([(s.conj() @ P @ s).real for P in (X, Y, Z)])
print("   Wootters Wigner minimum over conventions, |->: %.4f ; |+>: %.4f" % (wigner_min(bloch(minus)), wigner_min(bloch(plus))))
check(wigner_min(bloch(minus)) >= -1e-12, "Liar fixed state has no Wigner negativity in any convention: the -1 is a sign on an amplitude, not a signed probability")

# ---------------------------------------------------------------- C
print("C. which self-referential endomaps force negativity: rotation about axis n")


def rot(n, theta):
    n = np.asarray(n, float); n = n / np.linalg.norm(n)
    return np.cos(theta / 2) * I2 - 1j * np.sin(theta / 2) * (n[0] * X + n[1] * Y + n[2] * Z)


def fixed_rays(U):
    w, v = np.linalg.eig(U)
    return [v[:, k] / np.linalg.norm(v[:, k]) for k in range(2)]


cases = [("Liar  X            axis x", (1, 0, 0), np.pi),
         ("phase hypodox      axis z", (0, 0, 1), np.pi / 4),
         ("order-3 Clifford   axis (1,1,1)", (1, 1, 1), 2 * np.pi / 3),
         ("generic            axis random", rng.normal(size=3), 1.0)]
mins = {}
for name, n, th in cases:
    U = rot(n, th)
    fr = fixed_rays(U)
    b = [bloch(s) for s in fr]
    l1 = [np.abs(bb).sum() for bb in b]
    wm = [wigner_min(bb) for bb in b]
    mins[name] = min(wm)
    print("   %-32s fixed Bloch vectors %s, %s ; |n|_1 = %.3f ; min Wigner = %+.4f, %+.4f"
          % (name, np.round(b[0], 3), np.round(b[1], 3), l1[0], wm[0], wm[1]))
check(mins["Liar  X            axis x"] >= -1e-12 and mins["phase hypodox      axis z"] >= -1e-12,
      "Liar and phase-hypodox fixed states are stabiliser states (inside the octahedron)")
check(mins["order-3 Clifford   axis (1,1,1)"] < -0.1 and mins["generic            axis random"] < 0,
      "order-3 Clifford and generic self-reference fix magic states (outside it, Wigner-negative)")
# the identity: minimum over conventions is (1-|n|_1)/4 exactly
ns = rng.normal(size=(200, 3)); ns /= np.linalg.norm(ns, axis=1)[:, None]
err = max(abs(wigner_min(n) - (1 - np.abs(n).sum()) / 4) for n in ns)
check(err < 1e-12, "min_conventions W(fixed state) = (1 - |n|_1)/4 for 200 random axes: negative iff n is off the three record axes")
# order-3 Clifford: check it cycles X -> Y -> Z -> X
C3 = rot((1, 1, 1), 2 * np.pi / 3)
cyc = np.allclose(C3 @ X @ C3.conj().T, Y) and np.allclose(C3 @ Y @ C3.conj().T, Z) and np.allclose(C3 @ Z @ C3.conj().T, X)
check(cyc, "the axis-(1,1,1) rotation by 2pi/3 cycles the three classical structures X -> Y -> Z -> X: a three-valued Liar")

# ---------------------------------------------------------------- D
print("D. Liar cycles and the PR box")


def global_sections(negs):
    """x_{k+1} = x_k xor negs[k] around a 4-cycle; count consistent assignments."""
    return [x for x in itertools.product((0, 1), repeat=4)
            if all(x[(k + 1) % 4] == (x[k] ^ negs[k]) for k in range(4))]


odd = global_sections([0, 0, 0, 1]); even = global_sections([0, 0, 1, 1])
print("   4-cycle, one negation (Liar cycle): %d global assignments; two negations (hypodox cycle): %d -> %s" % (len(odd), len(even), even))
check(len(odd) == 0 and len(even) == 2, "odd cycle is a paradox (0 sections), even cycle a hypodox (2 sections)")
# PR box: contexts (a_i, b_j), i,j in {0,1}; outcome pair (a,b) with a xor b = i*j, prob 1/2 each
contexts = [(0, 0), (0, 1), (1, 0), (1, 1)]
assign = list(itertools.product((0, 1), repeat=4))  # (a0, a1, b0, b1)
best = 0
for g in assign:
    sat = sum(1 for (i, j) in contexts if (g[i] ^ g[2 + j]) == (i & j))
    best = max(best, sat)
print("   PR box: a deterministic global assignment satisfies at most %d of the 4 edges" % best)
check(best == 3, "no non-negative global section: the PR box satisfies all 4 with probability one")
# signed global section: solve M w = p
rows, rhs = [], []
for (i, j) in contexts:
    for (a, b) in itertools.product((0, 1), repeat=2):
        rows.append([1.0 if (g[i] == a and g[2 + j] == b) else 0.0 for g in assign])
        rhs.append(0.5 if (a ^ b) == (i & j) else 0.0)
M = np.array(rows); p = np.array(rhs)
wgt, *_ = np.linalg.lstsq(M, p, rcond=None)
res = np.linalg.norm(M @ wgt - p)
print("   signed global section (least-norm): residual %.1e, min weight %+.4f, max weight %+.4f, sum %.4f" % (res, wgt.min(), wgt.max(), wgt.sum()))
check(res < 1e-12 and wgt.min() < -1e-6, "a signed global section exists and is genuinely signed (Abramsky--Brandenburger)")

# ---------------------------------------------------------------- E
print("E. no natural diagonal on C^2")


def haar_u2():
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    Q, R = np.linalg.qr(A)
    return Q * (np.diag(R) / np.abs(np.diag(R)))


# unknown Delta is 4x2 complex; constraint Delta U - (U x U) Delta = 0 is linear in vec(Delta)
rows = []
for _ in range(8):
    U = haar_u2()
    # vec: Delta U -> (U^T x I_4) vec(Delta); (UxU) Delta -> (I_2 x (UxU)) vec(Delta)  [column-major]
    L = np.kron(U.T, np.eye(4)) - np.kron(np.eye(2), np.kron(U, U))
    rows.append(L)
Lall = np.vstack(rows)
sv = np.linalg.svd(Lall, compute_uv=False)
null_dim = int(np.sum(sv < 1e-10))
print("   dim of {Delta : Delta U = (U x U) Delta for 8 Haar U}: %d (smallest singular value %.2e)" % (null_dim, sv.min()))
check(null_dim == 0, "no linear map C^2 -> C^2 x C^2 is natural under U(2): no diagonal, so no diagonal argument, pre-FANOUT")
nat = lambda D, U: np.linalg.norm(D @ U - np.kron(U, U) @ D)
Pphase = np.diag([1, np.exp(1j * 0.7)])
print("   copy map of Z: naturality residual under the basis swap X: %.1e ; under a phase gate: %.3f ; under the scalar -1: %.3f"
      % (nat(dZ, X), nat(dZ, Pphase), nat(dZ, -I2)))
check(nat(dZ, X) < 1e-12 and nat(dZ, Pphase) > 0.1 and nat(dZ, -I2) > 1,
      "the record's copy map is natural for its own permutations only; phases and the scalar -1 break it (the fibre)")

# ---------------------------------------------------------------- F
print("F. composition: what the Liar, the hypodox and their square roots generate")
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S = np.diag([1, 1j]).astype(complex)
sqrtX = H @ S @ H


def canon(U):
    """projective canonical form: first entry of largest modulus made real positive."""
    k = np.argmax(np.abs(U.ravel()) > 1e-9)
    ph = U.ravel()[k] / abs(U.ravel()[k])
    return np.round(U / ph, 8)


def closure(gens):
    elems = [canon(I2)]
    frontier = [canon(I2)]
    while frontier:
        new = []
        for A in frontier:
            for G in gens:
                B = canon(G @ A)
                if not any(np.allclose(B, E) for E in elems):
                    elems.append(B); new.append(B)
        frontier = new
    return elems


def proj_order(U):
    P = I2.copy()
    for k in range(1, 13):
        P = U @ P
        if np.allclose(canon(P), canon(I2)):
            return k
    return 0


def fixed_l1(U):
    return [np.abs(bloch(s)).sum() for s in fixed_rays(U)]


rebit = closure([X, Z, H])
orders = sorted(proj_order(U) for U in rebit)
print("   <X, Z, H> mod phases: %d elements, orders %s" % (len(rebit), sorted(set(orders))))
check(len(rebit) == 8 and 3 not in orders, "Liar + signed truth-teller + their exchange: 8 elements (the rebit's Clifford group), none of order 3")
by_type = {}
for U in rebit:
    o = proj_order(U)
    l1 = round(max(fixed_l1(U)), 6)
    by_type.setdefault((o, l1), 0)
    by_type[(o, l1)] += 1
for (o, l1), cnt in sorted(by_type.items()):
    print("      %d element(s) of order %d with fixed-state |n|_1 = %.6f (Wigner minimum %+.4f)" % (cnt, o, l1, (1 - l1) / 4))
check(by_type.get((2, 1.0), 0) == 3 and by_type.get((2, round(np.sqrt(2), 6)), 0) == 2 and by_type.get((4, 1.0), 0) == 2,
      "Paulis fix stabiliser states; the two Hadamard-type involutions fix H-type magic states (|n|_1 = sqrt2, negative); quarter-turns fix stabiliser states")
hfix = [np.round(bloch(s), 3) for s in fixed_rays(H)]
print("   Fix(H) = %s, %s : the fixed points of the exchange of record and Liar structures are magic" % (hfix[0], hfix[1]))
HX = H @ X
wr, vr = np.linalg.eig(HX.real)
real_fixed = [k for k in range(2) if abs(wr[k].imag) < 1e-12]
fy = [np.round(bloch(s), 3) for s in fixed_rays(HX)]
print("   quarter-turn HX: real eigenvalues %s -> no real fixed ray; complex fixed Bloch vectors %s, %s" % (np.round(wr, 3), fy[0], fy[1]))
check(len(real_fixed) == 0 and all(abs(abs(f[1]) - 1) < 1e-9 for f in fy),
      "the quarter-turn has no fixed ray over R and fixes the y-records over C: the third classical structure")
C = S @ sqrtX
o3 = proj_order(C)
l1c = fixed_l1(C)
print("   S sqrtX = sqrtZ sqrtX: projective order %d, fixed-state |n|_1 = %.4f, %.4f, min Wigner %+.4f" % (o3, l1c[0], l1c[1], min(wigner_min(bloch(s)) for s in fixed_rays(C))))
check(o3 == 3 and min(l1c) > 1.7, "half a hypodox composed with half a Liar is the three-cycle; its fixed states are magic (|n|_1 = sqrt3)")
cliff = closure([X, Z, H, S])
ord3 = [U for U in cliff if proj_order(U) == 3]
l1_ord3 = min(min(fixed_l1(U)) for U in ord3) if ord3 else 0
print("   <X, Z, H, S> mod phases: %d elements, %d of order 3, min |n|_1 over their fixed states %.4f" % (len(cliff), len(ord3), l1_ord3))
check(len(cliff) == 24 and len(ord3) == 8 and l1_ord3 > 1.7, "the full Clifford group: every order-3 element fixes only magic states")

print("=" * 70)
print("LIAR HYPODOX FANOUT: %s" % ("PASS" if ok else "FAIL"))
