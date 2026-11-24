# Session note: the mass gap as the cost of a new relationship

Date: 2026-11-21T0800. Session: Claude Code (Fable 5.2), thinking session,
working for JS on `main`. Script:
`scripts/mass_gap_relationship_cost_2026-11-21T0800.py` (seed 20261121, pure
numpy, 27/27, final line `MASS GAP RELATIONSHIP COST: PASS`). Batch:
`bib/mass_gap_relationship_cost_refs_2026-11-21T0830.bib` (14 keys, not
imported). Nothing patched, built or committed. `knowledge/invalid_routes.md`
was read first; nothing below retries a logged route.

## What was asked

JS, 2026-11-21: the paper deliberately avoids the Yang--Mills mass gap, but
the framework has something to say that could point people in a productive
direction. Confinement falls out of GHZ being maximally entangled: quarks have
no spare budget for relationships on the colour basis, and since spacetime is
a network of relationships there is no space apart to be pulled to. This is
very different from the standard view, where colour flux is squeezed into
tubes by the colour analogue of superconductivity. To make the connection,
think in terms of how much energy is required to create new spacetime and
therefore new relationships.

## 0. The answer

1. The direction is right, and it can be made exact. In the electric basis of
   a gauge theory the confining vacuum is literally empty: no link carries
   flux, no link is related to any other. A string between charges and a
   glueball are both made by creating links, and both cost a multiple of one
   number, the cost of a link. The string tension is that cost per unit
   length. The gap is that cost times the size of the smallest closed
   network. Script A: the two stay locked, gap/sigma = 4.0 falling only to
   3.9, across the confined regime.
2. "Very different from the standard view" is too strong. The empty electric
   vacuum and the perfect magnetic condensate are one state written in two
   bases (script B, exact). The framework's picture and the dual
   superconductor do not disagree about the vacuum. They disagree about which
   basis is real, and the framework has a reason for its choice: records.
3. "Energy to create new space" already has three standard names, and the
   framework should claim the reading and not the bookkeeping: the link cost
   at strong coupling, the bag constant B, and the trace anomaly. The last is
   the deep one. The trace of the stress tensor is the response to dilating
   space, and the mass of every colour-only state is its trace-anomaly
   charge. Mass is the cost of the space the state makes.
4. The gap is not the budget's consequence alone, and one sentence of
   `sec:mass-gap` is wrong as it stands. A gap can exist with no confinement
   (script A, weak coupling). And closed networks are not bounded below in
   size in a continuum. What bounds the gap is a competition: making extent
   costs sigma L, resolving a small extent costs c/L, and the minimum is
   2 sqrt(c sigma), which is positive when both costs are.
5. The productive direction for mathematicians, in one line: prove the gap
   as a lower bound on the cost of a non-empty closed colour network, in the
   network basis where the vacuum is empty, by showing colour networks never
   proliferate into a space. Chatterjee (2021) has proved the opposite
   implication rigorously on the lattice. The framework's contribution is a
   reason to expect the converse and a vocabulary for it.
6. What is still owed is the scale. Nothing here fixes the number.
   `op:qcd-scale` is one number, the strong coupling at the matching scale.

## 1. What the paper says now

`sec:mass-gap` names the Clay problem, declines it, and gives a conditional
heuristic: colour has no debt-free direction, "closed networks are
topologically discrete", "there is no continuum of ever-smaller closed
networks by which geodesic lengths could accumulate towards zero", so the
spectrum is bounded below by the minimal closed network. It then gives two
directions: Cubitt, Perez-Garcia and Wolf's undecidability, and a
tensor-network test of the area law. "Confinement and pre-spatial
co-location" says a quark "has no place apart to be pulled to".
`op:confinement-potential` asks for the potential as geodesic length resolved
by emergent distance. My note of 2026-11-07 found that Gauss's law in the
electric basis is the GHZ spider, that a copied flux costs c(1) times the
graph distance in every dimension, and that the framework "has the linear law
for nothing and owes only the coefficient". It ended: the missing dynamics is
why SU(3) stays in the copied phase at every coupling, and "I do not see how
to do it today." JS's direction is aimed exactly at that coefficient.

## 2. The cost of a link (script A)

Take the lattice Hamiltonian in Kogut and Susskind's form. Its states, in the
electric basis, are closed networks of flux: the paper's "closed colour
networks". Its vacuum at strong coupling is the empty network. The electric
term charges c(1) for each link that carries a unit of flux. The magnetic
term creates and reshapes networks.

I computed the centre theory, Z_3, and Z_2 beside it, in two space
dimensions on 9 and 16 plaquettes, exactly, by Lanczos, across the whole
range of the plaquette coupling x. Three results.

(i) One cost, two observables. At strong coupling the static potential is
V(R) = R c(1) and the gap is 4 c(1), each to better than half a per cent at
x = 0.02. A string of length R creates R links. The lightest neutral
excitation is the smallest closed network, one plaquette, four links. So

    gap = n_min x (cost of a link),   sigma = (cost of a link) / (length of a link),

and gap / (sigma a) = n_min = 4 on a square lattice. The ratio stays between
3.87 and 4.00 for Z_3 up to x = 0.6, where the link cost itself has fallen by
14 per cent. The gap and the tension are renormalised together. That is the
precise sense of JS's connection: confinement and the gap are the same cost
counted along an open chain and around a closed one. STRUCTURAL at strong
coupling (Osterwalder and Seiler proved the area law and the gap there in
1978, VERIFY-SUPPORT); the persistence of the ratio is numerical, on a toy.

(ii) The vacuum fills. As x grows the vacuum acquires flux: the density of
flux-carrying links rises from 0 to about a half, the tension falls to zero,
and the vortex order parameter M falls from 1 to near 0. The cost of a link,
measured by sigma, goes to zero when the vacuum is already full of links.
Relationships are free where space made of them already exists.

(iii) A gap without confinement. At large x the gap is large (6.9 for Z_3 at
x = 3, 20.8 for Z_2 at x = 6) while sigma/gap is below 0.05. This is the
deconfined, topologically ordered phase. So a gap does not imply
confinement, and any sentence of the form "the gap exists because of
confinement" must be about a theory that has no such phase. For Z_N in 2+1
dimensions the phase exists. For SU(3) in 3+1 it is believed not to, and that
belief is the open problem.

On the framework's own graph the smallest closed colour network is the
triangle, the three-gluon K_3 that the confinement section already singles
out, and the count would be n_min = 3. CANDIDATE, and small: it is a count
on a graph the framework has not specified.

## 3. Empty and condensed are one state (script B)

On two plaquettes with seven Z_3 links, the zero-flux state is, exactly: the
uniform superposition of all 2187 gauge fields; a state in which each
plaquette's holonomy is uniformly distributed; a state in which every Wilson
loop vanishes; a state in which the vortex-creation operator has expectation
1; and, Fourier transformed link by link, the single product state e = 0 with
zero entanglement between any link and the rest.

The last two lines are the two pictures. "No relationships" is the electric
reading. "A perfect condensate of magnetic vortices" is the magnetic reading,
and it is 't Hooft's and Mandelstam's dual superconductor at its strong-
coupling end. M in script A is that order parameter, and it is also one
minus the vacuum's flux content, to leading order. The condensate is how
emptiness looks from the conjugate side.

So I would not write that the framework's view is very different from the
standard one. I would write that the standard view describes the vacuum in
the basis in which it is full, and the framework describes it in the basis
in which it is empty, and that the framework has a reason to prefer the
second: flux, N-ality, is what a record can or cannot carry (note of
2026-11-07, section 5), and holonomy is not. The framework's "no medium"
commitment survives in this form: there is no medium in the basis records
read. It does not survive as a denial that a condensate exists. The gluon
condensate is a measured number (section 5). CANDIDATE.

## 4. Why the gap is positive: two costs, not discreteness

The paper's heuristic leans on "no arbitrarily small closed structure". On a
lattice that is true by construction. In a continuum it is false: a closed
loop of flux can be as small as one likes, and if its energy were sigma L
alone the spectrum would run down to zero. The lattice hides this because
its spacing is put in by hand, and the framework has said (2026-11-07,
lattice note) that it keeps no such spacing as ontology.

What holds the gap open is that a small network is expensive for a different
reason. To be a network of size L at all, a state must resolve the distance
L, and resolving L costs of order hbar c / L. In QCD this is asymptotic
freedom's regime: a small loop is a pair of nearly free gluons with energy
about 1/L. In the framework's vocabulary it is the cost of a record
(Margolus and Levitin: a system with energy E above its ground state needs a
time at least pi hbar / 2E to reach a distinguishable state, VERIFY-SUPPORT).
So a closed network of size L costs at least

    E(L) = sigma L + c / L,   minimum  2 sqrt(c sigma)  at  L = sqrt(c / sigma).

Extent is expensive in the infrared because space has to be made. Resolution
is expensive in the ultraviolet because a relationship has to be
distinguishable. The gap is the cheapest compromise, and its size is the
size of a hadron. The photon sector has the second cost and not the first,
so its minimum is zero, reached at infinite L: space made of electromagnetic
relationships is free at long range, which is the Coulomb phase.

This gives the connection a sharp form that a mathematician can attack:

    in pure SU(N) Yang--Mills,  m_gap >= C sqrt(sigma)  with C universal.

It says confinement, with the uncertainty principle, implies the gap. I do
not know of a rigorous inequality of this kind. The other direction exists:
Chatterjee proved on the lattice that "if the center of the gauge group is
nontrivial, and correlations decay exponentially under arbitrary boundary
conditions, then center symmetry does not break", and that "a theory is
confining when center symmetry is unbroken". A strong form of the gap
implies the area law. The framework's direction is the converse. CONJECTURE.

Numbers, and a warning against fitting them. The lattice ratio for SU(3) is
m/sqrt(sigma) = 3.405(21) (Athenodorou and Teper 2021, read) or 3.55(7)
(Lucini, Teper and Wenger 2004, read). The compromise formula gives 2.51,
3.54 or 5.01 for c = pi/2, pi, 2 pi, and a closed Nambu--Goto string gives
4.80. All are within a factor 1.5 of the lattice and they differ from each
other by a factor 2. c = pi sits at -0.1 sigma from the 2004 value and
+6.7 sigma from the 2021 value. That is what a coincidence looks like when
the data improve. The formula has the right order and no claim on the number.
Do not chase c.

## 5. "Energy to create space" has standard names

(i) The bag constant. The MIT bag charges an energy B for each unit of volume
in which colour fields exist. Minimising x/R + (4 pi/3) B R^3 gives a
glueball of mass (4/3)(4 pi B)^(1/4) x^(3/4), which is 9.0 B^(1/4) for the
lowest two-gluon mode and is zero if and only if B is zero. Minimising a
tube's energy g^2/(2A) + B A over its cross-section A gives
sigma = sqrt(2 g^2 B). Both the gap and the tension are functions of the one
price B, with exponents 1/4 and 1/2, so again m ~ sqrt(sigma). With
B^(1/4) = 0.145 GeV the bag gives a 1.3 GeV glueball and sqrt(sigma) = 0.30
GeV against 1.7 and 0.44. The bag is JS's sentence as a 1974 model: it costs
energy to make a place where colour relationships can exist. What the
framework changes is the reading of the outside. In the bag the outside is a
vacuum that pushes back. In the framework the outside is where no colour
relationship has been made. Section 3 says these are the same statement.

(ii) The trace anomaly. Classical Yang--Mills has no scale, and in a
scale-free theory dilating space costs nothing. Quantisation breaks this:
T^mu_mu = (beta/2g) G^2 (Collins, Duncan and Joglekar 1977). Two
consequences are standard. The vacuum energy density is
-(b0/32) <(alpha_s/pi) G^2>, which with the sum-rule condensate 0.012 GeV^4
(from memory) is -(0.25 GeV)^4 for pure glue: the bag constant with its
sign, derived. And the mass of any state in the chiral limit is the
expectation of the integrated trace: all of a glueball's mass, and nearly all
of the proton's, is its trace-anomaly charge (VERIFY-SUPPORT; I am quoting a
textbook result from memory, usually attributed to Shifman, Vainshtein and
Zakharov and to Ji).

Since T^mu_mu is by definition the response of the action to a local change
of scale, this is the exact form of JS's sentence. The mass of a colour-only
object is the energy it costs to dilate the space it occupies, and that cost
is non-zero because the quantum theory, unlike the classical one, has a unit.
It also fits the Paper 2 thread, where mass is a clock and "above the
electroweak crossover there are no clocks": a gapped colour sector is one
that has made its own clock, and the gap is that clock's rate. STRUCTURAL as
physics; CANDIDATE as the framework's reading.

(iii) The fence this raises for Paper 2. An energy per unit volume for
making space is a cosmological constant. B is some 10^44 times the observed
dark-energy density. The framework inherits the standard problem here in its
own words: if making colour-space costs B, what does gravity read? This is
the boundary already recorded in the Paper 2 hub (which column gravity
reads). It is not answered here.

## 6. When do colour relationships form a space?

The gap closes, in a network description, in one way: networks proliferate.
Loops of every size appear in the vacuum at no cost and the flux lines of a
charge can spread through them. Levin and Wen call this string-net
condensation and show that it is how a deconfined gauge field, a photon,
emerges. Script A shows it for Z_N: rho rises, sigma dies.

Read in the framework's terms, a condensed network of colour flux is a space
made of colour relationships. Then "confinement and a gap" is the statement
that colour relationships never form a space, at any scale, and "there is no
space apart to be pulled to" is not a consequence of confinement but its
definition in the network basis. The modern standard statement is the same
with other words: confinement is an unbroken one-form centre symmetry, and a
massless gauge boson is the Goldstone boson of a broken continuous one-form
symmetry (Gaiotto, Kapustin, Seiberg and Willett 2015, VERIFY-SUPPORT). The
centre of SU(3) is discrete, so it has no Goldstone boson to offer. That is
the 2026-11-07 "unshareable label" again, and it is the paper's "no
debt-free direction" in the language mathematicians now use. It explains why
nothing protects a massless colour-neutral state. It does not prove none
exists.

What would prove it, in the framework's own terms, is a theorem that the
record structure forbids a condensed colour network: that a state in which
colour flux has long-range order would let a record carry N-ality. I think
this is the right target and I cannot derive it. It needs the dynamics the
paper has not built. CONJECTURE, and the same missing step as on 2026-11-07,
now with a form.

## 7. Where the scale comes from

Nothing above produces a number in GeV. In pure Yang--Mills every dimensional
quantity is a multiple of one scale, so sigma ~ gap^2 is true of any account.
The scale itself is dimensional transmutation:

    ln(M / Lambda) = 2 pi / (b0 alpha_s(M)) = (8 pi^2 / g^2) / b0.

8 pi^2/g^2 is the action of one instanton, the cost in nats of one unit of
winding, and the instanton is the quaternionic Hopf fibration the paper
already uses for two-qubit entanglement. Script C3: at the paper's matching
scale of 3.6 TeV, alpha_s = 0.0791 at one loop and 0.0784 at two, the
instanton action is 79 to 80 nats, and one-loop running with thresholds gives
Lambda_3 = 0.14 GeV, ln(3.6 TeV/Lambda) = 10.1 and Lambda/v = 5.8e-4. So
`op:qcd-scale` is equivalent to one dimensionless input: the strong coupling
at the matching scale. The framework derives sin^2 theta_W there and has no
rule for g_s; the fibre-dimension rule was tried and failed (note of
2026-10-30). This is the honest position: the framework can say what the gap
is and why it should be positive, and cannot yet say how big.

Not a route: g_s^2 at 3.6 TeV comes out at 0.994 (one loop) and 0.985 (two
loops), near 1. With the top Yukawa at 1 in the paper this will be tempting.
It is one number, it moves by one per cent between loop orders, and the
matching scale was fixed by a different condition. Do not chase it without a
mechanism.

## 8. What I think

JS's instinct is sound and the paper currently undersells it and misstates
one step. The framework does have something to say about the mass gap, and it
is not a route to the Clay prize. It is a change of the question.

The Clay problem asks for a spectral gap of a Hamiltonian on a given R^4.
The framework has no given R^4. In a relational setting the natural question
is different: what does it cost to make a relationship, and can relationships
of this kind be made cheaply enough, at long enough range, to constitute a
space? For electromagnetism the answer is yes, and the result is the Coulomb
phase and a massless photon. For colour the answer is no, and the two faces
of "no" are confinement (open chains cost per link) and the gap (closed
networks cost at least the compromise of section 4). Both are standard
physics in the electric basis. What is the framework's is the claim that this
basis is the fundamental one because it is the one records read, and the
identification of "mass" with "cost of made space" through the trace anomaly.

Three things I would not let the paper say. First, that confinement is
understood without dynamics: script A's weak-coupling rows show the same
kinematics deconfined. Second, that the gap follows from discreteness: it
follows from two costs. Third, that the standard picture is wrong: it is the
same vacuum in the conjugate basis.

The most useful single thing to hand to mathematicians is the inequality of
section 4 together with Chatterjee's theorem. Between them they would make
"gap" and "confinement" equivalent for a group with a non-trivial centre,
and the half that is missing is exactly the half the framework's picture
makes natural.

## 9. Findings for JS's ruling

(a) `sec:mass-gap`, third paragraph: replace "closed networks are
topologically discrete ... no continuum of ever-smaller closed networks" by
the two-cost argument of section 4. Draft below.

(b) Add the cost-of-a-link identity (section 2) as the bridge between
`op:confinement-potential` and `op:glueball-spectrum`: one coefficient, an
open chain and a closed one.

(c) Soften "no confining medium" to "no medium in the basis records read",
with the electric and magnetic readings of one vacuum (section 3), and cite
't Hooft and Mandelstam as the conjugate description and not as a rival.

(d) Add the trace anomaly as the standard form of "all mass is the cost of
made space", beside "all mass is geodesic length". It gives that subsection a
theorem to stand next to.

(e) Add the forward direction: the conjecture m_gap >= C sqrt(sigma), with
Chatterjee's converse, in place of or beside the tensor-network suggestion.

(f) Record in `op:qcd-scale` that it is equivalent to g_s at the matching
scale, with ln(M/Lambda) = 10.1 as the number owed.

(g) Paper 2: the bag constant as a cosmological term is a debt of the
"energy to create space" reading; put it with the which-column boundary.

Draft for (a) and (e), paper register, not applied:

    What the framework does supply is a reason to expect a gap, and a form
    for it. In the electric description of a gauge theory the states are
    closed networks of colour flux and the confining vacuum is the empty
    network. A static pair is joined by an open chain and a glueball is a
    closed one, and at strong coupling both are priced by a single number,
    the cost of one link: the tension is that cost per unit length and the
    gap is that cost times the size of the smallest closed network. In this
    sense confinement and the gap are one fact counted two ways. A continuum
    has no smallest network, and what then holds the gap open is a second
    cost: a network of size $L$ must resolve the distance $L$, at a price of
    order $\hbar c/L$, so that its energy is bounded below by
    $\sigma L + c/L$ and hence by $2\sqrt{c\,\sigma}$. Extent is expensive
    because space must be made; resolution is expensive because a
    relationship must be distinguishable. The electromagnetic sector has the
    second cost without the first, and its minimum is zero. We state the
    consequence as a conjecture for others to test and not as a result: in
    pure Yang--Mills theory the gap is bounded below by a universal multiple
    of $\sqrt{\sigma}$. The converse implication, from a strong form of the
    gap to the area law, has been proved on the lattice for gauge groups with
    a non-trivial centre \autocite{chatterjee2021probabilistic}.

## 10. Fences

- The model is Z_N, not SU(3); two space dimensions, not three; 9 and 16
  plaquettes with a fixed outer boundary; no continuum limit. It shows
  kinematics and the two phases. It says nothing about SU(3) at weak
  coupling.
- The Z_3 transition is first order in 2+1 dimensions and the Z_2 one is
  continuous; on these sizes neither is resolved, and I draw nothing from
  the transition region.
- gap/sigma = 4 is in lattice units. It is not the continuum m/sqrt(sigma).
- The first run of the script failed one check, 26/27. The failure was mine:
  the numerical minimisation of the tube energy searched cross-sections up to
  60 GeV^-2 and the minimum is at 102. I widened the range; no other line
  changed. The stdout below is the second run.
- From memory and unverified: the bag mode x = 2.744, the condensate 0.012
  GeV^4, the bag coupling 0.55, the mass-equals-trace theorem's attribution,
  Chen et al.'s 1710 MeV, the Communications in Mathematical Physics
  reference for Chatterjee.
- Margolus--Levitin is a bound on orthogonalisation time. Using it for "the
  cost of resolving a distance" is an analogy with the right dimensions.
- I do not know the literature on rigorous gap--tension inequalities well
  enough to say none exists. "I do not know of one" is the claim.

## 11. Proposed ledger entries (for JS; not written)

- **STRUCTURAL** In the electric basis of a Z_N lattice gauge theory at
  strong coupling the static potential is R c(1) and the gap is n_min c(1),
  n_min the size of the smallest closed network; the zero-flux vacuum is a
  product state and is the uniform superposition of gauge fields with vortex
  order parameter 1. Verified exactly (script A to 0.5 per cent at x = 0.02;
  script B to 1e-12).
- **CANDIDATE** Confinement and the mass gap are one cost, that of a colour
  relationship, counted along an open chain and around a closed one; the
  framework's "no space apart" is the electric reading of the dual
  superconductor's vacuum.
- **CANDIDATE** All colour-only mass is the cost of made space: the trace
  anomaly as the standard form of "all mass is geodesic length" in the
  colour sector.
- **CONJECTURE** In pure Yang--Mills theory m_gap >= C sqrt(sigma) with C
  universal, from sigma L + c/L. Converse to Chatterjee 2021.
- **CONJECTURE** The record structure forbids a condensed colour network;
  this is the missing dynamics of confinement in the framework's terms.
- **OPEN** `op:qcd-scale` restated: derive g_s at the 3.6 TeV matching scale.
  PASS: alpha_s(3.6 TeV) inside 0.0784 +/- 0.0010 (two-loop from
  alpha_s(M_Z) = 0.1180(9); the band is my estimate and needs a four-loop
  check). FAIL: any rule already closed on 2026-10-30.
- Proposed for `invalid_routes.md`: "the gap from the discreteness of closed
  networks alone" (fails in a continuum; section 4), and "g_s^2 = 1 at the
  matching scale read off the one-loop number" (section 7).

## 12. Exact stdout of `scripts/mass_gap_relationship_cost_2026-11-21T0800.py`

```

A. Z_3 gauge theory, 3 x 3 plaquettes (19683 states); c(1) = 1.5000
      x      gap   gap/4c1     V(1)     V(2)     V(3)   sigma   sigma/c1  gap/sigma      M     rho
   0.02   5.9797   0.9966   1.4998   2.9996   4.4995  1.4998    0.9999      3.987  1.000  0.0000
   0.05   5.9483   0.9914   1.4989   2.9977   4.4966  1.4989    0.9992      3.969  1.000  0.0002
   0.10   5.8930   0.9822   1.4954   2.9907   4.4861  1.4954    0.9969      3.941  0.999  0.0009
   0.20   5.7707   0.9618   1.4809   2.9614   4.4421  1.4806    0.9871      3.897  0.996  0.0036
   0.30   5.6317   0.9386   1.4557   2.9098   4.3642  1.4544    0.9696      3.872  0.992  0.0083
   0.40   5.4754   0.9126   1.4195   2.8338   4.2488  1.4150    0.9434      3.869  0.984  0.0152
   0.60   5.1131   0.8522   1.3140   2.6030   3.8938  1.2908    0.8605      3.961  0.962  0.0363
   1.00   4.2693   0.7116   0.9937   1.8656   2.7565  0.8910    0.5940      4.792  0.865  0.1129
   3.00   6.8736   1.1456   0.0738   0.0929   0.1613  0.0685    0.0457    100.366  0.098  0.5427
  worst Lanczos residual 1.8e-10
  [PASS] Z_3: Lanczos residuals below 1e-6
  [PASS] Z_3 strong coupling: gap = 4 c(1) within 2% (the smallest closed network has four links)
  [PASS] Z_3 strong coupling: V(R) = R c(1) within 2% for R = 1, 2, 3 (one cost per link created)
  [PASS] Z_3 strong coupling: vacuum has M > 0.99 and flux-link density rho < 0.01
  [PASS] Z_3: sigma falls monotonically as the plaquette term grows
  [PASS] Z_3: M falls and rho rises monotonically (the vacuum fills with flux)
  [PASS] Z_3 weak coupling (x = 3.0): gap is large while sigma/gap < 0.05 (a gap without confinement)

A. Z_2 gauge theory, 4 x 4 plaquettes (65536 states); c(1) = 2.0000
      x      gap   gap/4c1     V(1)     V(2)     V(3)   sigma   sigma/c1  gap/sigma      M     rho
   0.02   7.9990   0.9999   1.9996   3.9992   5.9988  1.9996    0.9998      4.000  1.000  0.0000
   0.10   7.9760   0.9970   1.9900   3.9800   5.9700  1.9900    0.9950      4.008  0.999  0.0010
   0.30   7.7900   0.9738   1.9131   3.8207   5.7275  1.9068    0.9534      4.085  0.989  0.0090
   0.60   7.2263   0.9033   1.6839   3.3116   4.9205  1.6090    0.8045      4.491  0.952  0.0359
   1.00   6.1735   0.7717   1.2676   2.3487   3.3679  1.0192    0.5096      6.057  0.852  0.0988
   1.50   5.2625   0.6578   0.7522   1.2198   1.6387  0.4189    0.2094     12.563  0.618  0.2078
   2.00   5.7698   0.7212   0.4082   0.5747   0.7282  0.1535    0.0767     37.591  0.359  0.3043
   3.00   9.0079   1.1260   0.1536   0.1839   0.2143  0.0304    0.0152    296.032  0.124  0.3941
   6.00  20.7902   2.5988   0.0322   0.0343   0.0365  0.0022    0.0011   9540.164  0.021  0.4563
  worst Lanczos residual 1.8e-07
  [PASS] Z_2: Lanczos residuals below 1e-6
  [PASS] Z_2 strong coupling: gap = 4 c(1) within 2% (the smallest closed network has four links)
  [PASS] Z_2 strong coupling: V(R) = R c(1) within 2% for R = 1, 2, 3 (one cost per link created)
  [PASS] Z_2 strong coupling: vacuum has M > 0.99 and flux-link density rho < 0.01
  [PASS] Z_2: sigma falls monotonically as the plaquette term grows
  [PASS] Z_2: M falls and rho rises monotonically (the vacuum fills with flux)
  [PASS] Z_2 weak coupling (x = 6.0): gap is large while sigma/gap < 0.05 (a gap without confinement)

B. The empty electric vacuum in the link basis: two plaquettes, seven Z_3 links
  [PASS] zero electric energy: every link shift has expectation 1
  [PASS] the state is uniform over all 2187 gauge fields (amplitude spread 0.0e+00)
  plaquette holonomy distribution: [[0.33333333333333326, 0.33333333333333326, 0.33333333333333326], [0.33333333333333326, 0.33333333333333326, 0.33333333333333326]]
  [PASS] each plaquette holonomy is uniformly distributed (1/3 each): magnetic flux fully disordered
  [PASS] Wilson loops vanish: |<W_1>|, |<W_2>|, |<W_12>| = 1.2e-16, 1.3e-16, 1.3e-16
  [PASS] vortex (holonomy-shift) operator has expectation 1.000000: a perfect magnetic condensate
  [PASS] in the electric basis it is the one product state e = 0 (weight 1.000000000000): no link is related to any other
  [PASS] entanglement entropy of one link with the rest = -8.88e-16

C1. Loop competition E(L) = sigma L + c/L, minimum 2 sqrt(c sigma) at L = sqrt(c/sigma)
  c = 1.5708: numerical minimum 2.506628, 2 sqrt(c) = 2.506628 (units sqrt(sigma))
  c = 3.1416: numerical minimum 3.544908, 2 sqrt(c) = 3.544908 (units sqrt(sigma))
  c = 6.2832: numerical minimum 5.013257, 2 sqrt(c) = 5.013257 (units sqrt(sigma))
  [PASS] numerical minimum equals 2 sqrt(c sigma) for the three values of c
  candidate                                                         m/sqrt(sigma)   pull A   pull B
  c = pi/2   one orthogonalisation per traversal (Margolus-Levitin)     2.507    -42.8    -14.9
  c = pi     half a wavelength on the loop                              3.545     +6.7     -0.1
  c = 2 pi   one wavelength on the loop                                 5.013    +76.6    +20.9
  closed Nambu-Goto string, D = 4, N = 1: sqrt(8 pi 11/12)              4.800    +66.4    +17.9
  lattice A (from memory, VERIFY-CITE)     m/sqrt(sigma) = 3.405 +/- 0.021  ->  c required = 2.899
  lattice B (from memory, VERIFY-CITE)     m/sqrt(sigma) = 3.550 +/- 0.070  ->  c required = 3.151
  [PASS] every candidate is within a factor 1.5 of the lattice ratio, and they disagree with each other by 2.00x: order of magnitude only

C2. The bag: creating a volume V of colour space costs B V
  B^(1/4) = 0.145 GeV: glueball bag mass 1.305 GeV (closed form 1.305), radius 1.11 fm, M/B^(1/4) = 9.000
  B^(1/4) = 0.200 GeV: glueball bag mass 1.800 GeV (closed form 1.800), radius 0.80 fm, M/B^(1/4) = 9.000
  B^(1/4) = 0.241 GeV: glueball bag mass 2.169 GeV (closed form 2.169), radius 0.67 fm, M/B^(1/4) = 9.000
  [PASS] bag mass equals (4/3)(4 pi B)^(1/4) x^(3/4): linear in B^(1/4), zero iff B = 0
  trace anomaly, n_f = 0: vacuum energy density = -(b0/32) <alpha G^2/pi> = -0.00413 GeV^4, |eps|^(1/4) = 0.253 GeV
  trace anomaly, n_f = 3: vacuum energy density = -(b0/32) <alpha G^2/pi> = -0.00337 GeV^4, |eps|^(1/4) = 0.241 GeV
  bag flux tube: sigma = sqrt(32 pi alpha_s B / 3); alpha_s = 0.55, B^(1/4) = 0.145 GeV gives sqrt(sigma) = 0.300 GeV (measured 0.44)
  [PASS] tube energy g^2/(2A) + B A minimised numerically equals sqrt(2 g^2 B) = 0.09026 GeV^2

C3. Dimensional transmutation: ln(M/Lambda) = 2 pi / (b0 alpha_s(M)) = (8 pi^2/g^2)/b0
  1-loop: alpha_s(3.6 TeV) = 0.07913, g_s^2 = 0.9944, instanton action 8 pi^2/g^2 = 2 pi/alpha_s = 79.40 nats
  2-loop: alpha_s(3.6 TeV) = 0.07835, g_s^2 = 0.9845, instanton action 8 pi^2/g^2 = 2 pi/alpha_s = 80.20 nats
  [PASS] one-loop integration agrees with the closed form (0.079130, 0.079130)
  one-loop Lambda: n_f = 6 continued from 3.6 TeV 0.0427 GeV; n_f = 5: 0.0878; n_f = 4: 0.1196; n_f = 3: 0.1425 GeV
  ln(3.6 TeV / Lambda_3) = 10.14;  Lambda_3 / v = 5.79e-04 (v = 246.22 GeV);  sqrt(sigma)/v = 1.79e-03
  [PASS] the one-loop hadronic scale is of order 1e-3 of v, as op:qcd-scale states

27/27 checks passed
MASS GAP RELATIONSHIP COST: PASS
```

## Addendum 2026-11-21T1000: the OpenAI existence announcement, and where the two ends meet

JS asked whether OpenAI's announced Yang--Mills result, which comes from
lattice gauge theory, can be brought together with the framework's account,
which starts from the entanglement budget.

**What was read.** The page
`https://openai.com/index/building-scientific-understanding-with-academic-communities/`,
dated 26 October 2026, section "Existence of quantum chromodynamics and
completions of the Standard Model", read today through a fetch agent
(paraphrase plus short quotations; I did not see the full text verbatim).
No paper, preprint or Lean repository is linked. Everything below about the
result is "Support: announcement only".

- Claim: "a mathematically rigorous existence proof of certain interacting
  quantum field theories" with gauge fields and fermions in four dimensions,
  including QCD; pure Yang--Mills existence as a subproblem; the proof
  "pertains to the simplest grand unified theory" containing the Standard
  Model's gauge fields and fermions. Gauge group not named on the page.
- Method: "Balaban's approach in constructive quantum field theory". Asymptotic
  freedom is called "the key mechanism underlying the existence".
- Not claimed: the mass gap, confinement, an area law, the Clay problem.
  What "existence" means (which axioms, finite or infinite volume) is not
  stated.
- Status: natural-language proofs dated 9 and 18 September 2026; a Lean
  formalisation of Yang--Mills existence finished 16 October 2026; artefacts
  withheld while a group led by David Gross, with Douglas, Jaffe, Klebanov
  and Nekrasov, writes it up. Not peer reviewed, not public.

**Assessment (CANDIDATE unless marked).**

1. The two are the two halves of the Clay problem, not two routes to one
   result. Existence is an ultraviolet statement and rests on asymptotic
   freedom. The gap is an infrared statement and rests on strong coupling.
   The framework's link-cost argument is exact only at strong coupling
   (sections 2 to 4). Neither implies the other.
2. The meeting place is definite. Balaban's method is a block-spin
   renormalisation group: it produces, at each scale, an effective lattice
   gauge theory at unit spacing, and is controlled while the running
   coupling is small (from memory; VERIFY-SUPPORT against Balaban and the
   Dimock review the page links, Rev. Math. Phys. 25 (2013) 1330010). The
   framework's statements are statements about exactly such an object: a
   lattice gauge theory in the electric basis with a link cost. So the join
   is: the effective theory where Balaban's flow stops, at spacing of order
   1/Lambda, is the theory on which "one link cost prices tension and gap"
   has to be proved.
3. What is missing is the middle, and it is the known hard part: that the
   flow from weak to strong coupling crosses no phase boundary, so the
   effective theory at 1/Lambda is in the phase where the empty network is
   the vacuum. The framework's sentence for it is section 6's: colour
   relationships never form a space. It does not prove it. Correction 2 of
   section 9 (a gap can exist without confinement) is the reason this cannot
   be skipped.
4. The budget argument is about quarks; the Clay problem has none. In pure
   Yang--Mills the framework's statement must be carried by the centre
   one-form symmetry and the area law (the 2026-11-07 note's N-ality
   grading), not by the GHZ budget of three quarks. With fundamental quarks,
   as in QCD, the string breaks and there is no area law; the gap there is
   set by chiral symmetry breaking and the pion, which the framework has not
   addressed in this thread. OPEN.
5. Two tensions with the framework, both real.
   (a) Grand unification. The announced completion is a grand unified
   theory. The reason is forced by the method: hypercharge is not
   asymptotically free, so the Standard Model alone has no continuum limit
   of this kind. The framework excludes grand unification and has no scale
   between 3.6 TeV and Planck. It therefore owes its own answer to the
   hypercharge ultraviolet problem. The answer it already gives is that the
   continuum completion is a convention (continuity section, patched
   2026-10-29) and the lattice is the exchange graph (2026-11-07 lattice
   note); that answer should be stated beside sin^2 theta_W = 1/4, because a
   reader who knows this result will ask. Proposed OPEN.
   (b) The continuum. If continuum Yang--Mills exists, then discreteness of
   the network cannot be what holds the gap open, since the continuum theory
   is believed to have the gap too. This is correction 3 again, now with a
   theorem (if it stands) behind it.
6. What each side could use from the other. From them: a rigorous
   Lambda, which makes `op:qcd-scale` a well-posed question about one
   number. From the framework: a target for the infrared half stated on
   their effective lattice theory, namely the conjecture m_gap >= C sqrt(sigma)
   as the converse of Chatterjee 2021, and the observation that the confined
   vacuum is a product state in the electric basis.

No computation was run for this addendum. Proposed ledger entry: OPEN, "the
hypercharge ultraviolet completion without grand unification", PASS a stated
mechanism that bounds the hypercharge coupling at every scale the framework
owns without a unifying group, FAIL any route that introduces a unification
scale.
