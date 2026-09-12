# Corrections Ledger: the Two Sedenion Triples (2026-08-27)

Notebook T (Parts B-C, same date) established: Brown's S_3 -- the doubling's new factor --
stabilises each octonion copy `core (+) V_i` through the quaternion core; the map cycling those
copies is a lifted G_2 element (the colour-line three-cycle, fixing the core pointwise); the
core triple is therefore COLOUR structure, the March finding one rung up. The doubling's S_3
permutes the three HALVINGS `O, psi O, psi^2 O` instead, and generations are the psi-orbit
(as in Gresnigt-Gourlay-Varma 2023 and Gresnigt 2026). This ledger lists every committed-corpus
location carrying the old attribution, with a suggested fix and handling. Adjudication is JS's;
nothing here has been patched. The uncommitted 2026-08-25 section draft is already superseded by
the 2026-08-27 revision, which needs no entry.

## Paper sources (.tex, in-place edits warranted)

1. `particle_zoo_section_2026-06-08.tex`, triality paragraph ("Three generations and the
   doublet"): "singles out the three Fano lines through that direction --- ... --- each a
   quaternionic subalgebra; these are the three generations."
   WHY WRONG: contradicts the corpus's own March finding (octonion_generations_calculation.md,
   sec. 4: the three lines through the preferred direction are three COLOURS within one
   generation). The lines are the colour basis of C^3.
   FIX: re-voice as a colour statement or drop the generation identification; let the
   generation count rest on the sedenion promotion (sec:sedenions-generations), which the
   signpost now points to. Also adjust the following sentence "Triality gives three; the K_3
   obstruction refines this..." accordingly.

2. `particle_zoo_section_2026-06-08.tex`, sec:sedenion-announcement: "The octonions'
   automorphism group G_2 contains no S_3" and "acting by permuting three octonion subalgebras
   whose triple intersection is a shared quaternionic core."
   WHY WRONG: G_2 contains many S_3 subgroups (G_2 > SO(3) > S_3); the correct statement is
   that G_2 is CONNECTED (no component group) and triality is not induced by any automorphism
   of O. And the core triple is not what Brown's S_3 permutes.
   HANDLING: this subsection is REPLACED wholesale by the signpost
   (`zoo_sedenion_pointer_replacement_2026-08-25T0700.tex` + its patch, both updated
   2026-08-27); the signpost's own wording ("gains exactly the finite factor S_3 that the
   octonions lack") is factor-language and stands. No separate edit needed IF the signpost
   patch is run; otherwise both sentences need the fixes above.

3. `appendices/appendix_hardware_fez_2026-07-10.tex`, app:hw-ckm: "the S_3 permuting three
   intersecting octonion subalgebras that share a quaternionic core
   \autocite{gillardgresnigt2019three}".
   FIX: "...as a permutation factor, Aut(S) = G_2 x S_3, whose order-three element rotates the
   register's octonion into its doubled copy; the three generations are its orbit
   (\S\ref{sec:sedenions-generations}, Remark on the two triples)". Keep the Brown cite; the
   gillardgresnigt2019three cite can move to the two-triples remark's context or stay with a
   "first construction" gloss.

4. `masses_section_2026-06-08.tex`, op:up-quark, the 2026-07-12 clause: "notebook M's
   route-closure recorded (bare geometry contains no 2/9; bare cross-algebra vertex maximal;
   the dressing carries the entire suppression)".
   WHY AFFECTED: M's pi/4 vertex is a cross-V_i (colour-triple) statement; whether the bare
   cross-HALVING vertex is also maximal is not yet computed.
   FIX: add one flag clause, e.g. "; the scan ran on the core triple and its verdict awaits
   re-execution on the psi-orbit (notebook T, two-triples correction)" -- do not delete the
   record. Notebook N's pre-registered first hypothesis inherits the same flag.

## Project documents (.md, dated addenda -- statuses never upgraded/downgraded in place)

5. `sedenion_generations_mechanism_2026-07-10.md`, secs 1-2 ("Aut(O) = G2 contains NO S3";
   "Three generations = the S3-orbit of the three octonion subalgebras O_1, O_2, O_3
   (Gillard-Gresnigt triple)"; "Shared triple-intersection H = the electroweak core => WHY all
   generations carry identical EW quantum numbers").
   ADDENDUM: the S3-orbit is of the halvings, not the core copies; gauge-equivalence follows
   from the direct product, not the shared core; the core copies are colour. Point at notebook
   T and the 2026-08-27 section.

6. `fourth_qubit_ckm_pmns_2026-07-06.md`, sec 3 (same three-copies-through-the-core grounding).
   ADDENDUM: same correction; the "framework resonance: generations share their electroweak
   (H-rung) machinery" sentence is the part that dies -- what survives is gauge-blindness via
   the direct product.

7. Constructor note 2026-08-12 (copies-through-the-spine): "the CP^2 of octonion copies through
   the core".
   ADDENDUM: that CP^2 is colour space (the projective plane of colour directions); the
   classification ledger's "two moduli spaces ... Relation: open" is thereby partially
   resolved -- they are different objects because one is colour kinematics and the other is
   mixing moduli.

8. `classification_ledger_d4_arena_2026-08-16T0522.md`, sec 4(c): "The same pair
   (V4, S3 = Aut(V4)) that organises the sedenion side -- sectors graded by K = Z2 x Z2,
   generations permuted by S3 = Aut(K)".
   ADDENDUM: the Klein grading {core, V_1, V_2, V_3} is the colour grading; "generations
   permuted by S3 = Aut(K)" is the logged invalid route. Conjecture 3(a) ("both S3's are
   literally Spin(8) triality ... ONE action seen twice") should be restated against the
   halvings before any work is spent on it.

9. Notebook M's record (`appendices/appendix_notebook_record_2026-07-11.tex`, entry M).
   ADDENDUM (one sentence in the appendix or a dated note alongside): computations stand;
   interpretation re-pointed per notebook T Part B; generation-side re-run owed.

## Optional consumer-pointer (already drafted, not patched)

10. `hopf_justification_section_2026-06-08.tex`, the two-climbs paragraph: the one-clause
    stitch "(unbounded in length, and --- as \S\ref{sec:wf-chain-type} records --- bounded in
    type...)" is supplied in the splice header for JS to apply or skip.

## What does NOT need correction

The register-side K_3 construction itself (the count, the doublet, the sterile class); the
flavour-conservation splice and no-force propositions (they argue from gate structure, not from
the core triple); prop:gsm, confinement, theta_QCD; the Cabibbo circuit and its numbers; the
signpost prose; Gresnigt citations as such (the line's own later papers are the corrected
mechanism's source).
