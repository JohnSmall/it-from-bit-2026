# Development Plan: From Hopf Fibrations to Particle Masses

## Status note — 2026-06-08

This is a build plan for the entanglement-to-particle-physics linkage, organised like a
software project: numbered stages, explicit dependencies, a deliverable and an acceptance
criterion ("done when") for each, and two parallel branches that fork off the main line. The
critical path runs from the already-drafted Hopf-justification section to a zero-free-parameter
mass spectrum. Two destinations the brief asks us to *set up* — quantum circuits for interactions,
and the particle-zoo classification — are marked as Branch A and Branch B and wired to the stages
they depend on.

### Dual-audience convention (read this first)

Every stage is written to be legible from two directions: readers fluent in **quantum computation
(QC)** but not gauge theory, and readers fluent in **gauge theory (GT)** but not quantum computation.
Each stage therefore carries three fixed fields — a **QC view**, a **GT view**, and a **Bridge**
(the single shared object both views are talking about). This is not decoration: the bridge is the
load-bearing claim of the stage, and if it cannot be stated cleanly the stage is not done. The
convention is mandatory for every section written from this plan.

### The Rosetta Stone (Stage 0 deliverable, used by every later stage)

| Quantum computation | Gauge theory | Shared object |
|---|---|---|
| qubit | a charge-carrying internal degree of freedom | a point on a Bloch sphere $S^2$ |
| local unitary on one qubit | (no direct analogue) | rotation of one Bloch sphere |
| entanglement (non-separability) | internal/gauge structure beyond the free particle | failure of the Hopf base to factorise |
| SLOCC class | particle species *type* | stratum of the state space |
| reduced-density-matrix eigenvalues | gauge-invariant labels | local-unitary invariants |
| Hopf fibre ($S^1, S^3, S^7$) | gauge orbit / phase freedom | the fibre that is quotiented away |
| Cayley–Dickson rung ($\mathbb{C},\mathbb{H},\mathbb{O}$) | gauge group ($U(1), SU(2), SU(3)$) | division-algebra level |
| GHZ class (special Frobenius) | colour triplet — quark | irreducible tripartite link |
| W class (anti-special Frobenius) | weak doublet — lepton | distributed pairwise link |
| Bell pair (bipartite) | gauge boson — force carrier / edge | two-party connector |
| product (separable) state | Higgs / vacuum | unlinked node |
| measurement / \textsc{fanout} | fixing a gauge / symmetry breaking | singling out the complex direction $e_1$ |

Terminology throughout follows `terminology_reconciliation_entanglement_dictionary_2026-06-08.md`:
"Bell" is the entanglement class, never a synonym for SU(2); the ℍ rung is named as such.

---

## Entry point

**Stage 0 — Foundation (already drafted).**
The Hopf-justification section (Hopf fibrations forced by Hurwitz + Adams; $G_{\mathrm{SM}}$ as the
$\mathrm{Spin}(9)$ stabiliser) and the entanglement-classes section (GHZ → colour/quark, W →
lepton, as theorems). The plan begins immediately after these. *Status: done.*

---

## Critical path: Stage 0 → particle masses

### Stage 1 — One fermion as a three-qubit register
**Goal.** Establish the internal structure of a single fermion as three entangled qubits
$A \otimes B \otimes C$ over $\mathbb{C} \otimes \mathbb{H} \otimes \mathbb{O}$, one Bloch sphere
per gauge sector, using the Filatov two-Bloch-sphere representation as the visualisation tool.
**Builds on.** Stage 0; `cayley_dickson_qubits_for_review.md`; Filatov–Auzinsh two-sphere work.
**QC view.** A particle is a specific three-qubit entangled state; you already know how to draw and
manipulate it. **GT view.** A particle carries hypercharge ($A$), weak isospin ($B$), and colour
($C$); these are the three internal labels. **Bridge.** Each qubit's Bloch sphere *is* one gauge
sector's internal space; the three Hopf levels are the three gauge groups.
**Deliverable.** Section: "A fermion is three qubits." **Status: structural (assembly of established pieces).**
**Done when.** A reader of either background can point at the register and say which qubit is which gauge sector.

### Stage 2 — Quantum numbers from the state
**Goal.** Read electric charge $Q$, weak isospin $T_3$, hypercharge $Y$, and colour off the
register; recover $Q = T_3 + Y$.
**Builds on.** Stage 1; the GHZ → ℂ³ and W → $SU(2)_L$-doublet theorems; `hypercharge_derivation.md`;
`electroweak_unification_theorem.md`.
**QC view.** Which qubits are active and how they are entangled fixes the state's invariant labels
(the reduced-density-matrix spectra). **GT view.** The Standard Model quantum-number assignment of
one generation, derived rather than tabulated. **Bridge.** Local-unitary invariants = gauge-invariant
charges. **Deliverable.** Section: "Reading the charges." **Status: proved core (GHZ/W) + structural (assembly).**
**Done when.** Each generation member's $(Q, T_3, Y, \text{colour})$ is read off its state.
**→ Milestone 1: either audience can extract a fermion's SM quantum numbers from its three-qubit state.**

### Stage 3 — The fermion content of one generation  *(feeds Branch B)*
**Goal.** Assemble all fermions of a single generation from entanglement structure plus chirality.
**Builds on.** Stage 2; `k3_obstruction_chirality_sterile.md` (chirality from the computability-split
orientation); `w_to_su2l_doublet_theorem.md` (left-handed doublets).
**QC view.** Enumerate the distinct entanglement configurations of the register. **GT view.** The
left- and right-handed quarks (×3 colour) and leptons of one family. **Bridge.** The particle list
*is* the list of inequivalent register states; chirality is the orientation of the split.
**Deliverable.** Section: "One generation as a classification." **Status: structural; chirality selection owed.**
**Done when.** The one-generation table is reproduced with no particle assigned by hand.

### Stage 4 — Three generations and the sterile class  *(completes Branch B)*
**Goal.** Derive exactly three generations and the fourth a-chiral (sterile-neutrino) class.
**Builds on.** Stage 3; `octonion_generations_calculation.md`; the $K_3$ obstruction; triality on
$S^{15} \to S^8$.
**QC view.** The three inequivalent ways to resolve the non-two-colourable $K_3$ frustration graph;
a fourth, all-same resolution sits outside the chiral structure. **GT view.** Family replication
$\times 3$, plus a sterile neutrino as a dark-matter candidate. **Bridge.** Generation index =
$K_3$ resolution class; triality permutes the three Cayley–Dickson qubits.
**Deliverable.** Section: "Why three." **Status: structural / owed (the formal topological proof is Open Problem in `fermion_topology_open_problems.md`).**
**Done when.** Exactly three chiral generations plus one sterile class drop out of the obstruction count.
**→ Milestone 2: the full Standard Model fermion zoo as an entanglement classification (Branch B output).**

### Stage 5 — The geometry of mass
**Goal.** Lay the conceptual foundation for mass before any number is computed: mass as
**associator-debt** (the octonionic associator $[a,b,c]$, dimension $[L^{-1}]$), the single
dimensional parameter (the self-referential scale ambiguity), and the Higgs VEV as the exchange
rate that fixes the scale.
**Builds on.** Stage 1 (register geometry); `higgs_mass_charge_internal_distance.md`;
`mass_ratios_from_triality.md`; the associator-debt principle.
**QC view.** Mass is the information cost of specifying a bracketing in a non-associative algebra —
a property of the entanglement geometry, not an external label. **GT view.** Yukawa coupling $\times$
VEV; the Higgs mechanism. **Bridge.** The non-associativity that forbids a metric on $S^7$ is the
same fact that makes mass an associator-debt rather than a geodesic length on the fibre.
**Deliverable.** Section: "What mass is here." **Status: structural.**
**Risk / sub-task.** Reconcile the associator-debt *conceptual* account with the geodesic-length
*operational* formula used in the fermion-mass and glueball notes — these must be shown to be the
same quantity or the relationship made explicit. Treat like the Bell-terminology reconciliation.
**Done when.** Both audiences agree on what "mass" denotes and where the one dimensional parameter enters.

### Stage 6 — Charged lepton masses (the showcase)
**Goal.** The cleanest result first: the single Koide parameter $\delta_0 = 2/9$ reproducing all
three charged-lepton masses to $<0.01\%$, with the Koide $\alpha = \sqrt{2}$ traced to the
Cayley–Dickson doubling norm.
**Builds on.** Stage 4 (three generations — Koide is a cross-generation relation); Stage 5 (geometry);
`fermion_mass_geodesic_calculation.md`; `flavour_mass_generations_j3o.md`.
**QC view.** The three masses are eigenvalues of a Jordan-algebra element built from the lepton's
register; one parameter sets all three. **GT view.** The charged-lepton spectrum with zero free
dimensionless parameters. **Bridge.** Leptons sit in the associative ℂ-singlet sector, where the
doubling norm is exactly $\sqrt 2$. **Deliverable.** Section + computation. **Status: proved (postdiction, <0.01%).**
**Done when.** $m_e, m_\mu, m_\tau$ are reproduced from $\delta_0 = 2/9$ and one mass scale.
**→ Milestone 3: first zero-free-parameter mass postdiction.**

### Stage 7 — Quark masses
**Goal.** Extend to quarks: the deviation from the lepton baseline driven by the short-root coset
(non-associative) and the Casimir ratio $3 = (\sqrt 3)^2$, via $\alpha^2 = 2 + 2|Q|^{3/2}$, with the
up/down distinction by $|Q|$ and the Georgi–Jarlskog factor of 3 recovered without $SU(5)$.
**Builds on.** Stages 5–6; `quark_neutrino_masses.md`; `g2_root_length_correction_2026-06-08.md`
(quarks on the short-root coset; gluons on the long roots).
**QC view.** The quark register accesses the non-associative ℂ³ sector, which modifies the effective
coupling. **GT view.** Quark mass hierarchy and the quark/lepton ratio. **Bridge.** The $G_2$
root-length ratio is the algebraic measure of the non-associativity the quark sector feels.
**Deliverable.** Section + computation. **Status: conjecture (open problem: Casimir account vs fitted $|Q|^{3/2}$).**
**Done when.** Up- and down-type Koide parameters are reproduced and the open reconciliation is stated honestly.

### Stage 8 — Boson masses and electroweak parameters  *(sets up Branch A)*
**Goal.** $\sin^2\theta_W = 1/4$ (tree), $m_H = v/2 \approx 123.1$ GeV, $y_t = 1 \Rightarrow m_t \approx 174$ GeV,
and $m_W, m_Z$ from fibre geometry.
**Builds on.** Stage 5; `boson_mass_fibre_geometry.md`; `higgs_chirality_flip.py`; the
gauge-boson-as-edge identification (terminology note).
**QC view.** Boson masses come from the geometry of the Bell-pair (edge) channels and the Higgs
product-state scale-setter. **GT view.** Electroweak symmetry breaking, the weak mixing angle, the
top Yukawa. **Bridge.** The Higgs (product state) sets the scale; the gauge bosons (Bell edges)
acquire mass from the fibre embedding. **Deliverable.** Section + computations. **Status: proved/structural (tree-level postdictions within ~2%).**
**Done when.** The four numbers above are reproduced and the boson = bipartite-edge picture is in place for Branch A.

### Stage 9 — Extended predictions (forward-testable)
**Goal.** Neutrino masses ($\Sigma m_\nu \approx 2.6$ meV, strongly normal ordering, testable by
DESI/Euclid/CMB-S4) and the lightest glueball ($m(0^{++}) \approx 1.7$ GeV from C-only Bell networks).
**Builds on.** Stages 4–7; `glueballs_zx_circuits_2026-05-03T0625.md`; geodesic-length machinery.
**QC view.** Glueballs are closed networks of C-qubit Bell pairs; neutrino masses follow from the
sterile-class geometry. **GT view.** Sum of neutrino masses and ordering; the scalar glueball.
**Bridge.** Same geodesic/associator machinery as the fermion masses, on gauge-only (C) registers.
**Deliverable.** Section: "Predictions." **Status: prediction (neutrinos) / speculative (glueball mass).**
**Done when.** The numbers are stated as falsifiable predictions with their experimental tests named.

---

## Branch A — Quantum circuits for particle interactions
**Forks after.** Stage 2 (registers exist) and Stage 8 (bosons as edges).
**Goal.** Represent interactions as quantum circuits: gauge bosons as bipartite edges / gates
(photon → A-gate, W → B-gate, gluon → C-gate, per the terminology note's map–state-duality bridge),
vertices as Bell links, Feynman diagrams as circuits; beta decay as the showcase; the proton as a
9-qubit register.
**Builds on.** `qubits_circuits_nucleon_physics.md`; the terminology reconciliation note (state vs
gate via Choi–Jamiołkowski).
**QC view.** Interactions are gate sequences on identified qubits — directly runnable on hardware
(Qiskit/Aer). **GT view.** Feynman vertices and amplitudes. **Bridge.** A vertex is an edge attached
to two nodes; applying a boson is applying a gate to the relevant qubit (map–state dual).
**Status: structural / owed.** **Prerequisite to close first:** the two open identifications in the
terminology note (electroweak quartet as ℂ⊗ℍ Bell states; eight gluons as the $SU(3)$ adjoint at the
𝕆 level). **Done when.** Beta decay runs end-to-end as a circuit with correct correlations.

## Branch B — The particle zoo as an entanglement classification
**Delivered by.** Stages 3–4 (output of Milestone 2).
**Goal.** The standalone statement "the Standard Model fermion content = the SLOCC classification of
few-qubit entanglement," with the product/Bell/GHZ/W primitives in bijection with Higgs/boson/quark/
lepton, and generations from the $K_3$ obstruction.
**Builds on.** `fermion_topology_open_problems.md` §9; Dür–Vidal–Cirac; Coecke–Kissinger.
**QC view.** A finite classification of entanglement primitives. **GT view.** The particle zoo.
**Bridge.** The Rosetta-Stone bijection. **Status: proved core (GHZ/W) + structural (the bijection as a whole).**
**Done when.** The bijection is stated with each row's epistemic status attached.

---

## Dependency graph (text form)

```
Stage 0 (done)
   └─> Stage 1 (register)
         └─> Stage 2 (quantum numbers) ── Milestone 1
               ├─> Stage 3 (one generation) ─┐
               │        └─> Stage 4 (three generations) ── Milestone 2 ──> Branch B
               └─> (Branch A needs Stage 2 + Stage 8)
   Stage 1 ─> Stage 5 (geometry of mass)
                 ├─> Stage 6 (lepton masses, needs Stage 4) ── Milestone 3
                 │       └─> Stage 7 (quark masses, needs G2 correction)
                 ├─> Stage 8 (boson masses) ──> Branch A
                 └─> Stage 9 (neutrinos, glueballs; needs 4,6,7)
```

Critical path to masses: 0 → 1 → 2 → 3 → 4 → 6 → 7, with 5 joining at 6 and the G₂ correction
feeding 7. Boson masses (8) and predictions (9) hang off Stage 5. Branches A and B are parallel
once their prerequisites are met.

---

## Milestones

1. **Quantum numbers legible (after Stage 2)** — either audience reads SM charges off a state.
2. **Full fermion zoo classified (after Stage 4)** — Branch B output; the classification theorem.
3. **First zero-parameter mass (after Stage 6)** — charged-lepton Koide postdiction.
4. **Full mass spectrum (after Stages 7–8)** — fermion and boson masses, one dimensional parameter.
5. **Predictions on the table (after Stage 9)** — neutrino sum, ordering, glueball mass.

---

## Risk / epistemic register

- **Proved, safe to lead with:** GHZ/W theorems (Stages 2–4 core), charged-lepton Koide (Stage 6),
  tree-level electroweak numbers (Stage 8).
- **Structural, needs careful framing:** the register assembly (Stage 1), the boson-as-edge picture
  (Branch A), the zoo bijection (Branch B).
- **Owed / open, must travel with a flag:** chirality selection (Stage 3); the formal three-generation
  topological proof (Stage 4); the associator-debt ↔ geodesic-length reconciliation (Stage 5); the
  Casimir vs $|Q|^{3/2}$ account of quark masses (Stage 7); the two boson identifications gating Branch A.
- **Cross-cutting hazard:** terminology drift. Every stage must conform to the reconciliation note;
  the two-readings distinction and the corrected $G_2$ root labelling are the two places the corpus
  has already gone wrong, and both feed the mass stages.

---

## Mapping to the papers

Paper 1 (accessible) takes the *results* and *bridges* of each stage — enough for either audience to
follow the chain and engage with the open problems. Paper 2 carries the full derivations and the
discharge of the owed items. Stages 6–7 (masses) and Branches A–B are the natural Paper 1 headline
results; Stage 5's reconciliation and Stage 4's topological proof are Paper 2 obligations.
