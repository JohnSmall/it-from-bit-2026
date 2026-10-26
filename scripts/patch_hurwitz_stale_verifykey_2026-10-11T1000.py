#!/usr/bin/env python3
"""patch_hurwitz_stale_verifykey_2026-10-11T1000.py

Paper 1, masses section, the %% provenance block: retire a stale VERIFY-KEY
instruction. It tells a future reader to "replace \autocite{hurwitz1898} below
with the library's existing Hurwitz key before compiling". That replacement was
made on 2026-09-09 by scripts/patch_hurwitz_citekey_2026-09-09T1640.py, whose
EDITED line is already at the head of this file, and the live citation at the
sedenion-step paragraph reads \autocite{hurwitz1898composition}.

So the instruction is not merely redundant, it is misleading: the only
occurrence of the bare key `hurwitz1898` anywhere in paper1 is inside this
comment, and it makes an audit of citation keys report a missing reference that
does not exist. Every live Hurwitz citation in the paper, six of them across
five files, already uses `hurwitz1898composition`.

Comment only. No typeset output changes and the PDF is byte-identical but for
the EDITED header's effect on nothing at all.

One file, one edit. Sentinel-gated: anchor matches exactly once
(whitespace-insensitive), .bak written, "% EDITED" header added, refuses to run
twice. `--check` verifies without writing.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-10-11"
SCRIPT = Path(__file__).name
STAMP = "2026-10-11T1000"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
CHECK = "--check" in sys.argv
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/masses_section_2026-06-08.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


ANCHOR = (r"%%   VERIFY-KEY: replace \autocite{hurwitz1898} below with the library's existing"
          "\n"
          r"%%   Hurwitz key before compiling.")

REPL = (r"%%   KEY RESOLVED 2026-09-09 by scripts/patch_hurwitz_citekey_2026-09-09T1640.py:"
        "\n"
        r"%%   the Hurwitz citation below reads \autocite{hurwitz1898composition}, which is"
        "\n"
        r"%%   the library's key, and nothing further is owed. The unsuffixed form of that"
        "\n"
        r"%%   key resolves to nothing; this comment deliberately does not spell it out,"
        "\n"
        r"%%   because when it did, an audit of the paper's citation keys reported it as a"
        "\n"
        r"%%   missing reference.")


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    hits = list(re.finditer(ws(ANCHOR), text))
    if len(hits) != 1:
        sys.exit("anchor matched %d times" % len(hits))

    # the live citation this comment refers to must already be the resolved key
    if r"\autocite{hurwitz1898composition}" not in text:
        sys.exit("precondition failed: the resolved citation is not in this file")

    m = hits[0]
    new = text[: m.start()] + REPL + text[m.end():]

    if re.search(r"hurwitz1898(?!composition)", new):
        sys.exit("post-check failed: a bare hurwitz1898 survives")
    for s in ["KEY RESOLVED 2026-09-09", "deliberately does not spell it out"]:
        if s not in new:
            sys.exit("post-check failed: %r" % s)

    print("verified: %s (1 edit, comment only)" % TARGET.relative_to(ROOT))
    if CHECK:
        print("--check: nothing written"); return
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s)" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
