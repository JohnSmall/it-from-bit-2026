# Records and causal structure at very high temperature

Date: 2026-09-20T1400. Fable session, at JS's prompt: "think about how this
might impact the formation of records, and hence the causal structure of
spacetime, at very high temperatures." Follows
`landauer_temperature_fanout_energy_2026-09-20T1200.md` (the thermal time as
the crossover; the four corners of Landauer's equation) and
`indefinite_causal_order_fanout_2026-09-19T0900.md` (order is a record).
Numbers from `scripts/records_high_temperature_2026-09-20T1400.py`, exact
stdout in section 9. Labels proposed. Everything here is standard physics
reorganised by the framework's vocabulary; the one place it bites the paper is
section 2's sphaleron check.

## 0. The answer in brief

Temperature does two opposite things to records, and both scale with $T$.
It makes them form faster, since decoherence rates rise with $T$, so causal
order becomes definite sooner; and it makes them die faster, since the bath
scrambles any fragment whose energy gap is below $k_{B}T$, so causal order is
forgotten sooner. Causal definiteness rises with temperature and causal
memory falls with it, and the thermal time $\hbar/k_{B}T$ is both the finest
resolution of the causal structure and the length of its memory. What
survives at high $T$ are records written into degrees of freedom the bath
cannot reach: heavy modes with gaps above $k_{B}T$, and conserved charges,
whose records last until the conservation law itself melts. Three
consequences for the causal structure follow. Above the electroweak
crossover there are no masses, so in the framework there are no clocks and
no proper time: causal order exists (light cones, carried by conserved
charges and hydrodynamics) but no metric scale, a conformal phase in which
the only time is thermal time. A few orders of magnitude below the Planck temperature the thermal entropy
of a region exceeds the record capacity of its boundary, the area law,
within a few thermal lengths, and at the Planck temperature within less
than one: no region can hold its own records, and there is no causal
structure to speak of, which is the framework's reading of the initial
singularity. And at infinite temperature the complex inverse temperature is
purely imaginary, Landauer's price per bit is infinite, and only the unitary
rotation is left: the hot limit is record-free in the same way the
pre-FANOUT regime is, but with the information scrambled into the bath
rather than held in the phases, so that high-temperature order is definite
and forgotten, never indefinite.

## 1. Two rates, both proportional to $T$ [STRUCTURAL; the reading CANDIDATE]

*Definiteness.* A record forms when a fragment's state becomes correlated
with the system, and a thermal environment does this at a rate that grows
with temperature (Caldeira--Leggett: the decoherence rate of a superposition
separated by $\Delta x$ goes as $k_{B}T\,\Delta x^{2}$ times the damping). So
at high $T$ the switch's control decoheres in a fraction of a thermal time,
the indefinite-order signal of the ICO note falls to zero at once, and every
"which came first" acquires an answer. Laboratory ICO exists because the
photonic control's gap, an optical $\hbar\omega$ of order an electronvolt,
is sixty times $k_{B}T$ at room temperature; the control is cold. A bath
hotter than the control's gap kills ICO within a thermal time. That is the
thermal form of the paper's "never amplified into records while remaining
indefinite".

*Forgetting.* The same bath scrambles the fragment. A record persists only
while the fragment's two states stay distinguishable, and thermal
fluctuations mix any pair of states whose energy separation is below
$k_{B}T$ in about a thermal time; the fastest possible scrambling is bounded
by the chaos bound, a Lyapunov rate of at most $2\pi k_{B}T/\hbar$, one full
turn of the imaginary column per thermal period (Maldacena, Shenker and
Stanford, verified 2026-09-20; their abstract gives
$\lambda_{L} \le 2\pi k_{B}T/\hbar$), the bound being **conjectured**, with
a precise mathematical argument resting on plausible physical assumptions,
from analyticity of the correlator in the complex-time strip --- their word
is "conjecture", not "derive", and this sentence should not promote it --- the same $\beta_{c}$ structure as the
two-columns note. Black holes saturate it. So a causal order recorded at
temperature $T$ is forgotten after a scrambling time of order the thermal
time times the log of the entropy. Part A: at the electroweak crossover the
thermal time is $4\times10^{-27}$ s and the maximal scrambling rate
$1.5\times10^{27}$ per second.

*The distinction that matters.* "No accessible record of the order" covers
two different states. In the pre-FANOUT case the information is in the
phases, recoverable by uncomputing, and the order is indefinite: the switch
works. In the hot case the information has gone into the bath, the real
cost has been paid, and the order is definite but unknown: a classical
mixture over orders. High temperature produces the second, never the first.
The framework's earlier phrasing, "causal structure is post-FANOUT
bookkeeping", needs this qualification: the bookkeeping is done at high $T$,
faster than anywhere else, and the books are then burnt.

*Resolution and memory.* The formation time is bounded below by the thermal
time (nothing decoheres faster than the bath fluctuates) and so is the
forgetting time. So the causal structure at temperature $T$ has a temporal
resolution no finer than $\hbar/k_{B}T$ and a memory no longer than a few
scrambling times. The framework's "time is operation count" keeps counting,
at a rate that itself rises with $T$ (Margolus--Levitin per unit energy,
Lloyd's limit), but the count is not recorded: a universe with a rate and no
clock reading, in Pearson et al.'s vocabulary a clockwork with a register
that erases itself.

## 2. What can hold a record at temperature $T$ [STRUCTURAL; the check OPEN]

A fragment holds a bit stably only if flipping it costs more than the bath
supplies, $\Delta E \gg k_{B}T$; this is Landauer's own condition for bit
stability, older than his bound. So records at temperature $T$ live in the
degrees of freedom heavier than $T$, and as $T$ rises the record-carrying
modes are fewer and heavier. The graded picture of the hub's section 4b
still holds, but the plateau never persists: the rotation toward the real
column is fast and the redundancy is lost as fast as it is gained. The FANOUT
boundary requires a hierarchy, the fragment hotter than the bath in the sense
of its gap, and high temperature removes the hierarchy from below.

The exception is a record written into a conserved quantity. A bit stored
as a difference of electric charge, or of baryon number, cannot be
thermalised at any temperature, because no bath process changes the total.
These are the records that carry causal structure through a hot plasma, and
they are exactly the hydrodynamic modes: conserved densities diffuse and
propagate as sound, and their correlations are the only long-range,
long-lived structure a plasma has. So above the scale at which every
non-conserved fragment thermalises, the causal structure is hydrodynamic:
sound cones and diffusion fronts at scales above the mean free path, and no
locked relations below it. This is standard kinetic theory, and it is what
the framework's "records" reduce to in a plasma.

*The check the paper owes.* A conservation law can itself melt. In the
Standard Model baryon number plus lepton number is violated non-perturbatively
by sphaleron transitions, exponentially suppressed today and unsuppressed
above the electroweak crossover, where their rate is of order
$\alpha_{W}^{5}T$ (**attribution corrected 2026-09-20**: the unsuppression
above the transition is Kuzmin, Rubakov and Shaposhnikov 1985, but the fifth
power of $\alpha_{W}$ is not. Their abstract claims only that the rate
"exceeds the expansion rate of the universe at $T >$ (a few) $\times 10^{2}$
GeV". The fifth power is Arnold, Son and Yaffe, Phys. Rev. D 55, 6264
(1997), whose abstract says the literature estimate was
$O(\alpha_{W}^{4}T^{4})$ and that "damping effects in the plasma suppress
the rate by an extra power of $\alpha_{W}$ to give $O(\alpha_{W}^{5}T^{4})$";
the intermediate step is Arnold and McLerran 1987. Both citations are needed
here, and `arnoldsonyaffe1997rate` is in the batch). So the
$B+L$ record is erased above $10^{15}$ K while $B-L$, electric charge and
colour survive. Paper 1 says baryon-number conservation is "the same fact as
the absence of the leptoquark gates" and that the framework "gets it for
free". That statement is perturbative. If the framework's gate dictionary
reproduces the Standard Model's chiral gauge structure it must also carry the
anomaly, and then baryon number is conserved only perturbatively and the
paper should say so; if it does not carry the anomaly, it conflicts with the
Standard Model at high temperature and with every leptogenesis scenario.
Proposed as an OPEN check, op:sphaleron: PASS is an explicit statement of
where the $B+L$ anomaly sits in the dictionary (a topological transition
between vacua, not a vertex) and a one-clause correction of the "for free"
sentence; FAIL is a dictionary that forbids it, which would be a prediction
against the Standard Model and would need to be owned as such.
*Taken up 2026-09-20T2000* in `sphaleron_slocc_collective_conversion_2026-09-20T2000.md`:
the sphaleron is a collective, topological, register-number-changing
operation outside SLOCC's single-register scope; the GHZ/W split stands as
the perturbative statement; op:sphaleron is restated there with PASS/FAIL.

## 3. The clock ladder: above the electroweak crossover there is no proper time [CANDIDATE]

In the framework a mass is a clock, the rate of imaginary cost per unit
proper time, its magnitude fixed at the Yukawa vertex by the vacuum value
(hub, sections 4a and 4d). Above the electroweak crossover, $k_{B}T$ above
about $160$ GeV, the vacuum value is zero and every particle is massless.
Then no particle performs an anti-event per Compton period in any rest
frame, because none has one; the Planck cell of the Landauer table is empty
for every species; and there is no physical system whose phase advances at a
proper-time rate. Causal order still exists, carried by conserved charges and
by light cones, but there is no metric scale: the phase is conformal, and
the only time in it is the bath's, the thermal time $\hbar/k_{B}T$, which is
the modular flow of the thermal state (Connes and Rovelli's thermal-time
hypothesis, verified 2026-09-20 against Crossref 10.1088/0264-9381/11/12/007
and batched with the two-columns references; body not read, so that the
modular flow of the thermal state is what they call the thermal time is
taken on the title and not checked). So in this framework the electroweak crossover is
the birth of proper time: below it clocks exist, above it only order does.
This is the framework's own restatement of a standard fact (a massless
theory has causal structure and no scale), and its value is that it names
which of the framework's objects, order or duration, survives.

Below the crossover the clocks switch on one species at a time, heaviest
first, and each is a stable clock only once the bath has fallen below its
pair threshold $k_{B}T = mc^{2}$, since above that the bath outruns the clock
and writes the particle's records faster than the particle accrues its
phase. Part B, on the textbook radiation-era estimate: top, Higgs, $Z$ and
$W$ become cold clocks at about $10^{-11}$ s, the tau at $10^{-7}$ s, the muon
at $2\times10^{-5}$ s, and the electron at about three seconds, the
electron--positron annihilation epoch. RHYME, kept out of the paper: the
universe acquires a recordable proper time carried by a stable charged
particle at about three seconds, and before $10^{-11}$ s it has none.
Neutrinos, with thresholds near room temperature and no records to speak
of, are not clocks for anyone.

## 4. The capacity of a boundary: where records cannot fit [STRUCTURAL as arithmetic; the reading CONJECTURE]

Paper 2 reads the entropy--area law as the count of locked relations a FANOUT
boundary can hold. Thermal radiation in a region of size $R$ carries entropy
proportional to $T^{3}R^{3}$; the boundary's capacity is proportional to
$R^{2}$ in Planck units; the two cross at a size $R^{*}$ that falls as
$T^{-3}$ (Part C). At the QCD and electroweak crossovers $R^{*}$ is
astronomical, $10^{23}$ m and $10^{14}$ m, and the bound is irrelevant. At the framework's matching scale, $3.6$ TeV, it is $4\times10^{10}$ m,
still far beyond any thermal scale. The framework has no scale between that
and the Planck scale, having excluded grand unification, so the approach is
a pure power law: $R^{*}$ in thermal lengths is $(45/2\pi g_{*})(E_{P}/k_{B}T)^{2}$,
a hundred thousand thermal lengths at a thousandth of the Planck energy,
where a region that size already holds more thermal records than its
boundary can lock, and one thermal length at a quarter of it. At the Planck
temperature $R^{*}$ is less than
one thermal length: no region, not even a single thermal cell, can hold its
own records. In the framework's terms this is the temperature at which no
causal structure forms at any scale, because the records that would
constitute it exceed the capacity of every boundary that would lock them,
which is the pre-geometric layer with nothing above it. The framework's
reading of the initial singularity is then not a divergence of curvature but
the failure of records: the point at which the thermal time reaches the
Planck time and the capacity bound reaches one thermal cell together, which
happens at one and the same temperature by the definition of the Planck
scale. CONJECTURE, for Paper 2; the numbers are standard (this is the
statement that Planck-temperature radiation collapses into black holes at
every scale), and what the framework adds is only the reading.

## 5. The complex temperature at $\beta \to 0$ [CANDIDATE]

With $\beta_{c} = \beta + it/\hbar$, infinite temperature makes the inverse
temperature purely imaginary: $e^{-\beta_{c}H} \to e^{-iHt/\hbar}$, the
thermal factor is trivial, and only the unitary rotation is left. On the
Landauer table this is the Planck column: at $\beta \to 0$ the exchange rate
$k_{B}T$ per real nat is infinite, so a record costs infinite energy, and the
maximally mixed bath, invariant under every unitary, has no preferred basis
in which to write one. The FANOUT boundary needs a bath with structure,
$\beta > 0$, exactly as it needs a fragment with a gap. The hot limit is
therefore record-free in the same sense as the pre-FANOUT regime, and the
two are distinguished only by where the information sits: in the phases,
recoverable, in the one case; in the bath, paid for and gone, in the other.
The window in which causal structure exists is one-sided in temperature:
records are stable and cheap as $T \to 0$ (the branching model of notebook S
is a zero-temperature model and works), and impossible as $T \to \infty$.
What $T \to 0$ removes is not records but thermal erasure, so that indefinite
order can survive there for as long as nothing copies the control; what
$T \to \infty$ removes is records, and with them both definite and
indefinite order.

## 6. What this gives Paper 2

- The causal structure at temperature $T$ has resolution $\hbar/k_{B}T$ and
  memory of order the scrambling time; the chaos bound, one turn of the
  imaginary column per thermal period, is the fastest FANOUT rotation and
  carries the same $2\pi$ as the Unruh relation (Landauer-temperature note,
  section 4).
- Above the electroweak crossover: order without duration; a conformal
  phase; thermal time as the only time. Below: the clock ladder of section
  3.
- In a plasma the records are the conserved charges and the causal
  structure is hydrodynamic; the framework's "locked relations" are, there,
  the hydrodynamic correlations, and the mean free path is the scale below
  which the layer is pre-geometric.
- The area law as record capacity; the capacity is exceeded within $10^{5}$ thermal lengths at a thousandth
  of the Planck energy and within one thermal length at a quarter of it;
  there is no intermediate scale, grand unification being excluded;
  the singularity as the failure of records.
- A fence Paper 2 must carry: "temperature" presupposes local equilibrium
  over a region, and local equilibrium presupposes a causal patch in which
  to equilibrate; near the Planck scale the patch is one thermal cell and
  the notion of $T$ is itself failing with the records. The framework
  cannot use $T$ to describe the regime in which $T$ is undefined; section
  4 is a statement about the approach to that regime, not about it.

*Addendum 2026-09-20T1800.* Whether gravity itself fails at high temperature,
and what the Planck scale then means, is answered in
`gravity_planck_scale_high_temperature_2026-09-20T1800.md`: the equation of
state holds at every temperature the framework owns and fails only near the
Planck temperature; the Planck length is the record's grain; above the
electroweak crossover the conformal factor has no record.

## 7. Fences and pushback

- Nothing here is derived from the framework. Decoherence rates, the chaos
  bound, bit stability, hydrodynamics, the electroweak crossover, the
  Bekenstein--area comparison and the radiation-era timeline are all
  standard; the framework supplies a vocabulary in which they line up
  (order as record, duration as phase, the area law as capacity). That is
  worth having only if Paper 2 says so.
- The sphaleron check (section 2) is the one place where the framework's
  existing text is at risk, and it should be settled before v2.
- "Proper time is born at the electroweak crossover" is a reading of a
  standard fact; do not present it as a prediction. The three-second
  electron epoch is a rhyme.
- The chaos bound bounds scrambling in systems with a large number of
  degrees of freedom and a thermal state; applying it to "the forgetting of
  a causal order" is a reading.
- None of this distinguishes the framework from standard cosmology
  observationally.

## 8. Proposed ledger entries and references

- **STRUCTURAL** (standard physics) Decoherence and scrambling rates both
  scale with $T$; the thermal time bounds both the formation and the
  forgetting of a record; a fragment holds a bit only if its gap exceeds
  $k_{B}T$ or a conservation law protects it; conserved charges are the
  long-lived records of a plasma.
- **CANDIDATE** Causal definiteness rises with $T$ and causal memory falls
  with it; the causal structure at temperature $T$ has resolution
  $\hbar/k_{B}T$; high-temperature order is definite and forgotten, never
  indefinite.
- **CANDIDATE** Above the electroweak crossover the framework has no clocks
  and no proper time: order without duration, thermal time the only time.
- **CONJECTURE** The initial singularity as the failure of records: the
  temperature at which the thermal time reaches the Planck time and the
  area capacity of every region falls below one thermal cell.
- **OPEN** op:sphaleron: locate the $B+L$ anomaly in the gate dictionary or
  own its absence; correct "baryon number for free" to "perturbatively".
- **RHYME** The clock ladder's cosmic times; the fastest FANOUT rotation as
  the chaos bound's $2\pi$.
- References, verified 2026-09-20 (Opus session) against Crossref and, for
  two of them, INSPIRE-HEP. Batched in
  `bib/records_high_temperature_refs_2026-09-20T2200.bib`. **Every volume,
  issue and page remembered was right**; the corrections were additions only.
  Maldacena, Shenker and Stanford, "A bound on chaos", JHEP 08 (2016) 106,
  doi 10.1007/JHEP08(2016)106; Sekino and Susskind, "Fast scramblers", JHEP
  10 (2008) 065; Hayden and Preskill, "Black holes as mirrors", JHEP 09
  (2007) 120; Lloyd, "Ultimate physical limits to computation", Nature 406,
  1047--1054 (2000); Bekenstein 1981, "Universal upper bound on the
  entropy-to-energy ratio for bounded systems", Phys. Rev. D 23, 287--298;
  D'Onofrio and Rummukainen 2016, "Standard model cross-over on the lattice",
  Phys. Rev. D 93, 025003. Kuzmin, Rubakov and Shaposhnikov 1985 and 't Hooft
  1976 are verified and batched with the sphaleron references; Connes and
  Rovelli 1994 with the two-columns references. Kolb and Turner is added to
  the batch unverified in one field: no database confirms the ISBN of the
  1990 Addison-Wesley printing, and Crossref's record of the 2018 reissue
  drops Turner from the author list.

  Two claims were checked against the sources and both hold. D'Onofrio and
  Rummukainen's abstract gives "T_c = 159.5 +/- 1.5 GeV" and calls the
  transition "a smooth cross-over" of width about 5 GeV, so both the number
  and the word are theirs. Maldacena, Shenker and Stanford's abstract gives
  lambda_L <= 2 pi k_B T / hbar, which is this document's one turn per
  thermal period. **One word to change:** section 2 says the bound is
  "derived from analyticity". Their own wording is "We conjecture a sharp
  bound ... We give a precise mathematical argument, based on plausible
  physical assumptions, establishing this conjecture." Conjectured, with an
  argument, is the accurate description, and the framework should not lean on
  it as a theorem.

## 9. Exact stdout of `scripts/records_high_temperature_2026-09-20T1400.py` (re-run after the GUT rows were replaced)

```
=== Part A: thermal time, chaos-bound rate, Landauer per bit ===
Planck temperature 1.417e+32 K ; Planck time 5.391e-44 s ; Planck energy 1.221e+19 GeV
epoch                           k_B T hbar/k_B T (s)   2pi k_B T/hbar        k_B T ln2
QCD crossover            1.550e+08 eV      4.247e-24      1.480e+24 /s    1.074e+08 eV
electroweak crossover    1.600e+11 eV      4.114e-27      1.527e+27 /s    1.109e+11 eV
matching scale 3.6 TeV   3.600e+12 eV      1.828e-28      3.437e+28 /s    2.495e+12 eV
Planck                   1.221e+28 eV      5.391e-44      1.165e+44 /s    8.463e+27 eV
at the Planck temperature the thermal time is 1.000 Planck times

=== Part B: the clock ladder, pair thresholds and the cosmic time the bath falls below them ===
particle         m c^2 T = mc^2/k_B   t_cosmic (s)
electron  5.1100e+05 eV    5.930e+09 K      2.827e+00
muon      1.0566e+08 eV    1.226e+12 K      2.098e-05
tau       1.7769e+09 eV    2.062e+13 K      7.418e-08
W         8.0369e+10 eV    9.326e+14 K      3.626e-11
Z         9.1188e+10 eV    1.058e+15 K      2.817e-11
Higgs     1.2520e+11 eV    1.453e+15 K      1.494e-11
top       1.7257e+11 eV    2.003e+15 K      7.865e-12

=== Part C: thermal entropy against the area bound ===
S_rad(R) = (2 pi^2/45) g* (k_B T/hbar c)^3 R^3 ; S_A(R) = pi R^2/l_P^2 ; cross at R* = (45/(2 pi g*)) (hbar c/k_B T)^3 / l_P^2
QCD crossover            thermal length 1.273e-15 m ; R* = 5.299e+23 m = 4.163e+38 thermal lengths = 3.279e+58 l_P
electroweak crossover    thermal length 1.233e-18 m ; R* = 4.818e+14 m = 3.906e+32 thermal lengths = 2.981e+49 l_P
matching scale 3.6 TeV   thermal length 5.481e-20 m ; R* = 4.230e+10 m = 7.716e+29 thermal lengths = 2.617e+45 l_P
Planck                   thermal length 1.616e-35 m ; R* = 1.084e-36 m = 6.709e-02 thermal lengths = 6.709e-02 l_P
R*/lambda = (45/(2 pi g*)) (E_P/k_B T)^2 ; so R* = 1e5 lambda at k_B T = 8.191e-04 E_P and R* = lambda at k_B T = 0.259 E_P
```


## Correction pointer, 2026-10-08

Sections 0 and 3 say that above the electroweak crossover there are no
masses, no clocks and no proper time, a conformal phase. That is too strong:
thermal masses of order $gT$ remain, a quasiparticle has a proper time, and
the phase is scale-free only up to $\mu_{H}$ and the running. The vacuum
(Yukawa) masses do vanish; the correct sentence is that no particle has a
clock of its own above the crossover. The CANDIDATE ledger proposal of
section 8 on this point is withdrawn and replaced. See
`knowledge/sessions/thermal_masses_crossover_correction_2026-10-08T2200.md`.
