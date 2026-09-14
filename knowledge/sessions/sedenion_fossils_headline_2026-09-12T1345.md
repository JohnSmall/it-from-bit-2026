# Session note: two pre-sedenion fossils in the headline list

Date: 2026-09-12T1345. Session: Claude Code (Fable 5.1), `it_from_bit_fable_5_1`.
A paper edit at JS's instruction, not a thinking session; recorded so the
change and its sources are traceable.

## What JS asked

main.tex's headline items "Three generations" and "Chirality" were fossils
from before the sedenion section, each carrying the marker "wrong! to be
fixed with sedenions". Recommend a rewording; then apply it.

## What was read

`paper1/main.tex` lines 176--240 (the headline enumerate and its register).
`paper1/sedenions_generations_section_2026-08-27.tex`: the header's record of
the corrected mechanism, sec:sedenions-generations, eq:brown and eq:brown-psi
in sec:sedenions-promotion (including the sentence that the three Fano lines
through the preferred direction "are the three colour lines of C^3 and not
three generations"), sec:sedenions-flavour-not-force, the Szangolies
comparison (chirality housed at the register), sec:sedenions-shadow.
`paper1/particle_zoo_section_2026-06-08.tex`: the Filatov constraint and the
K_3 obstruction, "Three generations and the doublet", the sterile a-chiral
class, the spectrum summary, op:chirality, and the "deeper reason" paragraph.
Labels and keys used were checked to exist: sec:sedenions-generations,
sec:sedenions-promotion, sec:sedenions-shadow, sec:generations, op:chirality,
op:filatov-extension; brown1967generalized, filatov2024towards.

## What was changed

`scripts/patch_sedenion_fossils_headline_2026-09-12T1345.py`, one run, a
header and a dated .bak per file.

- `paper1/main.tex`: the "Three generations" item now states Brown's direct
  product Aut(S) = G_2 x S_3 with the identity component unchanged, the S_3
  acting on the three octonion halvings O, psi O, psi^2 O, and the three
  consequences the sedenion section draws (three; a family label and never a
  fourth force; no fifth rung), with the register count read as the shadow.
  The "Chirality" item now houses handedness at the register: Filatov's
  opposite-handedness constraint on an entangled pair, K_3 not
  two-colourable, three chiral classes and one a-chiral class, the frustrated
  pair's two resolutions as the weak doublet so the weak force acts on one
  handedness only, the a-chiral class blind to it; op:chirality and
  op:filatov-extension named as the open ends.
- `paper1/particle_zoo_section_2026-06-08.tex`: the paragraph "There is a
  deeper reason for the number three" still called the three Fano lines
  through the preferred direction "the three generations", which
  sec:sedenions-promotion contradicts. Re-pointed: the triality observation
  kept, the three lines named as colour with that section cited, the
  generation three located one rung up on the halvings, the count here read
  as the shadow, the corroboration sentence kept.

Nothing else touched. No ledger entry arises: every statement is one the
sedenion or zoo sections already make, re-said in the headline register. Not
built (JS's rule: builds on his OK); not committed.

## Second edit, T1400: the "Spacetime dimensionality" headline and the Bloch sphere

JS: main.tex's spacetime item spoke of the Bloch sphere and Lorentz boosts
forcing d = 3, while the spacetime section never mentions the Bloch sphere.
Read: main.tex's item; `spacetime_from_non-computability.tex`
sec:three-dimensions (Adams' parallelisable spheres plus the associativity
filter; the general-relativistic route from mutual acceleration; Masanes and
Mueller's three-dimensional Bloch ball as a convergent), sec:lorentz (the
computability split fixing C^2, "the qubit density operators fill the future
cone", measurement as cone-tipping), op:three-dimensions, and the paragraph
at line 515 that says the Kaluza--Klein intuition "misdiagnoses" the S^7
degrees of freedom as spatial; `hopf_justification_section` for the 9+1
reading, which is Szangolies's route cited as independent arrival.

Finding: the headline folded the count and the Lorentz group into one
Bloch-sphere sentence the section does not argue; its Spin(1,d) clashed with
the section's Spin(1,d+1); its Kaluza--Klein sentence said the opposite of
the section, and "six internal dimensions of SU(3) x SU(2) x U(1)" was wrong
on its face (the group has twelve; the six are the real dimensions of C^3).

`scripts/patch_spacetime_bloch_headline_2026-09-12T1400.py`, backups
`.2026-09-12T1400.bak` on both files: the headline item now gives the two
routes to the count as the section does, the Lorentz group separately from
C^2 with the density operators as the future cone and the pure states as its
celestial sphere, S^7 as filter with no metric and the Kaluza--Klein remark
as the section makes it, and names op:three-dimensions. sec:lorentz gains one
sentence after the Mueller citations: the Bloch ball as the unit-trace slice
of the cone, the Bloch sphere as its celestial sphere with the Moebius action
of SL(2,C), state reduction and boosts as one operation in two charts.
Standard (Penrose and Rindler vol. 1 for the celestial sphere; not cited,
resting on the existing Baez citation for SL(2,A); a VERIFY-CITE entry if JS
wants the source named). The paragraph was not re-filled because it carries
a "%"-continued line. Not built; not committed.

T1415: JS found the T1400 item correct but too long, and stated the standard
for the headline list: a few results with pointers to where they are
derived, enough to entice the reader, not half a derivation.
`scripts/patch_spacetime_headline_short_2026-09-12T1415.py` (backup
`.2026-09-12T1415.bak`) replaces it with three lines pointing at
sec:three-dimensions, sec:lorentz and op:three-dimensions. The "Three
generations" and "Chirality" items written at T1345 are ten to twelve lines
each and fail the same standard; shortened versions were offered to JS, who
accepted them: `scripts/patch_headline_generations_chirality_short_2026-09-13T0705.py`
(backup `main.tex.2026-09-13T0705.bak`) makes each four lines, pointing at
sec:sedenions-generations, sec:generations and op:chirality. The Filatov
citation, the halvings, the shadow reading and op:filatov-extension now live
only in the body text they summarise, which is where they belong.

An untracked `newfile.tex` (18 KB, 2026-09-12 21:59) sits at the repository
root carrying main.tex's header lines; not this session's, left alone and
not to be staged with this session's paths.

## Pushback recorded

The masses section still introduces the generations as "the three
off-diagonal octonionic entries of J_3(O), cyclically permuted by a Z_3
triality"; the sedenion section's header says eq:z3 has been re-grounded on
the psi-orbit, so the two readings are presumably reconciled there, but the
masses sentence itself does not say so. Worth one clause when that section
is next opened.
