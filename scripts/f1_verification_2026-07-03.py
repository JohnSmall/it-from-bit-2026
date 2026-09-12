"""Executable verification for the F1 lemma of op:hopf-frobenius
(the one-qubit dictionary: dagger-SCFAs on C^2 <-> lifted antipodal skeletons
of the complex Hopf bundle S^3 -> S^2).

Checks map to the lemma parts in f1_scfa_hopf_dictionary_2026-07-03.md:
  1-2 -> (a) bijection and phase-pinning (copyables are vectors, not rays)
  3   -> (b) U(2)-equivariance of the correspondence
  4   -> (b) the centre acts non-trivially (lifts are recorded)
  5   -> (c) induced channel = skeleton dephasing, independent of the section
  6   -> (c) structures over a fixed skeleton form a Map(P,U(1))-torsor
  (specialness, coassociativity, cocommutativity asserted throughout)
Run: python3 f1_verification_2026-07-03.py   (prints PASS/FAIL per check)
"""
import numpy as np

rng = np.random.default_rng(7)
k0 = np.array([1, 0], complex); k1 = np.array([0, 1], complex)

def scfa(v0, v1):
    """Copy map (4x2) of the dagger-SCFA whose copyables are the basis {v0,v1}."""
    return (np.outer(np.kron(v0, v0), v0.conj())
            + np.outer(np.kron(v1, v1), v1.conj()))

def copyable(d, x): return np.allclose(d @ x, np.kron(x, x))

def axioms(d):
    mu, I2 = d.conj().T, np.eye(2)
    S = np.zeros((4, 4)); S[0, 0] = S[3, 3] = 1; S[1, 2] = S[2, 1] = 1
    return (np.allclose(mu @ d, I2),                                   # special
            np.allclose(np.kron(d, I2) @ d, np.kron(I2, d) @ d),        # coassociative
            np.allclose(S @ d, d))                                      # cocommutative

def dephase(d, rho): return d.conj().T @ np.kron(rho, np.eye(2)) @ d

def report(name, ok): print(("PASS " if ok else "FAIL ") + name); return ok

all_ok = True
d0 = scfa(k0, k1)
th = 0.7

# 1-2: bijection + phase-pinning
ok = copyable(d0, k0) and copyable(d0, k1) and not copyable(d0, np.exp(1j*th)*k0)
w0 = np.exp(1j*th)*k0
d1 = scfa(w0, k1)
ok &= (not np.allclose(d1, d0)) and copyable(d1, w0) and not copyable(d1, k0)
ok &= all(axioms(d0)) and all(axioms(d1))
all_ok &= report("(a) copyables are vectors, not rays; rephased basis = distinct valid SCFA", ok)

# 3: U(2)-equivariance
ok = True
for _ in range(5):
    A = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
    U, _ = np.linalg.qr(A)
    dU = np.kron(U, U) @ d0 @ U.conj().T
    ok &= all(axioms(dU)) and copyable(dU, U@k0) and copyable(dU, U@k1) and not copyable(dU, k0)
all_ok &= report("(b) U(2)-transport: valid SCFA with copyables {Uv0, Uv1}", ok)

# 4: the centre moves the structure (lift data recorded)
al = 0.9
Uc = np.exp(1j*al)*np.eye(2)
dc = np.kron(Uc, Uc) @ d0 @ Uc.conj().T
ok = np.allclose(dc, np.exp(1j*al)*d0) and copyable(dc, np.exp(1j*al)*k0)
all_ok &= report("(b) centre e^{ia}id: delta -> e^{ia} delta, copyables -> e^{ia}v_i", ok)

# 5: induced channel = skeleton dephasing, section-independent
P0, P1 = np.outer(k0, k0.conj()), np.outer(k1, k1.conj())
dP = scfa(np.exp(1.1j)*k0, np.exp(-0.4j)*k1)
ok = not np.allclose(dP, d0)
for _ in range(5):
    B = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
    rho = B @ B.conj().T; rho /= np.trace(rho)
    ok &= np.allclose(dephase(d0, rho), P0@rho@P0 + P1@rho@P1)
    ok &= np.allclose(dephase(d0, rho), dephase(dP, rho))
all_ok &= report("(c) Delta_delta = skeleton dephasing; identical for all sections", ok)

# 6: torsor over a fixed skeleton
ds, ok = [], True
for t0 in (0.0, 0.7, 2.1):
    for t1 in (0.0, -1.3):
        dd = scfa(np.exp(1j*t0)*k0, np.exp(1j*t1)*k1)
        ok &= all(axioms(dd)); ds.append(dd)
ok &= all(not np.allclose(ds[i], ds[j]) for i in range(len(ds)) for j in range(i+1, len(ds)))
all_ok &= report("(c) fixed skeleton: every phase pair a valid, distinct SCFA (torsor)", ok)

print("\nALL CHECKS PASS" if all_ok else "\nSOME CHECKS FAILED")
