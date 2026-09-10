# Why observables bundle at measurement: the Frobenius spider as the composition event

*Session: April 19, 2026*

## 1. The question

In other sessions we've developed the view that **particles are not bundles of labels** (charge, spin, isospin, mass glued onto some little ball) **but composition rules for information exchange between events in spacetime**. GHZ and W aren't states — they're the Coecke-Kissinger compositional primitives. What we reify as "a particle" is a rule for how a set of events are causally composed.

This raises a sharp question. Commuting observables *can* be separated between preparation and measurement — that's the Cheshire Cat effect (Aharonov et al. 2013; Denkmayr et al. 2014). Mass can travel one arm of an interferometer while spin travels the other, as a pattern of weak values.

But at the detector click, this separability vanishes. Whatever arrives always arrives **as a bundle**: some charge, some mass, some spin, at some spacetime event. You never see a disembodied electric charge without a carrier. You never see isospin floating free. Even neutrinos — notoriously weakly interacting — always present a complete tuple of quantum numbers *at* an interaction vertex.

So: why the bundle? What is it about strong measurement, as opposed to weak measurement, that insists on assembling all commuting observables into a single tuple at a single spacetime event?

## 2. The core answer: the spider node is a single algebraic point

The framework has already identified:

- Measurement = FANOUT (the transition from non-clonable private amplitude to clonable classical record)
- FANOUT = special commutative Frobenius algebra (Coecke-Kissinger)
- A classical record = a spider node in the ZX/Frobenius diagrammatic language

What hasn't been spelled out is the immediate algebraic consequence:

> **A Frobenius spider node is, by its defining property, a single idempotent in the preferred classical basis. All mutually commuting observables that share that basis are simultaneously diagonalised at that node.**

This is not a physical claim waiting for proof — it's the definition of what a Frobenius algebra *does*. The SCFA selects a preferred basis (the set of "classical states"), and the spider node's output is *a single basis element*. A single basis element in a maximal commuting family has a single tuple of eigenvalues — one for each commuting observable.

So the bundling isn't an additional postulate. It's the statement that a classical record is a classical record — a single piece of copyable data, not an unfinished family of weakly-associated facts.

**The bundle IS the spider node.** That's the whole story in one line.

## 3. Why weak measurement looks different

If the bundle is the spider node, then the ability to "separate" observables in the Cheshire Cat regime is explained precisely: *no spider node has fired yet*.

Weak measurement doesn't FANOUT. It perturbs without producing a classical record. So the amplitude structure that governs weak values is pre-spider: it's the structure of a composition in progress, not a completed composition. In this regime, different commuting observables can have support on different spatial regions of the wavefunction because no single classical anchor has yet been formed to force them into a common tuple.

This gives a clean reading of the Hance-Hofmann (2024) result that Cheshire Cat is fundamentally contextual: contextuality is precisely the statement that "which tuple of eigenvalues the observables take" depends on the measurement context — i.e., on *which spider is about to fire*. Before any spider fires, there is no fact of the matter. Weak values probe the amplitude structure in this no-fact regime.

The Cheshire Cat's grin separates from the cat precisely because the cat has not yet been registered as a classical fact. At registration, the grin snaps back into place — because a single spider can only produce a single tuple.

## 4. Tracing the specific observables

The algebraic point above tells us *that* the commuting observables bundle. It doesn't yet tell us *why the specific bundle is position + mass/energy + gauge charges + spin*. The framework gives each of these an independent reason to be present at a classical record, and they converge:

### 4.1 Position is the FANOUT index

Classical data is, by the FANOUT criterion, data that can be copied and shared. Sharing requires observers to agree on **what they are sharing**, which requires an indexing scheme — a way of saying "this fact, not that fact". In a spacetime theory, events are precisely the points that different observers can unambiguously agree on (up to Poincaré transformations that don't change event-identity).

So: every classical record carries a spacetime-event index as a structural requirement, not as an extra property. A record without a location is a fact no two observers can agree they are looking at — i.e., not a shared fact, i.e., not classical data. **Position is not bundled to the record; position is the record's index, and therefore part of every record by definition.**

*(Structural conjecture, formalisable: position coordinates of a spider node are the FANOUT index of the classical data it produces. Natural audience: categorical quantum mechanics community. Resolution criterion: a theorem that in any operational theory with FANOUT, the index set of the copy morphism must carry the structure of a pseudo-Riemannian manifold with a causal order.)*

### 4.2 Gauge charges are fibre labels; fibres require a base

Electric charge is conserved under U(1), colour under SU(3), weak isospin under SU(2). These live on the fibres of the Hopf tower. A fibre is by construction attached to a point of the base — a fibre without a base point is not a mathematical object in the bundle sense; it is at best a section of a trivial bundle, which only makes sense once the bundle has a base space.

So gauge charge at a classical record is not bundled to position as a separate fact — it is the fibre value *at* the base point. You couldn't detach them algebraically if you tried, because the detachment would require the fibre to exist independently of its base, which it doesn't.

This also says something about what "disembodied charge" would even mean. The only way to have charge without position would be to have the fibre without the base — that is, to have the gauge structure without the classical-record structure. That *is* the pre-measurement regime. In the amplitude, the fibre is there (the state has a phase, the wavefunction has complex structure), but the base point is not yet fixed. Strong measurement fixes the base point, and the fibre value becomes a definite charge at that point.

### 4.3 Mass is the composition cost

From session_summary_2026_04_02: the Higgs VEV is the exchange rate between entanglement entropy (dimensionless) and GeV (dimensionful). Every composition rule has a cost in the framework — it consumes some number of configuration changes before the FANOUT produces the classical record. Rule 𝒜 says there's a global ℏ-scale lower bound on how quickly a computation can proceed, so the cost is always finite and non-zero.

Mass = the entanglement cost of sustaining the channel through the composition event. A classical record with zero cost would be a spider that fires without consuming any configuration changes — a violation of Rule 𝒜. So every classical record has a definite mass-energy-momentum associated with the event it registers.

This is why mass/energy-momentum always comes with the bundle: it is the bill for producing the record, payable at the record.

### 4.4 Spin co-transforms with the spatial frame

This one is already in the project (March 12 session 2): measurement is a Lorentz boost, and SL(2,ℂ) acts both on the qubit (spin structure) and on Minkowski spacetime (frame structure) — *the same* SL(2,ℂ). The boost that fixes the spatial frame of the classical record also fixes the spin-direction basis. They share a common action.

So spin isn't bundled to position as an extra fact — it is co-determined by the same group action that fixes the spatial frame. You cannot pick the frame without picking the spin basis, because the group doesn't let you separate those choices.

### 4.5 The convergence

Four different structural reasons — FANOUT indexing, fibre-base adjacency, composition cost, and SL(2,ℂ) co-transformation — all force the same bundle to appear at any event where a spider fires. This over-determination is reassuring: each observable in the bundle has its own reason for being there. The answer to "why this bundle?" is not one reason but four compounding ones, and they correspond neatly to the four distinct structures the framework identifies (Hopf base / Hopf fibre / Rule 𝒜 ℏ-quantum / SL(2,ℂ)).

## 5. Reframing: particles as bundling rules, not bundled things

Pull back out to the particles-as-composition-rules picture. A particle is not a thing that has these properties; a particle is a rule that specifies, when it fires, which classical tuple is produced.

- The GHZ-rule (quark) fires a spider whose tuple is (position, colour, electric charge with |Q| = 2/3 or 1/3, weak isospin, spin). The colour triplet is part of the rule's specification — it's what SCFA composition on ℂ³ produces.
- The W-rule (lepton) fires a spider whose tuple is (position, lepton number, electric charge with |Q| = 0 or 1, weak isospin, spin) — no colour, because the W-rule operates on ℂ rather than ℂ³.

"What particle was it?" = "Which composition rule fired?" The rule *is* the bundling pattern. You don't have charge without a rule because charge is a label identifying which rule's tuple you're reading.

This is the reason, from inside the framework, that the question "why can't we have electric charge on its own?" has no inside-the-theory referent: electric charge is a projection out of a composition rule's tuple, and a projection from an empty tuple doesn't exist. To have "charge on its own" would be to have a rule that produced a classical record with only one entry in its tuple — and no such rule exists in the Frobenius algebra classification (all valid SCFAs have at least the unit and counit structure, which carry the minimal tuple of position + energy + whatever the algebra's preferred basis labels are).

## 6. A new observation: GHZ-particles are self-FANOUTing; W-particles are not

This is a point I don't think has been made explicit yet, and it drops out of the preceding argument.

GHZ is a **special** commutative Frobenius algebra — it has FANOUT. So a GHZ-rule firing is a self-contained classical-record-generator. A single quark vertex can, in principle, produce a classical record on its own — the GHZ-structure is what classical-record-making *is*.

W is **anti-special** — no FANOUT. A W-rule firing does not produce a classical record on its own; it produces a channel whose content has to be FANOUT-ed by something else (a partner with GHZ structure, e.g., a detector atom, a scintillator, an atmospheric molecule).

This gives a conceptual re-reading of confinement that I don't think is in the literature:

> **Quarks confine because they are the classical-record-generators. You can't have half a classical record, so you can't have an isolated quark.**

Not a force preventing separation. Not a potential that grows linearly with distance. *The GHZ-rule is the SCFA, and the SCFA is what "producing a classical record" means, and the tripartite structure of GHZ is the minimum irreducible SCFA needed for classicality on ℂ³. Below three, the structure doesn't close.* Confinement is the statement that fewer than three quarks cannot form a complete SCFA over ℂ³.

Correspondingly, leptons don't confine because they're not classical-record-generators — they're channel-content. A single lepton happily propagates; it only produces a detectable event when it meets something with GHZ structure (the detector). This is why we always see leptons "through" their interactions.

This is a new framing worth taking seriously. Resolution criterion: work out the ZX-calculus of a quark-only diagram versus a lepton-only diagram and check whether the former diagram admits a completed spider without additional GHZ-structure introduced, while the latter does not. I suspect this is straightforward to verify. Natural audience: the categorical quantum mechanics community (Coecke-Kissinger's students; Paquette, Gogioso, Selinger).

## 7. Consistency check: this fits the causal-stratification story

The April 10 session document notes that properties stratify by causal accessibility:

- Mass: always in causal past (gravitational)
- Electric charge: in causal past (electromagnetic)
- Spin: not in causal past until measured
- Colour: not in causal past until high-energy collision

Reading this through the spider-node lens: each observable becomes part of the observer's causal past at the moment it becomes a classical record — i.e., at the moment a spider node is fired that includes it in its tuple. Ambient gravitational and electromagnetic interactions keep firing low-energy spider nodes continuously, so mass and charge are "always on". Spin and colour require higher-energy or more specific interactions — i.e., specific spider nodes — to be promoted from amplitude structure to classical record.

The Cheshire Cat effect at the detector is what it looks like when we try to probe an observable whose spider node has not yet fired: we get weak-value structure, not a tuple entry. Once the strong measurement completes, the spider fires, and the observable joins the tuple at the event where the record is made.

## 8. Connection to Born rule and inside/outside principle

The Born rule derivation (session_summary_2026_03_27) turned on the observation that global phase is the observer's private self-referential ignorance, cannot be FANOUT-ed, and so observables must be U(1)-invariant, with quadratic being the minimum-degree invariant. The spider-bundle argument is the same machinery applied one step further: what *is* producible by FANOUT is a classical record, and classical records come as tuples because the SCFA that produces them is defined by the single-basis-element structure.

In the inside/outside language: the inside observer's classical access is tuple-access. There is no observational stance from which one could access an untupled observable, because untupled observables would be data the inside observer could not index and therefore could not be classical data for them. The tuple structure of observations is the inside observer's unavoidable form of access, forced by the self-referential structure that also forces ℂ-amplitudes in the first place.

This means: observable bundling is not an independent fact about measurement. It's the same inside-ness that gives us complex probability amplitudes, seen from the other side of FANOUT. The amplitude side is tuple-structured by virtue of being a state on a Hilbert space over ℂ. The classical side is tuple-structured by virtue of being the output of a SCFA. The FANOUT boundary maps one onto the other consistently.

## 9. What's settled, what's new, what's speculative

**Settled (either already in the framework or standard category-theoretic/quantum-foundations fact):**
- Measurement = FANOUT = SCFA spider firing
- GHZ = SCFA, W = ACFA (Coecke-Kissinger)
- Cheshire Cat = contextuality (Hance-Hofmann 2024)
- Measurement = SL(2,ℂ) boost acting on both spin and spacetime
- FANOUT as the ontological/epistemological boundary

**New identifications from this session:**
- The spider node's single-basis-element structure is the *immediate reason* for observable bundling at measurement. Not a separate postulate.
- Position as the FANOUT index — every classical record is spacetime-indexed because sharing requires agreement on "where", which is the event-structure.
- The four-fold convergence (FANOUT index + fibre-base adjacency + composition cost + SL(2,ℂ) co-transformation) explaining why the specific bundle is position + charge + mass + spin.
- GHZ-particles (quarks) are self-FANOUT-ing; W-particles (leptons) are channel-content requiring partner FANOUT. Reframes confinement as "quarks are what classical-record-making is, and you can't have half a classical record".

**Speculative / open:**
- The formalisation of "position as FANOUT index" as a theorem in categorical quantum mechanics is plausible but not written down. A clean statement would be: in an operational theory with a FANOUT primitive, the index set on which FANOUT copies must carry the structure of a pseudo-Riemannian manifold with causal order.
- Whether the quark-FANOUT / lepton-channel-content distinction gives a genuine new derivation of confinement or just rephrases the Cayley-Dickson split (ℂ vs ℂ³). The two are probably equivalent; worth checking.

## 10. For the paper

This argument deserves a paragraph or two in Paper 1, probably in the QM-derivation section alongside the Born rule. The structure would be:

> The FANOUT criterion gives measurement a specific algebraic identity: each classical record is a single spider node in a special commutative Frobenius algebra. The spider node, by definition, is a single idempotent in the preferred basis, so all commuting observables that share that basis take simultaneous definite values at the node. This is why observable properties always bundle at measurement — charge with position, mass with spin, gauge content with spacetime event — even though the Cheshire Cat effect (Aharonov et al. 2013) shows they can be separated between preparation and measurement. The bundling is the spider; weak measurement probes the pre-spider regime.

And a line for the confinement reframing, probably in Paper 2 or a discussion section:

> Because GHZ is a special Frobenius algebra and W is anti-special, quarks are the classical-record-generators of the theory while leptons are channel content. Quark confinement is the statement that fewer than three quarks cannot produce a complete classical record on ℂ³ — not a force preventing separation but a structural requirement of the SCFA.

## 11. Follow-up for next session

1. Check whether the "position as FANOUT index" statement has been made in the categorical quantum mechanics or ZX-calculus literature (Gogioso, Paquette, Coecke's recent work on spacetime-from-process). If not, this may be a publishable result on its own.
2. Work out the explicit ZX diagram for a quark-only composition (3-party GHZ with no external GHZ-input) and for a lepton-only composition (W channel terminated by a GHZ-detector). Confirm that the former closes and the latter requires external GHZ structure.
3. Consider whether this bundling argument strengthens the case for Paper 1 leading with "particles as composition rules" as the organising frame, rather than "particles as bundles of quantum numbers". The reframing is subtle but consequential: it changes the reading of every subsequent derivation.

---

*End of session document.*
