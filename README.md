# It from Bit via Gödel

Multi-paper series deriving Standard Model structure from self-reference
and computability. Paper 1 (foundations, submitted to ...) and Paper 2
(dynamics, in draft). Preprints: [links when available].

## Repository layout

| Path            | What it is                                              |
|-----------------|----------------------------------------------------------|
| `paper1/`       | Paper 1: `main.tex`, its sections, `appendices/`, its bib|
| `paper2/`       | Paper 2: root document and its bibliography              |
| `notes/`        | Working state: to-do items and ideas, no status labels   |
| `notebooks/`    | Jupyter notebooks behind the appendix computations       |
| `ris/`          | Dated RIS import batches                                 |
| `scripts/`      | Python calculations and LaTeX patch scripts              |
| `knowledge/`    | Curated results, open problems, and session archive      |
| `knowledge/publications/` | The author's earlier papers and posters, frozen |
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

The `.bib` files under `knowledge/publications/` are outside all of this. They
belong to finished work, carry their own citation keys, and are never
regenerated or reconciled with Zotero.

## Scripts

    python scripts/<name>.py

All calculations are seed-locked and use Cayley-Dickson Convention A.
Outputs are recorded verbatim in the session note of the same date.

## Conventions

British English, prose over bullets. Dated filenames as
`description_YYYY-MM-DDTHHMM`. Nothing is deleted: rename to
`attic_<name>.superseded`. Every claim carries a status label; see
`knowledge/README.md` for the vocabulary.

Unicode is allowed in `.tex` and `.md` where it belongs to a name, title or
quoted source: Gödel, Göttingen and Časlav all need it. Typography is not a
name, so use the LaTeX idioms and not the literal characters: `---` and `--`
for dashes, ``` `` ```, `''` and `'` for quotes, `\S` for the section sign.
Ligature codepoints (U+FB01 fi, U+FB03 ffi) are PDF copy-paste damage and are
always wrong. `CLAUDE.md` states the same rule for AI assistants.

## For AI assistants

Read `knowledge/README.md` first; it explains what is authoritative, what
is raw archive, and the order to consult things. Behavioural rules for
Claude Code are in `CLAUDE.md`.

## Authors and citation

John Small ([0000-0001-7123-411X](https://orcid.org/0000-0001-7123-411X)).

Citation metadata is in `CITATION.cff`; GitHub renders it as a "Cite this
repository" button and Zenodo reads it when minting a DOI. Once a preprint
exists, cite that in preference and use the repository DOI for the exact
source state it was built from.

Claude (Anthropic) was used for mathematical elaboration, literature
verification, LaTeX production and bibliography management. It is not an
author: arXiv's policy is that "generative AI language tools should not be
listed as an author", while significant use must be reported, and
responsibility for any AI-generated error rests with the author. Papers
carry a disclosure statement to that effect.

## Licence

Two licences, by kind of material.

**CC BY 4.0** (`LICENSE`) covers the prose, figures and everything under
`knowledge/`: the papers, their sections and appendices, the ledgers, and the
document and conversation archive. Reuse freely with attribution.

**MIT** (`LICENSE-MIT`) covers `scripts/` and `notebooks/`, so the
verification code can be reused without the attribution obligations that
suit prose.

Attribute as: John Small, "It from Bit via Gödel",
https://github.com/JohnSmall/it-from-bit-2026

`knowledge/archive/` holds transcripts of research conversations, which
contain both the author's words and model output. They are published here
under the same CC BY 4.0 terms.

**Third-party, under their own terms.** `knowledge/publications/` bundles
LaTeX templates that are not the author's and are not his to relicense: Anish
Athalye's Gemini beamerposter theme in each poster directory, which carries
its own MIT `LICENSE.md`, and the American Institute of Physics `aipproc`
class with the 2005 paper. The posters and the paper themselves are the
author's, under the CC BY 4.0 above.

## Releases and DOI

Tags are paper-scoped and follow arXiv version numbering, `paper1-v1`,
`paper2-v1`, so a tag can be checked out to reproduce exactly the source
behind a given preprint version. Dated `snapshot-YYYY-MM-DD` tags mark
working states and are not released.

Semantic versioning is deliberately not used: it encodes an API
compatibility contract, and there is no API here.

Publishing a GitHub release mints a Zenodo version DOI, plus one concept DOI
resolving to the latest. Note that a release archives the **whole**
repository, `knowledge/` included, and Zenodo records are not designed to be
withdrawn.

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
│   ├── publications/             # prior papers and posters, frozen + INDEX.md
│   ├── memory/                   # exported Claude.ai memory files, as-is
│   ├── project-docs/             # export target (docs not already in repo)
│   └── archive/
│       ├── INDEX.md
│       └── conversations/        # export target
├── paper1/, paper2/, notes/, notebooks/, scripts/, ris/ ...

