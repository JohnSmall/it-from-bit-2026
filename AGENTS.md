# AGENTS.md

`CLAUDE.md` is the behaviour contract for this repository and it applies to
every coding agent, not only Claude. **Read it first and follow it.** This file
exists because Codex and some other tools look for `AGENTS.md` rather than
`CLAUDE.md`; it is a pointer, not a second set of rules, and if the two ever
disagree, `CLAUDE.md` wins.

Then read `CONTRIBUTING.md` for who may change what, and
`knowledge/README.md` for what in `knowledge/` is authoritative and what is
raw archive.

## Before anything else: who are you talking to?

**If `CONTRIBUTOR.md` is not in the repository root, this is a fresh clone and
you have not met this person.** Do not assume it is the maintainer. The
ledgers, session notes and commit messages say "JS" throughout and read as
though a conversation is under way; it is not, and it may be with someone
else.

Ask their name, background and expertise, what they want to work on, and
whether they are the maintainer or a contributor. Write the answers to
`CONTRIBUTOR.md`, shaped like `CONTRIBUTOR.template.md`. That file is
gitignored, so it never leaves their machine and every clone asks afresh. If
they would rather not say, write what you have and carry on. If it already
exists, read it and do not ask again.

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
