#!/usr/bin/env python3
"""Replace the fossil subsection "Reversible continuity" in what_is_a_quantum_state.tex by a
pointer to sec:continuity, and fix the two sentences that refer to it.

JS, 2026-09-15: the subsection (lines 546--560) predates sec:continuity and contradicts it
twice: it says the diagonal construction fills the gaps in Q to give R "and hence continuity",
which sec:continuity explicitly corrects (the diagonal presupposes the completed line), and it
says reversible continuity "is a consequence of self-reference", which is now conditional on
one open premise (prop:connected-transitive; op:limit-realisability). Its label is referenced
from main.tex (introduction) and from earlier in the same file, so the label is kept.

Two files, one header each, one run only.

paper1/what_is_a_quantum_state.tex
  1. The subsection body is replaced by a short pointer: the recordless reversible regime,
     Hardy's axiom and what it affords (the TRUE/FALSE superposition), the corrected reading
     of the diagonal, and the honest status with a pointer to sec:continuity and
     op:limit-realisability.
  2. The earlier sentence "We expand on that topic when discussing reversible continuity in
     \\ref{sec:reversible-continuity}" promised a discussion of quaternionic and octonionic
     amplitudes that the subsection never gave; it now says that continuity fixes the metric
     and not the field, and points to sec:continuity.
paper1/main.tex
  3. The introduction's "this forces reversible continuity \\ref{sec:reversible-continuity}"
     becomes "we take up reversible continuity, which \\ref{sec:continuity} reduces to a single
     open premise about values". Bare \\ref kept to match the paragraph (a style pass over that
     paragraph is a separate todo).

Every anchor is matched whitespace-insensitively and must match exactly once; edited prose is
pre-filled or re-filled to 96 columns. A dated .bak is written per file, a "% EDITED" header
is prepended, and the header makes the script refuse to run twice (already-patched files are
skipped).
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-15"
STAMP = "2026-09-15T1525"
SCRIPT = "scripts/patch_reversible_continuity_fossil_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

WIQS = "paper1/what_is_a_quantum_state.tex"
MAIN = "paper1/main.tex"


def ws(s):
    return r"\s+".join(re.escape(p) for p in s.split())


def fill(s):
    return textwrap.fill(" ".join(s.split()), width=WIDTH,
                         break_long_words=False, break_on_hyphens=False)


def replace_once(text, anchor, replacement):
    pat = re.compile(ws(anchor.strip()))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: anchor matched %d times, expected 1:\n  %s" % (n, anchor.strip()[:70]))
    m = pat.search(text)
    return text[:m.start()] + replacement + text[m.end():]


def refill_paragraph_at(text, marker):
    i = text.index(marker)
    start = text.rfind("\n\n", 0, i) + 2
    end = text.find("\n\n", i)
    para = text[start:end]
    for line in para.splitlines():
        if line.lstrip().startswith(("\\begin", "\\end", "\\item", "%", "\\subsection",
                                     "\\section", "\\label", "\\paragraph")):
            sys.exit("REFUSING: paragraph to re-fill contains structure:\n  %s" % line)
    return text[:start] + fill(para) + text[end:]


# 1. the subsection body
OLD_SUB = r"""
\subsection{Reversible continuity}
\label{sec:reversible-continuity}
In the pre-FANOUT regime erasing information has no thermodynamic cost, everything is reversible
and because there are no copyable records there is no well defined ordering of events. Cantor's
diagonalisation argument is used to show that there are more real numbers than countable
numbers, by construction we can use self-referential diagonalisation to generate numbers that
are not in any list. Which means self-reference can generate the numbers to fill in the gaps in
$\mathbb{Q}$ to get $\mathbb{R}$ and hence continuity. Hardy's "Quantum Theory From Five
Reasonable Axioms" \autocite{Hardy2001a} identifies the axiom of reversible continuity as the
key differentiator between classical and quantum theory. Reversible continuity means we can
reversibly and continuously move between say $\ket{TRUE}$ and $\ket{FALSE}$, prior to FANOUT
there is no preferred basis. The fact that a superposition $\ket{TRUE}$ and $\ket{FALSE}$
enables a quantum state to represent the classically inadmissable states that arise in paradoxes
of self-reference is a consequence of the axiom of reversible continuity. Working from Popper's
model we find that reversible continuity is a consequence of self-reference.
"""
NEW_SUB = "\n".join([
    r"\subsection{Reversible continuity}",
    r"\label{sec:reversible-continuity}",
    fill(r"""
In the pre-\textsc{fanout} regime erasing information has no thermodynamic cost, everything is
reversible, and because there are no copyable records there is no well-defined ordering of
events. Hardy's reconstruction \autocite{Hardy2001a} identifies reversible continuity --- that a
continuous reversible transformation connects any two pure states, so that one can move
continuously between $\ket{TRUE}$ and $\ket{FALSE}$ with no preferred basis --- as the one axiom
that separates quantum from classical probability, and it is what lets a superposition of
$\ket{TRUE}$ and $\ket{FALSE}$ represent the classically inadmissible states of the paradoxes of
self-reference. Whether self-reference forces that axiom is the subject of
\S\ref{sec:continuity}. It is tempting to read Cantor's diagonal as filling the gaps in
$\mathbb{Q}$ to give $\mathbb{R}$, and continuity with it; the reading is backwards, as that
section explains, since the diagonal presupposes the completed line rather than building it. The
honest position is the one given there: continuity is not an axiom of the framework, but it
reduces, by a theorem, to a single premise about values --- that self-referential ignorance is
not rationed --- stated as Open Problem~\ref{op:limit-realisability}.
"""),
])

# 2. the earlier promise
OLD_PROMISE = r"""
commutative, it can't depend on the ordering. We expand on that topic when discussing reversible
continuity in \ref{sec:reversible-continuity}. Therefore probabilities which occur in such
self-referential setups have to be complex numbers.
"""
NEW_PROMISE = r"""
commutative, it can't depend on the ordering. Continuity, which fixes the metric and not the
field, is taken up separately in \S\ref{sec:continuity}. Therefore probabilities which occur in
such self-referential setups have to be complex numbers.
""".strip()

# 3. the introduction
OLD_INTRO = r"""
Once we're arrived at that stage we go on to find that
this forces reversible continuity \ref{sec:reversible-continuity} and once that is settled it
leads to the L2 metric \ref{sec:reversible-continuity-l2}.
"""
NEW_INTRO = r"""
Once we have arrived at that stage we take up reversible continuity
\ref{sec:reversible-continuity}, which \ref{sec:continuity} reduces to a single open premise
about values, and once that is settled it leads to the L2 metric
\ref{sec:reversible-continuity-l2}.
""".strip()


def patch(path, fn, must_contain):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if HEADER in text:
        print("already patched, skipping: %s" % path)
        return
    text = fn(text)
    for s in must_contain:
        if s not in text:
            sys.exit("REFUSING: %s lacks %r after the edit" % (path, s))
    shutil.copy(path, path + "." + STAMP + ".bak")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HEADER + text)
    print("patched %s (backup %s.%s.bak)" % (path, path, STAMP))


def edit_wiqs(text):
    text = replace_once(text, OLD_SUB, NEW_SUB)
    text = replace_once(text, OLD_PROMISE, NEW_PROMISE)
    text = refill_paragraph_at(text, "is taken up separately in")
    if text.count(r"\label{sec:reversible-continuity}") != 1:
        sys.exit("REFUSING: label count wrong")
    return text


def edit_main(text):
    text = replace_once(text, OLD_INTRO, NEW_INTRO)
    return text


def main():
    patch(WIQS, edit_wiqs, [r"\ref{op:limit-realisability}", r"\S\ref{sec:continuity}"])
    patch(MAIN, edit_main, [r"\ref{sec:continuity} reduces to a single open premise"])


if __name__ == "__main__":
    main()
