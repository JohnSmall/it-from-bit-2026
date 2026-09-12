# Session note: the Zotero ISBN sweep

Date: 2026-09-12T1400. Session: Claude Code (Opus 5), housekeeping.

## What this was

Two biber warnings on the Laraudogoitia entries turned out to be the visible
edge of a Mendeley-import artefact. Mendeley wrote an `ISBN:` line into the
Extra field of items that have no business carrying one, Better BibTeX reads
`ISBN:` in Extra as a field injection, and so the export grew an `isbn` field
on journal articles. Where the value was not an ISBN at all, biber warned.

A full scan of the library (3,353 items) found **47 items** with an `ISBN:`
line in Extra, not the nineteen an earlier partial query had suggested.

## The rule

A line was removed only if its value is demonstrably not an ISBN. A valid ISBN
was never removed: it is real metadata, and its presence on a journalArticle
means the *item type* is wrong, which is a different fix.

Validation is stricter than a check digit alone, because a check digit on its
own is not enough. Several arXiv identifiers pass it by coincidence once
punctuation is stripped --- `1706.03762v7` becomes `1706037627`, ten digits,
and validates. So a value must first *look* like an ISBN (digits, hyphens and
spaces only, optional trailing X, no full stops and no `v`), and an ISBN-13
must carry an assigned EAN prefix, 978 or 979. That is what rejects
`1077300570792` and `1077300692968`, which validate but cannot be ISBNs.

Other Extra lines were preserved verbatim. Items carrying both an `arXiv:` and
an `ISBN:` line kept the former: `vaswaniAttentionAllYou2017`, `Svozil2005` and
`cerfComplexvaluedWignerEntropy2023` were checked after the sweep and still
export `eprint` with no `isbn`.

## Result

**29 lines removed across 29 items, 18 valid ISBNs kept, 0 failures.** Every
PATCH was guarded by `If-Unmodified-Since-Version`; none was skipped. A
re-scan afterwards reports nothing left to delete.

By class: 21 were ISSNs in the ISBN slot (the `0924-6495` of *Minds and
Machines* accounts for six of them on its own), 6 were arXiv identifiers, and
2 were unrecognised digit strings.

## What was removed, and from where

Restore by putting the value back as an `ISBN: <value>` line in that item's
Extra field.

| citation key | Zotero key | class | removed value |
|---|---|---|---|


## Valid ISBNs kept (18)

`Brukner2009`, `Carlip2009c`, `Carnielli2016`, `Hadley2007`, `Jain2008`, `Khrennikov2012`, `Michel2008c`, `Nakamoto2008`, `Tobergte2013`, `Wood2014a`, `acaciodebarrosMeasuringObservableQuantum2016`, `jacobsConvexityDualityEffects2010`, `krasnovOctonionsComplexStructures2025`, `nowakowskiQuantumEntanglementTime2017`, `pushaEfficiencyAnalysisHydraulic2013`, `rovelliUnfinishedRevolution2006`, `wheelerQuantumTheoryMeasurement`, `wiltschePhenomenologicalApproachesPhysics2020`

Two of these want a look, and neither was touched. `Brukner2009` is a book
chapter filed as a journalArticle --- its `publicationTitle` is *Deep Beauty:
Understanding the Quantum World Through Mathematical Innovation*, its DOI is
`10.1017/CBO9780511976971.011`, and the ISBN is that Cambridge volume's, so the
ISBN is right and the type is wrong. And `Tobergte2013` and `Wood2014a` share
one ISBN, `9788578110796`, which is valid but is a known Mendeley default
rather than either paper's book.

## Effect on the papers

None yet. Of the 29 swept items, **none is cited in either paper**, so
`references.bib` is unchanged by the sweep. It is preventive: those entries
would have exported a bad `isbn` as and when they were cited.

The two entries that *were* visible are separate and already fixed in Zotero:
`Laraudogoitia1998` by JS (the ISSN moved to its own field) and
`Laraudogoitia_1997` earlier today (Extra cleared, ISSN corrected to the
hyphenated `0007-0882`). `paper1/references.bib` in the working tree still
pre-dates the second of those, so one more re-export clears both biber
warnings.

After that re-export, the paper's remaining 12 `isbn` fields sit on
`@book`, `@incollection` and `@inproceedings` entries, where they belong ---
with `Brukner2009` the single `@article` exception noted above.

## Files

- `scripts/zotero_isbn_sweep_scan_2026-09-12T1400.py` --- scans and classifies,
  writing the plan with each item's Extra field before the edit
- `scripts/zotero_isbn_sweep_apply_2026-09-12T1400.py` --- applies it

## Not done

No build, no re-export: both are JS's to run.
