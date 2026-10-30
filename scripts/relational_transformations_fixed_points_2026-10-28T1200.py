#!/usr/bin/env python3
"""Relational transformations and pure fixed points (2026-10-28T1200).

Checks behind sessions/relational_state_continuity_2026-10-28T1200.md.
The premise under test is (I): every admissible reversible transformation
is a phase of some admissible classical structure, i.e. is diagonal in the
record basis of some admissible observer. Its consequence is (F): every
admissible transformation fixes an admissible pure state (fixed-point route,
2026-10-10T1500).

A. One-qubit Clifford group modulo phases: which elements are phases of an
   admissible structure (diagonal in the X, Y or Z basis), and whether that
   set coincides with the elements having a fixed stabiliser state.
B. Two admissible phases compose to an inadmissible one: the axis of
   S_Z(pi/2) S_X(pi/2) and the overlap of its eigenstates with the Pauli
   bases.
C. The rebit: SO(2) on the real projective line has derangements; the
   missing fixed points are the complex eigenvectors (1, +-i)/sqrt 2.
D. Real quantum theory in higher dimension: SO(3) elements all have a real
   eigenvector; generic SO(4) elements have none. Complex: every sampled
   unitary has an eigenvector.

Fixed seed 20261028. No hidden state. Pure numpy.
"""
import itertools
import numpy as np

SEED = 20261028
rng = np.random.default_rng(SEED)
TOL = 1e-9

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S = np.array([[1, 0], [0, 1j]], dtype=complex)
PAULIS = {"X": X, "Y": Y, "Z": Z}


def proj_equal(U, V):
    """U and V equal up to a global phase."""
    t = np.trace(U.conj().T @ V)
    return abs(abs(t) - 2) < 1e-7 and np.allclose(U * (t / abs(t)), V, atol=1e-7)


def clifford_mod_phase():
    elems = [I2]
    frontier = [I2]
    while frontier:
        new = []
        for g in frontier:
            for h in (H, S):
                c = h @ g
                if not any(proj_equal(c, e) for e in elems):
                    elems.append(c)
                    new.append(c)
        frontier = new
    return elems


def bloch(psi):
    psi = psi / np.linalg.norm(psi)
    return np.real(np.array([psi.conj() @ P @ psi for P in (X, Y, Z)]))


def stabiliser_states():
    out = []
    for P in (X, Y, Z):
        w, v = np.linalg.eigh(P)
        for k in range(2):
            out.append(v[:, k])
    return out


def fixes_some(U, states):
    return any(abs(abs(s.conj() @ U @ s) - 1) < TOL for s in states)


def is_phase_of(U, P):
    """U is diagonal in the eigenbasis of Pauli P, i.e. commutes with P."""
    return np.allclose(U @ P, P @ U, atol=1e-9)


print("Relational transformations and pure fixed points, seed", SEED)
print("=" * 86)

# ---------------------------------------------------------------- A
cliff = clifford_mod_phase()
stab = stabiliser_states()
phase_of_some = [any(is_phase_of(U, P) for P in PAULIS.values()) for U in cliff]
fixes = [fixes_some(U, stab) for U in cliff]
n_phase = sum(phase_of_some)
n_fix = sum(fixes)
agree = all(a == b for a, b in zip(phase_of_some, fixes))
per_basis = {k: sum(is_phase_of(U, P) for U in cliff) for k, P in PAULIS.items()}
print(f"A. Clifford mod phases: {len(cliff)} elements; stabiliser states: {len(stab)}")
print(f"   elements that are a phase of X, Y or Z (diagonal in an admissible basis): {n_phase}"
      f"  (per basis {per_basis}, identity shared)")
print(f"   elements fixing some stabiliser state: {n_fix}; derangements: {len(cliff) - n_fix}")
print(f"   'phase of an admissible structure' == 'fixes an admissible state' element by element: {agree}")

# ---------------------------------------------------------------- B
SX = H @ S @ H          # phase pi/2 of the X structure
comp = S @ SX           # Z-phase then X-phase, both admissible
w, v = np.linalg.eig(comp)
order = next(n for n in range(1, 13) if proj_equal(np.linalg.matrix_power(comp, n), I2))
axis = bloch(v[:, 0])
overlaps = {k: abs(v[:, 0].conj() @ P @ v[:, 0]) for k, P in PAULIS.items()}
print(f"B. composite S_Z(pi/2) S_X(pi/2): projective order {order}; eigenstate Bloch axis "
      f"({axis[0]:+.4f}, {axis[1]:+.4f}, {axis[2]:+.4f}), |axis_k| = 1/sqrt3 = {1/np.sqrt(3):.4f}")
print(f"   |<eig|P|eig>| for P = X, Y, Z: " + ", ".join(f"{k} {o:.4f}" for k, o in overlaps.items())
      + "  (a stabiliser state would give one 1 and two 0)")
print(f"   phase of X, Y or Z: {any(is_phase_of(comp, P) for P in PAULIS.values())};"
      f" fixes a stabiliser state: {fixes_some(comp, stab)}")

# ---------------------------------------------------------------- C
print("C. rebit: SO(2) acting on the real projective line RP^1")
for theta in (np.pi / 4, np.pi / 2, 2 * np.pi / 3):
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    phis = np.linspace(0, np.pi, 3601, endpoint=False)
    vs = np.stack([np.cos(phis), np.sin(phis)])
    best = np.max(np.abs(np.einsum("ij,ij->j", vs, R @ vs)))
    wr = np.linalg.eigvals(R)
    print(f"   theta = {theta:.4f}: max over 3601 real directions of |<v|Rv>| = {best:.6f} < 1 (no fixed point);"
          f" eigenvalues {wr[0]:.3f}, {wr[1]:.3f}, eigenvectors (1, +-i)/sqrt2 -- outside the rebit")

# ---------------------------------------------------------------- D
def random_SO(n):
    A = rng.normal(size=(n, n))
    Q, Rr = np.linalg.qr(A)
    Q = Q @ np.diag(np.sign(np.diag(Rr)))
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1
    return Q


def random_U(n):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, Rr = np.linalg.qr(A)
    return Q @ np.diag(np.diag(Rr) / np.abs(np.diag(Rr)))


def has_real_eigvec(Q):
    w = np.linalg.eigvals(Q)
    return bool(np.any(np.abs(np.imag(w)) < 1e-9))


N = 1000
so3 = sum(has_real_eigvec(random_SO(3)) for _ in range(N))
so4 = sum(has_real_eigvec(random_SO(4)) for _ in range(N))
so5 = sum(has_real_eigvec(random_SO(5)) for _ in range(N))
u2 = sum(np.linalg.eigvals(random_U(2)).size == 2 for _ in range(N))
u4 = sum(np.linalg.eigvals(random_U(4)).size == 4 for _ in range(N))
print(f"D. real quantum theory: random SO(n) elements with a real eigenvector (a fixed point of RP^(n-1)):")
print(f"   SO(3): {so3}/{N}   SO(4): {so4}/{N}   SO(5): {so5}/{N}   (even n: generically none; odd n: always)")
print(f"   complex: random U(2) with an eigenvector {u2}/{N}, U(4) {u4}/{N} (always; the fundamental theorem of algebra)")
print("=" * 86)
ok = (agree and n_phase == 10 and len(cliff) - n_fix == 14 and order == 3
      and so3 == N and so4 == 0 and so5 == N and u2 == N and u4 == N)
print("RELATIONAL FIXED POINTS:", "PASS" if ok else "FAIL")
