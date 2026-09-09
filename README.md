# It from Bit via Gödel

Multi-paper series deriving Standard Model structure from self-reference
and computability. Paper 1 (foundations, submitted to ...) and Paper 2
(dynamics, in draft). Preprints: [links when available].

## Repository layout

| Path            | What it is                                              |
|-----------------|----------------------------------------------------------|
| `main.tex`      | Paper 1 root document                                   |
| `*.tex`         | One file per section, at top level, input from `main.tex`|
| `paper2/`       | Paper 2 (separate root)                                  |
| `references.bib`| Generated from Zotero (see Bibliography)                 |
| `ris/`          | Dated RIS import batches                                 |
| `scripts/`      | Python calculations and LaTeX patch scripts              |
| `knowledge/`    | Curated results, open problems, and session archive      |
| `attic_*`       | Superseded material, kept for provenance; never deleted  |

## Building

Requires TeX Live 2025 (pinned to match Overleaf) with biber.

    latexmk            # full build of main.tex
    latexmk -pvc       # rebuild on save
    latexmk -C         # clean; use when citations misbehave after a .bib change

`.latexmkrc` in the root sets pdflatex + biber. Check `main.log` for lines
beginning with `!` before treating a build as clean.

## Bibliography

`references.bib` is auto-exported by Better BibTeX from the Zotero
collection "self-ref-2026"; do not edit it by hand. New references go in
via a dated RIS batch under `ris/` imported into Zotero, then the AUX
scanner keeps the collection aligned with what the paper cites. Citation
keys are `author+year+keyword`.

## Scripts

    python scripts/<name>.py

All calculations are seed-locked and use Cayley-Dickson Convention A.
Outputs are recorded verbatim in the session note of the same date.

## Conventions

British English, pure ASCII in .tex and .md, prose over bullets. Dated
filenames as `description_YYYY-MM-DDTHHMM`. Nothing is deleted: rename to
`attic_<name>.superseded`. Every claim carries a status label; see
`knowledge/README.md` for the vocabulary.

## For AI assistants

Read `knowledge/README.md` first; it explains what is authoritative, what
is raw archive, and the order to consult things. Behavioural rules for
Claude Code are in `CLAUDE.md`.

## Authors and citation

John ..., with ... . Cite as: [bibtex block once there's a preprint].
## Directory Structure
self-ref-2026/
├── CLAUDE.md                     # behaviour contract (short)
├── .latexmkrc
├── .claude/
│   ├── rules/                    # empty for now
│   └── skills/
│       └── search-archive/SKILL.md
├── knowledge/
│   ├── README.md                 # map: what lives where, consult order
│   ├── results_ledger.md         # curated — filled by distillation
│   ├── invalid_routes.md
│   ├── open_problems.md
│   ├── principles.md
│   ├── literature.md
│   ├── people.md
│   ├── memory/                   # exported Claude.ai memory files, as-is
│   ├── project-docs/             # export target (docs not already in repo)
│   └── archive/
│       ├── INDEX.md
│       └── conversations/        # export target
├── main.tex, section .tex files, scripts/, ris/, attic_* ...

