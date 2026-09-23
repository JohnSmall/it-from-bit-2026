# Paper 1 v2: the complex-cost revision, a plan

Date: 2026-09-18T1000. Written by the Fable session at JS's instruction that
the complex-cost clarifications of 2026-09-16 to 18 "need to be in paper 1
(version 2)". v1 is on Zenodo (DOI 10.5281/zenodo.22755871) and carries JS's
note in the conclusions that the pre-/post-FANOUT cost split is wrong and
too late for v1. This plan lists every v2 insertion with its target
passage, where its draft lives, its label, and what it depends on, so the
patches can be written in order once a v2 branch exists.

Sources: `knowledge/project-docs/complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`
(sections 1--8, "the note" below) and
`knowledge/sessions/graded_fanout_complex_cost_2026-09-18T0830.md` ("the
session note"), with `notebooks/notebook_S_graded_fanout_complex_cost_2026-09-18.ipynb`
as the computation.

## 0. Process

- v2 is a branch from the tag that marks the Zenodo upload (`paper1-v1`);
  nothing below touches main until JS says so. 2026-09-20: JS said so for
  items 1 and 2, which are applied on the main working tree, uncommitted;
  whether to branch before committing is JS's call. The seven passages that say "free"
  (note, section 1) are the checklist; every one is either corrected or
  given the forward pointer of item 1.
- The conclusions' "Updates" note of v1 is replaced by one sentence saying
  v2 makes the correction, with the section references.
- All numbers quoted come from the notebook and the numpy script, seed
  20260918; the hardware run the Opus session is setting up (IBM backend,
  phase-only test) is added to the appendix of item 9 when it exists.

## 1. The promissory note at the first mention

Target: `what_is_a_quantum_state.tex`, the paragraph "Before FANOUT no
classical records exist ... An anti-event erases information without
thermodynamic cost" (v1 line 438).
Change: "without thermodynamic cost" becomes "without real cost", and a
sentence says the jump from zero to $kT\ln 2$ at the first copy is a
placeholder corrected in the redundancy ladder (item 5), needing the
complex amplitudes of the next subsection and the redundancy of that one.
Draft: JS's proposal of 2026-09-18 and the Fable reply (session transcript;
wording in the note's section 1 to be added at patch time).
Label: expository. Depends on: nothing.
**Applied 2026-09-20** on the main working tree, uncommitted, not built:
`scripts/patch_anti_event_real_cost_v2_2026-09-20T1000.py`; see
`knowledge/sessions/born_cost_ledger_patch_2026-09-20T1000.md`.

## 2. The anti-event's cost at the complex-amplitude step, and the Born rule from the cost ledger

Target: `what_is_a_quantum_state.tex`, a new subsection "The cost of a
record, and why it is a square" (label sec:born-cost-ledger) inserted before
"Scale and dimension of limits to information", at the end of the
complex-amplitudes discussion and before either later Born-rule section.
Change (JS, 2026-09-20: "integrate this derivation into the additions we're
going to do for complex temperature pre-FANOUT, and refer back to it in the
section where we derive the Born rule via the Hopf route"): three paragraphs.
The complex surprisal of an amplitude, additive, modulo $2\pi i$; the
anti-event as $-\ln p - i\pi$, its imaginary part the whole of its cost before
FANOUT (consistent with item 1's "without real cost"), forward pointers to
items 5 and 6. The record as a copy, a copy as a correlation with one factor
per party, the return leg the conjugate; Landauer makes the record's
surprisal real and additive, hence $-\alpha\ln|\psi|$, and the loop fixes
$\alpha = 2$ as the number of legs; the L2 normalisation makes it a
probability; the loop carries no phase, a record is a loop of zero net period,
real on the complex temperature of item 6; the unclosed loop is the
off-diagonal element that item 5 removes. Then the status paragraph: same
quadratic as sec:born-rule and sec:born-invariance, shared fibre-blindness,
the $|\psi|$ loophole closed by analyticity, none of the three routes needs
Gleason's lattice, all hold for a single qubit, structural not theorem.
Drafted in full as `scripts/patch_born_cost_ledger_v2_2026-09-20T0900.py`
(anchors verified with `--check` on 2026-09-20). The same script carries the
back-references of item 2b, so item 2b is folded in here and the three edits
land together. **Applied 2026-09-20** on the main working tree at JS's
instruction, uncommitted, not built; labels and the one citation checked;
see `knowledge/sessions/born_cost_ledger_patch_2026-09-20T1000.md`.
Draft: note section 3(b); session note section 7; two-columns note section
2 (the complex surprisal, the half, the branch), which supplies the three
sentences and the citations Hartle 2008 and Baez--Pollard 2015 (once
verified) so the reader knows what is old and what is new. Wording fixed
2026-09-20: the complex cost is the surprisal of a pair of histories, one
run backward (the density-matrix element, the influence functional), and
reduces to Shannon's surprisal only when the pair closes; never say that
"phases cancel between a path and its time-reverse" as if it were a
mechanism, it is the Born rule.
Label: CANDIDATE for the cost-ledger reading; ESTABLISHED (arithmetic) for
the $|\psi|$ loophole and its closure. Depends on: item 1 (the "without real
cost" wording it refers to) and items 5 and 6 existing to point at; the
labels sec:wf-redundancy and app:fanout-boundary already exist, so the
script compiles before 5 and 6 land, and only the pointers' content waits.

## 3. The five faces become graded

Target: `continuity_section_2026-07-04.tex`, "Five faces of one regime"
(v1 line 72 ff.), and the pointer subsection "Reversible continuity" in
`what_is_a_quantum_state.tex` (v1 line 560, "erasing information has no
thermodynamic cost").
Change: "no classical record" is $|\lambda| = 1$ for every fragment; the
faces fail together and by degrees, with the angle of item 5 as the degree;
"no thermodynamic cost" becomes "no real cost".
Draft: session note section 5.
Label: CANDIDATE. Depends on: item 5.

## 4. The global phase as the free part of the cost

Target: `L2_metric_global_phase_section_2026_06_07.tex`, the subsection
"The fibre as self-referential ignorance".
Change: one clause: the part of the phase that is free is the observer's
blind spot; a relative phase is observable and reversible; declaring a
phase inaccessible is the payment.
Draft: session note section 7.
Label: CANDIDATE. Depends on: item 5.

## 5. The resolution: the cost of a copy, in the redundancy ladder

Target: `wigners_friend_in_the_hopf_picture_2026-06-13.tex`,
sec:wf-redundancy, after "their private phases, each fragment's own
self-ignorance, fail to add coherently and wash out"; and the earlier
sentence "The single relational copy is unitary and free; the $kT\ln 2$
cost is incurred ... by the amplification" (v1 lines 265--269).
Change: define the cost of a copy, $-\ln\lambda_k$, real part the record,
imaginary part the phase, $i$ times the Feynman--Vernon influence action;
state the rotation ($1/\sqrt{R}$ for independent fragments; none for a
replica environment); Landauer recovered at the plateau while the real
cost accumulates as redundancy; the phase is what fails to proliferate.
"Free" at $R = 1$ becomes "$\gamma_1 - i\theta_1$, the real part small but
not zero". Cite Zurek (`zurek_2009`, `zurek2003decoherence`), Feynman and
Vernon, Caldeira and Leggett, and, once verified, Guryanova, Friis and
Huber 2020 (`guryanova2020projective`) for the infinite cost of a perfect
record, $-\ln|\lambda_k| \to \infty$ as $|\lambda_k| \to 0$ (note section
4e); refer to the appendix of item 9 for the numbers.
Draft: session note sections 1--3 and 5; note section 4b; two-columns note
section 5 for the three real quantities, which the text must name: the
record (joint entropy, one bit; "Landauer at the plateau" is said of this),
the redundancy priced in heat (the local fragment-entropy sum, linear in
$R$), and the invisibility of the phase (the decoherence exponent, the real
part of $C$, a fidelity, linear in $R$ with a different slope). No sentence
may call $C$ or its real part an entropy.
Label: STRUCTURAL for the cost and the rotation; CANDIDATE for the
framework's reading. Depends on: complex amplitudes (item 2's section),
the redundancy ladder's own $R$.

## 6. Hawking's rotation, in the FANOUT-boundary appendix

Target: `appendices/fanout_boundary_section_2026-07-06.tex`, the paragraph
"The thermodynamic reading is Landauer's ... pre-firing there is nothing
to pay for" (v1 lines 160--165).
Change: "nothing to pay for" becomes "nothing real to pay; the phase
accrues"; add that at imaginary inverse temperature the Caldeira--Leggett
noise kernel is a phase ($\coth(ix) = -i\cot x$), Hawking's CTC bath
(`Hawking1995QuantumCurves`), and that the real part Hawking inserts by
hand is here the fragment sum with angle $1/\sqrt{R}$.
Add one sentence pairing Margolus--Levitin (a floor on action for an
anti-event, $\pi\hbar/2$) with Landauer (a floor on heat for a record), the
two columns' floors (two-columns note section 3; Margolus and Levitin 1998,
Physica D 120(1-2), 188--195, doi 10.1016/S0167-2789(98)00054-2, verified
2026-09-20 and batched in `bib/two_columns_action_refs_2026-09-20T2200.bib`;
body not read, so the $\pi\hbar/2$ floor is not checked against them, and
the Mandelstam--Tamm companion for the energy-spread form has no Crossref or
INSPIRE record and is still unbatched).
Frame (added 2026-09-20): write Landauer's reading as $Q = \Delta S/\beta_{c}$
with $\beta_{c} = \beta + it/\hbar$ and name its four corners, Landauer's heat
(real, real), Planck's $E = \hbar\omega$ (imaginary, imaginary), the width and
the Matsubara frequencies (the mixed cells); "the phase accrues" becomes
"the cost sits in the Planck cell", and the rotation runs from that cell to
Landauer's through the width cell. The thermal time $\hbar/k_{B}T$ as the
crossover between action-paid and heat-paid records, one sentence. Draft:
`knowledge/project-docs/landauer_temperature_fanout_energy_2026-09-20T1200.md`
sections 2 and 3.
Draft: session note section 4; note section 3(a).
Label: STRUCTURAL for the identity and the four corners; CANDIDATE for the
mapping and the rotation.
Depends on: item 5.

## 7. Mass: the two accounts identified, and the width

Target: `masses_section_2026-06-08.tex`, "What mass is: associator-debt",
after the debt-to-defect bridge splice ("the associator prices the debt
at issuance ... the sedenion norm defect is where it settles").
Change: a paragraph identifying issuance with the imaginary column and
settlement with the real column: the debt per composition step is the
phase per tick of proper time, the Compton clock; the associator's
inverse-length dimension is that rate; the uniform associator magnitude is
why a mass is a constant; the magnitude is fixed at the vertex. Then a
paragraph on the complex pole $m - i\Gamma/2$ as the complex cost rate:
decay channels are the records, open when the products reach a continuum
(Fermi's golden rule), the optical theorem filling the two columns,
stability as the absence of an admissible record, oscillation and virtual
loops writing nothing. Cite the Compton-clock experiment and de Broglie
1924 for the clockwork's rate, and Pearson et al. 2021 (`pearson2021timekeeping`) for the
register's price: entropy per registered tick, linear in accuracy, none for an unregistered
clockwork (note section 4e); write "one clockwork cycle per half period; nothing is
registered", not "one anti-event per half period". A textbook for the optical theorem.
Draft: note section 4a and 4d, including the "decay channels as records"
paragraph; and (2026-09-20) one clause each citing the Planck cell for the
clock (the electron's anti-event over half a Compton period returns
$m_{e}c^{2}$, Part A of the Landauer-temperature script) and the width cell
for the pole.
Label: STRUCTURAL for the physics; CANDIDATE for the identification;
RHYME for the top at the calibration bound (keep out of the text or fence
it in one clause).
Depends on: items 5 and 6 for "record" and "real cost".

## 8. op:associator-geodesic: the proposed reconciliation

Target: the open problem `op:associator-geodesic` in the masses section.
Change: add the candidate route: the geodesic proxy computes accrued
action, steps times per-step debt; the length that mass multiplies is the
worldline's proper time, not an internal geodesic, so the March retraction
stands. PASS/FAIL unchanged.
Draft: note section 4d, "a route for op:associator-geodesic".
Label: CANDIDATE. Depends on: item 7.

## 9. New appendix: Computation S

Target: a new file `appendices/appendix_computation_S_graded_fanout_<date>.tex`,
input after the hardware appendix, in the style of the Qiskit appendices.
Content: the circuit; the closed forms; the rotation table ($R = 1..12$,
the $1/\sqrt{R}$ law); the graded boundary at $R = 1$; the plateau figure
(export the notebook's PNG); the phase-only test on Aer (P(+) = 0.0053
against 0.0050 for $\theta_k = 1$; reversal 1.0000; untracked average 0.826
against 0.829); the hardware run when the Opus session has it, with device
decoherence noted as a real-cost term the model omits.
Draft: the notebook's markdown cells; session note "The Qiskit notebook".
Label: STRUCTURAL (computation). Depends on: nothing; the hardware cell on
Opus.

## 10. The open problem op:complex-cost

Target: with item 5 (end of sec:wf-redundancy) or with item 6.
Statement: define $C$ for general couplings with energy exchange and show
(criterion (i), restated 2026-09-18T1200) that for a thermal environment of
$R$ fragments the local fragment-entropy sum reproduces Landauer's heat per
record and the joint entropy saturates at the record's size, while
$\mathrm{Re}\,C$ is the decoherence exponent, bounded below by the
single-shot max-entropy cost and never itself a heat; prove the
phase-recoverability bound $\prod_{k\notin F}|\lambda_k| \to 1$; derive the
real part of Hawking's complex inverse temperature as the fragment sum.
PASS: all three with the $1/\sqrt{R}$ law, and (added 2026-09-18, note
section 4e) the exchange rate $r^{2}\,\mathrm{Re}\,C = $ const reducing, for a
register of $R$ fragments, to a phase--entropy relation of the form
$\langle\delta\phi^{2}\rangle\,\Delta S_{\rm tick} \geq$ const (Pearson et al.
2021, eq. (3) with (B1)) that respects the thermodynamic uncertainty
relation; and (added 2026-09-20) derive the mixed cells of $Q = \Delta S/\beta_{c}$,
the width and Matsubara entries, from the Feynman--Vernon functional, so
that the table of the Landauer-temperature note is a result and not
bookkeeping. FAIL: a replica environment paying a real cost, a record's
entropy acquiring an imaginary part, a register beating the TUR, or any
sentence equating $\mathrm{Re}\,C$ with a heat.
Draft: session note, proposed open_problems entry; note section 6.
Label: OPEN. Depends on: item 5.

## 11. Motion as phase, and the closed-loop quantisation (optional for v2)

Target: one forward pointer from item 5 to Paper 2 (free propagation as
phase accumulation, the track as the redundant record, Mott, Joos--Zeh;
and, added 2026-09-19, "duration is a phase, order is a record": the quantum
switch under graded FANOUT of its control, note
`knowledge/project-docs/indefinite_causal_order_fanout_2026-09-19T0900.md`,
which is the graded form of Paper 1's "never amplified into records while
remaining indefinite" and belongs in Paper 2's causal-order section; and,
added 2026-09-20, the high-temperature note
`knowledge/project-docs/records_causal_structure_high_temperature_2026-09-20T1400.md`
for Paper 2: thermal time as the causal resolution, no proper time above the
electroweak crossover, the area law as record capacity);
and, if JS wants it in v2, a remark in the spacetime section that
consistency of transport around a closed loop is single-valuedness of the
phase, $\oint p\cdot dx = 2\pi n\hbar$, with the Koide phase as the
contrasting open-path case.
Draft: note section 4c.
Label: CANDIDATE. Depends on: item 7; JS's call on scope.

## 2b. The Born rule's wording: "polynomial", and the analyticity premise (added 2026-09-20; folded into item 2's script)

Target: `derivation_of_the_quantum_postulates.tex`, sec:born-invariance,
"There is no $U(1)$-invariant of degree one; the lowest-degree invariant is
quadratic"; and `self_reference_section_2026-07-04.tex`, sec:born-rule, "The
lowest-degree invariant of a complex amplitude is the quadratic $|\psi|^{2}$".
Change: $|\psi|$ is a $U(1)$-invariant of degree one, so both sentences need
"polynomial", and one clause naming what excludes the non-polynomial
invariant: analyticity in the amplitude, the premise declared at the Shannon
step (sec:complex-amplitudes), under which $|\psi|^{\alpha}$ is admissible
only for even $\alpha$. Optionally one sentence in sec:born-rule reading the
square as the closed loop of the cost ledger (forward and return legs; the
record's cost real because the loop's net period vanishes), CANDIDATE.
Draft: two-columns note section 2a.
Label: ESTABLISHED for the loophole and its closure (arithmetic); CANDIDATE
for the loop reading. Depends on: nothing; could go in a v1.1 erratum before
the rest of v2 if JS wants the weakness closed early.

## 2c. The baryon-number sentences: "perturbative" (added 2026-09-20T2000)

Target: `interactions_circuits_section_2026-06-08.tex`, "Baryon and lepton
number conservation \emph{is} class conservation"; `predictions_section_2026-06-13.tex`,
"which the framework gets for free"; the absent-gate section.
Change: re-scope to perturbative: class conservation forbids a single-register
GHZ--W gate (no leptoquark, no perturbative proton decay); the Standard
Model's non-perturbative $B + L$ violation is a collective conversion of
twelve registers at a unit change of winding, outside the gate set, conserving
$B - L$, negligible today and unsuppressed above the electroweak crossover; not
excluded by the framework. One clause on the reduced spectrum being a
local-unitary invariant that separates the canonical orbits, the three-tangle
being the class invariant.
Draft: `knowledge/project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md`
section 6, with op:sphaleron's restated PASS/FAIL to mint beside it.
Label: the re-scoping ESTABLISHED (the Standard Model's anomaly); the
collective-conversion reading CANDIDATE; the two-copy conversions STRUCTURAL
by construction (numpy exact; Qiskit on Aer). **Applied 2026-09-20T2100** on
the main working tree at JS's instruction ("This needs to be noted in paper
1"), uncommitted and unbuilt, by
`scripts/patch_collective_class_conversion_2026-09-20T2100.py`, including
Open Problem op:sphaleron in the text for JS to keep or strip; batch
`bib/sphaleron_slocc_refs_2026-09-20T2100.bib` (verified 2026-09-20 and
corrected in place; a fourth key, `thooft1976quantum`, was added for a
proposed fix). **One discrepancy found:** 't Hooft 1976's own Eq. (24) is
the two-generation model, eight fermions with $\Delta B = \Delta L = 2$, not
the twelve with $\Delta B = \Delta L = 3$ the paper attributes to him. The
proposed wording is in section 13 of
`knowledge/project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md`;
the paper is NOT edited.
Still owed: the references read; the reduced-spectrum clause in
`entanglement_classes_and_gauge_groups` (not patched).
Also owed (2026-09-20T2200): "the three supplied by colour" in the new
paragraph should read "by colour and hypercharge together", citing
prop:trace-blind; see the sphaleron note section 14 ("Why twelve, when two
would do"). Also owed, from the Opus session's section 13 there: 't Hooft's
Letter treats the two-generation model (eight fermions, Delta B = Delta L = 2);
cite thooft1976quantum beside it and, if wanted, the one-sentence parenthesis
proposed there. JS to accept or decline. 2026-09-21T0900: the paragraph
gained the circuit scope statement (what the two-copy circuits can and
cannot do; gauge-respecting circuits for a subsequent paper), applied by
`scripts/patch_circuit_scope_statement_2026-09-21T0900.py`. 2026-09-23: the
op:sphaleron revision (two windings, hypercharge in the uniqueness, the
two-register FAIL, computable PASS iv) and the op:sterile-gravity boundary
restatement applied at JS's instruction.

## 11a. The Jaynes appendix: the complex multiplier (added 2026-09-18T1200)

Target: `appendices/appendix_jaynes_fibration_2026-07-19.tex`, the closing
status section or the mixed-states subsection.
Change: one paragraph: the complex inverse temperature $\beta_{c} = \beta +
it/\hbar$ is Jaynes's multiplier continued to the complex plane, real part
inference (the records' side, $k_{B}T$), imaginary part dynamics (the
inside, $\hbar$); "time is operation count" is the statement that the
imaginary multiplier counts composition steps. Optionally one sentence in
sec:cencov-route naming the quantum geometric tensor (Fubini--Study plus $i$
times Berry curvature) as the second-order form of the two columns.
Draft: two-columns note sections 3 and 6.
Label: CANDIDATE (the multiplier); STRUCTURAL (the tensor). Depends on:
item 2.

## 12. Ledgers (for the Opus session, at v2 time)

- results_ledger: the STRUCTURAL items of the session note (the cost as
  $-\sum\ln\lambda_k$; the $1/\sqrt{R}$ rotation; $\coth(ix) = -i\cot x$;
  the width as the real cost rate via the optical theorem; uniform
  associator implies a constant clock) and the CANDIDATE readings
  (graded boundary as rotation; issuance/settlement as imaginary/real;
  decay channels as records; free part of the phase as the blind spot).
- invalid_routes: the v1 statement "erasure before FANOUT is free and
  Landauer applies at the first copy", retired as too sharp (not false
  about real heat; false about the cost being zero).
- open_problems: op:complex-cost with criterion (i) as restated in item 10;
  op:associator-geodesic gains its candidate route.
- results_ledger, from the two-columns note (section 11 there): the complex
  surprisal (STRUCTURAL), the three real quantities (ESTABLISHED as
  computation), the two exchange rates (CANDIDATE), the fidelity-not-entropy
  reading (CANDIDATE), and the two rhymes.

## 13. References: verified and batched 2026-09-20

All verified by the Opus session on 2026-09-20 against Crossref by DOI, with
INSPIRE-HEP and the arXiv API where a paper has no Crossref record. **Every
journal, volume and first page in the list this section used to carry was
right**; the corrections were page ranges, titles, issue numbers and DOIs
added, plus the four exceptions named below. Nothing in any batch is from
memory any longer. No body was read except Guryanova, Friis and Huber 2020,
Chirco and Liberati 2010, Chitambar, Duan and Shi 2008 and Foot 1994, so what
any other paper argues is still this project's own summary of it.

Batches written, all awaiting import and re-export:

- `bib/complex_cost_v2_refs_2026-09-20T2200.bib` --- Feynman and Vernon 1963,
  Caldeira and Leggett 1983, de Broglie 1925, del Rio et al. 2011, Reeb and
  Wolf 2014, Mott 1929, Joos and Zeh 1985, Peskin and Schroeder 1995.
- `bib/two_columns_action_refs_2026-09-20T2200.bib` --- the fourteen from the
  two-columns note, sections 9 and 2a.
- `bib/clock_thermodynamics_refs_2026-09-18T1100.bib` --- corrected in place;
  all seven verified, Guryanova et al. read in full.
- `bib/koide_renyi_refs_2026-09-20T2200.bib`,
  `bib/indefinite_causal_order_refs_2026-09-20T2200.bib`,
  `bib/landauer_temperature_refs_2026-09-20T2200.bib`,
  `bib/records_high_temperature_refs_2026-09-20T2200.bib`,
  `bib/jacobson_nonequilibrium_refs_2026-09-20T2200.bib`,
  `bib/multicopy_slocc_refs_2026-09-20T2300.bib` (the Fable session's, which
  superseded the Opus session's 2200 duplicate) --- the other documents'
  lists.
- `bib/sphaleron_slocc_refs_2026-09-20T2100.bib` --- corrected in place; this
  is the urgent one, since the paper cites its keys now.

Four things in this section's old list need a decision, not just a field.

1. **de Broglie is 1925, not 1924, if it is the published paper.** The thesis
   was defended in Paris in November 1924; the text with a DOI is Annales de
   Physique, series 10, volume 3, pages 22--128, dated 1925. The batch has the
   published version. If item 7 means the thesis, it wants a `@thesis` entry
   instead and the two must not both be imported.
2. **Peskin and Schroeder must not be taken from Crossref.** Crossref has only
   the 2018 CRC reissue and its record drops Schroeder from the author list.
   The batch uses the 1995 Addison-Wesley printing, whose ISBN is the one
   field no database confirmed.
3. **Mott's title in Crossref is corrupt**, carrying U+221D where the Greek
   alpha belongs. The batch writes `$\alpha$`.
4. **Berry 1984 was already in the library** as `berry1984quantal` and is
   correct as it stands, so it is not batched.

## 14. Order of work

Items 5 and 9 first (the resolution and its computation), then 1, 2 (its
script is written and anchor-checked; run it after item 1 so the "without
real cost" wording it cites is in place), 3, 4 and 6 (the pointers and the
corrected statements, which need 5 to exist), then 7, 8 and 10 (mass, the
geodesic route, the open problem), then 11 at JS's discretion. Each as a sentinel-gated patch with its diff shown; the
seven-passage checklist re-run at the end so no "free" survives
unqualified, and a second grep for "entropy" so that no sentence calls the
complex cost or its real part an entropy.
