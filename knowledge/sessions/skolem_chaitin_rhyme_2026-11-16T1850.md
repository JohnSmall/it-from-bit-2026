# Session note: Skolem's paradox and Chaitin's added axioms, recorded as a rhyme

Date: 2026-11-16T1850. Session: Claude Code (Fable 5.2), thinking session,
working for JS on `main`. No numerical script: nothing here is computed.
Patch: `scripts/patch_skolem_chaitin_rhyme_2026-11-16T1850.py`, applied.
Batch: `bib/skolem_rhyme_refs_2026-11-16T1850.bib` (5 keys). No build, no
commit.

## What was asked

JS asked what I knew of Skolem's paradox, then observed that it rhymes with
Chaitin's and Penrose's point that a proposition unprovable from given axioms
becomes provable when information is added as new axioms. His ruling: add it
to the paper as an interesting rhyme for mathematicians and logicians to work
on, without committing to any reading of Skolem's work; it becomes relevant
in Paper 2, where inside and outside, and spatial distance as the information
that must be added to make events causally connected, become very important.

## What I think, in short

1. The bridge is Goedel's completeness theorem: a sentence is unprovable from
   T exactly when some model of T makes it false. Adding an axiom and
   discarding models are one act. This is the precise sense in which an axiom
   is information.
2. The closest contact: a model of T + not-Con(T) contains an object it takes
   for a proof of a contradiction, which from outside is a nonstandard number
   and no finite proof. A countable model of set theory contains a set it
   takes to be uncountable, which from outside is countable. Same shape: the
   inside is right by its own lights, the correction comes from a vantage
   that sees more, and that vantage has the same defect. On the proof side
   the tower is Turing's and Feferman's progressions; on the model side,
   forcing can make any set countable in a larger universe.
3. Where it breaks: incompleteness is a shortage of axioms and moves when
   axioms are added; Skolem relativity is a weakness of first-order language
   and does not move, since every consistent extension has countable models.
   So a distance counted in added bits does not transfer to the continuum
   question without its own derivation.
4. Cautions: the reading of Chaitin's theorem as measuring the information in
   a theory is disputed (Raatikainen 1998; Con(T) is short and strong).
   Penrose's step needs soundness of T to be known first.

## What was patched

One paragraph at the end of `sec:measuring-non-computability` in
`paper1/what_is_a_quantum_state.tex`, between `% BEGIN skolem-chaitin-rhyme`
and `% END` markers, in the first person of that subsection. It states the
theorem, the likeness (points 1 and 2), the difference (point 3), the
Raatikainen caution, that the paper takes no side on what Skolem's result
means, that only the theorem is used (in `sec:continuity`), and the pointer
to Paper 2 and `sec:comp-distance`. Penrose is not named in the paragraph:
his argument adds a claim about minds that the rhyme does not need.

Found while placing it: `sec:continuity` (the closedness paragraph, "Any
collection of first-order principles ... that has an infinite model has a
countable one") already uses the Loewenheim--Skolem theorem without naming or
citing it. The new paragraph points there. A citation at that sentence is
suggested, not applied.

## Proposed ledger entry (for JS)

- **RHYME** Skolem relativity and Chaitin's added axioms: both are failures
  of a first-order description to fix its intended interpretation from
  inside, repaired only from an outside with the same defect; bridged by the
  completeness theorem (STRUCTURAL, imported). They differ in that added
  axioms move provability and do not move Skolem's countable models. No
  reading of Skolem's philosophical conclusions is adopted. Paper 1
  `sec:measuring-non-computability`; carried to Paper 2.

## Proposed open problem for Paper 2 (wording for JS, no PASS/FAIL yet)

Whether "distance as information that must be added" can be given a
model-theoretic form: a tower of inside/outside presentations in which the
bits added at each step are the bits that select among models, with the
difference in point 3 either respected or shown not to bite.

## Citations

VERIFY-SUPPORT: skolem1922remarks (not read; quoted at second hand from
Bays), turing1939systems and feferman1962transfinite (titles and standard),
raatikainen1998interpreting (from memory of the abstract). Read:
bays2025skolem. Three DOIs verified against Crossref. All five keys are
undefined in the build until imported into `self-ref-2026-cited` and
re-exported.

## Not done

No build. No commit. No Zotero import. No ledger entry written.

## Addendum, 2026-11-16 evening: what Svozil's book says

JS remarked that Svozil's *Physical (A)Causality* (`svozil_k_2018`) does not
relate this to the inside/outside issue. Checked against the text of JS's
local PDF (pdftotext, searched for Skolem, Loewenheim, non-standard,
countable model, model theory, Feferman, Putnam).

- The book names Loewenheim--Skolem once, Appendix A.5 "Abundance of True Yet
  Unprovable Statements", pp. 174--175, index entry "Loewenheim-Skolem, 174".
  After Rice's theorem: "As Yanofsky observes this bears some similarity to
  the downward Loewenheim-Skolem", followed by a quotation from Yanofsky,
  *The Outer Limits of Reason* (MIT Press, 2013), footnote 20, p. 375.
- So the likeness between unprovability and Skolem is noted there in one
  sentence, at second hand. It is not connected to the intrinsic/extrinsic
  observer distinction, which the book treats at length (the words occur 42
  and 21 times). JS's remark holds for the inside/outside relation.
- No mention of non-standard models, countable models, model theory, or the
  Turing--Feferman progressions.

Proposed, not applied: add `\autocite[174--175]{svozil_k_2018}` to the patched
paragraph as the antecedent for the likeness, with a clause that the relation
to inside and outside is not drawn there. Yanofsky 2013 is not read and not
in a batch.

Fence on "not well explored": the logic side is heavily explored
(non-absoluteness, forcing, the multiverse view, Putnam's argument). What is
thin is the link to physics and to observers. From memory, Benioff wrote on
models of ZF as carriers for the mathematics of physics in 1976 (VERIFY-CITE,
not checked).

## Addendum, 2026-11-21: antecedent cited

JS ruled: cite as Yanofsky, as quoted by Svozil. Applied by
`scripts/patch_skolem_yanofsky_antecedent_2026-11-21T0730.py`: one sentence
after "Set beside Chaitin's observation the two look alike.", citing
`\autocite[174--175]{svozil_k_2018}` (key already in the library; passage
read). Yanofsky is named in the text only and has no key; his book is not
read. No build, no commit.

## Addendum, 2026-11-21 (second): tied to Rice's theorem

JS ruled: tie the antecedent to Rice's theorem. Applied by
`scripts/patch_skolem_rice_tie_2026-11-21T0732.py`, which replaces the sentence added
earlier today. The sentence now says the similarity Yanofsky observes is
between Rice's theorem and the downward theorem, which is where Svozil places
it. No new key. No build, no commit.

## Addendum, 2026-11-21 (third): the five keys imported into Zotero

At JS's instruction, `bib/skolem_rhyme_refs_2026-11-16T1850.bib` was imported
with `scripts/zotero_batch_import_2026-11-08T0634.py` (check, import, verify).
Check: 0 of 5 matched any of 1626 regular items. Import: HTTP 201, 5 items,
moved into self-ref-2026-cited, which went from 346 to 351. Verify: 5 of 5
keys resolve in Better BibTeX and are in the collection. The verifier flagged
`raatikainen1998interpreting` for the braced word "Chaitin's"; the export has
`{{Chaitin}}'s`, so the capital is protected and the flag is a false alarm.
Better BibTeX re-exported `paper1/references.bib` within a minute: 349
entries, 67 lines added, none removed, all five keys present. The note field
of `bays2025skolem` (first published 2009) is not in the export. No build, no
commit.
