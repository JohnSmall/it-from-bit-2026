# Session note: the Koide phase delta = 2/9 -- is there a derivation?

Date: 2026-09-11T1600. Session: Claude Code (Fable 5.1), continuing from the
migration and orphan-placement work of 2026-09-09 to 2026-09-11.

## The question

JS asked whether the masses section's "one genuine gap" -- the Koide phase
delta = 2/9 rad, matched rather than derived -- is genuine, or whether the
norm-defect account of mass (the debt-to-defect bridge, eq:debt-defect, and
the norm-defect subsection spliced into the boson-masses section on
2026-09-10) now supplies a derivation.

## What was read

`paper1/masses_section_2026-06-08.tex`: prop:koide (alpha = sqrt2 gives the
2/3 ratio independently of delta), the "matched to five significant figures"
passage and its dimension-ratio reading 2/9 = dim C / dim(O+R), the
"one genuine gap" paragraph, op:koide-delta (one closed route: the sin^4
holonomy-squared model), the bridge splice ("the identity fixes the object,
not the spectrum"), the dilution rule, op:up-quark's record that "the bare
geometry has since been scanned and does not supply the angle".
`paper1/appendices/appendix_notebook_record_2026-07-11.tex` app:nb-M: the
eighteen-comparison inventory of the sedenion triple's structural angles
(2026-07-10): twelve T1 entries identically zero, four T2 leakage angles at
exactly pi/4, two T3 ratios at exactly 1/4; zero hits on 2/9.
`knowledge/project-docs/session_summary_2026-07-10.md` section 4, the same
verdict at source. `knowledge/project-docs/mass_ratios_from_triality.md`
(2026-03-16), where the phase first appears as a fit, theta = -12.73 deg,
with "where theta comes from" marked conjectured. `knowledge/invalid_routes.md`
(five routes, none of them about the phase). The archive index entry recording
that all non-Fano associator triples have identical magnitude 2 by G2
transitivity, ruling out mass ratios from specific octonionic directions.

## What was computed

`scripts/koide_delta_fit_and_angle_scan_2026-09-11T1600.py`, seed 20260911,
no hidden state. Part 1 inverts the Z3 form exactly on the three PDG masses
and propagates the PDG bands by Monte Carlo. Part 2 is a pre-registered scan
of four families of "natural" angles against the fitted band. Exact stdout:

```
koide_delta_fit_and_angle_scan_2026-09-11T1600.py  seed=20260911
--- Part 1 [PDG 2024]: exact inversion + MC error propagation (N=200000, seed=20260911)
inputs  m_e = 0.51099895069 MeV, m_mu = 105.6583755 MeV, m_tau = 1776.93 +/- 0.09 MeV
Koide ratio from data          = 0.66666446   (2/3 = 0.66666667; deviation -2.20e-06)
M (scale)                      = 17.715838 sqrt(MeV)
alpha (fitted)                 = 1.4142089 +/- 0.0000108   (sqrt2 = 1.4142136; shift -0.0003%, -0.43 sigma)
delta (fitted)                 = 0.22222476 +/- 0.00000626 rad
2/9                            = 0.22222222 rad
  2/9 - delta_fit              = -0.00000254 rad = -0.41 sigma = -0.0011%
  relative width of the band   = 2.82e-05  (constrains ~4.6 significant figures of delta)
paper construction (alpha=sqrt2, delta=2/9, M from tau):
  m_e  predicted = 0.510983 MeV   error -0.0031%
  m_mu predicted = 105.6561 MeV   error -0.0021%
  m_tau          = 1776.93 MeV   (scale)
--- Part 1 [PDG 2022 tau, sensitivity]: exact inversion + MC error propagation (N=200000, seed=20260911)
inputs  m_e = 0.51099895069 MeV, m_mu = 105.6583755 MeV, m_tau = 1776.86 +/- 0.12 MeV
Koide ratio from data          = 0.66666051   (2/3 = 0.66666667; deviation -6.16e-06)
M (scale)                      = 17.715562 sqrt(MeV)
alpha (fitted)                 = 1.4142005 +/- 0.0000144   (sqrt2 = 1.4142136; shift -0.0009%, -0.91 sigma)
delta (fitted)                 = 0.22222963 +/- 0.00000834 rad
2/9                            = 0.22222222 rad
  2/9 - delta_fit              = -0.00000741 rad = -0.89 sigma = -0.0033%
  relative width of the band   = 3.75e-05  (constrains ~4.4 significant figures of delta)
paper construction (alpha=sqrt2, delta=2/9, M from tau):
  m_e  predicted = 0.510963 MeV   error -0.0070%
  m_mu predicted = 105.6520 MeV   error -0.0060%
  m_tau          = 1776.86 MeV   (scale)
shift of delta_fit between tau values = +0.00000487 rad (+0.78 sigma_2024)
--- Part 2: pre-registered natural-angle scan, band = delta_fit +/- 3 sigma = [0.22220599, 0.22224353] rad
2/9 rad = 12.73240 deg = 1/28.2743 turn; 2/9 of a turn would be 1.39626 rad
(a) rational multiples of pi (q<=400): 24339 candidates, 1 inside the band (chance expectation 0.58); nearest 22pi/311 = 0.222235 rad at 2 sigma
    IN BAND: 22pi/311 = 0.22223485
(a') rational multiples of pi, small denominators (q<=60): 551 candidates, 0 inside the band (chance expectation 0.01); nearest 4pi/57 = 0.220463 rad at 282 sigma
(b) acos/asin/atan of rationals (q<=100): 12178 candidates, 0 inside the band (chance expectation 0.29); nearest asin(13/59) = 0.222162 rad at 10 sigma
(c) acos/asin/atan of surds sqrt(p/q) (q<=100): 18264 candidates, 0 inside the band (chance expectation 0.44); nearest atan(sqrt(5/98)) = 0.222149 rad at 12 sigma
(d) cap Berry phases pi(1-cos(p pi/q)) (q<=200): 12232 candidates, 0 inside the band (chance expectation 0.29); nearest cap Berry phase, half-angle 23/191pi = 0.222138 rad at 14 sigma
(e) 2pi x (2/9) = 1.396263 rad, 187665 sigma from delta_fit
```

## Reading of the output

1. The data fix delta to 0.2222248 +/- 0.0000063 rad (PDG 2024; the tau
   mass sets the width). 2/9 sits 0.41 sigma below the centre. The band
   constrains about 4.6 significant figures, so the section's "matched to
   five significant figures" is defensible on PDG 2024 (the first five digits
   agree) and would be a shade generous on PDG 2022 (4.4). alpha comes out
   0.43 sigma from sqrt2. The Koide ratio itself holds in the data to 2e-6.

2. With alpha = sqrt2 and delta = 2/9 exactly, and M set by the tau mass, the
   electron and muon are reproduced to -0.003% and -0.002% (PDG 2024) or
   -0.007% and -0.006% (PDG 2022). The results ledger's "<0.006%" and the
   section's table "-0.01%" are the same fact at two roundings and two PDG
   vintages; neither is stale. The predictions and summary sections' "to about
   a tenth of a per cent" is loose by a factor of ten against the section's
   own table and is corrected in this session's patch.

3. Earlier in the session I told JS the data constrain only four significant
   figures and that the nearest rational multiple of pi was 4pi/57 at over two
   hundred sigma. The first was computed on PDG 2022 and is superseded by
   item 1. The second was wrong as stated: 22pi/311 lies inside the band at
   2 sigma. It carries no weight -- with 24,339 candidates up to denominator
   400 the chance expectation of one hit in the 6-sigma band is 0.58, and 311
   is prime -- but the honest statement is the small-denominator one: no
   rational multiple of pi with denominator up to 60 comes within 280 sigma
   (chance expectation 0.01). The inverse-trigonometric families (rationals
   and surds, denominators up to 100) and the cap Berry phases (denominators
   up to 200) have no member within 10 sigma.

4. The natural-angle scan is the substantive finding. Angles that come out of
   geometry are rational multiples of pi (discrete symmetry; the notebook M
   inventory's pi/4 is what these look like), inverse trigonometric functions
   of algebraic numbers (angles between vectors), or rational fractions of
   4 pi (holonomy on a round sphere). 2/9 is none of these within the band at
   any simple denominator. A bare rational number of radians is the signature
   of flat geometry with rational periods, not of round geometry.

## Opinion, as given to JS

The gap is genuine and the norm defect cannot close it. eq:debt-defect is a
quartic magnitude identity: it fixes sizes (existence of mass, the scale of
the debt, alpha, which is itself a norm) and has no handle on an orientation.
delta is the orientation of the Z3 triality frame against the preferred
complex structure. The bridge splice's own sentence -- "the identity fixes the
object, not the spectrum" -- is exactly right and should not be promoted.

The dimension-ratio reading 2/9 = dim C / dim(O+R) has a units problem: a
ratio of dimensions is a pure number, the natural unit of angle in symmetric
geometry is the turn, and 2/9 of a turn is 1.396 rad. The reading needs a
mechanism in which one radian is the natural unit. Until one is exhibited the
reading is "suggestive, matched rather than derived", which is what the
section says.

Correction to my own recommendation: I proposed, as the one cheap decisive
computation, the angle between the preferred C in O and the S3 triality frame
in the sedenion doubling. That computation was already done on 2026-07-10 as
notebook M's eighteen-comparison inventory, in the up-quark context, and it
returned exactly what I predicted a symmetric embedding would: pi/4, zero, 1/4,
and no 2/9. It is recorded in the paper against op:up-quark and in app:nb-M
but not against op:koide-delta and not in invalid_routes.md. This session
proposes recording it in both places rather than re-running it.

CONJECTURE (mine, direction not result): if delta is a holonomy at all, the
connection carrying it is flat along the relevant direction (the S1 fibre, a
torus), not the round Hopf connection named in op:koide-delta.

## Files changed this session (pending JS approval before commit)

- `scripts/koide_delta_fit_and_angle_scan_2026-09-11T1600.py` (new)
- `knowledge/sessions/koide_delta_gap_2026-09-11T1600.md` (this note)
- `knowledge/results_ledger.md`, `knowledge/invalid_routes.md`,
  `knowledge/open_problems.md`: dated 2026-09-11 entries appended, labels
  marked PROPOSED for JS to confirm
- `scripts/patch_koide_gap_and_parameter_count_2026-09-11T1700.py` (new):
  adds \subsection{The shape of the gap} (label sec:koide-gap) after
  op:koide-delta in the masses section, amends op:koide-delta to list the
  three closed routes, and makes the parameter-count and precision wording
  consistent across masses, headline, predictions and summary
- `notes/todo.md`: the ledger-reconciliation item updated

## Status-label proposals

See the 2026-09-11 entries in the three ledgers. In brief: split the
ESTABLISHED "delta_0 = 2/9 reproduces the charged-lepton masses" entry into
the numerical fact (ESTABLISHED) and the dimension-ratio reading (CANDIDATE,
arguably RHYME); log four closed routes for the phase in invalid_routes;
sharpen op:koide-delta (OPEN) with the band and the rational-radian
constraint.

## VERIFY-CITE

None. No new references. PDG values are literals in the script, quoted from
the PDG 2024 (and 2022 for the tau) lepton summary tables; the vintage the
paper's "1776.9" refers to is not stated in the section.

## Not done

The two-dimensional scan JS may want next -- whether 2/9 rad appears as a
holonomy of any flat connection with rational periods on the S1 fibre of the
Hopf chain -- is not attempted here; it would need the connection specified
first.
