# Corrections to the exported memory

`memory/` is kept verbatim as Claude web wrote it, because it is evidence of
what the system believed. It is *not* corrected in place. Known errors are
listed here instead, and the curated files in `knowledge/` follow this page
rather than the memory.

Recorded 2026-09-10.

## A constructed dialogue was read as a record of events

`archive/conversations/2026-07-28_self-reference-and-complex-valued-logic-dialogue_f639a491.md`
is a deliberate fiction: minutes of a meeting that never happened, with
Bertrand Russell, George Spencer-Brown, Karl Svozil, Terence Tao and David
Deutsch as attendees, and Godel, Aaronson and Hawking sending apologies. It
was written as a device to break an impasse on deriving continuity from
self-reference -- an attempt at simulated annealing on a stuck argument.

The device worked and the document is kept. But **Karl Svozil subsequently
appeared in `people.md` as an interlocutor**, which he is not. There is no
record anywhere in the corpus of an exchange with him. He is an author whose
work is cited and whose likely objections are modelled.

Nothing in that dialogue was said by any named person. Tao and Deutsch, also
in the cast, were never carried into the curated files; that was luck rather
than design.

## A real correspondence was overstated

A private communication from Scott Aaronson, in which he characterised the
development of **his own** related ideas, was rendered in the distilled memory
as an endorsement of *this framework's* Shannon-information route -- a
different and much stronger claim, and one he has never been asked about.

The inflated wording is not reproduced here, since repeating it would
propagate a false attribution to a named person, which is what this
correction exists to stop. `people.md` states positively what the
correspondence did and did not establish, and that is the record to rely on.

## A private remark was redacted

A brief coffee-break exchange at a Vaxjo conference, in which a named
researcher said in passing that he had not considered a connection the
framework relies on, had propagated into `people.md`, the exported memory,
the archive index, and a conversation -- and in one document was doing
argumentative work, offered as evidence for how unexplored the connection
is. The exchange was slight, was not consented to for publication, and could
not support that weight.

Those passages are redacted, marked in place with
`[redacted 2026-09-10: private remark by a named third party]`. Citations of
the same researcher's *published* work are untouched and remain throughout.

One instance is deliberately kept: the provenance note in
`project-docs/pedagogical_chain_selfref_to_l2_2026-08-04T1720.md`, headed
"NOT for print without permission". It records the discipline working -- a
flag raised and honoured -- and is the single qualified statement on the
matter rather than one of several unqualified ones.

## Two conversations were removed as off-topic

The 100 archived conversations were selected from a 237-conversation account
export by scoring names and summaries against the framework's vocabulary,
because the export carries no project field. Two passed on a single stray
keyword and were removed on 2026-09-10 after review, leaving 98:

- **An onboarding-prompt review for EMFA**, a commercial Atlassian/Jira
  project. It contained *one* occurrence of "self-referential" -- describing
  EMFA's own architecture, not this framework -- against 744 mentions of
  EMFA, 300 of Jira and 426 of sprint, and zero occurrences of Hopf,
  octonion, FANOUT, sedenion, negative probability, Godel, entanglement or
  qubit. 484 KB of unrelated client work.
- **A conversation on productising expertise**, mixing meditation and quantum
  computing: business positioning rather than physics.
  It was reinstated on 2026-09-14 on the view that the author's professional
  and personal context belongs in the record, and removed again the same day
  once JS had read the text: it is a business-coaching conversation belonging
  to a different project, and the physics vocabulary in it is incidental. Both
  the original exclusion and this confirmation were judgements made after
  reading, not by the keyword filter. The archive stands at 99.

The lesson generalises: a keyword filter over summaries will admit anything
sharing a term of art, and "self-referential" is common enough in software
architecture to be a poor discriminator. Any future addition to this archive
should be checked by term *density*, not term presence.

Separately, `2026-07-11_sedenion-extensions-onboarding` was tagged
`[tooling]` in error -- the word "onboarding" matched a tooling regex. It is
one of the largest physics sessions in the corpus and the tag has been
removed.

## The published history was rewritten

On 2026-09-10, before this repository was made public, its git history was
rewritten with `git filter-repo` to remove two things it should never have
carried: two conversations belonging to unrelated commercial work, and a
private remark by a named third party made in passing and without consent to
publication.

Redacting the working tree would not have been enough. Both were already
pushed, and git keeps every earlier version reachable, so anyone cloning the
repository could have recovered them from the history. The rewrite removes
them from every commit. Commit history is otherwise preserved: the record of
how this corpus was assembled, corrected and checked is intact, and the
commits that performed the redaction are part of it.

The GitHub repository was deleted and recreated rather than force-pushed,
because a force-push leaves the superseded commits addressable by their
hashes until GitHub garbage-collects them, which is neither immediate nor
guaranteed.

CLAUDE.md's standing rule is "No force-push". It was amended in the same pass
to record this exception rather than leaving the rule quietly broken.

## Why this is published rather than quietly fixed

The corpus is public so that the collaboration can be audited rather than
taken on trust. Both errors above are ordinary failure modes of AI
distillation -- fiction absorbed as fact, and a modest claim inflated into an
endorsement -- and a reader is better served seeing them caught than seeing a
version with no visible seams.
