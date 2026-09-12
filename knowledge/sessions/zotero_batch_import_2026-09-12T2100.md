# Session note: importing the seven reference batches through the Zotero API

Date: 2026-09-12T2100. Session: Claude Code (Opus 5), housekeeping.

## What was asked

Import the batches the newly added sections and appendices need, using the
local Zotero API rather than the GUI, and check that none creates a duplicate.

## Duplicate check first

Every entry in the seven batches was parsed and tested against all 3,353
library items before anything was written. Three tests: equal DOI (decisive),
citation key already present (decisive), and equal normalised title with years
within one (reported for judgement). Of 48 entries, **41 were new and seven were
already in the library under a different key**:

| key the paper wants | already in the library as | resolved by |
|---|---|---|
| `verstraete2002four` | `verstraeteFourQubitsCan2002` | re-pinned |
| `proietti2019experimental` | `Proietti2019` | re-pinned |
| `wisemancavalcantirieffel2023thoughtful` | `wisemanThoughtfulLocalFriendliness2022` | re-pinned |
| `schmidyingleifer2023sixewf` | `schmidReviewAnalysisSix2023` | re-pinned |
| `moreno1998zerodivisors` | `morenoZeroDivisorsCayleyDickson1997` | re-pinned |
| `pinillaluthra2009hopf` | `Pinilla_2009` | re-pinned |
| `gunaydin1973quark` | `gunaydingursey1974quark` | citation re-pointed |

Six were re-pinned rather than imported, because their existing keys were cited
nowhere in either paper and appeared in no exported bibliography -- so moving
the key to the one the text uses costs nothing and creates no duplicate. The
seventh could not be treated that way: `gunaydingursey1974quark` is already
cited twice and already in `references.bib`, so the appendix moved instead
(`scripts/patch_gunaydin_citekey_2026-09-12T2100.py`). Its DOI,
10.1063/1.1666240, is what matched the two.

Note that the existing key names 1974 while the item's date field says 1973,
which the journal reference supports. The key is only a label and was left
alone; renaming it would have been a third way to break the standing citations.

## A capability worth recording

`citationKey` is writable through the local API, and Better BibTeX honours it.
A `PATCH` of that field alone returns 204, the field reads back changed, and
after a short reindex BBT's own export endpoint resolves the new key and no
longer resolves the old one. This was tested on one item before the other five
were touched.

That matters beyond this import: it means references can be created
programmatically with their intended keys, without the `.bib` import step and
without pinning by hand. The `.bib` route remains the documented one in
`bib/README.md` because it is reproducible from a file in the repository; the
API route is the faster one when a batch already exists.

## What was written

- Six existing items re-pinned to the keys the papers use.
- The same six added to the `self-ref-2026-cited` collection, which none of
  them was in -- an item outside that collection is not exported, so the
  re-pinning alone would not have been enough.
- **41 new items created in one POST: 41 success, 0 unchanged, 0 failed**, each
  with its citation key set and its collection assigned.

## Verification

All 47 intended keys resolve through BBT's export endpoint under exactly the
keys the papers cite. Resolving the input tree from `main.tex` afterwards: 251
keys cited by live files, 205 in the current export, 46 missing -- and all 46
are now in Zotero. Nothing cited is unsupplied.

## Not done

The export itself, and the build. Both are JS's. After a re-export of
`self-ref-2026-cited` the only outstanding structural item should be the
undefined label `sec:flavour-conservation`.
