# knowledge/

The project's context, moved out of Claude web on 2026-09-09 so that Claude
Code, Codex or any other local tool can work inside it.

## What is authoritative, and what is raw

Three tiers, and the difference matters.

**Curated, but not yet labelled.** `results_ledger.md`, `invalid_routes.md`,
`open_problems.md`, `principles.md`, `people.md`, `literature.md`. These were
distilled by Claude from the project's own memory files, not authored by John.
Every claim in this project carries exactly one of ESTABLISHED, STRUCTURAL,
CANDIDATE, CONJECTURE, RHYME or OPEN, and **none of these entries carries one
yet**. Until John has been through them, treat their contents as reported
rather than settled. They are append-only: supersede with a dated entry, never
edit history.

**Distilled memory, as exported.** `memory/` holds the project's memory files
exactly as Claude web wrote them. `memory/project/results-and-principles.md`
is the source the curated files above were seeded from;
`memory/project/ways-of-working.md` is visibly the source CLAUDE.md was
written from. Lines there marked `[stated]` carry a provenance flag, not a
status label.

**Raw archive.** `project-docs/` (the 122 documents attached to the web
project) and `archive/conversations/` (100 conversations, full turns). This is
primary source material: it is where a claim's derivation actually lives, and
it contains superseded reasoning alongside current reasoning. Nothing here is
authoritative on its own.

## Consult order

1. `results_ledger.md` and `open_problems.md` — loaded into every session by
   CLAUDE.md, so you have them already.
2. `invalid_routes.md` — **before proposing any mechanism or mass route.** A
   route logged there was tried and failed; do not retry it.
3. `principles.md` for framing, `people.md` and `literature.md` as needed.
4. Only then the raw archive. `archive/` is never imported wholesale. Grep
   `archive/INDEX.md`, which carries every conversation's summary, then open at
   most three files. `project-docs/INDEX.md` does the same for the documents.

## Layout

    README.md              this file
    results_ledger.md      established results and the neutrino prediction
    invalid_routes.md      routes tried and failed; read before proposing one
    open_problems.md       formal open problems, and what is outstanding
    principles.md          core structural principles of the framework
    people.md              collaborators and interlocutors
    literature.md          pointer to the two Zotero-exported bibliographies
    sessions/              dated session notes (CLAUDE.md writes them here)
    memory/                exported Claude.ai memory files, as-is
    project-docs/          122 web-project documents + INDEX.md
    archive/
      INDEX.md             greppable: date, title, summary, size
      conversations/       100 conversations, full turns

## Provenance

Exported from the Claude web project "negative probability"
(uuid `019bd5b6-57f1-76bf-bda6-1c102e52f609`, created 2026-01-19) on
2026-09-09; imported here 2026-09-10.

The conversation export carries no project field, so the 100 archived
conversations were selected from a 237-conversation account export by scoring
names and summaries against the framework's vocabulary. The 137 excluded are
software consulting work — Elixir, XSLT, Atlassian — unrelated to the physics.
Conversations about the project's *tooling* are included and marked
`[tooling]` in the index. That selection is a heuristic: if something is
missing, the full export is still at
`~/Documents/claude_downloads/conversations-000/`.

Of the 122 project documents, 12 were exact duplicates and were dropped, and 4
were omitted because the repository already carries them as live sources.
Where a filename had several versions all are kept, suffixed `__vN_<date>`.
