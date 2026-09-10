# Session summary: supertasks, CTCs, and imaginary temperature

Date: 2026-07-26
Participants: JS + Claude
Type: context-transfer session summary (navigable archive)
Feeds: the planned appendix on infinities in QFT. Working placement: beside
op:qft-depth from the loop-recursion appendix, cross-referencing the solenoid
subsection of app:padic-shadow.
Posture agreed: the composite chain below is to be introduced as a FENCED
SUGGESTION with follow-up pointers, and left as such. No LaTeX splice yet.
Sentinel-gated paragraph and RIS batch deferred until JS says go.


## 0. Position in the corpus

This session sits downstream of app:padic-shadow
(appendix_padic_ctc_division_2026-07-23T0617.tex: Prop. carry, prop:padic-hopf
"positivity as the exotic phenomenon", the solenoid subsection, caution (c),
op:padic-hensel) and of session_summary_loop_recursion_2026-07-25.md
(op:qft-depth, lem:transversality, RHYME 2, RHYME 3, Adams clause (ix) in the
loop ledger). It assembled, in order:

(1) the literature standing of the supertask--CTC relationship;
(2) two formal identifications (lamp = exterior view of the negating loop;
    Deutsch consistency = Archimedean summation);
(3) JS's indistinguishability thesis, its proof shape, and its quantum flank;
(4) the QFT chain from infinite frequency to division algebras, arrow by
    arrow, with anchors and fences;
(5) the imaginary-temperature reading of Hawking gr-qc/9502017 (read in full
    this session) and its refinement into a fourth clause of RHYME 2.

Seed framing (JS, opening turn): CTCs and supertasks are both devices that
license information non-conservation -- creation from nowhere (Deutsch:
knowledge paradox, D-CTC entropy injection) and transport to nowhere
(Laraudogoitia: the beautiful supertask, in which total energy disappears
although each collision conserves it, and whose time reverse is spontaneous
self-excitation ex nihilo). Hawking's two-disk model (Section 4) exhibits both
faces in one construction.


## 1. The supertask--CTC relationship: literature standing

The relationship has been studied, but only computationally, never
structurally, and never on spheres. The one paper that explicitly joins the
two is Andreka--Nemeti--Szekely, Parallel Processing Letters 22(3) (2012),
arXiv:1105.0047, which substitutes wormhole-based CTCs for Malament--Hogarth
supertask scenarios explicitly to escape the blueshift problem -- the
replacement enacted in print, same computational job, swapped interior.
Behind it: Hogarth (1992), Earman--Norton (1993), Etesi--Nemeti (2002),
Nemeti--David (2006), Manchak (2010).

Power disanalogy (important): Malament--Hogarth supertasks decide the halting
problem and climb Hogarth's hierarchy; bounded Deutsch CTCs cap at PSPACE
(aaronsonwatrous2009, in library) -- computable. The two devices are NOT
equivalent representations of non-computability. The gap is exactly the fixed
point: Deutsch's consistency condition is the move that tames the loop from
divergence to PSPACE.

Verification problem (the computable-discrimination side): Davis's "myth of
hypercomputation" papers; the oracle-hypermachine verification-problem
literature; and Svozil, arXiv:physics/0508207, whose black-box analysis
reduces verification of an alleged super-Turing oracle to the induction
problem. Falsifiability asymmetry: a wrong "does not halt" is finitely
exhibitable by running the machine to its halt; a wrong "halts" is never
finitely refuted.


## 2. Formal identifications established this session

### 2.1 Lamp = exterior view of the negating loop

The exterior view of the grandfather CTC -- state, negated state, state, with
no pointwise limit -- is the orbit of the once-around monodromy map. It IS
Thomson's lamp; Benacerraf undetermination IS the classical inconsistency of
the CTC. The oscillation is indexed by traversal count, not exterior time;
what the exterior couples to is the mean (Hawking's heat-bath reading:
Section 4).

### 2.2 Deutsch consistency = Archimedean summation. STATUS: theorem-backed
statement, CANDIDATE reading

Von Neumann's mean ergodic theorem: Cesaro averages of the iterates converge
to the projection onto the fixed subspace. For the negating loop, the Cesaro
average of the orbit from rho_0 is (rho_0 + X rho_0 X)/2; the
start-independent maximum-entropy member of the fixed set is I/2 -- Grandi's
series summed to 1/2. Reading: a CTC is a supertask completed by summation,
and the choice of summation method is the choice of place. Cesaro/ergodic
averaging is the Archimedean completion; Prop. carry is the non-Archimedean
one. This is the Archimedean partner of the app:padic-shadow RHYME (paradox
at the Archimedean place, attractor at the finite places). Respects caution
(c): the ergodic completion assigns a mixed state, not a parity -- the
record-level lamp question stays undetermined while the ledger gets I/2 (the
lamp's double duty from continuity_limit_realisability_2026-07-04.md,
restated).

### 2.3 JS's indistinguishability thesis

Statement: a supertask can be replaced by a CTC and there is no computable
way to tell the difference.

No-provenance lemma (theorem-grade, provable in-house, three lines): any
finite record transcript of interaction with a black box is a finite object,
hence computable, hence exactly reproducible by a Turing machine with a patch
table. No total computable test can certify "interior ran a supertask",
"interior contains a CTC", or "interior exceeds Turing": the adversary hands
the test a computable simulacrum agreeing on the realised transcript.

One-rung-up proposition: the discrimination predicate is real but located one
level up. By Shoenfield's limit lemma a guesser identifies the classification
in the limit, converging without ever certifiably having converged
(confirmation Pi_2, refutation Sigma_2). Punchline: telling a supertask from
a CTC is itself a supertask. The bump in the carpet as a theorem shape:
indistinguishability does not eliminate the non-computable difference, it
relocates it into the observer's test.

Quantum flank (the one place the thesis could leak; the literature already
contains the fight): Brun--Harrington--Wilde claim Deutsch CTCs perfectly
distinguish non-orthogonal states -- a finite-statistics record-side
signature no linear supertask machine can counterfeit, since linearity is
kinematic and Zeno compression does not break it. Bennett--Leung--Smith--
Smolin reply (linearity trap): presented with a labelled mixture, the CTC is
of no use; CTC-assisted evolution is nonlinear, so its output on a mixture is
not the convex combination of outputs on components. The P-CTC model is
strictly weaker again (Holevo bound still applies). If BLSS are right under
proper operational accounting, the thesis holds in full; if BHW, the
fixed-point content remains provenance-free but the dynamical wrapper leaks
mechanism-class through statistics -- and even then nonlinearity is no
certificate of geometry. See OP-3.

### 2.4 Framework placement

FANOUT forgets order-type. The record is a finite string; whether it was
produced by an actual omega-sequence (supertask; Cesaro/ergodic completion),
by consistency on a loop (CTC; Brouwer on the compact density body), or by
ultrametric contraction (Banach--Hensel) is interior gauge. One fixed point,
three certificates, zero provenance.

Caveat (recorded): the CTC does not discharge limit-realisability, it
relocates it -- Deutsch existence is Brouwer, i.e. compactness of the state
body, so the Archimedean premise re-enters through the state space after
leaving the timeline.

Scrutiny flag (recorded): this is the THIRD corpus instance of "the record
forgets which forgetful operation produced it" (Jaynes purifications;
FANOUT-plus-HJW; mechanism-of-fixed-point). Each instance requires its own
proof. No citing the pattern.


## 3. The QFT chain (target of the next conversation)

Proposed chain (JS): infinite frequency (UV divergence) -> supertask ->
CTC representation -> information transport round the loop -> parallelisable
spheres -> division algebras. Assessment: every individual arrow has at least
one citable anchor; only the composite is ours. Right shape for a fenced
suggestion.

### 3.1 Placement fence (load-bearing)

The CTC attaches to the COMPLETED DIVERGENCE -- the supertask limit of the
recursion, the infinite-frequency tail -- never to a single diagram. (JS's
correction, loop-recursion session: a single Feynman loop is finite and
daily-computed; the identification would be cheap and unfalsifiable.) The
fence is what makes the chain non-trivial.

### 3.2 Lorentzian theorem-face: Misner space

Misner space is Minkowski space identified under a Lorentz boost. Each
circuit of the loop applies the boost: a circulating mode climbs a GEOMETRIC
frequency ladder omega, lambda*omega, lambda^2*omega, ... -- infinite
frequency is generated by circulation, not merely represented by it. The
vacuum energy is an image sum over winding number. Hiscock--Konkowski (1982)
first demonstrated its divergence at the chronology horizon; later work
(PRD 49, 5240 (1994)) shows the leading divergence is universal (independent
of mass and curvature coupling). Hawking's chronology protection conjecture
(1992) is built on this result. Kay--Radzikowski--Wald: the two-point
function cannot remain Hadamard at a compactly generated Cauchy horizon.

### 3.3 The n = 0 / n != 0 distinction and the horizon conversion. STATUS:
CANDIDATE

In the image sum, the n = 0 term is the ordinary flat-space UV divergence
(coincidence limit, renormalised as usual); the n != 0 winding terms are
finite away from the horizon. The two infinities are distinct EXCEPT on the
chronology horizon, where the boosted images become null-related to the
point: one circuit lands on the point's own light cone, and the winding sum
probes the coincidence singularity at finite loop parameter. Defensible
claim: the chronology horizon is precisely where the loop converts the local
UV limit into a global winding sum -- the CTC as the device that transports
the coincidence limit around a finite circuit. See OP-2.

### 3.4 Holonomy reads the divergence

Automorphic fields (twisted by e^{i alpha} around the loop, i.e. carrying a
U(1) holonomy): Sushkov showed a special alpha makes the renormalised <T>
vanish; Cramer (gr-qc/9606027) reproduces this by image sums and proves the
KRW singularity of the two-point function persists. Li--Gott (1998): an
adapted Rindler vacuum at identification scale 2 pi with vanishing <T>
throughout -- a self-consistent vacuum. Hiscock's rejoinder (gr-qc/0009061):
the cancellations require tuning to a measure-zero value, and nonconformal
fields diverge regardless. Readings: the completed divergence is a FUNCTION
OF THE TRANSPORT round the loop; the special holonomies are fixed points of
the once-around consistency condition (Deutsch in field-theoretic dress);
and the KRW persistence is the bump in the carpet operating verbatim inside
this literature -- the divergence is not eliminated by the self-consistent
choice, only relocated from the stress tensor into the state's
microstructure.

### 3.5 The twist ladder and the falsifier surface

The fibre ladder has standard physics at three rungs before the framework
says anything: Z_2 twist = spin structure on the loop (antiperiodic thermal
fermions; the fermionic Matsubara frequencies are the S^0 monodromy made
quantitative); U(1) twist = Sushkov's alpha, equivalently a Wilson line or
chemical potential round the circle; SU(2)-and-up holonomy round the
Euclidean time circle = the Polyakov loop, the deconfinement order parameter.
The octonionic rung is the open slot: the once-around composition is
Moufang, so the n-th image contribution requires an ordering of traversals --
the associator enters the SUM ITSELF, not merely its value. If the
octonionic-twisted winding sum is ill-defined as a sum, that is
division-algebra termination showing up as termination of the
loop-completion ladder -- the actual content of "the infinite energies of
QFT bring division algebras into play". See OP-1. This is the falsifier
surface for the chain's payoff arrow.

### 3.6 Where the spheres actually sit

CTC existence is cheap: a closed manifold admits a Lorentzian metric iff its
Euler characteristic vanishes (among spheres, exactly the odd ones), and
every compact Lorentzian manifold contains CTCs (Geroch; Hawking--Ellis
Prop. 6.4.2). So CTC existence does not select the parallelisable spheres.
What parallelisability buys is the LEDGER: saying "the same bit came back
negated" requires identifying the fibre with itself round the loop, i.e. a
global frame. Declaring Adams' frame parallel gives curvature-free
(Weitzenboeck) transport with all anholonomy in torsion; on S^5 no such
frame exists and the once-around comparison is path-dependent before any
paradox is stated. Slogan (STATUS: topology theorem; causal reading
CANDIDATE): odd spheres host loops; division-algebra spheres host loop
accounting -- Adams read causally.

In gauge theory the division-algebra spheres already enter as the TOTAL
SPACES of the Hopf bundles over the physical spheres: Dirac monopole
S^3 -> S^2, BPST instanton S^7 -> S^4 (Trautman 1977: the Maxwell and
Yang--Mills solutions are the Hopf fibrings). Physics on the base,
accounting upstairs. This routes the meeting through geometry, as
lem:transversality demands (routes meet in the geometry both algebras act
on, never by identifying the algebras).

Taub--NUT: the canonical homogeneous CTC spacetime -- Misner's
"counterexample to almost anything" -- has its closed time circles along the
Hopf fibres of S^3 (the Taub sector is biaxial Bianchi IX preserving the
Hopf S^2; beyond the null hypersurface the Hopf-fibred direction becomes
timelike; time is nontrivially fibred over S^2, with the Misner string as
gravitational Dirac string). Refinement worth keeping: the CTC region of
Taub--NUT contains no closed causal geodesics -- the loop exists but cannot
be traversed freely-fallingly; it must be driven. Fenced reading: the
paradox requires a computation, not a flow. RHYME.

### 3.7 The p-adic resonance. STATUS: RHYME, fenced

The Misner blueshift ladder is geometric -- a lambda-filtration, the only
kind caution (c) licenses -- and the same winding tally that diverges
Archimedeanly at the chronology horizon contracts on the solenoid.
Chronology protection as an Archimedean-place phenomenon, with
op:padic-solenoid acquiring a physical divergence to balance.

### 3.8 The two faces and the chosen posture

Euclidean face: Matsubara, Casimir, Polyakov -- the winding sums complete,
the completed energy reads the holonomy; "representation" is the honest
word. Lorentzian face: Misner, KRW -- theorem-grade, but the CTC's job is
obstruction (protection). The appendix presents both faces via the
complex-beta plane, with Hawking's small-real-part damping (Section 4.2) as
the interpolation, and claims neither.


## 4. Imaginary temperature: Hawking gr-qc/9502017, read in full this session

### 4.1 The verbatim fact

JS's reading is not an inference; Hawking states it in exactly those terms.
The CTC systems in the two-disk model are like a particle coupled to a heat
bath where the only difference is that the temperature of the heat bath is
imaginary: the spacetime is identified periodically in real Lorentzian time,
rather than periodically in imaginary time as for a normal thermal state.
Citable fact, not framework reading.

### 4.2 Three further details from the paper (all verified by direct
reading)

(i) Damping: when rotating the disk separation from imaginary to almost
real, Hawking keeps 1/T imaginary WITH A SMALL POSITIVE REAL PART, and it is
that residual real part which damps the high-frequency divergences by the
thermal factor exp(-E/T). Read against Section 3: the record-side (real-
beta) component is what holds off the infinite-frequency supertask; the
pure-CTC limit (imaginary axis) is where the damping vanishes and the
winding divergence lives.

(ii) Reality by symmetrisation: he sums the rotations in both directions to
ensure the initial-to-final probabilities come out real -- record-side
realness enforced as z plus its conjugate.

(iii) Creation ex nihilo: the model produces particles in the final state
even from an empty initial state. Caution recorded: Hawking attributes this
energy non-conservation to the fixed background (no back-reaction), noting
that in the two-dimensional black hole case with back-reaction the
superscattering matrix conserves energy. Do not oversell the channel; it
pairs with the Laraudogoitia annihilation channel at the level of structure,
not of established dynamics.

### 4.3 The refined chain. STATUS: step one citable fact; steps two and
three CANDIDATE, fenced as the fourth clause of RHYME 2

At 1/T = i a the Gibbs weights exp(-E_n/T) become unimodular phases
exp(-i a E_n): a COMPLEX QUASI-PROBABILITY DISTRIBUTION SUMMING TO ONE. The
loop's thermal statistics are pre-record ledger statistics (Khrennikov
territory), and positivity of Gibbs weights is exposed as a property of the
real-beta axis only -- the thermodynamic echo of "positivity as the exotic
phenomenon" (prop:padic-hopf). Every functional built on the weights
(ln Z, S = E/T + ln Z) goes GENERICALLY COMPLEX -- complex, not purely
imaginary; precision worth keeping for referees.

Record-side refinement (supplied by Hawking's own result): the record never
receives imaginary entropy. The exterior sees REAL decoherence entropy --
pure states go to mixed because part of the state circulates on the CTCs
unmeasured, and evolution is by a superscattering operator that does not
factorise. Honest chain: imaginary temperature => complex (ledger-valued)
information ON THE LOOP => real coherence loss AT THE RECORD. The imaginary
part is paid at the cut. RHYME 2 gains its fourth clause:

  Im(amplitude)          = the cut                    (iv)
  Im(influence action)   = the decoherence functional (v)
  Im(complex information)= the debt                   (framework)
  Im(1/T)                = the loop                   (this session)

with Hawking's coherence loss as the payment.

### 4.4 External anchors for complex entropy (verified this session)

Pseudo-entropy (Nakata--Takayanagi--Taki--Tamaoka--Wei, PRD 103, 026005
(2021), arXiv:2005.13801) and timelike entanglement entropy (Doi--Harper--
Mollabashi--Takayanagi--Taki, PRL 130, 031601 (2023), arXiv:2210.09457):
both take complex values in general, related by analytic continuation; the
imaginary part is read as the emergence of time in dS/CFT; and -- the detail
the appendix most wants -- the DIVERGENT terms of the timelike entanglement
entropy are PURELY IMAGINARY, coming from the timelike extremal surfaces.
Divergence and imaginarity coincide at exactly the junction the
infinities appendix occupies. The generating move (rotating a spacelike cut
into a timelike one) is the same rotation as Hawking's disk separation. The
emergence-of-time reading is consonant with the operational-time line;
RHYME, fenced.

### 4.5 The record-side square

The record sees |Z(beta + i t)|^2 -- the spectral form factor -- the Born
quotient (discard phase, keep the quadratic invariant) applied to the loop
partition function. The boost-quotient Lorentzian saddle computing its ramp
(the double cone; Misner's construction in modern dress) is standard
equipment in current quantum gravity. VERIFY before RIS: Saad--Shenker--
Stanford, arXiv:1806.06840.

### 4.6 Cautions (recorded as fences; see Section 6)

Imaginary temperature is not negative temperature (the latter is real
thermodynamics of bounded spectra; a referee will reach for it). And
exp(-i a H)/Z must not be called a density matrix -- it is non-Hermitian and
not a state; its failure to be one IS the content.


## 5. Statuses

Theorem / textbook: mean ergodic completion; the no-provenance lemma (once
written, OP-4); chi = 0 criterion and Geroch / Hawking--Ellis 6.4.2; Adams
parallelisability; Weitzenboeck flatness-with-torsion; frequency--winding
duality on the loop.

Citable fact (surfaced or read this session): all of Sections 1, 3.2, 3.4,
4.1, 4.2, 4.4; the BHW-vs-BLSS dispute.

CANDIDATE: CTC as representation of the completed divergence (3.1 with 2.2);
horizon conversion (3.3); Adams read causally (3.6); complex
quasi-probability reading of imaginary-temperature weights and Im(1/T) as
fourth RHYME 2 clause (4.3).

RHYME (fenced): chronology protection as an Archimedean-place phenomenon
(3.7); "the paradox requires a computation, not a flow" (3.6);
emergence-of-time consonance (4.4).

Open: OP-1 through OP-4 below.


## 6. Fences (recorded so they are not violated or retried)

(a) No identification of a single Feynman diagram with a CTC. The CTC
    attaches to the completed divergence only.
(b) The ordinary UV infinity is the n = 0 coincidence term; identification
    with the winding sum is exact only on the chronology horizon.
(c) Imaginary temperature is not negative temperature.
(d) exp(-i a H)/Z is not a density matrix; the prose must not call it one.
(e) Thermodynamic functionals at 1/T = i a are generically complex, not
    purely imaginary.
(f) The record never receives imaginary entropy; the record-side face is
    real decoherence. The chain must terminate there.
(g) Third instance of the no-provenance pattern (Jaynes purifications;
    FANOUT-plus-HJW; mechanism-of-fixed-point): each instance requires its
    own proof; no citing the pattern.
(h) Hawking's creation-ex-nihilo channel is a fixed-background artefact by
    his own account; structure-level pairing with Laraudogoitia only.
(i) Statuses are never upgraded.


## 7. Open problems / seeds for the QFT conversation

OP-1 (octonionic once-around; the falsifier surface). Compute the Z_2-,
U(1)-, and SU(2)-twisted image sums on the two-disk / Misner-type loop
(standard machinery: antiperiodic Matsubara; automorphic alpha; Polyakov
line). Then state precisely what fails for an octonion-valued twist: Moufang
composition, ordering of image contributions, the associator entering the
sum itself. PASS: a well-defined octonionic completion exists under stated
conditions. FAIL: the sum is ill-defined as a sum -- division-algebra
termination = termination of the winding-completion ladder. Either outcome
is structural.

OP-2 (horizon conversion). Make 3.3 precise: a lemma-shaped statement that
the n-th boosted image becomes null-separated exactly at the chronology
horizon, so the winding sum probes the Hadamard coincidence singularity at
finite loop parameter. Target: explicit with the Hiscock--Konkowski kernel.

OP-3 (BLSS separation). Does any finite-copy statistical test, under the
Bennett--Leung--Smith--Smolin correlated-input rules, separate Deutsch
consistency from linear Zeno completion? A separation names the one
observable that survives the record functor; a no-go upgrades the
indistinguishability thesis from computability to full operational
statistics.

OP-4 (no-provenance lemma, in-house). Write the three-line adversary proof;
PASS/FAIL check: exhibit the computable simulacrum for a given finite
transcript. Companion proposition via Shoenfield: discrimination is
limit-identifiable but not decidable (confirmation Pi_2, refutation
Sigma_2); telling a supertask from a CTC is itself a supertask.

OP-5 (deferred deliverables). Sentinel-gated LaTeX paragraph for the
infinities appendix plus RIS batch, on request only, after key
verification per Section 8.


## 8. Citation ledger

Bin A -- surfaced or read directly this session (bibliographic form still to
be confirmed at RIS time per house rule):

  andrekanemetiszekely2012  Andreka, Nemeti, Szekely, Parallel Processing
                            Letters 22(3) (2012), arXiv:1105.0047
  hiscockkonkowski1982      Hiscock, Konkowski, Phys. Rev. D 26, 1225 (1982)
  hawking1992chronology     Hawking, Phys. Rev. D 46, 603 (1992)
  hawking1995coherence      Hawking, arXiv:gr-qc/9502017 (read in full)
  cramer1996                Cramer, arXiv:gr-qc/9606027 (Sushkov result via
                            image sums; KRW persistence)
  ligott1998                Li, Gott, Phys. Rev. Lett. 80, 2980 (1998)
  hiscock2000               Hiscock, arXiv:gr-qc/0009061 (review; rejoinder)
  misnermassive1994         Phys. Rev. D 49, 5240 (1994) (massive /
                            nonconformal extension; AUTHOR LIST: VERIFY)
  svozil2005                Svozil, arXiv:physics/0508207
  doi2023timelike           Doi, Harper, Mollabashi, Takayanagi, Taki,
                            Phys. Rev. Lett. 130, 031601 (2023),
                            arXiv:2210.09457
  nakata2021pseudo          Nakata, Takayanagi, Taki, Tamaoka, Wei,
                            Phys. Rev. D 103, 026005 (2021),
                            arXiv:2005.13801
  taubnuthopf2018           arXiv:1806.10135 (biaxial Bianchi IX; Hopf
                            direction becomes timelike; FULL FORM: VERIFY)

Bin B -- from model memory; VERIFY before RIS:

  hogarth1992               Found. Phys. Lett. 5, 173 (1992)
  earmannorton1993          Phil. Sci. 60, 22 (1993)
  manchak2010               Found. Phys. 40, 276 (2010)
  etesinemeti2002           Int. J. Theor. Phys. (2002)
  nemetidavid2006           Appl. Math. Comput. (2006)
  davis2004myth             in Teuscher (ed.), Alan Turing: Life and Legacy
                            (2004); companion 2006 paper
  krw1997                   Kay, Radzikowski, Wald, Commun. Math. Phys. 183,
                            533 (1997)
  geroch1967                J. Math. Phys. 8, 782 (1967); or Hawking--Ellis
                            Prop. 6.4.2
  trautman1977              Int. J. Theor. Phys. 16, 561 (1977)
  misner1967                in Ehlers (ed.), Relativity Theory and
                            Astrophysics I (1967)
  clementgaltsov2015        Clement, Gal'tsov, Guenouche (no closed causal
                            geodesics in the CTC region; likely Phys. Lett.
                            B 750 (2015))
  bhw2009                   Brun, Harrington, Wilde, Phys. Rev. Lett. 102,
                            210402 (2009)
  blss2009                  Bennett, Leung, Smith, Smolin, Phys. Rev. Lett.
                            103, 170502 (2009)
  leeyang1952               Phys. Rev. 87, 404 and 410 (1952)
  heyl2013                  Heyl, Polkovnikov, Kehrein, Phys. Rev. Lett.
                            110, 135704 (2013)
  sss2018doublecone         Saad, Shenker, Stanford, arXiv:1806.06840
  parikhwilczek2000         Phys. Rev. Lett. 85, 5042 (2000)
  isham1978                 Proc. R. Soc. A 362, 383 (1978)

Already in library: deutsch1991, laraudogoitia1998, aaronsonwatrous2009.
Laraudogoitia's 1996 Mind paper (the beautiful supertask) may warrant its
own key if the appendix names the annihilation channel explicitly: VERIFY.


## 9. One-sentence version for the appendix fence

A closed timelike curve is a supertask completed by consistency instead of
by an omega-th step; no computable test can tell the two interiors apart;
the completed divergence reads the transport round the loop; globally
consistent transport on spheres exists exactly at the division-algebra
rungs; and at imaginary temperature the loop's statistics are complex
quasi-probabilities whose record-side face is real decoherence -- offered as
a suggestion with the pointers above, and left there.
