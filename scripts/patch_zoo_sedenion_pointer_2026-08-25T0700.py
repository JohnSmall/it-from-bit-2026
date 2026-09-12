#!/usr/bin/env python3
"""
patch_zoo_sedenion_pointer_2026-08-25T0700.py

REPLACES the old \\subsection sec:sedenion-announcement in
particle_zoo_section_2026-06-08.tex with the short SIGNPOST block from
zoo_sedenion_pointer_replacement_2026-08-25T0700.tex, now that the
mechanism lives in the standalone section sedenions_generations_section.

This is a SPAN replacement (removes the old subsection body), which is
riskier than an insertion, so the gates are strict.

Span detection:
  BEGIN anchor: the subsection line
    "\\subsection{The extra wire: how a deeper mechanism announced itself}"
  END anchor: the START of the next subsection. The old subsection is the
    last one carrying sedenion prose before the section's open-problem
    material; the audit-confirmed next \\subsection line is
    "\\subsection{" occurring AFTER the begin anchor. The script replaces
    from the begin anchor up to (but not including) the next
    "\n\\subsection{" after it.

Gates (any failure => no write, exit 1):
  1. target exists and is pure ASCII;
  2. begin anchor occurs exactly once;
  3. at least one "\\subsection{" follows the begin anchor (the end
     boundary exists);
  4. the signpost has not already been applied (idempotence: the new
     label sentence "where it is resolved" absent);
  5. the replacement span does NOT contain "\\begin{openproblem}" -- a
     guard against swallowing the op:filatov-extension block if the
     subsection ordering differs from the audit. If it does, ABORT and
     ask for a hand edit.

Writes target+".bak" before modifying. Retains it as the delta record.

Usage:
    python3 patch_zoo_sedenion_pointer_2026-08-25T0700.py \
        [particle_zoo_section_2026-06-08.tex] \
        [zoo_sedenion_pointer_replacement_2026-08-25T0700.tex]
"""
import shutil
import sys

BEGIN_ANCHOR = "\\subsection{The extra wire: how a deeper mechanism announced itself}"
NEXT_SUBSEC = "\n\\subsection{"
IDEMPOTENCE_MARK = "where it is resolved"
OP_GUARD = "\\begin{openproblem}"

SIG_BEGIN = "% SIGNPOST-BEGIN sedenion-pointer 2026-08-25T0700"
SIG_END = "% SIGNPOST-END sedenion-pointer 2026-08-25T0700"

DEFAULT_TARGET = "particle_zoo_section_2026-06-08.tex"
DEFAULT_SIG = "zoo_sedenion_pointer_replacement_2026-08-25T0700.tex"


def fail(msg):
    print("FAIL: " + msg)
    sys.exit(1)


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TARGET
    sigfile = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_SIG

    try:
        with open(target, "r", encoding="ascii") as fh:
            text = fh.read()
    except FileNotFoundError:
        fail("target not found: " + target)
    except UnicodeDecodeError:
        fail("target is not pure ASCII: " + target)

    try:
        with open(sigfile, "r", encoding="ascii") as fh:
            sigtext = fh.read()
    except FileNotFoundError:
        fail("signpost file not found: " + sigfile)
    except UnicodeDecodeError:
        fail("signpost file is not pure ASCII: " + sigfile)

    if IDEMPOTENCE_MARK in text:
        fail("signpost already applied (idempotence mark present)")

    if sigtext.count(SIG_BEGIN) != 1 or sigtext.count(SIG_END) != 1:
        fail("signpost file must contain exactly one SIGNPOST-BEGIN/END pair")
    sb = sigtext.index(SIG_BEGIN)
    se = sigtext.index(SIG_END) + len(SIG_END)
    block = sigtext[sb:se].rstrip("\n") + "\n"

    n = text.count(BEGIN_ANCHOR)
    if n != 1:
        fail("begin anchor found %d times (need exactly 1)" % n)
    start = text.index(BEGIN_ANCHOR)

    nxt = text.find(NEXT_SUBSEC, start + len(BEGIN_ANCHOR))
    if nxt == -1:
        fail("no following \\subsection found; end boundary undetermined")
    end = nxt + 1  # keep the newline that precedes the next \subsection

    span = text[start:end]
    if OP_GUARD in span:
        fail("replacement span contains \\begin{openproblem}; ordering "
             "differs from audit -- apply by hand, do not run")

    patched = text[:start] + block + "\n" + text[end:]

    bak = target + ".bak"
    shutil.copyfile(target, bak)
    with open(target, "w", encoding="ascii") as fh:
        fh.write(patched)

    assert BEGIN_ANCHOR not in patched
    assert patched.count(SIG_BEGIN) == 1 and patched.count(SIG_END) == 1
    removed = span.count("\n")
    added = block.count("\n")
    print("PASS: replaced the old subsection with the signpost")
    print("      target        : " + target)
    print("      backup        : " + bak)
    print("      lines removed  : ~%d  added: ~%d" % (removed, added))
    print("REMINDER: (1) add \\input{sedenions_generations_section_2026-08-27} "
          "to main.tex after the boson-mass arc;")
    print("          (2) re-point MAP-LABEL sec:flavour-conservation and the "
          "openproblem env in the new section;")
    print("          (3) import both RIS batches; (4) pdflatex x2 + biber, "
          "zero errors, before commit.")


if __name__ == "__main__":
    main()
