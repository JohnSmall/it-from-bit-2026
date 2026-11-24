# Would a relational space still need lattice QCD? The lattice as the exchange graph

Fable session, 2026-11-07T0700. Script
`scripts/relational_distance_lattice_2026-11-07T0700.py` (PASS, stdout in
section 14). Bibliography batch `bib/lattice_causal_set_refs_2026-11-07T0710.bib`.

JS's question: "When doing simulations in QCD people currently divide space
into a lattice to avoid the infinities that occur when treating space as
continuous. But if space is relational instead of substantive and distance
is inferred from information exchange would we need to use lattice QCD?"

## 0. The answer in five lines

1. Yes to the computation, no to the ontology. The lattice is not a remedy
   for continuity; it is the only known gauge-invariant, non-perturbative
   regulator that a computer can run (Wilson 1974), and it already works
   the way JS describes space: it is a dimensionless graph of link
   variables, the parallel transporters between neighbouring sites, with
   an action that is a sum over faces, and the spacing in metres is
   inferred afterwards by matching a computed correlation to a measured
   one (Sommer 1994; Lüscher 2010). Script A: a Wilson loop's expectation
   is r^n with n the count of enclosed faces, even for a disconnected set
   of faces, and the spacing a = sqrt(sigma_lat/sigma_phys) runs from 0.40
   to 0.08 fm as the coupling is tuned. The lattice is relational already;
   what is substantival is only the belief that a -> 0 is a limit of
   something.
2. Under a relational ontology the graph changes status, not existence:
   there is no continuum to discretise and no limit to take, because the
   graph is the exchange structure itself. Every relational-discrete
   programme in the literature (causal sets, Lloyd's computational
   universe, quantum graphity, spin networks, causal dynamical
   triangulations) is lattice gauge theory on a graph in all but the
   graph's regularity, and regularity is what has to go: a regular lattice
   has a frame. Script B: cut to one causal diamond, a square lattice's
   longest chain grows by half under a boost of rapidity one, while a
   Poisson sprinkling has no frame (Bombelli, Henson and Sorkin 2009) and
   its order and number alone return proper time to 1.6% and dimension to
   0.3%. The relational lattice is random, Lorentz-invariant and
   non-local; that is the price list.
3. The infinities are not where the question puts them. Ultraviolet
   divergences come from unboundedly many degrees of freedom in a region,
   not from continuity as such, and the renormalisation group (Wilson and
   Kogut 1974) says the hadron scale is insensitive to what regulates at
   the Planck scale except through a finite number of parameters. A
   relational cutoff at 10^-35 m therefore changes nothing in a lattice
   computation at 10^-16 m, whose "continuum limit" is an extrapolation
   from 0.05--0.15 fm and never literally a = 0. The finiteness JS wants is
   real (Bekenstein's bound; the framework's finite records; the Planck
   cell of the 09-20 Landauer table) and it regulates gravity, not QCD.
4. Two places where the relational reading does bite on QCD proper.
   Chirality: no local, chirally symmetric, doubler-free regular lattice
   exists (Nielsen and Ninomiya 1981; script C: two species per dimension,
   sixteen in four; the Wilson term lifts the doublers to mass 2r/a by
   breaking chiral symmetry), and the known escapes are non-locality
   (Ginsparg--Wilson) or a boundary (Kaplan's domain wall). The sign
   problem: lattice QCD computes in Euclidean time so that the weights are
   real probabilities; real time and finite density have complex weights
   (Troyer and Wiese 2005), which in this framework's vocabulary is the
   pre-record regime of the October thread, and the way round it is to
   run the Kogut--Susskind Hamiltonian on qubits (Martinez et al. 2016;
   Bañuls et al. 2020), which is lattice QCD on a graph of exchanges, the
   relational lattice built.
5. For the framework: `sec:comp-distance` already defines distance as a
   count, and `op:confinement-potential` asks for the string tension from
   emergent distance. Script A is the toy form that answer must take, an
   area law that is a count of faces, and the lattice computes the same
   inference in the opposite direction. The framework's own crossover
   temperature of 160 GeV (09-20 note) is a lattice result (D'Onofrio and
   Rummukainen 2016). The framework needs the lattice; what it changes is
   what the lattice is.

## 1. Where the question meets the corpus

`paper1/spacetime_from_non-computability.tex`, `sec:comp-distance`:

> A physical clock counts completed irreversible loops, so proper time
> literally counts loop completions and the metric ... is a loop-density
> tensor, the conversion from coordinate intervals to loop counts

> The spacelike distance between two events is then the number of such
> curves that would have to be closed to make them causally connected.

> the loops such telephones would close, and carry nothing round, are
> what spacelike separation is, their number is the distance, and the
> metric is read off from them.

`paper1/confinement_section_2026-06-13.tex`, "The confinement potential is
distance-free in origin":

> Distance, in this framework, is not fundamental: it is emergent and
> relational, built from the network of interactions. So the task is not
> to compute the energy of a flux tube stretched across a pre-existing
> space; it is to show how a potential that depends on separation arises
> at all from a constraint that contains no separation.

and `op:confinement-potential`: "Derive the static quark--antiquark
potential --- equivalently the quantity lattice QCD and Regge trajectories
call the string tension --- as the associator-geodesic length ... resolved
by the emergent distance". The mass-gap passage of the same section:
"there is no Hamiltonian here whose spectrum could be bounded, no Hilbert
space of the field theory, and no continuum R^4 to put one on".

Paper 2 (`paper2/paper2_main_2026-07-07.tex`) names its neighbours: Lloyd's
computational universe (geometry from a computation's causal structure)
and the causal-set programme's sequential growth (Rideout and Sorkin 2000),
and reads Isaacson's averaging scale as "the chart re-emergence scale, the
minimum region over which enough locking pattern accumulates for an
effective step-direction, hence a count-rate, to exist again".

The 09-20 records note: above the electroweak crossover "causal order
still exists, carried by conserved charges and by light cones, but there
is no metric scale"; its crossover temperature is taken from D'Onofrio and
Rummukainen's lattice computation (`donofriorummukainen2016crossover`, in
the library).

So the question is already answered in part by the framework's own
definitions: distance is a count. What this note adds is that the lattice
is a count too, and in what sense the two counts are the same object.

## 2. What the lattice is for (STRUCTURAL, imported)

Wilson's construction (1974) puts the gauge field on the links of a graph
as group elements U_l, the parallel transporters that compare the internal
frames at neighbouring sites; the action is a sum over faces of
Re Tr of the product round the face; gauge invariance is exact at every
spacing; and the only dimensionful quantity is the lattice spacing a,
which does not appear in the dimensionless computation at all. Three
consequences the question needs:

- The action knows only the graph. Sites, links, faces and the group:
  no coordinates, no metric. The regular hypercubic graph is a choice
  made for the Brillouin zone and the Monte Carlo, not for the physics.
- The spacing is an output. A lattice computation produces dimensionless
  ratios; a is assigned afterwards by matching one computed correlation
  (the string tension, the Sommer scale r_0 from the static force, the
  Wilson-flow time t_0) to one measured number. This is "distance inferred
  from information exchange" done daily in every lattice collaboration.
- The continuum limit is a tuning of the coupling, controlled by
  asymptotic freedom: a(g) -> 0 as g -> 0, with the renormalisation group
  guaranteeing that the long-distance physics depends on the regulator
  through finitely many parameters (Wilson and Kogut 1974). Practitioners
  extrapolate from a = 0.05--0.15 fm; nobody takes a to zero, and the
  question whether space is continuous at the Planck scale does not enter.

Creutz's 1980 Monte Carlo is where the method became a computation; the
Kogut--Susskind Hamiltonian form (1975) is the version a quantum computer
runs.

## 3. Script A: a loop sees the count of faces; the spacing is inferred

Two-dimensional U(1) with the Wilson action exp(b cos theta_f) per face
and free boundaries. Axial gauge makes the face angles independent, so a
Wilson loop enclosing a set F of faces has expectation (I_1(b)/I_0(b))^|F|:
the count of faces, nothing else. Checked at b = 2 on 20000 samples of a
6 x 6 face array:

| region          | faces | <W>    | r^n    |
|-----------------|-------|--------|--------|
| 1 x 1           | 1     | 0.6982 | 0.6978 |
| 2 x 1           | 2     | 0.4898 | 0.4869 |
| 2 x 2           | 4     | 0.2413 | 0.2371 |
| L-shaped        | 3     | 0.3485 | 0.3397 |
| four on a diagonal, not connected | 4 | 0.2328 | 0.2371 |

all within three standard errors (0.021). The last row is the point: the
"area" the loop measures is a count of exchanges, and the embedding of
those exchanges in a plane is invisible to it. This is the two-dimensional
case of Witten's 1991 result that two-dimensional Yang--Mills depends on
the surface only through its area and topology (Migdal 1975 for the
lattice form): the theory is relational already.

Scale setting: sigma_lat(b) = -ln(I_1/I_0) per face; with the physical
string tension (440 MeV)^2 the inferred spacing is

| b   | sigma_lat per face | a inferred (fm) |
|-----|--------------------|-----------------|
| 1   | 0.8066             | 0.4028          |
| 2   | 0.3599             | 0.2690          |
| 4   | 0.1467             | 0.1718          |
| 8   | 0.0670             | 0.1160          |
| 16  | 0.0323             | 0.0806          |

The spacing is never an input; it is what the measured correlation
assigns to one face. (A toy: two-dimensional U(1) confines trivially and
has no asymptotic freedom; the inference is the point, not the numbers.)

## 4. Script B: the relational lattice is a causal set, and it is random

Bombelli, Lee, Meyer and Sorkin (1987): a discrete relational spacetime is
a partial order with a counting measure, "order plus number equals
geometry". Distance is not put in; it is read off. Two readings checked:

*Proper time from a count.* N points sprinkled uniformly into a
two-dimensional causal diamond of proper height tau. The longest chain is
the longest increasing subsequence of a random permutation (rotate the
diamond to a square), with mean 2 sqrt N (Vershik and Kerov 1977; Logan
and Shepp 1977) and correction -1.7711 N^{1/6} (Baik, Deift and Johansson
1999). The proper time is tau = L/sqrt(2 rho):

| N     | longest chain | 2 sqrt N | BDJ-corrected | tau inferred |
|-------|---------------|----------|---------------|--------------|
| 1000  | 58.2          | 63.2     | 57.6          | 0.9202       |
| 4000  | 120.6         | 126.5    | 119.4         | 0.9534       |
| 16000 | 249.0         | 253.0    | 244.1         | 0.9843       |

*Dimension from a count.* The fraction of related pairs in a causal
interval is Gamma(d+1) Gamma(d/2) / (2 Gamma(3d/2)) (Myrheim 1978; Meyer
1988): 1/2 in two dimensions, 1/10 in four. Measured 0.5024 (dimension
estimate 1.994) and 0.1018 (3.979). Dimension is an output here too, as
`sec:three-dimensions` wants it to be, though by a different argument.

*The regular lattice has a frame.* A square lattice of spacing 0.025 cut
to the same diamond, boosted by rapidity eta with the diamond held fixed:

| eta | points | longest chain | chain/(2 sqrt N) | ordering fraction |
|-----|--------|---------------|------------------|-------------------|
| 0.0 | 821    | 41            | 0.715            | 0.4812            |
| 0.3 | 769    | 41            | 0.739            | 0.4840            |
| 0.6 | 767    | 47            | 0.849            | 0.4830            |
| 1.0 | 817    | 61            | 1.067            | 0.4887            |

At rest the lattice's longest chain is sqrt(2N), not 2 sqrt N: a regular
lattice undercounts proper time by 1/sqrt2 relative to a sprinkling of
the same density, and the count changes with the observer. A Poisson
sprinkling boosted is a Poisson sprinkling of the same density; Bombelli,
Henson and Sorkin (2009) prove that it has no preferred frame. That
theorem is the answer to "would we need a lattice": a relational discrete
structure that respects Lorentz invariance must be random, and its price
is non-locality, since each element has infinitely many near-null
neighbours (Sorkin 2009; the causal-set d'Alembertian of Benincasa and
Dowker 2010 is non-local for exactly this reason). Christ, Friedberg and
Lee (1982) used random lattices for the Euclidean analogue, rotational
invariance, decades ago.

The other relational-discrete programmes sit here too: spin networks are
lattice gauge theory on a graph with the metric emergent (Rovelli and
Smolin 1995); quantum graphity makes locality itself emergent from a
graph (Konopka, Markopoulou and Severini 2008); causal dynamical
triangulations recover four dimensions from a random triangulation
(Ambjørn, Jurkiewicz and Loll 2004); Lloyd's computational universe reads
the geometry off a quantum circuit's causal structure (Paper 2's named
neighbour). None removes the lattice. Each removes its regularity and its
continuum limit.

## 5. The infinities and the renormalisation group

The question's premise "to avoid the infinities that occur when treating
space as continuous" needs one correction. The divergences of continuum
QCD arise because a region of any size is allowed unboundedly many
degrees of freedom, so that products of fields at a point are
ill-defined. Any regulator that bounds the degrees of freedom removes
them: dimensional regularisation, Pauli--Villars, the lattice. The lattice
is chosen not because it removes infinities better but because it does so
while keeping gauge invariance exact and the integral finite-dimensional,
which is what a Monte Carlo needs. The renormalisation group then says
that the hadron-scale theory is a fixed-point neighbourhood whose
dependence on the regulator is through a finite set of couplings. A
relational ontology supplies a physical regulator, a finite number of
exchanges per region (Bekenstein 1981; the framework's finite records;
the Planck cell of the 09-20 Landauer table). That is a statement about
gravity and about the Planck scale; by universality it changes nothing at
the scales where QCD is computed. So "would we need lattice QCD" splits:
as a regulator, the relational structure already is one; as a method, the
lattice stays.

## 6. Script C and the two places the relational reading bites

*Chirality.* Nielsen and Ninomiya (1981): a lattice fermion action that is
local, translation-invariant on a regular lattice, Hermitian and chirally
symmetric has as many left-handed as right-handed species. Script C: the
naive dispersion sin(ka) has zeros at ka = 0 and pi with slopes +1 and -1,
two species of opposite chirality per dimension, sixteen in four; the
Wilson term r(1 - cos ka) leaves the zero at k = 0 and gives the doubler
mass 2r/a (checked at r = 0.5 and 1), and it is a mass term, so chiral
symmetry is what pays. The escapes are the Ginsparg--Wilson relation
(1982; overlap fermions, non-ultralocal) and Kaplan's domain wall (1992),
where the chiral fermion lives on a boundary of one more dimension. On an
irregular graph there is no Brillouin zone and the theorem's hypotheses
fail; that is not a theorem that doublers are absent, and Christ,
Friedberg and Lee's random-lattice fermions are the place to look
(VERIFY-SUPPORT). For this framework, whose leptons are chiral (the
October twistor thread), the constraint is sharp: if its exchange
structure were a regular graph its chiral species would come paired, so
the graph must be irregular or the chirality boundary-borne. Kaplan's
"chiral fermion on a boundary" beside Paper 2's "spacetime from the
FANOUT boundary" is a RHYME and is fenced as one.

*The sign problem.* Lattice QCD is Euclidean so that exp(-S_E) is a real,
positive weight a Monte Carlo can sample. Real-time evolution and finite
baryon density have complex weights, and sampling them is NP-hard in
general (Troyer and Wiese 2005). In the vocabulary of the October notes
the Euclidean lattice computes the post-record regime, where weights are
probabilities, and the sign problem is the pre-record regime, where they
are the complex quasi-probabilities of the 10-16T2200 note. The way round
it is to let a quantum register carry the amplitudes: the Kogut--Susskind
Hamiltonian on trapped ions (Martinez et al. 2016) and the programme
reviewed by Bañuls et al. (2020). That is lattice gauge theory on a graph
of qubit exchanges with the distance read off the couplings, which is the
relational lattice JS describes, already under construction. CANDIDATE
reading; the identification of Euclidean with post-record is the
framework's, not the literature's.

## 7. Script D: distance from exchange in a toy

A single excitation hopping on a chain of 61 sites with amplitude J. The
first time its probability at site j exceeds 0.02 grows linearly in the
graph distance j with slope 0.5123 per site against the light-cone value
1/(2J) = 0.5. The Hamiltonian is the coupling graph; embedding the sites
regularly or at random positions (mean spacing 1.008, spread 0.787)
changes no arrival time. Distance inferred from exchange is the graph
distance, and the physical length of a hop is whatever the front speed
assigns to one exchange, as the string tension assigns a length to one
face in script A. This is JS's premise in its smallest form, and it shows
why the premise does not remove the lattice: the exchange graph is the
lattice.

## 8. What I think

The question has a clean answer once "lattice" is split into three things
the word carries. The graph of exchanges with group elements on its links
stays; it is what a relational gauge theory is. The regular hypercubic
graph goes, because it has a frame, and the relational replacement is a
random order with non-local kinematics. The continuum limit goes as an
ontology and stays as an extrapolation, because the renormalisation group
makes the hadron scale indifferent to the regulator. So a relational
space does not remove lattice QCD; it removes the apology for it.

What the framework has not got, and would need before it could say more
than this: a specified exchange graph (which graph, at what density, with
what statistics; Paper 2's chart re-emergence scale is where the count
becomes a metric but the count itself is unspecified); a Hamiltonian on
it (the confinement section says so itself); a reason the graph is
irregular, or a boundary that carries the chirality; and a derivation of
the area law as a count of exchanges with a coefficient, which is
`op:confinement-potential` restated in the lattice's own terms. The
lattice literature has done the inference in one direction for fifty
years: compute the count, infer the distance. The framework proposes to
run it the other way: define the distance as the count. Script A says
these are the same arithmetic; the open problem is the coefficient.

## 9. Second-order findings for JS's ruling

(a) `op:confinement-potential` calls the target "the quantity lattice QCD
and Regge trajectories call the string tension" as if the lattice supplied
the number and the framework the explanation. The lattice's string tension
is itself a count per face, and the physical a is inferred from it. A
clause recording that the relational derivation and the lattice
computation are one inference run in opposite directions would make the
open problem's PASS criterion sharper: PASS is a coefficient, not a
mechanism. CANDIDATE wording.

(b) Paper 2's neighbours paragraph names the causal-set dynamics (Rideout
and Sorkin) and not the kinematics. The kinematic results are the ones the
chart re-emergence scale needs: order plus number gives the metric
(Bombelli, Lee, Meyer and Sorkin 1987), the dimension estimator needs a
minimum count to work (Myrheim; Meyer), and Lorentz invariance requires
the count to be random (Bombelli, Henson and Sorkin 2009). A sentence
citing these, with Surya's 2019 review, would locate the chart
re-emergence scale in an existing literature. CANDIDATE.

(c) The 09-20 records note's crossover temperature is a lattice number;
the note cites it but does not say that the framework's "birth of proper
time" is dated by a lattice computation. One line recording the
dependence would be honest.

(d) The chirality constraint of section 6 is new to the corpus: the
October twistor thread's chiral leptons and any regular exchange graph are
incompatible by Nielsen--Ninomiya. Worth a line in the twistor thread's
open questions; no wording proposed.

## 10. Prior work and ownership

The lattice is Wilson's; the Hamiltonian form Kogut and Susskind's; the
Monte Carlo Creutz's; scale setting Sommer's and Lüscher's; the
renormalisation-group argument Wilson and Kogut's; the doubling theorem
Nielsen and Ninomiya's with the Ginsparg--Wilson and Kaplan escapes; the
sign-problem hardness Troyer and Wiese's; quantum simulation Martinez et
al. and Bañuls et al. Causal sets are Bombelli, Lee, Meyer and Sorkin's,
the chain law Brightwell and Gregory's (with Vershik--Kerov, Logan--Shepp
and Baik--Deift--Johansson behind it), the dimension estimator Myrheim's
and Meyer's, the symmetry theorem Bombelli, Henson and Sorkin's, the
non-locality Sorkin's and Benincasa--Dowker's, the review Surya's; random
lattices Christ, Friedberg and Lee's; two-dimensional Yang--Mills Migdal's
and Witten's. The framework's contributions in this note are readings:
the lattice as the exchange graph in its own vocabulary; Euclidean as
post-record and the sign problem as pre-record; the doubling theorem as a
constraint on its chirality; and the observation that `op:confinement-potential`
and lattice scale setting are one inference in two directions.

## 11. Fences

- Two-dimensional U(1) is a toy: it confines trivially, is quasi-topological,
  and has no asymptotic freedom. The inferred spacings in script A
  illustrate the inference and are not QCD numbers.
- The causal-set checks are kinematic. Nothing here is a dynamics, and the
  framework has none to offer on a graph.
- "The Nielsen--Ninomiya hypotheses fail on an irregular graph" is not a
  claim that doublers are absent there.
- The free chain of script D has no gauge field; it shows only that the
  embedding is invisible to exchange.
- The identification of Euclidean weights with the post-record regime is
  the framework's reading and is labelled CANDIDATE.
- No claim about the Born rule, the FANOUT boundary, or the value of any
  QCD observable is made or changed.

## 12. Proposed ledger entries (for JS to write or refuse)

- **STRUCTURAL** Wilson's lattice gauge theory is a theory on a graph:
  link variables, a face action, exact gauge invariance, no coordinates;
  the spacing is assigned afterwards by matching one computed correlation
  to one measurement (Sommer scale, Wilson flow). In two dimensions a
  Wilson loop's expectation is (I_1(b)/I_0(b))^n with n the number of
  enclosed faces, whatever their embedding (Migdal; Witten). Imported;
  verified numerically (script A).
- **STRUCTURAL** In a causal set, proper time is the longest chain divided
  by sqrt(2 rho) in two dimensions (mean 2 sqrt N with the
  Baik--Deift--Johansson correction) and dimension is read off the fraction
  of related pairs (Myrheim--Meyer: 1/2 in two dimensions, 1/10 in four);
  a Poisson sprinkling has no preferred frame (Bombelli--Henson--Sorkin)
  while a regular lattice has one. Imported; verified numerically (script B:
  tau to 1.6%, dimension to 0.3%, a boost of rapidity one lengthening the
  lattice's chain by half).
- **STRUCTURAL** Nielsen--Ninomiya: a local, translation-invariant,
  Hermitian, chirally symmetric fermion action on a regular lattice has
  2^d species; the Wilson term lifts the doublers to mass 2r/a by breaking
  chiral symmetry. Imported; verified numerically (script C).
- **ESTABLISHED** (finite check, script PASS) The four checks above and
  script D: on a hopping chain the first-arrival time grows linearly in the
  graph distance at the light-cone speed 2J, independent of the embedding.
- **CANDIDATE** A relational space does not remove lattice QCD; it removes
  the regular graph and the continuum limit as ontology. The exchange graph
  with group elements on its links is what a relational gauge theory is;
  the physical spacing is what a correlator assigns to one exchange, which
  is the inference lattice QCD already performs, and `op:confinement-potential`
  is the same inference run in reverse.
- **CANDIDATE** Euclidean lattice QCD computes the post-record regime
  (real weights); the sign problem of real time and finite density is the
  pre-record regime (complex quasi-probabilities); quantum simulation of
  the Kogut--Susskind Hamiltonian is lattice gauge theory on a graph of
  qubit exchanges.
- **CANDIDATE** If the framework's exchange structure were a regular
  graph, its chiral leptons would come paired (Nielsen--Ninomiya); the graph
  must be irregular or the chirality boundary-borne.
- **RHYME** Kaplan's chiral fermion on a domain wall beside "spacetime from
  the FANOUT boundary".

## 13. Files

- `scripts/relational_distance_lattice_2026-11-07T0700.py` -- new, PASS,
  0 FAIL (one fix during the session: the Brillouin-zone zero count is
  taken on a half-step periodic grid so that no sample sits on a zero).
- `knowledge/sessions/relational_distance_lattice_2026-11-07T0700.md`
  -- this note.
- `bib/lattice_causal_set_refs_2026-11-07T0710.bib` -- 29 keys, 25
  Crossref-verified; VERIFY-CITE on Migdal 1975 (Crossref holds only the
  1996 reprint), Myrheim 1978 and Meyer 1988 (preprint and thesis, no
  DOI), Vershik--Kerov 1977 (no Crossref record), and the author list of
  Wilson--Kogut 1974 (Crossref lists Wilson alone); VERIFY-SUPPORT on every
  body.
- `notes/todo.md` -- pointer appended.
- Nothing patched, built or committed. The sentences of section 9 are
  proposals.

## 14. Exact stdout of the script (2026-11-07)

```
A. two-dimensional U(1) gauge theory: a loop sees the count of faces, the spacing is inferred
   ok   b = 1.0 : one-face expectation 0.446390 = I_1/I_0 = 0.446390
   ok   b = 2.0 : one-face expectation 0.697775 = I_1/I_0 = 0.697775
   ok   b = 4.0 : one-face expectation 0.863523 = I_1/I_0 = 0.863523
   region 1x1             faces n = 1 : <W> = 0.6982  r^n = 0.6978
   ok   loop expectation is r^n with n the number of enclosed faces (3 sigma = 0.021)
   region 2x1             faces n = 2 : <W> = 0.4898  r^n = 0.4869
   ok   loop expectation is r^n with n the number of enclosed faces (3 sigma = 0.021)
   region 2x2             faces n = 4 : <W> = 0.2413  r^n = 0.2371
   ok   loop expectation is r^n with n the number of enclosed faces (3 sigma = 0.021)
   region L-shaped 3      faces n = 3 : <W> = 0.3485  r^n = 0.3397
   ok   loop expectation is r^n with n the number of enclosed faces (3 sigma = 0.021)
   region diagonal-ish 4  faces n = 4 : <W> = 0.2328  r^n = 0.2371
   ok   loop expectation is r^n with n the number of enclosed faces (3 sigma = 0.021)
   the 'diagonal-ish' region is not even connected: the loop expectation depends on the face count alone
   scale setting: sigma_lat(b) = -ln(I_1/I_0) per face; a = sqrt(sigma_lat / sigma_phys) with sigma_phys = (440 MeV)^2
      b =   1.0 : sigma_lat = 0.8066 per face ; inferred a = 0.4028 fm ; large-b form 1/(2b) = 0.5000
      b =   2.0 : sigma_lat = 0.3599 per face ; inferred a = 0.2690 fm ; large-b form 1/(2b) = 0.2500
      b =   4.0 : sigma_lat = 0.1467 per face ; inferred a = 0.1718 fm ; large-b form 1/(2b) = 0.1250
      b =   8.0 : sigma_lat = 0.0670 per face ; inferred a = 0.1160 fm ; large-b form 1/(2b) = 0.0625
      b =  16.0 : sigma_lat = 0.0323 per face ; inferred a = 0.0806 fm ; large-b form 1/(2b) = 0.0312
   ok   the inferred spacing falls as the coupling b grows: the continuum limit is a tuning of b, the spacing is never an input
B. a causal set: proper time and dimension from order and number
   two-dimensional diamond of proper height tau = 1; light-cone coordinates (u, v) in [0, tau/sqrt2]^2
      N =  1000 : longest chain 58.2 ; 2 sqrt N = 63.2 ; BDJ-corrected 57.6 ; tau inferred = 0.9202
   ok   longest chain within 6% of the Vershik--Kerov/Logan--Shepp law with the Baik--Deift--Johansson correction (N = 1000)
      N =  4000 : longest chain 120.6 ; 2 sqrt N = 126.5 ; BDJ-corrected 119.4 ; tau inferred = 0.9534
   ok   longest chain within 6% of the Vershik--Kerov/Logan--Shepp law with the Baik--Deift--Johansson correction (N = 4000)
      N = 16000 : longest chain 249.0 ; 2 sqrt N = 253.0 ; BDJ-corrected 244.1 ; tau inferred = 0.9843
   ok   longest chain within 6% of the Vershik--Kerov/Logan--Shepp law with the Baik--Deift--Johansson correction (N = 16000)
   ok   proper time inferred from the chain count alone is within 5% of the truth at N = 16000 (0.9843)
   ordering fraction, 2D sprinkling N = 2000 : 0.5024 ; Myrheim--Meyer f(2) = 0.5000 ; dimension estimate 1.994
   ok   two-dimensional ordering fraction is 1/2
   ok   dimension read off the order alone is 2
   ordering fraction, 4D sprinkling N = 1500 : 0.1018 ; Myrheim--Meyer f(4) = 0.1000 ; dimension estimate 3.979
   ok   four-dimensional ordering fraction is 1/10
   ok   dimension read off the order alone is 4
   a regular lattice cut to the same diamond, boosted by rapidity eta (the diamond is held fixed):
      eta = 0.0 : points in diamond  821 ; longest chain  41 ; chain/(2 sqrt N) = 0.715 ; ordering fraction 0.4812
      eta = 0.3 : points in diamond  769 ; longest chain  41 ; chain/(2 sqrt N) = 0.739 ; ordering fraction 0.4840
      eta = 0.6 : points in diamond  767 ; longest chain  47 ; chain/(2 sqrt N) = 0.849 ; ordering fraction 0.4830
      eta = 1.0 : points in diamond  817 ; longest chain  61 ; chain/(2 sqrt N) = 1.067 ; ordering fraction 0.4887
   ok   the regular lattice's chain length or ordering fraction changes with the boost: it has a frame
   ok   at rest the regular lattice's longest chain is sqrt(2N), not 2 sqrt N: it undercounts proper time by 1/sqrt2 relative to a sprinkling of the same density
   a Poisson sprinkling boosted is a Poisson sprinkling of the same density; its statistics above are frame-free by construction
C. fermion doubling on a regular lattice
   naive dispersion sin(k a)/a in one dimension: zeros at k a = [0.    3.142] ; slopes cos(k a) = [ 1. -1.]
   ok   two species of opposite chirality per dimension
   ok   sixteen species in four dimensions (2^4 Brillouin-zone corners)
   ok   Wilson term r = 0.5: the zero at k = 0 survives, the doubler acquires mass 2r/a = 1.00
   ok   Wilson term r = 1.0: the zero at k = 0 survives, the doubler acquires mass 2r/a = 2.00
   the Wilson term is a mass term, chirally asymmetric: no local, chirally symmetric, doubler-free regular lattice (Nielsen--Ninomiya)
D. distance from exchange: a single excitation on a chain of 61 sites
   first-arrival time t_j (probability > 0.02) for graph distance j = 1..20: slope 0.5123 per site, intercept -0.488 ; 1/(2J) = 0.500
   ok   arrival time grows linearly with graph distance at the hopping light-cone speed 2J
   the same chain embedded regularly (spacing 1.0) and at random positions (mean spacing 1.008, spread 0.787):
      the Hamiltonian is the coupling graph; the arrival times above are identical for both embeddings
   ok   distance inferred from exchange is the graph distance j, whatever the embedding; the metric spacing is what a correlator assigns to one hop
   the chain's hop length in physical units is c x (t_{j+1} - t_j) if the front moves at c: a is inferred from the exchange, as in A
RELATIONAL DISTANCE LATTICE: PASS
```
