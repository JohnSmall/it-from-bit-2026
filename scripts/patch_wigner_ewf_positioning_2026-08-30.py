#!/usr/bin/env python3
"""
patch_wigner_ewf_positioning_2026-08-30.py

Inserts the SPLICE block of wigner_ewf_positioning_splice_2026-08-30.tex into
wigners_friend_in_the_hopf_picture_2026-06-13.tex, immediately BEFORE the
chain-type coda, so the section reads:

    ... Two cautions close the argument. ... both can check.

    [sec:wf-ewf   -- the extended-friends positioning]   <-- this patch

    [sec:wf-chain-type -- where the chain goes next]     <-- 08-27 patch

ORDER REQUIREMENT: patch_wigner_chain_type_2026-08-27.py must have been
applied FIRST. This patch anchors on the chain coda's SPLICE-BEGIN line and
REFUSES if it is absent, so the two insertions cannot land out of order.

Gates (any failure => no write, exit 1):
  - target and splice exist and are pure ASCII;
  - the chain-type sentinel line occurs EXACTLY once in the target
    (absent => "apply patch_wigner_chain_type_2026-08-27.py first");
  - idempotence: the label "sec:wf-ewf" absent from the target;
  - the splice file contains exactly one SPLICE-BEGIN/END pair.
Writes <target>.bak_2026-08-30 before modifying, and prints the three lines
on each side of the inserted block for eyeballing.

Usage:
    python3 patch_wigner_ewf_positioning_2026-08-30.py \
        [wigners_friend_in_the_hopf_picture_2026-06-13.tex] \
        [wigner_ewf_positioning_splice_2026-08-30.tex]
"""
import shutil
import sys

CHAIN_SENTINEL = "% SPLICE-BEGIN wf-chain-type 2026-08-27"
IDEMPOTENCE_MARK = "sec:wf-ewf"
SIG_BEGIN = "% SPLICE-BEGIN wf-ewf 2026-08-30"
SIG_END = "% SPLICE-END wf-ewf 2026-08-30"

DEFAULT_TARGET = "wigners_friend_in_the_hopf_picture_2026-06-13.tex"
DEFAULT_SPLICE = "wigner_ewf_positioning_splice_2026-08-30.tex"


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
    n = text.count(CHAIN_SENTINEL)
    if n == 0:
        fail("chain-type coda not found -- apply "
             "patch_wigner_chain_type_2026-08-27.py first")
    if n != 1:
        fail("chain-type sentinel found %d times (need exactly 1)" % n)
    if stext.count(SIG_BEGIN) != 1 or stext.count(SIG_END) != 1:
        fail("splice must contain exactly one SPLICE-BEGIN/END pair")

    block = stext[stext.index(SIG_BEGIN):stext.index(SIG_END) + len(SIG_END)]
    block = block.rstrip("\n") + "\n"

    pos = text.index(CHAIN_SENTINEL)
    patched = text[:pos] + block + "\n" + text[pos:]

    bak = target + ".bak_2026-08-30"
    shutil.copyfile(target, bak)
    with open(target, "w", encoding="ascii") as fh:
        fh.write(patched)

    assert patched.count(SIG_BEGIN) == 1 and patched.count(SIG_END) == 1
    assert patched.index(SIG_END) < patched.index(CHAIN_SENTINEL)
    lines = patched.split("\n")
    b = next(i for i, ln in enumerate(lines) if SIG_BEGIN in ln)
    e = next(i for i, ln in enumerate(lines) if SIG_END in ln)
    print("PASS: positioning subsection inserted before the chain-type coda")
    print("      target : " + target)
    print("      backup : " + bak)
    print("      context before the block:")
    for ln in lines[max(0, b - 3):b]:
        print("        | " + ln)
    print("      ... block (%d lines) ..." % (e - b + 1))
    print("      context after the block:")
    for ln in lines[e + 1:e + 4]:
        print("        | " + ln)
    print("REMINDER: (1) import extended_wigners_friend_refs_2026-08-30.ris")
    print("          AND ewf_splice_supplementary_refs_2026-08-30.ris;")
    print("          (2) all EWF keys are VERIFY-flagged -- refs-first gate;")
    print("          (3) pdflatex x2 + biber, zero errors, before commit.")


if __name__ == "__main__":
    main()
