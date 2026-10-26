# Session record: continuity review appendix

Work begun 18 October and completed 19 October 2026. Filename time is in
Europe/London. Prepared for John Small, maintainer. Scientific status labels
in the appendix are proposals for his review; no ledger was amended.

## Request and scope

John asked to put the ten attempted derivations in a LaTeX appendix, leaving
a short summary, the CANDIDATE insight and an internal reference for the main
text. The requested appendix is now
[appendix_continuity_self_reference_2026-10-18T2119.tex](../../paper1/appendices/appendix_continuity_self_reference_2026-10-18T2119.tex).
It adapts the earlier
[discussion draft](continuity_from_self_reference_open_problem_2026-10-18T1811.md).

The appendix contains ten route reviews, the proposed missing physical
insight, an operational OPEN formulation, and three conditional group
arguments. The OPEN formulation sharpens the existing
`op:limit-realisability` rather than creating a duplicate numbered problem.
Its main reference label is `app:continuity-self-reference`.

The header supplies this inclusion line for the existing appendices environment:

```tex
\input{appendices/appendix_continuity_self_reference_2026-10-18T2119}
```

It also supplies a commented, short suggested main-text summary and
CANDIDATE paragraph using
`Appendix~\ref{app:continuity-self-reference}`.
The production main file and continuity section were not edited. Including
the appendix and replacing the main discussion are the later integration
step; this task produced and checked the requested appendix source.

## Files created

- The appendix linked above.
- [Initial patch script](../../scripts/patch_continuity_review_appendix_2026-10-18T2119.py).
- [Line-break patch script](../../scripts/patch_continuity_appendix_linebreaks_2026-10-18T2130.py).
- This session record.

Both scripts assert unique anchors, retain backups, add an EDITED header
and refuse a repeated application. For the new file, the first script
backs up its initial BEGIN/END scaffold before inserting the appendix.
The second preserves the complete first version in a separately dated
backup. The first script also creates a temporary manuscript wrapper under
`/tmp/continuity_appendix_2026-10-18T2119/` for validation.

There were many pre-existing tracked and untracked changes, including
changes to the generated bibliography. Those files were preserved. No
generated bibliography, Zotero library, ledger or publication was edited.
No commit was made.

## Patch executions

Command, from the repository root:

```sh
python3 scripts/patch_continuity_review_appendix_2026-10-18T2119.py
```

Exact stdout, exit status 0:

```text
created paper1/appendices/appendix_continuity_self_reference_2026-10-18T2119.tex
backup (initial scaffold): paper1/appendices/appendix_continuity_self_reference_2026-10-18T2119.tex.bak
created /tmp/continuity_appendix_2026-10-18T2119/continuity_check.tex
backup (initial scaffold): /tmp/continuity_appendix_2026-10-18T2119/continuity_check.tex.bak
Route subsections: 10; appendix labels: 24; collisions: 0
Pending bibliography keys: backens2014zx, bennett2003notes, chiribella2010purification, chiribella2011informational, simon2001nosignaling
Production main.tex and generated bibliography: unchanged
PATCH: PASS
```

Repeating that command tested the refusal guard. Stdout was empty; exit
status was 1. Exact stderr:

```text
REFUSING: target or backup already exists: /home/john/Documents/tex/self-ref-2026/paper1/appendices/appendix_continuity_self_reference_2026-10-18T2119.tex
```

The first successful manuscript build reported three small overfull
paragraphs within the appendix. Their prose was rephrased through a second
patch; the mathematics and labels were unchanged.

```sh
python3 scripts/patch_continuity_appendix_linebreaks_2026-10-18T2130.py
```

Exact stdout, exit status 0:

```text
patched paper1/appendices/appendix_continuity_self_reference_2026-10-18T2119.tex
backup: paper1/appendices/appendix_continuity_self_reference_2026-10-18T2119.tex.2026-10-18T2130.bak
Rephrased 3 overfull paragraphs; mathematical claims and labels unchanged
PATCH: PASS
```

The final three-paragraph diff was displayed for review. The complete new
appendix diff had also been displayed during drafting.

## Compilation and review

No competing latexmk process was found before the build. The temporary
wrapper uses the production preamble and inputs and adds the appendix
immediately before the existing end of the appendices environment.
All build artefacts are under the temporary output directory.

Final command, run from `paper1/`:

```sh
latexmk -r ../.latexmkrc -cd- -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/continuity_appendix_2026-10-18T2119/build /tmp/continuity_appendix_2026-10-18T2119/continuity_check.tex > /tmp/continuity_appendix_2026-10-18T2119/build_final.stdout 2> /tmp/continuity_appendix_2026-10-18T2119/build_final.stderr
```

The command completed with exit status 0 and produced a 204-page PDF. The
appendix is Appendix M, occupying pages 182--187 in that temporary build.
All 24 new labels resolve, including its references to the existing OPEN
problem and continuity section. The final log contains no overfull boxes
within the new appendix.

Exact final latexmk summary from stdout:

```text
Latexmk: Summary of warnings from last run of *latex:
  Latex failed to resolve 2 reference(s)
  Latex failed to resolve 7 citation(s)
Latexmk: All targets (/tmp/continuity_appendix_2026-10-18T2119/build/continuity_check.pdf) are up-to-date
```

The seven citation occurrences correspond to five distinct pending keys:
`backens2014zx`, `bennett2003notes`, `simon2001nosignaling`,
`chiribella2010purification` and `chiribella2011informational`.
They already have entries in the
[reference batch](../../bib/continuity_open_problem_refs_2026-10-18T1811.bib)
prepared during the preceding write-up. They require the maintainer's
Zotero import and Better BibTeX re-export.

The two unresolved-reference occurrences concern the pre-existing
`sec:somthing` reference in `paper1/what_is_a_quantum_state.tex:604`.
Existing layout and PDF-string warnings elsewhere in the manuscript remain.
The whole manuscript is therefore not claimed to be warning-free.

The required TeX-error scan was:

```sh
rg -n '^!' /tmp/continuity_appendix_2026-10-18T2119/build/continuity_check.log
```

It returned no output, exit status 1 (no matches). The opening appendix page
was rendered with pdftoppm and visually inspected: the title, first
cross-references and target equation fit the manuscript layout. No claim of
a complete visual audit of the manuscript is made.

## Scientific status and source provenance

The appendix preserves the proposed dependency order before the physical
L2 metric, first Hopf fibration and Born rule. The three group arguments are
explicitly conditional STRUCTURAL results. The physical relation between
self-recording limits and continuously accessible alternatives remains
CANDIDATE; the requested derivation or countermodel remains OPEN. The
paradox/hypodox comparison remains RHYME.

These are the same proposals recorded in the
[earlier session note](continuity_open_problem_writeup_2026-10-18T1811.md).
They do not upgrade any ledger entry. The earlier note records the primary
sources checked and the proposed ledger amendments; this conversion did not
add new literature claims or a new bibliography batch.

No new VERIFY-CITE or VERIFY-SUPPORT item was introduced. The two Chiribella
references retain their explicit abstract-only support limit and support
only the limited statements made. Pending bibliography import is distinct
from an unverified citation.

The appendix source requested in this turn is complete. Main-text
integration, bibliography import and the maintainer's judgement on status
proposals remain outstanding. The continuity derivation itself remains the
stated research problem.
