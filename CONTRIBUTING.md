# Contributing

This is a working research repository for a multi-paper physics series, not a
software project, and the conventions follow from that: the papers are the
product, the ledgers are the memory, and provenance matters more than speed.

## Getting started

You need TeX Live 2025 with `biber`, and Python 3 for the scripts.
`texlive.profile` is the answer file that produced the maintainer's
installation, so `install-tl --profile texlive.profile` reproduces it.

    git clone git@github.com:JohnSmall/it-from-bit-2026.git
    cd it-from-bit-2026
    latexmk paper1/main.tex

That should finish with `Output written on main.pdf`. A build is clean only if
`grep -E '^!' paper1/main.log` returns nothing. `latexmk` on its own builds
both papers; `latexmk -C` cleans them.

Nothing else needs installing. There are no absolute paths in the repository
and the scripts are seed-locked, so they give the same numbers on your machine
as on anyone else's. The one thing that will not work for you is the Zotero
tooling, which needs a local library you do not have --- see **Bibliography**
below.

## Read before you write

In this order:

1. `CLAUDE.md` --- the behaviour contract. It binds people as well as agents.
   `AGENTS.md` points Codex and similar tools at it.
2. `knowledge/README.md` --- what in `knowledge/` is authoritative, what is
   raw archive, and the order to consult it.
3. `knowledge/results_ledger.md`, `knowledge/open_problems.md` and
   `knowledge/invalid_routes.md`.

That third one is not optional. **Before proposing any mechanism or mass
route, read `invalid_routes.md`.** A route logged there was tried and failed,
often expensively, and the entry says why. Re-deriving a closed route is the
most common way to waste a week here.

## Who changes what

The maintainer is John Small. He works on `main` directly. Everyone else
branches and opens a pull request.

    git switch -c topic/short-description

One reviewable change per pull request. In the description, say what you
changed, what you built, and what the build printed.

**Yours to change freely**, on a branch:

- section and appendix `.tex` files, through a patch script (see below)
- `scripts/` and `notebooks/`
- `notes/todo.md` and `notes/ideas.md`
- a new dated session note in `knowledge/sessions/`

**Propose, do not apply:**

- *Status labels.* Every claim carries exactly one of ESTABLISHED,
  STRUCTURAL, CANDIDATE, CONJECTURE, RHYME, OPEN. Labels are never upgraded
  in place. Put the proposed label and its evidence in your session note and
  let the maintainer write it into the ledger.
- *Ledger entries* in `knowledge/`. The ledgers are append-only: supersede
  with a dated entry, never edit history.
- *The bibliography.* See below.

**Do not touch:**

- `knowledge/publications/` --- the 2005 CASYS paper and the Vaxjo posters,
  kept verbatim as presented. Corrections go upstream to their own
  repositories, not here.
- `knowledge/archive/` and `knowledge/memory/` --- the exported record, kept
  as it was written.
- `paper1/references.bib` and `paper2/references_paper2.bib` --- generated.

## Editing the papers

`.tex` edits go through a sentinel-gated patch script in `scripts/`, named
`patch_<what>_<YYYY-MM-DDTHHMM>.py`. The script must assert that each anchor
matches exactly once (whitespace-insensitively), write a `.bak`, prepend an
`% EDITED <date> <script>` header, and refuse to run twice. Commit the script
with the change: it is the record of what was done and why, and several have
already caught mistakes that a hand edit would have buried.

British English. Paragraphs, not bullets, in paper prose. Citations via
`\autocite`. Unicode belongs in names and quoted titles; use LaTeX idioms for
typography, not literal characters.

## Bibliography

`paper1/references.bib` is exported by Better BibTeX from the maintainer's
Zotero library. **You cannot regenerate it**, and that is the one real
friction of working here.

So when you need a new reference:

1. Write a dated BibLaTeX batch to `bib/`, as `.bib` and never `.ris`. The
   entry key is the citation key --- `author+year+keyword`. `bib/README.md`
   has the details, including two ways an import silently goes wrong.
2. Cite that key in the text as normal.
3. Say in the pull request that an import and re-export are owed.

Until the maintainer imports the batch, your build reports that citation as
undefined. **That is expected, not a fault** --- say so in the pull request so
a reviewer does not chase it.

Any citation you cannot verify against a source you actually read is marked
`VERIFY-CITE` in the text and listed in your summary.

## Computations

Fixed seed, Cayley-Dickson Convention A, no hidden state. Run the script and
paste the **exact stdout** into a dated session note in `knowledge/sessions/`.
Never describe an output you did not produce. If a result is worth a ledger
entry, propose one in the note.

## Working alongside someone else

- **Two `latexmk` runs at once corrupt each other's `.aux`.** Check
  `pgrep -af latexmk` before building. If you are sharing a machine or a
  working tree with another session, ask before you build.
- **Only the maintainer writes to Zotero.** It is a SQLite database with one
  writer, and the scripts named `zotero_*` in `scripts/` need a local API key
  that exists only on his machine.
- Expect tracked files to change under you mid-session if more than one agent
  is working. Re-read before editing.

## Commits

Dated, one line on what changed and why:

    2026-09-14: add the conclusions section and input it in main.tex

Never commit build artefacts; `.gitignore` covers them. Nothing is deleted ---
superseded files are renamed `attic_<name>.superseded` and moved to
`paper1/attic/`. No force-push.

## Authorship and AI

Claude is used here for mathematical elaboration, literature verification,
LaTeX production and bibliography management, and its contributions are
recorded in commit trailers and in `knowledge/archive/`. It is not an author:
arXiv's policy is that generative AI tools should not be listed as authors,
while significant use must be reported, and responsibility for any
AI-generated error rests with the human author.

If you contribute materially to a paper, authorship is a conversation to have
with the maintainer before submission, not something settled by the commit
log.
