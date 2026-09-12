#!/usr/bin/env python3
"""
Notebook T -- the trigintaduonion constructor.  2026-08-27.

QUESTION (ledger item, Notebook T): when the sedenions S = A_4 are doubled
to the trigintaduonions T = A_5, does the automorphism group gain a
further S_3 (Brown's finite factor again) or only the Z/2 of the doubling
involution?  Eakin--Sathaye state the general step as
Aut(A_{n+1}) = Aut(A_n) x G with G in {Z/2, S_3}; which branch applies
over the reals decides whether "the fifth wire adds nothing new in kind"
can be stated at citation grade.

METHOD.  Brown's three maps on A_n = A_{n-1} (+) A_{n-1} u, written
x = (a, b) for a + b u (Gresnigt--Gourlay--Varma 2023, eqs 42--44, quoting
Brown 1967):
    theta'(a, b) = (theta a, theta b)                     (lift)
    eps(a, b)    = (a, -b)                                (doubling involution)
    psi(a, b)    = ( [a + 3a* + sqrt3 (b - b*)]/4,
                     [b + 3b* - sqrt3 (a - a*)]/4 )       (order three)
psi fixes 1 and u and rotates every (a, a u) plane, a imaginary, by 120
degrees.  We verify directly, on every pair of basis units:
  (T1) psi is an algebra automorphism of A_n for n = 3, 4, 5, 6;
  (T2) psi^3 = id, eps^2 = id, eps psi = psi^2 eps  (so <eps, psi> = S_3);
  (T3) psi is NOT a lift theta': it mixes the two halves;
  (T4) the new S_3 at rung n commutes with the lifted S_3 from rung n-1
       (direct product), for n = 5 and 6;
  (T5) dim Der(A_n) = 14 for n = 3, 4, 5  (identity component stays G_2;
       Schafer / Brown), against 3 at n = 2 and 0 at n = 1.
(T1)-(T4) settle the branch: S_3 at every rung >= 4 over R.
PART B / PART C (added the same day, after the check exposed it):
  which triple of octonion subalgebras Brown's S_3 permutes.  The
  corpus's mechanism used the core triple (core (+) V_i); Part B
  shows that triple is permuted by a lifted G_2 element (the
  colour-line 3-cycle) and stabilised by Brown's S_3; Part C shows
  the doubling's S_3 permutes the three halvings O, psi O, psi^2 O.
  INVALID ROUTE LOGGED: 'generations = the three copies through the
  H-core, permuted by the doubling's S_3' -- the copies are colour.  (T5) is
the continuous half: no new derivations, hence no new connected
symmetry, hence no new force, at the fifth rung or beyond (checked to
five; the sixth is Brown's).

Equality Aut(A_{n-1}) x S_3 = Aut(A_n) for n = 4, 5, 6 is Brown's
theorem and is CITED, not computed here; this notebook verifies the
INCLUSION and the direct-product structure, plus the derivation count.

Conventions: the corpus Cayley--Dickson recursion
    (a, b)(c, d) = (a c - conj(d) b,  d a + b conj(c)),
    conj(a, b)   = (conj(a), -b),
basis ordering e_0 = 1, ..., e_{2^n - 1}; the doubling unit of rung n is
e_{2^{n-1}} = (0, 1).  Pure numpy.  Tolerance 1e-10.
"""
import sys
import numpy as np

TOL = 1e-10
SQ3 = np.sqrt(3.0)


# ---------------------------------------------------------------------
# Cayley--Dickson arithmetic on real vectors of length 2^n
# ---------------------------------------------------------------------
def cd_conj(x):
    x = np.asarray(x, dtype=float)
    c = -x.copy()
    c[0] = x[0]
    return c


def cd_mul(x, y):
    """Recursive Cayley--Dickson product, corpus convention."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = x.shape[0]
    if n == 1:
        return x * y
    h = n // 2
    a, b = x[:h], x[h:]
    c, d = y[:h], y[h:]
    first = cd_mul(a, c) - cd_mul(cd_conj(d), b)
    second = cd_mul(d, a) + cd_mul(b, cd_conj(c))
    return np.concatenate([first, second])


def basis(n):
    N = 2 ** n
    return [np.eye(N)[:, i] for i in range(N)]


def mult_table(n):
    """Signed structure: e_i e_j = sgn * e_k.  Returns (K, SGN) arrays."""
    N = 2 ** n
    E = basis(n)
    K = np.zeros((N, N), dtype=int)
    SGN = np.zeros((N, N), dtype=float)
    for i in range(N):
        for j in range(N):
            p = cd_mul(E[i], E[j])
            nz = np.flatnonzero(np.abs(p) > 0.5)
            assert nz.size == 1, "basis product not a signed unit"
            K[i, j] = nz[0]
            SGN[i, j] = p[nz[0]]
    return K, SGN


# ---------------------------------------------------------------------
# Brown's maps on A_n = A_{n-1} (+) A_{n-1} u  (as N x N matrices)
# ---------------------------------------------------------------------
def brown_maps(n):
    N = 2 ** n
    h = N // 2
    E = basis(n)

    def psi_vec(x):
        a, b = x[:h], x[h:]
        ac, bc = cd_conj(a), cd_conj(b)
        first = (a + 3 * ac + SQ3 * (b - bc)) / 4.0
        second = (b + 3 * bc - SQ3 * (a - ac)) / 4.0
        return np.concatenate([first, second])

    def eps_vec(x):
        y = x.copy()
        y[h:] = -y[h:]
        return y

    PSI = np.column_stack([psi_vec(e) for e in E])
    EPS = np.column_stack([eps_vec(e) for e in E])
    return PSI, EPS


def lift(M):
    """theta' : (a, b) -> (theta a, theta b), block-diagonal lift to A_{n+1}."""
    Z = np.zeros_like(M)
    return np.block([[M, Z], [Z, M]])


def is_automorphism(M, n):
    """Check M(e_i e_j) = M(e_i) M(e_j) on all basis pairs."""
    N = 2 ** n
    E = basis(n)
    worst = 0.0
    for i in range(N):
        Mi = M @ E[i]
        for j in range(N):
            lhs = M @ cd_mul(E[i], E[j])
            rhs = cd_mul(Mi, M @ E[j])
            worst = max(worst, np.max(np.abs(lhs - rhs)))
    return worst < TOL, worst


# ---------------------------------------------------------------------
# Derivation algebra dimension:  D(xy) = D(x) y + x D(y)
# Unknown D is N x N; equations are sparse (signed permutations).
# Build the normal matrix A^T A (N^2 x N^2) and count null directions.
# ---------------------------------------------------------------------
def derivation_dim(n):
    N = 2 ** n
    K, SGN = mult_table(n)
    # index of unknown D[m, i] is m + N*i
    rows = []
    # For each (i, j) and each component m:
    #   D[m, k]*s_ij  -  (D(e_i) e_j)[m]  -  (e_i D(e_j))[m] = 0
    # (D(e_i) e_j)[m] = sum_p D[p,i] (e_p e_j)[m] = D[p,i]*SGN[p,j] where K[p,j]=m
    # (e_i D(e_j))[m] = sum_q D[q,j] (e_i e_q)[m] = D[q,j]*SGN[i,q] where K[i,q]=m
    # Precompute inverses: for fixed j, the map p -> K[p,j] is a bijection.
    invR = np.zeros((N, N), dtype=int)  # invR[m, j] = p with K[p, j] = m
    invL = np.zeros((N, N), dtype=int)  # invL[i, m] = q with K[i, q] = m
    for j in range(N):
        for p in range(N):
            invR[K[p, j], j] = p
    for i in range(N):
        for q in range(N):
            invL[i, K[i, q]] = q
    ATA = np.zeros((N * N, N * N))
    for i in range(N):
        for j in range(N):
            k, s = K[i, j], SGN[i, j]
            for m in range(N):
                p = invR[m, j]
                q = invL[i, m]
                # row vector with three entries
                cols = [m + N * k, p + N * i, q + N * j]
                vals = [s, -SGN[p, j], -SGN[i, q]]
                # accumulate outer product into ATA
                for c1, v1 in zip(cols, vals):
                    for c2, v2 in zip(cols, vals):
                        ATA[c1, c2] += v1 * v2
    w = np.linalg.eigvalsh(ATA)
    return int(np.sum(w < 1e-8))


# ---------------------------------------------------------------------
# PART B -- which S_3 permutes which triple (the two-triples check).
# The corpus's sedenion mechanism used the CORE TRIPLE: three octonion
# copies  core (+) V_i  through the quaternion core <1, e4, e8, e12>
# (Gillard--Gresnigt 2019's split; notebook M's V_i).  Question: is that
# triple permuted by Brown's new S_3, or by something already in G_2?
# ---------------------------------------------------------------------
def part_B():
    n, N = 4, 16
    E = basis(n)
    PSI, EPS = brown_maps(n)
    I = np.eye(N)
    core = [0, 4, 8, 12]
    V = {1: [1, 5, 9, 13], 2: [2, 6, 10, 14], 3: [3, 7, 11, 15]}

    def in_span(vec, idxs):
        mask = np.ones(N, bool); mask[idxs] = False
        return np.max(np.abs(vec[mask])) < 1e-10

    stab = {"core": all(in_span(PSI @ E[i], core) for i in core)}
    for k in (1, 2, 3):
        stab["V_%d" % k] = all(in_span(PSI @ E[i], V[k]) for i in V[k])
    S3 = [I, PSI, PSI @ PSI, EPS, EPS @ PSI, EPS @ PSI @ PSI]
    any_permutes = any(all(in_span(M @ E[i], V[2]) for i in V[1]) for M in S3)

    # the colour-line 3-cycle in G_2 = Aut(O), fixing e4 (hence in its SU(3)):
    # e1->e2->e3->e1, e5->e6->e7->e5, e4 fixed; lifted diagonally to S.
    sig_O = np.zeros((8, 8)); sig_O[0, 0] = 1; sig_O[4, 4] = 1
    for a, b in ((1, 2), (2, 3), (3, 1), (5, 6), (6, 7), (7, 5)):
        sig_O[b, a] = 1
    ok_O, _ = is_automorphism(sig_O, 3)
    SIG = lift(sig_O)
    ok_S, _ = is_automorphism(SIG, 4)
    fixes_core = all(np.allclose(SIG @ E[i], E[i]) for i in core)
    cycles = (all(in_span(SIG @ E[i], V[2]) for i in V[1]) and
              all(in_span(SIG @ E[i], V[3]) for i in V[2]) and
              all(in_span(SIG @ E[i], V[1]) for i in V[3]))
    commutes = np.allclose(SIG @ PSI, PSI @ SIG)
    fixdim = N - np.linalg.matrix_rank(PSI - I)

    print("PART B -- the two triples")
    print("  Brown psi_4 stabilises setwise: core=%s V_1=%s V_2=%s V_3=%s"
          % (stab["core"], stab["V_1"], stab["V_2"], stab["V_3"]))
    print("  Any element of Brown's S_3 carries V_1 into V_2: %s" % any_permutes)
    print("  Colour-line 3-cycle sigma: automorphism of O: %s; lifted to S: %s;"
          " fixes core pointwise: %s; cycles V_1->V_2->V_3->V_1: %s;"
          " commutes with psi: %s" % (ok_O, ok_S, fixes_core, cycles, commutes))
    print("  Fix(psi_4) = span{e0, e8}: dimension %d" % fixdim)
    verdict = (all(stab.values()) and not any_permutes and ok_S and
               fixes_core and cycles and commutes and fixdim == 2)
    print("  VERDICT B: the core triple is permuted INSIDE G_2 (colour), "
          "not by the doubling's S_3: %s" % verdict)
    return verdict


# ---------------------------------------------------------------------
# PART C -- the triple Brown's S_3 does permute: the three halvings
# O, psi(O), psi^2(O) of S, all doubled by the same fixed unit e8.
# ---------------------------------------------------------------------
def part_C():
    n, N = 4, 16
    E = basis(n)
    PSI, EPS = brown_maps(n)
    O = np.column_stack(E[:8])
    halvings = [O, PSI @ O, PSI @ PSI @ O]

    def is_subalgebra(S):
        Q, _ = np.linalg.qr(S); P = Q @ Q.T
        for i in range(S.shape[1]):
            for j in range(S.shape[1]):
                p = cd_mul(S[:, i], S[:, j])
                if np.max(np.abs(P @ p - p)) > 1e-9:
                    return False
        return True

    def dim_intersection(*subs):
        comps = []
        for S in subs:
            Q, _ = np.linalg.qr(S)
            comps.append(np.eye(N) - Q @ Q.T)
        return N - np.linalg.matrix_rank(np.vstack(comps), tol=1e-9)

    subalg = all(is_subalgebra(H) for H in halvings)
    pair = dim_intersection(halvings[0], halvings[1])
    triple = dim_intersection(*halvings)
    regen = all(np.linalg.matrix_rank(np.hstack(
        [H, np.column_stack([cd_mul(H[:, i], E[8]) for i in range(8)])]),
        tol=1e-9) == 16 for H in halvings)
    # the three involutions eps psi^k fix the three halvings pointwise, one each
    invs = [EPS @ np.linalg.matrix_power(PSI, k) for k in range(3)]
    fixtable = [[np.allclose(inv @ H, H) for H in halvings] for inv in invs]
    one_each = all(sum(row) == 1 for row in fixtable) and \
               all(sum(col) == 1 for col in zip(*fixtable))
    print("PART C -- the psi-orbit triple")
    print("  O, psi(O), psi^2(O) octonion subalgebras: %s" % subalg)
    print("  dim pairwise intersection: %d; dim triple intersection: %d "
          "(the real line)" % (pair, triple))
    print("  each halving with e8 regenerates S (S = H (+) H e8): %s" % regen)
    print("  eps psi^k fixes halving k pointwise, one each: %s" % one_each)
    verdict = subalg and pair == 1 and triple == 1 and regen and one_each
    print("  VERDICT C: Brown's S_3 permutes the three halvings of S through "
          "the fixed doubling unit: %s" % verdict)
    return verdict


# ---------------------------------------------------------------------
def main():
    np.set_printoptions(precision=4, suppress=True)
    print("Notebook T -- trigintaduonion automorphisms (2026-08-27)")
    print("=" * 66)

    results = {}
    prev_PSI = prev_EPS = None
    for n in (3, 4, 5, 6):
        N = 2 ** n
        PSI, EPS = brown_maps(n)
        ok_psi, w_psi = is_automorphism(PSI, n)
        ok_eps, w_eps = is_automorphism(EPS, n)
        I = np.eye(N)
        ord3 = np.max(np.abs(PSI @ PSI @ PSI - I)) < TOL
        ord2 = np.max(np.abs(EPS @ EPS - I)) < TOL
        s3rel = np.max(np.abs(EPS @ PSI - PSI @ PSI @ EPS)) < TOL
        h = N // 2
        mixes = np.max(np.abs(PSI[h:, :h])) > 0.5  # top-right block nonzero
        line = ("A_%d (dim %3d): psi automorphism=%s (worst %.1e); "
                "eps automorphism=%s; psi^3=I:%s; eps^2=I:%s; "
                "eps psi = psi^2 eps:%s; psi mixes halves:%s"
                % (n, N, ok_psi, w_psi, ok_eps, ord3, ord2, s3rel, mixes))
        print(line)
        commute = None
        if prev_PSI is not None:
            LP, LE = lift(prev_PSI), lift(prev_EPS)
            ok_lift, _ = is_automorphism(LP, n)
            c1 = np.max(np.abs(PSI @ LP - LP @ PSI)) < TOL
            c2 = np.max(np.abs(PSI @ LE - LE @ PSI)) < TOL
            c3 = np.max(np.abs(EPS @ LP - LP @ EPS)) < TOL
            commute = ok_lift and c1 and c2 and c3
            # the lifted psi is a different order-3 element (not psi^k)
            distinct = all(np.max(np.abs(LP - np.linalg.matrix_power(PSI, k)))
                           > 0.5 for k in range(3))
            print("      lifted S_3 from A_%d is an automorphism: %s; "
                  "commutes with the new S_3: %s; lifted psi distinct from "
                  "new psi^k: %s" % (n - 1, ok_lift, commute, distinct))
        results[n] = dict(psi=ok_psi, eps=ok_eps, ord3=ord3, ord2=ord2,
                          s3=s3rel, mixes=mixes, commute=commute)
        prev_PSI, prev_EPS = PSI, EPS

    print("-" * 66)
    print("Derivation-algebra dimension (identity component of Aut):")
    for n in (1, 2, 3, 4, 5):
        d = derivation_dim(n)
        tag = {1: "expect 0", 2: "expect 3 (so(3))", 3: "expect 14 (g2)",
               4: "expect 14 (g2, Schafer)", 5: "expect 14 (g2, Schafer)"}[n]
        print("  dim Der(A_%d) = %2d   [%s]" % (n, d, tag))
        results[("der", n)] = d

    print("-" * 66)
    branch_ok = all(results[n]["psi"] and results[n]["ord3"] and
                    results[n]["s3"] and results[n]["mixes"] for n in (4, 5, 6))
    prod_ok = all(results[n]["commute"] for n in (5, 6))
    der_ok = all(results[("der", n)] == 14 for n in (3, 4, 5))
    print("VERDICT")
    print("  S_3 branch at rungs 4, 5, 6 (Brown's psi is an automorphism, "
          "order three, mixing, not a lift): %s" % branch_ok)
    print("  Direct-product structure (new S_3 commutes with lifted S_3): "
          "%s" % prod_ok)
    print("  Identity component unchanged from the octonions "
          "(dim Der = 14 at n = 3, 4, 5): %s" % der_ok)
    print("-" * 66)
    b_ok = part_B()
    print("-" * 66)
    c_ok = part_C()
    print("-" * 66)
    verdict = branch_ok and prod_ok and der_ok and b_ok and c_ok
    print("NOTEBOOK T: %s" % ("PASS -- (A) the fifth rung adds a further "
                              "finite S_3 and no continuous symmetry, the "
                              "Z/2-vs-S_3 dichotomy settled on the S_3 side "
                              "over R; (B) the core triple is colour, permuted "
                              "inside G_2; (C) the doubling's S_3 permutes the "
                              "three halvings of S" if verdict else "FAIL"))
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
