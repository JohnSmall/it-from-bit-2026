# The Sedenion Mechanism for Three Generations: K3 as Shadow

**Session document, 2026-07-10.** JS's criticism: the K3 obstruction treats the odd qubit
differently by its Hopf-tower rung -- distinguishability smuggled, not derived; K3 works but is a
placeholder. Verdict of the session: the criticism is right in sharpened form, and the sedenion
structure is not a replacement but the EXPLANATION -- K3 is the register-level shadow of a
symmetry whose home is one rung up. Status vocabulary throughout.

## 0. Corrections to the prompt (recorded)

- "Labeled qubits can't entangle": repaired. Distinguishable subsystems entangle freely. The real
  tension: the canonical W/GHZ orbits are permutation-SYMMETRIC while the K3 reading needs
  which-vertex-is-odd plus its rung identity -- distinguishability imported from the tower
  architecture without derivation. Placeholder-shaped, as suspected.
- "Sedenions create an extra conservation rule": sharpened, not found verbatim in the record. The
  supported version: an extra APPROXIMATELY conserved label (below, section 4).
- "Zero divisors => no fibration => flavour not force": verbatim correct (the fourth-qubit doc's
  safety rail; notebook I measured its matrix form: kernels on cross-half diagonal units).

## 1. The pivotal algebraic fact: the triality promotion

Aut(O) = G2 contains NO S3 -- Spin(8) triality is invisible to the octonions' own automorphisms.
Aut(S) = G2 x S3 (Brown 1967; VERIFY-CITE, refs-first step). The Cayley-Dickson doubling promotes
triality from outer/spinorial to a manifest automorphism factor. Physically: the generation
symmetry exists at the register level only as broken-triality shadows (the zoo's Fano-lines
paragraph); it acquires a carrier one rung up. THE EXTRA QUBIT IS THE WIRE ON WHICH TRIALITY
FINALLY ACTS. The register could not hold the index natively -- which is exactly why K3 had to
smuggle rung labels: it reconstructs combinatorially a symmetry homed upstairs.

## 2. The mechanism, K3-free

Fermions on C^16 = C (x) S (exact). Three generations = the S3-orbit of the three octonion
subalgebras O_1, O_2, O_3 (Gillard-Gresnigt triple; make explicit at refs-first). Count = 3 by
Brown's theorem, not by frustration. Shared triple-intersection H = the electroweak core =>
WHY all generations carry identical EW quantum numbers (a fact K3 never explained). The sterile
= the S3-INVARIANT sector (the trivial rep: nothing to permute), matching a-chirality with no
frustration story. Statuses: the algebra is theorem-grade pending the two verifications; the
physical identification is the follow-up paper's central conjecture.

## 3. What happens to op:filatov-extension

The COMPANION CLAUSE (GHZ coverage) DISSOLVES if the shadow theorem (section 5) lands: quark
generations never needed per-pair Bloch handedness -- the label is the O_i index, algebra-level,
class-blind. Certification asymmetry survives reinterpreted: not whether the label exists but
whether the state can READ it (W geometry shows the shadow: state-certified; GHZ marginals don't:
frame-certified) -- exactly notebooks K (frame-mode) and J (r-channel) as measured. DIVISION OF
LABOUR: sedenions own the count and the label; Filatov keeps chirality and the doublet (per-pair
handedness is genuinely pairwise physics, provable where proven). The op SHRINKS, not vanishes.
Paper 1 untouched until the shadow theorem exists; the op's current pricing remains honest.

## 4. New: generation number as an approximately conserved charge

Exact under everything inside a single O_i (gauge dynamics live in the shared core + per-copy
structure); violated ONLY by cross-algebra operations = the zero-divisor-adjacent sector = the
mixing vertices. => THE CKM IS NEARLY DIAGONAL BECAUSE THE LABEL IS NEARLY CONSERVED; the
Wolfenstein hierarchy as cost-per-cross-algebra-step (candidate: lambda^n ~ n crossings).
This is a mechanism for lambda's smallness K3 never offered. Status: minted this session,
open; joins the AME-deficit route as the second quantitative handle on mixing.

## 4b. First application: the up quark (2026-07-10, same session)

JS asked whether the new machinery reaches the fenced exception. It does, and a disclosed
candidate scan (eight framework-native forms tested against the exact +28.5% overshoot) found:
pred/obs = 1/(1 - 2/9) to 0.1% -- **m_u = (1 - delta0) x formula = 2.162 MeV vs PDG 2.16**.
The Koide angle's FOURTH role (lepton Koide; dilution numerator; lambda = sin(2/9); now the
gen-1 admixture). Consonances: linear in delta0 = the FIRST-ORDER response the interference
appendix verified on hardware (the op's own constraint list); level repulsion gives the sign;
the op's old "some twenty per cent" was 2/9 = 22.2% unrecognised. Mechanism home: the admixture
= zero-divisor-sector leakage of the gen-1 state; "why the leakage angle equals delta0" is now
a sedenion computation (checklist item 3b). CAVEATS recorded: multiple comparisons (basket of
eight); PDG band on m_u much wider than the central-value hit; candidate, not derivation --
op:up-quark SHARPENED, not discharged. Paper touch applied at recorded-candidate status.

## 4c. Notebook M executed (2026-07-10, same session): the skeleton scan

STRUCTURAL RESULTS (all PASS, paper-grade):
- The explicit triple: S = H (+) V1 (+) V2 (+) V3 with V1 = <e1,e5,e9,e13>,
  V2 = <e2,e6,e10,e14>, V3 = <e3,e7,e11,e15>; each H(+)V_i norm-multiplicative;
  exhaustive over core-doublings. CHECKLIST ITEM 1 EXECUTED.
- THE GRADING THEOREM (stronger than needed): V_i V_i c H, V_i V_j c V_k cyclic --
  the generation structure is an S3-GRADING of the sedenion algebra itself.
- sigma (order 3) and tau (involution) constructed explicitly, verified
  multiplicative on all 256 basis pairs: S3 <= Aut(S) BY HAND. ITEM 2 EXECUTED;
  Brown's citation now decorates a construction rather than carrying it.
- THE ZERO-DIVISOR DIAGONAL: (e_a + sigma e_a) is an ISOMETRY (first-run
  discovery); the true ZDs are z = (a + sigma(e8 . a))/sqrt2 -- generation step
  COMPOSED WITH doubling step, kernels dim 4. MIXING = (TAG FLIP) x (GENERATION
  STEP): the algebra itself says cross-generation transitions require the fourth
  qubit -- the CKM circuit's extra wire, now at theorem grade.

THE ANGLE VERDICT (pre-registered, 18 comparisons, 0 hits): delta0 = 2/9 is NOT
in the skeleton geometry. T1 = 0 identically (the S3 action is phase-blind to
core complex structures -- sector orthogonality kills every overlap phase);
T2 = pi/4 exactly (ZD leakage is maximal and generation-blind); T3 = 1/4 twice.
CONSTRAINTS DELIVERED: delta0 is not a sigma-phase, not raw ZD leakage, not a
naked dimension ratio. THE CANDIDATE (1 - delta0) STANDS -- nothing contradicts
it -- and its derivation target sharpens: the Koide angle must arise in the
DRESSED problem, the framework's mass operator (associator debt + the selected
direction + the GHZ/W dressing) built on C (x) S. Checklist 3b rewritten below.

REPRODUCTION: independently re-run on JS's machine 2026-07-10, output identical digit for
digit (structural checks all PASS; the 18-angle inventory exact: T1 = 0 x12, T2 = pi/4 x4,
T3 = 1/4 x2; zero hits on 2/9). The skeleton verdict is now double-run and closed.

## 5. The shadow theorem (the programme's keystone)

CONJECTURE: the S3 action on {O_i}, projected through the selected C (op:fanout-selection's
direction), reproduces the K3 frustration classes on the register -- the three odd-qubit-out
classes as the shadows of the three O_i, the all-same class as the invariant sector. Candidate
bridge ALREADY IN PAPER 1: the three Fano lines through the selected direction (zoo, triality
paragraph) vs the three O_i -- pose the correspondence line_i <-> O_i and prove it. Notebook I's
composability/kernels data is this programme's first evidence (composition confined to the
C-line; cross-half kernels).

## 6. Checklist (ordered)

1. Brown 1967 verified and cited; the GG triple written out explicitly (refs-first -- already
   the fourth-qubit programme's step 1, now with sharper purpose).
2. The shadow theorem posed precisely; the Fano-line correspondence attempted first.
3. The near-conservation formalised: define the O_i-sector charge; show gauge dynamics commute;
   locate the violating operators in the zero-divisor sector; extract the lambda-power cost.
   NOTE (post-M): the violating sector is now explicit -- the (tag flip) x (generation step)
   diagonals; the charge is the grading degree.
3b. THE DRESSED MASS OPERATOR (the sharpened up-quark target): construct the framework's
   associator-debt functional on C (x) S with the selected direction placed inside the
   generation sector, dress with the GHZ/W register structure per the op's interference
   construction, and compute the generation-one first-order shift. It equals -delta0 or the
   candidate dies. The skeleton (notebook M) is fully prepared; this is a construction, not
   a scan.
4. Chirality's residence confirmed: Filatov keeps the doublet and handedness on the W side;
   the quark doublet's story under the split re-examined (the frame/parity setting of sec:frame
   is the expected home).
5. Only then: the Paper-1 touch (one clause at op:filatov-extension noting the dissolution
   route), and the follow-up paper's spine rewritten around sections 1-2 of this document.

## 7. Relations

Paper 1: sec:generations (K3 + the triality paragraph -- the shadow's two halves already
adjacent), op:filatov-extension, sec:frame, op:fanout-selection (the same selection breaks the
same triality). Fourth-qubit doc 2026-07-06 (the licence, the risks -- risk 2's 1(+)2 design now
reads as the S3 rep structure 1 (+) 2, a retrodiction). Notebooks I, J, K (the evidence base).
The witness section (S3-breaking as vacuum selection -- the thin-spectrum import may apply to
the generation S3 too: a THIRD locking).
