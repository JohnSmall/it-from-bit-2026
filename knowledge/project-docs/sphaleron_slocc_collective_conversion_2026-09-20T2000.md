# Sphalerons and the GHZ/W split: a collective conversion, not a breakdown of SLOCC

Date: 2026-09-20T2000. Fable session, at JS's prompt on op:sphaleron: "the
sphaleron scale permits transitions between baryon and anti-lepton,
preserving the B-L count. How does this relate to our view of the quark /
lepton split being equivalent to the GHZ/W split enforced by SLOCC, are
sphalerons equivalent a breakdown of SLOCC?" Follows
`records_causal_structure_high_temperature_2026-09-20T1400.md` section 2,
where op:sphaleron was proposed. Numbers from
`scripts/sphaleron_slocc_check_2026-09-20T2000.py`, stdout in section 8.
Labels proposed; the paper's own statements quoted are in
`interactions_circuits_section_2026-06-08.tex` ("Baryon and lepton number
conservation *is* class conservation") and
`entanglement_classes_and_gauge_groups_2026-06-08.tex` (the canonical
orbits).

## 0. The answer in brief

No. A sphaleron is not a breakdown of SLOCC; it is an operation SLOCC never
classified. SLOCC classes are invariants of a *single register* under
*local invertible* operations, and that is exactly the right statement of
what the framework claims and the Standard Model confirms: no vertex turns
one quark into one lepton, no leptoquark gate, no perturbative proton
decay. The sphaleron is neither single-register nor local. It is the 't
Hooft vertex, twelve fermions at once, one from every left-handed doublet,
driven by a unit change in the topological winding of the gauge field: per
generation, one quark from each of the three colours and one lepton,
$\epsilon_{abc}\,q^{a}q^{b}q^{c}\,\ell$, over all three generations. In the
dictionary that is three GHZ registers, one from each colour copy of the
core split, converted collectively with one W register, generation by
generation, under a unit change of the weak vacuum's winding, which is not the
charge winding of the paper's Lemma (see section 17). The
single-copy inequivalence of GHZ and W is untouched, because it was never
about many copies; the multi-copy SLOCC literature already shows that
conversions between the classes become possible with several copies
(verified 2026-09-20 against Chitambar, Duan and Shi, arXiv:0805.2977v1
full text: their Theorem 1(b) is GHZ^{\otimes 3} -> W^{\otimes 2} under SLOCC),
and "forbidden per register, allowed collectively" is
precisely the structure the anomaly has. What the collective conversion
conserves is the copy-additive count $B - L$: three GHZ registers per W
register, the three supplied by colour. So the paper's sentence must change
from "baryon and lepton number conservation is class conservation" to
"class conservation is perturbative baryon and lepton number conservation;
the collective, topological conversion the anomaly supplies conserves
$B - L$", and the framework gains a structural prediction to check: the
fermion content of the 't Hooft vertex is the unique $G_{2}$- and
$S_{3}$-invariant way of changing the class of every doublet register once.

## 1. What the sphaleron is [STRUCTURAL, standard physics]

The electroweak $SU(2)_{L}$ vacuum has a discrete family of gauge-inequivalent
configurations labelled by Chern--Simons winding number; a transition between
neighbouring ones, by tunnelling (instanton) at zero temperature or over the
saddle (the sphaleron, barrier $E_{\rm sph} \sim 9$ TeV) at high temperature,
changes the winding by one. By the index theorem each left-handed $SU(2)$
doublet species loses or gains exactly one fermion per unit winding. The
doublets are three colours times three generations of quarks and three
generations of leptons, twelve in all, so the effective vertex has twelve
fermion legs: per generation a colour-singlet $\epsilon_{abc}q^{a}q^{b}q^{c}$
and one lepton, and all three generations at once. $\Delta B = 3$ and
$\Delta L = 3$ (Part C), so $B + L$ changes by six and $B - L$ by zero;
$B - L$ is the anomaly-free global charge. The rate is $e^{-4\pi/\alpha_{W}}
\approx 10^{-161}$ at zero temperature (Part D), so the proton is stable to
every practical purpose, and it is unsuppressed above the electroweak
crossover, where the barrier vanishes with $v(T)$, which is the
Kuzmin--Rubakov--Shaposhnikov observation on which every leptogenesis
scenario rests (verified 2026-09-20 against INSPIRE-HEP recid 214544 and
Crossref 10.1016/0370-2693(85)91028-7; their abstract puts the rate above
the expansion rate for T > (a few) x 10^2 GeV, and their word is "phase
transition", not "crossover"). Only the left-handed doublets take part: the
process is chiral.

## 2. What SLOCC classifies, and what the paper claims [STRUCTURAL; the paper's claim ESTABLISHED as stated, over-stated in scope]

Dür, Vidal and Cirac's classification (`durvidalcirac2000three`) says: a
single three-qubit state lies in one of two classes of genuine tripartite
entanglement, GHZ or W, and no invertible local operation, one operator per
qubit, takes a state of one class to the other. The class invariant is the
three-tangle, four times the modulus of Cayley's hyperdeterminant: one on
GHZ, zero on W, and nonzero on every SLOCC deformation of GHZ (Part A). The
one-qubit reduced spectrum the paper uses to separate the two canonical
orbits, $(1/2, 1/2)$ against $(2/3, 1/3)$, is a local-unitary invariant and
does its job on the canonical orbits, as the paper says; it is not the
class invariant, since the deformed GHZ-class state with $a^{2} = 2/3$ has
W's spectrum and tangle $8/9$. Worth one clause when the passage is next
touched.

The paper's claim is exact and correct at the level it is made: quark
registers are GHZ-class, lepton registers W-class, every gate the derived
forces supply is class-preserving, the GHZ--W converter "exists as
mathematics and is absent from the gate set", and the $SU(5)$ leptoquarks
are exactly the missing converter. The paper even adds the precision that
the converter is a legitimate circuit on three laboratory qubits and that
the claim is only that a particle's register is not addressed that way. All
of this is single-register: one register in, one register out, one operator
per qubit. That is the perturbative statement, and it is the right one.

## 3. Why the sphaleron is outside SLOCC's scope [CANDIDATE]

Three reasons, each sufficient.

*It is collective.* Twelve registers change together. SLOCC inequivalence is
a statement about one copy. With several copies the classification changes:
tensor rank, the quantity that orders the classes (rank two for GHZ, three
for W, border rank two for W), is not multiplicative over copies, and
conversions between the classes that are impossible for one copy become
possible for several (Chitambar, Duan and Shi 2008; Yu, Chitambar, Guo and
Duan 2010; both verified 2026-09-20, abstracts and, for Chitambar et al., the
full text read. Chitambar et al.'s Theorem 1(b) gives
GHZ^{\otimes 3} -> W^{\otimes 2} under SLOCC. Yu et al. claim the tensor rank
of W^{\otimes 2} is seven; **the correct value is eight**, proved by Chen and
Friedland for the lower bound and Christandl, Jensen and Zuiddam for the
upper. Either way the sentence stands, because a multiplicative rank would
give nine. Both are batched, with six more, in
`bib/multicopy_slocc_refs_2026-09-20T2300.bib`, the Fable session's file;
the Opus session's duplicate of 2200 is withdrawn to
`bib/attic_multicopy_slocc_refs_2026-09-20T2200.bib.superseded`, which records
why and supplies the Chen and Friedland journal details that batch still
wants). "Impossible per register, possible collectively" is therefore not
a breakdown of anything; it is what SLOCC theory itself says once copies are
counted.

*It is not local.* The 't Hooft vertex is induced by a change in the gauge
field's winding, a global property of the configuration, and it acts on all
doublets simultaneously. The framework has a home for this that its gate
dictionary does not yet have: a carrier of the weak vacuum's winding, the
Chern--Simons number of the $SU(2)_{L}$ configuration. (Corrected 2026-09-21,
section 17: this is *not* the ladder number of Lemma lem:winding-number, which is
the colour circle's winding and counts electric charge, conserved by the
sphaleron.) A unit change of that winding is a global operation, not a gate, and "one fermion per
doublet per unit winding" is the selection rule the framework would have to
reproduce from that lemma. That is the PASS criterion below.

*It changes the number of registers.* Nine registers are annihilated and
three created. SLOCC classes label states of a fixed register; they say
nothing about processes that consume and produce registers. What such a
process can conserve is a count additive over registers, and the count the
anomaly conserves is $B - L$: in the dictionary, one third per GHZ register
minus one per W register, with the three coming from colour.

Part B adds a single-copy fact worth keeping in mind and not over-reading:
W lies on the boundary of the GHZ class (the overlap of a rank-two
combination with W tends to one as the tangle tends to zero), so a quark
register can approach a lepton register as a limit and the reverse cannot
happen even as a limit. The sphaleron runs in both directions because it is
collective; the one-copy asymmetry is a different fact.

## 4. The structural match [CANDIDATE]

The fermion content of the 't Hooft vertex is what the framework's own
symmetries would pick out for a collective class change. Colour is the
$C^{3}$ core split, three copies of $\mathbb{C}$; the minimal colour-neutral
combination of GHZ registers is one from each copy, antisymmetrised, which
is $\epsilon_{abc}q^{a}q^{b}q^{c}$. Generations are the component group
$S_{3}$; an operation invariant under it treats the three generations alike,
one colour singlet and one lepton each. The anomaly lives in $SU(2)_{L}$,
which in the framework acts on the left-handed doublet sector and nothing
else (`quantum_numbers_section`, "the doublet is left-handed"), so the
operation is chiral. And the index theorem's "one per doublet per unit
winding" is a change of class for every doublet register at once. So: the
sphaleron's twelve-fermion structure is the unique $G_{2}$- and
$S_{3}$-invariant collective operation that changes the class of every
doublet register once, and its $3 : 1$ ratio of GHZ to W registers per
generation is the core split's three. This is a reading of the Standard
Model's selection rule in the framework's terms, and its value is that the
framework's structure predicts the rule's shape rather than merely
accommodating it. What it does not predict is the rate, which is the
instanton action, dynamics not classification.

## 5. The two columns of the rate [CANDIDATE; the physics STRUCTURAL]

The instanton weight $e^{-S_{E}/\hbar}$ with $S_{E} = 8\pi^{2}/g^{2}$ is a
Euclidean action: the imaginary column of the Landauer-temperature note,
Planck's cell read on a closed Euclidean loop, and at zero temperature the
$B + L$ record is erased only by tunnelling, at $10^{-161}$ per attempt. At
high temperature the same erasure is thermally activated over the sphaleron
barrier, $e^{-E_{\rm sph}/k_{B}T}$, the real column, and above the crossover
the barrier is gone. The sphaleron is therefore the Standard Model's own
example of a record-erasing process whose price rotates from action to heat
with temperature, which is what the high-temperature note said records do.
The record erased is $B + L$; the record that survives, because no operation
in the theory can change it, is $B - L$; and the high-temperature note's
"records survive in conserved charges until the conservation law melts" has
its instance: $B + L$ melts at the crossover, $B - L$ does not.

## 6. What the paper must change, and what op:sphaleron becomes

*The sentences.* `interactions_circuits_section`: "Baryon and lepton number
conservation *is* class conservation" becomes "Class conservation is
perturbative baryon and lepton number conservation: no gate converts one
register's class. The anomaly's collective conversion, twelve registers at
a unit change of winding, is not a gate, conserves $B - L$, and is discussed
at [the new passage]." `predictions_section`: "which the framework gets for
free" becomes "which the framework gets for free at every order in
perturbation theory; the non-perturbative $B + L$ violation of the Standard
Model, negligible today and unsuppressed above the electroweak crossover, is
a collective operation outside the gate set and is not excluded". The
absent-gate section gains one clause of the same kind.

*op:sphaleron, restated with PASS/FAIL.* PASS: (i) identify the dictionary's carrier of the weak vacuum's winding (the
Chern--Simons number, distinct from the charge winding of lem:winding-number)
and exhibit the twelve-register operation as its unit change, with one class
change per doublet register and the charge winding conserved; (ii) show it is the unique $G_{2}$- and $S_{3}$-invariant such
operation, hence $\epsilon(qqq)\ell$ per generation; (iii) show it acts on
the left-handed doublet sector only; (iv) show the copy-additive count it
conserves is $B - L$ with the framework's own charge assignments
(`quantum_numbers_section`). FAIL: a dictionary in which no carrier of the weak vacuum's
winding exists (then the framework forbids the sphaleron and contradicts the
Standard Model, to be owned as a prediction), or one in which a
single-register conversion exists (then it predicts proton decay and is
refuted). The rate is not part of the problem; it is $8\pi^{2}/g^{2}$ and
the framework inherits it.

*op:baryon-contact.* The carried-over open problem "proton stability via
quartic $\epsilon(qqq)\ell$ structure" is, on this reading, the same
object: the per-generation factor of the 't Hooft vertex. Whether the
Hopf--Frobenius machinery it is tied to (op:heunen-functor) produces that
factor as the collective conversion, and not as a perturbative contact term
(which would be proton decay), is the question that joins the two problems.
JS to decide whether to merge them.

## 7. Fences and pushback

- Everything about the sphaleron in section 1 is textbook and cited from
  memory; Kuzmin--Rubakov--Shaposhnikov 1985, 't Hooft 1976, Klinkhamer and
  Manton 1984 (the sphaleron, Phys. Rev. D 30, 2212) and the multi-copy
  SLOCC papers must be read before any of this is written into the paper.
- The multi-copy SLOCC results are cited for their existence and direction
  of travel, not for a rate; nothing here computes a conversion probability,
  and the $10^{-161}$ is the instanton action, which the framework does not
  derive.
- "Unique $G_{2}$- and $S_{3}$-invariant operation" is asserted, not proved;
  it is the content of PASS (ii).
- The framework's $B - L$ assignment is the Standard Model's, reproduced by
  its hypercharge derivation; the claim that $B - L$ is what a collective
  conversion conserves is a reading of that, not a new derivation.
- The paper's current sentence is over-stated in scope, not wrong in
  content. Fix the scope; keep the claim.

## 9. The conversions constructed, and the circuits (added 2026-09-20T2100)

JS asked whether a quantum circuit can be made for the multi-copy conversion.
It can, and the constructions turn the citation of section 3 into a result.
`scripts/multicopy_slocc_conversion_2026-09-20T2100.py` (numpy, exact) and
`scripts/qiskit_multicopy_slocc_circuit_2026-09-20T2100.py` (Qiskit 2.5.2 on
Aer, seed 20260920) do the following, all verified to $10^{-15}$ in the
statevector and by sampling.

*Two GHZ registers to one W register* [STRUCTURAL, by construction]. Each
party holds one qubit of each copy. It sends its two-qubit states
$\lvert01\rangle, \lvert10\rangle, \lvert11\rangle$ to the corresponding factor
of $\lvert001\rangle + \lvert010\rangle + \lvert100\rangle$ and annihilates
$\lvert00\rangle$; scaled by $1/\sqrt2$ this is a valid Kraus operator. The
output is exactly W with success probability $3/32$. As a circuit: a local
two-qubit unitary that sends the kept subspace to (second qubit $= 0$), a
controlled-$R_{y}(\pi/2)$ from the output qubit onto an ancilla for the
$1/\sqrt2$ weight, and the run is kept when the second qubit and the ancilla
both read $0$. Depth 5 after transpilation; sampled kept fraction $0.0926$
against $3/32 = 0.0938$; output distribution $001 : 010 : 100$ at
$0.334 : 0.340 : 0.326$.

*Two W registers to one GHZ register* [STRUCTURAL, by construction]. The
partial isometries $A = \lvert1\rangle\langle00\rvert + \lvert0\rangle\langle11\rvert$,
$B = \lvert1\rangle\langle01\rvert + \lvert0\rangle\langle00\rvert$,
$C = \lvert1\rangle\langle10\rvert + \lvert0\rangle\langle00\rvert$ send $W \otimes W$
to exactly GHZ with success probability $2/9$. As a circuit: two local
basis permutations (party C needs none) and the run is kept when every
party's second qubit reads $0$. Depth 10; sampled kept fraction $0.2173$
against $2/9 = 0.2222$; output $000 : 111$ at $0.503 : 0.497$.

*The sphaleron-shaped maps* [STRUCTURAL as construction; the shape CANDIDATE].
Three GHZ registers to one W register, the same construction on three
copies, success $3/64$; three W registers to one GHZ, using two of the three
copies and projecting the third, $2/27$. Neither needs the third copy for
rank; the sphaleron's three is colour neutrality, not tensor rank.

*What the circuits show, and do not.* They show that the multi-copy
conversion between the classes is a concrete, local, postselected
operation, in both directions, with two copies; that one copy suffices in
neither direction (tensor rank one way, the three-tangle the other, Part A
of the numpy script); and that the sphaleron's fermion content is a
particular such conversion with an extra symmetry constraint. They do not
show that the sphaleron *is* an SLOCC conversion: the physical process is a
unitary transition of the gauge field with the fermion number change forced
by the index theorem, and its "success probability" is the instanton weight,
not a postselection rate. The right statement, now in the paper, is that
multi-copy inter-convertibility is the kinematic room the anomaly occupies,
and the winding change is what selects, out of every collective conversion
the mathematics permits, the one nature performs.

*A hardware run.* The two circuits are six and nine qubits, depth ten and
five, and every gate after preparation is local to one party; with
postselection on the flags they are within reach of the IBM backend the Opus
session is setting up for notebook S. The expected signatures are the
$000/111$ and $001/010/100$ distributions above with kept fractions $2/9$
and $3/32$, degraded by device noise. Worth adding to the hardware task.

## 10. Applied to Paper 1 (2026-09-20T2100)

`scripts/patch_collective_class_conversion_2026-09-20T2100.py`, on the main
working tree, uncommitted and unbuilt: the absent-gate subsection's sentence
re-scoped to "at every order in perturbation theory ... on a single
register"; a new paragraph with the 't Hooft vertex, the multi-copy
conversions with the explicit constructions and probabilities, $B-L$ as the
copy-additive count, the candidate reading of the vertex's content, and the
kinematic-room sentence; Open Problem op:sphaleron with the PASS/FAIL of
section 6; the predictions section's "gets for free" re-scoped with a
pointer. Three new citation keys in `bib/sphaleron_slocc_refs_2026-09-20T2100.bib`,
verified 2026-09-20 (see section 13) and undefined until imported.

## 14. Why twelve, when two would do (added 2026-09-20T2200; numbered 14 to leave the Opus session's 13 in place)

JS: "The sphaleron converts 3 baryons into 3 anti-leptons. But these circuits
are doing a different transformation. If the circuits can do the transform
with fewer qubits, why does the sphaleron need 3 baryons and 3 anti-leptons?"

Three counts from three sources. *Entanglement kinematics* sets the minimum
for a class change: two registers (section 9). *Gauge invariance* forbids
the two-to-one conversion: two quarks are not a colour singlet, and two quark
doublets carry hypercharge $2/3$ against a lepton doublet's $-1$; electric
charge and $B-L$ fail likewise. The smallest gauge-neutral collective class
change is three quarks of three colours to one lepton, per generation:
$\epsilon_{abc}$ for colour and $3\times\tfrac13 - 1 = 0$ for hypercharge.
*The index theorem* makes it all generations at once: a unit change of
winding shifts the fermion number of every left-handed doublet by one,
because the gauge coupling is universal, so one step is twelve fermions, one
per doublet; with one generation it would be $qqq\ell$ and $\Delta B = 1$.
The sphaleron does not need three baryons; one ladder step touches every
generation once.

In the framework's terms: colour neutrality is one register from each copy
of the core split; hypercharge neutrality per generation is the paper's own
tracelessness (a generation as a complete multiplet of the traceless
generator, the Jaynes appendix's `prop:trace-blind` and op:anomalies), so the
neutral operator is one complete multiplet; and a ladder step is blind to the
$S_{3}$ of generations, so it acts in all three. The 't Hooft vertex is the
minimal traceless collective class change, once per generation, all
generations together, which is PASS (ii) of op:sphaleron stated more sharply.

Owed to the paper (v2 list): the new paragraph's "the three supplied by
colour" should read "supplied by colour and hypercharge together", citing the
tracelessness proposition. A faithful circuit would be, per generation, three
colour-distinct GHZ registers to one W register (nine qubits plus three
flags, success $3/64$, computed exactly, not built), performed in all three
generations at once (twenty-seven register qubits plus flags), since the
winding step is one operation on the whole register.

## 11. Exact stdout of `scripts/multicopy_slocc_conversion_2026-09-20T2100.py`

```
=== Part A: single copy ===
tangle(GHZ) = 1.000000 ; tangle(W) = 0.000000 ; tensor rank GHZ = 2, W = 3 (W = |001>+|010>+|100> is three product terms and no fewer)
rank cannot rise under local operators, so GHZ -> W is impossible for one copy; W -> GHZ is impossible because the tangle of any local image of W is zero

=== Part B: GHZ x GHZ -> W ===
Kraus norms at most one: A True, B True, C True
GHZ x GHZ -> W (each party 4 -> 2 dims)  success probability = 0.093750 = 3/32 ; fidelity with target = 1.000000000000000

=== Part C: W x W -> GHZ ===
Kraus norms at most one: A True, B True, C True (partial isometries)
W x W -> GHZ (each party 4 -> 2 dims)    success probability = 0.222222 = 2/9 ; fidelity with target = 1.000000000000000

=== Part D: the sphaleron-shaped conversions ===
GHZ x GHZ x GHZ -> W (three colours to one lepton) success probability = 0.046875 = 3/64 ; fidelity with target = 1.000000000000000
W x W x W -> GHZ (copy 3 projected onto |001>) success probability = 0.074074 = 2/27 ; fidelity with target = 1.000000000000000

=== Part E: summary ===
two copies suffice in both directions; one copy suffices in neither; the sphaleron's three-to-one is colour, not rank
```

## 12. Exact stdout of `scripts/qiskit_multicopy_slocc_circuit_2026-09-20T2100.py`

```
=== Circuit 1: W x W -> GHZ (postselected local permutations) ===
exact: success probability = 0.222222 (2/9 = 0.222222) ; fidelity of the kept output with GHZ = 1.000000000000
Aer, 40000 shots, seed 20260920: kept fraction = 0.2173 ; output distribution on (a1 b1 c1): {'000': 0.5029, '111': 0.4971}
depth after transpile to Aer: 10

=== Circuit 2: GHZ x GHZ -> W (postselected local unitaries with an ancilla weight) ===
exact: success probability = 0.093750 (3/32 = 0.093750) ; fidelity of the kept output with W = 1.000000000000
Aer, 40000 shots, seed 20260920: kept fraction = 0.0926 ; output distribution on (a1 b1 c1): {'001': 0.3343, '010': 0.34, '100': 0.3257}
depth after transpile to Aer: 5

both conversions are local: every gate after preparation acts within one party's qubits, and the only communication is the classical decision to keep the run
```

## 8. Exact stdout of `scripts/sphaleron_slocc_check_2026-09-20T2000.py`

```
=== Part A: single-register invariants ===
GHZ  reduced spectrum (0.500000, 0.500000) ; three-tangle = 1.000000
W    reduced spectrum (0.666667, 0.333333) ; three-tangle = 0.000000
a|000>+b|111>, a = 0.60: spectrum (0.6400, 0.3600) ; tangle = 0.921600 = 4 a^2 b^2 = 0.921600
a|000>+b|111>, a = 0.80: spectrum (0.6400, 0.3600) ; tangle = 0.921600 = 4 a^2 b^2 = 0.921600
a|000>+b|111>, a = 0.95: spectrum (0.9025, 0.0975) ; tangle = 0.351975 = 4 a^2 b^2 = 0.351975

=== Part B: W as a limit of GHZ-class (rank-two) states ===
e = 0.500: |<W|chi_e>|^2 = 0.78688525 ; tangle(chi_e) = 6.880e-02
e = 0.100: |<W|chi_e>|^2 = 0.99006633 ; tangle(chi_e) = 4.357e-03
e = 0.010: |<W|chi_e>|^2 = 0.99990001 ; tangle(chi_e) = 4.444e-05
e = 0.001: |<W|chi_e>|^2 = 0.99999900 ; tangle(chi_e) = 4.444e-07
the overlap tends to one while the tangle tends to zero: the W class is on the boundary of the GHZ class, not inside it

=== Part C: the 't Hooft vertex ===
left-handed doublets: 9 quark (3 colours x 3 generations) + 3 lepton = 12 ; one fermion each per unit winding
Delta B = 9 x 1/3 = 3 ; Delta L = 3 x 1 = 3 ; Delta(B - L) = 0 ; Delta(B + L) = 6
per generation: epsilon_abc q^a q^b q^c l, one quark from each colour copy and one lepton: three GHZ registers to one W register

=== Part D: the two columns of the rate ===
alpha_W = alpha_em(M_Z)/sin^2 theta_W = 0.03380 ; instanton action 4 pi/alpha_W = 371.7 ; weight exp(-4 pi/alpha_W) = 10^-161.4 (T = 0, action column)
k_B T =      1 GeV: activation factor exp(-E_sph/k_B T) = 10^-3908.7  (E_sph = 9 TeV, heat column; the barrier itself falls with v(T) and vanishes above the crossover)
k_B T =     10 GeV: activation factor exp(-E_sph/k_B T) = 10^-390.9  (E_sph = 9 TeV, heat column; the barrier itself falls with v(T) and vanishes above the crossover)
k_B T =    100 GeV: activation factor exp(-E_sph/k_B T) = 10^-39.1  (E_sph = 9 TeV, heat column; the barrier itself falls with v(T) and vanishes above the crossover)
k_B T =    160 GeV: activation factor exp(-E_sph/k_B T) = 10^-24.4  (E_sph = 9 TeV, heat column; the barrier itself falls with v(T) and vanishes above the crossover)
```

## 13. Citation verification (added 2026-09-20T2200, Opus session)

All three keys in `bib/sphaleron_slocc_refs_2026-09-20T2100.bib` were checked
against records and against the sources themselves. The batch has been
corrected in place and each `note` now says what was checked and where.
Bibliographic corrections: 't Hooft pages 8 to 8--11; Kuzmin, Rubakov and
Shaposhnikov gained the registered DOI `10.1016/0370-2693(85)91028-7`, which
the original note said did not exist, and pages 36 to 36--42; Chitambar, Duan
and Shi gained the issue number and the arXiv eprint.

**One discrepancy, reported and not fixed.** Section 1 of this document and the
new paragraph in `paper1/interactions_circuits_section_2026-06-08.tex` both
attribute a twelve-fermion vertex with $\Delta B = \Delta L = 3$ to 't Hooft
1976. The scanned Letter was read. Its Standard-Model application is Eq. (24)
on page 10, and it is the **two-generation** Weinberg--Salam model:

> $\Delta E = \Delta M = 1$, $\Delta u + \Delta d^{C} = 3$,
> $\Delta u' + \Delta s^{C} = 3$
>
> "Thus, because of the Cabibbo rotation, a proton and a neutron (two baryons
> equal six quarks) may annihilate to form two antileptons, one of electron and
> one of muon type."

That is **eight** fermions with $\Delta B = \Delta L = 2$. The twelve-fermion,
$\Delta B = \Delta L = 3$ form is the standard three-generation extension and
is correct physics; it is simply not what the cited Letter says, and $B - L$
conservation is implicit in his Eq. (24) rather than asserted anywhere in it.
The Letter is also a toy SU(2) model with $N$ flavours for most of its length;
the detailed effective vertex was deferred to the companion, Phys. Rev. D 14
(1976) 3432, added to the batch as `thooft1976quantum`.

Proposed fix, for JS to accept or decline, to the sentence in
`interactions_circuits_section_2026-06-08.tex` beginning "A unit change in the
winding". Replace

> ... with $\Delta B = \Delta L = 3$ and $B-L$ conserved
> \autocite{thooft1976symmetry}.

with

> ... with $\Delta B = \Delta L = 3$ and $B-L$ conserved
> \autocite{thooft1976symmetry,thooft1976quantum}. ('t~Hooft's own
> application is the two-generation model, where the vertex has eight
> fermions and $\Delta B = \Delta L = 2$; the count above is the
> three-generation case.)

If the parenthesis is unwanted, citing both keys alone is still an improvement,
since the companion is where the vertex is computed. A patch script is not
written: the fix is JS's to take.

Two smaller points, neither a fault. The rate figure $10^{-161}$ uses
$\alpha_{W} = \alpha_{\mathrm{em}}(M_{Z})/\sin^{2}\theta_{W} = 0.03380$
(Part D above); 't Hooft writes the same factor on page 10 as
$\exp(-4\pi \times 137 \sin^{2}\theta_{W})$, which at the low-energy
$\alpha$ would give roughly $10^{-173}$. Same formula, different scale, and
the paper's choice is the defensible one. And Kuzmin, Rubakov and Shaposhnikov
say "phase transition" where the paper says "crossover"; the crossover is the
later lattice result and belongs to D'Onofrio and Rummukainen.

## 15. References for multi-copy conversion, verified 2026-09-20T2300 (Fable session)

JS asked what references exist for using copies of GHZ to obtain W or the
reverse. Verified against the arXiv abstract pages (authors, title, journal
reference, DOI) and batched in `bib/multicopy_slocc_refs_2026-09-20T2300.bib`;
the Opus session's section 13 above covers the three keys of the earlier
batch and the 't Hooft discrepancy.

- Dür, Vidal and Cirac 2000 (`durvidalcirac2000three`, in the library): the
  single-copy inequivalence of GHZ and W under SLOCC.
- Chitambar, Duan and Shi, Phys. Rev. Lett. 101, 140502 (2008): tensor rank
  governs SLOCC convertibility; NP-hard in general; Theorem 1(b) gives
  GHZ$^{\otimes 3} \to$ W$^{\otimes 2}$ (Opus session, full text read); the
  GHZ-to-EPR-triangle rate is the matrix multiplication exponent.
- Yu, Chitambar, Guo and Duan, Phys. Rev. A 81, 014301 (2010): bounds on the
  rank of copies of W; their rank seven for two copies was later corrected.
- Chen, Chitambar, Duan, Ji and Winter, Phys. Rev. Lett. 105, 200501 (2010):
  transformations impossible for one copy become possible in multiple-copy
  bunches or with a catalyst.
- Chen and Friedland, Linear Algebra Appl. 543, 1--16 (2018): the rank of two
  copies of W is eight, with the upper bound of Christandl, Jensen and
  Zuiddam (2018, VERIFY-CITE the details).
- Yu, Guo and Duan, Phys. Rev. Lett. 112, 160401 (2014): one W from one GHZ
  asymptotically, rate one, from $n + o(n)$ copies of GHZ.
- Vrana and Christandl, J. Math. Phys. 56, 022204 (2015): GHZ to W at rate
  one for any number of parties, via degeneration and border rank; the W to
  GHZ rate computed with Strassen's monotones (value not in the abstract).
- Neven, Gunn, Hebenstreit and Kraus, SciPost Phys. 11, 042 (2021): under
  multi-state LOCC the SLOCC class of an individual state can be changed by
  transferring entanglement from another.
- Walter, Gross and Eisert, arXiv:1612.02437 (2016): the review.

One thing to read for. The Opus session quotes Chitambar, Duan and Shi as
remarking that "previously, only one copy of the W state is known to be
convertible from three copies of GHZ". Section 9's construction gives one W
from *two* copies of GHZ at probability $3/32$, and it is elementary: two
copies of GHZ are the four-level GHZ state, whose local images are every
tensor of rank at most four, and W has rank three. Either the remark refers
to a different notion (a rate, or a deterministic conversion) or the
two-copy construction was not in the literature they surveyed; whoever reads
the paper in full should settle which, and the paper's paragraph should not
claim the two-copy map as theirs.

## 16. What the circuits cannot see: charges (added 2026-09-21)

JS: "the quantum circuits we've been using don't seem to be able to
represent gauge symmetries and hence charges, is that correct?" Correct of
the circuits used (notebook S, the switch, the two-copy conversions): bare
qubits, arbitrary local unitaries or Kraus maps, no charge operators, no
restriction of the gate set, no colour or hypercharge labels; they carry the
entanglement class and the phases only, which is why the two-copy conversion
could ignore colour and hypercharge. Not correct of circuits in general: a
global charge is an operator commuting with every gate, and a gauge symmetry
proper is standard in lattice-gauge-theory simulation with link registers
and a Gauss-law constraint (Banuls et al. 2020 review; Martinez et al. 2016;
VERIFY-CITE). In the framework's own terms the charges are already functions
of the circuit state: the register is $\mathbb{O} = \mathbb{C} \oplus
\mathbb{C}^{3}$ with the phase torus acting, hypercharge the trace direction
(prop:trace-blind), colour which of the three lines the state occupies, and
the three-qubit space is the sixteen real dimensions of two octonions, so
every simulated state has an octonionic image and hence a colour and a
hypercharge. What the circuits lack is (i) the charge operators written on
the register so they can be computed or measured, and (ii) the gate set cut
to operations commuting with them, which is what "the dictionary is
class-closed" means in circuit terms; the paper's Qiskit appendices (beta
decay with CKM, GHZ--W interference, the baryon) are circuits of that kind.

A gauge-faithful sphaleron circuit, proposed as the next computation: tag
three registers as the three colour lines; require the collective map to be
antisymmetric under permuting them and neutral under the trace direction;
show the two-copy map fails both and the three-to-one per generation passes.
Needs the charge operators on the register written out from the
quantum-numbers section first.

*In the paper (2026-09-21T0900).* JS: "honestly state what the circuits can
do, and what they can't do, and say that we're working on circuits that
respect gauge symmetries and conservation laws and will publish in a
subsequent paper." Applied by `scripts/patch_circuit_scope_statement_2026-09-21T0900.py`
to the collective-conversion paragraph of the absent-gate subsection: the
circuits carry class and phase only, no charge operator and no restricted
gate set, hence can perform what the charges forbid; they establish the
kinematic room and only that; charges are functions of the register's
octonionic image (sec:charges) so faithful circuits are possible at the
price of the operators and the restriction; such circuits are in preparation
for a subsequent paper; nothing in the section rests on them. Uncommitted,
unbuilt.

## 17. Correction: two windings, not one (added 2026-09-21T1000)

JS asked whether op:sphaleron needs changing in the light of the later
conversations. It does, and the first change is a correction of my own
error. The minted problem and the motivating sentence identified the
sphaleron with "a change in the ladder number of the whole register
(Lemma lem:winding-number)". The lemma says the ladder number is the
relative winding of the colour circle's spinor lift, with $Q = N/3$: it is
the electric charge in thirds, a property of one register. The sphaleron
conserves electric charge. Its winding is the Chern--Simons number of the
$SU(2)_{L}$ vacuum, a property of the gauge configuration, and the
dictionary has as yet no object that carries it; finding one is the real
content of PASS (i). Every sentence in this note that said "ladder step" or
"ladder number of the whole register" for the sphaleron meant the weak
vacuum's winding, and sections 0, 3 and 6 are amended above; section 14's
"one ladder step touches every generation once" should be read the same way.

The second change is a sharpening from section 14: uniqueness needs
neutrality under the trace direction (hypercharge) as well as colour (the
$G_{2}$ stabiliser) and $S_{3}$. The third is from section 16: a FAIL for a
dictionary whose lawful gates admit the two-register conversion, and PASS
(iv) made computable with the charge operators on the register, which ties
the problem to the gauge-respecting circuits the paper now promises.

The revised statement is drafted, anchor-checked and unrun in
`scripts/patch_op_sphaleron_revised_2026-09-21T1000.py`; it also corrects the
motivating sentence in the paragraph and retitles the problem "The sphaleron
as a collective class change". JS ruled 2026-09-23: applied on the main
working tree (backup `.2026-09-21T1000.bak`), uncommitted, unbuilt; labels
checked, no old wording survives.

## 18. Can the sphaleron route generate sterile neutrinos? (added 2026-09-21T1100)

JS's last question before leaving sphalerons. No, directly; yes, in the
direction the standard literature runs it, and with a consequence for the
framework's own sterile pair.

*No, directly* [STRUCTURAL]. The 't Hooft vertex has one leg per left-handed
(2)_{L}$ doublet and none else. A sterile neutrino is a singlet with
{3} = 0$ and  = 0$, the framework's "sterile class" of the
quantum-numbers section, and it never appears on the vertex. In this note's
language it is outside the twelve registers of the collective class change.
Steriles are made from active neutrinos by mixing through the Yukawa
coupling, a gate, not by the winding.

*Yes, reversed* [STRUCTURAL as standard physics]. Leptogenesis: steriles
produce a lepton asymmetry, by out-of-equilibrium CP-violating decay
(Fukugita and Yanagida 1986) or by CP-violating oscillations (Akhmedov,
Rubakov and Smirnov 1998; the $
u of Asaka and Shaposhnikov 2005), and
the sphaleron converts part of it to baryons,  = (28/79)(B-L)$ in the
Standard Model. The steriles are the source; the sphaleron is the converter;
baryons are the product. All from memory, VERIFY-CITE.

*The framework's pair* [CANDIDATE]. Two steriles with {1} = 0$ exactly is
the minimal two-right-handed-neutrino seesaw, the Frampton--Glashow--Yanagida
structure (2002, VERIFY-CITE): rank-two active mass matrix, one Majorana
phase, the sign of the baryon asymmetry fixed by the low-energy CP phase. So
the framework's neutrino sector is the textbook leptogenesis sector. Its
scale is not: at .6$ TeV the Davidson--Ibarra bound gives a CP asymmetry of
	imes10^{-13}$ against the ^{-6}$ to ^{-7}$ needed, a shortfall of
six to seven orders (Part A). The only thermal route left is resonant
leptogenesis (Pilaftsis and Underwood 2004, VERIFY-CITE), which requires the
two steriles to be degenerate to about one part in ^{6}$ to ^{7}$
(Part B). The framework puts both at the one matching scale, so a near
degeneracy is natural rather than tuned; whether their splitting is that
small is a question the framework can ask of itself, and if it can answer
it, the baryon asymmetry becomes a prediction or a refutation. The
oscillation route prefers GeV-scale steriles and does not obviously reach
.6$ TeV. Numbers in section 19.

*What it does to the record picture.* The high-temperature note called
-L$ the record that survives the crossover. That holds only if the steriles
are Dirac. A Majorana mass is a $\Delta L = 2$ eraser, and with it nothing
protects $; that is precisely what leptogenesis needs. The framework must
therefore say whether its steriles are Majorana or Dirac: Majorana gives it
leptogenesis and costs it the -L$ record; Dirac keeps the record and
leaves the baryon asymmetry unexplained. In the two-columns language the
asymmetry is a CP phase, imaginary column, converted by an out-of-equilibrium
decay into a conserved-charge record, real column, that survives to the
present: the oldest record there is. RHYME, kept out of the paper.

*Owed.* JS to say Majorana or Dirac; the splitting of the two steriles from
the matching-scale construction (op:matching-scale); the references above.

## 19. Exact stdout of `scripts/sterile_leptogenesis_scale_2026-09-21T1100.py`

```
=== Part A: hierarchical leptogenesis at the framework's sterile scale ===
Davidson--Ibarra bound at M = 3.6 TeV, m_3 = 0.050 eV: |eps_1| <= 3.548e-13
kappa = 1e-01: eps needed = 6.35e-07 ; shortfall factor = 1.8e+06
kappa = 1e-02: eps needed = 6.35e-06 ; shortfall factor = 1.8e+07
hierarchical thermal leptogenesis fails at 3.6 TeV by six to seven orders of magnitude (the Davidson--Ibarra bound wants M >~ 1e9 GeV)

=== Part B: the resonant route, two nearly degenerate steriles ===
kappa = 1e-01: enhancement needed ~ 1.8e+06, so Delta M / M ~ 5.6e-07
kappa = 1e-02: enhancement needed ~ 1.8e+07, so Delta M / M ~ 5.6e-08
i.e. the two 3.6 TeV steriles must be degenerate to about one part in 1e6 to 1e7 for the sphaleron route to supply the observed asymmetry
sphaleron conversion factor B/(B-L) = 28/79 = 0.354

=== Part C: the framework's neutrino sector as the minimal two-sterile seesaw ===
two right-handed (sterile) neutrinos, active mass matrix of rank 2: m_1 = 0 exactly; one Majorana phase; one Dirac phase
this is the Frampton--Glashow--Yanagida structure, in which the sign of the baryon asymmetry is fixed by the low-energy CP phase
```

## 20. Do non-interacting steriles gravitate? (added 2026-09-21T1200)

JS: "The key point within the framework's reading of spacetime as purely a
network of relations between events is that it was a problem for massive
sterile neutrinos to form records if they don't interact with anything, and
therefore they can't have a gravitational pull. But if an interaction
channel opens up at the sphaleron scale then there is a possibility of them
interacting with other things."

The tension is real and the framework's own premises resolve it, but the
channel is not the sphaleron and the problem is narrower than stated.

*They do interact, and copiously, once* [STRUCTURAL as standard physics].
A sterile couples to the lepton doublet and the Higgs through its Yukawa,
the framework's Higgs vertex, the chirality-flip gate. With seesaw-size
Yukawas at  = 3.6$ TeV the coupling squared is 	imes10^{-12}$, the width
.5	imes10^{-10}$ GeV, the lifetime 	imes10^{-16}$ s, and the washout
parameter  = \Gamma_{N}/H(T = M) pprox 47$ (Part B): at  \sim M$, about
^{-14}$ s, the steriles are in thermal equilibrium with the plasma
through that gate. They form records then, in abundance, and they decay
promptly into records (active leptons and Higgs or gauge bosons). So the
framework's 3.6 TeV steriles are early-universe particles with a recorded
birth and a recorded death, not dark matter. The channel that opens at high
temperature is the Yukawa, not the sphaleron, which never touches a singlet
(section 18); the sphaleron's role is downstream, converting the lepton
asymmetry those interactions can leave.

*Energy-momentum is a record that persists* [CANDIDATE, from the
high-temperature note]. For anything that interacts only once, at its
production, the framework still holds a record of its energy and momentum:
the recoil of its production partners, and after that the conservation law,
which the high-temperature note identified as the kind of record that
survives. A particle's gravitational monopole, its total energy-momentum, is
therefore recorded by everything it has ever exchanged momentum with, and
stays recorded whether or not it interacts again. In Jacobson's terms the
horizon's records are the vacuum correlations of every field across the
surface, free fields included, and a free particle's energy flux across a
local Rindler horizon is heat like any other. So "no interaction after
production, hence no gravity" is not what the framework's premises say. What
they do say is sharper and better.

*What is not a fact: the field between events* [CANDIDATE]. Between its
production and its next record a particle's motion is a phase (hub, section
4c), and its position is not a fact. So its gravitational field at
resolution finer than its records is not a fact either: only the conserved
totals are. The framework predicts that unrecorded matter gravitates as a
delocalised source until something localises it, which is Paper 2's "gravity
follows the resolution, not the average" applied to a source that has not
been resolved, and it is what dark-matter phenomenology sees, a smooth
density and no localised lensing by individual particles. A species that has
never had an event at all is not in the network and has no gravity, and also
no existence anyone could test; the framework's relationalism bites only
there, which is Mach's position and not a defect.

*So, for the framework's own steriles.* They gravitate in the early
universe as thermal particles, recorded at every collision; after they
decay, their energy is in their products. If JS intends a stable sterile as
dark matter, it is not these: a stable one needs a Yukawa small enough to
survive, is produced by mixing (Dodelson--Widrow) at a recorded epoch, and
gravitates thereafter through its conserved energy as a delocalised source,
which is exactly the cold, smooth component observed. The sphaleron plays no
part in either case.

*Owed.* JS to say whether the 3.6 TeV steriles are meant to be stable (then
the Yukawa must be far below seesaw size and the neutrino masses come from
elsewhere) or the leptogenesis pair of section 18; and Paper 2 to carry the
"delocalised source" statement beside its Page--Geilker paragraph.

## 21. Exact stdout of `scripts/sterile_records_early_universe_2026-09-21T1200.py`

```
=== Part A: the Yukawa gate and the decay ===
seesaw Yukawa squared h^2 ~ 5.95e-12 ; mixing angle squared theta^2 ~ m_3/M = 1.39e-14
width Gamma_N = 8.52e-10 GeV ; lifetime 7.7e-16 s : the framework's steriles decay promptly and are not dark matter

=== Part B: equilibrium at T = M ===
H(T = 3.6 TeV) = 1.82e-11 GeV ; K = Gamma_N / H = 47
K >> 1: the steriles thermalise through the Yukawa gate (strong washout); they interact copiously at T ~ M and form records then

=== Part C: when ===
sterile epoch, T = M     T = 3.600e+03 GeV ; t ~ 1.8e-14 s
top/Higgs threshold      T = 1.726e+02 GeV ; t ~ 7.9e-12 s
electroweak crossover    T = 1.600e+02 GeV ; t ~ 9.1e-12 s
the steriles' records are written at ~1e-13 s, before the clocks of the top and Higgs switch on at ~1e-11 s
```
