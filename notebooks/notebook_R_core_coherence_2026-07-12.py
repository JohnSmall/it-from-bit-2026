# %% [markdown]
# ### NOTEBOOK R -- Family-2 landscape: the core-coherence obstruction.
#  2026-07-12. Successor to notebook N (whose registered family was
#  refuted by the annihilation lemma). R's shape differs by an honesty
#  constraint stated openly: N's PUBLISHED diagnostics (control-B's
#  c2 = -3.0000, overlap 1/2) permit the family-2 landscape to be
#  decomposed analytically BEFORE any run -- so a single-hypothesis
#  gamble would be theatre. R therefore registers a LEMMA with its
#  predictions derived in the registration, verifies it across an
#  enumerated variant set, and registers the conclusion.
#
#  ================= PRE-REGISTRATION =================================
#  LEMMA (core coherence). For the generation unit f1 and the two
#  zero-divisor diagonals z_c = (f1 + u_c)/sqrt2 of N's construction,
#  the excursion image decomposes as
#        L_{z_c} f1 = ( -e0 + u_c f1 ) / sqrt2 ,
#  i.e. HALF into the shared quaternionic core (the -e0/sqrt2 part) and
#  HALF into a single unit of the THIRD sector (u_c f1: the V2-diagonal
#  leaks into V3 and vice versa -- an S3 twist). Consequently, for EVERY
#  coupling built from diagonal images (enumerated below), the two core
#  halves add COHERENTLY and the second-order coefficient is
#        c2 = -( |coherent core|^2 + |sector|^2 + |sector|^2 )
#           = -( 2 + 1/2 + 1/2 ) = -3 ,
#  independent of diagonal signs and mixtures. The -2 that hypothesis H
#  (delta m/m = -2 x 1/9) requires is UNREACHABLE in this family except
#  by hand-orthonormalisation of the channels, which is the tautology
#  control, flagged as such.
#  VARIANTS (counted, five): (a) plain diagonals (z2, z3); (b) conjugate
#  diagonals (zbar_c = (f1 - u_c)/sqrt2); (c) mixed (z2, zbar3);
#  (d) unnormalised images; (e) TAUTOLOGY CONTROL: Gram-Schmidt
#  orthonormalised channels (must give exactly -2, and proves nothing).
#  GATES (counted, seven):
#   G-R0  machinery (sigma etc.) re-derived, as in N.
#   G-R1  image decomposition: each |core part|^2 = 1/2, each sector
#         part a single unit of the THIRD sector, |.|^2 = 1/2.
#   G-R2  overlap <w2, w3> = +1/2 exactly; |sum of images|^2 = 3.
#   G-R3  variants (a)-(d): c2 = -3.000000 +/- 1e-6 (exact extractor).
#   G-R4  tautology control (e): c2 = -2.000000 +/- 1e-6, FLAGGED.
#   G-R5  register face (simulator): two rotations into targets sharing
#         one mode -- t2 = (|01>+|10>)/sqrt2, t3 = (|01>+|11>)/sqrt2,
#         the SPECTATOR |01> playing the tag-blind core -- give survival
#         deficit coefficient c = 3 +/- 0.05 at 200000 shots: the
#         obstruction as a measured number against notebook N's c = 2.
#   G-R6  (hardware, OFF until credits): same scan on ibm_fez, job id
#         printed, advisory c = 3 +/- 0.3 unmitigated.
#  REGISTERED CONCLUSION (if all gates pass): family-2 -- the pure
#  16-dimensional algebra with unit gap -- cannot price the up-quark
#  deficit at -2/9: the shared core is a coherent sink that every
#  diagonal excursion feeds. The ninth-pricing must therefore close on
#  the REGISTER-ALGEBRA COMPOSITE, where the generation label is the
#  tag pair and core motion is TAG-BLIND (the register's own semantics:
#  the spectator state is the semantically empty direction), so only
#  the sector halves can register. That composite family takes the next
#  free letter (S) at its own registration; its numbers are NOT minted
#  here. RUN_ON_HARDWARE = False; backend pinned ibm_fez.
#  ADDENDUM (2026-07-12, first execution): G-R3/G-R4 failed their
#  +/- 1e-6 tolerances on the first run purely through the extractor's
#  O(h^4) truncation at h = 0.02 (error 3.4e-5; every variant read
#  -2.999966). The step is reduced to h = 0.005 (truncation ~1e-7);
#  registered tolerances UNCHANGED, physics untouched.
#  =====================================================================

# %%
import sys
import numpy as np

RUN_ON_HARDWARE = False   # flip when QPU credits allow (pinned: ibm_fez)
HW_SHOTS = 8192

ok_all = True
def report(msg, ok):
    global ok_all
    print(("PASS " if ok else "FAIL ") + msg); ok_all &= ok

print("== NOTEBOOK R: the core-coherence obstruction ==")

# %% [markdown]
# ## Machinery (as notebook N, gated)

# %%
def cd_conj(x): y = x.copy(); y[1:] = -y[1:]; return y
def cd_mult(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b = x[:h], x[h:]; c, d = y[:h], y[h:]
    return np.concatenate([cd_mult(a, c) - cd_mult(cd_conj(d), b),
                           cd_mult(d, a) + cd_mult(b, cd_conj(c))])
D = 16; E = np.eye(D)
def u(i): return E[i].copy()
def Lmat(v): return np.column_stack([cd_mult(v, E[j]) for j in range(D)])

CORE = [0, 4, 8, 12]
V = {1: [1, 5, 9, 13], 2: [2, 6, 10, 14], 3: [3, 7, 11, 15]}
def sector_of(vec, tol=1e-9):
    for name, idx in (("H", CORE), ("V1", V[1]), ("V2", V[2]), ("V3", V[3])):
        if np.linalg.norm(vec - sum(vec[i]*E[i] for i in idx)) < tol:
            return name
    return "mixed"

# sigma per M's recipe: the order-3 automorphism from generators {e4, e8,
# e1, e2} (the e2 seed is essential -- {e1, e4, e8} alone generate only
# O_1 and never reach V2/V3), fixing the core sector and cycling
# V1 -> V2 -> V3. Search basis-signed images with cheap structural
# filters first, the 40-product automorphism test last.
from itertools import product as iproduct

def mul_idx(a, b):
    w = cd_mult(u(a), u(b)); k = int(np.argmax(np.abs(w))); return k, float(np.sign(w[k]))

def build_from_seeds(seeds):
    img = dict(seeds); img[0] = (0, 1.0)
    changed = True
    while changed and len(img) < 16:
        changed = False
        for a in list(img):
            for b in list(img):
                k, s = mul_idx(a, b)
                if k in img: continue
                ia, sa = img[a]; ib, sb = img[b]
                kk, ss = mul_idx(ia, ib)
                img[k] = (kk, s * sa * sb * ss); changed = True
    if len(img) < 16: return None
    if len({ia for ia, _ in img.values()}) < 16: return None
    S = np.zeros((D, D))
    for a, (ia, sa) in img.items(): S[ia, a] = sa
    return S

sigma = None
rng = np.random.default_rng(11)
for i1, s1, i2, s2, i4, s4, i8, s8 in iproduct(V[2], (1., -1.), V[3], (1., -1.),
                                               CORE[1:], (1., -1.), CORE[1:], (1., -1.)):
    if i8 == i4: continue
    S = build_from_seeds({1: (i1, s1), 2: (i2, s2), 4: (i4, s4), 8: (i8, s8)})
    if S is None: continue
    if np.linalg.norm(S @ S @ S - np.eye(D)) > 1e-8: continue
    if not (sector_of(S @ u(1)) == "V2" and sector_of(S @ S @ u(1)) == "V3"
            and sector_of(S @ u(4)) == "H"): continue
    good = all(np.linalg.norm(S @ cd_mult(x, y) - cd_mult(S @ x, S @ y)) < 1e-8
               for x, y in (rng.normal(size=(2, D)) for _ in range(40)))
    if good:
        sigma = S; break

g0 = sigma is not None and np.allclose(sigma.T @ sigma, np.eye(D)) and \
     np.linalg.norm(sigma @ sigma @ sigma - np.eye(D)) < 1e-8
report("(G-R0) sigma re-derived (4-generator seed): order 3, core sector fixed, "
       "V1->V2->V3, isometry, automorphism on 40 random products", bool(g0))
if sigma is None:
    print("machinery failure: no sigma candidate found -- physics gates not run"); sys.exit(1)

# %% [markdown]
# ## The lemma, gated

# %%
f1 = u(1)
w = cd_mult(u(8), f1)
u2 = sigma @ w; u2 /= np.linalg.norm(u2)
u3 = sigma @ sigma @ w; u3 /= np.linalg.norm(u3)
z2 = (f1 + u2) / np.sqrt(2); z3 = (f1 + u3) / np.sqrt(2)
zb2 = (f1 - u2) / np.sqrt(2); zb3 = (f1 - u3) / np.sqrt(2)

def image(zc):
    img = Lmat(zc) @ f1
    core = sum(img[i] * E[i] for i in CORE)
    rest = img - core
    return img, core, rest

g1 = True
sector_targets = {}
for nm, zc, own in (("z2", z2, "V2"), ("z3", z3, "V3")):
    img, core, rest = image(zc)
    kr = int(np.argmax(np.abs(rest)))
    sec = sector_of(rest / np.linalg.norm(rest))
    sector_targets[nm] = sec
    print(f"  {nm}: |core|^2 = {core @ core:.4f}, sector part = single unit e{kr} in {sec}, "
          f"|sector|^2 = {rest @ rest:.4f}")
    g1 &= abs(core @ core - 0.5) < 1e-9 and abs(rest @ rest - 0.5) < 1e-9
third = sector_targets["z2"] == "V3" and sector_targets["z3"] == "V2"
report(f"(G-R1) image decomposition: half core, half a single THIRD-sector unit "
       f"(the S3 twist: {sector_targets})", g1 and third)

i2, _, _ = image(z2); i3, _, _ = image(z3)
w2 = i2 / np.linalg.norm(i2); w3 = i3 / np.linalg.norm(i3)
ov = float(w2 @ w3); ssum = float((i2 + i3) @ (i2 + i3))
report(f"(G-R2) overlap <w2, w3> = {ov:+.6f} (= +1/2); |sum of images|^2 = {ssum:.6f} (= 3)",
       abs(ov - 0.5) < 1e-9 and abs(ssum - 3.0) < 1e-9)

def lam_at(Vop, g):
    wl, Uv = np.linalg.eigh(np.eye(D) - np.outer(f1, f1) + g * Vop)
    j = int(np.argmax(np.abs(Uv.T @ f1)))
    return wl[j]

def c2_of(Vop, h=0.005):
    lm2, lm1, l0, lp1, lp2 = (lam_at(Vop, g) for g in (-2*h, -h, 0.0, h, 2*h))
    return (-lp2 + 16*lp1 - 30*l0 + 16*lm1 - lm2) / (12*h*h) / 2.0

def hop(vecs):
    return sum(np.outer(v, f1) + np.outer(f1, v) for v in vecs)

variants = {
    "(a) plain diagonals":     hop([w2, w3]),
    "(b) conjugate diagonals": hop([ (Lmat(zb2) @ f1) / np.linalg.norm(Lmat(zb2) @ f1),
                                     (Lmat(zb3) @ f1) / np.linalg.norm(Lmat(zb3) @ f1) ]),
    "(c) mixed z2, zbar3":     hop([w2, (Lmat(zb3) @ f1) / np.linalg.norm(Lmat(zb3) @ f1)]),
    "(d) unnormalised images": hop([i2, i3]),
}
g3 = True
for nm, Vop in variants.items():
    c2 = c2_of(Vop)
    print(f"  {nm}: c2 = {c2:+.6f}")
    g3 &= abs(c2 + 3.0) < 1e-6
report("(G-R3) every diagonal-image coupling: c2 = -3.000000 (the lemma)", g3)

# tautology control: Gram-Schmidt
e2h = w2.copy()
e3h = w3 - (w3 @ w2) * w2; e3h /= np.linalg.norm(e3h)
c2_t = c2_of(hop([e2h, e3h]))
report(f"(G-R4) TAUTOLOGY control (orthonormalised): c2 = {c2_t:+.6f} = -2 by construction, "
       f"proving nothing", abs(c2_t + 2.0) < 1e-6)

# %% [markdown]
# ## The register face: the obstruction as a measured 3

# %%
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def shared_mode_unitary(theta):
    t2 = np.zeros(4); t2[1] = t2[2] = 1/np.sqrt(2)   # (|01> + |10>)/sqrt2
    t3 = np.zeros(4); t3[1] = t3[3] = 1/np.sqrt(2)   # (|01> + |11>)/sqrt2
    e0 = np.zeros(4); e0[0] = 1.0
    def rot(target, th):
        Umat = np.eye(4)
        a = e0; b = target - (target @ e0) * e0; b /= np.linalg.norm(b)
        P = np.column_stack([a, b])
        R2 = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
        return np.eye(4) + P @ (R2 - np.eye(2)) @ P.T
    return rot(t3, theta) @ rot(t2, theta)

def survival_circuit(theta):
    qc = QuantumCircuit(2)
    qc.unitary(shared_mode_unitary(theta), [0, 1])
    qc.measure_all()
    return qc

sim = AerSimulator()
S2 = np.linspace(0.005, 0.05, 9)
SCAN_SHOTS = 200000
p00 = []
for s2 in S2:
    th = np.arcsin(np.sqrt(s2))
    counts = sim.run(transpile(survival_circuit(th), sim), shots=SCAN_SHOTS).result().get_counts()
    p00.append(counts.get('00', 0) / SCAN_SHOTS)
y = (1.0 - np.array(p00)) / S2
Wt = S2**2
A = np.vstack([np.ones_like(S2), S2]).T
c_est = np.linalg.lstsq(A * Wt[:, None], y * Wt, rcond=None)[0][0]
report(f"(G-R5) register face: shared-mode deficit coefficient c = {c_est:.3f} "
       f"(gate 3 +/- 0.05; notebook N's orthogonal channels gave 2)", abs(c_est - 3.0) <= 0.05)

if RUN_ON_HARDWARE:
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
    service = QiskitRuntimeService()
    backend = service.backend("ibm_fez")            # pinned, per house rules
    print("hardware target:", backend.name)
    circs = [transpile(survival_circuit(np.arcsin(np.sqrt(s2))), backend,
                       optimization_level=3) for s2 in S2]
    job = Sampler(mode=backend).run(circs, shots=HW_SHOTS)
    print("job id:", job.job_id())
    res = job.result()
    p00h = [res[i].data.meas.get_counts().get('00', 0) / HW_SHOTS for i in range(len(S2))]
    yh = (1.0 - np.array(p00h)) / S2
    ch = np.linalg.lstsq(A * Wt[:, None], yh * Wt, rcond=None)[0][0]
    print(f"HW: c = {ch:.3f} raw (advisory 3 +/- 0.3 unmitigated)")
    report("(G-R6) hardware advisory", abs(ch - 3.0) <= 0.3)
else:
    print("\nRUN_ON_HARDWARE = False: hardware block skipped (flip when credits allow; pinned ibm_fez).")

# %%
print()
if ok_all:
    print("VERDICT: the core-coherence LEMMA is ESTABLISHED across the registered variants.")
    print("         Family-2 (the pure 16-dimensional algebra, unit gap) cannot produce the")
    print("         -2 x (1/9) pricing: every diagonal excursion feeds the shared core")
    print("         coherently, c2 = -3 universally, and -2 is reachable only by the flagged")
    print("         tautology. REGISTERED CONCLUSION: the up-quark pricing must close on the")
    print("         register-algebra composite, where core motion is tag-blind (the spectator")
    print("         direction) and only the sector halves can register. That family is")
    print("         notebook S, at its own future registration; its numbers are not minted here.")
else:
    print("VERDICT: gate failure(s) above -- the lemma as registered does not hold; the")
    print("         printed decompositions are the finding.")
if not ok_all:
    sys.exit(1)
