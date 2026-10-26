#!/usr/bin/env python3
"""
Can a hypodox be assigned a probability greater than one?
Fable session, 2026-10-16T2200.  Session note:
knowledge/sessions/hypodox_probability_above_one_2026-10-16T2200.md

Question (JS): a probability greater than 1 of an event is a negative
probability of the event not happening; consistency with Shannon forced the
complex plane; paradoxes carry complex truth values; can a hypodox carry a
probability greater than one?

What is checked, on C^2 with the record basis Z = {|0>, |1>} ("true" = |0>):

  A. The complement rule and the two surprisals.  P(A) > 1 gives real
     negative information -ln P(A); its complement 1 - P(A) < 0 gives
     -ln|1-P| - i pi.  Only the complement enters the complex plane.
  B. The three Liars and the hypodox as Moebius maps of the amplitude ratio
     x = beta/alpha: x -> 1/x is X (fixed points +-1, the states |+->);
     Kauffman's x -> -1/x is Y (fixed points +-i, the states |+-i>);
     sqrt(NOT) has the same fixed rays as NOT; the hypodox x -> x fixes
     everything.  All four Liar states have Z-probability 1/2 and no Wigner
     negativity; the Kirkwood--Dirac (Z,X) distribution of |+i> is complex
     with non-negative real part.  Negating a sentence conjugates its endomap
     by X and does not exchange paradox with hypodox.
  C. The loop count Tr L: hypodox 2, Liar 0, sign-flipped hypodox -2,
     graded 2 cos(theta/2); diagonal loop weights; the normalised loop
     quasi-probability has real part exactly 1/2 for every one-qubit loop,
     so a loop closed on itself never carries a real part above one.
  D. The Kirkwood--Dirac conditional quasi-probability of the sentence's
     value between the agent's pre-FANOUT state |i> and the record outcome
     <f|: q(a|i,f) = <f|a><a|i>/<f|i>.  Sums to one; Born marginals; equals
     0 or 1 when the record is in the sentence's own basis; equals the
     l^1-normalised amplitude psi_a/(psi_0+psi_1) when the record is |+>;
     at the Kauffman phase phi = pi/2 it is p - i sqrt(p(1-p)); at
     phi = pi it exceeds one with a negative complement; it diverges as the
     boundary pair approaches the Liar's (|i> -> |->, <f| = <+|).  The
     three-box values (1, 1, -1).  The identity
     sum_a |q(a|i,f)|^2 = P_FANOUT(f|i) / P_no-FANOUT(f|i).
  E. Surprisals of the anomalous values: real negative for q > 1, -i pi for
     q < 0, and at the Kauffman phase |q(a)|^2 = Born p(a), so the real
     part of the surprisal is half the Born surprisal.

Seed 20261016 for the random states used in the identities.  No hidden
state.  Final line "HYPODOX PROBABILITY ABOVE ONE: PASS" or "... FAIL".
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True, linewidth=120)
rng = np.random.default_rng(20261016)
ok = True

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
K0 = np.array([1, 0], dtype=complex)
K1 = np.array([0, 1], dtype=complex)
PLUS = (K0 + K1) / np.sqrt(2)
MINUS = (K0 - K1) / np.sqrt(2)
PLUSI = (K0 + 1j * K1) / np.sqrt(2)
MINUSI = (K0 - 1j * K1) / np.sqrt(2)


def check(cond, msg):
    global ok
    ok = ok and bool(cond)
    print(("   ok  " if cond else "   FAIL") + " " + msg)


def ip(a, b):
    return np.vdot(a, b)


def bloch(psi):
    rho = np.outer(psi, psi.conj())
    return np.real(np.array([np.trace(rho @ X), np.trace(rho @ Y), np.trace(rho @ Z)]))


def wigner_min(b):
    """Minimum over the eight Wootters sign conventions of the qubit Wigner function
    W = (1 + s_z z + s_x x + s_y y)/4 (same helper as the 2026-10-16T1100 script)."""
    x, y, z = b
    return min((1 + sz * z + sx * x + sy * y) / 4 for sz in (1, -1) for sx in (1, -1) for sy in (1, -1))


def kd_joint(rho, basis_a, basis_b):
    """Kirkwood--Dirac joint quasi-probability Q[a,b] = <b|a><a|rho|b>."""
    return np.array([[ip(b, a) * (a.conj() @ rho @ b) for b in basis_b] for a in basis_a])


def kd_cond(a, i, f):
    """Conditional Kirkwood--Dirac quasi-probability of the value a between
    pre-selection |i> and post-selection <f|: <f|a><a|i>/<f|i>."""
    return ip(f, a) * ip(a, i) / ip(f, i)


def surprisal(q):
    """-log q on the principal branch: real for q > 0, -ln|q| - i pi for q < 0."""
    return -np.log(complex(q))


def random_state():
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    return v / np.linalg.norm(v)


def psi(p, phi):
    return np.sqrt(p) * K0 + np.sqrt(1 - p) * np.exp(1j * phi) * K1


def same_ray(u, v):
    return abs(abs(ip(u, v)) - 1) < 1e-12


def rot(n, theta):
    n = np.asarray(n, float) / np.linalg.norm(n)
    return np.cos(theta / 2) * I2 - 1j * np.sin(theta / 2) * (n[0] * X + n[1] * Y + n[2] * Z)


# ----------------------------------------------------------------------------
print("A. the complement rule and the two surprisals")
for P in (1.5, 2.0, 2.895):
    Q = 1 - P
    IP, IQ = surprisal(P), surprisal(Q)
    print("   P(A) = %.3f  I(A) = %+.4f%+.4fi ;  P(not A) = %+.3f  I(not A) = %+.4f%+.4fi"
          % (P, IP.real, IP.imag, Q, IQ.real, IQ.imag))
    check(abs(IP.imag) < 1e-12 and IP.real < 0, "an event with P > 1 has real, negative information")
    check(abs(abs(IQ.imag) - np.pi) < 1e-12 and abs(np.exp(-IQ) - Q) < 1e-12,
          "its complement has complex information, imaginary part -i pi, and exp(-I) recovers 1 - P")
check(abs(surprisal(-1.0) - 1j * (-np.pi)) < 1e-12, "the anti-event of weight -1 has surprisal -i pi on this branch (the 09-16 note's i pi up to the branch sign)")

# ----------------------------------------------------------------------------
print("B. three Liars and the hypodox as Moebius maps of the amplitude ratio x = beta/alpha")
M_inv = np.array([[0, 1], [1, 0]], dtype=complex)      # x -> 1/x
M_kauff = np.array([[0, -1], [1, 0]], dtype=complex)   # x -> -1/x
check(np.allclose(M_inv, X), "x -> 1/x is the Liar endomap X")
check(np.allclose(M_kauff, -1j * Y), "Kauffman's x -> -1/x is Y up to the phase -i")
# fixed points of the Moebius maps and the states they name
for name, x in (("x = +1", 1), ("x = -1", -1), ("x = +i", 1j), ("x = -i", -1j)):
    st = (K0 + x * K1) / np.sqrt(2)
    tgt = {1: PLUS, -1: MINUS, 1j: PLUSI, -1j: MINUSI}[x]
    print("   %s -> state %s, Bloch %s, Z-probabilities %s, Wigner min %.4f"
          % (name, np.round(st, 4), np.round(bloch(st), 3), np.round(np.abs(st) ** 2, 3), wigner_min(bloch(st))))
    check(same_ray(st, tgt), "the Moebius fixed point names the expected stabiliser state")
    check(abs(abs(st[0]) ** 2 - 0.5) < 1e-12, "its Z-probability is 1/2 (the Kleene gap)")
    check(wigner_min(bloch(st)) > -1e-12, "no Wigner negativity in any convention")
check(same_ray(X @ PLUS, PLUS) and same_ray(X @ MINUS, MINUS), "x = +-1 are the fixed rays of X (the Liar)")
check(same_ray(Y @ PLUSI, PLUSI) and same_ray(Y @ MINUSI, MINUSI), "x = +-i are the fixed rays of Y (Kauffman's Liar)")
SQNOT = (1 + 1j) / 2 * I2 + (1 - 1j) / 2 * X
check(np.allclose(SQNOT @ SQNOT, X), "sqrt(NOT) = (1+i)/2 I + (1-i)/2 X squares to NOT")
check(same_ray(SQNOT @ PLUS, PLUS) and same_ray(SQNOT @ MINUS, MINUS),
      "sqrt(NOT) has the Liar's fixed rays |+->; Kauffman's i is not its fixed point but Y's")
S = np.diag([1, 1j]).astype(complex)
check(same_ray(S @ PLUS, PLUSI), "|+i> = S|+>: the complex truth value is a quarter-turn phase on the Liar's state")
Q_kauff = kd_joint(np.outer(PLUSI, PLUSI.conj()), [K0, K1], [PLUS, MINUS])
Q_liar = kd_joint(np.outer(PLUS, PLUS.conj()), [K0, K1], [PLUS, MINUS])
print("   KD(Z,X) of |+> (the Liar's state):\n", np.round(Q_liar, 4))
print("   KD(Z,X) of |+i> (Kauffman's state):\n", np.round(Q_kauff, 4))
check(np.allclose(Q_liar.imag, 0) and (Q_liar.real >= -1e-12).all(), "the Liar's state has a real, non-negative KD(Z,X)")
check(np.allclose(Q_kauff.real, 0.25) and np.allclose(np.abs(Q_kauff.imag), 0.25) and abs(Q_kauff.sum() - 1) < 1e-12,
      "Kauffman's state has KD(Z,X) entries (1 +- i)/4: complex, real part non-negative, summing to one")
# negation conjugates the endomap by X
check(np.allclose(X @ I2 @ X, I2) and np.allclose(X @ X @ X, X) and np.allclose(X @ Y @ X, -Y),
      "negating the sentence conjugates its endomap by X: the hypodox stays a hypodox, each Liar stays a Liar")

# ----------------------------------------------------------------------------
print("C. the loop count and the loop quasi-probability")
loops = (("hypodox  I", I2), ("Liar     X", X), ("Kauffman Y", Y), ("sqrt(NOT)", SQNOT), ("anti-hypodox -I", -I2))
for name, L in loops:
    t = np.trace(L)
    dz = [np.real_if_close(a.conj() @ L @ a) for a in (K0, K1)]
    dx = [np.real_if_close(a.conj() @ L @ a) for a in (PLUS, MINUS)]
    print("   %-16s Tr L = %s ; Z-weights %s ; X-weights %s ; P-CTC success |Tr L|^2/4 = %.3f"
          % (name, np.round(t, 4), np.round(dz, 4), np.round(dx, 4), abs(t) ** 2 / 4))
check(abs(np.trace(I2) - 2) < 1e-12 and abs(np.trace(X)) < 1e-12 and abs(np.trace(-I2) + 2) < 1e-12,
      "counts: hypodox 2, Liar 0, sign-flipped hypodox -2")
check(abs((PLUS.conj() @ X @ PLUS) - 1) < 1e-12 and abs((MINUS.conj() @ X @ MINUS) + 1) < 1e-12,
      "the Liar's zero count is +1 on |+> and -1 on |->: a signed pair that cancels")
check(abs(abs(np.trace(SQNOT)) - np.sqrt(2)) < 1e-12, "the half-Liar's count is 1 + i, modulus sqrt 2")
for theta in (0.0, 1.0, 2.0, np.pi, 2 * np.pi):
    check(abs(np.trace(rot([1, 0, 0], theta)) - 2 * np.cos(theta / 2)) < 1e-12,
          "graded count 2 cos(theta/2) at theta = %.3f : %+.4f" % (theta, 2 * np.cos(theta / 2)))
# normalised loop quasi-probability q(a) = <a|L|a>/Tr L
worst = 0.0
for _ in range(200):
    n = rng.normal(size=3)
    theta = rng.uniform(0.05, np.pi - 0.05)
    L = rot(n, theta)
    q0 = (K0.conj() @ L @ K0) / np.trace(L)
    nz = n[2] / np.linalg.norm(n)
    worst = max(worst, abs(q0 - (0.5 - 0.5j * nz * np.tan(theta / 2))))
check(worst < 1e-9, "for a rotation about n the loop quasi-probability of |0> is 1/2 - (i/2) n_z tan(theta/2): real part exactly 1/2 (worst residual %.1e)" % worst)
print("   the loop quasi-probability has a pole at theta = pi (the Liar, Tr L = 0) and real part 1/2 everywhere else")

# ----------------------------------------------------------------------------
print("D. the sentence's value between the pre-FANOUT state and the record: Kirkwood--Dirac")
# sums to one, Born marginals
worst_sum = worst_marg = 0.0
for _ in range(100):
    i = random_state()
    U = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))[0]
    fbasis = [U[:, 0], U[:, 1]]
    for f in fbasis:
        worst_sum = max(worst_sum, abs(sum(kd_cond(a, i, f) for a in (K0, K1)) - 1))
    for a in (K0, K1):
        marg = sum(abs(ip(f, i)) ** 2 * kd_cond(a, i, f) for f in fbasis)
        worst_marg = max(worst_marg, abs(marg - abs(ip(a, i)) ** 2))
check(worst_sum < 1e-12, "q(0|i,f) + q(1|i,f) = 1 for random boundaries (worst %.1e)" % worst_sum)
check(worst_marg < 1e-12, "averaging q over the record outcomes with their Born weights returns the Born probability of a (worst %.1e)" % worst_marg)
# own basis: 0 or 1
worst_own = 0.0
for _ in range(50):
    i = random_state()
    for f in (K0, K1):
        for a in (K0, K1):
            worst_own = max(worst_own, abs(kd_cond(a, i, f) - (1.0 if np.allclose(a, f) else 0.0)))
check(worst_own < 1e-12, "a record in the sentence's own basis gives q = 0 or 1: a hypodox read in its own basis is never anomalous")
# the complementary record: l^1-normalised amplitude
worst_l1 = 0.0
for _ in range(50):
    i = random_state()
    for a, k in ((K0, 0), (K1, 1)):
        worst_l1 = max(worst_l1, abs(kd_cond(a, i, PLUS) - i[k] / (i[0] + i[1])))
check(worst_l1 < 1e-12, "a record reading |+> gives q(a) = psi_a / (psi_0 + psi_1): the amplitude normalised in l^1, not l^2")
p = 0.7
print("   p = %.2f ; the record reads |+> ; q(true) and q(false) against the Kauffman phase phi:" % p)
for phi in (0.0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi):
    i = psi(p, phi)
    q0, q1 = kd_cond(K0, i, PLUS), kd_cond(K1, i, PLUS)
    anomalous = (abs(q0.imag) > 1e-12) or q0.real > 1 + 1e-12 or q0.real < -1e-12
    print("      phi = %.4f : q(true) = %+.4f%+.4fi  q(false) = %+.4f%+.4fi  |q(true)|^2 = %.4f  %s"
          % (phi, q0.real, q0.imag, q1.real, q1.imag, abs(q0) ** 2, "outside [0,1]" if anomalous else "inside [0,1]"))
i0 = psi(p, 0.0)
check(0 <= kd_cond(K0, i0, PLUS).real <= 1 and abs(kd_cond(K0, i0, PLUS).imag) < 1e-12, "phi = 0: ordinary, inside [0,1]")
ik = psi(p, np.pi / 2)
qk = kd_cond(K0, ik, PLUS)
check(abs(qk - (p - 1j * np.sqrt(p * (1 - p)))) < 1e-12, "phi = pi/2 (Kauffman's i): q(true) = p - i sqrt(p(1-p)): real part the Born probability, imaginary part the coherence")
check(abs(abs(qk) ** 2 - p) < 1e-12, "phi = pi/2: |q(true)|^2 = p, the modulus of the quasi-probability is the modulus of the amplitude")
ipi = psi(p, np.pi)
q0, q1 = kd_cond(K0, ipi, PLUS), kd_cond(K1, ipi, PLUS)
check(q0.real > 1 and abs(q0.imag) < 1e-12 and q1.real < 0 and abs(q0 + q1 - 1) < 1e-12,
      "phi = pi: q(true) = %.4f > 1 and q(false) = %.4f < 0, summing to one: the probability above one and the negative complement are one configuration" % (q0.real, q1.real))
check(abs(q0 - np.sqrt(p) / (np.sqrt(p) - np.sqrt(1 - p))) < 1e-12, "phi = pi: q(true) = sqrt p / (sqrt p - sqrt(1-p))")
print("   approach to the Liar's boundary pair (phi = pi, p -> 1/2 from above; <f| = <+|, |i> -> |->):")
for d in (0.1, 0.01, 0.001, 0.0001):
    i = psi(0.5 + d, np.pi)
    q0 = kd_cond(K0, i, PLUS)
    print("      p = 1/2 + %-7g : q(true) = %10.3f   1/(2 d) = %10.3f   |<+|i>|^2 = %.2e" % (d, q0.real, 1 / (2 * d), abs(ip(PLUS, i)) ** 2))
check(abs(ip(PLUS, MINUS)) < 1e-12, "at p = 1/2 the pre-FANOUT state is |-> and the record |+>: the pole is the Liar's boundary pair, <+|X|+> read as <+|->")
i = psi(0.5 + 1e-4, np.pi)
check(kd_cond(K0, i, PLUS).real > 1000, "the value exceeds one without bound as the boundary pair approaches the Liar's")
# the three-box paradox
A, B, C = np.eye(3, dtype=complex)
i3 = (A + B + C) / np.sqrt(3)
f3 = (A + B - C) / np.sqrt(3)
qa, qb, qc = (kd_cond(v, i3, f3) for v in (A, B, C))
print("   three-box (Aharonov--Vaidman): q(A) = %+.3f  q(B) = %+.3f  q(C) = %+.3f  q(A or B) = %+.3f" % (qa.real, qb.real, qc.real, (qa + qb).real))
check(abs(qa - 1) < 1e-12 and abs(qb - 1) < 1e-12 and abs(qc + 1) < 1e-12, "three-box: 1, 1, -1 ; the event 'A or B' has quasi-probability 2 and its complement -1")
# the FANOUT identity: sum_a |q(a|i,f)|^2 = P_FANOUT(f|i) / P_no-FANOUT(f|i)
worst_id = 0.0
for _ in range(100):
    i = random_state()
    f = random_state()
    lhs = sum(abs(kd_cond(a, i, f)) ** 2 for a in (K0, K1))
    p_fan = sum(abs(ip(f, a)) ** 2 * abs(ip(a, i)) ** 2 for a in (K0, K1))   # a Z-FANOUT fired between i and f
    p_no = abs(ip(f, i)) ** 2                                              # no FANOUT fired
    worst_id = max(worst_id, abs(lhs - p_fan / p_no))
check(worst_id < 1e-9, "sum_a |q(a|i,f)|^2 = P(f | FANOUT fired in the sentence's basis) / P(f | no FANOUT) (worst %.1e)" % worst_id)
lhs3 = sum(abs(q) ** 2 for q in (qa, qb, qc))
check(abs(lhs3 - 3) < 1e-12, "three-box: the ratio is 3 = (1/3) / (1/9): the post-selected outcome is three times likelier with a record in the box basis than without")
print("   a modulus above one forces the ratio above one: the record outcome is likelier with an intermediate FANOUT than without, destructive interference across the sentence's values; the Liar is the ratio's pole")

# ----------------------------------------------------------------------------
print("E. surprisals of the anomalous values")
i = psi(p, np.pi)
q0, q1 = kd_cond(K0, i, PLUS), kd_cond(K1, i, PLUS)
I0, I1 = surprisal(q0), surprisal(q1)
print("   phi = pi : I(true) = %+.4f%+.4fi   I(false) = %+.4f%+.4fi" % (I0.real, I0.imag, I1.real, I1.imag))
check(abs(I0.imag) < 1e-12 and I0.real < 0, "the value with q > 1 has real negative information")
check(abs(abs(I1.imag) - np.pi) < 1e-12, "its complement with q < 0 carries the i pi")
i = psi(p, np.pi / 2)
q0 = kd_cond(K0, i, PLUS)
I0 = surprisal(q0)
print("   phi = pi/2: I(true) = %+.4f%+.4fi ; half the Born surprisal -ln(p)/2 = %+.4f ; arctan(sqrt((1-p)/p)) = %+.4f"
      % (I0.real, I0.imag, -np.log(p) / 2, np.arctan(np.sqrt((1 - p) / p))))
check(abs(I0.real + np.log(p) / 2) < 1e-12, "at the Kauffman phase the real part of the surprisal is half the Born surprisal, -ln|psi_true|")
check(abs(I0.imag - np.arctan(np.sqrt((1 - p) / p))) < 1e-12, "and the imaginary part is the angle of the amplitude against the sum of amplitudes")
for phi in (0.0, np.pi / 2, np.pi):
    i = psi(p, phi)
    qs = [kd_cond(a, i, PLUS) for a in (K0, K1)]
    Hkd = -sum(q * np.log(complex(q)) for q in qs)
    print("   phi = %.4f : -sum q ln q = %+.4f%+.4fi  (Born H(p) = %.4f nat)" % (phi, Hkd.real, Hkd.imag, -(p * np.log(p) + (1 - p) * np.log(1 - p))))

print("HYPODOX PROBABILITY ABOVE ONE: %s" % ("PASS" if ok else "FAIL"))
