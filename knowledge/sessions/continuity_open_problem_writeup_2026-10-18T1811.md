# Session record: continuity open-problem write-up

18 October 2026, filename time in Europe/London. Prepared for John Small,
maintainer. All scientific status labels below are proposals for his review.
No ledger labels were assigned or changed.

## Request and deliverable

John asked for a record of the attempts to derive continuity of reversible
transformations from self-reference, why each is insufficient, a possible
missing physical insight, and an OPEN proposal suitable for seeking advice.

The standalone [discussion draft](continuity_from_self_reference_open_problem_2026-10-18T1811.md)
contains ten attempted routes, their individual gaps, the intended order
before the Born rule, a candidate direction centred on the physical act of
self-description, an explicit OPEN problem, questions for advisers, and an
appendix proving the surviving conditional group arguments. It is separate
from this process record so it can be shared on its own.

The write-page skill was used for document structure and editorial review,
with the repository's local destination and conventions taking precedence:
[SKILL.md](/home/john/.codex/plugins/cache/openai-curated-remote/pages/0.1.23/skills/write-page/SKILL.md).
The draft is in sessions because notes/README.md reserves notes/ for working
chores and ideas without claim-status assignments. No remote Page was created.

## Files created

- [Discussion draft](continuity_from_self_reference_open_problem_2026-10-18T1811.md).
- [Five-reference BibLaTeX batch](../../bib/continuity_open_problem_refs_2026-10-18T1811.bib).
- This session record.

The starting working tree contained numerous pre-existing modifications and
untracked files, including modifications to the generated bibliography.
This task edited none of those files. No manuscript, ledger, generated
bibliography or frozen publication was changed. No commit was made.

## Proposed append-only ledger entries

These are proposals, not edits to the ledgers. The full OPEN statement is
in the discussion draft; the summary below identifies the intended entry.

### For knowledge/open_problems.md

**OPEN — Physical self-description and continuous reversible accessibility
(proposed sharpening of op:limit-realisability).** Specify an operational
condition R for the limitations on an embedded observer's self-description,
including physical memory, record production and feedback. In finite-dimensional
operational models carrying the explicitly declared complex-amplitude
structure, determine whether R forces continuous reversible paths between
any two pure states. First isolate the question with closedness and
transitivity granted; then identify whether those assumptions and available
inverses are derivable or independent. PASS: either a proof for all models of
explicit, independently motivated premises, or a countermodel with the same
premises and the full observer/record procedures. FAIL as a derivation: using
Born probabilities, a quadratic physical norm, full ray admissibility or
continuous control before these are derived, or equating a continuum of
mixed-state probabilities with connected pure states. A successful narrow
result is conditional, not a derivation from self-reference alone.

### For knowledge/results_ledger.md, if useful

**STRUCTURAL.** A closed group of reversible affine automorphisms of a
finite-dimensional compact convex state body is a compact Lie group. If it
acts transitively on a connected pure-state space, its identity component
acts transitively. Divisibility is an alternative sufficient condition for
connectedness of the group, not a consequence of an unspecified absence of a
preferred step. Evidence: manuscript propositions prop:divisible-closed and
prop:connected-transitive; explicit proofs in the new discussion draft.

**STRUCTURAL.** With that compact Lie structure and transitivity, requiring
every reversible transformation to fix an admissible pure state forces a
nontrivial pure-state space to be connected and positive-dimensional. The
finite action on identity-component orbits would otherwise have a derangement.
Evidence: 10 October fixed-point session and the new appendix. This statement
retains the pure fixed-point premise; mixed fixed points do not suffice.

**CANDIDATE.** The missing physical link may be a constraint on information,
disturbance and recoverable correlations in a complete act of self-description.
One possible direction is a physical reason why an obstruction to reversible
access would supply a repeatably readable distinction; another is an operational
purification or reversible-dilation principle. Neither link has been derived.
This is a research direction, not a status upgrade for continuity.

### For knowledge/invalid_routes.md, if useful

Record these as failed implications in their stated form, not as bans on
routes with genuinely additional physical premises:

- Operational normalisation to continuity via absolute-square weights is
  circular in the intended continuity -> metric -> Hopf -> Born order.
  The 10 October probability-conservation note's section 2 explicitly
  supplies the square weights as its third premise.
- Complex amplitudes, preservation of a quadratic norm, or symmetry among
  admitted bases do not separately require a connected transformation group.
  Finite Clifford actions provide the relevant complex example.
- Restricted superposition admissibility does not imply nonlinear maps.
  The stabiliser phase gate is complex-linear and reversible.
- Diagonalisation, uncountability, a continuum of mixed probabilities, and
  closure under limits do not separately establish connected pure states.
- Absence of heat dissipation alone does not establish a physically available
  inverse; the thermodynamic, logical and dynamical assertions must be separated.

The connected-state-space and pure-fixed-point routes are retained as
conditional mathematics, not entered as false theorems.

## Source verification and its limits

Primary sources were read at the level indicated below. No exact quotation
was needed in the discussion draft. Existing reference keys were reused by
provenance; the five missing sources were prepared in a new batch for John
to import if wanted. Nothing was written to Zotero.

| Source | Passage checked and limited use |
| --- | --- |
| [Hardy, quant-ph/0101012](https://arxiv.org/pdf/quant-ph/0101012) | Axiom 5 and operational state description. The preprint is from 2001, not 2008. |
| [Popper, Part I](https://cqi.inf.usi.ch/qic/popper-indet.pdf) | Printed pp. 118–119 include calculation, permanent prediction records and classical limitations on universal self-prediction. No claim about universal failure of every partial record. |
| [Backens, 1307.7025](https://arxiv.org/pdf/1307.7025) | Section 2.1 gives the Clifford phase gate and finite single-qubit group; section 5 states the six single-qubit pure stabiliser states. |
| [Spekkens, quant-ph/0401052](https://arxiv.org/pdf/quant-ph/0401052) | Toy-bit pure epistemic states and reversible permutations, sections III.A and III.C. Used as the earlier finite foil, not as a native complex-amplitude model. |
| [Bennett, physics/0210005](https://arxiv.org/pdf/physics/0210005) | Preprint pp. 1–2 distinguish logical information loss, entropy transfer and microscopic reversibility; copying into a blank register is discussed explicitly. |
| [Simon, Bužek and Gisin, quant-ph/0102125](https://arxiv.org/pdf/quant-ph/0102125) | Abstract and opening assumptions explicitly include Hilbert rays and the usual trace probability rule. |
| [Chiribella, D'Ariano and Perinotti, 0908.1583](https://arxiv.org/abs/0908.1583) | Support: abstract only. Used for the existence and stated scope of operational purification, not a new continuity theorem. |
| [Chiribella, D'Ariano and Perinotti, 1011.6451](https://arxiv.org/abs/1011.6451) | Support: abstract only. Used to state that purification is accompanied by other informational axioms. No claim about all background topological assumptions. |
| [Yanofsky, math/0305282](https://arxiv.org/html/math/0305282) | Theorem 1 and its diagonal construction, together with the discussion of representation and structure-preserving maps. Used to retain the missing hypotheses of a Lawvere argument. |

Bibliographic metadata for the five new entries was checked against their
arXiv records. The two abstract-only limitations are also in their BibLaTeX
notes. No unresolved VERIFY-CITE or VERIFY-SUPPORT item was introduced for
the limited claims made. An audit of the full purification reconstructions
would be new work, not something this note claims to have completed.

## Validation

The draft was read back and reviewed for hidden uses of Born normalisation,
full state admissibility, physical continuity and pure rather than mixed
fixed points. Its group arguments were checked as mathematical proofs; no
numerical verification of those arguments is claimed. No earlier numerical
script was rerun, and none of its recorded results is presented as a new run.

The following initial inline, deterministic document check was run. It checks local
link targets, delimiter counts, five distinct bibliography keys, brace
balance and trailing whitespace. It is not a BibLaTeX parser or a proof checker.

```sh
python3 - <<'PY'
from pathlib import Path
import re

root = Path.cwd()
doc = root / 'knowledge/sessions/continuity_from_self_reference_open_problem_2026-10-18T1811.md'
bib = root / 'bib/continuity_open_problem_refs_2026-10-18T1811.bib'
body = doc.read_text()
targets = re.findall(r'\]\(([^)]+)\)', body)
local = sorted({t for t in targets if not t.startswith(('http://', 'https://', '#'))})
missing = [t for t in local if not (doc.parent / t.split('#', 1)[0]).is_file()]
assert not missing, missing
assert body.count(r'\(') == body.count(r'\)')
assert body.count(r'\[') == body.count(r'\]')
entries = re.findall(r'^@\w+\{([^,]+),', bib.read_text(), re.M)
assert len(entries) == 5 and len(set(entries)) == 5
assert bib.read_text().count('{') == bib.read_text().count('}')
for path in (doc, bib):
    assert all(line == line.rstrip() for line in path.read_text().splitlines()), path
print(f'Local Markdown targets: {len(local)} checked, none missing')
print('Mathematical delimiters: balanced')
print('New BibLaTeX entries: 5 distinct keys; braces balanced')
print('Trailing whitespace: none in the two draft files')
print('Document checks: PASS')
PY
```

Exact stdout (exit status 0):

```text
Local Markdown targets: 9 checked, none missing
Mathematical delimiters: balanced
New BibLaTeX entries: 5 distinct keys; braces balanced
Trailing whitespace: none in the two draft files
Document checks: PASS
```

The discussion draft was then converted to Markdown dollar-delimited maths
for Markdown preview compatibility. An error while generating the revised
validator produced a Python syntax error before its checks ran. Exact
combined output (stdout empty, exit status 1):

```text
  File "<stdin>", line 13
    assert body.replace('$', '').count('
                                       ^
SyntaxError: unterminated string literal (detected at line 13)
```

The display delimiters and validator generation were corrected. The final
validator was the initial command above with its two mathematical-delimiter
assertions replaced by:

```python
assert body.count('$$') % 2 == 0
assert body.replace('$$', '').count('$') % 2 == 0
assert not re.search(r'^\$$', body, re.M)
```

Exact final stdout (exit status 0):

```text
Local Markdown targets: 9 checked, none missing
Mathematical delimiters: balanced
New BibLaTeX entries: 5 distinct keys; braces balanced
Trailing whitespace: none in the two draft files
Document checks: PASS
```

Compile status: not run; only Markdown and a bibliography batch were created.
The batch is not consumed by a manuscript build until the maintainer imports
and exports it. The directly linked sources already make the discussion
draft usable without that import.

Outstanding: maintainer judgement on proposed ledger entries and labels;
optional Zotero import. The requested write-up is complete. Deriving the
missing physical principle remains the OPEN research problem, not an
unperformed part of this documentation task.
