"""Executable verification for prop:trace-blind (quantum-numbers section):
the trace direction of the register's phase torus is record-blind, and a
traceless generator, by contrast, acts on records.

Checks: (1) diagonal transport is a global scalar on any classical structure
on C^4; (2) copyables rephase; (3) the induced record channel is independent
of the trace phase; (4) the trace direction's Wilson action on records is the
identity; (5) contrast: the traceless hypercharge pattern diag(-1,1/3,1/3,1/3)
(Tr = 0) moves records. Extends prop:f1-dictionary's computation from C^2 to
the register, dimension-independently.
Run: python3 trace_blind_verification_2026-07-04.py
"""
import numpy as np
rng = np.random.default_rng(11)

A = rng.normal(size=(4,4)) + 1j*rng.normal(size=(4,4))
Q, _ = np.linalg.qr(A)
V = [Q[:,i] for i in range(4)]

def scfa(vs): return sum(np.outer(np.kron(v,v), v.conj()) for v in vs)
def copyable(d, x): return np.allclose(d @ x, np.kron(x,x))
def record(d, rho): return d.conj().T @ np.kron(rho, np.eye(4)) @ d
def report(name, ok): print(("PASS " if ok else "FAIL ") + name); return ok

all_ok = True
d = scfa(V); al = 0.83
U = np.exp(1j*al)*np.eye(4)
dU = np.kron(U,U) @ d @ U.conj().T

all_ok &= report("(1) trace transport is a global scalar", np.allclose(dU, np.exp(1j*al)*d))
all_ok &= report("(2) copyables rephase to e^{ia} v_i", all(copyable(dU, np.exp(1j*al)*v) for v in V))
ok = True
for _ in range(5):
    B = rng.normal(size=(4,4)) + 1j*rng.normal(size=(4,4))
    rho = B @ B.conj().T; rho /= np.trace(rho)
    ok &= np.allclose(record(d, rho), record(dU, rho))
    ok &= np.allclose(U @ rho @ U.conj().T, rho)
all_ok &= report("(3)+(4) record channel and Wilson action blind to the trace phase", ok)

Y = np.diag([-1, 1/3, 1/3, 1/3]).astype(complex)
W = np.diag(np.exp(1j*0.9*np.diag(Y)))
rho = np.outer(sum(V), sum(V).conj()); rho /= np.trace(rho)
all_ok &= report("(5) traceless generator (Tr Y = %.0e) acts on records" % abs(np.trace(Y)),
                 not np.allclose(W @ rho @ W.conj().T, rho))
print("\nALL CHECKS PASS" if all_ok else "\nSOME CHECKS FAILED")
