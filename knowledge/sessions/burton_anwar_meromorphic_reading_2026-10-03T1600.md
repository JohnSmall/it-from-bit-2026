# Reading note: Burton and Anwar, "Meromorphic Quantum Computing" (Quantinuum, arXiv:2605.06251, 7 May 2026)

Session 2026-10-03, Fable 5.1. JS: "Read the full paper and write a reading
note." Read in full from the arXiv PDF (v1, 17 pages, `pdftotext`). The
library already holds the entry as `burtonanwar2026meromorphic` and the paper
already cites it twice in `sec:hopf-compositional` (hopf_justification
section, committed before 2026-09-11); section 4 below checks those two
sentences against the text, second-order style, and finds one of them
overstated. Script `scripts/burton_anwar_meromorphic_check_2026-10-03T1600.py`
(seed 20261003, numpy only, PASS), stdout in section 3.

## 1. What the paper does

Simon Burton and Hussain Anwar, both Quantinuum. The paper projectivises the
kinematic axioms: a state is a one-dimensional subspace, not a unit vector up
to phase, so a qubit is the complex projective line, the Riemann sphere, with
the chart $z = v_{0}/v_{1}$ ($|0\rangle$ at $z=\infty$, $|1\rangle$ at $z=0$,
$|\pm X\rangle$ at $z=\pm1$). Invertible operators act by Möbius maps;
unitaries by rotations; eigenvectors become fixed points and eigenvalues are
forgotten (their Prop. 1.2). The zero vector, which no projective space
contains, is adjoined as an "impossible element" $\bot$ so that postselection
maps become pointed functions (Prop. 1.3), and with the Segre embedding as
laxator projectivisation is a lax monoidal functor from finite-dimensional
vector spaces to pointed sets under smash product (Prop. 1.4, their only
proof of substance in the kinematics). Their summary of projective quantum
mechanics is three lines: states are points of projective spaces or
impossible, operators are maps preserving the impossible state, composition
is lax monoidal.

The structural result is Prop. 3.1: the three monoid structures on
$\mathbb{C}^{2}$ that the ZX and ZW calculi use, the Z-spider, the X-spider
and the W-spider, projectivise to three monoids on the pointed Riemann
sphere,
$$(w,z)\mapsto wz,\qquad (w,z)\mapsto \frac{wz+1}{w+z},\qquad (w,z)\mapsto w+z,$$
undefined (impossible) at $(0,\infty)$, $(1,-1)$ and $(\infty,\infty)$
respectively. Their sentence: "the multiplication and addition of complex
numbers is the projectivization of the Z- and W-spiders", which is how they
recover the arithmetic GHZ/W-calculus of Coecke, Kissinger, Merry and Roy
(2011, "The GHZ/W-calculus contains rational arithmetic") without the formal
construction. The X-spider, in the reciprocal chart $z\mapsto 1/z$, is
$(w+z)/(wz+1)$, "the familiar formula for Lorentz velocity addition"; they
say no more about that.

The application is to codes. For an $[[n,1,d]]$ code the logical decoder
$L^{\dagger}$ applied to a product of $n$ copies of $|\psi_{z}\rangle$ is a
meromorphic function $f(z)=p(z)/q(z)$, the "meromorphic decoder" (Prop. 4.1).
Its degree is $n$ for the examples; its stationary points (branch points,
$f'(z)=0$) are where coherent error on the inputs is suppressed to order
$\varepsilon^{m_{z}}$, $m_{z}$ the number of sheets; the Riemann--Hurwitz
count $\sum(m_{z}-1)=2(n-1)$ (Thm. 2.1, 4.2) says such points exist
generically; fixed points $f(z)=z$ are the states the decoder distils
(Prop. 4.7, roots of $r(z)=p-zq$); concatenation composes decoders
(Prop. 4.6); for CSS codes the decoder is a ratio of weight enumerators
(Thm. 4.4), with a MacWilliams-type duality under $z\mapsto(z+1)/(z-1)$
(Prop. 4.3). Klein's octahedral function $E_{7}(z)=108z^{4}(z^{4}-1)^{4}/
(z^{8}+14z^{4}+1)^{3}$ detects Clifford equivalence of points (Prop. 2.3).
Examples: Shor $[[9,1,3]]$, $f=(z^{9}+3z^{3})/(3z^{6}+1)$; five-qubit
$[[5,1,3]]$, $f=(z^{5}-5z)/(5z^{4}-1)$, which weakly distils the eight
$F$-states (face centres of the Bloch octahedron, roots of
$z^{8}+14z^{4}+1$) to $O(\varepsilon^{2})$; Steane $[[7,1,3]]$,
$f=(z^{7}+7z^{3})/(7z^{4}+1)$; the $[[15,1,3]]$ triorthogonal code. The
closing section asks what the Galois group of the number fields the states
live in means physically ("which $i$ do you mean?"), notes that mixed states
need antiholomorphic structure, and points at geometric quantisation.

Not mentioned anywhere: Hopf fibrations, division algebras, quaternions,
octonions, the three-tangle, SLOCC. Their reference [7], Gharahi, Mancini
and Ottaviani 2020, is the algebraic-geometric SLOCC classification (Segre,
secant and tangent varieties), cited only for the Segre embedding.
Acknowledgements thank Aleks Kissinger among others.

## 2. Verified, and two small findings about the paper itself

Everything checked holds, and the examples were rebuilt from the codes'
logical states rather than from the printed formulas:

- Prop. 3.1, the three monoid formulas, to $10^{-15}$.
- The Shor, five-qubit and Steane decoders agree with the printed $f(z)$ as
  functions, Shor and Steane exactly, the five-qubit one up to a factor
  $-1$ (see the second finding).
- Riemann--Hurwitz, counting the point at infinity: Shor, degree 9, seven
  finite triple points plus a triple point at infinity, $16=2\cdot8$;
  five-qubit, degree 5, eight double points (the $F$-states), unramified at
  infinity, $8=2\cdot4$; Steane, degree 7, five finite triple points plus a
  triple point at infinity (the six stabiliser states), $12=2\cdot6$.
- $E_{7}$ is invariant under $S(z)=-iz$ and $H(z)=(z+1)/(z-1)$, which
  generate the Clifford image; it takes the value $0$ at the stabiliser
  states, $1$ at the $H$-states and has poles at the $F$-states, so it is a
  Belyi function with the octahedral dessin, which is the "dessin d'enfants"
  remark of their Fig. 2 made explicit.

Two things the paper does not say, or says imprecisely:

1. *Labels swapped in Example 5.1.* The multivariate paragraph assigns
   $g=z_{1}z_{2}z_{3}$ to $\langle XXI,IXX\rangle$ and the symmetric rational
   function to $\langle ZZI,IZZ\rangle$; rebuilt from the logical states it
   is the other way round ($\langle ZZI,IZZ\rangle$ has $|0_{L}\rangle
   =|000\rangle$, $|1_{L}\rangle=|111\rangle$, so its decoder is
   $z_{1}z_{2}z_{3}$). The univariate line ("$g(z)=(z^{3}+3z)/(3z^{2}+1)$
   and $h(z)=z^{3}$ respectively") and the Shor decoder $f=g\circ h$ are
   right; only the multivariate labels are crossed. A typo, harmless.
2. *The distilled set is frame-dependent; the branch points are not.* With
   the stabilisers as printed and $L_{X}=+X^{\otimes5}$, the five-qubit
   decoder comes out as $-(z^{5}-5z)/(5z^{4}-1)$, i.e. the printed decoder
   followed by a logical $Z$. The branch points (coherent suppression) are
   unchanged, but the fixed points are not: the printed frame distils $z=0$
   and the four $H$-states with $z^{4}+1=0$, as they say; the $+X^{\otimes5}$
   frame distils the six stabiliser states instead. Their "distils up to a
   Clifford" covers this, but the sentence "the meromorphic decoder distills
   $z=0$ as well as four of the $H$-states" is a statement about a logical
   Pauli frame, not about the code. Worth knowing if anyone cites it.

## 3. Exact stdout

```
Burton--Anwar checks, seed 20261003
========================================================================
A. spider monoids on the Riemann sphere (500 random pairs)
   Z: wz              max error 0.00e+00
   X: (wz+1)/(w+z)    max error 1.99e-15
   W: w+z             max error 0.00e+00
B. the two charts: phase addition and velocity addition
   X-spider, reciprocal chart, real segment = tanh(eta_1 + eta_2): max error 3.89e-16
   Z-spider, unit circle = phase addition:                        max error 1.05e-15
   diag(e^{i th},1) rotates the Bloch vector about Z by -th:       max error 6.29e-16
   diag(e^{eta},1) boosts n_z by rapidity eta (aberration law):     max error 6.66e-16
C. meromorphic decoders rebuilt from the codes' logical states
   Shor [[9,1,3]]         f_built / f_paper = (1-0j) (constant to 3.9e-15)
   five-qubit [[5,1,3]]   f_built / f_paper = (-1+0j) (constant to 9.3e-16)
   Steane [[7,1,3]]       f_built / f_paper = (1-0j) (constant to 2.7e-15)
D. Riemann--Hurwitz sum over branch points, including infinity
   Shor [[9,1,3]]         degree 9; finite branch points 7 with sheets [3]; at infinity 3 sheets; sum(m-1) = 16, 2(d-1) = 16 OK
      fixed points r(z)=0: (-0+1j), (-0-1j), (-0.618+0j), (-1+0j), (-1.618+0j), (0.618+0j), (1+0j), (1.618+0j), 0j
   five-qubit [[5,1,3]]   degree 5; finite branch points 8 with sheets [2]; at infinity 1 sheets; sum(m-1) = 8, 2(d-1) = 8 OK
      fixed points r(z)=0: (-0.7071+0.7071j), (-0.7071-0.7071j), (0.7071+0.7071j), (0.7071-0.7071j), 0j
      same decoder followed by logical Z (the +X^5 frame built above, f -> -f): fixed points (-1+0j), (1+0j), -1j, 0j, 1j
   Steane [[7,1,3]]       degree 7; finite branch points 5 with sheets [3]; at infinity 3 sheets; sum(m-1) = 12, 2(d-1) = 12 OK
      fixed points r(z)=0: -0.4142, -1.0, -2.4142, 0.0, 0.4142, 1.0, 2.4142
E. Klein's E7 invariant under S(z) = -iz (rel. err 0.0e+00) and H(z) = (z+1)/(z-1) (rel. err 1.8e-14)
   E7 at a stabilizer state (z=1): 0.0e+00; at an H-state (1+sqrt2): 1.000000000000; at an F-state: |E7| = 1.6e+26 (pole); E7(1/z)=E7(z): 6.0e-16
F. n-leg spiders: the Z (GHZ) spider is branched at the copyable states, the W spider is not
   n=2  Z -> prod z_i (err 0.0e+00): degree 2, branch points [(-0.0, 2)] + infinity with 2 sheets, sum(m-1)=2=2(d-1); W -> sum z_i (err 0.0e+00): degree 1, no branch points
   n=3  Z -> prod z_i (err 0.0e+00): degree 3, branch points [(0.0, 3)] + infinity with 3 sheets, sum(m-1)=4=2(d-1); W -> sum z_i (err 0.0e+00): degree 1, no branch points
   n=4  Z -> prod z_i (err 0.0e+00): degree 4, branch points [(0.0, 4)] + infinity with 4 sheets, sum(m-1)=6=2(d-1); W -> sum z_i (err 1.1e-16): degree 1, no branch points
   n=5  Z -> prod z_i (err 0.0e+00): degree 5, branch points [(0.0, 5)] + infinity with 5 sheets, sum(m-1)=8=2(d-1); W -> sum z_i (err 2.2e-16): degree 1, no branch points
========================================================================
BURTON--ANWAR CHECKS: PASS
```

## 4. The paper's existing engagement, checked against the text

`sec:hopf-compositional` cites Burton and Anwar twice. First: "That silence
has, in the months this paper was in draft, just begun to break from the
categorical side, with a projective, base-level reading of the same
calculus." Accurate: they projectivise a fragment of the ZXW-calculus and
work on the base $\mathbb{CP}^{1}$; they do not mention fibrations or
division algebras, so "from the categorical side" and "base-level" are both
right.

Second, after `prop:f1-dictionary`: "Burton and Anwar pass functorially to
the base and deliberately discard the fibre, and the classical structures
turn out to live in exactly the data their projectivisation forgets --- the
two readings compose, and the resulting triangle is a consistency condition."
The first clause is right ("annoying fluff on the carpet" is their phrase
for the global phase, and they discard the norm with it). The second clause
is overstated, and their Prop. 3.1 is the counter-evidence: the Frobenius
multiplications *survive* projectivisation, as the three monoids on the
pointed sphere ("lax monoidal functors preserve monoids"), with their units
($z=1$ for the Z-monoid, $z=\infty$ for the W-monoid, $z=0$ for the
X-monoid) and their idempotent, copyable points ($0$ and $\infty$ for Z).
What projectivisation forgets is the *section*: which lift of each copyable
ray the structure carries, the $\mathrm{Map}(P,U(1))$ torsor of the
proposition. So the accurate sentence is that the data distinguishing
structures with the same skeleton, the section, is exactly what their
functor forgets, while the skeleton and the monoid pass through. That is
still the proposition's point (classicality is section data) and still
composes with their reading; it is the word "structures" that overreaches.
Proposed v2 wording, for JS:

> Burton and Anwar pass functorially to the base and deliberately discard
> the fibre; the monoid of each structure survives the passage (their
> Prop. 3.1: the Z- and W-spiders become multiplication and addition on the
> Riemann sphere), and what their projectivisation forgets is exactly the
> section data that Proposition~\ref{prop:f1-dictionary} identifies as the
> structure's classical content --- the two readings compose, and the
> resulting triangle is a consistency condition available to constrain the
> remaining conditions of the correspondence.

Second-order status of the existing citation: reference exists, metadata
right, supports the first sentence, supports the second only after the
correction above. Recorded here, not edited around.

## 5. Where it meets the framework

(a) *Same base, different choice about the fibre.* The paper's
`sec:L2-metric` reaches $S^{3}/U(1)=\mathbb{CP}^{1}$ as the Bloch sphere by
the Hopf quotient and keeps the fibre (the global phase is "a clean
symmetry", the lifts carry the records' phases); Burton and Anwar reach the
same sphere by forgetting the fibre and the norm together, which is why
their maps are Möbius rather than unitary. Their "impossible element" $\bot$
is the projective name for the zero vector; in the complex-cost ledger it is
the outcome of infinite real cost, $-\ln 0$. RHYME, one sentence at most.

(b) *GHZ multiplies, W adds.* The entanglement-classes section identifies the
canonical GHZ and W orbits with the special and anti-special Frobenius
normalisations. Read projectively those two algebras are complex
multiplication and complex addition on the sphere. That is a clean sentence
to add there, citing Coecke, Kissinger, Merry and Roy 2011 for the arithmetic
and Burton and Anwar for its derivation by projectivisation (STRUCTURAL,
theirs, verified here). Whether "quarks multiply and leptons add" means
anything is a RHYME with no mechanism, and should not be written.

(c) *Ramification separates the classes.* Script part F, our observation
built from the spider matrices: the $n$-leg Z (GHZ) spider projectivises to
$z^{n}$, a degree-$n$ cover of the sphere branched only at the two copyable
states with $n$ sheets each (Riemann--Hurwitz $2(n-1)$ saturated by the two
points), while the $n$-leg W spider projectivises to $z_{1}+\dots+z_{n}$,
univariate $nz$, degree one, unbranched. So on the projective base the GHZ
class is the branched one and the W class the Möbius one; copying is
ramification, and the copyable states are the branch points. This is
elementary algebra once Prop. 3.1 is in hand (ESTABLISHED as a numerical and
algebraic fact), and it rhymes with the paper's "GHZ genuinely tripartite,
W pairwise-robust" without yet being the same statement; a RHYME until
someone relates the sheet number to a class invariant. One caution, written
down because the sphaleron thread shows the conflation is easy: the degree
$n$ here is the number of legs, not the charge winding of
`lem:winding-number`, which is the colour circle's spinor lift and has
nothing to do with how many registers a spider copies into.

(d) *The X-spider is a boost law, and the Z-spider is the other one.* Burton
and Anwar note that the X-monoid in the reciprocal chart is Lorentz velocity
addition and stop. The framework's spacetime section already says the
qubit's $SL(2,\mathbb{C})$ is the Lorentz group acting on the Bloch sphere
as the celestial sphere by Möbius maps. Put together, and checked in script
part B: for fixed $w$ the Z-monoid $z\mapsto wz$ is the Möbius map of
$\mathrm{diag}(w,1)$, which for $|w|=1$ rotates the Bloch vector about the
$Z$ axis and for real $w=e^{\eta}$ boosts it along $Z$ by rapidity $\eta$
(the aberration law $n_{z}\mapsto(n_{z}+\tanh\eta)/(1+n_{z}\tanh\eta)$,
verified to $10^{-16}$); the X-monoid is the same pair of one-parameter
groups about the $X$ axis, and its real section is Einstein's
velocity-addition law, $\tanh(\eta_{1}+\eta_{2})$. So the strongly
complementary pair of Frobenius algebras, read on the celestial sphere, is
the pair of abelian subgroups $\mathbb{C}^{*}$ of the Lorentz group about two
perpendicular axes, each a rotation times a boost. That is a precise,
checkable sentence for the celestial-sphere paragraph of the spacetime
section, and it makes the "qubit is Minkowski" reading one step more
concrete: complementarity is two perpendicular rotation-and-boost axes.
STRUCTURAL for the Möbius facts; the reading is CANDIDATE and stands with
the section's identification of measurement with cone-tipping.

(e) *"Which $i$ do you mean?"* Their closing question is one the framework
has an answer to in two parts. The Galois group of $\mathbb{C}/\mathbb{R}$,
complex conjugation, is the anti-event, the time reverse that closes the
Born-rule loop (two-columns note, 2026-09-18). The further ambiguity, which
imaginary unit of $\mathrm{Im}\,\mathbb{O}$ the amplitude's $i$ is, is a
point of $S^{6}=G_{2}/SU(3)$, and the stabiliser of the choice is colour
(complexified-vs-complex-structure note, section 4, CANDIDATE). Their
"states have names which are polynomials, ambiguous up to the Galois group"
also marks a contrast: the framework's charged-lepton mass eigenstates
carry the phase $\delta=2/9$ rad, whose exponential is transcendental
(ledger 2026-09-11, Lindemann--Weierstrass), so they lie in no number field
and have no polynomial name at all. Stabiliser, $H$- and $F$-states are
algebraic (cyclotomic, their App. D); generation states are not. RHYME, but
a sharp one, and it says the Koide phase is not a Clifford-type object.

(f) *Pure is holomorphic, mixed is not.* Their remark that incoherent states
need functions of $\bar{z}$ is the two-columns split seen from the base:
holomorphic in $z$ is the phase column, $\bar{z}$ enters when a record is
written. RHYME, one sentence.

(g) *What they do not do that the framework does.* No fibre, so no Berry
phase, no winding, no section data; no higher Hopf rungs, so no quaternionic
or octonionic structure; no SLOCC. Their Prop. 1.4 (lax monoidal, Segre
embedding) is the natural setting for the SLOCC classes as projective
varieties, which is Gharahi, Mancini and Ottaviani's paper (their [7]); the
framework's three-qubit classification could cite that paper as the
algebraic-geometric form of Dür--Vidal--Cirac (W on the tangential variety
of the Segre threefold, GHZ generic). Not in the library; batch written,
support from abstract only (VERIFY-SUPPORT).

## 6. Proposed wording, labels and references

v2 wording items, JS to rule:

1. `sec:hopf-compositional`, the second Burton--Anwar sentence: replace with
   the corrected sentence in section 4.
2. Entanglement-classes section, the special/anti-special sentence: add
   "read projectively, the two algebras are multiplication and addition on
   the Riemann sphere, the GHZ/W arithmetic of Coecke, Kissinger, Merry and
   Roy \autocite{coeckekissingermerryroy2011ghzw}, which Burton and Anwar
   derive by projectivisation \autocite{burtonanwar2026meromorphic}".
3. Spacetime section, celestial-sphere sentence: add one clause that the
   complementary Frobenius pair projectivises to the rotation-and-boost
   monoids about two perpendicular axes, the X-spider's law being Einstein
   velocity addition \autocite{burtonanwar2026meromorphic}, with the script
   as the check.
4. Optional: cite Gharahi, Mancini and Ottaviani where Dür--Vidal--Cirac is
   first cited, as the algebraic-geometric form of the classification
   (VERIFY-SUPPORT until read).

Labels proposed: Prop. 3.1 and the decoder examples STRUCTURAL (theirs,
verified here); the ramification distinction (c) ESTABLISHED as algebra,
RHYME as physics; the Lorentz reading (d) CANDIDATE; (a), (e), (f) RHYME.
No ledger entry is needed for the correction in section 4; it is a wording
item.

References: `burtonanwar2026meromorphic` is in the library and cited
(batch `bib/burton_anwar_meromorphic_ref_2026-10-03T1600.bib` is therefore
not to be imported; its header is the support record for the four claims
attached to the citation, all read against the text). New batch
`bib/ghzw_arithmetic_segre_refs_2026-10-03T1700.bib`: Coecke, Kissinger,
Merry and Roy 2011 (EPTCS 52) and Gharahi, Mancini and Ottaviani 2020 (Phys.
Rev. Research 2, 043003, Crossref-verified); support status in the batch.
