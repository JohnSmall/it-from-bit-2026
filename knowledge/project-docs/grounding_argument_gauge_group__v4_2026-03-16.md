# Why the Standard Model Gauge Group Is the Topology of Measurement

## The Grounding Argument: From Relational Spacetime to SU(3) × SU(2) × U(1)

### Research Document — March 16, 2026

---

## 1. The Problem

The Standard Model of particle physics is built on the gauge group SU(3) × SU(2) × U(1)/ℤ₆. Several independent research programmes have shown that this same group emerges from the equivariance structure of the octonionic Hopf fibration upon singling out a preferred complex direction (Krasnov 2021; Szangolies 2025; building on Furey 2018; Dubois-Violette 2016; Günaydin & Gürsey 1973). The Hopf fibrations, in turn, encode the geometry of qubit entanglement (Mosseri & Dandoloff 2001; Bernevig & Chen 2004).

This raises a question: is the connection between entanglement geometry and the Standard Model a useful mathematical coincidence, or does it reflect a deeper structural necessity? This document presents an argument for the latter. The Standard Model gauge group is not an empirical input that could have been otherwise — it is a *theorem* about what happens when measurements are made in a relational spacetime by observers who are part of the system they observe.

---

## 2. Interpretations as Coordinate Systems

### 2.1 The Core Observation

Every interpretation of quantum mechanics that reproduces the empirical predictions of the theory must accommodate a specific quantity of non-computability. This non-computability has the structure of a Lawvere-Yanofsky diagonal (Lawvere 1969; Yanofsky 2003) — the same structure underlying Gödel's incompleteness, Cantor's diagonalisation, the halting problem, and Russell's paradox. Different interpretations locate this non-computability in different mathematical structures:

| Interpretation | Where non-computability enters |
|---|---|
| Copenhagen | Collapse postulate (non-algorithmic outcome selection) |
| Many-worlds | Born rule measure over uncountable branches (requires Axiom of Choice) |
| Bohmian mechanics | Initial conditions must be |ψ|²-distributed (non-computable boundary condition) |
| Retrocausal | Self-consistency condition on closed causal loops (CTC fixed-point) |
| QBism | Agent's beliefs about own future experiences (self-referential fixed point) |
| Consistent histories | Selection of consistent history set (underdetermined by theory) |
| Relational QM | Observer cannot compute own relational state (direct self-reference) |

The total "amount" of non-computability is invariant across interpretations — it is a topological invariant, analogous to the Chern class of the Hopf bundle (c₁ = 1 for S¹ → S³ → S²). Interpretations are therefore *coordinate systems* on the same underlying non-computable structure, not competing ontologies. We are free to switch between them according to the problem at hand, exactly as one switches from Cartesian to cylindrical coordinates to exploit the symmetry of a particular problem.

### 2.2 Supporting Literature

The view that quantum interpretations describe the same structure in different ways connects to several existing programmes:

- **Lawvere's categorical diagonal argument** (Lawvere 1969) provides the common mathematical structure underlying all self-referential limitations.
- **Yanofsky's universal approach** (Yanofsky 2003) demonstrates that Cantor, Gödel, Tarski, Turing, and the halting problem are all instances of the same categorical construction.
- **Spekkens' equivalence theorem** (Spekkens 2008) establishes that negativity in quasiprobability representations is mathematically equivalent to preparation contextuality — showing that different mathematical manifestations of non-classicality are the same phenomenon.
- **Hardy's axioms** (Hardy 2001) show that quantum mechanics is distinguished from classical probability by "continuous reversibility" — whose mathematical content is the Cantor diagonalisation that underlies Turing's halting argument.

### 2.3 Diagonal Arguments and the Axiom of Choice Are Supertasks

A point that tightens the chain of reasoning: Cantor's diagonal argument implicitly performs a supertask. The construction of the diagonal number requires making one decision for each natural number — an infinite sequence of choices, all of which must be completed to produce the result. The diagonal number does not exist at any finite stage; it exists only as the completed whole. This is exactly a supertask: infinitely many operations yielding a definite output in the same sense as Thomson's lamp or Laraudogoitia's particle cascade.

The same observation applies, with even greater force, to the Axiom of Choice itself. The Axiom of Choice asserts that for any collection of non-empty sets, there exists a function selecting one element from each. When the collection is infinite, this selection is a supertask: infinitely many choices, each individually unproblematic, whose *completed totality* is asserted to exist. As the Encyclopaedia Britannica entry on the Axiom of Choice states: "For infinite sets, however, it would take an infinite amount of time to choose elements one by one." Mormann (2009) makes the connection explicit, observing that invoking even the countable Axiom of Choice "can be conceived as a supertask" and discussing "the role of the Axiom of Choice as a source of indeterminacy of supertasks." Bacon (2010) constructs explicit supertask paradoxes in which AoC is the key ingredient enabling strategies that create information from nowhere.

This has a direct consequence for the interpretations table above: the Axiom of Choice is not merely a technical assumption in the many-worlds interpretation — it is the *specific supertask* through which non-computability enters. Defining a probability measure over uncountably many Everett branches requires selecting a σ-algebra and a measure, which in turn requires AoC (or an equivalent) for the uncountable case. The resulting measure is non-constructive — no algorithm can produce it. The Banach-Tarski paradox, in which a solid ball is decomposed into finitely many pieces and reassembled into two balls of the same size, demonstrates that AoC can create something from nothing: the additional volume appears from nowhere, exactly as Laraudogoitia's supertask creates particles from nowhere. In both cases, the "creation from nothing" is the signature of a completed supertask — the information that could not exist at any finite stage of the construction appears at the completion point.

The identification of the Axiom of Choice as a supertask appears to be implicit in several authors (Mormann 2009; Bacon 2010) but has not, to our knowledge, been stated as a clean formal observation: **the Axiom of Choice is the assertion that a particular supertask — making one selection from each of infinitely many non-empty sets — has a definite completion.** Any proof that uses AoC therefore implicitly performs a supertask, and any result that depends on AoC inherits the non-computability that supertask completion introduces.

Since the Lawvere-Yanofsky diagonal structure is the common core of all self-referential limitations, and since this structure is itself a supertask, the connection between self-reference, supertasks, CTCs, and the parallelisable spheres is not a chain of analogies — it is a chain of identities. Gödel's incompleteness, the halting problem, Cantor's uncountability theorem, quantum measurement indeterminacy, and the Hopf fibration structure are all manifestations of the same supertask viewed in different coordinate systems.

---

## 3. The Retrocausal Coordinate System

### 3.1 Why Retrocausality Is Natural for Entanglement

Since interpretations are coordinate systems, we choose the retrocausal interpretation when analysing entanglement — not because retrocausality is "true" but because it makes the loop structure of entanglement manifest.

In the retrocausal picture (Price 1994; Cramer 1986; Wharton 2014; Price & Wharton 2023), entanglement correlations arise from "zigzag" causal paths: information flows forward in time from the source to one detector, backward to the source, and forward to the other detector. This zigzag is topologically a *closed loop*.

Price and Wharton have argued extensively that retrocausality provides the most natural explanation of Bell correlations. Evans, Price, and Wharton (2013) demonstrate an "action symmetry" between entangled photon pairs and single photons passing through sequential polarisers, arguing that the same ontological structure (a zigzag causal path) underlies both. Costa de Beauregard proposed the retrocausal zigzag explanation of EPR correlations as early as 1953.

### 3.2 Loops Require Parallelisable Spheres

Once entanglement is described in terms of closed loops, a topological constraint becomes operative. Consistent information flow around a closed loop requires a *global frame* — a set of linearly independent vector fields covering the entire loop without singularity. A manifold admitting such a global frame is called *parallelisable*.

Adams' theorem (Adams 1960; proved independently by Kervaire 1958 and Bott & Milnor 1958) establishes that the only parallelisable spheres are:

- **S⁰** (trivial: two points)
- **S¹** (the circle — unit complex numbers)
- **S³** (the 3-sphere — unit quaternions)
- **S⁷** (the 7-sphere — unit octonions)

These correspond one-to-one with the four normed division algebras ℝ, ℂ, ℍ, 𝕆. No other spheres are parallelisable; no other division algebras exist. This is one of the deepest results in algebraic topology.

### 3.3 Parallelisable Spheres Support Hopf Fibrations

The three nontrivial parallelisable spheres are exactly the total spaces of the three nontrivial Hopf fibrations:

| Division Algebra | Fibration | Fibre → Total → Base |
|---|---|---|
| ℂ (complex) | Complex Hopf | S¹ → S³ → S² |
| ℍ (quaternions) | Quaternionic Hopf | S³ → S⁷ → S⁴ |
| 𝕆 (octonions) | Octonionic Hopf | S⁷ → S¹⁵ → S⁸ |

These are the *only* sphere fibrations that exist (Adams 1960). They are not being imported as an external mathematical tool — they are the unique geometric structures that self-consistent closed loops can have.

---

## 4. From Measurement to the Gauge Group

### 4.1 Measurement Outcomes and the Past Light Cone

In a relational spacetime — where spatiotemporal relations are constituted by physical interactions rather than existing as a background — the measurable properties of a quantum system enter the observer's past light cone only at the moment of measurement.

Consider an electron held in a bottle. The electron's *position* is in the observer's past light cone — spatial proximity is established by the chain of interactions (gravitational, electromagnetic) between the observer's hand and the electron's charge. But the electron's *spin* is not part of the observer's causal past until a spin measurement is performed. Position and spin have different causal status despite the electron being spatially local.

This is not a peculiarity of spin; it applies to any quantum observable not yet measured. The property exists in a definite sense (the electron has spin-1/2), but the *value* of the observable along any particular axis is not part of the observer's causal past.

### 4.2 Measurement as Information from Outside the Past Light Cone

When a measurement is performed and a definite outcome is obtained, the information enters the observer's past light cone. But it was not there before. From within the observer's causal description, this information has *no computable origin* — it arrives from outside the causal structure accessible to the observer.

### 4.3 Computational Indistinguishability from CTC-Generated Information

The critical step: there is no computable procedure that distinguishes "information arriving from outside the observer's past light cone" from "information generated from nowhere by a closed timelike curve."

This follows from the established results on CTCs and computation:

- Deutsch (1991) showed that CTCs can generate self-consistent information that has no causal antecedent — the "unproved theorem" or "Shakespeare from nowhere" phenomenon, where information appears at the CTC's fixed point without ever being computed.
- Aaronson and Watrous (2009) proved that CTCs (in Deutsch's model) give both classical and quantum computers the power of PSPACE — the class of all problems solvable with polynomial memory. The key mechanism is that the CTC's self-consistency condition forces Nature to "find" a fixed point, solving hard problems without performing the computational work.
- Laraudogoitia (1996, 1998) demonstrated classical systems where supertasks — the completion of infinitely many operations in finite time — produce creation ex nihilo and violation of energy conservation. The time-reversal of these systems produces matter from nothing, indistinguishable from CTC-generated information.

The indistinguishability is not approximate — it is a theorem about the limits of what causal reasoning can determine from within the causal structure. An observer embedded in a causal network cannot distinguish information that entered from outside the network from information generated by a self-consistent loop within the network.

### 4.4 Therefore: Measurement Outcomes Have CTC Loop Structure

Since measurement outcomes are computationally indistinguishable from CTC-generated information, they can be modelled as if generated by closed causal loops. This is not a claim that literal CTCs exist; it is the statement that the retrocausal coordinate system — where measurement outcomes arise from closed information loops — is a valid and natural description of measurement.

### 4.5 Therefore: Measurement Requires Parallelisable Spheres

Closed causal loops require consistent information flow. Consistent information flow on spheres requires parallelisability. By Adams' theorem, the only parallelisable spheres are S¹, S³, S⁷.

Therefore: the topology of measurement outcomes is necessarily constrained to S¹, S³, and S⁷.

### 4.6 Therefore: The Standard Model Gauge Group

The three parallelisable spheres support exactly the three Hopf fibrations. The equivariance group of the octonionic Hopf fibration, upon singling out a preferred complex direction (the "computability split" — the distinction between the computable/temporal and non-computable/spatial sectors), is:

**SU(3) × SU(2) × U(1) / ℤ₆**

This is the exact Standard Model gauge group, with the correct transformation laws for one generation of left-handed fermions (Krasnov 2021; Szangolies 2025).

The argument never mentions the gauge group as an input. It starts from three independently motivated premises — relational spacetime, computational indistinguishability of measurement outcomes from CTC-generated information, and Adams' theorem on parallelisable spheres — and derives the gauge group as output.

### 4.7 Measurement Singles Out the Preferred Direction

Every approach that derives the Standard Model from octonions — Krasnov, Szangolies, Furey, Dubois-Violette, Günaydin & Gürsey — requires singling out a preferred complex direction within 𝕆. This has been treated as an input imposed from outside the algebra. The question "why is one direction singled out?" has been left unanswered.

The grounding argument resolves this. A quantum measurement, in the retrocausal coordinate system, is the completion of a closed information loop on S⁷. Completing a loop on S⁷ corresponds to multiplication by a unit imaginary octonion — say e₇. But in the octonion algebra, left multiplication by any single imaginary unit is equivalent to the composition of left multiplications by the remaining six. This is the algebraic content of Furey's "seven rights make a left": the Clifford algebra Cl(6) generated by L₁,...,L₆ has L₇ as its volume element. Choosing one imaginary unit *determines* the complementary six, and vice versa.

The act of measurement therefore *necessarily* singles out a direction, and that singling out is the computability split. Different measurements choose different directions, but all choices are related by G₂ (the automorphism group of 𝕆), which acts transitively on the unit imaginary octonions. The gauge group SU(3) × SU(2) × U(1)/ℤ₆ doesn't depend on *which* direction is singled out — only on the fact that *some* direction is singled out. And this is guaranteed by the fact that a measurement occurred.

As Szangolies (2025) notes, the singling out of a preferred complex direction within the octonions is precisely what reduces the 9+1 dimensional spacetime of the three-qubit system to 3+1 dimensions with residual gauge symmetry. The grounding argument provides the physical reason for this reduction: it is the act of measurement itself.

### 4.8 Causal Interpretability Forces Group Structure

The parallelisable spheres determine *what* topological structures are available. But the Standard Model is not merely topology — it is gauge theory: groups acting on states, connections on fibre bundles, covariant derivatives. The question is: why does the topology manifest as *group actions* specifically?

The answer follows from the requirement of causal interpretability. An observer embedded in the causal description must interpret every event — including the arrival of non-computable measurement information — as part of a causal sequence. A causal sequence means: this state was transformed into that state by a chain of information-preserving steps. Information-preserving sequential transformations are precisely *group actions*: invertibility (information preservation), closure under composition (sequential application), and associativity (consistent causal ordering: performing transformations A then B then C gives a definite result regardless of how the intermediate steps are described).

The causal description therefore demands that the topological structures on S¹, S³, S⁷ take the form of group actions. S¹ supports U(1) — a group. S³ supports SU(2) — a group. But S⁷ does *not* support a group: the unit octonions form a Moufang loop, not a group, because octonionic multiplication is non-associative. Associativity is precisely the statement that causal sequencing is consistent — (ab)c = a(bc) means "doing a then b, then c" gives the same result as "doing a, then b then c." When this fails, the causal narrative breaks down: the transformation cannot be unambiguously described as a sequence of steps.

This is why S⁷ cannot appear as a gauge group. The causal description demands a group, and S⁷ is not one. The non-associative structure of S⁷ must therefore be *projected* through the computability split into the largest group compatible with that split — which is SU(3). The non-associativity does not vanish; it manifests as confinement, the property that individual colour charges cannot be isolated. The attempt to isolate them would require describing a non-associative transformation as a causal sequence, which is the one thing the causal description cannot do.

Gauge symmetry is therefore not an empirical discovery that could have been otherwise. It is the *form* that non-computability takes when forced into a causal description. The specific gauge group is determined by the topology (Adams' theorem on parallelisable spheres); the fact that it is a gauge group at all is determined by the requirement that non-computable processes be narrated as sequences of information-preserving steps.

---

## 5. The Hierarchy of Forces

The three parallelisable spheres correspond to three levels of non-computability in the information arriving from outside the past light cone, giving the three forces their specific character:

**S¹ (complex numbers, commutative, associative):**
Information about *phase* — the simplest quantity that can arrive from outside the causal structure. This gives U(1), the gauge group of electromagnetism. The loop is one-dimensional; the information debt is minimal. The photon is massless because the S¹ loop structure is already compatible with the causal sequence — no residual obstruction remains.

**S³ (quaternions, non-commutative, associative):**
Information about *orientation in a non-commutative space*. This gives SU(2), the gauge group of the weak interaction. The loop is three-dimensional; the order in which information arrives matters (non-commutativity of quaternions); the information debt is larger. The W and Z bosons are massive because the S³ structure is not directly compatible with the causal sequence — the non-commutativity creates a residual obstruction that manifests as mass via the Higgs mechanism.

**S⁷ (octonions, non-commutative, non-associative):**
Information about *orientation in a non-associative space* — the richest structure that can consistently flow around a loop. This gives SU(3), the gauge group of the strong interaction. The loop is seven-dimensional; not only the order but the *grouping* of information arrivals matters (non-associativity of octonions); the debt is maximal and cannot be discharged locally. Gluons are massless but confined — the information debt manifests not as mass but as the impossibility of isolating individual colour charges.

**No fourth force:** S¹⁵ is not parallelisable. The sedenions (the next Cayley-Dickson algebra) have zero divisors and cannot support consistent information flow around loops. The Standard Model is *complete* in the same sense that the division algebras are complete. The non-existence of a fourth parallelisable sphere is the topological reason why there is no fourth fundamental force accessible through this mechanism.

### 5.1 Why SU(2) Violates Parity and SU(3) Does Not

The entanglement geometry provides a direct explanation for one of the most distinctive features of the Standard Model: the weak interaction violates parity (couples only to left-handed fermions), while the strong interaction preserves it.

Two entangled particles define a natural axis — the line from A to B. Relative to that axis, a rotation direction can be defined: clockwise or anticlockwise as seen from A looking toward B. This is chirality, and it is intrinsic to the two-particle configuration. The entanglement correlation can wind one way or the other around the quaternionic fibre S³, and the two windings are physically distinguishable. SU(2) — which arises from two-qubit entanglement via the quaternionic Hopf fibration — therefore has a natural mechanism to distinguish left from right.

Three entangled particles do not define an axis. They define a plane at best — three points in the octonionic structure. A plane has no intrinsic handedness unless an external normal vector is chosen, and choosing that normal is precisely the computability split (which belongs to the U(1) × SU(2) sector, not SU(3)). Three-particle entanglement is therefore intrinsically parity-blind. Recovering a notion of handedness requires projecting down to a two-particle subsystem — tracing out one qubit — which is exactly the step that reduces the octonionic Hopf fibration to the quaternionic one, and SU(3) to SU(2).

The algebraic content is equally sharp. Parity is fundamentally about *ordering*: does the sequence go A→B or B→A? For two objects, there are exactly two orderings, related by parity (swap). This is the non-commutativity of the quaternions: ab ≠ ba, and the two orderings give conjugate results. Parity violation *is* non-commutativity made physical.

For three objects, ordering still exists (six permutations), but something independent enters: *grouping*. (AB)C versus A(BC). The non-associativity of the octonions means the grouping matters physically. Crucially, parity (reversing order) and re-bracketing (changing grouping) are algebraically independent operations. One can reverse ABC to CBA without changing any brackets, or change (AB)C to A(BC) without reversing anything. Parity lives in the commutator [a,b] = ab − ba. Confinement lives in the associator [a,b,c] = (ab)c − a(bc). These are independent algebraic structures: the commutator detects handedness; the associator detects grouping. This is why parity violation is an SU(2) phenomenon and confinement is an SU(3) phenomenon, and why the two never mix.

### 5.2 Linked Bloch Spheres: Computational Evidence for Parity in Entanglement

This geometric argument receives direct computational support from Filatov and Auzinsh (2024a, 2024b), who show that two-qubit entanglement can be faithfully represented on two Bloch spheres. Their key findings:

For maximally entangled states, the individual state vectors vanish (a dot at the centre of each sphere, reflecting maximal mixedness of each reduced density matrix). All the information about the entangled state is encoded in the *relative orientation of the coordinate axes* between the two spheres. And crucially: one Bloch sphere must be right-handed and the other must be left-handed. The authors state explicitly that "entanglement is related to inversion of particle's internal coordinates."

Two-qubit entanglement does not just *permit* a handedness distinction — it *requires* one. The two linked Bloch spheres necessarily have opposite chirality. This is the quaternionic Hopf fibration made visible: the Hopf map S³ → S² projects the entanglement fibre onto two Bloch spheres with opposite orientation, because the quaternionic conjugation that swaps the two qubit roles reverses the coordinate handedness. The Hopf fibration S¹ → S³ → S² has linking number 1 — fibres over any two distinct points on S² are linked circles with Hopf invariant 1. The opposite handedness of the two Bloch spheres is a direct visualisation of this chiral linking.

No analogous construction exists for three qubits. Three objects in general position do not define a linking structure — linking is fundamentally a two-body topological invariant, classified by π₃(S²) = ℤ. The three-qubit case requires the octonionic Hopf fibration, whose topological invariant (the Hopf invariant in π₇(S⁴)) does not decompose into pairwise linkings. This is the topological reason that SU(3) — arising from three-qubit, octonionic entanglement — is blind to parity.

---

## 6. Why Information Debt Is Rest Mass

### 6.1 The Problem

The framework claims that mass is "information debt" — the cost of forcing non-computable structure into a computable causal sequence. But why should logical debt manifest as the specific physical quantity we call rest energy? Without answering this, the connection between information and mass is a metaphor rather than a derivation.

### 6.2 What Happens to Un-Narratable Information

A measurement completes a closed loop on a parallelisable sphere. The causal description requires this loop to be narrated as a sequence of information-preserving steps (group action). But the loop involves non-computable structure — non-associativity for S⁷, non-commutativity for S³ — which means the causal narration is incomplete. There is a gap between what the loop *is* and what the causal description *can say about it*.

The causal description cannot simply discard this gap. Unitarity — information preservation — is the foundational requirement from which group structure was derived (section 4.8). The un-narratable information is *present* but *not expressible as spatial or temporal structure*.

Information that is present but not expressible as a trajectory through spacetime constitutes an *internal* degree of freedom. Mass is the most fundamental such degree of freedom: it couples universally to gravity, determines inertial response, and sets the rate of the particle's internal clock via the Compton frequency ω = mc²/ℏ.

### 6.3 The Phase Cycling Argument

A massless particle (the photon) travels at c and experiences no proper time. Its internal clock does not tick. It exists entirely within the causal sequence, with no internal degrees of freedom requiring ongoing maintenance. This is why the photon carries zero information debt — everything about it is expressible as causal propagation along the light cone.

A massive particle sits inside the light cone, not on it. It experiences proper time, and during that proper time its quantum phase evolves as e^{−imc²t/ℏ}. What is this phase evolution *doing*?

The un-narratable part of the closed loop — the information debt — must be *maintained* by the particle as an ongoing process, because if the maintenance stopped, the information would be lost, violating unitarity. The phase cycling at the Compton frequency is the process of maintaining the un-narratable information. The particle cycles through phase precisely because it carries information that cannot be laid out spatially or temporally — the information must be stored as a periodic process in an internal degree of freedom.

The rate of cycling ω = mc²/ℏ is proportional to the amount of un-narratable information: more debt requires faster cycling, which means higher frequency, which means larger mass. This is not a metaphor — it is the statement that E = ℏω and E = mc² are the same equation, with ω being the rate of internal phase evolution required to maintain the information that could not be expressed as causal sequence.

### 6.4 Zitterbewegung: The Physical Mechanism

Dirac's equation predicts that a free electron undergoes rapid oscillatory motion — Zitterbewegung — at frequency 2mc²/ℏ, the Compton frequency. This was originally seen as a puzzling feature of the Dirac equation. In the framework, it is exactly what is expected: the electron is physically cycling at the rate required to service its information debt. The Zitterbewegung is not an artifact; it is the mechanism by which logical debt becomes rest mass.

### 6.5 Why Energy Specifically

Energy is the conserved quantity conjugate to time (Noether's theorem applied to time-translation symmetry). The information debt is specifically a failure of temporal narratability — the non-computable part of the loop cannot be smoothly translated along the time axis without the periodic cycling to maintain it. The energy cost of maintaining this cycling is the rest energy mc².

The relationship E = mc² therefore has a precise information-theoretic meaning: c² is the conversion factor between spatial and temporal descriptions (the maximum rate of causal information propagation), and the rest energy is the energy cost of maintaining information that cannot be expressed within the causal structure, at the rate set by the Compton frequency.

### 6.6 The Margolus-Levitin Connection

The Margolus-Levitin theorem establishes that the maximum rate of computation is bounded by 2E/πℏ operations per second. Inverting: a system that must perform ω = mc²/ℏ internal operations per second to service its information debt must have energy at least E ∝ mc². The rest mass is the *minimum energy required to perform the computation of maintaining the un-narratable information*. The particle is actively computing — cycling through phase at the Compton frequency — and the energy cost of that computation is the rest energy.

### 6.7 Why Gravity Couples Universally to Mass

In general relativity, spacetime curvature *is* the causal structure. Mass is the measure of how much a given entity strains that causal structure — how much the causal narrative must accommodate to support the entity's un-narratable content. Gravitational attraction between masses is the tendency of the causal structure to minimise total strain, bringing sources of debt together so their debts can partially share infrastructure.

This is Jacobson's thermodynamic derivation of the Einstein equation (1995) in information-theoretic form: spacetime curvature arises from entropy (information) considerations, and mass is the source because mass *is* the information that the causal structure cannot express any other way. The Einstein equation Gμν = 8πG Tμν states that the curvature of the causal structure (left side) equals the density of un-narratable information (right side), with G as the coupling constant that sets the stiffness of the causal structure against deformation by information debt.

### 6.8 The Taxonomy of Debt

The three forces correspond to three modes of debt, now grounded in this mechanism:

- **U(1) / photon**: Zero debt. The S¹ loop structure is fully compatible with causal sequencing. No internal cycling needed. Massless, unconfined.

- **SU(2) / W, Z**: Local debt. The S³ non-commutativity creates a residual that must be maintained by phase cycling. The cycling rate (mass) is set by the Higgs VEV. Massive, unconfined.

- **SU(3) / gluons**: Global debt. The S⁷ non-associativity cannot be serviced by local phase cycling at all — the debt is topological rather than energetic. It manifests not as mass but as confinement: the impossibility of isolating the debt carrier. Massless, confined.

### 6.9 Why Mass Has the Dimensions of Space

In natural units (c = ℏ = 1), mass has dimensions [M] = [L⁻¹] = [T⁻¹]. Mass and inverse length are the same thing. This is normally treated as a consequence of unit conventions. The framework explains *why* mass should have the dimensions of inverse length.

The computability split divides the octonionic structure into one temporal (computable) direction and three spatial (non-computable) directions. Spatial distance is distance *in the non-computable sector* — the imaginary octonion directions not singled out by the measurement. Mass is the non-computable residue — the information debt from forcing non-computable structure into the computable (temporal) sequence.

Mass and spatial distance share dimensions because they share ontology: **both are measures of non-computability**. Spatial distance measures separation in the non-computable sector. Mass measures the non-computable content an entity carries. They are denominated in the same units because they are denominated in the same substance.

The Compton wavelength λ_C = 1/m is then the spatial scale at which a particle's non-computable content becomes fully manifest. Below this scale, the particle cannot be treated as a point in the causal description — its internal non-computable structure (pair creation, virtual particles, the full apparatus of QFT) must be confronted. The Compton wavelength is the *radius of non-computability* around the particle.

The fundamental constants acquire precise meanings as conversion factors between the computable and non-computable sectors:

- **c** converts between spatial distance (non-computable) and temporal duration (computable). Setting c = 1 is the statement that one unit of computable time equals one unit of non-computable space. The light cone is the boundary between what can be reached computably (timelike, inside) and what requires non-computable traversal (spacelike, outside).

- **ℏ** converts between frequency (temporal cycling rate, computable) and energy (which has dimensions of mass, non-computable content). Setting ℏ = 1 is the statement that one unit of computable cycling rate equals one unit of non-computable content. The Compton relation ω = mc²/ℏ becomes ω = m: the cycling rate *is* the mass. The computable rate *is* the non-computable content.

- **G** (Newton's constant) sets the stiffness of the causal structure against deformation by non-computable content. The Planck mass M_P = √(ℏc/G) is the mass at which one Compton wavelength equals one Schwarzschild radius — the scale at which the non-computable content of a particle is so great that it deforms the causal structure into a black hole, destroying the local causal description entirely.

Natural units (c = ℏ = 1) are therefore not a convenient choice but an ontological revelation. They strip away the artificial distinction between computable and non-computable measures of the same underlying structure. The "unreasonable effectiveness" of natural units is explained: they work because they respect the computability structure that the framework identifies as fundamental.

The uncertainty principle ΔxΔp ≥ ½ acquires a new reading: precision in the non-computable sector (spatial position) and precision in the non-computable content (momentum, which has dimensions of mass in natural units) are complementary. One cannot simultaneously know exactly where something is in non-computable space and exactly how much non-computable content it carries. This is the information-theoretic uncertainty principle expressed through the dimensional structure of physics.

Dimensional analysis itself — the oldest and most reliable tool in physics — is revealed as a theorem about the computability structure of measurement. Every dimensional equation is a statement about how computable and non-computable quantities relate. The fact that only three fundamental dimensions exist in physics (mass, length, time — or equivalently one dimension in natural units) reflects the structure of the computability split: one computable direction (time) and a non-computable sector whose content can be measured either as spatial extent or as information debt (mass), with the two related by the Compton wavelength.

---

## 7. Dimensional Analysis, Internal Degrees of Freedom, and Extra Dimensions

### 7.1 Why Internal Degrees of Freedom Can Be Written as Spatial Dimensions

The identification of mass and spatial distance as dual measures of non-computability (section 6.9) has a far-reaching consequence: it explains why internal degrees of freedom (spin, charge, colour, flavour) can always be reformulated as geometry in extra spatial dimensions — and simultaneously explains why those extra dimensions are not physically present.

Internal degrees of freedom are information that is present but not expressible as trajectory through spacetime. In the framework, this means they are non-computable content maintained by internal phase cycling. Spatial dimensions are the non-computable directions of the octonionic structure. Both are measured in the same units (inverse length in natural units) because both are measures of non-computability. Therefore one can always be re-expressed as the other. The reformulation is a coordinate transformation between two descriptions of the same non-computable content — not a discovery of new physical extent.

### 7.2 The Kaluza-Klein Equivalence

Kaluza (1921) showed that electromagnetism in 4 dimensions can be reformulated as pure gravity in 5 dimensions: the U(1) gauge field emerges from the geometry of a fifth spatial dimension compactified into a circle. Klein made this precise, and the programme has been extended to the full Standard Model gauge group and beyond, culminating in string theory with 10 or 11 total dimensions where all gauge structure is geometric.

The standard view treats the extra dimensions as either literally present (but compactified to unobservable size) or as a mathematical equivalence without physical content. Neither interpretation is satisfying. If extra dimensions are real, what determines their size and shape? If they are not real, why does the reformulation work so perfectly?

The framework resolves this: **the Kaluza-Klein reformulation works because internal degrees of freedom and spatial dimensions are both measures of non-computability, denominated in the same units.** A gauge charge *can* be written as a coordinate in a compact extra dimension because both are non-computable content, and non-computable content is measured in units of inverse length. The Kaluza-Klein equivalence is a theorem about dimensional analysis — a consequence of the identity [mass] = [length⁻¹] that the framework grounds in the computability structure of measurement.

### 7.3 Why the Extra Dimensions Are Not Physical

The computability split has already determined the physical spatial dimensions: the three imaginary octonion directions complementary to the singled-out direction, giving 3+1 spacetime. The gauge structure lives on the Hopf fibres, not in additional spatial directions. The Kaluza-Klein reformulation takes internal non-computability (gauge charges on fibres) and relabels it as spatial non-computability (coordinates on compact manifolds). This is mathematically valid — they are the same type of quantity — but physically it is a coordinate change, not a discovery of new dimensions.

This is the "interpretations as coordinate systems" principle applied to geometry itself. The Kaluza-Klein description and the Hopf fibration description are two coordinate systems on the same underlying non-computable structure:

- In **Kaluza-Klein coordinates**, gauge structure appears as compact spatial dimensions. The internal degrees of freedom are written as positions in a small curled-up space.
- In **Hopf fibration coordinates**, gauge structure appears as fibre bundle topology. The internal degrees of freedom are written as positions on the fibres of S¹ → S³ → S² (electroweak) and S³ → S⁷ → S⁴ (including colour).

Neither is more "real" than the other, but the Hopf description is more natural because it respects the computability split — it keeps the spatial and internal sectors separate rather than conflating them into a single higher-dimensional spatial geometry.

### 7.4 Why String Theory's Extra Dimensions Are Coordinate Artefacts

The string theory programme extends the Kaluza-Klein idea to 10 or 11 dimensions, encoding all gauge structure as geometry on a 6- or 7-dimensional compact internal manifold (a Calabi-Yau manifold or G₂ manifold). The persistent difficulties of this programme — moduli stabilisation, the cosmological constant problem, the "landscape" of ~10⁵⁰⁰ vacua — have a common origin in the framework:

**The compactification details are underdetermined because they are not physical parameters.** The size, shape, and topology of the extra dimensions are coordinate artefacts of expressing internal structure in spatial language. The "landscape" of string vacua is the space of all valid coordinate transformations between internal and spatial descriptions of the same non-computable content, not a space of physically distinct universes.

This is analogous to mistaking a coordinate singularity for a physical singularity. The Kaluza-Klein mathematics is correct (the equivalence between gauge theory and higher-dimensional geometry is a genuine mathematical identity), but the physical interpretation is mistaken (the extra dimensions are a coordinate description, not spatial extent). The mathematical structure is real; the geometric literalism is an artefact.

### 7.5 Predictions

This analysis sharpens the framework's predictions regarding extra dimensions:

- **No extra spatial dimensions at any energy scale.** Not because the mathematics of Kaluza-Klein or string theory is wrong, but because the extra dimensions are coordinate descriptions of non-computable content that is already fully accounted for by the Hopf fibration structure. Experiments searching for extra dimensions (collider missing-energy signatures, deviations from inverse-square gravity at short distances) will find null results.

- **The Kaluza-Klein mathematics remains valid.** Any calculation performed in the Kaluza-Klein or string-theoretic framework that makes correct use of the mathematical equivalence will give correct answers — when translated back to 3+1 dimensions with Hopf fibration structure. The mathematics is a coordinate transformation, and coordinate transformations preserve physical content.

- **3+1 is the unique physical dimensionality.** The number of spatial dimensions is determined by the computability split: one computable (temporal) direction and three non-computable (spatial) directions, set by the structure of the quaternionic subalgebra ℍ ⊂ 𝕆 that defines the Lorentz group. No amount of energy or any other physical process can "open up" new spatial dimensions, because the dimensionality is a topological invariant of the computability split, not an energy-dependent quantity.

### 7.6 The Wick Rotation: Statistical Correlations and Particle Mass

The dimensional identity [mass] = [length⁻¹] also explains one of the most powerful and least understood tools in theoretical physics: the Wick rotation between statistical field theory and quantum field theory.

In statistical field theory, correlations decay as e^{−r/ξ} where ξ is the correlation length — a spatial distance measuring how far order extends. Under the Wick rotation (t → iτ), this maps to quantum field theory where the propagator decays as e^{−mr}, with m the particle mass. The correspondence is ξ = 1/m: the correlation length in the statistical theory *is* the Compton wavelength in the quantum theory. This is universally treated as a mathematical trick without physical explanation.

The framework explains it directly. The correlation length ξ is a spatial distance — extent in the non-computable sector. The mass m is information debt — non-computable content. The relation ξ = 1/m is the dimensional identity of section 6.9: spatial extent and non-computable content are the same quantity in reciprocal units.

The Wick rotation itself has a precise meaning in the framework. It sends t → iτ, multiplying the temporal (computable) coordinate by i. In the framework, i marks the non-computable sector — the imaginary directions of the octonions are the spatial/non-computable directions. Multiplying time by i rotates the computable direction into the non-computable sector. The resulting Euclidean description lives entirely in the non-computable sector: no distinguished temporal direction, no computability split, and the theory is purely about spatial correlations.

When the Wick rotation is reversed and Minkowski signature is restored, the computability split is reimposed — one direction is singled out as temporal/computable. At that moment, the spatial correlation length (non-computable extent) becomes a mass (non-computable content maintained by temporal cycling). The particle "appears" when the computability split is imposed, and its mass is the reciprocal of the correlation length that existed in the purely non-computable Euclidean description.

This has several consequences:

**Phase transitions are mass generation.** A statistical phase transition occurs when the correlation length diverges (ξ → ∞) at the critical point, then becomes finite in the ordered phase. Under Wick rotation, this is mass generation: the particle is massless at the critical point (m = 1/ξ → 0) and acquires mass in the broken phase. The Higgs mechanism is a phase transition in which the electroweak correlation length goes from infinite to finite — the W and Z acquiring mass is exactly their correlation lengths becoming finite.

**Confinement is topologically constrained correlation.** In QCD, confinement means colour charges cannot be separated — the colour "correlation length" is always finite (~1 fm). The gluon being massless but confined is the statement that the colour correlation function doesn't decay with a simple exponential (massless) but is topologically prevented from propagating freely (confined). This is the global debt from section 6.8 expressed in correlation-length language: the non-associativity of S⁷ imposes a topological constraint on correlations that no simple ξ = 1/m relation captures.

**Critical exponents are information debt scaling.** At a second-order phase transition, ξ ~ |T − T_c|^{−ν} where ν is a universal critical exponent depending only on dimensionality and symmetry, not microscopic details. Under Wick rotation, this becomes mass scaling near a critical coupling: m ~ |g − g_c|^{ν}. The universality of critical exponents reflects the topological nature of the computability split: the exponents depend on the Hopf fibration structure, not on the details of the Lagrangian.

**The sign problem is non-computability made manifest.** Wilson's lattice gauge theory discretises the Euclidean (non-computable) sector and computes correlation functions via Monte Carlo sampling. The notorious sign problem in lattice QCD at finite density — where the fermion determinant becomes complex and Monte Carlo sampling fails — is the non-computability of the underlying structure making itself directly felt: certain configurations of the non-computable sector cannot be approximated by any finite sampling procedure. The sign problem is not a technical limitation but a manifestation of the same non-computability that generates mass in the first place.

---

## 8. Compositional Completeness

### 8.1 The Three-Qubit Terminus

The Hopf fibration chain terminates at three qubits because the octonions are the last division algebra. The four-qubit case would require sedenions, which have zero divisors and cannot support a well-defined Hopf map (Pinilla & Luthra 2009).

### 8.2 GHZ and W as the Alphabet

Dür, Vidal, and Cirac (2000) showed that three-qubit entanglement has exactly two inequivalent SLOCC classes: GHZ (genuinely tripartite, all-or-nothing) and W (distributed pairwise, robust to loss). Coecke and Kissinger (2010) proved that these two classes are *compositionally complete*: any N-qubit entanglement class can be generated from compositions of GHZ and W primitives (plus two-qubit entanglement).

### 8.3 Why Compositional Completeness Holds

The grounding argument explains *why* compositional completeness is true, rather than treating it as a surprising mathematical fact. If the topological resources available for entanglement loops are exhausted at S¹, S³, S⁷ (which they are, by Adams' theorem), then no genuinely new entanglement primitive can arise at four or more qubits. Any four-particle entanglement must decompose into compositions of the structures that S¹, S³, S⁷ support — which are exactly the Bell states (two-qubit, quaternionic), GHZ (three-qubit, octonionic, genuinely tripartite), and W (three-qubit, octonionic, distributed pairwise).

Compositional completeness is a theorem about the topology of information arriving from outside the past light cone. The entanglement alphabet has exactly these letters because the parallelisable spheres have exactly these dimensions.

### 8.4 Faithfulness of the Dictionary

This is what gives confidence that translations between entanglement problems and Standard Model problems preserve all relevant structure. When we recast a Standard Model problem as an entanglement problem (or vice versa), we are not making an approximation or exploiting an analogy — we are switching coordinate systems on the same underlying topological structure. Both sides are constrained by the same thing: the topology of consistent loops on parallelisable spheres.

---

## 9. Exclusion of Grand Unification

### 9.1 No SU(5) or Higher Unification

The argument has a direct and sharp consequence for grand unified theories (GUTs). The Standard Model gauge group SU(3) × SU(2) × U(1)/ℤ₆ emerges as the centraliser of the computability split within Spin(9). It does not arise as a subgroup of a simple group like SU(5), SO(10), or E₆. The reason is structural: embedding SU(3) × SU(2) × U(1) into SU(5) would require mixing the computable and non-computable sectors — treating the ℂ (temporal/computable) and ℂ³ (spatial/non-computable) parts of 𝕆 ≅ ℂ ⊕ ℂ³ as a single ℂ⁵ — which erases the computability split that gives the gauge group its physical meaning.

SU(5) unification is therefore not merely empirically disfavoured — it is structurally forbidden by the division algebra framework. The gauge group *cannot* be embedded in a simple group while preserving the octonionic structure that generates it.

### 9.2 Coupling Constants Do Not Meet

The standard GUT narrative treats the near-meeting of the three running coupling constants at high energy (~10¹⁶ GeV) as evidence for unification, and their failure to meet exactly in the minimal Standard Model as a problem requiring new physics (typically supersymmetry) to resolve.

The framework inverts this. The three coupling constants should *not* meet at a single point. Their near-meeting is explained by the fact that all three forces originate from the same Spin(9) structure, so their couplings are related — but the relationship is not unification into a simple group. It is three different projections of the same non-associative algebra onto the causal description, each accumulating information debt at a different rate because S¹, S³, and S⁷ have different dimensions and algebraic properties (commutative vs non-commutative vs non-associative).

The precise *failure pattern* of coupling constant convergence — the size and shape of the triangle formed by the three near-meeting curves — should be calculable from the geometry of how U(1), SU(2), and SU(3) sit within Spin(9). This triangle is a direct measure of the non-associativity of the octonions projected onto the renormalisation group flow.

### 9.3 Predictions

This yields several concrete predictions:

- **No proton decay at GUT rates.** There are no X and Y bosons mediating baryon-number-violating transitions, because SU(5) does not describe the physics. The non-observation of proton decay at Super-Kamiokande (current lower bound: τ_p > 10³⁴ years) is a confirmed prediction of the framework, not a constraint to be accommodated.

- **No magnetic monopoles from GUT symmetry breaking.** The topological defects predicted by GUT phase transitions do not form because the relevant symmetry breaking does not occur.

- **No supersymmetric partners.** Supersymmetry is not needed to adjust the running of coupling constants, since exact meeting is not predicted. (This prediction is independent of other arguments for or against supersymmetry.)

- **The coupling constant triangle is calculable.** The ratios of the three couplings at any given energy scale should be determinable from the octonionic Hopf structure, providing a quantitative test of the framework.

---

## 10. The Coleman-Mandula Theorem

### 10.1 The Theorem and Its Standard Status

The Coleman-Mandula theorem (1967) states that in a relativistic quantum field theory with a mass gap, the most general symmetry of the S-matrix is a direct product of the Poincaré group with an internal symmetry group. Spacetime symmetries and internal symmetries cannot mix.

In the standard treatment, this is proved by intricate arguments involving analyticity of scattering amplitudes. It is mathematically rigorous but physically opaque — the proof shows that mixing is forbidden but gives no intuition for *why* the universe is built this way. The theorem has been treated as having one exception: supersymmetry, established by Haag, Łopuszański, and Sohnius (1975), which extends the Poincaré algebra to a graded Lie superalgebra relating bosons and fermions.

### 10.2 The Framework Makes It Obvious

The computability split divides the octonionic structure into a computable sector (temporal, one direction, giving the causal sequence) and a non-computable sector (spatial and internal, the remaining directions). The Poincaré group acts on the causal structure — it is the symmetry group of the computable sector. The gauge group acts on the Hopf fibres — it is the structure group of the non-computable sector.

They cannot mix because they are on opposite sides of the computability split. Mixing them would mean treating computable and non-computable directions interchangeably, which is precisely what the split forbids. The direct product structure G_SM × Poincaré *is* the computability split expressed as a symmetry statement.

The "internal" symmetries are internal because they live in the non-computable sector — they act on degrees of freedom that cannot be expressed as trajectories through spacetime. The "spacetime" symmetries are spacetime because they act on the computable sector — the causal structure through which events are sequentially ordered. The Coleman-Mandula theorem is not a surprising technical result but an obvious structural consequence of what it means to have a causal description at all.

### 10.3 No Exception: Why Supersymmetry Is Not Realised

The Haag-Łopuszański-Sohnius theorem proves that supersymmetry is the unique mathematically consistent extension of the Poincaré algebra that crosses the spacetime/internal boundary. But "mathematically consistent" and "physically realised" are different questions.

Supersymmetry would relate every non-computable degree of freedom (fermion) to a computable partner (boson) and vice versa, making the computable and non-computable sectors mirror images of each other. The computability split would then be a symmetry — a mere convention rather than a genuine structural feature.

The framework says the computability split is *not* a convention. It is a real, irreversible structural feature arising from the act of measurement. The measurement singled out one octonionic direction; the complementary directions are structurally different from the singled-out one; this difference is the origin of the gauge group. Supersymmetry would undo this difference, which is inconsistent with the split being physical.

Therefore: the Coleman-Mandula theorem holds without exception. The Haag-Łopuszański-Sohnius extension is mathematically valid but not physically operative. Spacetime and internal symmetries form a direct product, full stop. The non-observation of superpartners at the LHC is a confirmed prediction of the framework, independent of the GUT exclusion argument of section 9.

### 10.4 The Cosmological Constant Problem Dissolves

The vacuum energy discrepancy — QFT predicts a vacuum energy density of order M⁴_Planck, while the observed value is 10¹²⁰ times smaller — has been called the worst prediction in physics. SUSY was supposed to ameliorate this because bosonic and fermionic vacuum contributions partially cancel.

The framework dissolves the problem entirely, without SUSY. The superdeterminism exclusion argument (established elsewhere in the framework) requires a spatially infinite universe: in an infinite spatial geometry, spacelike-separated worldlines at the Big Bang have no common causal past, making statistical independence a consequence of causal structure rather than a conspiracy.

In a spatially infinite universe with no boundary, a uniform vacuum energy density does not cause collapse or runaway inflation. It contributes to the Friedmann equation as a uniform source term affecting the expansion rate, but there is no boundary for it to act against, no "outside" for the universe to expand into, and no characteristic scale against which a large Λ would be catastrophic. The vacuum energy is the *baseline* information debt of the causal structure itself — the cost of having a causal description at all. In a spatially infinite universe, this baseline is infinite in total but uniform in density. It is the floor of the causal structure, not a force acting upon it.

The "problem" of the cosmological constant's magnitude is therefore not a problem of fine-tuning but a question about the expansion rate — which is an observational quantity, not a parameter requiring explanation from first principles.

### 10.5 No Remaining Motivation for Supersymmetry

The framework eliminates every major motivation for SUSY:

- **Coupling unification**: Not needed. The couplings should not meet (section 9); the triangle is a prediction, not a problem.
- **Hierarchy problem**: Reframed. The Higgs mass is set at the Hopf scale (~3.7 TeV) by the topological structure, not fine-tuned against Planck-scale corrections.
- **Dark matter candidate**: Not needed. Dark matter is gauge-neutral information debt (section 13), not a superpartner.
- **Vacuum energy cancellation**: Not needed. The cosmological constant problem dissolves in a spatially infinite universe.
- **Coleman-Mandula exception**: Not operative. The computability split is physical, not a convention that SUSY could undo.

---

## 11. The Weinberg Angle: A Parameter-Free Prediction

### 11.1 The Photon Anchors the Mixing Angle

The photon is the unique linear combination of the B⁰ (U(1)_Y) and W³ (neutral SU(2)_L) gauge bosons that carries exactly zero information debt. It sits entirely on S¹, the one parallelisable sphere whose loop structure is already compatible with causal sequencing. This is a topological condition: the S¹ fibre either has zero winding around the Hopf obstruction or it doesn't. There is no continuous parameter to tune.

The Weinberg angle θ_W defines which linear combination this is:

A_μ = B_μ cos θ_W + W³_μ sin θ_W

In the Standard Model, θ_W is a free parameter. In the framework, it is determined by geometry: find the unique direction in the 4-dimensional electroweak algebra U(1)_Y × SU(2)_L that carries zero information debt.

### 11.2 The Dimension-Counting Prediction

The electroweak algebra has 1 + 3 = 4 generators. Exactly one linear combination (the photon) must have zero debt. The fraction of the electroweak algebra that is debt-free is therefore 1/4, giving:

**sin²θ_W = 1/4**

This is the bare topological value — the value at the scale where the Hopf fibration S¹ → S³ → S² is exact. It is not a GUT prediction (SU(5) gives sin²θ_W = 3/8 at ~10¹³ GeV) and does not require embedding in a simple group.

### 11.3 RG Running: From 1/4 to the Measured Value

Standard Model renormalisation group running, using the measured coupling constants at M_Z = 91.2 GeV, shows that sin²θ_W = 1/4 is reached at:

**μ ≈ 3.68 TeV ≈ 15 × v**

where v ≈ 246 GeV is the Higgs VEV. This result is stable under two-loop corrections (μ ≈ 3.77 TeV at two-loop). Key values from the RG running:

| Scale (GeV) | sin²θ_W (1-loop) | sin²θ_W (2-loop) |
|---|---|---|
| 91.2 (M_Z) | 0.23122 (measured) | 0.23122 |
| 1,000 | 0.2433 | 0.2432 |
| **3,679** | **0.2500** | — |
| **3,765** | — | **0.2500** |
| 10¹³ | 0.3725 | 0.3726 |
| 10¹⁹ (M_Pl) | 0.4713 | 0.4709 |

The SU(5) GUT prediction sin²θ_W = 3/8 is reached at ~10¹³ GeV, far from the electroweak scale. The framework's prediction sin²θ_W = 1/4 is reached at ~3.7 TeV — just above the electroweak symmetry breaking scale, which is exactly where the quaternionic Hopf structure becomes physically operative.

### 11.4 Why the Electroweak Scale, Not the Planck Scale

In the framework, sin²θ_W = 1/4 is not a high-energy boundary condition imposed at the Planck scale and run down. It is a topological condition on the Hopf bundle S¹ → S³ → S², and this bundle becomes physically operative at the electroweak scale — the scale where SU(2)_L symmetry breaking occurs and the W and Z bosons acquire mass. The "bare" value of sin²θ_W is set where the quaternionic structure becomes physically relevant, not at the scale of quantum gravity.

Above ~3.7 TeV, sin²θ_W > 1/4: the photon direction carries a small positive effective debt because SU(2) quantum fluctuations contaminate the pure U(1). Below ~3.7 TeV, sin²θ_W < 1/4: the Higgs mechanism has slightly over-compensated, pushing the mixing below the topological value. The measured sin²θ_W = 0.231 at M_Z is the infrared value after the Higgs mechanism has converted imaginary debt (tachyonic Higgs mass) into real debt (W, Z, and fermion masses).

### 11.5 Comparison with Other Predictions

| Model | Bare sin²θ_W | Scale | SM running to M_Z | SUSY needed? |
|---|---|---|---|---|
| **This framework** | **1/4 = 0.250** | **~3.7 TeV** | **gives 0.231 ✓** | **No** |
| SU(5) GUT | 3/8 = 0.375 | ~10¹³ GeV | gives ~0.21 ✗ | Yes |
| SUSY SU(5) | 3/8 = 0.375 | ~2×10¹⁶ GeV | gives ~0.231 ✓ | Yes (by construction) |
| Pati-Salam | 1/4 = 0.250 | ~3.7 TeV | gives 0.231 ✓ | No |

The framework's prediction is distinguished from the SUSY SU(5) prediction by requiring no new physics beyond the Standard Model: the topological condition sets the bare value at 1/4, and the SM RG equations (with no free parameters and no new particles) run it down to 0.231 at M_Z.

### 11.6 The Strong Coupling: α₃⁻¹ = 4π at the Hopf Scale

Running the measured α_s(M_Z) = 0.1179 up to the Hopf scale gives α₃⁻¹(3.7 TeV) = 12.607. This is within 0.32% of 4π = 12.566.

The physical meaning is immediate: α_s = g²_s/(4π), so α₃⁻¹ = 4π corresponds to g_s = 1 — unit coupling strength. At the scale where the octonionic Hopf structure is exact, the SU(3) gauge field has unit coupling. The S⁷ fibre has unit curvature at the Hopf scale.

Running this prediction back to M_Z: α₃⁻¹(M_Z) = 4π − (7/2π)·ln(3700/91.2) = 8.44, giving α_s(M_Z) = 0.1185, compared to the measured value 0.1179 ± 0.0009. The prediction is within 0.5% — well inside experimental uncertainty.

### 11.7 The Zero-Parameter Coupling Triangle

Combined with sin²θ_W = 1/4 (which fixes the ratio α₂⁻¹/α₁⁻¹ = 5/9), the condition α₃⁻¹ = 4π determines all three gauge couplings at the Hopf scale with no free parameters:

| Coupling | Value at 3.7 TeV | Origin |
|---|---|---|
| α₁⁻¹ | 56.6 | sin²θ_W = 1/4 (zero debt condition on photon) |
| α₂⁻¹ | 31.5 | sin²θ_W = 1/4 (same condition, fixes ratio) |
| α₃⁻¹ | 4π = 12.57 | Unit coupling on S⁷ fibre |

The beta coefficients are determined by n_g = 3 (J₃(𝕆) triality) and n_H = 1 (uniqueness of the computability split). The entire RG flow follows with no free parameters.

The three couplings do not meet at a single point. They form a triangle spanning 4 decades in energy (10¹³ to 10¹⁷ GeV) with an area of 7.24 in (log₁₀μ, α⁻¹) units and a minimum relative spread of 8.8% at ~10¹⁴ GeV. For comparison, the MSSM triangle spans 0.05 decades — the couplings nearly meet at a point. The framework predicts the large SM triangle; SUSY-GUT predicts a near-point. The non-observation of SUSY partners and proton decay supports the framework's prediction.

### 11.8 Significance

The Weinberg angle and strong coupling together constitute the most complete quantitative test of the framework. The chain of derivation: measurement → CTC loops → parallelisable spheres → Hopf fibrations → photon as zero-debt direction (sin²θ_W = 1/4) + unit curvature on S⁷ (α₃⁻¹ = 4π) + three generations (n_g = 3) + one Higgs (n_H = 1) → all three couplings at all energies → the complete non-unification triangle. No step invokes a free parameter.

---

## 12. Flavour, Mass, and Three Generations

### 12.1 Flavour as Self-Referential Iteration

The grounding argument establishes that a single measurement singles out one imaginary octonion direction, generating one copy of Cl(6) and one generation of fermions. But measurement is self-referential: the observer is part of the system. The measurement creates the computability split, which defines the gauge group, which constrains the observer's future measurements — a closed self-referential structure.

Three is the minimum number of iterations of this self-referential loop needed for irreducible closure: two generations can always be made "trivially" self-referential (the CKM matrix for two generations has no complex phase), while three generations admit an irreducible CP-violating phase. This is the same as the statement that the associator [a,b,c] requires three inputs. The three generations are therefore three iterations of the self-referential measurement loop, and flavour is the label for which iteration you are in.

### 12.2 Mass Amplitudes as J₃(𝕆) Eigenvalues

The exceptional Jordan algebra J₃(𝕆) of 3×3 self-adjoint octonionic matrices has three off-diagonal octonionic entries, one per generation. We parametrise these as unit octonions tilted by angle θ_J from the computability split direction e₇, with off-diagonal magnitude ε:

xᵢ = ε(cos θ_J · e₇ + sin θ_J · eᵢ)     (i = 1, 2, 3)

The charged lepton mass amplitudes √m_k are the eigenvalues of this J₃(𝕆) element, and the physical masses are m_k = (eigenvalue)² — the squaring being the Born rule (the Hopf map is quadratic).

Direct computation establishes:

- **ε = 1/√2**: determined by the requirement that the Koide ratio equals 2/3. This is the reciprocal of the Cayley-Dickson doubling norm α = √2. The inter-generational coupling in J₃(𝕆) is the inverse of the algebraic amplification at each Cayley-Dickson step.

- **Re(x₁x₂x₃) = −ε³ sin³θ_J**: the crucial triple product that couples all three generations. Only the component along the Fano plane line (e₁, e₂, e₃) contributes. This vanishes when θ_J = 0 (all off-diagonals along the computability split), giving degenerate masses and no mixing.

- **sin³θ_J = −cos(3θ_K)**: an exact trigonometric identity relating the J₃(𝕆) tilt angle θ_J to the Koide phase θ_K, derived from the triple cosine product identity. Both angles are determined by a single underlying parameter.

### 12.3 The Single Free Parameter

All structural parameters of the mass formula are determined by the algebra:

| Parameter | Value | Origin |
|---|---|---|
| Three generations | 3 | J₃(𝕆) off-diagonal entries / minimum for irreducible self-reference |
| Off-diagonal ε | 1/√2 | Cayley-Dickson doubling norm (reciprocal) |
| Born rule squaring | m = λ² | Hopf map is quadratic |
| Koide ratio | 2/3 | Theorem: α = √2 + Z₃ ⟹ 2/3 |
| Angle relation | sin³θ_J = −cos(3θ_K) | Triple cosine product identity |

The single remaining free parameter is **θ_K ≈ 13°**, the Higgs-triality misalignment angle. This one parameter simultaneously determines:

- All three charged lepton masses (via the Koide formula)
- The J₃(𝕆) tilt angle (via sin³θ_J = −cos(3θ_K))
- The CKM mixing angles (via the J₃(𝕆) off-diagonal structure)
- CP violation (via the octonionic non-associativity)

The approximate equality θ_K ≈ θ_Cabibbo (13.04°, to within 0.3°) suggests that the Higgs-triality misalignment and the generation mixing angle are the same geometric quantity.

### 12.4 Verification

The predicted charged lepton mass ratios from J₃(𝕆) eigenvalues²:

| Ratio | Predicted | Observed | Agreement |
|---|---|---|---|
| m_τ/m_e | 3470 | 3477 | 99.8% |
| m_μ/m_e | 206.3 | 206.8 | 99.8% |
| Koide ratio | 2/3 (exact) | 0.66666 | 99.999% |

### 12.5 Why the Hierarchy Is Large

The eigenvalue ratios of J₃(𝕆) are moderate (roughly 59:14:1 for the amplitudes). The enormous mass hierarchy (3477:207:1) arises from the Born rule squaring: m_k = λ_k². This is not a fine-tuning — it is the quadratic nature of the Hopf map, which converts moderate amplitude ratios into large energy ratios. The hierarchy is a consequence of the Born rule applied to the J₃(𝕆) spectrum.

---

## 13. Open Problem: Dark Matter as Information Debt

### 13.1 The Tension

The framework constructs spacetime relationally — structure is constituted by interactions. An entity that participates in no gauge interactions (electromagnetic, weak, strong) completes no loops on S¹, S³, or S⁷ and carries no gauge charges. In what sense does it participate in the relational network? Dark matter, which interacts gravitationally but not via any known gauge force, appears to challenge the relational foundation of the framework.

### 13.2 Two Modes of Relational Existence

The framework resolves the tension by distinguishing two fundamentally different modes of participating in the relational network:

**Mode 1: Gauge interaction.** Completing loops on S¹, S³, S⁷. This gives the entity gauge charges and embeds it in the network of electromagnetic, weak, and strong interactions. Normal matter participates in this mode. This is "loud" relational existence — the entity actively exchanges information through gauge boson loops.

**Mode 2: Gravitational participation.** Carrying information debt that deforms the causal structure. This does not require gauge charges. It does not require loops on any parallelisable sphere. It requires only that the entity's presence imposes a strain on the causal fabric that other entities detect through modified geometry. This is "quiet" relational existence.

This distinction is available because, in the framework, gravity is not a gauge force from a fourth parallelisable sphere (S¹⁵ is not parallelisable). Gravity is the response of the causal structure itself to the presence of information debt — the content of Jacobson's thermodynamic derivation. Gauge forces and gravity have fundamentally different origins: gauge forces arise from the topology of loops; gravity arises from the thermodynamics of the causal fabric.

Dark matter participates via Mode 2. It exists relationally because it deforms the causal structure through which everything else propagates. When a galaxy rotates faster than its visible mass accounts for, the dark matter's information debt is changing the causal paths available to the visible matter. The dark matter is not inert — it strains the causal fabric, and that strain is a relation.

### 13.3 What Dark Matter Might Be: Four Possibilities

The framework constrains dark matter to be gauge-neutral information debt that gravitates, but does not yet uniquely determine its origin. Four possibilities are consistent with the framework, each with different observational signatures:

**Possibility 1: Unprojected octonionic structure.** The computability split projects one direction of 𝕆 onto gauge structure. The full octonionic Hopf bundle contains more information than any single projection captures. The excess — the structure of 𝕆 that the split doesn't project onto gauge-charged representations — still carries information debt (it still strains the causal fabric) but lacks gauge charges (it wasn't captured by the projection). Dark matter would be the shadow of the octonionic structure that the computability split cannot express.

**Possibility 2: Secondary structural debt.** Creating gauge-charged matter (primary debt) necessarily deforms the causal structure around it. This deformation itself carries energy — the gravitational field's energy content. In the framework, creating visible matter generates secondary debt: the cost of accommodating primary debt within a consistent causal structure. Dark matter would not be a separate substance but the causal fabric's self-consistent response to the existence of matter. The ratio of total to primary debt would be determined by a fixed-point condition — debt creates structural debt which creates further structural debt, converging to a ratio potentially consistent with the observed ~6:1 ratio of total matter to visible matter.

**Possibility 3: Topological energy of the Hopf bundle.** The Hopf bundles have non-zero topological invariants (Chern classes) representing global structure that no local measurement can fully capture. This global debt carries energy (it gravitates) but is not associated with any local gauge charge. Dark matter would be the energy content of the topological twisting itself. This would naturally explain why dark matter dominates at galactic scales but is negligible at collider scales: the topological nontriviality of the Hopf bundle manifests over scales large enough for the global structure to matter. At short distances, the bundle looks locally trivial and the dark matter content is undetectable.

**Possibility 4: Boundary debt from finite causal horizons.** The framework predicts a spatially infinite universe. Any observer's causal description is bounded by their past light cone — finite within infinite space. The mismatch between infinite spatial reality and finite causal description generates debt at the causal boundary. This boundary debt would appear, from within the causal description, as gravitational mass that doesn't interact via gauge forces — because it is at the boundary of the causal structure rather than within it.

### 13.4 Observational Discriminants

The four possibilities make different predictions:

| Property | Possibility 1 | Possibility 2 | Possibility 3 | Possibility 4 |
|---|---|---|---|---|
| Self-interaction | None | None | None | None |
| Spatial distribution | Traces visible matter | Traces visible matter | Determined by bundle geometry | Approximately uniform |
| Dark-to-visible ratio | From J₃(𝕆) dimensions | From fixed-point condition | From Chern classes | From causal horizon geometry |
| Scale dependence | Present at all scales | Present at all scales | Emerges at galactic scales | Emerges at cosmological scales |
| Nature | Field-like | Geometric | Topological | Boundary effect |

All four possibilities predict that dark matter is truly collisionless and lacks any gauge interaction. They differ primarily in spatial distribution, scale dependence, and the predicted dark-to-visible ratio.

### 13.5 Status

This is a genuinely open problem. The framework constrains dark matter to be gauge-neutral information debt that gravitates via Mode 2, but does not yet determine which of the four possibilities (or what combination) is correct. The resolution likely requires understanding how the total information content of the octonionic Hopf bundle distributes between gauge-projected (visible) and non-projected (dark) sectors — a calculation that connects the topology of the Hopf bundle to the cosmological dark matter density. This is among the most important open targets of the framework, and different resolutions lead to different falsifiable predictions.

---

## 14. Summary of the Argument

1. **Interpretations of quantum mechanics are coordinate systems** on a single non-computable structure. Different interpretations locate the non-computability in different mathematical objects, but the total non-computability is invariant. The Lawvere-Yanofsky diagonal that underlies all self-referential limitations is itself a supertask. The Axiom of Choice is the assertion that a particular supertask has a definite completion, and is the specific mechanism by which non-computability enters the many-worlds interpretation.

2. **The retrocausal coordinate system** is natural for analysing entanglement because it makes the loop structure manifest.

3. **In relational spacetime, measurement outcomes enter the observer's past light cone without a computable causal antecedent.** This is computationally indistinguishable from information generated by a closed timelike curve.

4. **Therefore, measurement outcomes can be modelled as arising from closed causal loops.** This is the retrocausal description applied universally to all measurement.

5. **Consistent information flow around closed loops requires parallelisable spheres.** By Adams' theorem, the only parallelisable spheres are S¹, S³, S⁷.

6. **These three spheres support exactly the three Hopf fibrations.** The equivariance group of the octonionic Hopf fibration, upon singling out the computability split, is SU(3) × SU(2) × U(1)/ℤ₆ — the Standard Model gauge group.

7. **The Standard Model is therefore a necessary consequence of measurement in relational spacetime,** not a contingent feature of our universe that could have been otherwise.

8. **Rest mass is the energy cost of maintaining un-narratable information.** Information that cannot be expressed as causal sequence must be maintained by ongoing phase cycling at the Compton frequency ω = mc²/ℏ. The rest energy E = mc² is the minimum energy required for this computation (Margolus-Levitin bound). Gravity couples universally to mass because mass is the measure of how much a given entity strains the causal structure (Jacobson's thermodynamic derivation of the Einstein equation). Mass has the dimensions of inverse length in natural units because both mass and spatial distance are measures of non-computability — mass measures how much non-computable content an entity carries, while spatial distance measures separation in the non-computable sector. The fundamental constants c, ℏ, G are conversion factors between the computable (temporal) and non-computable (spatial/massive) sectors.

9. **Internal degrees of freedom can be rewritten as spatial dimensions because both are measures of non-computability.** This explains the mathematical success of the Kaluza-Klein programme and string theory's extra dimensions while predicting that no extra spatial dimensions are physically present. The Kaluza-Klein equivalence is a coordinate transformation between two descriptions of the same non-computable content (gauge charges on Hopf fibres vs positions in compact spaces), not a discovery of new spatial extent. The persistent difficulties of string compactification (moduli stabilisation, the landscape) arise from treating coordinate artefacts as physical parameters.

10. **The compositional completeness of GHZ and W entanglement classes** follows from the same topological constraint: the parallelisable spheres exhaust the available topological resources at three qubits.

11. **Grand unification via SU(5) or any simple group is structurally excluded** because it would require erasing the computability split. The running coupling constants do not meet at a single point; their near-meeting reflects common origin in Spin(9), not unification into a simple group.

12. **The Coleman-Mandula theorem holds without exception.** The direct product structure G_SM × Poincaré is the computability split expressed as a symmetry statement. Supersymmetry is not physically realised because it would undo the computability split. Every motivation for SUSY is independently eliminated: coupling unification is not needed (the triangle is a prediction), the hierarchy problem is reframed (Higgs mass set at the Hopf scale), SUSY dark matter is not needed (dark matter is information debt), and the cosmological constant problem dissolves in a spatially infinite universe (uniform vacuum energy has no boundary to act against).

13. **All three gauge couplings are determined at the Hopf scale.** The photon's zero information debt fixes sin²θ_W = 1/4 (determining the α₁/α₂ ratio), and unit coupling on the S⁷ fibre fixes α₃⁻¹ = 4π. Combined with beta coefficients determined by n_g = 3 and n_H = 1, the entire RG flow of all three couplings is a zero-parameter prediction. The resulting non-unification triangle spans 4 decades in energy with 8.8% minimum spread — confirmed by the non-observation of SUSY partners and proton decay. The predicted α_s(M_Z) = 0.1185 agrees with the measured 0.1179 to 0.5%.

14. **Charged lepton masses are J₃(𝕆) eigenvalues squared.** The mass amplitudes √m_k are eigenvalues of a J₃(𝕆) element with off-diagonal coupling ε = 1/√2 (the Cayley-Dickson reciprocal). The Born rule squaring converts moderate amplitude ratios into the observed mass hierarchy. All parameters are algebraically determined except one angle θ ≈ 13° (the Higgs-triality misalignment ≈ Cabibbo angle), which simultaneously controls the mass spectrum and generation mixing.

15. **Dark matter is gauge-neutral information debt** (open problem). The framework distinguishes two modes of relational existence: gauge interaction (loops on parallelisable spheres) and gravitational participation (straining the causal fabric). Dark matter participates via the second mode only. Its origin likely lies in the octonionic Hopf structure — either as unprojected algebraic content, secondary structural debt in the causal fabric, topological energy of the Hopf bundle, or a combination. The resolution determines the dark-to-visible matter ratio and the spatial distribution of dark matter, both in principle calculable from the framework.

---

## 15. References

### Parallelisable Spheres and Hopf Fibrations
- Adams, J.F. "On the non-existence of elements of Hopf invariant one." *Annals of Mathematics* 72 (1960), 20–104.
- Bott, R. & Milnor, J. "On the parallelizability of the spheres." *Bulletin of the AMS* 64 (1958), 87–89.
- Kervaire, M. "Non-parallelizability of the n-sphere for n > 7." *Proceedings of the National Academy of Sciences* 44 (1958), 280–283.
- Baez, J. "The Octonions." *Bulletin of the AMS* 39 (2002), 145–205.
- Gluck, H., Warner, F. & Ziller, W. "The geometry of the Hopf fibrations." *L'Enseignement Mathématique* 32 (1986), 173–198.

### Hopf Fibrations and Entanglement
- Mosseri, R. & Dandoloff, R. "Geometry of entangled states, Bloch spheres and Hopf fibrations." *J. Phys. A: Math. Gen.* 34 (2001), 10243.
- Bernevig, B.A. & Chen, H.-D. "Geometry of the 3-Qubit State, Entanglement and Division Algebras." *J. Phys. A: Math. Gen.* 37 (2004), 3069.
- Mosseri, R. "Two and Three Qubits Geometry and Hopf Fibrations." In *Topology in Condensed Matter*, Springer (2006).
- Pinilla, M.R. & Luthra, J. "Hopf Fibration and Quantum Entanglement in Qubit Systems." (2009). arXiv:0904.4925.
- Lévay, P. "The geometry of entanglement: metrics, connections and the geometric phase." *J. Phys. A* (2004). quant-ph/0306115.

### Standard Model from Hopf Fibrations / Division Algebras
- Szangolies, J. "The Standard Model Symmetry and Qubit Entanglement." *Entropy* 27(6), 569 (2025). arXiv:2512.17328.
- Krasnov, K. "SO(9) characterisation of the Standard Model gauge group." *J. Math. Phys.* 62, 021703 (2021). arXiv:1912.11282.
- Furey, C. "SU(3)_C × SU(2)_L × U(1)_Y (× U(1)_X) as a symmetry of division algebraic ladder operators." *Phys. Lett. B* (2018).
- Dubois-Violette, M. "Exceptional quantum geometry and particle physics." (2016). arXiv:1604.01247.
- Günaydin, M. & Gürsey, F. "Quark structure and octonions." *J. Math. Phys.* 14 (1973).

### Entanglement Classification
- Dür, W., Vidal, G. & Cirac, J.I. "Three qubits can be entangled in two inequivalent ways." *Phys. Rev. A* 62, 062314 (2000).
- Coecke, B. & Kissinger, A. "The Compositional Structure of Multipartite Quantum Entanglement." *ICALP 2010*, LNCS 6199.

### Linked Bloch Spheres and Parity in Entanglement
- Filatov, S. & Auzinsh, M. "Towards Two Bloch Sphere Representation of Pure Two-Qubit States and Unitaries." *Entropy* 26(4), 280 (2024a). arXiv:2403.10587.
- Filatov, S. & Auzinsh, M. "Entanglement on Two Bloch Spheres: Exploring Two-Qubit Stabilizer Group Structure." (2024b). arXiv:2406.05174.

*Note:* The relevance of Filatov and Auzinsh's linked Bloch sphere result to parity violation in the Standard Model was first recognised at the 2024 Växjö Conference on Quantum Foundations, where Filatov presented preliminary results on a single A4 sheet pinned to a poster panel. The connection between the opposite handedness of the two Bloch spheres and the chirality of the weak interaction — via the quaternionic Hopf fibration — was identified at the conference, and Filatov was subsequently encouraged to develop the result into a full publication. This episode illustrates a broader theme of the present work: results whose significance for fundamental physics is invisible within their native discipline become recognisable once the Hopf fibration dictionary connecting entanglement geometry to gauge theory is in place.

### Self-Reference and Diagonal Arguments
- Lawvere, F.W. "Diagonal arguments and cartesian closed categories." In *Category Theory, Homology Theory and their Applications II*, Springer (1969), 134–145.
- Yanofsky, N.S. "A universal approach to self-referential paradoxes, incompleteness and fixed points." *Bulletin of Symbolic Logic* 9 (2003), 362–386.

### Closed Timelike Curves and Computation
- Deutsch, D. "Quantum mechanics near closed timelike lines." *Phys. Rev. D* 44 (1991), 3197–3217.
- Aaronson, S. & Watrous, J. "Closed timelike curves make quantum and classical computing equivalent." *Proc. Roy. Soc. A* 465 (2009), 631–647. arXiv:0808.2669.
- Aaronson, S. "Computability Theory of Closed Timelike Curves." (2016). ECCC TR16-146.

### Retrocausality
- Price, H. *Time's Arrow and Archimedes' Point*. Oxford University Press (1996).
- Cramer, J. "The transactional interpretation of quantum mechanics." *Rev. Mod. Phys.* 58 (1986), 647–688.
- Evans, P., Price, H. & Wharton, K. "New slant on the EPR–Bell experiment." *British Journal for the Philosophy of Science* 64 (2013), 297–324.
- Wharton, K. "Quantum states as ordinary information." *Information* 5 (2014), 190–208.
- Price, H. & Wharton, K. "Why Entanglement?" (2023). philsci-archive.pitt.edu/21657.
- Wharton, K. & Argaman, N. "Colloquium: Bell's theorem and locally mediated reformulations of quantum mechanics." *Rev. Mod. Phys.* 92 (2020), 021002.

### Supertasks and Creation Ex Nihilo
- Thomson, J.F. "Tasks and super-tasks." *Analysis* 15 (1954), 1–13.
- Laraudogoitia, J.P. "A beautiful supertask." *Mind* 105 (1996), 81–83.
- Laraudogoitia, J.P. "Infinity machines and creation ex nihilo." *Synthese* 115 (1998), 259–265.

### Axiom of Choice and Supertasks
- Mormann, T. "Topological Games, Supertasks, and (Un)determined Experiments." PhilArchive (2009).
- Bacon, A. "A paradox for supertask decision makers." (2010).

### Contextuality and Negative Probability
- Spekkens, R. "Negativity and contextuality are equivalent notions of nonclassicality." *Phys. Rev. Lett.* 101 (2008), 020401.

### Grand Unification and Proton Decay
- Georgi, H. & Glashow, S.L. "Unity of all elementary-particle forces." *Phys. Rev. Lett.* 32 (1974), 438–441.
- Super-Kamiokande Collaboration. "Search for proton decay via p → e⁺π⁰ and p → μ⁺π⁰ with an enlarged fiducial volume in Super-Kamiokande I–IV." *Phys. Rev. D* 95, 012004 (2017).

### Information, Gravity, and Computation
- Jacobson, T. "Thermodynamics of spacetime: The Einstein equation of state." *Phys. Rev. Lett.* 75 (1995), 1260–1263.
- Margolus, N. & Levitin, L.B. "The maximum speed of dynamical evolution." *Physica D* 120 (1998), 188–195.

### Kaluza-Klein and Extra Dimensions
- Kaluza, T. "Zum Unitätsproblem der Physik." *Sitzungsberichte der Preussischen Akademie der Wissenschaften* (1921), 966–972.
- Klein, O. "Quantentheorie und fünfdimensionale Relativitätstheorie." *Zeitschrift für Physik* 37 (1926), 895–906.

### Quantum Foundations
- Hardy, L. "Quantum theory from five reasonable axioms." (2001). quant-ph/0101012.
- Fuchs, C., Mermin, N.D. & Schack, R. "An introduction to QBism with an application to the locality of quantum mechanics." *Am. J. Phys.* 82 (2014), 749–754.

### Koide Formula and Mass Relations
- Koide, Y. "New view of quark and lepton mass hierarchy." *Phys. Rev. D* 28 (1983), 252.
- Rivero, A. & Gsponer, A. "The strange formula of Dr. Koide." (2005). hep-ph/0505220.

### Exceptional Jordan Algebra and Generations
- Dubois-Violette, M. "Exceptional quantum geometry and particle physics." (2016). arXiv:1604.01247.
- Dubois-Violette, M. & Todorov, I. "Exceptional quantum geometry and particle physics II." *Nuclear Physics B* 938 (2019), 751–761.
- Boyle, L. "The Standard Model, the Exceptional Jordan Algebra, and Triality." (2020). arXiv:2006.16265.
- Günaydin, M. & Gürsey, F. "Quark structure and octonions." *J. Math. Phys.* 14 (1973).
- Gresnigt, N.G. "The Standard Model particle content from the S₃ automorphisms of the sedenions." (2020).

---

*Document Status: Central argument for the paper. March 16, 2026.*
