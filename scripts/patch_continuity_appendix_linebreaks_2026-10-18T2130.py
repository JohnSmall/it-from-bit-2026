#!/usr/bin/env python3
"""Rephrase three overfull paragraphs found by the appendix's first build.

Work only inside the appendix's unique BEGIN/END sentinels. Keep the first
script's scaffold backup; this stage writes its own pre-edit .bak. Refuse a
second run. The changes preserve the scientific claims and status labels.
"""

from pathlib import Path
import re
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "paper1/appendices/appendix_continuity_self_reference_2026-10-18T2119.tex"
SCRIPT = "scripts/patch_continuity_appendix_linebreaks_2026-10-18T2130.py"
HEADER = "% EDITED 2026-10-18 " + SCRIPT + "\n"
BACKUP = TARGET.with_name(TARGET.name + ".2026-10-18T2130.bak")
BEGIN = "% BEGIN CONTINUITY SELF REFERENCE APPENDIX"
END = "% END CONTINUITY SELF REFERENCE APPENDIX"
CHANGES = (
    ("Each downstream arrow retains its own premises, including the representation\n"
     "and norm-preservation assumptions used to select the metric.",
     "Each downstream arrow retains its own premises, including assumptions\n"
     "about how states are represented and which transformations preserve the norm."),
    ("The liar and truth-teller suggest a comparison between inconsistent Boolean\n"
     "self-assignment and consistent but underdetermined self-assignment.",
     "The liar and truth-teller suggest a comparison between a Boolean\n"
     "self-assignment that is inconsistent and one that is consistent but\n"
     "underdetermined."),
    ("Specify an operational condition $\\mathcal R$ expressing the limitation\n"
     "on self-description.",
     "Specify an operational condition $\\mathcal R$ that states the limits of\n"
     "an observer's self-description."),
)


def unique(text, anchor):
    pattern = re.compile(r"\s+".join(re.escape(p) for p in anchor.split()))
    matches = list(pattern.finditer(text))
    assert len(matches) == 1, (anchor, len(matches))
    return matches[0]


def main():
    text = TARGET.read_text()
    if HEADER.strip() in text or BACKUP.exists():
        sys.exit("REFUSING: appendix linebreak patch already applied")
    begin, end = unique(text, BEGIN), unique(text, END)
    assert begin.end() < end.start()
    body = text[begin.end():end.start()]
    for old, new in CHANGES:
        match = unique(body, old)
        body = body[:match.start()] + new + body[match.end():]
    result = HEADER + text[:begin.end()] + body + text[end.start():]
    unique(result, BEGIN)
    unique(result, END)
    shutil.copy2(TARGET, BACKUP)
    TARGET.write_text(result)
    print("patched " + str(TARGET.relative_to(ROOT)))
    print("backup: " + str(BACKUP.relative_to(ROOT)))
    print("Rephrased 3 overfull paragraphs; mathematical claims and labels unchanged")
    print("PATCH: PASS")


if __name__ == "__main__":
    main()
