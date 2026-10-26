#!/usr/bin/env python3
"""
hypodox_ctc_fanout_2026-10-16T0900.py

Closed loops through a FANOUT.  The consistency condition of a closed timelike
curve in Deutsch's model, rho = Tr_CR[U (rho_in (x) rho) U^dag], is the
fixed-point equation v = g(v) of
knowledge/sessions/liar_hypodox_fanout_2026-10-16T1100.md with g the loop's
map.  This script applies it, and the post-selected (Lloyd) condition, to the
four self-referential loops a single FANOUT admits, and sets the graded open
chain of quantum Darwinism beside them.

  A  Deutsch fixed-point sets.  NOT loop (grandfather = Liar), identity loop
     (bootstrap = truth-teller), the system on the loop through a CNOT with a
     fresh record (self-measurement), the record on the loop through a CNOT
     with a chronology-respecting system.  Generic loops for comparison.
  B  The chronology-respecting output.  With the record on the loop the
     system's coherence is multiplied by c = Tr(X rho_R), the loop's own Liar
     value: c = 1 leaves it alone, c = -1 applies Z, Deutsch's maximum-entropy
     c = 0 dephases it to Born weights and the loop holds no record.  With the
     system on the loop, the fresh record copies whatever the loop holds.
  C  Post-selected loops.  C = Tr_CTC U: NOT -> weight 0 (the paradox is
     post-selected away), identity -> 2 I, system on loop -> record projected
     on |+>, record on loop -> system projected on |0>; graded, the flipping
     branch is damped by cos(theta/2).
  D  Graded copy, open against closed.  A partial copy exp(-i theta X/2)
     damps the coherence by cos(theta/2) per fresh record (smooth in N); the
     closed loop's fixed set is the record's diagonal for every theta > 0, and
     the open chain converges to the Born-weighted member of that set.
  E  Quantum Darwinism.  I(S:F_k) against the number k of fragments read:
     N = 6 perfect copies give the plateau at H(p) (the hypodox regime, every
     fragment agrees) and the rise to 2H(p) only at k = N (where the loop could
     still be undone); N = 10 partial copies show the plateau approached
     smoothly; the curve is antisymmetric about N/2 for a pure global state.
  F  Born against maximum entropy.  The open chain's limit diag(p, 1-p)
     against the loop's I/2: relative entropy 1 - H(p) bits, one-shot
     distinguishability (1 + |p - 1/2|)/2.

Seed 20261016.  numpy only.  Final line: HYPODOX CTC FANOUT: PASS.
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
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
P0 = np.array([[1, 0], [0, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)
k0 = np.array([1, 0], dtype=complex)
k1 = np.array([0, 1], dtype=complex)
kp = (k0 + k1) / np.sqrt(2)
km = (k0 - k1) / np.sqrt(2)
kyp = (k0 + 1j * k1) / np.sqrt(2)
kym = (k0 - 1j * k1) / np.sqrt(2)


def proj(v):
    return np.outer(v, v.conj())


def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


LET = "abcdefghijklmnopqrstuvwxyz"


def ptrace(rho, dims, keep):
    """Reduced matrix on the subsystems in `keep` (ascending order)."""
    n = len(dims)
    keep = sorted(keep)
    t = rho.reshape(list(dims) + list(dims))
    row = [LET[i] for i in range(n)]
    col = [LET[i].upper() if i in keep else LET[i] for i in range(n)]
    out = "".join(LET[i] for i in keep) + "".join(LET[i].upper() for i in keep)
    res = np.einsum("".join(row) + "".join(col) + "->" + out, t)
    d = int(np.prod([dims[i] for i in keep]))
    return res.reshape(d, d)


def rx(theta):
    return np.cos(theta / 2) * I2 - 1j * np.sin(theta / 2) * X


def controlled(G):
    """Control on the first qubit, G on the second."""
    return kron(P0, I2) + kron(P1, G)


CNOT = controlled(X)


def vn_entropy(rho):
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    w = w[w > 1e-12]
    return float(-np.sum(w * np.log2(w)))


def h2(p):
    return float(-p * np.log2(p) - (1 - p) * np.log2(1 - p))


def haar_u4():
    A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    Q, R = np.linalg.qr(A)
    return Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))


def random_pure():
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    return proj(v / np.linalg.norm(v))


# --- Deutsch's model ---------------------------------------------------------
def deutsch_map(U, rho_in, ctc):
    """ctc = 0: the loop system is the first factor and the chronology-
    respecting input rho_in the second; ctc = 1 the other way round."""
    def T(rho_c):
        full = kron(rho_c, rho_in) if ctc == 0 else kron(rho_in, rho_c)
        out = U @ full @ U.conj().T
        return ptrace(out, [2, 2], [ctc])
    return T


def cr_output(U, rho_in, rho_c, ctc):
    full = kron(rho_c, rho_in) if ctc == 0 else kron(rho_in, rho_c)
    out = U @ full @ U.conj().T
    return ptrace(out, [2, 2], [1 - ctc])


def superop(T, d=2):
    M = np.zeros((d * d, d * d), dtype=complex)
    for k in range(d * d):
        E = np.zeros((d, d), dtype=complex)
        E.flat[k] = 1.0
        M[:, k] = T(E).reshape(-1)
    return M


def fixed_dim(T, d=2, tol=1e-9):
    s = np.linalg.svd(superop(T, d) - np.eye(d * d), compute_uv=False)
    return int(np.sum(s < tol))


def unique_fixed_point(T, d=2):
    M = superop(T, d) - np.eye(d * d)
    _, s, vh = np.linalg.svd(M)
    v = vh[-1].conj().reshape(d, d)
    v = (v + v.conj().T) / 2
    return v / np.trace(v).real


STATES = [("|0>", proj(k0)), ("|1>", proj(k1)), ("|+>", proj(kp)), ("|->", proj(km)),
          ("|y+>", proj(kyp)), ("|y->", proj(kym)), ("I/2", I2 / 2)]


def fixed_states(T, tol=1e-10):
    return [name for name, r in STATES if np.linalg.norm(T(r) - r) < tol]


def pctc_operator(U, ctc):
    """Lloyd's post-selected loop: C = Tr_CTC U on the chronology-respecting
    system (the operator, unnormalised)."""
    return ptrace(U, [2, 2], [1 - ctc])


# ---------------------------------------------------------------------------
print("=" * 72)
print("A  Deutsch fixed-point sets of the four loops through one FANOUT")
print("=" * 72)
alpha = np.sqrt(0.3)
beta = np.sqrt(0.7) * np.exp(0.4j)
psi = alpha * k0 + beta * k1
rho_psi = proj(psi)
p_born = abs(alpha) ** 2
print(f"  chronology-respecting system psi = sqrt(0.3)|0> + sqrt(0.7) e^(0.4 i)|1>, "
      f"p = |alpha|^2 = {p_born:.1f}")

cases = [
    ("NOT loop (grandfather = Liar): record on loop, CR input |1>",
     CNOT, proj(k1), 1, 2, {"|+>", "|->", "I/2"}),
    ("identity loop (bootstrap = truth-teller)",
     np.eye(4, dtype=complex), proj(k0), 1, 4, {n for n, _ in STATES}),
    ("system on loop, fresh record |0> (self-measurement)",
     CNOT, proj(k0), 0, 2, {"|0>", "|1>", "I/2"}),
    ("record on loop, CR system psi (the agent's record closed on itself)",
     CNOT, rho_psi, 1, 2, {"|+>", "|->", "I/2"}),
]
maps = {}
for label, U, rho_in, ctc, edim, efix in cases:
    T = deutsch_map(U, rho_in, ctc)
    maps[label] = T
    dim = fixed_dim(T)
    fix = fixed_states(T)
    print(f"\n  {label}")
    print(f"    fixed-point subspace dimension {dim}; fixed among the seven test states: {fix}")
    check(dim == edim, f"fixed subspace dimension {dim} == {edim}")
    check(set(fix) == efix, f"fixed test states == {sorted(efix)}")
    check(np.linalg.norm(T(I2 / 2) - I2 / 2) < 1e-12,
          "I/2 is a fixed point (the maximum-entropy choice is available)")

print("\n  generic loops: Haar-random U(4) with a random pure CR input")
for i in range(5):
    U = haar_u4()
    T = deutsch_map(U, random_pure(), 1)
    dim = fixed_dim(T)
    rho_star = unique_fixed_point(T)
    ev = sorted(np.abs(np.linalg.eigvals(superop(T))), reverse=True)
    rho = random_pure()
    for _ in range(2000):
        rho = T(rho)
    res = np.linalg.norm(rho - rho_star)
    bloch = np.real([np.trace(rho_star @ X), np.trace(rho_star @ Y), np.trace(rho_star @ Z)])
    print(f"    loop {i}: fixed dim {dim}; second eigenvalue modulus {ev[1]:.4f}; iteration residual "
          f"after 2000 steps {res:.2e}; Bloch vector of the fixed point {bloch}, |r| = {np.linalg.norm(bloch):.4f}")
    check(dim == 1, f"generic loop {i}: unique fixed point")
    check(ev[1] < 1 - 1e-6, f"generic loop {i}: spectral gap, so the fixed point is reached by iteration")
    check(res < 1e-8, f"generic loop {i}: iteration of the open chain converges to it")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("B  The chronology-respecting output")
print("=" * 72)
print("  record on the loop, system psi passes: the output coherence is c times the input, c = Tr(X rho_R)")
for c in (1.0, 0.0, -1.0):
    rho_R = (I2 + c * X) / 2
    T = maps[cases[3][0]]
    check(np.linalg.norm(T(rho_R) - rho_R) < 1e-12, f"c = {c:+.0f}: (I + cX)/2 is a fixed point")
    out = cr_output(CNOT, rho_psi, rho_R, 1)
    ratio = out[0, 1] / rho_psi[0, 1]
    print(f"    c = {c:+.0f}: output diag = {np.real(np.diag(out))}, coherence ratio = {ratio:.4f}")
    check(abs(ratio - c) < 1e-12, f"c = {c:+.0f}: coherence multiplied by c")
    if c == 0.0:
        check(np.allclose(out, np.diag([p_born, 1 - p_born])), "c = 0: Born-weighted dephased system")
    if c == -1.0:
        check(np.allclose(out, Z @ rho_psi @ Z), "c = -1: the |-> record applies Z to the system")
print("  system on the loop, fresh record |0>: the record copies the loop's content")
T = maps[cases[2][0]]
for q in (0.3, 0.5, 0.9):
    rho_S = np.diag([q, 1 - q]).astype(complex)
    check(np.linalg.norm(T(rho_S) - rho_S) < 1e-12, f"q = {q}: diag(q, 1-q) is a fixed point")
    out = cr_output(CNOT, proj(k0), rho_S, 0)
    check(np.allclose(out, rho_S), f"q = {q}: the record leaves with diag({q}, {1-q:.1f}), the loop's own content")
print("    the loop's content is unconstrained: any classical value is self-consistent (the jinn)")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("C  Post-selected loops (Lloyd): C = Tr_CTC U")
print("=" * 72)
C = pctc_operator(CNOT, 1)
print(f"  record on loop, C = Tr_R CNOT =\n{C}")
check(np.allclose(C, 2 * P0), "record on loop: C = 2|0><0|, the system is projected on the non-flipping branch")
w = np.linalg.norm(C @ k1) ** 2
print(f"  NOT loop (CR input |1>): weight |C|1>|^2 = {w:.4f}")
check(w < 1e-12, "NOT loop: the paradox has weight zero, it is post-selected away")
C = pctc_operator(np.eye(4, dtype=complex), 1)
check(np.allclose(C, 2 * I2), "identity loop: C = 2 I, no constraint on the system")
C = pctc_operator(CNOT, 0)
v = C @ k0
v = v / np.linalg.norm(v)
print(f"  system on loop, C = Tr_S CNOT = I + X; record output C|0>/norm = {v}")
check(np.allclose(C, I2 + X), "system on loop: C = I + X = 2|+><+|")
check(abs(abs(v @ kp.conj()) - 1) < 1e-12, "system on loop: the fresh record leaves in |+>, the Liar's state")
print("  graded record on loop, U = controlled exp(-i theta X/2):")
for theta in (0.0, 0.6, 1.5, np.pi):
    lam = np.cos(theta / 2)
    C = pctc_operator(controlled(rx(theta)), 1)
    out = C @ psi
    wt = np.linalg.norm(out) ** 2 / 4
    print(f"    theta = {theta:.4f}: C = diag{tuple(np.round(np.real(np.diag(C)), 4))}, "
          f"weight (|alpha|^2 + lam^2 |beta|^2) = {wt:.4f}")
    check(np.allclose(C, 2 * P0 + 2 * lam * P1), f"theta = {theta:.4f}: C = 2|0><0| + 2 cos(theta/2)|1><1|")
    check(abs(wt - (p_born + lam ** 2 * (1 - p_born))) < 1e-12, f"theta = {theta:.4f}: weight is graded by cos^2")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("D  Graded copy: the open chain against the closed loop")
print("=" * 72)
theta = 0.6
lam = np.cos(theta / 2)
U_th = controlled(rx(theta))
T_open = deutsch_map(U_th, proj(k0), 0)   # the same superoperator serves both
rho = rho_psi.copy()
print(f"  theta = {theta}, cos(theta/2) = {lam:.6f}; N fresh records in turn:")
for N in range(1, 9):
    rho = T_open(rho)
    r = abs(rho[0, 1]) / abs(rho_psi[0, 1])
    print(f"    N = {N}: |coherence| ratio = {r:.6f}, cos^N = {lam ** N:.6f}")
    check(abs(r - lam ** N) < 1e-12, f"N = {N}: open chain damps the coherence by cos(theta/2)^N")
rho = rho_psi.copy()
for _ in range(1500):
    rho = T_open(rho)
check(np.allclose(rho, np.diag([p_born, 1 - p_born]), atol=1e-9),
      "the open chain converges to diag(p, 1-p), the Born-weighted member of the fixed set")
print("  closed loop (system on loop) fixed-set dimension against theta:")
for th in (0.0, 1e-3, 0.6, np.pi):
    dim = fixed_dim(deutsch_map(controlled(rx(th)), proj(k0), 0))
    print(f"    theta = {th:.4f}: dim Fix = {dim}  {'(everything)' if dim == 4 else '(the record diagonal)'}")
    check(dim == (4 if th == 0.0 else 2), f"theta = {th:.4f}: closure is all or nothing")
print("  closed loop (record on loop, graded) fixed test states against theta:")
for th in (0.0, 1e-3, 0.6, np.pi):
    T = deutsch_map(controlled(rx(th)), rho_psi, 1)
    fix = fixed_states(T)
    print(f"    theta = {th:.4f}: {fix}")
    check(set(fix) == ({n for n, _ in STATES} if th == 0.0 else {"|+>", "|->", "I/2"}),
          f"theta = {th:.4f}: a record on a closed loop carries no Z value for any theta > 0")
rho_R = I2 / 2
out = cr_output(controlled(rx(theta)), rho_psi, rho_R, 1)
r = abs(out[0, 1]) / abs(rho_psi[0, 1])
print(f"  maximum-entropy loop record at theta = {theta}: system coherence ratio {r:.6f} = cos(theta/2) = {lam:.6f}")
check(abs(r - lam) < 1e-12, "a maximum-entropy loop record decoheres the system by exactly one open copy")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("E  Quantum Darwinism: I(S:F_k) against the number of fragments read")
print("=" * 72)


def reduced(Psi, dims, keep):
    """Reduced density matrix of a pure state on the subsystems in keep."""
    n = len(dims)
    keep = sorted(keep)
    rest = [i for i in range(n) if i not in keep]
    t = Psi.reshape(dims).transpose(keep + rest)
    dk = int(np.prod([dims[i] for i in keep]))
    M = t.reshape(dk, -1)
    return M @ M.conj().T


def darwin_curve(N, th):
    dims = [2] * (N + 1)
    phi1 = rx(th) @ k0
    b0 = kron(*([k0.reshape(2, 1)] * (N + 1))).reshape(-1)
    b1 = kron(*([k1.reshape(2, 1)] + [phi1.reshape(2, 1)] * N)).reshape(-1)
    Psi = alpha * b0 + beta * b1
    SS = vn_entropy(reduced(Psi, dims, [0]))
    row = [0.0]
    for k in range(1, N + 1):
        frag = list(range(1, k + 1))
        row.append(SS + vn_entropy(reduced(Psi, dims, frag)) - vn_entropy(reduced(Psi, dims, [0] + frag)))
    return SS, row


Hp = h2(p_born)
print(f"  p = {p_born:.1f}, H(p) = {Hp:.4f} bits")
for N, th in ((6, np.pi), (10, 2.0), (10, 1.0)):
    SS, row = darwin_curve(N, th)
    lam_th = np.cos(th / 2)
    print(f"  N = {N}, theta = {th:.4f} (fragment overlap {lam_th:.4f}, residual coherence "
          f"cos^N = {lam_th ** N:.2e}): S(S) = {SS:.4f}")
    print("    k       : " + " ".join(f"{k:6d}" for k in range(N + 1)))
    print("    I(S:F_k): " + " ".join(f"{v:6.4f}" for v in row))
    check(all(abs(row[k] + row[N - k] - 2 * SS) < 1e-9 for k in range(N + 1)),
          f"N = {N}, theta = {th:.2f}: I(S:F_k) + I(S:F_(N-k)) = 2 S(S), the curve is antisymmetric about N/2")
    check(all(row[k + 1] >= row[k] - 1e-12 for k in range(N)), f"N = {N}, theta = {th:.2f}: I(S:F_k) is monotone")
    if th == np.pi:
        check(all(abs(row[k] - Hp) < 1e-9 for k in range(1, N)),
              "perfect copies: I(S:F_k) = H(p) for 1 <= k <= N-1, the plateau")
        check(abs(row[N] - 2 * Hp) < 1e-9, "perfect copies: 2 H(p) only with every fragment")
    else:
        deficit = [SS - v for v in row[: N // 2 + 1]]
        print("    S(S) - I  : " + " ".join(f"{v:6.4f}" for v in deficit))
        if th == 2.0:
            check(deficit[3] < 0.05 * SS, "theta = 2.00: within 5% of the plateau after three of ten fragments")
            check(abs(SS - Hp) < 0.01, "theta = 2.00, N = 10: the system is decohered to within 0.01 bit of H(p)")
        if th == 1.0:
            check(deficit[3] > 0.05 * SS, "theta = 1.00: three of ten fragments are not yet within 5% of the plateau")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("F  Born against maximum entropy")
print("=" * 72)
D = float(p_born * np.log2(2 * p_born) + (1 - p_born) * np.log2(2 * (1 - p_born)))
td = abs(p_born - 0.5)
print(f"  D(diag(p)||I/2) = {D:.4f} bits = 1 - H(p) = {1 - Hp:.4f}")
print(f"  trace distance |p - 1/2| = {td:.4f}; one-shot success (1 + {td:.1f})/2 = {(1 + td) / 2:.4f}")
check(abs(D - (1 - Hp)) < 1e-12, "relative entropy of the Born coin from the fair coin is 1 - H(p)")

# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
if FAILS:
    print(f"{len(FAILS)} FAILED CHECKS:")
    for f in FAILS:
        print("  -", f)
    print("HYPODOX CTC FANOUT: FAIL")
else:
    print("HYPODOX CTC FANOUT: PASS")
