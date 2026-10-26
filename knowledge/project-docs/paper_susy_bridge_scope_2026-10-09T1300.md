# Scope for a follow-on paper: supersymmetry as the theory of the unsplit arena (2026-10-09)

Session 2026-10-09, Fable 5.1. JS: the rhyme "supersymmetry is the regime
where the associator cancels, mass the regime where it does not" is not
for Paper 1, but "there could be a useful follow-on paper dedicated to
expanding that idea. Because so much work has been done on supersymmetry,
it's important to make a connection to that work and also to explain why
it has no experimental evidence to back it up. Creating a bridge between
the work on supersymmetry and this framework shows how it's integrated in
and is an extension of the decades of work gone before." This document
scopes that paper. It is a plan, not a draft; every claim carries the
label it has today. "Paper 3" is already spoken for (the Jaynes appendix's
`%% PAPER3` comments name a companion paper on measurement-scale
unification), so this is "the supersymmetry bridge paper" until JS numbers
it.

## 1. Working titles and the thesis in one paragraph

Titles, JS to choose: *Where supersymmetry went: the division algebras,
the computability split, and the absence of superpartners*; or
*Supersymmetry as the theory of the unsplit arena*; or *The superpartners
are the colour directions*.

Thesis. Supersymmetry is real, as the symmetry of the octonionic rung of
the Cayley--Dickson tower when that rung is read as spacetime: the
super-Yang--Mills theories exist exactly in the dimensions of
$\mathbb{R},\mathbb{C},\mathbb{H},\mathbb{O}$, and the $\mathcal N=4$ theory
in four dimensions is the ten-dimensional octonionic theory reduced on six
directions. The framework's computability split, the selection of a
preferred $\mathbb{C}\subset\mathbb{O}$ by the record, reads those six
directions as gauge algebra instead of geometry: they become the colour
space $\mathbb{C}^{3}$, the R-symmetry $SU(4)_{R}=\mathrm{Spin}(6)$ that
rotates them is cut to $U(3)=SU(3)\times U(1)$, colour and the preferred
direction's phase, and the supercharges go with the geometry. Mass
appears in the split theory as associator debt, exactly where the
trilinear spinor identity that supersymmetry needs stops applying. So the
world has no superpartners because it is the split theory; supersymmetry
has no experimental evidence because experiments are records and the
unsplit theory has none; and what experiment does see of the unsplit
theory is what survives the split: the gluon trees, the $\mathcal N=4$
summand of one-loop QCD, and gravity as the square of gauge theory. The
decades of supersymmetry are then the theory of the arena before records,
inherited whole and reinterpreted, not refuted.

## 2. Why this paper, and why it is separate from Paper 1

Paper 1 excludes supersymmetry on the grounds that nothing motivates it
(grounding argument, section 10.5) and that the termination theorem leaves
no room for it. That is a negative result stated in one place. The bridge
paper turns it positive: it says what supersymmetry *is* in the framework,
derives the exclusion from the split rather than from the absence of
motivations, and connects to the body of work (Haag--Łopuszański--Sohnius,
Nahm, the division-algebra classification, $\mathcal N=4$ amplitudes, the
double copy, AdS/CFT) as inherited structure. That is a paper's worth of
material, it needs computations Paper 1 does not, and it would unbalance
Paper 1, whose spine is the mass sector.

## 3. The chain of argument, with today's labels

1. **Supersymmetry comes from the division algebras.** [STRUCTURAL,
   imported] Kugo--Townsend 1983, Evans 1988, Baez--Huerta 2010: SYM in
   $D=n+2$, $n=\dim\mathbb{K}$, because the supersymmetry of the action
   needs the 3-$\psi$'s identity, which holds iff $\mathbb{K}$ is
   alternative. The framework's tower is the same list for its own reason
   (Hurwitz; `prop:termination`).
2. **The ten-dimensional theory is the framework's declined option.**
   [Paper 1] $SL(2,\mathbb{O})\cong\mathrm{Spin}(9,1)$ is "the unsplit
   ten-dimensional option the computability split declines" (spacetime
   section, 2026-09-27 patch); the $S^{7}$ sector is algebra, not metric.
3. **The reduction is the split.** [STRUCTURAL, verified 2026-10-09]
   $\mathrm{Herm}_{2}(\mathbb{O})$ has signature $(1,9)$; the preferred line
   cuts it into $(1,3)$ plus the six-dimensional colour complement; the
   colour derivations fix the four and rotate the six;
   $\mathfrak{g}_{2}\cap\mathfrak{u}(3)=\mathfrak{su}(3)$ with the $U(1)$
   outside $G_{2}$. In $\mathcal N=4$ language: the six scalars are the
   colour directions, $SU(4)_{R}$ is the rotation group of colour space,
   and the choice of $J=L_{e_{1}}$ is the $\mathcal N=4\to\mathcal N=1$
   reduction of the R-symmetry. (Script
   `scripts/n4_sym_unsplit_octonionic_spacetime_2026-10-09T1000.py`;
   session note `amplituhedron_susy_unsplit_2026-10-09T1000.md`.)
4. **The split removes the supercharges and keeps the R-symmetry
   subgroup.** [CANDIDATE] The selection of $e_{1}$ is a record
   (`sec:fanout-direction`), a real-column event; the $\mathcal N=4\to\mathcal
   N=1$ decomposition keeps one Grassmann direction, the split keeps none.
   Superpartners are excluded by the termination theorem and the
   no-leptoquark theorem.
5. **Mass is where the 3-$\psi$'s identity stops.** [RHYME today; the
   paper's central computation] The framework's mass is associator debt
   settled where the preferred direction composes cross-copy legs
   (`sec:associator-higgs`, `eq:debt-defect`); the supersymmetric action
   is invariant because the associator cancels in the 3-$\psi$'s
   combination. The paper must exhibit the associator term that survives
   the split as the obstruction to the supersymmetry variation, and
   identify it with the norm-defect identity. Until that is done this is a
   rhyme.
6. **Why there is no experimental evidence.** [CANDIDATE, with the
   standard physics STRUCTURAL] Experiments are records; the unsplit theory
   has no records, no preferred direction, no masses, no scale. What
   survives the split is what experiment sees: tree-level gluon amplitudes
   (theory-independent), the $\mathcal N=4$ summand of the Bern--Dixon--Dunbar--Kosower
   decomposition of one-loop QCD, the double copy's gravitational
   two-body dynamics. The LHC null results and the naturalness debate
   (Giudice 2008) are then not a failure of a prediction but the expected
   silence of the arena. The standard motivations are handled elsewhere:
   the hierarchy by $m_{H}=v/2$ as bundle geometry, unification by its
   exclusion (no GUT), dark matter by Paper 2's network status.
7. **What is inherited.** [each STRUCTURAL as import, CANDIDATE as
   reading] The classification theorems (Coleman--Mandula 1967,
   Haag--Łopuszański--Sohnius 1975, Nahm 1978) as the symmetry algebra of
   the arena, with the superconformal $PSU(2,2|4)$ the symmetry of the
   twistor arena of the 2026-10-07 thread; $\mathcal N=4$ amplitudes and
   the amplituhedron as the arena's positive geometry; Seiberg--Witten
   1994 as the quaternionic rung's exact results ($\mathcal N=2$, $SU(2)_{R}$,
   $\mathrm{Herm}_{2}(\mathbb{H})$ with signature $(1,5)$, no colour); the
   magic pyramid of supergravities (Anastasiou, Borsten, Duff, Hughes and
   Nagy 2014; Borsten, Duff, Hughes and Nagy 2014) as the double copy of
   division-algebra SYM, i.e. gravity as the square of the unsplit
   theory, to be set beside the framework's gravity as post-record
   bookkeeping; $\mathcal N=8$ supergravity and eleven-dimensional
   supergravity on the parallelised $S^{7}$ (Englert 1982, VERIFY-CITE) as
   the octonionic sphere the framework's "parallelisable spheres" sentence
   names; AdS/CFT (Maldacena 1997) with the unsplit theory on the boundary
   and gravity in the bulk, to be set beside `sec:jacobson`'s imaginary
   information, as a direction only.

## 4. The central computation, and what it needs

- Read Baez and Huerta 2010 for the exact form of the 3-$\psi$'s identity
  and its conventions (spinors in $\mathbb{K}^{2}$, the vector as
  $\psi\psi^{\dagger}$-type bilinear, the trilinear map). Verify it
  numerically in Convention A for $\mathbb{O}$, and verify its failure for
  the sedenions (where the alternativity fails and the ledger already has
  the zero-divisor locus). This is the paper's first script.
- Express the supersymmetry variation of the ten-dimensional action
  restricted to the split: with the preferred $\mathbb{C}$ fixed, which
  terms of the variation involve the associator of elements of
  $\mathbb{C}$ with elements of $\mathbb{C}^{3}$, and do they vanish? The
  expectation is that they vanish while all legs stay in one
  division-clean copy and fail across copies, which is `eq:debt-defect`'s
  condition for a non-zero defect. If so, the obstruction to supersymmetry
  after the split *is* the associator debt. If not, the rhyme is wrong and
  the paper has a different shape.
- The $\mathcal N=4\to\mathcal N=1\to\mathcal N=0$ chain in field content,
  stated honestly: the $\mathcal N=4$ multiplet is adjoint (gauginos and
  scalars), the framework's quarks are triplets and its scalars are not
  particles but the colour directions; the bridge is at the level of
  symmetry and arena, not field by field. Say so early.
- The BDK decomposition for the four-gluon one-loop amplitude, as an
  illustration: the $\mathcal N=4$ piece is the box without rational terms;
  the rational terms come from the scalar loop. Textbook, to be reproduced
  numerically for one helicity configuration.
- Read Haag--Łopuszański--Sohnius for what "supersymmetries of the
  S-matrix" assumes (a mass gap or an S-matrix in a given spacetime) and
  whether the pre-record arena satisfies its hypotheses; the framework's
  arena has no S-matrix in the record sense, which may be where the
  theorem's permission for supersymmetry and the framework's absence of it
  meet.

## 5. Predictions and distinctions the paper would state

- No superpartners at any scale, not "broken above the LHC's reach": the
  exclusion is structural (termination theorem), so a superpartner at
  $10^{16}$ GeV is as excluded as one at a TeV. Falsifiable by any
  superpartner.
- The one new scale is the 3.6 TeV matching scale (Paper 1); no
  supersymmetry-breaking scale exists.
- The $\mathcal N=4$ summand of one-loop QCD amplitudes is a trace of the
  unsplit theory in a record-side quantity; the paper can say which
  terms of a physical amplitude are "arena" terms and which are "split"
  terms (the rational terms), which is a reading, not a prediction.
- The Koide and mass sector has no supersymmetric contribution: the
  framework's masses are associator debt, which is zero in the unsplit
  theory.

## 6. Fences and risks

- The Coulomb-branch vev of $\mathcal N=4$ (a direction in the six,
  $\mathrm{Spin}(6)\to\mathrm{Spin}(5)$) and the framework's preferred
  direction (a direction in the seven, $G_{2}\to SU(3)$) are different
  breakings. The paper must not identify the Higgs mechanisms.
- A supercharge has no framework object yet. The arena's superconformal
  algebra has fermionic generators; what they are in the Hopf-fibration
  language (a map between fibre and base? the FANOUT functor's odd part?)
  is OPEN and the paper should name it as such rather than invent it.
- The framework is $\mathcal N=0$, not $\mathcal N=1$. The group theory of
  the split is $\mathcal N=1$'s; the spectrum is not. The paper must not
  drift into "the framework is a hidden $\mathcal N=1$ theory".
- The 3-$\psi$'s computation may fail (section 4). Then the paper is about
  the reduction (sections 3 and 6 of this scope) and not about mass.
- The literature is vast and the paper must engage it as a reader of it,
  not as a critic: the tone is "here is where all of this lives", in the
  manner JS asked for with Filatov.

## 7. What Paper 1 and Paper 2 must settle first

- `op:fanout-selection` (uniqueness of the preferred direction) and
  `op:chirality` (which $SU(2)$ factor): the bridge paper's step 4 needs
  the selection to be the record's and to have a definite type.
- `op:comp-metric`, at least to the extent that "the unsplit arena is
  spacetime before records" is a stated reading in Paper 2.
- The mass identification `eq:debt-defect` must be stable; the bridge
  paper's step 5 computes against it.

## 8. Next steps (concrete, for the todo)

1. Read Baez--Huerta 2010 (and II, 2010) in full; write the 3-$\psi$'s
   script for $\mathbb{O}$ and the sedenions.
2. Read Haag--Łopuszański--Sohnius for its hypotheses.
3. Attempt the split supersymmetry variation (section 4, second item);
   record PASS/FAIL.
4. Only then outline the paper.

References: `bib/supersymmetry_bridge_refs_2026-10-09T1300.bib` (this
document) and `bib/amplituhedron_susy_division_refs_2026-10-09T1100.bib`
(the 2026-10-09 session note). Englert 1982 and the ATLAS/CMS search
summaries are not batched: VERIFY-CITE when the paper is drafted.
