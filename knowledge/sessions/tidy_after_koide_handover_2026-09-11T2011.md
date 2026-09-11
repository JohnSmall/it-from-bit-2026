# Session note: tidying after the Koide handover

Date: 2026-09-11T2011. Session: Claude Code (Opus 5), housekeeping, taking
over from the Fable session recorded at `koide_flat_direction_2026-09-11T1900.md`.
Starting points as given by JS: `notes/todo.md` and the two Koide session
notes of the same date.

## 1. The two unverified references, both now cleared

`koide_flat_direction_2026-09-11T1900.md` carried Brannen 2006 and Sumino 2009
as VERIFY-CITE, neither read, neither in the bibliography.

**Sumino.** Verified against Crossref and arXiv; the recollection in the note
was exact.

- `sumino2009family`: "Family gauge symmetry and Koide's mass formula",
  Yukinari Sumino, Physics Letters B **671** (4-5), 477--480, February 2009,
  doi 10.1016/j.physletb.2008.12.060, arXiv:0812.2090.
- `sumino2009origin`: "Family gauge symmetry as an origin of Koide's mass
  formula and charged lepton spectrum", JHEP **2009** (05), 075, 18 May 2009,
  doi 10.1088/1126-6708/2009/05/075, arXiv:0812.2103.

**Brannen.** Read in full: `https://brannenworks.com/MASSES2.pdf`, "The Lepton
Masses", Carl A. Brannen, Liquafaction Corp., Woodinville, WA, dated 2 May
2006 on the document. Unpublished, no DOI.

It carries more than the number. Brannen writes the square-root masses as the
eigenvalues of a circulant Hermitian matrix with unit diagonal and off-diagonal
entries `eta exp(+/- i delta)`:

    Gamma(mu, eta, delta) |n> = mu (1 + 2 eta cos(delta + 2 pi n / 3)) |n>

fits `eta_1^2 = 0.500003(23)` and `delta_1 = 0.2222220(19)` to the PDG
charged-lepton masses, and says in terms: "a new coincidence is that delta_1
is close to 2/9, a fact that went unnoticed until this author discovered it in
2005". Assuming the Koide relation exact he tightens this to
`delta_1 = 0.22222204715(312)` from the MeV data and `0.22222204717(48)` from
AMU.

So Brannen 2006 already contains, over the complex numbers: the framework's
`alpha = 2 eta = sqrt 2` (his `eta^2 = 1/2`), the phase `delta = 2/9`, and the
matrix-eigenvalue formulation. **That is the complex case of
`prop:koide-jordan`**, which the 1900 session established yesterday as the
spectrum of the democratic element of J3(O) and, over C, as the spectrum of the
Gram matrix of three mutually unbiased states. The octonionic lift, the
Bargmann-invariant reading, the positivity bound `|Phi| <= pi/4` and the
transcendence argument are the framework's own; the complex skeleton is
Brannen's and is nineteen years old.

The masses section currently credits Koide 1983 for the ratio and nobody for
any of this. How much to credit and where is JS's call, which is why nothing
was patched here.

One further VERIFY-CITE from the 1900 note falls out as a by-product: the tau
mass "1776.99 +/- 0.29 MeV, around 2006" used in that session's sensitivity
line is Brannen's quoted PDG value, and is confirmed --- with the correction
that it is asymmetric, `1776.99 (+0.29 -0.26) MeV`.

`bib/koide_attribution_refs_2026-09-11T2011.bib` holds all three entries. It is
the first batch written under the `.bib` rule; the entry keys are the intended
citation keys and should arrive pinned.

## 2. The undefined section references

Thirteen "Reference ... undefined" warnings, ten distinct names, rendering as
"??" in the PDF; all but three sit in the introduction's "Paper structure"
paragraph. `scripts/patch_undefined_section_refs_2026-09-11T2030.py` resolves
nine of the ten. Each target was found by reading the heading the sentence
describes.

Retargeted to labels that already existed:

| was | now | heading |
|---|---|---|
| `sec:negative_probaility` | `sec:complex-amplitudes-2` | The price is negative probability |
| `sec:self-ignorance` | `sec:fibre-self-ignorance` | The fibre as self-referential ignorance |
| `sec:quantum_number` | `sec:charges` | Quantum Numbers |
| `sec:particle_zoo` | `sec:generations` | The Particle Zoo |
| `sec:quantum_circuits` | `sec:interactions` | Interactions as Quantum Circuits |
| `sec:sedenions-generations` (x3) | `sec:sedenion-announcement` | The extra wire: how a deeper mechanism announced itself |

Given a label, the heading having had none:

| was | now | heading given the label |
|---|---|---|
| `sec:achirality_qcd` | `sec:achirality-qcd` | Why the colour force is not chiral |
| `sec:Kioid` | `sec:koide` | Charged leptons: the Koide relation |
| `sec:weak_mixing_angle` | `sec:weak-mixing-angle` | The weak mixing angle and the $W$/$Z$ mass ratio |

Two of the old names were simple misspellings (`sec:Kioid`,
`sec:negative_probaility`). `sec:complex-amplitudes-2` is the right target for
the third sentence of the paragraph on content and on order: `main.tex` inputs
`self_reference_section` immediately after `what_is_a_quantum_state`.

**Left undefined deliberately: `sec:sedenions-mixing`**, one occurrence in
`wigners_friend_in_the_hopf_picture`. The sentence says that section "reads
that phase --- through the paper's negativity--contextuality chain --- as this
wire's contextual cargo". Either the masses section's
`\subsection{Mass eigenstates versus weak eigenstates}` or the interactions
section's provenance paragraph on the sedenion route to the full CKM could be
meant. That is an editorial choice, not a typo.

Verified statically: none of the nine old names survives anywhere in paper 1,
and every retargeted name now has a `\label`. A sweep of every `\ref` against
every `\label` in the paper leaves `sec:sedenions-mixing` as the only live
unresolved reference; `app:nb-N`, `app:nb-P`, `app:nb-R`, `app:nb-S` and
`op:...` also come up, but all five are inside comments and are not compiled.

## 3. Not done, and why

- **No build.** JS co-ordinates builds between sessions and has asked that
  none be run without his say-so. Both changes above are static and were
  checked by grep, but neither has been compiled. The reference patch in
  particular wants a build to confirm the warning count falls from thirteen to
  one.
- **No citation added for Brannen or Sumino.** The keys enter
  `references.bib` only when the batch is imported and the collection
  re-exported, and the wording of a priority credit is JS's.
- **The `\ref` style in that paragraph.** The eighteen references in "Paper
  structure" are bare `\ref{}`, so they render as "1.2" with no "section"
  before them, unlike the rest of the paper, which uses `\S\ref`. Not touched:
  it is a style pass over one paragraph and nothing to do with the warnings.
- Everything else on `notes/todo.md` is untouched.

## 4. Files changed

- `bib/koide_attribution_refs_2026-09-11T2011.bib` (new)
- `scripts/patch_undefined_section_refs_2026-09-11T2030.py` (new) and its
  effect on `paper1/main.tex`,
  `paper1/wigners_friend_in_the_hopf_picture_2026-06-13.tex`,
  `paper1/particle_zoo_section_2026-06-08.tex`,
  `paper1/masses_section_2026-06-08.tex`,
  `paper1/boson_masses_section_2026-06-08.tex`; `.bak` beside each
- `notes/todo.md`: the reference item rewritten, the undefined-reference item
  rewritten
- `knowledge/sessions/tidy_after_koide_handover_2026-09-11T2011.md` (this note)

## 5. Status-label proposals

None. No ledger was edited.

## 6. VERIFY-CITE

Two cleared (Brannen 2006, Sumino 2009), one cleared as a by-product (the 2006
tau mass). Still outstanding elsewhere in the corpus and not addressed here:
`schafer1954cayleydickson` (volume and JSTOR DOI recorded "from memory" in the
2026-08-27 batch and never confirmed), `eakinsathaye1990automorphisms` (page
range 263--278 against 263--280 in secondary sources),
`noether1918invariante` in paper 2 (no DOI exists; page range 235--257
unconfirmable), and the two sub-checks the 1900 note records against Baker and
against Springer and Veldkamp.
