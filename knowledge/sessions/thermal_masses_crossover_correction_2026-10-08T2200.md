# Correction: "no masses and no proper time above the electroweak crossover" (2026-10-08T2200)

Session 2026-10-08, Fable 5.1. JS, on a sentence I reused today from the
records note of 2026-09-20: "'above the electroweak crossover there are no
masses and no proper time', that sounds suspicious, is that generally
accepted or something we've just invented? Is it the case that above the
electroweak crossover the rest mass of a particle is smaller than the mass
equivalents of the energies of interaction at that scale. The mass is
still there, but small compared to the interaction energy?"

Short answer: partly standard, partly invented, and the invented part is
wrong as stated. Script
`scripts/thermal_masses_above_crossover_2026-10-08T2200.py` (textbook
leading-order formulas, no randomness), stdout in section 5; references in
section 6, Crossref-verified, texts not read.

## 0. The answer in brief

Three separate statements were run together on 2026-09-20.

1. *The Higgs-generated masses vanish above the crossover.* Standard, in
   the mean-field picture (Kirzhnits--Linde 1972, Weinberg 1974,
   Dolan--Jackiw 1974): the thermal effective potential restores the
   symmetry, $v(T)\to0$, and with it every Yukawa mass and the $W$, $Z$
   masses. The lattice settled that for the physical Higgs mass this is a
   smooth crossover, not a transition, at $T_{c}=159.5\pm1.5$ GeV (Kajantie,
   Laine, Rummukainen and Shaposhnikov 1996; D'Onofrio and Rummukainen
   2016). So, against JS's alternative: the Yukawa mass is not "still there
   but small"; it goes to zero with $v(T)$, smoothly (script part A: the top
   from 173 GeV to 14 GeV at $T=159$ GeV to zero at $T_{c}$). One
   gauge-invariance caveat: by Elitzur's theorem, which the paper already
   invokes in the superconductor section, $v$ is not an order parameter,
   and the gauge-invariant $\langle\phi^{\dagger}\phi\rangle$ is continuous and
   non-zero at all $T$; "the condensate melts" is the perturbative way of
   speaking about a crossover in which nothing is discontinuous.
2. *There are no masses above the crossover.* Not standard, and false.
   Every particle in the plasma acquires a thermal mass of order $gT$ from
   its interactions: for a quark $m_{q}^{2}=(g_{s}^{2}/6)T^{2}$, for a
   left-handed lepton $(3g^{2}+g'^{2})T^{2}/32$, Debye masses
   $(11/6)g^{2}T^{2}$ and $(11/6)g'^{2}T^{2}$ for the gauge fields, and
   $m_{H}^{2}(T)=c_{H}T^{2}-\mu_{H}^{2}$ for the Higgs (Carrington 1992;
   Arnold--Espinosa 1993; the coefficients are from memory and
   VERIFY-SUPPORT). Script part B: these are $0.2$ to $0.9$ times $T$, so
   a quark at $T=1$ TeV carries a plasma mass near $500$ GeV. Here JS's
   instinct is right and the records note wrong, with a twist: the mass
   that is "still there" is not the rest mass made small but a new mass
   comparable to $T$, and it is not a Lorentz-invariant rest mass at all
   but a quasiparticle mass in the plasma frame.
3. *No clocks, no proper time, a conformal phase.* Invented, on
   2026-09-20, and too strong. What is true: all the thermal masses are
   proportional to $T$, so no particle owns a clock, every rate is the
   bath's rate times a coupling, and the phase is scale-free up to the
   fixed scales that survive: $\Lambda_{\mathrm{QCD}}$ (negligible, $10^{-3}T$ at
   the crossover), the Higgs mass parameter $\mu_{H}=88$ GeV (not
   negligible until $T\gg1$ TeV: $0.55T$ at the crossover, $0.025T$ at the
   framework's 3.6 TeV), and the logarithmic running of the couplings, the
   trace anomaly, which breaks scale invariance in every phase. A
   quasiparticle of mass $gT$ has a timelike worldline and a proper time
   along it; what it lacks is a proper time of its own, since its clock
   rate is set by the bath. The defensible sentence is: *above the
   crossover no particle has a clock of its own; every clock is the bath's,
   with rate proportional to $T$; the phase is scale-free in the limit
   $T\gg\mu_{H}$, broken by the running and by $\mu_{H}$.* "No proper time"
   must go; "no Yukawa clock" and "no clock of its own" may stay.

## 1. What JS asked, answered directly

"Is the rest mass still there, but small compared to the interaction
energy?" Two different masses are in play. The vacuum (Yukawa) mass is not
still there: it vanishes with the condensate, smoothly, at the crossover.
The thermal mass is there, is of order $gT$, is comparable to the
interaction energy rather than small compared with it, and is a property
of the particle in the bath, not of the particle. The fixed scales that
are "still there but small" are $\Lambda_{\mathrm{QCD}}$ and $\mu_{H}$, and
$\mu_{H}$ is small only well above a TeV. So the records note's picture
survives as "the particle's own clock is gone and the bath's clock
replaces it", which is in fact closer to the note's own thesis that $T$
belongs to the payer (Landauer note, 2026-09-20) than the sentence it
wrote.

## 2. What changes in the framework's statements

- Records note (2026-09-20T1400), section 0 and section 3 ("no masses, so
  no clocks and no proper time: a conformal phase"; "the electroweak
  crossover is the birth of proper time"): superseded by the sentence in
  item 3 above. The clock ladder of section 3 (pair thresholds, cold
  clocks switching on heaviest first) stands: it is about when the
  zero-temperature Compton clock outruns the bath, and part D of the script
  gives the ratio $mc^{2}/k_{B}T$. The proposed CANDIDATE ledger entry in
  its section 8 ("no clocks above the crossover") is withdrawn and
  replaced by the one in section 4 below. Not yet in any ledger, so no
  retraction entry is needed; the note gets a dated correction pointer.
- Gravity note (2026-09-20T1800), section 0: "above the electroweak
  crossover there are no masses, hence no clocks and no rulers, and a
  conformal phase has no record of the metric's scale, only of its causal
  structure; so gravity splits there". The split survives in weakened
  form: the record of the metric's scale above the crossover is the bath's
  ($T$ itself, through the thermal masses), not any particle's, so the
  conformal factor is recorded only relative to the thermal scale, and is
  a fact to the extent $T$ is. "No record of the scale" becomes "no record
  of the scale except $T$". The Planck-grain conclusions do not depend on
  this.
- Inflation note (2026-10-07T1200), sections 3, 5 and 7: "in the phase
  where the first records form there are no masses and no scale; a
  record-forming process with no scale produces a spectrum with no scale".
  The direction survives with the correction already built into its
  caution: the phase has the one scale $T$, and the spectrum would be
  scale-free in the sense that every rate is $\propto T$, broken by the
  running and by $\mu_{H}$ near the crossover. The tilt remark ("the first
  scale announcing itself") should name the running of the couplings as
  the candidate, not the crossover, since the modes of interest leave the
  horizon far above it. Section 7's "the conformal factor is not a fact
  until clocks appear" becomes "is a fact only relative to $T$ until the
  Yukawa clocks appear".
- Twistor note (2026-10-07T1600), section 11, the sentence I reused today
  ("no masses, so no clocks and no proper time"): corrected by pointer; the
  argument there needs only "no relation, no Yukawa mass, null", which
  stands.
- v2 plan line "no proper time above the crossover" (Paper 2 pointer):
  reword to "no particle-owned clock above the crossover".

## 3. What does not change

The two-column reading of mass (rate of imaginary cost per unit proper
time, fixed at the Yukawa vertex by the vacuum value) is untouched: it is
a statement about the vacuum mass, and the vacuum mass does vanish above
the crossover. What the correction adds is that the bath supplies a
second kind of mass, $\propto T$, which the framework should read as the
bath writing the particle's records at its own rate (the records note's
section 1 already has decoherence rates $\propto T$), so that the thermal
mass is the real-column counterpart of the Yukawa mass's imaginary-column
clock. That is a CANDIDATE reading and is the one thing in this correction
that is the framework's own: the Yukawa mass is the particle's phase
clock, the thermal mass is the bath's record clock, and above the crossover
only the second remains.

## 4. Proposed ledger entry (replacing the withdrawn one)

- **CANDIDATE** Above the electroweak crossover the vacuum (Yukawa) masses
  vanish with the condensate and every particle carries a thermal mass
  $\propto T$: no particle has a clock of its own, every clock is the bath's,
  and the phase is scale-free in the limit $T\gg\mu_{H}$ up to the running
  of the couplings. The framework reads the Yukawa mass as the particle's
  phase clock and the thermal mass as the bath's record clock. Supersedes
  the 2026-09-20 proposal "no clocks and no proper time above the
  crossover", which was wrong: a quasiparticle of mass $gT$ has a proper
  time, and the phase is not conformal.
- STRUCTURAL (textbook): symmetry restoration, the crossover at $159.5$
  GeV, thermal masses of order $gT$. VERIFY-SUPPORT for the coefficients.

## 5. Exact stdout of `scripts/thermal_masses_above_crossover_2026-10-08T2200.py`

```
Thermal masses above the electroweak crossover (textbook leading order, approximate inputs)
============================================================================================
A. mean-field: c_H = 0.397, T_c(mean field) = 140 GeV (lattice crossover 159.5 GeV)
   T =  100 GeV: v(T) =  191.6 GeV, m_top(T) =  134.2 GeV, m_e(T) = 0.3984 MeV  (Yukawa masses vanish at T_c)
   T =  140 GeV: v(T) =  117.9 GeV, m_top(T) =   82.5 GeV, m_e(T) = 0.2450 MeV  (Yukawa masses vanish at T_c)
   T =  155 GeV: v(T) =   58.0 GeV, m_top(T) =   40.6 GeV, m_e(T) = 0.1206 MeV  (Yukawa masses vanish at T_c)
   T =  159 GeV: v(T) =   19.5 GeV, m_top(T) =   13.6 GeV, m_e(T) = 0.0405 MeV  (Yukawa masses vanish at T_c)
B. thermal masses above the crossover, as fractions of T (all proportional to T):
   quark (QCD)  m_q/T = 0.498;  lepton (EW)  m_l/T = 0.209;  SU(2) Debye  m_D/T = 0.883;  U(1) Debye  0.483;  Higgs  sqrt(c_H) = 0.630
   so a quark at T = 1 TeV carries a plasma mass of about 498 GeV: not small compared with T
C. fixed scales that survive, as fractions of T:
   T =   160 GeV: Lambda_QCD/T = 1.3e-03   mu_H/T = 0.552   (thermal masses / T are T-independent)
   T =  1000 GeV: Lambda_QCD/T = 2.0e-04   mu_H/T = 0.088   (thermal masses / T are T-independent)
   T =  3600 GeV: Lambda_QCD/T = 5.6e-05   mu_H/T = 0.025   (thermal masses / T are T-independent)
   T = 10000 GeV: Lambda_QCD/T = 2.0e-05   mu_H/T = 0.009   (thermal masses / T are T-independent)
D. the particle's own clock against the bath's: m c^2 / k_B T (zero-temperature masses, below the crossover only)
   electron  at T = 1, 10, 100 GeV: 5.1e-04  5.1e-05  5.1e-06
   W         at T = 1, 10, 100 GeV: 8.0e+01  8.0e+00  8.0e-01
   top       at T = 1, 10, 100 GeV: 1.7e+02  1.7e+01  1.7e+00
============================================================================================
THERMAL MASSES: PASS (arithmetic reproduced; see the note for what the framework must change)
```

## 6. References

Batch `bib/finite_temperature_refs_2026-10-08T2300.bib`: Kirzhnits and
Linde 1972; Weinberg 1974; Dolan and Jackiw 1974; Carrington 1992; Arnold
and Espinosa 1993; Kajantie, Laine, Rummukainen and Shaposhnikov 1996;
D'Onofrio and Rummukainen 2016. Metadata Crossref-verified 2026-10-08;
none read; VERIFY-SUPPORT throughout, the coefficients in section 0 item 2
in particular. A textbook (Kapusta and Gale, *Finite-Temperature Field
Theory*) is the place to check them and is not batched.
