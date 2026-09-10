# Terminology Reconciliation: The Two Readings of the Entanglement–Particle Dictionary

## Status note — 2026-06-08

The corpus uses the word **Bell** — and the entanglement–particle dictionary more
generally — in two distinct senses that are easy to conflate, and the conflation has
already produced an apparent inconsistency ("Bell ↔ SU(2)" versus "Bell ↔ gauge bosons").
This note fixes a controlled vocabulary, records which claims are proved and which are
structural or owed, and lists the documents that need aligning. It is intended as the
reference for terminology before the gauge-boson sector is drafted.

The short version: there are two independent dictionaries, one indexed by **Cayley–Dickson
level** and one indexed by **SLOCC entanglement class**. They answer different questions and
coincide only for the weak sector. "Bell" should be reserved for the entanglement class;
the quaternionic rung should be named as such.

---

## 1. The two readings

### 1.1 The level reading — Cayley–Dickson rung → gauge group

This is the Hopf-tower / division-algebra correspondence (Krasnov; Dubois-Violette–Todorov;
Mosseri–Dandoloff; Bernevig–Chen), and it is the one the paper's dictionary table uses.

| Rung | Algebra | Hopf fibration | Gauge group |
|------|---------|----------------|-------------|
| 1 qubit | ℂ | S³ → S² | U(1) |
| 2 qubits | ℍ | S⁷ → S⁴ | SU(2) |
| 3 qubits | 𝕆 | S¹⁵ → S⁸ | SU(3) × SU(2) × U(1) / ℤ₆ |

**Epistemic status: proved.** This is the established representation-theoretic chain of
§(Hopf justification). Here "two-qubit / quaternionic" gives SU(2); the phrase carries no
implication about *which kind of particle* lives there.

### 1.2 The topology reading — SLOCC class → particle type

This is the entanglement-class dictionary (Dür–Vidal–Cirac; Coecke–Kissinger), indexed by
the *topology* of the entanglement rather than the rung.

| SLOCC class | Topology | Particle type | Role |
|-------------|----------|---------------|------|
| product / separable | no link | Higgs | creates the arena |
| Bell (bipartite) | two-party edge | gauge boson | connector / symmetry of the arena |
| GHZ (genuinely tripartite, special) | irreducible three-party | quark | confined matter |
| W (tripartite, anti-special) | distributed pairwise | lepton | free matter |

**Epistemic status: mixed.** The GHZ → quark and W → lepton rows are *proved* (the GHZ
confinement and W accessibility theorems). The product → Higgs and Bell → gauge-boson rows
are *structural identifications*, not theorems of the same standing (see §6).

### 1.3 Where the two readings coincide, and where they diverge

The two readings name the same object **only for the weak sector**, because SU(2) *is* the
quaternionic rung — the SU(2) gauge bosons are exactly the bosons whose gauge group equals
the two-qubit level. This coincidence is why "Bell = SU(2)" reads as natural. It is a special
case, not the general rule.

For the photon and the gluon the readings diverge:

- a **gluon** is bipartite ("Bell" in the topology sense — a two-party colour connector) but
  lives at the **octonionic** rung (SU(3)), not the quaternionic one;
- a **photon** is electroweak, sitting in the ℂ⊗ℍ structure, and only acquires its pure-U(1)
  character after electroweak mixing.

So "Bell ↔ SU(2)" (level) and "Bell ↔ gauge boson" (topology) are **different claims**.
Treating them as one is the error this note exists to prevent.

---

## 2. The unifying picture: nodes and edges

The reading that makes the topology dictionary coherent is the channels ontology already
developed in `session_summary_g2_channels_furey_wedderburn_2026-04-30_0543.md`. A **fermion
is a node** (a qubit carrying internal Cayley–Dickson structure); a **gauge boson is an edge**
— a bipartite connector between two matter parties. Bipartite (Bell-class) entanglement is
the edge primitive, which is why every force carrier is "Bell" in the topological sense, and
why interaction vertices are trivalent (two fermion lines + one boson line = an edge attached
to two nodes).

Which boson an edge is depends on **which sector it connects** — that is, which internal
qubit / which division-algebra level carries the attribute being exchanged. The gauge group
of a boson is the gauge group acting on the sector its edge spans. This is the single
sentence that links the two readings:

> A gauge boson is a bipartite (Bell-class) edge; its gauge group is the group of the
> Cayley–Dickson sector the edge connects.

---

## 3. The forces, stated unambiguously

**Photon.** An edge in the U(1) sector. In the electroweak picture the quartet (γ, W±, Z) is
the four-state structure of a bipartite link at the ℂ⊗ℍ level (qubits A and B); the physical
photon is the post-mixing combination coupling to electric charge Q = T₃ + Y, so its pure-U(1)
character is emergent after symmetry breaking. The "photon = A-qubit gate" shorthand in
`fermion_topology_open_problems.md` §7 is the post-mixing electromagnetic limit; strictly the
photon involves both A (hypercharge) and B (isospin) through the Weinberg angle. Standardise:
*the photon is electroweak (ℂ⊗ℍ level); its U(1)_EM identity is the broken-phase limit.*

**W±, Z.** Edges at the ℍ / SU(2) level. This is the unique sector where the level reading
and the topology reading refer to the same object, so "Bell = SU(2)" is correct *here only*.

**Gluon.** A bipartite colour link at the 𝕆 level — a Bell pair on two C-qubits, the eight of
them spanning the SU(3) adjoint (the long roots of G₂ in the corrected assignment of
`g2_root_length_correction_2026-06-08.md`; the colour-triplet ℂ³ they act on is the short-root
coset). This is the case where *only* the topology reading applies: the gluon is "Bell" because
it is a two-party connector, not because it has anything to do with SU(2).

**Higgs.** A product (separable) state — no edge. It is necessarily a singlet because there is
no link structure to classify.

---

## 4. State versus operation: map–state duality

A further wrinkle worth recording: the corpus sometimes describes a boson as a **Bell pair**
(a state — e.g. gluons as Bell pairs on C-qubits in the glueball note) and sometimes as a
**gate** on a qubit (photon = A-gate, W = B-gate, gluon = C-gate in `fermion_topology_open_problems.md`
§7). These are not competing pictures: they are related by **map–state duality**
(Choi–Jamiołkowski), under which a Bell pair is dual to the identity channel and applying a
gate to half of a Bell pair encodes the operation as a state. This duality is the categorical
backbone Coecke and Kissinger build on, so the "boson = link" and "boson = interaction"
readings are two faces of one object. **Status: asserted, not yet written out.** Discharging it
explicitly is part of the boson-sector work (§6).

---

## 5. Controlled vocabulary (recommended usage)

To keep future documents consistent:

1. **Reserve "Bell" for the two-qubit SLOCC entanglement class** (the topology sense). When the
   intended meaning is the quaternionic rung of the Cayley–Dickson tower, write **"the ℍ rung"**
   or **"the quaternionic level"**, never "Bell".
2. **Never write "Bell = SU(2)" as a general statement.** It is true only for the electroweak
   sector. Either say "the ℍ rung gives SU(2)" (level reading) or "the electroweak bosons form
   a bipartite quartet at the ℂ⊗ℍ level" (topology reading), as appropriate.
3. **For the generic boson claim, write "a gauge boson is a bipartite (Bell-class) edge / connector"**
   — not "Bell = gauge boson", which invites the SU(2) misreading.
4. **Keep the two dictionaries typographically separate.** The level dictionary maps *rung → gauge
   group*; the topology dictionary maps *SLOCC class → particle type*. Do not merge their columns
   into a single row (this was the §4 category error already flagged in the G₂ channels session).
5. **In the paper's dictionary table, use the level reading for the gauge-group column** (U(1),
   SU(2), SU(3) by rung) and present "boson = bipartite channel" as interpretive framing, not as a
   theorem. The drafted `entanglement_classes_section_2026-06-08.tex` already does this; keep it.
6. **Use "node" for fermion and "edge" for gauge boson** when invoking the channels ontology, and
   reserve "channel" for the edge itself (the boson), consistent with the April-30 channels note.
7. **Photon:** describe as electroweak (ℂ⊗ℍ); call its U(1)_EM character the broken-phase limit.
   Avoid the bare "photon = U(1) only" except when explicitly in the post-symmetry-breaking limit.

---

## 6. Epistemic status ledger

**Proved.**
- Level reading: rung → gauge group (Hopf tower / Krasnov).
- GHZ → quark (colour triplet, confined); W → lepton (colour singlet, doublet).

**Structural (motivated, not yet at theorem standing).**
- Gauge boson = bipartite connector / edge (the topology reading of the boson row).
- The node/edge channels ontology and the "gauge group = group of the connected sector" rule.

**Owed / open (flagged in `fermion_topology_open_problems.md` §11).**
- The four electroweak bosons as the four states of a ℂ⊗ℍ bipartite quartet — *planned calculation*.
- The eight gluons as the SU(3) adjoint at the 𝕆 level — *planned calculation*.
- The map–state (Choi–Jamiołkowski) identification of "boson = Bell pair" with "boson = gate" —
  *asserted, to be written out*.
- The photon's A/B (hypercharge/isospin) composition through the Weinberg angle, reconciling the
  "A-gate" shorthand with the electroweak quartet — *to be made precise*.

Until the first two are discharged, the boson row of the topology dictionary should travel with an
explicit structural/owed flag, in contrast to the proved fermion rows.

---

## 7. Documents to align

- `fermion_topology_open_problems.md` — §9 dictionary (topology reading, "Bell → gauge bosons")
  and §7 gauge-bosons-as-gates: add a pointer to this note; standardise the photon entry per §3.
- `session_summary_2026_04_02.md` — dictionary uses the topology reading; flag the boson row's status.
- `glueballs_zx_circuits_2026-05-03T0625.md` — "gluons as Bell pairs on C-qubits" is the topology
  reading; correct the residual old root-length labelling (gluons = long roots; colour triplet ℂ³ =
  short-root coset) per `g2_root_length_correction_2026-06-08.md`.
- `qubits_circuits_nucleon_physics.md` — "photon = A-gate, W = B-gate, gluon = C-gate" is the gate
  (operation) face; cross-reference §4 here so it is read as map–state dual to the Bell-pair face.
- `entanglement_classes_section_2026-06-08.tex` (paper) — already on the level reading; no change,
  but its boson row should carry the structural framing rather than a theorem claim.

---

*References (all in the project bibliographies): Dür–Vidal–Cirac (2000); Coecke–Kissinger (2010);
Krasnov (2021); Dubois-Violette–Todorov (2018/2019); Mosseri–Dandoloff (2001); Bernevig–Chen (2003);
Szangolies (2025). Companion notes: `g2_root_length_correction_2026-06-08.md`;
`session_summary_g2_channels_furey_wedderburn_2026-04-30_0543.md`.*
