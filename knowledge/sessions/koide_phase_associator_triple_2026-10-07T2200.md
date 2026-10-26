# The Koide phase and the associator of the edge triple (2026-10-07T2200)

Session 2026-10-07, Fable 5.1. JS, on the W-triangle note (twistor note,
section 9a): "a triple whose three pairs generate three different
quaternionic subalgebras is exactly a non-associative triple. This is
interesting because we are identifying mass with 'associator debt' and also
the norm defect that comes from the zero divisors in the sedenions. So
finding non-associative triples in the W state, which in the framework map
to leptons, is interesting." Script
`scripts/koide_phase_associator_identity_2026-10-07T2200.py` (Convention A,
seed 20261007, PASS), stdout in section 6. `invalid_routes.md` read first:
the octonionic-direction route and the "read delta out of the calibration
bound" route are closed, and nothing below retries them; section 4 says
why not.

## 0. The answer in brief

The place in the paper where three unit octonions sit on the three edges of
a triangle is `prop:koide-jordan`: the democratic element of
$J_{3}(\mathbb{O})$ has one off-diagonal unit octonion $u_{ij}$ per pair of
generations, and the Koide phase is $\cos\Phi=\mathrm{Re}(u_{1}u_{2}u_{3})$,
$3\delta=\Phi$. Those three edges are the three edges of the W register's
triangle: the frame section makes a generation the odd vertex out of the
frustrated triangle, so a pair of generations is a pair of vertices, which
is an edge, which is where $u_{ij}$ lives. So JS's non-associative triple
has a precise home: the three imaginary directions $n_{i}$ of the edge
octonions $u_{i}=\cos t_{i}+\sin t_{i}\,n_{i}$.

Writing the Koide phase in those terms gives an exact identity
(section 1): the cubic term of $\cos\Phi$ is the associative calibration
$\phi(n_{1},n_{2},n_{3})$, and $\phi^{2}+\tfrac14|[n_{1},n_{2},n_{3}]|^{2}
=|n_{1}\wedge n_{2}\wedge n_{3}|^{2}$, so the associator norm of the edge
triple is exactly the calibration's shortfall from the volume, inside the
formula for the Koide phase. That is "associator debt" and "Koide phase" in
contact through one identity, which they were not before. Three regimes
follow (section 2), and the paper's current reading, the Bargmann
invariant of three mutually unbiased states, is the associative one; JS's
W-register intuition is the non-associative one. What the identity does
*not* do (section 4): the data fix $\cos\Phi$ and nothing else, and random
non-associative triples reproduce $\cos(2/3)$ with associator norms
anywhere from $0.2$ to $2$, so this is no route to $\delta$ and the closed
routes stay closed. Where the regimes would differ is in the eigenframes,
hence in mixing, not in the masses (section 5).

## 1. The identity [ESTABLISHED as algebra; verified]

For unit octonions $u_{i}=c_{i}+s_{i}n_{i}$ ($c_{i}=\cos t_{i}$,
$s_{i}=\sin t_{i}$, $n_{i}$ unit imaginary), script part A to $10^{-16}$:
$$\cos\Phi=\mathrm{Re}(u_{1}u_{2}u_{3})
= c_{1}c_{2}c_{3}-c_{1}s_{2}s_{3}\,(n_{2}\!\cdot\! n_{3})-s_{1}c_{2}s_{3}\,(n_{1}\!\cdot\! n_{3})
-s_{1}s_{2}c_{3}\,(n_{1}\!\cdot\! n_{2})-s_{1}s_{2}s_{3}\,\phi(n_{1},n_{2},n_{3}),$$
with $\phi(a,b,c)=\langle a,bc\rangle$ the associative three-form of
Harvey and Lawson, the same $\phi$ the antitelephone note (2026-09-27, 6b)
used. The real part is bracketing-independent, which is why the paper's
proposition is well posed; the imaginary part is not (max difference $1.8$
across bracketings in the sample). Part B: $\phi^{2}+\tfrac14|[n_{1},n_{2},n_{3}]|^{2}
=\mathrm{vol}^{2}$, the constant $\tfrac14$ as found on 2026-09-27. So
$$s_{1}s_{2}s_{3}\,\phi = \pm s_{1}s_{2}s_{3}\sqrt{\mathrm{vol}^{2}-\tfrac14|[n_{1},n_{2},n_{3}]|^{2}}:$$
the triple-product term of the Koide phase is the calibration bound less
the associator debt of the edge triple. Three independent directions in one
quaternionic subalgebra saturate the bound; three directions whose
pairwise subalgebras differ fall short by exactly the associator.

## 1a. Why the formula has that shape: it is distributivity, not a fit (added 2026-10-07T2300)

JS: "this looks too much like accidental numerological coincidence. We
would need to justify why a trig polynomial, why add the cubic term, and
then multiply by the associative three-form." Fair demand; the answer is
that nothing in the formula is chosen. Script part A' checks it term by
term.

1. *Why the polar form.* Every unit octonion lies in a complex subalgebra
   $\mathrm{span}(1,n)$ for a unit imaginary $n$ and so is $\cos t+\sin t\,n$;
   that is the octonionic polar form, not an ansatz (the direction is
   undefined only when $\sin t=0$).
2. *Why a trigonometric polynomial.* Multiply out
   $(c_{1}+s_{1}n_{1})(c_{2}+s_{2}n_{2})(c_{3}+s_{3}n_{3})$ by
   distributivity: eight monomials, containing zero, one, two or three of
   the $n_{i}$, each with a coefficient that is a product of three cosines
   and sines. That is where the trigonometric polynomial comes from, and
   it is the same expansion that gives the triple-angle formula
   $\cos(t_{1}+t_{2}+t_{3})=c_{1}c_{2}c_{3}-c_{1}s_{2}s_{3}-s_{1}c_{2}s_{3}-s_{1}s_{2}c_{3}$
   when all three directions coincide (part A', checked).
3. *Why those coefficients.* Take the real part of each monomial, which is
   all $\cos\Phi$ is. Monomials with one $n$ are imaginary and drop out.
   Monomials with two have $\mathrm{Re}(n_{i}n_{j})=-n_{i}\cdot n_{j}$, the
   composition-algebra identity. The single monomial with three has
   $\mathrm{Re}(n_{i}n_{j}n_{k})$, which is the same for either bracketing
   and equals $-\langle n_{i},n_{j}n_{k}\rangle$. Nothing is "multiplied by
   the three-form": the real part of a product of three imaginary
   octonions *is* the associative three-form, by its definition
   $\phi(a,b,c)=\langle a,bc\rangle$ in Harvey and Lawson. The cubic term is
   not added; it is the one term of the expansion that survives taking the
   real part and contains all three directions.
4. *The one theorem used.* $\phi^{2}+\tfrac14|[a,b,c]|^{2}=|a\wedge b\wedge c|^{2}$
   is Harvey and Lawson's associator identity (their ch. IV; VERIFY-SUPPORT,
   not read), not a fit: the script confirmed its constant, it did not
   find it.

So the identity is the angle-addition formula for octonions, with the
three-form appearing exactly where associativity would have let the
angles add. Where numerology *could* enter is one step later, in reading
the cubic term as "associator debt" and attaching the word to lepton mass;
section 4 fences that, and section 5 says the only place such a reading
could be tested is the eigenframes.

## 2. Three regimes for the edge directions [STRUCTURAL as cases]

Script part C, equal angles $t=2/9$ on each edge:

| regime | the three $n_{i}$ | $\phi$ | associator | $\Phi$ |
|---|---|---|---|---|
| (i) one complex subalgebra | coincident | $0$ | $0$ | $t_{1}+t_{2}+t_{3}=2/3$ |
| (ii) one quaternionic subalgebra | independent, associative | $\pm\mathrm{vol}$ | $0$ | $0.531$ (quaternionic composition) |
| (iii) three different pair subalgebras | non-associative | $|\phi|<\mathrm{vol}$ | $0.66$ | $0.374$ |

Regime (i) is the paper's: the Bargmann invariant of three mutually
unbiased states lives in one $\mathbb{C}$, the three overlap phases add, and
the ledger's constraint on `op:koide-delta` says "angles summing to $2/3$
in the coplanar case". Regime (iii) is JS's W-register triple, the one in
which the three edges are three different quaternionic subalgebras and
the triple is non-associative, as the W triangle's three edges are three
different two-qubit systems with no common frame (twistor note, 9a). The
paper has not chosen between (i) and (iii); its wording presupposes (i).

## 3. Why the W triangle and the generation triangle are the same triangle [CANDIDATE]

The register section draws three spheres per fermion, one per row of the
table, and makes the W register's $K_{3}$ frustration the seed of the
generation count: "which vertex of the triangle is the odd one out" is the
generation. A pair of generations is then a pair of vertices, an edge, and
`prop:koide-jordan` puts one unit octonion on each pair of generations. So
the three edge octonions of the democratic element and the three chiral
edges of the W register (det $T=-4/27$, holonomy $-1$) are indexed by the
same three edges. The W edges carry a $\mathbb{Z}_{2}$ holonomy; the
$J_{3}(\mathbb{O})$ edges carry a phase holonomy $\Phi$ whose real part is
well defined round the triangle despite non-associativity. Whether the
$\mathbb{Z}_{2}$ is the sign of something in the $U(1)$, or the two are
simply two decorations of one triangle, is not known. This is the
correspondence JS's remark needs, and it is a reading of the paper's own
indexing, not a computation; CANDIDATE.

## 4. What the identity does not give, and the closed routes [the fence]

- *The spectrum is blind to the regime.* The eigenvalues of the democratic
  element depend on $\cos\Phi$ only (the flat-direction note already
  checked a non-coplanar triple, 2026-09-11, line 89). Part D: of 500 random
  non-associative triples with equal edge angles, 493 admit an angle $t$
  with $\cos\Phi=\cos(2/3)$; $t$ ranges from $0.25$ to $1.02$ (the coplanar
  value is $0.222$) and the associator norm from $0.23$ to $1.96$, with
  correlation $-0.14$ between them. The one measured number constrains one
  combination of the directions and nothing else. No route to $\delta$ is
  claimed, and none should be tried: the octonionic-direction route is
  closed (G$_{2}$ transitivity), and so is reading $\delta$ out of the
  calibration bound. This identity is the calibration bound appearing in
  the phase formula; it fixes the shape of the term, not its value.
- *"Associator debt" in the paper is the existence and scale of mass*
  (`sec:associator-higgs`: "existence from the associator, ratios from the
  triality angle and the dilution rule"). The identity here puts the
  associator inside the ratio formula, which is a different place from
  where the paper puts it. That is either a unification or a confusion of
  two uses of the word, and the paper should not say the former until
  something is computed with it.
- *The sedenion norm defect* (`prop:zd-defect`, the coassociative four-form)
  is the next rung's calibration, on four components; the identity here is
  the octonionic rung's, the associative three-form on three edge
  directions. They are the same kind of object one rung apart, which is
  what JS's remark pointed at; the exact relation is not computed here.

## 5. Where the regimes would show: the eigenframes and mixing [direction, no computation]

Two democratic elements with the same $\Phi$ but edge directions in
regimes (i) and (iii) have the same three eigenvalues and different
primitive idempotents, since the idempotents depend on the $u_{i}$ and not
only on their triple product. The idempotents are the mass eigenframes, so
the regime is invisible in the masses and visible wherever two frames are
compared: the mixing matrix. If the lepton edges are a non-associative
triple, the PMNS structure is where the associator of the edge triple
would be read, with the bracketing-dependent imaginary part of
$u_{1}u_{2}u_{3}$ as the natural candidate for the quantity that carries it.
This needs the paper's definition of the weak frame in $J_{3}(\mathbb{O})$,
which the generation-transitions note (2026-08-30, v2 2026-09-01) is the
place to look, and the Dray--Manogue eigenvector method for octonionic
Hermitian matrices. Not attempted; it is the computation JS's remark
earns, and it belongs with `op:koide-delta`'s companion, not with $\delta$.

## 6. Proposed ledger and wording items

- **ESTABLISHED** (algebra, verified) For unit octonions $u_{i}=\cos t_{i}
  +\sin t_{i}n_{i}$, $\mathrm{Re}(u_{1}u_{2}u_{3})$ equals the stated
  trigonometric polynomial in the pairwise inner products and the
  associative three-form $\phi(n_{1},n_{2},n_{3})$, with
  $\phi^{2}+\tfrac14|[n_{1},n_{2},n_{3}]|^{2}=\mathrm{vol}^{2}$. The Koide
  phase's triple-product term is the calibration bound less the associator
  norm of the edge triple.
- **CANDIDATE** The three edge octonions of the democratic Jordan element
  and the three chiral edges of the W register are indexed by the same
  three edges of the generation triangle.
- *Wording, `op:koide-delta` constraint:* "angles summing to $2/3$ in the
  coplanar case" should say that this is the associative regime, and that
  the non-associative regime, in which the three edge directions generate
  three different quaternionic subalgebras, is compatible with the data
  and has not been excluded; in it $\Phi$ is not a sum of angles and the
  per-edge angle is not $2/9$.
- *Direction, for the generation-transitions thread:* the regime is
  visible in the eigenframes and hence in mixing, not in the masses.

## 7. Exact stdout of `scripts/koide_phase_associator_identity_2026-10-07T2200.py` (re-run after part A' was added)

```
Koide phase and the associator, Convention A, seed 20261007
====================================================================================
A. cos Phi identity (max err 2.2e-16); Re bracketing-independent (3.3e-16); Im bracketing-dependent (max 1.768)
A'. term by term: Re(n) = 0 (0e+00); Re(n_i n_j) = -n_i.n_j (2e-16); Re((n_i n_j) n_k) = Re(n_i (n_j n_k)) = -phi(n_i,n_j,n_k) (2e-16)
    so the formula is the product multiplied out, with phi = <a, bc> the definition of the associative 3-form (Harvey--Lawson);
    with n1 = n2 = n3 it is the triple-angle formula cos(t1+t2+t3) = c1c2c3 - c1s2s3 - s1c2s3 - s1s2c3.
    check: 0.081483301334 = 0.081483301334
B. phi^2 + |[n1,n2,n3]|^2/4 = vol^2:  max err 7.8e-16   (associator norm = calibration shortfall)
C. three regimes, equal angles t = 2/9 on each edge (3 delta = 2/3 would need the coplanar case)
   (i)   coincident directions:          Phi = 0.666667  (3t = 0.666667)   phi = 0.0e+00  |assoc| = 0.0e+00
   (ii)  one quaternionic subalgebra:    Phi = 0.192634               |phi| = 0.2271 = vol 0.2271  |assoc| = 1.6e-16
   (iii) three different pair subalgebras: Phi = 0.407467               |phi| = 0.3964 < vol 0.7374  |assoc| = 1.2435  (n3 outside <n1,n2>: 0.767)
D. non-associative triples compatible with cos Phi = cos(2/3): equal angle t solved per triple (500 triples)
   solutions found: 496; per-edge angle t: min 0.2444  median 0.3978  max 0.9824  (coplanar value 2/9 = 0.2222)
   associator norm of those triples: min 0.339 median 1.400 max 1.938  (not fixed by the phase)
   correlation of t with |assoc|: -0.094
====================================================================================
KOIDE ASSOCIATOR IDENTITY: PASS
```
