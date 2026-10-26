# Twistor space and the Hopf maps (2026-10-07)

Session 2026-10-07, Fable 5.1. JS, after the positive-Grassmannian question:
"I'd like to know more about twistor space and the relation to Hopf maps."
From my own knowledge, with every fact that can be computed computed:
`scripts/twistor_hopf_factorisation_2026-10-07T1600.py` (Convention A, seed
20261007, PASS), stdout in section 8. References from memory, six of seven
verified against Crossref (section 7); no text read this session.

## 0. The answer in brief

Twistor space is Penrose's $\mathbb{C}^{4}$, projectivised to
$\mathbb{CP}^{3}$, in which a point of spacetime is a line and a point of
twistor space is a totally null two-plane. In Euclidean signature the
correspondence becomes a fibration (Atiyah, Hitchin and Singer 1978):
$\mathbb{CP}^{3}\to S^{4}$ with fibre $\mathbb{CP}^{1}$, the fibre over a
point being the sphere of complex structures on its tangent space. That
fibration is the quaternionic Hopf map with the complex Hopf map quotiented
out: $S^{7}\to\mathbb{CP}^{3}\to S^{4}$ composes to $S^{7}\to S^{4}$, the
$S^{3}$ fibre of the quaternionic map being itself Hopf-fibred over the
twistor fibre $S^{2}=Sp(1)/U(1)$. So the paper's two-qubit rung is the
twistor arena, exactly, and the twistor fibre is the sphere of choices of
$i$ inside the quaternions, which is the quaternionic step of the ladder
whose octonionic step is colour ($S^{6}=G_{2}/SU(3)$, 2026-09-27). In
two-qubit language, verified: the base $S^{4}$ is the first qubit's reduced
Bloch vector together with the complex concurrence, the $Sp(1)$ fibre is
the second qubit's local unitary group, and the twistor fibre is that
qubit's Bloch sphere of local states modulo its phase. At the octonionic
rung the factorisation fails, verified: the octonionic Hopf map is not
invariant under any $U(1)$ of the form $e^{e_{k}t}$, so there is no
twistor space of $S^{8}$ by this route, which is non-associativity again.
Two things for the paper: the sentence "the $SU(2)$ fibre of $S^{7}\to S^{4}$
carries exactly the entanglement that survives local operations" has fibre
and base the wrong way round; and Penrose's twistor programme is prior art
for the paper's conjecture that the Minkowski $i$ is the amplitude's $i$,
and is not cited.

## 1. Penrose's twistor space [STRUCTURAL, from memory]

Twistor space $\mathbb{T}=\mathbb{C}^{4}$ with coordinates
$Z^{\alpha}=(\omega^{A},\pi_{A'})$, two spinor indices each. The incidence
relation $\omega^{A}=\mathrm{i}\,x^{AA'}\pi_{A'}$ ties a twistor to a point
$x$ of complexified Minkowski space written as a $2\times2$ matrix. For
fixed $x$ the solutions form a two-plane in $\mathbb{C}^{4}$, a projective
line $\mathbb{CP}^{1}\subset\mathbb{PT}=\mathbb{CP}^{3}$; so spacetime
points are lines in projective twistor space, and the space of lines,
$\mathrm{Gr}(2,4)$, is compactified complexified Minkowski space (the
Klein quadric in $\mathbb{CP}^{5}$ under Plücker). This is the first place
the Grassmannian of the previous question enters: $\mathrm{Gr}(2,4)$ is
spacetime, and the amplituhedron's $\mathrm{Gr}(k,k+4)$ generalises it.
Conversely a point of $\mathbb{PT}$ is a totally null two-plane in complex
spacetime; real Minkowski points are the lines lying in the null
hypersurface $\mathbb{PN}$ where the Hermitian form $Z^{\alpha}\bar{Z}_{\alpha}$
vanishes, and a point of $\mathbb{PN}$ is a null ray of real Minkowski
space. The $\mathbb{CP}^{1}$ over a real point is its celestial sphere of
null directions, on which $SL(2,\mathbb{C})$ acts by Möbius maps; that is
the picture the spacetime section already uses (Bloch sphere as celestial
sphere, sec:comp-distance region of the Lorentz paragraph). Penrose's
slogan, that the complex numbers of the celestial sphere and of quantum
amplitudes are one structure, is the paper's "Minkowski $i$ is the
amplitude's $i$" conjecture stated in 1967. Penrose 1967, "Twistor
algebra", J. Math. Phys. 8, 345, Crossref-verified, body not read.

## 2. Euclidean signature: the twistor fibration [STRUCTURAL]

In Euclidean signature the correspondence becomes a fibration. Identify
$\mathbb{C}^{4}=\mathbb{H}^{2}$. A point of $\mathbb{CP}^{3}$ is a complex
line; the quaternionic line it spans is a point of
$\mathbb{HP}^{1}=S^{4}$; the complex lines inside one quaternionic line
form a $\mathbb{CP}^{1}$. So $\mathbb{CP}^{3}\to S^{4}$ with fibre $S^{2}$,
and Atiyah, Hitchin and Singer showed the fibre over $x$ is the sphere of
orthogonal complex structures on $T_{x}S^{4}$ compatible with the
orientation, $SO(4)/U(2)$. The anti-self-dual Yang--Mills equations on
$S^{4}$ become holomorphic bundles on $\mathbb{CP}^{3}$ (Ward 1977), and
the instantons are constructed there (Atiyah, Drinfeld, Hitchin and Manin
1978). The connection on the quaternionic Hopf bundle is itself the basic
instanton (Trautman 1977), which the paper cites through Lévay for the
two-qubit rung; the twistor fibration is where that instanton is a
holomorphic object. All Crossref-verified, none read.

## 3. The factorisation: twistor fibration = quaternionic Hopf map mod the complex one [STRUCTURAL; verified]

$S^{7}\subset\mathbb{H}^{2}$. The quaternionic Hopf map
$h(q_{1},q_{2})=(2q_{1}\bar{q}_{2},\;|q_{1}|^{2}-|q_{2}|^{2})\in\mathbb{H}\times\mathbb{R}$
lands on $S^{4}$ and is invariant under the right action of $Sp(1)$,
$(q_{1},q_{2})\mapsto(q_{1}g,q_{2}g)$, whose orbits are its $S^{3}$ fibres.
The unit complex numbers $U(1)=\{e^{\mathrm{i}t}\}\subset Sp(1)$ act on the
right too, so $h$ is constant on $U(1)$ orbits and descends to
$S^{7}/U(1)=\mathbb{CP}^{3}$; the descended map is the twistor fibration,
with fibre $Sp(1)/U(1)=S^{2}$. Script part A: invariance under right
$Sp(1)$ and right $U(1)$ to $10^{-16}$. One subtlety, which part A also
shows: *left* multiplication by $e^{\mathrm{i}t}$ is not in the fibre; it
rotates the $j$-component of the base point by $2t$ and fixes the rest. So
which $U(1)$ is "the complex Hopf map" depends on which complex structure
on $\mathbb{H}^{2}$ one means, and section 4 says what that is in qubit
terms.

The $S^{3}$ fibre of the quaternionic map is itself Hopf-fibred,
$S^{1}\to S^{3}\to S^{2}$, over the twistor fibre: the tower's first rung
sits inside its second. Script part C: $g\mapsto g\,e_{1}\bar{g}$ is the
Hopf map $S^{3}\to S^{2}$ onto the unit imaginary quaternions, invariant
under $g\mapsto g\,e^{e_{1}t}$, and each image $n$ gives $J=L_{n}$ with
$J^{2}=-1$ and $J$ orthogonal. So the twistor fibre is, concretely, the
sphere of unit imaginary quaternions, each a complex structure on the
quaternionic line: *the sphere of choices of $i$*.

## 4. In two-qubit language [STRUCTURAL as mathematics; verified]

Mosseri and Dandoloff (2001, Crossref-verified, body not read) write
$\psi=\alpha|00\rangle+\beta|01\rangle+\gamma|10\rangle+\delta|11\rangle$
as $(q_{1},q_{2})=(\alpha+\beta j,\;\gamma+\delta j)$ and apply $h$. Script
part B, every clause to $10^{-15}$:

- The base point is $(2\rho_{1}[0,1],\;2(\beta\gamma-\alpha\delta),\;\rho_{1}[0,0]-\rho_{1}[1,1])\in\mathbb{C}\times\mathbb{C}\times\mathbb{R}$:
  the first qubit's reduced Bloch vector $r$, of length
  $\sqrt{1-C^{2}}$, and the concurrence $C=2|\alpha\delta-\beta\gamma|$
  with a phase. $|r|^{2}+C^{2}=1$ is the statement that the point lies on
  $S^{4}$. Separable states have $C=0$ and sit on the $S^{2}$ of unit
  Bloch vectors; maximally entangled states have $r=0$ and sit on the
  circle of concurrence phases.
- The right $Sp(1)$ action is $(1\otimes U)\psi$ with $U\in SU(2)$: the
  fibre is the local unitary group of the *second* qubit.
- The right $U(1)$ is the local $Z$-phase of qubit 2,
  $(\alpha e^{\mathrm{i}t},\beta e^{-\mathrm{i}t},\gamma e^{\mathrm{i}t},\delta e^{-\mathrm{i}t})$,
  not the global phase. It is the global phase of the partially
  conjugated vector $\psi'=(\alpha,\bar{\beta},\gamma,\bar{\delta})$, which
  is what the coordinates of $\mathbb{H}^{2}$ are for the right-$i$
  complex structure. So the twistor $\mathbb{CP}^{3}$ is the projective
  space of $\psi'$, the same manifold as the two-qubit projective space,
  identified through conjugation of the second qubit's $|1\rangle$
  amplitudes. The $Sp(1)$ orbit has dimension 3 modulo the global phase
  of $\psi$ and dimension 2 modulo the right $U(1)$: the twistor fibre.
- The twistor fibre over a base point is therefore the second qubit's
  orbit under its local unitaries modulo its phase: for a separable state,
  its Bloch sphere. And by section 3 that sphere *is* the sphere of
  complex structures on the quaternionic line fixed by the first qubit and
  the concurrence. The second qubit's Bloch sphere is the sphere of
  choices of $i$.

Correction owed to the paper (second-order, on an existing sentence).
`sec:hopf-compositional` says "At two qubits, the $SU(2)$ fibre of
$S^{7}\to S^{4}$ carries exactly the entanglement that survives local
operations". The fibre is the local operations; the entanglement is what
the projection to the base preserves. Proposed wording: "At two qubits,
the $Sp(1)$ fibre of $S^{7}\to S^{4}$ is the local unitary freedom of one
qubit, and the base $S^{4}$ carries exactly what survives it: the other
qubit's reduced Bloch vector and the concurrence, which fill the base as
$|r|^{2}+C^{2}=1$ \autocite{mosseri2001hopf}". Mosseri--Dandoloff is the
citation already there; VERIFY-SUPPORT that their conventions match
(they do by the computation, but the text was not read).

## 5. The ladder of choices of $i$ [STRUCTURAL as arithmetic; the reading RHYME]

Script part E. At each rung the sphere of complex structures is the unit
sphere of the imaginary part of the algebra, and the stabiliser of a
choice is the symmetry that survives it:

| rung | sphere of choices of $i$ | stabiliser | where it appears |
|---|---|---|---|
| $\mathbb{C}$ | $S^{0}=\{\pm i\}$ | trivial | Galois conjugation; the anti-event; Burton--Anwar's "which $i$?" |
| $\mathbb{H}$ | $S^{2}=Sp(1)/U(1)$ | $U(1)$ | the twistor fibre; the second qubit's Bloch sphere |
| $\mathbb{O}$ | $S^{6}=G_{2}/SU(3)$ | $SU(3)$ | colour, the complexified-vs-complex-structure note, section 4 |

$S^{0}$, $S^{2}$ and $S^{6}$ are the three spheres that carry an almost
complex structure from the algebra, which is the known fact that only
$S^{2}$ and $S^{6}$ (and trivially $S^{0}$) are almost complex among
spheres. The reading, that the paper's recurring "choice of $i$" is one
object seen at three rungs, with twistor theory being its quaternionic
case, is a RHYME until something is computed with it; the arithmetic is
exact.

## 6. The octonionic rung has no twistor space by this route [STRUCTURAL; verified]

Script part D. The octonionic Hopf map $h(a,b)=(2a\bar{b},|a|^{2}-|b|^{2})$
on $S^{15}\subset\mathbb{O}^{2}$ lands on $S^{8}$, but for every unit
imaginary $e_{k}$ and both right and left multiplication,
$h(a e^{e_{k}t},b e^{e_{k}t})$ differs from $h(a,b)$ by order one, while
it agrees to $10^{-16}$ when $a$, $b$ and $e_{k}$ lie in one quaternionic
subalgebra. So no $U(1)$ of the form the complex Hopf map uses lies in
the fibres, the octonionic Hopf map does not descend to $\mathbb{CP}^{7}$,
and there is no "twistor space of $S^{8}$" as a quotient of the three-qubit
sphere. The reason is the one the paper gives for everything at this rung:
the fibre $S^{7}$ is not a group and the fibres are not orbits. Whether
$\mathbb{CP}^{7}$ fibres over $S^{8}$ by some other map is a topological
question I have not settled and do not claim. For the framework this is
consistent with the spacetime section: the quaternionic rung gives a
spacetime ($S^{4}$, the twistor base, the Euclidean form of the
$SL(2,\mathbb{C})$ story), the octonionic rung gives algebra and not
geometry.

## 7. References and what the paper owes

In the library and cited: `mosseri2001hopf`, `levay2004geometry`,
`baez2002octonions`. New batch `bib/twistor_refs_2026-10-07T1700.bib`:
Penrose 1967 (J. Math. Phys. 8, 345--366), Atiyah--Hitchin--Singer 1978
(Proc. R. Soc. A 362, 425--461), Ward 1977 (Phys. Lett. A 61, 81--82),
Atiyah--Hitchin--Drinfeld--Manin 1978 (Phys. Lett. A 65, 185--187), Trautman
1977 (Int. J. Theor. Phys. 16, 561--565), all Crossref-verified 2026-10-07;
Penrose and MacCallum 1973 (Phys. Rep. 6, 241) VERIFY-CITE, Crossref did not
return it. No text read; all VERIFY-SUPPORT for the one-line claims above.

Owed: (i) the fibre/base sentence (section 4); (ii) one sentence in the
spacetime section, where the Minkowski-$i$ conjecture is stated, crediting
Penrose's twistor programme as its prior statement and the twistor
fibration as the Euclidean form of the celestial-sphere picture; (iii)
optionally, in `sec:hopf-compositional`, that the two-qubit rung's bundle
is the twistor fibration and Lévay's instanton is Trautman's, with Ward's
correspondence as where it becomes holomorphic. All for JS to rule; no
patch drafted, since the question was a question.

## 8. Exact stdout of `scripts/twistor_hopf_factorisation_2026-10-07T1600.py`

```
Twistor space and the Hopf maps, Convention A, seed 20261007
==============================================================================
A. quaternionic Hopf map: right Sp(1) is the fibre, right U(1) inside it, left U(1) is not
   lands on S^4 (max | |h|-1 |):                       5.6e-16
   invariant under right Sp(1):                        4.9e-16
   invariant under right U(1) = e^{i t}:               3.9e-16   -> descends to S^7/U(1) = CP^3
   left e^{i t}: (1,i,real) parts fixed 5.6e-16, j-part rotated by exactly 2t (err 3.0e-16): NOT in the fibre
B. two-qubit dictionary
   base = (qubit-1 Bloch vector r, complex concurrence), |r|^2 + C^2 = 1:  max err 1.1e-15
   separable states: C = 0 and the base lies on the unit-Bloch S^2 in S^4:  max err 6.7e-16
   right Sp(1) on (q1,q2) equals a local SU(2) on qubit 2 (1 (x) U):       max err 7.9e-17
   right U(1) orbit of psi = global phase of psi' = (alpha, conj beta, gamma, conj delta): max err 7.9e-17
   Sp(1)-orbit dimension mod global phase of psi: [3]; mod right U(1) (= phase of psi'): [2]  -> twistor fibre S^2
C. the twistor fibre as the sphere of complex structures on H
   g -> g e1 conj(g): unit imaginary, invariant under g -> g e^{e1 t} (Hopf S^3 -> S^2): max err 4.9e-16
   each image n gives J = L_n with J^2 = -1, J orthogonal (a complex structure):         max err 1.7e-15
D. octonionic Hopf map: no factorisation through the complex Hopf map
   lands on S^8 (max | |h|-1 |):                                   4.4e-16
   right e^{e_k t}, k=1..7, max |h(a u, b u) - h(a, b)|:            [1.735 1.836 1.831 1.659 1.769 1.882 1.827]
   left  e^{e_k t}, k=1..7, max |h(u a, u b) - h(a, b)|:            [1.958 1.974 1.966 1.96  1.959 1.973 1.966]
   same, with a, b, e_1 in one quaternionic subalgebra:             4.5e-16  (associative: invariant)
E. the ladder of spheres of complex structures
   unit sphere of Im C: S^0 ; stabiliser of a point {1}            dim 0 ; check dim(group) - dim(stab) = 0
   unit sphere of Im H: S^2 ; stabiliser of a point U(1) in Sp(1)  dim 1 ; check dim(group) - dim(stab) = 2
   unit sphere of Im O: S^6 ; stabiliser of a point SU(3) in G2    dim 8 ; check dim(group) - dim(stab) = 6
==============================================================================
TWISTOR HOPF: PASS
```


## 9. Chirality: the two Hopf fibrations, Filatov's inversion and the partial transpose (added 2026-10-07T1900)

JS: "From what little I know about twistors I gather that they're
inherently chiral, so when I see 'twistor factorisation of the quaternionic
Hopf map' I immediately think of Filatov's paper showing how a Bell state
can be decomposed into two Bloch spheres where one is the inversion of the
other." The paper already uses Filatov and Auzinsh (`filatov2024towards`,
in the library) in `sec:frame`: the handedness bit $\chi\in\{L,R\}$ is the
"Filatov datum", the two spheres of an entangled pair are forced
opposite-handed, $K_{3}$ is not two-colourable, and `op:filatov-extension`
and `op:chirality` rest on it. The text calls the opposite-handedness "a
topological fact about the quaternionic Hopf fibration, not a drawing
convention" without saying which fact. Here is which fact, computed:
`scripts/twistor_chirality_filatov_2026-10-07T1900.py` (seed 20261007,
PASS), stdout below.

*Twistors are chiral, and the chirality is left versus right.* On
$\mathbb{H}=\mathbb{R}^{4}$ the two commuting actions of $Sp(1)$, left
and right multiplication, are the two factors of
$\mathrm{Spin}(4)=Sp(1)_{L}\times Sp(1)_{R}$, and for the orientation
$(1,i,j,k)$ the three left multiplications are self-dual two-forms and the
three right multiplications anti-self-dual (part A). The twistor fibre over
a point is the sphere of complex structures compatible with an
orientation, which is the unit sphere of one chirality; the fibre of the
right Hopf fibration at the base point $[1:0]$ is the sphere of left
multiplications $L_{n}$ (section 3), the self-dual ones. The other
fibration, with fibres the left $Sp(1)$ orbits, has fibre the right
multiplications, anti-self-dual. The two Hopf fibrations of $S^{7}$ are
the twistor space and the dual twistor space of $S^{4}$. STRUCTURAL,
verified.

*In two-qubit language the two chiralities are unitary and antiunitary.*
Part B, exact: with the standard complex structure, the right $Sp(1)$ is
$(1\otimes U)$, the unitary local group of qubit 2; the left $Sp(1)$ is
generated by left $i$, which is the global phase, and left $j$, which is
$(1\otimes(-\mathrm{i}\sigma_{y}K))$, the antiunitary spin flip of qubit 2
acting on the whole vector. So the chirality of the fibration one builds
is the choice between the unitary local group and the group generated by
the phase and the spin flip; and the two fibrations are exchanged by
partially conjugating one qubit (part C: $h_{R}(\psi')$ is $h_{L}(\psi)$ up
to a fixed rotation of $S^{4}$). Partial conjugation of one subsystem is
the operation Wigner's theorem forbids as a symmetry, and the Peres
partial transpose is its action on density matrices.

*Filatov's inversion is $\det T=-C^{2}$.* Part D. For a pure two-qubit
state with correlation matrix $T_{ij}=\langle\sigma_{i}\otimes\sigma_{j}\rangle$,
the map from qubit 1's measurement axis to qubit 2's conditional Bloch
vector has $\det T=-C^{2}$, $C$ the concurrence. It is orientation-reversing
for every entangled pure state, not only for Bell states, and its
strength is $C^{2}$. For the four Bell states $\det T=-1$: the singlet has
$T=-1$, the second sphere the inversion of the first; the other three
have one axis reflected after a rotation, which is the "odd number of
axes inverted" of Filatov and Auzinsh. The antiunitary spin flip sends
$r\to-r$, the same inversion, so the inverted second sphere is the
first sphere seen through the antiunitary chirality. Part E: the spin
flip of qubit 2 on the right Hopf base reflects qubit 1's Bloch vector in
the $y$ axis (it conjugates everything) and conjugates the concurrence
phase, both orientation-reversing. STRUCTURAL, verified.

*The constraint is the partial-transpose criterion.* Part F. Reversing
the chirality by hand, the partial transpose on qubit 2, gives
$\det T^{\Gamma}=+C^{2}$ and an operator with smallest eigenvalue $-C/2$:
not a state, for every entangled pure state. The same-handed tensor
$T=+1$, a second sphere that is a copy of the first at full correlation,
has eigenvalue $-\tfrac12$ and is not a state; the inverted tensor
$T=-1$ is the singlet. So Filatov's opposite-handedness is Peres and
the Horodeckis' criterion seen on the Bloch spheres: an entangled pair
*must* be opposite-handed because the same-handed version is the partial
transpose, which positivity forbids. For two qubits the criterion is
necessary and sufficient, so the handedness bit is entanglement itself.
STRUCTURAL as mathematics (Peres 1996; Horodecki, Horodecki and Horodecki
1996; Wootters 1998 for $C$; batch written, Crossref-verified, texts not
read).

*What this gives the paper.* Three things, for JS to rule.

1. `sec:frame` can say which topological fact: the two spheres of a pair
   are the two chiralities of the quaternionic Hopf fibration, twistor and
   dual twistor, exchanged by the antiunitary spin flip of one qubit; an
   entangled pair is forced opposite-handed because the same-handed
   assignment is the partial transpose and is not a state. One sentence,
   citing `filatov2024towards` and the Peres--Horodecki batch.
2. The Filatov datum has a strength: $|\det T|=C^{2}$. For the W-class
   lepton register the pairwise concurrences are what they are (the
   marginal spectrum $(\tfrac23,\tfrac13)$ of `prop:w-doublet`); the
   handedness bit of each edge therefore carries a number as well as a
   sign, which `op:filatov-extension` could use. CANDIDATE.
3. For `op:chirality`: the left-versus-right choice is made the moment one
   chooses a complex structure on $\mathbb{H}^{2}$, since "unitary" and
   "antiunitary" are defined relative to it, and the paper's complex
   structure is the amplitude's $i$ (lem:cproj, the 2026-09-27 note). So
   the weak doublet's handedness and the twistor chirality are both
   fixed by the same choice of $i$. Whether that selects $SU(2)_{L}$ rather
   than $SU(2)_{R}$ is exactly `op:chirality` and is not settled here;
   what is settled is that the chirality is a consequence of the complex
   structure, not an extra datum. CANDIDATE.

Fence: the octonionic rung has no such pair of fibrations (section 6),
so the extension of the handedness structure to three spheres, which is
`op:filatov-extension`, cannot be read off from twistor theory; it needs
the three quaternionic subalgebras of a triple, which is the
`sec:three-dimensions` picture of the antitelephone note (2026-09-27, 6b).
That is a pointer, not a proof.

### Exact stdout of `scripts/twistor_chirality_filatov_2026-10-07T1900.py`

```
Twistor chirality and Filatov's inversion, Convention A, seed 20261007
================================================================================
A. chirality of Spin(4): left and right multiplications as (anti-)self-dual 2-forms, orientation (1,i,j,k)
   left  multiplications by i, j, k: *w = +1 w  (all three)
   right multiplications by i, j, k: *w = -1 w  (all three)
   opposite chiralities: yes
B. the two Sp(1) actions on H^2 = two qubits
   right Sp(1) = (1 (x) U) psi, U in SU(2), unitary on qubit 2:              max err 0.0e+00
   left  e^{i t} = global phase e^{i t} psi:                                  max err 0.0e+00
   left  j = (1 (x) (-i sigma_y K)) psi, the antiunitary spin flip of qubit 2: max err 0.0e+00
C. the two Hopf maps
   h_L invariant under left Sp(1):                                   6.2e-16
   h_L constant on global-phase orbits (descends to the two-qubit CP^3): 4.1e-16
   h_R moved by the global phase (max over sample):                   1.921  (it descends to CP^3 of psi' instead)
   h_R(psi') = D h_L(psi) with D = diag(1,-1,-1,1,1), det D = +1 (a rotation of S^4): max err 0.0e+00
D. correlation matrix T_ij = <sigma_i (x) sigma_j>: det T = -C^2
   random pure states, max |det T + C^2|:                               6.7e-16
   Phi+ T = diag(1, -1, 1)  det -1  (second sphere = reflection in one axis after a rotation of the first)
   Phi- T = diag(-1, 1, 1)  det -1  (second sphere = reflection in one axis after a rotation of the first)
   Psi+ T = diag(1, 1, -1)  det -1  (second sphere = reflection in one axis after a rotation of the first)
   Psi- T = diag(-1, -1, -1)  det -1  (second sphere = inversion of the first)
   the spin flip -i sigma_y K sends the Bloch vector r -> -r (inversion):      max err 0.0e+00
E. the spin flip of qubit 2 (left j, antiunitary) on the right Hopf base (r_1, C e^{i phi}, r_z)
   qubit 1: r_y -> -r_y (the K alone, a reflection); concurrence phase phi -> -phi; qubit 2: r -> -r:  max err 2.2e-16
F. the opposite chirality is the partial transpose, and it is not a state
   det T^Gamma = +C^2 (chirality reversed):                                    max err 4.4e-16
   min eigenvalue of rho^Gamma = -C/2 (negative for every entangled pure state): max err 5.6e-16
   the 'same-handed' tensor T = +1 (second sphere a copy of the first): min eigenvalue -0.50, not a state
   the inverted tensor T = -1 (the singlet):                            min eigenvalue 0.00, a state
================================================================================
TWISTOR CHIRALITY / FILATOV: PASS
```


## 9a. The W triangle: three chiral edges and a $\mathbb{Z}_{2}$ holonomy (added 2026-10-07T2100)

JS, on the fence at the end of section 9: "Yes we know that one case GHZ
does not have pairs of fibrations, but the W case does have 3 pairs, the
quaternionic subalgebras of a triple." Agreed, and the chirality of
section 9 can be put on the three edges of the register directly, because
$\det T$ and the partial transpose are defined for the *mixed* pair states
that the three-qubit reductions are, where the pure-state Hopf map is not.
Script `scripts/w_triangle_chirality_holonomy_2026-10-07T2100.py` (seed
20261007, PASS), stdout below.

*Canonical W.* Every edge has correlation matrix
$T=\mathrm{diag}(\tfrac23,\tfrac23,-\tfrac13)$, so $\det T=-4/27$: improper,
the map from one sphere's axis to the other's conditional Bloch vector
reverses orientation on all three edges. Each edge has Wootters
concurrence $2/3$ and partial transpose with smallest eigenvalue
$(1-\sqrt5)/6=-0.206$: entangled, by the two-qubit criterion that is
necessary and sufficient. The $\mathbb{Z}_{2}$ holonomy round the
triangle, the sign of $\det T_{AB}\det T_{BC}\det T_{CA}$, is $-1$. That is
the paper's frustration made a number: a handedness bit per sphere with
$\chi_{X}\neq\chi_{Y}$ on every improper edge has no solution on $K_{3}$
(part D enumerates the eight assignments and finds none), and the
obstruction is exactly the product of the three edge signs, a
$\mathbb{Z}_{2}$ holonomy like the twist of a Möbius band. The marginal
spectrum $(\tfrac23,\tfrac13)$ of `prop:w-doublet` sits beside it.

*Canonical GHZ.* Every edge has $T=\mathrm{diag}(0,0,1)$, $\det T=0$,
concurrence $0$, partial transpose positive. No edge carries a chirality
and the holonomy is undefined ($0$): the three spheres are unconstrained
by the state, which is the frame section's "a quark's electroweak identity
is written nowhere in its local state", now as arithmetic. The
$\mathbb{Z}_{3}$ of the GHZ register must come from the fibre
(`sec:charges`), not from the edges, exactly as the paper routes it.

*Local unitaries* leave $\det T$, $C$ and the holonomy invariant on both
(part B), so the statements are about the LU orbits of the canonical
representatives, which the paper calls the physical configurations.

*Off the canonical orbit the dichotomy does not survive*, and this is the
honest finding (part C). Under random invertible local maps, a quarter of
W-class images have an edge with $\det T>0$ while all three partial
transposes stay negative: an entangled mixed pair with a *proper*
correlation map. And generic GHZ-class images have all three edges
entangled (partial transposes negative in 300 of 300) and improper in most
cases. So the sign of $\det T$ is neither an SLOCC invariant nor an
entanglement witness for mixed pairs; it is a pure-state theorem
($\det T=-C^{2}$, section 9) and a canonical-orbit fact. Two consequences:

1. The frame section's "an entangled pair of qubits forces the two
   spheres' frames to be opposite-handed", citing Filatov, holds for pure
   pairs and for the canonical W register's mixed pairs, not for every
   entangled mixed pair. The sentence needs "pure, or on the canonical
   orbit" or a footnote. Second-order on `filatov2024towards`, whose
   theorem is for pure two-qubit states (its title says so; text not
   read).
2. The paper's choice to treat the canonical (special and anti-special
   Frobenius) orbits as the physical configurations and the SLOCC
   deformations as unphysical (`sec:entanglement-classes`, map--state
   duality paragraph) is what makes the edge chirality a class property.
   The handedness dichotomy is therefore a consequence of that choice, not
   independent support for it. Worth saying, since the frame section
   reads as if the dichotomy were a theorem about the classes.

*The three quaternionic subalgebras of a triple.* JS's phrase is the
right one and I do not yet have the computation that earns it. The three
edges of the W register are three two-qubit systems, each with its own
pair of Hopf fibrations (twistor and dual twistor, section 9), and the
three cannot be given a common complex-structure convention, which is the
holonomy. In the octonionic picture of the antitelephone note (2026-09-27,
6b) three links compose consistently only when their three pairwise
quaternionic subalgebras coincide, and a triple whose three pairs generate
three *different* quaternionic subalgebras is exactly a non-associative
triple. The W triangle's holonomy $-1$ and the associator of such a
triple are two measures of "three pairs with no common frame", and
whether they are the same measure is the content of
`op:filatov-extension`. Pointer, not proof; RHYME until computed.

Proposed ledger entries (JS to approve):

- **ESTABLISHED** (arithmetic) On the canonical W register every edge has
  $\det T=-4/27$, concurrence $2/3$, negative partial transpose, and the
  $\mathbb{Z}_{2}$ holonomy of edge chiralities round the triangle is $-1$;
  on the canonical GHZ register every edge has $\det T=0$ and no chirality.
  Invariant under local unitaries; not under SLOCC.
- **CANDIDATE** The frame section's $K_{3}$ frustration is this holonomy;
  the Filatov datum per edge has sign $-1$ and strength $|\det T|=4/27$
  on the W register.
- *Precision owed:* Filatov's opposite-handedness is a pure-state theorem
  and holds on the canonical orbit; it is not a property of every
  entangled mixed pair. Wording item for `sec:frame`.

### Exact stdout of `scripts/w_triangle_chirality_holonomy_2026-10-07T2100.py`

```
W triangle chirality and holonomy, seed 20261007
========================================================================================
A. canonical representatives
   W   three-tangle 0.000, marginal spectrum [0.6667 0.3333]
       edge AB: diag T = [ 0.6667  0.6667 -0.3333]  det T = -0.1481  C = 0.6667  min eig(rho^Gamma) = -0.2060
       edge BC: diag T = [ 0.6667  0.6667 -0.3333]  det T = -0.1481  C = 0.6667  min eig(rho^Gamma) = -0.2060
       edge CA: diag T = [ 0.6667  0.6667 -0.3333]  det T = -0.1481  C = 0.6667  min eig(rho^Gamma) = -0.2060
       Z_2 holonomy sign(det T_AB det T_BC det T_CA) = -1
   GHZ three-tangle 1.000, marginal spectrum [0.5 0.5]
       edge AB: diag T = [0. 0. 1.]  det T = +0.0000  C = 0.0000  min eig(rho^Gamma) = +0.0000
       edge BC: diag T = [0. 0. 1.]  det T = +0.0000  C = 0.0000  min eig(rho^Gamma) = +0.0000
       edge CA: diag T = [0. 0. 1.]  det T = +0.0000  C = 0.0000  min eig(rho^Gamma) = +0.0000
       Z_2 holonomy sign(det T_AB det T_BC det T_CA) = +0
   W edge exactly: det T = -4/27 = -0.1481; min eig(rho^Gamma) = (1 - sqrt5)/6 = -0.2060
B. local unitaries (300 random SU(2)^3): invariance of det T, C, and holonomy
   W   max change in (det T, C) over edges: 2.0e-08; holonomies seen: [-1]
   GHZ max change in (det T, C) over edges: 1.5e-16; holonomies seen: [0]
C. random SLOCC images (300 random GL(2,C)^3, normalised): off the canonical orbit
   W   three-tangle range [0.000, 0.000]; holonomy counts {-1: 226, 0: 1, 1: 73}; {'all three edges improper (det<0)': 227, 'some edge det>0': 73, 'some edge det=0': 0}; all three partial transposes negative: 300/300
   GHZ three-tangle range [0.000, 0.584]; holonomy counts {-1: 259, 0: 1, 1: 40}; {'all three edges improper (det<0)': 260, 'some edge det>0': 40, 'some edge det=0': 0}; all three partial transposes negative: 300/300
D. the frustration as a Z_2 holonomy
   handedness assignments chi in {L,R}^3 with chi_X != chi_Y on all three edges: 0  (K_3 not two-colourable)
   obstruction = product of edge signs: W gives (-1)^3 = -1 (frustrated); GHZ gives 0 (no constraint on any edge)
========================================================================================
W TRIANGLE: PASS
```


## 9b. Did Filatov and Auzinsh see the Hopf or twistor structure? Read, 2026-10-07T2330

JS: "I don't think Filatov picked up on that in his 2024 paper." Checked
against the texts, both read from the arXiv PDFs this session
(`2403.10587`, 37 pages, the Entropy paper; `2406.05174v3`, 10 pages, the
stabiliser follow-up).

*The 2024 paper (`filatov2024towards`).* The words twistor, Hopf,
fibration, quaternion, Penrose, self-dual, chiral, partial transpose and
Peres do not occur. Mosseri and Dandoloff are not cited. The handedness is
found empirically: "the key element for constructing the representation of
entangled states did not originate from GA. Instead, it emerged through
the process of rewriting the four Bell basis states in all three conjugate
bases", after which the rule is that aligned arrows in a basis give
aligned axes and anti-aligned give inverted, so that "odd number of
coordinate axes is always inverted on the second BS" (Fig. 4 caption), and
"it is impossible to go from right- to left-handed coordinates by rotation
of axes only". That is $\det T=-1$ for the Bell states, observed basis by
basis, with no theorem behind it and no statement for general entangled
pairs. The one fibration remark is second-hand: they cite Uskov and Rau
2008 for "an extension of the Bloch sphere to two qubits involving a
four-sphere at each point of which is a fiber consisting of two
two-spheres of SU(2)", which is the quaternionic Hopf base $S^{4}$ with
its fibre described loosely, and they do not use it. Their entanglement
measure is "the surface area of the sphere enclosing the state", not the
concurrence as a base coordinate.

*The follow-up (`2406.05174`, not in the library).* The introduction lists
"examination of fibrations" among prior approaches and cites Mosseri and
Dandoloff 2001, Bernevig and Chen 2003, Mosseri 2006 and Uskov and Rau in
one bracket, then moves on; the body derives the two-sphere picture from
the stabiliser group of the state. No twistor, no quaternion, no
chirality as such.

So JS is right: neither paper connects the opposite handedness to the
quaternionic Hopf fibration, to its two chiralities, to twistor space, or
to the partial-transpose criterion. The paper's sentence in `sec:frame`,
"this opposite-handedness, the Filatov constraint, is a topological fact
about the quaternionic Hopf fibration, not a drawing convention", is
therefore the paper's own claim, with Filatov cited for the observation
and not for the fact, and section 9 of this note is the first place the
fact is written down and computed. Two consequences:

1. The citation is honest as it stands (Filatov and Auzinsh did observe
   the handedness), but the sentence should not read as though the
   topological fact were theirs. One clause: "observed by Filatov and
   Auzinsh for the Bell states and read here as ...".
2. The content of section 9 (two Hopf fibrations as twistor and dual
   twistor, unitary versus antiunitary fibre, $\det T=-C^{2}$, the
   partial-transpose reading) is, as far as these two papers and the
   library show, unpublished. If it goes in the paper it should be
   stated as the paper's, with Mosseri and Dandoloff, Atiyah--Hitchin--Singer
   and Peres--Horodecki as the components. Whether someone else has put
   the components together is not checked beyond these two papers and
   the library; a search would be owed before claiming priority in print.

Reference for the follow-up, from the arXiv PDF header and Crossref-free:
Filatov, S. and Auzinsh, M., "Entanglement on Two Bloch Spheres: Exploring
Two-Qubit Stabilizer Group Structure", arXiv:2406.05174v3, 1 November
2024; batch not written since nothing in the paper cites it yet.


## 9c. Literature search: has anyone linked Bell-state handedness to twistors? (2026-10-07, later)

JS: "Do a literature search for anyone linking Bell-state handedness to
twistors." Ten web searches, nine papers downloaded and read in part
(term counts and the relevant passages; none read in full except as
quoted), DOIs Crossref-verified where given. The short answer: no one
has made the link. The longer answer is that each half of section 9 has
an owner, and the two halves have never been joined.

### The handedness half: who has det T < 0, and since when

- **Altepeter, Jeffrey, Medic and Kumar 2009**, "Multiple-Qubit Quantum
  State Visualization", CLEO/IQEC 2009 paper IWC1 (from James's reference
  list; not located, VERIFY-CITE). James credits Altepeter as "the first
  to point out a connection between chirality of Bloch vector
  representations and entanglement". Altepeter's 2006 Illinois thesis
  was downloaded and contains no handedness or chirality language (the
  word "mirror" occurs only for optical mirrors), so the observation
  postdates it.
- **James 2022**, "Quantum kinematics in terms of observable quantities and
  the chirality of entangled two-qubit states", J. Opt. Soc. Am. A 39,
  C86 (Crossref-verified). Defines the *sinisterness* $S=\det c_{ij}$ of
  the correlation matrix, notes that the two singular-vector frames have
  opposite chirality for entangled states and that an improper
  transformation turns a right-handed basis into a left-handed one;
  mentions the partial transpose and Peres, and the spin-flipped state in
  an appendix on concurrence. No Hopf fibration, no twistor, no
  quaternion.
- **Gamel 2016**, "Entangled Bloch spheres: Bloch matrix and two-qubit
  state space", Phys. Rev. A 93, 062320 (Crossref-verified). Defines the
  *correlation orientation* $d=\det M\det N=\mathrm{sgn}\det R$ of the
  singular value decomposition of the correlation matrix, shows that
  maximally entangled states have "an opposite handedness in each Bloch
  sphere", and, the part closest to section 9, shows that the partial
  transpose acts as a reflection $Q_{t}=\mathrm{diag}(1,-1,1)$ on one
  Bloch frame and so "flips the orientation $d\to-d$", interpreting the
  Peres--Horodecki criterion "as a reflection, or a change of a single
  sign". This is the partial-transpose-reverses-chirality statement of
  section 9, part F, published ten years earlier in the Bloch-matrix
  language. No Hopf fibration beyond one citation of Mosseri, no twistor.
- **Avron and Kenneth 2009**, "Entanglement and the geometry of two
  qubits", Ann. Phys. 324, 470 (Crossref-verified). Minkowski-signature
  language for two qubits: local $SL(2,\mathbb{C})\otimes SL(2,\mathbb{C})$
  as Lorentz transformations, a "tilde map" $\tilde A=(\sigma_{3}\otimes\sigma_{3})A^{t}(\sigma_{3}\otimes\sigma_{3})$
  which "acts on the Pauli spin matrices as spin-flip", *self-dual*
  operators $W=\tilde W$ (time-reversal invariant; the Bell projections
  are self-dual) and *anti-self-dual* ones (the Lie algebra of the local
  group), and the Peres test as "the reflection about the
  $\sigma_{3}^{\otimes2}$ axis" of the tetrahedron of Bell-diagonal
  states. So the words self-dual and anti-self-dual, time reversal, spin
  flip and the partial transpose as a reflection are all in one paper,
  but as a duality under the spin-flip on operators, not as the
  Hodge duality of two-forms on $S^{4}$ that section 9 part A uses, and
  with no Hopf fibration or twistor space.
- **Filatov and Auzinsh, June 2026**, "Roto-Reflection Geometry of Pure
  Two-Qubit Entanglement", arXiv:2606.12637 (10 June 2026). States
  $\det T=-C^{2}$ as their eq. (33) and $C=\sqrt{-\det T}$, shows every
  maximally entangled state's correlation tensor is an improper
  orthogonal map, a roto-reflection, whose "orientation-reversing
  character survives arbitrary local rotations", and defines an
  "Entanglement Roto-Reflection Plane". This is section 9 part D
  exactly, four months before I computed it, and it supersedes the
  ledger line that proposed $\det T=-C^{2}$ as the paper's: it is theirs
  (or earlier: Gamel's $d=\mathrm{sgn}\det R$ with the pure-state
  determinant is implicit in 2016; the explicit equality I found first
  here). Mosseri is cited once in passing; no twistor, no partial
  transpose, no antiunitary.

### The twistor half: who has twistors with two qubits

- **Lévay 2005**, "Geometry of three-qubit entanglement", Phys. Rev. A 71,
  012334 (arXiv title "The twistor geometry of three-qubit entanglement";
  Crossref-verified). Three qubits as points of the Klein quadric, with
  $\alpha$- and $\beta$-planes (self-dual and anti-self-dual bivectors) and
  "subspaces of this form are called $\beta$-planes in twistor theory".
  Three qubits, not two, and no handedness of Bell states.
- **Lévay 2004** (`levay2004geometry`, in the library): the quaternionic
  Hopf bundle, its instanton connection "with self-dual curvature".
  Self-duality of the connection, not a chirality of states.
- **Chin and Lee 2014**, "Momentum bispinor, two-qubit entanglement and
  twistor space", arXiv:1407.2492 (SNUTP-14-007; no journal found). The
  closest prior work to the framework's reading. The two-qubit reduced
  density matrix is a massive momentum bispinor; concurrence is mass,
  $\det A=\mu=me^{\mathrm{i}\psi}$ the complex mass; the local
  $SU(2)\times SU(2)$ is "$SU(2)_{R}$ (gauge) $\times SU(2)_{L}$
  (rotation)", one acting on the Hopf fibre and the other on the base;
  the Hopf base is $S^{4}\simeq B^{3}\times S^{1}/\mathbb{Z}_{2}$ with
  separable states the boundary of the ball (massless momenta); then a
  momentum-twistor construction with the incidence relation, and a
  tachyonic (imaginary-mass) sector. They cite Mosseri--Dandoloff and
  Lévay for the Hopf geometry. They have the left/right split as gauge
  versus rotation and the twistor space, but say nothing about
  handedness of correlations, Bell states, the partial transpose or the
  antiunitary fibre.
- **Szangolies 2025** (`szangolies2025standardmodel`, already credited in
  the paper): the entangled two-qubit state as a left- and a
  right-handed Weyl spinor, with the chirality of the weak interaction
  read from it. Chirality of spinors, not of Bloch-sphere frames, and no
  twistor.
- **Orion and Akkermans 2025**, "Topological tenfold classification and
  the entanglement of two qubits", Phys. Rev. B 111, 245408
  (Crossref-verified): the antiunitary time-reversal operator identifies
  concurrence and separates entangling from non-entangling operators via
  the Cartan decomposition. The antiunitary-is-the-entanglement-chirality
  theme, in the tenfold-way language; no Hopf, no twistor.
- Also read and found silent: Najarbashi et al. 2007 (quaternionic
  conformal maps, J. Phys. A 40, 6481), Pinilla 2009 (Hopf fibration and
  entanglement), the 2014 pure-spinor paper (arXiv:1403.6419), the 2026
  spin-chirality paper (arXiv:2605.14515, a different chirality).

### What is and is not already in print

| statement in section 9 | owner |
|---|---|
| maximally entangled correlation maps are improper; handedness bit | Altepeter 2009 (observation), James 2022 ($\det c$), Gamel 2016 ($d$), Filatov--Auzinsh 2024 (drawing) |
| $\det T=-C^{2}$ for pure states | Filatov--Auzinsh June 2026, eq. (33) |
| partial transpose reverses the orientation; Peres as a reflection | Gamel 2016; Avron--Kenneth 2009 |
| self-dual / anti-self-dual, spin flip, time reversal as the duality | Avron--Kenneth 2009 (on operators) |
| left and right $SU(2)$ as gauge versus rotation on the Hopf bundle; twistor space for two qubits | Chin--Lee 2014 |
| the two Hopf fibrations of $S^{7}$ as twistor and dual twistor space of $S^{4}$ | Atiyah--Hitchin--Singer (mathematics); **not stated for qubits anywhere found** |
| the fibre of one chirality is the unitary local group, of the other the phase-and-spin-flip group; the chiralities exchanged by conjugating one qubit | **not found** |
| handedness of the Bell pair *is* the twistor chirality, and the same-handed pair is the partial transpose, hence forbidden | **not found**: the join of the two columns |
| Filatov's $K_{3}$ frustration as the $\mathbb{Z}_{2}$ holonomy of edge chiralities on the W register; canonical-orbit dependence | **not found** |

So the joining sentence, that the opposite handedness of an entangled pair
is the choice of chirality of the twistor fibration over the Hopf base,
with the same-handed assignment being the dual-twistor fibration reached by
an antiunitary on one qubit, which positivity forbids, is not in the
literature I could reach. The ingredients all are, and the paper should
cite them as such: Gamel and Avron--Kenneth for the partial transpose as
a reflection, James and Filatov--Auzinsh for the handedness, Filatov and
Auzinsh 2026 for $\det T=-C^{2}$, Chin and Lee for the left/right split on
the Hopf bundle and the twistor space, Atiyah--Hitchin--Singer for the
fibration. A fresh search of Google Scholar citations of Chin--Lee and of
James would be the one further check before the word "first" is used
anywhere; I did not do that.

Corrections to the earlier sections of this note: section 9's
"$\det T=-C^{2}$" is Filatov--Auzinsh 2026, not new; section 9's
partial-transpose reading has Gamel 2016 as its owner in the Bloch-matrix
language. The ledger proposal in 9a for the identity stands as *arithmetic
on the W register*, with those attributions.

Batch `bib/handedness_twistor_prior_refs_2026-10-07T2359.bib`: James 2022,
Gamel 2016, Avron--Kenneth 2009, Lévay 2005, Orion--Akkermans 2025
(Crossref-verified), Filatov--Auzinsh 2026 and Chin--Lee 2014 (arXiv
only), Altepeter et al. 2009 (VERIFY-CITE, from James's list). Support
status per entry in the batch; the passages quoted above are what was
read.


## 10. Reading list: spinors versus twistors (added 2026-10-08T2000)

JS: "where can I learn about the difference between a twistor and a
spinor?" The one-paragraph answer, then the sources, metadata verified
against Crossref and the arXiv API on 2026-10-08 (none read this session
beyond what the earlier sections used).

A two-component spinor $\pi_{A'}$ is a vector in the defining representation
of $SL(2,\mathbb{C})$, the Lorentz group at a point: it knows a null
direction (the flagpole $\pi^{A}\bar\pi^{A'}$) and a phase, and nothing about
where it is. A twistor $Z^{\alpha}=(\omega^{A},\pi_{A'})$ is a vector in the
defining representation of $SU(2,2)=\mathrm{Spin}(2,4)$, the conformal
group of Minkowski space, and the second spinor carries the position
through the incidence relation $\omega^{A}=\mathrm{i}x^{AA'}\pi_{A'}$: a
twistor is a spinor together with a point on the null ray it points along,
up to the ray's own scaling, and the twistor norm $Z^{\alpha}\bar Z_{\alpha}$
is the helicity. So: a spinor is a twistor at a point, and a twistor is a
spinor plus a place. In the two-qubit model of section 4, a twistor is
$\mathbb{C}^{4}$, two spinors, two qubits; the fibre of $\mathbb{CP}^{3}\to S^{4}$
over a point is the sphere of spinors at that point up to scale, which is
the celestial sphere in Lorentzian signature and the sphere of complex
structures in Euclidean, and the Bloch sphere in either.

Sources, gentlest first:

- Huggett and Tod, *An Introduction to Twistor Theory*, 2nd ed., LMS
  Student Texts 4, Cambridge, 1994 (Crossref: 10.1017/CBO9780511624018).
  Short, starts from two-spinors, builds twistors from the incidence
  relation. The place to start.
- Penrose, *The Road to Reality*, 2004: the hypercomplex-numbers chapter
  for spinors and the twistor chapter near the end, for the pictures and
  the motivation (Robinson congruences, why "twistor"). Not verified
  against a record; from memory.
- Adamo, *Lectures on twistor theory*, PoS Modave 2017, arXiv:1712.02196
  (API-verified). Modern, free, aimed at amplitudes; the first two lectures
  are the spinor-to-twistor dictionary.
- Penrose and Rindler, *Spinors and Space-Time*, vol. 1 (Two-spinor
  calculus and relativistic fields, Cambridge 1984, Crossref
  10.1017/CBO9780511564048) and vol. 2 (Spinor and twistor methods in
  space-time geometry, 1986; Crossref query failed, metadata from memory).
  The standard reference; vol. 1 is the spinor half, vol. 2 the twistor
  half.
- Ward and Wells, *Twistor Geometry and Field Theory*, Cambridge 1990
  (Crossref 10.1017/CBO9780511524493). The mathematician's account,
  including the Euclidean twistor fibration and the Ward correspondence
  used in section 2.
- Dunajski, *Solitons, Instantons, and Twistors*, Oxford 2009 (Crossref
  10.1093/oso/9780198570622.001.0001). Euclidean twistors and instantons,
  closest to the $S^{7}\to\mathbb{CP}^{3}\to S^{4}$ story.
- Woit, *Notes on the twistor* $\mathbf{P}^{1}$, arXiv:2202.02657 (2022,
  listed in the Woit note). Short, on exactly the fibre.
- For spinors alone, Lawson and Michelsohn, *Spin Geometry*, Princeton
  1989 (from memory). More than is needed here.

Batch `bib/twistor_reading_list_2026-10-08T2000.bib` for the five
verified items; the two from memory are VERIFY-CITE and not batched.


## 11. A spinor plus a place: the relation is the move off the cone (added 2026-10-08T2100)

JS: "in our framework a 'place' is created when a relation is formed.
Pre-FANOUT a quantum state is isolated from the network of events, once it
becomes connected to the network of events it acquires a location, a new
entry in the record book is created. There is an interesting connection
here to a twistor being a spinor plus a place. Or am I thinking in the
wrong direction?" Right direction, with one correction that makes it
exact: the twistor is not the connected object but the object one step
short of it. Script `scripts/spinor_twistor_place_2026-10-08T2100.py`
(seed 20261008, PASS), stdout below.

*The geometry.* Write the two-qubit amplitudes as a $2\times2$ matrix $A$.
Then $\rho_{1}=AA^{\dagger}$ and $2\rho_{1}=p^{0}+\mathbf p\cdot\sigma$ is a
future 4-vector, the paper's "density operators fill the future cone"
(`sec:comp-distance` region, the Lorentz paragraph). Its Minkowski norm is
$p^{2}=4\det\rho_{1}=4|\det A|^{2}=C^{2}$, the squared concurrence (part A).
So a qubit with no relation to its partner has a null $p$: it is on the
cone, a light ray, with no rest frame. A qubit entangled with its partner
has a timelike $p$ with mass $C$: it is inside the cone and has a rest
frame, reached by a boost of rapidity $\operatorname{artanh}|\mathbf r|$
(part D), infinite for a separable pair, zero for a Bell pair, which sits
at rest, $p=(1,\mathbf 0)$. Local invertible maps on the qubit are Lorentz
transformations of $p$ with $\det A$ invariant (part B), so the mass is the
$SL(2,\mathbb{C})$ invariant of the pair, as in Avron--Kenneth and Chin--Lee;
local unitaries of the *partner* do nothing to $p$ at all. And the Hopf
base point of section 4, $(\mathbf r, Ce^{\mathrm{i}\phi})$, is Chin and
Lee's $(\mathbf p/p^{0},\mu)$ with $|\mathbf r|^{2}+C^{2}=1$ (part C): the
base of the fibration is momentum space, and the relation coordinate is
the mass.

*The three stages, in the paper's words.* A lone spinor is a null
direction with no place. A twistor is a spinor along a null ray: the ray
is the set of points a signal from here could reach, so the twistor is a
spinor with its *possible* relations, and in Euclidean signature the
fibre over a point is the sphere of possible measurement axes (section 4,
and the observer note of today, section 5): possibility in both
signatures, nothing written. An entangled pair is the actual relation: the
record coordinate $Ce^{\mathrm{i}\phi}$ is non-zero, $p$ leaves the cone, a
rest frame exists, and "rest frame" is what a place is for a worldline.
So the sequence is spinor, twistor, place, with the twistor the
counterfactual stage between the two, and FANOUT the step from the second
to the third. JS's sentence holds with "a twistor is a spinor plus a
*possible* place, and the relation makes it actual". The record-book entry
is the concurrence.

*Why this is the paper's own picture and not a new one.* `sec:gr-nonlocality`:
"location is inherited relationally, a place obtained by being related to
things that have places"; an entangled pair shares one knowledge-space
location until one partner is fanned out into the already-located
network. Here that is geometry: a pair's reduced 4-vector is at rest in
the pair's own frame, and the pair's place in the wider network is
acquired by the same mechanism one rung up. The records note (2026-09-20,
section 3): "a mass is a clock"; "above the electroweak crossover there are
no masses, so no clocks and no proper time". Here: no relation, no mass,
null, no proper time along it; the first relation gives the first mass
and the first rest frame. The Chin--Lee reading of concurrence as mass is
the two-qubit (quaternionic-rung) shadow of the paper's "mass is the
relation's debt", and the paper's mass proper is the octonionic rung's
associator debt; this is a RHYME between rungs, not the same quantity,
and the note says so.

*What it does not say.* The 4-vector is the reduced state's, so "place"
here is a rest frame in the pair's momentum space, not a location in the
record network's spatial count (`op:comp-metric`, OPEN). The twistor's
null ray is a Lorentzian object and the Hopf fibre a Euclidean one; the
two are the same $\mathbb{CP}^{1}$ over a point (section 1), but the
sentence "the ray is the possible relations" is the Lorentzian reading
only. And the counterfactual reading of the twistor stage is the observer
note's CANDIDATE, not a theorem.

Labels: part A to C STRUCTURAL (textbook geometry of the two-qubit reduced
state, verified); the three-stage reading CANDIDATE; the mass rhyme RHYME.
Proposed wording, one sentence for `sec:gr-nonlocality` or the Lorentz
paragraph, JS to rule: "At the two-qubit rung the acquisition of a
location is literal: a qubit's reduced density operator is null, a light
ray with no rest frame, until it is entangled, and its concurrence with
the network is the invariant mass that puts it inside the cone, where a
rest frame, a place, exists." With `chinlee2014momentum` and
`avronkenneth2009entanglement` from the 2026-10-07 batch.

### Exact stdout of `scripts/spinor_twistor_place_2026-10-08T2100.py`

```
Spinor, twistor, place: the two-qubit 4-vector, seed 20261008
==================================================================================
A. p^2 = C^2 = 4|det A|^2, p^0 = 1 (normalised):                  max err 6.7e-16
   separable pair: p^2 = -1.1e-16 (null, on the cone)    Bell pair: p = [1. 0. 0. 0.] (at rest)
B. local SL(2,C) on qubit 1 = Lorentz on p (Lambda^T eta Lambda = eta, Lambda p = p'): max err 1.6e-13; det A invariant 7.7e-16
   local SU(2) on qubit 1 = rotation (p^0, |p| fixed): 5.6e-16; local SU(2) on qubit 2 leaves p alone: 6.9e-16
C. base point (r, C e^{i phi}) = (p/p^0, mu): |r|^2 + C^2 = 1:        max err 6.7e-16   (Chin--Lee's |p|^2 + |mu|^2 = 1)
D. the stages
   separable (twistor: null ray, no place)    C = 0.000   p^2 = -0.000   |r| = 1.000   rapidity to rest frame = inf
   C = 0.3                                    C = 0.300   p^2 = 0.090   |r| = 0.954   rapidity to rest frame = 1.874
   C = 0.9                                    C = 0.900   p^2 = 0.810   |r| = 0.436   rapidity to rest frame = 0.467
   Bell (at rest: a place)                    C = 1.000   p^2 = 1.000   |r| = 0.000   rapidity to rest frame = 0.000
==================================================================================
SPINOR TWISTOR PLACE: PASS
```


## Correction pointer, 2026-10-08

Section 11 quotes the records note's "no masses, so no clocks and no proper
time" above the crossover. Corrected the same day: vacuum masses vanish,
thermal masses $\propto T$ remain, no particle has a clock of its own.
Section 11's argument needs only the first clause and stands. See
`knowledge/sessions/thermal_masses_crossover_correction_2026-10-08T2200.md`.
