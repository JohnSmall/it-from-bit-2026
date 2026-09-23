# Session note: the Born rule from the cost ledger, patched; and the 2026-09-18 to 20 thread

Date: 2026-09-20T1000. Fable session (deep thinking). JS: "Ok go ahead and make
the edits and update the knowledge history." This note records the two patches
applied today, the thread of thinking they close, the files produced since the
2026-09-18 session note, the ledger proposals collected for JS, and what was
not done.

## 1. Patches applied today (main working tree, uncommitted, not built)

Both are v2 material applied at JS's instruction to the checked-out `main`
working tree; no branch was made and nothing was committed. Backups are the
`.2026-09-20T1000.bak` and `.2026-09-20T0900.bak` files beside the targets.

**`scripts/patch_anti_event_real_cost_v2_2026-09-20T1000.py`** (v2 plan item
1). `paper1/what_is_a_quantum_state.tex`, sec:fanout-boundary: "without
thermodynamic cost" (twice) became "without real cost", and one sentence was
added: "The step from nothing to $kT\ln 2$ at the first copy is a placeholder:
once the amplitudes are complex (\S\ref{sec:complex-amplitudes}) the cost
before FANOUT is a phase, and the redundancy ladder of \S\ref{sec:wf-redundancy}
replaces the step by a rotation, paid by degrees as the copies accumulate." No
occurrence of "without thermodynamic cost" remains in the file.

**`scripts/patch_born_cost_ledger_v2_2026-09-20T0900.py`** (v2 plan item 2,
with 2b folded in). Three files, five edits, anchors verified with `--check`
before running:

- `paper1/what_is_a_quantum_state.tex`: new subsection "The cost of a record,
  and why it is a square", label sec:born-cost-ledger, inserted before "Scale
  and dimension of limits to information" (three paragraphs: the complex
  surprisal of an amplitude and the anti-event's $-\ln p - i\pi$; the record
  as the closed loop of a history and its return leg, $p = |\psi|^{2}$ with the
  exponent the number of legs, the loop of zero net period real on the complex
  temperature of the FANOUT appendix, the unclosed loop as the off-diagonal
  element redundancy removes; the status paragraph naming the two other
  routes, the shared fibre-blindness, the $|\psi|$ loophole closed by
  analyticity, and that none of the three routes needs Gleason's lattice so
  all hold for a single qubit; flagged structural, not theorem).
- `paper1/self_reference_section_2026-07-04.tex`, sec:born-rule: "lowest-degree
  invariant" became "lowest-degree polynomial invariant" with the clause that
  the non-polynomial $|\psi|$, of degree one, is excluded by the analyticity
  declared at sec:complex-amplitudes; and a back-reference: "The same square is
  reached from the cost side in \S\ref{sec:born-cost-ledger} ... neither route
  uses the lattice of projections that Gleason's theorem needs, and both hold
  for a single qubit."
- `paper1/derivation_of_the_quantum_postulates.tex`, sec:born-invariance: the
  same "polynomial" and analyticity wording; "two independent routes to one
  rule" became "three routes to one rule, each holding for a single qubit",
  naming the cost-ledger route.

Diff: 3 files, 75 insertions, 13 deletions. Checks run after patching: every
label the new text references exists exactly once (sec:l2-metric-fibre,
sec:fanout-boundary, sec:wf-redundancy, app:fanout-boundary, sec:born-rule,
sec:born-invariance, sec:complex-amplitudes, sec:born-cost-ledger); the one
new citation key, Landauer_1961, is in references.bib; braces balance in all
three files. **Compile status: not built.** The standing rule is that no build
runs without JS's say-so; the build is owed and should be run by whichever
session JS designates (`latexmk`, then `grep -E '^!' main.log`).

Forward pointers now in the text whose targets do not yet carry the promised
content: sec:wf-redundancy (plan item 5, the cost of a copy and the rotation)
and app:fanout-boundary (plan item 6, Hawking's rotation). The labels exist,
so the paper compiles; the pointers become true when items 5 and 6 land.

## 1a. Later the same day: the collective class conversion patch (2026-09-20T2100)

JS: "This needs to be noted in paper 1 and that the relationship between
conversions between classes becomes possible with several copies might be
related to the sphaleron anomaly. Is it possible to create a quantum circuit
for this?" Done both. `scripts/patch_collective_class_conversion_2026-09-20T2100.py`
re-scopes "baryon and lepton number conservation is class conservation" in
the absent-gate subsection to its single-register, perturbative meaning, adds
a paragraph on the 't Hooft vertex, the explicit two-copy GHZ/W conversions
(GHZ x GHZ -> W at 3/32; W x W -> GHZ at 2/9; three colour copies to one W at
3/64), B-L as the copy-additive count, the candidate reading of the vertex's
fermion content and the kinematic-room sentence, mints Open Problem
op:sphaleron (JS to keep or strip), and re-scopes the predictions section's
"gets for free". Labels checked; three new citation keys are undefined until
`bib/sphaleron_slocc_refs_2026-09-20T2100.bib` is imported (VERIFY-CITE, all
three). Constructions verified exactly in numpy and run as Qiskit circuits on
Aer (`scripts/multicopy_slocc_conversion_2026-09-20T2100.py`,
`scripts/qiskit_multicopy_slocc_circuit_2026-09-20T2100.py`); stdout in
`project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md`
sections 11 and 12. Not built; not committed.

## 1b. 2026-09-21 to 23: the scope statement and the two open-problem revisions

- 2026-09-21T0900 `patch_circuit_scope_statement_2026-09-21T0900.py`: the
  collective-conversion paragraph states what the two-copy circuits can and
  cannot do and promises gauge-respecting circuits in a subsequent paper.
- 2026-09-23, at JS's instruction, two patches drafted on 2026-09-21 applied:
  `patch_op_sphaleron_revised_2026-09-21T1000.py` (the motivating sentence and
  op:sphaleron: the sphaleron's winding is the weak vacuum's Chern--Simons
  number, not the charge winding of lem:winding-number, which it conserves;
  uniqueness under colour, the trace direction and $S_{3}$; a FAIL for a
  dictionary admitting the two-register conversion; PASS (iv) by computation
  with the charge operators; retitled "a collective class change") and
  `patch_op_sterile_gravity_boundary_2026-09-21T1300.py` (op:sterile-gravity
  retitled "a boundary", its three routes named with what the thread
  established, PASS/FAIL for the count-density dictionary, and one sentence in
  the spacetime section's deferred dark-matter paragraph). Diff: 3 files, 110
  insertions, 25 deletions. Labels all resolve once; braces balance; no old
  wording survives. Not built; not committed.

## 1c. 2026-09-23: notebook T re-run

JS asked what notebook T is for, then to run it and record the results. It is
the trigintaduonion-automorphism computation of 2026-08-27 (pure numpy, no
Qiskit): does doubling the sedenions add a further S_3 or only a Z/2 to the
automorphism group, does the identity component stay G_2, and which triple of
octonion subalgebras the doubling's S_3 permutes. Re-run unchanged:
Python 3.10.12, numpy 1.21.5, 3 min 11 s, exit 0; output byte-identical to the
2026-08-27 capture; saved as `notebooks/notebook_T_output_2026-09-23_rerun.txt`;
the notebook's markdown record gains a re-run paragraph. Exact stdout:

```
Notebook T -- trigintaduonion automorphisms (2026-08-27)
==================================================================
A_3 (dim   8): psi automorphism=True (worst 1.1e-16); eps automorphism=True; psi^3=I:True; eps^2=I:True; eps psi = psi^2 eps:True; psi mixes halves:True
A_4 (dim  16): psi automorphism=True (worst 1.1e-16); eps automorphism=True; psi^3=I:True; eps^2=I:True; eps psi = psi^2 eps:True; psi mixes halves:True
      lifted S_3 from A_3 is an automorphism: True; commutes with the new S_3: True; lifted psi distinct from new psi^k: True
A_5 (dim  32): psi automorphism=True (worst 1.1e-16); eps automorphism=True; psi^3=I:True; eps^2=I:True; eps psi = psi^2 eps:True; psi mixes halves:True
      lifted S_3 from A_4 is an automorphism: True; commutes with the new S_3: True; lifted psi distinct from new psi^k: True
A_6 (dim  64): psi automorphism=True (worst 1.1e-16); eps automorphism=True; psi^3=I:True; eps^2=I:True; eps psi = psi^2 eps:True; psi mixes halves:True
      lifted S_3 from A_5 is an automorphism: True; commutes with the new S_3: True; lifted psi distinct from new psi^k: True
------------------------------------------------------------------
Derivation-algebra dimension (identity component of Aut):
  dim Der(A_1) =  0   [expect 0]
  dim Der(A_2) =  3   [expect 3 (so(3))]
  dim Der(A_3) = 14   [expect 14 (g2)]
  dim Der(A_4) = 14   [expect 14 (g2, Schafer)]
  dim Der(A_5) = 14   [expect 14 (g2, Schafer)]
------------------------------------------------------------------
VERDICT
  S_3 branch at rungs 4, 5, 6 (Brown's psi is an automorphism, order three, mixing, not a lift): True
  Direct-product structure (new S_3 commutes with lifted S_3): True
  Identity component unchanged from the octonions (dim Der = 14 at n = 3, 4, 5): True
------------------------------------------------------------------
PART B -- the two triples
  Brown psi_4 stabilises setwise: core=True V_1=True V_2=True V_3=True
  Any element of Brown's S_3 carries V_1 into V_2: False
  Colour-line 3-cycle sigma: automorphism of O: True; lifted to S: True; fixes core pointwise: True; cycles V_1->V_2->V_3->V_1: True; commutes with psi: True
  Fix(psi_4) = span{e0, e8}: dimension 2
  VERDICT B: the core triple is permuted INSIDE G_2 (colour), not by the doubling's S_3: True
------------------------------------------------------------------
PART C -- the psi-orbit triple
  O, psi(O), psi^2(O) octonion subalgebras: True
  dim pairwise intersection: 1; dim triple intersection: 1 (the real line)
  each halving with e8 regenerates S (S = H (+) H e8): True
  eps psi^k fixes halving k pointwise, one each: True
  VERDICT C: Brown's S_3 permutes the three halvings of S through the fixed doubling unit: True
------------------------------------------------------------------
NOTEBOOK T: PASS -- (A) the fifth rung adds a further finite S_3 and no continuous symmetry, the Z/2-vs-S_3 dichotomy settled on the S_3 side over R; (B) the core triple is colour, permuted inside G_2; (C) the doubling's S_3 permutes the three halvings of S
```

Ledger proposal: close the open_problems.md line "Notebook T: extend
Cayley-Dickson constructor to trigintaduonions to settle Z/2 vs S_3 branch
dichotomy by construction" as settled on the S_3 side (2026-08-27, confirmed
2026-09-23); the results it supports are already in the results ledger's
sedenion entries and in the invalid_routes entry of 2026-09-12.

## 1d. 2026-09-23: notebook T closed in the ledger and recorded in the paper

At JS's instruction: (i) `knowledge/open_problems.md` gains a dated entry
"2026-09-23 -- notebook T settled" superseding the carried-over Z/2-versus-S_3
item (append-only; the old line stands with the new entry closing it);
(ii) the todo item is repaired (its path had been eaten by a shell heredoc)
and checked off; (iii) the two typeset passages that already state the
result (sedenion section, Wigner's-friend fifth-wire passage) point to the
notebook-record appendix, which had no entry for T, so
`scripts/patch_notebook_record_T_2026-09-23T0700.py` appends
\subsection{Notebook T} with label app:nb-T in the appendix's fixed template
(provenance with both runs, claim, design, verified outputs, hardware record
"numerics only", status, consistency). 67 lines added; labels and the three
citation keys resolve; braces balance; the appendix is input by main.tex.
Not built; not committed.

## 2. The thread this closes (2026-09-18 to 20)

- 2026-09-18: JS supplied Pearson et al. 2021 (thermodynamic cost of
  timekeeping). Note section 4e of the complex-cost note: clockwork versus
  register, the accuracy--entropy exchange rate, mass as a clockwork rate with
  no register. Batch `bib/clock_thermodynamics_refs_2026-09-18T1100.bib`.
- 2026-09-18: "Think about the relationships" between Shannon entropy and
  thermodynamics that the anti-event brings together. Project-docs note
  `two_columns_shannon_thermodynamics_action_2026-09-18T1200.md` with
  `scripts/two_columns_renyi_check_2026-09-18T1200.py`: the complex surprisal;
  $k_{B}T$ and $\hbar$ as the two exchange rates; second law versus
  single-valuedness; the real column split into record, redundancy in heat,
  and invisibility (a fidelity, not an entropy); the quantum geometric tensor
  as the second-order form.
- 2026-09-19: two papers on indefinite causal order. Project-docs note
  `indefinite_causal_order_fanout_2026-09-19T0900.md` with
  `scripts/quantum_switch_graded_fanout_2026-09-19T0900.py`: duration is a
  phase, order is a record; the switch's indefinite-order signal falls as
  $\cos^{R}\phi$ under graded FANOUT of the control; op:ico-threshold
  proposed.
- 2026-09-19: JS asked for the Koide-as-Rényi-1/2 remark to be expanded.
  Session note `koide_renyi_half_2026-09-19T1100.md` with
  `scripts/koide_renyi_profile_2026-09-19T1100.py`: four equivalent forms
  (Foot's angle, negativity, purity of the democratic mixture, power sums);
  the order-1/2 entropy is blind to the phase, which enters at cubic order.
- 2026-09-20: JS objected that adding the surprisals of an amplitude and its
  conjugate is just $|\psi|^{2}$. Conceded and corrected: the pairing is the
  Born rule, the content is in the pair that fails to close (the off-diagonal
  element, the influence functional); multiplication kills the phase, addition
  keeps its real part (the two-cycle/three-cycle mechanism of the Koide
  blindness). Two-columns note section 2 rewritten; Koide note and plan item 2
  amended.
- 2026-09-20: JS: "we've rediscovered the Born rule". Assessed in two-columns
  note section 2a: not rediscovered, re-derived along the paper's own
  fibre-privacy route with one gain, the $|\psi|$ loophole named and closed by
  the analyticity premise; the Hawking zero-net-period reading is CANDIDATE.
  JS then asked for the derivation to be integrated into the v2 complex-cost
  additions with back-references from the Hopf route, both routes holding for
  a single qubit unlike Gleason: drafted as the item-2 script, then applied
  (section 1).

## 3. Ledger proposals collected (labels are JS's to apply)

From the two-columns note (section 11 there):
- STRUCTURAL (arithmetic): the complex surprisal of an amplitude is half the
  Shannon surprisal of its outcome minus $i$ times the action over $\hbar$;
  an anti-event contributes $i\pi$; defined modulo $2\pi i$.
- ESTABLISHED (computation): decoherence exponent $-\ln|\lambda|$ and
  fragment entropy $h((1+|\lambda|)/2)$ are not proportional (ratio 0.24 to
  5.6); the former diverges, the latter saturates at $\ln 2$; for $R$
  fragments the joint entropy is bounded by $\ln 2$ while the local sum and
  the exponent are linear in $R$.
- CANDIDATE: $k_{B}T$ and $\hbar$ as the two exchange rates of one currency
  on the two sides of the FANOUT boundary; Margolus--Levitin and Landauer as
  the two floors.
- CANDIDATE: the real part of the complex cost is a fidelity (Rényi order
  one half), not an entropy; Landauer's form is its many-fragment limit.
- RHYME: $K = e^{-H_{1/2}}$; the Unruh--Hawking $2\pi$.

From section 2a of the same note (today):
- CANDIDATE: the Born rule read as the closed loop of the cost ledger (two
  legs, zero net period, real temperature). Now in the paper as
  sec:born-cost-ledger, flagged structural.
- ESTABLISHED (arithmetic): $|\psi|$ is a $U(1)$-invariant of degree one; the
  paper's "lowest-degree invariant" needed "polynomial" and the analyticity
  premise. Now fixed in both Born-rule sections.

From the ICO note (section 8 there):
- STRUCTURAL (computation): the graded switch's $X$-basis statistics,
  $P(\pm) = (1 \pm \mathrm{Re}[\Lambda c])/2$, signal falling as $\cos^{R}\phi$,
  restored exactly on uncomputation.
- CANDIDATE: duration is a phase, order is a record.
- CANDIDATE: the thermodynamic resource in switch refrigeration is the
  control's unrecorded coherence.
- OPEN: op:ico-threshold (finite or asymptotic definitisation of order), with
  PASS/FAIL.
- RHYME: the commutator as the holonomy of the order loop.

From the Koide session note (section 6 there):
- STRUCTURAL (arithmetic): $K = e^{-H_{1/2}(p)} = e^{-H_{2}(q)}$; Foot's
  $45^{\circ}$; purity $2/3$ of the democratic mixture; the phase enters the
  power sums at cubic order.
- CANDIDATE: quadratic invariant fixes the Koide ratio, cubic fixes the
  individual masses; a max-entropy statement one bit below democratic.

open_problems: op:complex-cost criterion (i) restated (plan item 10);
op:ico-threshold new. invalid_routes: none.

## 4. VERIFY-CITE, all from memory unless noted

Margolus and Levitin 1998; Dahlsten, Renner, Rieper and Vedral 2011; Faist,
Dupuis, Oppenheim and Renner 2015; Tomamichel, Colbeck and Renner 2009;
Provost and Vallee 1980; Berry 1984; Hartle 2008; Goldstein and Page 1995;
Gell-Mann and Hartle 1990; Baez and Pollard 2015; Caticha 2011; Connes and
Rovelli 1994; Zurek 2005 (envariance); Masanes, Galley and Müller 2019;
Aaronson 2004 (island); Aharonov and Reznik 2002; Foot 1994; König, Renner and
Schaffner 2009; Araújo et al. 2015; Felce and Vedral 2020; Nie et al. 2022;
Guha, Alimuddin and Parashar 2020; Simonov et al. 2022; Capela, Verma, Costa
and Céleri 2023; Oreshkov, Costa and Brukner 2012; Chiribella et al. 2013;
Goswami et al. 2018; Oreshkov 2019; Zych et al. 2019; the Zygon paper's volume
and pages. In the clock batch, VERIFY-CITE: Erker 2017, Barato and Seifert
2016, Milburn 2020, Schwarzhans 2021, Guryanova 2020, Lan 2013. None of these
is cited in the paper text yet; the patched subsection cites only
Landauer_1961.

## 5. Not done, and for the Opus session

- No build (rule). No commit (rule). No v2 branch: the two patches sit on the
  `main` working tree; if JS wants v1's `main` untouched, branch from the tag
  `paper1-v1` before committing and carry the working tree across.
- The forward pointers to items 5 and 6 are promises until those land.
- Verification and batching of the references above; import and re-export.
- The remaining v2 items in the plan's order of work (5 and 9 first).
- op:ico-threshold needs an SDP solver in the Python environment.
