# Can a hypodox carry a probability greater than one? Kirkwood--Dirac between the pre-FANOUT state and the record

Fable session, 2026-10-16T2200. Script
`scripts/hypodox_probability_above_one_2026-10-16T2200.py` (PASS, stdout in
section 14). Bibliography batch
`bib/kirkwood_dirac_weak_value_refs_2026-10-16T2210.bib`. Sixth note of the
October self-reference thread; the previous five are listed in the memory
file `october-2026-self-reference-logic-thread`.

JS's question: "A probability greater than 1 of an event happening can be
read as a negative probability of an event not happening. We've already
discovered that for probability to be consistent with Shannon Information
Theory we have to step into the complex plane. In the context of paradox
and hypodox, logical paradoxes can be assigned complex truth value, can we
assign a probability greater than 1 for a hypodox?"

Convention throughout: one qubit, record basis Z, "true" is |0>, a sentence
is an endomap of the value (the 10-16T1100 note), the hypodox is the
identity, the Liar is X. Kirkwood--Dirac is written KD.

## 0. The answer in five lines

1. Yes, and the number already has a name and a literature: it is the
   Kirkwood--Dirac conditional quasi-probability of the hypodox's value,
   taken between the agent's pre-FANOUT state and the record outcome that
   closes the apparent loop. It is complex, its two values sum to one, and
   when the record is the Liar's (the complementary basis) it is the
   amplitude normalised in l^1 rather than l^2: q(a) = psi_a/(psi_0+psi_1).
   STRUCTURAL in its mathematics (Kirkwood 1933, Dirac 1945, Aharonov,
   Bergmann and Lebowitz 1964), ESTABLISHED on C^2 by the script.
2. The value exceeds one, with a negative complement, exactly when the
   pre-FANOUT amplitudes carry opposite signs with the "true" amplitude the
   larger; it grows without bound as the boundary pair approaches the
   Liar's; and by Pusey's theorem a value outside [0,1] is a proof of
   contextuality, the same resource the paper already prices as negativity.
   So the "probability greater than one" of a hypodox is not a new thing
   beside negative probability: it is the same anomaly read on the other
   value, and the complement rule JS states is a theorem of this structure.
3. It is not a property of the hypodox alone. A hypodox read in its own
   basis has value 0 or 1; a loop closed on itself (the trace) has a
   quasi-probability with real part exactly 1/2 for every one-qubit loop;
   the hypodox's loop *count* is 2, which is the number of its fixed points
   and not a probability. The anomaly needs the two boundaries, the
   pre-FANOUT state and a complementary record, which is the "apparent
   CTC" of the 10-16T0900 note.
4. The complex truth value of the paradox (Spencer-Brown's imaginary value,
   Kauffman's i = -1/i) is, on the Bloch sphere, the Y-eigenstate: a
   quarter-turn phase on the Liar's state, Z-probability 1/2, no Wigner
   negativity, KD entries (1 +- i)/4. It is the phase phi of the
   pre-FANOUT state, and phi is the dial that takes the hypodox's KD value
   from ordinary (phi = 0) through complex (phi = pi/2, where
   q = p - i sqrt(p(1-p)), real part the Born probability, imaginary part
   the coherence) to anomalous (phi = pi, q > 1). The paradox's complex
   value and the hypodox's value above one are one object at two phases.
5. The step into the complex plane is asymmetric. An event with
   probability above one has real, negative information; only its
   complement, with negative probability, has complex information, the
   anti-event's i pi of the 09-16 note. The budget identity behind the
   anomaly is sum_a |q(a)|^2 = P(record | FANOUT fired in the sentence's
   basis) / P(record | no FANOUT): a modulus above one means the record
   outcome was likelier with an intermediate record than without, which is
   destructive interference across the sentence's two values, and the Liar
   is the pole of that ratio.

## 1. Where JS's three premises come from in the corpus

(a) "Consistent with Shannon forces the complex plane." The paper,
`sec:complex-amplitudes` (`paper1/what_is_a_quantum_state.tex`):

> we have to plug a negative value into the log function. But that can
> only work if we use analytic continuation to extend the domain of the log
> function the complex plane and that is why quantum probabilities require
> complex values.

and `sec:complex-amplitudes-2` (`paper1/self_reference_section_2026-07-04.tex`):

> A signed information measure must extend Shannon's S = -ln p off the
> positive axis, and the analytic continuation of the logarithm carries p
> into the complex plane: amplitudes, with the phase as the continued
> information.

The same section already holds the demarcation this note sharpens:

> every negativity in the tradition lives in intermediate, unrecorded
> quantities and never in a final record.

and cites the Kirkwood--Dirac review (`arvidssonshukur2024kirkwood`) for
"complex quasiprobability from 1933 to the present". The September note
(`complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`, the anti-event
identity) gives the surprisal of a negative entry as -log|p| - i pi.

(b) "Paradoxes can be assigned complex truth value." The paper quotes
Spencer-Brown's report of Russell's approval (`Spence-Brown-1969`, p. ix)
and, since the 10-10 patch, Kauffman and Collings's BF calculus "with a
square root of negation" (`kauffmancollings2019bf`). The May theorem draft
(`fanout_logic_measure_correspondence_theorem_v2_2026-05-17.md`, sections
8.3--8.4) already reads the Spencer-Brown imaginary value as "the phase of
<i|rho|j> itself". The lineage behind Spencer-Brown's chapter 11 is
Varela's calculus for self-reference (1975), Kauffman and Varela's "Form
dynamics" (1980), Kauffman's "Self-reference and recursive forms" (1987,
where the Liar J = not J becomes J = -1/J with solution i) and
Hellerstein's *Diamond* (1997, two paradox values). All VERIFY-SUPPORT
beyond the Kauffman--Collings paper; see the batch.

(c) "Probability greater than one as negative probability of the
complement." Not in the paper. The framework's negative probabilities so
far are Wigner (sec:contextuality), the anti-event (09-16) and the signed
count of the 10-16T1030 note; nothing in the corpus has yet named a
quantity above one. The 10-16T1100 note found that the Liar's states have
a real non-negative KD distribution over (Z, X), which is the starting
point here.

## 2. The complement rule and the two surprisals (script A)

With P(A) + P(not A) = 1 kept, P(A) > 1 is the same statement as
P(not A) < 0. The information is not symmetric. On the principal branch of
the logarithm:

| P(A)  | I(A) = -ln P(A) | P(not A) | I(not A)           |
|-------|-----------------|----------|--------------------|
| 1.5   | -0.4055         | -0.5     | +0.6931 - i pi     |
| 2.0   | -0.6931         | -1.0     | 0 - i pi           |
| 2.895 | -1.0630         | -1.895   | -0.6392 - i pi     |

The over-probable event has real, negative information: knowing it happened
would remove more than no uncertainty. Its complement enters the complex
plane with the imaginary part i pi of the September note (the branch sign
is a convention; the September note writes +i pi). So "stepping into the
complex plane" is the complement's step, and JS's chain runs: probability
above one on one value, negative probability on the other, complex
information on the other only. ESTABLISHED (arithmetic).

## 3. The three Liars and the complex truth value (script B)

Write a pure state as |0> + x|1> with x = beta/alpha the amplitude ratio,
the stereographic coordinate on the Bloch sphere. The Boolean negation
v -> 1 - v, written on ratios, is x -> 1/x; its Moebius matrix is X. Its
fixed points are x = +-1, the states |+->: the Liar of the 10-16T1100 note.
Kauffman's arithmetic for the Liar, J = -1/J, is the Moebius map
x -> -1/x, whose matrix is -iY; its fixed points are x = +-i, the states
|+-i> = S|+->, a quarter-turn phase on the Liar's state. Deutsch's
sqrt(NOT) = (1+i)/2 I + (1-i)/2 X squares to X and has the *same* fixed
rays as X; so the "square root of negation" as an operator fixes the Liar's
states, and the "square root of minus one" as a value names Y's. The
hypodox x -> x fixes everything.

All four Liar states have Z-probability 1/2 (the Kleene gap), Bloch vectors
on the equator, and no Wigner negativity in any of the eight Wootters
conventions: they are stabiliser states, inside Spekkens's octahedron, as
the 10-16T1100 note found for |+->. Their KD(Z,X) distributions differ:
|+> has entries 1/2 and 0, real and non-negative; |+i> has entries
(1 +- i)/4, complex with non-negative real part, summing to one. The
complex truth value is therefore exactly what the 10-16T1030 note called
the promoted phase: visible in the KD distribution's imaginary part,
invisible to the Z-record (C_Z is phase-blind), and not a negativity. A
complex KD entry with non-negative real part is not by itself a
nonclassicality witness (Arvidsson-Shukur, Drori and Yunger Halpern 2021,
"conditions tighter than noncommutation", VERIFY-SUPPORT); the toy theory
holds |+i> as an ordinary epistemic state.

Negating the sentence conjugates its endomap by X: X I X = I and X X X = X
(and X Y X = -Y, the same ray map). The complement of a hypodox is a
hypodox and the complement of a Liar is a Liar. So JS's complement rule
does not pair the paradox with the hypodox; it pairs the two values of one
sentence under one pair of boundary conditions. The paradox/hypodox duality
is the duality I versus X of the loop map, and the count realises it
(section 4).

## 4. The loop count and the loop quasi-probability (script C)

For a sentence closed on itself as a trace (the pre-FANOUT loop of the
10-16T0900 note; Lloyd's P-CTC; Hawking's imaginary-temperature count of
the 10-16T1030 note):

| loop            | Tr L   | Z-weights <a|L|a> | X-weights   | P-CTC success |Tr L|^2/4 |
|-----------------|--------|-------------------|-------------|---------------------------|
| hypodox I       | 2      | 1, 1              | 1, 1        | 1                         |
| Liar X          | 0      | 0, 0              | +1, -1      | 0                         |
| Kauffman Y      | 0      | 0, 0              | 0, 0        | 0                         |
| sqrt(NOT)       | 1 + i  | (1+i)/2 each      | 1, i        | 1/2                       |
| anti-hypodox -I | -2     | -1, -1            | -1, -1      | 1                         |

The hypodox counts 2, both its fixed points; the Liar counts 0, and read in
its own fixed basis the zero is a signed pair +1, -1; the identity with the
spinor sign counts -2 (Hawking's Z < 0, the 10-16T1030 note's Im S = pi);
the graded loop counts 2 cos(theta/2). The count is where "2 for the
hypodox" lives, but it is a count of consistent values, not a probability:
normalised as the P-CTC success probability it is 1 for the hypodox, 0 for
the Liar and 1 again for the anti-hypodox, the sign being a global phase.

The normalised loop quasi-probability q(a) = <a|L|a>/Tr L of the value a
on a loop carrying a rotation by theta about n is, for every axis and angle
(200 random checks, residual 9e-16),

    q(0) = 1/2 - (i/2) n_z tan(theta/2),

real part exactly 1/2, imaginary part set by the loop's Z-component,
diverging at theta = pi (the Liar, Tr L = 0, the Fisher zero). A loop
closed on itself therefore never carries a real part above one. The
anomaly needs two distinct boundaries.

## 5. The sentence's value between the pre-FANOUT state and the record (script D)

Let the agent's pre-FANOUT state be |i> and let the record that closes the
apparent loop read f. The quasi-probability that the sentence's value in
between was a is the KD conditional (Kirkwood 1933; Dirac 1945; Aharonov,
Bergmann and Lebowitz 1964; Steinberg 1995; the weak value of the
projector |a><a|, Aharonov, Albert and Vaidman 1988):

    q(a | i, f) = <f|a><a|i> / <f|i>.

Checked on random boundaries: the two values sum to one (residual 9e-16),
and averaging over the record outcomes with their Born weights returns the
Born probability of a (6e-16). Three cases:

*Own basis.* If the record is in the sentence's basis, f in {|0>, |1>},
then q(a|i,f) = delta_{af}: 0 or 1. A hypodox read by its own record is
never anomalous.

*The Liar's basis.* If the record reads |+>, then
q(a) = psi_a/(psi_0 + psi_1): the amplitude normalised by the sum of
amplitudes, l^1 in place of l^2. This is the weak value Lundeen et al.
measure to read a wavefunction directly (2011, VERIFY-SUPPORT for the
exact form), and it is the plainest statement of "the step into the
complex plane": the quasi-probability *is* the amplitude. For
|i> = sqrt p |0> + sqrt(1-p) e^{i phi} |1>, p = 0.7:

| phi    | q(true)           | q(false)          | |q(true)|^2 | status        |
|--------|-------------------|-------------------|-------------|---------------|
| 0      | +0.6044           | +0.3956           | 0.365       | inside [0,1]  |
| pi/4   | +0.6214 - 0.1966i | +0.3786 + 0.1966i | 0.425       | complex       |
| pi/2   | +0.7000 - 0.4583i | +0.3000 + 0.4583i | 0.700       | complex       |
| 3pi/4  | +1.0683 - 0.9208i | -0.0683 + 0.9208i | 1.989       | complex, >1   |
| pi     | +2.8956           | -1.8956           | 8.385       | real, >1, <0  |

At phi = pi/2, Kauffman's phase, q(true) = p - i sqrt(p(1-p)) exactly:
real part the Born probability, imaginary part the coherence |rho_01|, and
|q(true)|^2 = p. At phi = pi, q(true) = sqrt p/(sqrt p - sqrt(1-p)) > 1
and q(false) < 0, summing to one. This is JS's first sentence as a
theorem: the probability above one of "true" and the negative probability
of "false" are one configuration, not two.

*The pole.* As p -> 1/2 at phi = pi the pre-FANOUT state tends to |-> and
the record is |+>: the boundary pair of the Liar (post-select on NOT of
the pre-selection). q(true) = 5.4, 50.5, 500.5, 5000.5 at
p = 1/2 + 0.1, 0.01, 0.001, 0.0001, asymptotically 1/(2 d). The hypodox's
value above one measures its distance to the Liar; at the Liar it is
undefined, which is the Fisher zero of section 4 seen from the open side.

*The classic.* The three-box configuration of Aharonov and Vaidman (1991):
|i> = (|A>+|B>+|C>)/sqrt3, <f| = (<A|+<B|-<C|)/sqrt3 gives q(A) = 1,
q(B) = 1, q(C) = -1, so "A or B" has quasi-probability 2 and its complement
-1. This is the textbook instance of JS's complement rule.

*Pusey.* A weak value of a projector outside [0,1] is a proof of
contextuality (Pusey 2014; Kunjwal, Lostaglio and Pusey 2019 extend the
result to noise and to imaginary parts; abstracts only, VERIFY-SUPPORT).
Contextuality is what the paper prices as negativity (Spekkens 2008,
`sec:contextuality`). So the hypodox's probability above one is the same
resource as the paradox's negative probability, and the paper's
"self-referential paradox <=> negative probability" sentences, which the
10-16T1100 note found to use the one sentence that does not pay, have a
candidate replacement in section 9.

## 6. The FANOUT identity behind the anomaly (script D, last block)

Since |q(a|i,f)|^2 = |<f|a>|^2 |<a|i>|^2 / |<f|i>|^2,

    sum_a |q(a | i, f)|^2 = P(f | a FANOUT in the sentence's basis fired between i and f)
                            / P(f | no FANOUT fired),

checked on 100 random boundary pairs (residual 3e-13), and equal to 3 for
the three-box (1/3 over 1/9). The numerator is the decohered probability,
the denominator the coherent one. A modulus above one forces the ratio
above one: the record outcome was *likelier* with an intermediate record
than without, which is destructive interference across the sentence's two
values. The Liar's boundary pair is the ratio's pole: an outcome reachable
through a record and unreachable without one. (The converse fails: two
complex values of modulus below one can still have squared moduli summing
above one.) This is the anomaly stated in the framework's own primitive:
a hypodox carries a value above one exactly when the agent's record would
have been more probable had the hypodox been recorded on the way.

## 7. Surprisals of the anomalous values (script E)

At phi = pi, I(true) = -ln 2.8956 = -1.0632, real and negative; I(false)
= -ln(-1.8956) = -0.6396 - i pi. Only the complement is complex. At
phi = pi/2, I(true) = -ln(p - i sqrt(p(1-p))) = -(1/2) ln p + i arctan
sqrt((1-p)/p): the real part is half the Born surprisal, that is the
surprisal of the amplitude's modulus, and the imaginary part is the angle
of the amplitude against the sum of amplitudes. The quantity
-sum_a q ln q is printed for three phases (0.671, 1.025 + 0.303i,
-1.866 + 5.955i against H(p) = 0.611 nat) and no identity is claimed for
it; it is not an entropy and the printout is a record, not a result.

## 8. What I think

JS's sentence is right in its parts and the parts are already joined by
the Kirkwood--Dirac distribution, which the paper cites but has not yet
used. The right reading of "probability greater than one for a hypodox" is
the KD conditional of the hypodox's value between the pre-FANOUT state
and a complementary record; it is the amplitude normalised in l^1; it is
complex in general, above one with a negative complement at phase pi, and
it diverges at the Liar. Three things to hold on to:

- The anomaly is not the hypodox's. The hypodox contributes nothing (its
  endomap is the identity); the anomaly is entirely in the pair of
  boundaries the agent imposes, the pre-FANOUT state and the record it
  closes the loop with. That is the 10-16T0900 note's "apparent CTC" made
  quantitative: the agent's loop is a pre- and post-selected interval, and
  the two-state-vector formalism is the right language for it.
- The complement rule does not pair paradox with hypodox. The negation of
  a hypodox is a hypodox. What the complement rule pairs is the two values
  of one reading; the paradox/hypodox pairing is the loop map's, I against
  X, and it lives in the count (2 against 0) and in the pole (the Liar is
  where the hypodox's value becomes infinite).
- The complex truth value of the paradox is the phase, and the phase is
  the dial of the anomaly. This is yesterday's correction (phase promoted,
  coherence spent) again from the other side: Jozsa (2007) and Dressel and
  Jordan (2012) show that the imaginary part of a weak value shifts the
  pointer's conjugate variable, not its reading (VERIFY-SUPPORT), which is
  the literature's form of "the imaginary part is promoted, not recorded".

What this does not give: a probability above one *recorded*. The paper's
sentence that negativity "never [lives] in a final record" is confirmed and
sharpened: a record in the sentence's own basis reads 0 or 1; the value
above one is a conditional on two records in complementary bases, and is
read off only through a third, weak, record (Aharonov, Albert and
Vaidman's pointer). Nothing here moves the Born rule.

## 9. Second-order findings for JS's ruling

(a) `sec:self-reference` and `sec:contextuality` ("self-referential
paradox <=> negative probability", both sentences flagged in the
10-16T1100 note). A replacement consistent with the Liar's non-negativity
and with this note: "a self-referential sentence read through a
complementary record has an anomalous quasi-probability, negative on one
value and above one on the other, and by Pusey's theorem that anomaly is
contextuality". Citation keys: pusey2014anomalousweakvalues,
kunjwallostagliopusey2019anomalous, with arvidssonshukur2024kirkwood
already in the library. CANDIDATE wording; JS to rule.

(b) `sec:complex-amplitudes-2`, "amplitudes, with the phase as the
continued information". The continued information of a negative entry is
-ln|p| - i pi, a fixed i pi, not a free phase (section 2 and the 09-16
note); the free phase enters as the KD imaginary part, which the Jozsa and
Dressel--Jordan results place in the conjugate pointer. The sentence is
not wrong but it conflates the two, as the 10-16T1030 note found the
September notes doing. Proposed: "amplitudes, the modulus carrying the
continued information and the phase the promoted part". CANDIDATE.

(c) `sec:complex-amplitudes-2`, "never in a final record". Confirmed by
script D's own-basis check and sharpened: the anomalous value is a
conditional on two records in complementary bases. No change needed; a
footnote citing the three-box would make the sentence checkable.

(d) For the Khrennikov email on the todo list: p-adic probability theory
(Khrennikov 1993, 2009) is the one existing calculus in which frequencies
converge to probabilities outside [0,1], negative rationals and "2"
included, because the p-adic norm does not order them. A probability
greater than one is ordinary there. RHYME only, but it is a sentence
Khrennikov would recognise, and it connects this thread to the adelic open
problem.

## 10. Prior work and ownership

The KD distribution and its conditional form are Kirkwood's (1933) and
Dirac's (1945); the two-boundary reading is Aharonov, Bergmann and
Lebowitz (1964); anomalous values are Aharonov, Albert and Vaidman (1988)
and the three-box is Aharonov and Vaidman (1991); conditional
quasi-probabilities as such are Steinberg (1995); the complex phases are
Jozsa (2007), Hofmann (2011) and Dressel and Jordan (2012); the
contextuality theorem is Pusey (2014) with Kunjwal, Lostaglio and Pusey
(2019); the l^1 form is Lundeen et al. (2011); the resource reading is the
2024 review already in the library and Lostaglio et al. (2023). The
complex truth value lineage is Spencer-Brown (1969), Varela (1975),
Kauffman and Varela (1980), Kauffman (1987), Hellerstein (1997) and
Kauffman and Collings (2019). The framework's own contributions here are
the identifications: the agent's apparent CTC as a two-boundary interval;
the Moebius reading of the three Liars; the FANOUT identity of section 6;
the Liar as the pole of the hypodox's value; and the phase as the common
dial of the paradox's complex value and the hypodox's value above one.
None of the mathematics is new.

## 11. Fences

- One qubit throughout. The l^1 form q(a) = psi_a/(sum psi) holds for a
  record reading the uniform superposition in any dimension; the
  three-box is the d = 3 instance.
- "Anomalous implies contextual" is Pusey's theorem under its conditions
  (sufficiently weak measurement; perfect correlations in the original,
  relaxed in 2019). I have read neither paper today; abstract-level.
- The surprisal branch: -i pi here, +i pi in the September note; a
  convention, recorded in script A.
- The count of section 4 is a trace, dimension-dependent, and is not a
  probability; the note keeps "2" for the hypodox as a count.
- The quantity -sum q ln q of section 7 is printed, not interpreted.
- No claim about a recorded probability above one; none exists.

## 12. Proposed ledger entries (for JS to write or refuse)

- **STRUCTURAL** The Kirkwood--Dirac conditional q(a|i,f) =
  <f|a><a|i>/<f|i> of a value between a preparation and a post-selection
  sums to one over a, returns the Born probability of a when averaged over
  the post-selection outcomes with their Born weights, equals the weak value
  of the projector |a><a|, and lies outside [0,1] only in configurations
  that are contextual (Pusey 2014). Imported; verified numerically on C^2
  (sums and marginals to 1e-15).
- **ESTABLISHED** (finite check, script PASS) On C^2 with record basis Z:
  a record in the sentence's own basis gives q in {0, 1}; a record reading
  |+> gives q(a) = psi_a/(psi_0+psi_1); for sqrt p |0> + sqrt(1-p) e^{i phi}
  |1> this is p - i sqrt(p(1-p)) at phi = pi/2 and
  sqrt p/(sqrt p - sqrt(1-p)) at phi = pi, above one with negative
  complement for p > 1/2 and divergent as p -> 1/2 where the boundary pair
  is the Liar's; the loop quasi-probability <0|L|0>/Tr L of a rotation
  about n by theta is 1/2 - (i/2) n_z tan(theta/2); and
  sum_a |q(a|i,f)|^2 equals the probability of f with a FANOUT in the
  a-basis between i and f divided by the probability without.
- **CANDIDATE** The agent's apparent closed loop (10-16T0900) is a
  two-boundary interval, pre-FANOUT state and record, and the
  quasi-probability of a self-referential sentence's value inside it is the
  Kirkwood--Dirac conditional; "a probability greater than one for a
  hypodox" is that conditional read through a complementary record, it is
  the same contextual anomaly as a negative probability on the other value,
  and it measures the hypodox's distance to the Liar.
- **CANDIDATE** The complex truth value of the Liar (Spencer-Brown,
  Kauffman) is the Y-eigenstate, a phase on the Liar's state; the phase of
  the pre-FANOUT state is the dial that carries the hypodox's conditional
  from ordinary through complex to anomalous. The paradox's complex value
  and the hypodox's value above one are one object at two phases.
- **RHYME** The sign-flipped identity loop, count -2, is the hypodox with
  a spinor sign: a "negative-probability hypodox" indistinguishable from
  the hypodox by any single reading. p-adic probabilities (Khrennikov) are
  the one calculus where "2" is an ordinary probability.

## 13. Files

- `scripts/hypodox_probability_above_one_2026-10-16T2200.py` -- new, PASS,
  0 FAIL.
- `knowledge/sessions/hypodox_probability_above_one_2026-10-16T2200.md`
  -- this note.
- `bib/kirkwood_dirac_weak_value_refs_2026-10-16T2210.bib` -- 20 keys,
  18 Crossref-verified, bodies VERIFY-SUPPORT; header records the claim
  each supports.
- `notes/todo.md` -- pointer appended.
- Nothing patched, built or committed. The sentences of section 9 are
  proposals.

## 14. Exact stdout of the script (2026-10-16)

```
A. the complement rule and the two surprisals
   P(A) = 1.500  I(A) = -0.4055-0.0000i ;  P(not A) = -0.500  I(not A) = +0.6931-3.1416i
   ok   an event with P > 1 has real, negative information
   ok   its complement has complex information, imaginary part -i pi, and exp(-I) recovers 1 - P
   P(A) = 2.000  I(A) = -0.6931-0.0000i ;  P(not A) = -1.000  I(not A) = -0.0000-3.1416i
   ok   an event with P > 1 has real, negative information
   ok   its complement has complex information, imaginary part -i pi, and exp(-I) recovers 1 - P
   P(A) = 2.895  I(A) = -1.0630-0.0000i ;  P(not A) = -1.895  I(not A) = -0.6392-3.1416i
   ok   an event with P > 1 has real, negative information
   ok   its complement has complex information, imaginary part -i pi, and exp(-I) recovers 1 - P
   ok   the anti-event of weight -1 has surprisal -i pi on this branch (the 09-16 note's i pi up to the branch sign)
B. three Liars and the hypodox as Moebius maps of the amplitude ratio x = beta/alpha
   ok   x -> 1/x is the Liar endomap X
   ok   Kauffman's x -> -1/x is Y up to the phase -i
   x = +1 -> state [0.7071+0.j 0.7071+0.j], Bloch [1. 0. 0.], Z-probabilities [0.5 0.5], Wigner min 0.0000
   ok   the Moebius fixed point names the expected stabiliser state
   ok   its Z-probability is 1/2 (the Kleene gap)
   ok   no Wigner negativity in any convention
   x = -1 -> state [ 0.7071+0.j -0.7071+0.j], Bloch [-1.  0.  0.], Z-probabilities [0.5 0.5], Wigner min 0.0000
   ok   the Moebius fixed point names the expected stabiliser state
   ok   its Z-probability is 1/2 (the Kleene gap)
   ok   no Wigner negativity in any convention
   x = +i -> state [0.7071+0.j     0.    +0.7071j], Bloch [0. 1. 0.], Z-probabilities [0.5 0.5], Wigner min 0.0000
   ok   the Moebius fixed point names the expected stabiliser state
   ok   its Z-probability is 1/2 (the Kleene gap)
   ok   no Wigner negativity in any convention
   x = -i -> state [0.7071+0.j     0.    -0.7071j], Bloch [ 0. -1.  0.], Z-probabilities [0.5 0.5], Wigner min 0.0000
   ok   the Moebius fixed point names the expected stabiliser state
   ok   its Z-probability is 1/2 (the Kleene gap)
   ok   no Wigner negativity in any convention
   ok   x = +-1 are the fixed rays of X (the Liar)
   ok   x = +-i are the fixed rays of Y (Kauffman's Liar)
   ok   sqrt(NOT) = (1+i)/2 I + (1-i)/2 X squares to NOT
   ok   sqrt(NOT) has the Liar's fixed rays |+->; Kauffman's i is not its fixed point but Y's
   ok   |+i> = S|+>: the complex truth value is a quarter-turn phase on the Liar's state
   KD(Z,X) of |+> (the Liar's state):
 [[ 0.5+0.j  0. +0.j]
 [ 0.5+0.j -0. +0.j]]
   KD(Z,X) of |+i> (Kauffman's state):
 [[0.25-0.25j 0.25+0.25j]
 [0.25+0.25j 0.25-0.25j]]
   ok   the Liar's state has a real, non-negative KD(Z,X)
   ok   Kauffman's state has KD(Z,X) entries (1 +- i)/4: complex, real part non-negative, summing to one
   ok   negating the sentence conjugates its endomap by X: the hypodox stays a hypodox, each Liar stays a Liar
C. the loop count and the loop quasi-probability
   hypodox  I       Tr L = (2+0j) ; Z-weights [1. 1.] ; X-weights [1. 1.] ; P-CTC success |Tr L|^2/4 = 1.000
   Liar     X       Tr L = 0j ; Z-weights [0. 0.] ; X-weights [ 1. -1.] ; P-CTC success |Tr L|^2/4 = 0.000
   Kauffman Y       Tr L = 0j ; Z-weights [0. 0.] ; X-weights [0. 0.] ; P-CTC success |Tr L|^2/4 = 0.000
   sqrt(NOT)        Tr L = (1+1j) ; Z-weights [0.5+0.5j 0.5+0.5j] ; X-weights [1.+0.j 0.+1.j] ; P-CTC success |Tr L|^2/4 = 0.500
   anti-hypodox -I  Tr L = (-2+0j) ; Z-weights [-1. -1.] ; X-weights [-1. -1.] ; P-CTC success |Tr L|^2/4 = 1.000
   ok   counts: hypodox 2, Liar 0, sign-flipped hypodox -2
   ok   the Liar's zero count is +1 on |+> and -1 on |->: a signed pair that cancels
   ok   the half-Liar's count is 1 + i, modulus sqrt 2
   ok   graded count 2 cos(theta/2) at theta = 0.000 : +2.0000
   ok   graded count 2 cos(theta/2) at theta = 1.000 : +1.7552
   ok   graded count 2 cos(theta/2) at theta = 2.000 : +1.0806
   ok   graded count 2 cos(theta/2) at theta = 3.142 : +0.0000
   ok   graded count 2 cos(theta/2) at theta = 6.283 : -2.0000
   ok   for a rotation about n the loop quasi-probability of |0> is 1/2 - (i/2) n_z tan(theta/2): real part exactly 1/2 (worst residual 8.9e-16)
   the loop quasi-probability has a pole at theta = pi (the Liar, Tr L = 0) and real part 1/2 everywhere else
D. the sentence's value between the pre-FANOUT state and the record: Kirkwood--Dirac
   ok   q(0|i,f) + q(1|i,f) = 1 for random boundaries (worst 8.9e-16)
   ok   averaging q over the record outcomes with their Born weights returns the Born probability of a (worst 5.7e-16)
   ok   a record in the sentence's own basis gives q = 0 or 1: a hypodox read in its own basis is never anomalous
   ok   a record reading |+> gives q(a) = psi_a / (psi_0 + psi_1): the amplitude normalised in l^1, not l^2
   p = 0.70 ; the record reads |+> ; q(true) and q(false) against the Kauffman phase phi:
      phi = 0.0000 : q(true) = +0.6044+0.0000i  q(false) = +0.3956+0.0000i  |q(true)|^2 = 0.3652  inside [0,1]
      phi = 0.7854 : q(true) = +0.6214-0.1966i  q(false) = +0.3786+0.1966i  |q(true)|^2 = 0.4247  outside [0,1]
      phi = 1.5708 : q(true) = +0.7000-0.4583i  q(false) = +0.3000+0.4583i  |q(true)|^2 = 0.7000  outside [0,1]
      phi = 2.3562 : q(true) = +1.0683-0.9208i  q(false) = -0.0683+0.9208i  |q(true)|^2 = 1.9891  outside [0,1]
      phi = 3.1416 : q(true) = +2.8956-0.0000i  q(false) = -1.8956+0.0000i  |q(true)|^2 = 8.3848  outside [0,1]
   ok   phi = 0: ordinary, inside [0,1]
   ok   phi = pi/2 (Kauffman's i): q(true) = p - i sqrt(p(1-p)): real part the Born probability, imaginary part the coherence
   ok   phi = pi/2: |q(true)|^2 = p, the modulus of the quasi-probability is the modulus of the amplitude
   ok   phi = pi: q(true) = 2.8956 > 1 and q(false) = -1.8956 < 0, summing to one: the probability above one and the negative complement are one configuration
   ok   phi = pi: q(true) = sqrt p / (sqrt p - sqrt(1-p))
   approach to the Liar's boundary pair (phi = pi, p -> 1/2 from above; <f| = <+|, |i> -> |->):
      p = 1/2 + 0.1     : q(true) =      5.449   1/(2 d) =      5.000   |<+|i>|^2 = 1.01e-02
      p = 1/2 + 0.01    : q(true) =     50.495   1/(2 d) =     50.000   |<+|i>|^2 = 1.00e-04
      p = 1/2 + 0.001   : q(true) =    500.499   1/(2 d) =    500.000   |<+|i>|^2 = 1.00e-06
      p = 1/2 + 0.0001  : q(true) =   5000.500   1/(2 d) =   5000.000   |<+|i>|^2 = 1.00e-08
   ok   at p = 1/2 the pre-FANOUT state is |-> and the record |+>: the pole is the Liar's boundary pair, <+|X|+> read as <+|->
   ok   the value exceeds one without bound as the boundary pair approaches the Liar's
   three-box (Aharonov--Vaidman): q(A) = +1.000  q(B) = +1.000  q(C) = -1.000  q(A or B) = +2.000
   ok   three-box: 1, 1, -1 ; the event 'A or B' has quasi-probability 2 and its complement -1
   ok   sum_a |q(a|i,f)|^2 = P(f | FANOUT fired in the sentence's basis) / P(f | no FANOUT) (worst 2.8e-13)
   ok   three-box: the ratio is 3 = (1/3) / (1/9): the post-selected outcome is three times likelier with a record in the box basis than without
   a modulus above one forces the ratio above one: the record outcome is likelier with an intermediate FANOUT than without, destructive interference across the sentence's values; the Liar is the ratio's pole
E. surprisals of the anomalous values
   phi = pi : I(true) = -1.0632+0.0000i   I(false) = -0.6396-3.1416i
   ok   the value with q > 1 has real negative information
   ok   its complement with q < 0 carries the i pi
   phi = pi/2: I(true) = +0.1783+0.5796i ; half the Born surprisal -ln(p)/2 = +0.1783 ; arctan(sqrt((1-p)/p)) = +0.5796
   ok   at the Kauffman phase the real part of the surprisal is half the Born surprisal, -ln|psi_true|
   ok   and the imaginary part is the angle of the amplitude against the sum of amplitudes
   phi = 0.0000 : -sum q ln q = +0.6712-0.0000i  (Born H(p) = 0.6109 nat)
   phi = 1.5708 : -sum q ln q = +1.0253+0.3025i  (Born H(p) = 0.6109 nat)
   phi = 3.1416 : -sum q ln q = -1.8663+5.9553i  (Born H(p) = 0.6109 nat)
HYPODOX PROBABILITY ABOVE ONE: PASS
```
