# Open problems

<!-- Seeded 2026-09-10 from the Claude web project memory exported 2026-09-09.
     Unlabelled: status labels are John's to apply. Append-only. -->

## Formal open-problem documents

Each states a conjecture with explicit PASS/FAIL criteria. Full text in
`project-docs/`.

- `project-docs/appendix_continuity_open_problems_2026-07-17.tex` — 
- `project-docs/fermion_topology_open_problems.md` — The Standard Model from Three Entangled Bloch Spheres
- `project-docs/open_problem_adelic_mass_constraints.md` — Open Problem: Adelic Constraints on Particle Masses from Division Algebra Structure
- `project-docs/open_problem_asymptotic_freedom.md` — Open Problem: Asymptotic Freedom from Entanglement Class Flow
- `project-docs/open_problem_entanglement_to_physics_2026-05-03T1307.md` — Open Problem: The Dual Direction — Outstanding Problems in Entanglement Classification via the Particle-Physics Dictionary
- `project-docs/open_problem_hopf_frobenius.md` — Open Problem: Compositional Completeness as a Corollary of Adams' Theorem
- `project-docs/open_problem_qudit_degeneration.md` — Open Problem: Geometric Degeneration of Qudit State Spaces as a Consequence of the Division Algebra Constraint

Also: `project-docs/fermion_topology_open_problems.md` and
`project-docs/appendix_continuity_open_problems_2026-07-17.tex`.

## 2026-09-10 — carried over from the project memory

### Named in the overview as outstanding

- Complete John's four framing prose sections to finalise Paper 1 for arXiv submission
- Bridge test resolving the K3 Class-4 / psi-fixed line housing seam
- Patch remaining fossils in `fermion_topology_table.py` and `fermion_topology_open_problems.md` §5.2
- Echo and verify sedenion_zero_divisor_scan_2026-08-31.py output
- Newtonian limit computation for Paper 2 (op:p2-newton)
- Email Andrei Khrennikov leading with the complementarity reframe and Tsirelson-as-ramification correspondence (p-adic/adelic session deliverable)
- Mendeley import with dedupe checks for multiple RIS batches
- Label mapping for four master-file section labels (`sec:hopf`, `sec:born`, `sec:fanout`, `sec:contextuality`) in the Jaynes appendix; two `%% PAPER2` / `%% PAPER3` comments await companion-paper citation keys
- Notebook T: extend Cayley-Dickson constructor to trigintaduonions to settle ℤ/2 vs S₃ branch dichotomy by construction
- `op:baryon-contact` (proton stability via quartic ε(qqq)ℓ structure): tied to op:heunen-functor Hopf-Frobenius machinery
- Attic rename of `entanglement_classes_section_2026-06-08.tex` once main.tex `\input` is confirmed

### Flagged against current work

- Active work centres on the sedenion framework: zero-divisor structure, G₂-orbit, colour dictionary, sterile sector, and the D4 arena of four-qubit entanglement
- A sedenion session (August 2026) produced double-verified Python scripts (seed-locked, Convention A Cayley-Dickson), session notes, RIS batches, and a D4-ledger addendum
- One script (sedenion_zero_divisor_scan_2026-08-31.py) remains unechoed
- A housing seam between the K3 document's Class-4 placement and the psi-fixed line placement requires a bridge test
- The up-quark mass paragraph in `masses_section` was patched (2026-08-24) to remove a GHZ–W interference fossil, replaced with cross-algebra excursion / comparability condition language consistent with `op:up-quark`
- Fossils flagged but not yet patched: the following paragraph's "two-per-cent W component"; entries in `fermion_topology_table.py` and `fermion_topology_open_problems.md` §5.2

### Paper 2

- Paper 2 ("Spacetime from the FANOUT Boundary") has a compilable skeleton
- The gravitational wave energy objection is answered: Isaacson averaging scale = chart re-emergence scale
- Seven open problems are priced; next computation is the Newtonian limit (op:p2-newton)

## 2026-09-11 -- op:koide-delta sharpened (see sessions/koide_delta_gap_2026-09-11T1600.md)

- **OPEN** `[PROPOSED]` Derive delta = 2/9 rad. PASS: a mechanism that returns
  a value inside delta = 0.2222248 +/- 0.0000063 rad (PDG 2024; the tau mass
  sets the band) with no fitted input. FAIL: any route that ends in a rational
  multiple of pi, an inverse trigonometric function of a simple algebraic
  number, or a round-sphere holonomy -- these are excluded by the scan and by
  notebook M. Constraint: the answer is a rational number of radians, which
  points at a flat structure with rational periods (the S1 fibre) rather than
  the round Hopf connection the problem is currently phrased around. Four
  routes closed; see invalid_routes.md, 2026-09-11.
- Parameter count, for the headline claims: the charged-lepton sector has no
  fitted dimensionless parameter and one matched one (delta). The paper's
  "zero adjustable dimensionless parameters" is made consistent with this in
  the 2026-09-11 patch; the count returns to zero only when op:koide-delta
  closes.

## 2026-09-11 -- op:koide-delta restated in the paper's own construction (see sessions/koide_flat_direction_2026-09-11T1900.md)

- **OPEN** `[PROPOSED]` op:koide-delta, restated: derive Re(u_1 u_2 u_3) =
  cos(2/3) for the three off-diagonal unit octonions of the democratic J3(O)
  element, equivalently the Bargmann invariant 3 delta = 2/3 of three mutually
  unbiased generation states (prop:koide-jordan). PASS: a value of 3 delta
  inside 0.6666743 +/- 0.0000188 rad with no fitted input. FAIL before
  checking: any route ending in an algebraic e^{i delta}. Constraint: the u_i
  must be exponentials exp(theta_i n_i) of rational multiples of imaginary
  units, with angles summing to 2/3 in the coplanar case; the flat structure
  is non-compact in the direction that carries the phase, and the number is an
  area or a length in natural units. Supersedes the 2026-09-11 entry above in
  its phrasing of "the S1 fibre" as the flat structure. Eight routes closed in
  all; see invalid_routes.md, both 2026-09-11 sections.
- **OPEN** `[PROPOSED]` The QED problem: an exact tree-level 2/9 at the pole
  masses must survive corrections of relative size alpha_em/pi, which would
  move delta by about 5e-4 rad (eighty sigma) unless they cancel in the
  combination the Z3 form sees. Any derivation inherits this; cf. Sumino 2009
  (VERIFY-CITE). No PASS/FAIL yet beyond the band itself.
