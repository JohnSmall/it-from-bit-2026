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
- [ ] Import `bib/koide_attribution_refs_2026-09-11T2011.bib` into Zotero and
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

- [ ] Re-export `self-ref-2026-cited` to pick up `chapter = {9}` on
      `Aaronson:dem`. Written to Zotero 2026-09-12 via the local API as
      `tex.chapter: 9` in the item's Extra field (Zotero has no chapter field
      for a bookSection), and confirmed in BBT's own export. The change is in
      the library but not yet in `paper1/references.bib`.
- [ ] Decide how chapter 9 should actually be cited. `Aaronson:dem` is a
      Zotero bookSection, so it exports as `@incollection` with the book's
      title in `title` and no `booktitle`; adding `chapter = {9}` leaves an
      entry that is bibliographically odd, a chapter number attached to what
      biblatex reads as a section title. The idiomatic alternative is to make
      it a plain `@book` and cite `\autocite[ch.~9]{Aaronson:dem}`, which is
      also closer to the "[Aaronson, Ch 9]" he asked for. JS's call.
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
