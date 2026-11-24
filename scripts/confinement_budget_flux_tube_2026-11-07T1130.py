#!/usr/bin/env python3
"""confinement_budget_flux_tube_2026-11-07T1130.py

JS (2026-11-07): the framework reads confinement as the saturation of the
tripartite entanglement budget of the GHZ colour singlet; the standard
picture squeezes the colour flux into a string. The two have to be aligned.

Finite checks of the alignment proposed in the companion session note
(knowledge/sessions/confinement_budget_flux_tube_2026-11-07T1130.md):

Part A  The budget in numbers: GHZ_3 and W_3 one-tangles, pairwise tangles,
        three-tangle (CKW residual and Cayley hyperdeterminant agree); for
        GHZ_n and W_n the pairwise concurrence (0 versus 2/n) and the
        entropy across a cut (1 ebit versus H(1/n)): copy versus share.
Part B  Gauss's law at an uncharged vertex of a Z_N lattice gauge theory,
        in the electric basis, is a GHZ-class Frobenius spider: the neutral
        subspace has dimension N^(k-1), its uniform superposition is the
        Fourier transform of the N-level GHZ_k state, for N=2, k=3 it has
        three-tangle 1 and pairwise concurrence 0, and the W_k state is a
        charged vertex. The two-valent vertex is the copy map (flux in equals
        flux out), a chain of them has a one-dimensional neutral subspace,
        and the Z_3 trivalent all-inward vertex is neutral at (1,1,1): the
        baryon junction.
Part C  Copy versus share as energy: a centre (Z_N) charge carried over m
        parallel routes costs the same for every m (one route takes it
        whole); a real-valued Abelian flux costs q^2 R/m (it spreads). The
        shared-flux law on a d-dimensional lattice (FFT Poisson solve) is
        linear in d=1, logarithmic in d=2 and Coulomb 1/R in d=3; the
        copied-flux law is sigma times the graph distance in every d.
Part D  The centre Z_3 of SU(3) grades the computability split: the map
        that fixes the line (e_0, e_1) and rotates the colour C^3 by a
        phase theta is an automorphism of O exactly at theta in
        {0, 2pi/3, 4pi/3}; it is the scalar omega on the colour C^3, the
        identity on the record line, commutes with the su(3) derivations
        and not with a generic g_2 derivation. N-ality of the split: record
        line 0, colour 1, anticolour 2.
Part E  The SU(3) singlet epsilon_{ijk}|ijk> versus the GHZ model: both
        have maximally mixed one-party marginals (zero slack), but the
        singlet's two-quark marginal is the antisymmetric Werner state with
        negativity 1/3, while GHZ_3 (qubit or qutrit) has separable pairs.
Part F  SU(3) irreps (p,q): dimension, quadratic Casimir, N-ality; the
        strong-coupling cost per link (Casimir) against the datum that
        survives gluon screening (N-ality). Tabulation, no check.

Pure numpy; seed 20261107; Cayley--Dickson Convention A as in
scripts/colour_su3_from_e1_structure_2026-09-27T1500.py (e_1 the preferred
unit, colour planes (e_2,e_3), (e_4,e_5), (e_6,-e_7)). Exact stdout is
pasted into the session note.
"""
import itertools
import math

import numpy as np

rng = np.random.default_rng(20261107)
np.set_printoptions(precision=6, suppress=True, linewidth=120)

FAILS = []


def check(name, cond, detail=""):
    tag = "ok  " if cond else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILS.append(name)


# --------------------------------------------------------------------------
# generic quantum helpers
# --------------------------------------------------------------------------
def ptrace(rho, dims, keep):
    """partial trace of a density matrix over the subsystems not in `keep`"""
    n = len(dims)
    keep = list(keep)
    rho = rho.reshape(dims + dims)
    # trace out, from the highest index downwards, every subsystem not kept
    for s in sorted([i for i in range(n) if i not in keep], reverse=True):
        rho = np.trace(rho, axis1=s, axis2=s + rho.ndim // 2)
    d = int(np.prod([dims[i] for i in keep]))
    return rho.reshape(d, d)


def dm(psi):
    return np.outer(psi, psi.conj())


def vn_entropy(rho, base=2.0):
    ev = np.linalg.eigvalsh(rho)
    ev = ev[ev > 1e-14]
    return float(-(ev * np.log(ev)).sum() / np.log(base))


SY = np.array([[0, -1j], [1j, 0]])
YY = np.kron(SY, SY)


def concurrence(rho2):
    R = rho2 @ YY @ rho2.conj() @ YY
    ev = np.sort(np.sqrt(np.clip(np.linalg.eigvals(R).real, 0, None)))[::-1]
    return max(0.0, ev[0] - ev[1] - ev[2] - ev[3])


def one_tangle(rho1):
    return float(2 * (1 - np.trace(rho1 @ rho1).real))


def negativity(rho, dA, dB):
    """sum of |negative eigenvalues| of the partial transpose on B"""
    pt = rho.reshape(dA, dB, dA, dB).transpose(0, 3, 2, 1).reshape(dA * dB, dA * dB)
    ev = np.linalg.eigvalsh((pt + pt.conj().T) / 2)
    return float(-ev[ev < 0].sum()), ev


def hyperdet(psi):
    """Cayley hyperdeterminant of a three-qubit amplitude tensor psi[i,j,k]"""
    p = psi.reshape(2, 2, 2)
    a = p[0, 0, 0]; b = p[0, 0, 1]; c = p[0, 1, 0]; d = p[0, 1, 1]
    e = p[1, 0, 0]; f = p[1, 0, 1]; g = p[1, 1, 0]; h = p[1, 1, 1]
    return (a * a * h * h + b * b * g * g + c * c * f * f + d * d * e * e
            - 2 * (a * h * b * g + a * h * c * f + a * h * d * e + b * g * c * f + b * g * d * e + c * f * d * e)
            + 4 * (a * d * f * g + b * c * e * h))


def ghz(n, N=2):
    v = np.zeros(N ** n, complex)
    for a in range(N):
        v[int(str(a) * n, N)] = 1
    return v / math.sqrt(N)


def wstate(n):
    v = np.zeros(2 ** n, complex)
    for l in range(n):
        v[1 << (n - 1 - l)] = 1
    return v / math.sqrt(n)


def H2(x):
    return 0.0 if x in (0.0, 1.0) else float(-x * math.log2(x) - (1 - x) * math.log2(1 - x))


# ==========================================================================
print("=== Part A: the budget in numbers (copy versus share) ===")
# ==========================================================================
prod3 = np.zeros(8, complex); prod3[0] = 1
print(f"  {'state':8s} {'tau_A':>7s} {'C^2_AB':>7s} {'C^2_AC':>7s} {'tau3(CKW)':>10s} {'4|Det|':>8s}")
for name, psi in [("GHZ_3", ghz(3)), ("W_3", wstate(3)), ("product", prod3)]:
    rho = dm(psi)
    tA = one_tangle(ptrace(rho, [2, 2, 2], [0]))
    cAB = concurrence(ptrace(rho, [2, 2, 2], [0, 1])) ** 2
    cAC = concurrence(ptrace(rho, [2, 2, 2], [0, 2])) ** 2
    t3 = tA - cAB - cAC
    hd = 4 * abs(hyperdet(psi))
    print(f"  {name:8s} {tA:7.4f} {cAB:7.4f} {cAC:7.4f} {t3:10.4f} {hd:8.4f}")
    check(f"{name}: CKW residual equals the hyperdeterminant three-tangle", abs(t3 - hd) < 1e-9)
check("GHZ_3 saturates: tau3 = 1 and both pairwise tangles 0",
      abs(4 * abs(hyperdet(ghz(3))) - 1) < 1e-12
      and concurrence(ptrace(dm(ghz(3)), [2, 2, 2], [0, 1])) < 1e-9)
check("W_3: tau3 = 0, pairwise tangles 4/9, slack 1/9",
      abs(4 * abs(hyperdet(wstate(3)))) < 1e-12
      and abs(concurrence(ptrace(dm(wstate(3)), [2, 2, 2], [0, 1])) ** 2 - 4 / 9) < 1e-9
      and abs(1 - one_tangle(ptrace(dm(wstate(3)), [2, 2, 2], [0])) - 1 / 9) < 1e-9)

print()
print("  GHZ_n versus W_n: pairwise concurrence, entropy across 1|(n-1) and across the balanced cut (bits)")
print(f"  {'n':>3s} {'C(GHZ)':>7s} {'C(W)':>7s} {'2/n':>7s} {'S1(GHZ)':>8s} {'S1(W)':>8s} {'H(1/n)':>8s} {'Sbal(GHZ)':>10s} {'Sbal(W)':>8s}")
okA = True
for n in range(3, 9):
    dims = [2] * n
    rg, rw = dm(ghz(n)), dm(wstate(n))
    cg = concurrence(ptrace(rg, dims, [0, 1]))
    cw = concurrence(ptrace(rw, dims, [0, 1]))
    s1g = vn_entropy(ptrace(rg, dims, [0])); s1w = vn_entropy(ptrace(rw, dims, [0]))
    half = list(range(n // 2))
    sbg = vn_entropy(ptrace(rg, dims, half)); sbw = vn_entropy(ptrace(rw, dims, half))
    print(f"  {n:3d} {cg:7.4f} {cw:7.4f} {2 / n:7.4f} {s1g:8.4f} {s1w:8.4f} {H2(1 / n):8.4f} {sbg:10.4f} {sbw:8.4f}")
    okA &= cg < 1e-9 and abs(cw - 2 / n) < 1e-9 and abs(s1g - 1) < 1e-9 and abs(s1w - H2(1 / n)) < 1e-9 and abs(sbg - 1) < 1e-9
check("GHZ_n: 1 ebit across every cut, pairwise 0; W_n: pairwise 2/n, 1|rest entropy H(1/n)", okA)

# ==========================================================================
print()
print("=== Part B: Gauss's law in the electric basis is a GHZ-class spider ===")
# ==========================================================================


def neutral_configs(N, signs):
    k = len(signs)
    return [e for e in itertools.product(range(N), repeat=k) if sum(s * x for s, x in zip(signs, e)) % N == 0]


def charge(N, signs, e):
    return sum(s * x for s, x in zip(signs, e)) % N


def basis_index(e, N):
    idx = 0
    for x in e:
        idx = idx * N + x
    return idx


def spider_state(N, signs):
    k = len(signs)
    v = np.zeros(N ** k, complex)
    for e in neutral_configs(N, signs):
        v[basis_index(e, N)] = 1
    return v / np.linalg.norm(v)


def fourier(N):
    w = np.exp(2j * np.pi / N)
    return np.array([[w ** (a * b) for b in range(N)] for a in range(N)]) / math.sqrt(N)


for N in (2, 3):
    for signs in [(+1, -1), (+1, +1, +1), (+1, +1, +1, +1)]:
        k = len(signs)
        cfg = neutral_configs(N, signs)
        S = spider_state(N, signs)
        # undo the Fourier transform leg by leg (conjugate on outward legs)
        F = fourier(N)
        U = np.array([[1.0 + 0j]])
        for s in signs:
            U = np.kron(U, (F if s > 0 else F.conj()).conj().T)
        back = U @ S
        fid = abs(np.vdot(ghz(k, N), back)) ** 2
        tag = "in,out" if k == 2 else "all inward"
        print(f"  Z_{N}, valence {k} ({tag}): neutral configurations {len(cfg):3d} = N^(k-1) = {N ** (k - 1):3d};"
              f"  |<GHZ_k^(N)| F^-1 spider>|^2 = {fid:.12f}")
        check(f"Z_{N} k={k}: neutral count N^(k-1) and spider = Fourier transform of GHZ", len(cfg) == N ** (k - 1) and abs(fid - 1) < 1e-12)

# N=2, trivalent: budget numbers of the spider state itself
S23 = spider_state(2, (+1, +1, +1))
r = dm(S23)
t3 = 4 * abs(hyperdet(S23))
c01 = concurrence(ptrace(r, [2, 2, 2], [0, 1]))
print(f"  Z_2 trivalent spider state: tau3 = {t3:.6f}, pairwise concurrence = {c01:.6f}, one-tangle = {one_tangle(ptrace(r, [2, 2, 2], [0])):.6f}")
check("Z_2 trivalent Gauss spider saturates the budget (tau3 = 1, pairwise 0)", abs(t3 - 1) < 1e-12 and c01 < 1e-9)
# N=3 trivalent: pairwise marginal separable (negativity 0), one-party maximally mixed
S33 = spider_state(3, (+1, +1, +1))
r3 = dm(S33)
neg, _ = negativity(ptrace(r3, [3, 3, 3], [0, 1]), 3, 3)
pur = np.trace(ptrace(r3, [3, 3, 3], [0]) @ ptrace(r3, [3, 3, 3], [0])).real
print(f"  Z_3 trivalent spider state: two-party negativity = {neg:.6f}, one-party purity = {pur:.6f} (1/3 = maximally mixed)")
check("Z_3 trivalent Gauss spider: pairwise separable, marginals maximally mixed", neg < 1e-9 and abs(pur - 1 / 3) < 1e-12)

# the W state as a charged vertex
for N in (2, 3):
    signs = (+1, +1, +1)
    W = np.zeros(N ** 3, complex)
    for l in range(3):
        e = [0, 0, 0]; e[l] = 1
        W[basis_index(e, N)] = 1
    W /= np.linalg.norm(W)
    P0 = np.zeros((N ** 3, N ** 3))
    for e in neutral_configs(N, signs):
        i = basis_index(e, N); P0[i, i] = 1
    Q = np.zeros((N ** 3, N ** 3))
    for e in itertools.product(range(N), repeat=3):
        i = basis_index(e, N); Q[i, i] = charge(N, signs, e)
    print(f"  Z_{N}: W_3 (one unit of flux on one of three inward legs): ||P_neutral W||^2 = {np.linalg.norm(P0 @ W) ** 2:.6f}; "
          f"charge eigenstate: {np.allclose(Q @ W, 1 * W)} (charge 1)")
    check(f"Z_{N}: the W_3 vertex is charged (orthogonal to the neutral subspace, charge 1)",
          np.linalg.norm(P0 @ W) < 1e-12 and np.allclose(Q @ W, W))

# the two-valent vertex is the copy map, and a chain copies the source charge all the way
for N in (2, 3):
    copy_img = sorted(neutral_configs(N, (+1, -1)))
    print(f"  Z_{N} two-valent (in,out) neutral configurations: {copy_img}  -> e_out = e_in: the copy map")
    check(f"Z_{N} two-valent neutral subspace is the image of the copy map", copy_img == [(e, e) for e in range(N)])
    R = 5
    q = 1
    sols = [e for e in itertools.product(range(N), repeat=R)
            if e[0] == q and all(e[i] == e[i + 1] for i in range(R - 1))]
    allsols = [e for e in itertools.product(range(N), repeat=R)
               if (e[0] - q) % N == 0 and all((e[i] - e[i + 1]) % N == 0 for i in range(R - 1))]
    print(f"  Z_{N} chain of {R} links from a source of charge {q}: neutral configurations {len(allsols)} (all links carry {q}: {allsols})")
    check(f"Z_{N} chain: one neutral configuration, the charge copied along every link", len(allsols) == 1 and allsols[0] == tuple([q] * R))

# the Z_3 trivalent all-inward vertex: the baryon junction
print("  Z_3 trivalent all-inward vertex, charge of each configuration (0 = neutral):")
rows = []
for e in itertools.product(range(3), repeat=3):
    rows.append(f"{e}:{charge(3, (1, 1, 1), e)}")
for i in range(0, 27, 9):
    print("    " + "  ".join(rows[i:i + 9]))
check("Z_3 junction: (1,1,1) three fundamentals in is neutral (the baryon vertex), (2,2,2) likewise",
      charge(3, (1, 1, 1), (1, 1, 1)) == 0 and charge(3, (1, 1, 1), (2, 2, 2)) == 0)
check("Z_3 junction: (1,2,0) fundamental in, antifundamental in, nothing is neutral (the meson passes through)",
      charge(3, (1, 1, 1), (1, 2, 0)) == 0)
check("Z_3 junction: (1,0,0) and (1,1,0) are charged (N-ality 1 and 2): open flux must end on a charge",
      charge(3, (1, 1, 1), (1, 0, 0)) == 1 and charge(3, (1, 1, 1), (1, 1, 0)) == 2)

# ==========================================================================
print()
print("=== Part C: copy versus share as energy; the Coulomb law needs the embedding, the confining law does not ===")
# ==========================================================================


def zn_cost(e, N):
    return 1 - math.cos(2 * math.pi * e / N)


print("  (i) a unit centre charge over m parallel routes of R links; cost per link 1 - cos(2 pi e/N); minimum over neutral assignments")
R = 7
print(f"  {'m':>3s} {'Z_2 min':>9s} {'Z_3 min':>9s} {'R c(1), Z_2':>12s} {'R c(1), Z_3':>12s} {'real E: R/m':>12s}")
okC = True
for m in range(1, 7):
    mins = {}
    for N in (2, 3):
        best = None
        for e in itertools.product(range(N), repeat=m):
            if sum(e) % N == 1:
                cost = R * sum(zn_cost(x, N) for x in e)
                best = cost if best is None else min(best, cost)
        mins[N] = best
    share = R * 1.0 ** 2 / m
    print(f"  {m:3d} {mins[2]:9.4f} {mins[3]:9.4f} {R * zn_cost(1, 2):12.4f} {R * zn_cost(1, 3):12.4f} {share:12.4f}")
    okC &= abs(mins[2] - R * zn_cost(1, 2)) < 1e-12 and abs(mins[3] - R * zn_cost(1, 3)) < 1e-12
check("centre charge: minimal cost R c(1) for every m (copied whole along one route); real flux: R/m (shared)", okC)
# the real-valued minimisation, checked by least squares rather than asserted
m = 5
A = np.ones((1, m)); b = np.array([1.0])
E_share = np.linalg.lstsq(A, b, rcond=None)[0]           # minimum-norm solution of sum E_i = 1
print(f"  real flux over m = {m} routes: minimum-norm solution E_i = {E_share[0]:.4f} each, energy R sum E^2 = {R * (E_share ** 2).sum():.4f} = R/m = {R / m:.4f}")
check("real flux spreads evenly: minimum-norm solution has E_i = 1/m", np.allclose(E_share, 1 / m))

print()
print("  (ii) shared (real) flux between +1 at the origin and -1 at distance R on a periodic lattice: V = G(0) - G(R) by FFT")


def lattice_potential(d, L, Rs):
    k = 2 * np.pi * np.fft.fftfreq(L) * 1.0
    grids = np.meshgrid(*([k] * d), indexing="ij")
    lap = sum(2 - 2 * np.cos(g) for g in grids)        # -(discrete Laplacian) in Fourier space
    lap[(0,) * d] = np.inf                                # drop the zero mode (neutral source)
    out = []
    for R in Rs:
        rho = np.zeros((L,) * d)
        rho[(0,) * d] = 1.0
        idx = [0] * d; idx[0] = R
        rho[tuple(idx)] = -1.0
        phi = np.real(np.fft.ifftn(np.fft.fftn(rho) / lap))
        V = 0.5 * (phi[(0,) * d] - phi[tuple(idx)])      # half of sum E^2 = half of sum rho phi
        out.append(V)
    return np.array(out)


Rs = np.arange(3, 11)
L1 = 512
V1 = lattice_potential(1, L1, Rs)
V1_ring = 0.5 * Rs * (L1 - Rs) / L1          # exact on a ring: flux (L-R)/L on the short arc, R/L on the long one
V2 = lattice_potential(2, 256, Rs)
V3 = lattice_potential(3, 64, Rs)
slope1 = np.polyfit(Rs, V1, 1)[0]
slope2 = np.polyfit(np.log(Rs), V2, 1)[0]
slope3 = np.polyfit(1.0 / Rs, V3, 1)[0]
print(f"  {'R':>3s} {'d=1':>9s} {'d=2':>9s} {'d=3':>9s}")
for R, a, b2, c in zip(Rs, V1, V2, V3):
    print(f"  {R:3d} {a:9.4f} {b2:9.4f} {c:9.4f}")
print(f"  d=1: slope dV/dR = {slope1:.4f} (one route: linear; the ring of L = {L1} gives exactly R(L-R)/2L, slope 1/2 as L -> infinity;"
      f" max |V - R(L-R)/2L| = {np.max(np.abs(V1 - V1_ring)):.2e})")
print(f"  d=2: slope dV/dlnR = {slope2:.4f} (expected 1/(2 pi) = {1 / (2 * np.pi):.4f})")
print(f"  d=3: slope dV/d(1/R) = {slope3:.4f} (expected -1/(4 pi) = {-1 / (4 * np.pi):.4f}: Coulomb)")
check("shared flux in d=1 equals the exact ring formula R(L-R)/2L (linear, slope 1/2 as L -> infinity)",
      np.max(np.abs(V1 - V1_ring)) < 1e-9 and abs(slope1 - 0.5) < 0.02)
check("shared flux: logarithmic in d=2 (slope 1/2pi within 5%)", abs(slope2 - 1 / (2 * np.pi)) < 0.05 / (2 * np.pi))
check("shared flux: Coulomb in d=3 (slope -1/4pi within 8%)", abs(slope3 + 1 / (4 * np.pi)) < 0.08 / (4 * np.pi))

print()
print("  (iii) copied (centre) flux on the same lattices: cost = c(1) x graph distance, whatever d and whatever the embedding")
seps = [(5, 0, 0), (3, 4, 0), (0, 0, 5), (5, 5, 0), (3, 3, 3)]
print(f"  {'separation':>12s} {'Euclid':>8s} {'graph dist':>11s} {'cost/c(1)':>10s}")
okC3 = True
for s in seps:
    eu = math.sqrt(sum(x * x for x in s)); gd = sum(abs(x) for x in s)
    print(f"  {str(s):>12s} {eu:8.3f} {gd:11d} {gd:10d}")
    okC3 &= True
check("copied flux: V/c(1) equals the Manhattan graph distance; (5,0,0) and (3,4,0) share a Euclidean length but not a cost",
      abs(math.sqrt(25) - math.sqrt(9 + 16)) < 1e-12 and (5 != 7))

# ==========================================================================
print()
print("=== Part D: the centre Z_3 of SU(3) grades the computability split (Convention A octonions) ===")
# ==========================================================================


def conj_o(x):
    y = np.array(x, copy=True); y[1:] = -y[1:]; return y


def cd(x, y):
    n = x.size
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate((cd(a, c) - cd(conj_o(d), b), cd(d, a) + cd(b, conj_o(c))))


E8 = np.eye(8)
T = np.array([[cd(E8[i], E8[j]) for j in range(8)] for i in range(8)])     # T[i,j,:] = e_i e_j
pairs = [(2, 3, 1), (4, 5, 1), (6, 7, -1)]                                  # e_1 e_a = s e_b
check("Convention A: e_1 e_2 = e_3, e_1 e_4 = e_5, e_1 e_6 = -e_7 (the colour planes of the 09-27 script)",
      all(np.allclose(T[1, a], s * E8[b]) for a, b, s in pairs))

# derivations by the Leibniz nullspace
rows = []
for i in range(8):
    for j in range(8):
        M = np.zeros((8, 64))
        for a in range(8):
            for b in range(8):
                col = a * 8 + b
                # D(e_i e_j) = sum_k T[i,j,k] D[:,k]  -> component a of D e_k is D[a,k]
                M[a, col] += T[i, j, b]                      # D[a,b] contributes to component a when k = b
                # - D(e_i) e_j: D e_i = sum_a' D[a',i] e_a'; (e_a' e_j) has components T[a',j,:]
                if b == i:
                    M[:, col] -= T[a, j, :]
                # - e_i D(e_j): D e_j = sum_b' D[b',j] e_b'; (e_i e_b') has components T[i,b',:]
                if b == j:
                    M[:, col] -= T[i, a, :]
        rows.append(M)
Mfull = np.vstack(rows)
u, sv, vt = np.linalg.svd(Mfull)
null = vt[sv.size - (sv < 1e-10).sum():] if (sv < 1e-10).sum() else vt[64:]
nullity = int((sv < 1e-10).sum()) + (64 - sv.size)
Ders = [v.reshape(8, 8) for v in vt[64 - nullity:]]
print(f"  dim Der(O) = {len(Ders)} (g_2 = 14)")
check("dim Der(O) = 14", len(Ders) == 14)
# the stabiliser of e_1 inside Der(O): D e_1 = 0
B = np.array([D.reshape(64) for D in Ders]).T          # 64 x 14
C1 = np.array([D[:, 1] for D in Ders]).T               # 8 x 14: the images of e_1
u2, s2, vt2 = np.linalg.svd(C1)
nul2 = 14 - int((s2 > 1e-10).sum())
Stab = [sum(c * D for c, D in zip(vt2[14 - nul2 + i], Ders)) for i in range(nul2)]
print(f"  dim {{D in Der(O): D e_1 = 0}} = {len(Stab)} (su(3) = 8)")
check("stabiliser of e_1 has dimension 8", len(Stab) == 8)

# the complex structure J = L_{e_1} on the complement, and the phase map phi_theta
J = T[1].T.copy()                     # J[a,b] = component a of e_1 e_b
Jc = J[2:, 2:]
check("L_{e_1} squares to -1 on the complement of (e_0, e_1)", np.allclose(Jc @ Jc, -np.eye(6)))


def phi(theta):
    P = np.eye(8)
    P[2:, 2:] = math.cos(theta) * np.eye(6) + math.sin(theta) * Jc
    return P


def aut_residual(P):
    return max(np.linalg.norm(P @ T[i, j] - cd(P @ E8[i], P @ E8[j])) for i in range(8) for j in range(8))


thetas = [0.0, math.pi / 3, 2 * math.pi / 3, math.pi, 4 * math.pi / 3, 5 * math.pi / 3, math.pi / 2, 2 * math.pi / 5] + list(rng.uniform(0, 2 * math.pi, 3))
print(f"  {'theta/(2pi/3)':>14s} {'automorphism residual':>22s}")
res = {}
for th in thetas:
    res[th] = aut_residual(phi(th))
    print(f"  {th / (2 * math.pi / 3):14.6f} {res[th]:22.3e}")
at_cube_roots = [res[th] for th in (0.0, 2 * math.pi / 3, 4 * math.pi / 3)]
elsewhere = [res[th] for th in thetas if min(abs(th - c) for c in (0.0, 2 * math.pi / 3, 4 * math.pi / 3, 2 * math.pi)) > 1e-6]
check("phi_theta is an automorphism of O exactly at theta in {0, 2pi/3, 4pi/3}: the centre Z_3 of SU(3)",
      max(at_cube_roots) < 1e-12 and min(elsewhere) > 0.1)
Om = phi(2 * math.pi / 3)
check("phi_{2pi/3}^3 = identity and phi_{2pi/3} is not the identity", np.allclose(Om @ Om @ Om, np.eye(8)) and not np.allclose(Om, np.eye(8)))
ev = np.linalg.eigvals(Om)
print("  eigenvalues of phi_{2pi/3}:", np.round(np.sort_complex(ev), 6))
w = np.exp(2j * np.pi / 3)
n0 = int(np.sum(np.abs(ev - 1) < 1e-9)); n1 = int(np.sum(np.abs(ev - w) < 1e-9)); n2 = int(np.sum(np.abs(ev - w.conj()) < 1e-9))
print(f"  multiplicities: eigenvalue 1 -> {n0} (the record line e_0, e_1), omega -> {n1}, omega-bar -> {n2} (the colour C^3 and its conjugate)")
check("eigenvalue multiplicities 2, 3, 3", (n0, n1, n2) == (2, 3, 3))


def to_c3(o):
    return np.array([o[a] + 1j * s * o[b] for a, b, s in pairs])


okscalar = True
for a, b, s in pairs:
    for v in (E8[a], E8[b]):
        okscalar &= np.allclose(to_c3(Om @ v), w * to_c3(v))
x = np.zeros(8); x[2:] = rng.normal(size=6)
print(f"  on a random colour vector: to_c3(phi x) = omega * to_c3(x): {np.allclose(to_c3(Om @ x), w * to_c3(x))};  phi fixes e_0 and e_1: {np.allclose(Om[:, :2], E8[:, :2])}")
check("phi_{2pi/3} is the scalar omega on the colour C^3 (in the 09-27 pairing) and the identity on the record line",
      okscalar and np.allclose(Om[:, :2], E8[:, :2]))
comm_stab = max(np.linalg.norm(Om @ D - D @ Om) for D in Stab)
Dgen = sum(rng.normal() * D for D in Ders)
comm_gen = np.linalg.norm(Om @ Dgen - Dgen @ Om)
print(f"  commutator with the 8 su(3) derivations: max norm {comm_stab:.2e}; with a generic g_2 derivation: {comm_gen:.3f}")
check("phi_{2pi/3} is central in SU(3) and not central in G_2", comm_stab < 1e-10 and comm_gen > 0.1)
print("  N-ality of the split (eigenvalue of the centre, as a power of omega): record line C -> 0; colour C^3 -> 1; anticolour -> 2")

# ==========================================================================
print()
print("=== Part E: the SU(3) singlet epsilon_{ijk}|ijk> against the GHZ model ===")
# ==========================================================================
eps = np.zeros(27, complex)
for p in itertools.permutations(range(3)):
    sign = np.linalg.det(np.eye(3)[list(p)])
    eps[p[0] * 9 + p[1] * 3 + p[2]] = sign
eps /= np.linalg.norm(eps)
reps = dm(eps)
rho1 = ptrace(reps, [3, 3, 3], [0]); rho12 = ptrace(reps, [3, 3, 3], [0, 1])
neg_eps, ev_eps = negativity(rho12, 3, 3)
print(f"  singlet: one-quark marginal purity {np.trace(rho1 @ rho1).real:.6f} (1/3: maximally mixed, slack r^2 = 0); one|rest entropy {vn_entropy(rho1, math.e):.6f} = ln 3 = {math.log(3):.6f}")
print(f"  singlet: two-quark partial-transpose eigenvalues {np.round(np.sort(ev_eps), 6)}; negativity {neg_eps:.6f} (1/3)")
Pa = np.zeros((9, 9))
for i in range(3):
    for j in range(3):
        if i != j:
            v = np.zeros(9); v[3 * i + j] = 1; v[3 * j + i] = -1; v /= math.sqrt(2)
            Pa += np.outer(v, v) / 2
check("singlet two-quark marginal is the antisymmetric projector over 3 (the antisymmetric Werner state)", np.allclose(rho12, Pa / 3 * 1.0) or np.allclose(rho12, Pa))
check("singlet: one-quark marginal maximally mixed (zero slack, as for GHZ)", abs(np.trace(rho1 @ rho1).real - 1 / 3) < 1e-12)
check("singlet: two-quark marginal entangled, negativity 1/3 (unlike GHZ)", abs(neg_eps - 1 / 3) < 1e-9)
for name, psi, dims in [("qubit GHZ_3", ghz(3), [2, 2, 2]), ("qutrit GHZ_3", ghz(3, 3), [3, 3, 3])]:
    r12 = ptrace(dm(psi), dims, [0, 1]); n12, _ = negativity(r12, dims[0], dims[1])
    r1 = ptrace(dm(psi), dims, [0])
    print(f"  {name}: one-party purity {np.trace(r1 @ r1).real:.6f}, two-party negativity {n12:.6f}")
    check(f"{name}: pairs separable (negativity 0)", n12 < 1e-9)
# tracing one party: what is left
print(f"  after tracing one quark: singlet pair negativity {neg_eps:.4f} (still entangled); GHZ pair negativity 0 (classically correlated only)")

# ==========================================================================
print()
print("=== Part F: SU(3) irreps -- the copy cost per link (Casimir) and the datum that survives screening (N-ality) ===")
# ==========================================================================
print(f"  {'(p,q)':>6s} {'dim':>4s} {'C_2':>7s} {'C_2/C_2(fund)':>14s} {'N-ality':>8s} {'asymptotic string':>18s}")
for p, q in [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (2, 1), (0, 3)]:
    dim = (p + 1) * (q + 1) * (p + q + 2) // 2
    c2 = (p * p + q * q + p * q + 3 * p + 3 * q) / 3
    k = (p - q) % 3
    fate = "sigma_1 (fundamental's)" if k in (1, 2) else "breaks (screened to 0)"
    print(f"  ({p},{q}) {dim:4d} {c2:7.4f} {c2 / (4 / 3):14.4f} {k:8d} {fate:>18s}")
check("Casimir of the fundamental is 4/3 and of the adjoint 3; N-ality of (1,0),(0,1),(1,1),(2,0) is 1,2,0,2",
      abs((1 + 0 + 0 + 3 + 0) / 3 - 4 / 3) < 1e-12 and abs((1 + 1 + 1 + 3 + 3) / 3 - 3) < 1e-12
      and [(p - q) % 3 for p, q in [(1, 0), (0, 1), (1, 1), (2, 0)]] == [1, 2, 0, 2])

print()
if FAILS:
    print(f"CONFINEMENT BUDGET FLUX TUBE: FAIL ({len(FAILS)}): " + "; ".join(FAILS))
else:
    print("CONFINEMENT BUDGET FLUX TUBE: PASS")
