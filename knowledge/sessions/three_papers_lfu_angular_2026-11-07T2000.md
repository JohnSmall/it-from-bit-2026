# Three papers: the angular tests of lepton universality, the universal C_9 deficit, and a fit that puts new physics on one generation

Fable session, 2026-11-07, late evening. JS: "These three recent papers are
interesting https://arxiv.org/abs/2512.18053 , https://arxiv.org/abs/2510.17742 ,
https://arxiv.org/abs/2502.10291". Follows the same day's
`b_anomaly_lepton_universality_2026-11-07T1900.md`, whose section 3 quotes
the framework's propositions and is not repeated here.

Script: `scripts/three_papers_lfu_angular_2026-11-07T2000.py`, seed 20261107,
27/27 checks, final line `THREE PAPERS LFU ANGULAR: PASS`; exact stdout in
section 10. Bibliography batch: `bib/three_papers_lfu_refs_2026-11-07T2010.bib`,
13 keys, 12 Crossref-verified by DOI, no VERIFY-CITE.

## 0. The answer in five lines

1. The LHCb electron-mode angular analysis is the cleanest universality
   test yet: eight Q_i observables consistent with zero (chi^2 6.6/8, p =
   0.58, correlations neglected), Delta C_9 within one sigma of zero. The
   framework predicts exactly this, with the lepton-mass term as its only
   non-zero contribution. CANDIDATE prediction, passed; the SM passes too.
2. The same electron data prefer the same C_9 shift of about -1 as the
   muons, at above 2 sigma on their own, and the full-dataset muon letter
   puts the shift at 3.6 to 4.1 sigma. The deficit is lepton-universal, as
   the framework requires of any deviation; but the framework can only call
   it long-distance Standard Model physics, and LHCb's data-driven analyses
   say the nonlocal part does not absorb it. This is now the framework's
   most exposed point in flavour physics. OPEN.
3. Mir, Alda and Peñaranda assume what prop:fcnc denies: a rank-one
   projector on the generation label. Their own fit drives lepton mixing
   to zero, leaving a tau-only, aligned pattern driven by R_D(*) and
   B -> K nu nubar, which the framework predicts at the SM (3.6 sigma
   against it on the four headline inputs, with the HFLAV correlation).
4. New structural point: S_3-equivariance alone would not forbid that
   pattern. The commutant of S_3 on the label space is span{1, J}, and the
   democratic term J is diagonal in the Koide mass basis, on the tau alone.
   The framework's prohibition is the stronger trivial action of the
   identity component on pi_0, and R_D(*) and B -> K nu nubar test exactly
   that. STRUCTURAL as mathematics, CONJECTURE as a reading.
5. Five findings for ruling in section 6; nothing patched, built or
   committed.

## 1. The three papers

### 1.1 LHCb, angular analysis of B0 -> K*0 e+ e- (JHEP 06 (2025) 140, arXiv:2502.10291)

Nine inverse femtobarns, 1.1 < q^2 < 6.0 GeV^2, the first full angular
analysis of the electron mode in the central bin and "the most precise
measurement of the B0 -> K*0 e+e- angular observables in the central-q^2
region to date, improving the precision on P4' and P5', previously measured
by Belle, by more than a factor of two". Table 3: F_L = 0.58 +/- 0.04 +/-
0.05, P5' = -0.16 +/- 0.11 +/- 0.11, A_FB = -0.15 +/- 0.05 +/- 0.04; "the
largest differences of around 2 sigma found for F_L and A_FB".

The universality observables Q_i = P_i(mu) - P_i(e), proposed by
Capdevila, Descotes-Genon, Matias and Virto in 2016 because the hadronic
uncertainties cancel in the difference, are formed against LHCb's own 2020
muon sample re-fitted with the same strategy. Table 4 (1.1-6.0 GeV^2):

| Q_i   | value | stat | syst |
|-------|-------|------|------|
| Q_FL  | +0.12 | 0.05 | 0.05 |
| Q_1   | -0.10 | 0.26 | 0.25 |
| Q_4   | -0.07 | 0.17 | 0.13 |
| Q_5   | +0.05 | 0.13 | 0.11 |
| Q_2   | +0.07 | 0.10 | 0.12 |
| Q_6   | -0.05 | 0.14 | 0.10 |
| Q_8   | -0.28 | 0.17 | 0.14 |
| Q_3   | +0.22 | 0.14 | 0.11 |

"Most observables show good agreement with the LFU hypothesis. The largest
difference of around 2 sigma is found for Q_FL." A global fit varying C_9
separately for electrons and muons finds that "a negative shift in the
values of C_9^(e) of the order of -1 with respect to the SM prediction is
required to describe the measured B0 -> K*0 e+e- angular observables, with
a significance above 2 sigma, which is similar to what is found for the
muon channel", and the scan of Delta C_9 = C_9^(mu) - C_9^(e) is
"compatible with zero within one standard deviation, which is fully
consistent with the LFU hypothesis". (The abstract's closing sentence says
"No sign of lepton-flavour-violating effects is observed" where the body
means universality-violating; a slip, noted.)

### 1.2 LHCb, comprehensive analysis of B0 -> K*0 mu+ mu- (PRL 137 (2026) 021802, arXiv:2512.18053)

The full 8.4 inverse femtobarns (2011-2012 and 2016-2018), the complete set
of CP-averaged and CP-asymmetric observables, the K pi S-wave and its
interference with the P-wave for the first time, and "for the first time,
this analysis accounts for the lepton mass when determining the angular
observables", the muon-mass effect being "significant up to q^2 of about 6
GeV^2, with the most pronounced effect at the lowest q^2 values".

Results: "The CP-asymmetry observables all agree with SM expectations".
"Tensions with SM predictions in localized regions of phase space have
broadly increased relative to the levels reported" in 2020: P5' discrepant
with the GRvDV (ABCDMN) predictions at 2.6 and 2.7 sigma (2.1 and 2.4) in
the 4-6 and 6-8 GeV^2 bins and 2.7 (1.6) in 1.1-2.5; A_FB at 2.5 and 1.9
sigma (BSZ) in 2.5-4 and 4-6; the branching fraction 2.1 sigma (1.5) low in
1.1-6. A one-parameter fit of Re(C_9): the 2020 discrepancy of 3.3 sigma
"becomes 3.6 sigma (3.8 sigma) with Flavio (EOS). Including the
differential branching fraction, the discrepancy increases to 4.1 sigma
(4.0 sigma)", with a best-fit shift of -0.94 +0.21/-0.17 (Flavio) or
-0.92 +/- 0.23 (EOS). On the long-distance question the letter is explicit:
"Recent LHCb analyses that try to quantify these effects by fitting
B0 -> K*0 mu+mu- data together with ancillary data and theoretical
predictions do not suggest substantially enhanced long-distance effects",
citing the 2024 amplitude analyses (C_9 alone at 1.8-1.9 sigma and 2.1
sigma from the SM in those).

### 1.3 Mir, Alda and Peñaranda, B-meson anomalies: EFT meets machine learning (EPS-HEP 2025 proceedings, arXiv:2510.17742)

A four-page proceedings of the full paper (Alda, Mir and Peñaranda, Int.
J. Theor. Phys. 65 (2026) 46). Two left-handed semileptonic SMEFT
operators, singlet and triplet, "assuming NP effects only affect a single
generation in the interaction basis, leading to non-universal mixing when
rotating to the mass basis". The flavour structure is a pair of rank-one
projectors, their eq. (2),

    lambda = (1/(1+|alpha|^2+|beta|^2)) [ |alpha|^2  alpha beta*  alpha ;
                                          alpha* beta  |beta|^2   beta  ;
                                          alpha*       beta*      1     ],

one for quarks and one for leptons, hermitian, idempotent, trace one: the
projector onto the direction (alpha, beta, 1). Inputs, their Table 1:

| observable              | SM                 | experiment         |
|-------------------------|--------------------|--------------------|
| R_D                     | 0.299 +/- 0.004    | 0.342 +/- 0.026    |
| R_D*                    | 0.257 +/- 0.005    | 0.287 +/- 0.012    |
| R_J/psi                 | 0.258 +/- 0.004    | 0.52 +/- 0.20      |
| BR(B+ -> K+ nu nubar)   | 0.429e-5 +/- 0.021e-5 | 2.3e-5 +/- 0.7e-5 |

Three scenarios; the preferred Scenario III has C_1 = -0.205 +/- 0.015,
C_3 = -0.12 +0.02/-0.01, quark mixing beta_q = 0.64 +1.36/-0.24 between the
second and third generations only, no lepton mixing by construction, pull
6.25 sigma, Delta chi^2 = 46.66 over the full smelli observable set. Where
lepton mixing is allowed (Scenarios I, II) the fit returns beta_l = 0.00
+/- 0.02 and alpha_l = 0.0 +/- 0.07: the data want none. The improvements
are R_D*^l by 3.3 sigma, R_D^l by 1 sigma, B+ -> K+ nu nubar by 1.7 sigma;
B0 -> K*0 nu nubar worsens by 1 sigma, and "within a setup with only
left-handed effective operators it is not possible to accommodate
simultaneously B+ -> K+ nu nubar and B0 -> K*0 nu nubar". (Their Table 1
values for R_D(*) are HFLAV's 2023 averages, cited to the 2021 paper; their
R_J/psi = 0.52 +/- 0.20 differs from LHCb 2018's published 0.71 +/- 0.17
+/- 0.18 and is not reconciled here.)

## 2. What the framework says, and where each paper bites

The propositions are quoted in yesterday's note, section 3. In one line:
the generation index is the component group S_3 of Aut(S), no gate acts on
it (prop:fcnc, Lean-checked as V^dag (c 1) V = c 1; prop:neutral-blind;
sec:sedenions-flavour-not-force), and the mediators that would make a
non-universal coupling are excluded (rem:no-fifth-force, sec:absent-gate,
the desert of sec:predictions). The framework's prediction for every
universality observable is therefore the Standard Model's.

**The electron angular analysis** is a test of that prediction in the
place where it is cleanest. R_K is a ratio of rates; the Q_i are
differences of shapes, with the form factors and the charm loop cancelling
between the two lepton modes (Capdevila et al., VERIFY-SUPPORT for the
exact statement). The framework's Q_i are not zero but the lepton-mass
term: the kinematic scale 4 m_mu^2/q^2 runs from 4.1 per cent at q^2 = 1.1
GeV^2 to 0.7 per cent at 6, bin-averaged 1.6 per cent, against electron
terms of order 1e-6. That is a factor 4.6 below the tightest Q_i error
(Q_FL, 0.071) and a factor 2 to 5 below the others: the test passes, and
the mass term will matter for the next F_L comparison, which is why the
muon letter now fits it. Script B1.

**The muon letter** bites on the other side. The framework forbids a
label-dependent amplitude, but a label-blind shift of C_9 is not forbidden
by prop:fcnc. It is forbidden by the discussion paragraph that follows
prop:fcnc, which says every flavour observable is "pinned at its
charged-current-loop floor" because "the framework admits no such mediator
at any scale", and that an excess "beyond the charged-loop prediction
refutes the framework". A short-distance universal C_9 shift of -0.9, a
fifth of the Standard Model coefficient, is such an excess. So the
framework is committed, in writing, to the position that the deficit is
long-distance Standard Model dynamics. Yesterday's note already said this
with Ciuchini et al. (SM-compatible once charm rescattering is fitted from
data) on the framework's side and Algueró et al. against. Today adds: LHCb's
own data-driven analyses "do not suggest substantially enhanced
long-distance effects"; Isidori, Polonsky and Tinari's explicit estimate of
the leading D* D_s rescattering gives "a long-distance amplitude which does
not exceed a few percent relative to the short-distance one" (abstract;
VERIFY-SUPPORT for the C_9 number); and the electron mode independently
prefers the same shift. The framework has no hadronic argument of its own.
The CP asymmetries at zero and the muon-mass effects are both as the
framework expects and as the Standard Model expects; no discrimination.

**Mir, Alda and Peñaranda** assume the negation of prop:fcnc's premise.
Their lambda is the maximally label-dependent coupling, a rank-one
projector, and the whole content of their model is that conjugation by the
rotation to the mass basis does not preserve it (script A1: a Haar-random
conjugation changes its entries by up to 0.59, while c 1 is invariant to
1e-16). In the quark sector their best fit needs an s-b entry beta/(1 +
beta^2) = 0.454, an order of magnitude above the CKM's |V_tb V_ts*| of
about 0.04 (PDG): a second quark mixing matrix. The framework has exactly
one mixing matrix per sector, forced as the operational shadow of the zero
divisors (interactions section), and no room for another. In the lepton
sector their own fit does the framework's work: beta_l = 0.00 +/- 0.02 is
the Glashow-Guadagnoli-Lane aligned case, non-universal but
flavour-diagonal, and with alpha_l = beta_l = 0 the projector is exactly
P_tau. What survives of the anomaly literature after 2022 is therefore a
tau-only, aligned coupling driven by R_D(*) and B -> K nu nubar. Against
those four inputs the framework, predicting the SM, stands at 3.1 sigma
uncorrelated and 3.6 sigma with the HFLAV R_D-R_D* correlation of -0.39
(script B2); their 6.25 sigma is a model-comparison statistic over the
full smelli set, which I cannot and do not reproduce.

## 3. The structural point: equivariance is not enough

The framework says the gauge sector acts trivially on the generation
label. It is worth separating that from the weaker statement that the
gauge sector respects the S_3 flavour symmetry, because the two differ by
exactly the pattern the data now select.

**STRUCTURAL.** The commutant of the permutation representation of S_3 on
the label space C^3 is span{1, J}, J the all-ones matrix: the
representation is trivial plus standard, each once, so Schur gives
dimension two. Script A2 confirms it (nullity 2 of the 54 x 9 commutator
map, random commutant element in span{1, J} to 9e-16). An S_3-equivariant
coupling is a 1 + b J; the S_3 average of any coupling lands there (script
A3: the average of Mir et al.'s quark projector is a = 0.182, b = 0.151,
eigenvalues 0.636 on (1,1,1)/sqrt3 and 0.182 twice).

**STRUCTURAL.** The identity component G_0 of a topological group acts
trivially on pi_0 = G/G_0 by conjugation (g s g^-1 s^-1 lies in G_0 for g
in G_0, G_0 being normal). A gate in exp(g_2) = Aut(S)_0 therefore acts
on the component label as the identity, not merely equivariantly: b = 0.
This is the mathematical content of prop:fcnc's "none of these acts on the
triality index" and of sec:sedenions-flavour-not-force's "the gauge content
of the whole tower lives in the identity component". The paper's statement
is the strong one, and it is right to be.

**STRUCTURAL (complex circulant representative).** J commutes with the
Hermitian circulant X = 1 + rho (u C + u* C^T), u = e^{i Phi/3}, which has
the Koide spectrum 1 + 2 rho cos((Phi + 2 pi k)/3) of prop:koide-jordan
(script A4, to 1e-16 with rho = 1/sqrt2, Phi = 2/3). Its eigenvectors are
the Z_3 Fourier modes; (1,1,1)/sqrt3 is the k = 0 mode and carries the
largest eigenvalue 2.379, the tau (k = 1 is the electron at 0.040, k = 2
the muon at 0.580; squared ratios 2.9e-4 and 0.0595). So a 1 + b J is
diagonal in the mass basis, diag(a + 3b, a, a), with its non-universal
part on the tau alone: aligned, no lepton flavour violation, third
generation only.

**CONJECTURE (the reading).** If the tau anomalies harden, the minimal
retreat from the framework's position is not "some new mediator" but "the
gauge sector sees the label equivariantly rather than trivially", and that
retreat predicts a tau-only aligned coupling: the pattern Mir et al.'s fit
selects in the lepton sector. It would not reproduce their quark sector:
the democratic term is diagonal in the circulant mass basis, so its b-s
entry in the down basis would be of CKM size, 3b |V_tb V_ts*| of order
0.02, not their 0.45. I am not proposing the retreat; I am saying which
premise R_D(*) and B -> K nu nubar test, and that it is the trivial action
specifically, not S_3 symmetry. invalid_routes.md has no entry on a
democratic or tau-specific coupling.

**RHYME.** The one S_3-equivariant, non-trivial structure the framework
does put on the label is the democratic Jordan element of
prop:koide-jordan, in the mass sector. The mass sector sees the label
democratically and the gauge sector not at all; the two propositions are
the same statement about J, made in two places.

**Fence.** The diagonalisation statement is for the circulant
representative. The Koide spectrum depends only on Phi = arg(u_1 u_2 u_3)
and the off-diagonal phases can be moved by a diagonal rephasing, under
which J is not invariant; the S_3 permutation action is defined in the
basis in which the label is permuted, and the paper's Z_3 form is the
circulant one, so the statement holds in the paper's own basis. Over the
octonions the primitive idempotents are not Fourier modes and the
statement is not made.

## 4. The script

`scripts/three_papers_lfu_angular_2026-11-07T2000.py`, numpy only, seed
20261107. Part A: (A1) the prop:fcnc identity for a Haar-random unitary
against Mir et al.'s projector, its Hermiticity, idempotence, trace and s-b
entry, and the lepton-sector tau-mu entry at their fitted bound; (A2) the
commutant of S_3 by SVD of the commutator map; (A3) the S_3 average of the
projector; (A4) the Koide circulant, its spectrum against the formula, the
commutation with J, the k = 0 eigenvector, the generation assignment and
the diagonal form of a 1 + b J in the mass basis. Part B: (B1) the eight
Q_i against zero with stat and syst in quadrature, chi^2 for eight (even)
degrees of freedom by the closed-form survival function, the lepton-mass
scale at four q^2 values and bin-averaged; (B2) the four Table 1 inputs
against the SM, uncorrelated and with the HFLAV correlation, and the
R_D-R_D* pair alone. One check was mis-stated in the first run (I had
written "two orders below the smallest Q_i error"; the ratio is 4.6) and
was replaced by the bin-averaged comparison before the run recorded in
section 10. 27/27 PASS.

## 5. What I think

The three papers are the post-2022 landscape in miniature. Universality
holds in shapes as well as in rates; a universal deficit persists at a
significance that depends on how one treats the charm loop; and the only
non-universal anomalies left are in the tau sector and the neutrino mode.
Read against the framework:

- The pass is real and cheap. The framework predicted Q_i = 0 up to the
  mass term before the measurement existed, as a theorem of the dictionary
  rather than an accident; so did the Standard Model. The framework's
  distinctive content was the exclusion of the muon-specific models that
  dominated the literature until 2022, and those are gone.
- The exposure is real and specific. A universal C_9 deficit at 4 sigma
  that is not long-distance would refute the framework by its own written
  criterion. LHCb's data-driven analyses lean against the long-distance
  explanation; Isidori, Polonsky and Tinari's explicit charm estimate leans
  against it; Ciuchini et al. lean for it. The framework has placed a bet
  on hadronic physics with no hadronic argument. I would rather it said so
  in the paper than be found to have said nothing.
- The tau anomalies test one premise, and now I can name it: the trivial
  action of the identity component on pi_0, not S_3 symmetry. That is a
  sharper falsifier than "no new physics in the desert", and it has a
  mathematical shape (the b J term) that the framework already uses in the
  mass sector. If R_D(*) and B -> K nu nubar go away, as R_K did, the
  framework was right twice for the same reason. If they stay, the first
  thing to re-examine is whether the gauge gates' action on the label is
  trivial or only equivariant, and the answer the data would want is "on
  the tau alone".
- Mir et al.'s model, on its own terms, costs two flavour matrices, one of
  them a second quark mixing at ten times CKM size, to buy 3.6 sigma on
  four observables. Their own fit removes the lepton half. The framework
  pays nothing and stands 3.6 sigma off. Those are the two positions, and
  Belle II will decide between them.

## 6. Second-order findings for JS's ruling

(a) Yesterday's finding 6(a), the universality paragraph for
`sec:predictions`: add the angular test as a second passed instance, with
the numbers of section 1.1 (Q_i chi^2 6.6/8, p = 0.58, correlations
neglected; Delta C_9 within one sigma of zero), and the clause that the
framework's Q_i are the lepton-mass term, bin-averaged 1.6 per cent in
1.1-6 GeV^2, a factor 4.6 below the tightest current error. CANDIDATE.

(b) Yesterday's finding 6(d), sharpened: the discussion paragraph after
`prop:fcnc` already says flavour observables are pinned at the
charged-loop floor and that an excess refutes the framework. It should
name b -> s l l's C_9 explicitly: the full-dataset shift of -0.9 at 3.6 to
4.1 sigma (theory-nuisance dependent; 1.5 to 2.1 sigma in LHCb's
data-driven analyses) is lepton-universal, as the framework requires, and
within the framework can only be long-distance Standard Model physics; a
short-distance origin established at five sigma refutes the framework.
Cite the dispute both ways (Ciuchini et al.; Isidori, Polonsky and Tinari;
the LHCb amplitude analyses). CANDIDATE prediction, OPEN dispute.

(c) Yesterday's finding 6(e), the open-problem entry: add B+ -> K+ nu
nubar beside R_D(*). Belle II's 2.3e-5 is 2.7 sigma above the SM; the
framework predicts the SM (no gate acts on the lepton label, so no
tau-neutrino enhancement; the two sterile neutrinos at 3.6 TeV are far
above the B mass). PASS if the branching fraction moves into the SM band
with more Belle II data; FAIL if established at five sigma above it. OPEN.

(d) A remark after `prop:fcnc` or in
`sec:sedenions-flavour-not-force`: that S_3-equivariance alone would leave
a coupling a 1 + b J whose non-universal part is diagonal in the Koide mass
basis and falls on the tau, and that the proposition uses the stronger
fact that the identity component acts trivially on pi_0, which forces
b = 0. Two sentences, STRUCTURAL; with the reading of section 3 fenced as
CONJECTURE if JS wants it in at all.

(e) A one-clause cross-reference from `prop:koide-jordan` to `prop:fcnc`:
the democratic element is the one S_3-equivariant structure the framework
puts on the generation label, and it lives in the mass sector; the gauge
sector sees the label not at all. RHYME.

## 7. Fences

- The Q_i chi^2 neglects the correlations LHCb reports (Tables 13 to 16 of
  the paper, "generally small", up to 20 per cent). The p-value is
  indicative.
- The lepton-mass scale 4 m^2/q^2 is a kinematic size, not a prediction of
  any Q_i's value; the SM predictions for the Q_i (Capdevila et al.) carry
  coefficients of order one on that scale and were not computed here.
- The 3.6 sigma of script B2 uses Mir et al.'s SM values, which differ
  slightly from HFLAV's (0.299 against 0.298; 0.257 against 0.254);
  yesterday's HFLAV-only pair gave 3.4 sigma, today's pair 3.1 with their
  SM values. Same conclusion, different inputs, stated.
- Section 3's diagonalisation is for the circulant representative (see
  its own fence). The group-theory fact about G_0 and pi_0 is general.
- I have not read Mir et al.'s full paper, the LHCb papers' supplementary
  material, or the Capdevila et al. and Isidori et al. bodies; their
  support marks are in the batch header.
- Nothing here bears on the OPEN finding 6(b) of yesterday (the lepton tag
  "coupling at the state level"); that still needs JS's reading.

## 8. Proposed ledger entries (not written; maintainer's call)

- **CANDIDATE** Lepton universality in the b -> s l l angular observables:
  LHCb's 2025 Q_i are consistent with zero (chi^2 6.6/8, p = 0.58,
  correlations neglected) and Delta C_9 is within one sigma of zero; the
  framework predicts Q_i equal to the lepton-mass term, bin-averaged 1.6 per
  cent in 1.1-6 GeV^2, a factor 4.6 below the tightest current error.
  Second passed test of prop:fcnc's universality, after R_K and R_K*.
- **STRUCTURAL** The commutant of S_3 on the generation label space is
  span{1, J}; the identity component of Aut(S) acts trivially on pi_0, so
  gates in exp(g_2) act on the label as c 1 and not merely as a 1 + b J.
  Prop:fcnc uses the trivial action; equivariance alone would permit a
  tau-only aligned coupling (J is diagonal in the circulant Koide mass
  basis, on the k = 0 mode, the tau).
- **OPEN** The universal C_9 deficit: -0.9 at 3.6 to 4.1 sigma in LHCb's
  full dataset (binned; theory-nuisance dependent), 1.5 to 2.1 sigma in
  LHCb's data-driven amplitude analyses; the electron mode prefers the same
  shift at above 2 sigma. Within the framework it must be long-distance
  SM dynamics. FAIL if a short-distance origin is established at five
  sigma; PASS if the shift is absorbed by nonlocal contributions in future
  data-driven analyses.
- **OPEN** B+ -> K+ nu nubar as a falsifier beside R_D(*): Belle II 2.3e-5
  against SM 0.43e-5 (short-distance; 2.7 sigma on Belle II's own
  accounting); the framework predicts the SM. PASS/FAIL as in 6(c).

## 9. Files

- `knowledge/sessions/three_papers_lfu_angular_2026-11-07T2000.md` (this).
- `scripts/three_papers_lfu_angular_2026-11-07T2000.py`, PASS, 27/27.
- `bib/three_papers_lfu_refs_2026-11-07T2010.bib`, 13 keys, 12 DOIs
  Crossref-verified, one arXiv-only proceedings, no VERIFY-CITE;
  VERIFY-SUPPORT on capdevila2016assessing and
  isidoripolonskytinari2025charm as recorded in the header.
- `notes/todo.md`: section "2026-11-07: three papers on b -> s l l angular
  analyses and the R_D(*) fit".
- Scratchpad (not in the repo): the three arXiv HTML renderings and their
  text extractions, eleven related abstracts, thirteen Crossref records.
- Not touched: the paper, the ledgers, references.bib, anything built or
  committed.

## 10. Exact stdout of `scripts/three_papers_lfu_angular_2026-11-07T2000.py`

```
THREE PAPERS, LEPTON UNIVERSALITY AND THE ANGULAR OBSERVABLES  (seed 20261107)

PART A: structure

A1  prop:fcnc versus the Mir-Alda-Penaranda projector
  [PASS] V^dag (c 1) V = c 1 for a Haar-random unitary V  (max deviation 1.1e-16)
  [PASS] lambda(0, 0.64) is Hermitian
  [PASS] lambda(0, 0.64) is idempotent
  [PASS] tr lambda = 1
  [PASS] s-b entry = beta/(1+beta^2)  (0.45403)
    off-diagonal norm of lambda: 0.6421; after conjugation by V: 0.7580
  [PASS] a rank-one projector on the label is not conjugation-invariant  (max change 0.586)
    lepton projector beta_l = 0.00: tau-mu entry 0.0000 (their fit: beta_l = 0.00 +/- 0.02, lepton mixing consistent with zero)
    lepton projector beta_l = 0.02: tau-mu entry 0.0200 (their fit: beta_l = 0.00 +/- 0.02, lepton mixing consistent with zero)
  [PASS] beta_l = 0 gives the pure third-generation projector (aligned, no LFV)

A2  commutant of the S_3 permutation action on C^3
  [PASS] commutant has dimension 2  (singular values [3.4641 3.4641 3.4641 3.4641 3.4641 3.4641 3.4641 0.     0.    ])
  [PASS] 1 commutes with every permutation
  [PASS] J commutes with every permutation
  [PASS] a random commutant element lies in span{1, J}  (residual 8.7e-16)

A3  S_3 average of the projector lambda(0, 0.64)
  [PASS] S_3 average equals a 1 + b J with b = (sum of entries - 1)/6, a = 1/3 - b  (a = 0.1820, b = 0.1513)
    eigenvalues of the average: [0.182 0.182 0.636]  (a + 3b = 0.6360 on (1,1,1)/sqrt3, a twice)
  [PASS] the average is non-universal (b != 0) but equivariant

A4  the democratic term in the Koide mass basis (complex circulant representative)
  [PASS] Koide circulant is Hermitian
  [PASS] eigenvalues are 1 + 2 rho cos((Phi + 2 pi k)/3)  ([0.0403 0.5802 2.3794])
  [PASS] J commutes with the Koide circulant
  [PASS] the largest eigenvalue's eigenvector is (1,1,1)/sqrt3, the k = 0 mode  (|overlap| = 1.000000)
    k = 0, 1, 2 -> sqrt-mass values [2.3794 0.0403 0.5802] -> generations ['tau', 'electron', 'muon']
    squared ratios to the k = 0 mode: [1.     0.0003 0.0595]  (m_e/m_tau = 2.88e-04, m_mu/m_tau = 0.0595)
  [PASS] k = 0 is the heaviest generation
  [PASS] a 1 + b J is diagonal in the mass basis  (diag = [0.182 0.182 0.636])
  [PASS] its non-universal part sits on the tau alone

PART B: data against the framework's prediction (= the SM's)

B1  LHCb B0 -> K*0 e+e- (JHEP 06 (2025) 140), Table 4: Q_i = P_i(mu) - P_i(e), 1.1 < q^2 < 6.0 GeV^2
    Q_FL  = +0.12 +/- 0.071   pull from zero +1.70 sigma
    Q_1   = -0.10 +/- 0.361   pull from zero -0.28 sigma
    Q_4   = -0.07 +/- 0.214   pull from zero -0.33 sigma
    Q_5   = +0.05 +/- 0.170   pull from zero +0.29 sigma
    Q_2   = +0.07 +/- 0.156   pull from zero +0.45 sigma
    Q_6   = -0.05 +/- 0.172   pull from zero -0.29 sigma
    Q_8   = -0.28 +/- 0.220   pull from zero -1.27 sigma
    Q_3   = +0.22 +/- 0.178   pull from zero +1.24 sigma
    chi^2 = 6.58 for 8 observables (correlations neglected), p = 0.58
  [PASS] every Q_i is within 2 sigma of universality  (largest |pull| 1.70)
  [PASS] the Q_i set is consistent with Q_i = 0  (p = 0.58)
    the framework's non-zero prediction is the lepton-mass term; its scale 4 m^2/q^2:
      q^2 = 1.1 GeV^2: muons  4.06 %, electrons 9.5e-07
      q^2 = 2.5 GeV^2: muons  1.79 %, electrons 4.2e-07
      q^2 = 4.0 GeV^2: muons  1.12 %, electrons 2.6e-07
      q^2 = 6.0 GeV^2: muons  0.74 %, electrons 1.7e-07
  [PASS] muon-mass scale is below one per cent by q^2 = 6 GeV^2
    bin-averaged muon-mass scale over 1.1-6 GeV^2: 1.55 %; smallest Q_i error 0.071 (Q_FL); ratio 4.6
  [PASS] bin-averaged muon-mass scale is below every Q_i error  (ratio 4.6)
  [PASS] but within a factor ten of the Q_FL error: the mass term matters for the next F_L test

B2  Mir, Alda and Penaranda Table 1 inputs against the SM (the framework predicts the SM value)
    R_D                    exp 0.342 +/- 0.026, SM 0.299 +/- 0.004: pull +1.63 sigma
    R_D*                   exp 0.287 +/- 0.012, SM 0.257 +/- 0.005: pull +2.31 sigma
    R_J/psi                exp 0.520 +/- 0.200, SM 0.258 +/- 0.004: pull +1.31 sigma
    BR(B+->K+nunu) x 1e5   exp 2.300 +/- 0.700, SM 0.429 +/- 0.021: pull +2.67 sigma
    uncorrelated: chi^2 = 16.85/4, p = 2.1e-03, 3.08 sigma
    with rho(R_D, R_D*) = -0.39: chi^2 = 21.08/4, p = 3.0e-04, 3.61 sigma
    R_D, R_D* pair alone: chi^2 = 12.23/2, 3.06 sigma
  [PASS] no single headline input exceeds 3 sigma  (largest 2.67 sigma (B+ -> K+ nu nubar))
  [PASS] the four together stand against the SM at about 3 sigma  (3.61 sigma)
    (their global pull of 6.25 sigma, Delta chi^2 = 46.66 for three parameters over the full
     smelli observable set, is a model-comparison statistic and is not reproduced here)

SUMMARY
  27/27 checks passed
THREE PAPERS LFU ANGULAR: PASS
```
