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

The primary record (`project-docs/Pure_states_and_mixed_states_in_quantum_foundations_2026_04_11.md`)
says Scott Aaronson confirmed by private communication that **his own** ideas
on negative probability leading to quantum amplitudes were "not even well
developed enough to form into a conjecture".

`memory/project/overview.md` and `memory/project/rolling-memory.md` render
[wording removed; see CORRECTIONS.md]

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

## Why this is published rather than quietly fixed

The corpus is public so that the collaboration can be audited rather than
taken on trust. Both errors above are ordinary failure modes of AI
distillation -- fiction absorbed as fact, and a modest claim inflated into an
endorsement -- and a reader is better served seeing them caught than seeing a
version with no visible seams.
