# To do

Actionable items with enough context to act on without reconstructing the
reasoning. Delete when done.

## Zotero housekeeping


## Manuscript

- [ ] Place the remaining two fragments in `orphans/`, both structural rather
      than mechanical: `summary_section_2026-07-07.tex` is a whole section
      needing an \input line in main.tex, and
      `headline_results_snippet_2026-07-07.tex` is an introduction list its
      own header says you were to approve or veto item by item.
      `associator_debt_higgs_mechanism_2026-07-03.tex` is done: its
      norm-defect version replaced the subsection in
      `paper1/boson_masses_section_2026-06-08.tex` and it is atticked. Some may be splice sources
      whose content already lives in a section, in which case they are
      superseded rather than pending -- `jaynes_paragraph_2026-07-19.tex` has
      a live counterpart of the same date, so diff before deciding.
      `spacetime_additions_2026-07-04.tex` carries a header warning about
      colliding with the Overleaf state, which no longer exists.
- [ ] Check the cross-reference from `predictions_section` line 227 ("no
      experiment will ever hold a record of indefinite causal order") through
      to the qualified statement in `sec:no-quantised-gravity`. That
      qualification now carries more weight, see `ideas.md`.
- [ ] Complete the four framing prose sections for Paper 1 -- introduction,
      abstract, preamble check, conclusions. Named in the project memory as
      the only thing between Paper 1 and arXiv submission.

## Aaronson citation

- [ ] Add `chapter = {9}` to `Aaronson:dem` in Zotero and re-export. He asked
      specifically for "[Aaronson, Ch 9]"; the entry currently has no chapter,
      only a `lec9.html` URL.
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
- [ ] Do NOT cite him as a personal communication. He named a public source,
      and ICMJE says to avoid personal communications where one exists. If a
      personal-communication citation is ever wanted anyway, ICMJE requires
      "written permission and confirmation of accuracy from the source" -- the
      same rule the Abramsky provenance note already applies.

- [ ] The `\medskip` summary closing `sec:spacetime-open-problems` in
      `paper1/spacetime_from_non-computability.tex` enumerates the prospects by
      name and now under-counts: the two loops/renormalisability paragraphs
      spliced on 2026-09-11 are not mentioned. Which prospects to name there is
      an editorial call.
- [ ] TeX-style ``...'' quoting survives in 20 files across paper 1 (77
      instances), predating the move to `\enquote{}`. Converting is mechanical
      but touches most of the paper, so worth doing as one deliberate pass.

- [ ] The results ledger says delta_0 = 2/9 reproduces charged lepton masses
      to "<0.006%"; `paper1/masses_section_2026-06-08.tex` says the phase is
      "matched to five significant figures". These may be measuring different
      quantities, or one may be stale. The headline snippet now follows the
      section. Worth reconciling, and the ledger entry is labelled ESTABLISHED
      while the section calls delta = 2/9 "the one genuine gap", matched rather
      than derived, with op:koide-delta attached -- so the label may want
      revisiting too.

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
- [ ] Echo and verify the output of `sedenion_zero_divisor_scan_2026-08-31.py`.
- [ ] Newtonian limit computation for Paper 2 (`op:p2-newton`).
- [ ] Email Andrei Khrennikov, leading with the complementarity reframe and
      the Tsirelson-as-ramification correspondence.
- [ ] Label mapping for the four master-file section labels (`sec:hopf`,
      `sec:born`, `sec:fanout`, `sec:contextuality`) in the Jaynes appendix.
