# Jacobson's "non-equilibrium spacetime", read as the graded FANOUT of a horizon

Date: 2026-09-20T1600. Fable session, at JS's prompt quoting the closing
paragraph of Jacobson 1995 (gr-qc/9504004, `Jacobson1995` in the library,
read in full for this note): sufficiently high-frequency or large-amplitude
disturbances of the gravitational field would not be described by the
Einstein equation, "not because some quantum operator nature of the metric
would become relevant, but because the local equilibrium condition would
fail", and the hope of understanding "non-equilibrium spacetime". Paper 2
carries a TODO for exactly this ("one paragraph engaging the
equation-of-state moral's history, Jacobson's own caveats, Padmanabhan's
atoms of spacetime"); section 7 drafts it. Follows
`records_causal_structure_high_temperature_2026-09-20T1400.md` and
`landauer_temperature_fanout_energy_2026-09-20T1200.md`. Labels proposed.

## 0. The answer in brief

Jacobson's paragraph is the framework's thesis stated by its precedent: no
quantised metric, and a regime boundary set by the failure of local
equilibrium. What the framework adds is the answer to the question his
analogy leaves open, what the molecules are and what their equilibrium is.
The molecules are records, locked relations across the local Rindler horizon;
the equilibrium is the plateau of the graded FANOUT, at which the count of
records is a function of the area alone; local equilibrium fails when the
disturbance changes the horizon faster than records can lock (bounded by the
thermal time of the hovering observer, hence in the strict local limit only
at the Planck scale of the patch) or delivers more records than the patch can
hold (the capacity bound of the high-temperature note). Off the plateau the
cost is partly still in the imaginary column, the real entropy lags the area,
and the lag is entropy production: Jacobson's sound that "no longer
propagates in a time reversal invariant manner" is the closed loop of the
two-columns note failing to close. The literature has already pursued his
hope some way, in Eling, Guedens and Jacobson's entropy-production term and
in Chirco and Liberati's identification of the dropped shear term with the
horizon's viscosity at the Kovtun--Son--Starinets value $\eta/s = 1/4\pi$;
the framework should inherit both rather than rederive them, and its own
contribution is a well-formed open problem: derive the non-equilibrium
correction from the graded count with a relaxation time bounded by the chaos
bound.

## 1. What Jacobson assumes and says [read]

The derivation: heat is energy flux across a causal horizon; entropy is
proportional to horizon area with a cutoff $l_{c}$ that consistency fixes at
the Planck length; the temperature is the Unruh temperature of an observer
hovering just inside, taken in the limit of infinite acceleration where
temperature and flux both diverge with a finite ratio; through every point a
local Rindler horizon is chosen with vanishing expansion and shear, "so that
the system is instantaneously stationary (in local equilibrium)"; then the
Raychaudhuri equation with the $\theta^{2}$ and $\sigma^{2}$ terms dropped
turns $\delta Q = T\,dS$ into the Einstein equation with
$G = (4\hbar\eta)^{-1}$. Four remarks of his matter here.

The scale separation. The analysis "relies heavily" on the curvature radius
being vastly larger than $l_{c}$, $10^{38}$ at a stellar black hole, and fails
"only near the big bang or a black hole singularity, or in the final stages
of evaporation of a primordial black hole".

The equilibrium caveat. $\delta Q = T\,dS$ "only applies to variations
between nearby states of local thermodynamic equilibrium"; in free expansion
of a gas entropy rises without heat flow and the relation fails; "local
temperature and entropy are not even well defined away from equilibrium".

The deeper assumption, and the speculation. The usual short-distance vacuum
fluctuations, the vacuum as a zero-temperature thermal state, are assumed;
"we speculate that out of equilibrium vacuum fluctuations would entail an
ill-defined spacetime metric".

The analogy. The Einstein equation is to the molecules as the sound wave is
to the gas: a statistically defined observable on the fundamental phase
space, not to be canonically quantised "even though there is no question
that the individual molecules are quantum mechanical"; at high frequency or
intensity local equilibrium breaks, entropy increases, and sound propagation
is no longer time-reversal invariant.

## 2. The dictionary [CANDIDATE]

*The molecules are records.* Jacobson's system is "the degrees of freedom
beyond the horizon", the entropy "the correlations between vacuum
fluctuations just inside and outside", with a cutoff. In the framework the
horizon is a FANOUT boundary drawn by the observer's motion (Paper 1: the
Unruh effect is Wigner's friend for accelerated observers), the degrees of
freedom beyond it are relations declared inaccessible, the correlations
across it are the records, and the cutoff is the record's size, one locked
relation per unit of area in Planck units, which Paper 2's count-density
dictionary is to supply (op:p2-coefficient). Jacobson's "given a microscopic
theory of spacetime structure one may someday be able to compute $\eta$ in
terms of a fundamental length scale" is that open problem in his words.

*Local equilibrium is the plateau.* The graded FANOUT of the hub's section
4b has a rotation from the imaginary column (phase, unlocked) to the real
column (records), and a plateau at which the joint record is complete and
the count is a function of the fragments alone. For a horizon patch,
equilibrium is the plateau: the count of locked relations across the patch is
a state function of its area, so that $dS = \eta\,\delta A$ holds with no
history dependence. Jacobson's two conditions map onto the two things that
can go wrong with a plateau. Vanishing expansion and shear at $p$ is the
condition that no records are being created or redistributed across the
patch during the variation, so that the count is not lagging; and the
standard vacuum fluctuations are the condition that the pre-geometric layer
below the cutoff is at rest, in its KMS state for the hovering observer, so
that there is a well-defined column to rotate from. His speculation that
out-of-equilibrium vacuum fluctuations "would entail an ill-defined
spacetime metric" is, word for word, the framework's claim that the layer
beneath locking is pre-geometric: no metric before the records exist.

*Sound is the hydrodynamics of conserved records.* The high-temperature note
(section 2) reduced a plasma's causal structure to the conserved densities,
whose long-wavelength modes are sound and diffusion. Jacobson's analogy is
then not an analogy in the framework: the Einstein equation is the
long-wavelength mode of the record fluid, propagating "via a myriad of
incoherent" lockings, and it fails where sound fails, when the disturbance is
faster than the local relaxation.

## 3. Why and where equilibrium fails [CANDIDATE; the scales STRUCTURAL]

Two rates and one capacity, all from the earlier notes, decide it.

*Records cannot lock faster than the thermal time.* The rotation to the real
column is bounded by the chaos bound, one turn per thermal period of the
observer whose horizon it is. For Jacobson's hovering observer the
acceleration diverges, the Unruh temperature with it, and the thermal time
goes to zero: in the strict local limit locking is instantaneous and
equilibrium holds for any disturbance of finite frequency. So the failure
cannot come from the point; it comes from the patch. The patch must be large
enough for the area to be a count, many records across, and small enough to
be instantaneously stationary; a disturbance whose wavelength approaches the
patch size, or whose period approaches the locking time of the patch's
records, leaves no surface on which both hold. The floor on the patch is the
record's size, $l_{c} \sim l_{P}$, and that is Jacobson's own scale
separation: non-equilibrium spacetime is the regime in which a horizon patch
holds of order one record, and no state function exists because there is
nothing to average.

*Records cannot exceed the capacity.* The high-temperature note's section 4:
the count a patch can lock is bounded by its area, and thermal record
production exceeds it within a few thermal lengths on the approach to the
Planck temperature. Large-amplitude disturbances deliver records faster than
the plateau can absorb them. In Jacobson's derivation this is where the
dropped terms return: the $\theta^{2}$ and $\sigma^{2}$ in the Raychaudhuri
equation are exactly the non-linear focusing that a large flux produces, and
keeping them is keeping the non-equilibrium.

*The consequence is entropy production.* Off the plateau the cost of the
variation is partly still imaginary, phase not yet locked, and the real
entropy lags the area. The Clausius relation acquires an irreversible term,
$\delta Q = T\,(dS + d_{i}S)$ with $d_{i}S \ge 0$, and the equation of state
acquires dissipative corrections: bulk dissipation from $\theta^{2}$, shear
dissipation from $\sigma^{2}$. The record fluid, like any fluid, has a
viscosity, and the framework's claim is only that its coefficients are set by
the same $\eta$ that sets $G$, because they count the same records.

## 4. How far the literature has already carried the hope [bibliography verified 2026-09-20; one attribution wrong]

*Verification, 2026-09-20 (Opus session).* Every reference in this section
and in section 9 is verified against Crossref by DOI, except Padmanabhan 2012,
which arXiv and INSPIRE both show as an unpublished preprint with no DOI, so
it is entered as `@online`. Every journal, volume and article number
remembered was right. Two spellings to note: Eling, Guedens and Jacobson, and
Chirco and Liberati, both print "Nonequilibrium" as one word.

**The coefficient is not Chirco and Liberati's.** Their paper was read,
because this section proposes to inherit a number from it. They do state
$\eta = 1/(16\pi G)$, but as a review: "it is also noticed in [2] that by
using (19), one gets $\eta = 1/(16\pi G)$ in agreement with the value
obtained for the shear viscosity of the stretched horizon of a black hole in
the so called membrane paradigm", closing with "This result concludes the
review of the argument described in [1, 2, 12]." Their [2] is Eling, Guedens
and Jacobson; the membrane-paradigm references are Price and Thorne. They do
re-derive it in their own setting later, as $\eta = \hbar\alpha/4\pi$ "in
agreement with the universal relation for the viscosity to entropy density
ratio found in the AdS/CFT context", but they never write $1/4\pi$ as a
number. Their own result, and it is a different statement, is that the
internal entropy production term in GR "is identical to the so called tidal
heating term of Hartle-Hawking".

So the closing sentence of this section, "The framework should inherit the
Chirco--Liberati coefficient, not rederive it", should read that it inherits
the **membrane-paradigm** coefficient, as reviewed and re-derived by Chirco
and Liberati, citing Eling, Guedens and Jacobson alongside them. Nothing in
the physics changes; the credit does. One further care: Kovtun, Son and
Starinets state $\eta/s \ge 1/4\pi$ as a lower **bound**, saturated in the
holographic examples, and this section calls $1/4\pi$ "the
Kovtun--Son--Starinets value", which should say whether it means the bound or
the saturation.


- Eling, Guedens and Jacobson, "Non-equilibrium thermodynamics of
  spacetime", Phys. Rev. Lett. 96, 121301 (2006): for an entropy density
  that is a function of curvature ($f(R)$ gravity) the Clausius relation
  cannot be satisfied without an entropy-production term, which they
  interpret as bulk-viscosity-like dissipation; the equilibrium assumption
  fails for those theories and the correction is computable.
- Chirco and Liberati, "Non-equilibrium thermodynamics of spacetime: the
  role of gravitational dissipation", Phys. Rev. D 81, 024016 (2010): keeping
  the shear term Jacobson dropped gives an internal entropy production
  matching the membrane paradigm's shear viscosity of the horizon,
  $\eta_{\rm visc} = 1/16\pi G$, hence $\eta_{\rm visc}/s = 1/4\pi$, the
  Kovtun--Son--Starinets value. Non-equilibrium spacetime, at leading order,
  is a horizon fluid of minimal viscosity.
- Jacobson, "Entanglement equilibrium and the Einstein equation", Phys.
  Rev. Lett. 116, 201101 (2016): the equilibrium condition restated as
  maximal vacuum entanglement of a small ball, with the semiclassical
  Einstein equation as its consequence.
- Padmanabhan, "Thermodynamical aspects of gravity: new insights", Rep.
  Prog. Phys. 73, 046901 (2010), and "Emergence and expansion of cosmic
  space as due to the quest for holographic equipartition", arXiv:1206.4916:
  the "atoms of spacetime", surface and bulk degrees of freedom, equilibrium
  as holographic equipartition $N_{\rm sur} = N_{\rm bulk}$, and cosmic
  expansion as the approach to it. In the framework's terms his atoms are
  records, his equipartition is the plateau, and his expansion as an
  approach to equipartition is nascent locking; Paper 2 should say so and
  cite him beside Jacobson.
- The rate side, from the high-temperature note: Maldacena, Shenker and
  Stanford for the chaos bound; Sekino and Susskind for scrambling.

The framework should inherit the Chirco--Liberati coefficient, not rederive
it, and claim only what is its own: the reading of the plateau, the rates,
and the open problem below.

## 5. The two columns and time reversal [CANDIDATE; the loop RHYME]

Jacobson's criterion for equilibrium is time-reversal invariance of the
propagating mode, and his criterion for its failure is the loss of it with
entropy increase. In the two-columns note the Born rule was the closed loop
of a history and its return leg, phases cancelling, real cost on the
diagonal; the off-diagonal, the loop that fails to close, keeps a phase and
is what records remove. Equilibrium spacetime is the diagonal: every
variation of the horizon is a loop that closes, forward and return legs
cancel, the relation $\delta Q = T\,dS$ is reversible, and the Einstein
equation is time-symmetric. Non-equilibrium spacetime is the off-diagonal: a
variation whose return leg does not cancel, because records formed in
between, leaves a net imaginary part that is paid as $d_{i}S$. The
relaxation time of this process is bounded below by the chaos-bound time,
$\hbar/2\pi k_{B}T$, and the shape of the resulting dynamics is that of
second-order (Israel--Stewart) hydrodynamics, whose holographic relaxation
times are of the same order (Baier, Romatschke, Son, Starinets and
Stephanov, JHEP 04 (2008) 100, verified 2026-09-20 against Crossref
10.1088/1126-6708/2008/04/100; body not read, so the claim that their
relaxation times are of the chaos-bound order is not checked against them).
RHYME: the
horizon's $\eta/s = 1/4\pi$ is a relaxation time of half a turn of the
imaginary column per thermal period; whether the half is the two legs of the
loop is not shown.

## 6. A well-formed open problem for Paper 2 [OPEN, proposed]

op:p2-nonequilibrium. Derive, from the graded count of locked relations
across a local Rindler horizon patch, the non-equilibrium correction to
$\delta Q = T\,dS$ as an entropy-production term $d_{i}S \ge 0$, and show
three things. (i) Its shear coefficient reproduces the membrane paradigm's
horizon viscosity, $\eta_{\rm visc}/s = 1/4\pi$ (Chirco--Liberati), from the
same $\eta$ that fixes $G$ in op:p2-coefficient. (ii) Its relaxation time is
bounded below by $\hbar/2\pi k_{B}T_{U}$, the chaos-bound time of the hovering
observer, and the bound cancels against the flux in the local limit as the
temperature does. (iii) The breakdown scale is the patch that holds of order
one record, $l_{c} \sim l_{P}$, and no scale below the Planck scale appears.
PASS: (i) exactly and (ii), (iii) at the level of scaling. FAIL: a
coefficient or relaxation time that depends on the arbitrary hovering
observer without cancelling, a $d_{i}S$ that can be negative, or a
non-equilibrium scale below the Planck scale, which would contradict Paper
1's "standard decoherence rates, nothing gravity-specific". Depends on
op:p2-coefficient; the Chirco--Liberati and Eling--Guedens--Jacobson papers
must be read first.

## 7. Draft of the Paper 2 paragraph (the TODO at the end of the ontology section)

Jacobson's own caveats already draw the boundary this paper draws. His
derivation, he says, "presumed the existence of local equilibrium
conditions", the relation $\delta Q = T\,dS$ applying only between nearby
equilibrium states, with local temperature and entropy "not even well
defined away from equilibrium"; it assumed the usual short-distance vacuum
fluctuations, and he speculated that out-of-equilibrium fluctuations "would
entail an ill-defined spacetime metric"; and his closing analogy is that
sufficiently high-frequency or large-amplitude disturbances would escape the
Einstein equation "not because some quantum operator nature of the metric
would become relevant, but because the local equilibrium condition would
fail" \autocite{Jacobson1995}. The present paper takes that sentence as its
programme and supplies what the analogy with sound leaves open: the
molecules are locked relations, their equilibrium is the plateau of
redundancy at which their count is a function of the horizon's area alone,
and local equilibrium fails when a disturbance changes the horizon faster
than relations can lock or delivers more of them than the patch can hold, the
first bounded by the thermal time of the hovering observer and the second by
the area itself, so that in the local limit the failure is confined to
patches of Planck size, which is Jacobson's own separation of scales. Off the
plateau the entropy lags the area and the Clausius relation acquires an
irreversible term; the literature has computed its leading form, an entropy
production for curvature-dependent entropies \autocite{elingguedensjacobson2006nonequilibrium}
and, from the shear term the original derivation set aside, a horizon
viscosity at the Kovtun--Son--Starinets value \autocite{chircoliberati2010dissipation},
which this paper inherits as the leading description of non-equilibrium
spacetime and does not rederive (Open Problem~\ref{op:p2-nonequilibrium}).
Padmanabhan's atoms of spacetime, and his reading of cosmic expansion as the
approach to holographic equipartition \autocite{padmanabhan2010thermodynamical,
padmanabhan2012emergence}, are the same picture with the atoms unnamed: the
atoms are records, the equipartition is the plateau, and the approach to it is
the nascent locking of Section~\ref{sec:p2-junction}. (All citation keys other than `Jacobson1995` were placeholders. They are now
real: verified 2026-09-20 and batched, under exactly these keys, in
`bib/jacobson_nonequilibrium_refs_2026-09-20T2200.bib`. Undefined until the
batch is imported.)

## 8. Fences and pushback

- The dictionary of section 2 is a reading. Jacobson's derivation does not
  need it, and the framework has not yet produced the count that would make
  "the molecules are records" more than a name (op:p2-coefficient).
- The only quantitative content in sight is inherited (Chirco--Liberati's
  $1/4\pi$; Eling--Guedens--Jacobson's production term), and neither has
  been read for this note. Claim nothing about them beyond the citations
  until they are.
- No prediction at accessible frequencies. The framework's non-equilibrium
  regime is Planckian or high-temperature, consistent with Paper 1's
  "standard decoherence rates"; anyone hoping for anomalous gravitational-wave
  dispersion from this should be told no.
- The "molecules" analogy has a known limit Jacobson himself flags: sound's
  phase space is given, spacetime's is what is being derived; Paper 2's
  two-level reading (the arena as the post-FANOUT record) is the answer,
  and this note does not add to it.
- The half-turn rhyme of section 5 is a rhyme.

## 9. Proposed ledger entries and references

- **CANDIDATE** Jacobson's local equilibrium is the plateau of the graded
  FANOUT across a local Rindler horizon; his two assumptions (stationarity
  at $p$; standard vacuum fluctuations) are the two conditions for a plateau
  (no lag; the pre-geometric layer at rest); his "ill-defined metric out of
  equilibrium" is the framework's pre-geometric layer.
- **CANDIDATE** Local equilibrium fails through two rates and one capacity:
  locking bounded by the thermal time, production bounded by the area; in
  the local limit the failure is confined to patches of Planck size.
- **CANDIDATE** Equilibrium spacetime is the closed loop (time-reversal
  invariance), non-equilibrium the unclosed one (entropy production).
- **OPEN** op:p2-nonequilibrium, section 6.
- **RHYME** $\eta/s = 1/4\pi$ as half a turn per thermal period.
- References, verified 2026-09-20 (Opus session) and batched in
  `bib/jacobson_nonequilibrium_refs_2026-09-20T2200.bib` under the keys this
  document already uses. Eling, Guedens and Jacobson 2006, Phys. Rev. Lett.
  96, 121301; Chirco and Liberati 2010, Phys. Rev. D 81, 024016 (body read;
  see the attribution correction in section 4); Jacobson 2016, Phys. Rev.
  Lett. 116, 201101; Padmanabhan 2010, Rep. Prog. Phys. 73, 046901;
  Padmanabhan 2012, arXiv:1206.4916, which is **unpublished** and is entered
  as `@online`; Baier, Romatschke, Son, Starinets and Stephanov 2008, JHEP 04
  (2008) 100; Kovtun, Son and Starinets 2005, Phys. Rev. Lett. 94, 111601;
  Israel and Stewart 1979, Ann. Phys. 118(2), 341--372. Every journal, volume
  and article number remembered was right. Read for this note: Jacobson 1995
  (in the library) and, by the verification pass, Chirco and Liberati 2010.
  None of the other six has been read.
