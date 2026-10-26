# Paper 2: revisit the complex-cost thread of 2026-09-16 to 20 before drafting

Date: 2026-09-20T1900. Written by the Fable session at JS's instruction:
"Make sure this conversation is to be revisited when we work on paper 2."
This is the hub. It lists every note the thread produced that bears on Paper
2 ("Spacetime from the FANOUT boundary"), what each contributes to which
section or open problem, the drafts that are ready, the open problems
proposed, and the checks owed. The conversation itself is the Fable session
https://claude.ai/code/session_01GbVeonvSKSmXFrHyFY1mj3 (local transcript
under `~/.claude/projects/-home-john-Documents-tex-self-ref-2026/`); the notes
below are its durable form.

## The thread in one paragraph

Deletion before FANOUT has a complex thermodynamic cost, the imaginary part a
phase, the real part a record; the two are the two columns of one currency,
nats, exchanged at $\hbar$ per nat of phase and $k_{B}T$ per nat of record,
and FANOUT is the rotation between them. Mass is the imaginary cost rate (the
Compton clock), width the real cost rate, the Born rule the closed loop of a
history and its return leg. Order is a record and duration a phase, so the
quantum switch and its thermal death fall on the same ladder as the phase.
Temperature belongs to the payer; at a horizon it is fixed by Unruh and
cancels in Jacobson's derivation. At high temperature records form faster
and die faster, the thermal time is the causal structure's resolution, above
the electroweak crossover there are no clocks, and near the Planck
temperature no region can hold its own records. Jacobson's "non-equilibrium
spacetime" is the graded FANOUT of a horizon; gravity's equation of state
holds at every temperature the framework owns and fails only near the Planck
temperature; the Planck length is the record's grain and the Planck
temperature the boundary of the concept of temperature.

## The notes, and where each goes in Paper 2

| note (knowledge/project-docs unless stated) | contributes to |
|---|---|
| `complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md` (hub; sections 4a--4e) | the FANOUT-boundary junction: mass as imaginary cost rate, width as real rate, the graded rotation, decay channels as records |
| `two_columns_shannon_thermodynamics_action_2026-09-18T1200.md` | the four-constant junction ($\hbar$ and $k_{B}T$ as exchange rates); the closed loop as time-reversal invariance; the record as fidelity, not entropy; the Born rule (sec. 2a) |
| `indefinite_causal_order_fanout_2026-09-19T0900.md` | the causal-order section: "duration is a phase, order is a record"; the graded switch as the toy proof of the theorem target; the Oreshkov paragraph; the Rubino witness; op:ico-threshold |
| `landauer_temperature_fanout_energy_2026-09-20T1200.md` | the four-constant paragraph (sec. 4 there: Unruh fixes $T$, it cancels, $G$ enters through the area); the count-density dictionary is entropic; the Planck/Landauer/width/Matsubara table |
| `records_causal_structure_high_temperature_2026-09-20T1400.md` | the early universe: thermal time as causal resolution; hydrodynamic causal structure; no clocks above the electroweak crossover; area law as capacity; the singularity as the failure of records; op:sphaleron |
| `jacobson_non_equilibrium_spacetime_2026-09-20T1600.md` | the TODO paragraph at the end of the ontology section (draft in sec. 7 there); op:p2-nonequilibrium; the literature to inherit (Eling--Guedens--Jacobson, Chirco--Liberati, Jacobson 2016, Padmanabhan) |
| `gravity_planck_scale_high_temperature_2026-09-20T1800.md` | the domain of the equation of state; the Planck length as the record's grain, $G$ as equilibrium coefficient; conformal gravity above the crossover (op:p2-newton is a below-crossover statement); the hierarchy $M_{P}/v$ owed |
| `knowledge/sessions/graded_fanout_complex_cost_2026-09-18T0830.md`, `notebooks/notebook_S_graded_fanout_complex_cost_2026-09-18.ipynb` | the computation behind the rotation ($\mathrm{Re}\,C \propto R$, $\mathbb{E}|\mathrm{Im}\,C| \propto \sqrt{R}$) |
| `notes/paper1_v2_complex_cost_revision_plan_2026-09-18T1000.md` | what Paper 1 v2 will already say, so Paper 2 can cite rather than repeat (items 5, 6, 7, 11) |

Scripts, all seed-locked with stdout in the notes: `graded_fanout_complex_cost_2026-09-18T0830.py`,
`two_columns_renyi_check_2026-09-18T1200.py`, `quantum_switch_graded_fanout_2026-09-19T0900.py`,
`koide_renyi_profile_2026-09-19T1100.py`, `landauer_temperature_fanout_2026-09-20T1200.py`,
`records_high_temperature_2026-09-20T1400.py`, `hubble_records_high_temperature_2026-09-20T1800.py`.

- (added 2026-10-07) `inflation_horizon_infinitude_2026-10-07T1200.md`: the cosmology paragraph's three claims (infinite, flat, homogeneous) disentangled; the horizon dissolution placed at the first-record surface (needs the Planck-boundary result of the records note, section 4, not the electroweak one); flatness owed; the spectrum as a record of conformal structure as the direction for the hard debt; the no-inflationary-tensors prediction. Goes in Paper 2's cosmology section; the Paper 1 paragraph correction is drafted as `scripts/patch_inflation_paragraph_2026-10-07T1300.py`.

## Drafts that are ready

- The Jacobson paragraph for the ontology-section TODO (Jacobson note, sec. 7), in the paper's register, citation keys placeholders.
- The basis for the causal-order section and the Oreshkov paragraph (ICO note, secs. 3 and 5), with the Part B table as its figure.
- The four-constant paragraph (Landauer-temperature note, sec. 4).
- The early-universe material (high-temperature note, sec. 6; gravity note, secs. 1 and 4).

## Open problems proposed for Paper 2 (JS to mint)

- op:p2-nonequilibrium (Jacobson note, sec. 6): entropy production from the graded count; shear coefficient at $\eta/s = 1/4\pi$; relaxation time bounded by the chaos-bound time; no scale below Planck. Depends on op:p2-coefficient.
- op:ico-threshold (ICO note, sec. 6): finite or asymptotic definitisation of causal order; needs an SDP solver.
- op:sphaleron (high-temperature note, sec. 2; restated with PASS/FAIL in `sphaleron_slocc_collective_conversion_2026-09-20T2000.md` sec. 6): Paper 1's "baryon number for free" against the $B+L$ anomaly; the sphaleron as a collective class change outside SLOCC's scope; rule before v2. Also the Standard Model's own example of a record erased by action at $T = 0$ and by heat above the crossover, for the early-universe section.

## Checks owed before Paper 2 uses any of it

- Read and batch: Eling--Guedens--Jacobson 2006; Chirco--Liberati 2010; Jacobson 2016; Padmanabhan 2010, 2012; Maldacena--Shenker--Stanford 2016; Kovtun--Son--Starinets 2005; the ICO thermodynamics papers (Felce--Vedral 2020; Capela et al. 2023); Oreshkov 2019; Zych et al. 2019. All cited from memory in the notes.
- The trace anomaly and the bath's temperature as objections to "no fact of the scale factor above the electroweak crossover" (gravity note, sec. 5).
- The hierarchy $M_{P}/v$: the record's grain is a second scale beside $v$; say so wherever the Planck length is called the record's size.
- No grand-unification scale anywhere: the framework's ladder is QCD crossover, electroweak crossover, 3.6 TeV, Planck.
- Nothing in the thread is observational at accessible frequencies; Paper 2 must keep "standard decoherence rates, nothing gravity-specific".
- Unrecorded matter gravitates as a delocalised source (sphaleron note, section 20): energy-momentum is a record that persists by conservation, the field between events is not a fact below the resolution of the records; put beside the Page--Geilker paragraph. JS to rule whether the 3.6 TeV steriles are stable or the leptogenesis pair.
- **The boundary** (`boundary_gravity_of_unrecorded_matter_2026-09-21T1300.md`, JS's ruling 2026-09-21): the count-density dictionary must say which column gravity reads, tick-rate (Paper 1's dark-matter prospect) or records (Paper 2's abstract); the thread recommends the conserved-charge reading (c); if the dictionary cannot decide, Paper 2 must say the framework predicts nothing about dark matter. This is the first problem of the dark-matter companion named in Paper 1's summary.

## Where the pointers are

`notes/todo.md` (the Paper 2 section); comments in `paper2/paper2_main_2026-07-07.tex` beside the TODOs this thread answers (added 2026-09-20 by `scripts/patch_paper2_revisit_comments_2026-09-20T1900.py`); the auto-memory file `paper2-revisit-complex-cost-thread` for future sessions; this hub in `knowledge/project-docs/INDEX.md`.
