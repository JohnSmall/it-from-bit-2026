# Invalid routes

Routes that were tried and failed. CLAUDE.md requires this file to be read
before proposing any mechanism or mass route, and a logged route is not to be
retried.

<!-- Seeded 2026-09-10 from knowledge/memory/project/results-and-principles.md,
     the distilled memory exported from the Claude web project "negative
     probability" on 2026-09-09. Those lines were marked [stated] there, a
     provenance flag, NOT one of this project's six status labels.

     NOTHING BELOW CARRIES A STATUS LABEL YET. Per CLAUDE.md every claim takes
     exactly one of ESTABLISHED / STRUCTURAL / CANDIDATE / CONJECTURE / RHYME /
     OPEN, and labels are John's to apply. Treat every entry as unlabelled
     until he has been through it.

     This ledger is append-only: supersede with a dated entry, never edit
     history. -->

Entries here carry no status label. The six labels grade claims the project
makes; a route recorded here is one the project does not make, and its status
is exactly that it failed. Each entry records why.

## 2026-09-10 -- seeded from the Claude web project memory

- Geodesic/path-length picture for quark mass (§7.8, March 18): retracted; replaced by associator debt framing
- GHZ–W superposition reading for quarks: fails — SLOCC classes are orbits, not orthogonal summands; canonical orbit postulate requires zero pairwise concurrence
- Mass from Fano plane combinatorics: ruled out (all counting gives polynomial/binomial ratios; cannot produce super-exponential hierarchies)
- S⁷ as metric space for non-computable distance: excluded by non-associativity (Moufang loop, not group)
- Naive pushforward of W(F4) action: non-descent confirmed by three-coset argument

## 2026-09-11 -- routes to the Koide phase delta = 2/9 (see sessions/koide_delta_gap_2026-09-11T1600.md)

- Holonomy-squared model m_k ~ sin^4(theta_0 + 2 pi k/3): does not reproduce
  the spectrum. Recorded in op:koide-delta since 2026-06; entered here so the
  file is complete.
- Frame orientation in the bare sedenion geometry: notebook M's eighteen-
  comparison inventory of the sedenion triple's structural angles
  (2026-07-10, app:nb-M) returns twelve zeros, four angles at exactly pi/4
  and two ratios at exactly 1/4; no 2/9. Run against the up-quark leakage
  angle, but it is the same number and the same geometry, so it closes the
  route for the Koide phase too. Do not re-run the angle inventory hoping for
  a different answer; only a dressed operator can produce a non-symmetric
  angle.
- Any octonionic direction: the associator has uniform magnitude on every
  non-vanishing bracketing (G2 transitivity; recorded 2026-04 in the archive,
  and stated in the masses section's division-of-labour paragraph), so no
  choice of direction in O supplies a number.
- The norm-defect identity eq:debt-defect: a quartic magnitude identity, it
  fixes sizes (existence of mass, scale of the debt, alpha) and has no handle
  on an orientation. "The identity fixes the object, not the spectrum." Do not
  try to read delta out of the calibration bound.
- Natural-angle families: rational multiples of pi (denominator <= 60),
  inverse trigonometric functions of rationals and surds (denominator <= 100),
  symmetric-cap Berry phases (denominator <= 200), and the dimension ratio
  read as a fraction of a turn. None lands within the experimental band
  (script koide_delta_fit_and_angle_scan_2026-09-11T1600.py). A derivation
  that ends in one of these families is wrong before it is checked.

## 2026-09-11 -- the flat direction (see sessions/koide_flat_direction_2026-09-11T1900.md)

- A compact flat torus, with or without quantised flux: quantised flux gives
  rational multiples of 2 pi (Pick's theorem on lattice areas), the family the
  scan excludes; an unquantised flat holonomy is a modulus and re-houses the
  fitted number. Hopf tori in S^3 are flat with a flat restricted connection,
  but their holonomies are the excluded cap phases by Stokes. Closes the
  "torus" half of the 2026-09-11T1600 conjecture; the "flat" half stands as
  "exponential of a rational number, non-compact direction".
- Any construction in which e^{i delta} is algebraic: roots of unity,
  finite-group phases (Clifford, Pauli, Weyl of G2), algebraic state
  configurations, SIC and MUB overlaps, octonionic structure-constant triples,
  round holonomies around polygons with algebraic vertices. Excluded exactly
  by Lindemann--Weierstrass if 2/9 is exact, and numerically by the 1600 scan
  at simple denominators if it is not. A derivation that ends here is wrong
  before it is checked.
- The coherent-state (Pancharatnam) model: three coherent states on an
  equilateral triangle in phase space, mass roots the Gram eigenvalues, phase
  twice the enclosed area. One parameter, two targets: fixing the overlap at
  1/sqrt2 gives Phi = (sqrt3/2) ln 2 = 0.600 rad (3500 sigma from 2/3), fixing
  Phi = 2/3 gives alpha = 1.361 (4900 sigma from sqrt2). Script
  koide_flat_direction_gram_2026-09-11T1900.py, Part D.
- Near-miss, not a route: 108 p_e p_mu p_tau = 4 det G = 2 sqrt2 cos(3 delta)
  - 2 = 0.2228, 0.27% above 2/9, 18 sigma. Do not chase.
