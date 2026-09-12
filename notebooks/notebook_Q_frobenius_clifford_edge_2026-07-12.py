# %% [markdown]
# ### NOTEBOOK Q -- The Frobenius--Clifford edge (the triangle witness).
#  2026-07-12. Companion to open_problem_hopf_frobenius_v2 (sections
#  3.1-3.6) and sec:algebraic-dictionary; witness first run 2026-07-12,
#  filed same day.
#
#  CONTENT, with PASS/FAIL gates (nonzero exit on any failure):
#    (G1) GHZ tensor + diagonal cap: associative, unit (1,1), two
#         orthogonal idempotents, loop m.delta = identity -- the algebra
#         is C (+) C, semisimple: the SPECIAL side, exactly;
#    (G2) W tensor + antidiagonal cap: associative, unit |0>, nilpotent
#         |1> with |1>^2 = 0 -- the algebra is the dual numbers
#         C[x]/(x^2) = Lambda(C): the one-mode GRASSMANN algebra;
#    (G3) the anti-special loop IS occupation: m.delta = 2 N_1; and the
#         spectral chain to Clifford: eig(loop) + (-1) = eig(i c_x c_y)
#         with the multiplicity pattern of the module (notebook P's
#         engine, met from the categorical side);
#    (G4) the exponential keystone: (dual numbers)^{graded tensor 3}
#         equals Lambda(C^3), all 64 basis products, Koszul signs exact;
#    (G5) strong complementarity <=> anticommutation <=> mutual
#         unbiasedness on the qubit, with a deliberately failing
#         intermediate angle.
#  SHOT/HARDWARE FACE (G6): Grassmann nilpotency as a count distribution
#  -- the contracted W-pair's forbidden single-excitation weight (the
#  anti-speciality circuit of the composition-laws family, recaptioned:
#  x^2 = 0 on a device). RUN_ON_HARDWARE = False by default; flip when
#  QPU credits allow -- backend PINNED to ibm_fez, job id printed, raw
#  beside derived. Epistemic status: execution validates the ENCODING,
#  never the classification (that is two lines of algebra) and never
#  the conjecture.

# %%
import sys
import numpy as np
from itertools import product

RUN_ON_HARDWARE = False   # flip to True when QPU credits allow (pinned: ibm_fez)
HW_SHOTS = 8192
SIM_SHOTS = 8192

ok_all = True
def report(msg, ok):
    global ok_all
    print(("PASS " if ok else "FAIL ") + msg); ok_all &= ok

print("== NOTEBOOK Q: the Frobenius--Clifford edge ==")

# %% [markdown]
# ## The two induced algebras

# %%
def induced(T, G):
    m = np.einsum('ijl,lk->ijk', T, G)
    A = np.einsum('ijp,pkq->ijkq', m, m); B = np.einsum('jkp,ipq->ijkq', m, m)
    gap = np.linalg.norm(A - B)
    unit = None
    for u in (np.array(v, float) for v in ((1, 0), (0, 1), (1, 1))):
        if np.allclose(np.einsum('i,ijk->jk', u, m), np.eye(2)) and \
           np.allclose(np.einsum('j,ijk->ik', u, m), np.eye(2)):
            unit = u; break
    return m, unit, gap

GHZ = np.zeros((2, 2, 2)); GHZ[0, 0, 0] = GHZ[1, 1, 1] = 1
W   = np.zeros((2, 2, 2)); W[0, 0, 1] = W[0, 1, 0] = W[1, 0, 0] = 1
DIAG, ANTI = np.eye(2), np.array([[0., 1.], [1., 0.]])

def loop_of(T, G, m):
    delta = np.einsum('abl,ai,bj,lk->kij', T, G, G, G)
    return np.einsum('kij,ijp->kp', delta, m)

m_g, u_g, gap_g = induced(GHZ, DIAG)
e0, e1 = np.eye(2)
idem = np.allclose(np.einsum('i,j,ijk->k', e0, e0, m_g), e0) and \
       np.allclose(np.einsum('i,j,ijk->k', e1, e1, m_g), e1) and \
       np.allclose(np.einsum('i,j,ijk->k', e0, e1, m_g), 0)
loop_g = loop_of(GHZ, DIAG, m_g)
report(f"(G1) GHZ+diag: assoc gap {gap_g:.1e}, unit {u_g}, two orthogonal idempotents, "
       f"loop = {np.round(loop_g, 6).tolist()} = id  (SPECIAL; algebra = C (+) C)",
       gap_g < 1e-12 and u_g is not None and np.allclose(u_g, (1, 1)) and idem
       and np.allclose(loop_g, np.eye(2)))

m_w, u_w, gap_w = induced(W, ANTI)
nilp = np.allclose(np.einsum('i,j,ijk->k', e1, e1, m_w), 0)
loop_w = loop_of(W, ANTI, m_w)
N1 = np.diag([0., 1.])
report(f"(G2) W+antidiag: assoc gap {gap_w:.1e}, unit {u_w} = |0>, |1>^2 = 0 "
       f"(algebra = dual numbers C[x]/(x^2) = one-mode Grassmann)",
       gap_w < 1e-12 and u_w is not None and np.allclose(u_w, (1, 0)) and nilp)
report(f"(G3a) the anti-special loop IS occupation: m.delta = {np.round(loop_w, 6).tolist()} = 2 N_1",
       np.allclose(loop_w, 2*N1))

# spectral chain to the Clifford engine (module side, from the CD table)
def cd_conj(x): y = x.copy(); y[1:] = -y[1:]; return y
def cd_mult(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b = x[:h], x[h:]; c, d = y[:h], y[h:]
    return np.concatenate([cd_mult(a, c) - cd_mult(cd_conj(d), b),
                           cd_mult(d, a) + cd_mult(b, cd_conj(c))])
E8 = np.eye(8)
def Lm(v): return np.column_stack([cd_mult(v, E8[j]) for j in range(8)])
Jm = Lm(E8[1]); w2 = Jm @ E8[2]; k2 = int(np.argmax(np.abs(w2))); s2 = float(np.sign(w2[k2]))
bil = 1j * Lm(E8[2]).astype(complex) @ (s2 * Lm(E8[k2]).astype(complex))
eig_loop = sorted(np.round(np.linalg.eigvalsh(loop_w).real, 9))          # [0, 2]
eig_bil = sorted(np.round(np.linalg.eigvalsh(bil).real, 9))              # [-1 x4, +1 x4]
report(f"(G3b) spectral chain: eig(loop) - 1 = {[v-1 for v in eig_loop]} matches "
       f"eig(i c_x c_y) values {sorted(set(eig_bil))} at multiplicity 4 per value "
       f"(the mode's two levels, tensored through the module)",
       [v - 1 for v in eig_loop] == [-1.0, 1.0] and eig_bil == [-1.0]*4 + [1.0]*4)

# %% [markdown]
# ## The exponential keystone and complementarity

# %%
def dual_mult(p, q):
    if p == 0: return (1, q)
    if q == 0: return (1, p)
    return None

def cube_mult(P, Q):
    coeff = 1
    for k in range(3):
        coeff *= (-1) ** (sum(P[j] for j in range(k + 1, 3)) * Q[k])
    out = []
    for k in range(3):
        r = dual_mult(P[k], Q[k])
        if r is None: return None
        coeff *= r[0]; out.append(r[1])
    return (coeff, tuple(out))

def wedge(S, T):
    if set(S) & set(T): return None
    arr = list(S) + list(T); sign = 1
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]: arr[i], arr[j] = arr[j], arr[i]; sign = -sign
    return (sign, tuple(arr))

koszul = True; checked = 0
for P in product((0, 1), repeat=3):
    for Q in product((0, 1), repeat=3):
        c = cube_mult(P, Q)
        w = wedge(tuple(i for i in range(3) if P[i]), tuple(i for i in range(3) if Q[i]))
        if (c is None) != (w is None): koszul = False
        elif c is not None:
            koszul &= (tuple(i for i in range(3) if c[1][i]) == w[1] and c[0] == w[0])
        checked += 1
report(f"(G4) (dual numbers)^(graded tensor 3) = Lambda(C^3): {checked}/64 basis "
       f"products, Koszul signs exact", koszul and checked == 64)

Z = np.diag([1., -1.]); X = np.array([[0., 1.], [1., 0.]])
def mub(A, B):
    _, Ua = np.linalg.eigh(A); _, Ub = np.linalg.eigh(B)
    return np.allclose(np.abs(Ua.conj().T @ Ub) ** 2, 0.5)
pairs = [("Z,X", Z, X, True), ("Z,Z", Z, Z, False),
         ("Z,(X+Z)/sqrt2", Z, (X + Z)/np.sqrt(2), False)]
comp_ok = True
for nm, A, B, expect in pairs:
    ac = np.allclose(A @ B + B @ A, 0); ub = mub(A, B)
    print(f"   {nm}: anticommute = {ac}, mutually unbiased = {ub}")
    comp_ok &= (ac == ub == expect)
report("(G5) complementarity <=> anticommutation <=> unbiasedness (incl. failing angle)", comp_ok)

# %% [markdown]
# ## The shot-level face: Grassmann nilpotency as a count distribution
#
# Two W triples, inner endpoints contracted by a Bell cap (postselect 00):
# the output has ZERO weight on the single-excitation strings of $W_4$ --
# anti-speciality, which (G2) identifies as $x^2 = 0$. The forbidden
# weight is the witness; ideal 0, unmitigated hardware sits at the
# single-bit-flip floor (the June record: 7.6% marrakesh, 7.2% kingston).

# %%
from qiskit import QuantumCircuit, transpile
Wvec = np.zeros(8, complex); Wvec[0b001] = Wvec[0b010] = Wvec[0b100] = 1/np.sqrt(3)

def w_contraction_circuit():
    qc = QuantumCircuit(6)
    qc.prepare_state(Wvec, [0, 1, 2]); qc.prepare_state(Wvec, [3, 4, 5])
    qc.cx(2, 3); qc.h(2)               # Bell cap on (q2, q3): postselect 00
    qc.measure_all()
    return qc

def forbidden_weight(counts):
    pc, kept = {}, 0
    for b, c in counts.items():
        if b[-3] == '1' or b[-4] == '1': continue     # cap qubits q2, q3
        kept += c
        key = ''.join(b[-1 - q] for q in (5, 4, 1, 0))
        pc[key] = pc.get(key, 0) + c
    single = sum(v for k, v in pc.items() if k.count('1') == 1)
    return single / kept, kept, pc

from qiskit_aer import AerSimulator
sim = AerSimulator()
counts = sim.run(transpile(w_contraction_circuit(), sim), shots=SIM_SHOTS).result().get_counts()
fw, kept, _ = forbidden_weight(counts)
report(f"(G6) simulator: forbidden single-excitation weight = {fw:.4f} on "
       f"{kept} postselected shots (x^2 = 0 as counts)", fw < 0.01)

if RUN_ON_HARDWARE:
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
    service = QiskitRuntimeService()
    backend = service.backend("ibm_fez")             # pinned, per house rules
    print("hardware target:", backend.name)
    isa = transpile(w_contraction_circuit(), backend, optimization_level=3)
    job = Sampler(mode=backend).run([isa], shots=HW_SHOTS)
    print("job id:", job.job_id())
    counts = job.result()[0].data.meas.get_counts()
    fw_hw, kept_hw, pc_hw = forbidden_weight(counts)
    print(f"HARDWARE: forbidden weight = {fw_hw:.4f} raw, {kept_hw} postselected shots "
          f"(June floor: 0.072-0.076 unmitigated); distribution: "
          f"{ {k: round(v/kept_hw, 3) for k, v in sorted(pc_hw.items())} }")
    report("(G7) hardware: forbidden weight below 0.12 unmitigated advisory", fw_hw < 0.12)
else:
    print("\nRUN_ON_HARDWARE = False: hardware block skipped (flip when credits allow; backend pinned to ibm_fez).")

print("\nALL CHECKS PASS" if ok_all else "\nSOME CHECKS FAILED")
if not ok_all:
    sys.exit(1)
