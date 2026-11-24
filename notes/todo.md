# To do

Actionable items with enough context to act on without reconstructing the
reasoning. Delete when done.

## Manuscript

- [ ] Spacetime dimensionality now appears twice in the introduction: as a
      structural derivation in `Principal Results`, and as a hedged glimpse
      (op:three-dimensions) in the headline list spliced after it. That may be
      deliberate -- the same result seen structurally and numerically -- or it
      may read as repetition. Worth a look when reviewing the finished paper.
- [ ] Check the cross-reference from `predictions_section` line 227 ("no
      experiment will ever hold a record of indefinite causal order") through
      to the qualified statement in `sec:no-quantised-gravity`. That
      qualification now carries more weight, see `ideas.md`.
- [ ] Complete the four framing prose sections for Paper 1 -- introduction,
      abstract, preamble check, conclusions. Named in the project memory as
      the only thing between Paper 1 and arXiv submission.
- [X] Import `bib/koide_attribution_refs_2026-09-11T2011.bib` into Zotero and
      re-export, then credit the phase in the masses section. Both references
      are now verified and the VERIFY-CITE is cleared: Brannen 2006 (read in
      full) and Sumino 2009 (Crossref and arXiv). Brannen turns out to carry
      more than the number -- the circulant Hermitian form with
      lambda_n = mu(1 + 2 eta cos(delta + 2 pi n/3)), eta^2 = 1/2 (the
      framework's alpha = sqrt2) and delta_1 = 0.2222220(19) -- so it is the
      complex precursor of prop:koide-jordan, not only of delta = 2/9. How
      much to credit, and where, is JS's call; see the 2026-09-11T2011
      session note.

- [ ] The `\medskip` summary closing `sec:spacetime-open-problems` in
      `paper1/spacetime_from_non-computability.tex` enumerates the prospects by
      name and now under-counts: the two loops/renormalisability paragraphs
      spliced on 2026-09-11 are not mentioned. Which prospects to name there is
      an editorial call.
- [ ] TeX-style ``...'' quoting survives in 20 files across paper 1 (77
      instances), predating the move to `\enquote{}`. Converting is mechanical
      but touches most of the paper, so worth doing as one deliberate pass.

- [ ] Paper 1 v2: the complex-cost revision. Eleven insertions with target
      passages, drafts, labels and order of work are in
      `notes/paper1_v2_complex_cost_revision_plan_2026-09-18T1000.md`;
      needs a v2 branch from the Zenodo tag first, then nine references
      verified and batched (plan section 13), then the patches in the
      order of section 14. JS, 2026-09-18: "these are important
      clarifications that need to be in paper 1 (version 2)". 2026-09-20:
      items 1 and 2 applied on the main working tree at JS's instruction
      (two patch scripts, .bak files beside the targets), uncommitted and
      unbuilt; build, then decide whether to branch from `paper1-v1` before
      committing. See `knowledge/sessions/born_cost_ledger_patch_2026-09-20T1000.md`.
- [ ] Paper 2, causal-order section: the Oreshkov--Costa--Brukner TODO
      paragraph and the "theorem target" now have a draft basis in
      `knowledge/project-docs/indefinite_causal_order_fanout_2026-09-19T0900.md`
      (section 5 lists what the section gets; section 3 is the toy proof with
      its table). Also there: op:ico-threshold, whether causal nonseparability
      of the graded switch dies at finite redundancy, needs an SDP solver
      (cvxpy) in the Python environment the Opus session is setting up; and
      the thermodynamics-of-the-switch references to verify and batch
      (section 8). The predictions-section item above ("no experiment will
      ever hold a record") should be re-read against it: the phase decays
      asymptotically, the order possibly at a finite threshold.
- [ ] Paper 1, the baryon-number sentences (predictions section, "which the
      framework gets for free"; the absent-gate section): the Standard Model
      violates B+L non-perturbatively above the electroweak crossover
      (sphalerons). Either locate the anomaly in the gate dictionary and say
      "perturbatively", or own the conflict. Proposed as op:sphaleron in
      `knowledge/project-docs/records_causal_structure_high_temperature_2026-09-20T1400.md`
      section 2. JS to rule before v2. Answered in outline 2026-09-20T2000 in
      `knowledge/project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md`:
      the sphaleron is collective and topological, outside SLOCC's single-register
      scope, so the GHZ/W split stays as the perturbative statement; the two
      sentences get "perturbative" and a pointer; op:sphaleron restated with
      PASS/FAIL (section 6 there); op:baryon-contact may be the same object.
      Applied to the paper 2026-09-20T2100 (absent-gate subsection and
      predictions section; op:sphaleron minted in the text for JS to keep or
      strip; uncommitted, unbuilt). The two-copy conversions are constructed
      and run as Qiskit circuits (note sections 9 and 12); add them to the
      IBM hardware task. Import `bib/sphaleron_slocc_refs_2026-09-20T2100.bib`.
      2026-09-20T2300: multi-copy SLOCC references verified (Fable, against
      arXiv) and batched in `bib/multicopy_slocc_refs_2026-09-20T2300.bib`;
      the sphaleron batch verified by Opus (section 13 of the note), with the
      't Hooft two-generation discrepancy and a proposed one-sentence fix for
      JS to accept or decline. Import both batches; the Opus 2200 duplicate is
      atticked.
      2026-09-21: the circuits are gauge-blind (sphaleron note section 16); a
      gauge-faithful version needs the charge operators on the register from
      the quantum-numbers section and a gate set restricted to commute with
      them. Proposed as the next computation, after JS's ruling. 2026-09-21T0900:
      the scope statement is in the paper (patch_circuit_scope_statement), with
      the gauge-respecting circuits promised for a subsequent paper; that
      promise is now a commitment to track here.
      2026-09-21T1100: sterile neutrinos and the sphaleron route (note section
      18): steriles are outside the vertex; leptogenesis runs the other way;
      the framework's two steriles at 3.6 TeV need degeneracy to ~1e-6 for
      resonant leptogenesis, a prediction-or-refutation once op:matching-scale
      gives their splitting. JS to rule Majorana or Dirac (it decides whether
      B-L is a surviving record).
      2026-09-21T1200: do non-interacting steriles gravitate (note section 20)?
      The 3.6 TeV steriles thermalise via the Yukawa at T ~ M (K ~ 47) and
      decay in ~1e-15 s, so they are recorded and are not dark matter; the
      framework's answer for anything else is that conserved energy-momentum
      is a persisting record and the field between events is delocalised.
      JS to say whether the steriles are meant to be stable.
- [ ] **Boundary, JS's ruling 2026-09-21:** what gravitates when nothing has
      been recorded is a genuine boundary where the framework may make no
      prediction. Note `knowledge/project-docs/boundary_gravity_of_unrecorded_matter_2026-09-21T1300.md`;
      op:sterile-gravity restated with PASS/FAIL and a boundary sentence for
      the spacetime section, drafted and anchor-checked, NOT RUN:
      `scripts/patch_op_sterile_gravity_boundary_2026-09-21T1300.py`. Applied
      2026-09-23 at JS's instruction, together with the op:sphaleron revision
      (`patch_op_sphaleron_revised_2026-09-21T1000.py`); both uncommitted and
      unbuilt; the ledger entries are proposed in the notes.
      Paper 1 (tick-rate) and Paper 2 (post-FANOUT) currently disagree on
      what gravitates; the dictionary must choose.
- [ ] Paper 2, the TODO paragraph on "the equation-of-state moral's history
      (Jacobson's own caveats; Padmanabhan's atoms of spacetime)" at the end
      of the ontology section: a draft in the paper's register is in
      `knowledge/project-docs/jacobson_non_equilibrium_spacetime_2026-09-20T1600.md`
      section 7, with op:p2-nonequilibrium (section 6) to mint beside it.
      Needs Eling--Guedens--Jacobson 2006, Chirco--Liberati 2010, Jacobson
      2016 and Padmanabhan 2010/2012 read and batched first (all cited from
      memory there).

## Paper 2

- [ ] **Before any Paper 2 drafting, read**
      `knowledge/project-docs/paper2_revisit_complex_cost_thread_2026-09-20T1900.md`.
      JS, 2026-09-20: "Make sure this conversation is to be revisited when we
      work on paper 2." It indexes the seven notes of the complex-cost thread
      (mass as imaginary cost rate, the two columns, order as a record, the
      temperature in Landauer, records at high temperature, Jacobson's
      non-equilibrium spacetime, gravity and the Planck scale), the drafts
      ready for the Paper 2 TODOs, three proposed open problems and the checks
      owed. Comments beside the relevant TODOs in `paper2_main_2026-07-07.tex`
      point to the same hub.

- [X] open_problems.md listed "Notebook T ... Z/2 vs S_3" as outstanding;
      settled on the S_3 side 2026-08-27 and confirmed by an identical re-run
      2026-09-23 (notebooks/notebook_T_output_2026-09-23_rerun.txt). Closed by
      JS 2026-09-23 with a dated entry in open_problems.md.

## Aaronson citation

- [ ] Re-export `self-ref-2026-cited` once more: `Aaronson:dem` changed again
      after the export of 2026-09-12. Chapter 9 is now carried as a citation
      postnote rather than a `chapter` field, which is the biblatex idiom and
      nearer to the "[Aaronson, Ch 9]" he asked for. The Zotero item went from
      bookSection to book and the `tex.chapter` Extra was removed, both via the
      local API, so it exports as a plain `@book`; the three citations in
      `what_is_a_quantum_state.tex` now read
      `\autocites{aaronson_lect9}[ch.~9]{Aaronson:dem}` at the two two-key
      sites and `\autocite[ch.~9]{Aaronson:dem}` under the block quotation
      (patch 2026-09-12T1300). `paper1/references.bib` still holds the older
      `@incollection` with `chapter = {9}`, so a build before the re-export
      prints the wrong shape. Wants a build afterwards: `\autocites` is used
      here for the first time in the paper.
- [ ] Reconcile the gloss at `paper1/what_is_a_quantum_state.tex` line 97,
      "Accept negative probability as a fact", with his own position. His email
      of 21 June 2021 states there are no negative probabilities for actual
      events: the generalisation is to negative and complex *numbers*, the
      amplitudes, with probabilities remaining real in [0,1]. The direct
      quotation in that passage is accurate; the gloss around it is not. His
      correction is already the framework's position -- signed entries are
      internal bookkeeping, observable entries stay honest probabilities -- so
      aligning the two costs nothing and closes an obvious line of attack on a
      paper whose project is named "negative probability".
- [X] Do NOT cite him as a personal communication. He named a public source,
      and ICMJE says to avoid personal communications where one exists. If a
      personal-communication citation is ever wanted anyway, ICMJE requires
      "written permission and confirmation of accuracy from the source" -- the
      same rule the Abramsky provenance note already applies.

- [ ] op:parallelisable-renormalisable, proposed 2026-09-27 (Tang reading note
      section 7): PASS/FAIL for the paper's question "does parallelisability
      determine renormalisability?", the one-loop self-energy as a winding sum
      with bounded phase. JS to mint or decline. Tang 2025 is not support for it.
      2026-09-27T1100: attempted (`scripts/self_energy_winding_recast_2026-09-27T1100.py`,
      note `knowledge/sessions/parallelisable_renormalisable_attempt_2026-09-27T1100.md`):
      FAIL for the winding sum, the bounded phase and the compact momentum
      space; a compact fibre bounds the phase and discretises the modes, the
      divergence is the number of modes. The finiteness reading is closed; the
      paper's removability question is untouched. Restate the problem before
      minting: removability from settlement at the record, not finiteness.

- [ ] v2 wording pass: wherever the paper says "complexified" quaternions/
      octonions/sedenions, decide whether Furey's C (x) A is meant or the real
      algebra with the amplitude's complex structure (the framework's own,
      lem:cproj); the complexified algebras have zero divisors from H onward.
      `knowledge/sessions/complexified_vs_complex_structure_2026-09-27T1400.md`.

- [x] v2 wording, spacetime section "Three dimensions of space": "the same
      non-associativity forbids a metric outright" -> "forbids a metric built
      from the sphere's own composition law outright", so a reader does not take
      it as the claim that R^8 has no metric; and one clause noting that
      SL(2,O) = Spin(9,1) is the unsplit ten-dimensional option the
      computability split declines. Session note
      `complexified_vs_complex_structure_2026-09-27T1400.md` section 5.
      DONE 2026-09-27T1800, revised T1900, applied uncommitted, together with
      two new paragraphs in `sec:comp-distance`: the antitelephone inversion
      (JS: readers in the standard order "might miss the inversion and then get
      confused when we dismiss octonionic spacetime") and JS's many-observer
      antitelephone network (consistency is associativity; two links always
      compose, three only in a quaternionic subalgebra, so the largest
      consistent network in S^7 is an S^3):
      `scripts/patch_spacelike_inversion_2026-09-27T1800.py`, three edits on
      `paper1/spacetime_from_non-computability.tex`; numerical check
      `scripts/antitelephone_network_associativity_2026-09-27T1900.py` (PASS,
      stdout in the note). Session note sections 6a and 6b. Owed: build (two
      new keys undefined until imported); VERIFY-SUPPORT on conway_2003 (Artin)
      and harvey1982calibrated (associative 3-planes), flagged in a %% comment;
      JS to read the paragraphs; commit.

- [ ] Import `bib/tachyonic_antitelephone_refs_2026-09-27T1800.bib` (keys
      `tolman1917theory`, `benfordbooknewcomb1970tachyonic`); metadata verified
      against Crossref and archive.org, texts not read, so both VERIFY-SUPPORT
      for the closed-loop consistency argument they are cited for.

- [ ] **Burton--Anwar (Quantinuum, arXiv:2605.06251) read 2026-10-03**, note
      `knowledge/sessions/burton_anwar_meromorphic_reading_2026-10-03T1600.md`,
      script `scripts/burton_anwar_meromorphic_check_2026-10-03T1600.py` (PASS).
      Four v2 wording items, JS to rule (note section 6):
      (1) `sec:hopf-compositional`, second Burton--Anwar sentence: "the classical
      structures live in exactly the data their projectivisation forgets" is
      overstated (their Prop. 3.1: the monoids survive; the section data is what
      is forgotten); corrected sentence drafted in note section 4. Second-order
      finding on an existing citation; not edited around.
      (2) entanglement-classes section, special/anti-special sentence: one clause
      "read projectively the two algebras are multiplication and addition on the
      Riemann sphere" citing coeckekissingermerryroy2011ghzw and
      burtonanwar2026meromorphic.
      (3) spacetime section, celestial-sphere sentence: one clause that the
      complementary pair projectivises to rotation-and-boost monoids about two
      perpendicular axes, the X-spider's law being Einstein velocity addition.
      (4) optional: cite gharahimanciniottaviani2020finestructure beside
      Duer--Vidal--Cirac as the algebraic-geometric form of the classification.
      Import `bib/ghzw_arithmetic_segre_refs_2026-10-03T1700.bib` (two keys,
      metadata verified, both VERIFY-SUPPORT). Do NOT import
      `bib/burton_anwar_meromorphic_ref_2026-10-03T1600.bib`: the key is already
      in the library; the file is the support record.

- [ ] **Cosmology paragraph (2026-10-07)**: the spacetime section's "spatially
      infinite, and being a network without a boundary, naturally flat" and
      "infinitude settles flatness" are wrong (an open universe is infinite and
      never flat; flatness is a Friedmann fine-tuning the framework has not
      derived). The flatness sentence is FIXED at JS's ruling (2026-10-07T1400,
      "infinite therefore flat or negative curvature"), applied uncommitted by
      `scripts/patch_infinite_not_flat_2026-10-07T1400.py`. Unrun patch replacing
      the rest of the paragraph, re-anchored and anchor-checked:
      `scripts/patch_inflation_paragraph_2026-10-07T1300.py`; it also states the
      horizon answer as a claim about initial data (not "same laws"), separates
      background from fluctuations, and adds the no-inflationary-tensors
      prediction. Note `knowledge/project-docs/inflation_horizon_infinitude_2026-10-07T1200.md`,
      script `scripts/inflation_debts_at_framework_scales_2026-10-07T1200.py`.
      Import `bib/inflation_alternatives_refs_2026-10-07T1300.bib` (seven keys;
      six arXiv-verified, Penrose 1979 VERIFY-CITE; all VERIFY-SUPPORT). JS to
      rule on the patch; ledger entries proposed in note section 9.

- [ ] **Twistor space and the Hopf maps (2026-10-07)**, note
      `knowledge/sessions/twistor_hopf_maps_2026-10-07T1600.md`, script
      `scripts/twistor_hopf_factorisation_2026-10-07T1600.py` (PASS). For JS to
      rule, no patch drafted: (i) `sec:hopf-compositional`, "the SU(2) fibre of
      S^7 -> S^4 carries exactly the entanglement that survives local
      operations" has fibre and base reversed (the fibre is the second qubit's
      local unitaries; the base carries the first qubit's Bloch vector and the
      concurrence); corrected sentence in note section 4. (ii) Credit Penrose's
      twistor programme where the Minkowski-i conjecture is stated. (iii)
      Optionally name the two-qubit bundle as the twistor fibration. Import
      `bib/twistor_refs_2026-10-07T1700.bib` (six keys; five Crossref-verified,
      Penrose--MacCallum VERIFY-CITE; all VERIFY-SUPPORT). Added T1900 (note
      section 9, script `scripts/twistor_chirality_filatov_2026-10-07T1900.py`,
      PASS): the two Hopf fibrations of S^7 are twistor and dual twistor
      space, unitary versus antiunitary (spin-flip) fibre; Filatov's
      inversion is det T = -C^2 for every entangled pure pair; the
      opposite-handedness is the partial-transpose criterion. (iv) For
      `sec:frame`: one sentence naming the topological fact; (v) the Filatov
      datum has strength C^2 (op:filatov-extension); (vi) chirality is fixed
      by the choice of complex structure (op:chirality). Import
      `bib/peres_horodecki_wootters_refs_2026-10-07T1930.bib`. Literature
      search (note 9c): det T = -C^2 is Filatov--Auzinsh June 2026 (arXiv
      2606.12637, eq. 33), the partial transpose as a reflection is Gamel 2016
      and Avron--Kenneth 2009, the handedness is Altepeter 2009 / James 2022,
      the left/right SU(2) on the Hopf bundle with twistor space is Chin--Lee
      2014; the JOIN (handedness = twistor chirality, same-handed = partial
      transpose) is not found. Import
      `bib/handedness_twistor_prior_refs_2026-10-07T2359.bib` (eight keys)
      before any of section 9 goes into the paper, and cite accordingly. Added T2100
      (note section 9a, script `scripts/w_triangle_chirality_holonomy_2026-10-07T2100.py`,
      PASS): canonical W has det T = -4/27 on every edge and Z_2 holonomy -1
      (the K_3 frustration as a number); canonical GHZ has det T = 0 on every
      edge; LU-invariant, NOT SLOCC-invariant (a quarter of W-class images
      have a proper edge while entangled). (vii) `sec:frame`: "an entangled
      pair forces opposite handedness" is a pure-state / canonical-orbit
      statement; add the qualifier. Ledger entries proposed in 9a.

- [ ] **Koide phase and the edge-triple associator (2026-10-07T2200)**, note
      `knowledge/sessions/koide_phase_associator_triple_2026-10-07T2200.md`,
      script `scripts/koide_phase_associator_identity_2026-10-07T2200.py` (PASS).
      Identity: the cubic term of cos Phi is the associative 3-form phi of the
      three edge directions, and phi^2 + |assoc|^2/4 = vol^2, so the associator
      of the edge triple is the calibration shortfall inside the Koide phase.
      The paper's Bargmann reading is the associative regime; JS's W-register
      triple is the non-associative one; the spectrum cannot tell them apart
      (no route to delta; closed routes untouched). For JS: (i) ledger entry
      for the identity; (ii) one clause in op:koide-delta's constraint naming
      the two regimes; (iii) the regime shows in eigenframes/mixing, a
      computation for the generation-transitions thread, not attempted.

- [ ] **Note to Filatov and Auzinsh (2026-10-08)**: JS asked for a brief PDF
      note on the handedness/twistor link and the prior work neither of their
      papers cites. Source `notes/correspondence/filatov_handedness_twistor_note_2026-10-08.tex`
      (standalone article class, manual bibliography, builds clean with
      latexmk in its own directory; the PDF is gitignored). Four pages: the
      observation, the prior literature (Altepeter, James, Gamel,
      Avron--Kenneth, Mosseri--Dandoloff, Levay, Chin--Lee), the two-qubit Hopf
      dictionary, the two chiralities, handedness = chirality via the partial
      transpose, a three-qubit remark (W edges det T = -4/27, Z_2 holonomy -1;
      GHZ edges 0; LU- not SLOCC-invariant). Rewritten 2026-10-08T1800 at
      JS's request in a friendly letter tone (Stanislav is a Vaxjo friend with
      an active exchange): directions his picture can go rather than gaps;
      added a section reading the two spheres as counterfactual observers
      (interaction-free measurement; spacelike separation as counterfactual
      observation), and his 2024 stabiliser paper in the references. Previous
      version kept as `.v1.tex.bak` (gitignored). JS to send; commit the .tex.

- [ ] **Woit's right-handed spacetime (2026-10-08)**, note
      `knowledge/sessions/woit_right_handed_spacetime_2026-10-08T1000.md`, script
      `scripts/woit_chirality_two_qubit_isotropy_2026-10-08T1000.py` (PASS).
      Verified: at a point of the two-qubit Hopf base the isotropy Spin(4)
      splits by a chosen complex structure into U(1) x Sp(1) = U(2) (Woit's
      electroweak group; the paper's fibres); which Sp(1) is unitary depends
      on the complex structure and partial conjugation swaps them (= Filatov
      handedness). Reading (CANDIDATE): weak chirality and spacetime chirality
      are one selection, the record's i; the spacetime chirality contains time
      reversal. JS's arrow (weak -> relations -> spacetime) and Woit's are the two
      charts (relational, fixed-background), related by the partial conjugation
      of one qubit; the common cause is the chart-invariant (note section 8). Section 9:
      the paper's `sec:fanout-direction` already claims measurement selects
      the direction (CANDIDATE); the computation shows this fixes the
      continuous part (which i within a chirality, the Higgs direction) and
      not the discrete part (left or right type = handedness), which stays
      op:chirality. Wording owed there: one sentence separating the two. For JS: one sentence citing Woit in the SL(2,A) paragraph
      or op:chirality; import `bib/woit_twistor_refs_2026-10-08T1100.bib`.

- [ ] **Observer defined by the selection of i (2026-10-08T1500)**, note
      `knowledge/sessions/observer_defined_by_selection_2026-10-08T1500.md`.
      JS: no observer without the possibility of observing, so selecting an i
      defines what an observer is; extends Mueller's first-person perspective.
      In the paper's objects: observer = carrier of a classical structure =
      committed direction (prop:f1-dictionary) = complex structure (twistor
      note section 4); converse of the self-reference section's derivation of
      i from the observer; the two form definition and derivation. Consequence
      (CANDIDATE): observers in one network share the chirality of spacetime
      while differing in preferred direction. Section 5 (T1700): the
      counterfactual possibility of observation is the section data = the
      imaginary column; interaction-free measurement is that column made
      visible; the counterfactual records between observers are spacelike
      separation (antitelephone loops); possibility is not definiteness.
      Import `bib/interaction_free_measurement_refs_2026-10-08T1700.bib`.
      For JS: a definition sentence
      (drafted, note section 4), a ledger entry, and reading Mueller 2020 before
      "extends Mueller" is printed. Import
      `bib/mueller_law_without_law_ref_2026-10-08T1500.bib`.

- [ ] **Spinor, twistor, place (2026-10-08T2100)**, twistor note section 11,
      script `scripts/spinor_twistor_place_2026-10-08T2100.py` (PASS): a qubit's
      reduced 4-vector is null when unrelated and timelike with mass = C when
      entangled; the twistor is the counterfactual stage (a spinor with its
      possible relations), the entangled pair the actual place (a rest frame).
      JS's "a place is created when a relation is formed" made literal at rung
      two; concurrence-as-mass is a RHYME with the octonionic associator debt.
      One sentence proposed for sec:gr-nonlocality (note section 11).

- [ ] **Correction (2026-10-08T2200)**: "no masses and no proper time above
      the electroweak crossover" (records note 2026-09-20, reused since) is too
      strong. Vacuum masses vanish with the condensate (standard, smooth
      crossover at 159.5 GeV); thermal masses ~ gT remain (0.2 to 0.9 T); a
      quasiparticle has a proper time; scale-free only up to mu_H and the
      running. Correct sentence: no particle has a clock of its own above the
      crossover. Note `knowledge/sessions/thermal_masses_crossover_correction_2026-10-08T2200.md`,
      script `scripts/thermal_masses_above_crossover_2026-10-08T2200.py`;
      dated correction pointers appended to the records, gravity, inflation
      and twistor notes; v2-plan line reworded. Replacement CANDIDATE ledger
      entry in note section 4 (Yukawa mass = the particle's phase clock,
      thermal mass = the bath's record clock). Import
      `bib/finite_temperature_refs_2026-10-08T2300.bib` (seven keys).

- [ ] **Amplituhedron and supersymmetry (2026-10-09)**, note
      `knowledge/sessions/amplituhedron_susy_unsplit_2026-10-09T1000.md`,
      script `scripts/n4_sym_unsplit_octonionic_spacetime_2026-10-09T1000.py`
      (PASS). Verified: Herm_2(O) has signature (1,9); the preferred C cuts it
      into (1,3) + the six-dimensional colour C^3; colour derivations fix the
      four and rotate the six; g2 ∩ u(3) = su(3), the U(1) outside G2. Reading
      (CANDIDATE): N=4 SYM is the unsplit octonionic spacetime reduced on the
      colour directions, its SU(4)_R the rotation group of colour space, the
      N=4 -> N=1 reduction = G2 -> SU(3); supersymmetry is what the octonionic
      rung has as geometry and loses as algebra; the amplituhedron is the
      positive geometry of the unsplit theory. Tree amplituhedron gluons =
      pure YM; positive geometry has gone non-SUSY (scaffolded gluons 2024).
      Precision owed on the 2026-10-07 opening sentence (split vs Euclidean
      real forms). For JS: ledger entries in note section 9; import
      `bib/amplituhedron_susy_division_refs_2026-10-09T1100.bib` (18 keys
      after section 10's four on experimental contact; four fields VERIFY-CITE,
      all VERIFY-SUPPORT). No patch.

- [ ] **Follow-on paper: the supersymmetry bridge (2026-10-09)**. JS: the
      "associator cancels / mass is where it does not" rhyme is not for Paper 1
      but a dedicated follow-on paper should expand it, connect to the decades
      of supersymmetry work, and explain the absence of experimental evidence.
      Scope written: `knowledge/project-docs/paper_susy_bridge_scope_2026-10-09T1300.md`
      (thesis, chain of argument with labels, central computation, inherited
      literature, predictions, fences, prerequisites). Next steps in its
      section 8: read Baez--Huerta 2010 in full and script the 3-psi's identity
      for O and the sedenions; read Haag--Lopuszanski--Sohnius for its
      hypotheses; attempt the split supersymmetry variation and record
      PASS/FAIL; only then outline. Import
      `bib/supersymmetry_bridge_refs_2026-10-09T1300.bib` (eleven keys,
      verified, all VERIFY-SUPPORT). "Paper 3" is already the measurement-scale
      companion paper (Jaynes appendix comments); JS to number this one.

- [ ] **Continuity section: conservation of probability (2026-10-10)**. JS:
      measured probability must sum to 1, therefore probability is conserved.
      Review: the section's "continuity is what entitles the theory to make
      [the cut from GL to U]" is wrong, GL(n,C) being connected; conservation
      makes the cut, and the paper nowhere derives conservation from records
      (every route reads normalisation off the L^2 sphere continuity delivered;
      sec:born-cost-ledger borrows it explicitly). Conservation route proposed:
      exactly one outcome per FANOUT at any operation count + closed-loop
      squares (not ratios: analyticity) + linearity => sphere preserved =>
      unitary; or "undone by the anti-event" = U^dagger U = 1. Continuity then
      does connectedness and the p=2 selection only. Note
      `knowledge/sessions/continuity_probability_conservation_2026-10-10T1000.md`,
      script `scripts/probability_conservation_vs_renormalisation_2026-10-10T1000.py`
      (PASS). DRAFTED UNRUN, --check passes, JS to rule:
      `scripts/patch_continuity_cut_conservation_2026-10-10T1100.py` (one
      paragraph). Two further wording items (L^2 section premise; Postulate 5
      origin clause) and one in sec:born-cost-ledger, in note section 5. Ledger
      entry proposed in section 6. Section 8 (T1300): op:limit-realisability is
      NOT cleared (the stabiliser fragment satisfies every premise of the
      conservation route); "reversible" in the problem can read "unitary";
      restatement possible as "one transformation of infinite projective
      order", with the Koide phase 2/9 rad an empirical witness (RHYME).
      Script `scripts/value_continuum_infinite_order_2026-10-10T1300.py`.

- [ ] **The chain to reversible continuity; fixed-point route to the value
      continuum (2026-10-10T1500)**. JS: why can't we show self-reference ->
      negative probability -> complex measure -> (with conservation) reversible
      continuity; what remains? Answer: the gap is the value continuum, a
      declared premise at the Shannon step (continuation unique only on a
      connected domain), consumed again at the continuity step; conservation
      does not supply it. Candidate route: premise (F) "every admissible
      transformation fixes an admissible pure state" (Lawvere's conclusion)
      + transitivity + closedness => connected positive-dimensional state
      space (Jordan + components; elementary theorem) => Hardy's fifth. (F)
      passes the FAIL test: 14 of 24 Clifford elements and 14 of 24 toy-bit
      permutations are derangements; the Clifford derangements' fixed points
      are the magic states. Remaining: exhibit the regime as an instance of
      Lawvere's hypothesis (objects, point-surjectivity, fixed point admitted
      as the lamp principle). Note
      `knowledge/sessions/value_continuum_fixed_point_route_2026-10-10T1500.md`,
      script `scripts/fixed_point_route_value_continuum_2026-10-10T1500.py`
      (PASS). For JS: restate op:limit-realisability (wording in note section
      6); ledger entries there; import `bib/jordan_theorem_ref_2026-10-10T1500.bib`.

## Bibliography hygiene

- [ ] Dedupe three pairs the ChatGPT review's .bib import created:
      biss2008annihilators / BissDuggerIsaksen2008Annihilators,
      moreno1998zerodivisors / Moreno1998ZeroDivisors,
      gillardgresnigt2019three / GillardGresnigt2019Generations; keep the keys
      the paper cites. Tang: the library has Tang2025AssociatorMass; the Fable
      batch tang2025associator is superseded by it (v2 plan item 7 to use the
      library key). Morita 2014 Sec. 5 is VERIFY-SUPPORT (paywalled). Unrun
      patch adding the antecedent citations to prop:zd-defect:
      `scripts/patch_zd_defect_antecedents_2026-09-27T0900.py`; JS to rule.
      Reading note: `knowledge/sessions/chatgpt_sedenion_prior_work_review_2026-09-27T0900.md`.

- [ ] Import `bib/pais_physics_in_denmark_ref_2026-09-26T0900.bib` (key
      `pais2002physicsdenmark`, Pais's Nobel-site essay, for the Carlsberg
      Foundation's support of Bohr; verified against the page, support quoted
      in the batch header) and re-export. The sentence that cites it is not yet
      in the repository: JS to say which file.

- [ ] **Second-order citation pass** (JS, 2026-09-25: "second order hallucinated
      references, where a reference exists, but doesn't support the statements
      in the paper. Something we have to guard against"). For every citation
      added since 2026-09-18, read the cited passage and record in the batch's
      note whether it supports the sentence that cites it, quoting the text;
      entries checked against abstracts only are now marked VERIFY-SUPPORT
      (`bib/multicopy_slocc_refs_2026-09-20T2300.bib`). Then the same pass over
      the whole of paper1/references.bib, oldest first, as time allows.
      Convention recorded in bib/README.md ("Second-order checks"). The
      standing example is the 't Hooft two-generation discrepancy, still
      awaiting JS's ruling on the proposed sentence.

- [ ] Re-export `self-ref-2026-cited` again: `Laraudogoitia_1997` was fixed in
      Zotero on 2026-09-12 (the Mendeley fossil `ISBN: 00070882` removed from
      Extra, the ISSN corrected to the hyphenated `0007-0882`). With the 1998
      entry already fixed, both biber ISBN warnings should then be gone.
- [ ] `Brukner2009` is a book chapter filed as a journalArticle. Its
      `publicationTitle` is "Deep Beauty: Understanding the Quantum World
      Through Mathematical Innovation", a Cambridge volume, its DOI is
      `10.1017/CBO9780511976971.011` and its ISBN is that book's. So the ISBN
      is right and the item type is wrong; it should be a bookSection with
      `bookTitle` set, which exports as `@incollection` and carries the ISBN
      legitimately. Changes how the entry renders, so it is a decision, not a
      sweep. It is the only `@article` in `references.bib` that will still
      carry an `isbn` after the next re-export.
- [ ] `Tobergte2013` and `Wood2014a` share the ISBN `9788578110796`, which is
      valid but is a known Mendeley default rather than either paper's book.
      Neither is cited. Worth deleting both when convenient.

## The sedenion section, and what it still needs

- [ ] Import three batches into Zotero and re-export. They carry exactly the
      seven keys `sedenions_generations_section_2026-08-27.tex` cites and the
      library lacks: `bib/szangolies_sedenion_refs_2026-08-25T0633.bib`
      (pinillaluthra2009hopf, gresnigtgourlayvarma2023three,
      gourlaygresnigt2024algebraic, tangtang2023unified),
      `bib/gresnigt_cl10_ref_2026-08-25T0700.bib` (gresnigt2026three) and
      `bib/cp_context_core_refs_2026-09-12.bib` (kobayashimaskawa1973,
      jarlskog1985). Until then a build reports seven undefined citations.
- [ ] `sec:flavour-conservation` is referenced by the sedenion section and
      defined nowhere. The flavour-conservation splice is recorded in the
      project memory as done, so the label was probably never set; find the
      subsection and label it.
- [ ] Reduce `sec:sedenion-announcement` in the zoo to a forward pointer. The
      sedenion section's preamble says it absorbs that subsection's content and
      that a draft replacement was supplied separately;
      `scripts/patch_zoo_sedenion_pointer_2026-08-25T0700.py` looks like it.
      The same preamble warns explicitly NOT to run the 2026-08-25T0633
      positioning patch, which is not among the files.

## The Wigner's-friend splices, now that their sources have arrived

The two files the orphan references pointed at were downloaded on 2026-09-12
and are filed. Three patch scripts are ready to run, none of them applied.

- [ ] Import `bib/extended_wigners_friend_refs_2026-08-30.bib` (13 keys) and
      `bib/ewf_splice_supplementary_refs_2026-08-30.bib`
      (nurgalievarenner2020testing) into Zotero and re-export. They are no
      longer orphans: `paper1/wigner_ewf_positioning_splice_2026-08-30.tex`
      cites 14 keys of which 13 are missing, and these two batches supply
      exactly those. Only `yingetal2024relating` would arrive uncited.
- [ ] Run `scripts/patch_zoo_sedenion_pointer_2026-08-25T0700.py`, which
      reduces the zoo subsection to the forward pointer in
      `paper1/zoo_sedenion_pointer_replacement_2026-08-25T0700.tex`. That
      replacement keeps `\label{sec:sedenion-announcement}`, so existing
      references to it stay valid.

## The build, and what is blocking it

- [ ] **Re-export `self-ref-2026-cited` once more**, for `szangolies_2020`
      again. The raw passthrough worked, but biber rewrote the `\rangle` in it
      into the Unicode character, which inputenc maps to the text-mode
      `\textrangle` --- invalid inside the `$...$` it sits in. Four LaTeX
      warnings, and the bracket printed as `>`. The Zotero item now uses
      `\ket{}` from `braket`, which the paper already loads and biber does not
      rewrite; verified through BBT's export endpoint. This is the only defect
      in an otherwise clean 189-page build.
- [ ] *(superseded, kept for the record)* The earlier note on this entry:
      Its title is genuinely mathematical --- "This Sentence Is
      $\frac{1}{\sqrt{2}}(|True\rangle + |False\rangle)$" --- and Zotero
      held it as literal text, so the export escaped every backslash and it
      would have printed as `\textbackslash frac\{1\}...`. It is cited three
      times, including from `main.tex`, so it would have been visible. Fixed in
      the library with BBT's raw passthrough, `tex.title = ...` in Extra; see
      `bib/README.md`. A scan of all 252 entries for escaped maths, stray
      backslashes, escaped braces and ligature codepoints found nothing else.
- [ ] Four newly imported entries carry no DOI, eprint, URL or ISBN:
      `hickeygour2018imaginarity`, `klyachko2006marginal`,
      `thooft1980naturalness`, `vidal2000monotones`. Not errors --- the batches
      supplied no identifier --- but each is worth one lookup before
      submission.
- [ ] `verstraete2002four` carries `pages = {521121--521125}`, a Mendeley
      mangling of the article number 052112. It was already in the library and
      is now cited by the reverse-flow appendix, so the wrong range would
      print. One field to correct in Zotero.
- [ ] Confirm the substitution made for `sec:flavour-conservation` on
      2026-09-12. The label was defined nowhere -- the 2026-08-12 flavour
      splice went in without a section label -- and the sedenion section's own
      preamble said to "use prop:fcnc / prop:neutral-blind if the splice has no
      section label of its own". The clause now reads "the no-force
      propositions of \S\ref{sec:interactions}, Propositions~\ref{prop:fcnc}
      and~\ref{prop:neutral-blind}". Editorial, so worth a glance.
- [ ] One `.tex` in `paper1/` is still unreached from `main.tex`:
      `zoo_sedenion_pointer_replacement_2026-08-25T0700.tex`, the source its
      patch will paste in. The other consumed sources were atticked on
      2026-09-12 once their patches had run.
- [ ] `scripts/patch_wigner_hopf_ladder_fig_2026-08-30.py` is obsolete and
      refuses to run. The 2026-08-30 revision of the EWF splice embeds the
      figure inline --- the tikzpicture in the target is byte-identical to the
      standalone `fig_wigner_hopf_ladder_2026-08-30.tex`, now atticked --- so
      there is nothing left for it to insert. Keep it for provenance.

## Batches still unimported, and what they imply

- [ ] Import `bib/reverse_flow_refs_2026-07-23.bib` (22 keys) and re-export.
      No longer an orphan: `appendix_reverse_flow_2026-07-23.tex` arrived on
      2026-09-12, is filed in `paper1/appendices/` and is now input last in the
      appendix block. It cites 24 keys, 22 of them from this batch, and all 22
      are still absent from `references.bib`. The `.ris` beside it converts to
      the same key set exactly.
- [ ] `bib/tower_extension_refs_2026-07-25.ris` is superseded: its single key
      `eakinsathaye1990` is the same work as `eakinsathaye1990automorphisms`,
      already in Zotero and cited. Do not import it.
- [ ] Review the 2026-09-12 entry drafted in `knowledge/invalid_routes.md`
      (the sedenion core triple as the generations). It also supersedes part of
      the 2026-09-11 frame-orientation entry: notebook M's angle inventory ran
      on the core triple, which the correction makes the colour triple, so it
      does not close the generation-side frame. Re-running the eighteen-angle
      inventory on the psi-orbit of halvings is the cheap way to settle it.
- [ ] Work through the nine corpus locations the corrections ledger lists as
      still carrying the old attribution --- the zoo's triality paragraph, the
      hardware appendix's app:hw-ckm, op:up-quark's route-closure clause,
      notebook M's appendix entry, and four project documents. Item 2 on that
      list is discharged by running the zoo pointer patch; the rest are JS's
      adjudication, as the ledger says.

## Unreferenced labels

- [ ] Work through `notes/unreferenced_labels_2026-09-13.md`: 63 `\label{}`s in
      the live tree that no `\ref` points at, 56 in paper 1 and 7 in paper 2.
      None breaks the build. Each is either a fossil whose referring text was
      rewritten or atticked, or a sign that the referring splice was never
      brought over from Claude web --- the signature that found the Wigner
      splices on 2026-09-12. All 63 were searched for across project-docs,
      sessions, attic, notes and `~/Downloads` (2,235 files); four turned up and
      all four are fossils, so the other 59 have no referring text anywhere on
      this machine.
- [ ] Restore the paragraph that introduces Figure `fig:wf-hopf-ladder`. The
      2026-08-30 EWF splice brought the figure but not its introduction; the
      prose survives in `scripts/patch_wigner_hopf_ladder_fig_2026-08-30.py`,
      whose anchor phrase still occurs exactly once in the target. As it stands
      the figure floats with nothing in the body pointing at it.
- [ ] Within that list, three more are editorial decisions rather than tidying:
      `fig:myimage` is unreferenced and looks like a placeholder name; every
      proposition in the zero-divisor appendix (`prop:zd-*`) is unreferenced
      although its central equation is cross-referenced; and
      `op:generation-mechanism` was minted against an instruction that left the
      choice open, so that decision is half-made.
- [ ] `~/Downloads/latex_stuff/` holds 143 unreviewed files -- publisher
      citation downloads named by DOI, and July copies of section files that are
      older and smaller than the live ones. History rather than missing work,
      but never looked at.

## Ledgers

- [ ] Confirm the four status labels marked `[JUDGED]` in
      `knowledge/results_ledger.md` and `knowledge/principles.md`: the Born
      rule derivation (ESTABLISHED vs CANDIDATE), the Coecke-Kissinger
      classification (STRUCTURAL), the no-leptoquark theorem (ESTABLISHED
      though conditional), and "interpretations are coordinate systems"
      (RHYME vs CANDIDATE).
- [ ] Confirm the readings given for **ESTABLISHED**, **CONJECTURE** and
      **OPEN**. Only STRUCTURAL, CANDIDATE and RHYME are defined in the
      corpus, in `paper1/appendices/appendix_jaynes_fibration_2026-07-19.tex`
      section `app:jaynes:status`. The other three were inferred.

## Versioning and release

The release needs **two Zenodo deposits**, and that is not a mistake to be
avoided. Zenodo issues the concept DOI --- the one that always resolves to the
latest version --- only on first publication, so the paper cannot cite it until
a deposit exists. The first deposit therefore cites its own version DOI, which
is self-consistent but not future-proof, and the second cites the concept DOI.
The arXiv submission is the second one, so arXiv v1 corresponds to Zenodo
deposit 2. The README says to expect exactly this.

- [ ] **1. Deposit.** Publish the current state to Zenodo against the reserved
      DOI `10.5281/zenodo.22755871`. The paper's colophon and the
      `small2026itfrombit` entry both name that DOI, and it is the DOI of the
      deposit that contains them, so the record is internally correct. Tag the
      repository first so the deposit has a name.
- [ ] **2. Read the concept DOI.** It exists from the moment of publication. If
      the web form does not show it, the REST API does:
      `curl -s https://zenodo.org/api/records/<recid> | python3 -c "import json,sys; print(json.load(sys.stdin).get('conceptdoi'))"`
- [ ] **3. Swap it in, in two places.** The colophon in `paper1/main.tex` (patch
      script; `scripts/patch_colophon_2026-09-16T1700.py` is the one that put
      the DOI there) and the `small2026itfrombit` item in Zotero, then
      re-export `references.bib`. Both cite a living record, so a version DOI
      would freeze them to deposit 1.
- [ ] **4. Finish the release edit while you are in there.** The title's
      `Version 0.5`, the colophon, the DRAFT watermark and the
      work-in-progress note under `\maketitle` all want settling together, and
      the colophon should then name the tag it was built from. Build clean.
- [ ] **5. Deposit again, then submit that one to arXiv.** Deposit 2 is the
      artefact the paper describes and the one the arXiv record should point
      at.

Deposit 1 is not wasted: it is the honest record of the paper at the moment it
could only name itself. The colophon also carries the repository URL beside the
DOI, and that pointer never goes stale, so even deposit 1 leads a reader to the
current state.

## Before the repository goes public

- [ ] Read through `knowledge/` -- 26 MB, published permanently by a Zenodo
      release. `memory/profile.md` gives a home town; seven conversations in
      the archive are tagged `[tooling]` and wander off-topic.
- [ ] Enable the repository in Zenodo, then tag `paper1-v1` and publish a
      release to mint the DOI.
- [ ] `noether1918invariante` remains VERIFY-CITE: no DOI exists for the 1918
      original and the page range 235-257 could not be confirmed against any
      machine-readable source.

## Carried over from the project memory

These were listed as outstanding when the Claude web project was exported and
have not been checked since.

- [ ] Bridge test resolving the K3 Class-4 / psi-fixed line housing seam.
- [ ] Patch the remaining fossils in `fermion_topology_table.py` and
      `fermion_topology_open_problems.md` section 5.2.
- [ ] Newtonian limit computation for Paper 2 (`op:p2-newton`).
- [ ] Email Andrei Khrennikov, leading with the complementarity reframe and
      the Tsirelson-as-ramification correspondence.
- [ ] Label mapping for the four master-file section labels (`sec:hopf`,
      `sec:born`, `sec:fanout`, `sec:contextuality`) in the Jaynes appendix.

- [ ] Nine of the ten undefined section references are resolved (patch
      2026-09-11T2030; see sessions/tidy_after_koide_handover_2026-09-11T2011.md
      for the mapping). Needs a build to confirm the warning count falls from
      thirteen to one. The one left is `sec:sedenions-mixing` in
      `wigners_friend_in_the_hopf_picture`: the sentence says that section
      "reads that phase ... as this wire's contextual cargo", which could be
      the masses section's `\subsection{Mass eigenstates versus weak
      eigenstates}` or the interactions section's provenance paragraph on the
      sedenion route to the full CKM. JS to choose.
- [ ] The eighteen references in main.tex's "Paper structure" paragraph are
      bare `\ref{}`, so they render as "1.2" rather than "\S1.2" as the rest
      of the paper does. A one-paragraph style pass, unrelated to the warnings
      above.

## 2026-10-16: paradox, hypodox and FANOUT (Fable session)

- [ ] Read `knowledge/sessions/liar_hypodox_fanout_2026-10-16T1100.md`.
      Two second-order findings for JS: prop:fanout-correspondence (b) in
      the FANOUT appendix overclaims per state (|-> has off-diagonals in Z
      and a non-negative Wigner function in every convention), and the two
      "<=> negative probability" sentences in `what_is_a_quantum_state.tex`
      conflate a sign on an amplitude with a signed quasi-probability. The
      Liar's consistent states are stabiliser states; negativity first
      appears at Fix(H). Proposed wording in the note's section 10.
- [ ] Import `bib/liar_hypodox_refs_2026-10-16T1200.bib` (16 keys; three
      VERIFY-CITE in the header). Dourdent2020Godelian is in the library and
      uncited; the note suggests the lineage paragraph.
- [ ] Read Roberts 2023 (`roberts2023substructural`) for whether contraction
      survives; "no diagonal, no paradox" depends on it.

## 2026-10-16: the hypodox as an open loop; closed timelike curves (Fable session, later the same morning)

- [ ] JS: read `knowledge/sessions/hypodox_ctc_fanout_2026-10-16T0900.md`
      (script `scripts/hypodox_ctc_fanout_2026-10-16T0900.py`, PASS). Two
      second-order findings for ruling (section 8): the `sec:comp-distance`
      sentence "a unique consistent solution or none" misses the
      underdetermined case that carries the bit; `prop:self-creation` is
      single-shot and fails in the ensemble against a maximum-entropy loop.
      Proposed wording is in the note; nothing patched.
- [ ] Zotero: import `bib/ctc_darwinism_refs_2026-10-16T1000.bib` (18 keys;
      VERIFY-CITE on the Dunlap journal form and the Pinzani proceedings
      form only; the rest are Crossref or arXiv verified).
- [ ] Read Hasegawa 1997 for the exact statement "trace in a cartesian
      category = Conway fixed-point operator" before the trace-to-fixed-point
      sentence (note section 3) goes anywhere near the paper.
- [ ] Read Deutsch_91 for the "from nowhere ... from and into other universes"
      passage and the entropy rule (quoted second-hand from Dunlap today).

## 2026-10-16: complex temperature and the coherence budget (Fable session, late morning)

- [ ] JS: read `knowledge/sessions/coherence_budget_complex_count_2026-10-16T1030.md`
      (script `scripts/coherence_budget_complex_count_2026-10-16T1030.py`,
      PASS). The claim "information added at the observation = the imaginary
      component of the pre-FANOUT knowledge, leaving a real value" is an exact
      identity if "imaginary component" means the coherence in the record
      basis (S(rho) + C_Z(rho) = H(p) at every stage of the graded FANOUT),
      and false if it means the phase (phase-blind; the phase is promoted).
      Three second-order findings for ruling (section 8): the 09-16 note's
      "decoherence is the phase becoming entropy", the paper's "counted in
      imaginary numbers", and the 07-26 note's "generically complex S" (true
      for three or more levels, not for the bit). Nothing patched.
- [ ] Zotero: import `bib/complex_temperature_coherence_refs_2026-10-16T1040.bib`
      (7 keys, all Crossref-verified; VERIFY-SUPPORT on the bodies).
- [ ] Read Wei and Liu 2012 (body) for the exact mapping between probe-spin
      coherence and the partition function at complex temperature; it is the
      citable bridge from Hawking's imaginary temperature to the FANOUT's
      decoherence factor, and the September complex cost is then a complex
      free energy.

## 2026-10-16: a probability greater than one for a hypodox (Fable session, evening)

- [ ] JS: read `knowledge/sessions/hypodox_probability_above_one_2026-10-16T2200.md`
      (script `scripts/hypodox_probability_above_one_2026-10-16T2200.py`,
      PASS). The "probability greater than one of a hypodox" is the
      Kirkwood--Dirac conditional of its value between the pre-FANOUT state
      and a complementary record, q(a) = psi_a/(psi_0+psi_1): complex in
      general, above one with a negative complement at phase pi, divergent
      at the Liar's boundary pair, and by Pusey's theorem contextual, so the
      same resource as negative probability. A hypodox read in its own basis
      is 0 or 1; a loop closed on itself has real part exactly 1/2; the count
      2 is a count. Four findings for ruling (section 9): the two
      "paradox <=> negative probability" sentences (replacement wording with
      Pusey), "the phase as the continued information", "never in a final
      record" (confirmed), and a p-adic sentence for the Khrennikov email.
      Nothing patched.
- [ ] Zotero: import `bib/kirkwood_dirac_weak_value_refs_2026-10-16T2210.bib`
      (20 keys; 18 Crossref-verified; VERIFY-CITE on the Kauffman--Varela
      author list and the Hellerstein edition; VERIFY-SUPPORT on all bodies).
- [ ] Read Pusey 2014 and Kunjwal--Lostaglio--Pusey 2019 for the exact
      conditions under which a projector's weak value outside [0,1] proves
      contextuality, before the replacement sentence of finding (a) goes
      near the paper.
- [ ] Read Kauffman 1987 to confirm the J = -1/J arithmetic for the Liar is
      there and not only in the later Laws of Form essays.

## 2026-11-07: would a relational space still need lattice QCD? (Fable session, morning)

- [ ] JS: read `knowledge/sessions/relational_distance_lattice_2026-11-07T0700.md`
      (script `scripts/relational_distance_lattice_2026-11-07T0700.py`,
      PASS). The lattice is already a relational object: a graph of link
      variables with a face action and no coordinates, whose spacing is
      inferred afterwards from a correlation (script A: a Wilson loop sees
      only the count of enclosed faces). A relational ontology removes the
      regular graph (it has a frame; a Poisson sprinkling does not, script
      B) and the continuum limit as ontology, not the lattice. The
      infinities are regulated by any bound on degrees of freedom and the
      renormalisation group makes the hadron scale indifferent to a Planck
      cutoff. Two constraints bite: Nielsen--Ninomiya doubling (script C)
      against any regular exchange graph carrying the framework's chiral
      leptons, and the sign problem as the pre-record regime. Four
      findings for ruling (section 9): `op:confinement-potential` as the
      lattice inference reversed; causal-set kinematics for Paper 2's
      chart re-emergence scale; the 09-20 crossover temperature is a
      lattice number; the chirality constraint for the twistor thread.
      Nothing patched.
- [x] Zotero: import `bib/lattice_causal_set_refs_2026-11-07T0710.bib`
      (29 keys; 25 Crossref-verified; VERIFY-CITE on Migdal 1975, Myrheim
      1978, Meyer 1988, Vershik--Kerov 1977 and the Wilson--Kogut author
      list; VERIFY-SUPPORT on all bodies).
      2026-11-08T0634: imported via the connector, keys pinned, in self-ref-2026-cited; 28 created; bombellileemeyersorkin1987causalset skipped as duplicate of rd_sorkin_87, re-pin owed; see `knowledge/sessions/zotero_batch_import_2026-11-08T0634.md`.
      2026-11-08T0913: moved to its own collection `lattice_causal_set_refs_2026-11-07T0710`, not exported.
- [ ] Read Christ, Friedberg and Lee 1982 (and the random-lattice fermion
      papers that follow it) for the status of fermion doubling on an
      irregular graph, before the chirality constraint of section 6 goes
      near the twistor thread.
- [ ] Read Bombelli, Henson and Sorkin 2009 for the exact statement of the
      no-preferred-frame theorem, before Paper 2 cites it for the chart
      re-emergence scale.

## 2026-11-07: aligning the budget and the flux tube (Fable session, late morning)

- [ ] JS: read `knowledge/sessions/confinement_budget_flux_tube_2026-11-07T1130.md`
      (script `scripts/confinement_budget_flux_tube_2026-11-07T1130.py`,
      PASS). The two pictures share one tensor: the GHZ copy structure the
      paper's glueball subsection names is Gauss's law in the electric
      basis (script B: the Z_N neutral subspace is the Fourier transform of
      the N-level GHZ state, the two-valent vertex is the copy map, a chain
      copies the source charge, the Z_3 trivalent vertex is neutral at
      (1,1,1)). The flux tube is the colour-basis FANOUT of
      `sec:bell-not-counterexample`. Copy versus share is the tube versus
      the Coulomb field (script C: a centre charge costs the same over any
      number of routes, real flux costs R/m; shared flux is linear, log,
      Coulomb in d = 1, 2, 3, copied flux is c(1) times the graph distance
      in every d). The centre Z_3 of SU(3) grades the computability split
      (script D: phase rotations of the colour C^3 are automorphisms of O
      exactly at the cube roots; record 0, colour 1, anticolour 2), so
      "no record carries bare colour" is 't Hooft's N-ality criterion. One
      fence (script E): the SU(3) singlet's two-quark marginal is the
      antisymmetric Werner state, negativity 1/3; the "every bipartite
      tangle zero" clause is the register model's. Six findings for
      ruling (section 9). Nothing patched.
- [x] Zotero: import `bib/confinement_flux_tube_refs_2026-11-07T1140.bib`
      (25 keys; all Crossref-verified; no VERIFY-CITE; VERIFY-SUPPORT on
      all bodies).
      2026-11-08T0634: imported via the connector, keys pinned, in self-ref-2026-cited; 25 created; see `knowledge/sessions/zotero_batch_import_2026-11-08T0634.md`.
      2026-11-08T0913: moved to its own collection `confinement_flux_tube_refs_2026-11-07T1140`, not exported.
- [ ] Rule on the pairwise-zero clause (confinement section line 138) and
      on the asymptotic-freedom document's "GHZ state across three
      qutrits": the SU(3) singlet has pairwise negativity 1/3; the access
      argument uses only r^2 = 0, which survives.
- [ ] Rule on "colour triality" in `sec:quantum-numbers`: it is N-ality,
      a different Z_3 from the Koide triality of `sec:masses`.
- [ ] Read Haegeman, Van Acoleyen, Schuch, Cirac and Verstraete 2015 for
      the exact form of the gauging map's vertex tensor before the
      mass-gap subsection's "tensor-network interface" sentence cites it.
- [ ] Read 't Hooft 1978 for the exact statement of the N-ality criterion
      before `sec:bell-not-counterexample` is aligned with it.

## 2026-11-07: qutrits in the Hopf picture (Fable session, afternoon)

- [ ] JS: read `knowledge/sessions/qutrit_hopf_picture_2026-11-07T1600.md`
      (script `scripts/qutrit_hopf_picture_2026-11-07T1600.py`, PASS). A
      qutrit has no Hopf fibration and no Bloch ball (script F), so it is
      not a register; it lives on the three-qubit base as the colour
      equator, whose radius squared is the one-tangle (script A: S^8 is
      the join S^2 * S^5), fibred over CP^2 by the record circle
      exp(theta e_1), whose automorphism subgroup is the centre Z_3
      (script B). Colour SU(3) acts on the register as diag(1, SU(3)) on
      the two internal qubits, an entangling gate fixing the record
      amplitude (script C). The SU(3) singlet is det = phi + i *phi(e_1,
      ...): an SU(3) colour frame spans a quaternion subalgebra of O
      (script D), the same condition `sec:three-dimensions` uses for three
      composing links. Two fences: the colour direction on the base is
      vector data, not ray data; and the CGLMP maximum for two qutrits is
      not at the maximally entangled state (script E), so the ball
      argument for Tsirelson is qubit-only. Seven findings for ruling
      (section 9). Nothing patched.
- [x] Zotero: import `bib/qutrit_hopf_refs_2026-11-07T1610.bib` (9 keys; all
      Crossref-verified; no VERIFY-CITE; VERIFY-SUPPORT on all bodies).
      2026-11-08T0634: imported via the connector, keys pinned, in self-ref-2026-cited; 9 created (pilot); see `knowledge/sessions/zotero_batch_import_2026-11-08T0634.md`.
      2026-11-08T0913: moved to its own collection `qutrit_hopf_refs_2026-11-07T1610`, not exported; kimura2003bloch alone remains in self-ref-2026-cited (cited in Paper 1).
- [ ] Rule on adding the CGLMP degeneracy to
      `knowledge/project-docs/open_problem_qudit_degeneration.md` (9(a)).
- [ ] Rule on the proposition "an SU(3) colour frame is a quaternion
      subalgebra; Im epsilon = *phi(e_1, ...)" for the confinement section
      (9(d)), and on its CONJECTURE reading against the masses section's
      coassociative calibration.
- [ ] Read Harvey and Lawson 1982, the theorem on associative 3-planes
      (imaginary parts of quaternion subalgebras) and the special
      Lagrangian case inside C^3, before 9(d) is applied.
- [ ] Read Acín, Durt, Gisin and Latorre 2002 for the exact statement of
      the optimal CGLMP state before 9(a) is applied.
- [x] 2026-11-07T1700: JS accepted all seven findings of section 9. Applied
      by `scripts/patch_qutrit_hopf_rulings_2026-11-07T1700.py` to six
      paper files and the qudit-degeneration document (note section 15).
      Static checks pass; NOT BUILT; not committed.
- [ ] Build paper1 after the patch (JS co-ordinates builds). Expected: one
      undefined citation, `kimura2003bloch`, until the 2026-11-07T1610
      batch is imported; new labels `prop:singlet-quaternion`,
      `eq:singlet-calibration`.
- [ ] Write the note's section 12 ledger entries (four STRUCTURAL, one
      ESTABLISHED, two CANDIDATE, one RHYME, one CONJECTURE, one fence)
      now that section 9 is accepted; maintainer's call on wording.
- [x] Acín et al. 2002 read (arXiv v2): gamma = (sqrt11 - sqrt3)/2,
      maximum 1 + sqrt(11/3); VERIFY-SUPPORT discharged (note section 15).
- [ ] Harvey and Lawson 1982 still unread (Euclid bot wall); the citation
      in `prop:singlet-quaternion` and in `sec:three-dimensions` stays
      VERIFY-SUPPORT.

## 2026-11-07: the B-meson anomalies and lepton universality (Fable session, evening)

- [ ] JS: read `knowledge/sessions/b_anomaly_lepton_universality_2026-11-07T1900.md`
      (script `scripts/b_anomaly_lepton_universality_2026-11-07T1900.py`,
      PASS). Alda, Guasch and Peñaranda 2021 (arXiv:2105.05095) is a
      proceedings fit of the 2021 R_K, R_K*, R_D(*) anomalies needing LFU
      violation (their LFU scenario 0.55 sigma, e+mu 4.97 sigma). The
      framework forbids LFU violation at the gauge level (prop:fcnc,
      prop:neutral-blind, flavour-not-force) and excludes the mediators
      (absent gate, no fifth force, desert); it predicts R = 1. LHCb Dec
      2022: chi^2 1.76/4 against R = 1 (p = 0.78). Still open against it:
      HFLAV 2023 R(D(*)) at 3.1 sigma; the universal b -> s mu mu deficit,
      which the framework must call hadronic. Five findings for ruling
      (section 6), one of them OPEN: whether "the lepton tag may couple at
      the state level" (interactions, fourth-qubit paragraph) is unitary
      mixing (LFU kept) or a label-dependent amplitude (LFU broken).
- [x] Zotero: import `bib/b_anomaly_refs_2026-11-07T1910.bib` (11 keys; 8
      Crossref-verified by DOI; hflav2023averages and belleii2024rdstar
      carry VERIFY-CITE on their journal fields).
      2026-11-08T0634: imported via the connector, keys pinned, in self-ref-2026-cited; 10 created; aldaguaschpenaranda2021anomalies skipped as duplicate of aldaAnomaliesMesonsDecays2021, re-pin owed; see `knowledge/sessions/zotero_batch_import_2026-11-08T0634.md`.
      2026-11-08T0913: moved to its own collection `b_anomaly_refs_2026-11-07T1910`, not exported.
- [ ] Rule on 6(a) (LFU prediction paragraph for sec:predictions), 6(c)
      (TeV mediators inside the desert), 6(d) (universal C_9 deficit is
      hadronic within the framework), 6(e) (open-problem entry with
      PASS/FAIL on R(D(*))).
- [ ] Read Glashow, Guadagnoli and Lane 2015 (PRL 114, 091801) for the
      exact alignment statement, and Bordone, Isidori and Pattori 2016
      (EPJC 76, 440) for R_K = 1.00 +/- 0.01, before 6(a) is applied.
- [ ] Read Alda et al. sections 5 and 6 (not reached in the HTML) for
      their stated open questions.

## 2026-11-07: three papers on b -> s l l angular analyses and the R_D(*) fit (Fable session, late evening)

- [x] Session note `knowledge/sessions/three_papers_lfu_angular_2026-11-07T2000.md`
      (script `scripts/three_papers_lfu_angular_2026-11-07T2000.py`, PASS).
      JS sent arXiv:2502.10291 (LHCb, B0 -> K*0 e+e- angular analysis, JHEP
      06 (2025) 140), arXiv:2512.18053 (LHCb, full-dataset B0 -> K*0 mu+mu-,
      PRL 137 (2026) 021802) and arXiv:2510.17742 (Mir, Alda and Peñaranda,
      EFT fit with new physics on one generation in the interaction basis).
      The electron Q_i are consistent with universality (chi^2 6.6/8, p =
      0.58, correlations neglected) and Delta C_9 is within 1 sigma of zero,
      while the electron mode alone prefers the same C_9 shift of about -1
      as the muons at > 2 sigma: the deficit is lepton-universal, as the
      framework requires, and is now at 3.6-4.1 sigma in the muon letter;
      within the framework it can only be long-distance SM, and LHCb's own
      data-driven analyses say the nonlocal part does not absorb it. This is
      the framework's most exposed point in flavour physics. Mir et al.'s
      assumption (a rank-one projector on the generation label) is the exact
      negation of prop:fcnc's premise; their fit itself drives lepton mixing
      to zero. New structural point: the commutant of S_3 on the label space
      is span{1, J}; an S_3-equivariant but non-trivial coupling a 1 + b J is
      diagonal in the Koide mass basis and falls on the tau alone, which is
      the pattern the data select; the framework's prohibition is stronger
      (the identity component acts trivially on pi_0) and R_D(*) and
      B -> K nu nubar test exactly that stronger premise. Five findings for
      ruling (section 6).
- [x] Zotero: import `bib/three_papers_lfu_refs_2026-11-07T2010.bib` (13 keys;
      12 Crossref-verified by DOI; miraldapenaranda2025bmeson is arXiv-only
      proceedings; no VERIFY-CITE).
      2026-11-08T0634: imported via the connector, keys pinned, in self-ref-2026-cited; 13 created; see `knowledge/sessions/zotero_batch_import_2026-11-08T0634.md`.
      2026-11-08T0913: moved to its own collection `three_papers_lfu_refs_2026-11-07T2010`, not exported.
- [ ] Rule on 6(a) (angular LFU test added to yesterday's prediction
      paragraph), 6(b) (the universal C_9 deficit named in prop:fcnc's
      discussion as a long-distance-or-refuted statement, with the
      Isidori--Polonsky--Tinari versus Ciuchini et al. dispute cited), 6(c)
      (B -> K nu nubar added to yesterday's 6(e) PASS/FAIL entry), 6(d)
      (remark that S_3-equivariance alone would not forbid a tau-only
      coupling; the trivial action of the identity component on pi_0 is what
      prop:fcnc uses), 6(e) (one-clause cross-reference from
      prop:koide-jordan to prop:fcnc: the mass sector sees the label
      democratically, the gauge sector not at all).
- [ ] VERIFY-SUPPORT reads owed: Capdevila, Descotes-Genon, Matias and Virto
      2016 (the Q_i definition); Isidori, Polonsky and Tinari 2025 (the body's
      number for the charm-rescattering shift of C_9); Belle II 2024 (the SM
      value used for the 2.7 sigma).
- [ ] Reconcile Mir et al.'s R_J/psi = 0.52 +/- 0.20 (citing HFLAV) with
      LHCb 2018's 0.71 +/- 0.17 +/- 0.18 before either number is quoted in
      the paper.

## 2026-11-16: GIM and flavour-changing neutral currents (Fable session)

- [x] Session note `knowledge/sessions/gim_fcnc_label_blind_2026-11-16T0630.md`
      with `scripts/gim_fcnc_label_blind_2026-11-16T0630.py` (33/33 PASS).
- [ ] JS to rule on findings 6(a)--(f): loop lemma after prop:fcnc;
      completeness in place of "arranged ... forced"; the Higgs; V as a
      relative frame and the commutator criterion; op:cabibbo sharpened by
      the circulant no-go, with the sigma for 2/9; first-row unitarity and
      mu -> e gamma as falsifiers.
- [ ] Zotero: import `bib/gim_fcnc_refs_2026-11-16T0640.bib` (13 keys; 11
      Crossref-verified by DOI; VERIFY-CITE on three title wordings and the
      Acta Physica Polonica reference) into a collection of the same name,
      not into self-ref-2026-cited.
- [ ] VERIFY-SUPPORT reads: Glashow--Weinberg 1977 and Paschos 1977 (the
      natural-flavour-conservation theorem), Gaillard--Lee 1974 (charm mass),
      Inami--Lim 1981 (S0, Y0), D'Ambrosio et al. 2002, Aguilar-Saavedra 2004
      (the 1e-14 for t -> cZ).
- [ ] The masses section quotes |V_ud| = 0.97435 (PDG fit) beside
      |V_us| = 0.22430 (PDG direct); choose one source.

## 2026-11-16: Skolem's paradox and Chaitin, a rhyme (Fable session)

- [x] Paragraph added at the end of `sec:measuring-non-computability`
      (`paper1/what_is_a_quantum_state.tex`) by
      `scripts/patch_skolem_chaitin_rhyme_2026-11-16T1850.py`; note
      `knowledge/sessions/skolem_chaitin_rhyme_2026-11-16T1850.md`. Unbuilt.
- [x] (done 2026-11-21, 5/5 resolve, references.bib re-exported at 349 entries)
      Zotero: import `bib/skolem_rhyme_refs_2026-11-16T1850.bib` (5 keys, all
      cited in Paper 1) into self-ref-2026-cited and re-export; until then
      five undefined citations are expected.
- [ ] JS: RHYME ledger entry and the Paper 2 open-problem wording proposed in
      the note.
- [ ] Optional: cite skolem1922remarks at the unnamed use of the
      Loewenheim--Skolem theorem in `sec:continuity` (closedness paragraph).
- [ ] VERIFY-SUPPORT reads: Skolem 1922, Turing 1939, Feferman 1962,
      Raatikainen 1998.
- [x] 2026-11-21: antecedent sentence added to the same paragraph (Yanofsky,
      as quoted by Svozil, pp. 174--175) by
      `scripts/patch_skolem_yanofsky_antecedent_2026-11-21T0730.py`. Unbuilt.
- [x] 2026-11-21: that sentence reworded to tie the similarity to Rice's
      theorem, by `scripts/patch_skolem_rice_tie_2026-11-21T0732.py`. Unbuilt.

## 2026-11-21: the mass gap as the cost of a new relationship (Fable session)

- [x] Session note `knowledge/sessions/mass_gap_relationship_cost_2026-11-21T0800.md`
      with `scripts/mass_gap_relationship_cost_2026-11-21T0800.py` (27/27 PASS
      on the second run; the first failed one check through a search range of
      mine, recorded in the note).
- [ ] JS to rule on findings 9(a)--(g): the two-cost argument in place of
      "topologically discrete" in sec:mass-gap; the cost-of-a-link bridge
      between op:confinement-potential and op:glueball-spectrum; "no medium
      in the basis records read"; the trace anomaly beside "all mass is
      geodesic length"; the conjecture m_gap >= C sqrt(sigma) with
      Chatterjee's converse; op:qcd-scale as g_s at the matching scale; the
      bag constant as a cosmological term for Paper 2. A draft paragraph is
      in the note, not applied.
- [ ] Zotero: import `bib/mass_gap_relationship_cost_refs_2026-11-21T0830.bib`
      (14 keys; 13 Crossref-verified by DOI; VERIFY-CITE on the Lucini--
      Teper--Wenger title wording and the Chatterjee journal reference) into
      a collection of the same name, not into self-ref-2026-cited.
- [ ] VERIFY-SUPPORT reads: Osterwalder--Seiler 1978, Chodos et al. 1974,
      Jaffe--Johnson 1976 (x = 2.744), Johnson--Thorn 1976, Collins--Duncan--
      Joglekar 1977, Shifman--Vainshtein--Zakharov 1979 (0.012 GeV^4),
      Isgur--Paton 1985, Gaiotto et al. 2015, Levin--Wen 2005, Margolus--
      Levitin 1998, Chen et al. 2006; and the attribution of "mass equals the
      integrated trace anomaly".
- [ ] Four-loop check of alpha_s(3.6 TeV) before the PASS band proposed for
      op:qcd-scale is used.

- (2026-11-21, JS ruling) Mass-gap thread parked: too speculative for Paper 1 except to name problems with the framework's approach. Ledger, open-problem and invalid-route entries written 2026-11-21; revisit from `knowledge/sessions/mass_gap_relationship_cost_2026-11-21T0800.md`.
