# Mathematical research invitation — 2026-10-10T1050

John Small asked for the mathematical avenue to be presented as an invitation to
mathematicians, with significance for pure mathematics even though completing it
is outside the paper's scope. He identified Mortensen's inconsistent mathematics
and Deutsch's proposal to admit physically realised logical operations as the
relevant connections.

## Change and scope

Replaced the paragraph immediately after the Deutsch quotation in
[what_is_a_quantum_state.tex](../../paper1/what_is_a_quantum_state.tex) with three
paragraphs connecting this enquiry to existing inconsistent mathematics and
imaginary logical values. The passage identifies a proposed common origin in
self-reference for extended logical values and physical amplitudes. It expressly
leaves that mathematical programme for further work, while allowing the
conditional reversible-continuity-to-`p=2` argument to be assessed on its premises.

The revised passage recognises that mathematics can already study quantum
structures axiomatically. A derivation from self-reference would add foundational
explanation. The correspondence between superposition and inconsistent logical
states is posed as a question requiring a semantics.

Changed or added:

- `paper1/what_is_a_quantum_state.tex`
- `scripts/patch_mathematical_research_invitation_2026-10-10T1050.py`
- `bib/mathematical_research_refs_2026-10-10T1050.bib`
- this session note

The script created
`paper1/what_is_a_quantum_state.tex.2026-10-10T1050.bak`.
Existing work in the source was preserved by replacing one uniquely matched
paragraph. No ledger, generated bibliography, or publication was edited.
The adjacent assertion about a complex probability for a bijection between
`Q` and `R` was outside this splice; this change supplies no proof of it.

## Source verification

[Mortensen's publisher record](https://link.springer.com/book/10.1007/978-94-015-8453-1)
verifies the book metadata and supplies an introductory excerpt about controlling
inconsistency. His
[own overview](https://plato.stanford.edu/entries/mathematics-inconsistent/)
explains nontriviality and the foundational motivation. The full book was not
read. Its publisher front-matter PDF could not be fetched.

[Kauffman and Collings](https://arxiv.org/html/1905.12891), abstract and
introduction, directly support the existence of earlier work on imaginary
logical values and a square root of negation. This rules out retaining the
paragraph's categorical claim that logicians have not used these ideas.

[Deutsch, Ekert and Lupacchini](https://arxiv.org/html/math/9911150),
section 2, support the existing quotation about admitting an operation on the
strength of its physical realisation.

The new bibliography batch records the precise attached claims, support read,
metadata provenance, and limitations. No new VERIFY-CITE or VERIFY-SUPPORT item
remains. The cited sources do not establish the proposed identification of
superposition with self-referential inconsistency.

## Status proposals for JS

These are proposals, not applied labels or ledger changes.

| Claim | Proposed status |
| --- | --- |
| The cited literature contains nontrivial inconsistent mathematics and a four-valued calculus with square-root negation. | ESTABLISHED |
| Self-reference may supply a common foundation for extended logical values and quantum amplitudes. | CONJECTURE |
| A precise semantics connecting quantum superposition to the inconsistent states relevant to self-reference remains to be constructed. | OPEN |

No upgrade of the existing continuity argument is proposed. No new mathematical
result requiring a ledger entry was obtained.

## Exact validation output

Read-only preflight, exit 0:

```text
verified: one whitespace-insensitive paragraph anchor
verified: one BEGIN/END pair and existing norm-section label
verified: both new citation keys occur once in the dated batch
--check: nothing written
```

Patch application, exit 0:

```text
verified: one whitespace-insensitive paragraph anchor
verified: one BEGIN/END pair and existing norm-section label
verified: both new citation keys occur once in the dated batch
patched: paper1/what_is_a_quantum_state.tex
backup: paper1/what_is_a_quantum_state.tex.2026-10-10T1050.bak
```

Read-only repeat attempt, exit 1 as intended. Stdout was empty; exact stderr:

```text
Refusing to run twice: edit sentinel or backup already exists.
```

`git diff --check -- paper1/what_is_a_quantum_state.tex` exited 0 with no output.

New bibliography batch validation, exit 0:

```text
INFO - This is Biber 2.21 running in TOOL mode
INFO - Logfile is '/tmp/self-ref-mathematical-invitation-2026-10-10T1050/mathematical_research_refs_2026-10-10T1050.bib.blg'
INFO - Looking for bibtex file 'bib/mathematical_research_refs_2026-10-10T1050.bib'
INFO - LaTeX decoding ...
INFO - Found BibTeX data source 'bib/mathematical_research_refs_2026-10-10T1050.bib'
INFO - Datamodel validation starting
INFO - Datamodel validation complete
INFO - Overriding locale 'en_US' defaults 'variable = shifted' with 'variable = non-ignorable'
INFO - Overriding locale 'en_US' defaults 'normalization = NFD' with 'normalization = prenormalized'
INFO - Sorting list 'tool/global//global/global/global' of type 'entry' with template 'tool' and locale 'en_US'
INFO - No sort tailoring available for locale 'en_US'
INFO - Writing '/tmp/self-ref-mathematical-invitation-2026-10-10T1050/mathematical_research_refs_2026-10-10T1050_bibertool.bib' with encoding 'UTF-8'
INFO - Output to /tmp/self-ref-mathematical-invitation-2026-10-10T1050/mathematical_research_refs_2026-10-10T1050_bibertool.bib
```

No running latexmk process was reported by the pre-build `pgrep -af '[l]atexmk'`
check (exit 1, empty output). The build used an isolated output directory under
`/tmp`. Exact build-wrapper stdout:

```text
command: latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/self-ref-mathematical-invitation-2026-10-10T1050 paper1/main.tex
latexmk exit code: 0
main.log lines beginning !: 0
PDF produced: True
new citation undefined (mortensen1995inconsistent): True
new citation undefined (kauffmancollings2019bf): True
build transcript: /tmp/self-ref-mathematical-invitation-2026-10-10T1050/build.stdout.log
compile log: /tmp/self-ref-mathematical-invitation-2026-10-10T1050/main.log
```

The build succeeded with zero lines beginning `!` in `main.log`.
The two new citations remain undefined until JS imports the dated batch into
Zotero and re-exports `paper1/references.bib`. Biber also reported pre-existing
case mismatches for the Moreno and Spekkens keys. No bibliography export or
commit was performed.

## Exact diff against the script's backup

```diff
--- paper1/what_is_a_quantum_state.tex.2026-10-10T1050.bak	2026-10-10 10:51:25.338520783 +0100
+++ paper1/what_is_a_quantum_state.tex	2026-10-10 10:51:25.346520849 +0100
@@ -1,3 +1,4 @@
+% EDITED 2026-10-10 scripts/patch_mathematical_research_invitation_2026-10-10T1050.py
 % EDITED 2026-09-26 scripts/patch_carlsberg_footnote_2026-09-26T0930.py
 % EDITED 2026-09-20 scripts/patch_born_cost_ledger_v2_2026-09-20T0900.py
 % EDITED 2026-09-20 scripts/patch_anti_event_real_cost_v2_2026-09-20T1000.py
@@ -516,15 +517,32 @@
 entitled to propose a new logical operation $\sqrt{not}$. Why? Because a faithful physical model
 for it exists in nature!
 \end{quotation}
-However logicians have not used $\sqrt{not}$ in their discussions of self-referential logic.
-This is quite understandable since the postulates of quantum mechanics are an ad-hoc collection
-without explanation other than the fact that they work and we can calculate numbers which match
-experiment. Which isn't good enough for mathematicians who want a well founded explanation.
-Hence Deutsch's suggestion that logicians could use the logical states enabled by quantum
-mechanics has certainly not been adopted by people working in and around the fields of
-self-referential logic and inconsistent mathematics. Although we're in a strange land where
-people are using quantum computation, which involves imaginary truth values, yet logicians have
-not taken to using them in their exploration of self-referential paradoxes and hypodoxes.
+% BEGIN mathematical_research_invitation_2026-10-10T1050
+Deutsch's suggestion connects the present enquiry with Mortensen's programme of inconsistent
+mathematics, which studies mathematical theories in logics that tolerate contradictions without
+making every proposition provable \autocite{mortensen1995inconsistent}. There is also work directly
+extending Spencer-Brown's imaginary logical values: Kauffman and Collings develop a four-valued
+calculus with a square root of negation \autocite{kauffmancollings2019bf}. These provide
+mathematical starting points for asking whether quantum superposition can supply a semantics for
+self-referential expressions that admit no consistent Boolean assignment.
+
+The proposed connection is that the obstruction identified by Lawvere and Yanofsky may motivate
+both an extension of logical values and the complex amplitudes used in physics. A mathematical
+derivation along these lines would give superposition a foundation in the structure of
+self-reference, strengthening Deutsch's appeal to physically realised operations. Quantum
+structures can already be studied axiomatically; the additional gain would be an explanation of
+why such structures arise. Establishing the correspondence between superposition and the states
+used in inconsistent mathematics remains part of this enquiry.
+
+Completing this route could therefore open further work on self-reference, nonclassical semantics
+and computation, with significance for pure mathematics independent of its applications to
+quantum foundations. Here it is offered as an invitation to mathematicians. The present paper
+develops the physically motivated route through self-referential ignorance and Shannon
+information; it leaves the proposed mathematical connection for further work. Its conditional
+argument from reversible continuity to the $p=2$ norm
+(\S\ref{sec:reversible-continuity-l2}) can be assessed on its stated premises without completing
+that wider programme.
+% END mathematical_research_invitation_2026-10-10T1050
 
 \subsection{The cost of a record, and why it is a square}
 \label{sec:born-cost-ledger}
```

