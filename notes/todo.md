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

## Bibliography hygiene

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
- [ ] Within that list, four are editorial decisions rather than tidying: both
      figures (`fig:wf-hopf-ladder`, `fig:myimage`) are unreferenced from the
      prose; every proposition in the zero-divisor appendix (`prop:zd-*`) is
      unreferenced although its central equation is cross-referenced; and
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
