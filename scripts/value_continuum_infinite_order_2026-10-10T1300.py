#!/usr/bin/env python3
"""value_continuum_infinite_order_2026-10-10T1300.py

JS, 2026-10-10: does the conservation route clear op:limit-realisability?
Two facts for the answer, standard, no randomness.

  A. The stabiliser fragment satisfies every premise of the conservation
     route (one outcome per FANOUT, closed-loop squares, linearity, U^dagger
     U = 1) and has finitely many pure states: its one-qubit transformation
     group, the Clifford group modulo phases, has 24 elements of orders 1,
     2, 3 and 4, and the orbit of |0> is the six stabiliser states.  So the
     route cannot touch the value continuum; the open problem's own FAIL
     criterion says so.
  B. What would: one transformation of infinite projective order.  A closed
     group containing one is a compact Lie group of positive dimension and
     its orbits are continua.  The Clifford group has none; a rotation by
     the Koide phase delta = 2/9 rad about any axis has one, since 2/9 rad
     is an irrational fraction of a turn: U^n is never projectively the
     identity (that would need n/(9 pi) integral), the closest approaches
     in n <= 10^6 being the convergents of pi (n = 103993 = 33102 x pi to
     nine figures), while every Clifford element returns within 4 steps.  The Koide phase is an empirical witness that
     the regime's group is not finite, not a derivation of the continuum.
"""
import itertools

import numpy as np

I2 = np.eye(2, dtype=complex)
H = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
S = np.diag([1, 1j])


def proj_equal(A, B):
    return abs(abs(np.trace(A.conj().T @ B)) - 2) < 1e-9


# A: generate the one-qubit Clifford group modulo phases from H and S
elems = [I2]
frontier = [I2]
while frontier:
    new = []
    for g in frontier:
        for h in (H, S):
            c = g @ h
            if not any(proj_equal(c, e) for e in elems):
                elems.append(c); new.append(c)
    frontier = new
orders = []
for g in elems:
    p = I2.copy()
    for n in range(1, 30):
        p = p @ g
        if proj_equal(p, I2):
            orders.append(n); break
ket0 = np.array([1, 0], complex)
states = []
for g in elems:
    v = g @ ket0
    if not any(abs(abs(np.vdot(v, s)) - 1) < 1e-9 for s in states):
        states.append(v)
print("Value continuum and infinite order")
print("=" * 70)
print("A. one-qubit Clifford group mod phases: %d elements; element orders %s; orbit of |0>: %d states"
      % (len(elems), sorted(set(orders)), len(states)))
print("   every Clifford element conserves probability (max |U^dagger U - 1| = %.1e)" % max(np.linalg.norm(g.conj().T @ g - I2) for g in elems))
# B: the Koide rotation
delta = 2.0 / 9.0
U = np.diag([np.exp(1j * delta), np.exp(-1j * delta)])     # rotation by 2 delta about z, projectively
best = (np.inf, 0)
p = I2.copy()
for n in range(1, 1_000_001):
    p = p @ U
    d = abs(abs(np.trace(p)) - 2)
    if d < best[0]:
        best = (d, n)
# analytic: U^n projectively trivial iff 2 n delta in 2 pi Z iff n delta / pi integer
frac = abs(best[1] / (9 * np.pi) - round(best[1] / (9 * np.pi)))
print("B. rotation by the Koide phase delta = 2/9 rad: closest projective approach in n <= 10^6 is n = %d, |tr U^n| - 2 = -%.2e, n/(9 pi) off an integer by %.1e" % (best[1], best[0], frac))
print("   (U^n = 1 projectively iff n/(9 pi) is an integer; never, pi being irrational)")
print("   a closed group containing it is a compact Lie group of positive dimension; its orbit of |0> is a continuum (the z-circle)")
print("=" * 70)
print("INFINITE ORDER: %s" % ("PASS" if len(elems) == 24 and max(orders) == 4 and len(states) == 6 and best[0] > 1e-14 and frac > 1e-9 else "FAIL"))
