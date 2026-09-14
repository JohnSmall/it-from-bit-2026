# AGENTS.md

`CLAUDE.md` is the behaviour contract for this repository and it applies to
every coding agent, not only Claude. **Read it first and follow it.** This file
exists because Codex and some other tools look for `AGENTS.md` rather than
`CLAUDE.md`; it is a pointer, not a second set of rules, and if the two ever
disagree, `CLAUDE.md` wins.

Then read `CONTRIBUTING.md` for who may change what, and
`knowledge/README.md` for what in `knowledge/` is authoritative and what is
raw archive.

The five rules most easily broken by an agent that has read nothing:

1. **Claims carry status labels.** Every claim takes exactly one of
   ESTABLISHED, STRUCTURAL, CANDIDATE, CONJECTURE, RHYME, OPEN. Labels are
   never upgraded in place, and only the maintainer writes them. Propose.

2. **Read `knowledge/invalid_routes.md` before proposing any mechanism or
   mass route.** A route logged there was tried and failed. Do not retry it.

3. **`.tex` edits go through a sentinel-gated patch script in `scripts/`** ---
   one that asserts its anchors match exactly once, writes a `.bak`, adds an
   `% EDITED <date>` header and refuses to run twice. Do not hand-edit a
   section file.

4. **`paper1/references.bib` is generated** by Better BibTeX from the
   maintainer's Zotero library. Never edit it. A new reference is a dated
   `.bib` batch in `bib/`; see `bib/README.md`.

5. **Never describe an output you did not produce.** Run the script, paste the
   exact stdout into a dated session note in `knowledge/sessions/`.

Two practical notes. Builds are `latexmk`, and two of them at once corrupt
each other's `.aux` --- check `pgrep -af latexmk` first, and if you are working
alongside someone, ask before building. And the maintainer works on `main`;
everyone else branches and opens a pull request.
