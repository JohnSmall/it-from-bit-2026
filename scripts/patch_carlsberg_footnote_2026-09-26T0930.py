#!/usr/bin/env python3
"""patch_carlsberg_footnote_2026-09-26T0930.py

paper1/what_is_a_quantum_state.tex: JS's footnote on the Many Worlds line
(2026-09-26): "followers of the Many Worlds Interpretation in the evening after
few beers" becomes "... after a few beers (Carlsberg of course\\footnote{The
Carlsberg Foundation was a prominent supporter of Bohr in his development of
quantum mechanics \\autocite{pais2002physicsdenmark}.})". The key is in
bib/pais_physics_in_denmark_ref_2026-09-26T0900.bib (verified; support quoted
there) and is undefined until imported and re-exported.

Sentinel-gated: anchor matches once (whitespace-insensitive), .bak written,
"% EDITED" header, refuses to run twice.
"""
import re
import shutil
import sys
from pathlib import Path

DATE = "2026-09-26"
SCRIPT = Path(__file__).name
STAMP = "2026-09-26T0930"
HEADER = "%% EDITED %s scripts/%s\n" % (DATE, SCRIPT)
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/what_is_a_quantum_state.tex"


def ws(s):
    return r"\s+".join(re.escape(tok) for tok in s.split())


ANCHOR = r"afternoon, and followers of the Many Worlds Interpretation in the evening after few beers. Each"
REPL = (r"afternoon, and followers of the Many Worlds Interpretation in the evening after a few beers"
        "\n" r"(Carlsberg of course\footnote{The Carlsberg Foundation was a prominent supporter of Bohr in his"
        "\n" r"development of quantum mechanics \autocite{pais2002physicsdenmark}.}). Each")


def main():
    text = TARGET.read_text()
    if HEADER in text:
        sys.exit("%s already carries %s; refusing to run twice" % (TARGET.name, SCRIPT))
    hits = list(re.finditer(ws(ANCHOR), text))
    if len(hits) != 1:
        sys.exit("anchor matched %d times" % len(hits))
    m = hits[0]
    new = text[: m.start()] + REPL + text[m.end():]
    if new.count("pais2002physicsdenmark") != 1:
        sys.exit("post-check failed")
    bak = TARGET.with_name(TARGET.name + "." + STAMP + ".bak")
    shutil.copyfile(TARGET, bak)
    TARGET.write_text(HEADER + new)
    print("patched: %s (backup %s)" % (TARGET.relative_to(ROOT), bak.name))


if __name__ == "__main__":
    main()
