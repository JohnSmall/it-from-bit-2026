#!/usr/bin/env python3
"""Hard-wrap a .tex file's prose to the project's ~96-column convention.

Usage:  python3 scripts/rewrap_tex_2026-09-11T1000.py <file.tex> [--apply]

Files carried over from Overleaf keep its soft-wrapping: one paragraph is one
very long line. That is invisible in an editor set to `nowrap`, and worse, it
makes every one-word change show in git as a whole-paragraph diff. The rest of
Paper 1 is hard-wrapped at 95-99 columns; this brings a file into line.

Only the line breaks change. Specifically it will NOT break:
  * inside braces -- so \\autocite{a, b} and \\S\\ref{sec:x} stay intact;
  * inside inline math $...$;
  * a comment line, or any line beginning with % (left exactly as found);
  * inside a verbatim-like or tabular-like environment;
  * a line that is a lone command such as \\input{...} or \\label{...}.

Paragraphs are blank-line separated and reflowed independently, so blank lines,
environment boundaries and comment placement are all preserved.

Verify with pdftotext before and after: the rendered text must be identical.
"""

import re
import shutil
import sys

WIDTH = 96
NOWRAP_ENVS = {"verbatim", "lstlisting", "tabular", "align", "equation", "eqnarray",
               "array", "matrix", "pmatrix", "bmatrix", "tikzpicture", "figure", "table"}


def breakable(line):
    """Yield indices of spaces at brace depth 0 and outside inline math."""
    depth = 0
    math = False
    for i, ch in enumerate(line):
        if ch == "\\":
            continue
        if ch == "$" and (i == 0 or line[i - 1] != "\\"):
            math = not math
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth = max(0, depth - 1)
        elif ch == " " and depth == 0 and not math:
            yield i


def wrap_paragraph(text, width=WIDTH):
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    out = []
    while len(text) > width:
        cuts = [i for i in breakable(text) if i <= width]
        if not cuts:                       # no legal break inside the budget
            later = [i for i in breakable(text) if i > width]
            if not later:
                break
            cuts = [later[0]]
        cut = cuts[-1]
        out.append(text[:cut])
        text = text[cut + 1:]
    if text:
        out.append(text)
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path, apply = sys.argv[1], "--apply" in sys.argv
    src = open(path, encoding="utf-8").read()
    lines = src.split("\n")

    out, para, env = [], [], []
    def flush():
        if para:
            out.extend(wrap_paragraph(" ".join(para)))
            para.clear()

    for line in lines:
        s = line.strip()
        m_begin = re.match(r"\\begin\{([^}]+)\}", s)
        m_end = re.match(r"\\end\{([^}]+)\}", s)
        if m_begin and m_begin.group(1) in NOWRAP_ENVS:
            flush(); env.append(m_begin.group(1)); out.append(line); continue
        if env:
            out.append(line)
            if m_end and m_end.group(1) == env[-1]:
                env.pop()
            continue
        if not s:
            flush(); out.append(""); continue
        if s.startswith("%"):
            flush(); out.append(line); continue
        if re.fullmatch(r"\\[a-zA-Z@]+(\[[^\]]*\])?(\{[^{}]*\})*\*?", s):
            flush(); out.append(line); continue     # lone command on its own line
        para.append(s)
    flush()

    new = "\n".join(out)
    if not new.endswith("\n"):
        new += "\n"

    before = [len(l) for l in src.split("\n")]
    after = [len(l) for l in new.split("\n")]
    print(f"  {path}")
    print(f"    lines {len(before)} -> {len(after)}")
    print(f"    longest {max(before)} -> {max(after)}")
    print(f"    over {WIDTH} chars: {sum(1 for n in before if n > WIDTH)} -> {sum(1 for n in after if n > WIDTH)}")
    words_b = len(re.sub(r"\s+", " ", src).split())
    words_a = len(re.sub(r"\s+", " ", new).split())
    print(f"    word count {words_b} -> {words_a} {'(unchanged)' if words_b == words_a else '** CHANGED **'}")
    if words_b != words_a:
        sys.exit("REFUSING: word count changed; not written")

    if apply:
        shutil.copy2(path, path + ".bak")
        open(path, "w", encoding="utf-8").write(new)
        print(f"    written (backup {path}.bak)")
    else:
        print("    (dry run -- pass --apply to write)")


if __name__ == "__main__":
    main()
