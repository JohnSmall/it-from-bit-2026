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

---

## 6. Compositional Completeness

### 6.1 The Three-Qubit Terminus

The Hopf fibration chain terminates at three qubits because the octonions are the last division algebra. The four-qubit case would require sedenions, which have zero divisors and cannot support a well-defined Hopf map (Pinilla & Luthra 2009).

### 6.2 GHZ and W as the Alphabet

Dür, Vidal, and Cirac (2000) showed that three-qubit entanglement has exactly two inequivalent SLOCC classes: GHZ (genuinely tripartite, all-or-nothing) and W (distributed pairwise, robust to loss). Coecke and Kissinger (2010) proved that these two classes are *compositionally complete*: any N-qubit entanglement class can be generated from compositions of GHZ and W primitives (plus two-qubit entanglement).

### 6.3 Why Compositional Completeness Holds

The grounding argument explains *why* compositional completeness is true, rather than treating it as a surprising mathematical fact. If the topological resources available for entanglement loops are exhausted at S¹, S³, S⁷ (which they are, by Adams' theorem), then no genuinely new entanglement primitive can arise at four or more qubits. Any four-particle entanglement must decompose into compositions of the structures that S¹, S³, S⁷ support — which are exactly the Bell states (two-qubit, quaternionic), GHZ (three-qubit, octonionic, genuinely tripartite), and W (three-qubit, octonionic, distributed pairwise).

Compositional completeness is a theorem about the topology of information arriving from outside the past light cone. The entanglement alphabet has exactly these letters because the parallelisable spheres have exactly these dimensions.

### 6.4 Faithfulness of the Dictionary

This is what gives confidence that translations between entanglement problems and Standard Model problems preserve all relevant structure. When we recast a Standard Model problem as an entanglement problem (or vice versa), we are not making an approximation or exploiting an analogy — we are switching coordinate systems on the same underlying topological structure. Both sides are constrained by the same thing: the topology of consistent loops on parallelisable spheres.

---

## 7. Summary of the Argument

1. **Interpretations of quantum mechanics are coordinate systems** on a single non-computable structure. Different interpretations locate the non-computability in different mathematical objects, but the total non-computability is invariant.

2. **The retrocausal coordinate system** is natural for analysing entanglement because it makes the loop structure manifest.

3. **In relational spacetime, measurement outcomes enter the observer's past light cone without a computable causal antecedent.** This is computationally indistinguishable from information generated by a closed timelike curve.

4. **Therefore, measurement outcomes can be modelled as arising from closed causal loops.** This is the retrocausal description applied universally to all measurement.

5. **Consistent information flow around closed loops requires parallelisable spheres.** By Adams' theorem, the only parallelisable spheres are S¹, S³, S⁷.

6. **These three spheres support exactly the three Hopf fibrations.** The equivariance group of the octonionic Hopf fibration, upon singling out the computability split, is SU(3) × SU(2) × U(1)/ℤ₆ — the Standard Model gauge group.

7. **The Standard Model is therefore a necessary consequence of measurement in relational spacetime,** not a contingent feature of our universe that could have been otherwise.

8. **The compositional completeness of GHZ and W entanglement classes** follows from the same topological constraint: the parallelisable spheres exhaust the available topological resources at three qubits.

---

## 8. References

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
- Laraudogoitia, J.P. "A beautiful supertask." *Mind* 105 (1996), 81–83.
- Laraudogoitia, J.P. "Infinity machines and creation ex nihilo." *Synthese* 115 (1998), 259–265.

### Contextuality and Negative Probability
- Spekkens, R. "Negativity and contextuality are equivalent notions of nonclassicality." *Phys. Rev. Lett.* 101 (2008), 020401.

### Quantum Foundations
- Hardy, L. "Quantum theory from five reasonable axioms." (2001). quant-ph/0101012.
- Fuchs, C., Mermin, N.D. & Schack, R. "An introduction to QBism with an application to the locality of quantum mechanics." *Am. J. Phys.* 82 (2014), 749–754.

---

*Document Status: Central argument for the paper. March 16, 2026.*
