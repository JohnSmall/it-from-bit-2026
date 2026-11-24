# Confinement as an exhausted budget and confinement as a flux tube: the copy structure read twice

Fable session, 2026-11-07T1130. Script
`scripts/confinement_budget_flux_tube_2026-11-07T1130.py` (PASS, stdout in
section 14). Bibliography batch `bib/confinement_flux_tube_refs_2026-11-07T1140.bib`.
Companion to this morning's `relational_distance_lattice_2026-11-07T0700.md`.

JS's question: "The framework's reading of confinement from saturation of
the entanglement budget in GHZ, colour force, compositions is direct and
elegant. But it's so different from the idea that confinement comes from
the colour force being squeezed into string-like connections that it's
hard to see any connection. And yet it is the most interesting and
revealing place to investigate. The different points of view have to be
aligned somehow."

## 0. The answer in five lines

1. The two pictures share one object, and the paper already names it
   without noticing that the lattice does too. The GHZ class is the
   special Frobenius structure, the copy map (Coecke and Kissinger 2010;
   the paper's glueball subsection: "the GHZ structure is special
   Frobenius --- it possesses the copy operation"). Gauss's law at an
   uncharged vertex of a lattice gauge theory, written in the electric
   (flux) basis, is that same copy map: flux in equals flux out, the
   representation label is passed whole from link to link. Script B: for
   Z_N the neutral subspace at a k-valent vertex has dimension N^(k-1), its
   uniform superposition is the Fourier transform of the N-level GHZ_k
   state (fidelity 1.000000000000 for N = 2, 3 and k = 2, 3, 4), the
   two-valent vertex is the copy map, a chain of them has exactly one
   neutral configuration (the source charge copied along every link), and
   the trivalent Z_3 vertex is neutral at (1,1,1): three fundamentals
   meeting, the baryon junction. The W state is a charged vertex.
2. A flux tube is therefore a chain of copy maps carrying the colour label
   from one charge to another, which is precisely the "colour-basis
   FANOUT built of quarks and gluons, not of records" that the Bell
   subsection of the confinement section says must exist and that no
   record can read. "Squeezed into a string" and "budget exhausted" are the
   copy structure read as a map (the chain) and as a state (the junction:
   the Z_2 trivalent Gauss spider has three-tangle 1 and pairwise
   concurrence 0, script B). The same all-or-nothing character shows at
   the state level as 1 ebit across every cut of GHZ_n independent of n
   (script A) and at the flux level as the label being indivisible.
3. Copy versus share is the tube versus the Coulomb field, and it is an
   energy statement (script C). A centre charge over m parallel routes
   costs R c(1) for every m: one route takes it whole. A real-valued
   Abelian flux costs R q^2/m: it spreads. On a lattice the shared law is
   linear in d = 1, logarithmic in d = 2 (slope 0.1602 against 1/2pi =
   0.1592) and Coulomb in d = 3 (slope -0.0834 against -1/4pi = -0.0796);
   the copied law is c(1) times the graph distance in every d. The
   Coulomb law needs the embedding to count routes; the confining law
   needs only the count of links, which in this framework is what distance
   is (sec:comp-distance). The framework has the linear potential for
   free and owes the Coulomb term, the reverse of the standard order.
4. What is confined is the centre charge, and the centre grades the
   computability split (script D). The map that fixes the record line
   (e_0, e_1) and rotates the colour C^3 by a phase is an automorphism of
   the octonions exactly at the cube roots of unity (residual 6e-16 there,
   at least 0.40 elsewhere); it is the scalar omega on the colour C^3,
   the identity on the record line, central in the su(3) stabiliser and
   not in g_2. N-ality: record 0, colour 1, anticolour 2. "No classical
   record carries bare colour" is 't Hooft's criterion "no asymptotic
   state has non-zero N-ality" ('t Hooft 1978), and the lattice fact that
   the asymptotic string tension depends only on N-ality (Lucini and
   Teper 2001) with adjoint strings breaking (de Forcrand and Philipsen
   2000) is the statement that only the record-side datum is screenable.
5. One fence the alignment forces (script E): the SU(3) singlet
   epsilon_{ijk}|ijk> has maximally mixed one-quark marginals, as GHZ_3
   does, but its two-quark marginal is the antisymmetric Werner state with
   negativity 1/3; the qubit and qutrit GHZ_3 have separable pairs. The
   budget argument's robust clause is the one-to-rest saturation (slack
   r^2 = 0), which the Bell subsection already uses; its clause "every
   bipartite tangle, internal or external, is forced to zero" holds in the
   register model and not for the SU(3) singlet. The alignment must run
   through r = 0 and the copy structure, not through pairwise zero. And
   the alignment is kinematic: the paper's own "the budget alone does not
   confine" stands, because the same Gauss law admits a Coulomb phase for
   compact U(1) in four dimensions (Guth 1980), so which phase is realised
   is the lattice's answer, not the spider's.

## 1. What the corpus says

Quoted from `paper1/confinement_section_2026-06-13.tex` unless stated.

- Lines 127--161, the budget subsection: "the binding state is the maximal
  GHZ state --- the colour singlet"; "For the maximal GHZ state tau_3 = 1:
  the budget is fully spent on the tripartite binding, and every bipartite
  tangle, internal or external, is forced to zero"; "This is not a force
  that grows with separation; it is a property of the state, with no
  distance in it."
- Lines 163--221, `sec:budget-converse`: the W register's slack 1/9, the
  external ceiling, and the sentence that travels: "record-broadcast
  structures are GHZ-shaped copy tensors, external GHZ participation is
  the one mode whose pairwise cost vanishes".
- Lines 223--300, `sec:bell-not-counterexample`: "Confinement is the claim
  that no classical record ever carries bare colour"; "To copy a colour
  state one needs an ancilla spanning the colour space ... a colour-basis
  FANOUT is built of quarks and gluons, not of records"; the access
  ladder, slack = r^2 = sup C_frac, "the quark's locked wire is its
  species-defining sector, its access is exactly zero"; and the closing
  "the budget alone does not confine. The budget, the sector, and the
  access do."
- Lines 318--343, the distance-free subsection and `op:confinement-potential`:
  "No flux tube or confining medium is posited"; derive the string
  tension "as the associator-geodesic length ... resolved by the emergent
  distance", with "asymptotic freedom at short range as the limit in which
  little tripartite budget is yet committed".
- Lines 360--392, `prop:energy-locus`: three Bell pairs on the triangle
  with Frobenius fusion at each vertex contract to GHZ_3 at success 1/4;
  "The quark triple and the gluon network are two contraction orders of
  one closed tensor".
- Lines 395--410, glueballs: "A quark trio produces a classical colour
  record for free, because the GHZ structure is special Frobenius --- it
  possesses the copy operation that broadcasts a record".
- Lines 636--645, the mass-gap subsection: "in a fixed lattice geometry,
  the question of whether the budget-saturation constraint of this
  section reproduces area-law Wilson loops is one that tensor-network
  methods can address now, and it is the interface at which this
  framework's account of confinement first becomes commensurable with the
  standard one". JS's question is this interface.
- `paper1/quantum_numbers_section_2026-06-08.tex` lines 236--249: the Z_6
  quotient "identifies a combination of the Z_3 centre of colour, the Z_2
  centre of weak isospin, and a U(1)_Y phase", with hypercharge "locked to
  its colour triality". The centre of colour is in the paper; its action
  on the split is not.
- `knowledge/project-docs/open_problem_asymptotic_freedom.md` (April
  2026): "In a baryon, the colour singlet condition epsilon_{ijk}|i>|j>|k>
  is a GHZ state across three qutrits" and "At every level, tracing out
  any colour subsystem destroys all colour entanglement." Script E
  contradicts both for the SU(3) singlet (section 6).
- This morning's note, section 9(a): the lattice's string tension is a
  count per face and the relational derivation runs the same inference
  backwards; PASS for `op:confinement-potential` is a coefficient.

## 2. The standard picture, stated so that it can be aligned

Six statements, all STRUCTURAL (imported), each with the reference the
batch carries.

(a) The confinement criterion is the area law of the Wilson loop, and the
string tension sigma is its coefficient (Wilson 1974). At strong coupling
the area law is a tiling of the minimal surface by faces and sigma is the
cost per face; this morning's script A exhibited the two-dimensional case
exactly.

(b) In the Hamiltonian formulation (Kogut and Susskind 1975) the electric
energy is a sum over links of (g^2/2) times the quadratic Casimir of the
representation the link carries, and Gauss's law at each vertex ties the
representations of the incident links together. At strong coupling a
source and sink in the fundamental are joined by the shortest chain of
links in the fundamental and V(R) = (g^2/2a) C_2(fund) R: linear, with
the cost per link the Casimir (Casimir scaling, which the lattice confirms
at intermediate distance; Bali 2001).

(c) The dynamical mechanism proposed for the squeezing is the dual Meissner
effect: a condensate of chromomagnetic monopoles expels electric flux into
a tube of fixed cross-section (Mandelstam 1976; 't Hooft 1981). Polyakov
1977 showed compact U(1) in three dimensions confines by monopoles; in four
dimensions compact U(1) has a Coulomb phase at weak coupling (Guth 1980;
Banks, Myerson and Kogut 1977). The tube's transverse profile has been
measured on the lattice (Bali, Schlichter and Schilling 1995) and the
string's fluctuations give the Lüscher term -pi/(12 R) (Lüscher, Symanzik
and Weisz 1980; Lüscher 1981).

(d) The datum that cannot be screened is the centre charge. Gluons carry
N-ality 0, so a source of N-ality k can be screened only down to the
lightest representation of the same N-ality: the asymptotic string tension
depends on k alone ('t Hooft 1978; Lucini and Teper 2001; Del Debbio et al.
2001), and an adjoint string breaks (de Forcrand and Philipsen 2000). With
dynamical quarks the fundamental string breaks too, by pair creation, at
about 1.2 fm (Bali et al. 2005).

(e) The baryon's three strings meet at a junction, the Y shape, with the
junction the SU(3) intertwiner epsilon_{ijk} (Takahashi et al. 2001).

(f) The phenomenological potential is the Cornell form, V(r) =
-(4/3) alpha_s/r + sigma r (Eichten et al. 1978): a Coulomb term from
one-gluon exchange at short distance and the linear term at long.

## 3. The common object: Gauss's law is the GHZ spider (script B)

Work in the electric basis of a Z_N lattice gauge theory: each link carries
e in Z_N, and the Gauss operator at a vertex is the signed sum of the
incident e's modulo N (inward +, outward -). The neutral subspace is the
kernel.

- Count. For valence k the neutral configurations number N^(k-1) (2, 4, 8
  for Z_2; 3, 9, 27 for Z_3 at k = 2, 3, 4).
- Spider. The uniform superposition over the neutral configurations is,
  leg by leg, the Fourier transform (conjugated on outward legs) of the
  N-level GHZ_k state (1/sqrt N) sum_a |a...a>. Fidelity 1 to twelve
  places in all six cases. In Coecke and Duncan's language (2011) the
  neutral subspace is spanned by the X-spider, the group-algebra Frobenius
  structure on C[Z_N], and the GHZ state in the holonomy basis is the
  Z-spider, the function-algebra structure; the two are strongly
  complementary and both are GHZ-class. Gauss's law is a spider.
- Budget. For Z_2 at k = 3 the spider state has three-tangle 1.000000,
  pairwise concurrence 0.000000 and one-tangle 1.000000: it saturates the
  budget exactly as the paper's colour singlet does, because it is
  H^(x3) GHZ_3. For Z_3 at k = 3 the two-party negativity is 0 and the
  one-party purity 1/3.
- Copy. The two-valent (in, out) neutral subspace is {(e, e)}: the copy
  map. A chain of five links from a source of charge 1 has exactly one
  neutral configuration, (1,1,1,1,1), for Z_2 and for Z_3: the charge is
  copied along every link. This is the flux tube in the electric basis: a
  classical channel for the colour label, in Coecke and Kissinger's own
  reading of the GHZ spider.
- Junction. For Z_3 with three inward legs, (1,1,1) is neutral: three
  fundamentals meeting at a point carry no centre charge. So are (2,2,2)
  and every permutation of (0,1,2) (a fundamental passing through as an
  antifundamental, the meson chain). The configurations (1,0,0) and
  (1,1,0) are charged, with N-ality 1 and 2: open flux must end on a
  charge.
- Charge. The W_3 state, one unit of flux on one of three inward legs, is
  orthogonal to the neutral subspace and an eigenstate of the Gauss
  operator with charge 1 for Z_2 and Z_3. The W structure at a vertex is
  a source, not a junction.

The identification is standard in the tensor-network treatment of gauge
theories, where the gauge-invariant subspace is built by placing a
Gauss-law projector, the group average, at every vertex (Haegeman et al.
2015; Tagliacozzo, Celi and Lewenstein 2014; Zohar and Burrello 2015), and
the toric code's ground state, the Z_2 case, is a PEPS whose vertex tensors
are copy tensors (Verstraete et al. 2006; Kitaev 2003). None of it is the
framework's. What is the framework's is that its confinement argument is
stated in exactly these terms already: the special Frobenius copy
structure of the GHZ class, which the glueball subsection credits with
broadcasting a classical colour record and the Bell subsection says can be
built only of quarks and gluons. The flux tube is that colour-basis
FANOUT. The paper's two sentences and the lattice's Gauss law are one
tensor.

For the non-Abelian case the two-valent vertex is the intertwiner
j (x) j-bar -> 1, which again forces the representation to continue, and
the trivalent vertex for SU(3) fundamentals is epsilon_{ijk}, which is
also the paper's quartic baryon structure (`op:baryon-contact`). That
intertwiner is not the Abelian Z_3 spider, and section 6 says what the
difference costs.

## 4. Copy versus share: the tube and the Coulomb field (script C)

(i) Routes. A unit centre charge carried from source to sink over m
parallel routes of R links, each link costing 1 - cos(2 pi e/N): the
minimum over neutral assignments is R c(1) for every m from 1 to 6, for Z_2
(14.0000 at R = 7) and Z_3 (10.5000). The charge goes whole along one
route; adding routes buys nothing, because Z_N has no fractions. A
real-valued flux with the same constraint spreads to E_i = 1/m on every
route (the minimum-norm solution, checked by least squares) and costs R/m.
Copy: cost independent of the number of routes. Share: cost falling as
1/m. At the state level these are GHZ_n (1 ebit across every cut, pairwise
0, for every n) and W_n (pairwise concurrence 2/n, one-against-rest entropy
H(1/n)): script A, n = 3 to 8.

(ii) Dimension. Shared flux between +1 and -1 at separation R on a periodic
lattice, solved by FFT: in d = 1 the energy is exactly R(L - R)/2L (to
7e-14), linear with slope 1/2 as L -> infinity; in d = 2 it is logarithmic
with slope 0.1602 against 1/2pi = 0.1592; in d = 3 it is Coulomb with slope
-0.0834 in 1/R against -1/4pi = -0.0796 (lattice artefacts at R <= 10 on
L = 64). The shared law knows the dimension because the number of routes
at radius r grows as r^(d-1). The copied law does not: the cost is c(1)
times the graph distance, so (5,0,0) costs 5 and (3,4,0) costs 7 at the
same Euclidean length. The confining potential at strong coupling is a
Manhattan count, and rotational symmetry is restored only by the
roughening transition (Lüscher 1981), which is a dynamical fact about the
embedding, not about the count.

(iii) What this says for the framework. `sec:comp-distance` defines
distance as a count of loop completions. In such a space the energy of a
copy chain is sigma times the distance by definition: the linear form is
not derived, it is what "distance" and "copy" mean together, and the whole
content of `op:confinement-potential` is the coefficient, the cost of one
copy, which this morning's note already said. The Coulomb term, by
contrast, needs an embedding in which routes can be counted, which in this
framework is the emergent chart. The Cornell potential's two terms are
then the share term (one gluon exchanged, perturbative, W-like, pairwise)
and the copy term (the chain, GHZ-like, all-or-nothing), and the clause in
`op:confinement-potential` asking that "asymptotic freedom at short range"
appear "as the limit in which little tripartite budget is yet committed" is
the statement that at short range the share term dominates. CANDIDATE.

(iv) The fence. The copy/share dichotomy is a statement about Gauss's
law's kinematics: what the constraint allows. Which configuration the
ground state is, at a given coupling, is dynamics. Compact U(1) has
integer flux and the same copy chains at strong coupling, and still has a
Coulomb phase at weak coupling in four dimensions (Guth 1980), where the
flux of a charge is a coherent dressing of the vacuum by closed loops and
spreads; the deconfined phase of Z_2 gauge theory is the same story
(Fradkin and Susskind 1978; Wegner 1971). SU(3) has no such phase at zero
temperature, and the reason is dynamical: the centre symmetry is unbroken
and the monopole or vortex condensate expels flux ('t Hooft 1978, 1981).
The spider identity of section 3 says what the budget and the tube have in
common; it does not say why SU(3) sits in the copied phase at every
coupling, and the paper's "the budget alone does not confine" is exactly
right. What the framework can claim is weaker and still useful: the datum
that cannot be shared is the centre charge, because Z_3 has no fractions,
while U(1)'s charge can be dressed into a continuous field. Confinement is
the physics of an unshareable label.

## 5. What is confined is what the record cannot carry: the centre grades the split (script D)

With e_1 the preferred unit and J = L_{e_1} on the six-dimensional
complement of (e_0, e_1) (the pairing (e_2,e_3), (e_4,e_5), (e_6,-e_7) of
the 09-27 colour script), define phi_theta as the identity on the record
line and cos theta + sin theta J on the complement. Results:

- phi_theta is an automorphism of O exactly at theta in {0, 2pi/3, 4pi/3}:
  residual 0, 6.5e-16, 1.5e-15 there and at least 0.397 at every other
  angle tested (nine others, three random). The phase rotations of the
  colour C^3 that are octonion automorphisms are the centre Z_3 of SU(3),
  and nothing else: U(3) meets G_2 in SU(3).
- phi_{2pi/3} has eigenvalue 1 with multiplicity 2 (the record line),
  omega with multiplicity 3 and omega-bar with multiplicity 3; in the
  09-27 pairing it is the scalar omega on the colour C^3 (checked on the
  basis vectors and on a random colour vector). It is central in the
  su(3) stabiliser (commutator norm 2e-15 with all eight derivations) and
  not central in g_2 (norm 3.66 with a generic derivation).
- N-ality of the computability split: record line 0, colour C^3 1,
  anticolour 2.

So the quantity 't Hooft's criterion says is confined, non-zero N-ality,
is exactly the C^3 side of the split, and the quantity the framework says
no record can carry, "bare colour", is the centre-charged part of the
octonion. The two confinement criteria coincide on the split:

    no asymptotic state of non-zero N-ality   ('t Hooft 1978)
    no classical record of C^3-side data      (sec:bell-not-counterexample)

are the same sentence, because the record side is the centre-invariant
subspace. The lattice facts of section 2(d) now read directly: gluons
(N-ality 0) can screen any N-ality-0 datum, so adjoint strings break and
Casimir scaling is only intermediate; the asymptotic string tension
depends on N-ality alone, the one datum a record cannot absorb; the hadron
(N-ality 0) "is the unit that carries the worldline", as the Bell
subsection says.

Two Z_3's must be kept apart. The centre of colour acts as the scalar
omega on the colour C^3 and fixes the record line; it is in
`sec:quantum-numbers` as the Z_3 inside the Z_6 quotient. The generation
triality of `sec:masses` cyclically permutes the three off-diagonal
octonions of J_3(O) and is a component of pi_0(Aut O) = S_3; it does not
act on a single octonion by a phase. "Colour triality" in the quantum
numbers section means N-ality and should perhaps say so, since "triality"
is also the Koide word two sections later.

Script F tabulates the SU(3) irreps (p,q) with dimension, Casimir and
N-ality: the copy cost per link at strong coupling is the Casimir (4/3,
3, 10/3, 6 for 3, 8, 6, 10), the datum that survives screening is
(p - q) mod 3, and only the latter is visible to the split. The number
`op:confinement-potential` owes is sigma_1, the tension of N-ality 1; the
Casimir hierarchy at intermediate distance is a lattice fact the split
does not see.

## 6. The fence the alignment forces: the SU(3) singlet is not pairwise-unentangled (script E)

The colour singlet of three quarks is epsilon_{ijk}|ijk>/sqrt 6, three
qutrits. Its one-quark marginal is I/3 (purity 0.333333, entropy ln 3): the
slack r^2 = 0, exactly as for GHZ_3. Its two-quark marginal is the
antisymmetric projector over 3, the antisymmetric Werner state (Werner
1989), whose partial transpose has eigenvalues -1/3 (once) and 1/6 (eight
times): negativity 1/3 (Vidal and Werner 2002). The pairs are entangled.
The qubit GHZ_3 and the qutrit GHZ_3 have two-party negativity 0: their
pairs are classically correlated only. Tracing one quark out of the
singlet leaves an entangled pair; tracing one qubit out of GHZ leaves a
separable one.

Consequences, stated carefully.

- The clause "every bipartite tangle, internal or external, is forced to
  zero" (confinement section, line 138) is true of the register model's
  GHZ_3 and false of the SU(3) singlet. The dictionary maps GHZ-class
  three-qubit states to the colour sector through the octonionic Hopf map;
  it does not say the SU(3) singlet is a qutrit GHZ state. The
  asymptotic-freedom document says exactly that, and that "tracing out any
  colour subsystem destroys all colour entanglement"; both sentences are
  wrong for epsilon.
- The clause that does the work in the Bell subsection is the one-to-rest
  saturation: slack = r^2 = 0 for every party. That clause holds for
  epsilon (every quark maximally mixed) and for GHZ alike, and it is the
  state-level form of Gauss's law at the junction: a quark in a singlet
  has no colour of its own to record. The alignment of this note runs
  through r = 0 and the copy structure and does not need pairwise zero.
- Why the two differ is itself the alignment's content. The Abelian Z_3
  spider at a trivalent vertex is the uniform superposition over the nine
  neutral flux configurations, pairwise separable (script B); the
  non-Abelian junction epsilon is a single configuration in which the
  three strings carry three different colours, and "different" is a
  pairwise correlation. The pairwise negativity 1/3 of the singlet is the
  antisymmetry of the Y junction: it is what the flux-tube picture calls
  three strings of distinct colour meeting, and what the budget picture
  called zero. The budget picture's number is the Abelian shadow of the
  non-Abelian junction.
- Monogamy for qutrits is not the CKW inequality (which is a qubit
  theorem; Osborne and Verstraete 2006 extends it to n qubits), so the
  "budget" vocabulary has no literal qutrit form. The one-tangle
  1 - r^2 does, and that is the quantity to keep.

## 7. The all-or-nothing resource, state and flux (script A)

For the record, the numbers behind "copy versus share" at the state level.
GHZ_3: one-tangle 1, both pairwise tangles 0, three-tangle 1 (CKW residual
and 4|Det| agree to 1e-9; W_3: 8/9, 4/9, 4/9, 0; slack 1/9). For n = 3 to
8: GHZ_n has pairwise concurrence 0, 1 bit across the 1|(n-1) cut and 1
bit across the balanced cut, for every n; W_n has pairwise concurrence
exactly 2/n and 1|(n-1) entropy H(1/n), falling as n grows. The GHZ
correlation is held whole or not at all, whatever the number of parties;
the W correlation is one excitation shared, thinning as it is shared more
widely. These are the two Frobenius structures as states: the copy
structure holds its datum whole, the share structure distributes one
quantum. A flux line in a fixed irrep is the copy structure as a map, and
its energy does not thin with routes; a Coulomb field is one unit of flux
shared over r^(d-1) routes, and its energy density thins as r^(-2(d-1)).

The three-tangle's property that forces the paper's external-zero
conclusion is that tau_3 = 1 forces purity, so the triple is in a product
with everything else; the W register's 1/9 comes from the n-qubit
inequality with the internal pairwise tangles retained. Both arguments are
in the paper; this note only observes that "tau_3 = 1 forces purity" is
the state-level form of "a copied label is whole or absent".

## 8. What I think

The alignment JS asks for exists and is cheap, and it is not an analogy.
Both pictures are built from one tensor, the copy map, which the paper
already calls the GHZ structure and the lattice already calls Gauss's law.
The paper reads it as a state (the junction, the saturated budget) and
the lattice reads it as a map (the chain, the tube). The paper's "no
distance in it" and the lattice's "cost per link" are the same fact seen
from the two ends: a copy chain's state is independent of its length, and
its energy is proportional to it. In a relational space the second is a
tautology, which is why the framework finds confinement "direct and
elegant": it has the linear law for nothing and owes only the coefficient.

What the alignment does not do is supply dynamics. The paper is right that
the budget alone does not confine; the spider is the same in the Coulomb
phase of compact electrodynamics. The honest statement is: the framework
has the kinematics of confinement (what Gauss's law allows, what a record
can carry) in a form the lattice recognises, and it has not got the
dynamics (why SU(3) is in the copied phase at every coupling), which the
lattice has numerically and nobody has analytically. The place where the
framework could add something is the one the centre grading points at:
the reason the colour label cannot be shared is that Z_3 has no fractions,
and the reason the record line can be shared is that it is
centre-invariant. If the framework ever derives why the vacuum pays to
keep the centre symmetry unbroken, that would be the missing dynamics, and
it would be stated in the vocabulary this note sets up. I do not see how
to do it today.

Three smaller things I believe after this session. First, the
asymptotic-freedom document's identification of the SU(3) singlet with a
qutrit GHZ state should be withdrawn; the pairwise negativity is 1/3, not
0, and the correct clause is r = 0. Second, "colour triality" in the
quantum numbers section is N-ality and should be named so, since the Koide
triality is a different Z_3. Third, the Cornell potential is the
framework's share-plus-copy in one formula, and `op:confinement-potential`
is better posed as "derive sigma_1 and the crossover scale" than as
"derive V(r)".

## 9. Second-order findings for JS's ruling

(a) `paper1/confinement_section_2026-06-13.tex`, line 138: "every
bipartite tangle, internal or external, is forced to zero" is a register
statement. For the SU(3) singlet the two-quark negativity is 1/3 (script
E). The Bell subsection's argument uses r^2 = 0, which holds for both.
Suggested CANDIDATE clause after the sentence: "in the register model; the
SU(3) singlet epsilon_{ijk} shares the saturated one-tangle and not the
vanishing pair tangles, its two-quark marginal being the antisymmetric
Werner state, and the access argument below uses only the former."

(b) `knowledge/project-docs/open_problem_asymptotic_freedom.md`, the
"Confinement as recursive GHZ structure" paragraph: "the colour singlet
condition epsilon_{ijk}|i>|j>|k> is a GHZ state across three qutrits" and
"tracing out any colour subsystem destroys all colour entanglement" are
false for epsilon. A dated correction note, not an edit of the April
document.

(c) `paper1/quantum_numbers_section_2026-06-08.tex`, line 243, "colour
triality": N-ality, and a different Z_3 from the Koide triality of
`sec:masses`. One parenthesis would prevent the conflation. CANDIDATE.

(d) The mass-gap subsection's "tensor-network interface" sentence (line
~640) now has a concrete first step: Gauss's law in the electric basis is
the GHZ spider, so the budget-saturation constraint and the gauge-invariant
tensor network of Haegeman et al. are the same object, and the question
"does budget saturation reproduce the area law" is the question "does a
PEPS of Gauss-law spiders with this coupling have an area-law Wilson
loop", which is what those methods compute. A sentence citing
haegeman2015gauging and tagliacozzocelilewenstein2014tensor there.
CANDIDATE.

(e) `op:confinement-potential`: the linear form is structural in a
relational space (section 4(iii)); the coefficient sigma_1 and the
crossover to the share term are the content. Sharpening of this morning's
9(a). CANDIDATE wording: "PASS: sigma_1, the tension of N-ality 1, from the
cost of one copy; and the scale below which the share term (one-gluon
exchange) dominates. The linear dependence on relational distance is not
at stake."

(f) The centre grading of the split (section 5) is new to the corpus and
is derived, not matched. A proposition for the Hopf or quantum-numbers
section: "the centre Z_3 of SU(3) is the set of phase rotations of the
colour C^3 that are automorphisms of O; it fixes the record line; N-ality
grades the computability split as 0, 1, 2 on C, C^3, C^3-bar." STRUCTURAL
for the mathematics, CANDIDATE for the identification of "record-side"
with "centre-invariant".

## 10. Prior work and ownership

- Gauss's law as a copy tensor: standard in tensor-network gauge theory
  (Haegeman et al. 2015; Tagliacozzo, Celi and Lewenstein 2014; Zohar and
  Burrello 2015) and in the toric-code PEPS (Verstraete et al. 2006;
  Kitaev 2003). Spiders and strong complementarity: Coecke and Duncan 2011;
  classical structures: Coecke, Pavlovic and Vicary 2013 (in the library).
  Not the framework's.
- Centre symmetry, N-ality and the asymptotic tension: 't Hooft 1978;
  Lucini and Teper 2001; Del Debbio et al. 2001; de Forcrand and Philipsen
  2000. Not the framework's.
- The action of the centre of SU(3) on O with the fixed unit: implicit in
  Günaydin and Gürsey 1973 (the SU(3) subgroup of G_2 and the 1 + 3 + 3-bar
  + 1 decomposition); the automorphism check at the cube roots is this
  session's, trivial once stated.
- The antisymmetric Werner state as the two-quark marginal of the singlet:
  elementary; Werner 1989 for the state.
- The framework's own: the identification of the flux tube with the
  colour-basis FANOUT of `sec:bell-not-counterexample`; the reading of the
  computability split as the centre grading; "copy versus share" as the
  tube versus the Coulomb field with the embedding entering only through
  the route count; and the correction of the pairwise-zero clause.
- Entanglement entropy of gauge fields is not a tensor-product quantity
  (Casini, Huerta and Rosabal 2014); any attempt to turn the budget into a
  cut-entropy statement on the lattice will meet the centre/edge-mode
  ambiguity there. Noted, not used.

## 11. Fences

- The spider identity is for Z_N in the electric basis. For SU(N) the
  vertex tensor is the intertwiner, GHZ-class in the sense of being a
  copy of the representation label through two-valent vertices, but not
  the uniform Abelian spider at three-valent ones (section 6).
- Nothing here is dynamical. The copied phase for SU(3) at all couplings
  is the lattice's result, not derived.
- Script C's "shared law" uses real-valued flux; compact U(1) has integer
  flux and reaches the Coulomb law only through the vacuum's loop
  dressing. The dichotomy is exact for the centre charge (no fractions)
  and only effective for U(1).
- The lattice Coulomb slopes (d = 2, 3) carry finite-size and lattice
  artefacts at the few-per-cent level; the d = 1 result is exact on the
  ring.
- The GHZ/W numbers of script A are the qubit theory; the qutrit singlet
  has no CKW inequality (section 6).
- The "share term equals one-gluon exchange" reading in section 4(iii) is
  CANDIDATE, not computed: no beta function or running is derived here,
  and the asymptotic-freedom document's numerology is untouched.
- No claim about the Yang--Mills mass gap; the paper's own fence stands.

## 12. Proposed ledger entries

- **STRUCTURAL** Gauss's law at an uncharged k-valent vertex of a Z_N
  lattice gauge theory, in the electric basis, is the group-algebra
  Frobenius spider: the neutral subspace has dimension N^(k-1), its
  uniform superposition is the leg-wise Fourier transform of the N-level
  GHZ_k state, the two-valent vertex is the copy map, and a chain copies
  the source charge along every link. Verified for N = 2, 3 and k = 2, 3, 4
  (fidelity 1 to 1e-12); script B.
- **STRUCTURAL** The phase rotations of the colour C^3 (complex structure
  L_{e_1}) that are automorphisms of O are exactly the centre Z_3 of
  SU(3); the generator fixes the record line (e_0, e_1), is the scalar
  omega on C^3, is central in su(3) and not in g_2. N-ality grades the
  computability split 0, 1, 2. Script D.
- **STRUCTURAL** The asymptotic string tension depends only on the
  N-ality of the source; adjoint strings break ('t Hooft 1978; Lucini and
  Teper 2001; de Forcrand and Philipsen 2000). Imported.
- **ESTABLISHED** A unit centre charge over m parallel routes costs R c(1)
  for every m; real-valued flux costs R/m; the shared law on a lattice is
  linear, logarithmic and Coulomb in d = 1, 2, 3 (slopes 0.4873 exact on
  the ring, 0.1602, -0.0834) and the copied law is c(1) times the graph
  distance in every d. Script C.
- **ESTABLISHED** The SU(3) singlet epsilon_{ijk} has one-quark marginals
  I/3 and two-quark marginal the antisymmetric Werner state, negativity
  1/3; the qubit and qutrit GHZ_3 have two-party negativity 0. Script E.
  *Corrects in part* the confinement section's "every bipartite tangle
  ... forced to zero" as a statement about the SU(3) singlet (it holds for
  the register model), and the asymptotic-freedom document's "GHZ state
  across three qutrits".
- **CANDIDATE** The flux tube is the colour-basis FANOUT of
  `sec:bell-not-counterexample`: a chain of colour copy maps that no record
  can read. Confinement as exhausted budget (the junction as a state) and
  confinement as a string (the chain as a map) are the one copy structure.
- **CANDIDATE** The record side of the computability split is the
  centre-invariant subspace, so "no record carries bare colour" and "no
  asymptotic state has non-zero N-ality" are one criterion.
- **CANDIDATE** The Cornell potential's two terms are the share term (one
  quantum over r^(d-1) routes, needing the embedding) and the copy term
  (sigma times the count, needing none); in a relational space the linear
  law is definitional and `op:confinement-potential` owes sigma_1 and the
  crossover scale.
- **RHYME** String breaking (Bali et al. 2005) as the copy chain ending on
  a charge the vacuum pays for: the budget opening a new register. Fenced.
- **OPEN** (restated, not new) Why SU(3) sits in the copied phase at every
  coupling: the dynamics of centre symmetry, which the spider identity
  does not touch. "The budget alone does not confine" stands.

## 13. Files

- `scripts/confinement_budget_flux_tube_2026-11-07T1130.py` (new; PASS,
  0 FAIL; seed 20261107; pure numpy; Convention A; one fix during the
  session: the d = 1 Coulomb check was tightened from a 2% asymptote to
  the exact ring formula R(L-R)/2L after the finite ring gave slope
  0.4873).
- `knowledge/sessions/confinement_budget_flux_tube_2026-11-07T1130.md`
  (this note).
- `bib/confinement_flux_tube_refs_2026-11-07T1140.bib` (25 keys, all
  Crossref-verified; no VERIFY-CITE; VERIFY-SUPPORT on every body).
- `notes/todo.md`: section "2026-11-07: aligning the budget and the flux
  tube (Fable session, late morning)" appended.
- Nothing in the paper patched; nothing built; nothing committed.

## 14. Exact stdout of `scripts/confinement_budget_flux_tube_2026-11-07T1130.py`

```
=== Part A: the budget in numbers (copy versus share) ===
  state      tau_A  C^2_AB  C^2_AC  tau3(CKW)   4|Det|
  GHZ_3     1.0000  0.0000  0.0000     1.0000   1.0000
  [ok  ] GHZ_3: CKW residual equals the hyperdeterminant three-tangle
  W_3       0.8889  0.4444  0.4444    -0.0000   0.0000
  [ok  ] W_3: CKW residual equals the hyperdeterminant three-tangle
  product   0.0000  0.0000  0.0000     0.0000   0.0000
  [ok  ] product: CKW residual equals the hyperdeterminant three-tangle
  [ok  ] GHZ_3 saturates: tau3 = 1 and both pairwise tangles 0
  [ok  ] W_3: tau3 = 0, pairwise tangles 4/9, slack 1/9

  GHZ_n versus W_n: pairwise concurrence, entropy across 1|(n-1) and across the balanced cut (bits)
    n  C(GHZ)    C(W)     2/n  S1(GHZ)    S1(W)   H(1/n)  Sbal(GHZ)  Sbal(W)
    3  0.0000  0.6667  0.6667   1.0000   0.9183   0.9183     1.0000   0.9183
    4  0.0000  0.5000  0.5000   1.0000   0.8113   0.8113     1.0000   1.0000
    5  0.0000  0.4000  0.4000   1.0000   0.7219   0.7219     1.0000   0.9710
    6  0.0000  0.3333  0.3333   1.0000   0.6500   0.6500     1.0000   1.0000
    7  0.0000  0.2857  0.2857   1.0000   0.5917   0.5917     1.0000   0.9852
    8  0.0000  0.2500  0.2500   1.0000   0.5436   0.5436     1.0000   1.0000
  [ok  ] GHZ_n: 1 ebit across every cut, pairwise 0; W_n: pairwise 2/n, 1|rest entropy H(1/n)

=== Part B: Gauss's law in the electric basis is a GHZ-class spider ===
  Z_2, valence 2 (in,out): neutral configurations   2 = N^(k-1) =   2;  |<GHZ_k^(N)| F^-1 spider>|^2 = 1.000000000000
  [ok  ] Z_2 k=2: neutral count N^(k-1) and spider = Fourier transform of GHZ
  Z_2, valence 3 (all inward): neutral configurations   4 = N^(k-1) =   4;  |<GHZ_k^(N)| F^-1 spider>|^2 = 1.000000000000
  [ok  ] Z_2 k=3: neutral count N^(k-1) and spider = Fourier transform of GHZ
  Z_2, valence 4 (all inward): neutral configurations   8 = N^(k-1) =   8;  |<GHZ_k^(N)| F^-1 spider>|^2 = 1.000000000000
  [ok  ] Z_2 k=4: neutral count N^(k-1) and spider = Fourier transform of GHZ
  Z_3, valence 2 (in,out): neutral configurations   3 = N^(k-1) =   3;  |<GHZ_k^(N)| F^-1 spider>|^2 = 1.000000000000
  [ok  ] Z_3 k=2: neutral count N^(k-1) and spider = Fourier transform of GHZ
  Z_3, valence 3 (all inward): neutral configurations   9 = N^(k-1) =   9;  |<GHZ_k^(N)| F^-1 spider>|^2 = 1.000000000000
  [ok  ] Z_3 k=3: neutral count N^(k-1) and spider = Fourier transform of GHZ
  Z_3, valence 4 (all inward): neutral configurations  27 = N^(k-1) =  27;  |<GHZ_k^(N)| F^-1 spider>|^2 = 1.000000000000
  [ok  ] Z_3 k=4: neutral count N^(k-1) and spider = Fourier transform of GHZ
  Z_2 trivalent spider state: tau3 = 1.000000, pairwise concurrence = 0.000000, one-tangle = 1.000000
  [ok  ] Z_2 trivalent Gauss spider saturates the budget (tau3 = 1, pairwise 0)
  Z_3 trivalent spider state: two-party negativity = 0.000000, one-party purity = 0.333333 (1/3 = maximally mixed)
  [ok  ] Z_3 trivalent Gauss spider: pairwise separable, marginals maximally mixed
  Z_2: W_3 (one unit of flux on one of three inward legs): ||P_neutral W||^2 = 0.000000; charge eigenstate: True (charge 1)
  [ok  ] Z_2: the W_3 vertex is charged (orthogonal to the neutral subspace, charge 1)
  Z_3: W_3 (one unit of flux on one of three inward legs): ||P_neutral W||^2 = 0.000000; charge eigenstate: True (charge 1)
  [ok  ] Z_3: the W_3 vertex is charged (orthogonal to the neutral subspace, charge 1)
  Z_2 two-valent (in,out) neutral configurations: [(0, 0), (1, 1)]  -> e_out = e_in: the copy map
  [ok  ] Z_2 two-valent neutral subspace is the image of the copy map
  Z_2 chain of 5 links from a source of charge 1: neutral configurations 1 (all links carry 1: [(1, 1, 1, 1, 1)])
  [ok  ] Z_2 chain: one neutral configuration, the charge copied along every link
  Z_3 two-valent (in,out) neutral configurations: [(0, 0), (1, 1), (2, 2)]  -> e_out = e_in: the copy map
  [ok  ] Z_3 two-valent neutral subspace is the image of the copy map
  Z_3 chain of 5 links from a source of charge 1: neutral configurations 1 (all links carry 1: [(1, 1, 1, 1, 1)])
  [ok  ] Z_3 chain: one neutral configuration, the charge copied along every link
  Z_3 trivalent all-inward vertex, charge of each configuration (0 = neutral):
    (0, 0, 0):0  (0, 0, 1):1  (0, 0, 2):2  (0, 1, 0):1  (0, 1, 1):2  (0, 1, 2):0  (0, 2, 0):2  (0, 2, 1):0  (0, 2, 2):1
    (1, 0, 0):1  (1, 0, 1):2  (1, 0, 2):0  (1, 1, 0):2  (1, 1, 1):0  (1, 1, 2):1  (1, 2, 0):0  (1, 2, 1):1  (1, 2, 2):2
    (2, 0, 0):2  (2, 0, 1):0  (2, 0, 2):1  (2, 1, 0):0  (2, 1, 1):1  (2, 1, 2):2  (2, 2, 0):1  (2, 2, 1):2  (2, 2, 2):0
  [ok  ] Z_3 junction: (1,1,1) three fundamentals in is neutral (the baryon vertex), (2,2,2) likewise
  [ok  ] Z_3 junction: (1,2,0) fundamental in, antifundamental in, nothing is neutral (the meson passes through)
  [ok  ] Z_3 junction: (1,0,0) and (1,1,0) are charged (N-ality 1 and 2): open flux must end on a charge

=== Part C: copy versus share as energy; the Coulomb law needs the embedding, the confining law does not ===
  (i) a unit centre charge over m parallel routes of R links; cost per link 1 - cos(2 pi e/N); minimum over neutral assignments
    m   Z_2 min   Z_3 min  R c(1), Z_2  R c(1), Z_3  real E: R/m
    1   14.0000   10.5000      14.0000      10.5000       7.0000
    2   14.0000   10.5000      14.0000      10.5000       3.5000
    3   14.0000   10.5000      14.0000      10.5000       2.3333
    4   14.0000   10.5000      14.0000      10.5000       1.7500
    5   14.0000   10.5000      14.0000      10.5000       1.4000
    6   14.0000   10.5000      14.0000      10.5000       1.1667
  [ok  ] centre charge: minimal cost R c(1) for every m (copied whole along one route); real flux: R/m (shared)
  real flux over m = 5 routes: minimum-norm solution E_i = 0.2000 each, energy R sum E^2 = 1.4000 = R/m = 1.4000
  [ok  ] real flux spreads evenly: minimum-norm solution has E_i = 1/m

  (ii) shared (real) flux between +1 at the origin and -1 at distance R on a periodic lattice: V = G(0) - G(R) by FFT
    R       d=1       d=2       d=3
    3    1.4912    0.4302    0.2252
    4    1.9844    0.4769    0.2324
    5    2.4756    0.5128    0.2366
    6    2.9648    0.5420    0.2393
    7    3.4521    0.5666    0.2413
    8    3.9375    0.5878    0.2427
    9    4.4209    0.6066    0.2438
   10    4.9023    0.6233    0.2447
  d=1: slope dV/dR = 0.4873 (one route: linear; the ring of L = 512 gives exactly R(L-R)/2L, slope 1/2 as L -> infinity; max |V - R(L-R)/2L| = 6.66e-14)
  d=2: slope dV/dlnR = 0.1602 (expected 1/(2 pi) = 0.1592)
  d=3: slope dV/d(1/R) = -0.0834 (expected -1/(4 pi) = -0.0796: Coulomb)
  [ok  ] shared flux in d=1 equals the exact ring formula R(L-R)/2L (linear, slope 1/2 as L -> infinity)
  [ok  ] shared flux: logarithmic in d=2 (slope 1/2pi within 5%)
  [ok  ] shared flux: Coulomb in d=3 (slope -1/4pi within 8%)

  (iii) copied (centre) flux on the same lattices: cost = c(1) x graph distance, whatever d and whatever the embedding
    separation   Euclid  graph dist  cost/c(1)
     (5, 0, 0)    5.000           5          5
     (3, 4, 0)    5.000           7          7
     (0, 0, 5)    5.000           5          5
     (5, 5, 0)    7.071          10         10
     (3, 3, 3)    5.196           9          9
  [ok  ] copied flux: V/c(1) equals the Manhattan graph distance; (5,0,0) and (3,4,0) share a Euclidean length but not a cost

=== Part D: the centre Z_3 of SU(3) grades the computability split (Convention A octonions) ===
  [ok  ] Convention A: e_1 e_2 = e_3, e_1 e_4 = e_5, e_1 e_6 = -e_7 (the colour planes of the 09-27 script)
  dim Der(O) = 14 (g_2 = 14)
  [ok  ] dim Der(O) = 14
  dim {D in Der(O): D e_1 = 0} = 8 (su(3) = 8)
  [ok  ] stabiliser of e_1 has dimension 8
  [ok  ] L_{e_1} squares to -1 on the complement of (e_0, e_1)
   theta/(2pi/3)  automorphism residual
        0.000000              0.000e+00
        0.500000              2.000e+00
        1.000000              6.474e-16
        1.500000              2.000e+00
        2.000000              1.542e-15
        2.500000              2.000e+00
        0.750000              1.414e+00
        0.600000              1.902e+00
        2.356624              1.801e+00
        2.063552              3.967e-01
        0.440015              1.965e+00
  [ok  ] phi_theta is an automorphism of O exactly at theta in {0, 2pi/3, 4pi/3}: the centre Z_3 of SU(3)
  [ok  ] phi_{2pi/3}^3 = identity and phi_{2pi/3} is not the identity
  eigenvalues of phi_{2pi/3}: [-0.5-0.866025j -0.5-0.866025j -0.5-0.866025j -0.5+0.866025j -0.5+0.866025j -0.5+0.866025j  1. +0.j
  1. +0.j      ]
  multiplicities: eigenvalue 1 -> 2 (the record line e_0, e_1), omega -> 3, omega-bar -> 3 (the colour C^3 and its conjugate)
  [ok  ] eigenvalue multiplicities 2, 3, 3
  on a random colour vector: to_c3(phi x) = omega * to_c3(x): True;  phi fixes e_0 and e_1: True
  [ok  ] phi_{2pi/3} is the scalar omega on the colour C^3 (in the 09-27 pairing) and the identity on the record line
  commutator with the 8 su(3) derivations: max norm 2.47e-15; with a generic g_2 derivation: 3.663
  [ok  ] phi_{2pi/3} is central in SU(3) and not central in G_2
  N-ality of the split (eigenvalue of the centre, as a power of omega): record line C -> 0; colour C^3 -> 1; anticolour -> 2

=== Part E: the SU(3) singlet epsilon_{ijk}|ijk> against the GHZ model ===
  singlet: one-quark marginal purity 0.333333 (1/3: maximally mixed, slack r^2 = 0); one|rest entropy 1.098612 = ln 3 = 1.098612
  singlet: two-quark partial-transpose eigenvalues [-0.333333  0.166667  0.166667  0.166667  0.166667  0.166667  0.166667  0.166667  0.166667]; negativity 0.333333 (1/3)
  [ok  ] singlet two-quark marginal is the antisymmetric projector over 3 (the antisymmetric Werner state)
  [ok  ] singlet: one-quark marginal maximally mixed (zero slack, as for GHZ)
  [ok  ] singlet: two-quark marginal entangled, negativity 1/3 (unlike GHZ)
  qubit GHZ_3: one-party purity 0.500000, two-party negativity -0.000000
  [ok  ] qubit GHZ_3: pairs separable (negativity 0)
  qutrit GHZ_3: one-party purity 0.333333, two-party negativity -0.000000
  [ok  ] qutrit GHZ_3: pairs separable (negativity 0)
  after tracing one quark: singlet pair negativity 0.3333 (still entangled); GHZ pair negativity 0 (classically correlated only)

=== Part F: SU(3) irreps -- the copy cost per link (Casimir) and the datum that survives screening (N-ality) ===
   (p,q)  dim     C_2  C_2/C_2(fund)  N-ality  asymptotic string
  (1,0)    3  1.3333         1.0000        1 sigma_1 (fundamental's)
  (0,1)    3  1.3333         1.0000        2 sigma_1 (fundamental's)
  (1,1)    8  3.0000         2.2500        0 breaks (screened to 0)
  (2,0)    6  3.3333         2.5000        2 sigma_1 (fundamental's)
  (0,2)    6  3.3333         2.5000        1 sigma_1 (fundamental's)
  (3,0)   10  6.0000         4.5000        0 breaks (screened to 0)
  (2,1)   15  5.3333         4.0000        1 sigma_1 (fundamental's)
  (0,3)   10  6.0000         4.5000        0 breaks (screened to 0)
  [ok  ] Casimir of the fundamental is 4/3 and of the adjoint 3; N-ality of (1,0),(0,1),(1,1),(2,0) is 1,2,0,2

CONFINEMENT BUDGET FLUX TUBE: PASS
```
