# Persistent file storage in Claude Code

- conversation uuid: `386a4d7d-0832-4837-b9c4-1d9b62043eb9`
- created: 2026-09-08T04:49:09.945113Z  |  updated: 2026-09-08T18:46:03.274417Z
- messages: 28  |  keyword score: 2

## Summary (from the Claude export)

**Conversation overview**

The person is working on a long-term physics paper project called "negative probability" (repo: self-ref-2026, paper titled "It from Bit via Gödel") that involves LaTeX, Python scripts, BibTeX/RIS references, and a multi-paper series. They currently use Claude web projects with GitHub sync for persistent knowledge, and the conversation began by exploring how to replicate that persistent knowledge base in Claude Code. Claude explained Claude Code's CLAUDE.md import system, `.claude/rules/` path-scoped rules, and skills directories as the equivalent of project knowledge files, with auto memory for session-level residue. The recommended migration strategy was to export accumulated project knowledge (results ledger, invalid routes, open problems, principles, literature anchors, people) into a `knowledge/` directory in the repo, keep CLAUDE.md as a short behaviour contract with `@imports` for always-needed files, and use skills for procedural knowledge like sentinel-gated patch scripts and RIS batch rules.

The conversation then shifted to local LaTeX tooling. The person uses Neovim and wants citation autocompletion equivalent to Overleaf's `\autocite` reference picker. Claude recommended VimTeX combined with either nvim-cmp and the cmp-vimtex source (which shows author/title/year in popups, not just keys) or the texlab LSP, with a note to configure latexmk with biber to match the existing compile chain. The person's citation key convention (author+year+keyword) was noted as well-suited to prefix matching.

The final topic was replacing Overleaf's Mendeley connector when working locally. Claude outlined three options: scripting the Mendeley web API directly (single paginated GET returning BibTeX natively, ~40 lines in Python or Elixir/Req, storing the refresh token in keychain), manual export, or migrating to Zotero with Better BibTeX for automatic `.bib` re-export on collection change. The person's stated blocker for switching to Zotero — inability to transfer saved PDFs — was addressed: Zotero's built-in Mendeley online importer (File → Import → Mendeley Reference Manager online) pulls PDFs and annotations via the API without any export step, and is idempotent for incremental imports. The key caveat is that Mendeley group libraries must be copied to personal library folders before import. Finally, the person asked about scripting a workflow to build a Zotero collection from only the references actually cited in the paper; Claude described Better BibTeX's built-in AUX scanner (right-click collection → Scan AUX file) as the no-script solution, and outlined a ~30-line Python script using BBT's local JSON-RPC endpoint and the Zotero web API for unattended use from a `make bib` target.

## Transcript

### 1. human  ·  2026-09-08 04:49:13

When I'm using Claude web I can keep files in projects that any conversation in that project can refer to. But when I'm using Claude Code I don't have that feature. How can I build that feature into Claude Code

When I'm using Claude web I can keep files in projects that any conversation in that project can refer to. But when I'm using Claude Code I don't have that feature. How can I build that feature into Claude Code

### 2. assistant  ·  2026-09-08 04:49:41


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good news: the building blocks are already in Claude Code, you just have to wire them up. Claude Code has two persistent mechanisms: CLAUDE.md files: instructions you write to give Claude persistent context; Auto memory: notes Claude writes itself based on your corrections and preferences. The equivalent of a project's knowledge folder is a directory of markdown files in the repo, pulled in through one of three loading strategies depending on how often each file matters.

**1. Always-loaded reference (closest to project knowledge).** Put your reference docs in the repo and import them from `CLAUDE.md`. CLAUDE.md files can import additional files using `@path/to/import` syntax. Imported files are expanded and loaded into context at launch alongside the CLAUDE.md that references them.

```
my_app/
├── CLAUDE.md
└── docs/claude/
    ├── architecture.md
    ├── domain-glossary.md
    └── decisions.md
```

```markdown
# CLAUDE.md
Phoenix 1.8 / LiveView app. Run `mix test` before reporting done.

@docs/claude/architecture.md
@docs/claude/domain-glossary.md
@docs/claude/decisions.md
```

Imports nest up to four hops, so `decisions.md` can itself import per-ADR files. The catch: everything imported costs tokens every session, so keep this tier for things you'd genuinely re-explain every time.

**2. Load-on-relevance.** For material that only matters in part of the codebase, use `.claude/rules/` with path scoping. Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns. So `.claude/rules/liveview.md` with `paths: ["lib/my_app_web/live/**"]` loads only when Claude touches LiveView code. Nested `CLAUDE.md` files in subdirectories behave the same way — loaded when Claude reads files there.

**3. Load-on-demand.** For big reference material (API docs, a spec, a playbook), make it a skill in `.claude/skills/<name>/SKILL.md`. For task-specific instructions that don't need to be in context all the time, use skills instead, which only load when you invoke them or when Claude determines they're relevant to your prompt. That's the closest analogue to Claude web deciding to consult a project file when the question calls for it.

**Sharing across repos.** If you want one knowledge base feeding several projects (your EMFA/ExSlt/FutureSync cluster, say), keep it in a shared directory and either import it with `@~/.claude/knowledge/elixir-conventions.md` or symlink it in: The `.claude/rules/` directory supports symlinks, so you can maintain a shared set of rules and link them into multiple projects. Note that external imports from a project-level file trigger a one-time approval dialog.

**Auto memory is the other half.** Claude Code also keeps its own notes per repo: Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`. The `<project>` path is derived from the git repository, so all worktrees and subdirectories within the same repo share one auto memory directory. Saying "remember that…" in a session writes there. It's machine-local though, so anything the team or your other machines need belongs in the committed files above.

Practical starting point: run `/init` to seed a `CLAUDE.md`, move your existing Confluence-style project overviews into `docs/claude/`, import the two or three that matter every session, and push the rest into skills. Run `/context` to confirm what actually loaded.

*[tool_use: view]*

*[tool_result: view]*

*[tool_use: web_fetch]*

*[tool_result: web_fetch]*

*[tool_use: web_search]*

*[tool_result: web_search]*

*[tool_use: web_fetch]*

*[tool_result: web_fetch]*

Good news: the building blocks are already in Claude Code, you just have to wire them up. Claude Code has two persistent mechanisms: CLAUDE.md files: instructions you write to give Claude persistent context; Auto memory: notes Claude writes itself based on your corrections and preferences. The equivalent of a project's knowledge folder is a directory of markdown files in the repo, pulled in through one of three loading strategies depending on how often each file matters.

**1. Always-loaded reference (closest to project knowledge).** Put your reference docs in the repo and import them from `CLAUDE.md`. CLAUDE.md files can import additional files using `@path/to/import` syntax. Imported files are expanded and loaded into context at launch alongside the CLAUDE.md that references them.

```
my_app/
├── CLAUDE.md
└── docs/claude/
    ├── architecture.md
    ├── domain-glossary.md
    └── decisions.md
```

```markdown
# CLAUDE.md
Phoenix 1.8 / LiveView app. Run `mix test` before reporting done.

@docs/claude/architecture.md
@docs/claude/domain-glossary.md
@docs/claude/decisions.md
```

Imports nest up to four hops, so `decisions.md` can itself import per-ADR files. The catch: everything imported costs tokens every session, so keep this tier for things you'd genuinely re-explain every time.

**2. Load-on-relevance.** For material that only matters in part of the codebase, use `.claude/rules/` with path scoping. Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns. So `.claude/rules/liveview.md` with `paths: ["lib/my_app_web/live/**"]` loads only when Claude touches LiveView code. Nested `CLAUDE.md` files in subdirectories behave the same way — loaded when Claude reads files there.

**3. Load-on-demand.** For big reference material (API docs, a spec, a playbook), make it a skill in `.claude/skills/<name>/SKILL.md`. For task-specific instructions that don't need to be in context all the time, use skills instead, which only load when you invoke them or when Claude determines they're relevant to your prompt. That's the closest analogue to Claude web deciding to consult a project file when the question calls for it.

**Sharing across repos.** If you want one knowledge base feeding several projects (your EMFA/ExSlt/FutureSync cluster, say), keep it in a shared directory and either import it with `@~/.claude/knowledge/elixir-conventions.md` or symlink it in: The `.claude/rules/` directory supports symlinks, so you can maintain a shared set of rules and link them into multiple projects. Note that external imports from a project-level file trigger a one-time approval dialog.

**Auto memory is the other half.** Claude Code also keeps its own notes per repo: Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`. The `<project>` path is derived from the git repository, so all worktrees and subdirectories within the same repo share one auto memory directory. Saying "remember that…" in a session writes there. It's machine-local though, so anything the team or your other machines need belongs in the committed files above.

Practical starting point: run `/init` to seed a `CLAUDE.md`, move your existing Confluence-style project overviews into `docs/claude/`, import the two or three that matter every session, and push the rest into skills. Run `/context` to confirm what actually loaded.

### 3. human  ·  2026-09-08 04:57:17

My the biggest use of project files is the negative probability project where I keep a lot of project knowledge we've accumulated over months. Because this relates to work on a physics paper written in Latex and the conversation gives me Python files to update certain sections, which involves checking out the project to local files, running the Python scripts, then committing the code, then re-synchonsing the GitHub repo in the project documents. Each change has lots of manual steps. So I want to switch to running in Claude Code, but then I'd lose the project documents. They are a long term knowledge base

My the biggest use of project files is the negative probability project where I keep a lot of project knowledge we've accumulated over months. Because this relates to work on a physics paper written in Latex and the conversation gives me Python files to update certain sections, which involves checking out the project to local files, running the Python scripts, then committing the code, then re-synchonsing the GitHub repo in the project documents. Each change has lots of manual steps. So I want to switch to running in Claude Code, but then I'd lose the project documents. They are a long term knowledge base

### 4. assistant  ·  2026-09-08 04:58:04


```
This block is not supported on your current device yet.
```

This one is actually the ideal candidate, because of a detail in how you've set it up: the project knowledge panel for self-ref-2026 is a GitHub sync of the repo. In Claude Code the repo *is* the working directory, so the "check out → run script → commit → re-sync" loop collapses to "Claude edits, compiles, commits". The sync step disappears rather than needing to be rebuilt. The only thing you'd lose is the knowledge that lives in the Claude.ai project but *not* in the repo — the accumulated ledger of results, invalid routes, status conventions, literature anchors. So the migration is really: get that material into the repo as markdown, then tell Claude Code how to load it.

**Step 1 — export the non-repo knowledge into the repo.** In the Claude web project, ask Claude to write out everything it holds about the project as markdown files (project instructions, the accumulated summaries, anything in the knowledge panel that isn't a synced repo file). Commit them under something like:

```
self-ref-2026/
├── CLAUDE.md
├── knowledge/
│   ├── results_ledger.md        # ESTABLISHED/STRUCTURAL/CANDIDATE… claims
│   ├── invalid_routes.md        # geodesic quark mass, GHZ–W superposition, Fano counting…
│   ├── open_problems.md         # op:p2-newton, op:baryon-contact, op:up-quark…
│   ├── principles.md            # FANOUT boundary, mass = associator debt / norm defect
│   ├── literature.md            # anchors + VERIFY-CITE status
│   └── people.md                # Dowker, Khrennikov, Abramsky correspondence…
├── .claude/
│   ├── rules/
│   └── skills/
└── main.tex, sections/, scripts/, ris/, attic_* …
```

That's a better home for it anyway: it's versioned, greppable, and readable by you, Overleaf collaborators, and the Claude web project (which will pick it up on the next sync — so nothing stops you using both).

**Step 2 — CLAUDE.md is the behaviour contract, not the encyclopaedia.** Keep it short and put your working disciplines there, since these are the things Claude must hold every session:

```markdown
# self-ref-2026 — "It from Bit via Gödel"

Multi-paper physics series. John drives conceptual synthesis; Claude does
mathematical elaboration, critical engagement, literature, document production.

## Non-negotiables
- Every claim carries a status: ESTABLISHED / STRUCTURAL / CANDIDATE / CONJECTURE / RHYME / OPEN. Never upgrade in place.
- Before proposing any mechanism, read @knowledge/invalid_routes.md and do not retry a logged route.
- LaTeX edits are sentinel-gated splices (BEGIN/END). Compile-verify: two passes of
  `pdflatex -interaction=nonstopmode`, then `grep -E '^!' *.log` must be empty.
- Pure ASCII in .tex and .md; native Unicode in .ris. British English, paragraphs not bullets, \autocite.
- Never delete: rename to attic_<name>.superseded. Dated filenames description_YYYY-MM-DDTHHMM.
- Python: fixed seed, Convention A Cayley-Dickson. Run the script and paste exact stdout into the session notes.

## Where things live
@knowledge/results_ledger.md
@knowledge/open_problems.md
Consult knowledge/principles.md, knowledge/literature.md, knowledge/people.md on demand.
```

Import only the two or three files that matter in every session; the rest Claude reads with its file tools when the task calls for it, and you can nudge it with a line like "consult X before Y".

**Step 3 — turn the repeated procedures into skills.** The patch-script pattern (assert anchors whitespace-insensitively, write `.bak`, add `EDITED` header, refuse to run twice), the RIS batch rules (one `AU` per author, citation key in `ID`, DOI only when deterministic), and the sedenion computation conventions are exactly what `.claude/skills/<name>/SKILL.md` is for: they load only when relevant, so they don't cost context on a session about Paper 2's Newtonian limit. This is the closest thing to the way Claude web decides to consult a project file.

**Step 4 — enforce the compile check with a hook rather than trusting the instruction.** A `PostToolUse` hook on edits to `*.tex` that runs the two-pass pdflatex and fails on any `^!` line makes "zero errors before delivery" mechanical instead of behavioural. Same idea for a `PreToolUse` deny on `rm` of anything matching `*.tex|*.md|*.ris`, given your attic-never-delete rule.

**Step 5 — let auto memory handle the session-level residue.** Claude Code keeps per-repo notes in `~/.claude/projects/<repo>/memory/` for corrections and preferences it picks up. Fine for "John prefers X", but anything that's a *result* — a resolved prediction, a retracted route, a new fossil flagged — should go into `knowledge/` and be committed, otherwise it's stuck on one machine.

**What the new loop looks like.** "Patch the up-quark paragraph to remove the GHZ–W fossil" becomes: Claude reads `invalid_routes.md`, writes the sentinel-gated patch script, runs it, compiles, greps the log, shows you the diff, and commits with a dated message once you approve. The unechoed `sedenion_zero_divisor_scan_2026-08-31.py` would just get run, with stdout captured into a dated session-notes file. Your independent re-run for reproduction verification still works exactly as before — it's the same repo.

One thing to decide up front: whether to keep the Claude web project alive for the pure-thinking sessions (Khrennikov email, complementarity reframe) where a terminal is the wrong medium. If the knowledge lives in the repo and the project syncs from GitHub, running both costs you nothing beyond hitting the sync button after Claude Code commits.

*[tool_use: memory_read]*

*[tool_result: memory_read]*

This one is actually the ideal candidate, because of a detail in how you've set it up: the project knowledge panel for self-ref-2026 is a GitHub sync of the repo. In Claude Code the repo *is* the working directory, so the "check out → run script → commit → re-sync" loop collapses to "Claude edits, compiles, commits". The sync step disappears rather than needing to be rebuilt. The only thing you'd lose is the knowledge that lives in the Claude.ai project but *not* in the repo — the accumulated ledger of results, invalid routes, status conventions, literature anchors. So the migration is really: get that material into the repo as markdown, then tell Claude Code how to load it.

**Step 1 — export the non-repo knowledge into the repo.** In the Claude web project, ask Claude to write out everything it holds about the project as markdown files (project instructions, the accumulated summaries, anything in the knowledge panel that isn't a synced repo file). Commit them under something like:

```
self-ref-2026/
├── CLAUDE.md
├── knowledge/
│   ├── results_ledger.md        # ESTABLISHED/STRUCTURAL/CANDIDATE… claims
│   ├── invalid_routes.md        # geodesic quark mass, GHZ–W superposition, Fano counting…
│   ├── open_problems.md         # op:p2-newton, op:baryon-contact, op:up-quark…
│   ├── principles.md            # FANOUT boundary, mass = associator debt / norm defect
│   ├── literature.md            # anchors + VERIFY-CITE status
│   └── people.md                # Dowker, Khrennikov, Abramsky correspondence…
├── .claude/
│   ├── rules/
│   └── skills/
└── main.tex, sections/, scripts/, ris/, attic_* …
```

That's a better home for it anyway: it's versioned, greppable, and readable by you, Overleaf collaborators, and the Claude web project (which will pick it up on the next sync — so nothing stops you using both).

**Step 2 — CLAUDE.md is the behaviour contract, not the encyclopaedia.** Keep it short and put your working disciplines there, since these are the things Claude must hold every session:

```markdown
# self-ref-2026 — "It from Bit via Gödel"

Multi-paper physics series. John drives conceptual synthesis; Claude does
mathematical elaboration, critical engagement, literature, document production.

## Non-negotiables
- Every claim carries a status: ESTABLISHED / STRUCTURAL / CANDIDATE / CONJECTURE / RHYME / OPEN. Never upgrade in place.
- Before proposing any mechanism, read @knowledge/invalid_routes.md and do not retry a logged route.
- LaTeX edits are sentinel-gated splices (BEGIN/END). Compile-verify: two passes of
  `pdflatex -interaction=nonstopmode`, then `grep -E '^!' *.log` must be empty.
- Pure ASCII in .tex and .md; native Unicode in .ris. British English, paragraphs not bullets, \autocite.
- Never delete: rename to attic_<name>.superseded. Dated filenames description_YYYY-MM-DDTHHMM.
- Python: fixed seed, Convention A Cayley-Dickson. Run the script and paste exact stdout into the session notes.

## Where things live
@knowledge/results_ledger.md
@knowledge/open_problems.md
Consult knowledge/principles.md, knowledge/literature.md, knowledge/people.md on demand.
```

Import only the two or three files that matter in every session; the rest Claude reads with its file tools when the task calls for it, and you can nudge it with a line like "consult X before Y".

**Step 3 — turn the repeated procedures into skills.** The patch-script pattern (assert anchors whitespace-insensitively, write `.bak`, add `EDITED` header, refuse to run twice), the RIS batch rules (one `AU` per author, citation key in `ID`, DOI only when deterministic), and the sedenion computation conventions are exactly what `.claude/skills/<name>/SKILL.md` is for: they load only when relevant, so they don't cost context on a session about Paper 2's Newtonian limit. This is the closest thing to the way Claude web decides to consult a project file.

**Step 4 — enforce the compile check with a hook rather than trusting the instruction.** A `PostToolUse` hook on edits to `*.tex` that runs the two-pass pdflatex and fails on any `^!` line makes "zero errors before delivery" mechanical instead of behavioural. Same idea for a `PreToolUse` deny on `rm` of anything matching `*.tex|*.md|*.ris`, given your attic-never-delete rule.

**Step 5 — let auto memory handle the session-level residue.** Claude Code keeps per-repo notes in `~/.claude/projects/<repo>/memory/` for corrections and preferences it picks up. Fine for "John prefers X", but anything that's a *result* — a resolved prediction, a retracted route, a new fossil flagged — should go into `knowledge/` and be committed, otherwise it's stuck on one machine.

**What the new loop looks like.** "Patch the up-quark paragraph to remove the GHZ–W fossil" becomes: Claude reads `invalid_routes.md`, writes the sentinel-gated patch script, runs it, compiles, greps the log, shows you the diff, and commits with a dated message once you approve. The unechoed `sedenion_zero_divisor_scan_2026-08-31.py` would just get run, with stdout captured into a dated session-notes file. Your independent re-run for reproduction verification still works exactly as before — it's the same repo.

One thing to decide up front: whether to keep the Claude web project alive for the pure-thinking sessions (Khrennikov email, complementarity reframe) where a terminal is the wrong medium. If the knowledge lives in the repo and the project syncs from GitHub, running both costs you nothing beyond hitting the sync button after Claude Code commits.

### 5. human  ·  2026-09-08 05:03:48

I can edit files locally using Neovim, and set up a standard compile chain. But one feature from overleaf that I'd really miss is when I want to `\autocite` a references, the Overleaf editor presents a list of possible references based on the first few characters I've typed. How can I do this in Neovim. Is there a package in Neovim for working with `*.tex` files that already does this?

I can edit files locally using Neovim, and set up a standard compile chain. But one feature from overleaf that I'd really miss is when I want to `\autocite` a references, the Overleaf editor presents a list of possible references based on the first few characters I've typed. How can I do this in Neovim. Is there a package in Neovim for working with `*.tex` files that already does this?

### 6. assistant  ·  2026-09-08 05:04:07

Yes — this is a solved problem in Neovim, and you have two good routes. Both parse your `.bib` file (found via `\addbibresource{...}` / `\bibliography{...}`) and pop up matching keys as you type inside `\autocite{`.

**Route 1: VimTeX + a completion engine (the classic setup).** [VimTeX](https://github.com/lervag/vimtex) is the standard `.tex` plugin — syntax, folding, compile-on-save via latexmk, forward/inverse search with a PDF viewer, and an omni-completion source that knows about citations, labels, and commands. On its own you'd trigger it with `<C-x><C-o>`; to get Overleaf-style automatic popups, wire it into a completion engine:

- With **nvim-cmp**: add [cmp-vimtex](https://github.com/micangl/cmp-vimtex), which is purpose-built for this and shows author/title/year in the popup, not just the key.
- With **blink.cmp** (the newer, faster alternative): use its omni source with VimTeX's omnifunc, or the `blink-cmp-vimtex` community source.

Minimal lazy.nvim sketch with nvim-cmp:

```lua
{ "lervag/vimtex", init = function()
    vim.g.vimtex_view_method = "skim"   -- or "zathura" / "sioyek"
    vim.g.vimtex_compiler_method = "latexmk"
end },
{ "hrsh7th/nvim-cmp", dependencies = { "micangl/cmp-vimtex" },
  config = function()
    require("cmp").setup({ sources = { { name = "vimtex" }, { name = "buffer" } } })
  end },
```

Type `\autocite{abra` and the popup filters keys by prefix (and, with cmp-vimtex, fuzzy-matches on author/title too, which is nicer than Overleaf).

**Route 2: texlab LSP.** [texlab](https://github.com/latex-lsp/texlab) is a LaTeX language server; install it via Mason or Homebrew and enable it with `vim.lsp.enable("texlab")` (Neovim 0.11+) or lspconfig. You then get citation and label completion through whatever LSP completion you already use, plus diagnostics, go-to-definition on labels, and a build command. It's the lower-config option if you already have LSP set up for Elixir.

The two combine well: VimTeX for editing ergonomics and compilation, texlab for completion and diagnostics. Most people run both.

Two things specific to your setup worth noting: your bib key convention (`author+year+keyword`) prefix-matches cleanly, so typing the author surname will narrow the list fast. And since your `.bib` comes out of Mendeley, point `latexmk` at biber (`$biber = 'biber %O %S'` in `.latexmkrc`, or `vim.g.vimtex_compiler_latexmk_engines`) so the VimTeX compile matches your Overleaf chain — VimTeX defaults to `-pdf` with bibtex otherwise.

Yes — this is a solved problem in Neovim, and you have two good routes. Both parse your `.bib` file (found via `\addbibresource{...}` / `\bibliography{...}`) and pop up matching keys as you type inside `\autocite{`.

**Route 1: VimTeX + a completion engine (the classic setup).** [VimTeX](https://github.com/lervag/vimtex) is the standard `.tex` plugin — syntax, folding, compile-on-save via latexmk, forward/inverse search with a PDF viewer, and an omni-completion source that knows about citations, labels, and commands. On its own you'd trigger it with `<C-x><C-o>`; to get Overleaf-style automatic popups, wire it into a completion engine:

- With **nvim-cmp**: add [cmp-vimtex](https://github.com/micangl/cmp-vimtex), which is purpose-built for this and shows author/title/year in the popup, not just the key.
- With **blink.cmp** (the newer, faster alternative): use its omni source with VimTeX's omnifunc, or the `blink-cmp-vimtex` community source.

Minimal lazy.nvim sketch with nvim-cmp:

```lua
{ "lervag/vimtex", init = function()
    vim.g.vimtex_view_method = "skim"   -- or "zathura" / "sioyek"
    vim.g.vimtex_compiler_method = "latexmk"
end },
{ "hrsh7th/nvim-cmp", dependencies = { "micangl/cmp-vimtex" },
  config = function()
    require("cmp").setup({ sources = { { name = "vimtex" }, { name = "buffer" } } })
  end },
```

Type `\autocite{abra` and the popup filters keys by prefix (and, with cmp-vimtex, fuzzy-matches on author/title too, which is nicer than Overleaf).

**Route 2: texlab LSP.** [texlab](https://github.com/latex-lsp/texlab) is a LaTeX language server; install it via Mason or Homebrew and enable it with `vim.lsp.enable("texlab")` (Neovim 0.11+) or lspconfig. You then get citation and label completion through whatever LSP completion you already use, plus diagnostics, go-to-definition on labels, and a build command. It's the lower-config option if you already have LSP set up for Elixir.

The two combine well: VimTeX for editing ergonomics and compilation, texlab for completion and diagnostics. Most people run both.

Two things specific to your setup worth noting: your bib key convention (`author+year+keyword`) prefix-matches cleanly, so typing the author surname will narrow the list fast. And since your `.bib` comes out of Mendeley, point `latexmk` at biber (`$biber = 'biber %O %S'` in `.latexmkrc`, or `vim.g.vimtex_compiler_latexmk_engines`) so the VimTeX compile matches your Overleaf chain — VimTeX defaults to `-pdf` with bibtex otherwise.

### 7. human  ·  2026-09-08 05:09:15

Overleaf has a connector to Mendeley that pulls references from Mendeley groups into the local `bib` file. How would I do that if I skipped Overleaf and just ran locally?

Overleaf has a connector to Mendeley that pulls references from Mendeley groups into the local `bib` file. How would I do that if I skipped Overleaf and just ran locally?

### 8. assistant  ·  2026-09-08 05:09:43


```
This block is not supported on your current device yet.
```

Overleaf's connector talks to the Mendeley web API, and the current Mendeley Reference Manager desktop app dropped the old "BibTeX syncing" feature that Mendeley Desktop had — Mendeley no longer integrates automatically with LaTeX; you can export a BibTeX file, but it's standalone and won't update automatically. So you have three realistic ways to get the equivalent locally.

**1. Script the Mendeley API yourself (closest to what Overleaf does).** Register an app at dev.mendeley.com, do the OAuth dance once to get a refresh token, then hit `GET https://api.mendeley.com/documents?group_id=<id>&limit=500&view=bib` with the header `Accept: application/x-bibtex`. The API returns BibTeX directly, using each record's stored citation key — so the `author+year+keyword` keys you carry in the RIS `ID` field come through intact. Wrap that in a 40-line script (Python, or an Elixir script using Req — it's a single paginated GET) that writes `references.bib`, and call it from a `make bib` target or a Claude Code hook so the file refreshes before each compile. The one wrinkle is the token refresh; store the refresh token in your keychain and let the script exchange it.

**2. Manual export per group.** In Mendeley Reference Manager, open the group, select all, export as BibTeX, overwrite `references.bib`. Zero setup, but it's exactly the kind of manual step you're trying to eliminate, and easy to forget after a RIS import.

**3. Move the bibliography to Zotero with Better BibTeX.** This is what most people running a local LaTeX toolchain settle on. Better BibTeX watches a collection and re-exports the `.bib` file automatically whenever anything changes — a true replacement for the Mendeley Desktop sync of old, with no script and no API. Zotero imports RIS natively, so your existing dated RIS batches drop in unchanged, and BBT lets you pin a citation key per item (via `Citation Key: xxx` in the Extra field) so your keys stay stable through the migration. The cost is a one-off migration of the library and a change to your "Mendeley import with dedupe" habit; Zotero's duplicate detection is at least as good.

If you want to keep Mendeley, do (1) — it's an afternoon's work and slots straight into the CLAUDE.md/hook setup we discussed. If you're open to changing the reference manager, (3) is the lower-maintenance end state and the one that plays best with VimTeX/texlab completion, since the `.bib` is always current.

*[tool_use: web_search]*

*[tool_result: web_search]*

Overleaf's connector talks to the Mendeley web API, and the current Mendeley Reference Manager desktop app dropped the old "BibTeX syncing" feature that Mendeley Desktop had — Mendeley no longer integrates automatically with LaTeX; you can export a BibTeX file, but it's standalone and won't update automatically. So you have three realistic ways to get the equivalent locally.

**1. Script the Mendeley API yourself (closest to what Overleaf does).** Register an app at dev.mendeley.com, do the OAuth dance once to get a refresh token, then hit `GET https://api.mendeley.com/documents?group_id=<id>&limit=500&view=bib` with the header `Accept: application/x-bibtex`. The API returns BibTeX directly, using each record's stored citation key — so the `author+year+keyword` keys you carry in the RIS `ID` field come through intact. Wrap that in a 40-line script (Python, or an Elixir script using Req — it's a single paginated GET) that writes `references.bib`, and call it from a `make bib` target or a Claude Code hook so the file refreshes before each compile. The one wrinkle is the token refresh; store the refresh token in your keychain and let the script exchange it.

**2. Manual export per group.** In Mendeley Reference Manager, open the group, select all, export as BibTeX, overwrite `references.bib`. Zero setup, but it's exactly the kind of manual step you're trying to eliminate, and easy to forget after a RIS import.

**3. Move the bibliography to Zotero with Better BibTeX.** This is what most people running a local LaTeX toolchain settle on. Better BibTeX watches a collection and re-exports the `.bib` file automatically whenever anything changes — a true replacement for the Mendeley Desktop sync of old, with no script and no API. Zotero imports RIS natively, so your existing dated RIS batches drop in unchanged, and BBT lets you pin a citation key per item (via `Citation Key: xxx` in the Extra field) so your keys stay stable through the migration. The cost is a one-off migration of the library and a change to your "Mendeley import with dedupe" habit; Zotero's duplicate detection is at least as good.

If you want to keep Mendeley, do (1) — it's an afternoon's work and slots straight into the CLAUDE.md/hook setup we discussed. If you're open to changing the reference manager, (3) is the lower-maintenance end state and the one that plays best with VimTeX/texlab completion, since the `.bib` is always current.

### 9. human  ·  2026-09-08 05:12:53

The problem that has stopped me switching to Zotero is that I can't export saved pdfs of papers and reimport them into Zotero

The problem that has stopped me switching to Zotero is that I can't export saved pdfs of papers and reimport them into Zotero

### 10. assistant  ·  2026-09-08 05:13:09


```
This block is not supported on your current device yet.
```

That obstacle has actually been removed. Zotero has a built-in Mendeley importer that doesn't go through RIS/BibTeX at all — it talks to Mendeley's web API and pulls the PDFs down with the records. Go to File → Import within Zotero and choose the "Mendeley Reference Manager (online import)" option. You'll be asked to log in to Mendeley to allow Zotero to perform the import. If you use Mendeley Reference Manager, your data and files are already all online, so there's nothing to export first. It brings across folders as collections, attached PDFs, and the highlight and note annotations inside the PDFs, which Zotero's own reader can display. It's also idempotent: The importer is compatible with the existing local importer, so if you've added items to Mendeley since a previous import, you can import again using either tool and new items will be imported without duplicating existing items — so you can migrate in stages rather than in one nervous afternoon.

The manual RIS/BibTeX route you were presumably trying is exactly the one that loses attachments; that's the export path, not the importer.

Two caveats worth knowing before you start:

Group libraries aren't imported directly. It's not possible to directly import group libraries. To import items in group libraries, copy the group items to a collection in your Mendeley library before importing. You can then create a Zotero group and drag imported collections or items to that group. Since your references live in Mendeley groups (that's what the Overleaf connector was reading), this is a step you'll definitely hit — copy each group into a folder in your personal library first.

Completeness depends on Mendeley's own sync. Some users have reported a few PDFs or annotations missing after import where their Mendeley web library hadn't fully synced them, so check the count of items-with-attachments in Zotero against Mendeley after the run, and re-run the import if anything's short — re-runs don't duplicate.

For your citation keys: Better BibTeX honours a `Citation Key: <key>` line in each item's Extra field. Mendeley's importer won't populate that automatically, so once the import is done, a one-off script over the Zotero library (or BBT's own bulk "pin key" using a formula that reproduces `author+year+keyword` for the bulk of them, with manual fixes for the keyword part) will get your existing `\autocite` keys matching. Do that before switching `references.bib` over and your `.tex` files won't need touching.

*[tool_use: web_search]*

*[tool_result: web_search]*

That obstacle has actually been removed. Zotero has a built-in Mendeley importer that doesn't go through RIS/BibTeX at all — it talks to Mendeley's web API and pulls the PDFs down with the records. Go to File → Import within Zotero and choose the "Mendeley Reference Manager (online import)" option. You'll be asked to log in to Mendeley to allow Zotero to perform the import. If you use Mendeley Reference Manager, your data and files are already all online, so there's nothing to export first. It brings across folders as collections, attached PDFs, and the highlight and note annotations inside the PDFs, which Zotero's own reader can display. It's also idempotent: The importer is compatible with the existing local importer, so if you've added items to Mendeley since a previous import, you can import again using either tool and new items will be imported without duplicating existing items — so you can migrate in stages rather than in one nervous afternoon.

The manual RIS/BibTeX route you were presumably trying is exactly the one that loses attachments; that's the export path, not the importer.

Two caveats worth knowing before you start:

Group libraries aren't imported directly. It's not possible to directly import group libraries. To import items in group libraries, copy the group items to a collection in your Mendeley library before importing. You can then create a Zotero group and drag imported collections or items to that group. Since your references live in Mendeley groups (that's what the Overleaf connector was reading), this is a step you'll definitely hit — copy each group into a folder in your personal library first.

Completeness depends on Mendeley's own sync. Some users have reported a few PDFs or annotations missing after import where their Mendeley web library hadn't fully synced them, so check the count of items-with-attachments in Zotero against Mendeley after the run, and re-run the import if anything's short — re-runs don't duplicate.

For your citation keys: Better BibTeX honours a `Citation Key: <key>` line in each item's Extra field. Mendeley's importer won't populate that automatically, so once the import is done, a one-off script over the Zotero library (or BBT's own bulk "pin key" using a formula that reproduces `author+year+keyword` for the bulk of them, with manual fixes for the keyword part) will get your existing `\autocite` keys matching. Do that before switching `references.bib` over and your `.tex` files won't need touching.

### 11. human  ·  2026-09-08 05:15:43

Can I create a script to read the actual references I use in the paper and create a Zotero group from those

Can I create a script to read the actual references I use in the paper and create a Zotero group from those

### 12. assistant  ·  2026-09-08 05:16:09

Yes, and Better BibTeX already has most of it built in, so you may not need to write anything.

**The no-script route: BBT's AUX scanner.** Compile the paper once, then in Zotero right-click a collection → *Scan AUX file…* and point it at `main.aux`. BBT reads every cited key (it understands both BibTeX's `\citation{}` lines and biblatex's `\abx@aux@cite{}`), finds the matching items by citation key, and adds them to that collection. It reports any keys it can't resolve, which doubles as a check that your key pinning after the Mendeley import worked. This is precisely "the references I actually use", derived from the compiled document rather than a grep, so it also handles keys cited only via `\nocite` or inside `\input` files.

Then set that collection as a BBT auto-export target (right-click → *Export Collection…*, tick *Keep updated*), pointing at `references.bib` in the repo. From then on the `.bib` regenerates itself whenever the collection changes — the Mendeley/Overleaf loop replaced by a watched folder.

**Group vs collection.** A Zotero *collection* in My Library is what you want for a solo paper; it's what auto-export watches and what the AUX scanner targets. A Zotero *group* is a shared library you'd create on zotero.org if Fay or Andrei need to see it — you can't create groups via the API, only through the website, but once one exists you drag the collection into it.

**If you do want a script** (e.g. to run it from Claude Code after each compile), the pieces are:

1. Get the cited keys. Cleanest is from biber's control file: `xmllint --xpath '//bcf:citekey/text()' main.bcf`, or `grep -o '\\abx@aux@cite{[^}]*}' main.aux`. Falling back to `grep -oh '\\autocite\[[^]]*\]\?{[^}]*}' *.tex` works but misses `\nocite` and multi-key cites unless you split on commas.
2. Resolve keys to Zotero items via BBT's local JSON-RPC endpoint at `http://localhost:23119/better-bibtex/json-rpc` — the `item.search` / `item.citationkey` methods take keys and return item IDs; `collection.scanAUX(collection, auxPath)` exposes the scanner above directly, so a script can just call that.
3. Add items to a collection with the Zotero Web API (`POST /users/<id>/items/<key>` with a `collections` array, or one `PATCH` per item), authenticated with an API key from zotero.org settings. Zotero 7's local API on the same port is read-only, so writes go through the web API and sync back.

A ~30-line Python script with `requests` covers 1–3; the only thing it adds over the right-click is that it can run unattended from a `make bib` target. I'd start with the built-in scanner and only script it if the manual step turns out to be the one you keep forgetting.

Yes, and Better BibTeX already has most of it built in, so you may not need to write anything.

**The no-script route: BBT's AUX scanner.** Compile the paper once, then in Zotero right-click a collection → *Scan AUX file…* and point it at `main.aux`. BBT reads every cited key (it understands both BibTeX's `\citation{}` lines and biblatex's `\abx@aux@cite{}`), finds the matching items by citation key, and adds them to that collection. It reports any keys it can't resolve, which doubles as a check that your key pinning after the Mendeley import worked. This is precisely "the references I actually use", derived from the compiled document rather than a grep, so it also handles keys cited only via `\nocite` or inside `\input` files.

Then set that collection as a BBT auto-export target (right-click → *Export Collection…*, tick *Keep updated*), pointing at `references.bib` in the repo. From then on the `.bib` regenerates itself whenever the collection changes — the Mendeley/Overleaf loop replaced by a watched folder.

**Group vs collection.** A Zotero *collection* in My Library is what you want for a solo paper; it's what auto-export watches and what the AUX scanner targets. A Zotero *group* is a shared library you'd create on zotero.org if Fay or Andrei need to see it — you can't create groups via the API, only through the website, but once one exists you drag the collection into it.

**If you do want a script** (e.g. to run it from Claude Code after each compile), the pieces are:

1. Get the cited keys. Cleanest is from biber's control file: `xmllint --xpath '//bcf:citekey/text()' main.bcf`, or `grep -o '\\abx@aux@cite{[^}]*}' main.aux`. Falling back to `grep -oh '\\autocite\[[^]]*\]\?{[^}]*}' *.tex` works but misses `\nocite` and multi-key cites unless you split on commas.
2. Resolve keys to Zotero items via BBT's local JSON-RPC endpoint at `http://localhost:23119/better-bibtex/json-rpc` — the `item.search` / `item.citationkey` methods take keys and return item IDs; `collection.scanAUX(collection, auxPath)` exposes the scanner above directly, so a script can just call that.
3. Add items to a collection with the Zotero Web API (`POST /users/<id>/items/<key>` with a `collections` array, or one `PATCH` per item), authenticated with an API key from zotero.org settings. Zotero 7's local API on the same port is read-only, so writes go through the web API and sync back.

A ~30-line Python script with `requests` covers 1–3; the only thing it adds over the right-click is that it can run unattended from a `make bib` target. I'd start with the built-in scanner and only script it if the manual step turns out to be the one you keep forgetting.

### 13. human  ·  2026-09-08 05:22:08

Should I use the downloadable desktop version of Zotero or the web version or both?

Should I use the downloadable desktop version of Zotero or the web version or both?

### 14. assistant  ·  2026-09-08 05:22:17

Both, but the desktop app is the one that matters. Everything we've discussed — Better BibTeX, the AUX scanner, auto-export of `references.bib`, the Mendeley online importer, the PDF reader that shows imported annotations — is a desktop-app feature. Plugins don't run in the web library, and the local JSON-RPC endpoint on port 23119 is the desktop app listening.

The web version isn't really a separate product; it's a view of your synced library at zotero.org, useful for three things: reading your library from a machine without Zotero installed, managing groups (creating them, inviting collaborators, which can only be done there), and generating the API key if you script against the Web API. You get it for free by creating a zotero.org account and turning on sync in the desktop app, which you'll want anyway for backup and for the "Add to Zotero" browser connector that pulls a paper straight from arXiv or a journal page into a collection.

Two practical points on sync. Metadata sync is unlimited and free; file storage for attached PDFs is 300 MB on the free tier, which a physics literature library will exceed quickly. Options are paying Zotero for storage (their pricing is modest and funds the project), or setting up WebDAV file sync to your own server — which given your self-hosted infrastructure might appeal, though it's one more thing to maintain. Or just don't sync files at all: the PDFs live on your Mac, metadata syncs everywhere, and you keep Time Machine as the backup. That's the lowest-friction choice for a single-machine LaTeX workflow.

So: install Zotero 7 desktop plus Better BibTeX, create the account, enable data sync, decide on file storage once you see the library size after the Mendeley import.

Both, but the desktop app is the one that matters. Everything we've discussed — Better BibTeX, the AUX scanner, auto-export of `references.bib`, the Mendeley online importer, the PDF reader that shows imported annotations — is a desktop-app feature. Plugins don't run in the web library, and the local JSON-RPC endpoint on port 23119 is the desktop app listening.

The web version isn't really a separate product; it's a view of your synced library at zotero.org, useful for three things: reading your library from a machine without Zotero installed, managing groups (creating them, inviting collaborators, which can only be done there), and generating the API key if you script against the Web API. You get it for free by creating a zotero.org account and turning on sync in the desktop app, which you'll want anyway for backup and for the "Add to Zotero" browser connector that pulls a paper straight from arXiv or a journal page into a collection.

Two practical points on sync. Metadata sync is unlimited and free; file storage for attached PDFs is 300 MB on the free tier, which a physics literature library will exceed quickly. Options are paying Zotero for storage (their pricing is modest and funds the project), or setting up WebDAV file sync to your own server — which given your self-hosted infrastructure might appeal, though it's one more thing to maintain. Or just don't sync files at all: the PDFs live on your Mac, metadata syncs everywhere, and you keep Time Machine as the backup. That's the lowest-friction choice for a single-machine LaTeX workflow.

So: install Zotero 7 desktop plus Better BibTeX, create the account, enable data sync, decide on file storage once you see the library size after the Mendeley import.

### 15. human  ·  2026-09-08 05:24:10

Most of the time I work on this Linux machine, but sometimes I use my Mac. I'm thinking that AWS S3 might be a good place to store the PDFs

Most of the time I work on this Linux machine, but sometimes I use my Mac. I'm thinking that AWS S3 might be a good place to store the PDFs

### 16. assistant  ·  2026-09-08 05:24:31

S3 can work, but not directly — Zotero's file sync only speaks two protocols: Zotero's own storage, or WebDAV. So the question is whether you want to put a WebDAV front on S3 or skip it.

**Option A: Zotero Storage.** Honest answer for a two-machine setup: this is the path of least resistance. Zotero's paid tiers are inexpensive, the sync is designed and tested for exactly this, and both machines just work once you log in. It also funds the project that makes Better BibTeX possible. Check the current prices on zotero.org/storage, but the unlimited tier has historically been in the region of $10/month.

**Option B: S3 behind WebDAV.** If you'd rather own the storage, run a WebDAV server backed by S3 on one of your self-hosted machines. `rclone serve webdav --addr :8080 s3remote:zotero-bucket` is the one-liner version; people do run Zotero against it successfully, but you'd want basic auth and TLS in front (Caddy or nginx), and you'd be relying on a server on your own infrastructure being reachable whenever either machine syncs — which given your IPv6-only setup means both the Linux box and the Mac need a route to it. Zotero has a *Verify Server* button in the sync preferences that tells you quickly whether the WebDAV implementation is compatible. Use a standard S3 storage class, not Glacier; Zotero expects immediate reads. Cost-wise a few GB of PDFs is pennies a month, so the saving over Option A is real but small next to the maintenance.

**What not to do:** point both machines' Zotero data directories, or the `storage/` subfolder, at a shared S3 mount (s3fs, rclone mount, Dropbox-style sync). Zotero's SQLite database and attachment folders are not safe under that kind of concurrent sync and the documentation warns about database corruption. Sync must go through Zotero's own mechanism.

**A middle path worth knowing:** Zotero can use *linked* attachments with a "Linked Attachment Base Directory" set per machine, so the PDFs live outside Zotero's data directory in a folder you sync however you like — including an rclone job to S3 on a schedule. Metadata syncs via zotero.org (free), files travel separately. The catch is that the Mendeley importer creates *stored* attachments, so you'd need a plugin like ZotMoveFile to convert them to linked after import, and you'd be responsible for keeping the folder in step yourself. It's the most S3-native option but the most hand-assembled.

If I were choosing for a paper you're trying to finish: A now, and revisit B if the bill ever annoys you.

S3 can work, but not directly — Zotero's file sync only speaks two protocols: Zotero's own storage, or WebDAV. So the question is whether you want to put a WebDAV front on S3 or skip it.

**Option A: Zotero Storage.** Honest answer for a two-machine setup: this is the path of least resistance. Zotero's paid tiers are inexpensive, the sync is designed and tested for exactly this, and both machines just work once you log in. It also funds the project that makes Better BibTeX possible. Check the current prices on zotero.org/storage, but the unlimited tier has historically been in the region of $10/month.

**Option B: S3 behind WebDAV.** If you'd rather own the storage, run a WebDAV server backed by S3 on one of your self-hosted machines. `rclone serve webdav --addr :8080 s3remote:zotero-bucket` is the one-liner version; people do run Zotero against it successfully, but you'd want basic auth and TLS in front (Caddy or nginx), and you'd be relying on a server on your own infrastructure being reachable whenever either machine syncs — which given your IPv6-only setup means both the Linux box and the Mac need a route to it. Zotero has a *Verify Server* button in the sync preferences that tells you quickly whether the WebDAV implementation is compatible. Use a standard S3 storage class, not Glacier; Zotero expects immediate reads. Cost-wise a few GB of PDFs is pennies a month, so the saving over Option A is real but small next to the maintenance.

**What not to do:** point both machines' Zotero data directories, or the `storage/` subfolder, at a shared S3 mount (s3fs, rclone mount, Dropbox-style sync). Zotero's SQLite database and attachment folders are not safe under that kind of concurrent sync and the documentation warns about database corruption. Sync must go through Zotero's own mechanism.

**A middle path worth knowing:** Zotero can use *linked* attachments with a "Linked Attachment Base Directory" set per machine, so the PDFs live outside Zotero's data directory in a folder you sync however you like — including an rclone job to S3 on a schedule. Metadata syncs via zotero.org (free), files travel separately. The catch is that the Mendeley importer creates *stored* attachments, so you'd need a plugin like ZotMoveFile to convert them to linked after import, and you'd be responsible for keeping the folder in step yourself. It's the most S3-native option but the most hand-assembled.

If I were choosing for a paper you're trying to finish: A now, and revisit B if the bill ever annoys you.

### 17. human  ·  2026-09-08 05:24:43

What is WebDav?

What is WebDav?

### 18. assistant  ·  2026-09-08 05:24:53

WebDAV is HTTP extended into a filesystem protocol. Plain HTTP lets a client GET a resource; WebDAV adds the verbs you'd need to treat a URL tree as a folder you can write to: `PUT` to upload a file, `DELETE`, `MKCOL` to make a directory, `MOVE` and `COPY`, `PROPFIND` to list a directory and read file properties like size and modification time, and `LOCK`/`UNLOCK` for coordinating concurrent edits. The name is "Web Distributed Authoring and Versioning"; it dates from the late 1990s and the spec is RFC 4918.

Because it's just HTTP with extra methods, it runs on port 80/443, goes through proxies and firewalls, works with ordinary TLS certificates, and uses ordinary HTTP authentication. That's why it became the lowest-common-denominator way for applications to talk to "some remote folder" without caring what's behind it. macOS Finder, Windows Explorer, and GNOME Files can all mount a WebDAV share as if it were a network drive. Nextcloud, ownCloud, and many NAS boxes expose their storage over it; Apache and nginx can serve it with a module.

In the Zotero case, Zotero doesn't want to know about S3, Dropbox, or your NAS — it wants a URL it can `PUT` zip files to and `PROPFIND` to check what's there. Anything that answers those requests correctly is a valid file-sync backend, which is what makes the `rclone serve webdav` trick work: rclone speaks S3 on one side and WebDAV on the other, and Zotero only ever sees the WebDAV side.

For an Elixir developer the closest analogy is a REST-ish API where the resource hierarchy is literally a directory tree and the operations are filesystem operations, with XML request and response bodies. It's unfashionable and a bit verbose, but it's stable, universal, and it doesn't need a vendor SDK.

WebDAV is HTTP extended into a filesystem protocol. Plain HTTP lets a client GET a resource; WebDAV adds the verbs you'd need to treat a URL tree as a folder you can write to: `PUT` to upload a file, `DELETE`, `MKCOL` to make a directory, `MOVE` and `COPY`, `PROPFIND` to list a directory and read file properties like size and modification time, and `LOCK`/`UNLOCK` for coordinating concurrent edits. The name is "Web Distributed Authoring and Versioning"; it dates from the late 1990s and the spec is RFC 4918.

Because it's just HTTP with extra methods, it runs on port 80/443, goes through proxies and firewalls, works with ordinary TLS certificates, and uses ordinary HTTP authentication. That's why it became the lowest-common-denominator way for applications to talk to "some remote folder" without caring what's behind it. macOS Finder, Windows Explorer, and GNOME Files can all mount a WebDAV share as if it were a network drive. Nextcloud, ownCloud, and many NAS boxes expose their storage over it; Apache and nginx can serve it with a module.

In the Zotero case, Zotero doesn't want to know about S3, Dropbox, or your NAS — it wants a URL it can `PUT` zip files to and `PROPFIND` to check what's there. Anything that answers those requests correctly is a valid file-sync backend, which is what makes the `rclone serve webdav` trick work: rclone speaks S3 on one side and WebDAV on the other, and Zotero only ever sees the WebDAV side.

For an Elixir developer the closest analogy is a REST-ish API where the resource hierarchy is literally a directory tree and the operations are filesystem operations, with XML request and response bodies. It's unfashionable and a bit verbose, but it's stable, universal, and it doesn't need a vendor SDK.

### 19. human  ·  2026-09-08 05:25:59

Can AWS S3 work as a WebDav server?

Can AWS S3 work as a WebDav server?

### 20. assistant  ·  2026-09-08 05:26:11

No — not on its own. S3 speaks only its own REST API; it has no WebDAV mode, and none of AWS's managed gateways add one either. AWS Transfer Family gives you SFTP, FTPS, FTP and AS2 in front of S3; Storage Gateway gives you NFS and SMB; nothing from AWS speaks WebDAV.

So "S3 as WebDAV" always means "a small server that translates". Your options, roughly in order of effort:

- **rclone on a machine you already run.** `rclone serve webdav` with an S3 remote as its backend. Runs anywhere — your Linux box, one of your self-hosted servers, or a tiny EC2 instance. Put Caddy in front for TLS and basic auth. This is the usual answer and it's a few minutes of setup.
- **A container on ECS/Fargate or a small EC2** running a WebDAV server (Apache with `mod_dav`, or one of the Go/Rust single-binary WebDAV servers) with the bucket mounted via `s3fs` or `mountpoint-s3`. Same idea, more moving parts, only worth it if you want it fully inside AWS rather than on your own kit.
- **Third-party WebDAV-over-S3 gateways** exist as hosted services, but they add a vendor for something rclone does for free.

Whichever way, S3's eventual consistency quirks are gone now (it's been strongly consistent since 2020), so Zotero's PROPFIND-after-PUT pattern is fine; the only real requirement is that the translating server is reachable from both the Linux machine and the Mac whenever they sync.

Given that the whole point was avoiding a server to maintain, this is where Zotero Storage earns its subscription: it's WebDAV-shaped in effect but somebody else runs it.

No — not on its own. S3 speaks only its own REST API; it has no WebDAV mode, and none of AWS's managed gateways add one either. AWS Transfer Family gives you SFTP, FTPS, FTP and AS2 in front of S3; Storage Gateway gives you NFS and SMB; nothing from AWS speaks WebDAV.

So "S3 as WebDAV" always means "a small server that translates". Your options, roughly in order of effort:

- **rclone on a machine you already run.** `rclone serve webdav` with an S3 remote as its backend. Runs anywhere — your Linux box, one of your self-hosted servers, or a tiny EC2 instance. Put Caddy in front for TLS and basic auth. This is the usual answer and it's a few minutes of setup.
- **A container on ECS/Fargate or a small EC2** running a WebDAV server (Apache with `mod_dav`, or one of the Go/Rust single-binary WebDAV servers) with the bucket mounted via `s3fs` or `mountpoint-s3`. Same idea, more moving parts, only worth it if you want it fully inside AWS rather than on your own kit.
- **Third-party WebDAV-over-S3 gateways** exist as hosted services, but they add a vendor for something rclone does for free.

Whichever way, S3's eventual consistency quirks are gone now (it's been strongly consistent since 2020), so Zotero's PROPFIND-after-PUT pattern is fine; the only real requirement is that the translating server is reachable from both the Linux machine and the Mac whenever they sync.

Given that the whole point was avoiding a server to maintain, this is where Zotero Storage earns its subscription: it's WebDAV-shaped in effect but somebody else runs it.

### 21. human  ·  2026-09-08 18:35:15

what do I need to have installed on my machine to be able to compile latex. My Overleaf project is currently set up to compile with pdflatex, but I could use LuaLatex if that's better. I want to use biber with biblatex.

what do I need to have installed on my machine to be able to compile latex. My Overleaf project is currently set up to compile with pdflatex, but I could use LuaLatex if that's better. I want to use biber with biblatex.

### 22. assistant  ·  2026-09-08 18:35:37

The short list is: a TeX Live distribution, `latexmk`, and `biber` — and the last two normally come with the first. The detail that matters is *which* TeX Live you install, because biber and biblatex are version-locked to each other and mismatches are the classic way local compiles break when Overleaf ones don't.

**Linux (your main machine).** Two choices:

- *Vanilla TeX Live from tug.org* (`install-tl`, choose the full scheme, ~7 GB). This is what Overleaf runs, so package versions match, `tlmgr` works for updates, and biber/biblatex are guaranteed in step. It's the one I'd pick for a paper that's already compiling cleanly elsewhere.
- *Distro packages* (`apt install texlive-full biber latexmk` on Debian/Ubuntu). Simpler, but you get whatever TeX Live year your distro froze, `tlmgr` is disabled, and Ubuntu has shipped biber/biblatex pairs that disagree. Fine on a rolling distro like Arch; riskier on Ubuntu LTS.

Either way, `latexmk` is included, and it's what VimTeX drives.

**Mac.** MacTeX (`brew install --cask mactex` or the installer from tug.org) is vanilla TeX Live plus GUI extras; you already have it. Keep both machines on the same TeX Live year and the `.bbl` files won't drift between them.

**Configure latexmk for biber.** A `.latexmkrc` in the repo root, so both machines and Claude Code behave identically:

```perl
$pdf_mode = 1;            # pdflatex; use 4 for lualatex
$biber = 'biber %O %S';
$bibtex_use = 2;
@default_files = ('main.tex');
$clean_ext = 'bbl bcf run.xml synctex.gz';
```

Then `latexmk` alone does the pdflatex → biber → pdflatex → pdflatex dance and stops when cross-references settle, which is more reliable than your current fixed two-pass rule. `latexmk -pvc` watches for changes and recompiles, which is the Overleaf experience.

**pdflatex or LuaLaTeX?** Since you keep `.tex` files pure ASCII and use standard packages (biblatex, braket, amsthm, booktabs, draftwatermark), pdflatex has no disadvantage and is about twice as fast, which matters for `-pvc` and for Claude Code's compile-verify hook. LuaLaTeX earns its keep when you want native Unicode in the source, OpenType fonts via `fontspec`, or have hit pdflatex's memory limits on very large documents. None of that applies yet. The switch is a one-line change in `.latexmkrc` and on Overleaf when you do want it, so start with pdflatex and don't pre-pay for a migration you may never need.

One habit to carry over from Overleaf: it recompiles from a clean state more often than you'd think. Locally, when something weird happens with citations after a `.bib` change, `latexmk -C` then a fresh `latexmk` clears stale `.bcf`/`.bbl` files and is usually the fix.

The short list is: a TeX Live distribution, `latexmk`, and `biber` — and the last two normally come with the first. The detail that matters is *which* TeX Live you install, because biber and biblatex are version-locked to each other and mismatches are the classic way local compiles break when Overleaf ones don't.

**Linux (your main machine).** Two choices:

- *Vanilla TeX Live from tug.org* (`install-tl`, choose the full scheme, ~7 GB). This is what Overleaf runs, so package versions match, `tlmgr` works for updates, and biber/biblatex are guaranteed in step. It's the one I'd pick for a paper that's already compiling cleanly elsewhere.
- *Distro packages* (`apt install texlive-full biber latexmk` on Debian/Ubuntu). Simpler, but you get whatever TeX Live year your distro froze, `tlmgr` is disabled, and Ubuntu has shipped biber/biblatex pairs that disagree. Fine on a rolling distro like Arch; riskier on Ubuntu LTS.

Either way, `latexmk` is included, and it's what VimTeX drives.

**Mac.** MacTeX (`brew install --cask mactex` or the installer from tug.org) is vanilla TeX Live plus GUI extras; you already have it. Keep both machines on the same TeX Live year and the `.bbl` files won't drift between them.

**Configure latexmk for biber.** A `.latexmkrc` in the repo root, so both machines and Claude Code behave identically:

```perl
$pdf_mode = 1;            # pdflatex; use 4 for lualatex
$biber = 'biber %O %S';
$bibtex_use = 2;
@default_files = ('main.tex');
$clean_ext = 'bbl bcf run.xml synctex.gz';
```

Then `latexmk` alone does the pdflatex → biber → pdflatex → pdflatex dance and stops when cross-references settle, which is more reliable than your current fixed two-pass rule. `latexmk -pvc` watches for changes and recompiles, which is the Overleaf experience.

**pdflatex or LuaLaTeX?** Since you keep `.tex` files pure ASCII and use standard packages (biblatex, braket, amsthm, booktabs, draftwatermark), pdflatex has no disadvantage and is about twice as fast, which matters for `-pvc` and for Claude Code's compile-verify hook. LuaLaTeX earns its keep when you want native Unicode in the source, OpenType fonts via `fontspec`, or have hit pdflatex's memory limits on very large documents. None of that applies yet. The switch is a one-line change in `.latexmkrc` and on Overleaf when you do want it, so start with pdflatex and don't pre-pay for a migration you may never need.

One habit to carry over from Overleaf: it recompiles from a clean state more often than you'd think. Locally, when something weird happens with citations after a `.bib` change, `latexmk -C` then a fresh `latexmk` clears stale `.bcf`/`.bbl` files and is usually the fix.

### 23. human  ·  2026-09-08 18:36:46

I see that Overleaf is set up for texlive 2025 , but 2026 is available

I see that Overleaf is set up for texlive 2025 , but 2026 is available

### 24. assistant  ·  2026-09-08 18:36:59

Pick one and match it on both sides rather than worrying about which is newer. Overleaf lets you set the TeX Live version per project (Menu → Settings → TeX Live version), so the choice is yours in either direction.

My suggestion: stay on 2025 everywhere for now. Your paper compiles cleanly against it, the biber/biblatex pair in 2025 is the one your `.bbl` was produced with, and 2025 is still in Overleaf's supported list and receiving no further package updates — which is actually a feature during the final stretch of a paper, since nothing shifts under you. Install TeX Live 2025 locally (the tug.org historic archive keeps the 2025 installer; MacTeX 2025 is still downloadable too) and you'll have byte-for-byte reproducibility between Overleaf, the Linux box, and the Mac.

Move to 2026 once local becomes the canonical build and Overleaf is just a viewer for collaborators — or after Paper 1 is submitted, whichever comes first. At that point set Overleaf to 2026 the same day you upgrade locally, run `latexmk -C && latexmk`, and check the `.log` for package warnings. In practice the year-over-year breakage for a document using biblatex, amsthm, booktabs and braket is close to nil; the thing to watch is biblatex, which occasionally changes bibliography driver behaviour between versions, so eyeball the reference list after the upgrade.

The one thing not to do is run 2026 locally while Overleaf stays on 2025: you'd be compiling with a newer biber than the one Overleaf uses, and if a `.bcf` or `.bbl` ever gets committed or synced by mistake you'll get confusing "biber version mismatch" errors on one side.

Pick one and match it on both sides rather than worrying about which is newer. Overleaf lets you set the TeX Live version per project (Menu → Settings → TeX Live version), so the choice is yours in either direction.

My suggestion: stay on 2025 everywhere for now. Your paper compiles cleanly against it, the biber/biblatex pair in 2025 is the one your `.bbl` was produced with, and 2025 is still in Overleaf's supported list and receiving no further package updates — which is actually a feature during the final stretch of a paper, since nothing shifts under you. Install TeX Live 2025 locally (the tug.org historic archive keeps the 2025 installer; MacTeX 2025 is still downloadable too) and you'll have byte-for-byte reproducibility between Overleaf, the Linux box, and the Mac.

Move to 2026 once local becomes the canonical build and Overleaf is just a viewer for collaborators — or after Paper 1 is submitted, whichever comes first. At that point set Overleaf to 2026 the same day you upgrade locally, run `latexmk -C && latexmk`, and check the `.log` for package warnings. In practice the year-over-year breakage for a document using biblatex, amsthm, booktabs and braket is close to nil; the thing to watch is biblatex, which occasionally changes bibliography driver behaviour between versions, so eyeball the reference list after the upgrade.

The one thing not to do is run 2026 locally while Overleaf stays on 2025: you'd be compiling with a newer biber than the one Overleaf uses, and if a `.bcf` or `.bbl` ever gets committed or synced by mistake you'll get confusing "biber version mismatch" errors on one side.

### 25. human  ·  2026-09-08 18:39:11

how do I install the full tex compile suite. I remember doing this inside a container and it took all night

how do I install the full tex compile suite. I remember doing this inside a container and it took all night

### 26. assistant  ·  2026-09-08 18:39:30

The overnight install is almost always one of two things: a slow default mirror, or the documentation and source trees, which roughly double the download for files you'll never open. Fix both and a full TeX Live is a 20–40 minute job on a decent connection.

On Linux, for a frozen TeX Live 2025 install:

```bash
# get the installer from the frozen 2025 repository
REPO=https://ftp.tug.org/historic/systems/texlive/2025/tlnet-final
wget $REPO/install-tl-unx.tar.gz
tar xzf install-tl-unx.tar.gz && cd install-tl-2025*

# non-interactive profile: full scheme, no docs, no sources
cat > texlive.profile <<'EOF'
selected_scheme scheme-full
TEXDIR /usr/local/texlive/2025
TEXMFLOCAL /usr/local/texlive/texmf-local
TEXMFSYSVAR /usr/local/texlive/2025/texmf-var
TEXMFSYSCONFIG /usr/local/texlive/2025/texmf-config
tlpdbopt_install_docfiles 0
tlpdbopt_install_srcfiles 0
tlpdbopt_autobackup 0
EOF

sudo ./install-tl --repository $REPO --profile texlive.profile
```

Then add `/usr/local/texlive/2025/bin/x86_64-linux` to your `PATH` and check with `latexmk --version && biber --version`. If `ftp.tug.org` is slow from Kent, swap the repository for a UK mirror of the same path (`mirror.ox.ac.uk/sites/ctan.org/systems/texlive/tlnet` carries current only, so for historic you may need `ftp.math.utah.edu` or `pi.kwarc.info`; `ctan.org/mirrors` lists which carry `historic`). The `tlnet-final` suffix is important: it's the snapshot taken when 2026 shipped, so `tlmgr` won't try to move you forward.

For 2026 instead, drop the `--repository` flag and change the four `2025` paths; the installer picks a nearby CTAN mirror automatically.

If you want to trim further, `scheme-medium` plus `tlmgr install biblatex biber latexmk braket draftwatermark background booktabs` covers your paper in about a quarter of the space, but you'll then hit an occasional missing package and have to `tlmgr install` it. Full without docs is the setting that never surprises you, and it's about 3 GB.

On the Mac, `brew install --cask mactex-no-gui` does the equivalent, though Homebrew will only offer the current year; for a pinned 2025 use the `MacTeX-2025.pkg` from `tug.org/mactex/` and skip Homebrew.

Once it's installed, you're in a good position for the Claude Code hook too: `latexmk` on the host is faster and simpler than compiling inside a container, and the PATH line in your shell rc is the only config it needs.

The overnight install is almost always one of two things: a slow default mirror, or the documentation and source trees, which roughly double the download for files you'll never open. Fix both and a full TeX Live is a 20–40 minute job on a decent connection.

On Linux, for a frozen TeX Live 2025 install:

```bash
# get the installer from the frozen 2025 repository
REPO=https://ftp.tug.org/historic/systems/texlive/2025/tlnet-final
wget $REPO/install-tl-unx.tar.gz
tar xzf install-tl-unx.tar.gz && cd install-tl-2025*

# non-interactive profile: full scheme, no docs, no sources
cat > texlive.profile <<'EOF'
selected_scheme scheme-full
TEXDIR /usr/local/texlive/2025
TEXMFLOCAL /usr/local/texlive/texmf-local
TEXMFSYSVAR /usr/local/texlive/2025/texmf-var
TEXMFSYSCONFIG /usr/local/texlive/2025/texmf-config
tlpdbopt_install_docfiles 0
tlpdbopt_install_srcfiles 0
tlpdbopt_autobackup 0
EOF

sudo ./install-tl --repository $REPO --profile texlive.profile
```

Then add `/usr/local/texlive/2025/bin/x86_64-linux` to your `PATH` and check with `latexmk --version && biber --version`. If `ftp.tug.org` is slow from Kent, swap the repository for a UK mirror of the same path (`mirror.ox.ac.uk/sites/ctan.org/systems/texlive/tlnet` carries current only, so for historic you may need `ftp.math.utah.edu` or `pi.kwarc.info`; `ctan.org/mirrors` lists which carry `historic`). The `tlnet-final` suffix is important: it's the snapshot taken when 2026 shipped, so `tlmgr` won't try to move you forward.

For 2026 instead, drop the `--repository` flag and change the four `2025` paths; the installer picks a nearby CTAN mirror automatically.

If you want to trim further, `scheme-medium` plus `tlmgr install biblatex biber latexmk braket draftwatermark background booktabs` covers your paper in about a quarter of the space, but you'll then hit an occasional missing package and have to `tlmgr install` it. Full without docs is the setting that never surprises you, and it's about 3 GB.

On the Mac, `brew install --cask mactex-no-gui` does the equivalent, though Homebrew will only offer the current year; for a pinned 2025 use the `MacTeX-2025.pkg` from `tug.org/mactex/` and skip Homebrew.

Once it's installed, you're in a good position for the Claude Code hook too: `latexmk` on the host is faster and simpler than compiling inside a container, and the PATH line in your shell rc is the only config it needs.

### 27. human  ·  2026-09-08 18:45:43

give me a prompt I can use in Claude Code to setup Linux TexLive 2025, set the PATH and so on

give me a prompt I can use in Claude Code to setup Linux TexLive 2025, set the PATH and so on

### 28. assistant  ·  2026-09-08 18:46:03

Here's a prompt you can paste straight into Claude Code from your home directory (or the paper repo — it'll handle either):

```
Install TeX Live 2025 (frozen) on this Linux machine and set it up for compiling
my biblatex/biber paper. Work step by step, show me each command before running
anything with sudo, and stop if a verification step fails.

Requirements:
1. Detect distro, package manager, and CPU arch (x86_64 vs aarch64). Install the
   prerequisites TeX Live needs: perl, wget or curl, tar, fontconfig, and
   perl-tk/libtk if the installer wants it. Nothing else from the distro's
   texlive packages — I want vanilla TeX Live, not the apt/dnf one. If a distro
   texlive is already installed, tell me and ask before removing it.
2. Check whether /usr/local/texlive/2025 already exists. If it does, skip the
   install and go straight to verification.
3. Download install-tl-unx.tar.gz from the frozen 2025 repo:
   https://ftp.tug.org/historic/systems/texlive/2025/tlnet-final
   If that host is slow or unreachable, find a mirror carrying the
   historic/systems/texlive/2025/tlnet-final path from https://ctan.org/mirrors
   and use that. Verify the sha512 if a checksum file is available.
4. Write a texlive.profile for a non-interactive install:
   scheme-full, TEXDIR /usr/local/texlive/2025, TEXMFLOCAL
   /usr/local/texlive/texmf-local, docfiles 0, srcfiles 0, autobackup 0.
5. Run the installer with --repository pointing at the tlnet-final URL and
   --profile. Run it in the background with output logged to
   ~/texlive-install.log and poll it, so the session doesn't hang.
6. Add the bin directory (/usr/local/texlive/2025/bin/<arch>-linux) to PATH
   in my shell rc file. Detect whether I use bash, zsh, or fish and edit the
   right file. Make the edit idempotent (don't add a duplicate line).
7. Verify in a fresh shell: pdflatex --version, lualatex --version,
   biber --version, latexmk --version, and confirm biber and biblatex versions
   are a matching pair (kpsewhich biblatex.sty, then grep the version from it).
8. Create a minimal test document in a temp directory using
   \usepackage[backend=biber]{biblatex}, \addbibresource with one entry, one
   \autocite, and \printbibliography. Compile it with latexmk -pdf and confirm
   the PDF exists and the .log has no lines starting with '!'.
9. If I'm inside a git repo containing main.tex, offer to create a .latexmkrc
   in the repo root with:
     $pdf_mode = 1;
     $biber = 'biber %O %S';
     $bibtex_use = 2;
     @default_files = ('main.tex');
     $clean_ext = 'bbl bcf run.xml synctex.gz';
   and add build artefacts (*.aux *.bbl *.bcf *.blg *.log *.run.xml *.synctex.gz
   *.fdb_latexmk *.fls *.out *.toc) to .gitignore if they're not there already.
10. Finish with a short summary: TeX Live path, biber/biblatex versions, the rc
    file you edited, the size on disk, and anything I still need to do by hand.

Don't run tlmgr update — this install is intentionally pinned to 2025.
```

Two notes for running it. Claude Code will prompt you to approve each `sudo` command; that's the "show me before running" clause working as intended, so keep it. And step 5's background-and-poll is worth insisting on: the installer takes 20–40 minutes, and a foreground command that long can trip Claude Code's tool timeout.

Here's a prompt you can paste straight into Claude Code from your home directory (or the paper repo — it'll handle either):

```
Install TeX Live 2025 (frozen) on this Linux machine and set it up for compiling
my biblatex/biber paper. Work step by step, show me each command before running
anything with sudo, and stop if a verification step fails.

Requirements:
1. Detect distro, package manager, and CPU arch (x86_64 vs aarch64). Install the
   prerequisites TeX Live needs: perl, wget or curl, tar, fontconfig, and
   perl-tk/libtk if the installer wants it. Nothing else from the distro's
   texlive packages — I want vanilla TeX Live, not the apt/dnf one. If a distro
   texlive is already installed, tell me and ask before removing it.
2. Check whether /usr/local/texlive/2025 already exists. If it does, skip the
   install and go straight to verification.
3. Download install-tl-unx.tar.gz from the frozen 2025 repo:
   https://ftp.tug.org/historic/systems/texlive/2025/tlnet-final
   If that host is slow or unreachable, find a mirror carrying the
   historic/systems/texlive/2025/tlnet-final path from https://ctan.org/mirrors
   and use that. Verify the sha512 if a checksum file is available.
4. Write a texlive.profile for a non-interactive install:
   scheme-full, TEXDIR /usr/local/texlive/2025, TEXMFLOCAL
   /usr/local/texlive/texmf-local, docfiles 0, srcfiles 0, autobackup 0.
5. Run the installer with --repository pointing at the tlnet-final URL and
   --profile. Run it in the background with output logged to
   ~/texlive-install.log and poll it, so the session doesn't hang.
6. Add the bin directory (/usr/local/texlive/2025/bin/<arch>-linux) to PATH
   in my shell rc file. Detect whether I use bash, zsh, or fish and edit the
   right file. Make the edit idempotent (don't add a duplicate line).
7. Verify in a fresh shell: pdflatex --version, lualatex --version,
   biber --version, latexmk --version, and confirm biber and biblatex versions
   are a matching pair (kpsewhich biblatex.sty, then grep the version from it).
8. Create a minimal test document in a temp directory using
   \usepackage[backend=biber]{biblatex}, \addbibresource with one entry, one
   \autocite, and \printbibliography. Compile it with latexmk -pdf and confirm
   the PDF exists and the .log has no lines starting with '!'.
9. If I'm inside a git repo containing main.tex, offer to create a .latexmkrc
   in the repo root with:
     $pdf_mode = 1;
     $biber = 'biber %O %S';
     $bibtex_use = 2;
     @default_files = ('main.tex');
     $clean_ext = 'bbl bcf run.xml synctex.gz';
   and add build artefacts (*.aux *.bbl *.bcf *.blg *.log *.run.xml *.synctex.gz
   *.fdb_latexmk *.fls *.out *.toc) to .gitignore if they're not there already.
10. Finish with a short summary: TeX Live path, biber/biblatex versions, the rc
    file you edited, the size on disk, and anything I still need to do by hand.

Don't run tlmgr update — this install is intentionally pinned to 2025.
```

Two notes for running it. Claude Code will prompt you to approve each `sudo` command; that's the "show me before running" clause working as intended, so keep it. And step 5's background-and-poll is worth insisting on: the installer takes 20–40 minutes, and a foreground command that long can trip Claude Code's tool timeout.
