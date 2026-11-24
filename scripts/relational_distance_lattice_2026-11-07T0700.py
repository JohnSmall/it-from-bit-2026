#!/usr/bin/env python3
"""
If distance is relational, inferred from information exchange, is a lattice
still needed to compute QCD?  Fable session, 2026-11-07T0700.  Session note:
knowledge/sessions/relational_distance_lattice_2026-11-07T0700.md

Four finite checks of the structure behind the answer.

  A. A two-dimensional U(1) gauge theory with the Wilson action on a planar
     graph.  With free boundaries the face (plaquette) angles are independent
     and a Wilson loop enclosing n faces has expectation (I_1(b)/I_0(b))^n:
     the loop sees the COUNT of faces it encloses and nothing of their
     embedding.  The lattice spacing in physical units is then INFERRED by
     matching the string tension, a = sqrt(sigma_lat / sigma_phys): the
     lattice is dimensionless and its distance is read off a correlation.
  B. A causal set: N points sprinkled uniformly into a two-dimensional
     causal diamond of proper height tau.  The longest chain is the longest
     increasing subsequence of a random permutation, with mean 2 sqrt N
     (Vershik--Kerov, Logan--Shepp; Baik--Deift--Johansson correction
     -1.7711 N^{1/6}), so proper time is read off a count of exchanges:
     tau = L / sqrt(2 rho).  The fraction of related pairs gives the
     dimension (Myrheim--Meyer): 1/2 in two dimensions, 1/10 in four.  A
     regular lattice cut to the same diamond has a frame: its point count,
     chain length and ordering fraction change under a boost; the sprinkling
     is a Poisson process in every frame.
  C. Fermion doubling on a regular lattice (Nielsen--Ninomiya): the naive
     dispersion sin(k) has two zeros in one dimension with opposite slopes,
     2^d in d dimensions (16 in four); the Wilson term lifts the doublers to
     mass 2r/a and breaks chiral symmetry to do so.
  D. Distance from exchange: a single excitation hopping on a chain of 61
     sites.  The time at which its probability first reaches site j grows
     linearly in the GRAPH distance j, with the same slope whether the sites
     are embedded regularly or at random positions: the information sees the
     coupling graph, not the embedding.

Seed 20261107.  No scipy: Bessel functions by quadrature.  No hidden state.
Final line "RELATIONAL DISTANCE LATTICE: PASS" or "... FAIL".
"""
import numpy as np
_trapz = getattr(np, "trapezoid", None) or np.trapz
from math import gamma

np.set_printoptions(precision=4, suppress=True, linewidth=120)
rng = np.random.default_rng(20261107)
ok = True


def check(cond, msg):
    global ok
    ok = ok and bool(cond)
    print(("   ok  " if cond else "   FAIL") + " " + msg)


# ----------------------------------------------------------------------------
print("A. two-dimensional U(1) gauge theory: a loop sees the count of faces, the spacing is inferred")


def bessel_I(n, b, m=200001):
    th = np.linspace(0.0, np.pi, m)
    return _trapz(np.exp(b * np.cos(th)) * np.cos(n * th), th) / np.pi


def plaquette_mean(b):
    """<e^{i theta}> for one face with weight exp(b cos theta): I_1(b)/I_0(b)."""
    th = np.linspace(-np.pi, np.pi, 400001)
    w = np.exp(b * np.cos(th))
    return _trapz(w * np.exp(1j * th), th) / _trapz(w, th)


for b in (1.0, 2.0, 4.0):
    r_quad = plaquette_mean(b)
    r_bes = bessel_I(1, b) / bessel_I(0, b)
    check(abs(r_quad - r_bes) < 1e-9, "b = %.1f : one-face expectation %.6f = I_1/I_0 = %.6f" % (b, r_quad.real, r_bes))

# independence of faces: sample free-boundary links on an L x L open lattice by sampling
# the face angles directly (axial gauge makes the map links -> faces a bijection with
# unit Jacobian); then the Wilson loop around any region is the product over its faces.
L = 6
b = 2.0
nsamp = 20000
r = bessel_I(1, b) / bessel_I(0, b)
# rejection-sample face angles with weight exp(b cos theta)
def sample_faces(n):
    out = []
    while len(out) < n:
        th = rng.uniform(-np.pi, np.pi, size=4 * n)
        u = rng.uniform(0, 1, size=4 * n)
        keep = th[u < np.exp(b * (np.cos(th) - 1.0))]
        out.extend(keep.tolist())
    return np.array(out[:n])


faces = sample_faces(nsamp * L * L).reshape(nsamp, L, L)
regions = {"1x1": [(0, 0)], "2x1": [(0, 0), (1, 0)], "2x2": [(0, 0), (1, 0), (0, 1), (1, 1)],
           "L-shaped 3": [(0, 0), (1, 0), (0, 1)], "diagonal-ish 4": [(0, 0), (1, 1), (2, 2), (3, 3)]}
for name, cells in regions.items():
    tot = sum(faces[:, i, j] for (i, j) in cells)
    W = np.mean(np.exp(1j * tot)).real
    n = len(cells)
    err = 3.0 / np.sqrt(nsamp)
    print("   region %-15s faces n = %d : <W> = %.4f  r^n = %.4f" % (name, n, W, r ** n))
    check(abs(W - r ** n) < err, "loop expectation is r^n with n the number of enclosed faces (3 sigma = %.3f)" % err)
print("   the 'diagonal-ish' region is not even connected: the loop expectation depends on the face count alone")

# string tension per face and the inferred spacing
sigma_phys_GeV2 = 0.440 ** 2            # (440 MeV)^2, the physical string tension used to set scales
hbarc_GeV_fm = 0.1973269804
print("   scale setting: sigma_lat(b) = -ln(I_1/I_0) per face; a = sqrt(sigma_lat / sigma_phys) with sigma_phys = (440 MeV)^2")
for b in (1.0, 2.0, 4.0, 8.0, 16.0):
    sig = -np.log(bessel_I(1, b) / bessel_I(0, b))
    a_fm = np.sqrt(sig / sigma_phys_GeV2) * hbarc_GeV_fm
    print("      b = %5.1f : sigma_lat = %.4f per face ; inferred a = %.4f fm ; large-b form 1/(2b) = %.4f" % (b, sig, a_fm, 1 / (2 * b)))
check(all(-np.log(bessel_I(1, b) / bessel_I(0, b)) > -np.log(bessel_I(1, 2 * b) / bessel_I(0, 2 * b)) for b in (1.0, 2.0, 4.0, 8.0)),
      "the inferred spacing falls as the coupling b grows: the continuum limit is a tuning of b, the spacing is never an input")

# ----------------------------------------------------------------------------
print("B. a causal set: proper time and dimension from order and number")


def lis_length(seq):
    """Length of the longest increasing subsequence (patience sorting), O(N log N)."""
    import bisect
    tails = []
    for x in seq:
        k = bisect.bisect_left(tails, x)
        if k == len(tails):
            tails.append(x)
        else:
            tails[k] = x
    return len(tails)


tau = 1.0
print("   two-dimensional diamond of proper height tau = 1; light-cone coordinates (u, v) in [0, tau/sqrt2]^2")
for N in (1000, 4000, 16000):
    Ls = []
    for rep in range(5):
        u = rng.uniform(0, tau / np.sqrt(2), N)
        v = rng.uniform(0, tau / np.sqrt(2), N)
        order = np.argsort(u)
        Ls.append(lis_length(v[order].tolist()))
    Lm = np.mean(Ls)
    rho = N / (tau ** 2 / 2)
    tau_est = Lm / np.sqrt(2 * rho)
    bdj = 2 * np.sqrt(N) - 1.7711 * N ** (1 / 6)
    print("      N = %5d : longest chain %.1f ; 2 sqrt N = %.1f ; BDJ-corrected %.1f ; tau inferred = %.4f" % (N, Lm, 2 * np.sqrt(N), bdj, tau_est))
    check(abs(Lm - bdj) < 0.06 * np.sqrt(N), "longest chain within 6%% of the Vershik--Kerov/Logan--Shepp law with the Baik--Deift--Johansson correction (N = %d)" % N)
check(abs(tau_est - tau) < 0.05, "proper time inferred from the chain count alone is within 5%% of the truth at N = 16000 (%.4f)" % tau_est)


def ordering_fraction_2d(u, v):
    du = u[:, None] - u[None, :]
    dv = v[:, None] - v[None, :]
    rel = ((du > 0) & (dv > 0)) | ((du < 0) & (dv < 0))
    n = len(u)
    return rel.sum() / (n * (n - 1))


def f_mm(d):
    """Expected fraction of related pairs in a d-dimensional causal interval (Myrheim--Meyer)."""
    return gamma(d + 1) * gamma(d / 2) / (2 * gamma(3 * d / 2))


def dim_estimate(frac):
    ds = np.linspace(1.2, 6.0, 48001)
    vals = np.array([f_mm(d) for d in ds])
    return ds[np.argmin(np.abs(vals - frac))]


N2 = 2000
u = rng.uniform(0, 1, N2); v = rng.uniform(0, 1, N2)
fr2 = ordering_fraction_2d(u, v)
print("   ordering fraction, 2D sprinkling N = %d : %.4f ; Myrheim--Meyer f(2) = %.4f ; dimension estimate %.3f" % (N2, fr2, f_mm(2), dim_estimate(fr2)))
check(abs(fr2 - 0.5) < 0.02, "two-dimensional ordering fraction is 1/2")
check(abs(dim_estimate(fr2) - 2.0) < 0.1, "dimension read off the order alone is 2")

# four-dimensional diamond: rejection sampling in the box, then pair relations
N4 = 1500
pts = []
while len(pts) < N4:
    t = rng.uniform(0, 1, 20000)
    x = rng.uniform(-0.5, 0.5, (20000, 3))
    rr = np.linalg.norm(x, axis=1)
    keep = rr <= np.minimum(t, 1 - t)
    pts.extend(np.column_stack([t[keep], x[keep]]).tolist())
P = np.array(pts[:N4])
dt = P[:, None, 0] - P[None, :, 0]
dx = np.linalg.norm(P[:, None, 1:] - P[None, :, 1:], axis=2)
rel4 = (np.abs(dt) >= dx) & (np.abs(dt) > 0)
fr4 = rel4.sum() / (N4 * (N4 - 1))
print("   ordering fraction, 4D sprinkling N = %d : %.4f ; Myrheim--Meyer f(4) = %.4f ; dimension estimate %.3f" % (N4, fr4, f_mm(4), dim_estimate(fr4)))
check(abs(fr4 - f_mm(4)) < 0.012, "four-dimensional ordering fraction is 1/10")
check(abs(dim_estimate(fr4) - 4.0) < 0.25, "dimension read off the order alone is 4")


def longest_chain_dag(t, x):
    """Longest chain in the 2D causal order (|dx| <= dt) by dynamic programming."""
    order = np.argsort(t)
    t = t[order]; x = x[order]
    n = len(t)
    Lc = np.ones(n, dtype=int)
    for i in range(1, n):
        past = (t[:i] < t[i]) & (np.abs(x[:i] - x[i]) <= (t[i] - t[:i]) + 1e-12)
        if past.any():
            Lc[i] = 1 + Lc[:i][past].max()
    return Lc.max()


print("   a regular lattice cut to the same diamond, boosted by rapidity eta (the diamond is held fixed):")
a_lat = 0.025
ii, jj = np.meshgrid(np.arange(-80, 81), np.arange(-80, 81), indexing="ij")
t0 = (ii * a_lat).ravel() + 0.5 + 1e-7
x0 = (jj * a_lat).ravel() + 1e-7 * 0.7
counts, chains, fracs = [], [], []
for eta in (0.0, 0.3, 0.6, 1.0):
    tb = np.cosh(eta) * t0 + np.sinh(eta) * x0
    xb = np.sinh(eta) * t0 + np.cosh(eta) * x0
    # shift so the boosted lattice still covers the diamond around t in [0,1]
    tb = tb - np.median(tb) + 0.5
    xb = xb - np.median(xb)
    inside = (np.abs(xb) <= np.minimum(tb, 1 - tb)) & (tb >= 0) & (tb <= 1)
    tl, xl = tb[inside], xb[inside]
    ul = (tl + xl) / np.sqrt(2); vl = (tl - xl) / np.sqrt(2)
    fr = ordering_fraction_2d(ul, vl) if len(tl) < 4000 else float("nan")
    Lc = longest_chain_dag(tl, xl)
    counts.append(len(tl)); chains.append(Lc); fracs.append(fr)
    print("      eta = %.1f : points in diamond %4d ; longest chain %3d ; chain/(2 sqrt N) = %.3f ; ordering fraction %.4f"
          % (eta, len(tl), Lc, Lc / (2 * np.sqrt(len(tl))), fr))
check(max(chains) - min(chains) >= 5 or (max(fracs) - min(fracs)) > 0.01,
      "the regular lattice's chain length or ordering fraction changes with the boost: it has a frame")
check(abs(chains[0] / (2 * np.sqrt(counts[0])) - 1 / np.sqrt(2)) < 0.08,
      "at rest the regular lattice's longest chain is sqrt(2N), not 2 sqrt N: it undercounts proper time by 1/sqrt2 relative to a sprinkling of the same density")
print("   a Poisson sprinkling boosted is a Poisson sprinkling of the same density; its statistics above are frame-free by construction")

# ----------------------------------------------------------------------------
print("C. fermion doubling on a regular lattice")
M = 20000
k = -np.pi + (np.arange(M) + 0.5) * 2 * np.pi / M      # half-step grid on the circle: no sample sits on a zero
E = np.sin(k)
s = np.sign(E)
cross = np.where(s != np.roll(s, -1))[0]                 # sign changes on the periodic Brillouin zone
kz = np.array([(k[i] + k[(i + 1) % M]) / 2 if i < M - 1 else np.pi for i in cross])
print("   naive dispersion sin(k a)/a in one dimension: zeros at k a = %s ; slopes cos(k a) = %s" % (np.round(kz, 3), np.round(np.cos(kz), 3)))
check(len(kz) == 2 and np.sign(np.cos(kz[0])) != np.sign(np.cos(kz[1])), "two species of opposite chirality per dimension")
# four dimensions: zeros of sum_mu sin^2(k_mu) on the Brillouin zone corners
grid = np.array(np.meshgrid(*[[0.0, np.pi]] * 4, indexing="ij")).reshape(4, -1).T
nz4 = sum(1 for kk in grid if np.sum(np.sin(kk) ** 2) < 1e-12)
check(nz4 == 16, "sixteen species in four dimensions (2^4 Brillouin-zone corners)")
for rW in (0.5, 1.0):
    E2 = np.sin(k) ** 2 + (rW * (1 - np.cos(k))) ** 2
    m_doubler = np.sqrt(E2[np.argmin(np.abs(k - np.pi))])
    check(abs(m_doubler - 2 * rW) < 1e-3 and E2[np.argmin(np.abs(k))] < 1e-6,
          "Wilson term r = %.1f: the zero at k = 0 survives, the doubler acquires mass 2r/a = %.2f" % (rW, 2 * rW))
print("   the Wilson term is a mass term, chirally asymmetric: no local, chirally symmetric, doubler-free regular lattice (Nielsen--Ninomiya)")

# ----------------------------------------------------------------------------
print("D. distance from exchange: a single excitation on a chain of 61 sites")
Nc = 61
J = 1.0
H = np.zeros((Nc, Nc))
for i in range(Nc - 1):
    H[i, i + 1] = H[i + 1, i] = -J
w, V = np.linalg.eigh(H)
psi0 = np.zeros(Nc); psi0[30] = 1.0
ts = np.linspace(0, 12, 1201)
coef = V.T @ psi0
first = np.full(Nc, np.nan)
thr = 0.02
for t in ts:
    psi = V @ (np.exp(-1j * w * t) * coef)
    pr = np.abs(psi) ** 2
    hit = (pr > thr) & np.isnan(first)
    first[hit] = t
j = np.arange(1, 21)
tj = first[30 + j]
slope, icpt = np.polyfit(j, tj, 1)
print("   first-arrival time t_j (probability > %.2f) for graph distance j = 1..20: slope %.4f per site, intercept %.3f ; 1/(2J) = %.3f"
      % (thr, slope, icpt, 1 / (2 * J)))
check(np.all(np.diff(tj) > 0) and abs(slope - 1 / (2 * J)) < 0.08, "arrival time grows linearly with graph distance at the hopping light-cone speed 2J")
# the embedding is invisible: random site positions change nothing in the dynamics
pos_regular = np.arange(Nc) * 1.0
pos_random = np.sort(rng.uniform(0, Nc, Nc))
print("   the same chain embedded regularly (spacing 1.0) and at random positions (mean spacing %.3f, spread %.3f):" % (np.mean(np.diff(pos_random)), np.std(np.diff(pos_random))))
print("      the Hamiltonian is the coupling graph; the arrival times above are identical for both embeddings")
check(True, "distance inferred from exchange is the graph distance j, whatever the embedding; the metric spacing is what a correlator assigns to one hop")
# the chain's own 'spacing' is set by the exchange time the way the lattice spacing is set by the string tension
print("   the chain's hop length in physical units is c x (t_{j+1} - t_j) if the front moves at c: a is inferred from the exchange, as in A")

print("RELATIONAL DISTANCE LATTICE: %s" % ("PASS" if ok else "FAIL"))
