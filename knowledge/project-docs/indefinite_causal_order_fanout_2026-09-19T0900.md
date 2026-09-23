# Indefinite causal order and the FANOUT boundary: order is a record, duration is a phase

Date: 2026-09-19T0900. Written by the Fable session at JS's request to read
two papers on indefinite causal order (ICO) and relate them to the
complex-cost discussion of 2026-09-16 to 18. Companion to
`complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md` and
`two_columns_shannon_thermodynamics_action_2026-09-18T1200.md`. The
computation is `scripts/quantum_switch_graded_fanout_2026-09-19T0900.py`,
exact stdout in section 9. Labels are proposals.

The paper already takes a position on ICO. Paper 1
(`spacetime_from_non-computability.tex`, the "three experimental postures"
paragraph; `predictions_section`, "no experiment will ever hold a record of
indefinite causal order") says laboratory ICO "lives below the locking
threshold and definitises at it" and "can never be amplified into records
while remaining indefinite". Paper 2 makes "no indefinite causal order
survives amplification into records" its "theorem target in that formalism"
and carries a TODO for an Oreshkov--Costa--Brukner paragraph. What follows
is the graded version of that position, its computation in the simplest
case, the vocabulary the two-columns note gives it, and an honest account of
what the two supplied papers do and do not add.

## 0. The answer in brief

The quantum switch superposes two orders of the same two operations. The
count of operations is the same on both branches; only their order differs,
and it differs exactly by the commutator. The switch therefore separates two
things the word "time" runs together: duration, which is the number of
composition steps and accrues as phase, and order, which is a fact about
which step came first. In the framework's terms, duration is imaginary-column
(the Compton clock counts), and order is a record. Before any fragment holds
the control's value, order is a phase relation between two histories; when
fragments hold it, order is a record. Graded FANOUT of the control multiplies
the order-interference by the same overlap product $\Lambda = \prod\lambda_k$
that hides a phase, so the ICO signal falls as $\cos^{R}\phi$ (Part B), is
rotated by the fragments' phases (Part C), and returns exactly when the
fragments are uncomputed (Part D). This is the paper's boundary, "never
amplified into records while remaining indefinite", in its graded form and
with a number attached. Nothing in it is new physics: that the switch needs
a coherent control is known. What is new is only the placement, on the same
ladder as the phase, and one question it raises that the literature can
answer: whether causal nonseparability dies at a finite redundancy or only
asymptotically (section 6).

## 1. The two papers, read

**Qureshi-Hurst and Pearson, "Quantum mechanics, time, and theology:
indefinite causal order and a new approach to salvation", Zygon (2020),
read in full.** A philosophy-of-time paper written by Qureshi-Hurst, with
Anna Pearson (the physicist; the same A. N. Pearson as the timekeeping paper,
on the affiliation) supplying the physics and, by the authors' own note,
"unwilling to commit herself to any particular argument at this stage". Its
physics is second-hand: Goswami et al. 2018 for the photonic switch, with
Oreshkov's 2019 caveat that whether the photonic realisations are ICO or
simulations of it "has remained controversial", and Zych et al. 2019 for the
gravitational case. Its argument: ICO is incompatible with an objective
present (the A-theory) and with fixed ordering relations (the classical
B-theory); what survives is a block universe in which "temporal ordering
relations ... apply only to large-scale classical systems in which quantum
effects do not take force", ordering being "emergent properties that apply
to classical objects and systems, and that do not apply at the quantum
level". The second half is theology and is not the framework's business.
Two things are useful. The conclusion is, in the framework's words, "causal
order is post-FANOUT bookkeeping", reached by a philosopher from the
experiment alone; it is a witness that the position is natural, not a source
for it. And footnote 14 says ICO "has yet to be discussed in an Everettian
setting" and that in a branching universe the conclusion "would not be the
case" as stated: that gap is exactly what graded FANOUT fills, a branching
account of how order becomes definite, and Paper 2 can say so. JS's phrase
"indefinite causal order in the pre-FANOUT regime" is a fair gloss of the
paper's position; the paper does not use those words.

**Filatov and Auzinsh, "Ordering the processes with indefinite causal
order", arXiv:2106.08976v3 (2022), read in full.** Five pages, heuristic by
its own account ("we don't have a rigorous proof"). Claim: by relabelling
the processes in the basis in which the control qubit is measured, an ICO
circuit is described with a definite order, "first $(A+B)/\sqrt2$ then
$(A-B)/\sqrt2$", causal nonseparability being traded for nonlocality of the
processes; hence ICO is not evidence for fundamental unorderability but a
feature of a reference frame. Assessment: the relabelling does not do what is
claimed. Causal nonseparability is a property of the process matrix, that it
is not a convex mixture of definitely ordered processes, and it is invariant
under a change of basis of the control; renaming a superposition of process
vectors "the first process" changes what "process" means, and the paper
concedes the result "is difficult to understand". The framework should not
cite it as support. What survives, and is correct, is weaker: "which came
first" is a question posed in a basis of the control, and until a record has
selected a basis it has no answer. That is the framework's own point about
records being basis-dependent (the every-basis lemma, and the blind-spot
clause of the v2 plan), and it is made better by the graded computation
below than by relabelling. One sentence of theirs is worth keeping: the
processes in a switch "don't involve irreversible processes", which is the
pre-FANOUT condition stated by authors who do not have the word.

## 2. The switch in the framework's terms [STRUCTURAL; the reading CANDIDATE]

Control $(\ket0 + \ket1)/\sqrt2$; control $\ket0$ applies $A$ then $B$ to the
target, giving $BA\ket\psi$; control $\ket1$ applies $B$ then $A$, giving
$AB\ket\psi$. Measuring the control in the $X$ basis leaves the target in
$(BA \pm AB)\ket\psi/2$, so

$$P(-) = \tfrac14\,\|[A,B]\psi\|^{2},\qquad P(+) = \tfrac14\,\|\{A,B\}\psi\|^{2}.$$

Part A: with $A = R_{x}(1.0)$, $B = R_{z}(0.7)$, $\psi = \ket0$,
$P(-) = 0.027025$, equal to the commutator norm to six figures; with two
$\sigma_{z}$ rotations, $P(-) = 0$. Order matters exactly where the
generators fail to commute, and the "$-$" outcome is the anti-event of order:
the history "$A$ then $B$" minus the history "$B$ then $A$". A classical
mixture of the two orders gives $P(\pm) = 1/2$; the indefinite-order signal
is $P(+) - 1/2$, here $0.472975$.

Two readings follow, and they are the point of the section.

*Duration is a phase; order is a record.* Both branches contain exactly two
operations. The operation count, which the framework makes time ("time is
operation count", and the Compton clock of the earlier notes), is definite on
both branches; the order is not. So the switch is the demonstration that
count and order are separable, and the framework's identification of
duration with a phase (the imaginary column) is compatible with ICO because
the phase counts steps and does not order them. Order becomes a fact when a
fragment holds the control's value, that is, at a record. This is the sentence
Paper 2's section on causal order should be organised around.

*The commutator is a holonomy.* To leading order in the generators
$A = e^{X}$, $B = e^{Y}$, $\log(AB) - \log(BA) = [X, Y] + \dots$
(Baker--Campbell--Hausdorff), and $ABA^{-1}B^{-1} = e^{[X,Y] + \dots}$: the
difference between the two orders is the holonomy around the loop that goes
out by one order and back by the other. In the two-columns note, section 6,
the imaginary column at second order is curvature (the Berry part of the
quantum geometric tensor). Indefinite order is the superposition of two
paths around a loop whose holonomy is the commutator; definite order is a
record of which path was taken. RHYME, fenced: the Bargmann invariant
$3\delta$ of the generation triple reverses sign when the cyclic order of
the three states is reversed, so the sign of the Koide phase is the
orientation of the generation loop. Arithmetic on an existing object; no
mechanism; keep out of the paper.

## 3. Graded FANOUT of the control: the computation [STRUCTURAL as computation]

$R$ fragments each copy the control's $Z$ value imperfectly, fragment $k$ in
$\ket{e^{0}_{k}}$ or $\ket{e^{1}_{k}}$ with
$\lambda_{k} = \langle e^{0}_{k}|e^{1}_{k}\rangle = e^{-i\theta_{k}/2}\cos\phi$,
the model of notebook S. Exactly,

$$P(\pm) = \tfrac12\left(1 \pm \mathrm{Re}[\Lambda\, c]\right),\qquad
\Lambda = \prod_{k}\lambda_{k},\qquad c = \langle BA\psi|AB\psi\rangle ,$$

checked against the full state vector to $10^{-12}$ for $R \le 8$ (Part B).
The indefinite-order signal is $\mathrm{Re}[\Lambda c]/2$ and its size falls
as $|\Lambda| = \cos^{R}\phi$: at $\phi = 0.3$ it is $0.473$ at $R = 0$,
$0.228$ at $R = 16$, $0.025$ at $R = 64$, $4\times10^{-6}$ at $R = 256$, and
reaches $1/e$ of its initial value at $R = 22 = \lceil 1/(-\ln\cos\phi)\rceil$.
Random fragment phases leave $|\Lambda|$ unchanged and rotate the signal,
which can change sign (Part C: $P(+) = 0.309$ at $R = 4$, below the mixture
value). Uncomputing the six fragments by applying the inverse of each copy
unitary restores the $R = 0$ signal to $10^{-15}$ (Part D).

What this is. The control's coherence between the two orders is the same
off-diagonal element that carries a phase in the notebook-S model, and the
fragments multiply it by the same $\Lambda$. So "the phase becomes
inaccessible" and "the order becomes definite" are one process with one
number, and the ladder of section 4b of the complex-cost note (rotation
angle $1/\sqrt R$ for the cost; $\cos^{R}\phi$ for the visibility) carries
causal order on the same rungs as the phase. It is the paper's boundary,
"indefinite causal order can never be amplified into records while remaining
indefinite", proved in the simplest case by exhibiting the amplification and
watching the indefiniteness go. What it is not: new. That a decohered control
turns the switch into a mixture of orders is in the first papers on the
switch. The framework's contribution is the placement and the vocabulary, not
the decay law.

*The witness is a record of $\Lambda$, not of the order.* `notes/ideas.md`
already flags Rubino et al. 2017 as the hardest case against "no experiment
will ever hold a record of indefinite causal order": a causal witness was
measured, and that is a record certifying indefiniteness. Part B makes the
paper's answer precise. The witness value is an average over many runs of
the $X$-basis statistics, and it is a function of $\Lambda$: it records that
the order was *not* recorded, run by run, in the apparatus. Two different
records are in play. A record of the order on a single run is a fragment of
the control's $Z$ value, and each such fragment multiplies the witness by
$\lambda_{k}$; a record of nonseparability is the accumulated statistics,
and it exists only to the extent that the first kind does not. The
prediction "no experiment will ever hold a record of indefinite causal
order" is therefore the statement that these two records exclude each other
at the rate $\cos^{R}\phi$, and Rubino's witness is a measurement of
$|\Lambda| \approx 1$, not a counterexample. That is the clause ideas.md
asks for, with a number behind it.

## 4. The thermodynamics of the switch [literature to engage; bibliography verified 2026-09-20, bodies still unread]

There is a literature claiming a thermodynamic advantage from ICO: a switch
of two identical thermalising channels followed by an $X$-basis measurement of
the control leaves the target, on one outcome, colder than the bath (Felce
and Vedral 2020, "Quantum refrigeration with indefinite causal order", Phys.
Rev. Lett. 125, 070603; an experiment by Nie et al. 2022; related work by
Guha, Alimuddin and Parashar 2020 and by Simonov et al. 2022); and a
reassessment arguing that the advantage comes from the control's coherence
and its measurement, obtainable with coherently controlled definite-order
processes as well (Capela, Verma, Costa and Céleri 2023, "Reassessing
thermodynamic advantage from indefinite causal order", Phys. Rev. A 107,
062208). All from memory.

The two-columns accounting takes a side, and should say so before a
reviewer asks. The resource is the control's coherence, an imaginary-column
quantity; cashing it needs an $X$-basis measurement of the control, a record,
whose Landauer cost is real; the "advantage" is a Maxwell-demon transaction
between the columns, and the framework's expectation is the reassessment's:
the order as such is not the resource, the unrecorded coherence is. Part B
adds the graded statement: any advantage disappears with the control's
FANOUT at the rate $\cos^{R}\phi$, because the signal that carries it does.
This makes the switch the cleanest test bed for op:complex-cost: a system
where the imaginary column (control coherence), the record (the $X$
measurement) and the extractable work are all standard, so the exchange rate
between the columns can be checked against Felce--Vedral's numbers once the
Landauer identification of the real column is fixed.

## 5. What this gives Paper 2

- The section on causal order (the "theorem target" and the TODO paragraph)
  gets its organising sentence, "duration is a phase, order is a record", and
  its toy proof, section 3, with the table of Part B as the figure.
- The Oreshkov--Costa--Brukner paragraph can now be written: the process-matrix
  formalism is the pre-FANOUT description of order; Oreshkov's
  time-delocalised subsystems are operations not localised in the count
  before a record localises them, which is what the framework means by "no
  events before FANOUT"; the photonic realisations are sub-threshold ICO,
  as the paper says, and the "simulation or the real thing" controversy is,
  on this reading, the question whether a record of the order exists
  anywhere in the apparatus, answerable case by case by looking for the
  fragment.
- Zych et al.'s gravitational switch (a mass in spatial superposition
  entangling the temporal order of two events) is the case where the
  unrecorded control is the mass's location; the framework's "no superposed
  metric, but the pre-geometric layer is quantum" says the temporal order
  is indefinite exactly until the mass's location is recorded, and the
  same $\Lambda$ governs it. That is a claim Paper 2 can make and the
  Bose--Marletto--Vedral programme can test in principle.
- The Everettian gap the Zygon paper names (footnote 14) is filled by the
  branching description of section 3, and can be cited as an open question
  the framework answers.

## 6. One question worth settling: is the threshold finite? [OPEN, proposed]

The paper says ICO "definitises at" a "locking threshold". For the phase, the
decay is asymptotic: the coherence is $\Lambda$ and never zero at finite $R$.
For causal order the situation may differ, because causal nonseparability is
membership outside a convex set (the causally separable process matrices),
and that set has an interior. The graded switch's process matrix is the
mixture of the two orders plus $\Lambda$ times a coherence term plus its
adjoint, and any causal witness $S$ evaluates on it as an affine function of
$\mathrm{Re}(\Lambda e^{i\alpha})$. If the classical mixture lies in the
interior of the separable set, there is a finite $|\Lambda^{*}| > 0$, hence
a finite $R^{*}$, below which no witness detects nonseparability and the
order is definite for every operational purpose. That would be a threshold in
the paper's sense, the causal analogue of a Werner state becoming separable
at finite noise. If instead the mixture lies on the boundary, nonseparability
persists for every $|\Lambda| > 0$ and the boundary is graded like the phase.

op:ico-threshold, proposed. PASS: the causal-separability threshold
$|\Lambda^{*}|$ of the qubit switch, computed by the causal-witness
semidefinite programme (Araújo, Branciard, Costa, Feix, Giarmatzi and Brukner
2015, "Witnessing causal nonseparability", New J. Phys. 17, 102001, doi
10.1088/1367-2630/17/10/102001, verified 2026-09-20 against Crossref; body
not read, so that the semidefinite programme is theirs and is the right one
for this threshold is still unchecked), is strictly positive, with its value as a function of the
operations $A$, $B$. FAIL: $|\Lambda^{*}| = 0$. Either outcome is
informative: PASS licenses the paper's word "threshold" and gives Paper 2 a
number; FAIL requires "threshold" to be replaced by "graded" wherever ICO is
discussed. Needs cvxpy or an equivalent SDP solver; a task for the
environment the Opus session is setting up. The session's own recollection
is that the switch survives a finite amount of white noise (Araújo et al.),
which bears on but does not settle the coherence-scaling case.

## 7. Fences and pushback

- The two supplied papers are weak anchors. The Zygon paper is philosophy
  and its physics is reported; the Filatov--Auzinsh note is heuristic and its
  central claim does not hold. Cite the first, if at all, for the Everettian
  gap and the "ordering relations are classical-level" conclusion; do not
  cite the second as support for anything.
- Section 3 is textbook decoherence of a control qubit. The label
  STRUCTURAL is for the computation; the placement on the ladder is
  CANDIDATE; "duration is a phase, order is a record" is CANDIDATE and rests
  on "time is operation count", which is the framework's premise.
- The switch does not show that order is "made of" phase. It shows that
  which-order information, like which-path information, is a phase relation
  until recorded. The framework's stronger thesis, that causal structure is
  the bookkeeping of locked relations (Paper 1, sec:no-quantised-gravity),
  is not derived here and the computation should not be quoted as if it were.
- The thermodynamic-advantage literature is from memory and must be read
  before Paper 2 engages it; the reassessment paper in particular, since the
  framework agrees with it and should cite it accurately.
- Whether the photonic switches are ICO or simulations (Oreshkov 2019) is
  not decided by this note; the framework's criterion, "is there a record of
  the order anywhere", is a proposal for how to decide it.

## 8. Proposed ledger entries and references

- **STRUCTURAL** (computation) In the quantum switch with $R$ fragments
  copying the control at overlap $\lambda = \cos\phi$, the $X$-basis
  statistics are $P(\pm) = (1 \pm \mathrm{Re}[\Lambda c])/2$ with
  $\Lambda = \prod\lambda_{k}$; the indefinite-order signal falls as
  $\cos^{R}\phi$, is rotated by fragment phases, and is restored exactly by
  uncomputing the fragments. At $R = 0$, $P(-) = \|[A,B]\psi\|^{2}/4$.
  (`scripts/quantum_switch_graded_fanout_2026-09-19T0900.py`, seed 20260919.)
- **CANDIDATE** Duration is a phase (operation count, imaginary column) and
  order is a record (real column); the switch separates them, and graded
  FANOUT of the control is the paper's "definitisation at the locking
  threshold" in its graded form.
- **CANDIDATE** The thermodynamic resource in switch-based refrigeration is
  the control's unrecorded coherence, cashed by a record; no advantage
  survives the control's FANOUT.
- **OPEN** op:ico-threshold, section 6, with its PASS/FAIL.
- **RHYME** The commutator as the holonomy of the order loop; the sign of
  the Koide phase as the orientation of the generation loop.
- Ledger note for Paper 1's existing wording: "definitises at the locking
  threshold" is asymptotic for the phase and possibly finite for the order;
  op:ico-threshold decides which word survives.

References, verified 2026-09-20 (Opus session) and batched in
`bib/indefinite_causal_order_refs_2026-09-20T2200.bib`. In the library and so
not batched: `procopio2015experimental`, `rubino2017indefinite`. Read for this
note: Qureshi-Hurst and Pearson, Zygon 55(3) (2020), doi 10.1111/zygo.12621 --
the volume and issue are confirmed but **the pages could not be found**, since
Crossref, OpenAlex and Semantic Scholar all record none and both the
publisher's site and Wiley refuse an automated request; and Filatov and
Auzinsh, "Ordering the processes with indefinite causal order",
arXiv:2106.08976, which has no journal_ref and no Crossref record, so it is
batched as `@online`. It is a different paper from the library's
`filatov2024towards` and the two must not be merged on import.

The twelve taken from reference lists or from memory are all verified against
Crossref by DOI and are in the batch: Oreshkov, Costa and Brukner 2012;
Chiribella, D'Ariano, Perinotti and Valiron 2013; Goswami et al. 2018;
Oreshkov 2019; Zych, Costa, Pikovski and Brukner 2019; Hardy 2009; Araújo et
al. 2015; Felce and Vedral 2020; Nie et al. 2022; Guha, Alimuddin and Parashar
2020; Simonov, Francica, Guarnieri and Paternostro 2022; Capela, Verma, Costa
and Céleri 2023. Every volume and article number remembered was right. Two
corrections worth naming. Hardy 2009 is a **book chapter**, not a journal
article: Western Ontario Series in Philosophy of Science is a book series, and
this is pages 379--401 of its volume 73, the Festschrift "Quantum Reality,
Relativistic Causality, and Closing the Epistemic Circle". And Nie et al. has
fourteen authors, not the handful "et al." suggests.

None of the twelve has been read. Two of them should be, before section 4 is
written up rather than after: Felce and Vedral 2020 is the claim section 4
argues with, and Capela, Verma, Costa and Céleri 2023 is titled "Reassessing
thermodynamic advantage from indefinite causal order", which may already make
section 4's argument.

## 9. Exact stdout of `scripts/quantum_switch_graded_fanout_2026-09-19T0900.py`

```
=== Part A: the switch without fragments (A = Rx(1.0), B = Rz(0.7), psi = |0>) ===
c = <BA psi|AB psi> = 0.945949 -0.148073 i
P(+) = 0.972975 = ||{A,B} psi||^2/4 = 0.972975 ; P(-) = 0.027025 = ||[A,B] psi||^2/4 = 0.027025
control case, both generators sigma_z (commuting): P(-) = 0.000000
classical mixture of the two orders: P(+) = P(-) = 0.5 ; indefinite-order signal at R = 0: P(+) - 1/2 = 0.472975

=== Part B: graded FANOUT of the control, real overlaps lambda = cos(0.3) = 0.955336 ===
   R       |Lambda|   P(+) exact   P(-) exact     P(+) brute       signal
   0   1.000000e+00     0.972975     0.027025       0.972975     0.472975
   1   9.553365e-01     0.951850     0.048150       0.951850     0.451850
   2   9.126678e-01     0.931669     0.068331       0.931669     0.431669
   3   8.719049e-01     0.912389     0.087611       0.912389     0.412389
   4   8.329625e-01     0.893970     0.106030       0.893970     0.393970
   6   7.602181e-01     0.859564     0.140436       0.859564     0.359564
   8   6.938266e-01     0.828162     0.171838       0.828162     0.328162
brute force agrees with the closed form to 1e-12 for R <= 8
  16   4.813953e-01     0.727688     0.272312              -     0.227688
  32   2.317414e-01     0.609608     0.390392              -     0.109608
  64   5.370410e-02     0.525401     0.474599              -     0.025401
 128   2.884130e-03     0.501364     0.498636              -     0.001364
 256   8.318206e-06     0.500004     0.499996              -     0.000004
signal falls to 1/e of its R = 0 value at R = 22 (= ceil(1/(-ln cos phi)))

=== Part C: seeded fragment phases theta_k ~ U(-pi, pi), phi = 0.3 ===
theta_k = -1.8401 +2.2942 +1.5986 +1.7783 +3.0558 +0.4839 -2.7596 +2.3650
   R       |Lambda|     arg Lambda   P(+) exact     P(+) brute
   1   9.553365e-01      +0.920069     0.829990       0.829990
   2   9.126678e-01      -0.227037     0.905382       0.905382
   4   8.329625e-01      -1.915488     0.308833       0.308833
   8   6.938266e-01      +2.795113     0.208783       0.208783
|Lambda| is cos^R(phi) regardless of the phases; the phases rotate the signal Re[Lambda c]/2

=== Part D: reversal at R = 6 (real overlaps), brute force on the full state vector ===
signal with 6 fragments written: 0.359564 (closed form 0.359564) ; after applying U_k^dag for all k: 0.472975 ; R = 0 value: 0.472975
reversal exact to 1.1e-15
```
