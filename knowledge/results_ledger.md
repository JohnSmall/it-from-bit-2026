# Results ledger

<!-- Seeded 2026-09-10 from knowledge/memory/project/results-and-principles.md.
     Labels applied 2026-09-10 from each entry's own wording; see the
     vocabulary note. Append-only: supersede with a dated entry, never edit
     history. -->

## The vocabulary

Recovered from `paper1/appendices/appendix_jaynes_fibration_2026-07-19.tex`
§`app:jaynes:status`, which defines three of the six explicitly:

- **STRUCTURAL** -- established mathematics, imported. "None of this is ours,
  and none of it is at stake."
- **CANDIDATE** -- the framework's assembly. Readings that "stand or fall with
  the main text's derivation chain".
- **RHYME** -- a fenced analogy.

The other three are not defined anywhere in the corpus and are used here on
the readings below. **They need John's confirmation.**

- **ESTABLISHED** -- the framework's own result, proved or numerically
  verified. Distinguished from STRUCTURAL, which is mathematics we imported
  rather than produced.
- **CONJECTURE** -- stated but not proved, without PASS/FAIL criteria.
- **OPEN** -- an open problem with explicit PASS/FAIL criteria.

Labels below were assigned from each entry's own wording ("proved",
"verified numerically", "theorem, not scan", "(candidate)"). Where the
wording did not settle it, the entry is marked `[JUDGED]` and is one John
should check first.

## 2026-09-10 -- seeded and labelled

### The framework's own results

- **ESTABLISHED** Born rule derived from U(1)-invariance on S3 forcing
  minimum-degree quadratic observables; works for a single qubit, unlike
  Gleason's theorem. `[JUDGED]` -- central to the derivation chain, so
  CANDIDATE is arguable.
- **ESTABLISHED** GHZ-class states map exclusively to the C3 colour sector
  under the octonionic Hopf map (proved); W-class states access the C lepton
  sector.
- **ESTABLISHED** theta_QCD = 0 topologically forced: the GHZ class has no
  oriented pairwise structure to carry a CP-violating phase.
- **ESTABLISHED** No-leptoquark theorem, conditional on four explicit
  premises; closes all trilinear vertices. Conditional, but a theorem.
- **ESTABLISHED** Flavour symmetry conserved but ungauged: forces come from
  the identity component of Aut(O) = G2; generations come from the component
  group pi_0 = S3, contributing nothing to any Lie algebra.
- **ESTABLISHED** Winding-equals-ladder-number lemma (`lem:winding-number`)
  proved and verified to numerical zero.
- **ESTABLISHED** Sedenion zero-divisor locus: single G2-orbit, every
  annihilator exactly 4-dimensional; norm defect equals the coassociative
  4-form. Theorem, not scan.
- **ESTABLISHED** delta_0 = 2/9 reproduces charged lepton masses to <0.006%
  with zero free dimensionless parameters.
- **ESTABLISHED** sin^2 theta_W = 1/4 at tree level, running to 0.231 at M_Z
  with matching scale ~3.6 TeV; m_H = v/2 (-1.7%); y_t = 1 (+0.9%).
- **CANDIDATE** Koide ratio equals 2/3 when phi^2 = 1/3 with the equal-weight
  frame reading. The source marks this "(candidate)".

### Imported mathematics the framework relies on

- **STRUCTURAL** Coecke-Kissinger GHZ (special Frobenius) / W (anti-special)
  classification, verified numerically here; strong complementarity
  equivalent to anticommutation. `[JUDGED]` -- the classification is theirs,
  the numerical verification ours.
- **STRUCTURAL** Adams, Hurwitz and Eakin-Sathaye collectively establish that
  no new kinematic structure appears above the fourth qubit.

### Neutrino prediction (recorded as resolved 2026-06-12)

- **CANDIDATE** Sum m_nu ~ 52 meV, per `fermion_mass_geodesic_calculation.md`
  (dilution rule, n=2).
- **CANDIDATE** Robust qualitative predictions: m_1 = 0 exactly, normal
  ordering, two sterile neutrinos at ~3.6 TeV, no fourth generation.
- **OPEN** Delta m^2_21 x30 tension and 0.6 degree theta_nu fine-tuning.
- *Superseded:* the earlier figure of 2.6 meV in `quark_neutrino_masses.md`.
  Recorded, not labelled: a retraction is not a claim.

## 2026-09-11 -- the Koide phase, refitted and split

<!-- Proposed by Claude Code in the session recorded at
     sessions/koide_delta_gap_2026-09-11T1600.md. Labels are PROPOSED; JS to
     confirm, amend or reject. Script: scripts/koide_delta_fit_and_angle_scan
     _2026-09-11T1600.py, seed 20260911. -->

- **ESTABLISHED** `[PROPOSED]` With alpha = sqrt2 and delta = 2/9 rad set by
  hand, and the scale M fixed by the tau mass, the electron and muon masses
  are reproduced to -0.003% and -0.002% (PDG 2024 inputs; -0.007% and -0.006%
  on PDG 2022). Inverting the Z3 form on the data gives
  delta = 0.2222248 +/- 0.0000063 rad, with 2/9 at -0.41 sigma, and
  alpha = 1.414209 +/- 0.000011, with sqrt2 at -0.43 sigma. The band, set by
  the tau mass, fixes 4.6 significant figures of delta. *Supersedes* the
  2026-09-10 entry "delta_0 = 2/9 reproduces charged lepton masses to <0.006%
  with zero free dimensionless parameters": the number was right, the
  parameter clause was not -- delta is matched, not derived, and counts as one
  matched dimensionless number.
- **CANDIDATE** `[PROPOSED]` The geometric reading
  2/9 = dim_R C / dim_R (O + R). It is a ratio of dimensions and delta is a
  number of radians; no mechanism yet makes one radian the natural unit
  (2/9 of a turn is 1.396 rad). RHYME is arguable. The section already calls
  it "suggestive, matched rather than derived".
- **ESTABLISHED** `[PROPOSED]` 2/9 rad is not a natural angle at any simple
  denominator: a pre-registered scan finds no rational multiple of pi with
  denominator up to 60 within 280 sigma of the fitted band, and no arccos,
  arcsin or arctan of a rational or surd (denominators to 100), nor any
  symmetric-cap Berry phase (denominators to 200), within 10 sigma. Widening
  the pi-multiples to denominator 400 produces one chance hit (22 pi/311, 2
  sigma) at the rate a random search would (expectation 0.58). Numerical
  fact; its reading is the CONJECTURE below.
- **CONJECTURE** `[PROPOSED]` A rational number of radians is the signature of
  flat geometry with rational periods, not of round geometry; if delta is a
  holonomy, its connection is flat along the direction that carries it (the
  S1 fibre, a torus), not the round Hopf connection. Direction, not result.
