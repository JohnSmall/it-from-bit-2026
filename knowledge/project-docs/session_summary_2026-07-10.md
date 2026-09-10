# Session Summary / Onboarding: 2026-07-07 to 2026-07-10

Purpose: onboard a fresh conversation. This session ran from Paper 1's final-pass completion
through the fez hardware batch, the superconductor witness, Paper 2's launch, the sedenion
three-generations mechanism, and the up-quark candidate. Companion documents from this session
(all in project/outputs, referenced not duplicated here):
`higgs_entanglement_superconductor_2026-07-07.md`, `paper2_metric_identification_2026-07-07.md`,
`hardware_results_fez_2026-07-10.md`, `sedenion_generations_mechanism_2026-07-10.md`.

## 1. Paper 1 state: COMPLETE except JS's framing prose

Twenty sections + four appendices; every cross-reference verified repeatedly. Awaiting ONLY:
introduction, abstract, preamble check, conclusions -- all JS's voice, audit on arrival.
New \input lines JS must confirm in main.tex: `fanout_boundary_section_2026-07-06` (between
sections 4-5), `superconductor_witness_section_2026-07-07` (between boson-masses and
interactions), `summary_section_2026-07-07` + `headline_results_snippet_2026-07-07` (end),
`appendix_hardware_fez_2026-07-10` (after the three-computations appendix).

This session's paper additions: (a) the superconductor witness section (dictionary's Bell/product
rows = the two strata of Anderson-Higgs; Elitzur = fibre privacy, the Meissner/Josephson split
mapping 1:1 onto private/recoverable phase; Fan-Lloyd identity as the anchor; mass-as-debt =
London stiffness; thin spectrum = op:fanout-selection's solvable toy; three stitches into
classes/boson-masses/fanout; summary brought current, supports count now FOUR, companions FIVE).
(b) The discovery-narrative subsection `sec:sedenion-announcement` in the zoo (K3's rough edge ->
the circuit forcing the extra wire -> the sedenion mechanism at candidate status; "the executable
representation refused to let the rough edge stay hidden"); op:filatov-extension gained the
dissolution-route clause. (c) The hardware appendix + six body stitches (see section 3). (d) The
up-quark candidate (see section 5). RIS batches delivered this session: gw_energy (Bondi,
Isaacson), higgs_entanglement (Anderson 1963, Fan-Lloyd 2005, van Wezel-van den Brink,
Poniatowski), brown_ref (Brown 1967, VERIFY on import), fanout_refs earlier. All need Mendeley
import by JS.

## 2. Paper 2 state: launched, compilable skeleton

`paper2_main_2026-07-07.tex`: "It from Bit via Godel, II: Spacetime from the FANOUT Boundary".
Drafted: the Margolus-Levitin/de Broglie Rosetta ((E,p) = step-count densities, hbar the exchange
rate); GR-energy dissolved (E = count-rate along a locked direction; Aoki's Noether-2 as the gauge
face; surviving charge = entropy current); THE GW OBJECTION ANSWERED IN-SECTION (Bondi mass-loss
theorem-grade at the locked boundary; Isaacson valid only after averaging; JEWEL: "Isaacson's
averaging scale = the chart re-emergence scale"; pseudotensors = junk because point-local in the
tipping bulk; conservation = bookend balance); the four-constant junction (delta Q/T = k_B ln2 dN
= (k_B c^3/4G hbar) dA; hbar and k_B cancel -- SELF-CHECK RULE: no final geometric equation may
contain hbar or k_B; G = the bit's area, natively 1); Dorau-Much positioned (their hypothesis =
our conjecture's conclusion; their ontology gap dissolved as post-FANOUT epistemic-made-rigid);
gravity-lives-post-FANOUT with the BMV/Penrose discriminator table. Seven open problems
(op:p2-pressure now carries Isaacson back-reaction as flagship). Next computation: the Newtonian
limit (op:p2-newton).

## 3. Hardware: the fez batch, five for five (ibm_fez, Heron r2)

Notebooks G (monogamy: tau=1, C=0 -- noise-ROBUST, the I/2-attractor honesty clause owed in any
appendix use), H (two-gluon: <XX> = +0.915, the copy-tensor discriminator fired), J (the ninth:
r^2 = 0.0935 vs 1/9, the -16% IS the depolarisation prediction; C = 0.016 = the Wootters floor;
job d98cnvaf47jc73a7ooog), K (CKM core: rung 1 |V_us| = 0.233 within 6%; lambda^4 elements AT the
~2% noise floor; leakage 2.2%; job d98cm0d2su3c739j4ang), L (mini-Meissner: +0.2864/-0.0167/-0.2948
vs +-1/3; THE SIGN FLIP MEASURED; V ~ 0.87; the measured correlator IS a measured tangle 0.859 --
"one number wearing both names"; job d98gtvgtcv6s73dm4cmg). All routed into Paper 1:
`appendix_hardware_fez_2026-07-10.tex` (labels app:hw-monogamy/-two-gluon/-ninth/-ckm/-meissner)
plus stitches in confinement (x2), interactions, witness ("carried out"), predictions, summary.
FINAL: G, H, L. OWED: J mitigated rerun; K-v2 = ANGLE AMPLIFICATION (apply the rung rotation n
times, divide) for the small CKM elements.

Notebook conventions established: .py + .ipynb pairs (converter script exists); real SamplerV2
hardware blocks (mode=backend, ISA transpile, res[i].data.c.get_counts(), job-id printed,
HW_SHOTS = 8192); exit only on failure (Jupyter-clean); PASS/FAIL printed per check. Environment:
pip install qiskit-aer and qiskit-ibm-runtime (hyphens) in JS's Docker; qiskit 2.5.0 verified.

## 4. The sedenion programme (the session's conceptual centre)

JS's criticism: K3 smuggles rung-distinguishability (the canonical orbits are permutation-
symmetric; the odd-qubit reading imports tower identity underived). Corrected form recorded
(labeled subsystems CAN entangle; the real tension is symmetry vs label). THE MECHANISM:
Aut(O) = G2 has NO S3; Aut(S) = G2 x S3 (Brown 1967) -- the doubling PROMOTES triality to a
manifest symmetry. Generations = the S3-orbit of three octonion subalgebras; sterile = the
invariant sector; shared H core = why identical EW numbers per generation; THE EXTRA QUBIT IS THE
WIRE ON WHICH TRIALITY FINALLY ACTS. K3 = the register-level shadow (shadow theorem = the
keystone conjecture, Fano lines the published half). Division of labour: sedenions own count +
label; Filatov keeps chirality + doublet. op:filatov-extension SHRINKS (companion clause
dissolves if the shadow theorem lands). New mint: generation number as an APPROXIMATELY conserved
charge (grading degree), violated only in the zero-divisor sector => CKM near-diagonality as
near-conservation.

NOTEBOOK M EXECUTED (the skeleton scan) -- structural results ALL PASS, paper-grade:
- Explicit triple: S = H (+) V1 (+) V2 (+) V3, V1 = <e1,e5,e9,e13>, V2 = <e2,e6,e10,e14>,
  V3 = <e3,e7,e11,e15>, core H = <e0,e4,e8,e12>; exhaustive over core-doublings.
- THE GRADING THEOREM: V_i V_i c H, V_i V_j c V_k cyclic -- generations are an S3-GRADING of
  the algebra itself.
- sigma (order 3) and tau (involution) CONSTRUCTED BY HAND, verified on all 256 pairs.
  (Constructor lesson: needs 4 generators {e4,e8,e1,e2}; core rotation must be allowed.)
- THE ZD-DIAGONAL DISCOVERY: (a + sigma a) is an isometry; true zero divisors are
  z = (a + sigma(e8 a))/sqrt2 -- MIXING = (TAG FLIP) x (GENERATION STEP), kernels dim 4.
  The extra wire's necessity is now theorem-grade.
- ANGLE VERDICT (pre-registered, 18 comparisons): NO 2/9 in the skeleton. T1 = 0 identically
  (sigma is phase-blind to core complex structures), T2 = pi/4 exactly, T3 = 1/4.

## 5. The up-quark candidate (installed at recorded status)

m_u = (1 - delta0) x 2.78 = 2.162 MeV vs PDG 2.16 (+0.10%) -- the Koide angle's FOURTH role
(lepton Koide; dilution numerator; lambda = sin(2/9); the gen-1 admixture). Found by a DISCLOSED
eight-candidate scan; linear in delta0 = the hardware-verified first-order response; sign from
level repulsion; the op's old "some twenty per cent" was 2/9 = 22.2% unrecognised. Installed:
masses paragraph + op:up-quark sharpened ("derive why the leakage angle equals delta0, with the
sedenion cross-algebra sector the candidate home, or refute") + verification-script check PASS.
Caveats recorded: PDG band wider than the hit; multiple comparisons. Discrepancy precision
corrected +29% -> +28.5% throughout. The skeleton scan (notebook M) did NOT find the angle =>
THE SHARPENED TARGET: **the dressed mass operator** -- the associator-debt functional on
C (x) S, selected direction inside the generation sector, GHZ/W register dressing, compute the
generation-one first-order shift. Equals -delta0 or the candidate dies. This is the next climb.

## 6. Conventions (unchanged, enforced)

British English; \autocite; statuses proved/structural/owed/open never upgraded; bash-python
patches with asserted anchors (GREP FIRST on any wording not written this session -- repeated
lesson); scripts print PASS/FAIL; outputs to /mnt/user-data/outputs; /mnt/project read-only;
op:filatov-extension content is Filatov's (pointer clauses only); RIS with confirm-notes, native
Unicode accents, ID = citekey, one author per AU line; pure-ASCII files; no bullets in paper
prose (exceptions stand: neutrino table, headline list, discriminator table).

## 7. Numbers bank (current)

v = 246.220 GeV (the single dimensional input); m_H = v/2 (-1.71%); y_t = 1 (+0.93%);
sin^2 theta_W: 1/4 -> 0.2312 vs 0.23122 (matching ~3.6 TeV = 14.6 v); delta0 = 2/9 (FOUR roles);
lambda = sin(2/9) = 0.2204; up: (1-delta0) x 2.78 = 2.162 vs 2.16 (+0.10%); Sigma m_nu ~ 52 meV,
m_1 = 0, NO; theta_QCD = 0; alpha_s(M_Z) 0.1185 vs 0.1179; ledger 8/9, slack = r^2 = 1/9
(CKW-saturated; the ninth is base presence, the r-channel); junction delta Q/T = k_B ln2 dN =
(k_B c^3/4 G hbar) dA, A_native = -S; Popper II p.187; Aoki J = entropy current; fez jobs
d98cnvaf47jc73a7ooog / d98cm0d2su3c739j4ang / d98gtvgtcv6s73dm4cmg.

## 8. Next steps (ordered)

1. JS: framing prose (intro/abstract/preamble/conclusions) -> audit on arrival; Mendeley imports
   (gw_energy, higgs_entanglement, brown, fanout batches); main.tex \input lines confirmed.
2. THE DRESSED MASS OPERATOR (checklist 3b in the sedenion doc) -- the up-quark derivation-or-
   refutation; notebook M's skeleton is fully prepared; start cold and rested.
3. K-v2 (angle amplification) + J mitigated rerun -> slot into the appendix's priced sentences.
4. The shadow theorem (S3 projected through the selected C reproduces the K3 classes; Fano-line
   correspondence first); refs-first: Brown 1967 verified, GG triple against M's construction.
5. Paper 2: the Newtonian limit (op:p2-newton) as the first computation; preamble sync with
   Paper 1's conventions.
6. Standing suite: eight papers + the Anderson-Higgs dictionary companion; Vaxjo items for
   Svozil (Hardy continuity) and Khrennikov (adelic constraints) unchanged.
