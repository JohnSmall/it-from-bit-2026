# Reading note: Tang 2025, non-associative sedenionic QED, against associator-debt and Koide

Date: 2026-09-25T2100. Fable session, at JS's request: read
`~/Documents/physics_papers/tang_preprints202511.0427.v1.pdf` (Jau Tang,
"Advantages of non-associative sedenionic QED without UV-divergence and
renormalization: predictions of lepton mass and magnetic moment anomaly",
Preprints.org, 7 November 2025, doi 10.20944/preprints202511.0427.v1, not
peer-reviewed, 15 pages) and say how it fits the framework's ideas about
associator-debt mass and the Koide relation. Read in full. Batch:
`bib/tang2025_associator_qed_ref_2026-09-25T2100.bib`. Numbers from
`scripts/tang2025_koide_check_2026-09-25T2100.py`, stdout in section 6.

## 0. Verdict

Tang makes the same identification the framework makes, mass from the
associator, and makes it independently, so he must be credited for it beside
his 2023 paper with Qiang Tang. Everything after the identification diverges,
and on the two points where the divergence can be tested the framework's side
is the computed one. He puts the generations into the *modulus* of the
associator (three norms, three masses); the framework has proved on the basis
units that the octonionic associator's modulus is uniform, so the ratios
cannot come from it, and puts the generations into the *phase*, the Bargmann
invariant $3\delta = 2/3$ of the triality form. He attaches the generations to
the three octonionic copies through the core of the sedenions; notebook T
showed that triple is colour. And his mass and $g-2$ tables carry no
derivation at all: no associator is computed, no embedding is specified, and
the "0.00 %" muon entry is $-0.003$ %, which is what the framework's own
tau-anchored fit gives and no better. The preprint is a statement of a
programme, not a calculation, and the framework should say so where it
credits him.

## 1. What the preprint claims [read]

An octonionic Dirac equation $(i\Gamma^{\mu}D_{\mu} - m)\Psi = 0$ with
octonion-valued $\Gamma^{\mu}$, $A_{\mu}$ and $\Psi$; a field strength with an
octonionic commutator; and an explicit associator term
$\epsilon[\bar\Psi, A_{\mu}, \Psi]$ in the Lagrangian. From the associator he
claims four things: a Yukawa screening $e^{-\mu r}$ of the Coulomb potential
with $\mu$ "determined by the associator norm", removing the self-energy
divergence and renormalisation; lepton masses $m_{\ell} \propto
\|[\bar\Psi, A_{\mu}, \Psi]\|$ with generation-dependent norms from
"distinct octonionic or sedenionic subalgebras"; $g-2$ at tree level from the
same associator, $a_{\ell} = \alpha_{A}\|[\ldots]\|/m_{\ell}$, normalised to the
electron; and three generations from the sedenions' "three distinct octonionic
families", with $S_{3}$ "broken into three inequivalent branches". Tables give
$m_{\mu} = 105.655$ MeV and $m_{\tau} = 1776.7$ MeV with the electron as input,
and $a_{\mu} = 1.1659205\times10^{-3}$ "matching the central value". No
associator norm is computed anywhere in the text; no $\Psi$ or $A_{\mu}$ is
written down; the reference list is unreliable ('t Hooft's dimensional
reduction cited for the Cayley--Dickson construction, Bender and Boettcher's
PT symmetry for neutrino oscillation).

## 2. Where it agrees with the framework [CANDIDATE, on both sides]

- Mass from the associator. His eq. (24), $m \propto \|[\bar\Psi, A_{\mu},
  \Psi]\|$, and the framework's "mass is associator-debt, the information cost
  of a bracketing the algebra leaves ambiguous" are one identification. He
  reached it independently and published it first in the 2023 paper; the
  framework's masses section should credit him for the identification where
  it defines the debt, as it already cites him for the sedenion generations.
- The inverse length. He reads the associator's scale as a screening length
  (a Yukawa $\mu$); the framework reads it as a Compton length, "the debt's
  range", $e^{-mr}$ along a spacelike separation (complex-cost note, section
  4d). Same dimension, same exponential; different carrier (his photon, the
  framework's fermion). RHYME.
- The associator as dynamical. He puts it in the Lagrangian as an explicit
  term; the framework's debt is kinematic, priced at the vertex. The
  framework's dynamical layer (the second paper, the propagators and rates)
  will need an associator term of some such form, and his is the only
  published attempt to write one. Worth reading for that when the time comes,
  with the caveat that his term has no derivation either.

## 3. Where it diverges, and what decides it

- **Modulus against phase** [the framework's side ESTABLISHED, the ledger's
  2026-09-11 entries]. Tang's hierarchy needs three different associator
  norms. Computed on the basis units, the octonionic associator has uniform
  magnitude on every bracketing not forced to vanish ($G_{2}$-transitivity),
  which is why the framework's masses section says the associator "does not
  by itself set the mass hierarchy" and why the route "any octonionic
  direction" is logged closed in invalid_routes. The framework's ratios come
  from the phase: the Koide ratio is fixed by $\alpha = \sqrt2$ (the quadratic
  invariant of the generation triple, blind to the phase) and the individual
  masses by $3\delta = 2/3$ (the cubic invariant, the Bargmann phase). In the
  two-columns vocabulary Tang puts generation in the real column and the
  framework in the imaginary column, and the uniformity theorem is what
  forbids the former in the octonions. In the sedenions the norm defect is
  not uniform, but notebook M's scan of the bare sedenion geometry against
  $\delta = 2/9$ returned zero hits, with the bare cross-copy vertex at
  $\pi/4$; if Tang's generation-dependent norms exist they are dressed
  quantities, and he has not dressed anything.
- **Which triple** [ESTABLISHED, notebook T]. His "three distinct octonionic
  families" and "three copies of the octonion algebra" are the core triple,
  permuted inside $G_{2}$ and therefore colour; the generation triple is the
  three halvings permuted by the doubling's $S_{3}$. And his "sedenionic QED
  breaks $S_{3}$ into three inequivalent branches" is the opposite of the
  framework's (and Gourlay--Gresnigt's) unbroken $S_{3}$, the direct product,
  with the masses differing through the triality angle rather than through a
  broken family symmetry.
- **The numbers** [ESTABLISHED, Part A--C of the script]. His muon is
  $-0.003$ % from PDG and his tau $-0.009$ % from the PDG 2022 value he
  quotes, $-0.013$ % from PDG 2024; the framework's tau-anchored fit reaches
  $-0.003$ % and $-0.002$ % for the electron and muon, and its
  electron-anchored $Z_{3}$ form (Part C) gives $105.6594$ and $1776.985$ MeV,
  $+0.001$ % and $+0.003$ %. Neither his table nor his text says how his
  numbers were produced. The Koide ratio of his predicted triple is
  $0.6666544$, $2.4\sigma$ below $2/3$ in the tau-set band, so whatever
  formula produced them is not exactly Koide and is not stated.
- **$g-2$ at tree level** [pushback]. A tree-level associator term that
  reproduces $a_{e}$ to nine decimals and the Fermilab $a_{\mu}$ to the central
  value, with "no adjustable parameters" after "normalising to the known
  electron anomaly", is a claim with one input and no formula. The Schwinger
  term is a loop; nothing in the preprint shows how an algebraic norm
  produces $\alpha/2\pi$. The framework's own position (interactions section)
  is that the anomalous moment is the natural route from the framework to
  field theory and is owed, not had.
- **Yukawa screening of the photon** [pushback]. A screened Coulomb potential
  is a massive photon; the bound on $\mu$ is many orders below any associator
  scale he could mean, and the point is not addressed.

## 4. How it fits, in one sentence each

Associator-debt: same identification, independently made, to be credited;
opposite mechanism for the hierarchy (modulus there, phase here), with the
uniformity of the octonionic associator deciding it in the framework's
favour. Koide: he does not mention it; his triple fails it at $2.4\sigma$; the
framework has it exactly as $\alpha^{2} = 2$, blind to the phase, with the
phase then fixing the individual masses. The sedenions: his generation triple
is the framework's colour triple. The one thing to take from him: the
associator written into a Lagrangian, as a form to test when the dynamical
layer is built.

## 5. For the paper and the ledgers

- v2 plan item 7 ("What mass is: associator-debt"): one clause crediting Tang
  (2023 with Qiang Tang; 2025 alone) with the independent identification of
  mass with the associator, and one sentence stating that his generation
  mechanism, three associator norms, is excluded in the octonions by the
  uniformity computed here and unsupported in the sedenions by notebook M,
  the framework's ratios being carried by the phase. Cite
  `tang2025associator` once imported; the 2023 key is in the library.
- Ledger, proposed: **CANDIDATE** the independent identification (his and
  ours); **ESTABLISHED** the uniformity of the octonionic associator's
  modulus as what separates the two mechanisms (already in the ledger under
  the closed Koide-phase routes; this note only points at it); no new open
  problem.
- No claim of his is adopted; nothing here is a route.

## 6. Exact stdout of `scripts/tang2025_koide_check_2026-09-25T2100.py`

```
=== Part A: Tang's Table 2 errors, recomputed ===
mu   predicted   105.6550 vs   105.6584 (his reference): -0.0032 % ; vs PDG 2024   105.6584: -0.0032 %
tau  predicted  1776.7000 vs  1776.8600 (his reference): -0.0090 % ; vs PDG 2024  1776.9300: -0.0129 %
his table says 0.00%% and 0.01%%; the muon figure is -0.003%%, ten times the PDG uncertainty of 2e-6 %%

=== Part B: the Koide ratio of the triples ===
K(Tang predicted) = 0.6666544 ; K(PDG 2024) = 0.6666645 ; 2/3 = 0.6666667
K band from the tau (+/- 0.09 MeV): +/- 5.08e-06 ; Tang's K sits -2.0 sigma from PDG's, -2.4 sigma from 2/3
no computation in the preprint produces his numbers; the Koide ratio is the test any associator-norm mass formula must pass

=== Part C: the framework's Z3 form with the electron as input ===
mu   from m_e, alpha = sqrt2, delta = 2/9:   105.6594 MeV ; PDG 2024   105.6584 (+0.0010 %) ; Tang    105.655 (-0.0042 % from the Z3 value)
tau  from m_e, alpha = sqrt2, delta = 2/9:  1776.9850 MeV ; PDG 2024  1776.9300 (+0.0031 %) ; Tang   1776.700 (-0.0160 % from the Z3 value)
K of the Z3 form is exactly (1 + alpha^2/2)/3 = 0.6666667
```

## 7. Does Tang support the parallelisability route to finiteness? (added 2026-09-27)

JS: Tang's paper "gives me confidence in my guess that an alternative route
to the framework ... by working from the purely ontological QFT framework
and finding that because infinite frequencies can be mapped to CTCs and
hence division algebras then we should find that only theories based on
division algebras can have their infinities easily removed by recasting them
as transport on parallelisable spheres ... now Jau Tang is doing exactly
that and finding results very close to our own."

Assessment. The shared items are the two identifications (associator--mass;
sedenion $S_{3}$--generations), which are proposals in both places and are
credited. On the one item that bears on the guess, the removal of
infinities, Tang's paper does not help and should not be cited as support.
His mechanism is a Yukawa screening of the Coulomb potential with $\mu$ from
the associator norm (eq. 19); the divergence he displays (eq. 14) is the
field energy at $r \to 0$, and a screened potential still behaves as $1/r$
there, so the integral still diverges: screening tames the infrared, not the
ultraviolet. It also makes the photon massive. No propagator, loop or finite
quantity is computed. The paper's own convergence rule (the
Boyle--Finn--Turok paragraph) applies: convergence is evidence about a
conclusion only when the conclusions are results, and here they are not.

The guess is already in the paper, as a direction and a question
(`spacetime_from_non-computability.tex`, "Loops, supertasks, and a second
route to parallelisability"; "Does parallelisability determine
renormalisability?"), and the paper's claim is about *removability*
(renormalisability), not finiteness; Tang's is the stronger claim, and he
delivers neither. In the thread's vocabulary the guess reads: a divergence is
an unbounded real-column cost; the imaginary column is periodic (a phase on a
compact fibre) and cannot diverge; the fibre is trivialisable exactly on the
parallelisable spheres (Adams); and the failure of transport at the next
rung is bounded (the norm-defect ratio in $[0, \sqrt2]$, prop:zd-defect). A
coherent picture, CONJECTURE, against which the standard objection stands:
the ultraviolet divergence is a property of the momentum measure, and every
earlier division-algebra field theory (quaternionic and octonionic; Gürsey
and Tze, Adler, Dixon; VERIFY-CITE) inherited it unchanged.

Proposed as a well-formed problem, op:parallelisable-renormalisable, for JS
to mint or decline. PASS: the one-loop electron self-energy recast as a
closed computational path in the framework's sense, a sum over windings on
the fibre with a bounded phase, reproducing the finite part of the
renormalised result. FAIL: the recasting leaves the momentum measure
$\int d^{4}k$ and its divergence untouched, or requires a cutoff put in by
hand. Either outcome settles whether the paper's question is structural or
accidental, which the paper itself says it does not know. Nothing Tang has
published contributes to either side.
