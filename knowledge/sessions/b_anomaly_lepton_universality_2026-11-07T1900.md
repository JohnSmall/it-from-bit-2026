# The B-meson anomalies and lepton universality in the framework

Session note, Fable 5.1, 2026-11-07T1900. JS asked: "read this recent paper
on the B-meson decay anomaly and tell me if there is anything in our
framework that can explain it", https://arxiv.org/abs/2105.05095.

Script: `scripts/b_anomaly_lepton_universality_2026-11-07T1900.py` (PASS,
seed 20261107, pure numpy; exact stdout in section 11). Batch:
`bib/b_anomaly_refs_2026-11-07T1910.bib` (11 keys). Status labels are
proposed, not applied; ledger entries proposed in section 9.

## 0. The answer in five lines

- The paper (Alda, Guasch and Peñaranda, LCWS2021 proceedings, May 2021,
  revised June 2021) is a summary of global fits to the 2021 anomalies:
  R_K = 0.846 (3.1 sigma), R_K* (2.3 and 2.4 sigma), R_D and R_D* (3.08
  sigma combined). Its conclusion is that the data need lepton flavour
  universality (LFU) violation: the LFU-conserving fit has pull 0.55 sigma,
  the electron-plus-muon fit 4.97 sigma, with opposite-sign couplings to
  electrons and muons.
- Nothing in the framework explains an LFU violation, and the framework
  forbids one at the gauge level. The generation index is the component
  group S_3 of Aut(S), not a Lie-algebra charge; every gate of the vertex
  dictionary acts as the identity on it (`prop:fcnc`, `prop:neutral-blind`,
  `sec:sedenions-flavour-not-force`); and the mediators the paper's
  operators need are excluded: a Z' by `rem:no-fifth-force`, a leptoquark by
  `sec:absent-gate`, any TeV-scale state by the desert prediction of
  `sec:predictions`. So R_K = R_K* = 1 up to lepton-mass effects, exactly as
  in the Standard Model.
- That is where the data went. LHCb's December 2022 reanalysis (9 fb^-1,
  with the electron misidentification backgrounds modelled) gives R_K =
  0.949 and R_K* = 1.027 in the central bin, R_K = 0.994 and R_K* = 0.927 in
  the low bin: chi^2 = 1.76 for 4 degrees of freedom against R = 1, p = 0.78
  (script, part B). The 2021 value was 3.4 sigma from 1 on the same
  convention.
- What survives is not an LFU violation. The b -> s mu mu branching
  fractions and angular observables still sit below the Standard Model; a
  lepton-universal shift C_9 of about -1.2 is favoured at 4.6 to 5.8 sigma
  by Algueró et al. 2023, while Ciuchini et al. 2023 find the same data
  consistent with the Standard Model once charm-loop rescattering is fitted.
  A universal shift is generation-blind and not touched by `prop:fcnc`, but
  as new physics it needs a new neutral mediator, which the framework
  excludes. The framework therefore sides with the hadronic reading. In
  b -> c tau nu the HFLAV 2023 average of R(D) and R(D*) is 3.1 sigma from
  the Standard Model (3.4 sigma with the experimental correlation alone);
  the framework predicts no deviation. These two are the live falsifiers.
- Labels: the structural exclusion is ESTABLISHED in its register form
  (`prop:fcnc` is Lean-checked) and conditional on the dictionary's premises
  (CANDIDATE); the prediction R_K = R_K* = R_D(*)/SM = 1 at the gauge level
  is CANDIDATE; the hadronic reading of the universal deficit is a
  CANDIDATE prediction, not a derivation. One OPEN point (section 6(b)): the
  interactions section's conjecture that the lepton tag "may couple at the
  state level" must be a unitary mixing of the label, not a label-dependent
  amplitude, or it would reopen LFU violation.

## 1. The paper

Alda, Guasch and Peñaranda, "Anomalies in B mesons decays: present status
and future collider prospects", arXiv:2105.05095 [hep-ph], v1 11 May 2021,
v2 14 June 2021; talk at the International Workshop on Future Linear
Colliders (LCWS2021), 15 to 18 March 2021; no journal. Read via the arXiv
abstract page and the HTML rendering of v2 (the PDF came back as bytes; the
text was cut inside section 4, so section 5 and the bibliography were not
read).

What it quotes (its section 1): HFLAV averages R_D = 0.340 +/- 0.027 +/-
0.013 and R_D* = 0.295 +/- 0.011 +/- 0.008 against Standard Model values
0.299 +/- 0.003 and 0.258 +/- 0.005 (1.4 sigma, 2.5 sigma, 3.08 sigma
combined); LHCb R_K[1.1, 6] = 0.846 +0.042/-0.039 +0.013/-0.012 (3.1 sigma)
and R_K*[0.045, 1.1] = 0.66 +0.11/-0.07 +/- 0.03, R_K*[1.1, 6] = 0.69
+0.11/-0.07 +/- 0.05 (2.3 and 2.4 sigma); P_5' named without a value.

What it does: a weak effective theory fit of C_9 and C_10 for electrons
and muons and C_VL for all three leptons (its Eq. 6), best fit C_9^NP,mu =
-1.09 and C_10^NP,mu = 0.48, 5.95 sigma over the Standard Model (its
section 2); then SMEFT fits with the semileptonic operators O_lq^(1) and
O_lq^(3) on third-generation quarks and same-generation leptons, with
C_lq^(1) = C_lq^(3) imposed to escape the Z-pole constraints (its Eq. 15),
run from Lambda = 1 TeV to m_b (its Eq. 14). Its Table 1: electrons only
2.97 sigma, muons only 2.34 sigma, taus only 1.96 sigma, electrons and
muons 4.97 sigma with C^e = -0.25 +/- 0.07 and C^mu = 0.24 +/- 0.06, all
three 4.97 sigma with C^e = -0.25 +/- 0.02, C^mu = 0.211 +/- 0.016, C^tau =
-0.3 +/- 0.4, the LFU-conserving scenario (e = mu = tau) 0.55 sigma, and
the pattern e = -mu = tau 5.54 sigma. Its own sentence: "LFU violation is
needed to accommodate it." The flavour structure is a U(2)^3 symmetry with
third-generation quark operators; the scale is "O(TeV)". Its collider
proposal is e+ e- -> b s at the ILC, "CKM-suppressed by V_ts".

## 2. Where the anomalies stand now

- LHCb, December 2022 (PRL 131, 051803 and PRD 108, 032002; 9 fb^-1,
  2011 to 2018): R_K low 0.994 +0.090/-0.082 +0.029/-0.027, R_K* low 0.927
  +0.093/-0.087 +0.036/-0.035, R_K central 0.949 +0.042/-0.041 +/- 0.022,
  R_K* central 1.027 +0.072/-0.068 +0.027/-0.026; "All four measurements
  are in agreement with predictions of the SM." The shift from 0.846 is
  attributed to "more stringent electron identification criteria" (0.064)
  and "the modeling of the residual misidentified background" (0.038); the
  low R_K* bin was moved from 0.045 to 0.1 GeV^2 to remove photon-pole
  contamination. Read from the arXiv HTML of both papers.
- Algueró, Biswas, Capdevila, Descotes-Genon, Matias and Novoa-Brunet 2023
  (EPJC 83, 648; v3 May 2024): the LFU-violating fits fall to 1.2 to 1.5
  sigma; a universal C_9 of -1.15 to -1.21 is preferred at 4.6 to 5.8 sigma
  depending on the scenario, with B -> K mu mu tensions "up to the level of
  4 sigma" against their Standard Model predictions and no q^2 dependence
  of the kind a missing charm-loop contribution would show. Read in part
  (sections 1 to 3 verbatim, 5 and 6 extracted).
- Ciuchini, Fedele, Franco, Paul, Silvestrini and Valli 2023 (PRD 107,
  055036): "We find data to be consistent with the Standard Model once
  rescattering from intermediate hadronic states is included"; the
  data-driven fit gives C_9^NP,mu in [-1.06, 1.01] at 95 per cent, the
  model-dependent one [-1.19, -0.67]; the evidence for new physics is
  "inextricably linked to the assumptions on charming-penguin amplitudes".
  Read in part.
- HFLAV, averages as of 2023 (arXiv:2411.18639v2, January 2026; the arXiv
  page gives PRD 113, 012008): R(D) = 0.342 +/- 0.026, R(D*) = 0.287 +/-
  0.012, rho = -0.39, against the Standard Model averages 0.298 +/- 0.004
  and 0.254 +/- 0.005; "deviates from the SM prediction by 3.1 sigma".
  Read from the PDF text (section 6.6 figure and the tau-physics summary).
- LHCb 2023 (PRL 131, 111802): R(D*) = 0.281 +/- 0.018 +/- 0.024 and R(D0)
  = 0.441 +/- 0.060 +/- 0.066, rho = -0.43, "1.9 standard deviations" from
  the Standard Model. Belle II 2024 (arXiv:2401.02840, 189 fb^-1): R(D*) =
  0.262 +0.041/-0.039 +0.035/-0.032, "consistent with the current world
  average and with standard model predictions". Abstracts only.

So the anomaly the paper is about, LFU violation in b -> s l l, is gone;
what remains is a lepton-universal deficit in the muon channels whose
interpretation is disputed, and a 3 sigma excess in b -> c tau nu.

## 3. What the framework says

Quoted from Paper 1 as it stands on disk today.

- `prop:fcnc` (interactions section, "No flavour-changing neutral
  currents"): "A neutral-current coupling is proportional to the identity
  in the generation index. In the mass basis ... V^dag D V = c 1 = D. The
  off-diagonal, flavour-changing entries vanish identically." Proof: "None
  of these acts on the triality index that labels the generation, because
  that index lives in the entanglement class and is orthogonal to the
  single-qubit gauge action." Lean-checked (`lean/`, `Fcnc.lean`, per the
  2026-11-03 commit). The same paragraph is careful that loop-level
  flavour-changing processes "are observed ... at rates matching the
  charged-loop calculation".
- `prop:neutral-blind`: "no composition of neutral gates changes a
  channel's generation", granted the class structure of `sec:generations`
  and inheriting `op:filatov-extension`.
- `sec:sedenions-flavour-not-force`: "A finite factor is the component
  group pi_0; it has no Lie algebra; and an object with no Lie algebra
  contributes no generators to any connection form. Whatever the fourth
  wire carries is therefore a discrete label and never a coupling charge."
  Ledger: ESTABLISHED, "Flavour symmetry conserved but ungauged".
- `rem:no-fifth-force`: "The discovery of a genuine fifth force ... would
  therefore refute the construction."
- `sec:absent-gate`: "ignoring the SLOCC restriction on a single register
  is physics-speak for positing a leptoquark"; the converter "exists as
  mathematics and is absent from the gate set". Ledger: ESTABLISHED,
  no-leptoquark theorem, conditional on four premises.
- `sec:predictions`: "There is no new physics between the electroweak
  scale and the matching scale at ~3.6 TeV ... refuted by any new state in
  that range not accounted for by the framework."
- Interactions section, the fourth-qubit paragraph: "mixing is forced ---
  the CKM and PMNS structure, its CP phase included, as the operational
  shadow of the sedenion zero divisors ... the lepton tag may couple at the
  state level where the quark tag must remain frame-coupled". Recorded
  there as "directions rather than results".

Reading these against the paper: the paper's operators O_lq^(1,3) with
lepton-flavoured coefficients are exactly couplings that act on the lepton
generation label; the paper's own fits say the label-blind coupling
(scenario VIII) does nothing for the anomalies and the label-odd one
(scenario IX) does everything. The framework stocks only label-blind gates.
Lepton flavour universality of the gauge couplings is therefore not an
accident to be explained but a theorem of the dictionary, and the only
generation-dependent input the framework has is the same one the Standard
Model has, the lepton masses (the Koide sector). Its prediction for every
LFU ratio is the Standard Model's: R_K = R_K* = 1.00 +/- 0.01 (Bordone,
Isidori and Pattori 2016 for the QED corrections), R(D(*)) at the Standard
Model value.

Three things the framework adds beyond "same as the Standard Model":

1. The explanations are excluded, not merely unneeded. The TeV-scale
   mediators the fits assume, Z' or leptoquark, are each forbidden by a
   named proposition, and the TeV scale itself is inside the predicted
   desert. If an LFU violation is ever established, the framework is
   refuted in the same way a fifth force would refute it; this is a
   falsifier of the same rank as `rem:no-fifth-force`, and it should be
   written down as one.
2. The lepton-universal deficit has only one home. A universal C_9 shift
   is not forbidden by `prop:fcnc`, since it is label-blind; but it needs
   a mediator if it is new physics, and the framework has none. So within
   the framework the b -> s mu mu deficit must be Standard Model dynamics,
   the charm loop. The framework takes Ciuchini et al.'s side of a live
   dispute, with no argument of its own about hadronic physics; that is a
   prediction, and a cheap one to be wrong about.
3. R(D) and R(D*) are now the sharper test. A 3 sigma excess in b -> c tau
   nu with the framework predicting zero is the one place where the
   anomaly literature and this framework disagree today. The framework
   cannot bend: it has no tau-specific coupling to offer.

## 4. The script

Part A builds the register toy: a quark register (gauge qubit x
three-valued generation label) and a lepton register (the same), gates of
exactly three kinds, the charged gate as the T_3 raise tensored with a
generic unitary on the quark label (the CKM rotation of
`sec:interactions`), and neutral gates as random unitaries on a gauge qubit
tensored with the identity on both labels. For 200 random gate words,
including 67 two-word sums standing in for loop interference, the summed
rate b -> s l l is identical for the three lepton generations to machine
zero. A label-diagonal phase gate inserted into the word changes nothing
(spread 4e-16): a classical tag cannot see a phase. A label-dependent
amplitude added to the universal one, A_l = A_SM (1 + C^l) with the paper's
scenario VII values, changes the ratio to exactly |1 + C^mu|^2 / |1 +
C^e|^2 = 2.6071: that is what R_K != 1 requires and what the dictionary
lacks. The Lean identity V^dag (c 1) V = c 1 holds to 6e-17 on 2000 Haar
unitaries; for D = diag(-0.25, 0.211, -0.3) the e-mu entry of V^dag D V has
median 0.13 and maximum 0.2511 against the bound (max D - min D)/2 =
0.2555, so a non-universal coupling is lepton-flavour-violating in every
basis but the aligned one (Glashow, Guadagnoli and Lane 2015).

Part B computes pulls from R = 1 with asymmetric errors symmetrised by the
larger side and a theory uncertainty 0.01 in quadrature: LHCb 2021 R_K
-3.42 sigma; LHCb 2022 four bins -0.06, -0.73, -1.05, +0.35 sigma, chi^2 =
1.76 for 4 dof, p = 0.78 (R_K* low bin against the Standard Model's 0.98:
-0.53 sigma). HFLAV 2023 R(D), R(D*): chi^2 = 14.8 for 2 dof with the
experimental correlation -0.39, p = 6.1e-4, 3.4 sigma (HFLAV's 3.1 sigma
includes the Standard Model correlation); individual pulls +1.67 and +2.54
sigma.

Part C decomposes the paper's fitted coefficient vectors into the
S_3-invariant part, the only shape a dictionary gate can have, and the
traceless part: scenario IV is -0.003 (1,1,1) plus a traceless vector of
norm 0.347; scenario VII is -0.113 (1,1,1) plus norm 0.398. The 2021
anomaly lived in the traceless part.

## 5. What I think

The honest headline is that the framework explains nothing here because
there is nothing left to explain in the channel the paper is about, and
that it was right for a structural reason rather than by luck: it never
had a gate that could tell a muon from an electron. That is also the
Standard Model's reason, and the framework should not claim credit the
Standard Model already owns. What it can claim is the exclusion: the paper
surveys Z' and leptoquark completions, and the framework rules out both by
propositions it wrote for other purposes (proton stability, no fifth
force). A theory that forbids the fashionable explanation of a 3 sigma
anomaly and is then vindicated by the reanalysis has earned a sentence in
the predictions section, no more.

The pushback runs the other way too. First, the framework now owes a
stance on R(D(*)), where the excess is at 3 sigma and has been for a
decade; it predicts the excess will go away, and if Belle II's full dataset
hardens it to 5 sigma the framework is in the same trouble as it would be
with a fifth force. Second, the universal b -> s mu mu deficit: the
framework's only consistent position is "hadronic", which commits it to
Ciuchini et al. against Algueró et al. in a dispute about charm loops that
the framework has no tools to adjudicate. Third, and the one I would put in
front of JS: the interactions section says the lepton tag "may couple at
the state level" to explain the large PMNS angles. If that coupling is a
unitary rotation of the label (mixing), LFU survives, because Part A's
first check holds for any unitary on the label as long as the gauge gates
are label-blind. If it is a label-dependent amplitude, LFU fails and
`prop:neutral-blind` has a loophole. The section should say which, and the
answer has to be the first.

## 6. Second-order findings for JS's ruling

(a) `paper1/predictions_section_2026-06-13.tex`: a paragraph recording
lepton flavour universality of the gauge couplings as a prediction of
`prop:fcnc` and `sec:sedenions-flavour-not-force`: R_K = R_K* = 1 up to
lepton-mass and QED effects, R(D(*)) at the Standard Model value; LHCb's
2022 R_K and R_K* as the test already passed; the HFLAV R(D(*)) excess as a
standing null; an established LFU violation as a falsifier of the same rank
as a fifth force. CANDIDATE (the framework's assembly).

(b) `paper1/interactions_circuits_section_2026-06-08.tex`, the fourth-qubit
paragraph ("the lepton tag may couple at the state level"): one clause
saying the coupling is a unitary mixing of the generation label and not a
label-dependent amplitude, so that it produces the PMNS angles without
breaking the universality of `prop:fcnc`. OPEN until JS confirms that is
the intended reading; if it is not, `prop:neutral-blind` needs a fence.

(c) `sec:predictions`, the desert paragraph: a clause that the TeV-scale
mediators of the b -> s l l fits (Z', leptoquarks, defined at Lambda = 1
TeV in the paper) fall inside the desert and are excluded by it as well as
by `sec:absent-gate` and `rem:no-fifth-force`. CANDIDATE.

(d) The universal C_9 deficit: a sentence in `prop:fcnc`'s discussion
paragraph (which already lists b -> s gamma and B_s -> mu mu as
loop-level processes) that any lepton-universal deviation in b -> s mu mu
must, in this framework, be Standard Model dynamics (the charm loop), with
the Algueró/Ciuchini disagreement cited. CANDIDATE prediction; the
framework offers no hadronic argument.

(e) `knowledge/open_problems.md`: a new entry, "LFU ratios as a falsifier",
with PASS/FAIL: PASS if R(D) and R(D*) move to the Standard Model band as
Belle II and LHCb Run 3 data arrive; FAIL if any LFU ratio is established
at 5 sigma away from the Standard Model. OPEN.

## 7. Prior work and ownership

- The anomalies and their fits: Alda, Guasch and Peñaranda 2021 and the
  literature they cite; Algueró et al. 2023; Ciuchini et al. 2023. Not
  the framework's.
- The data: LHCb 2021 (Nature Physics), LHCb 2022/2023 (PRL, PRD), LHCb
  2023 R(D*) and R(D0), Belle II 2024, HFLAV 2023 averages. Not the
  framework's.
- "LFU violation implies lepton flavour violation unless aligned":
  Glashow, Guadagnoli and Lane 2015. Part A's second check is a
  numerical restatement.
- The Standard Model prediction R_K = 1.00 +/- 0.01 with QED corrections:
  Bordone, Isidori and Pattori 2016.
- The GIM mechanism: Glashow, Iliopoulos and Maiani 1970, already cited by
  `prop:fcnc`.
- The framework's: the register reading of universality as "no gate acts
  on the label" (`prop:fcnc`, `prop:neutral-blind`, Lean-checked), the
  component-group argument (`sec:sedenions-flavour-not-force`), the
  exclusions (`sec:absent-gate`, `rem:no-fifth-force`, the desert), and
  this note's assembly of them against the B anomalies.

## 8. Fences

- Part A is a register toy, not a QCD calculation: no form factors, no
  loop integrals, no Wilson coefficients beyond the structural shape. It
  shows what kind of operator moves R_K off 1; it does not compute R_K.
- The pulls in Part B use a stated symmetrisation and treat the four 2022
  bins as independent; LHCb's likelihoods are not Gaussian and their own
  significance statements are quoted beside mine.
- The HFLAV chi^2 omits the Standard Model prediction correlation, which
  is why 3.4 sigma here against their 3.1 sigma.
- Sections 5 and 6 of Alda et al. (conclusions) were not read; nothing
  here depends on them.
- The "hadronic" stance of section 3, point 2, is a consequence of the
  framework's exclusions, not a judgement about charm loops.
- No claim is made about R(D(*)) beyond "the framework predicts the
  Standard Model value"; the tau mass enters exactly as in the Standard
  Model.
- Nothing here touches the Koide sector or the CKM values of
  `sec:interactions`.

## 9. Proposed ledger entries

- **ESTABLISHED** (register form; conditional on the dictionary's
  premises) Lepton flavour universality of every gate in the vertex
  dictionary: for any word in charged (T_3 raise x CKM) and neutral
  (gauge x 1) gates, including sums of words, the summed b -> s l l rate is
  independent of the lepton generation; a generation-dependent unitary
  phase changes nothing; only a generation-dependent amplitude interfering
  with the universal one moves the ratio, to |1 + C^mu|^2 / |1 + C^e|^2.
  Script part A; `prop:fcnc` Lean-checked.
- **CANDIDATE** The framework predicts R_K = R_K* = 1 up to lepton-mass
  and QED effects and R(D), R(D*) at their Standard Model values; the LHCb
  2022 measurements are consistent with this at p = 0.78 (chi^2 1.76/4);
  the HFLAV 2023 R(D(*)) average is 3.1 sigma away (3.4 sigma with the
  experimental correlation alone) and stands as an open falsifier.
- **CANDIDATE** Any lepton-universal deviation in b -> s mu mu is, within
  the framework, Standard Model dynamics: a new-physics universal C_9 shift
  needs a neutral mediator that `rem:no-fifth-force` and the desert
  prediction exclude.
- **STRUCTURAL** A generation-dependent coupling D is lepton-flavour-
  violating in every basis except the aligned set (Glashow, Guadagnoli and
  Lane 2015); numerically, for the paper's scenario VII, the e-mu entry of
  V^dag D V has median 0.13 and maximum 0.2511 against the bound 0.2555.
- **OPEN** Whether the interactions section's "lepton tag may couple at
  the state level" is a unitary mixing of the label (LFU preserved) or a
  label-dependent amplitude (LFU broken). PASS: JS confirms the first and
  the clause is added. FAIL: the second is intended, in which case
  `prop:neutral-blind` needs a fence and the framework has an LFU-violating
  channel to quantify.
- *Recorded, not labelled:* the anomaly the paper addresses (LFU violation
  in b -> s l l) no longer exists as of LHCb December 2022; the paper's
  scenario VIII (LFU) at 0.55 sigma was the framework-compatible one.

## 10. Files

- `scripts/b_anomaly_lepton_universality_2026-11-07T1900.py` (new; PASS;
  seed 20261107; one fix during the session: the first version inserted a
  label-diagonal phase gate and claimed it would move R_K, which it cannot
  without a second path; replaced by the two-case check now in part A).
- `knowledge/sessions/b_anomaly_lepton_universality_2026-11-07T1900.md`
  (this note).
- `bib/b_anomaly_refs_2026-11-07T1910.bib` (11 keys; 8 Crossref-verified
  by DOI; 3 arXiv-only records read directly, two of them with journal
  fields marked VERIFY-CITE; VERIFY-SUPPORT recorded per key).
- `notes/todo.md`: section "2026-11-07: the B-meson anomalies and lepton
  universality (Fable session, evening)" appended.
- Nothing in the paper patched; nothing built; nothing committed.

## 11. Exact stdout of `scripts/b_anomaly_lepton_universality_2026-11-07T1900.py`

```
=== Part A: lepton universality is the identity on the generation label ===
  [PASS] b -> s l l toy: rate independent of lepton generation for 200 random gate words (incl. 67 two-word sums)  (max relative spread 0.0e+00)
  [PASS] a generation-dependent phase gate alone leaves every rate unchanged (no second path to interfere with)  (spread 3.8e-16)
  universal amplitude plus a label-dependent one: rates [0.9874 2.5742 0.8601], R_(mu/e) = 2.6071 = |1 + C^mu|^2 / |1 + C^e|^2 = 2.6071
  [PASS] toy R_K moves off 1 exactly by the interference of a generation-dependent amplitude
  -> R_K != 1 needs an amplitude that acts on the generation label; the dictionary's gates all act as the identity there
     (prop:fcnc, prop:neutral-blind), so the framework predicts R_K = R_K* = 1 at the gauge level, with only lepton masses to break it
  [PASS] V^dag (c 1) V = c 1 for 2000 Haar-random V (prop:fcnc)  (max deviation 5.6e-17)
  V^dag D V for D = diag(-0.25, 0.211, -0.3): |e-mu entry| median 0.1303, 90th percentile 0.2100, max 0.2511; zero only on the aligned set
  (the maximum possible |e-mu| entry is (max D - min D)/2 = 0.2555)

=== Part B: the data against R = 1 (framework = SM at the gauge level) ===
  LHCb 2021 (Nature Physics 18, 277), R_K central bin 1.1 < q^2 < 6 GeV^2:
    R_K = 0.846 +0.042/-0.039 +0.013/-0.012  -> pull from 1: -3.42 sigma (sigma_tot 0.045; LHCb quote 3.1 sigma with their likelihood)
  LHCb 2022/2023 (PRL 131, 051803; PRD 108, 032002), four bins:
    R_K   low     0.1 < q^2 < 1.1: 0.994  -> pull -0.06 sigma
    R_K*  low     0.1 < q^2 < 1.1: 0.927  -> pull -0.73 sigma
    R_K   central 1.1 < q^2 < 6.0: 0.949  -> pull -1.05 sigma
    R_K*  central 1.1 < q^2 < 6.0: 1.027  -> pull +0.35 sigma
    chi^2 against R = 1 over four bins: 1.76 for 4 dof, p = 0.78
  [PASS] LHCb 2022 four bins consistent with R = 1 (p > 0.05)  (p = 0.78)
    (R_K* low bin against the SM's 0.98 instead of 1: pull -0.53 sigma)
  HFLAV 2023 averages (arXiv:2411.18639v2, Fig. in sec. 6.6): R(D) = 0.342 +/- 0.026, R(D*) = 0.287 +/- 0.012, rho = -0.39;
    SM: R(D) = 0.298 +/- 0.004, R(D*) = 0.254 +/- 0.005 (HFLAV's own SM averages)
    chi^2 = 14.8 for 2 dof, p = 6.1e-04, i.e. 3.4 sigma with the experimental correlation only (HFLAV quotes 3.1 sigma with the SM correlation included)
    individual pulls: R(D) +1.67 sigma, R(D*) +2.54 sigma
    LHCb 2023 alone (PRL 131, 111802): R(D*) = 0.281 +/- 0.018 +/- 0.024, R(D0) = 0.441 +/- 0.060 +/- 0.066, 1.9 sigma combined (their statement)
    Belle II 2024 (arXiv:2401.02840): R(D*) = 0.262 +0.041/-0.039 +0.035/-0.032, consistent with the SM (their statement)
  [PASS] R(D), R(D*) tension with R = SM is above 3 sigma on HFLAV 2023 numbers (the framework predicts none: open falsifier)  (3.4 sigma)

=== Part C: the paper's fit decomposed into what the framework can and cannot carry ===
  Scenario IV (e, mu): C_lq = [-0.25  0.24  0.  ]
    S_3-invariant (generation-blind) part: -0.003 x (1,1,1)   -- the only shape a dictionary gate can have
    traceless (LFU-violating) part: [-0.247  0.243  0.003], norm 0.347 vs invariant norm 0.006
  Scenario VII (e, mu, tau): C_lq = [-0.25   0.211 -0.3  ]
    S_3-invariant (generation-blind) part: -0.113 x (1,1,1)   -- the only shape a dictionary gate can have
    traceless (LFU-violating) part: [-0.137  0.324 -0.187], norm 0.398 vs invariant norm 0.196
  The paper's own LFU scenario VIII (C^e = C^mu = C^tau) has pull 0.55 sigma from the SM; its IX (e = -mu = tau) has 5.54 sigma:
  the 2021 anomaly lived entirely in the traceless part, which is the part no gate of the dictionary can produce.
  Post-2022: Alguero et al. 2023 find the LFUV fits at 1.2-1.5 sigma and a universal C9 shift of about -1.2 at 4.6-5.8 sigma;
  Ciuchini et al. 2023 find the same data consistent with the SM once charm-loop rescattering is fitted (C9^NP,mu 95% HPDI [-1.06, 1.01]).
  A universal C9 shift is generation-blind and so is not forbidden by prop:fcnc; but as new physics it would need a new neutral
  mediator, which rem:no-fifth-force excludes, so within the framework it can only be Standard-Model dynamics (the charm loop).

B ANOMALY LEPTON UNIVERSALITY: PASS
```
