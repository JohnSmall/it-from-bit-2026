# Gravitational memory: cognate record, structural contacts, and a derivation target for Paper 2

Provenance: session 2026-07-12 (gravitational memory effect). Companion to
paper2_metric_identification_2026-07-07.md; intended for the Paper-2 file set.

Status key: Sections 1--2 are established GR/QFT record. Section 3 holds one STRUCTURAL
contact, one CANDIDATE, one fenced RHYME. Section 4 records a heuristic repaired this
session, with the naive form kept per the invalid-routes convention. Section 5 is a
derivation target, OPEN, with PASS/FAIL criteria. Section 6 lists honesty flags. British
English; ASCII math throughout; c = 1 except where G and c are displayed for bookkeeping.

## 0. One-paragraph summary

A gravitational-wave burst leaves a permanent relative displacement between freely falling
masses after the wave has passed (the memory effect). The persistent quantity is not tilted
light cones -- local curvature returns to zero -- but the double time integral of the
transient tipping, stored in the worldlines and in the matching of asymptotic frames, and it
persists because the endpoint manifold is degenerate (the BMS vacua). This document records
the effect, its infrared-triangle structure, three contacts with the framework (Jacobson-type
flux-to-geometry as STRUCTURAL; BMS-vacua-as-thin-spectrum register as CANDIDATE;
sign-definiteness-as-arrow as fenced RHYME), the repaired light-cone-tipping heuristic (memory
as the GR shadow of monotone relation-creation, CANDIDATE), and one derivation target:
recover the Christodoulou integrand from marks-across-a-cut bookkeeping. Slogans to keep:
"the tipping is transient; its time integral is forever"; "order + number".

## 1. The effect (established record)

### 1.1 Definition and the two species

Memory: the transverse-traceless strain does not return to zero after a burst; pairs of
freely falling masses end at different proper separations than they began. Two species.

(a) Linear (ordinary) memory. Zel'dovich--Polnarev 1974. Sourced by net changes in the
source's mass/momentum multipoles: unbound encounters, neutrino bursts, asymmetric
supernovae. Sign: either, depending on the multipole change. Braginsky--Grishchuk 1985 named
the effect.

(b) Nonlinear (null / Christodoulou) memory. Christodoulou 1991. Sourced by the energy flux
of the gravitational waves themselves -- the radiation gravitates. Present in every compact
binary merger. Source is positive-definite (dE/dOmega du >= 0), so this piece accumulates
with a preferred-sign character (see honesty flag 3 for the tensor caveat).

### 1.2 The formula of record (Favata 2010 conventions)

Delta h_jk^TT(u) = (4G / (c^4 r)) * int_{-inf}^{u} du' int_{S^2} dOmega'
                   [ dE_gw / (du' dOmega') ] * [ n'_j n'_k / (1 - n'.N) ]^TT

with n' the unit vector to the flux element and N the unit vector to the observer. Geometry
responding to energy flux integrated over a null cut: this exact shape is what Section 5
targets from the counting side.

### 1.3 Geodesic-deviation reading

For initially comoving free masses with separation xi (schematic, c = 1):

xi_i'' = -R_{0i0j} xi^j        =>        Delta xi_i = - int du int^u du' R_{0i0j}(u') xi^j.

The memory is the DOUBLE TIME INTEGRAL of the curvature. The tipping (Riemann != 0) is
transient; the integral persists because the masses are free (no restoring force) and the
final-state manifold is degenerate (Section 2.2). The tipping is transient; its time integral
is forever.

### 1.4 Variants

Spin memory (Pasterski--Strominger--Zhiboedov 2016): a permanent asymmetry in light travel
times around a closed loop traversed in opposite directions -- a directly causal observable.
Velocity memory (plane-wave literature, Zhang--Duval--Gibbons--Horvathy line): the residue can
be a relative velocity, not just a displacement. Electromagnetic memory (Bieri--Garfinkle
2013): velocity kicks to free charges. Colour memory (Pate--Raclariu--Strominger 2017): a
burst of gluon radiation leaves a net colour-frame rotation -- Yang--Mills analogue; placement
in this programme is item 7.5.

### 1.5 Observational status (as of 2026-07-12)

Undetected. Single-event memory is below current ground-based sensitivity; the routes are
statistical stacking and low-frequency space detectors. Forecasts: SNR 3 (5) with roughly 35
(90) GW150914-like events at design sensitivity (Lasky et al. 2016); definitive evidence from
an ensemble of order 2000 BBH observations (Huebner et al. 2020); population SNR near 3
after about five years at design sensitivity (Boersma et al. 2020); updated displacement and
spin outlook in Grant--Nichols 2023. LISA sees massive-black-hole mergers cleanly at single
events. Asymmetric core-collapse supernovae could give strong memory ramps (lunar detectors;
possibly terrestrial for Galactic events).

## 2. The infrared triangle (established record)

### 2.1 The triangle

Strominger--Zhiboedov 2014: the memory formula is the Fourier transform in time of Weinberg's
1965 soft graviton theorem, and memory is the observable face of BMS supertranslations. Three
corners, one structure: soft theorem (QFT), supertranslation (asymptotic symmetry), memory
(observable). Spine reference: Strominger's 2018 Princeton lectures.

### 2.2 Vacuum degeneracy

Asymptotically flat gravity spontaneously breaks supertranslation symmetry: the vacuum is
infinitely degenerate, labelled by supertranslation frame. A burst of radiation is a
transition between inequivalent vacua; memory is the observable trace. The supertranslation
is an angle-dependent shift of retarded time, u -> u + f(theta, phi), and the memory tensor
is the trace-free double covariant derivative of f on the sphere,

Delta C_AB = -(2 D_A D_B - gamma_AB D^2) f     (overall sign per convention).

The soft pole is the statement that the record degree of freedom itself costs zero energy to
excite (see honesty flag 5 for the fence on this phrasing).

### 2.3 Soft hair

Hawking--Perry--Strominger 2016: the claim that this degenerate boundary register carries
black-hole information. Mainstream cognate for Section 3.2; add to the Paper-2 cognate map
beside Lloyd, Jacobson, Rideout--Sorkin.

## 3. Structural contacts with the framework

### 3.1 Flux across a null cut => permanent geometric change  [STRUCTURAL]

The Christodoulou integrand (1.2) and Jacobson's Clausius relation are the same structural
move: energy/information flux across a null boundary produces a geometric response --
Jacobson at a local Rindler horizon, memory at scri+. The junction identity
(paper2_metric_identification, sec 3b: one locking billed as dQ/T = k_B ln 2 dN_bits = area
increment) lives in exactly this territory. Memory is the one mainstream, in-principle
observable THEOREM instantiating the mechanism Paper 2 asserts, which makes it an anchor
rather than a new prediction: the framework must reproduce it (Section 5), and gets to cite
it as the classical face of the locking story if it does.

### 3.2 BMS vacuum manifold as the gravitational thin spectrum  [CANDIDATE]

Dictionary to be written (item 7.3): spontaneously broken supertranslations <-> spontaneously
broken phase symmetry; infinite degenerate vacuum family <-> Anderson tower / thin spectrum
(higgs_entanglement_superconductor_2026-07-07.md, Elitzur split); memory <-> the record
written into the degenerate manifold. Degenerate ground-state manifolds are what classical
records are made of: writing into them is energetically free (the soft pole), erasure is
where Landauer bills arrive -- consistent with graded-FANOUT locking with geometry itself as
the register, not in tension with it. Status: CANDIDATE until the dictionary is written and
the redundancy audit (7.2) is done.

### 3.3 Sign-definite accumulation and the arrow  [RHYME -- keep fenced]

The null memory's source is positive-definite, so the geometric ledger has a preferred-sign
character, rhyming with post-FANOUT thermodynamic irreversibility. Fences: the tensor
projection means components can partially cancel across the sky (no strict per-component
monotonicity); the linear memory is bidirectional. The arrow claim, if ever made, is confined
to the null piece and phrased as preferred-sign character, not monotonicity.

## 4. The light-cone-tipping heuristic, repaired (session 2026-07-12)

### 4.1 The naive form and its failure (recorded so it is not retried)

Naive: "gravity is light-cone tipping; a passing wave tips cones; therefore causal relations
change; therefore memory." This explains the TRANSIENT, not the RESIDUE. After the burst,
Riemann returns to zero (idealising away the remnant's static field): the cones locally
un-tip. Discriminator: the naive reading predicts residual curvature after passage; there is
none. Observed situation: zero residual curvature, nonzero relational offset. Any account of
memory as persistent tipping is therefore wrong and is not to be retried.

### 4.2 The repair

The memory is the double time integral of the tipping (1.3), stored in the worldlines and in
the frame matching, and it persists for two reasons that are one fact: the masses are free
(no restoring force; spacetime has no elasticity pulling them back) and the endpoint manifold
is degenerate (many flat configurations, all equally good -- the BMS vacua of 2.2). The
persistence and the vacuum degeneracy are the same statement.

### 4.3 Where "new causal relations" is exactly right

At the relational level, not the local-cone level. The supertranslation u -> u + f(theta,phi)
permanently re-threads the causal bookkeeping between distant worldlines -- events at equal
retarded time before the burst are not after -- while every local cone is Minkowski again.
Spin memory is DEFINED as a light-travel-time asymmetry: a causal observable. Velocity memory
means relations between the bodies continue to be created after the wave is gone. Pedigree:
Penrose 1965 -- exact plane-wave spacetimes admit no Cauchy surface (null focusing);
gravitational waves restructure global causal structure exactly, not metaphorically.

### 4.4 In-framework reading: memory as the GR shadow of monotone relation-creation  [CANDIDATE]

If causal order grows monotonically (Rideout--Sorkin sequential growth; loop closure creates
causal structure, time_as_computation_gr_emergence.md sec 10.1; the causal past is
write-once), then a burst that creates relations CANNOT leave no residue: un-creating
relations is not an available operation. Persistence becomes automatic rather than
surprising. Reading: the burst is a stream of loop closures traversing the region; the memory
offset is the net ledger change. The sign-definiteness of the null flux (3.3) is the rhyme
this reading expects. Status: CANDIDATE; it inherits every fence in Sections 3 and 6.

### 4.5 The precision tax: order + number

Causal order alone fixes only the conformal structure (Malament 1977;
Hawking--King--McCarthy 1976). The memory observable Delta h is a proper-distance offset -- a
LENGTH. The heuristic therefore needs both halves of the causal-set slogan, order AND number:
the burst adds relations and it adds counted events, and op:comp-metric must supply the
volume element for the offset to be a distance rather than a conformal re-labelling. This is
what upgrades the heuristic from a picture to a computation (Section 5).

## 5. Derivation target: the Christodoulou integrand from marks-across-a-cut  [OPEN]

Claim to attempt: the counting dictionary (relation-creation flux across a null cut, the
marks-across-a-cut bookkeeping of paper2_metric_identification caution flag 2) reproduces the
form of 1.2 -- the (4G / c^4 r) prefactor, the flux integrand dE_gw / (du' dOmega'), and the
angular kernel [ n'_j n'_k / (1 - n'.N) ]^TT.

Why this target is well-chosen: it is pre-solved on the GR side (Favata 2010 is the answer
sheet), it exercises exactly the open momentum-flux reading, and it is of the same rank as
the Newtonian-limit-vs-Lloyd check already on the spine.

PASS: the integrand and kernel emerge with the correct angular structure and 1/r falloff; the
prefactor lands within the O(1) already owed on the lambda/l_P coefficient.
FAIL: a mismatch in the angular kernel or the falloff. A FAIL falsifies the flux reading AS
FORMULATED (the marks-across-a-cut definition), not the framework; record and reformulate.

## 6. Honesty flags

1. Asymptotic vs ordinary scales. The clean supertranslation / vacuum-transition statement is
   exact only at scri+. Finite-distance persistent observables exist (Flanagan et al. 2019)
   but the BMS reading degrades away from infinity. Paper 2 lives at ordinary measurement
   scales; the bridge must be built, not assumed.
2. No redundancy criterion anywhere in the GR derivation: memory is classical through and
   through. "Memory offset = locked (post-FANOUT) relation" is CONJECTURE until the Zurek
   condition is checked (7.2). Sharp form of the question: the offset is imprinted on every
   pair of freely falling worldlines in the wave's wake -- does offset-on-every-geodesic-pair
   constitute Zurek redundancy (many independently accessible copies), or does the framework
   count only matter-register copies? If the former, memory is post-FANOUT by the framework's
   own criterion; if the latter, an unread offset is a low-R relation and geometry-as-register
   needs the matter-coupling step. Either answer is informative; neither is to be assumed.
3. Tensor cancellation across the sky; linear memory bidirectional; arrow claims confined to
   the null piece and phrased as preferred-sign character (3.3).
4. Velocity memory makes "permanent position offset" frame- and time-dependent in some
   spacetimes; the invariant statement is the re-matching of asymptotic frames, not a fixed
   displacement.
5. "Writing is free" applies to the record degree of freedom (the soft mode, strictly at
   omega -> 0), not to the emitting process, which radiates hard energy. Phrase accordingly
   wherever 3.2 is used.

## 7. First computations (candidates for the Paper-2 spine; proposed continuation of
paper2_metric_identification sec 6 as items 10--14)

1. (Spine 10) The integrand check: define marks-flux across a null cut, compute the induced
   relational offset, compare with 1.2 including the angular kernel and the 1/r falloff.
   PASS/FAIL per Section 5.
2. (Spine 11) Redundancy audit of the geometric record: formalise honesty flag 2's question;
   classify the unread offset's R-grade if the answer is matter-registers-only.
3. (Spine 12) Thin-spectrum dictionary: write the BMS-vacua <-> Anderson-tower mapping
   explicitly (broken generator, tower spacing in the asymptotic limit, record capacity);
   check against the Elitzur split in the Higgs-superconductor section.
4. (Spine 13) Landauer audit of erasure: what operation erases a memory offset, and at what
   cost? Note the null memory cannot be erased by more null memory in the same channel
   (sign-definite source); anti-memory requires engineered linear-memory flux. Cost
   accounting vs k_B T ln 2 per erased bit.
5. (Spine 14) Colour-memory placement: where Pate--Raclariu--Strominger sits relative to the
   GHZ/colour sector; likely Paper 3 or the gauge appendices; record the decision.

## 8. Relations

paper2_metric_identification_2026-07-07.md: the junction identity (sec 3b) is the mechanism
3.1 anchors; caution flag 2 is the definition Section 5 exercises; the cognate map (sec 4)
gains Hawking--Perry--Strominger and Strominger's lectures beside Lloyd, Jacobson,
Rideout--Sorkin; sec 6's spine gains items 10--14 above.
higgs_entanglement_superconductor_2026-07-07.md: thin spectrum / Anderson tower, Elitzur
split -- target of the 7.3 dictionary.
time_as_computation_gr_emergence.md sec 10.1: loop closure creates causal structure -- the
in-framework mechanism behind 4.4.
session_summary_2026_04_02.md sec 5: measurement = light-cone tipping (SL(2,C)
identification) -- the heuristic's native home; Section 4 is its radiation-sector repair.
grounding_argument_gauge_group.md sec 4: the relational past-light-cone reading that makes
4.3's relational-level statement natural.
fanout_logic_measure_correspondence_theorem_v2_2026-05-17.md: R-grading vocabulary for 7.2.
Paper-1 anchors: op:comp-metric (the gate for 4.5), sec:jacobson, the one-bit-per-closed-curve
pricing, the Unruh derivation.

## 9. References to mint (citation keys author+year+keyword; note fields give role)

Core:
- zeldovich1974memory -- Zel'dovich, Ya. B.; Polnarev, A. G. Sov. Astron. 18, 17 (1974).
  [linear memory origin]
- christodoulou1991memory -- Christodoulou, D. Phys. Rev. Lett. 67, 1486 (1991).
  [nonlinear (null) memory]
- favata2010memory -- Favata, M. Class. Quantum Grav. 27, 084036 (2010).
  [review; the integrand of record for Section 5]
- strominger2014memory -- Strominger, A.; Zhiboedov, A. JHEP 01 (2016) 086; arXiv:1411.5745.
  [memory = Fourier transform of soft theorem; the triangle]
- strominger2018lectures -- Strominger, A. Lectures on the Infrared Structure of Gravity and
  Gauge Theory. Princeton UP (2018). [spine for Section 2]
- hawking2016softhair -- Hawking, S. W.; Perry, M. J.; Strominger, A. Phys. Rev. Lett. 116,
  231301 (2016). [soft hair; register cognate for 3.2]

Supporting:
- braginsky1985memory -- Braginskii, V. B.; Grishchuk, L. P. Zh. Eksp. Teor. Fiz. 89, 744
  (1985). [named the effect; kinematic resonance]
- weinberg1965soft -- Weinberg, S. Phys. Rev. 140, B516 (1965). [soft graviton theorem]
- pasterski2016spinmemory -- Pasterski, S.; Strominger, A.; Zhiboedov, A. JHEP 12 (2016) 053.
  [spin memory; the causal observable of 4.3]
- pate2017colormemory -- Pate, M.; Raclariu, A.-M.; Strominger, A. Phys. Rev. Lett. 119,
  261602 (2017). [colour memory; item 7.5]
- penrose1965planewaves -- Penrose, R. Rev. Mod. Phys. 37, 215 (1965).
  [no Cauchy surface in plane waves; causal pedigree for 4.3]
- bieri2013emmemory -- Bieri, L.; Garfinkle, D. Class. Quantum Grav. 30, 195009 (2013).
  [electromagnetic (kick) memory]
- zhang2017velocitymemory -- Zhang, P.-M.; Duval, C.; Gibbons, G. W.; Horvathy, P. A. Phys.
  Lett. B 772, 743 (2017). [velocity memory in plane waves]
- flanagan2019persistent -- Flanagan, E. E.; Grant, A. M.; Harte, A. I.; Nichols, D. A. Phys.
  Rev. D 99, 084044 (2019). [finite-distance persistent observables; honesty flag 1]
- malament1977causal -- Malament, D. B. J. Math. Phys. 18, 1399 (1977).
  [causal order fixes conformal structure only; 4.5]
- hawking1976topology -- Hawking, S. W.; King, A. R.; McCarthy, P. J. J. Math. Phys. 17, 174
  (1976). [causal/conformal structure; companion to Malament]
- lasky2016memorydetect -- Lasky, P. D.; Thrane, E.; Levin, Y.; Blackman, J.; Chen, Y. Phys.
  Rev. Lett. 117, 061102 (2016). [stacking forecast, GW150914-like]
- huebner2020memorysearch -- Huebner, M.; Talbot, C.; Lasky, P. D.; Thrane, E. Phys. Rev. D
  101, 023011 (2020). [GWTC-1 search; order-2000-event forecast]
- boersma2020memoryforecast -- Boersma, O. M.; Nichols, D. A.; Schmidt, P. Phys. Rev. D 101,
  083026 (2020). [population SNR forecast at design sensitivity]
- grant2023memoryoutlook -- Grant, A. M.; Nichols, D. A. Phys. Rev. D 107, 064056 (2023).
  [displacement and spin memory outlook]

RIS file for Mendeley import available on request (native Unicode for accented names; one
author per AU line; citation key in ID field per convention).
