# Session note: graded FANOUT as the rotation of a complex cost

Date: 2026-09-18T0830. Session: Claude Code (Fable 5.1), `it_from_bit_fable_5_1`.
Continues `knowledge/project-docs/complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`.

## JS's brief

Move from "deletion before FANOUT is free, and Landauer applies sharply
after" to "deletion before FANOUT has a complex thermodynamic cost". The
attraction: no sharp cut where thermodynamics suddenly applies; it fits the
graded FANOUT of the Wigner's-friend section (a record is many copies, not
one event), with the real part of the cost accumulating over copies and the
phase parts cancelling; and it fits Hawking's complex temperature for a CTC
and Zurek's quantum Darwinism.

## The argument

Labels are proposals; JS applies them.

### 1. The complex cost is a standard object seen from a new side

**STRUCTURAL.** Let a system qubit $a|0\rangle + b|1\rangle$ be copied into
$R$ environment fragments, fragment $k$ going to $|\epsilon_0\rangle$ or
$|\epsilon_1^k\rangle$ according to the branch. The system's coherence
after $R$ copies is $a b^{*}\prod_k \overline{\lambda_k}$ with
$\lambda_k = \langle\epsilon_0|\epsilon_1^k\rangle$: Zurek's decoherence
factor, a product of complex overlaps. Its complex logarithm is the cost:

    C_R = - sum_k ln lambda_k,   Re C_R = sum_k ln(1/|lambda_k|),   Im C_R = - sum_k arg lambda_k.

The real part is the accumulated distinguishability of the fragments, the
record; the imaginary part is the phase they impart. This is the
Feynman--Vernon influence functional $e^{iS_I}$ with complex influence
action: $\mathrm{Im}\,S_I$ is decoherence, $\mathrm{Re}\,S_I$ is the phase
shift. The 2026-07-26 note's RHYME-2 clause (v), "Im(influence action) =
the decoherence functional", is therefore not a rhyme but an identity: the
complex cost is $i$ times the influence action, sign conventions aside.

### 2. Graded FANOUT is the rotation of the cost [STRUCTURAL, computed]

With $|\lambda_k| = \cos\phi$ for all fragments, $\mathrm{Re}\,C_R = R\gamma$,
$\gamma = -\ln\cos\phi$: linear in the number of copies. With independent
fragment phases $\theta_k$ of spread $\sigma$, $\mathrm{Im}\,C_R$ is a random
walk, $E|\mathrm{Im}\,C_R| = \sigma\sqrt{2R/\pi}$, so the angle of the cost
from the real axis falls as $1/\sqrt{R}$ (script: $E|\mathrm{Im}|/\mathrm{Re}$
= 2.23, 1.10, 0.54, 0.27 at $R$ = 16, 64, 256, 1024). A single phase-only
interaction ($|\lambda| = 1$) sits on the imaginary axis; many independent
records sit on the real axis; in between the boundary is an angle, not a
cut. This is the precise form of "the real component accumulates and the
phase components cancel": the phases do not cancel in the global state,
which is unitary, they fail to add coherently, and relative to the real part
they vanish like $1/\sqrt{R}$.

Two things the intuition did not contain:

- There is no sharp cut even at $R = 1$. A single copy with any
  distinguishability at all already has a real part, $\gamma_1 =
  -\ln|\lambda_1|$ (script: 0.00125 nat at $\phi = 0.05$, 0.62 nat at
  $\phi = 1$). Only $|\lambda| = 1$, a fragment that carries no
  which-branch information, is purely imaginary. So "pre-FANOUT" has an
  exact definition: interactions whose fragment overlaps have unit modulus.
  They can still shift phases: the imaginary cost. The Wigner's-friend
  section's "the single relational copy is unitary and free" becomes
  "$R = 1$ costs $\gamma_1 - i\theta_1$, the real part small but not zero".
- The rotation requires independent fragments. With identical phases (a
  coherent environment, every fragment a replica) $\mathrm{Im}\,C_R = R\theta$
  and the angle never moves (script: $-1.48$ rad at every $R$). Such an
  environment can be un-copied by one global operation and shows
  recurrences. Independence of the witnesses is Zurek's condition for
  objectivity, and it is what the framework must build into its definition
  of a record.

### 3. Zurek: the real part is redundancy, the phase is what fails to proliferate [STRUCTURAL]

The system's entropy saturates at the Landauer value $H(|a|^2)$ (script:
$S/\ln 2$ = 0.15, 0.62, 0.96, 1.00 at $R$ = 1, 8, 32, 128) while
$\mathrm{Re}\,C_R$ keeps growing. The surplus is redundancy: the count of
records, which is the $R$ of the redundancy ladder. Landauer's bound is per
bit erased at the system; the accumulated real cost is per copy in the
environment. The mutual information $I(S{:}F_f)$ with a fragment set of
size $f$ reaches the plateau $H_S$ well before $f = R$ and exceeds it only
when nearly all fragments are held (script: $I/H_S$ = 1.00 at $f = 12$ of
24 for weakly distinguishing fragments, 2.00 at $f = 24$): the pointer
information is redundant, the phase information is not. That is the exact
sense in which the imaginary part is "paid at the cut": it is conserved
globally and available locally to no one.

### 4. Hawking: the rotation is his rotation, with the angle derived [CANDIDATE; coth identity STRUCTURAL]

In the Caldeira--Leggett influence functional the noise kernel carries
$\coth(\beta\omega/2)$ and is the real-cost part; at imaginary inverse
temperature $\beta = ia$, $\coth(ix) = -i\cot x$ (script: identity to
machine precision), so the noise kernel becomes a phase: the bath's real
cost vanishes and only phase remains. That is Hawking's CTC bath at
imaginary temperature, and it is the pre-FANOUT regime. Hawking rotates
$1/T$ toward the real axis by keeping a small real part by hand, and that
real part damps the divergences. Here the real part arrives by counting:
$\mathrm{Re}\,C_R = \sum_k \ln(1/|\lambda_k|)$, and the angle is
$1/\sqrt{R}$. So the framework supplies the angle Hawking put in, as a
function of the redundancy, and the "damping" is the suppression of
recurrences by many independent witnesses.

### 5. What the change does to the framework's statements

- "Free" becomes "purely imaginary": correct only for $|\lambda| = 1$.
- The sharp FANOUT boundary becomes an angle, $\arctan(\mathrm{Im}/\mathrm{Re})$,
  that falls as $1/\sqrt{R}$ for independent records; the five faces of the
  regime (negativity, anti-events, no record, no basis, continuity) become
  graded together, since "no record" is $|\lambda| = 1$.
- The anti-event's cost $i\pi$ (surprisal of $-1$) is the imaginary axis
  itself; it is "paid", made inaccessible, only when records exist.
- The 2026-07-26 chain "imaginary temperature => complex ledger on the loop
  => real coherence loss at the record" acquires its mechanism.

### 6. Fences

- The model is pure dephasing on a branching state: no energy exchange, no
  back-action, environment a set of pure fragments. The real cost is
  coherence loss in nats and equals entropy production at the system; it
  is heat only when the environment is thermal and $kT$ converts it.
  "Thermodynamic" is so far the informational side.
- Imaginary temperature is a formal limit of the influence functional;
  Hawking's CTC is exotic; the framework's identification of the
  pre-FANOUT loop with a CTC is CANDIDATE, and the mapping in section 4
  inherits that status.
- At finite $R$ the coherence modulus $e^{-R\gamma}$ can revive if the
  fragments' states realign (recurrences); large $R$ suppresses them, which
  is the same fact as Hawking's damping. A coherent environment never
  suppresses them.
- Nothing here is a number for the paper; it is the mechanism behind a
  statement the paper makes in words.

### 7. JS's objection: the global phase is unobservable, so the deletion is free in practice

**STRUCTURAL.** The imaginary cost in the model is not a global phase. The
fragment phase $\theta_k$ is imparted to the $|1\rangle$ branch of the system
relative to the $|0\rangle$ branch: the coherence becomes
$ab^{*}e^{-i\sum\theta_k}$, and an $X$-basis measurement of the system reads
it, $P(+) = (1 + \cos\sum_k\theta_k)/2$. A phase-only interaction
($|\lambda| = 1$, a controlled phase) changes the system's interference
pattern and can be undone by another; it is free of dissipation, not free
of consequence. Likewise the anti-event's $i\pi$ is the sign of one entry
relative to the others, which is what negative quasi-probability shows up
as in interference. "Deletion" before FANOUT relocates information into
relative phases (a Hadamard deletes a bit from the computational basis into
the phase basis); the imaginary cost is that relocated information,
conserved and recoverable.

**When the phase is global.** If the operation phases every branch alike,
the phase is the Hopf fibre: no degree of freedom of the ray, unobservable
to the system alone, and carrying no cost because it carries no
information. The framework already names this: the global phase is the
self-referential ignorance (L^2 section title). But the global phase of a
subsystem is a relative phase of the composite, observable as soon as a
second party exists, and FANOUT is the arrival of the second party. So
"free for all practical purposes" is the pre-FANOUT condition restated
(no one has compared), not an objection to the cost.

**The sharpening.** Declaring the phase unobservable is discarding it, and
discarding it is what costs. Averaging the coherence over untracked
fragment phases gives the same reduced state as decoherence: the moment the
observer treats $\sum\theta_k$ as inaccessible, the imaginary cost has been
converted into the real one. Landauer's toll is incurred not by the
unitary but by the inaccessibility, i.e. by the redundancy that produces
it. In the model: cost $i\sum\theta_k$ while the phases are tracked; cost
$\sum_k\ln(1/|\lambda_k|) \to$ the Landauer value once they are not.
Reading [CANDIDATE]: the part of the phase that is free is exactly the
observer's blind spot, "free" and "ignorant" being the same fact seen from
the two sides of the boundary.

## What was computed

`scripts/graded_fanout_complex_cost_2026-09-18T0830.py`, seed 20260918,
closed forms validated against an explicit state vector at $R = 4$. Exact
stdout:

```
graded_fanout_complex_cost_2026-09-18T0830.py  seed=20260918  a=b=1/sqrt2  phi=0.30  sigma=0.50
per-copy real cost gamma = -ln cos(phi) = 0.045692 nat;  |lam| = 0.955336
--- validation: closed forms against an explicit state vector, R = 4
  rho_S(0,1) explicit = 0.414863-0.036679i ; closed form a b* prod conj(lam) = 0.414863-0.036679i
  S(rho_S) explicit = 0.287280 ; closed form = 0.287280
  I(S:F) for F = fragments 1,2: explicit = 0.287280 ; closed form = 0.287280
--- the cost with R copies: independent phases (theta_k ~ N(0, sigma)) vs identical phases
     R       Re C Im C(rand) arg(rand)      |D_R| S(rho_S)/ln2  Im C(same) arg(same)
     1     0.0457    -0.3882   -1.4536  9.553e-01      0.1543      -0.500   -1.4797
     2     0.0914     0.3281    1.2992  9.127e-01      0.2589      -1.000   -1.4797
     4     0.1828     1.2358    1.4240  8.330e-01      0.4145      -2.000   -1.4797
     8     0.3655    -0.7238   -1.1032  6.938e-01      0.6175      -4.000   -1.4797
    16     0.7311     0.6614    0.7354  4.814e-01      0.8257      -8.000   -1.4797
    32     1.4621    -0.5306   -0.3481  2.317e-01      0.9609     -16.000   -1.4797
    64     2.9243    -1.7448   -0.5380  5.370e-02      0.9979     -32.000   -1.4797
   128     5.8485     5.5645    0.7605  2.884e-03      1.0000     -64.000   -1.4797
   256    11.6971     3.3336    0.2776  8.318e-06      1.0000    -128.000   -1.4797
  1024    46.7883    -7.1439   -0.1515  4.788e-21      1.0000    -512.000   -1.4797
  E|Im C| over 2000 trials vs sigma sqrt(2R/pi); and E|Im C| / Re C:
    R=  16  E|Im C| = 1.630  (predicted 1.596)   E|Im C|/Re C = 2.2292  (~ 1/sqrt(R))
    R=  64  E|Im C| = 3.218  (predicted 3.192)   E|Im C|/Re C = 1.1004  (~ 1/sqrt(R))
    R= 256  E|Im C| = 6.363  (predicted 6.383)   E|Im C|/Re C = 0.5440  (~ 1/sqrt(R))
    R=1024  E|Im C| = 12.659  (predicted 12.766)   E|Im C|/Re C = 0.2705  (~ 1/sqrt(R))
--- phi = 0 (no distinguishability): cost purely imaginary, entropy zero, any R
  R=   1  Re C = -0.0  Im C = -0.388  S(rho_S) = 0.0
  R=  10  Re C = -0.0  Im C = 0.116  S(rho_S) = 0.0
  R=1000  Re C = -0.0  Im C = -6.806  S(rho_S) = 0.0
--- a single copy with phi > 0 already has a real part: the boundary is graded
  phi=0.05  |lam|=0.9988  Re C_1 = 0.00125 nat  S(rho_S)/ln2 after one copy = 0.00755
  phi=0.10  |lam|=0.9950  Re C_1 = 0.00501 nat  S(rho_S)/ln2 after one copy = 0.02519
  phi=0.30  |lam|=0.9553  Re C_1 = 0.04569 nat  S(rho_S)/ln2 after one copy = 0.15434
  phi=0.60  |lam|=0.8253  Re C_1 = 0.19197 nat  S(rho_S)/ln2 after one copy = 0.42750
  phi=1.00  |lam|=0.5403  Re C_1 = 0.61563 nat  S(rho_S)/ln2 after one copy = 0.77775
  phi=1.40  |lam|=0.1700  Re C_1 = 1.77215 nat  S(rho_S)/ln2 after one copy = 0.97906
--- quantum-Darwinism plateau at R = 24: I(S:F_f)/H_S against fragment size f
  H_S/ln2 = 0.9180 ;  f=1:0.177  f=2:0.300  f=3:0.403  f=4:0.492  f=6:0.644  f=8:0.773  f=12:1.000  f=16:1.227  f=20:1.508  f=23:1.823  f=24:2.000
  (the phase information needs f -> R: I(S:F) exceeds H_S only when nearly all fragments are held)
--- coth(i x) = -i cot(x): the thermal noise kernel becomes a phase at imaginary temperature
  x=0.3  coth(ix) = 0.000000-3.232728i   -i cot(x) = -0.000000-3.232728i   |diff| = 0.0e+00
  x=1.0  coth(ix) = 0.000000-0.642093i   -i cot(x) = -0.000000-0.642093i   |diff| = 0.0e+00
  x=2.0  coth(ix) = -0.000000+0.457658i   -i cot(x) = -0.000000+0.457658i   |diff| = 0.0e+00
done.
```

## Proposed ledger entries

### results_ledger.md, dated 2026-09-18

- **STRUCTURAL** The complex cost of copying a system into fragments is
  $C = -\sum_k \ln\langle\epsilon_0|\epsilon_1^k\rangle$: real part the
  accumulated log-distinguishability (the record), imaginary part the
  accumulated phase; it is $i$ times the Feynman--Vernon influence action.
  Pre-FANOUT is exactly $|\lambda_k| = 1$ (purely imaginary cost); any
  distinguishability at $R = 1$ already has a real part.
- **STRUCTURAL** For independent fragment phases the angle of the cost from
  the real axis falls as $1/\sqrt{R}$ ($E|\mathrm{Im}\,C| = \sigma\sqrt{2R/\pi}$
  against $\mathrm{Re}\,C = R\gamma$); for identical phases it does not
  rotate. The system's entropy saturates at the Landauer value while the
  real cost grows as redundancy; the phase information is not redundant
  (needs $f \to R$).
- **STRUCTURAL** $\coth(ix) = -i\cot x$: at imaginary inverse temperature
  the Caldeira--Leggett noise kernel is a phase; the bath has no real cost.
- **CANDIDATE** The graded FANOUT boundary is the rotation of the complex
  cost from the imaginary axis (Hawking's CTC bath, the self-referential
  loop) to the real axis (Landauer), with the angle a function of the
  redundancy; Hawking's hand-inserted real part of $1/T$ is
  $\sum_k\ln(1/|\lambda_k|)$.

### open_problems.md, dated 2026-09-18

- **OPEN** op:complex-cost, refined: (i) define the cost as above for
  general (not pure-dephasing) system--fragment couplings, with energy
  exchange, and show its real part reduces to Landauer's $kT\ln 2$ per bit
  for a thermal environment; (ii) prove that for a branching state the
  phase of the coherence is recoverable from a fragment set $F$ only to the
  extent $\prod_{k\notin F}|\lambda_k| \to 1$, the quantitative form of
  "the imaginary part is paid at the cut"; (iii) derive the real part of
  Hawking's complex inverse temperature as the fragment sum. PASS: (i)--(iii)
  with the $1/\sqrt{R}$ law for independent witnesses. FAIL: any version in
  which a coherent (replica) environment pays a real cost, or in which the
  record's entropy acquires an imaginary part.

## References to verify before citing (none cited in the paper yet)

- Feynman and Vernon 1963, Ann. Phys. 24, 118 (influence functional).
- Caldeira and Leggett 1983, Physica A 121, 587 (noise and dissipation
  kernels; the $\coth$).
- Zurek: `zurek2003decoherence`, `zurek_2009` already in the bibliography
  (decoherence factor; quantum Darwinism, redundancy, the plateau).
- Hawking: `Hawking1995QuantumCurves`, in the bibliography.

## The Qiskit notebook (added later the same morning, at JS's request)

`notebooks/notebook_S_graded_fanout_complex_cost_2026-09-18.ipynb`, written
by `scripts/make_notebook_S_graded_fanout_2026-09-18T0900.py` in the house
format of the lettered notebooks (title "Computation S", paper line,
markdown between cells, seed 20260918). The branching state is a circuit:
$H$ on $S$, then per fragment `cry(2 phi)` and `crz(theta_k)` controlled on
$S$, so $\lambda_k = e^{-i\theta_k/2}\cos\phi$ (the phase now lives in the
fragment, not on $S$). Six code cells: the circuit and closed-form checks
(coherence and entropy match to six figures); the rotation table for
$R = 1..12$ from statevectors plus the $1/\sqrt{R}$ ensemble law; the
graded boundary at $R = 1$; the Darwinism plateau for $R = 10$ at
$\phi = 0.3$ and $1.0$ with a figure; and the objection cell on Aer with
20000 shots: phase-only copies read in the $X$ basis ($P(+) = 0.0053$
measured against $0.0050$ from the formula for $\theta_k = 1$; the random
draw happened to sum to $-0.0078$ and gave $1.0000$ both ways, so a chosen
case was added), reversal to $P(+) = 1.0000$, and the untracked-phase
average $0.8257$ against $e^{-R\sigma^{2}/8} = 0.8290$.

Executed in a scratch environment (qiskit 2.5.2, qiskit-aer 0.17.2,
matplotlib 3.10.9; a venv built in the session scratchpad because the
system Python has no Qiskit and no venv bootstrap) by a kernel-free runner
that exec's the code cells in one namespace and writes stdout and PNG
figures back into the .ipynb; the committed notebook carries those real
outputs. No error outputs. Any Qiskit >= 1.0 environment re-runs it.

## Files

- `scripts/graded_fanout_complex_cost_2026-09-18T0830.py` (new)
- `scripts/make_notebook_S_graded_fanout_2026-09-18T0900.py` (new)
- `notebooks/notebook_S_graded_fanout_complex_cost_2026-09-18.ipynb` (new,
  executed)
- this note
- section 4b appended to
  `knowledge/project-docs/complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`

No paper text changed (v2 material). Uncommitted.
