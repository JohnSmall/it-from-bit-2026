# Complexified algebras or real algebras with a complex structure? (2026-09-27T1400)

JS: "the fact that we settled on complex probability amplitudes because
Shannon information has to be additive and therefore commutative means that
we have to view, i.e. perform experiments, through the lens of complex
probability amplitudes, which do allow a tensor product. So we always use
complexified quaternions, complexified octonions and complexified sedenions.
Is that correct?" Script `scripts/complexified_vs_complex_structure_2026-09-27T1400.py`,
stdout in section 3. Labels proposed.

## 1. Answer

Correct in substance, with one precision that matters. The premise is the
framework's own: the amplitudes are complex because information adds and
addition commutes, the Hilbert space is $\mathbb{C}^{2^{n}}$, tensor products
exist, and the first group of objections to division-algebra field theories
(no quaternionic tensor product, no octonionic operator calculus) never
arises. Dimensionally, $\mathbb{C}^{2^{n}}$ is both the complexification
$\mathbb{C}\otimes A_{n}$ of the $n$-th Cayley--Dickson algebra (complex
dimension $2^{n}$, Furey's and Gillard--Gresnigt's object) and the next
algebra $A_{n+1}$ viewed as a real space with a complex structure (real
dimension $2^{n+1}$, the Hopf tower's object: one qubit is $\mathbb{H}$, two
are $\mathbb{O}$, three are $\mathbb{O}^{2}$, the unit sphere of the
sedenions as a real space). Adding a qubit is one Cayley--Dickson doubling in
either reading (Part A).

The precision. Complexification destroys the division property. In
$\mathbb{C}\otimes\mathbb{H}$ and $\mathbb{C}\otimes\mathbb{O}$, with the
product extended bilinearly and the bilinear norm $N(x) = \sum x_{i}^{2}$,
the element $1 + i e_{1}$ has $N = 0$ and $x\bar x = 0$: a zero divisor (Part
B); $\mathbb{C}\otimes\mathbb{H}$ is $M_{2}(\mathbb{C})$ and
$\mathbb{C}\otimes\mathbb{O}$ is the split octonions. The properties the
framework uses, norm composition, no zero divisors before the sedenions,
parallelisability, Hurwitz and Adams, belong to the *real* algebras (Part B:
composition exact to $10^{-16}$ in real $\mathbb{H}$ and $\mathbb{O}$, a
defect of order one in real $\mathbb{S}$). And the framework's identification
is the real one: the paper's Lemma lem:cproj takes each first-qubit branch
$\mathbb{C}^{4}$ as the real octonions with the complex structure "left
multiplication by $e_{1}$". Part C constructs that identification from
Convention A's own table: $e_{1}$ pairs the basis as $(e_{0},e_{1})$,
$(e_{2},e_{3})$, $(e_{4},e_{5})$, $(e_{6},-e_{7})$, the last with a sign,
which is the "sign bookkeeping" the appendix says is part of the proof; with
it, the Hermitian norm of $\psi$ is the real octonionic norm of its 8-vector
and multiplying $\psi$ by $i$ is left multiplication by $e_{1}$, both exact.

So the accurate slogan is: the framework uses the real Cayley--Dickson
algebras carrying the amplitude's complex structure, with $e_{1}$ the
preferred direction, and the $n$-qubit register is $A_{n+1}$ so read. "The
complexified octonions" is Furey's construction and a true statement about
dimensions, but if it were meant literally the framework's division-algebra
results would be false, because the complexified algebras have zero divisors
from the quaternions onward. The two readings meet at the sedenions, which
have zero divisors either way; the ChatGPT review's caution about the real
versus the Hermitian norm in any norm-defect-to-mass bridge is the same point
from the other side, and lem:cproj is where the framework pays it.

## 2. Proposed ledger entry and a wording point

- **STRUCTURAL** (computation) $\mathbb{C}^{4} \cong \mathbb{O}$ via left
  multiplication by $e_{1}$ in Convention A, pairs
  $(0,1,+), (2,3,+), (4,5,+), (6,7,-)$; Hermitian norm equals real norm;
  $i \leftrightarrow L_{e_{1}}$ exactly. Complexified $\mathbb{H}$ and
  $\mathbb{O}$ have the zero divisor $1 + ie_{1}$; real $\mathbb{H}$,
  $\mathbb{O}$ compose norms exactly.
- Wording, wherever the paper or a note says "complexified": say "the real
  algebra with the amplitude's complex structure" unless Furey's
  $\mathbb{C}\otimes\mathbb{O}$ is meant, and say which. The
  hopf_justification and sedenion sections should be grepped for the word at
  the v2 pass.

## 3. Exact stdout

```
=== Part A: dimensions ===
qubits  dim_C C^(2^n)        dim_C C(x)A_n        dim_R A_(n+1)/2
     1              2                    2                      2
     2              4                    4                      4
     3              8                    8                      8
     4             16                   16                     16
adding a qubit doubles the space; so does one Cayley--Dickson step, in either reading

=== Part B: complexification has zero divisors, the real algebras up to O do not ===
C (x) H  x = 1 + i e_1: N(x) = 0j ; x xbar = True ; x nonzero, xbar nonzero -> zero divisor
C (x) O  x = 1 + i e_1: N(x) = 0j ; x xbar = True ; x nonzero, xbar nonzero -> zero divisor
H (real) worst relative norm-composition defect over 2000 random pairs: 6.68e-16
O (real) worst relative norm-composition defect over 2000 random pairs: 6.10e-16
S (real) worst relative norm-composition defect over 2000 random pairs: 6.81e-01
S (real) an explicit zero divisor pair from the corpus scans: |zw| = 0.000e+00

=== Part C: C^4 as the real octonions with the e_1 complex structure ===
L_{e_1}^2 = -I: True
e_1 e_a = s e_b on the pairs (a, b, s): [(0, 1, 1), (2, 3, 1), (4, 5, 1), (6, 7, -1)]
Hermitian norm of psi equals the real octonionic norm of its 8-vector: worst |difference| = 3.6e-15
multiplying psi by i equals left multiplication of its 8-vector by e_1: worst |difference| = 0.0e+00
so the paper's octonions are the REAL algebra carrying the amplitude's complex structure (e_1 with its sign bookkeeping), not the complexification
```

## 4. JS's example: the colour force from the octonions, the colour state a complex superposition (added 2026-09-27T1500)

The example is the place where the two structures meet, and the meeting is
one choice seen twice. Script `scripts/colour_su3_from_e1_structure_2026-09-27T1500.py`,
stdout below. In Convention A the derivations of $\mathbb{O}$ form a
14-dimensional algebra ($\mathfrak{g}_{2}$); those annihilating the preferred
unit $e_{1}$ form an 8-dimensional subalgebra; every one of them commutes
with left multiplication by $e_{1}$ (because $g(e_{1}x) = g(e_{1})g(x) =
e_{1}g(x)$ for an automorphism fixing $e_{1}$), so each is complex-linear for
the complex structure $e_{1}$ defines; read on the six-dimensional complement
of the line $(e_{0}, e_{1})$ through the three $e_{1}$-invariant planes
$(e_{2},e_{3})$, $(e_{4},e_{5})$, $(e_{6},-e_{7})$, they are traceless
anti-Hermitian $3\times3$ matrices: $\mathfrak{su}(3)$, leaving the line
alone. A generic derivation moves $e_{1}$ and mixes the line with the
$\mathbb{C}^{3}$. A random unit vector of that $\mathbb{C}^{3}$ is a colour
superposition, sits in the real octonions with no component on $e_{0}, e_{1}$,
and the exponential of a random $\mathfrak{su}(3)$ derivation, an
automorphism to $10^{-12}$, carries it to another unit vector of the same
$\mathbb{C}^{3}$, Hermitian norm preserved, inner product a phase-carrying
overlap: a colour rotation, not a loss.

So: choosing $e_{1}$ is at once (i) the amplitude's $i$, (ii) the split
$\mathbb{O} = \mathbb{C}\oplus\mathbb{C}^{3}$ into the lepton line and the
colour triplet, and (iii) the selection of $SU(3) = \mathrm{Stab}_{G_{2}}(e_{1})$
as the transformations that are complex-linear for that $i$. The quark's
colour state, a complex superposition of three colours, and the colour force,
the octonions' automorphisms that respect the preferred direction, are the
state side and the symmetry side of one structure on the real algebra. No
complexification enters; the complex numbers of the superposition are the
$e_{1}$-planes of the real octonions. This is the standard fact that the
stabiliser of an imaginary unit in $G_{2}$ is $SU(3)$ acting on
$\mathbb{C}^{3}$, here checked in the corpus convention with its sign
bookkeeping, and it is the algebraic content of the paper's "preferred
direction" doing two jobs at once. STRUCTURAL as mathematics; the reading
that this is why the framework needs no complexification is CANDIDATE.

```
=== Part A: derivations of O ===
dim Der(O) = 14 (expected 14, g_2)

=== Part B: the stabiliser of e_1 ===
dim {D in Der(O): D e_1 = 0} = 8 (expected 8, su(3))
every stabiliser derivation commutes with L_{e_1}: True
C-linear on the colour C^3: True ; anti-Hermitian: True ; traceless: True ; leaves the line (e_0, e_1) alone: True
a generic derivation moves e_1: |D e_1| = 2.267, and mixes the C line with the C^3 (entries D[2:,1] nonzero): True

=== Part C: a colour state is a unit vector of that C^3, and su(3) moves it inside C^3 ===
state as a real octonion: components on e_0, e_1 = 0.0e+00 (none: it lies in the colour C^3); real norm 1.000000
after exp(D): components on e_0, e_1 = 1.1e-15 ; real norm 1.000000 ; Hermitian inner product with the original = 0.431576+0.294534i (a colour rotation, not a loss)
exp(D) is an automorphism: worst |g(xy) - g(x)g(y)| over 200 random pairs = 2.2e-12
```

## 5. Octonionic spacetime, the metric, and the rolled-up-dimension misreading (added 2026-09-27T1600)

JS: "we dismissed the possibility of octonionic spacetime in our spacetime
section. The reason we gave was because octonionic multiplication is
non-associative so you can't form a metric space. But you still have an
algebra, which can be misinterpreted as rolled-up space-like dimensions."

The paper already carries the second half, as the paragraph "The $S^{7}$
sector as internal structure" (spacetime section): lacking associativity the
$S^{7}$ closed curves "support algebra, gauge charge, in place of geometry,
distance"; the Kaluza--Klein and string intuition "is tracking something real
in the $S^{7}$ structure, but misdiagnoses it as spatial"; the resemblance to
rolled-up dimensions "is genuine and instructive". Three precisions on the
first half.

1. *What the reason actually says.* The section does not claim that
   $\mathbb{R}^{8}$ has no metric; it says "the rotation group $SO(8)$ of the
   seven-sphere is of course a group; what fails is the sphere's own
   composition law, the one a ruler would use", and that a distance built by
   composing transports around closed curves is bracket-dependent on $S^{7}$,
   so the triangle inequality is ill-defined for *that* distance. Given the
   framework's definition of distance as loop-counting by composed transport,
   the argument is internally right. The risk is the sentence "the same
   non-associativity forbids a metric outright", which a reader will take as
   the naive claim; one clause, "a metric built from the sphere's own
   composition law", closes it. Proposed for the v2 wording pass.
2. *Octonionic spacetime exists, and the paper knows it.* $SL(2,\mathbb{O})
   \cong \mathrm{Spin}(9,1)$ gives ten-dimensional Minkowski space from the
   Hermitian $2\times2$ octonionic matrices (Kugo--Townsend; Baez--Huerta), and
   the paper cites the correspondence $SL(2,\mathbb{A}) \cong \mathrm{Spin}(1,d+1)$
   with $\mathbb{O}$ giving $9+1$. So the framework did not dismiss octonionic
   spacetime as impossible; it selected $\mathbb{C}$ for the base by the
   computability split and made $\mathbb{O}$ internal. "Ten dimensions" is
   what one gets by not splitting; "three plus one with an octonionic
   register" is what one gets by splitting, and the split is derived (the
   preferred direction), not chosen. The dismissal sentence should be read,
   and perhaps phrased, that way.
3. *The misreading, sharpened by today's computation.* The seven imaginary
   directions of the register are fibre directions, not base directions: six
   of them are the colour $\mathbb{C}^{3}$ on which $\mathrm{Stab}_{G_{2}}(e_{1})
   = SU(3)$ acts (section 4), the seventh is the preferred direction itself.
   Transport along them is by the algebra, bracket-dependent, so they cannot
   be rulers and have no size. A Kaluza--Klein reading gives them a radius,
   which would make colour a geometry with a metric, exactly what
   non-associativity forbids; and the success of the Kaluza--Klein intuition
   is explained by the same fact, since the isometries of an internal algebra
   look like the isometries of an internal space until one asks for a
   distance. One rung up, the sedenions have neither associativity nor a
   norm, so the $S^{15}$ directions are not even a loop: the generation label
   is "internal" in a stronger sense, and no rolled-up reading is available
   for it at all, which is consistent with generations never having been
   mistaken for dimensions.

Labels: (1) and (2) are readings of the paper's own text, STRUCTURAL where
they cite Kugo--Townsend and Baez--Huerta (in the library as
`baez2002octonions`; the others VERIFY-CITE); (3) is CANDIDATE, resting on
section 4 and the framework's definition of distance.

## 6. Spacelike separation is defined on non-causal loops (added 2026-09-27T1700)

JS: "In standard spacetime physics we can add dimensions as we please, and
the fact that if we could communicate between space-like separated observers
we could create a closed timelike loop is an afterthought. In our framework
we defined spacelike separation to mean that if you could set up a CTC
between observers, then they are spacelike separated. Spacelike separation
is defined on non-causal loops."

Confirmed against the text (spacetime section, sec:comp-distance): "The
spacelike distance between two events is then the number of such curves that
would have to be closed to make them causally connected", each curve a
computation whose output is its own input, one non-computable bit, carried by
the imaginary part of the complex information measure. The curves are
counterfactual, closed loops that carry no signal; that is what "non-causal"
means here, and it is why the count is imaginary. Three things follow and
are worth having in one place.

- *The inversion.* Special relativity uses the tachyonic antitelephone as a
  consistency check: superluminal signalling plus a boost would close a
  timelike loop, therefore no superluminal signalling. The framework makes
  the same object constitutive: the loops that would close if a signal ran
  round them are the spacelike loops, and their number is the distance.
  What is an afterthought there is the definition here.
- *Why dimensions cannot be added at will.* A spatial dimension is a family
  of such loops on which transport is consistent and shareable between
  observers, which requires a parallelisable sphere with a group law; $S^{1}$
  and $S^{3}$ qualify, $S^{7}$ is a Moufang loop and does not, and Adams
  forbids anything else. So there are three spatial dimensions as an output,
  and the seventh-sphere loops, which exist but cannot be composed into a
  ruler, are gauge structure: the Kaluza--Klein extra dimension is exactly a
  loop family that failed to be a dimension (section 5).
- *The tie to records.* A non-causal loop is a loop around which no record
  passes; the moment a record does, the loop is causal and its cost is real.
  So spacelike separation is measured by unrecorded loops and timelike
  separation by records (operation count), which is the records thread's
  "duration is a phase, order is a record" seen from the metric side, and it
  is the reason the paper's conjecture that the Minkowski $i$ is the
  amplitude's $i$ (sec:jacobson) is natural: both mark the column in which
  nothing has been written. Hawking's complex temperature for a closed
  timelike curve is the same statement in thermodynamic dress.

Labels: the definition and the dimension count are the paper's (ESTABLISHED
as its stated argument; the metric-space and signature claims are its own
OPEN op:comp-metric); the tie to records is CANDIDATE.


## 6a. Surfacing the inversion in the text (added 2026-09-27T1800)

JS: "people who are used to thinking that tachyonic anti-telephony is an
afterthought of the standard spacetime metric might miss the inversion and
then get confused when we dismiss octonionic spacetime." Agreed, and the
paper as it stood gave them nothing to hold on to: the word "antitelephone"
and the word "tachyon" appeared nowhere, the dismissal in "Three dimensions
of space" was two sentences long, and "forbids a metric outright" read as a
claim about $\mathbb{R}^{8}$. A reader in the standard order takes "you can
add dimensions as you please" as a background fact, so the sentence "$S^{7}$
cannot serve as a ruler" looks to them like a non sequitur (why should the
sphere's own multiplication have anything to do with whether eight
directions carry a metric?), and the dismissal looks like a mistake.

The fix is to state the inversion where the definition is made, in
`sec:comp-distance`, before it is used, and to say in one clause what the
dismissal does and does not deny. Applied, uncommitted, sentinel-gated:
`scripts/patch_spacelike_inversion_2026-09-27T1800.py` on
`paper1/spacetime_from_non-computability.tex`, three edits, backup kept.

1. After "identification is motivated by reproducing what nature does, not
   proved.": a new paragraph. Standard order: metric first, the antitelephone
   a corollary and a check (Tolman 1917; Benford, Book and Newcomb 1970).
   This paper: the loop first; the closed curves that would carry a signal
   round if one could be sent, and carry none, are spacelike separation, and
   the metric is read off from them. The corollary returns as a tautology (a
   loop that carried a record would not be spacelike), so nothing is lost;
   what is gained is that a spatial dimension becomes a definite thing, a
   family of such loops with a bracketing-independent composition law, which
   is a condition a family of loops can fail. Forward pointer to
   `sec:three-dimensions`, and the explicit statement that setting $S^{7}$
   aside as a ruler denies neither the Euclidean metric of $\mathbb{R}^{8}$
   nor the existence of the $SL(2,\mathbb{O})\cong\mathrm{Spin}(9,1)$
   spacetime (Baez 2002); it says the octonionic directions are algebra, not
   distance. Closing sentence: in the standard order that sentence has no
   content; in this one it is the reason space has three dimensions.
2. "forbids a metric outright" becomes "forbids a metric built from the
   sphere's own composition law outright" (the section 5 wording item, now
   done).
3. After "no geodesic structure exists.": a parenthesis saying what is
   untouched (the $\mathbb{R}^{8}$ metric and the ten-dimensional spacetime
   are metrics of the ordinary kind; what fails is a ruler made of loops),
   with a back-pointer to `sec:comp-distance`. This is the other section 5
   wording item.

Two references, batch `bib/tachyonic_antitelephone_refs_2026-09-27T1800.bib`,
keys `tolman1917theory` and `benfordbooknewcomb1970tachyonic`, to import.
Metadata verified this session (Crossref record for the DOI: Phys. Rev. D 2,
263--265, issued 1970-07-15; archive.org catalogue for Tolman: Berkeley,
University of California Press, 1917). Neither text was read, so both are
VERIFY-SUPPORT for the claim cited: the closed-loop argument presented as a
consistency constraint on superluminal signals. Until imported the build
reports the two keys undefined, which is expected. No build was run.

Labels: none change. The paragraph restates the section's own definition
(the paper's stated argument) and the dimension count that follows from it;
op:comp-metric (whether the count is a genuine metric and whether the
signature follows) is untouched and still OPEN. One thing the new paragraph
commits the paper to, which it did not say in so many words before: that
"a spatial dimension" means a loop family with a group composition law.
That is what `sec:three-dimensions` already uses; it is now said where the
reader can see it coming.

What I did not do: rewrite the "Three dimensions of space" paragraph itself
beyond the two clauses. Its argument (Adams; $S^{1}$, $S^{3}$ groups; $S^{7}$
Moufang; $S^{1}$ alone abelian; hence three) is sound as written once the
reader has the inversion; the risk was the missing preamble, not the
paragraph.


## 6b. The antitelephone network: JS's picture, checked, and the patch revised (added 2026-09-27T1900)

JS, on reading 6a: "I like the word 'antitelephone' or the phrase 'tachyonic
anti-telephone' because that immediately leads to the idea of many agents
sending messages to each other via 'tachyonic anti-telephones' and that
requires composition of rotations on parallelisable spheres and that cannot
be done consistently on $S^7$."

Agreed, and the picture is sharper than the "loop family with a composition
law" phrasing of 6a, because it says *whose* composition and *what* fails.
Many observers, each with an antitelephone to each of the others. A message
relayed from one to another through a third is the composition of two
transports; the network is consistent only if a relay composes to a single
transport however the relaying is bracketed. On $S^{1}$ and $S^{3}$ it does
(group law). On $S^{7}$ four things hold, and the patch now says the first
three:

1. *Two links always compose.* Any two octonions generate an associative
   subalgebra (Artin's theorem; a Moufang loop is diassociative). So no
   pairwise experiment, and no relay through one intermediary, can see the
   failure: it needs three independent links, four observers. This is the
   same "three is where it breaks" that runs through the paper's GHZ and
   associator material, here in the metric.
2. *Three links compose exactly when their imaginary parts lie in one
   quaternionic subalgebra.* Harvey--Lawson: a three-plane in $\mathrm{Im}\,
   \mathbb{O}$ is associative iff the associator of a basis vanishes, and the
   associative three-planes are the $\mathrm{Im}\,\mathbb{H}$ of the
   quaternionic subalgebras. Checked numerically below, together with the
   calibration identity $\phi(u,v,w)^{2} + \tfrac14\lvert[u,v,w]\rvert^{2}
   = \lvert u\wedge v\wedge w\rvert^{2}$ (the constant fitted to $0.25$ to
   $10^{-14}$): the network's inconsistency and the calibration defect are
   the same number.
3. *The largest consistent network inside $S^{7}$ is an $S^{3}$.* With two
   links in $H$ and a third anywhere, $[x,y,z]=[x,y,z_{\perp}]$ and
   $\lvert[x,y,z]\rvert = 2\,\lvert\mathrm{Im}\,x\wedge\mathrm{Im}\,y\rvert\,
   \lvert z_{\perp}\rvert$: the network sees the third link exactly through
   its component outside the subalgebra, and every escape is seen. So the
   three-dimensions argument gains a clause it did not have: not only does
   $S^{7}$ fail as a ruler, the largest sub-family of its loops on which
   relays compose is a quaternionic $S^{3}$, and all such choices are one
   $G_{2}$-orbit ($G_{2}/SO(4)$, the space of associative three-planes), so
   no triple is privileged. This is the sentence added to the parenthesis in
   `sec:three-dimensions`.
4. *Rotations.* Left multiplication by a unit octonion is a rotation of
   $\mathbb{R}^{8}$, and $L_{x}L_{y}$ is again a rotation ($SO(8)$ is a
   group), but it is not $L_{xy}$, nor $L_{w}$ for any $w$: the relayed
   rotation is one no single antitelephone induces. Even two quaternionic
   links fail to compose as rotations of all of $\mathbb{R}^{8}$ (they
   compose on $H$); on the quaternions $L_{x}L_{y}=L_{xy}$ exactly. Kept out
   of the paper: the paper's ruler composes links, not induced rotations,
   and the induced-rotation statement would need its own sentence on what
   is being rotated.

Script `scripts/antitelephone_network_associativity_2026-09-27T1900.py`,
Convention A, seed 20260927, numpy only, 22 s. Exact stdout:

```
Antitelephone network associativity, Convention A octonions, seed 20260927
==============================================================================
A. two links always compose (diassociativity)
   max |[u,v,w]| over words in two random links (10 pairs, 16 words each):  5.155e-16
B. three generic links: relay discrepancy |(xy)z - x(yz)|, unit links
   N=2000  min 0.1858  median 1.0930  max 1.9388  (zero would be consistent)
C. three links inside one quaternionic subalgebra
   closure of span{1,a,b,ab} as quaternions (bc=a, ca=b, c imaginary unit): 7.814e-16
   max |[x,y,z]| for x,y,z in H (200 subalgebras):                       4.302e-16
D. Harvey--Lawson calibration identity on Im O
   random imaginary triples: max |phi|/vol = 0.991195  (< 1: none associative)
   fitted c = (vol^2 - phi^2)/|[u,v,w]|^2: min 0.249999999999994  max 0.250000000000002
   quaternionic triples: max | |phi| - vol | = 5.155e-15  (calibration saturated)
E. maximality: two links in H, third link anywhere
   max |[x,y,z] - [x,y,z_perp]|:                         6.120e-16
   max | |[x,y,z]| - 2 |Im x ^ Im y| |z_perp| |:            1.138e-14
   min |[x,y,z]| / |z_perp| over N=2000:                    0.0439  (> 0: every escape from H is seen)
F. rotations: relay L_x L_y against a single link
   L_x L_y orthogonal (max |M^T M - 1|):                  1.498e-15  (a rotation of R^8)
   max |L_x L_y - L_{xy}|, generic octonion links:         3.9974  (not any single link)
   min |L_x L_y - L_{xy}|, both links in one H, on all R^8: 0.0595  (fails off H)
   max |L_x L_y - L_{xy}| on the quaternions (S^3):         4.123e-16
G. control: quaternion rung
   max |[x,y,z]| over N=2000 random unit quaternions:        3.724e-16
==============================================================================
ANTITELEPHONE NETWORK: PASS
```

Labels. Items 1 and 2 are STRUCTURAL (Artin; Harvey--Lawson), verified here
to $10^{-15}$; the calibration identity with $c=1/4$ is ESTABLISHED
numerically in Convention A and STRUCTURAL if it is Harvey--Lawson's (not
read; VERIFY-SUPPORT). Item 3 as a statement about octonions is STRUCTURAL
(it follows from 2). The reading, that a spatial dimension is a family of
antitelephone loops on which relays compose and that this is why the
largest consistent network is three-dimensional, is CANDIDATE: it is the
paper's own three-dimensions argument (already the paper's stated result)
restated in the operational picture, and it stands or falls with the
definition of spacelike separation on non-causal loops (op:comp-metric,
OPEN, untouched).

Patch revised. `scripts/patch_spacelike_inversion_2026-09-27T1800.py` was
rewritten before it was committed (the 6a version was restored from its
.bak and the revised script re-run; same three anchors, same header). The
new paragraph is now two: the inversion (metric first, telephone second
there; telephone first here; the corollary returns as a tautology), then
the network (many observers; consistency is associativity; two links
always compose, citing `conway_2003`; three only in a quaternionic
subalgebra, citing `harvey1982calibrated`; the largest consistent network
in $S^{7}$ is an $S^{3}$; then the "what is not being denied" sentence and
the closing line). The parenthesis in `sec:three-dimensions` says the
failure is not total and names the maximal $S^{3}$. A `%%` comment above
the paragraph carries the VERIFY-SUPPORT for the two library references:
neither the Conway--Smith passage nor Harvey--Lawson ch. IV was read this
session; both statements are verified numerically by the script. Brace and
dollar balance checked; no build run. The batch and the two new keys are
as in 6a.

Proposed for the Opus session: read Conway--Smith for Artin's theorem and
Harvey--Lawson ch. IV for the associative three-plane theorem and the
associator identity, quote the passages into the session note, and clear
the two VERIFY-SUPPORT marks if they hold.
