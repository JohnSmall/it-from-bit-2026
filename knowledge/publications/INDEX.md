# knowledge/publications/

The author's own prior publications, as LaTeX source. Six items: one
conference paper from 2005 and the five Vaxjo posters, 2022 to 2026. They are
the history of the ideas before the collaboration recorded in `../archive/`
began, and the web project carried them only as PDFs.

## How to treat this directory

**Frozen.** Each item is a self-contained snapshot of a finished, presented
piece of work and is not edited here. Corrections belong upstream, in the
item's own repository, not in this copy.

**Not built by this repository.** The root `.latexmkrc` names only
`paper1/main.tex` and `paper2/...`, so `latexmk` at the root does not touch
these. Each carries its own `.latexmkrc` and `Makefile` from upstream. The
posters need LuaTeX and the Raleway and Lato fonts; the 2005 paper needs the
AIP `aipproc` class, which is bundled with it.

**The bibliographies here are not Zotero exports.** Every `.bib` and `.BIB`
file in this directory came with its item and uses that item's own citation
keys, which do not match `paper1/references.bib`. CLAUDE.md's rule that a
`.bib` is generated and must never be hand-edited applies to the two papers'
bibliographies, not to these. Do not regenerate them, do not reconcile their
keys with Zotero, and do not cite from them in Papers 1 or 2: if one of these
references is wanted in a paper, add it to the Zotero collection in the normal
way.

**Third-party files.** Each poster directory carries Anish Athalye's Gemini
beamerposter theme verbatim: `beamerthemegemini.sty`,
`beamercolortheme*.sty`, and with them the theme's own `LICENSE.md` (MIT,
copyright Anish Athalye) and `README.md`. The `README.md` at the top of a
poster directory documents **the theme**, not the poster --- read `poster.tex`
for the poster. The 2005 paper's `aipproc.cls`, `aip-8s.clo` and `aipxfm.sty`
are the American Institute of Physics template, likewise third-party.

## Provenance

Copied on 2026-09-11 from `~/Documents/tex/my_publications/`, each from a
clean working tree, at the commits below. The `.git` directories were left
behind: they are separate repositories with their own Overleaf-linked GitHub
remotes, and nesting them here would leave broken gitlinks. The upstream
history is recoverable from the remote and commit named in each entry. The
copies are byte-identical to the working trees they came from.

## The items

### 2005 --- CASYS, Liege. `self_ref_2_casys/`

**Why do Quantum Systems Implement Self-referential Logic? A Simple Question
With a Catastrophic Answer.** Sole author, John Small. AIP conference
proceedings class, single file `causality_protection_2.TEX` (80 KB), with
`quantm_self_reference_3.BIB`, 89 entries. Sections: Introduction; Lessons
from current theory; Causality protection and non-computability; Conclusions.
Keywords as filed: causality protection, self-referentiality, entanglement,
spacetime dimensionality, Standard Model.

The abstract argues that self-referentiality is a foundational principle which
causality protection prohibits being observed directly, that quantum mechanics
and general relativity each implement one facet of that protection, and --- the
catastrophic answer of the title --- that there can therefore be no
mathematically consistent theory of quantum gravity. This is the ancestor of
the present framework's "bump in the carpet": the non-computability is
relocated, not removed, and lands at the QM/GR interface.

Upstream: `git@github.com:JohnSmall/self_ref_2_casys.git`,
commit `b31df35967c6582c0748d4a8b01bbeb428963b4f` ("Initial Overleaf Import",
2026-09-11). The import is recent; the paper is not.

### 2022 --- Vaxjo. `Vaxjo_2022_Poster_V3/`

**Self-reference, Circles and the Standard Model.** `poster.tex`, 168 lines;
`poster.bib` and `references.bib`, 22 entries between them. Blocks:
self-reference; self-reference requires negative probability; negative
probability requires complex probability amplitudes; circles; possible routes
to the Standard Model; a universe without foundation.

The derivation chain in its first public form, and the earliest statement of
the self-reference to negative-probability to complex-amplitude sequence that
Paper 1 still runs on.

Upstream: `git@github.com:JohnSmall/Vaxjo_2022_Poster_V3.git`,
commit `8b03878c4f98839914c6fa39a94eea01d9582677` ("Final product",
2022-06-06).

### 2023 --- Vaxjo. `Vaxjo-2023-Poster-V1/`

**Self-reference, Hopf Fibrations and the Standard Model.** `poster.tex`, 158
lines; 43 bib entries. Blocks: the one true interpretation of QM does not
exist; self-reference in the observer; negative probability and complex
amplitudes; negative information and epistemic horizons; circles and division
algebras; division algebras and Hopf fibrations; Hopf fibrations and the
Standard Model; singling out one imaginary octonion; beyond the Standard
Model?

The year the Hopf fibrations enter. "Singling out one imaginary octonion" is
the ancestor of the preferred complex structure that the Koide phase is
measured against.

Upstream: `git@github.com:JohnSmall/Vaxjo-2023-Poster-V1.git`,
commit `a940a81779742c6cdeb119558e532459a74149c2` ("Draft 4", 2023-06-03).

### 2024 --- Vaxjo. `Vaxjo_2024_Poster_V1/`

**Non-locality, non-computability and PR Boxes. A first-person view.**
`poster.tex`, 164 lines; 46 bib entries. Blocks: the first-person perspective
and solipsism; observer, observed and the process of observation; Karl Popper
has a thought; Claude Shannon gets involved; Edwin Jaynes and his quantum
omelette; Popescu and Rohrlich pose a question; bonus point; dedication.

The first-person framing and the Jaynes material that Paper 1 now carries in
`appendix_jaynes_fibration` and in the "quantum omelet" insert spliced into
`what_is_a_quantum_state` on 2026-09-11.

Upstream: `git@github.com:JohnSmall/Vaxjo_2024_Poster_V1.git`,
commit `15c23e33f4acb1e88aaaf834e235047c4ce1386e` ("Initial Overleaf Import",
2026-09-11).

### 2025 --- Vaxjo. `Vaxjo_2025_Poster_V1/`

**A curious connection between non-locality and the relationalist view of
spacetime.** `poster.tex`, 145 lines; `references_2025.bib`, 13 entries.
Blocks: what does locality mean in General Relativity?; a peculiar property of
quantum states; Karl Popper's key idea; joined with another key idea from
Gregory Chaitin; 3 dimensions?; where next?

Chaitin, three dimensions, and the relationalist reading of spacetime: the
line of thought that became Paper 2 and Open Problem `op:three-dimensions`.

Upstream: `git@github.com:JohnSmall/Vaxjo_2025_Poster_V1.git`,
commit `2d85bb247cc68a6dab3aa226bb483c20db935b79` ("Initial Overleaf Import",
2026-09-11).

### 2026 --- Vaxjo. `Vaxjo_2026_Poster_V1/`

**It from Bit via Godel.** `poster.tex`, 294 lines --- the largest of the
posters, and the one that shares Paper 1's title. Two bibliographies,
`references.bib` and `self-ref-2026.bib`, 301 entries between them; the second
is the Mendeley-derived file that `paper1/references.bib` replaced, so its
keys are the pre-migration ones. Two images: a generated illustration and a QR
code to `it-from-bit.vidhya.tv`. Blocks: self-reference; principle results;
Hopf maps, the key link; the non-computable bump shows up as particle mass;
quantitative predictions, bosonic sector; non-observation predictions; quantum
circuits.

The poster and Paper 1 are the same work at two lengths. Where a claim appears
in both, the paper is authoritative --- the poster predates the 2026-09
corrections.

Upstream: `git@github.com:JohnSmall/Vaxjo_2026_Poster_V1.git`,
commit `cf6184eb5fc1368b73b9b4aaa98516dfa54513a9` ("safety", 2026-09-11).
