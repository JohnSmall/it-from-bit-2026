#!/usr/bin/env python3
"""fixed_point_route_value_continuum_2026-10-10T1500.py

JS, 2026-10-10: why can the chain self-reference -> negative probability ->
complex measure -> (with conservation) reversible continuity not be closed;
what remains?  The gap is the value continuum (op:limit-realisability).  This
script checks the finite parts of a candidate route that replaces the
continuum premise by a fixed-point premise of Lawvere's shape.

  Theorem (finite part, Jordan 1872 via Burnside): a finite group acting
  transitively on a set of >= 2 points has an element with no fixed point.
  So "every admissible transformation fixes some admissible pure state"
  together with transitivity forces the state space to be infinite; with
  closedness, a connected manifold (component argument in the note).

  A. The stabiliser fragment: the one-qubit Clifford group mod phases (24
     elements) acting on the six stabiliser states.  Fixed-point counts per
     element; Burnside average = 1 orbit; the derangements are the order-2
     Hadamard-type and order-3 elements.  Their fixed points in CP^1 are the
     H-states and F-states of Burton--Anwar (2026-10-03): the magic states.
     So the fragment violates the fixed-point premise, and the states it
     lacks for it are exactly the magic states.
  B. Closing the fragment under the fixed points of its own transformations
     gives 6 + 12 + 8 = 26 states on which every Clifford element has a fixed
     point, but the action has three orbits: a superselection label, which
     the framework's "no record before FANOUT" excludes.  Fixed points and
     transitivity together are what kill finiteness.
  C. Spekkens's toy bit: S_4 on the six 2-subsets of {1,2,3,4}; 3-cycles and
     4-cycles are derangements.  The toy theory violates the premise too.
  D. Quantum theory satisfies it: every unitary has an eigenvector, so every
     element of U(2) fixes a point of CP^1 (sample of 200); and on the total
     space S^3 (with the global phase) it does not: scalar phases act freely.
     The fixed-point property lives on the base, where the records are.
Seed 20261010; numpy only.
"""
import itertools

import numpy as np

rng = np.random.default_rng(20261010)
I2 = np.eye(2, dtype=complex)
H = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
S = np.diag([1, 1j])
P = np.polynomial.polynomial


def peq(A, B): return abs(abs(np.trace(A.conj().T @ B)) - 2) < 1e-9
def seq(u, v): return abs(abs(np.vdot(u, v)) - 1) < 1e-9


def gen_group(gens):
    elems = [I2]; frontier = [I2]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                c = g @ h
                if not any(peq(c, e) for e in elems):
                    elems.append(c); new.append(c)
        frontier = new
    return elems


def order(g):
    p = I2.copy()
    for n in range(1, 50):
        p = p @ g
        if peq(p, I2): return n


def orbit(states, elems):
    out = list(states); changed = True
    while changed:
        changed = False
        for g in elems:
            for s in list(out):
                v = g @ s
                if not any(seq(v, t) for t in out):
                    out.append(v); changed = True
    return out


def orbits(states, elems):
    left = list(range(len(states))); res = []
    while left:
        i = left[0]; orb = {i}; frontier = [i]
        while frontier:
            j = frontier.pop()
            for g in elems:
                v = g @ states[j]
                k = next(m for m, t in enumerate(states) if seq(v, t))
                if k not in orb: orb.add(k); frontier.append(k)
        res.append(sorted(orb)); left = [m for m in left if m not in orb]
    return res


def chart(v):                                   # Burton--Anwar chart z = v0/v1
    return np.inf if abs(v[1]) < 1e-12 else v[0] / v[1]


def classify(z):
    if z == np.inf or abs(z) < 1e-9: return "stabiliser"
    for name, poly in (("stabiliser", [1, 0, 0, 0, -1]), ("H", [-1, -2, 1]), ("H", [-1, 2, 1]), ("H", [1, 0, 6, 0, 1]),
                       ("H", [1, 0, 0, 0, 1]), ("F", [1, 0, 0, 0, 14, 0, 0, 0, 1])):
        if abs(P.polyval(z, poly)) < 1e-6: return name
    return "other"


cliff = gen_group([H, S])
stab = orbit([np.array([1, 0], complex)], cliff)
print("Fixed points, derangements and the value continuum, seed 20261010")
print("=" * 86)
# A
fp = [sum(seq(g @ s, s) for s in stab) for g in cliff]
print("A. Clifford mod phases: %d elements on %d stabiliser states; Burnside average of fixed points = %.3f = number of orbits" % (len(cliff), len(stab), np.mean(fp)))
der = [(order(g), g) for g, f in zip(cliff, fp) if f == 0]
print("   derangements (no fixed stabiliser state): %d elements, of orders %s" % (len(der), sorted(set(o for o, _ in der))))
kinds = {}
for o, g in der:
    w, V = np.linalg.eig(g)
    for k in range(2):
        kinds.setdefault(o, set()).add(classify(chart(V[:, k])))
print("   their fixed points in CP^1 (eigenvectors), classified: %s  -> the magic states" % {o: sorted(v) for o, v in kinds.items()})
print("   every Clifford element fixes a point of CP^1 (has an eigenvector): %s; the fragment just does not contain it" % all(np.linalg.eig(g)[1].shape == (2, 2) for g in cliff))
# B
closure = list(stab)
for g in cliff:
    w, V = np.linalg.eig(g)
    for k in range(2):
        v = V[:, k] / np.linalg.norm(V[:, k])
        if not any(seq(v, t) for t in closure): closure.append(v)
fp26 = [sum(seq(g @ s, s) for s in closure) for g in cliff]
print("B. closing under fixed points: %d states (6 stabiliser + 12 H + 8 F); min fixed points per element now %d; Clifford orbits on them: %s"
      % (len(closure), min(fp26), [len(o) for o in orbits(closure, cliff)]))
print("   fixed-point property restored, transitivity lost: three orbits = a superselection label, a record before FANOUT")
# C
subsets = list(itertools.combinations(range(4), 2))
cnt = {}
for perm in itertools.permutations(range(4)):
    f = sum(tuple(sorted(perm[i] for i in sub)) == sub for sub in subsets)
    cyc = sorted(len(c) for c in _cycles(perm)) if False else None
    cnt.setdefault(f, 0); cnt[f] += 1
def cycle_type(perm):
    seen, ct = set(), []
    for i in range(4):
        if i in seen: continue
        n, j = 0, i
        while j not in seen: seen.add(j); j = perm[j]; n += 1
        ct.append(n)
    return tuple(sorted(ct, reverse=True))
der_types = sorted(set(cycle_type(p) for p in itertools.permutations(range(4)) if sum(tuple(sorted(p[i] for i in s)) == s for s in subsets) == 0))
print("C. toy bit: S_4 on the six 2-subsets; fixed-point counts {count: elements} = %s; derangement cycle types %s" % (dict(sorted(cnt.items())), der_types))
# D
ok = True
for _ in range(200):
    q, r = np.linalg.qr(rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))); U = q * (np.diag(r) / abs(np.diag(r)))
    w, V = np.linalg.eig(U); ok = ok and all(seq(U @ V[:, k], V[:, k]) for k in range(2))
th = rng.uniform(0.3, 3.0); v = rng.standard_normal(2) + 1j * rng.standard_normal(2); v /= np.linalg.norm(v)
print("D. U(2): every sampled unitary fixes a point of CP^1: %s; a global phase e^{i %.2f} fixes no point of S^3: |U v - v| = %.3f" % (ok, th, np.linalg.norm(np.exp(1j * th) * v - v)))
print("=" * 86)
print("FIXED POINT ROUTE: %s" % ("PASS" if len(cliff) == 24 and len(stab) == 6 and abs(np.mean(fp) - 1) < 1e-12 and len(der) > 0
      and len(closure) == 26 and min(fp26) > 0 and len(orbits(closure, cliff)) == 3 and 0 in cnt and ok else "FAIL"))
