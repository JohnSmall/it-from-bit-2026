---
name: ways-of-working
description: File and document discipline, claim-status conventions, collaboration split, and the toolchain (LaTeX, Mendeley, Python/Qiskit, GitHub)
sources: [backfill]
aliases: []
---

## Document and file discipline

- [stated] Dated filenames (`description_YYYY-MM-DDTHHMM`); attic prefix (`attic_*.superseded`) for deprecated files, never deletion
- [stated] Sentinel-gated LaTeX splices (BEGIN/END markers); compile-verify with pdflatex two passes before delivery; zero errors required
- [stated] Compile verification uses `pdflatex -interaction=nonstopmode` with two passes; errors checked via `grep -E '^!' *.log`
- [stated] Patch scripts assert anchors whitespace-insensitively, write `.bak` files, add `EDITED` headers, and refuse to run twice
- [stated] Status labels: ESTABLISHED / STRUCTURAL / CANDIDATE / CONJECTURE / RHYME / OPEN — never upgraded in place
- [stated] VERIFY-CITE and VERIFY-KEY flags on all unverified references
- [stated] Invalid routes logged explicitly in documents so they are not retried
- [stated] Session notes, ledger addenda, and RIS batches delivered as separate dated files
- [stated] Pure ASCII in `.tex` and `.md`; native Unicode in `.ris`

## Claim tracking

- [stated] Every claim requires explicit status encoding
- [stated] New conjectures formatted as PASS/FAIL open problems with explicit criteria
- [stated] Failed routes recorded alongside valid ones
- [stated] Cross-references resolved before file delivery; `MAP-LABEL` and `PAPER-COMPANION` markers used

## Collaboration style

- [stated] John drives all conceptual synthesis; Claude handles mathematical elaboration, critical engagement, literature connections, and document production
- [stated] John identifies inconsistencies between draft language and theoretical commitments; Claude diagnoses and proposes resolution
- [stated] Python scripts use a fixed random seed and Convention A for Cayley-Dickson multiplication; John runs scripts independently and reports exact terminal output for reproduction verification
- [stated] Prose style for paper text: paragraphs, no bullets; British English; `\autocite`; minimal formatting

## Tools and resources

- [stated] Computation: Python (numpy, scipy, qiskit), IBM Quantum Platform (ibm_fez Heron r2), Docker/Jupyter for the Qiskit environment; Qiskit credentials at `~/.qiskit/qiskit-ibm.json` (bind-mount recommended for persistence)
- [stated] Writing: LaTeX (pdflatex, biblatex, booktabs, braket, amsthm, draftwatermark/background); MacTeX via Homebrew; Overleaf for compilation; Biber 2.21
- [stated] Bibliography: Mendeley (`.ris` import); citation keys in `author+year+keyword` format; one `AU` line per author; native Unicode (never LaTeX escape macros — these break Mendeley import and cause LaTeX compilation errors); carry the `\autocite` citation key in the RIS `ID` field; DOIs included only where deterministic
- [stated] Repository: private GitHub (`JohnSmith/self-ref-2026`), accessed via the Claude Project knowledge panel sync rather than bash shell credentials; manual sync required after new commits; `project_knowledge_search` for content retrieval; `grep` on `/mnt/project` for label/delimiter auditing
- [stated] Key literature anchors: Moreno 1998, Biss-Dugger-Isaksen 2008, Cawagas 2004, Gunaydin-Gursey 1973, Eakin-Sathaye (J. Algebra 129, 1990), Adams 1960, Hurwitz 1898, Dür-Vidal-Cirac 2000, Coecke-Kissinger 2010, Verstraete et al. 2002, Szangolies 2025, Hardy 2001, Schack 2003, Abramsky-Brandenburger, Gillard-Gresnigt 2019; arXiv:2306.13098 flagged for priority assessment