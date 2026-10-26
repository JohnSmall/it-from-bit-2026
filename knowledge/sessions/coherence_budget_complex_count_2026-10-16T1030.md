# Session note: the coherence budget, and what Hawking's imaginary temperature counts

Date: 2026-10-16T1030. Session: Claude Code (Fable 5.1), thinking session.
Continues `knowledge/sessions/hypodox_ctc_fanout_2026-10-16T0900.md` (the
hypodox as an open loop) and the September complex-cost notes
(`knowledge/project-docs/complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`,
`knowledge/sessions/graded_fanout_complex_cost_2026-09-18T0830.md`). Script:
`scripts/coherence_budget_complex_count_2026-10-16T1030.py`, seed 20261016,
numpy only, final line `COHERENCE BUDGET COMPLEX COUNT: PASS`; exact stdout
in section 13. Reference batch:
`bib/complex_temperature_coherence_refs_2026-10-16T1040.bib`. Hawking
gr-qc/9502017 read today in full (pdftotext). Labels are proposals; JS
applies them. Nothing in the paper was patched.

## 0. Answer in brief

JS's claim: "From Hawking we know that a CTC has complex temperature, which
implies complex entropy, which implies a CTC encloses a region of complex
information. Therefore the information added to an agent's knowledge when
an observation is made, which closes an apparent CTC, should exactly match
the imaginary component of an agent's pre-FANOUT state of knowledge, thus
yielding a purely real value."

The conclusion is an exact identity under one reading of "imaginary
component" and false under the other, and the framework's own notes have
used both. The premises need two corrections of wording and one of scope.

1. **Exact, with "imaginary component" = the coherence in the record
   basis.** Let C_Z(rho) = S(Delta_Z rho) - S(rho), the relative entropy of
   coherence. Along the whole graded FANOUT the record-basis distribution is
   untouched, so

       S(rho_N) + C_Z(rho_N) = H(p)   for every N,

   verified to 1e-10 at every stage and every relative phase. What the
   records have gained (the system's entropy, which is the environment's
   information about it) plus the coherence still unspent equals the final
   real value. A pure pre-FANOUT state has S = 0 and C_Z = H(p): the
   coherence spent is exactly the information the record gains. The chain
   ends in diag(p, 1 - p), a real matrix. STRUCTURAL: it is the definition
   of C_Z plus the invariance of the diagonal under copying.
2. **False, with "imaginary component" = the phase.** C_Z is independent of
   the relative phase (four phases, identical C_Z = 0.8813); the X-coherence
   is not (0.25 to 0.99). A record in basis B spends the B-coherence, which is
   the complementary basis's data, and is blind to the phase of the
   record-basis amplitudes. The phase is promoted: under a full CNOT the
   joint coherence in the product basis is H(p) before and after. In the
   September complex cost C = gamma - i phi per fragment, the coherence is
   spent by the REAL part gamma = -ln|lambda|, and the imaginary part phi is
   not spent at all (two fragment phases, identical C_Z). So "decoherence is
   the phase becoming entropy, the imaginary part becoming heat" (09-16
   note, section 3(b)) has it backwards: the modulus becomes entropy and the
   real part of the cost is the heat. Second-order finding, section 8.
3. **Hawking, read today.** The temperature is imaginary, verbatim ("The
   only difference is that the temperature of the heat bath is imaginary"),
   and the result he draws is the budget itself: a pure state is carried
   into a mixed state because part of the state circulates on the loop and
   is traced out. For a two-level loop the "entropy" S = ln Z + beta<H> at
   imaginary beta is real while the count Z = Tr U is positive (and exceeds
   ln 2, so it is not an entropy), undefined at Z = 0, and has imaginary part
   exactly pi where Z < 0: the anti-event's i pi of the 09-16 note, and
   nothing else. Genuinely complex S needs three or more levels. "Complex
   temperature implies complex entropy" is therefore true generically and
   false for the bit. The count of a one-qubit loop is Tr U: 2 for the
   identity loop (the truth-teller), 0 for the Liar loop (the zeros of Z lie
   on the imaginary axis: the Liar loops are the Fisher zeros), -2 at a full
   2 pi turn (the spinor sign as a negative count). The FANOUT inside a loop
   removes one bit of count, 4 to 2, graded as 2 + 2cos(theta/2); that bit is
   the record's capacity, and the information gained, H(p), is at most it,
   not equal to it. The exact match is with the coherence, not with the
   count.
4. **The citable bridge from Hawking to the FANOUT.** Wei and Liu (2012;
   Peng et al. 2015 experimentally): the coherence of a probe spin coupled
   to a bath, as a function of time, is the bath's partition function at
   complex temperature or field, with time as the imaginary part; its zeros
   in time are the Lee--Yang zeros. So the September decoherence factor is
   a complex partition function and the complex cost a complex free energy.
   That is the chain JS wants, with a literature behind it, and it puts the
   Liar loop at a zero of the partition function. STRUCTURAL at the level of
   the abstracts (VERIFY-SUPPORT for the exact mapping).

## 1. What the paper and the notes say

`paper1/what_is_a_quantum_state.tex` (the Chaitin paragraph): "This leap of
faith gains some support from Hawking's observation that closed timelike
paths have a complex temperature \autocite{Hawking1995QuantumCurves} and
hence the number of states enclosed in the CTC is counted in imaginary
numbers."

`complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`, section 3(b):
"Unitarity is then the conservation of the imaginary cost (phase
information is moved, never destroyed), and FANOUT is the event that
converts imaginary cost into real cost: decoherence is the phase becoming
entropy, the imaginary part becoming heat."

`graded_fanout_complex_cost_2026-09-18T0830.md`, section 2: Re C_R = sum
ln(1/|lambda_k|) is the record; Im C_R = -sum arg lambda_k is a random walk
that "fails to add coherently" and falls relative to the real part as
1/sqrt(R). (This is already the correct accounting; the 09-16 sentence is
the one that conflicts with it.)

`session_summary_ctc_supertask_imaginary_temperature_2026-07-26.md`,
section 4.3: "Every functional built on the weights (ln Z, S = E/T + ln Z)
goes GENERICALLY COMPLEX"; "imaginary temperature => complex (ledger-valued)
information ON THE LOOP => real coherence loss AT THE RECORD. The imaginary
part is paid at the cut."

## 2. Hawking, read [STRUCTURAL, quotations from gr-qc/9502017]

- "there is loss of quantum coherence caused by the fact that part of the
  quantum state circulates on the closed timelike curves and is not
  measured at infinity." (abstract)
- "A particle that is initially in a pure quantum state, which interacts
  with the heat bath, will end up in a mixed quantum state. This loss of
  quantum coherence is to be expected: information about the original
  quantum state of the particle is lost into the heat bath. [...] The only
  difference is that the temperature of the heat bath is imaginary. This
  corresponds to a spacetime that is identified periodically in real
  Lorentzian time, rather than periodically in imaginary time, as in a
  normal heat bath."
- "One will therefore have to describe the state at infinity by a mixed
  state, obtained by tracing out over the part of the state that one can't
  see."
- On the rotation: "One should keep a small imaginary part to the
  separation. This damps possible divergences from high frequency modes by
  reducing them by a thermal factor, exp(-E/T), with 1/T imaginary but with
  a small positive real part." And: "I therefore think one should take the
  sum of the rotations in both directions. This will ensure that the
  probabilities of going from initial to final are real."
- Against Deutsch: the consistent-density-matrix approach "will also depend
  in a non linear way on the initial state, which means that one loses the
  superposition principle"; Hawking's own prescription is linear, a
  superscattering operator.

Three things follow for the claim. First, Hawking's imaginary temperature
is the statement that the loop's weight is Tr e^{-i H tau}, the trace of the
loop's evolution: the "trace before the diagonal" of the 0900 note, and the
P-CTC's operator. Second, his physical conclusion, pure to mixed by tracing
out the loop, is exactly the conversion of coherence into entropy that the
budget identity quantifies. Third, "complex temperature" is his analytic
continuation, imaginary with a small real part, and the September note's
section 4 already reads the real part as the record side; nothing today
changes that.

## 3. The count [STRUCTURAL, computed]

One qubit, H = X/2, Z(beta) = Tr e^{-beta H} = 2cosh(beta/2). On the
imaginary axis beta = i tau the loop is U = e^{-i tau X/2} and Z = Tr U =
2cos(tau/2):

| tau | U | Z = Tr U | S = ln Z + beta<H> |
|---|---|---|---|
| 0 | I | 2 | ln 2 (real) |
| pi/2 | | 1.4142 | 1.1320 (real, > ln 2) |
| pi | -iX | 0 | undefined |
| 3pi/2 | | -1.4142 | -2.0096 + i pi |
| 2pi | -I | -2 | ln 2 + i pi |

The zeros of Z(beta) are at beta = i pi (2k + 1), on the imaginary axis,
and there the loop is -iX up to sign: the Liar loops are the Fisher zeros
of the partition function. The identity loop counts two states, the
truth-teller's two fixed points. At a full turn the count is -2: the spinor
sign appears as a negative number of states. For two levels S is real while
Z > 0 (the i's cancel in beta<H>: S = ln(2cos(tau/2)) + (tau/2)tan(tau/2)),
exceeds ln 2 (so it is not an entropy of anything), and acquires exactly
i pi where Z < 0, the branch of the logarithm; it is invariant under energy
shifts modulo 2 pi i. For three levels (spectrum 0, 1, 3) S is genuinely
complex: 1.17 - 0.007i, 1.62 - 0.16i, 2.82 - 2.26i at tau = 0.3, 0.7, 1.1.
So the July note's "generically complex" is right for d >= 3 and wrong for
the bit, where the imaginary part of S is quantised to {0, pi}: the
anti-event's i pi of the 09-16 note, section 3(b), and nothing in between.

The loop with the FANOUT inside it: Tr(CNOT) = 2 against Tr(I_4) = 4, one
bit of count removed; graded, Tr(controlled e^{-i theta X/2}) = 2 +
2cos(theta/2), the bit removed running from 0 to 1 as theta runs from 0 to
pi. This is what "closing the apparent CTC on the record" costs the loop:
its count halves because the record's two states are locked to the
system's. It is a capacity, log 2, and the information actually gained is
H(p) <= log 2. The count matches the information only at p = 1/2.

## 4. The budget identity [STRUCTURAL, computed]

p = 0.3, H(p) = 0.881291 bits, copy angle theta = 2 (fragment overlap
0.5403), relative phase 0.4:

| N | S(rho_N) | C_Z(rho_N) | sum | |rho_01| |
|---|---|---|---|---|
| 0 | 0.000000 | 0.881291 | 0.881291 | 0.4583 |
| 1 | 0.683817 | 0.197474 | 0.881291 | 0.2476 |
| 2 | 0.825814 | 0.055477 | 0.881291 | 0.1338 |
| 3 | 0.865260 | 0.016031 | 0.881291 | 0.0723 |
| 6 | 0.880894 | 0.000397 | 0.881291 | 0.0114 |
| 12 | 0.881291 | 0.000000 | 0.881291 | 0.0003 |

The sum is H(p) at every stage for every relative phase (checked at four),
and the chain ends in diag(0.3, 0.7), real. The system's entropy is the
information the fragments hold about it (the plateau of the 0900 note's
Darwinism curve; part D here: at N = 8, S(rho_S) = 0.881257, C_Z =
0.000034, I(S:F_N) = 2 S(rho_S) with the classical half the plateau and the
quantum half the rise at the whole environment). The S(rho_N) column is the
0900 note's I(S:F_k) at k = N read on the system; the C_Z column is what the
earlier note called the open end.

Phase blindness: C_Z = 0.881291 at relative phases 0, 0.4, 1.7, 3.0; C_X =
0.2502, 0.3948, 0.9899, 0.2706. A record in Z spends the Z-coherence, which
is the X-basis's uncertainty, and never sees the phase; a record in X
spends phase information. This is the earlier note's complementarity
exchange in entropic form: which component is "real" and which "imaginary"
is fixed by the record basis.

Promotion: for |psi>|0> -> CNOT -> alpha|00> + beta|11>, the joint
relative entropy of coherence in the product Z basis is 0.881291 before and
after. The copy is an incoherent operation on the pair (a permutation of
the product basis) and cannot change it. The system's coherence H(p) has
become the system's entropy H(p), and the same H(p) of coherence now sits
one level up, between the branches, exactly the Wigner's friend section's
phase promotion. "Purely real" is true at the agent's level; the imaginary
budget is conserved globally.

## 5. The Wei--Liu form [STRUCTURAL at abstract level; computed here]

With a complex fragment overlap lambda = cos(theta/2) e^{i phi}, the
coherence after N fragments is rho_01 e^{-N(gamma - i phi)}, gamma = -ln
cos(theta/2) = 0.6156 nat at theta = 2. C_Z(N) is identical for phi = 0 and
phi = 0.9 at every N (0.8813, 0.1975, 0.0555, 0.0160, 0.0047, 0.0014,
0.0004): it depends on the real part of the accumulated cost only. In Wei
and Liu's language the coherence factor is a partition function on the
complex plane of temperature with time as the imaginary part, and the
Lee--Yang zeros are where it vanishes; for the qubit loop of section 3 those
zeros are the Liar loops. The September cost C_R = -sum ln lambda_k is then
a complex free energy, and the budget identity says: the record's entropy is
set by its real part; its imaginary part is the phase that is promoted.

## 6. Where the apparent CTC comes in

The 0900 note: the outcome is an open loop the agent closes, and closing it
on the record would cost the value. Today: the closing costs the loop one bit
of count (section 3) and the open chain spends the coherence (section 4).
The agent's "complex information" before the observation is C_Z = H(p) bits
of coherence, which is the information about the complementary basis the
record will destroy; the "real information" after is H(p) bits of record
entropy. The exchange is exact, and it is the exchange of a complementary
structure's data for the record structure's data. Nothing in it requires
the loop to be closed; Hawking's loop is the trace, and the trace of the
agent's loop with the record locked is 2, the two fixed points of the
hypodox.

## 7. What I think

JS's sentence is right if "imaginary component of the pre-FANOUT state of
knowledge" means the coherence in the record basis, the data of the
complementary structure, and the paper should say so in those words. The
identity S(rho) + C_Z(rho) = H(p) is the conservation law behind "yielding
a purely real value", and it is exact at every stage of the graded FANOUT,
not only at the end. It is not right if "imaginary" means the phase, which
is what the September notes and the July chain call imaginary: the phase is
promoted, the modulus is spent, and the real part of the complex cost is
what spends it. The framework has been using "imaginary" for both, and this
is the place to separate them: coherence (spent, converted to record
entropy) and phase (conserved, promoted). The premises: Hawking's
temperature is imaginary, with a small real part added by hand; "complex
entropy" is generic but the bit's is real up to the anti-event's i pi; and
"complex information enclosed" is the count Tr U, which for a loop through
the record is a capacity, not the information gained. Wei and Liu supply the
bridge the framework has wanted since July: a probe spin's coherence is a
partition function at complex temperature, so the decoherence factor of the
September note is Hawking's object seen from the record side.

## 8. Second-order findings for JS's ruling

(a) `complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`, section
3(b): "decoherence is the phase becoming entropy, the imaginary part
becoming heat." Proposed: "decoherence is the coherence becoming entropy;
the real part of the cost, -ln|lambda|, is the heat; the phase, the
imaginary part, is promoted to the next level and never becomes heat." The
07-26 note's "the imaginary part is paid at the cut" (section 4.3) needs the
same change. Both are JS's notes; neither is patched.

(b) `what_is_a_quantum_state.tex`: "the number of states enclosed in the
CTC is counted in imaginary numbers." The count is Tr U, which is complex
in general and, for a two-level loop, real with a sign: 2, 0 at the Liar
loop, -2 at the spinor sign. Proposed: "counted by a complex number, the
trace of the loop's evolution, which vanishes for the paradoxical loop and
is negative for a loop that returns a spinor to minus itself."

(c) `session_summary_ctc_supertask_imaginary_temperature_2026-07-26.md`,
section 4.3: "every functional ... goes generically complex." True for three
or more levels; for the bit S is real while Z > 0 and has imaginary part
exactly pi where Z < 0. Proposed: add "for three or more levels; for a
two-level loop the imaginary part is quantised to 0 or pi, the anti-event's
i pi".

## 9. References

- Hawking 1995 (in the library; read in full today, quotations above).
- Wei and Liu 2012, PRL 109, 185701 (abstract read); Peng et al. 2015, PRL
  114, 010601 (abstract read); Yang and Lee 1952, Lee and Yang 1952
  (titles). All Crossref-verified.
- Baumgratz, Cramer and Plenio 2014 (relative entropy of coherence);
  Streltsov, Adesso and Plenio 2017 (review). Crossref-verified; bodies not
  read, the definition and the monotonicity under incoherent operations are
  standard.
- Zwolak and Zurek 2013 (I = J + D; the two halves). Crossref-verified;
  VERIFY-SUPPORT.

No source found states the budget S + C_Z = H(p) as a reading of Hawking's
loop, or places the Liar loop at a Fisher zero; the budget identity itself
is elementary and should not be claimed as a result, only as the precise
form of a statement the framework makes in words.

## 10. Fences

- S = ln Z + beta<H> at complex beta is a formal continuation, not an
  entropy: for the qubit it exceeds ln 2. Nothing here licenses "complex
  entropy" as a physical quantity; the July note's "ledger-valued" caution
  stands.
- The budget is for a single qubit with Z-copies and an environment of pure
  fragments, as in September. With energy exchange, S(Delta_Z rho) is not
  invariant and the identity becomes an inequality.
- Wei and Liu's mapping is for a probe weakly coupled to an Ising-type bath;
  the identification of the September cost with their complex free energy is
  at abstract level.
- The paper's complex-probability language assigns the imaginary part to
  self-ignorance; today's split (coherence spent, phase promoted) is a
  proposal for how that language should be read, not a derivation of it.

## 11. Proposed ledger entries

results_ledger.md, dated 2026-10-16:

- **STRUCTURAL** Along the graded FANOUT in basis Z, S(rho_N) + C_Z(rho_N)
  = S(Delta_Z rho) = H(p) at every stage (C_Z the relative entropy of
  coherence); a pure pre-FANOUT state spends C_Z = H(p), exactly the
  record's entropy, and the chain ends in a real diagonal matrix. C_Z is
  independent of the relative phase; the joint coherence in the product
  basis is unchanged by the copy (promotion). Script parts B and D, PASS.
- **STRUCTURAL** With a complex fragment overlap, the coherence spent
  depends on the real part of the accumulated complex cost only; the
  imaginary part (the phase) is not spent. Script part C, PASS. Corrects the
  09-16 note's "the phase becoming entropy".
- **STRUCTURAL** For a one-qubit loop at imaginary temperature, Z = Tr U =
  2cos(tau/2): 2 at the identity loop, 0 at the Liar loop (the Fisher zeros
  lie on the imaginary axis at i pi(2k+1)), -2 at a full turn; S = ln Z +
  beta<H> is real while Z > 0, exceeds ln 2, and has Im S = pi where Z < 0;
  genuinely complex S needs d >= 3. A FANOUT inside the loop halves the
  count (graded 2 + 2cos(theta/2)). Script part A, PASS.
- **CANDIDATE** The framework's "imaginary information" splits into
  coherence (the complementary structure's data, spent by a record and
  converted exactly into record entropy) and phase (promoted, conserved).
  "Hawking's complex temperature implies complex information enclosed by
  the loop" is the count Tr U; "the observation converts the imaginary
  component into a real value" is the budget identity with "imaginary" =
  coherence. Via Wei and Liu, the decoherence factor is a partition function
  at complex temperature, which joins the two.

## 12. Files

- `scripts/coherence_budget_complex_count_2026-10-16T1030.py` (new, PASS).
- `knowledge/sessions/coherence_budget_complex_count_2026-10-16T1030.md`
  (this note).
- `bib/complex_temperature_coherence_refs_2026-10-16T1040.bib` (new; 7
  keys, all Crossref-verified; VERIFY-SUPPORT on bodies as listed in the
  header).
- `notes/todo.md` appended; `/tmp/fable_instructions_to_opus.md` section
  9.7h.
- Not patched: the paper, the September notes, the July note. Not built,
  not committed.

## 13. Exact stdout

```
========================================================================
A  Hawking's count for one qubit loop: Z(beta) = Tr exp(-beta H), H = X/2
========================================================================
  real beta (an ordinary bath):
    beta =  0.0: Z =   2.0000, S =   0.6931 nat
    beta =  1.0: Z =   2.2553, S =   0.5822 nat
    beta =  4.0: Z =   7.5244, S =   0.0901 nat
  [ok  ] real beta: S = ln 2 at infinite temperature and falls as beta grows
  imaginary beta = i tau (Hawking's loop, identified periodically in real time):
    tau = 0.0000: Z = Tr U = +2.0000+0.0000i,  S =  +0.6931 +0.0000i
    tau = 1.5708: Z = Tr U = +1.4142+0.0000i,  S =  +1.1320 +0.0000i
    tau = 3.1416: Z = Tr U = +0.0000+0.0000i,  S =     +nan    +nani
    tau = 4.7124: Z = Tr U = -1.4142+0.0000i,  S =  -2.0096 +3.1416i
    tau = 6.2832: Z = Tr U = -2.0000+0.0000i,  S =  +0.6931 +3.1416i
  [ok  ] tau = 0: the identity loop counts two states (the truth-teller's loop)
  [ok  ] tau = pi: Z = 0 and the loop is -iX, the Liar up to phase: no states
  [ok  ] tau = 2 pi: Z = -2, the spinor sign as a negative count
  [ok  ] tau = pi/2: for a two-level loop S is real (the i's cancel in beta<H>) and exceeds ln 2: not an entropy
  [ok  ] Z < 0: Im S = pi exactly, the anti-event's i pi; for the bit the imaginary part of S is quantised to {0, pi}
  three-level loop, spectrum (0, 1, 3): S at imaginary beta
    tau = 0.3: S = +1.1725-0.0074i
    tau = 0.7: S = +1.6192-0.1618i
    tau = 1.1: S = +2.8236-2.2614i
  [ok  ] three levels: S is genuinely complex, Im S neither 0 nor pi; the July note's 'generically complex' needs d >= 3
  [ok  ] two levels, any offset: S real modulo 2 pi i (energy shifts move ln Z across a branch of the logarithm)
  [ok  ] the zeros of Z lie on the imaginary axis at beta = i pi (2k+1): the Liar loops are the Fisher zeros
  the loop with the FANOUT inside it:
    Tr(I_4) = 4.0, Tr(CNOT) = 2.0, ln ratio = 0.6931 = ln 2
  [ok  ] the copy removes one bit of loop count: 4 -> 2
    theta = 0.0000: Tr = 4.0000 = 2 + 2 cos(theta/2) = 4.0000; bits of count removed = 0.0000; one-copy coherence factor cos(theta/2) = 1.0000
  [ok  ] theta = 0.00: graded count 2 + 2 cos(theta/2)
    theta = 1.0000: Tr = 3.7552 = 2 + 2 cos(theta/2) = 3.7552; bits of count removed = 0.0911; one-copy coherence factor cos(theta/2) = 0.8776
  [ok  ] theta = 1.00: graded count 2 + 2 cos(theta/2)
    theta = 2.0000: Tr = 3.0806 = 2 + 2 cos(theta/2) = 3.0806; bits of count removed = 0.3768; one-copy coherence factor cos(theta/2) = 0.5403
  [ok  ] theta = 2.00: graded count 2 + 2 cos(theta/2)
    theta = 3.1416: Tr = 2.0000 = 2 + 2 cos(theta/2) = 2.0000; bits of count removed = 1.0000; one-copy coherence factor cos(theta/2) = 0.0000
  [ok  ] theta = 3.14: graded count 2 + 2 cos(theta/2)

========================================================================
B  The budget identity S(Delta_B rho) = S(rho) + C_B(rho) along the graded chain
========================================================================
  p = 0.3, H(p) = 0.881291 bits; copy angle theta = 2.0, cos(theta/2) = 0.5403
  phi = 0.4, N fresh partial records in turn:
    N      S(rho_N)   C_Z(rho_N)   sum        H(p)       |rho_01|    max|Im rho|
     0    0.000000    0.881291    0.881291   0.881291    0.458258   1.78e-01
     1    0.683817    0.197474    0.881291   0.881291    0.247598   9.64e-02
     2    0.825814    0.055477    0.881291   0.881291    0.133778   5.21e-02
     3    0.865260    0.016031    0.881291   0.881291    0.072280   2.81e-02
     4    0.876625    0.004666    0.881291   0.881291    0.039053   1.52e-02
     5    0.879930    0.001361    0.881291   0.881291    0.021101   8.22e-03
     6    0.880894    0.000397    0.881291   0.881291    0.011401   4.44e-03
     7    0.881175    0.000116    0.881291   0.881291    0.006160   2.40e-03
     8    0.881257    0.000034    0.881291   0.881291    0.003328   1.30e-03
     9    0.881281    0.000010    0.881291   0.881291    0.001798   7.00e-04
    10    0.881288    0.000003    0.881291   0.881291    0.000972   3.78e-04
    11    0.881290    0.000001    0.881291   0.881291    0.000525   2.04e-04
    12    0.881291    0.000000    0.881291   0.881291    0.000284   1.10e-04
  [ok  ] the chain ends in diag(p, 1-p): a real matrix, the purely real value
  [ok  ] S(rho_N) + C_Z(rho_N) = H(p) at every stage, for every relative phase
  pure pre-FANOUT state: the coherence spent equals the information the record gains
  [ok  ] C_Z(pure) = H(p) = the record's entropy; S(pure) = 0
  phase blindness: C_Z against C_X for four relative phases
    phi = 0.0: C_Z = 0.881291, C_X = 0.250225, S(Delta_X rho) = 0.250225
    phi = 0.4: C_Z = 0.881291, C_X = 0.394796, S(Delta_X rho) = 0.394796
    phi = 1.7: C_Z = 0.881291, C_X = 0.989917, S(Delta_X rho) = 0.989917
    phi = 3.0: C_Z = 0.881291, C_X = 0.270591, S(Delta_X rho) = 0.270591
  [ok  ] C_Z is independent of the relative phase
  [ok  ] C_X depends on the relative phase: a record in X spends phase information
  promotion under a full CNOT: joint coherence in the product Z basis
    joint C before = 0.881291, after = 0.881291; system entropy after = 0.881291; H(p) = 0.881291
  [ok  ] the joint coherence H(p) is unchanged by the copy: promoted, not destroyed
  [ok  ] the system's entropy after the copy is H(p): the budget has become record entropy

========================================================================
C  Wei--Liu form: complex overlap, real part spends the coherence
========================================================================
  per-fragment real cost gamma = -ln cos(theta/2) = 0.615626 nat
    fragment phase 0.0: C_Z(N) = [0.8813 0.1975 0.0555 0.016  0.0047 0.0014 0.0004]
    fragment phase 0.9: C_Z(N) = [0.8813 0.1975 0.0555 0.016  0.0047 0.0014 0.0004]
  [ok  ] C_Z depends on |lambda|^N = e^{-N gamma} only: the imaginary cost is not spent
  [ok  ] C_Z falls monotonically with the real cost accumulated

========================================================================
D  Darwinism at N = 8: the budget and the two halves of I(S:F_N)
========================================================================
  S(rho_S) = 0.881257, C_Z(rho_S) = 0.000034, sum = 0.881291, H(p) = 0.881291
  I(S:F_N) = 1.762514 = 2 S(rho_S): classical half 0.881257 (the plateau), quantum half 0.881257 (the rise at k = N)
  [ok  ] N = 8 fragments: S(rho_S) + C_Z(rho_S) = H(p)
  [ok  ] I(S:F_N) = 2 S(rho_S) for the pure global state

========================================================================
COHERENCE BUDGET COMPLEX COUNT: PASS
```
