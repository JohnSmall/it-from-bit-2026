# What the temperature in Landauer's equation does to the energy cost of FANOUT

Date: 2026-09-20T1200. Fable session, at JS's prompt: "think about the
consequences of T in the Landauer equation. How does that affect the energy
cost of FANOUT?" Companion to `complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`
(the hub) and `two_columns_shannon_thermodynamics_action_2026-09-18T1200.md`
(sections 3 and 5). Numbers from `scripts/landauer_temperature_fanout_2026-09-20T1200.py`,
exact stdout in section 9. Labels proposed.

## 0. The answer in brief

Landauer's $Q \ge k_{B}T\,\Delta S$ has the temperature of the *bath that
receives the entropy*, and the framework has no bath of its own. So the
framework fixes the entropy side of FANOUT, in nats, and the energy side is
$T$ times that, with $T$ supplied by whoever pays: the apparatus in a
laboratory, the parent's rest mass in a decay, the Unruh bath at a horizon.
Three consequences follow, one standard, one the framework's, one for
Paper 2. Standard: the energy cost of FANOUT scales with $T$ and vanishes as
$T \to 0$, while its entropy cost does not; the boundary is entropic, not
energetic, and at low temperature the price of a record is action ($\hbar$
per nat, the imaginary column's floor), not heat. The framework's: allowing
the inverse temperature to be complex, as Hawking's CTC bath requires, turns
Landauer's one equation into a two-by-two table of known relations, of which
Landauer's heat and Planck's $E = \hbar\omega$ are the two real diagonal
cells and the width and the Matsubara frequencies the two imaginary
off-diagonal cells; FANOUT is the rotation from the Planck cell to the
Landauer cell, and mass as a clock rate is Landauer read at imaginary
temperature. For Paper 2: at a horizon $T$ is not borrowed. The Unruh
relation fixes it from $\hbar$, $c$ and the acceleration, and it cancels
against the energy flux in Jacobson's derivation, which is why the energy
cost of a horizon record is not a free parameter and why $G$ enters through
the area law alone.

## 1. $T$ belongs to the payer [STRUCTURAL as standard physics; the assignment CANDIDATE]

Landauer's bound is a statement about a bath: to erase a bit into a
reservoir at temperature $T$ costs at least $k_{B}T\ln 2$ of heat delivered to
that reservoir, because the reservoir's entropy must rise by at least the
bit's. The temperature is the reservoir's, and the bound is on heat, not on
entropy: the entropy moved is $\ln 2$ whatever $T$ is. Two limits make the
point. As $T \to 0$ the heat vanishes and the entropy does not; the record
still has to go somewhere, and a bath that can take it at no energy cost
still takes it (the third law says only that you cannot reach that bath, and
finite-size corrections of the Reeb--Wolf kind say a small bath heats up as
it takes records). And FANOUT itself, a controlled copy, is logically
reversible and costs nothing in principle; what costs is the blank fragment
it writes into, whose preparation is the erasure Bennett's accounting
charges. So "the energy cost of FANOUT" is $T$ times the entropy of the
fragments used, and the framework's own quantities are the entropies: the
record (the joint fragment entropy, at most one bit), the redundancy priced
in heat (the local sum, linear in $R$), and the invisibility of the phase
(the decoherence exponent, a fidelity and not an entropy, so not a heat at
all; two-columns note, section 5). Actual apparatus pays far above the bound:
Pearson et al.'s clock is within a factor of ten of its bound and that is
unusually close.

Who supplies $T$, in the three cases the framework meets. In a laboratory
measurement the apparatus does: Pearson et al.'s cavity drive and cold
resistor, a power supply, nothing to do with the system measured. In a decay
the parent does: the energy that becomes heat is $\Delta m\,c^{2}$, the
entropy is that of the products' phase space, and an effective temperature
$Q/\Delta S$ is set by the two together; this is the one case in which the
imaginary column's energy (the clock rate that stops) becomes the real
column's heat, and energy conservation across FANOUT is the equality of the
two. At a horizon the Unruh bath does, and section 4 says why that case is
different.

## 2. The complex temperature: four cells of one equation [each cell STRUCTURAL; the table CANDIDATE]

Write Landauer as $Q = \Delta S/\beta_{c}$ and let both factors be complex:
$\beta_{c} = \beta + it/\hbar$, as $e^{-\beta H}$ and $e^{-iHt/\hbar}$ are one
operator (two-columns note, section 3), and $\Delta S$ real for a record or
imaginary for a phase. Part A evaluates the four cases.

| | real $\beta$ (a thermal bath) | imaginary $\beta = it/\hbar$ (a clock) |
|---|---|---|
| real $\Delta S$ (a record) | $k_{B}T\,\Delta S$: Landauer's heat | $-i\hbar\,\Delta S/t$: an imaginary energy, records per unit time, a width |
| imaginary $\Delta S = i\phi$ (a phase) | $i k_{B}T\phi$: a phase per thermal period, the Matsubara frequencies | $\hbar\phi/t$: Planck's $E = \hbar\omega$, real |

Each cell is standard physics. The Landauer cell needs no comment. The
Planck cell is the imaginary column's energy: a phase $\phi$ accrued in time
$t$ costs $\hbar\phi/t$, and for the electron an anti-event, $\Delta S = i\pi$,
over half a Compton period returns $m_{e}c^{2}$ to six figures (Part A); this
is the mass identification of the hub's section 4a, now read as Landauer's
equation at imaginary temperature. The width cell is a real entropy paid at
an imaginary inverse temperature: the energy is imaginary, of size $\hbar$
times the rate at which records form, which is the imaginary part of the
complex pole $m - i\Gamma/2$ of section 4d, records being the decay
channels. The Matsubara cell is a phase paid at a real temperature: $2\pi n$
per thermal period $\hbar\beta$ gives $\hbar\omega_{n} = 2\pi n k_{B}T$, the
bosonic Matsubara frequencies, and $(2n+1)\pi$ per period the fermionic
ones, one anti-event per turn of the thermal circle being the antiperiodic
boundary condition. RHYME, to be kept fenced: the minus sign of a fermion
loop is an anti-event around a closed loop.

What is the framework's here is only the claim that these are one equation
with two complex arguments, and the reading of FANOUT as the rotation
between the two real cells: pre-FANOUT the cost sits in the Planck cell, a
real energy that is a clock rate and no heat; the records form through the
width cell; post-FANOUT the cost sits in the Landauer cell, heat at the
bath's temperature. The general case, both arguments at arbitrary phase,
gives $Q$ with a real part in which the two diagonal contributions add and an
imaginary part in which the two off-diagonal ones compete, vanishing when
the phase of the cost equals the phase of the inverse temperature. That a
record is stable (no width) exactly when its cost is in phase with its
environment's complex temperature is a CONJECTURE read off the naive
formula, and the formula itself is a proposal: the mixed cells must be
derived from the Feynman--Vernon functional before any of this is more than
bookkeeping, which is what op:complex-cost asks. Do not quote the table as a
result; quote its four corners, which are.

## 3. The crossover: thermal time [STRUCTURAL; the reading CANDIDATE]

The two exchange rates are $k_{B}T$ per real nat and $\hbar/t$ per imaginary
nat, so the columns exchange at equal cost when $t = \hbar/k_{B}T$, the
thermal time. A record formed faster than the thermal time is paid in action;
one formed slower is paid in heat. This is the ordinary quantum--classical
crossover $\hbar\omega$ against $k_{B}T$, read as the crossover between the two
columns of the cost, and it says where Landauer's floor and Margolus and
Levitin's floor take over from each other: the first scales with $T$ and
vanishes as $T \to 0$, the second scales with $\hbar$ and does not. At low
temperature FANOUT costs action, not heat.

Part B gives the scale. At room temperature the thermal time is
$2.5\times10^{-14}$ s and a bit costs $0.018$ eV; in a dilution refrigerator
the thermal time is half a nanosecond and a bit costs a micro-electronvolt;
the Unruh bath at one $g$ is at $4\times10^{-20}$ K, its thermal time is six
years, and a bit costs $2\times10^{-24}$ eV. Every terrestrial record is
formed fast compared with the Unruh thermal time, so relative to the
gravitational bath all ordinary FANOUT is on the action side of the
crossover, and the energy side of horizon bookkeeping is negligible per
record. That is the physical reason Jacobson's derivation must lean on the
entropy--area law and not on any energy scale, and it is the reason Paper 2's
count-density dictionary is an entropy dictionary.

## 4. At a horizon, $T$ is not borrowed [CANDIDATE, for Paper 2]

The one case in which the framework's own constants fix the temperature is
the horizon. Unruh's relation $k_{B}T = \hbar a/2\pi c$ sets the bath's
temperature from the acceleration of the observer for whom the records
behind the horizon are inaccessible, with no laboratory and no decaying
parent involved; and in Jacobson's derivation of the Einstein equation from
$\delta Q = T\,dS$ the acceleration cancels between the boost energy flux
$\delta Q$ and the temperature, leaving $dS = \eta\,\delta A$ and hence $G$.
In the two-columns language: a horizon is a FANOUT boundary drawn by an
observer's motion, its temperature is the exchange rate at which that
observer's imaginary column (the phase accrued along the accelerated
worldline, $2\pi$ per Euclidean period) is billed as real heat, and the
cancellation of $a$ is the statement that the energy cost of a horizon record
is fixed by the entropy alone. This is the "four-constant junction" of Paper
2's abstract, $c$, $\hbar$, $G$ and $k_{B}$ billed together for one locking:
$k_{B}$ and $\hbar$ through the Unruh exchange rate, $c$ through the boost,
$G$ through the area. Nothing here derives the area law; it says which
constant enters where, and that the $T$-dependence of Landauer's cost, which
is a free parameter in the laboratory and in a decay, is the thing the Unruh
relation removes at a horizon.

## 5. The particle's own crossover [STRUCTURAL as dimensional analysis; RHYME as reading]

A particle's clock runs at $mc^{2}/\hbar$; a bath at $T$ writes records at
up to $k_{B}T/\hbar$ per nat. They match at $k_{B}T = mc^{2}$: $5.9\times10^{9}$
K for the electron, $1.2\times10^{12}$ K for the muon, $1.1\times10^{13}$ K for
the proton (Part C). These are the pair-creation thresholds: the temperature
at which a thermal bath begins to write the particle's records is the
temperature at which it begins to create the particle. Below it the
particle's cost is in the Planck cell at every temperature the bath can
offer, which is why a stable particle in a cold universe is a clock and not a
heat source; above it the bath's records outrun the clock and the particle
is a thermal excitation. Reading only; the numbers are the standard ones.

## 6. Two asides

*Negative temperature.* A population-inverted bath has $T < 0$ and pays to
accept entropy: FANOUT into it releases energy rather than costing it. This
is a sign flip of $\beta$, not the anti-event's sign flip of the weight;
$\beta \to -\beta$ inverts $e^{-\beta E}$, the anti-event multiplies by
$e^{i\pi}$. Unrelated, and worth saying so before someone conflates them.

*The width as a temperature.* In a decay, $Q = \Delta m\,c^{2}$ and
$\Delta S$ is the log of the products' phase-space volume, so an effective
$T = Q/\Delta S$ exists and is computable case by case. Whether it means
anything beyond bookkeeping is not claimed.

## 7. What changes in the v2 plan

- Item 6 (Hawking's rotation, FANOUT-boundary appendix) takes the table of
  section 2 as its frame: "Landauer's reading" becomes $Q = \Delta S/\beta_{c}$
  with the four corners named, and "the phase accrues" becomes "the cost sits
  in the Planck cell". Item 7 (mass) cites the Planck cell for the clock and
  the width cell for the pole, one clause each.
- Item 10 (op:complex-cost) gains the mixed cells as a target: derive the
  off-diagonal entries from the Feynman--Vernon functional; the stable-record
  conjecture of section 2 is its PASS/FAIL if JS wants it minted.
- Paper 2: section 4 is the draft of the four-constant paragraph. Section 3's
  numbers say the count-density dictionary is entropic.

## 8. Proposed ledger entries

- **STRUCTURAL** (standard physics) Landauer's $T$ is the receiving bath's;
  the energy cost of FANOUT is $T$ times the fragments' entropy and vanishes
  as $T \to 0$ while the entropy cost does not; the thermal time
  $\hbar/k_{B}T$ is the crossover between heat-paid and action-paid records.
- **STRUCTURAL** (arithmetic) With $\beta_{c} = \beta + it/\hbar$ and $\Delta S$
  real or imaginary, $Q = \Delta S/\beta_{c}$ has the four corners Landauer,
  Planck, width, Matsubara; the electron's anti-event over half a Compton
  period returns $m_{e}c^{2}$.
- **CANDIDATE** FANOUT as the rotation from the Planck cell to the Landauer
  cell through the width cell; mass as Landauer at imaginary temperature.
- **CANDIDATE** At a horizon $T$ is fixed by the Unruh relation and cancels
  in Jacobson's derivation: the energy cost of a horizon record is set by
  the entropy alone; the four-constant junction reads $k_{B}$ and $\hbar$
  through the exchange rate, $c$ through the boost, $G$ through the area.
- **CONJECTURE** A record is width-free when the phase of its cost equals
  the phase of the environment's inverse temperature (from the naive complex
  formula; needs the Feynman--Vernon derivation).
- **RHYME** Fermionic antiperiodicity as one anti-event per thermal loop;
  the pair-creation threshold as the particle's column crossover.
- References, verified 2026-09-20 (Opus session) against Crossref. Every
  field remembered was right; the corrections were additions only. Batched in
  `bib/landauer_temperature_refs_2026-09-20T2200.bib`: Bennett 1982, "The
  thermodynamics of computation---a review", Int. J. Theor. Phys. 21(12),
  905--940, doi 10.1007/BF02084158; Proesmans, Ehrich and Bechhoefer 2020,
  "Finite-time Landauer principle", Phys. Rev. Lett. 125, 100602, doi
  10.1103/PhysRevLett.125.100602. Already in the library and checked correct
  as they stand, so not batched: Unruh 1976 (`unruh1976notes`, Phys. Rev. D
  14(4), 870--892), Jacobson 1995 (`Jacobson1995`), Landauer 1961
  (`Landauer_1961`). In the other batches of this date: Reeb and Wolf 2014,
  Margolus and Levitin 1998. No body was read; the physics attributed to any
  of them is still this document's own.

## 9. Exact stdout of `scripts/landauer_temperature_fanout_2026-09-20T1200.py`

```
=== Part A: Q = Delta S / beta_c, beta_c = beta + i t/hbar ===
real S, real beta   (Landauer) : Q = +2.8710e-21 +0.0000e+00 i J  (+1.7919e-02 +0.0000e+00 i eV)
imag S, imag beta   (Planck)   : Q = +3.3130e-22 +0.0000e+00 i J  (+2.0678e-03 +0.0000e+00 i eV)
real S, imag beta   (a width)  : Q = +0.0000e+00 -7.3097e-23 i J  (+0.0000e+00 -4.5624e-04 i eV)
imag S, real beta   (Matsubara) : Q = +0.0000e+00 +2.6025e-20 i J  (+0.0000e+00 +1.6243e-01 i eV)
Landauer cell at 300 K: k_B T ln 2 = 1.7919e-02 eV ; Planck cell: pi hbar / t = 2.0678e-03 eV for t = 1e-12 s
electron: anti-event (Delta S = i pi) over half a Compton period t = 4.0466e-21 s gives Q = 0.510999 MeV (m_e c^2 = 0.510999 MeV)
fermionic Matsubara check: Delta S = i pi per thermal period beta hbar gives Q = pi k_B T = hbar omega_0 with omega_0 = pi k_B T / hbar

=== Part B: thermal time hbar/(k_B T) and Landauer's energy per bit ===
bath                                T (K) hbar/k_B T (s)   k_B T ln2 (eV)
room                            3.000e+02      2.546e-14        1.792e-02
liquid helium                   4.200e+00      1.819e-12        2.509e-04
dilution fridge                 1.500e-02      5.092e-10        8.960e-07
Unruh at one g                  3.977e-20      1.921e+08        2.375e-24
Unruh temperature at one g: 3.977e-20 K ; its thermal time 1.921e+08 s = 6.1 years

=== Part C: k_B T = m c^2, the temperature at which the thermal rate equals the Compton rate ===
electron  m c^2 =     0.5110 MeV ; T = 5.930e+09 K ; Compton period h/(m c^2) = 8.093e-21 s
muon      m c^2 =   105.6584 MeV ; T = 1.226e+12 K ; Compton period h/(m c^2) = 3.914e-23 s
proton    m c^2 =   938.2721 MeV ; T = 1.089e+13 K ; Compton period h/(m c^2) = 4.408e-24 s
```
