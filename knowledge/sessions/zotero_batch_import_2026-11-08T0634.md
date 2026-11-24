# Session note: importing the five 2026-11-07 reference batches through the Zotero connector

Date: 2026-11-08T0634. Session: Claude Code (Opus 5.5), housekeeping, working
for JS on `main`. Script: `scripts/zotero_batch_import_2026-11-08T0634.py`
(subcommands `check`, `import`, `verify`). Raw API responses were saved in the
session scratchpad, not in the repository.

## What was asked

Import the five batches of 2026-11-07 into `self-ref-2026-cited` (collection
key S8W5V4AL), with their entry keys pinned as citation keys, after a
duplicate check, the 9-key qutrit batch first as a pilot:
`bib/qutrit_hopf_refs_2026-11-07T1610.bib` (9),
`bib/b_anomaly_refs_2026-11-07T1910.bib` (11),
`bib/three_papers_lfu_refs_2026-11-07T2010.bib` (13),
`bib/confinement_flux_tube_refs_2026-11-07T1140.bib` (25),
`bib/lattice_causal_set_refs_2026-11-07T0710.bib` (29): 87 entries. Also a
read-only presence check on the older unticked batches in `notes/todo.md`. No
build, no commit, no hand edit of `paper1/references.bib`.

## Route

The September route (`POST /api/users/0/items` with `Zotero-API-Key`) was
closed: no key file exists and the key is minted per Zotero restart. The
connector route worked: `POST /connector/import?session=<id>` with the raw
`.bib` text as body (Content-Type `application/x-bibtex`) returned 201 and the
created items, and `POST /connector/updateSession` with
`{"sessionID": <id>, "target": "C10", "tags": ""}` returned 200 `{}` and moved
them into `self-ref-2026-cited` (connector target `C10`, from
`/connector/getSelectedCollection`). Better BibTeX's importer won the
translator choice and pinned every entry key: the returned item JSON carries
`"citationKey": "hopf1935abbildungen"` and so on, never a formula key. Session
ids are derived from the batch filename (`imp-` + 16 hex of SHA-1), so the
script has no randomness; it refuses to import if any remaining key already
resolves through BBT, which also stops a second run.

## Duplicate check first

All library items were paged before anything was written (Zotero 10.0.6,
`Total-Results: 3694`). Script output:

    library: 3694 items paged, 1541 regular items

Tests: equal DOI (also DOI lines in Extra and doi.org URLs), citation key in
the item JSON or resolvable by BBT, equal arXiv identifier, equal or
near-equal normalised title with year within one. 85 of 87 entries matched
nothing. Two did:

| key the batch wants | already in the library as | resolved by |
|---|---|---|
| `aldaguaschpenaranda2021anomalies` | `aldaAnomaliesMesonsDecays2021` (item QU3RUCYE; preprint, arXiv:2105.05095 = DOI 10.48550/arXiv.2105.05095; added 2026-11-07T16:16:33Z; in no collection) | NOT imported; left for JS |
| `bombellileemeyersorkin1987causalset` | `rd_sorkin_87` (item EHLVIBHA; "Space-time as a causal set", 1987, Phys Rev Lett; Mendeley-era item, no DOI, creators mangled into one name, in collection Q3U6TZB5 only) | NOT imported; left for JS |

Exact output lines:

    aldaguaschpenaranda2021anomalies              ARXIV 2105.05095 = item QU3RUCYE as aldaAnomaliesMesonsDecays2021
    bombellileemeyersorkin1987causalset           TITLE~ item EHLVIBHA as rd_sorkin_87 (1987)

The first is decisive (same arXiv identifier). The second is a title-and-year
match and was judged to be the same Letter. Neither existing key is cited in
any `.tex` or `.bib` in the repository, so by the September precedent both
should be re-pinned to the keys the batches use and added to
`self-ref-2026-cited`; that needs the write key, so it was not done. Neither
wanted key is cited in any `.tex` yet either, so nothing is undefined today.
For `rd_sorkin_87`, re-pinning should also fix the creators (Bombelli, Luca;
Lee, Joohan; Meyer, David; Sorkin, Rafael D.) and add DOI
10.1103/PhysRevLett.59.521, as in the batch. Deleting it and importing the
batch entry is the alternative.

## What was written

| batch | entries | created | skipped (duplicate) | failed | collection numItems |
|---|---|---|---|---|---|
| qutrit_hopf (pilot) | 9 | 9 | 0 | 0 | 343 -> 352 |
| b_anomaly | 11 | 10 | 1 | 0 | 352 -> 363 |
| three_papers_lfu | 13 | 13 | 0 | 0 | 363 -> 377 |
| confinement_flux_tube | 25 | 25 | 0 | 0 | 377 -> 402 |
| lattice_causal_set | 29 | 28 | 1 | 0 | 402 -> 430 |
| total | 87 | 85 | 2 | 0 | 343 -> 430 |

The collection grew by 87, not 85: the b_anomaly and three_papers imports
each also created one standalone note (items UL9WDQ65 and 7YTLZCED, both in
`self-ref-2026-cited`) whose whole text is

    Import errors found: <ul><li>unhandled macro \mathcal</li></ul>

It comes from the `$\mathcal{R}(D^{*})$` title of `lhcb2023ratiosbranching`
and the `$\mathcal{B}(...)$` title of `lhcb2018ratiojpsi`. BBT does not export
standalone notes, so they do not reach `references.bib`; JS may delete them.
The bodies' `note` fields became child notes, as `bib/README.md` says.

Import output, exactly:

    session imp-efc9b9132a19f636; selected in GUI: 'My Library' id=None; target C10; collection numItems before 343
    import: HTTP 201
    import: 9 items returned
    updateSession: HTTP 200 '{}'
    collection numItems after 352
    session imp-2715052617655eab; selected in GUI: 'self-ref-2026-cited' id=10; target C10; collection numItems before 352
    skipping aldaguaschpenaranda2021anomalies (duplicate, left for the maintainer)
    import: HTTP 201
    import: 11 items returned
    updateSession: HTTP 200 '{}'
    collection numItems after 363
    session imp-c0dec2d9ab0a14b7; selected in GUI: 'self-ref-2026-cited' id=10; target C10; collection numItems before 363
    import: HTTP 201
    import: 14 items returned
    updateSession: HTTP 200 '{}'
    collection numItems after 377
    session imp-afeedf7238d1d949; selected in GUI: 'self-ref-2026-cited' id=10; target C10; collection numItems before 377
    import: HTTP 201
    import: 25 items returned
    updateSession: HTTP 200 '{}'
    collection numItems after 402
    session imp-1b3708beb0a61c35; selected in GUI: 'self-ref-2026-cited' id=10; target C10; collection numItems before 402
    skipping bombellileemeyersorkin1987causalset (duplicate, left for the maintainer)
    import: HTTP 201
    import: 28 items returned
    updateSession: HTTP 200 '{}'
    collection numItems after 430

(The "11 items returned" and "14 items returned" include the two error
notes.) The first updateSession also moved the GUI selection from My Library
to `self-ref-2026-cited`.

## Verification

Every one of the 85 imported keys resolves through
`/better-bibtex/export/item?citationKeys=<key>&translator=biblatex` under
exactly its own key, and every one is a top-level item of S8W5V4AL. Summary
lines of `verify`:

    9 entries, 9 resolve, 0 need attention
    10 entries, 10 resolve, 5 need attention
    13 entries, 13 resolve, 11 need attention
    25 entries, 25 resolve, 3 need attention
    28 entries, 28 resolve, 2 need attention

Key, DOI and collection were right for all 85; the "need attention" flags are
title text and name formatting, which were then read entry by entry against
the batch. What was found:

- Names: four flags are only BBT's extended name format
  (`family=Forcrand, given=Philippe, prefix=de, useprefix=true`;
  `given-i={{Sw}}` for HFLAV's Banerjee; `given-i=A{{Yu}}` for Kitaev). Same
  people, correct.
- Brace-protected words survived everywhere: `{{Bloch}}`, `{{Standard
  Model}}`, `{{Belle II}}`, `{{SU}}(2)`, `{{CP}}`. `{Monte Carlo}` came back as
  `Monte {{Carlo}}`, and `{{Yang--Mills}}` and `{{Einstein--Podolsky--Rosen}}`
  as `{{Yang}}–{{Mills}}` and so on: capitals kept, the `--` became a
  literal en dash, which the existing export already contains seven of.
- Maths in titles did not survive as LaTeX. BBT's importer turned it into
  Unicode and sub/superscript markup:
  `$B^{0} \to K^{*0} \mu^{+} \mu^{-}$` exports as
  `{{B}}⁰→{{K}}{\textsuperscript{*0}}𝜇⁺𝜇⁻`, and `$\alpha_s$` as `{{αₛ}}`. Two
  kinds of loss are real. `\mathcal` was dropped (`lhcb2023ratiosbranching`,
  `lhcb2018ratiojpsi`: R and B come out upright). The bar was dropped and the
  meaning changed: `belleii2024evidencekpnunu` reads `B⁺→K⁺νν` for
  `K^+ \nu \bar\nu`, and `isidoripolonskytinari2025charm` and
  `isidoripolonskytinari2025improved` read `ℓℓ` for `\bar\ell \ell`.
- **A probable build problem, untested because no build was run.** 17
  exported entries now carry characters such as `⁺ ⁻ ⁰ → ℓ 𝜇 ν τ ψ ϵ αₛ`
  (eleven from three_papers_lfu; `lhcb2023testlepton`,
  `lhcb2023measurementlepton`, `lhcb2023ratiosbranching` and
  `hflav2023averages` from b_anomaly; `sommer1994scalesetting` and
  `wilsonkogut1974renormalization`, with `{{ϵ}}`, from lattice_causal_set). Paper 1 builds with pdflatex
  and `\usepackage[utf8]{inputenc}`, where these are not set up, so the
  first citation of any of them is likely to stop the build with "Unicode
  character ... not set up for use with LaTeX". None of the 17 is cited in
  any `.tex` today. The fix is JS's: per `bib/README.md`, put the LaTeX title
  in each item's Extra as `tex.title = ...` (equals sign), or set the
  auto-export to ASCII output.
- `hopf1935abbildungen`: the German title was sentence-cased on import
  (`Über die abbildungen von sphären auf sphäre niedrigerer dimension` in
  Zotero) and BBT's English title-casing gives `Über Die Abbildungen von
  Sphären Auf Sphäre Niedrigerer Dimension` on export. Setting the item's
  Language to `de` should stop the title-casing; the nouns also need their
  capitals restored in Zotero. The batch did not brace them, which is the
  root cause.

### references.bib

BBT has an auto-export on the collection: `paper1/references.bib` rewrote
itself during the imports. Before and after (mtime, size; entry count; md5):

    2026-11-06 16:34:15.813794120 +0000 124824
    343
    6f50282e5ded5e2723dbdd3ace911646  paper1/references.bib

    2026-11-08 06:38:57.757114799 +0000 153972
    428
    687dd7165fac28691f3c9e425a74acbf  paper1/references.bib

Against `HEAD`: no key dropped, the 85 imported keys added, nothing else
added; `git diff --stat` reports `947 insertions(+)`, no deletions. The only
wanted keys absent are the two duplicates above. The file is modified in the
working tree, not staged or committed.

## Older batches: read-only presence check

Not imported, at JS's instruction. Output of `check` on the eight older
batches:

- `szangolies_sedenion_refs_2026-08-25T0633.bib` (4),
  `gresnigt_cl10_ref_2026-08-25T0700.bib` (1),
  `cp_context_core_refs_2026-09-12.bib` (2),
  `extended_wigners_friend_refs_2026-08-30.bib` (13),
  `ewf_splice_supplementary_refs_2026-08-30.bib` (1): **all 21 keys already
  in the library under exactly the wanted keys, and all 21 in
  `self-ref-2026-cited`**. These todo items (around lines 514 and 540) are
  done in effect and can be ticked by JS. One existing duplicate seen in
  passing: `jarlskog1985` (item 9ZCZ4N45) and `jarlskog1985commutator` (item
  HTXMS396) share a DOI and are both in the collection.
- `ctc_darwinism_refs_2026-10-16T1000.bib` (18): 17 missing. One already
  present by DOI: `aaronsonwatrous2009ctc` = `Aaronson2009` (item E8XU8KQS),
  not in `self-ref-2026-cited`.
- `complex_temperature_coherence_refs_2026-10-16T1040.bib` (7): all 7
  missing.
- `kirkwood_dirac_weak_value_refs_2026-10-16T2210.bib` (20): 17 missing.
  Present: `dirac1945analogy` = `dirac_1945` (item 5HLF68T5, by DOI),
  `dresseljordan2012imaginaryweakvalue` =
  `dresselSignificanceImaginaryPart2011` (item TBWMAQHI, by DOI),
  `aharonovbergmannlebowitz1964timesymmetry` = `Aharonov_64` (item LTJ7IYBI,
  title and year, for judgement). None of the three is in
  `self-ref-2026-cited`.

So of the 45 keys in the three October batches, 41 are missing and 4 exist
under other keys and would need re-pinning, not importing.

## Not done

- Re-pinning `aldaAnomaliesMesonsDecays2021` and `rd_sorkin_87` (or replacing
  them) and adding them to the collection: needs the write key.
- Deleting the two "Import errors found" notes UL9WDQ65 and 7YTLZCED.
- The Unicode-in-titles and Hopf-casing fixes above.
- The build: not run (JS co-ordinates builds). No commit, nothing staged.
- No ledger entries and no status labels: nothing here is a claim.

## Moved out of self-ref-2026-cited, 2026-11-08T0913

**Why.** `self-ref-2026-cited` is the collection BBT exports to
`paper1/references.bib`, and of the 85 items imported above only
`kimura2003bloch` is cited in Paper 1
(`paper1/entanglement_classes_and_gauge_groups_2026-06-08.tex`, line 382). A
grep of every `.tex` under `paper1/` and `paper2/` for the 85 keys finds that
one key and no other. At JS's instruction the other 84 left the exported
collection and stayed in the library, each filed in a top-level collection
named after its batch's `.bib` stem, as the library already does (e.g.
`koide_attribution_refs_2026-09-11T2011`).

**Route.** Local API writes, with `Zotero-Server-ID` and `Zotero-API-Key`
read from files passed as arguments (the key is not recorded here or in the
repository). Script: `scripts/zotero_batch_collections_2026-11-08T0913.py`.
It creates a collection only if no top-level collection of that name exists,
GETs each item fresh, and PATCHes `collections` alone with
`If-Unmodified-Since-Version`. An item that already has the wanted
collections is left alone, so running it twice changes nothing. The qutrit
batch went first as a pilot, was verified, and the full run then reported it
`unchanged` and created no second collection.

**Created** (none of the five names existed beforehand):

| collection | key |
|---|---|
| `qutrit_hopf_refs_2026-11-07T1610` | KFWILU3Z |
| `b_anomaly_refs_2026-11-07T1910` | TWV82PR9 |
| `three_papers_lfu_refs_2026-11-07T2010` | Y2RJGAHN |
| `confinement_flux_tube_refs_2026-11-07T1140` | XQ5EYK5G |
| `lattice_causal_set_refs_2026-11-07T0710` | J9UH6P7H |

**Moved.** Pilot output (exact):

    collection qutrit_hopf_refs_2026-11-07T1610: created, key KFWILU3Z
      acindurtgisinlatorre2002quantum               NJ3TNNBS v6163 ['S8W5V4AL'] -> ['KFWILU3Z']
      adams1962vectorfields                         WIMH6NT9 v6157 ['S8W5V4AL'] -> ['KFWILU3Z']
      collinsgisinlindenmassarpopescu2002bell       T9MRZTKY v6162 ['S8W5V4AL'] -> ['KFWILU3Z']
      eltschkahubermorellisiewert2021shape          U28H77UL v6161 ['S8W5V4AL'] -> ['KFWILU3Z']
      goyalsimonsinghsimon2016geometry              FCGRGHQS v6160 ['S8W5V4AL'] -> ['KFWILU3Z']
      hopf1935abbildungen                           3W67YNWX v6156 ['S8W5V4AL'] -> ['KFWILU3Z']
      kimura2003bloch                               RCW7NE3V v6158 ['S8W5V4AL'] -> ['S8W5V4AL', 'KFWILU3Z']
      kimurakossakowski2005bloch                    3MUTZ7QQ v6159 ['S8W5V4AL'] -> ['KFWILU3Z']
      nurmiev2000orbits                             HUUEMZ3T v6164 ['S8W5V4AL'] -> ['KFWILU3Z']
    qutrit_hopf_refs_2026-11-07T1610: 9 items, {'moved': 9, 'unchanged': 0, 'skipped_412': 0, 'failed': 0}

Full run, summary lines (exact):

    collection qutrit_hopf_refs_2026-11-07T1610: exists, key KFWILU3Z
    collection b_anomaly_refs_2026-11-07T1910: created, key TWV82PR9
    collection three_papers_lfu_refs_2026-11-07T2010: created, key Y2RJGAHN
    collection confinement_flux_tube_refs_2026-11-07T1140: created, key XQ5EYK5G
    collection lattice_causal_set_refs_2026-11-07T0710: created, key J9UH6P7H
    qutrit_hopf_refs_2026-11-07T1610: 9 items, {'moved': 0, 'unchanged': 9, 'skipped_412': 0, 'failed': 0}
    b_anomaly_refs_2026-11-07T1910: 10 items, {'moved': 10, 'unchanged': 0, 'skipped_412': 0, 'failed': 0}
    three_papers_lfu_refs_2026-11-07T2010: 13 items, {'moved': 13, 'unchanged': 0, 'skipped_412': 0, 'failed': 0}
    confinement_flux_tube_refs_2026-11-07T1140: 25 items, {'moved': 25, 'unchanged': 0, 'skipped_412': 0, 'failed': 0}
    lattice_causal_set_refs_2026-11-07T0710: 28 items, {'moved': 28, 'unchanged': 0, 'skipped_412': 0, 'failed': 0}

So 9 + 10 + 13 + 25 + 28 = 85 items were refiled, with no 412 and no failure:
84 left `self-ref-2026-cited`, and `kimura2003bloch` is now in both that
collection and its batch collection.

**Verification** (exact):

    S8W5V4AL self-ref-2026-cited numItems 346
    KFWILU3Z qutrit_hopf_refs_2026-11-07T1610 numItems 9
    TWV82PR9 b_anomaly_refs_2026-11-07T1910 numItems 10
    Y2RJGAHN three_papers_lfu_refs_2026-11-07T2010 numItems 13
    XQ5EYK5G confinement_flux_tube_refs_2026-11-07T1140 numItems 25
    J9UH6P7H lattice_causal_set_refs_2026-11-07T0710 numItems 28
    duplicate collection names: []
    kimura2003bloch ['S8W5V4AL', 'KFWILU3Z']
    note UL9WDQ65 ['S8W5V4AL']
    note 7YTLZCED ['S8W5V4AL']
    BBT resolves 85 of 85 keys

`self-ref-2026-cited` holds 346 = 343 old items + `kimura2003bloch` + the two
BBT error notes UL9WDQ65 and 7YTLZCED, which are still there.

**references.bib.** The auto-export fired by itself. Exact output:

    2026-11-08 09:14:57.390889797 +0000 125091
    344
     paper1/references.bib | 11 +++++++++++
     1 file changed, 11 insertions(+)

The diff against `HEAD` is exactly one added entry, `kimura2003bloch`, and no
deletions. It is modified in the working tree, not staged.

**Still JS's.**
- Deleting the two error notes UL9WDQ65 and 7YTLZCED from
  `self-ref-2026-cited`.
- The two re-pins (`aldaAnomaliesMesonsDecays2021` to
  `aldaguaschpenaranda2021anomalies`, and `rd_sorkin_87` to
  `bombellileemeyersorkin1987causalset`), with the creator and DOI fix on the
  latter. Both items are untouched and are in neither the cited collection
  nor a batch collection.
- The Unicode-in-titles fixes before any of the 17 maths-title entries is
  cited, and the Hopf 1935 casing.
- The build and the commit.

**For the maintainer: `bib/README.md` is out of date on the write key.** Its
last paragraph says the key "changes when Zotero restarts and has to be
fetched again from the settings panel". On Zotero 10 the key comes from
`POST /api/local/authorize` with a JSON body `{"appName": ...}`, which puts up
an Allow / Always Allow / Deny dialog in Zotero. A key granted with "Always
Allow" is kept in the profile's `localAPIKeys.json` and survives restarts; ten
such keys from September are there. The key used today was one of those,
which is why it still worked. Proposed correction only; `bib/README.md` was
not edited.
