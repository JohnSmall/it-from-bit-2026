# Who is working in this clone

This is the shape of `CONTRIBUTOR.md`, which lives beside it in the repository
root and is **gitignored** --- it stays on one machine and is never committed,
so every fresh clone starts by asking again.

An agent writes it on its first run, from what the person tells it. You can
also just copy this file to `CONTRIBUTOR.md` and fill it in by hand. Nothing
here is compulsory: leave out anything you would rather not record, and the
agent should not press for it.

Keep it short. It is a handshake, not a CV.

---

    # Contributor

    - name: <what to call you>
    - role: maintainer | contributor
    - git identity: <name and email git is configured with, if it differs>

    ## Background

    One or two sentences. Physics? Mathematics? Software? Which parts are
    deep and which are passing acquaintance? This sets how much an agent
    explains and what it can take for granted --- say "I know Hopf fibrations
    but not biblatex" if that is the truth, and it will stop explaining the
    one and start explaining the other.

    ## Interests

    What you want to work on here, and what you would rather leave alone.
    The open problems in `knowledge/open_problems.md` are a reasonable menu.

    ## Working preferences

    Anything an agent should know: how much you want to be asked before a
    change is made, whether to run builds unprompted, whether you prefer
    proposals in prose or as patches.

---

## Notes for whoever writes this

**Role matters.** The maintainer works on `main` directly and is the only
person who applies status labels, writes ledger entries, exports the Zotero
bibliography or touches `knowledge/publications/`. A contributor branches,
opens a pull request, and *proposes* those things. If the role is unclear,
assume contributor: proposing costs little, and applying a label that turns
out to be the maintainer's to give costs a correction in an append-only
ledger.

**Do not infer identity from the repository.** The session notes, ledgers and
commit messages say "JS" throughout and read as though a conversation is
already in progress. That conversation was with the maintainer, and it has
ended. Someone reading this is probably not him.
