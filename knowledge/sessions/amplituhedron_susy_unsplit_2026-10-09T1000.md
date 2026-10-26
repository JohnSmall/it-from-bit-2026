# The amplituhedron, supersymmetry, and the unsplit octonionic spacetime (2026-10-09)

Session 2026-10-09, Fable 5.1. JS: "let's think about the amplituhedron. In
the initial work on this authors had to use supersymmetry, but that has no
place in our framework. Or has it?" Script
`scripts/n4_sym_unsplit_octonionic_spacetime_2026-10-09T1000.py` (Convention
A, seed 20261009, PASS), stdout in section 8. References verified against
the arXiv API and Crossref on 2026-10-09; none read this session beyond
abstracts, except the facts marked as textbook; batch in section 9. Read
first: `knowledge/invalid_routes.md` (nothing here is a mass route);
`knowledge/project-docs/division_algebra_objections_2026-09-27T1300.md` (the
"wrong dimension" row, which this note extends); the spacetime section's
$SL(2,\mathbb{O})\cong\mathrm{Spin}(9,1)$ sentences; the grounding argument's
section 10.5 (no remaining motivation for supersymmetry).

## 0. The answer in brief

Supersymmetry has a precise place in the framework, and it is not in the
world. The super-Yang--Mills theories exist in exactly the dimensions
$3,4,6,10$ because of $\mathbb{R},\mathbb{C},\mathbb{H},\mathbb{O}$ (Kugo and
Townsend 1983; Evans 1988; Baez and Huerta 2010), and the $\mathcal N=4$
theory in four dimensions whose amplitudes the amplituhedron computes is the
ten-dimensional octonionic theory reduced on six directions. Ten is the
framework's declined option: $SL(2,\mathbb{O})\cong\mathrm{Spin}(9,1)$, "the
unsplit ten-dimensional option the computability split declines". The
script makes the reduction exact in the framework's own coordinates. The
ten-dimensional Minkowski space is $\mathrm{Herm}_{2}(\mathbb{O})$; the
preferred complex line $\mathbb{C}\subset\mathbb{O}$ cuts it into a $(1,3)$
Minkowski space and a six-dimensional Euclidean complement, and that
complement is exactly the colour $\mathbb{C}^{3}$ of 2026-09-27. The six
scalars of $\mathcal N=4$ SYM are the six colour directions read as
positions; its $SU(4)_{R}=\mathrm{Spin}(6)$ is the rotation group of the
colour space; the choice of the complex structure $J=L_{e_{1}}$ on the six
breaks $\mathrm{Spin}(6)$ to $U(3)$, which is the $\mathcal N=4\to\mathcal
N=1$ decomposition of the R-symmetry, and the framework's colour $SU(3)$ is
the $G_{2}$ part of that $U(3)$, the extra $U(1)$ lying outside $G_{2}$. So
$\mathcal N=4$ SYM is the theory of the unsplit arena: supersymmetry is the
symmetry the octonionic rung has when it is read as spacetime, and the
computability split, which reads it as algebra, is what removes it. That
is the sentence the paper can own (CANDIDATE); the group theory under it
is textbook and verified (STRUCTURAL).

On the amplituhedron itself, two facts settle the practical question.
Tree-level gluon amplitudes are the same in pure Yang--Mills and in
$\mathcal N=4$, since superpartners do not propagate in gluon trees, so the
tree amplituhedron's gluon component *is* the pure-Yang--Mills tree
amplitude: supersymmetry is scaffolding there, essential only at loop
level. And the positive-geometry programme has since left supersymmetry
behind: the kinematic associahedron (2017), the cosmological polytope
(2017), the all-loop curve-integral or "surfaceology" formulation of
$\mathrm{Tr}\,\phi^{3}$ (2023), pions from hidden zeros (2023), and pure
Yang--Mills gluons scaffolded from coloured scalars (2024) are all
non-supersymmetric. Supersymmetry was the first case, not the condition.

## 1. What supersymmetry does in the amplituhedron, and what it does not

The construction (Arkani-Hamed, Bourjaily, Cachazo, Goncharov, Postnikov
and Trnka 2012; Arkani-Hamed and Trnka 2013) is for planar $\mathcal N=4$
SYM, and supersymmetry enters in four places.

1. *Packaging.* The superamplitude depends on momentum twistors $Z_{a}\in\mathbb{C}^{4}$
   and Grassmann variables $\eta_{a}\in\mathbb{C}^{0|4}$, one component per
   supercharge; all helicity configurations sit in one object, graded by
   Grassmann degree $4k$ for the N$^{k}$MHV sector.
2. *Bosonisation.* The amplituhedron $\mathcal A_{n,k,m}$ is the image of the
   positive Grassmannian $G_{+}(k,n)$ in $\mathrm{Gr}(k,k+m)$ under a positive
   $n\times(k+m)$ matrix, with $m=4$ for physics. The $4$ of $k+4$ is the
   twistor dimension; the $k$ is obtained by bosonising the $\eta$'s with $k$
   auxiliary Grassmann variables. That the Grassmann degree $4k$ matches a
   $k$-plane in $k+4$ dimensions needs $\mathcal N=4$ exactly: the number of
   supercharges equals the twistor dimension, which is the coincidence of
   $\mathcal N=4$ with $D=4$, itself a division-algebra fact ($10=4+6$,
   $SU(4)_{R}=\mathrm{Spin}(6)$, section 3).
3. *The dlog forms.* On-shell diagrams in any planar gauge theory are the
   same positroid cells; what changes with $\mathcal N$ is the measure: for
   $\mathcal N=4$ it is the canonical $\prod d\log\alpha_{i}$, for $\mathcal N<4$
   it is that form times a factor carrying the ultraviolet behaviour
   (ABCGPT; Benincasa 2015 for $\mathcal N\le2$ including pure YM; Brown,
   Oktem and Trnka 2022 on the poles at infinity those factors produce).
   "Positive geometry" in the canonical-form sense is the $\mathcal N=4$
   case.
4. *Dual conformal symmetry and the loop integrand.* Momentum twistors are
   natural because planar $\mathcal N=4$ has dual conformal (Yangian)
   symmetry, and the loop integrand is a well-defined rational function
   only in the planar limit with that symmetry.

What supersymmetry does not do: at tree level, with external gluons only,
no superpartner runs anywhere, so the $n$-gluon tree amplitudes of pure
Yang--Mills, $\mathcal N=1$ and $\mathcal N=4$ coincide, and the
amplituhedron's tree-level gluon component is the pure-YM answer. The
statement "supersymmetry has no place in our framework" is therefore too
strong for the tree amplituhedron, whose gluon output the framework must
reproduce like everyone else; it is right for the loop amplituhedron, where
the superpartners circulate. STRUCTURAL (textbook), VERIFY-SUPPORT against
ABCGPT ch. on $\mathcal N<4$ for item 3.

## 2. Positive geometry without supersymmetry [STRUCTURAL, from abstracts]

- Arkani-Hamed, Bai and Lam 2017, "Positive geometries and canonical forms":
  the general definition, with no field theory attached.
- Arkani-Hamed, Bai, He and Yan 2017: the kinematic associahedron for
  bi-adjoint $\mathrm{Tr}\,\phi^{3}$, the first positive geometry for a
  non-supersymmetric theory, with colour and the worldsheet in the same
  picture.
- Arkani-Hamed, Benincasa and Postnikov 2017: the cosmological polytope for
  the wavefunction of the universe, conformally coupled scalars.
- Arkani-Hamed, Frost, Salvatori, Plamondon and Thomas 2023, "All loop
  scattering as a counting problem": $\mathrm{Tr}\,\phi^{3}$ at all loops
  and genus as integrals over curves on surfaces.
- Arkani-Hamed, Cao, Dong, Figueiredo and He 2023, "Hidden zeros": pions
  (the non-linear sigma model) from $\mathrm{Tr}\,\phi^{3}$ by a kinematic
  shift; and 2024, "Scalar-scaffolded gluons and the combinatorial origins
  of Yang--Mills theory": pure Yang--Mills gluon amplitudes from the same
  scalar curve integrals, the gluon polarisations arising from pairs of
  scalars.

So the non-supersymmetric gauge theory the framework contains does have a
positive-geometry-style description, by a route that does not pass through
the amplituhedron. If the paper mentions the programme, it should cite the
2024 scaffolding paper rather than the amplituhedron as the point of
contact.

## 3. Where supersymmetry sits in the framework's own algebra [STRUCTURAL; verified]

The theorem (Kugo and Townsend 1983; Evans 1988; Baez and Huerta 2010):
super-Yang--Mills exists in $D=n+2$ for $n=1,2,4,8$, the dimensions of
$\mathbb{R},\mathbb{C},\mathbb{H},\mathbb{O}$, because the supersymmetry of the
action needs a trilinear spinor identity (the "3-$\psi$'s rule") that holds
exactly when the spinors are valued in a normed division algebra; the
Lorentz group in $D=n+2$ is $SL(2,\mathbb{K})$. The $\mathcal N=4$, $D=4$
theory is the $D=10$, $\mathbb{K}=\mathbb{O}$ theory reduced on six
dimensions, its sixteen supercharges the one Majorana--Weyl spinor of ten
dimensions, its $SU(4)_{R}\cong\mathrm{Spin}(6)$ the rotation group of the six.

The script puts this in the framework's coordinates:

- $\mathrm{Herm}_{2}(\mathbb{O})$, the $2\times2$ Hermitian octonionic matrices,
  is ten-dimensional with determinant $ab-|o|^{2}$ of signature $(1,9)$:
  the Minkowski space of $SL(2,\mathbb{O})\cong\mathrm{Spin}(9,1)$ (Baez 2002,
  in the library). Restricting $o$ to the preferred line $\mathbb{C}=\mathrm{span}(1,e_{1})$
  gives signature $(1,3)$; the complement, $o\in\mathrm{span}(e_{2},\dots,e_{7})$,
  is six-dimensional Euclidean (part A). The six are the $e_{1}$-invariant
  complement of 2026-09-27: the colour $\mathbb{C}^{3}$. So $10=4+6$ with
  the six being colour space, and the six scalars of $\mathcal N=4$ SYM are
  the six colour directions read as positions.
- The derivations of $\mathbb{O}$ fixing $e_{1}$ (the colour $\mathfrak{su}(3)$,
  dimension 8) act on $\mathrm{Herm}_{2}(\mathbb{O})$ fixing the Minkowski four
  pointwise and rotating the six (part B); a generic derivation moves
  $e_{1}$ and mixes them. Colour is the part of $G_{2}$ that is internal to
  the reduced theory, which is what "internal" means in Kaluza--Klein
  language.
- $J=L_{e_{1}}$ restricted to the six is a complex structure; $\mathfrak{u}(3)=\{A\in\mathfrak{so}(6):[A,J]=0\}$
  is nine-dimensional; every colour derivation lies in it with zero complex
  trace; $J$ itself is in $\mathfrak{u}(3)$ and is not a derivation (Leibniz
  residual $3$). So $\mathfrak{g}_{2}\cap\mathfrak{u}(3)=\mathfrak{su}(3)$ and the
  $U(1)$ completing colour to $U(3)$ lies outside $G_{2}$ (part C). In
  $\mathcal N=4$ language: choosing a complex structure on the six breaks
  $SU(4)_{R}=\mathrm{Spin}(6)$ to $U(3)=SU(3)\times U(1)$, under which the
  supercharges go $\mathbf 4\to\mathbf 3\oplus\mathbf 1$ and the scalars
  $\mathbf 6\to\mathbf 3\oplus\bar{\mathbf 3}$; this is the decomposition of
  $\mathcal N=4$ into $\mathcal N=1$ language (one vector multiplet, three
  adjoint chirals rotated by $SU(3)$, $U(1)_{R}$). Textbook,
  VERIFY-SUPPORT. The framework's $G_{2}\to SU(3)$ by the preferred
  direction and the $\mathcal N=4\to\mathcal N=1$ reduction
  $\mathrm{Spin}(6)\to U(3)$ are the same reduction on the six.
- For contrast (part D), the quaternionic rung: $\mathrm{Herm}_{2}(\mathbb{H})$
  has signature $(1,5)$, the preferred line gives $(1,3)$, the complement is
  $\mathbb{C}^{1}$, and the derivation fixing $e_{1}$ is $\mathrm{ad}_{e_{1}}$
  itself, which in $\mathbb{H}$ *is* a derivation: no colour at rung two, as
  the paper says, and the six-dimensional theory's $\mathcal N=2$ has
  $SU(2)_{R}$ rather than $SU(4)_{R}$.

The reading, which is the framework's own and CANDIDATE: $\mathcal N=4$
SYM is the theory of the unsplit arena. Its supersymmetry is what the
octonionic rung has when the six directions are geometry; the
computability split reads them as algebra (gauge charge, the paper's $S^{7}$
sector), and in doing so removes the supersymmetry, keeping the $SU(3)$
and the $U(1)$ as the colour and the preferred direction's phase. The
spacetime section's sentence that "the Kaluza--Klein and string intuition
is tracking something real in the $S^{7}$ structure, but misdiagnoses it as
spatial" applies to $\mathcal N=4$ SYM exactly: it is the Kaluza--Klein
reduction of the octonionic spacetime, and the amplituhedron is its
geometry.

## 4. Why the split world has no superpartners [the paper's own results]

The reduction of section 3 lands on the R-symmetry of $\mathcal N=1$, not
on $\mathcal N=1$ itself, and the framework's world is $\mathcal N=0$. Three
reasons already in the paper, none new:

- The termination theorem (`prop:termination`; Adams, Hurwitz and
  Eakin--Sathaye, STRUCTURAL in the ledger): no new kinematic structure
  appears above the fourth qubit, so the entanglement alphabet is Bell, GHZ,
  W, and there is no room in the register for a doubled spectrum.
- The no-leptoquark theorem (ESTABLISHED, conditional): all trilinear
  vertices beyond the gauge ones are closed; a supersymmetric spectrum needs
  the gaugino and squark couplings.
- The grounding argument, section 10.5: with the hierarchy, unification and
  dark-matter motivations handled elsewhere, nothing motivates
  superpartners, and the LHC null results are consistent
  (`framework_summary_for_llm_review.md`).

And one reason that is structural rather than empirical: the preferred
direction is a *record* (sec:fanout-direction), a classical commitment,
not a supercharge direction. The $\mathcal N=4\to\mathcal N=1$ decomposition
keeps one Grassmann direction unbroken; the framework's split keeps none,
because what selects $e_{1}$ is a copy firing, and a copy is a real-column
event. So the group theory of the reduction is $\mathcal N=1$'s, the
spectrum is $\mathcal N=0$'s. CANDIDATE.

## 5. The 3-$\psi$'s rule and the associator [RHYME, with one CANDIDATE clause]

Baez and Huerta's theorem is that supersymmetry of the Yang--Mills action
needs the identity $(\psi\psi)\psi=0$ for spinors $\psi\in\mathbb{K}^{2}$,
which holds exactly when $\mathbb{K}$ is alternative: the associator must
cancel in a specific alternating combination. The framework reads mass as
associator debt, the associator failing to cancel when the preferred
direction composes cross-copy legs (`sec:associator-higgs`), and $\mathcal
N=4$ SYM is conformal and massless with no preferred direction
($SU(4)_{R}$ unbroken, no Yukawa vertex of the framework's kind). So the
rhyme is: supersymmetry is the regime in which the associator cancels, and
mass is the regime in which it does not; the split that gives the
framework its masses is the split that removes the supersymmetry. One
clause of this is more than a rhyme and is CANDIDATE: in the framework
there is no mass without a preferred direction, and in $\mathcal N=4$ there
is no mass without breaking $SU(4)_{R}$ (the Coulomb branch), and the
reduction of section 3 identifies the two symmetry groups. The caution
is that the Coulomb-branch vev is a direction in the six (breaking
$\mathrm{Spin}(6)\to\mathrm{Spin}(5)$), while the framework's preferred
direction is a direction in the seven of $\mathrm{Im}\,\mathbb{O}$ (breaking
$G_{2}\to SU(3)$); these are different breakings, and no identification of
the Higgs mechanisms is claimed. The 3-$\psi$'s identity itself was not
checked numerically (its conventions were not read); the alternativity of
$\mathbb{O}$ and its failure in the sedenions are already in the ledger.

## 6. Two precisions on the sentence that started this thread

The opening sentence of 2026-10-07 was "the amplituhedron lives in
momentum-twistor space, and twistor space $\mathbb{CP}^{3}$ fibres over
$S^{4}$". Two things in it should be tightened before any of it reaches
the paper.

- *Signature.* The amplituhedron's positivity is a real notion: real
  momentum twistors with all ordered minors positive. The real form in
  which momentum twistors are real is split signature $(2,2)$, where
  twistor space is $\mathbb{RP}^{3}$ and the twistor correspondence is the
  real Klein correspondence, a double fibration through the flag manifold,
  not a fibre bundle. The Euclidean fibration $\mathbb{CP}^{3}\to S^{4}$ of
  the twistor note is a different real slice of the same complex
  correspondence. Both are real forms of one object; the sentence
  conflated them. The quaternionic Hopf map factors through the Euclidean
  form; the amplituhedron lives in the split form.
- *Chirality.* The amplituhedron is built on momentum twistors, not
  ambitwistors, so it is chiral: parity is not manifest, the parity
  conjugate of the N$^{k}$MHV amplituhedron is the N$^{n-4-k}$MHV one in dual
  twistors. In split signature $\mathrm{Spin}(2,2)=SL(2,\mathbb{R})\times SL(2,\mathbb{R})$
  and the two chiralities are real and independent, which is the
  chirality thread of 2026-10-07 in its third signature. Woit, in a 2014
  post, took the amplitudes work as one application of twistor variables
  and no more (blog, not a paper; not cited).

And one RHYME for the two-columns ledger, fenced: the amplituhedron is an
object of orderings and inequalities, with a rational integrand whose
residues are $\pm1$ and no phases; the $i$'s and $\pi$'s of the amplitude
appear only when the integrand is integrated. In the ledger's terms the
positive geometry is the real column of the S-matrix and the integration
is where the imaginary column is paid. One sentence at most, and not in
Paper 1.

## 7. What the framework could do with the programme [directions, not results]

- The paper owes nothing to the tree amplituhedron and contradicts
  nothing in it: pure-YM gluon trees are its gluon component. If the
  paper cites the programme, the point of contact is the 2024 scaffolding
  paper (non-supersymmetric gluons), with the amplituhedron named as the
  $\mathcal N=4$ case that the unsplit reading explains.
- A framework-native positive geometry would be colour-ordered with $N=3$
  fixed rather than planar at large $N$; the programme's $1/N$ corrections
  are not small at $N=3$, and the framework has no planar limit to take.
- One structural question worth a note of its own, not opened here: the
  on-shell diagrams of ABCGPT are bipartite graphs whose black and white
  trivalent vertices are the two three-point primitives (the $\overline{\mathrm{MHV}}$
  and MHV amplitudes, supported on $\mathrm{Gr}(2,3)$ and $\mathrm{Gr}(1,3)$),
  and their positroid cells are the images of these graphs; the
  ZW-calculus of Coecke and Kissinger is a bipartite graphical calculus
  whose two spiders are the GHZ and W primitives, and Burton and Anwar
  (2026-10-03) read those projectively as multiplication and addition on
  the Riemann sphere. Whether the positroid cell of an on-shell diagram
  and the Frobenius class of the corresponding tensor network correspond
  is a question neither literature has asked. RHYME until someone computes
  a case; the three-point objects are the place to start.

## 8. Exact stdout of `scripts/n4_sym_unsplit_octonionic_spacetime_2026-10-09T1000.py`

```
N = 4 SYM as the unsplit octonionic spacetime, Convention A, seed 20261009
======================================================================================
A. Herm_2(O): det = ab - |o|^2 has signature (1, 9): Spin(9,1)
   o restricted to C = span(1,e1): signature (1, 3), Minkowski; complement o in C^3: signature (0, 6), six Euclidean
   10 = 4 + 6, the six being the e1-invariant complement, i.e. the colour C^3 of 2026-09-27
B. dim Der(O) = 14 (g2)
   dim Stab_g2(e1) = 8 (colour su(3))
   colour derivations act on Herm_2(O) fixing (a, b, o_0, o_1) pointwise: max leakage 1.5e-15; a generic derivation moves e1: 0.414
C. J = L_e1 on C^3: J^2 = -1 (0.0e+00), orthogonal (0.0e+00)
   every colour derivation commutes with J on the six: max 2.1e-15   (so colour c u(3))
   dim u(3) = dim{A in so(6): [A, J] = 0} = 9; dim so(6) = 15
   J itself is in u(3) (it commutes with itself) but is NOT a derivation of O: Leibniz residual 3.000
   complex trace of every colour derivation on C^3: 2.3e-16  -> g2 ∩ u(3) = su(3), the U(1) of U(3) lies outside G2
D. quaternions: dim Der(H) = 3 (so(3)); dim Stab(e1) = 1; L_e1 as a derivation? residual 0.0e+00 (it is one: ad_e1)
   Herm_2(H): signature (1,5); preferred C gives (1,3); complement C^1: no su(n) with n > 1: no colour at rung two
======================================================================================
N4 UNSPLIT: PASS
```

## 9. Proposed ledger entries and references

- **STRUCTURAL** (verified) $\mathrm{Herm}_{2}(\mathbb{O})$ has signature $(1,9)$;
  the preferred complex line cuts it into a $(1,3)$ Minkowski space and the
  six-dimensional colour complement; the colour derivations fix the four
  and rotate the six; $\mathfrak{g}_{2}\cap\mathfrak{u}(3)=\mathfrak{su}(3)$
  with the $U(1)$ of $U(3)$ outside $G_{2}$. (The $(1,9)$ signature and
  $SL(2,\mathbb{O})\cong\mathrm{Spin}(9,1)$ are Baez 2002; the rest is this
  session's computation.)
- **CANDIDATE** $\mathcal N=4$ super-Yang--Mills is the theory of the unsplit
  octonionic spacetime: its six scalars are the colour directions read as
  positions, its $SU(4)_{R}$ the rotation group of colour space, its
  $\mathcal N=4\to\mathcal N=1$ R-symmetry reduction the framework's
  $G_{2}\to SU(3)$; supersymmetry is what the octonionic rung has as
  geometry and loses as algebra. The amplituhedron is the positive
  geometry of that unsplit theory.
- **CANDIDATE** The split world has no superpartners: the termination
  theorem leaves no register room, the no-leptoquark theorem closes the
  vertices, and the preferred direction is a record, not a supercharge
  direction.
- **RHYME** Supersymmetry is the regime where the associator cancels
  (the 3-$\psi$'s rule), mass the regime where it does not.
- *Precision owed* to this thread's opening sentence: the amplituhedron's
  real form is split signature; the Euclidean twistor fibration is a
  different real slice.

Batch `bib/amplituhedron_susy_division_refs_2026-10-09T1100.bib`: fourteen
entries, metadata from the arXiv API and Crossref; journal references for
Baez--Huerta, Hodges and Arkani-Hamed--Bai--Lam are from memory and marked
VERIFY-CITE; all VERIFY-SUPPORT (abstracts only). The library already has
`baez2002octonions`, `coeckekissinger2010compositional`,
`burtonanwar2026meromorphic`.


## 10. Does the amplituhedron make contact with experiment? (added 2026-10-09T1200)

JS: "Does the amplituhedron make contact with experimental results?" From
knowledge, with the references Crossref-verified on 2026-10-09 (none read);
one web search for any amplituhedron-based collider prediction found none.

*Directly, no.* The amplituhedron computes amplitudes of planar
$\mathcal N=4$ super-Yang--Mills, a conformal, massless, supersymmetric
theory with no experimental realisation, and no number derived from the
amplituhedron has been compared with data. Its proponents' claim for it is
structural (locality and unitarity as outputs of positivity), and its
practical use is the computation of higher-loop integrands in that one
theory.

*Indirectly, in three ways, none of which is the amplituhedron itself.*

1. *Tree-level gluon amplitudes are theory-independent* (section 1): the
   $n$-gluon trees of pure Yang--Mills, hence of QCD with gluons only, are
   the gluon component of the tree amplituhedron. These enter every
   leading-order QCD prediction, but they were known by BCFW and
   Parke--Taylor before the amplituhedron and are not computed from it in
   practice.
2. *The supersymmetric decomposition of one-loop QCD.* Bern, Dixon, Dunbar
   and Kosower (1994, 1995) write a one-loop QCD gluon amplitude as
   $A^{\mathcal N=4}-4A^{\mathcal N=1\,\text{chiral}}+A^{\text{scalar}}$:
   the $\mathcal N=4$ one-loop amplitude is literally one term of the
   physical QCD amplitude, the simplest term, cut-constructible from box
   integrals. Through this, the planar one-loop objects the amplituhedron
   organises are a component of the one-loop amplitudes used in LHC
   predictions, and the on-shell and unitarity methods that produced the
   decomposition are the working tools of multi-loop QCD (BlackHat and its
   successors, Berger et al. 2008). This is the amplitudes programme's
   contact with experiment; the amplituhedron inherited the methods and
   returned none.
3. *The double copy and gravitational waves.* The sibling programme of
   gravity as the square of gauge theory produced the conservative
   two-body Hamiltonian at third post-Minkowskian order (Bern, Cheung,
   Roiban, Shen, Solon and Zeng 2019), which feeds the waveform models
   LIGO and Virgo compare with data. Again the programme, not the
   amplituhedron.

So the honest sentence is: the amplituhedron has made no contact with
experiment; the tools around it have, and the $\mathcal N=4$ amplitudes it
reorganises are one summand of a physical QCD amplitude at one loop.

*The framework's reading of why.* Section 3 read $\mathcal N=4$ SYM as the
theory of the unsplit arena, the octonionic rung as geometry before the
computability split. Experiments are records, and the unsplit theory has
no records: no preferred direction, no masses, no scale. So on the
framework's own terms the amplituhedron *cannot* meet experiment except
through what survives the split, and the three contacts above are exactly
that: the gluon trees, which are the same on both sides of the split; the
$\mathcal N=4$ summand of the one-loop amplitude, which is the unsplit
piece of a split quantity; and gravity, which in the framework is
post-record bookkeeping and in the double copy is reached by squaring the
unsplit theory. That the amplituhedron's experimental contact is confined
to these is what the "unsplit theory" reading predicts; it is a
consistency, not a test. CANDIDATE, one clause in the note's section 9
entry; not for the paper.

References, added to the batch: Bern, Dixon, Dunbar and Kosower 1994 and
1995 (Nucl. Phys. B 425, 217 and 435, 59); Berger et al. 2008 (Phys. Rev. D
78, 036003); Bern, Cheung, Roiban, Shen, Solon and Zeng 2019 (Phys. Rev.
Lett. 122, 201603). All Crossref-verified, none read, VERIFY-SUPPORT.
