#!/usr/bin/env python3
"""mass_gap_relationship_cost_2026-11-21T0800.py

Checks for knowledge/sessions/mass_gap_relationship_cost_2026-11-21T0800.md:
JS's direction that the Yang--Mills mass gap should be approached through the
energy needed to create new relationships (new space) in the colour sector.

Part A  Z_N lattice gauge theory in 2+1 dimensions, N = 3 (the centre of
        colour) and N = 2, on an open lattice of plaquettes, in the electric
        (flux-loop) basis.  A charge-free electric configuration on a planar
        graph is the gradient of a Z_N height on the plaquettes (outside
        height 0), so H = sum_links [1 - cos(2 pi e_l / N)]
                          - x sum_p (X_p + X_p^dagger),
        e_l the height difference across link l, X_p the plaquette operator.
        Static charges enter as a fixed offset on a string of links.
        Computed by Lanczos: the gap, the static potential V(R), the vortex
        (dual-superconductor) order parameter M = <cos(2 pi n_p / N)>, and
        the density rho of links carrying flux in the vacuum.
Part B  The same vacuum at x = 0 in the link (holonomy) basis, on two
        plaquettes with seven Z_3 links: the empty electric state is the
        uniform superposition of all gauge fields.
Part C  Arithmetic: the loop competition E(L) = sigma L + c/L, the bag,
        the trace anomaly, and one- and two-loop dimensional transmutation.

Pure numpy.  Seed 20261121 (used only for Lanczos start vectors).  No
Cayley--Dickson products are used.  Final line: MASS GAP RELATIONSHIP COST:
PASS or FAIL.
"""
import itertools, math, sys
import numpy as np

SEED = 20261121
rng = np.random.default_rng(SEED)
CHECKS = []
def check(name, ok):
    CHECKS.append(bool(ok)); print("  [%s] %s" % ("PASS" if ok else "FAIL", name))

# ---------------------------------------------------------------- Part A
def build(N, Lx, Ly, R):
    """Diagonal electric energy and flux-link count on the height basis.
    String of R horizontal links on the line between rows j=0 and j=1,
    covering i = 0..R-1: static charges at its two ends."""
    P = Lx * Ly
    idx = np.indices((N,) * P)
    pid = lambda i, j: i * Ly + j
    c = lambda e: 1.0 - np.cos(2 * np.pi * e / N)
    D = np.zeros((N,) * P); F = np.zeros((N,) * P); nl = 0
    for i in range(Lx):
        for j in range(Ly):
            n = idx[pid(i, j)]
            if i + 1 < Lx:
                e = (idx[pid(i + 1, j)] - n) % N; D += c(e); F += (e != 0); nl += 1
            if j + 1 < Ly:
                s = 1 if (j == 0 and i < R) else 0
                e = (idx[pid(i, j + 1)] - n + s) % N; D += c(e); F += (e != 0); nl += 1
            nb = (i == 0) + (i == Lx - 1) + (j == 0) + (j == Ly - 1)
            if nb:
                D += nb * c(n); F += nb * (n != 0); nl += nb
    return D, F / nl, idx

def lanczos(D, x, k=140):
    P = D.ndim; shape = D.shape; dim = D.size
    def H(v):
        a = v.reshape(shape); out = D * a
        for p in range(P):
            out = out - x * (np.roll(a, 1, axis=p) + np.roll(a, -1, axis=p))
        return out.reshape(dim)
    Q = np.zeros((k, dim)); al = np.zeros(k); be = np.zeros(k)
    q = rng.standard_normal(dim); q /= np.linalg.norm(q)
    m = k
    for it in range(k):
        Q[it] = q; w = H(q); al[it] = q @ w
        w -= Q[:it + 1].T @ (Q[:it + 1] @ w)
        w -= Q[:it + 1].T @ (Q[:it + 1] @ w)
        b = np.linalg.norm(w)
        if b < 1e-11: m = it + 1; break
        be[it] = b; q = w / b
    T = np.diag(al[:m]) + np.diag(be[:m - 1], 1) + np.diag(be[:m - 1], -1)
    ev, S = np.linalg.eigh(T)
    g = S[:, 0] @ Q[:m]; g1 = S[:, 1] @ Q[:m]
    res = max(np.linalg.norm(H(g) - ev[0] * g), np.linalg.norm(H(g1) - ev[1] * g1))
    return ev[0], ev[1], g, res

def run(N, Lx, Ly, xs, Rs):
    c1 = 1.0 - math.cos(2 * math.pi / N)
    print("\nA. Z_%d gauge theory, %d x %d plaquettes (%d states); c(1) = %.4f"
          % (N, Lx, Ly, N ** (Lx * Ly), c1))
    print("      x      gap   gap/4c1     V(1)     V(2)     V(3)   sigma   sigma/c1  gap/sigma      M     rho")
    rows = []; worst = 0.0
    centre = (Lx // 2 if Lx % 2 else 1) * Ly + (Ly // 2 if Ly % 2 else 1)
    for x in xs:
        D, F, idx = build(N, Lx, Ly, 0)
        e0, e1, g, r = lanczos(D, x); worst = max(worst, r)
        p = (g * g).reshape(D.shape)
        M = float((p * np.cos(2 * np.pi * idx[centre] / N)).sum())
        rho = float((p * F).sum())
        V = []
        for R in Rs:
            DR, _, _ = build(N, Lx, Ly, R)
            eR, _, _, r = lanczos(DR, x); worst = max(worst, r)
            V.append(eR - e0)
        gap = e1 - e0; sig = V[2] - V[1]
        rows.append((x, gap, V, sig, M, rho))
        print("  %5.2f %8.4f  %7.4f %8.4f %8.4f %8.4f %7.4f   %7.4f  %9.3f %6.3f  %6.4f"
              % (x, gap, gap / (4 * c1), V[0], V[1], V[2], sig, sig / c1,
                 gap / sig if abs(sig) > 1e-9 else float('inf'), M, rho))
    print("  worst Lanczos residual %.1e" % worst)
    check("Z_%d: Lanczos residuals below 1e-6" % N, worst < 1e-6)
    x0, gap0, V0, sig0, M0, rho0 = rows[0]
    check("Z_%d strong coupling: gap = 4 c(1) within 2%% (the smallest closed network has four links)" % N,
          abs(gap0 / (4 * c1) - 1) < 0.02)
    check("Z_%d strong coupling: V(R) = R c(1) within 2%% for R = 1, 2, 3 (one cost per link created)" % N,
          all(abs(V0[i] / ((i + 1) * c1) - 1) < 0.02 for i in range(3)))
    check("Z_%d strong coupling: vacuum has M > 0.99 and flux-link density rho < 0.01" % N,
          M0 > 0.99 and rho0 < 0.01)
    sigs = [r[3] for r in rows]; Ms = [r[4] for r in rows]; rhos = [r[5] for r in rows]
    check("Z_%d: sigma falls monotonically as the plaquette term grows" % N,
          all(sigs[i + 1] < sigs[i] + 1e-9 for i in range(len(sigs) - 1)))
    check("Z_%d: M falls and rho rises monotonically (the vacuum fills with flux)" % N,
          all(Ms[i + 1] < Ms[i] + 1e-9 for i in range(len(Ms) - 1)) and
          all(rhos[i + 1] > rhos[i] - 1e-9 for i in range(len(rhos) - 1)))
    xl, gapl, Vl, sigl, Ml, rhol = rows[-1]
    check("Z_%d weak coupling (x = %.1f): gap is large while sigma/gap < 0.05 (a gap without confinement)" % (N, xl),
          gapl > 1.0 and abs(sigl) / gapl < 0.05)
    return rows

rowsA3 = run(3, 3, 3, [0.02, 0.05, 0.10, 0.20, 0.30, 0.40, 0.60, 1.00, 3.00], [1, 2, 3])
rowsA2 = run(2, 4, 4, [0.02, 0.10, 0.30, 0.60, 1.00, 1.50, 2.00, 3.00, 6.00], [1, 2, 3])

# ---------------------------------------------------------------- Part B
print("\nB. The empty electric vacuum in the link basis: two plaquettes, seven Z_3 links")
N = 3; nlk = 7; dim = N ** nlk
# sites 0..5: (0,0),(1,0),(2,0),(0,1),(1,1),(2,1); links (tail, head)
links = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]
plaq = [[(0, 1), (5, 1), (2, -1), (4, -1)], [(1, 1), (6, 1), (3, -1), (5, -1)]]
conf = np.array(list(itertools.product(range(N), repeat=nlk)))
w = np.exp(2j * np.pi / N)
psi = np.ones(dim) / math.sqrt(dim)            # eigenvalue 1 of every link shift: zero electric flux
def shift(v, l, s=1):
    return np.roll(v.reshape((N,) * nlk), s, axis=l).reshape(dim)
elec = sum(1.0 - (psi @ shift(psi, l)) for l in range(nlk))
check("zero electric energy: every link shift has expectation 1", abs(elec) < 1e-12)
check("the state is uniform over all %d gauge fields (amplitude spread %.1e)" % (dim, np.ptp(psi)),
      np.ptp(psi) < 1e-15)
hol = [sum(s * conf[:, l] for l, s in pl) % N for pl in plaq]
dist = [[float((psi ** 2)[h == k].sum()) for k in range(N)] for h in hol]
print("  plaquette holonomy distribution: %s" % dist)
check("each plaquette holonomy is uniformly distributed (1/3 each): magnetic flux fully disordered",
      all(abs(d - 1 / 3) < 1e-12 for dd in dist for d in dd))
W = [abs((psi ** 2 * w ** h).sum()) for h in hol]
Wboth = abs((psi ** 2 * w ** ((hol[0] + hol[1]) % N)).sum())
check("Wilson loops vanish: |<W_1>|, |<W_2>|, |<W_12>| = %.1e, %.1e, %.1e" % (W[0], W[1], Wboth),
      max(W + [Wboth]) < 1e-12)
vort = psi @ shift(psi, 0)                      # shift on a boundary link of plaquette 1 = vortex creation
check("vortex (holonomy-shift) operator has expectation %.6f: a perfect magnetic condensate" % vort,
      abs(vort - 1) < 1e-12)
# electric basis: Fourier transform on every link; the state is the single basis vector e = 0
t = psi.reshape((N,) * nlk).astype(complex)
for l in range(nlk):
    t = np.fft.fft(t, axis=l) / math.sqrt(N)
pe = np.abs(t.reshape(dim)) ** 2
check("in the electric basis it is the one product state e = 0 (weight %.12f): no link is related to any other" % pe[0],
      abs(pe[0] - 1) < 1e-12)
rho_l = np.abs(np.tensordot(t, t.conj(), axes=(list(range(1, nlk)), list(range(1, nlk)))))
ent = -sum(p * math.log(p) for p in np.linalg.eigvalsh(rho_l) if p > 1e-14)
check("entanglement entropy of one link with the rest = %.2e" % ent, abs(ent) < 1e-10)

# ---------------------------------------------------------------- Part C
print("\nC1. Loop competition E(L) = sigma L + c/L, minimum 2 sqrt(c sigma) at L = sqrt(c/sigma)")
Ls = np.linspace(0.05, 20, 400001)
for c in (math.pi / 2, math.pi, 2 * math.pi):
    num = float((Ls + c / Ls).min())
    print("  c = %.4f: numerical minimum %.6f, 2 sqrt(c) = %.6f (units sqrt(sigma))" % (c, num, 2 * math.sqrt(c)))
check("numerical minimum equals 2 sqrt(c sigma) for the three values of c",
      all(abs(float((Ls + c / Ls).min()) - 2 * math.sqrt(c)) < 1e-6 for c in (math.pi / 2, math.pi, 2 * math.pi)))
lat = [("lattice A (from memory, VERIFY-CITE)", 3.405, 0.021), ("lattice B (from memory, VERIFY-CITE)", 3.55, 0.07)]
cands = [("c = pi/2   one orthogonalisation per traversal (Margolus-Levitin)", 2 * math.sqrt(math.pi / 2)),
         ("c = pi     half a wavelength on the loop", 2 * math.sqrt(math.pi)),
         ("c = 2 pi   one wavelength on the loop", 2 * math.sqrt(2 * math.pi)),
         ("closed Nambu-Goto string, D = 4, N = 1: sqrt(8 pi 11/12)", math.sqrt(8 * math.pi * 11 / 12))]
print("  candidate                                                         m/sqrt(sigma)   pull A   pull B")
for nm, v in cands:
    print("  %-66s %8.3f   %+6.1f   %+6.1f" % (nm, v, (v - lat[0][1]) / lat[0][2], (v - lat[1][1]) / lat[1][2]))
for nm, v, e in lat:
    print("  %-40s m/sqrt(sigma) = %.3f +/- %.3f  ->  c required = %.3f" % (nm, v, e, v * v / 4))
vals = [v for _, v in cands]
check("every candidate is within a factor 1.5 of the lattice ratio, and they disagree with each other by %.2fx: order of magnitude only" % (max(vals) / min(vals)),
      all(1 / 1.5 < v / 3.405 < 1.5 for v in vals) and max(vals) / min(vals) > 1.5)

print("\nC2. The bag: creating a volume V of colour space costs B V")
x_mode = 2 * 2.7437                              # two lowest TE gluon modes (from memory, VERIFY-CITE)
def bag_mass(B14):                               # E(R) = x/R + (4 pi/3) B R^3
    B = B14 ** 4; R = (x_mode / (4 * math.pi * B)) ** 0.25
    return x_mode / R + 4 * math.pi / 3 * B * R ** 3, R
for B14 in (0.145, 0.200, 0.241):
    Mb, Rb = bag_mass(B14)
    closed = 4 / 3 * (4 * math.pi) ** 0.25 * x_mode ** 0.75 * B14
    print("  B^(1/4) = %.3f GeV: glueball bag mass %.3f GeV (closed form %.3f), radius %.2f fm, M/B^(1/4) = %.3f"
          % (B14, Mb, closed, Rb * 0.19733, Mb / B14))
check("bag mass equals (4/3)(4 pi B)^(1/4) x^(3/4): linear in B^(1/4), zero iff B = 0",
      all(abs(bag_mass(b)[0] - 4 / 3 * (4 * math.pi) ** 0.25 * x_mode ** 0.75 * b) < 1e-12 for b in (0.145, 0.2, 0.241)))
G2 = 0.012                                       # <(alpha_s/pi) G^2> in GeV^4 (SVZ value, from memory)
for nf in (0, 3):
    b0 = 11 - 2 * nf / 3; eps = -b0 / 32 * G2
    print("  trace anomaly, n_f = %d: vacuum energy density = -(b0/32) <alpha G^2/pi> = %.5f GeV^4, |eps|^(1/4) = %.3f GeV"
          % (nf, eps, abs(eps) ** 0.25))
als, B14 = 0.55, 0.145
sig = math.sqrt(32 * math.pi * als * B14 ** 4 / 3)
print("  bag flux tube: sigma = sqrt(32 pi alpha_s B / 3); alpha_s = %.2f, B^(1/4) = %.3f GeV gives sqrt(sigma) = %.3f GeV (measured 0.44)"
      % (als, B14, math.sqrt(sig)))
A = np.linspace(1e-3, 400, 4000001); g2 = 4 * math.pi * als * 4 / 3; Bv = B14 ** 4
num = float((g2 / (2 * A) + Bv * A).min())
check("tube energy g^2/(2A) + B A minimised numerically equals sqrt(2 g^2 B) = %.5f GeV^2" % sig, abs(num - sig) < 1e-7)

print("\nC3. Dimensional transmutation: ln(M/Lambda) = 2 pi / (b0 alpha_s(M)) = (8 pi^2/g^2)/b0")
def run2(a, mu0, mu1, nf, loops=2, n=20000):
    b0 = 11 - 2 * nf / 3; b1 = 102 - 38 * nf / 3
    t0, t1 = math.log(mu0 ** 2), math.log(mu1 ** 2); h = (t1 - t0) / n
    f = lambda a: -a * a * (b0 / (4 * math.pi) + (b1 * a / (16 * math.pi ** 2) if loops == 2 else 0))
    for _ in range(n):
        k1 = f(a); k2 = f(a + h * k1 / 2); k3 = f(a + h * k2 / 2); k4 = f(a + h * k3); a += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a
MZ, MT, MM, aZ = 91.1876, 172.57, 3600.0, 0.1180
for loops in (1, 2):
    aM = run2(run2(aZ, MZ, MT, 5, loops), MT, MM, 6, loops)
    print("  %d-loop: alpha_s(3.6 TeV) = %.5f, g_s^2 = %.4f, instanton action 8 pi^2/g^2 = 2 pi/alpha_s = %.2f nats"
          % (loops, aM, 4 * math.pi * aM, 2 * math.pi / aM))
a1 = run2(run2(aZ, MZ, MT, 5, 1), MT, MM, 6, 1)
chk = 1 / (1 / aZ + 23 / 3 / (2 * math.pi) * math.log(MT / MZ) + 7 / (2 * math.pi) * math.log(MM / MT))
check("one-loop integration agrees with the closed form (%.6f, %.6f)" % (a1, chk), abs(a1 - chk) < 1e-8)
# one-loop Lambda with thresholds at m_t, m_b = 4.18, m_c = 1.27
lam6 = MM * math.exp(-2 * math.pi / (7 * a1))
at = 1 / (1 / aZ + 23 / 3 / (2 * math.pi) * math.log(MT / MZ)); lam5 = MZ * math.exp(-2 * math.pi / (23 / 3 * aZ))
ab = 1 / (1 / aZ + 23 / 3 / (2 * math.pi) * math.log(4.18 / MZ)); lam4 = 4.18 * math.exp(-2 * math.pi / (25 / 3 * ab))
ac = 1 / (1 / ab + 25 / 3 / (2 * math.pi) * math.log(1.27 / 4.18)); lam3 = 1.27 * math.exp(-2 * math.pi / (9 * ac))
print("  one-loop Lambda: n_f = 6 continued from 3.6 TeV %.4f GeV; n_f = 5: %.4f; n_f = 4: %.4f; n_f = 3: %.4f GeV"
      % (lam6, lam5, lam4, lam3))
print("  ln(3.6 TeV / Lambda_3) = %.2f;  Lambda_3 / v = %.2e (v = 246.22 GeV);  sqrt(sigma)/v = %.2e"
      % (math.log(MM / lam3), lam3 / 246.22, 0.44 / 246.22))
check("the one-loop hadronic scale is of order 1e-3 of v, as op:qcd-scale states", 2e-4 < lam3 / 246.22 < 5e-3)

print("\n%d/%d checks passed" % (sum(CHECKS), len(CHECKS)))
print("MASS GAP RELATIONSHIP COST: %s" % ("PASS" if all(CHECKS) else "FAIL"))
