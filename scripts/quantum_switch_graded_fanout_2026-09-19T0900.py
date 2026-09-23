#!/usr/bin/env python3
"""quantum_switch_graded_fanout_2026-09-19T0900.py

The quantum switch under graded FANOUT of its control: causal nonseparability
decays with the same overlap product that makes a phase inaccessible.

Model. Target qubit in |psi>; control qubit in (|0>+|1>)/sqrt2; two unitaries
A and B on the target. Control |0> applies A then B (target BA|psi>); control
|1> applies B then A (target AB|psi>). R environment fragments each copy the
control's Z-basis value imperfectly: fragment k is |e0_k> if the control is
|0> and |e1_k> if |1>, with overlap lambda_k = <e0_k|e1_k> = exp(-i theta_k/2)
cos(phi). The control is then measured in the X basis. Exact result, derived
in the note and checked here against the full state vector for R <= 8:

    P(+/-) = (1 +/- Re[Lambda c]) / 2,   Lambda = prod_k lambda_k,
    c = <BA psi | AB psi> = <psi| A^dag B^dag A B |psi>.

At Lambda = 1 (no fragments), P(-) = ||[A,B] psi||^2 / 4: the order matters
exactly by the commutator. A classical mixture of the two orders gives
P(+/-) = 1/2. So the indefinite-order signal is P(+) - 1/2 = Re[Lambda c]/2,
and its magnitude falls as |Lambda| = cos^R(phi).

Part A  the switch without fragments: commutator and anticommutator branches;
        a control case with commuting generators.
Part B  graded FANOUT, real overlaps (theta_k = 0): brute force against the
        closed form for R <= 8, closed form to R = 256.
Part C  graded FANOUT with seeded random fragment phases theta_k: |Lambda| is
        the same, the signal's sign and size follow the accumulated phase.
Part D  reversal: the fragments are written by controlled unitaries U_k on the
        full state vector; applying U_k^dag for every k (R = 6) restores the
        R = 0 signal exactly. Brute force, not the closed form.

Seed 20260919. No Cayley-Dickson algebra is used (qubits only). No hidden
state. numpy only.
"""
import math

import numpy as np

SEED = 20260919
rng = np.random.default_rng(SEED)

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def rot(axis, angle):
    """exp(-i angle axis/2)."""
    return math.cos(angle / 2) * I2 - 1j * math.sin(angle / 2) * axis


def frag_states(theta, phi):
    """|e0>, |e1> with <e0|e1> = exp(-i theta/2) cos(phi)."""
    e0 = np.array([1.0, 0.0], dtype=complex)
    e1 = np.array([math.cos(phi) * np.exp(-1j * theta / 2), math.sin(phi)], dtype=complex)
    return e0, e1


def closed_form(Lam, c):
    x = (Lam * c).real
    return (1 + x) / 2, (1 - x) / 2


def brute_force(psi, A, B, thetas, phi):
    """Full state vector: target (2) x control (2) x fragments (2^R). Returns P(+), P(-)."""
    R = len(thetas)
    branch0 = B @ A @ psi      # control |0>: A then B
    branch1 = A @ B @ psi      # control |1>: B then A
    env0 = np.array([1.0], dtype=complex)
    env1 = np.array([1.0], dtype=complex)
    for th in thetas:
        e0, e1 = frag_states(th, phi)
        env0 = np.kron(env0, e0)
        env1 = np.kron(env1, e1)
    # state = (|0>_c branch0 env0 + |1>_c branch1 env1)/sqrt2, ordered control x target x env
    ket0 = np.array([1, 0], dtype=complex)
    ket1 = np.array([0, 1], dtype=complex)
    state = (np.kron(np.kron(ket0, branch0), env0) + np.kron(np.kron(ket1, branch1), env1)) / math.sqrt(2)
    # project control on |+>, |->
    plus = np.array([1, 1], dtype=complex) / math.sqrt(2)
    minus = np.array([1, -1], dtype=complex) / math.sqrt(2)
    dim_rest = 2 * (2 ** R)
    Pp = np.kron(np.outer(plus, plus.conj()), np.eye(dim_rest))
    Pm = np.kron(np.outer(minus, minus.conj()), np.eye(dim_rest))
    return float(np.vdot(state, Pp @ state).real), float(np.vdot(state, Pm @ state).real)


# --- the switch itself ---
a, b = 1.0, 0.7
A = rot(SX, a)
B = rot(SZ, b)
psi = np.array([1.0, 0.0], dtype=complex)
c = np.vdot(B @ A @ psi, A @ B @ psi)
comm = A @ B - B @ A
anti = A @ B + B @ A

print("=== Part A: the switch without fragments (A = Rx(%.1f), B = Rz(%.1f), psi = |0>) ===" % (a, b))
print("c = <BA psi|AB psi> = %.6f %+.6f i" % (c.real, c.imag))
Pp, Pm = closed_form(1.0, c)
print("P(+) = %.6f = ||{A,B} psi||^2/4 = %.6f ; P(-) = %.6f = ||[A,B] psi||^2/4 = %.6f"
      % (Pp, np.linalg.norm(anti @ psi) ** 2 / 4, Pm, np.linalg.norm(comm @ psi) ** 2 / 4))
Bz = rot(SZ, 0.9)
cz = np.vdot(Bz @ B @ psi, B @ Bz @ psi)
print("control case, both generators sigma_z (commuting): P(-) = %.6f" % closed_form(1.0, cz)[1])
print("classical mixture of the two orders: P(+) = P(-) = 0.5 ; indefinite-order signal at R = 0: P(+) - 1/2 = %.6f" % (Pp - 0.5))

# --- graded FANOUT, real overlaps ---
phi = 0.3
lam = math.cos(phi)
print()
print("=== Part B: graded FANOUT of the control, real overlaps lambda = cos(%.1f) = %.6f ===" % (phi, lam))
print("%4s %14s %12s %12s %14s %12s" % ("R", "|Lambda|", "P(+) exact", "P(-) exact", "P(+) brute", "signal"))
for R in [0, 1, 2, 3, 4, 6, 8]:
    Lam = lam ** R
    Pp, Pm = closed_form(Lam, c)
    bp, bm = brute_force(psi, A, B, [0.0] * R, phi)
    print("%4d %14.6e %12.6f %12.6f %14.6f %12.6f" % (R, Lam, Pp, Pm, bp, Pp - 0.5))
    assert abs(bp - Pp) < 1e-12 and abs(bm - Pm) < 1e-12
print("brute force agrees with the closed form to 1e-12 for R <= 8")
for R in [16, 32, 64, 128, 256]:
    Lam = lam ** R
    Pp, Pm = closed_form(Lam, c)
    print("%4d %14.6e %12.6f %12.6f %14s %12.6f" % (R, Lam, Pp, Pm, "-", Pp - 0.5))
R_e = math.ceil(-1.0 / math.log(lam))
print("signal falls to 1/e of its R = 0 value at R = %d (= ceil(1/(-ln cos phi)))" % R_e)

# --- graded FANOUT with fragment phases ---
print()
print("=== Part C: seeded fragment phases theta_k ~ U(-pi, pi), phi = %.1f ===" % phi)
thetas = rng.uniform(-math.pi, math.pi, size=8)
print("theta_k = " + " ".join("%+.4f" % t for t in thetas))
print("%4s %14s %14s %12s %14s" % ("R", "|Lambda|", "arg Lambda", "P(+) exact", "P(+) brute"))
for R in [1, 2, 4, 8]:
    Lam = np.prod([np.exp(-1j * t / 2) * lam for t in thetas[:R]])
    Pp, Pm = closed_form(Lam, c)
    bp, bm = brute_force(psi, A, B, list(thetas[:R]), phi)
    print("%4d %14.6e %+14.6f %12.6f %14.6f" % (R, abs(Lam), np.angle(Lam), Pp, bp))
    assert abs(bp - Pp) < 1e-12
print("|Lambda| is cos^R(phi) regardless of the phases; the phases rotate the signal Re[Lambda c]/2")

# --- reversal ---
print()
print("=== Part D: reversal at R = 6 (real overlaps), brute force on the full state vector ===")


def copy_unitary(k, R, phi):
    """U_k = |0><0|_c x I + |1><1|_c x V_k, with V_k = exp(-i phi sigma_y) on fragment k,
    so that V_k |0> = cos(phi)|0> + sin(phi)|1> = |e1> (theta = 0). Ordering: control x target x env."""
    V = rot(SY, 2 * phi)
    Venv = np.array([[1.0]], dtype=complex)
    for j in range(R):
        Venv = np.kron(Venv, V if j == k else I2)
    P0 = np.array([[1, 0], [0, 0]], dtype=complex)
    P1 = np.array([[0, 0], [0, 1]], dtype=complex)
    dim_env = 2 ** R
    return np.kron(np.kron(P0, I2), np.eye(dim_env)) + np.kron(np.kron(P1, I2), Venv)


R = 6
ket0 = np.array([1, 0], dtype=complex)
ket1 = np.array([0, 1], dtype=complex)
env_init = np.array([1.0], dtype=complex)
for _ in range(R):
    env_init = np.kron(env_init, ket0)
state = (np.kron(np.kron(ket0, B @ A @ psi), env_init) + np.kron(np.kron(ket1, A @ B @ psi), env_init)) / math.sqrt(2)
Us = [copy_unitary(k, R, phi) for k in range(R)]
for U in Us:
    state = U @ state
plus = np.array([1, 1], dtype=complex) / math.sqrt(2)
Pp_op = np.kron(np.outer(plus, plus.conj()), np.eye(2 * 2 ** R))
sig_with = float(np.vdot(state, Pp_op @ state).real) - 0.5
for U in reversed(Us):
    state = U.conj().T @ state
sig_after = float(np.vdot(state, Pp_op @ state).real) - 0.5
sig0 = closed_form(1.0, c)[0] - 0.5
print("signal with 6 fragments written: %.6f (closed form %.6f) ; after applying U_k^dag for all k: %.6f ; R = 0 value: %.6f"
      % (sig_with, closed_form(lam ** R, c)[0] - 0.5, sig_after, sig0))
print("reversal exact to %.1e" % abs(sig_after - sig0))
