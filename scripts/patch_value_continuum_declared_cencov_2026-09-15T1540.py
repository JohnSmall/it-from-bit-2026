#!/usr/bin/env python3
"""Declare the value continuum once, at the Shannon step; consume it three times; add the
statistical route to the L^2 metric (Cencov's theorem and the every-basis lemma).

Companion to knowledge/sessions/continuity_connected_state_space_2026-09-15T1430.md (third
edit). JS, 2026-09-15: the analytic continuation of the logarithm that yields complex
amplitudes is unique only because credences range over a connected domain, so the complex
numbers do not imply the value continuum, they consume it; the premise should be declared once
where it first does work and referenced where it is consumed. And: with that premise the L^2
metric is justified by two routes that share only it.

Four files, one header each, one run only.

paper1/what_is_a_quantum_state.tex
  1. After "that is why quantum probabilities have complex amplitudes": the declared premise
     (credences take every value in [0,1]; self-referential ignorance is not rationed, unlike
     the epistricted theories), why the continuation needs it, and where it is consumed.
paper1/continuity_section_2026-07-04.tex
  2. op:limit-realisability: one sentence after "What remains open is the first." saying the
     premise is the Shannon step's, consumed at the continuation, here, and in the
     statistical route; the environment body re-filled.
paper1/L2_metric_global_phase_section_2026_06_07.tex
  3. The status paragraph: the premise is the Shannon step's and the statistical route
     consumes it and nothing else open.
  4. The closing paragraph of "Hardy's independent route": both roads start from continuity;
     a third starts from the value continuum.
  5. New \\subsection{The statistical route: Cencov's theorem and the every-basis lemma}
     (sec:cencov-route) before "The Hopf fibration and the Bloch sphere": Cencov's theorem
     (cited to Bengtsson and Zyczkowski, the one source for it in the bibliography), the
     every-basis lemma with proof (lem:every-basis), and the two-legs status paragraph.
paper1/derivation_of_the_quantum_postulates.tex
  6. "by an independent route" becomes "by a second route from the same continuity premise",
     with the statistical route named; "the independent isometry and counting arguments"
     becomes "the isometry and counting arguments and ... the statistical route".

Anchors are matched whitespace-insensitively and must match exactly once. Prose paragraphs
are re-filled to 96 columns where the block holds no structure; the Shannon-step paragraph
(which carries a \\label line) and the L^2 status paragraph (which adjoins its \\section
line) are not re-filled. A dated .bak is written per file, a "% EDITED" header is prepended,
and already-patched files are skipped.
"""

import re
import shutil
import sys
import textwrap

DATE = "2026-09-15"
STAMP = "2026-09-15T1540"
SCRIPT = "scripts/patch_value_continuum_declared_cencov_" + STAMP + ".py"
HEADER = "% EDITED " + DATE + " " + SCRIPT + "\n"
WIDTH = 96

WIQS = "paper1/what_is_a_quantum_state.tex"
CONT = "paper1/continuity_section_2026-07-04.tex"
L2 = "paper1/L2_metric_global_phase_section_2026_06_07.tex"
POST = "paper1/derivation_of_the_quantum_postulates.tex"


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


def refill_paragraph_at(text, marker, allow_inline_paragraph=False):
    i = text.index(marker)
    start = text.rfind("\n\n", 0, i) + 2
    end = text.find("\n\n", i)
    para = text[start:end]
    banned = ["\\begin", "\\end", "\\item", "%", "\\subsection", "\\section", "\\label"]
    if not allow_inline_paragraph:
        banned.append("\\paragraph")
    for line in para.splitlines():
        if line.lstrip().startswith(tuple(banned)):
            sys.exit("REFUSING: paragraph to re-fill contains structure:\n  %s" % line)
    return text[:start] + fill(para) + text[end:]


def refill_env_body(text, begin_line, end_line):
    """Re-fill the prose between an environment's \\begin line and its \\end line."""
    i = text.index(begin_line)
    j = text.index(end_line, i)
    body = text[i + len(begin_line):j]
    for line in body.splitlines():
        if line.lstrip().startswith(("\\begin", "\\end", "\\item", "%", "\\label")):
            sys.exit("REFUSING: environment body contains structure:\n  %s" % line)
    return text[:i + len(begin_line)] + fill(body) + "\n" + text[j:]


# ------------------------------------------------------------------ 1. Shannon step
OLD_SHANNON = r"""
into the log function. But that can only work if we use analytic continuation to extend the
domain of the log function the complex plane and that is why quantum probabilities have complex
amplitudes.
"""
NEW_SHANNON = (r"""
into the log function. But that can only work if we use analytic continuation to extend the
domain of the log function the complex plane and that is why quantum probabilities have complex
amplitudes.
""".strip() + "\n" + fill(r"""
One premise is declared here, because everything downstream consumes it. Analytic continuation
is an operation on a function defined on a connected domain, and its value at a negative entry
is unique only because credences range over such a domain. The framework takes it that an
embedded observer's credence in a proposition about itself can take every value in $[0,1]$ ---
self-referential ignorance is not rationed into whole bits, as it is in the epistricted theories
\autocite{spekkens2007toy} --- so that the surprisal is an analytic function on a continuum
rather than a table of values that any extension would fit. The same premise is what later makes
the pure states a connected space (\S\ref{sec:continuity}) and the probability simplex a
manifold (\S\ref{sec:cencov-route}); whether self-reference derives it is Open
Problem~\ref{op:limit-realisability}.
"""))

# ------------------------------------------------------------------ 2. op:limit-realisability
OLD_OP_SENT = r"""
closedness is the framework's adopted stance, the
operational completion. What remains open is the first. Derive, from the self-referential
"""
NEW_OP_SENT = r"""
closedness is the framework's adopted stance, the operational completion. What remains open is the
first. The premise is not new to this section: it is the one the Shannon step declares, since the
continuation of the logarithm that yields complex amplitudes is unique only because credences
range over a connected domain (\S\ref{sec:complex-amplitudes}); declared once there, it is
consumed at the continuation, here, and in the statistical route to the $L^{2}$ metric
(\S\ref{sec:cencov-route}). Derive, from the self-referential
""".strip()
OP_BEGIN = r"\begin{openproblem}[The value continuum from self-reference]\label{op:limit-realisability}" + "\n"
OP_END = r"\end{openproblem}"

# ------------------------------------------------------------------ 3. L2 status paragraph
OLD_L2_STATUS = r"""
value continuum, remains open. Assuming that premise can be proved, everything below inherits the
derivation; we carry that status, and do not upgrade it.
"""
NEW_L2_STATUS = r"""
value continuum, remains open. That premise is the one the Shannon step declares
(\S\ref{sec:complex-amplitudes}), and \S\ref{sec:cencov-route} below reaches the same metric by a
second route that consumes it and nothing else that is open. Assuming that premise can be proved,
everything below inherits the derivation; we carry that status, and do not upgrade it.
""".strip()

# ------------------------------------------------------------------ 4. Hardy's route closing
OLD_HARDY_END = r"should be cited as two roads rather than one road traversed twice."
NEW_HARDY_END = (r"should be cited as two roads rather than one road traversed twice. Both roads start from "
                 r"continuity. A third, in the next subsection, starts one step earlier, from the value "
                 r"continuum that continuity itself rests on, and reaches the same metric without passing "
                 r"through the transformation group at all.")

# ------------------------------------------------------------------ 5. the new subsection
ANCHOR_HOPF = r"\subsection{The Hopf fibration and the Bloch sphere}"
NEW_SUBSECTION = "\n".join([
    r"\subsection{The statistical route: \v{C}encov's theorem and the every-basis lemma}",
    r"\label{sec:cencov-route}",
    "",
    fill(r"""
The value continuum that \S\ref{sec:continuity} isolates as the one open premise reaches the
$L^{2}$ metric on its own, by a route that uses no transformation group. \v{C}encov's theorem
states that the only Riemannian metric on the simplex of probability distributions invariant
under coarse-graining --- under the Markov maps that merge or relabel outcomes --- is the
Fisher--Rao metric \autocite{bengtsson2006geometry}, and in the coordinates $x_{k} =
\sqrt{p_{k}}$ the Fisher--Rao metric is the round metric on the positive orthant of the unit
sphere. The premise the theorem consumes is that the simplex is a manifold, which is the value
continuum declared in \S\ref{sec:complex-amplitudes}, and the principle it uses, that
distinguishability does not depend on how outcomes are grouped, is one the Shannon bookkeeper of
that section already grants. What it does not supply is the passage from one orthant to the
whole projective space; that is the following lemma.
"""),
    "",
    r"\begin{lemma}[The every-basis lemma]\label{lem:every-basis}",
    fill(r"""
Let $g$ be a Riemannian metric on $\mathbb{CP}^{K-1}$ whose restriction to the positive real
orthant of every orthonormal basis --- the states $\sum_{k}\sqrt{p_{k}}\,e_{k}$ with $p$ in the
simplex --- is the Fisher--Rao metric. Then $g$ is the Fubini--Study metric, whose linear lift is
the $L^{2}$ inner product.
"""),
    r"\end{lemma}",
    "",
    r"\begin{proof}",
    fill(r"""
A tangent vector to $\mathbb{CP}^{K-1}$ at a state $\psi$ is represented by a vector $\phi$
orthogonal to $\psi$, and the curve $t \mapsto \cos t\,\psi + \sin t\,\phi$ with real $t$ lies in
the positive orthant of any orthonormal basis that contains $\psi$ and $\phi$. Along that curve
the Fisher--Rao metric is the round metric of the sphere in the coordinates $\sqrt{p}$, which is
the Fubini--Study metric restricted to real amplitudes; so $g$ and the Fubini--Study metric agree
on every tangent vector at every point, the direction $i\phi$ being reached by the basis that
contains $i\phi$ in place of $\phi$.
"""),
    r"\end{proof}",
    "",
    fill(r"""
The lemma's premise, that every orthonormal basis is a legitimate measurement and none is
privileged, is the fourth face of the pre-measurement regime seen from the measurement side
(\S\ref{sec:continuity}); in the stabiliser fragment of quantum theory it fails in the same way
everything else does, only the Pauli bases being measurements there. So the $L^{2}$ metric now
rests on two legs that share exactly one premise. Through reversible continuity it uses the value
continuum, closure and homogeneity (Proposition~\ref{prop:lamperti}); through \v{C}encov it uses
the value continuum, coarse-graining invariance and the equal standing of bases
(Lemma~\ref{lem:every-basis}). Neither leg needs anything else that is open, and nothing could
avoid the continuum, since a metric is a statement about one. That is the status of everything
downstream of this section, the Hopf fibrations included: derived from a premise every physicist
grants and the framework has not yet derived from self-reference
(Open Problem~\ref{op:limit-realisability}).
"""),
    "",
    ANCHOR_HOPF,
])

# ------------------------------------------------------------------ 6. postulates
OLD_POST_A = r"counting reaches the same quadratic norm by an independent route \autocite{Hardy2001a}."
NEW_POST_A = (r"counting reaches the same quadratic norm by a second route from the same continuity premise "
              r"\autocite{Hardy2001a}, and \v{C}encov's theorem with the every-basis lemma reaches it from "
              r"the value continuum alone (\S\ref{sec:cencov-route}).")
OLD_POST_B = r"carried jointly with the independent isometry and counting arguments."
NEW_POST_B = r"carried jointly with the isometry and counting arguments and with the statistical route."


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
    return replace_once(text, OLD_SHANNON, NEW_SHANNON)


def edit_cont(text):
    text = replace_once(text, OLD_OP_SENT, NEW_OP_SENT)
    return refill_env_body(text, OP_BEGIN, OP_END)


def edit_l2(text):
    text = replace_once(text, OLD_L2_STATUS, NEW_L2_STATUS)
    text = replace_once(text, OLD_HARDY_END, NEW_HARDY_END)
    text = refill_paragraph_at(text, "Both roads start from continuity.")
    if text.count(ANCHOR_HOPF) != 1:
        sys.exit("REFUSING: Hopf subsection anchor count %d" % text.count(ANCHOR_HOPF))
    text = text.replace(ANCHOR_HOPF, NEW_SUBSECTION)
    for lab in (r"\label{sec:cencov-route}", r"\label{lem:every-basis}", r"\label{prop:lamperti}"):
        if text.count(lab) != 1:
            sys.exit("REFUSING: %s occurs %d times" % (lab, text.count(lab)))
    return text


def edit_post(text):
    text = replace_once(text, OLD_POST_A, NEW_POST_A)
    text = replace_once(text, OLD_POST_B, NEW_POST_B)
    return refill_paragraph_at(text, "every-basis lemma reaches it", allow_inline_paragraph=True)


def main():
    patch(WIQS, edit_wiqs, ["self-referential ignorance is not rationed into whole bits"])
    patch(CONT, edit_cont, [r"\S\ref{sec:cencov-route}"])
    patch(L2, edit_l2, [r"\label{sec:cencov-route}", r"\autocite{bengtsson2006geometry}"])
    patch(POST, edit_post, [r"\S\ref{sec:cencov-route}"])


if __name__ == "__main__":
    main()
