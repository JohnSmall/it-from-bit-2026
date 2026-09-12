# Session note: the QED-correction problem for delta = 2/9

Date: 2026-09-11T2200. Session: Claude Code (Fable 5.1), `it_from_bit_fable_5_1`.
Follows `koide_flat_direction_2026-09-11T1900.md`, whose open-problems entry
"The QED problem" (now in `open_problems.md`, flat-direction section) is the
brief. Housekeeping arising from this note -- ledger entries, the .bib batch,
any paper splice -- is left for the Opus session, per the working split JS
set on 2026-09-11.

## The question

The Koide relation holds for the measured masses to a part in 10^5, and the
framework asserts alpha = sqrt2 and delta = 2/9 exactly. The measured masses
are pole masses. Pole masses carry QED corrections that differ between
generations, so a relation exact at one place in the renormalisation-group
flow is inexact elsewhere. Which masses is the framework's relation about,
does QED spoil delta = 2/9 at the precision of the band, and is there
anything left to derive or to test?

## What was read

`koide_flat_direction_2026-09-11T1900.md` (the OPEN entry and its numbers).
The other session's `tidy_after_koide_handover_2026-09-11T2011.md` and
`bib/koide_attribution_refs_2026-09-11T2011.bib`, for the now-verified
Sumino keys (`sumino2009family`, `sumino2009origin`; not yet in
references.bib, import pending) and for Brannen. Melnikov and van Ritbergen,
hep-ph/9912391, pages 1--5, read in full for the two-loop pole/MS-bar
relation with colour factors: eq. (10) has the light-flavour coefficient
d3 = 71/96 + pi^2/12 and eq. (13) the QCD numbers 13.4434 - 1.0414 N_L. That
reading is what fixed a bookkeeping error in my first draft of the script
(below). Sumino's two papers were not read; the description of his mechanism
is from their abstracts as recalled and is marked VERIFY where it matters.

## The argument

Labels are proposals; JS applies them.

### 1. What the QED problem is, in numbers

**STRUCTURAL (computed).** The Koide parameters are not renormalisation-group
invariants. Under one-loop QED running from the pole to a common MS-bar scale
mu, mbar_k(mu) = m_k [1 - (alpha/pi)(1 + (3/4) ln(mu^2/m_k^2))], so every
mass ratio at a common scale is (m_j/m_k)^(1 + eps) with eps = 3 alpha/2 pi
= 3.48e-3, independent of mu at this order. The Koide parameters at any
common scale therefore sit at fixed distances from their pole values:
K = 2/3 + 1.15e-3 (228 sigma), alpha = sqrt2 + 2.45e-3 (227 sigma),
delta = 2/9 - 1.09e-3 rad (174 sigma), the same to three figures at
mu = m_e, m_tau, M_Z and the framework's 3.6 TeV matching scale. Conversely,
a relation exact at any common scale predicts pole masses that miss the data
by the same amounts. The relation is a relation among pole masses, or --
equivalently to one loop, since m_k = mbar_k(mbar_k)(1 + alpha/pi) with the
same factor for all three -- among the masses at their own scales. This is
Sumino's observation (2009) in our numbers.

### 2. Whose problem it is

**CANDIDATE (framework reading).** A derivation that fixes Koide as a relation
among Yukawa couplings at some scale must explain why running to the pole
preserves it to 10^-5. Sumino's answer is a U(3) family gauge symmetry whose
gauge-boson loops cancel the QED logarithm (VERIFY: from the abstracts as
recalled; the papers are verified bibliographically by the other session,
not read). A derivation that fixes a relation among physical masses has no
such problem. Charged-lepton pole masses are scheme-independent,
scale-independent, infrared-finite observables, and a relation among them
needs no scale. The framework's mass claims are of exactly this kind: one
dimensional scale M, which the tau sets, and dimensionless ratios fixed by a
scale-free geometry. Introducing an external common mu is what breaks the
covariance between generations, and the framework has no external mu to
introduce. So the framework predicts, rather than assumes, that its relation
is among pole masses; and the data agree, pole-exact at 0.4 sigma against
common-scale-exact at two hundred.

Pushback, which the paper has to answer before it uses this. The framework
also states sin^2 theta_W = 1/4 "at tree level, running to 0.231 at M_Z with
matching scale about 3.6 TeV", and y_t = 1. Those are matching-scale
statements about couplings. The paper needs one stated principle for which of
its numbers are on-shell and which are matching-scale, or a referee will ask
why the lepton relation is exempt from the running that the weak angle is
not. The principle I would propose, labelled CANDIDATE: relations among
renormalisation-group invariants (pole masses, hence mass ratios) hold as
stated; relations among scheme-dependent parameters (gauge couplings,
Yukawas) are matching conditions at the scale where the geometry is exact,
and run below it. It must then be checked against m_H = v/2 and y_t = 1,
which mix a pole mass with a coupling. Not done here.

### 3. Where the genuine question is: the two-loop fork

**STRUCTURAL (computed; d3 verified).** At two loops the pole/self-scale
ratio is generation-dependent through the lighter leptons in each lepton's
self-energy. With the MS-bar coupling of each lepton's own effective theory,
M_k/mbar_k(mbar_k) = 1 + a + a^2 [c0 - d3 N_L], N_L = 0, 1, 2 for e, mu, tau,
d3 = 71/96 + pi^2/12 = 1.5621 (Melnikov and van Ritbergen eq. 10, the QED
reading of their QCD -1.0414 N_L in eq. 13). Those three couplings are not
the same number, so a comparison between generations has to be made with the
one physical alpha(0), and the running of alpha between the light masses
then enters at the same order: per lighter lepton l the coefficient becomes
(2/3) ln(m_k/m_l) - d3, i.e. +1.99 for the muon and +4.19 for the tau, so
M_k/mbar_k(mbar_k) differs between generations by +1.08e-5 (mu) and
+2.26e-5 (tau) relative to the electron. My first draft used a common
coupling with the massless-MS-bar coefficient alone, which gets the sign
wrong and the size about right; the corrected version is what the stdout
below shows. Light-mass corrections are of order d3 (m_l/m_k) and negligible
(5e-7 at most); three-loop terms are 1e-7 relative, a thousand times below
the band.

The consequence: "exact at the pole" and "exact at self-scale MS-bar" differ
in delta by 1.4e-6 rad, 0.22 sigma of the present band. The data sit at
+0.41 sigma from the first and +0.63 sigma from the second: no preference.
Separating them at 3 sigma needs the tau mass to +/- 0.007 MeV, thirteen
times better than PDG 2024. So the QED problem for delta = 2/9 is closed at
any precision now reachable, and closed in a specific way: the claim
"delta = 2/9 at the pole" is scheme-free to about 1e-6 rad and no further.
Below that a derivation would have to say which of the two readings it
derives, which is a statement about two-loop QED that no scale-free geometry
can make. That is a ceiling on the precision of the claim, and it should be
stated as one.

**Estimate, not computed.** Electroweak corrections to the pole masses are
generation-dependent through y_l^2 (alpha_W/4 pi), about 1e-4 x 3e-3 = 3e-7
relative for the tau: an order of magnitude below the two-loop QED fork and
two below the band.

### 4. Two structural facts for the record

**STRUCTURAL.** Sensitivities at the physical point: d delta/d ln m_tau =
-0.124 rad, d delta/d ln m_mu = +0.131, d delta/d ln m_e = -0.007. The
electron, known to a part in 10^10, contributes nothing to the band on delta;
the phase is a tau-muon affair and its precision is the tau's. This is also
why the 1600 session found the band tau-limited.

**STRUCTURAL.** Ratios of differences of logarithms of the masses are exactly
invariant under the one-loop distortion m -> C m^(1+eps); the Koide
combinations are not. Any Koide-like relation selects a scheme, and only
log-ratio relations do not. The invariant ratio (ln m_tau - ln m_mu)/
(ln m_mu - ln m_e) = 0.529378 is recorded so that no one has to compute it
again; it carries no claim.

### 5. An aside on Brannen's number

The other session records Brannen's 2006 fit as delta_1 = 0.2222220(19). If
the transcription is right, his uncertainty is ten times smaller than the
tau band of the day allows (the 1900 script gives +/- 2.0e-5 rad for
1776.99 +/- 0.29 MeV), so it cannot include the tau. Whoever writes the
credit should quote his central value and not his error bar, or say what the
error bar is.

## What was computed

`scripts/koide_qed_corrections_2026-09-11T2200.py`, deterministic, no
randomness, alpha_em = 1/137.035999 at zero momentum, PDG 2024 masses as in
the 1600 script, bands sigma_delta = 6.26e-6 and sigma_alpha = 1.08e-5 from
the 1600/1900 Monte Carlo and sigma_K propagated from the tau band. Exact
stdout of the corrected script:

```
koide_qed_corrections_2026-09-11T2200.py  (deterministic; alpha_em = 1/137.035999)
pole values: K = 0.66666446, alpha = 1.4142089, delta = 0.22222476 rad; sigma_K (tau band) = 5.08e-06, sigma_alpha = 1.1e-05, sigma_delta = 6.26e-06
--- Part A: one-loop QED running of the pole masses to a common MS-bar scale mu
pole masses (data)                           K-2/3 = -2.203e-06 (   -0.4 sig)  alpha-sqrt2 = -4.674e-06 (   -0.4 sig)  delta-2/9 = +2.540e-06 rad (   +0.4 sig)
common scale, linearised, mu = m_e           K-2/3 = +1.125e-03 ( +221.4 sig)  alpha-sqrt2 = +2.384e-03 ( +220.7 sig)  delta-2/9 = -1.057e-03 rad ( -168.8 sig)
common scale, linearised, mu = m_mu          K-2/3 = +1.146e-03 ( +225.5 sig)  alpha-sqrt2 = +2.428e-03 ( +224.8 sig)  delta-2/9 = -1.076e-03 rad ( -171.9 sig)
common scale, linearised, mu = m_tau         K-2/3 = +1.157e-03 ( +227.7 sig)  alpha-sqrt2 = +2.452e-03 ( +227.1 sig)  delta-2/9 = -1.087e-03 rad ( -173.6 sig)
common scale, linearised, mu = M_Z = 91187.6 MeV K-2/3 = +1.173e-03 ( +230.9 sig)  alpha-sqrt2 = +2.487e-03 ( +230.2 sig)  delta-2/9 = -1.102e-03 rad ( -176.1 sig)
common scale, linearised, mu = 3.6 TeV (matching scale) K-2/3 = +1.189e-03 ( +234.0 sig)  alpha-sqrt2 = +2.520e-03 ( +233.3 sig)  delta-2/9 = -1.117e-03 rad ( -178.4 sig)
common scale, power-law form, mu = m_tau     K-2/3 = +1.146e-03 ( +225.6 sig)  alpha-sqrt2 = +2.429e-03 ( +224.9 sig)  delta-2/9 = -1.081e-03 rad ( -172.7 sig)
self-scale mbar_k(m_k) (universal factor)    K-2/3 = -2.203e-06 (   -0.4 sig)  alpha-sqrt2 = -4.674e-06 (   -0.4 sig)  delta-2/9 = +2.540e-06 rad (   +0.4 sig)
if exact at a common scale, pole values would be: K = 2/3 -1.159e-03, alpha = sqrt2 -2.457e-03, delta = 2/9 +1.089e-03 rad, i.e. -228, -227, +174 sigma from the data
exponent of the one-loop distortion m -> m^(1+eps): eps = 3a/2pi = 3.48423e-03
--- Part B: sensitivities d(K, alpha, delta)/d ln m_k at the physical point
  d/d ln m_tau: dK = +0.10032 (analytic p_k(p_k-K) = +0.10032)  dalpha = +0.21280  ddelta = -0.12361 rad
  d/d ln m_e  : dK = -0.00879 (analytic p_k(p_k-K) = -0.00879)  dalpha = -0.01864  ddelta = -0.00699 rad
  d/d ln m_mu : dK = -0.09153 (analytic p_k(p_k-K) = -0.09153)  dalpha = -0.19417  ddelta = +0.13060 rad
  check: sum over k of each derivative (a common rescaling changes nothing): -1.1e-10 -1.1e-10 +1.4e-11
--- Part C: two-loop pole/self-scale ratio, generation dependence through the lighter leptons
  d3 = 71/96 + pi^2/12 = 1.5621 (verified: Melnikov-van Ritbergen eq. 10); (a0/pi)^2 = 5.395e-06
  e   lighter leptons none     : two-loop coefficient +0.0000 (common alpha(0)); relative shift of m_pole/mbar(mbar) = +0.000e+00   [MS-bar coupling at own scale: -0.0000, -0.000e+00]
  mu  lighter leptons e        : two-loop coefficient +1.9923 (common alpha(0)); relative shift of m_pole/mbar(mbar) = +1.075e-05   [MS-bar coupling at own scale: -1.5621, -8.428e-06]
  tau lighter leptons e,mu     : two-loop coefficient +4.1935 (common alpha(0)); relative shift of m_pole/mbar(mbar) = +2.263e-05   [MS-bar coupling at own scale: -3.1241, -1.686e-05]
  light-mass corrections ~ d3 (m_l/m_k) (a0/pi)^2: mu 4.1e-08, tau 5.0e-07  -- negligible
  exact at self-scale  =>  at the pole: K = 2/3 +1.286e-06 (+0.25 sig), alpha = sqrt2 +2.728e-06 (+0.25 sig), delta = 2/9 -1.393e-06 rad (-0.22 sig)
  data minus each hypothesis, delta: pole-exact +0.41 sig, self-scale-exact +0.63 sig; alpha: -0.43 sig, -0.69 sig
  to separate the two readings at 3 sigma in delta the band must shrink to 4.64e-07 rad, i.e. m_tau to +/- 0.007 MeV (now +/- 0.09)
  three-loop n_l terms: (a/pi)^3 x O(10) = 1e-07 relative -- below the band by 10^3
--- Part D: combinations exactly invariant under m -> C m^(1+eps)
  (ln m_tau - ln m_mu)/(ln m_mu - ln m_e) = 0.529378; invariant under the one-loop running, unlike K, alpha, delta
  under the two-loop n_l shifts it moves by +1.2e-06 (relative +2.2e-06)
done.
```

## Reading of the output

1. Part A: the common-scale shifts are the same to three figures at every
   mu, as the algebra says; the linearised and power-law forms agree to 1%
   of the shift (an O(alpha^2) difference). Self-scale masses return the pole
   values exactly. Common-scale exactness is excluded at 170 to 230 sigma
   on each of K, alpha, delta.
2. Part B: the finite-difference sensitivities match the analytic
   p_k(p_k - K) for K, and sum to zero across generations to 1e-10, as they
   must under a common rescaling.
3. Part C: with the physical alpha(0), the generation-dependent two-loop
   coefficients are +1.99 (mu) and +4.19 (tau); the bracketed MS-bar-coupling
   numbers are the uncorrected bookkeeping, kept to show that the sign, not
   the size, was at stake. The fork in delta is -1.39e-6 rad; data prefer
   neither reading.
4. Part D: the log-ratio invariant moves by 2e-6 relative under the two-loop
   shifts, i.e. it is invariant to one loop only, as stated.

## Opinion

The QED problem is real for Yukawa-level explanations of Koide and is not a
problem for a relation among physical masses; the framework is the second
kind of theory and should say so, with the one principle above that also
covers its coupling relations. Quantitatively the question is closed: the
scheme ambiguity that survives the on-shell reading is 1e-6 rad, a fifth of
the band, and unreachable by a factor of thirteen in the tau mass. What the
computation adds that the argument alone does not is the ceiling: delta = 2/9
is a claim about pole masses that is meaningful to about 1e-6 rad and not
beyond. The open problem op:koide-delta should carry that ceiling in its
PASS criterion, and the "QED problem" entry of the 1900 session should be
recorded as resolved by quantification rather than left open.

## Proposed paper text (for the Opus session to splice; wording JS's)

A paragraph for sec:koide-gap, after "What kind of number it must be":

> Which masses. The relation is among pole masses. Under one-loop QED
> running to any common scale $\mu$, every mass ratio acquires the factor
> $(m_j/m_k)^{3\alpha/2\pi}$, independent of $\mu$, and the parameters move
> to $K = 2/3 + 1.2\times10^{-3}$, $\alpha = \sqrt2 + 2.5\times10^{-3}$ and
> $\delta = 2/9 - 1.1\times10^{-3}$, each more than a hundred and seventy
> standard deviations from the data. A relation imposed on Yukawa couplings
> at the matching scale would therefore fail at the pole unless something
> cancels the logarithm, which is the problem Sumino's family gauge symmetry
> was built to solve \autocite{sumino2009family,sumino2009origin}. A
> relation among pole masses has no such problem: they are scheme-independent
> observables, and a framework with one dimensional scale and ratios fixed by
> a scale-free geometry can only be making a statement about them. To one
> loop the same relation holds for the masses at their own scales,
> $\bar m_k(\bar m_k)$, since $m_k/\bar m_k(\bar m_k) = 1 + \alpha/\pi$ is
> the same for all three. The two readings part only at two loops, through
> the lighter leptons in each lepton's self-energy: with the physical
> $\alpha$, $m_k/\bar m_k(\bar m_k)$ differs between generations by
> $(\alpha/\pi)^2\sum_{l<k}\bigl[\tfrac23\ln(m_k/m_l) - \tfrac{71}{96} -
> \tfrac{\pi^2}{12}\bigr]$ \autocite{melnikovvanritbergen2000threeloop},
> which moves $\delta$ by $1.4\times10^{-6}$ radians, a fifth of the present
> band. The claim $\delta = 2/9$ is thus free of scheme to about $10^{-6}$
> radians and no further; separating the two readings would need the tau
> mass to $\pm0.007$ MeV.

It uses two Sumino keys the other session has batched but not yet imported,
and one new key, below.

## Proposed ledger entries

### results_ledger.md, dated 2026-09-11 (QED session)

- **STRUCTURAL** The Koide parameters are not RG invariants. One-loop QED
  running to any common MS-bar scale multiplies every mass ratio by
  (m_j/m_k)^(3 alpha/2 pi), mu-independent, and moves (K, alpha, delta) by
  (+1.15e-3, +2.45e-3, -1.09e-3 rad): 228, 227 and 174 sigma from the data.
  The relation holds among pole masses, equivalently (to one loop) among the
  masses at their own scales, and nowhere else. Script
  koide_qed_corrections_2026-09-11T2200.py.
- **STRUCTURAL** The two readings "exact at the pole" and "exact at
  self-scale MS-bar" differ only at two loops, through the lighter leptons:
  with the physical alpha(0) the relative shift of m_k/mbar_k(mbar_k) is
  (alpha/pi)^2 sum_{l<k} [(2/3) ln(m_k/m_l) - 71/96 - pi^2/12], i.e.
  +1.08e-5 (mu), +2.26e-5 (tau), moving delta by 1.4e-6 rad = 0.22 sigma
  (coefficient d3 = 71/96 + pi^2/12 verified against Melnikov and van
  Ritbergen 2000, eq. 10). Data prefer neither (0.41 vs 0.63 sigma).
  Separation at 3 sigma needs m_tau to +/- 0.007 MeV. The claim delta = 2/9
  is scheme-free to about 1e-6 rad and no further.
- **STRUCTURAL** d delta/d ln m = -0.124 (tau), +0.131 (mu), -0.007 (e) rad:
  the band on delta is the tau's alone. Ratios of log-differences of the
  masses are the only combinations invariant under one-loop running; the
  Koide combinations select a scheme.
- **CANDIDATE** Framework reading: relations among RG invariants (pole
  masses, mass ratios) hold as stated, relations among scheme-dependent
  parameters (gauge couplings, Yukawas) are matching conditions at the scale
  where the geometry is exact. Makes the on-shell Koide relation a
  prediction rather than an assumption and the QED problem a problem for
  Yukawa-level models only. To be checked against m_H = v/2 and y_t = 1.

### invalid_routes.md, dated 2026-09-11 (QED session)

- Koide, alpha = sqrt2 or delta = 2/9 as a relation among running masses at
  a common scale, in particular Yukawa couplings at the 3.6 TeV matching
  scale: excluded at 170 to 230 sigma by the one-loop QED logarithm alone,
  at any common scale. A derivation whose output is a Yukawa relation at a
  scale must supply a cancellation of the logarithm (Sumino's family gauge
  symmetry is the existing proposal) before it is checked against the band.

### open_problems.md, dated 2026-09-11 (QED session)

- The "QED problem" OPEN entry of the flat-direction section is resolved by
  quantification: the generation-dependent QED correction that survives the
  on-shell reading is 1.4e-6 rad in delta, a fifth of the band, and
  unreachable by a factor of thirteen in the tau mass. Proposed: record as
  resolved, and add to op:koide-delta's PASS criterion the ceiling "a
  derivation is compared with the band and not below 1e-6 rad, where the
  pole and self-scale readings part". Recorded, not labelled: a resolution
  is not a claim.
- **OPEN** op:koide-delta, frozen by JS on 2026-09-11 as it now stands in
  the paper (patch T2300): two targets, the phase 3 delta = 2/3 with PASS
  band delta = 0.222225 +/- 0.000006 rad, and the amplitude alpha = 2 rho =
  sqrt2 with PASS band alpha = 1.414209 +/- 0.000011, both with no fitted
  input; comparison with the band and not below 1e-6 rad; FAIL for any
  algebraic e^{i delta} and for any relation among running masses at a
  common scale; nine routes closed (sin^4 model; notebook M angles; single
  octonionic direction; norm-defect identity; natural-angle families;
  compact flat torus; algebraic e^{i delta}; coherent-state model;
  common-scale relation). Supersedes the two earlier op:koide-delta entries
  of 2026-09-11. Not to be worked on further without a new mechanism; the
  paper says it does not expect to close it.
- **OPEN** Which of the framework's numbers are on-shell and which are
  matching-scale. PASS: one stated principle that assigns every headline
  number (Koide alpha and delta; sin^2 theta_W = 1/4; y_t = 1; m_H = v/2;
  the sector scales) to one of the two classes and is consistent with the
  quoted agreement of each. FAIL: any number that needs a class of its own.

## VERIFY-CITE and references to add

- `melnikovvanritbergen2000threeloop`: K. Melnikov and T. van Ritbergen,
  "The three-loop relation between the MS-bar and the pole quark masses",
  arXiv:hep-ph/9912391 (identifier and content verified: the PDF was read,
  pages 1--5). Journal: Physics Letters B 482 (2000) 99--108, from memory,
  VERIFY against Crossref before the .bib batch is written. Supports d3 and
  the colour-factor form used in Part C.
- Gray, Broadhurst, Grafe and Schilcher 1990, Z. Phys. C 48, 673, the
  original two-loop result quoted by Melnikov and van Ritbergen as their
  ref. [6] and by a search summary; not read; optional.
- `sumino2009family`, `sumino2009origin`: verified by the other session;
  import pending. My one-sentence description of the mechanism (U(3) family
  gauge bosons cancelling the QED logarithm) is from the abstracts as
  recalled: VERIFY before the paper says it.
- The electroweak estimate in section 3 is an order of magnitude, not a
  computation, and is labelled so.

## JS's decision, and the write-up (2026-09-11, late)

JS: freeze op:koide-delta with the ceiling and the alpha target and move on;
open problems are to be collected as the work progresses, as things for
people to work on; write it up so it appears in paper1. Done as
`scripts/patch_koide_freeze_2026-09-11T2300.py` on
`paper1/masses_section_2026-06-08.tex` (backup `.2026-09-11T2300.bak`):

- the "one genuine gap" paragraph now says the gap has two parts of
  different standing, alpha = sqrt2 identified (doubling norm; pairwise
  unbiased states) and delta = 2/9 matched, and that the paper does not
  expect to close the problem;
- op:koide-delta is retitled "The Koide phase and amplitude" and frozen:
  invariant targets 3 delta = 2/3 and alpha = 2 rho = sqrt2, PASS bands for
  both (delta = 0.222225 +/- 0.000006 rad; alpha = 1.414209 +/- 0.000011),
  the comparison made with the band and not below 1e-6 rad, FAIL clauses
  for algebraic e^{i delta} and for common-scale relations, nine closed
  routes, and what survives;
- the summary paragraph and the header comment no longer say "from the Hopf
  holonomy";
- sec:koide-gap gains the "Which masses" paragraph drafted above, citing
  sumino2009family, sumino2009origin and melnikovvanritbergen2000threeloop.

`bib/koide_qed_refs_2026-09-11T2300.bib` (new, one entry, verified against
Crossref and the arXiv PDF) carries the Melnikov and van Ritbergen key. The
Sumino keys are in the other session's batch of T2011. Neither batch is
imported yet, so the paper does not build cleanly until both are and
references.bib is re-exported; no build was run. The re-flow of the summary
paragraph after its edit was not done (one short line, no effect on output).

## Files changed this session

- `scripts/koide_qed_corrections_2026-09-11T2200.py` (new)
- `knowledge/sessions/koide_qed_corrections_2026-09-11T2200.md` (this note)
- `scripts/patch_koide_freeze_2026-09-11T2300.py` (new), applied to
  `paper1/masses_section_2026-06-08.tex`
- `bib/koide_qed_refs_2026-09-11T2300.bib` (new)

No ledger was touched; the proposals above are for the Opus session to
apply.

Build, 2026-09-12, after JS re-exported both collections (a first export had
written the paper 2 collection over paper1/references.bib; the local Zotero
API and Better BibTeX's pull export located the fault, and a fresh pull of
each collection is byte-identical to the re-exported file): paper1 has 205
entries, the 201 committed plus brannen2006lepton, sumino2009family,
sumino2009origin and melnikovvanritbergen2000threeloop, once each, the
Melnikov title as plain "MS-bar"; paper2 back to 19. `latexmk paper1/main.tex`
exit 0, no `^!` lines, zero undefined citations, all three new entries in
main.bbl, no biber warnings; one undefined reference remains,
`sec:sedenions-mixing`, the one the other session left for JS to place. The
frozen open problem renders as "Open Problem 22 (The Koide phase and
amplitude)" and the "Which masses" paragraph as the close of sec:koide-gap.
Uncommitted.

Brannen credit, 2026-09-12T1330. JS noted brannen2006lepton was in the bib
and uncited. I read the note in full (brannenworks.com/MASSES2.pdf, six
pages) before writing the credit, and it carries more than the other session
recorded: Sections IV--V build the circulant from three Pauli-algebra
projectors, read T = sqrt((1 + cos theta)/2) as their overlap and phi as
"half the (oriented) area of the spherical triangle" (the Pancharatnam
phase), set T = sqrt(1/2) and phi = 3 delta to recover the mass formula,
and footnote 4 states that in the Pauli algebra T = sqrt(1/2) forces
phi = +/- pi/4, incompatible with the data, so a larger algebra is needed.
That is the complex half of the Gram/Bargmann reading of sec:koide-gap, and
the bound |Phi| <= pi/4 of prop:koide-jordan is the general form of his
footnote; the paper now says so.
`scripts/patch_koide_brannen_credit_2026-09-12T1330.py` (backup
`.2026-09-12T1330.bak`) cites him at the delta = 2/9 sentence (circulant
form, eta^2 = 1/2, the fit delta = 0.2222220, the 2/9 observation) and at
the end of the reading paragraph. His eq. (14) uncertainty on delta_1
excludes the tau, as suspected: his eq. (18) shows the number comes from the
electron and muon with the Koide relation assumed exact. Not built (JS's
rule: builds on his OK). The other session's todo item on crediting the
phase is thereby done except for JS's judgement on how much credit to give.

## Not done

- The electroweak generation-dependent corrections: estimated, not computed.
- The check of the on-shell/matching-scale principle against m_H = v/2 and
  y_t = 1.
- Sumino's papers: not read.
- The .bib batch for Melnikov and van Ritbergen (and optionally Gray et al.):
  left for the other session, with the VERIFY above.
