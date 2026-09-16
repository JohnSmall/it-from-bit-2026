# Session note: the free-parameter count, made consistent across paper 1

Date: 2026-09-16T1400. Session: Claude Code (Fable 5.1), `it_from_bit_fable_5_1`.
JS: "review the count of the number of Standard Model free parameters and
ensure they're consistent throughout the paper. I don't want one section
claiming only 1 free parameter and another section counting 3."

## The inventory (every count statement in paper1/, read in context)

**Dimensional.**
- `masses_section` "dimensional-parameter count" paragraph and
  op:sector-scales: structurally exactly one dimensional input (the
  observer cannot fix the absolute scale from inside); as calculated, each
  charge sector carries its own fitted scale, three in all, the up-quark
  scale tied to $v$ by $y_t = 1$, the down-to-lepton ratio near 2. Honest.
- `boson_masses_section` op:vev: $v$ must be shown to be the *only*
  dimensional input; lists the lepton and down normalisations, the matching
  scale and the QCD scale as not yet derived from it. Honest.
- `boson_masses_section` line 262: "one free dimensional scale" as the
  framework's account, with no as-calculated caveat.
- `headline_results_snippet`, `predictions_section` line 269,
  `summary_section` lines 52 and 134: "$v$ the single dimensional input",
  no caveat. The structural claim presented as the current count. THIS IS
  THE INCONSISTENCY JS MEANT.
- The neutrino sector adds no dimensional input: its scale is the matching
  scale (which is itself matched to $\sin^2\theta_W(M_Z)$, op:matching-
  scale). The QCD scale is acknowledged as owed in the boson section.

**Dimensionless.**
- Since the 2026-09-11 patch: "no fitted dimensionless parameters (one, the
  Koide phase, matched rather than derived)" in the headline, predictions
  and summary; $\alpha = \sqrt2$ "fixed by the theory" (since 2026-09-11T2300:
  identified, not derived).
- `masses_section` eq:quarkalpha: the exponent $3/2$ in $\alpha^2 = 2 +
  2|Q|^{3/2}$ is "fixed empirically to within one per cent", its reading "a
  gloss, not a derivation"; op:colour-correction asks to derive it. A second
  rational number matched to data, of exactly the Koide phase's kind, and
  omitted from every headline count. SECOND INCONSISTENCY.
- The neutrino sector adds no dimensionless parameter: $\theta_\nu$ is
  predicted by the $n = 2$ dilution; the $0.6^\circ$ figure is the
  discrepancy, not a tuning.
- `appendix_hardware_fez` line 210: $\lambda = \sin(2/9)$ "with no free
  parameter" -- true only as "no parameter beyond the matched Koide phase".
- `main.tex` 84 and 124, `what_is_a_quantum_state` 10: "some free
  parameters" -- claim nothing countable; left alone.

## The canonical statement

No fitted dimensionless parameters. Two rational numbers matched rather than
derived: the Koide phase $2/9$ (op:koide-delta) and the quark exponent $3/2$
(op:colour-correction); $\alpha = \sqrt2$ identified. One dimensional input
admitted structurally, $v$; as calculated, the lepton and down-quark sector
scales are still set by hand (op:sector-scales), the up sector being tied to
$v$ by $y_t = 1$; the matching scale and the QCD scale are further
dimensional quantities not yet derived from $v$ (op:vev).

## What was changed

`scripts/patch_parameter_count_consistency_2026-09-16T1400.py` (three
invocations: two re-fill markers and one re-fill guard needed adjusting;
already-patched files are skipped), backups `.2026-09-16T1400.bak`:

- `headline_results_snippet_2026-07-07.tex`: the lead sentence now carries
  the canonical statement.
- `predictions_section_2026-06-13.tex`: the "count of adjustable
  constants" sentence likewise.
- `summary_section_2026-07-07.tex`: both count sentences likewise, in
  shorter form.
- `masses_section_2026-06-08.tex`: the lepton showcase's "no free
  dimensionless parameters" becomes "no fitted"; the quark exponent is
  named, where it is introduced, as "the second of the paper's two matched
  dimensionless numbers, beside the Koide phase, and counted with it
  wherever the paper counts". That paragraph holds an equation block and
  was not re-filled; one line runs over 96 columns.
- `boson_masses_section_2026-06-08.tex`: "one free dimensional scale"
  gains "structurally ... as calculated, three sector scales, of which
  $y_t = 1$ ties one to $v$ (op:sector-scales)".
- `appendices/appendix_hardware_fez_2026-07-10.tex`: "with no free
  parameter" becomes "with no parameter beyond the matched Koide phase".

Judgement call, decided by JS the same day: the $3/2$ exponent is counted
as the second matched dimensionless number, "following the paper's own
words" ("fixed empirically", "a gloss, not a derivation",
op:colour-correction). The patch stands as applied; no reversion.

Not built; not committed.

## For the ledgers (proposed)

- results_ledger, recorded not labelled: the parameter count as the
  canonical statement above, dated 2026-09-16, superseding the 2026-09-11
  "no fitted dimensionless parameter and one matched one (delta)" line in
  open_problems.md by adding the quark exponent $3/2$ as the second matched
  number.
