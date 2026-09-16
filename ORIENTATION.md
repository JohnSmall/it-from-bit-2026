# Orientation

For someone who has just cloned this and wants to understand, evaluate or
challenge the framework. If you want to *build* or *contribute*, read
`CONTRIBUTING.md` instead; this is about reading and asking.

## What is here

    paper1/main.tex     the paper. 192 pages, builds with `latexmk paper1/main.tex`
    paper2/             a compilable skeleton, not yet a paper
    knowledge/          the project's memory: what is settled, what failed, what is open
    bib/                reference batches waiting to be imported into Zotero
    scripts/            every computation and every edit ever made to the papers
    notebooks/          the Jupyter/Python record behind the appendix computations

**Only two documents build**, and `latexmk` with no arguments builds both:

    latexmk paper1/main.tex                      # the paper
    latexmk paper2/paper2_main_2026-07-07.tex    # the skeleton

Everything else is source or record. `paper1/*.tex` are the sections, pulled in
by `main.tex`; `paper1/appendices/` likewise. Anything named `attic_*` is
superseded and kept only for provenance --- nothing deletes here.

## Four bodies of text, and what each is worth

This matters more than the directory layout, because an answer's weight depends
entirely on where it came from.

**The paper** (`paper1/`) is the claim. If something is in the built PDF, it is
what the author is prepared to defend.

**The curated ledgers** (`knowledge/results_ledger.md`,
`knowledge/open_problems.md`, `knowledge/invalid_routes.md`,
`knowledge/principles.md`) are the working memory: what has been established,
what has been tried and failed, and what remains. They are append-only ---
superseded entries are struck through by a later dated entry, never edited ---
so reading one from top to bottom shows how a view changed.

**The session notes** (`knowledge/sessions/`) are dated working records, each
carrying the exact stdout of any script it ran. When a ledger entry says a
thing was verified, the session note is where you check.

**The archive** (`knowledge/archive/`, 99 conversations; `project-docs/`, 111
files) is raw material. It contains superseded reasoning alongside current
reasoning and is **authoritative about nothing**. Never read it wholesale ---
grep `INDEX.md`, which carries every conversation's summary, then open at most
two or three files.

## The status vocabulary

Every claim in this project carries exactly one of six labels, and they are the
key to reading anything here. Three are defined in the paper itself, in
`paper1/appendices/appendix_jaynes_fibration_2026-07-19.tex`:

- **STRUCTURAL** --- established mathematics, imported. *"None of this is ours,
  and none of it is at stake."*
- **CANDIDATE** --- the framework's own assembly. Readings that *"stand or fall
  with the main text's derivation chain"*.
- **RHYME** --- a fenced analogy. Suggestive, and explicitly not an argument.

Three more are used throughout and carry their ordinary sense:

- **ESTABLISHED** --- the framework's own result, proved or numerically verified.
- **CONJECTURE** --- stated but not proved, no pass/fail criteria.
- **OPEN** --- an open problem with explicit pass/fail criteria.

So "the Koide relation is ESTABLISHED" and "the dimension-ratio reading is
CANDIDATE" are very different assertions about the same paragraph, and the
difference is the point. Labels are never upgraded in place: a change of
status appears as a new dated entry, so the old judgement stays visible.

## The open problems are the invitation

There are **two lists and they are not the same**.

`knowledge/open_problems.md` is the working list, seeded from the project's
memory and unnumbered.

The paper carries **36 numbered open problems** in `openproblem` environments
across sixteen files --- `op:koide-delta`, `op:up-quark`,
`op:three-dimensions`, `op:vev`, `op:chirality` and the rest. These are the
priced ones: each states what would count as a solution and, often, what has
already been ruled out. They are the best place to start if you want to work
on something.

    grep -rn 'begin{openproblem}' paper1/*.tex paper1/appendices/*.tex

## Asking the framework questions

The repository is meant to be interrogated with an agent --- Claude Code,
Codex, or whatever you use --- and the questions that work are the ones that
say which body of text should answer them.

**"Has this been tried?"** --- `knowledge/invalid_routes.md`, always, before
anything else. It records routes that were tried and failed, with the reason.
Several entries cost weeks. An agent proposing a mechanism here is instructed
to read that file first; hold it to that.

**"What is the evidence for X?"** --- the ledger entry names it, the dated
session note in `knowledge/sessions/` carries the script's exact output, and
`scripts/` has the script. All three should agree. If a claim has no session
note behind it, that itself is the answer.

**"Why isn't X derived?"** --- look for a numbered open problem. The framework
is unusually explicit about its gaps; `sec:koide-gap` in the masses section is
a worked example of a gap being stated in full rather than glossed.

**"What does the framework say about Y?"** --- ask for the paper's claim and
its status label together. An answer that does not say whether the thing is
ESTABLISHED or RHYME has not answered.

**"Where did this idea come from?"** --- the archive, via `INDEX.md`. The
history is genuinely there, from January 2026 onward, including the wrong
turns.

Two things worth asking your agent to do as a matter of course: **say where an
answer came from** --- paper, ledger, session note or archive --- and
**distinguish a claim from a speculation**. The repository contains both in
quantity, and they look alike out of context.

## What it would take to refute this

A fair question, and the paper tries to answer it. `sec:predictions` lists what
is falsifiable and by what: the neutrino ordering that JUNO will measure, the
absence of a fourth generation at any collider, the sterile states near
3.6 TeV, the null predictions. The framework's own stated position is that the
open problems are a feature and the exposure is the point.

The honest gaps are equally findable. The up quark misses by 29 per cent and
says so. The Koide phase is matched rather than derived and says so, at
length. `knowledge/invalid_routes.md` is a list of the author's own failures,
kept deliberately.

## Practical notes

- Builds are `latexmk`. Two at once corrupt each other's `.aux`, so check
  `pgrep -af latexmk` if you share the machine.
- A build is clean only if `grep -E '^!' paper1/main.log` returns nothing.
- `paper1/references.bib` is generated from the maintainer's Zotero library and
  cannot be regenerated by anyone else; `CONTRIBUTING.md` explains what to do
  when you need a new reference.
- Scripts are seed-locked and use Cayley-Dickson Convention A, so they give the
  same numbers on your machine as on the author's. If one does not, that is a
  finding --- say so.
