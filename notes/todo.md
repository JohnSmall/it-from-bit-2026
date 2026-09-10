# To do

Actionable items with enough context to act on without reconstructing the
reasoning. Delete when done.

## Blocking a clean build

- [ ] **Re-export both Zotero collections.** `self-ref-2026-cited` holds 193
      items and `self-ref-2026-paper2-cited` holds 19, but `references.bib`
      and `references_paper2.bib` are still at 192 and 18. Both papers now
      cite `rubino2017indefinite`, which is in neither file, so a build gives
      an undefined citation until this is done.

## Zotero housekeeping

- [ ] **Empty the trash** (295 items). Everything worth recovering has been
      recovered; the four values the sweep still reports belong to records
      that now hold them correctly (`wigner_1967` for the Am. J. Phys. review,
      `repository`/`archiveID` for the Castagnoli preprint). The three trashed
      attachments whose parents are live are duplicate Mendeley
      `m-api-*.pdf` copies; every parent keeps its own PDF.
- [ ] Decide whether `attic_self-ref-2026.bib.superseded` and
      `attic_notes_old.tex.superseded` belong in `paper1/attic/`. Both were
      shared across the series or belonged to neither paper.

## Manuscript

- [ ] Place the seven fragments in `orphans/`. Some may be splice sources
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
