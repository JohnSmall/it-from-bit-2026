# Session note: the Koide phase along the flat direction

Date: 2026-09-11T1900. Session: Claude Code (Fable 5.1), session name
`it_from_bit_fable_5_1`. Follows `koide_delta_gap_2026-09-11T1600.md`, whose
closing conjecture -- that if delta is a holonomy its connection is flat
along the fibre direction, a torus -- was the brief for this session.

## The question

JS asked for thinking on op:koide-delta along the flat-torus direction. The
2026-09-11T1600 session had established that delta = 0.2222248 +/- 0.0000063
rad is a rational number of radians and not a natural angle of round
geometry at any simple denominator, and conjectured a flat structure with
rational periods. This session asks what that conjecture means precisely,
whether a torus can carry the number, and what the phase *is* inside the
framework's own construction.

## What was read

`knowledge/sessions/koide_delta_gap_2026-09-11T1600.md` in full.
`paper1/masses_section_2026-06-08.tex` lines 200--360: prop:koide, the
"one genuine gap" paragraph, op:koide-delta, and sec:koide-gap as patched
on 2026-09-11T1700. `scripts/koide_delta_fit_and_angle_scan_2026-09-11T1600.py`
Part 1, for the inversion convention (k = 0, 1, 2 = tau, e, mu) and the PDG
literals, both reused unchanged. The archive index and project-docs index
were grepped for Gram, Bargmann, Pancharatnam, unbiased, circulant,
Lindemann, transcendental and Sumino: no hits (the one "Bargmann" hit is the
Galilei mass in the Jaynes appendix, unrelated). So the readings below are
new to the corpus. Convention A for the Cayley-Dickson product was taken
from the 2026-08-31 zero-divisor conversation: (a,b)(c,d) = (ac - conj(d)b,
da + b conj(c)), e4 the doubling unit.

## The argument

Each claim carries one of the six labels. The labels are proposals; JS
applies them.

### 1. The invariant form of the coincidence

**STRUCTURAL.** Under the Z3 form delta is defined only modulo 2 pi/3
(relabelling k), so the invariant is 3 delta mod 2 pi, and cos(3 delta) =
(4/alpha^3) prod_k (sqrt(m_k)/M - 1). The coincidence "delta = 2/9" is
invariantly "3 delta = 2/3", and 2/3 is also the Koide ratio K. With
p_k = sqrt(m_k) / sum_j sqrt(m_j) (so sum p_k = 1) one has K = sum_k p_k^2
exactly, and the Z3 form is the discrete Fourier transform of p:
b = sum_k p_k exp(-2 pi i k/3) = (alpha/2) exp(i delta), with |b|^2 =
(3K - 1)/2. So alpha = 2|b| and delta = arg b are read off the data without
a fit, and K = 2/3 is the statement |b|^2 = 1/2. Numerically 3 delta =
0.6666743 +/- 0.0000188 rad; 2/3 sits at -0.41 sigma and K itself at -0.52
sigma. This is a restatement, not new evidence, but it changes what has to
be derived: not "an angle of 2/9" but "the Z3-invariant phase, in radians,
equals two thirds", and any mechanism must produce 3 delta.

**RHYME.** 3 delta = K, i.e. the invariant phase in radians equals
tr(X^2)/(tr X)^2 for the mass-root matrix X. No mechanism makes a phase equal
a trace ratio; recorded so that nobody rediscovers it as a result.

### 2. What the phase is: the Gram matrix and the democratic Jordan element

**STRUCTURAL (linear algebra; verified to 1e-15).** Any 3 x 3 Hermitian
matrix with unit diagonal and off-diagonal entries of common modulus rho has
eigenvalues 1 + 2 rho cos((Phi + 2 pi k)/3), where Phi is the argument of
the product of the three off-diagonal entries around the cycle. Hence the
Koide spectrum with alpha = sqrt2 is exactly the spectrum of the Gram matrix
of three unit vectors with pairwise |<psi_j|psi_k>|^2 = 1/2 -- three
mutually unbiased states -- and 3 delta is their Bargmann invariant, the
argument of <psi_0|psi_1><psi_1|psi_2><psi_2|psi_0>, which is the one
continuous invariant a triple of states has beyond its overlaps. Positivity
of the Gram matrix bounds it: |Phi| <= pi/4, with equality iff the three
states are coplanar (rank 2) and one generation is massless. The measured
3 delta is 0.849 of the bound; the shortfall pi/4 - 3 delta = 0.1187 rad
sets the electron mass, and to first order sqrt(m_e)/M = (pi/4 - 3 delta)/3
(0.0396 against the exact 0.0403, two per cent).

**STRUCTURAL (octonionic; verified to 3e-15 with Convention A).** The same
statement holds in the framework's own construction. The paper already
says the three generations are the off-diagonal octonionic entries of
J3(O) permuted by Z3 triality. Take the democratic element X with unit
diagonal and off-diagonal octonions x_i = rho u_i, u_i unit. Its
characteristic cubic is lambda^3 - 3 lambda^2 + (3 - 3 rho^2) lambda - N
with cubic norm N = 1 - 3 rho^2 + 2 rho^3 Re(u_1 u_2 u_3) (Baez 2002, 3.4),
and substituting lambda = 1 + 2 rho c gives 4c^3 - 3c = cos Phi with
cos Phi = Re(u_1 u_2 u_3). So the triality form is the spectrum of the
democratic Jordan element, alpha = 2 rho, and 3 delta is the phase of the
cyclic product of the three off-diagonal units. The real part of a triple
product is bracketing-independent in any composition algebra (checked:
1e-16 on random octonions whose associator has norm 0.54), so the phase is
well defined without associativity; and the spectrum depends on Phi alone,
not on the directions of the u_i (checked with a random non-coplanar triple,
associator norm 1.03: same eigenvalues to 3e-15). The question "why 2/9"
is therefore, inside the paper's construction, "why does the cyclic product
of the three off-diagonal units have real part cos(2/3)".

**CANDIDATE (pushback on the paper's wording).** The paper reads alpha =
sqrt2 as "the doubling norm |1 + i|". That names the number; the Gram
reading says what it is the norm of: alpha/2 = |<psi_j|psi_k>| = 1/sqrt2,
each pair of generation states mutually unbiased. Mutual unbiasedness is a
structural condition with content (it is what makes the Koide ratio
sit exactly midway between the degenerate value 1/3 and the pure value 1),
and I would propose the paper say it.

### 3. What kind of number the phase must be

**STRUCTURAL (Lindemann--Weierstrass).** If delta = 2/9 exactly -- or is any
non-zero algebraic number -- then e^{i delta} is transcendental, since e^a is
transcendental for every non-zero algebraic a. Consequences:

- The Bargmann product, and its octonionic form u_1 u_2 u_3, cannot be
  algebraic. So no construction of the three off-diagonal entries from the
  structure constants, from roots of unity, from a finite group (Clifford,
  Pauli, Weyl of G2), from SIC or MUB overlaps, or from any configuration of
  vectors with algebraic coordinates can give delta = 2/9 exactly. The
  holonomy of a round connection around a geodesic polygon with algebraic
  vertices is the argument of exactly such a Bargmann product and is
  excluded with them.
- Every charged-lepton mass ratio is then transcendental: m_j/m_k is a
  non-constant rational function of z = e^{i delta} with coefficients in
  Q(sqrt2, omega), so an algebraic value would force z algebraic,
  contradicting the theorem.
- Contrapositive: any mechanism that returns an algebraic value for even
  one mass ratio returns a delta that is zero or transcendental, and must
  then explain the agreement with 2/9 as an accident. The size of that
  accident: 56 reduced fractions with denominator at most nine lie in
  [0, 2 pi/3), the six-sigma band is 3.75e-5 rad wide, chance expectation
  1.0e-3. And 2/9 was proposed before the band narrowed: with the tau mass
  as listed around 2006 (1776.99 +/- 0.29 MeV, quoted from memory, VERIFY)
  the band was 3.2 times wider and 2/9 sat at +0.08 sigma; it now sits at
  -0.41 sigma of a band a third the width. A pre-registered value that
  survives a threefold narrowing is the strongest reason to take exactness
  seriously.
- What survives is exactly the class in which the phase is the exponential
  of a rational number: an action or symplectic area in units of hbar, a
  length along a flat direction in units of its radius, a Lie-algebra
  generator with a rational coefficient, a dynamical phase. This is the
  precise mathematical content of the 1600 session's "flat rather than
  round": round constructions are arguments of algebraic vector
  configurations; flat ones exponentiate a linear quantity.

The scan of the 1600 session and this theorem are complementary. The scan
excludes the natural transcendental-delta families (rational multiples of
pi, inverse trigonometric values, cap Berry phases) numerically at simple
denominators. The theorem excludes every algebraic-e^{i delta} family
exactly, on the hypothesis that 2/9 is exact. A derivation that ends in an
algebraic e^{i delta} is therefore wrong if 2/9 is exact and, if it is not,
still lands in a family the scan finds empty.

### 4. Flat, yes; torus, no

**STRUCTURAL (argument, no computation needed).** The torus half of the
1600 conjecture does not survive. On a compact flat torus with a quantised
flux, every enclosed phase is 2 pi n times a rational area fraction (Pick's
theorem on lattice regions), i.e. a rational multiple of 2 pi -- the family
the scan excludes. A flat connection whose holonomy is not quantised has a
holonomy that is a modulus: a free real parameter that the geometry leaves
open, which re-houses the fitted number rather than deriving it. The Hopf
tori inside S^3 (preimages of latitude circles) are flat, and the Hopf
connection restricted to them is flat, but their holonomies are fixed by
Stokes from the round geometry outside -- the cap Berry phases already
excluded. So the flat structure carrying the phase must be non-compact in
the direction that matters, and the rational number is then most naturally
an area, the product of two rational lengths in units of hbar, or a length
in units of a radius. Compactness kills rational radians; only the flat
plane, or a cylinder whose non-compact direction carries the phase, can
produce them.

**RHYME.** 3 delta = 2/3 = 2 (1/sqrt3)^2 is the Weyl commutator phase
exp(i(q_1 p_2 - q_2 p_1)) of two orthogonal phase-space displacements of
squared amplitude 1/3, the equal-weight number of the results ledger's
phi^2 = 1/3 reading. Equivalently delta = 2 phi^2/3 = 2 phi^4. Every such
identity is the same arithmetic on the number 2/3, and none of them is a
mechanism.

### 5. Two things closed by computation

**Closed route (proposed for invalid_routes).** The coherent-state model:
three coherent states |alpha_k>, alpha_k = r exp(2 pi i k/3), on an
equilateral triangle in phase space, mass roots the eigenvalues of their
Gram matrix, so that the Bargmann phase is twice the enclosed area (the
one genuinely "flat, non-compact, area-valued" model one can write down in
a line). One parameter r, two targets. Fixing the pairwise overlap at
1/sqrt2 (alpha = sqrt2 exactly) gives r^2 = ln2/3 and Phi = (sqrt3/2) ln 2
= 0.6003 rad, 3500 sigma below 2/3; the muon comes out 10.5% light and the
electron 147% heavy. Fixing Phi = 2/3 (triangle area exactly 1/3) gives
alpha = 2 exp(-2/(3 sqrt3)) = 1.3610, 4900 sigma below sqrt2, K = 0.642. The
Gaussian overlap ties magnitude and phase to the same r^2 with the wrong
ratio; no rescaling helps.

**Closed near-miss.** 4 det G = 108 p_e p_mu p_tau = 2 sqrt2 cos(3 delta) - 2
comes out 0.22283 (data) and 0.222825 (under 3 delta = 2/3 exactly), 0.27%
above 2/9, 18 sigma on the data's own uncertainty. It looks like 2/9 at
three figures and is not; recorded so it is not chased.

### 6. Two remarks not computed

**OPEN (remark).** An exact tree-level 2/9 at the pole masses has to survive
QED: a shift of relative size alpha_em/pi in one mass moves delta by roughly
5e-4 rad, eighty sigma. Either the corrections cancel in the combination the
Z3 form sees, or 2/9 is a statement about pole masses directly. This is the
known Koide QED problem (Sumino 2009, family gauge symmetry; VERIFY-CITE, not
read this session) and any derivation inherits it.

**Literature.** The parametrisation with delta = 2/9 is Brannen's (2006,
unpublished web note as I recall; VERIFY-CITE). The paper currently credits
Koide 1983 for the ratio and no one for the phase; it should credit the
phase. Added to notes/todo.md.

## What was computed

`scripts/koide_flat_direction_gram_2026-09-11T1900.py`, seed 20260911, no
hidden state; numpy 1.21.5 for eigenvalues and cubic roots. Exact stdout:

```
koide_flat_direction_gram_2026-09-11T1900.py  seed=20260911
--- Part A: fit-free extraction from PDG 2024 (tau 1776.93 +/- 0.09 MeV)
p = sqrt(m)/sum sqrt(m)  [tau, e, mu] = 0.79314427  0.01345015  0.19340558   (sum = 1.000000000000000)
K = sum p^2              = 0.66666446   (2/3 = 0.66666667; K - 2/3 = -2.20e-06)
b = sum p_k w^k          = 0.68971641 +0.15584598i
|b|^2                    = 0.49999670   (identity (3K-1)/2 = 0.49999670; 1/2 at K = 2/3)
alpha = 2|b|             = 1.4142089   (sqrt2 = 1.4142136)
delta = arg b            = 0.22222476 rad   (2/9 = 0.22222222)
MC (N=200000): delta = 0.22222476 +/- 0.00000626 rad, alpha = 1.4142089 +/- 0.0000108
Z3-invariant phase 3 delta = 0.6666743 +/- 0.0000188 rad
  2/3 - 3 delta            = -0.0000076 rad = -0.41 sigma
  K   - 3 delta            = -0.0000098 rad = -0.52 sigma   (the invariant coincidence: 3 delta = K)
  bound pi/4 = 0.7853982; 3 delta / (pi/4) = 0.848836; shortfall pi/4 - 3 delta = 0.1187239 rad
  delta as a fraction of the Z3 step 2 pi/3: 0.1061045  (irrational: 1/(3 pi) = 0.1061033 under the 2/9 hypothesis)
older tau 1776.99 +/- 0.29 MeV (VERIFY): delta = 0.22222059 +/- 0.00002016 rad; 2/9 at +0.08 sigma; band since narrowed by x3.2 and 2/9 is at -0.41 sigma of the 2024 band
--- Part B: Gram matrix of three mutually unbiased unit vectors in C^3
[Phi = 2/3 exactly]  pairwise |overlap|^2 = 0.500000000000 0.500000000000 0.500000000000;  Bargmann phase = 0.6666666667 (target 0.6666666667)
  Gram eigenvalues        = 2.3794381716 0.5802119201 0.0403499082
  1+sqrt2 cos((Phi+2pik)/3)= 2.3794381716 0.5802119201 0.0403499082   max|diff| = 8.9e-16
  normalised p from data  = 0.7931442737 0.1934055791 0.0134501472   (= eigenvalues/3 when Phi = 3 delta_fit)
  M from tau = 17.715799 sqrt(MeV): m_mu = 105.6561 MeV (-0.0021%), m_e = 0.510983 MeV (-0.0031%)
  det G = 0.05570621;  (sqrt2 cos Phi - 1)/2 = 0.05570621;  108 p_e p_mu p_tau (data) = 0.22282914
[Phi = 3 delta_fit]  pairwise |overlap|^2 = 0.500000000000 0.500000000000 0.500000000000;  Bargmann phase = 0.6666742857 (target 0.6666742857)
  Gram eigenvalues        = 2.3794373800 0.5802153499 0.0403472701
  1+sqrt2 cos((Phi+2pik)/3)= 2.3794373800 0.5802153499 0.0403472701   max|diff| = 6.7e-16
  normalised p from data  = 0.7931442737 0.1934055791 0.0134501472   (= eigenvalues/3 when Phi = 3 delta_fit)
  M from tau = 17.715805 sqrt(MeV): m_mu = 105.6575 MeV (-0.0009%), m_e = 0.510917 MeV (-0.0161%)
  det G = 0.05570288;  (sqrt2 cos Phi - 1)/2 = 0.05570288;  108 p_e p_mu p_tau (data) = 0.22282914
[Phi = pi/4]  eigenvalues = [9.4406904169e-17 6.3397459622e-01 2.3660254038e+00]  -> rank 2, one massless generation; third component c = 1.490e-08
random U(3) rotation: max|G' - G| = 4.4e-16, Bargmann phase 0.6666666667
--- Part C: J3(O) democratic element, Convention A octonions
e_i^2 = -1 for i=1..7: True;  e1 e2 = e3;  |xy|-1 = 0.0e+00;  alternativity 1.1e-16;  associator 0.540 (non-zero);  Re((xy)z) - Re(x(yz)) = 1.1e-16
(i) x1=x2=x3=exp((2/9) e1)/sqrt2: tr=3.000000 S=1.500000 N=0.0557062113; cubic roots 2.3794381716 0.5802119201 0.0403499082; Koide roots max|diff| = 2.7e-15
(ii) random directions, |u3| = 1.000000000000: Re((u1u2)u3) = 0.7858872608, Re(u1(u2u3)) = 0.7858872608, cos(2/3) = 0.7858872608
     cubic roots 2.3794381716 0.5802119201 0.0403499082; Koide roots max|diff| = 2.7e-15  (spectrum depends on Phi only)
     associator [(u1u2)u3 - u1(u2u3)] norm = 1.0282
--- Part D: coherent-state model, alpha_k = r exp(2 pi i k/3), G_jk = <alpha_j|alpha_k>
closure 1: r^2 = ln2/3 = 0.231049 -> |overlap|^2 = 0.500000, Phi = (sqrt3/2) ln 2 = 0.600283 rad (target 2/3: -0.0664 rad = -3537 sigma); delta = 0.200094
           masses with M from tau: m_mu = 94.567 MeV (-10.50%), m_e = 1.26131 MeV (+146.8%)
closure 2: Phi = 0.6666666667, triangle area = 0.333333, r^2 = 4/(9 sqrt3) = 0.256600 -> alpha = 2 e^{-3r^2/2} = 1.361037 (sqrt2: -0.0532 = -4937 sigma), K = 0.642070
           masses with M from tau: m_mu = 116.507 MeV (+10.27%), m_e = 1.91619 MeV (+275.0%)
--- Part E: near-miss and chance expectation
108 p_e p_mu p_tau = 4 det G: data 0.22282914, under 3 delta = 2/3 exactly 0.22282485; 2/9 = 0.22222222; excess over 2/9 = +6.03e-04 (+0.271%, +18 sigma). Not a coincidence worth pursuing.
reduced fractions p/q with q <= 9 in [0, 2 pi/3): 56; 6-sigma band width 3.75e-05 rad; chance expectation of one landing = 1.00e-03
done.
```

## Reading of the output

1. Part A reproduces the 1600 fit to all printed digits without fitting:
   delta = arg b = 0.22222476 rad, alpha = 2|b| = 1.4142089. The DFT
   reading is the fit. The invariant 3 delta = 0.6666743 +/- 0.0000188 rad.

2. Part B: the explicit unbiased triple has pairwise overlap probability
   exactly 1/2 and Bargmann phase exactly Phi; its Gram eigenvalues agree
   with 1 + sqrt2 cos((Phi + 2 pi k)/3) to 9e-16; with Phi = 2/3 and M from
   the tau it reproduces the paper's construction numbers (-0.0021%,
   -0.0031%). With Phi = 3 delta_fit the electron is -0.016% because the
   construction forces alpha = sqrt2 while the data's alpha is 0.43 sigma
   below it; the joint (sqrt2, 2/9) point fits better than (sqrt2,
   delta_fit), which is what a correlated band looks like. At Phi = pi/4 the
   smallest eigenvalue is 9e-17: the bound is tight and one generation is
   massless there. A random U(3) rotation leaves the Gram matrix invariant
   to 4e-16.

3. Part C: Convention A passes its checks (e_i^2 = -1, e1 e2 = e3, norm
   multiplicative, alternative to 1e-16, associator 0.54 on a random triple,
   Re((xy)z) = Re(x(yz)) to 1e-16). The democratic element with x_i =
   exp((2/9) e1)/sqrt2 has tr 3, S 3/2, N 0.0557062 and cubic roots equal to
   the Koide roots to 2.7e-15. A random non-coplanar triple with the same
   Re(u1 u2 u3) = cos(2/3) and associator norm 1.03 has the same roots to
   2.7e-15. The spectrum sees Phi and nothing else.

4. Part D: both closures of the coherent-state model fail by thousands of
   sigma; see section 5 above.

5. Part E: the near-miss is 18 sigma out; the chance expectation for a
   denominator-nine fraction in the six-sigma band is 1.0e-3; the older tau
   band was 3.2 times wider and contained 2/9 at +0.08 sigma.

## Opinion

The flat-torus conjecture was half right. The rational-radian argument
does point at exponentiating a linear quantity rather than taking the
argument of an algebraic configuration, and Lindemann--Weierstrass makes
that precise and rigorous: if 2/9 is exact, every algebraic construction
of the generation triple is dead before it is checked, and every charged-
lepton mass ratio is transcendental. But a torus cannot carry the number;
compactness forces rational multiples of 2 pi or leaves a modulus. The
structure has to be non-compact in the direction that carries the phase,
and the number is then an area or a length in natural units.

The more useful outcome is that the phase now has a definition inside the
paper's own construction. It is the phase of the cyclic product of the
three off-diagonal unit octonions of the democratic J3(O) element -- the
octonionic Bargmann invariant of the generation triple -- bounded by pi/4,
with the electron mass as the shortfall. That turns "derive 2/9" into
"derive Re(u_1 u_2 u_3) = cos(2/3)", a question about three unit octonions
rather than about a holonomy of an unspecified loop. Because the answer
must be transcendental, the u_i must be exponentials: u_i = exp(theta_i n_i)
with the theta_i summing (in the coplanar case) to 2/3. A rational sum of
three rotation angles, each a rotation in a complex line of O, is the shape
of the object to look for. I do not have a mechanism for it and did not
attempt one; the routes closed here are the two that the flat-area idea
suggests first.

I would also push back on one phrase in the paper: "the doubling norm
|1 + i| = sqrt2" is a name for a number, whereas "the three generation
states are pairwise mutually unbiased" is a condition on states, and it is
the second that the algebra actually says.

## Files changed this session (pending JS approval before commit)

- `scripts/koide_flat_direction_gram_2026-09-11T1900.py` (new)
- `knowledge/sessions/koide_flat_direction_2026-09-11T1900.md` (this note)
- `scripts/patch_koide_jordan_transcendence_2026-09-11T1930.py` (new) and
  its effect on `paper1/masses_section_2026-06-08.tex`: op:koide-delta gains
  the invariant target, the transcendence FAIL clause and the fourth closed
  route; the closing torus paragraph of sec:koide-gap is replaced by
  prop:koide-jordan with proof and three paragraphs (what the phase is, what
  kind of number it must be, flat but not a torus). Backup
  `paper1/masses_section_2026-06-08.tex.2026-09-11T1930.bak`.
- `notes/todo.md`: one line on crediting the 2/9 parametrisation, one on
  the stray build artefact below.

Compile: baseline `latexmk paper1/main.tex` clean (exit 0, no `^!` lines in
main.log). The first patched build failed with a truncated main.aux because
a second session built paper1 at the same moment (its commit e803fa5 and a
CLAUDE.md change landed mid-session); it left `paper1/main.bcf-SAVE-ERROR`
behind. Rebuilt alone: exit 0, no `^!` lines, prop:koide-jordan resolves.
The thirteen undefined-reference warnings (sec:Kioid, sec:sedenions-
generations and the like) predate this patch and are not touched by it.

No ledger was edited. Proposed entries follow.

## Proposed ledger entries

### results_ledger.md, dated 2026-09-11 (flat-direction session)

- **STRUCTURAL** `[PROPOSED]` The triality form is the spectrum of the
  democratic element of J3(O) (unit diagonal, off-diagonal octonions of
  common norm rho): eigenvalues 1 + 2 rho cos((Phi + 2 pi k)/3) with
  cos Phi = Re(u_1 u_2 u_3) for the unit off-diagonals, so alpha = 2 rho and
  3 delta = Phi. The phase is bracketing-independent and the spectrum
  depends on Phi only. Equivalently, over C, the Koide spectrum with
  alpha = sqrt2 is the spectrum of the Gram matrix of three pairwise
  mutually unbiased states and 3 delta is their Bargmann invariant.
  Positivity gives |Phi| <= pi/4 with equality iff one generation is
  massless; the measured 3 delta is 0.849 of the bound and sqrt(m_e)/M =
  (pi/4 - 3 delta)/3 to two per cent. Verified to 1e-15 (complex) and 3e-15
  (Convention A octonions).
- **STRUCTURAL** `[PROPOSED]` If delta = 2/9 exactly (or is any non-zero
  algebraic number) then e^{i delta} is transcendental
  (Lindemann--Weierstrass), hence: the cyclic product u_1 u_2 u_3 cannot be
  algebraic; no configuration of generation states with algebraic
  coordinates, no finite-group phase, no root of unity, no round holonomy
  around a polygon with algebraic vertices can be exact; and every
  charged-lepton mass ratio is transcendental. Any mechanism yielding an
  algebraic mass ratio yields delta zero or transcendental and must
  explain the five-figure agreement with 2/9 as chance (expectation 1e-3
  for a denominator-nine fraction in the six-sigma band).
- **STRUCTURAL** `[PROPOSED]` Fit-free form of the Koide data: with
  p_k = sqrt(m_k)/sum sqrt(m), K = sum p_k^2 and sum_k p_k e^{-2 pi i k/3} =
  (alpha/2) e^{i delta}, so |b|^2 = (3K - 1)/2 = 1/2 at K = 2/3. The
  Z3-invariant phase is 3 delta = 0.6666743 +/- 0.0000188 rad (PDG 2024);
  2/3 at -0.41 sigma.
- **RHYME** `[PROPOSED]` 3 delta = 2/3 = K: the invariant phase in radians
  equals the Koide ratio, tr X^2/(tr X)^2. Also 2/3 = 2 (1/sqrt3)^2, the
  Weyl commutator phase of two orthogonal displacements of squared
  amplitude 1/3. Arithmetic on one number; no mechanism.
- **CANDIDATE** `[PROPOSED]` Reading of alpha = sqrt2: the three generation
  states are pairwise mutually unbiased, |<psi_j|psi_k>|^2 = 1/2. Proposed
  to replace, or stand beside, "the doubling norm |1 + i|" in the paper.

### invalid_routes.md, dated 2026-09-11 (flat-direction session)

- A compact flat torus, with or without quantised flux: quantised flux
  gives rational multiples of 2 pi (Pick), the family the scan excludes;
  unquantised flat holonomy is a modulus and re-houses the fitted number.
  Hopf tori in S^3 are flat with a flat restricted connection but their
  holonomies are the excluded cap phases by Stokes. Supersedes the "torus"
  half of the 2026-09-11T1600 conjecture; the "flat" half stands as
  "exponential of a rational number, non-compact direction".
- Any construction in which e^{i delta} is algebraic: roots of unity,
  finite-group phases, algebraic state configurations, SIC/MUB overlaps,
  octonionic structure-constant triples, round holonomies around polygons
  with algebraic vertices. Excluded exactly by Lindemann--Weierstrass if
  2/9 is exact. A derivation that ends here is wrong before it is checked.
- The coherent-state (Pancharatnam) model: three coherent states on an
  equilateral triangle, mass roots the Gram eigenvalues, phase twice the
  enclosed area. One parameter, two targets; fixing the overlap gives
  Phi = (sqrt3/2) ln 2 = 0.600 (3500 sigma), fixing the phase gives
  alpha = 1.361 (4900 sigma). Script koide_flat_direction_gram_2026-09-11T1900.py.
- Near-miss, not a route: 108 p_e p_mu p_tau = 2 sqrt2 cos(3 delta) - 2 =
  0.2228, 0.27% above 2/9, 18 sigma. Do not chase.

### open_problems.md, dated 2026-09-11 (flat-direction session)

- **OPEN** `[PROPOSED]` op:koide-delta, restated in the paper's own
  construction: derive Re(u_1 u_2 u_3) = cos(2/3) for the three off-diagonal
  unit octonions of the democratic J3(O) element, equivalently the
  Bargmann invariant 3 delta = 2/3 of three mutually unbiased generation
  states. PASS: a value of 3 delta inside 0.6666743 +/- 0.0000188 rad with no
  fitted input. FAIL before checking: any route ending in an algebraic
  e^{i delta}. Constraint: the u_i must be exponentials exp(theta_i n_i) of
  rational multiples of imaginary units, with angles summing to 2/3 in the
  coplanar case; the flat structure is non-compact in the direction that
  carries the phase, and the number is an area or a length in natural units.
  Six routes closed (see invalid_routes 2026-09-11, both entries).
- **OPEN** `[PROPOSED]` The QED problem: an exact tree-level 2/9 at the
  pole masses must survive corrections of relative size alpha_em/pi, which
  would move delta by ~5e-4 rad (eighty sigma). Any derivation inherits
  this; cf. Sumino 2009 (VERIFY-CITE).

## VERIFY-CITE

- Brannen 2006 for the delta = 2/9 parametrisation (unpublished note as
  recalled; not read this session). Not in references.bib; not cited in the
  patch.
- Sumino 2009 (Phys. Lett. B 671, 477 and JHEP 0905:075, as recalled) for
  the Koide QED-correction problem. Not read this session; not in the bib;
  mentioned in this note only.
- The tau mass "1776.99 +/- 0.29 MeV, around 2006" in the script's
  sensitivity line is from memory; the line is labelled VERIFY in the
  stdout and is used in this note only.
- Baez 2002 (baez2002octonions, already in the bib) is cited in the patch
  for the cubic norm of J3(O), section 3.4; I have read that section in the
  past but did not reopen it this session, so the section number should be
  checked at proof stage.
- Lindemann--Weierstrass is stated without citation in the patch, as a
  named theorem; a textbook reference (Baker, Transcendental Number Theory,
  1975, ch. 1) could be added through Zotero if JS wants one.

## Not done

- No mechanism for Re(u_1 u_2 u_3) = cos(2/3) was attempted. The
  constraint (exponentials of rational angles, non-compact flat direction)
  is recorded; the object to look for is a rational sum of three rotation
  angles in complex lines of O.
- The QED question is stated, not computed.
- No RIS batch: the two references I would add (Brannen, Sumino) are not
  verified against sources read this session.
