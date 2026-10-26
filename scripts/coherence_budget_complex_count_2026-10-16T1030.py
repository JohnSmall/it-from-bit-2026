#!/usr/bin/env python3
"""
coherence_budget_complex_count_2026-10-16T1030.py

JS's claim of 2026-10-16: Hawking's complex temperature for a closed
timelike curve implies a complex entropy and a region of complex
information; the information an observation adds, closing an apparent
loop, should exactly match the imaginary component of the agent's
pre-FANOUT state of knowledge, leaving a purely real value.

  A  Hawking's count for one qubit loop.  H = X/2, Z(beta) = Tr e^{-beta H}
     = 2 cosh(beta/2).  At imaginary beta = i tau the "partition function" is
     the trace of the loop's unitary: 2 at tau = 0 (identity, the truth-
     teller's loop, two states), 0 at tau = pi (the loop is -iX, the Liar up
     to phase: no states), -2 at tau = 2 pi (the spinor sign: a negative
     count).  The zeros of Z are exactly the Liar loops, and they lie on the
     imaginary axis (Fisher zeros at beta = i pi (2k+1)).  The complex
     "entropy" S = ln Z + beta <H> is tabulated: for two levels it is real
     while Z > 0 (and exceeds ln 2), acquires exactly i pi where Z < 0, and
     is undefined at the zero; three levels make it genuinely complex.
     With the FANOUT inside the
     loop, Tr(CNOT) = 2 against Tr(I_4) = 4: the copy removes one bit of
     loop count; graded, Tr = 2 + 2 cos(theta/2).
  B  The budget identity.  S(Delta_B rho) = S(rho) + C_B(rho) with C_B the
     relative entropy of coherence in the record basis B; along the graded
     copy chain S(Delta_Z rho_N) = H(p) is invariant, so S(rho_N) + C_Z(rho_N)
     = H(p) at every stage: what the records have gained plus the coherence
     left equals the final real value.  The end state is real diagonal.
     C_Z is blind to the relative phase; C_X is not; a record in basis B
     spends the B-coherence.  Under a full CNOT the joint coherence in the
     product basis is unchanged (H(p) before and after): the budget is
     promoted, not destroyed.
  C  Wei--Liu form.  With a complex fragment overlap lambda = cos(theta/2)
     e^{i phi}, the coherence factor is e^{-N (gamma - i phi)}; C_Z depends on
     the real part gamma only.  The coherence is spent by the real part of
     the complex cost, and the imaginary part (the phase) is not spent.
  D  Darwinism at N = 8: S(rho_S) + C_Z(rho_S) = H(p), I(S:F_N) = 2 S(rho_S).

Seed 20261016.  numpy only.  Final line: COHERENCE BUDGET COMPLEX COUNT: PASS.
"""
import numpy as np

SEED = 20261016
rng = np.random.default_rng(SEED)
np.set_printoptions(precision=4, suppress=True, linewidth=120)
FAILS = []


def check(cond, msg):
    tag = "ok  " if cond else "FAIL"
    print(f"  [{tag}] {msg}")
    if not cond:
        FAILS.append(msg)


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
P0 = np.array([[1, 0], [0, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)
k0 = np.array([1, 0], dtype=complex)
k1 = np.array([0, 1], dtype=complex)
kp = (k0 + k1) / np.sqrt(2)
km = (k0 - k1) / np.sqrt(2)


def proj(v):
    return np.outer(v, v.conj())


def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


def rx(theta):
    return np.cos(theta / 2) * I2 - 1j * np.sin(theta / 2) * X


def controlled(G):
    return kron(P0, I2) + kron(P1, G)


CNOT = controlled(X)


def vn(rho):
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    w = w[w > 1e-13]
    return float(-np.sum(w * np.log2(w)))


def h2(p):
    return float(-p * np.log2(p) - (1 - p) * np.log2(1 - p))


def dephase(rho, basis):
    """Delta_B: keep the diagonal in the orthonormal basis given as columns."""
    out = np.zeros_like(rho)
    for j in range(basis.shape[1]):
        v = basis[:, j]
        out += (v.conj() @ rho @ v) * proj(v)
    return out


ZB = np.column_stack([k0, k1])
XB = np.column_stack([kp, km])


def crel(rho, basis):
    return vn(dephase(rho, basis)) - vn(rho)


def reduced(Psi, dims, keep):
    n = len(dims)
    keep = sorted(keep)
    rest = [i for i in range(n) if i not in keep]
    t = Psi.reshape(dims).transpose(keep + rest)
    dk = int(np.prod([dims[i] for i in keep]))
    M = t.reshape(dk, -1)
    return M @ M.conj().T


# ---------------------------------------------------------------------------
print("=" * 72)
print("A  Hawking's count for one qubit loop: Z(beta) = Tr exp(-beta H), H = X/2")
print("=" * 72)
Hm = X / 2


def exp_minus(beta):
    # exp(-beta X/2) = cosh(beta/2) I - sinh(beta/2) X
    return np.cosh(beta / 2) * I2 - np.sinh(beta / 2) * X


def Zf(beta):
    return np.trace(exp_minus(beta))


def Sf(beta):
    # S = ln Z + beta <H>, <H> = -d ln Z / d beta = -(1/2) tanh(beta/2)
    return np.log(2 * np.cosh(beta / 2)) - (beta / 2) * np.tanh(beta / 2)


print("  real beta (an ordinary bath):")
for b in (0.0, 1.0, 4.0):
    print(f"    beta = {b:4.1f}: Z = {Zf(b).real:8.4f}, S = {Sf(b).real:8.4f} nat")
check(abs(Sf(0.0) - np.log(2)) < 1e-12 and Sf(4.0).real < Sf(0.0).real, "real beta: S = ln 2 at infinite temperature and falls as beta grows")
print("  imaginary beta = i tau (Hawking's loop, identified periodically in real time):")
rows = []
for tau in (0.0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi):
    beta = 1j * tau
    U = exp_minus(beta)
    Zc = Zf(beta)
    with np.errstate(divide="ignore", invalid="ignore"):
        Sc = np.log(Zc) - (beta / 2) * np.tanh(beta / 2) if abs(Zc) > 1e-12 else complex(np.nan, np.nan)
    rows.append((tau, Zc, Sc, U))
    print(f"    tau = {tau:6.4f}: Z = Tr U = {Zc.real:+7.4f}{Zc.imag:+.4f}i,  S = {Sc.real:+8.4f}{Sc.imag:+8.4f}i")
check(abs(rows[0][1] - 2) < 1e-12, "tau = 0: the identity loop counts two states (the truth-teller's loop)")
check(abs(rows[2][1]) < 1e-12 and np.allclose(rows[2][3], -1j * X), "tau = pi: Z = 0 and the loop is -iX, the Liar up to phase: no states")
check(abs(rows[4][1] + 2) < 1e-12 and np.allclose(rows[4][3], -I2), "tau = 2 pi: Z = -2, the spinor sign as a negative count")
check(abs(rows[1][2].imag) < 1e-12 and rows[1][2].real > np.log(2),
      "tau = pi/2: for a two-level loop S is real (the i's cancel in beta<H>) and exceeds ln 2: not an entropy")
check(abs(rows[3][2].imag - np.pi) < 1e-12 and abs(rows[4][2].imag - np.pi) < 1e-12,
      "Z < 0: Im S = pi exactly, the anti-event's i pi; for the bit the imaginary part of S is quantised to {0, pi}")


def S_general(E, beta):
    w = np.exp(-beta * np.asarray(E, dtype=complex))
    Zg = np.sum(w)
    return np.log(Zg) + beta * np.sum(np.asarray(E) * w) / Zg


print("  three-level loop, spectrum (0, 1, 3): S at imaginary beta")
imparts = []
for tau in (0.3, 0.7, 1.1):
    Sg = S_general([0.0, 1.0, 3.0], 1j * tau)
    imparts.append(Sg.imag)
    print(f"    tau = {tau:.1f}: S = {Sg.real:+.4f}{Sg.imag:+.4f}i")
check(all(abs(v) > 1e-6 and abs(abs(v) - np.pi) > 1e-6 for v in imparts),
      "three levels: S is genuinely complex, Im S neither 0 nor pi; the July note's 'generically complex' needs d >= 3")
def im_mod(z):
    return (z.imag + np.pi) % (2 * np.pi) - np.pi


check(abs(im_mod(S_general([0.0, 1.0], 1j))) < 1e-12 and abs(im_mod(S_general([5.0, 6.0], 1j))) < 1e-12,
      "two levels, any offset: S real modulo 2 pi i (energy shifts move ln Z across a branch of the logarithm)")
check(abs(Zf(1j * np.pi) ) < 1e-12 and abs(Zf(3j * np.pi)) < 1e-12 and abs(Zf(1j * np.pi + 0.3)) > 0.1,
      "the zeros of Z lie on the imaginary axis at beta = i pi (2k+1): the Liar loops are the Fisher zeros")
print("  the loop with the FANOUT inside it:")
print(f"    Tr(I_4) = {np.trace(np.eye(4)).real:.1f}, Tr(CNOT) = {np.trace(CNOT).real:.1f}, "
      f"ln ratio = {np.log(4 / np.trace(CNOT).real):.4f} = ln 2")
check(abs(np.trace(CNOT) - 2) < 1e-12, "the copy removes one bit of loop count: 4 -> 2")
for th in (0.0, 1.0, 2.0, np.pi):
    t = np.trace(controlled(rx(th))).real
    print(f"    theta = {th:.4f}: Tr = {t:.4f} = 2 + 2 cos(theta/2) = {2 + 2 * np.cos(th / 2):.4f}; "
          f"bits of count removed = {np.log2(4 / t):.4f}; one-copy coherence factor cos(theta/2) = {np.cos(th / 2):.4f}")
    check(abs(t - (2 + 2 * np.cos(th / 2))) < 1e-12, f"theta = {th:.2f}: graded count 2 + 2 cos(theta/2)")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("B  The budget identity S(Delta_B rho) = S(rho) + C_B(rho) along the graded chain")
print("=" * 72)
p = 0.3
alpha = np.sqrt(p)
theta = 2.0
Hp = h2(p)
print(f"  p = {p}, H(p) = {Hp:.6f} bits; copy angle theta = {theta}, cos(theta/2) = {np.cos(theta / 2):.4f}")
T = lambda rho: (lambda full: (lambda out: np.array([[out[0, 0] + out[1, 1], out[0, 2] + out[1, 3]], [out[2, 0] + out[3, 1], out[2, 2] + out[3, 3]]]))(controlled(rx(theta)) @ full @ controlled(rx(theta)).conj().T))(np.kron(rho, proj(k0)))
phases = (0.0, 0.4, 1.7, 3.0)
budget_ok = True
for phi in phases:
    beta = np.sqrt(1 - p) * np.exp(1j * phi)
    rho = proj(alpha * k0 + beta * k1)
    if phi == 0.4:
        print("  phi = 0.4, N fresh partial records in turn:")
        print("    N      S(rho_N)   C_Z(rho_N)   sum        H(p)       |rho_01|    max|Im rho|")
    for N in range(0, 13):
        S = vn(rho)
        C = crel(rho, ZB)
        if phi == 0.4:
            print(f"    {N:2d}   {S:9.6f}   {C:9.6f}   {S + C:9.6f}  {Hp:9.6f}   {abs(rho[0, 1]):9.6f}   {np.max(np.abs(rho.imag)):.2e}")
        budget_ok &= abs(S + C - Hp) < 1e-10
        rho = T(rho)
    if phi == 0.4:
        for _ in range(600):
            rho = T(rho)
        check(abs(rho[0, 1]) < 1e-12 and np.max(np.abs(rho.imag)) < 1e-12 and np.allclose(rho, np.diag([p, 1 - p])),
              "the chain ends in diag(p, 1-p): a real matrix, the purely real value")
check(budget_ok, "S(rho_N) + C_Z(rho_N) = H(p) at every stage, for every relative phase")
print("  pure pre-FANOUT state: the coherence spent equals the information the record gains")
rho0 = proj(alpha * k0 + np.sqrt(1 - p) * np.exp(0.4j) * k1)
check(abs(crel(rho0, ZB) - Hp) < 1e-12 and abs(vn(rho0)) < 1e-12, "C_Z(pure) = H(p) = the record's entropy; S(pure) = 0")
print("  phase blindness: C_Z against C_X for four relative phases")
for phi in phases:
    rho = proj(alpha * k0 + np.sqrt(1 - p) * np.exp(1j * phi) * k1)
    print(f"    phi = {phi:.1f}: C_Z = {crel(rho, ZB):.6f}, C_X = {crel(rho, XB):.6f}, S(Delta_X rho) = {vn(dephase(rho, XB)):.6f}")
cz = [crel(proj(alpha * k0 + np.sqrt(1 - p) * np.exp(1j * phi) * k1), ZB) for phi in phases]
cx = [crel(proj(alpha * k0 + np.sqrt(1 - p) * np.exp(1j * phi) * k1), XB) for phi in phases]
check(max(cz) - min(cz) < 1e-12, "C_Z is independent of the relative phase")
check(max(cx) - min(cx) > 0.1, "C_X depends on the relative phase: a record in X spends phase information")
print("  promotion under a full CNOT: joint coherence in the product Z basis")
joint_in = np.kron(rho0, proj(k0))
joint_out = CNOT @ joint_in @ CNOT.conj().T
ZZ = np.eye(4, dtype=complex)
cin, cout = crel(joint_in, ZZ), crel(joint_out, ZZ)
sS = vn(reduced((CNOT @ np.kron(alpha * k0 + np.sqrt(1 - p) * np.exp(0.4j) * k1, k0)), [2, 2], [0]))
print(f"    joint C before = {cin:.6f}, after = {cout:.6f}; system entropy after = {sS:.6f}; H(p) = {Hp:.6f}")
check(abs(cin - Hp) < 1e-12 and abs(cout - Hp) < 1e-12, "the joint coherence H(p) is unchanged by the copy: promoted, not destroyed")
check(abs(sS - Hp) < 1e-12, "the system's entropy after the copy is H(p): the budget has become record entropy")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("C  Wei--Liu form: complex overlap, real part spends the coherence")
print("=" * 72)
gamma = -np.log(np.cos(theta / 2))
print(f"  per-fragment real cost gamma = -ln cos(theta/2) = {gamma:.6f} nat")
res = {}
for phi_f in (0.0, 0.9):
    lam = np.cos(theta / 2) * np.exp(1j * phi_f)
    rho = rho0.copy()
    vals = []
    for N in range(0, 7):
        c01 = rho0[0, 1] * lam ** N
        rhoN = np.array([[rho0[0, 0], c01], [np.conj(c01), rho0[1, 1]]])
        vals.append(crel(rhoN, ZB))
    res[phi_f] = vals
    print(f"    fragment phase {phi_f:.1f}: C_Z(N) = {np.round(vals, 6)}")
check(np.allclose(res[0.0], res[0.9]), "C_Z depends on |lambda|^N = e^{-N gamma} only: the imaginary cost is not spent")
check(all(res[0.0][k + 1] < res[0.0][k] for k in range(6)), "C_Z falls monotonically with the real cost accumulated")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("D  Darwinism at N = 8: the budget and the two halves of I(S:F_N)")
print("=" * 72)
N = 8
dims = [2] * (N + 1)
phi1 = rx(theta) @ k0
b0 = kron(*([k0.reshape(2, 1)] * (N + 1))).reshape(-1)
b1 = kron(*([k1.reshape(2, 1)] + [phi1.reshape(2, 1)] * N)).reshape(-1)
Psi = alpha * b0 + np.sqrt(1 - p) * np.exp(0.4j) * b1
rhoS = reduced(Psi, dims, [0])
rhoF = reduced(Psi, dims, list(range(1, N + 1)))
I_SF = vn(rhoS) + vn(rhoF) - 0.0
print(f"  S(rho_S) = {vn(rhoS):.6f}, C_Z(rho_S) = {crel(rhoS, ZB):.6f}, sum = {vn(rhoS) + crel(rhoS, ZB):.6f}, H(p) = {Hp:.6f}")
print(f"  I(S:F_N) = {I_SF:.6f} = 2 S(rho_S): classical half {vn(rhoS):.6f} (the plateau), quantum half {I_SF - vn(rhoS):.6f} (the rise at k = N)")
check(abs(vn(rhoS) + crel(rhoS, ZB) - Hp) < 1e-10, "N = 8 fragments: S(rho_S) + C_Z(rho_S) = H(p)")
check(abs(I_SF - 2 * vn(rhoS)) < 1e-10, "I(S:F_N) = 2 S(rho_S) for the pure global state")

print("\n" + "=" * 72)
if FAILS:
    print(f"{len(FAILS)} FAILED CHECKS:")
    for f in FAILS:
        print("  -", f)
    print("COHERENCE BUDGET COMPLEX COUNT: FAIL")
else:
    print("COHERENCE BUDGET COMPLEX COUNT: PASS")
