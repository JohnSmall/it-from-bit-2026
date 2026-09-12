#!/usr/bin/env python3
"""Cite Aaronson's chapter 9 as a postnote on a whole-book reference.

Scott Aaronson's reply of 21 June 2021 asked to be cited as "[Aaronson, Ch 9]".
The entry was a Zotero bookSection carrying the book's title with no booktitle,
so it exported as an @incollection, and the chapter had been added as a
`chapter = {9}` field. That is the wrong shape: a chapter number attached to
what biblatex reads as a section title.

The item is now a plain book (Zotero item RKQAT9IY changed to itemType `book`
via the local API on 2026-09-12, the tex.chapter Extra removed), so it exports
as `@book{Aaronson:dem}`. The chapter belongs in the citation instead, which is
both the biblatex idiom and nearer to what he asked for.

Three sites in what_is_a_quantum_state.tex:

  l.272  \autocite{aaronson_lect9,Aaronson:dem}
  l.301  \autocite{aaronson_lect9, Aaronson:dem}
         Two keys, and only the book takes a chapter, so these become
         \autocites{aaronson_lect9}[ch.~9]{Aaronson:dem} --- biblatex's
         multicite form, where a lone optional argument before a key is that
         key's postnote. A postnote on a plain \autocite with two keys would
         attach to the whole citation, which is not what is meant.
  l.311  \autocite{Aaronson:dem}, the attribution under the block quotation,
         becomes \autocite[ch.~9]{Aaronson:dem}.

`aaronson_lect9` is the Phys771 Lecture 9 page, which is the free online
version of that same chapter, so the pairing reads correctly: the page, and
chapter 9 of the book.

Postnote style is `ch.~9`, lower case, the biblatex convention; he wrote
"Ch 9" but the case is the bibliography style's to set, not the source's.

Anchors are matched whitespace-insensitively and each must match exactly once.
A .bak is written, an "% EDITED" header prepended, and the header makes the
script refuse to run twice.

Needs a re-export of the Zotero collection to pick up the @book change, and a
build, before it is verified. Neither is done here.
"""

import re
import shutil
import sys

DATE = "2026-09-12"
SCRIPT = "scripts/patch_aaronson_chapter_cite_2026-09-12T1300.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/what_is_a_quantum_state.tex"

EDITS = [
    (r"\autocite{aaronson_lect9,Aaronson:dem} are particularly useful.",
     r"\autocites{aaronson_lect9}[ch.~9]{Aaronson:dem} are particularly useful."),
    (r"Aaronson \autocite{aaronson_lect9, Aaronson:dem} takes a different approach.",
     r"Aaronson \autocites{aaronson_lect9}[ch.~9]{Aaronson:dem} takes a different approach."),
    (r"\hfill \autocite{Aaronson:dem}",
     r"\hfill \autocite[ch.~9]{Aaronson:dem}"),
]


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))
    if r"\autocites{aaronson_lect9}" in text:
        sys.exit("REFUSING: the multicite form is already present")

    before = text.count("Aaronson:dem")
    for old, new in EDITS:
        pat = re.compile(ws(old))
        n = len(pat.findall(text))
        if n != 1:
            sys.exit("REFUSING: anchor matched %d times, expected 1:\n  %s" % (n, old))
        text = pat.sub(lambda _m, r=new: r, text, count=1)

    if text.count("Aaronson:dem") != before:
        sys.exit("REFUSING: the number of Aaronson:dem citations changed")
    if text.count("ch.~9") != 3:
        sys.exit("REFUSING: expected three chapter postnotes, found %d" % text.count("ch.~9"))
    if r"\autocite{Aaronson:dem}" in text or "Aaronson:dem}" in text.replace(
            "[ch.~9]{Aaronson:dem}", ""):
        sys.exit("REFUSING: an un-noted Aaronson:dem citation survives")

    shutil.copy2(DEST, DEST + ".bak")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("patched %s" % DEST)


if __name__ == "__main__":
    main()
