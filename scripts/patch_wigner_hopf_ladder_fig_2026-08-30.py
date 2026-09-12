#!/usr/bin/env python3
"""
patch_wigner_hopf_ladder_fig_2026-08-30.py

Inserts, into wigners_friend_in_the_hopf_picture_2026-06-13.tex, immediately
after the two-idealisations paragraph (the one ending "...what bounds the
information a single such link can carry."):

  (1) a short paragraph deferring the Hopf-fibration pedagogy to Szangolies
      (szangolies2025standardmodel, in library) and pointing at the figure;
  (2) \\input{fig_wigner_hopf_ladder_2026-08-30}  (the figure floats [t]).

The paragraph's \\S-references to sec:wf-phase-promotion and
sec:wf-chain-type are forward references within the section, in the file's
established deliberate-forward convention; sec:sedenions-generations is the
2026-08-27 (rev. 2026-08-30) section. PREAMBLE: the figure needs
\\usepackage{tikz} and \\usetikzlibrary{arrows.meta} in main.tex -- confirm
or add before compiling.

ORDER: independent of patch_wigner_chain_type_2026-08-27.py and
patch_wigner_ewf_positioning_2026-08-30.py (this anchor is early in the
file; those act at the tail). Backup suffix is distinct so same-day runs
never overwrite each other's backups.

Gates (any failure => no write, exit 1):
  - target exists, pure ASCII;
  - anchor phrase "what bounds the information a single such link can"
    occurs EXACTLY once, with "carry." within 40 characters after it
    (whitespace-tolerant across the line break);
  - idempotence: "fig:wf-hopf-ladder" absent from the target.
Writes <target>.bak_2026-08-30_ladderfig before modifying, and prints three
lines each side of the insertion for eyeballing.

Usage:
    python3 patch_wigner_hopf_ladder_fig_2026-08-30.py \
        [wigners_friend_in_the_hopf_picture_2026-06-13.tex]
"""
import shutil
import sys

ANCHOR = "what bounds the information a single such link can"
TAIL = "carry."
IDEMPOTENCE_MARK = "fig:wf-hopf-ladder"
DEFAULT_TARGET = "wigners_friend_in_the_hopf_picture_2026-06-13.tex"

BLOCK = r"""
The fibrations themselves are not re-derived here: Szangolies's presentation is
the careful, self-contained introduction \autocite{szangolies2025standardmodel},
and we defer to it. What the framework adds is the mapping --- used throughout
the sections that follow, and easy to mistake for a notational convenience until
it is drawn --- and Figure~\ref{fig:wf-hopf-ladder} lays it out at a glance:
each observer in the chain holds a chart one rung further up the Cayley--Dickson
ladder; every chart carries its holder's own gauge circle, the self-referential
ignorance he cannot see around, together with a fibre in which the circle of the
observer below has become interferable (\S\ref{sec:wf-phase-promotion}); the
fibrations run out exactly at the completed triple; and the fourth wire delivers
a label in place of a fibre (\S\ref{sec:wf-chain-type},
\S\ref{sec:sedenions-generations}).

\input{fig_wigner_hopf_ladder_2026-08-30}
"""


def fail(msg):
    print("FAIL: " + msg)
    sys.exit(1)


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TARGET
    try:
        with open(target, "r", encoding="ascii") as fh:
            text = fh.read()
    except FileNotFoundError:
        fail("target not found: " + target)
    except UnicodeDecodeError:
        fail("target is not pure ASCII: " + target)

    if IDEMPOTENCE_MARK in text:
        fail("already applied (%s present)" % IDEMPOTENCE_MARK)
    n = text.count(ANCHOR)
    if n != 1:
        fail("anchor found %d times (need exactly 1)" % n)
    a = text.index(ANCHOR) + len(ANCHOR)
    d = text.find(TAIL, a)
    if d == -1 or d - a > 40:
        fail("'%s' not found within 40 chars of the anchor" % TAIL)
    eol = text.find("\n", d)
    eol = len(text) if eol == -1 else eol + 1

    patched = text[:eol] + BLOCK + text[eol:]
    bak = target + ".bak_2026-08-30_ladderfig"
    shutil.copyfile(target, bak)
    with open(target, "w", encoding="ascii") as fh:
        fh.write(patched)

    assert patched.count(IDEMPOTENCE_MARK) == 1
    lines = patched.split("\n")
    k = next(i for i, ln in enumerate(lines)
             if "fig_wigner_hopf_ladder_2026-08-30" in ln)
    print("PASS: deferral paragraph and figure input inserted")
    print("      target : " + target)
    print("      backup : " + bak)
    print("      context around the \\input line:")
    for ln in lines[max(0, k - 3):k + 3]:
        print("        | " + ln)
    print("REMINDER: (1) confirm/add in the main.tex preamble:")
    print("              \\usepackage{tikz}  \\usetikzlibrary{arrows.meta}")
    print("          (2) fig_wigner_hopf_ladder_2026-08-30.tex must sit in the")
    print("          tree (same directory as the WF section, or adjust the")
    print("          \\input path);")
    print("          (3) pdflatex x2 + biber, zero errors, before commit.")


if __name__ == "__main__":
    main()
