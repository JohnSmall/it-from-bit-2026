#!/usr/bin/env python3
"""
patch_wigner_chain_type_2026-08-27.py

Inserts the SPLICE block of wigner_chain_type_splice_2026-08-27.tex at the
end of sec:wigners-friend in wigners_friend_in_the_hopf_picture_2026-06-13.tex,
and re-words one phrase so the existing closing paragraph stays true.

Two edits, both anchor-gated:
  (1) "Two cautions close the section."  ->  "Two cautions close the argument."
  (2) insert the splice block after the line that ends the cautions
      paragraph: "observers never disagree about anything both can check."

Gates (any failure => no write, exit 1):
  - target and splice exist and are pure ASCII;
  - each anchor occurs EXACTLY once in the target (the July lesson: an
    anchor that also occurs in the header comments must be caught here);
  - idempotence: the splice's label "sec:wf-chain-type" absent from target;
  - the splice file contains exactly one SPLICE-BEGIN/END pair.
Writes <target>.bak_2026-08-27 before modifying, and prints the five lines
following the insertion point so the tail can be eyeballed.

Usage:
    python3 patch_wigner_chain_type_2026-08-27.py \
        [wigners_friend_in_the_hopf_picture_2026-06-13.tex] \
        [wigner_chain_type_splice_2026-08-27.tex]
"""
import shutil
import sys

PHRASE_OLD = "Two cautions close the section."
PHRASE_NEW = "Two cautions close the argument."
INSERT_ANCHOR = "observers never disagree about anything both can check."
IDEMPOTENCE_MARK = "sec:wf-chain-type"
SIG_BEGIN = "% SPLICE-BEGIN wf-chain-type 2026-08-27"
SIG_END = "% SPLICE-END wf-chain-type 2026-08-27"

DEFAULT_TARGET = "wigners_friend_in_the_hopf_picture_2026-06-13.tex"
DEFAULT_SPLICE = "wigner_chain_type_splice_2026-08-27.tex"


def fail(msg):
    print("FAIL: " + msg)
    sys.exit(1)


def read_ascii(path, what):
    try:
        with open(path, "r", encoding="ascii") as fh:
            return fh.read()
    except FileNotFoundError:
        fail("%s not found: %s" % (what, path))
    except UnicodeDecodeError:
        fail("%s is not pure ASCII: %s" % (what, path))


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TARGET
    splice = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_SPLICE
    text = read_ascii(target, "target")
    stext = read_ascii(splice, "splice")

    if IDEMPOTENCE_MARK in text:
        fail("already applied (label %s present)" % IDEMPOTENCE_MARK)
    if stext.count(SIG_BEGIN) != 1 or stext.count(SIG_END) != 1:
        fail("splice must contain exactly one SPLICE-BEGIN/END pair")
    block = stext[stext.index(SIG_BEGIN):stext.index(SIG_END) + len(SIG_END)]
    block = block.rstrip("\n") + "\n"

    for anchor in (PHRASE_OLD, INSERT_ANCHOR):
        n = text.count(anchor)
        if n != 1:
            fail("anchor found %d times (need exactly 1): %r" % (n, anchor))

    # edit (1)
    patched = text.replace(PHRASE_OLD, PHRASE_NEW, 1)
    # edit (2): insert after the end of the line containing the anchor
    pos = patched.index(INSERT_ANCHOR) + len(INSERT_ANCHOR)
    eol = patched.find("\n", pos)
    if eol == -1:
        eol = len(patched)
        patched = patched + "\n"
    else:
        eol += 1
    patched = patched[:eol] + "\n" + block + patched[eol:]

    bak = target + ".bak_2026-08-27"
    shutil.copyfile(target, bak)
    with open(target, "w", encoding="ascii") as fh:
        fh.write(patched)

    assert patched.count(PHRASE_NEW) == 1 and PHRASE_OLD not in patched
    assert patched.count(SIG_BEGIN) == 1 and patched.count(SIG_END) == 1
    tail_start = patched.index(SIG_END) + len(SIG_END)
    following = patched[tail_start:].split("\n")[1:6]
    print("PASS: coda inserted and closing phrase re-worded")
    print("      target : " + target)
    print("      backup : " + bak)
    print("      lines following the splice (should be blank or end-of-file):")
    for ln in following:
        print("        | " + ln)
    print("REMINDER: (1) re-point MAP-LABEL app:notebook-record in the splice;")
    print("          (2) import cayley_dickson_automorphism_refs_2026-08-27.ris;")
    print("          (3) sec:sedenions-generations must be the 2026-08-27 revision;")
    print("          (4) pdflatex x2 + biber, zero errors, before commit.")


if __name__ == "__main__":
    main()
