#!/usr/bin/env python3
"""Restore two passages the zoo signpost patch removed.

`patch_zoo_sedenion_pointer_2026-08-25T0700.py` replaced the old subsection
`The extra wire: how a deeper mechanism announced itself` with a short forward
pointer. Almost everything it removed is said elsewhere -- the discovery
narrative and the shadow relation moved into the sedenion section, the depth
ordering is in the zoo's own closing subsection and in the masses section, the
dressing result is in the masses section verbatim, and the fourth-generation
prediction is in the predictions section. Two passages were not:

  1. The comparison that prices the fourth-generation claim against the
     experimental bound it beats. The predictions section states the claim and
     its refutation criterion but drops the comparison, so without this
     sentence nothing in the paper says how much stronger the claim is.

  2. The methodological paragraph, on the executable-representation discipline
     having forced the finding. Rhetoric rather than result, but distinctive,
     and the discipline it describes is one the paper argues for elsewhere.

Both are restored verbatim from `particle_zoo_section_2026-06-08.tex.bak`, the
backup that patch wrote, in their original relative order and inside the
signpost, before its SIGNPOST-END sentinel.

The methodological paragraph opened "But the methodological point stands on its
own" in a context where "But" contrasted with a deferral to the follow-up
paper. In the signpost it follows the convergence sentence, which it contrasts
with just as well, so the text is unaltered.

Anchor matched whitespace-insensitively, exactly once. A .bak is written, an
"% EDITED" header prepended, and the header makes the script refuse to run twice.
"""

import re
import shutil
import sys

DATE = "2026-09-12"
SCRIPT = "scripts/patch_restore_zoo_signpost_prose_2026-09-12T2300.py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
DEST = "paper1/particle_zoo_section_2026-06-08.tex"
ANCHOR = "% SIGNPOST-END sedenion-pointer 2026-08-25T0700"

RESTORED = r"""
But the methodological point stands on its own and we state it plainly: this is how a
research programme works --- try an idea, find something better, replace the first --- and the
finding was forced by the paper's own discipline. The rule that every structure must compile to a
runnable circuit acted as a critic: the executable representation refused to let the rough edge
stay hidden.

One prediction is immediate and sharp: there are four classes and only three are chiral, so there is
no fourth generation at any scale --- a stronger statement than the $Z$-width bound, and falsifiable.
"""


def main():
    text = open(DEST, encoding="utf-8").read()
    if HEADER.strip() in text:
        sys.exit("REFUSING: %s already patched by %s" % (DEST, SCRIPT))
    if "methodological point stands on its own" in text:
        sys.exit("REFUSING: the methodological paragraph is already present")
    if "$Z$-width bound" in text:
        sys.exit("REFUSING: the Z-width sentence is already present")

    pat = re.compile(r"\s+".join(re.escape(p) for p in ANCHOR.split()))
    n = len(pat.findall(text))
    if n != 1:
        sys.exit("REFUSING: the SIGNPOST-END sentinel matched %d times, expected 1" % n)
    m = pat.search(text)

    text = text[:m.start()] + RESTORED.strip("\n") + "\n\n" + text[m.start():]

    for probe in ("methodological point stands on its own", "$Z$-width bound"):
        if text.count(probe) != 1:
            sys.exit("REFUSING: %r landed %d times" % (probe, text.count(probe)))
    if text.count(ANCHOR) != 1:
        sys.exit("REFUSING: the sentinel was disturbed")

    shutil.copy2(DEST, DEST + ".bak2")
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(HEADER + text)
    print("restored both passages into the signpost in %s" % DEST)


if __name__ == "__main__":
    main()
