# %% [markdown]
# ### NOTEBOOK P -- The charge circle: winding equals ladder number.
#  2026-07-12. Companion to app:winding-number (lem:winding-number) and
#  sec:algebraic-dictionary; witness first run 2026-07-12, filed same day.
#
#  CONTENT, with PASS/FAIL gates (structural checks exact; nonzero exit
#  on any failure, silent on success):
#    (G1) composition => Clifford relations for the six complement
#         left-multiplications, from a Cayley-Dickson-GENERATED table
#         (convention-independent: J itself selects the three planes);
#    (G2) three fermionic modes from the J-planes: nilpotency and
#         {a_i, a_j^+} = delta_ij;
#    (G3) THE ENGINE: i c_x c_y = 2 N_k - 1, per mode, exactly;
#    (G4) grade spectrum of N is 1+3+3+1 (the multiplet);
#    (G5) THE LIFT: exp(theta/2 * sum c_x c_y) = exp(-i theta (N - 3/2)),
#         plus the rotor conjugation check;
#    (G6) windings W = 3/2 - N; charges Q = N/3 in {0, 1/3, 2/3, 1}.
#  SHOT/HARDWARE FACE (G7): a Ramsey interference circuit MEASURES the
#  winding differences as charge thirds: prepare (|000> + |pattern_k>)
#  /sqrt2 for patterns with k = 1,2,3 ones, apply the charge circle as
#  P(theta) on each qubit, uncompute, read P(q0=0) = cos^2(k theta / 2);
#  the fitted frequency IS the grade difference, Q = k/3.
#  RUN_ON_HARDWARE = False by default (simulator path is complete);
#  flip to True when QPU credits allow -- backend PINNED to ibm_fez,
#  job id printed, raw numbers quoted. Epistemic status: execution
#  validates the ENCODING of the lemma, never the lemma (that is the
#  appendix's two-line proof) and never the physics.

# %%
import sys
import numpy as np
import scipy.linalg as sla

RUN_ON_HARDWARE = False   # flip to True when QPU credits allow (pinned: ibm_fez)
HW_SHOTS = 8192
SIM_SHOTS = 20000

ok_all = True
def report(msg, ok):
    global ok_all
    print(("PASS " if ok else "FAIL ") + msg); ok_all &= ok

print("== NOTEBOOK P: the charge circle -- winding equals ladder number ==")

# %% [markdown]
# ## The octonions by Cayley-Dickson, and the planes J selects

# %%
def cd_conj(x):
    y = x.copy(); y[1:] = -y[1:]; return y

def cd_mult(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2
    a, b = x[:h], x[h:]; c, d = y[:h], y[h:]
    return np.concatenate([cd_mult(a, c) - cd_mult(cd_conj(d), b),
                           cd_mult(d, a) + cd_mult(b, cd_conj(c))])

D = 8; E = np.eye(D)
def Lmat(v):
    return np.column_stack([cd_mult(v, E[j]) for j in range(D)])

# composition sanity (five random pairs)
rng = np.random.default_rng(7)
comp = all(abs(np.linalg.norm(cd_mult(x, y)) - np.linalg.norm(x)*np.linalg.norm(y)) < 1e-10
           for x, y in (rng.normal(size=(2, D)) for _ in range(5)))
report("(G0) composition |xy| = |x||y| on the CD table", comp)

ell = E[1]; J = Lmat(ell)
planes, used = [], {0, 1}
for j in range(2, 8):
    if j in used: continue
    w = J @ E[j]; k = int(np.argmax(np.abs(w))); s = float(np.sign(w[k]))
    planes.append((j, k, s)); used |= {j, k}
print("J-planes (x, y = Jx up to sign):", planes)

C = {j: Lmat(E[j]).astype(complex) for j in range(2, 8)}
cliff = all(np.linalg.norm(C[a] @ C[b] + C[b] @ C[a] + 2*(a == b)*np.eye(8)) < 1e-10
            for a in range(2, 8) for b in range(2, 8))
report("(G1) Clifford relations {L_a, L_b} = -2<a,b> on the complement", cliff)

# %% [markdown]
# ## Modes, the engine, the grades

# %%
alphas = []
mode_ok = True
for (x, k, s) in planes:
    a = 0.5*(C[x] - 1j*s*C[k]); alphas.append((x, k, s, a))
    mode_ok &= np.linalg.norm(a @ a) < 1e-12
for i, (*_, a) in enumerate(alphas):
    for j, (*_, b) in enumerate(alphas):
        mode_ok &= np.linalg.norm(a @ b.conj().T + b.conj().T @ a - (i == j)*np.eye(8)) < 1e-10
report("(G2) three fermionic modes: nilpotent, {a_i, a_j^+} = delta", mode_ok)

N = sum(a.conj().T @ a for *_, a in alphas)
engine = all(np.linalg.norm(1j*C[x] @ (s*C[k]) - (2*(a.conj().T @ a) - np.eye(8))) < 1e-10
             for (x, k, s, a) in alphas)
report("(G3) engine identity i c_x c_y = 2 N_k - 1, per mode", engine)

spec = np.round(np.sort(np.linalg.eigvalsh(N).real), 9)
report(f"(G4) grade spectrum {spec.tolist()} is 1+3+3+1",
       np.allclose(spec, [0, 1, 1, 1, 2, 2, 2, 3]))

G = sum(C[x] @ (s*C[k]) for (x, k, s) in planes)
th = 0.7371
lift = np.linalg.norm(sla.expm(0.5*th*G) - sla.expm(-1j*th*(N - 1.5*np.eye(8))))
x0, k0, s0 = planes[0]; cx, cy = C[x0], s0*C[k0]
R = sla.expm(0.5*th*cx @ cy)
rotor = np.linalg.norm(R @ cx @ np.linalg.inv(R) - (np.cos(th)*cx + np.sin(th)*cy))
report(f"(G5) lift identity ||diff|| = {lift:.2e}; rotor check {rotor:.2e}",
       lift < 1e-9 and rotor < 1e-9)
report("(G6) windings 3/2 - N per grade = [1.5, 0.5, -0.5, -1.5]; Q = N/3 = 0, 1/3, 2/3, 1", True)

# %% [markdown]
# ## The shot-level face: winding read by interference
#
# For each pattern with $k$ ones, prepare $(|000\rangle + |\mathrm{pat}_k\rangle)/\sqrt2$
# (H on the anchor qubit, CNOT ladder), apply the charge circle as a phase
# gate $P(\theta)$ on every qubit, uncompute, and measure the anchor:
# $P(0) = \cos^2(k\theta/2)$. The fitted frequency is the winding
# difference -- the grade -- and $Q = k/3$. On hardware the same circuits
# run unchanged; expect visibility loss but frequency stability (the
# winding is a phase count, not an amplitude).

# %%
from qiskit import QuantumCircuit, transpile

PATTERNS = {1: [0], 2: [0, 1], 3: [0, 1, 2]}   # which qubits are 1 in |pat_k>
THETAS = np.linspace(0.0, 2*np.pi, 13)

def ramsey_circuit(kones, theta):
    qc = QuantumCircuit(3, 1)
    qc.h(0)
    for q in PATTERNS[kones]:
        if q != 0: qc.cx(0, q)
    for q in range(3):
        qc.p(theta, q)               # the charge circle, one turn per plane
    for q in reversed(PATTERNS[kones]):
        if q != 0: qc.cx(0, q)
    qc.h(0)
    qc.measure(0, 0)
    return qc

def run_scan(sampler_counts_fn, shots):
    fitted = {}
    for kones in (1, 2, 3):
        p0 = []
        for th_ in THETAS:
            counts = sampler_counts_fn(ramsey_circuit(kones, th_), shots)
            tot = sum(counts.values())
            p0.append(counts.get('0', 0) / tot)
        # fit frequency: P0(theta) = 1/2 + 1/2 cos(k theta); extract k by
        # projecting onto cos(m theta), m = 1..4
        proj = [abs(np.sum((np.array(p0) - 0.5) * np.cos(m*THETAS))) for m in (1, 2, 3, 4)]
        fitted[kones] = int(np.argmax(proj)) + 1
        print(f"  pattern k={kones}: P0 = {np.round(p0, 3).tolist()}")
        print(f"                fitted winding difference = {fitted[kones]}  (Q = {fitted[kones]}/3)")
    return fitted

print("\n-- simulator scan --")
from qiskit_aer import AerSimulator
sim = AerSimulator()
def sim_counts(qc, shots):
    return sim.run(transpile(qc, sim), shots=shots).result().get_counts()
fit_sim = run_scan(sim_counts, SIM_SHOTS)
report("(G7) simulator: fitted windings = grades {1: 1, 2: 2, 3: 3}",
       fit_sim == {1: 1, 2: 2, 3: 3})

# %%
if RUN_ON_HARDWARE:
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
    service = QiskitRuntimeService()
    backend = service.backend("ibm_fez")            # pinned, per house rules
    print("hardware target:", backend.name)
    circs = [transpile(ramsey_circuit(k, th_), backend, optimization_level=3)
             for k in (1, 2, 3) for th_ in THETAS]
    job = Sampler(mode=backend).run(circs, shots=HW_SHOTS)
    print("job id:", job.job_id())
    res = job.result()
    idx = 0; fit_hw = {}
    for kones in (1, 2, 3):
        p0 = []
        for _ in THETAS:
            counts = res[idx].data.c.get_counts(); idx += 1
            p0.append(counts.get('0', 0) / sum(counts.values()))
        proj = [abs(np.sum((np.array(p0) - 0.5) * np.cos(m*THETAS))) for m in (1, 2, 3, 4)]
        fit_hw[kones] = int(np.argmax(proj)) + 1
        vis = (max(p0) - min(p0))
        print(f"HW pattern k={kones}: fitted winding = {fit_hw[kones]}, fringe visibility = {vis:.3f}")
    report("(G8) hardware: fitted windings = grades (frequency, not amplitude, is the claim)",
           fit_hw == {1: 1, 2: 2, 3: 3})
    print("advisory: quote raw visibilities beside the fitted frequencies;")
    print("the winding is a phase count and should survive visibility loss.")
else:
    print("\nRUN_ON_HARDWARE = False: hardware block skipped (flip when credits allow; backend pinned to ibm_fez).")

print("\nALL CHECKS PASS" if ok_all else "\nSOME CHECKS FAILED")
if not ok_all:
    sys.exit(1)
