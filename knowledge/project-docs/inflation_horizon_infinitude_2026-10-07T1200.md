# Inflation, infinitude and the horizon: what the framework dispenses with, and what it owes (2026-10-07)

Session 2026-10-07, Fable 5.1. JS: the spacetime section says that if the
computational count (computable steps real, non-computable imaginary) is an
identity with spacetime, the universe is spatially infinite, hence always
infinite, hence needs no inflationary epoch to flatten it; another Claude
conversation pointed out that inflation also solves the horizon problem; JS
proposes that if the laws of nature are the same everywhere then everywhere
starts at the same temperature, so an infinite universe with uniform laws
needs no inflation. "Think deeply about this and report back."

Sources read: `paper1/spacetime_from_non-computability.tex` (the paragraph
"Spatial infinitude and the status of inflation", `sec:gr-nonlocality`,
`sec:no-quantised-gravity`, `op:comp-metric`, the expansion paragraph), the
September high-temperature notes (`records_causal_structure_high_temperature_2026-09-20T1400.md`,
`gravity_planck_scale_high_temperature_2026-09-20T1800.md`), the 2024 and
2025 Vaxjo posters' statement of the infinite-extent consequence. Script
`scripts/inflation_debts_at_framework_scales_2026-10-07T1200.py` (standard
cosmology for scale, no randomness), stdout in section 10. Labels per the
ledger vocabulary; this is Paper 2 material and is pointed to from the Paper
2 hub.

## 0. The answer in brief

Four things, in decreasing order of how much they change.

First, the paper already has the horizon point. The paragraph in the
spacetime section says in so many words that infinitude "settles only
flatness, which was never inflation's principal task. The horizon problem
is, and an infinite space does nothing for it", and it gives the framework's
answer: the relational thesis of `sec:gr-nonlocality`. The other
conversation's objection was anticipated and is in the text.

Second, "same laws, same temperature" does not work as stated, and the
reason it fails is instructive. In standard physics the laws being the same
everywhere is already assumed; the horizon problem is a problem about
*initial data*, not about laws. The same Einstein equations and the same
Standard Model applied to different data on the initial surface give
different temperatures, and generic data on a surface in general relativity
are inhomogeneous. What makes the argument valid in the framework is not
uniformity of law but the absence of anywhere for data to vary over: before
the first records there is one knowledge-space location and one thermal
state, so the regions of the later sky are fanned out from a single source
and inherit its temperature because they were never separate things that
had to agree. That is the paper's relational thesis in thermodynamic dress,
and it is stronger than the laws argument, which it contains as a corollary.

Third, the paper's "infinite, therefore flat" is wrong and should be
corrected. An open universe of negative curvature is infinite at every epoch
and never flat; infinitude excludes the closed case and nothing else. The
flatness problem is a fine-tuning in the Friedmann dynamics, which the
framework has not derived (`op:comp-metric`, and the expansion paragraph's
own admission that the full history "remains to be done"). Flatness is
owed, not settled, and the paragraph says the opposite. The script gives the
size of the debt: with the present bound on the curvature, the first-record
surface a few decades below the Planck temperature had to be flat to one
part in $10^{57}$.

Fourth, the hard debt is the one the paper already names, the primordial
spectrum, and the framework now has a direction for it that it did not
have in June: the spectrum must be a record of conformal structure, since
in the phase where the first records form there is no scale to record,
which is why it is scale-invariant; the tilt is the first scale announcing
itself. That is a conjecture with a literature (Hollands and Wald; the
pseudo-conformal mechanism; Penrose), not a result. And one consequence is
falsifiable now: with no inflaton and no metric to fluctuate before records
exist, the framework predicts no primordial tensor spectrum of inflationary
form.

## 1. Three claims that are run together, kept apart

JS's chain is: identity, hence infinite extent, hence always infinite,
hence no inflation. The chain conflates three properties of the spatial
sections, each of which inflation is credited with explaining.

- *Infinite* (unbounded extent). The framework's argument: no upper bound
  on non-computability, so no upper bound on spacelike distance. This shows
  the arena is unbounded; it does not show the realised network is, and it
  does not exclude a closed universe on its own terms (the framework's own
  $S^{3}$ is the group of transports, not the spatial manifold, but nothing
  in the paper forbids the manifold being $S^{3}$ too). Observation says
  the curvature radius exceeds the Hubble radius by at least a factor of
  about fourteen ($|\Omega_{k}|<0.005$). Status: CANDIDATE, "unbounded by
  anything in the framework", not ESTABLISHED. "Always infinite" is then
  the statement that at every epoch with recorded lengths the extent is
  unbounded; before lengths are recorded (section 7) extent is not a fact.

- *Flat* (zero spatial curvature, $\Omega=1$). Independent of infinitude.
  Section 4.

- *Homogeneous* (same temperature in regions with no common past). Independent
  of both. Section 2 and 3.

Inflation addresses the last two dynamically and says nothing about the
first; a $k=0$ or $k=-1$ Friedmann universe is infinite at every $t>0$ with or
without inflation. So "always infinite, hence no need to flatten" is a
non sequitur in standard cosmology, and the paper's "being a network
without a boundary, naturally flat" is a non sequitur too: a hyperbolic
tessellation is a network without a boundary.

## 2. "Same laws, same temperature": why it fails, and what makes it work here [CANDIDATE]

The standard objection, which any cosmologist will raise at once. The
cosmological principle has two halves: the laws are the same everywhere
(assumed by everyone, including the framework) and the *state* is the same
everywhere (the thing to be explained). Uniform laws do not force a uniform
state; they propagate whatever state is given on the initial surface, and
in general relativity that data is free and generically lumpy. The horizon
problem is precisely that the observed state is uniform over regions whose
past light cones do not meet, so no dynamics under those laws could have
made it uniform. Script part B: the particle horizon at recombination
subtends about $1.2^{\circ}$ today, so the sky holds roughly ten thousand
patches with no common past, all at the same temperature to $10^{-5}$. Inflation's
answer is to give them a common past. "Same laws" is not an answer to this;
it is one of the premises of the problem.

What the framework changes is the other premise, that the initial data
live on a surface with places. Three facts from the paper and the
September notes:

1. Spatial separation is produced by interaction, not revealed by it
   (`sec:gr-nonlocality`): two systems that have not interacted through the
   network occupy one knowledge-space location.
2. Above a few decades below the Planck temperature no region can hold its
   own records (records note, section 4; gravity note, section 0): there is
   no causal structure, hence no surface, hence no "here" and "there" on
   which data could differ.
3. The thermal state of the pre-record regime is one state with one modular
   flow, hence one thermal time and one temperature (records note, section
   3 and 5, Connes--Rovelli, `connesrovelli1994thermal`, body not read).

Put together: the first-record surface, the first thing that *is* a surface,
is produced by \textsc{fanout} from a single pre-spatial thermal state.
Every region of it inherits that state's temperature, not because the
regions equilibrated, and not because the laws are uniform, but because
there was one source. The later light cones are irrelevant to this: the
standard argument needs the data on the first surface to be uncorrelated
beyond the horizon, and the framework says they are maximally correlated
across the whole surface, horizon or no horizon. This is exactly the
paper's "pre-spatial entanglement correlates regions before \textsc{fanout}
spreads them into spatial separation", now with the thermodynamic
ingredient (one bath, one temperature) that turns "correlated" into "same
temperature".

So JS's argument is right in the framework, for a reason JS did not state
and the standard objection cannot touch: there is nowhere for initial data
to vary over. The laws being the same everywhere is, in the framework, not
an assumption either: the laws are the structure of the pre-spatial layer
(the division algebras, the fibrations, the computability split), which is
not located anywhere and so cannot differ between places. The clause that
should go in the paper is "the horizon problem is a problem about initial
data, and here the first data have no places to differ on", not "the laws
are the same everywhere".

Label: CANDIDATE, the relational thesis restated; it stands or falls with
the reading of spacelike separation as produced by records
(`op:comp-metric`).

## 3. Where the dissolution happens: the first-record surface, not the conformal phase

A precision, because the September notes invite a wrong placement. The
records note says that above the electroweak crossover there are no
clocks, no proper time and no metric scale, only causal order (section 3).
One might think the horizon problem dissolves there, in the conformal
phase. It does not. The horizon problem is a statement about causal
structure: the past light cones of two points on the last-scattering
surface do not intersect. Causal structure is conformal structure, and the
records note says conformal structure *survives* in the hot phase (light
cones carried by conserved charges and hydrodynamics). So the conformal
phase has horizons, and in it the problem stands. The dissolution is at
the Planck boundary, where no records can exist and there is no causal
structure at all, and it works through the correlation of the first data,
not through any later causal contact. This matters for Paper 2: the
cosmological argument needs the Planck-boundary result (records note
section 4, "no region can hold its own records"), not the electroweak one.

A second precision. The paper says "the horizon problem dissolves without
an inflaton." What dissolves is the homogeneity of the *background*. The
$10^{-5}$ anisotropies are then the Born-rule randomness of the first
records, different in different regions because the records are different.
That is the same division inflation makes (homogeneous background, quantum
fluctuations on it) with the inflaton's stretched vacuum replaced by the
first \textsc{fanout} operations. The framework should say so, because it
is the point at which the two accounts are compared and the framework's
debt (section 5) begins.

## 4. Flatness: owed, not settled [OPEN under op:comp-metric]

The flatness problem is that $\Omega-1 \propto a^{2}H^{2}$ grows in the
radiation and matter eras, so $\Omega=1$ is an unstable fixed point and the
present near-flatness requires extreme flatness early. Script part A, with
the Planck bound today and the Standard Model's entropy degrees of freedom
(no GUT, so $g_{s}$ saturates at 106.75):

| epoch | $|\Omega-1|$ had to be below |
|---|---|
| electroweak crossover, 160 GeV | $10^{-29}$ |
| 3.6 TeV matching scale | $10^{-32}$ |
| first records, $T_{P}/1000$ | $10^{-57}$ |
| Planck temperature | $10^{-63}$ |

Three honest statements. (i) The framework has no Friedmann equation yet,
so it neither has the problem nor its solution: the expansion paragraph
derives late-time exponential divergence only and says the full history
"remains to be done". (ii) The relational argument of section 2 does to
flatness what it does to homogeneity, and no more: it removes the freedom
to specify curvature on a first surface that does not pre-exist, so the
curvature is not a free initial parameter, but it does not say what the
curvature *is*. Removing a parameter's freedom is not fixing its value.
(iii) There is one framework-native hint and it cuts the other way from
inflation: the paper's own expansion mechanism, $\dot d \propto d$, is
exponential and would flatten, but it needs clocks (a proper time to
differentiate with respect to) and so cannot operate before the electroweak
crossover. The framework therefore cannot have an early inflationary phase
from its own dynamics, which is consistent with "no inflation" and leaves
flatness to be explained some other way. The paragraph's "naturally flat"
must go.

## 5. What inflation also does: the spectrum, the tensors, the monopoles

The historical motivations for inflation were horizon, flatness and
monopoles; the evidence for it is the primordial spectrum. The ledger of
what a no-inflation framework owes:

- *Monopoles.* No GUT (memory `no-grand-unification-scale`; the gauge group
  is $SU(3)\times SU(2)\times U(1)$ with $\pi_{2}$ of the broken coset
  trivial), so no 't Hooft--Polyakov monopoles are produced and nothing
  needs diluting. One clause; nothing owed.
- *The scalar spectrum.* Nearly scale-invariant, $n_{s}=0.965$, adiabatic,
  Gaussian, amplitude $2\times10^{-9}$ (Planck2020, in the library). This
  is the debt the paper names and it stands. What is new since June is a
  direction, from the September notes. In the phase where the first records
  form there are no masses and no scale; a record-forming process with no
  scale produces a spectrum with no scale. The near scale-invariance is
  then not the signature of a quasi-de-Sitter geometry but of recording in
  a conformal phase, and the tilt $n_{s}-1=-0.035$ is the first scale
  announcing itself (the approach to the crossover where clocks appear, or
  the framework's own 3.6 TeV matching scale; no computation). The
  spectrum is, in this reading, a record of conformal structure, of which
  modes locked in what order, and not of a scale-factor history, which in
  that phase is not a recorded quantity (section 7). CONJECTURE. Its
  literature neighbours, none read in this session and all VERIFY-CITE:
  Hollands and Wald 2002, "An alternative to inflation", in which modes are
  born at a fixed physical length in their ground state and the resulting
  spectrum is scale-invariant without inflation, which is close to "modes
  are born as records at the Planck grain" (gravity note, section 3), with
  the known difficulty that the amplitude is then hard to get right (the
  reply of Kofman, Linde and Mukhanov 2002); the pseudo-conformal mechanism
  (Rubakov 2009; Hinterbichler and Khoury 2012), scale invariance from a
  conformal phase with a time-dependent breaking; string-gas cosmology
  (Nayeri, Brandenberger and Vafa 2006), thermal fluctuations in a
  scale-free phase; and Penrose's conformal cyclic cosmology, which also
  puts the primordial data into conformal structure. A one-sentence caution
  learned from the parallelisability attempt (2026-09-27): "no scale,
  therefore scale-invariant" is a symmetry argument, and the standard
  calculation shows that a massless field in a conformally flat spacetime
  does *not* by itself give a flat spectrum; what gives it is the freeze-out
  at horizon crossing. In the framework the freeze-out is record formation,
  so the conjecture needs a rate at which modes lock, and that is the
  computation Paper 2 owes before this is more than a direction.
- *Tensor modes.* Inflation predicts a primordial gravitational-wave
  spectrum with amplitude $r$ and the consistency relation $n_{t}=-r/8$;
  the present bound is $r<0.036$ (BICEP/Keck 2021, VERIFY-CITE). The
  framework has no inflaton and no metric before records (`sec:no-quantised-gravity`:
  the pre-geometric layer carries amplitudes over the formation of
  relations, not over geometries), so there is nothing to produce an
  inflationary tensor spectrum. Prediction: $r$ consistent with zero at
  every sensitivity, and no $B$-mode signal satisfying the consistency
  relation. A detection by CMB-S4 or LiteBIRD of primordial $B$-modes with
  $n_{t}=-r/8$ would count against the framework's cosmology. This is the
  one place the no-inflation stance is falsifiable now, and it should be in
  the paper. CANDIDATE as a prediction, with the honesty that most
  alternatives to inflation predict the same.
- *Gaussianity.* Single-field inflation predicts $f_{\mathrm{NL}}$ of order
  the slow-roll parameters. The framework's first records are Born-rule
  outcomes on a single pre-spatial state; whether their statistics are
  Gaussian is not known. Owed.

## 6. Penrose's hypothesis is the framework's starting point [STRUCTURAL as a reading]

Penrose's long-standing objection to inflation is that the horizon and
flatness problems are special cases of a deeper one, the extraordinarily
low entropy of the initial state (the Weyl curvature hypothesis: the
gravitational degrees of freedom start unexcited), and that inflation does
not explain this but presupposes a still more special state to get going.
The framework has an answer to Penrose that inflation does not. Entropy in
the real column is records (two-columns note, 2026-09-18); gravity is the
bookkeeping of locked relations (`sec:no-quantised-gravity`); before the
first records there are no locked relations. So the initial state has zero
record entropy and zero gravitational structure *by construction*: there
is nothing to be entropic. The Weyl curvature hypothesis is not a
hypothesis here but the statement that records start at zero, and the
Second Law is their accumulation, which is the paper's arrow of time. This
is a genuine point in the framework's favour and belongs in the cosmology
paragraph in one sentence. Penrose 1979 ("Singularities and
time-asymmetry") is not in the library; VERIFY-CITE. `Penrose1994` in the
library is Shadows of the Mind and is not the right citation.

## 7. "An epoch" in a phase with no clocks [CANDIDATE]

A framework-native way to say what is wrong with the question "did
inflation happen". Inflation is a claim about the scale factor: that it
grew by $e^{60}$ or so before the hot big bang (script part C gives 70
from the Planck temperature). The gravity note (section 0) says that in the
conformal phase the conformal factor, the size, "is not a fact until clocks
appear": there is no record of the metric's scale above the electroweak
crossover, only of its causal structure. So "the universe expanded by
$e^{60}$ during the conformal phase" is a statement about the magnitude of
a quantity that has no record, and the framework declines to assign it a
truth value. This is not a trick. Inflation's evidence is the spectrum,
which *is* recorded; and the framework's reply is that what the spectrum
records is conformal structure (section 5), the one thing that phase can
record, so that "inflation happened" and "the first records locked in a
scale-free order" are two descriptions of the same record, of which only
the second is stated in quantities the phase possesses. JS's "always
infinite" should be restated in the same spirit: extent is a scale, and
before clocks it is not a fact; the initial state is not small, not
infinite, but a-spatial, one location. That is the framework's version of
$a\to0$: not a point in space but the absence of space.

## 8. Fences and pushback

- The relational dissolution is an answer to the horizon problem only if
  spacelike separation really is produced by records; that is
  `op:comp-metric`, OPEN. Until it closes, the cosmology paragraph is
  CANDIDATE throughout and should keep saying so.
- "One pre-record thermal state with one temperature" leans on the thermal
  time hypothesis for a state with no causal structure. Connes--Rovelli
  define thermal time from a state on an algebra of observables; what the
  algebra is when there are no records is not said anywhere in the
  framework. Owed to Paper 2 alongside the Newtonian limit.
- The framework's "infinite" is weaker than the paper says (section 1),
  and its "flat" is unsupported (section 4). Both are corrections the
  paper should take now, independently of whether the cosmology is
  developed further.
- The argument is a just-so story until it predicts a number. The one
  falsifiable statement (no inflationary tensors) is shared with most
  alternatives. The scalar spectrum's tilt is where a distinctive number
  could come from, and nothing here computes it.
- Nothing above retries a logged route; `invalid_routes.md` has no
  cosmology entries.

## 9. Proposed wording, labels, ledger entries, references

JS's ruling, 2026-10-07T1400: "Yes I did think that the 'Infinite,
therefore flat' was wrong because negative curvature can be infinite. So we
should remove that from the paper, 'infinite therefore flat or negative
curvature' would be better." APPLIED, uncommitted:
`scripts/patch_infinite_not_flat_2026-10-07T1400.py`, one edit: "the
universe is spatially infinite, which leaves its spatial sections flat or of
negative curvature and excludes only the closed case. Infinitude on its
own, however, does not settle flatness, which is a fine-tuning of the
Friedmann dynamics the framework has not yet derived (Open
Problem~\ref{op:comp-metric}); and flatness was in any case never
inflation's principal task." Backup kept; no build run.

v2 wording, the rest: replace the remainder of the paragraph as drafted,
unrun, re-anchored on the corrected text and anchor-checked:
`scripts/patch_inflation_paragraph_2026-10-07T1300.py`.
It (a) weakens "spatially infinite" to "unbounded by anything in the
framework"; (b) removes "naturally flat" and states that flatness is owed
under `op:comp-metric`; (c) keeps the relational answer to the horizon
problem and states it as a claim about initial data having no places to
differ on, with the "same laws" argument named as insufficient; (d) adds
the division into background (relational) and fluctuations (first
records); (e) keeps the spectrum as the hard debt; (f) adds the tensor-mode
prediction. The Penrose sentence (section 6) and the monopole clause are
left out of the patch pending the citation. JS to rule.

Proposed ledger entries:

- **CANDIDATE** The horizon problem dissolves at the first-record surface:
  the surface is produced by \textsc{fanout} from one pre-spatial thermal
  state, so its regions share a temperature because they had one source,
  not because they equilibrated or because the laws are uniform. "Same
  laws, same temperature" is valid in the framework only through this: the
  freedom of initial data to vary from place to place, which defeats the
  laws argument in standard physics, is absent because there are no places
  before records. Restates the `sec:gr-nonlocality` thesis in thermodynamic
  form; stands with `op:comp-metric`.
- *Retraction, recorded not labelled:* the spacetime section's "spatially
  infinite, and being a network without a boundary, naturally flat" and
  "infinitude settles flatness". Infinitude excludes only the closed case;
  flatness is a Friedmann fine-tuning the framework has not derived.
  Flatness is **OPEN** under `op:comp-metric`.
- **CANDIDATE** (prediction) No primordial tensor spectrum of inflationary
  form: $r$ consistent with zero, no $B$-modes obeying $n_{t}=-r/8$.
- **CONJECTURE** The primordial scalar spectrum is a record of conformal
  structure, scale-free because the recording phase has no scale, with the
  tilt as the first scale's signature. Direction only; needs the locking
  rate. Neighbours: Hollands--Wald, pseudo-conformal, string gas, CCC.
- **STRUCTURAL** (as a reading of the framework's own definitions) The
  Weyl curvature hypothesis is the statement that records start at zero.

References, batch `bib/inflation_alternatives_refs_2026-10-07T1300.bib`:
Hollands and Wald 2002; Kofman, Linde and Mukhanov 2002; Rubakov 2009;
Hinterbichler and Khoury 2012; Nayeri, Brandenberger and Vafa 2006;
BICEP/Keck 2021; Penrose 1979. Metadata verified against the arXiv API
where the batch says so; none of the texts read; all VERIFY-SUPPORT for
the one-line characterisations above. Planck2020 is in the library and
cited.

## 10. Exact stdout of `scripts/inflation_debts_at_framework_scales_2026-10-07T1200.py`

Standard cosmology reproduced for scale; nothing of the framework's own.
Approximations: $g_{s}$ stepped at the QCD and electroweak scales; the
curvature bound taken as a round $0.005$.

```
Standard-cosmology fine-tunings at the framework's scales (Planck 2018 base LCDM)
======================================================================================
A. flatness: bound on |Omega - 1| at temperature T, from |Omega_k0| < 0.005 today
   today                                    a =  1.00e+00   |Omega-1| <  5.00e-03
   recombination (0.26 eV)                  a =  9.03e-04   |Omega-1| <  1.09e-05
   BBN (1 MeV)                              a =  1.68e-10   |Omega-1| <  1.54e-18
   electron clock switches on (0.5 MeV)     a =  3.28e-10   |Omega-1| <  5.91e-18
   electroweak crossover (160 GeV)          a =  4.87e-16   |Omega-1| <  1.31e-29
   3.6 TeV matching scale                   a =  2.17e-17   |Omega-1| <  2.58e-32
   first records, T_P/1000                  a =  6.39e-30   |Omega-1| <  2.24e-57
   T_P/10                                   a =  6.39e-32   |Omega-1| <  2.24e-61
   T_P                                      a =  6.39e-33   |Omega-1| <  2.24e-63
B. horizon: flat LCDM, z_rec = 1090
   comoving particle horizon at recombination:     281 Mpc
   comoving distance to last scattering:         13865 Mpc
   angle subtended today: 1.16 deg;  disconnected patches on the sky ~ 4/theta^2 = 9744
C. e-folds inflation is asked for, from T_P to today
   (aH)_P / (aH)_0 = 1.49e+30  ->  N = ln of that = 69.5 e-folds (textbook: about 60)
======================================================================================
INFLATION DEBTS: PASS (textbook figures reproduced; see note for what the framework owes)
```


## Correction pointer, 2026-10-08

Sections 3, 5 and 7 lean on "no masses and no scale above the crossover".
Thermal masses $\propto T$ remain, so the phase has the one scale $T$ and
is scale-free only in that sense, up to $\mu_{H}$ and the running of the
couplings; the tilt remark should name the running, not the crossover. See
`knowledge/sessions/thermal_masses_crossover_correction_2026-10-08T2200.md`.
