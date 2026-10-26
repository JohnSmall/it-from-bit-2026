# Session note: Barontini's cold-atom entropic time, read and fenced

Date: 2026-10-21T2059. Session: Claude Code (Opus 5).
Source: `~/Documents/physics_papers/testing_the_problem_of_time_with_cold_atoms.pdf`,
read in full (6 pages, a Letter). Reference imported the same day as
`barontini2026relationaltime`; batch `bib/relational_time_cold_atoms_ref_2026-10-21T1600.bib`.

JS supplied the reference, asked for a reading, and set its status himself:
corroborating evidence that the computational reading of spacetime is pointed
the right way, and no more than that. This note records the reading, the
grounds for that ceiling, and the fence any citation has to carry.

## 1. What the paper does

Giovanni Barontini, *Testing the problem of time with cold atoms*, Phys. Rev.
Research **8**, L022047 (2026), doi 10.1103/1h9j-df4k. Received 25 July 2025,
accepted 29 April 2026.

A rubidium-87 condensate of 2.4e4 atoms in a conservative harmonic trap,
trapping frequencies 2 pi x (25, 70, 70) Hz, split by an 8 micron optical
barrier into an unobserved "dark" and an observed "bright" sector. Over the
100 ms of interest there is no measurable dissipation or particle loss, so the
whole is effectively closed with a time-independent Hamiltonian. Imaging every
2 ms for 120 ms, repeated at several barrier heights.

Entropy per atom is measured thermometrically and S = N s. The internal clock
is phi, the bright sector's centre of mass. The entropic time is

    tau(lambda) = (sigma / k_B) * integral_lambda |dS/dphi| dphi.

He verifies that the total entropy of dark plus bright is constant within
errorbars, which is the right control for "entropy moves between sectors and
is globally conserved". He then rewrites the laboratory-time-independent
Schroedinger equation in tau and reproduces the measured condensate width.

## 2. What is genuinely non-trivial in it

Not that an internal clock can be built. That the internal clock is
**demonstrably not a relabelling of the external one**:

- no entropic time elapses between a big crunch and the next big bang, because
  no entropy crosses the barrier there, while laboratory time runs on;
- raising the barrier slows the entropic clock, and at the top it stops
  altogether, his "heat death", which in laboratory time is a stationary state;
- so the ordering of events survives while the duration assigned to them is
  reassigned.

That is order and duration coming apart, measured on a bench.

## 3. Why the ceiling JS set is right, and if anything generous

**The evidential distance is two steps, not one.** The condensate is, in his
own words, "structurally similar to" a minisuperspace model; minisuperspace is
a truncation of general relativity with homogeneity imposed. Condensate to
minisuperspace to Wheeler-DeWitt to the spacetime of `op:comp-metric` is three
links, each an analogy someone argued for.

**And the apparatus has a clock on the wall.** The entropic time is built from
data already ordered by laboratory time and then shown to reproduce that
ordering. This can show the construction is not vacuous. It cannot show that
relational time is what time *is*, because the setup never lacked an external
one. The framework's claim concerns the case where there is nothing else, and
no analog experiment carrying a laboratory frame can reach it.

**Three further criticisms of the paper on its own terms**, recorded so that
nobody cites it more confidently than it deserves:

- The title's word "testing" is not earned. No outcome could have falsified
  the construction; had the clock failed to order the data, a different clock
  field would have been chosen, which he lists as future work. His own summary
  word, "benchmark", is the honest one.
- Monotonicity is secured by the absolute value in the integrand, not
  discovered. The text calls it "crucial" that tau grows monotonically; that is
  close to a tautology. The "wiggles" he reports fall exactly where dS and dphi
  disagree in sign, which is where the construction is actually fragile.
- The entropic-time Schroedinger equation is the laboratory-time-independent
  equation reparametrised by tau. Its agreement with the data is a consistency
  check, not an independent prediction, since the same data defined tau.

## 4. The fence [RHYME, proposed]

**Proposed for the ledger, for JS to accept, amend or reject.**

- **RHYME** `[PROPOSED]` Barontini's cold-atom entropic time is a laboratory
  instance of order and duration coming apart: an internal parameter built from
  entropy exchange across an observed/unobserved partition orders the observed
  sector's events while assigning them durations unlike the external clock's.
  The framework asserts the same separation in
  `project-docs/records_causal_structure_high_temperature_2026-09-20T1400.md`,
  where causal order survives above the electroweak crossover and metric scale
  does not. A fenced analogy and nothing more: his partition is an optical
  barrier in a trap, not a FANOUT boundary, and his minisuperspace resemblance
  is his own claim about his own apparatus. It corroborates the direction of
  `op:comp-metric` and contributes no step of its proof.

**A citation of this paper carries RHYME unless the sentence is purely
reportorial.** The thing to avoid is a sentence that slides from "an entropy
parameter can order events" to "spacetime is computational". That is the
paper's own overreach in its title, and the framework should not inherit it.

## 5. Currency caution

His entropy is coarse-grained thermodynamic entropy from thermometry. The
framework's real column is a record count in Landauer units. **These are not
the same quantity.** A sentence that moves between them without saying so
repeats the error already logged for `guryanova2020projective` in
`project-docs/complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`
section 4e, where the direction was right and the currency was wrong.

## 6. Contact points that are real

- His bright/dark partition is structurally the FANOUT boundary: observed
  against unobserved, entropy crossing, global state pure.
- He cites Mott's cloud chamber for classical records arising from entanglement
  while the global state stays pure. That is `mott1929tracks`, already in the
  bibliography, imported for exactly that purpose in the complex-cost v2 batch.
- His closing paragraph raises, and does not answer, whether entropic time and
  the thermal time of Connes and Rovelli coincide in any limit. He notes his
  construction is dynamical where the thermal time hypothesis is an equilibrium
  statement.

## 7. Proposed open problem

**For JS to mint or decline.** Not minted here.

- **OPEN** `[PROPOSED]` Do entropic time and thermal time coincide in a limit?
  PASS: exhibit a regime in which the entropic time of an observed sector,
  built from entropy exchange with its complement, agrees with the modular flow
  of the thermal state on that sector (`connesrovelli1994thermal`), with the
  agreement derived rather than fitted. FAIL: a proof that they cannot, or an
  explicit regime where they measurably diverge. Why the framework should care:
  the thermal-time material is currently postulated, and this is the only route
  on the table that ends at something measured. Barontini raises the question
  and leaves it open.

## 8. Not done

- No ledger was edited; sections 4 and 7 are proposals only.
- Nothing in `paper1/` was changed. No sentence cites this paper yet.
- The paper's bodies of its own references were not chased; the Mott
  connection is read off his citation, not verified against his use of it.
