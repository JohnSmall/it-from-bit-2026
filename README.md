# It from Bit via Gödel

Multi-paper series deriving Standard Model structure from self-reference
and computability. Paper 1 (foundations, submitted to ...) and Paper 2
(dynamics, in draft). Preprints: [links when available].

## Repository layout

| Path            | What it is                                              |
|-----------------|----------------------------------------------------------|
| `paper1/`       | Paper 1: `main.tex`, its sections, `appendices/`, its bib|
| `paper2/`       | Paper 2: root document and its bibliography              |
| `orphans/`      | Fragments reachable from neither paper; not yet placed   |
| `notebooks/`    | Jupyter notebooks behind the appendix computations       |
| `ris/`          | Dated RIS import batches                                 |
| `scripts/`      | Python calculations and LaTeX patch scripts              |
| `knowledge/`    | Curated results, open problems, and session archive      |
| `attic_*`       | Superseded material, kept for provenance; never deleted  |

## Building

Requires TeX Live 2025 (pinned to match Overleaf) with biber.

    latexmk                        # build every paper
    latexmk paper1/main.tex        # one paper only
    latexmk -pvc paper1/main.tex   # rebuild on save
    latexmk -C                     # clean every paper

Each paper is built in its own directory: `.latexmkrc` sets `$do_cd`, so
latexmk changes into `paper1/` or `paper2/` before running. That is why the
`\input` paths inside a paper are plain filenames with no directory
prefix, and why build artefacts land beside their source rather than in the
shared root. A raw `pdflatex paper1/main.tex` from the root does not chdir
and will fail to find the sections; use latexmk, or run pdflatex from
inside the paper's directory.

Check the paper's `.log` for lines beginning with `!` before treating a
build as clean.

`texlive.profile` is the answer file that produced this installation.
`install-tl --profile texlive.profile` reproduces the same TeX Live on
another machine, which is what "pinned" above means in practice.

## Bibliography

Each paper has its own bibliography, exported by Better BibTeX from its
own Zotero collection: `references.bib` from `self-ref-2026-cited` for
Paper 1, and `references_paper2.bib` from `self-ref-2026-paper2-cited` for
Paper 2. Some references appear in both. Neither file is edited by hand; a
missing key is a Zotero problem, not a `.bib` one. To export, right-click
the collection, choose Export Collection, and pick the Better BibTeX
format. Keep BBT's "Fields to omit from export" set to `abstract,file`, or
the export carries local storage paths into the repository.

New references go in as a dated RIS batch under `ris/`, imported into
Zotero. Zotero's importer discards the RIS `ID` field, so Better BibTeX
assigns a formula key on import and the intended key must then be pinned by
hand in the item's Citation Key field; the export honours whatever is
pinned there. Keys are `author+year+keyword`, inherited from the Mendeley
library the collections were built from.

A collection is aligned with its paper when the exported keys and the
`\abx@aux@cite` entries in that paper's `.aux` file are the same set. That
comparison is the check worth running after any change to either side.

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
├── paper1/, paper2/, orphans/, notebooks/, scripts/, ris/, attic_* ...

