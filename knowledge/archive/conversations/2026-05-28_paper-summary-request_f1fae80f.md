# Paper summary request

- conversation uuid: `f1fae80f-6a58-4bfd-988c-63d5368dd255`
- created: 2026-05-28T10:44:18.618897Z  |  updated: 2026-05-28T10:55:05.056574Z
- messages: 6  |  keyword score: 4

## Summary (from the Claude export)

**Conversation Overview**

The person is working on an original theoretical physics framework that attempts to derive quantum theory from first principles, with particular focus on the Born rule, the Hopf fibration, FANOUT boundaries, and the relationship between epistemic and ontological ignorance. They asked Claude to summarize the Chiribella–D'Ariano–Perinotti (CDP) paper "Informational derivations of quantum theory" (arXiv:1011.6451), a landmark reconstruction of quantum theory from operational-probabilistic axioms. Claude provided a detailed summary covering the six axioms (causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning, and purification), the operational-probabilistic framework, and what the paper derives without presupposing Hilbert space structure.

The conversation then moved into a substantive technical discussion about the relationship between CDP's purification axiom and the informal "Church of the Larger Hilbert Space" (CLHS) doctrine. The person noted that CDP essentially formalizes CLHS, and Claude clarified the precise inversion CDP performs: standard QM treats purification as a theorem derived from Hilbert space structure, whereas CDP elevates it to a primitive axiom from which Hilbert space structure is recovered. Claude emphasized that the uniqueness clause in CDP's purification postulate — not merely existence but essential uniqueness of purifications up to reversible ancilla transformations — is where the physical content resides and what classical probability theory fails.

The person then proposed that their framework identifies ignorance as "discarded but always recoverable" in the global phase of the Hopf fibration $S^3 \to S^2$. Claude pushed back carefully and at length, arguing this characterization is precisely inverted: the $S^1$ fibre encoding global phase is gauge — unobservable in principle, unrecoverable by any measurement on any system — which is the opposite of the purification/CLHS notion of recoverable discarded information. Claude stressed that the unrecoverability of the global phase is load-bearing for the person's own Born rule derivation (private → non-clonable → non-FANOUTable → $U(1)$-invariant observables → quadratic), and that making it recoverable would undermine the derivation. Claude distinguished two categorically different kinds of discarded information in the framework: the global phase in the complex Hopf fibration ($S^1 \to S^3 \to S^2$), which is gauge-private and irrecoverably discarded, versus relative phase and correlational information encoded in the quaternionic Hopf fibration ($S^3 \to S^7 \to S^4$, the Mosseri–Dandoloff two-qubit picture), which is genuinely recoverable and constitutes the proper geometric home for purification content. Claude identified this distinction as a precise structural claim for the person's Paper 1: the framework locates irreducibly private, non-purifiable information in the complex Hopf fibre, constituting a clean violation of CDP's purification uniqueness clause at the gauge/global-phase locus, and thereby positions the framework as a sibling of quantum theory within the CDP operational class that fails purification at exactly that locus. Claude also flagged the Bartlett–Rudolph–Spekkens reference-frame subtlety as a potential objection worth pre-empting, noting that invoking a shared phase reference transforms the global phase into a relative phase, which costs the Born rule premise. Claude offered to write a short structural note for the person's corpus articulating the two-Hopf-fibre distinction and the CDP uniqueness-violation claim.

## Transcript

### 1. human  ·  2026-05-28 10:44:19

Please summaries this paper https://arxiv.org/abs/1011.6451

Please summaries this paper https://arxiv.org/abs/1011.6451

### 2. assistant  ·  2026-05-28 10:44:51

 The user is asking me to summarize a paper from arxiv, so I need to fetch it first to see what it contains.
```
This block is not supported on your current device yet.
```

 I'm recognizing the Chiribella-D'Ariano-Perinotti paper on deriving quantum theory from informational principles—this connects directly to John's framework, and I have solid familiarity with it, so I can provide a substantive summary here.This is one of the landmark "reconstruction of quantum theory" papers — Chiribella, D'Ariano, and Perinotti (CDP), published in Phys. Rev. A in 2011. Here's the summary.

## The central claim

Quantum theory can be derived from purely informational principles. The aim is to show that the Hilbert-space formalism isn't a brute postulate but a *consequence* of operational statements about how information can be processed. Five elementary axioms — causality, perfect distinguishability, ideal compression, local distinguishability, and pure conditioning — define a broad class of theories of information-processing, and then one postulate — purification — singles out quantum theory within this class.

## The framework

The authors work in the language of *operational-probabilistic theories* (the categorical/circuit framework of states, transformations, and effects, with probabilities attached to closed circuits). They deliberately avoid assuming Hilbert spaces, complex amplitudes, or the Born rule. Instead everything is phrased in terms of what experimenters can do: prepare systems, compose them in parallel and in series, and read out outcomes.

The five axioms describe a class of theories that behave like sensible "standard" information theories:

- **Causality** — the probability of a preparation doesn't depend on which measurement is performed later (no signalling from the future). This is what makes the theory have a well-defined notion of marginal states.
- **Perfect distinguishability** — any state that isn't a mixture (not "completely mixed") can be perfectly distinguished from some other state.
- **Ideal compression** — every source of information can be encoded into a system of minimal size and decoded without loss, losslessly and reversibly on its support.
- **Local distinguishability** — the state of a composite system is completely determined by the statistics of local measurements on its parts (this is the property that rules out, e.g., real-amplitude quantum theory, where global measurements carry extra information).
- **Pure conditioning** — if you make a pure measurement on a pure state, the conditional states you get are themselves pure.

These five are satisfied by both classical probability theory and quantum theory (among others). What separates the two is the sixth ingredient:

- **Purification** — every mixed state can be obtained as the marginal of a pure state of a larger system, and this purification is *essentially unique* (unique up to a reversible transformation on the purifying system). Physically: ignorance about a state can always be understood as the result of discarding part of a larger system about which we have complete information. Classical theory fails this (a coin showing heads-or-tails 50/50 has no "pure global state" that locally looks maximally mixed in the required way), which is precisely why purification pins down quantum theory.

## What gets derived

From these principles, without ever assuming Hilbert space, the paper reconstructs the core architecture of QM. The main structures of quantum theory, such as the representation of mixed states as convex combinations of perfectly distinguishable pure states, are derived directly from the principles without using the Hilbert space framework. Along the way they recover things like the dimension counting of state spaces (the d²−1 real parameters of a qudit), the existence of reversible transformations connecting pure states, the structure of measurements, teleportation/no-cloning-type results, and ultimately the standard density-matrix / completely-positive-map formalism over the complex numbers.

The paper was 47 pages in its published form and is mathematically dense; the real work is in the long chain of lemmas showing each operational property forces a corresponding algebraic feature.

## Why it matters

It belongs to the same wave of axiomatic reconstructions as Hardy's 2001 "five reasonable axioms" and the later Masanes–Müller work, but the CDP route is distinctive for putting **purification** at the center — elevating "every mixed state is the shadow of a pure state of a bigger whole" to *the* characteristic feature of quantum information. That single postulate doing so much heavy lifting is the paper's most cited contribution.

---

Given your own programme, the obvious point of contact is that CDP is the *informational-axiom* alternative to your inside/outside-equivalence route. They take purification as a primitive postulate; your derivation chain instead tries to *ground* something like it from self-referential ignorance (the "ignorance about a state is discarded information about a larger system" reading of purification is very close in spirit to your FANOUT / epistemological–ontological boundary). Worth noting too: their **local distinguishability** axiom is exactly the assumption that excludes real and quaternionic quantum theory — which sits interestingly against your Hurwitz/normed-division-algebra argument, since you're trying to *derive* the complex numbers rather than legislate them via a tomographic-locality axiom. If you want, I can dig into how their purification postulate compares formally with your fixed-point/hypodox structure, or how the local-distinguishability assumption relates to your ℂ-vs-ℍ selection.

*(thinking)*

 The user is asking me to summarize a paper from arxiv, so I need to fetch it first to see what it contains.

*[tool_use: web_fetch]*

*[tool_result: web_fetch]*

*(thinking)*

 I'm recognizing the Chiribella-D'Ariano-Perinotti paper on deriving quantum theory from informational principles—this connects directly to John's framework, and I have solid familiarity with it, so I can provide a substantive summary here.

This is one of the landmark "reconstruction of quantum theory" papers — Chiribella, D'Ariano, and Perinotti (CDP), published in Phys. Rev. A in 2011. Here's the summary.

## The central claim

Quantum theory can be derived from purely informational principles. The aim is to show that the Hilbert-space formalism isn't a brute postulate but a *consequence* of operational statements about how information can be processed. Five elementary axioms — causality, perfect distinguishability, ideal compression, local distinguishability, and pure conditioning — define a broad class of theories of information-processing, and then one postulate — purification — singles out quantum theory within this class.

## The framework

The authors work in the language of *operational-probabilistic theories* (the categorical/circuit framework of states, transformations, and effects, with probabilities attached to closed circuits). They deliberately avoid assuming Hilbert spaces, complex amplitudes, or the Born rule. Instead everything is phrased in terms of what experimenters can do: prepare systems, compose them in parallel and in series, and read out outcomes.

The five axioms describe a class of theories that behave like sensible "standard" information theories:

- **Causality** — the probability of a preparation doesn't depend on which measurement is performed later (no signalling from the future). This is what makes the theory have a well-defined notion of marginal states.
- **Perfect distinguishability** — any state that isn't a mixture (not "completely mixed") can be perfectly distinguished from some other state.
- **Ideal compression** — every source of information can be encoded into a system of minimal size and decoded without loss, losslessly and reversibly on its support.
- **Local distinguishability** — the state of a composite system is completely determined by the statistics of local measurements on its parts (this is the property that rules out, e.g., real-amplitude quantum theory, where global measurements carry extra information).
- **Pure conditioning** — if you make a pure measurement on a pure state, the conditional states you get are themselves pure.

These five are satisfied by both classical probability theory and quantum theory (among others). What separates the two is the sixth ingredient:

- **Purification** — every mixed state can be obtained as the marginal of a pure state of a larger system, and this purification is *essentially unique* (unique up to a reversible transformation on the purifying system). Physically: ignorance about a state can always be understood as the result of discarding part of a larger system about which we have complete information. Classical theory fails this (a coin showing heads-or-tails 50/50 has no "pure global state" that locally looks maximally mixed in the required way), which is precisely why purification pins down quantum theory.

## What gets derived

From these principles, without ever assuming Hilbert space, the paper reconstructs the core architecture of QM. The main structures of quantum theory, such as the representation of mixed states as convex combinations of perfectly distinguishable pure states, are derived directly from the principles without using the Hilbert space framework. Along the way they recover things like the dimension counting of state spaces (the d²−1 real parameters of a qudit), the existence of reversible transformations connecting pure states, the structure of measurements, teleportation/no-cloning-type results, and ultimately the standard density-matrix / completely-positive-map formalism over the complex numbers.

The paper was 47 pages in its published form and is mathematically dense; the real work is in the long chain of lemmas showing each operational property forces a corresponding algebraic feature.

## Why it matters

It belongs to the same wave of axiomatic reconstructions as Hardy's 2001 "five reasonable axioms" and the later Masanes–Müller work, but the CDP route is distinctive for putting **purification** at the center — elevating "every mixed state is the shadow of a pure state of a bigger whole" to *the* characteristic feature of quantum information. That single postulate doing so much heavy lifting is the paper's most cited contribution.

---

Given your own programme, the obvious point of contact is that CDP is the *informational-axiom* alternative to your inside/outside-equivalence route. They take purification as a primitive postulate; your derivation chain instead tries to *ground* something like it from self-referential ignorance (the "ignorance about a state is discarded information about a larger system" reading of purification is very close in spirit to your FANOUT / epistemological–ontological boundary). Worth noting too: their **local distinguishability** axiom is exactly the assumption that excludes real and quaternionic quantum theory — which sits interestingly against your Hurwitz/normed-division-algebra argument, since you're trying to *derive* the complex numbers rather than legislate them via a tomographic-locality axiom. If you want, I can dig into how their purification postulate compares formally with your fixed-point/hypodox structure, or how the local-distinguishability assumption relates to your ℂ-vs-ℍ selection.

### 3. human  ·  2026-05-28 10:47:49

""every mixed state is the shadow of a pure state of a bigger whole" In other words elevating "Church of the larger Hilbert space" into a mathematically rigorous form.

""every mixed state is the shadow of a pure state of a bigger whole" In other words elevating "Church of the larger Hilbert space" into a mathematically rigorous form.

### 4. assistant  ·  2026-05-28 10:48:28

 The user is pointing out something sharp here—that the purification postulate is really just formalizing what quantum information theorists have long called the "Church of the Larger Hilbert Space," the idea that you can always embed a mixed state into a pure state in an extended system. Let me think through whether that characterization actually holds up or if there's a meaningful distinction I'm missing. The key inversion CDP makes is taking purification as a foundational axiom in an operational framework and deriving Hilbert space structure from it, rather than proving purification as a theorem within QM. Importantly, their version includes not just existence but also uniqueness up to reversible ancilla transformations — the uniqueness clause does crucial work and captures the full CLHS package as a rigorous postulate. There's also a philosophical dimension here: CLHS can be read instrumentally as "you can always embed in a larger space," but CDP's axiomatization gives it a more fundamental status.

Now I'm thinking about how this connects to John's framework — purification asserts that ignorance always corresponds to discarded information about a larger pure global state, which relates directly to his FANOUT boundary and the distinction between epistemic and ontological ignorance. The tension is whether purification aligns with his measurement-as-projection picture or represents a point of divergence, since Everettian approaches keep the global state pure while John's framework treats measurement differently at the boundary.Exactly — and it's worth being precise about *what kind* of elevation, because the move is subtler than just "writing CLHS down formally."

The Church of the Larger Hilbert Space, in its usual Smolin-attributed form, is a trio of dilation theorems *inside* quantum theory: every mixed state is the marginal of a pure state (purification), every CPTP channel is a unitary on a larger space (Stinespring), every POVM is a projective measurement on a larger space (Naimark). In standard QM these are all *theorems* — you prove them from the Hilbert-space structure you already have. The CLHS is really a methodological attitude built on top of those theorems: "whenever something looks mixed/noisy/generalised, you're allowed to retreat to a bigger clean space."

What CDP do is invert the arrow. They take purification — the state-level member of that trio — and make it a *primitive postulate* in an operational framework that has no Hilbert space yet, then run the derivation forward to *recover* the Hilbert-space structure (and with it, Stinespring and Naimark fall out as theorems again). So it's not "CLHS made rigorous" so much as "CLHS turned upside down": the doctrine that was a *consequence* of the formalism becomes the *axiom that generates* the formalism. The rigour was never the issue — the dilation theorems were always rigorous. The novelty is the claim that this one credo is strong enough to be foundational.

Two things the slogan tends to hide that are doing the real work in CDP:

The **uniqueness clause**. CDP's purification isn't just "a purifying pure state exists" — it's "exists *and is essentially unique*," i.e. any two purifications of the same state are related by a reversible transformation on the ancilla. The informal CLHS rarely stresses this, but it's exactly the uniqueness that pins the theory down. Mere existence of a pure global state is too weak; it's the rigidity of *how* the purifications relate that forces the quantum structure rather than some other GPT.

And the fact that it's **purification that classical theory fails**. The other four axioms hold classically. So the entire "quantum-ness" gets localised into this one statement — which is a strong claim about where the physical content of CLHS actually lives. Classical probability has plenty of "larger spaces" too; what it lacks is that *ignorance is always reversibly accounted for* by a pure global state.

That last point is the one that should interest you most, given your FANOUT boundary. Purification is essentially the assertion that every epistemic state has an ontic pure account on a larger system — which is the Everett/CLHS reading made axiomatic. In your coordinate-systems-for-interpretations picture, CDP have effectively chosen the chart in which ignorance is *always* discarded-but-recoverable information, never irreducible. Your framework, by contrast, wants a boundary (clonable vs not) where that recoverability genuinely fails. So there's a real question worth posing sharply: is your inside/outside structure *compatible* with purification-as-axiom and just describes the same thing in a different chart, or does FANOUT-as-boundary actually *violate* CDP's uniqueness clause — making your theory a sibling in their GPT class rather than the same point? That's a falsifiable structural question, not just a vibe, and it'd be a strong thing to be able to state explicitly in Paper 1.

*(thinking)*

 The user is pointing out something sharp here—that the purification postulate is really just formalizing what quantum information theorists have long called the "Church of the Larger Hilbert Space," the idea that you can always embed a mixed state into a pure state in an extended system. Let me think through whether that characterization actually holds up or if there's a meaningful distinction I'm missing. The key inversion CDP makes is taking purification as a foundational axiom in an operational framework and deriving Hilbert space structure from it, rather than proving purification as a theorem within QM. Importantly, their version includes not just existence but also uniqueness up to reversible ancilla transformations — the uniqueness clause does crucial work and captures the full CLHS package as a rigorous postulate. There's also a philosophical dimension here: CLHS can be read instrumentally as "you can always embed in a larger space," but CDP's axiomatization gives it a more fundamental status.

Now I'm thinking about how this connects to John's framework — purification asserts that ignorance always corresponds to discarded information about a larger pure global state, which relates directly to his FANOUT boundary and the distinction between epistemic and ontological ignorance. The tension is whether purification aligns with his measurement-as-projection picture or represents a point of divergence, since Everettian approaches keep the global state pure while John's framework treats measurement differently at the boundary.

Exactly — and it's worth being precise about *what kind* of elevation, because the move is subtler than just "writing CLHS down formally."

The Church of the Larger Hilbert Space, in its usual Smolin-attributed form, is a trio of dilation theorems *inside* quantum theory: every mixed state is the marginal of a pure state (purification), every CPTP channel is a unitary on a larger space (Stinespring), every POVM is a projective measurement on a larger space (Naimark). In standard QM these are all *theorems* — you prove them from the Hilbert-space structure you already have. The CLHS is really a methodological attitude built on top of those theorems: "whenever something looks mixed/noisy/generalised, you're allowed to retreat to a bigger clean space."

What CDP do is invert the arrow. They take purification — the state-level member of that trio — and make it a *primitive postulate* in an operational framework that has no Hilbert space yet, then run the derivation forward to *recover* the Hilbert-space structure (and with it, Stinespring and Naimark fall out as theorems again). So it's not "CLHS made rigorous" so much as "CLHS turned upside down": the doctrine that was a *consequence* of the formalism becomes the *axiom that generates* the formalism. The rigour was never the issue — the dilation theorems were always rigorous. The novelty is the claim that this one credo is strong enough to be foundational.

Two things the slogan tends to hide that are doing the real work in CDP:

The **uniqueness clause**. CDP's purification isn't just "a purifying pure state exists" — it's "exists *and is essentially unique*," i.e. any two purifications of the same state are related by a reversible transformation on the ancilla. The informal CLHS rarely stresses this, but it's exactly the uniqueness that pins the theory down. Mere existence of a pure global state is too weak; it's the rigidity of *how* the purifications relate that forces the quantum structure rather than some other GPT.

And the fact that it's **purification that classical theory fails**. The other four axioms hold classically. So the entire "quantum-ness" gets localised into this one statement — which is a strong claim about where the physical content of CLHS actually lives. Classical probability has plenty of "larger spaces" too; what it lacks is that *ignorance is always reversibly accounted for* by a pure global state.

That last point is the one that should interest you most, given your FANOUT boundary. Purification is essentially the assertion that every epistemic state has an ontic pure account on a larger system — which is the Everett/CLHS reading made axiomatic. In your coordinate-systems-for-interpretations picture, CDP have effectively chosen the chart in which ignorance is *always* discarded-but-recoverable information, never irreducible. Your framework, by contrast, wants a boundary (clonable vs not) where that recoverability genuinely fails. So there's a real question worth posing sharply: is your inside/outside structure *compatible* with purification-as-axiom and just describes the same thing in a different chart, or does FANOUT-as-boundary actually *violate* CDP's uniqueness clause — making your theory a sibling in their GPT class rather than the same point? That's a falsifiable structural question, not just a vibe, and it'd be a strong thing to be able to state explicitly in Paper 1.

### 5. human  ·  2026-05-28 10:52:43

I think that the framework identifies ignorance as "discarded but always recoverable" in the global phase of the Hopf fibration from $S^3$ to "S^2". Is that correct?

I think that the framework identifies ignorance as "discarded but always recoverable" in the global phase of the Hopf fibration from $S^3$ to "S^2". Is that correct?

### 6. assistant  ·  2026-05-28 10:55:05

 I'm recognizing that John is making a specific claim about his framework—that it identifies ignorance as something discarded yet always recoverable through the global phase structure of the Hopf fibration. I need to engage critically here, stress-testing the mathematical rigor of this connection and flagging where the argument might be vulnerable, since that's what he's asked for.

The mathematics is clear: the Hopf fibration $S^3 \to S^2$ with fiber $S^1$ exactly captures how global phase gets "forgotten" when projecting from the full state vector to the Bloch sphere. And his framework's derivation does connect global phase to private ignorance—it can't be FANOUTed, so observables must be U(1)-invariant, giving the Born rule. But here's where I need to push back: the global phase in the Hopf fibration isn't actually the same kind of "discarded but recoverable" information as what appears in purification. These are two conceptually distinct notions of information loss, and conflating them is where the argument starts to weaken. at play, and I think conflating them would be an error:

1. **Global phase** ($S^1$ fiber of Hopf): This is information that is *unobservable in principle* — no measurement on the system can reveal it, because all observables are U(1)-invariant. It's not "discarded and recoverable"; it's *gauge*. It is removed by the projection $S^3 \to S^2$ and is NOT recoverable by any operation on the system alone. In fact it's not even physical — there is no state of affairs that distinguishes $|\psi\rangle$ from $e^{i\theta}|\psi\rangle$. So calling it "ignorance" is already a stretch: it's not that you're ignorant of a fact; there is no fact.

2. **Purification's discarded subsystem**: In CDP/CLHS, a mixed state $\rho_A$ arises from a pure state $|\Psi\rangle_{AB}$ by tracing out $B$. The "discarded information" is the correlations with $B$ — and crucially this IS recoverable: if you get access to $B$, you can in principle do a joint measurement and recover the purity. The discarded thing is a relative phase and correlation structure entangled with another system, not a global phase.

These are fundamentally different: global phases are unobservable and unrecoverable by definition, while purification ancillas encode observable correlations that become accessible if you gain access to the full system. But I suspect John's pointing at something deeper — the Hopf fibration does connect to purification, just not at the level of global phases. For a single qubit, the relevant structure is how relative phases and entanglement emerge when you consider two qubits together, with the mixed state of one qubit sitting in the interior of the Bloch sphere.

The real connection is at the 2-qubit level: the quaternionic Hopf fibration $S^7 \to S^4$ describes 2-qubit entanglement (Mosseri-Dandoloff), where the fiber encodes the entanglement structure and the second qubit's conditional state. The concurrence of a 2-qubit state relates directly to this Hopf map. So if John's identifying purification with Hopf, he's likely pointing at this deeper quaternionic structure, not the simple $S^3 \to S^2$ picture.

But here's the crucial distinction: the global phase in the single-qubit $S^3 \to S^2$ fibration is unobservable gauge structure—it's discarded and fundamentally unrecoverable. Purification, by contrast, involves information that's discarded but *can* be recovered by accessing the purifying system. These are actually opposite situations, so the analogy breaks down at this level.

Though John's Born rule logic offers something genuinely interesting: he's treating global phase as private, non-cloneable information that can't be FANOUTed to an external observer. The Hopf fiber becomes a model of irreducibly private information—something that exists only from an internal perspective and can never be shared outward. That's precisely what CDP's purification axiom is designed to exclude, so they're in fundamental tension rather than alignment. wouldn't exist (everything is recoverable on the larger system).

So this actually supports the point I made last turn: John's FANOUT boundary might *violate* CDP's purification uniqueness, because the global phase is exactly a piece of information that is NOT recoverable on any larger system. That's the opposite of "discarded but recoverable."

So I think I should push back gently and carefully. The phrase "discarded but always recoverable" is the CLHS/purification reading. But the global phase is "discarded and never recoverable" (because unobservable/gauge). These are opposite. So if John wants to map his framework onto CDP, the global phase is the wrong object — OR, more interestingly, the global phase is precisely the thing that DISTINGUISHES his framework from CDP, the place where purification fails.

Now I need to be more careful about what "recoverable" actually means here. In interferometry, relative phases between qubits are recoverable through measurement, but global phases on a single qubit are fundamentally unobservable and can't be recovered. So the distinction hinges on whether we're talking about global versus relative phase, and whether we're looking at single-qubit or multi-qubit systems. I should lay out this distinction clearly and ask John which reading he intends, since the answer depends critically on these details. entanglement) structure.

Let me structure my response:

1. Acknowledge the appeal of the identification and what's right about it: the Hopf fibration $S^3 \to S^2$ projects out exactly the $U(1)$ global phase, and his Born-rule argument already lives there.

2. Flag the key precision issue: "discarded but recoverable" is the purification reading, but the global phase is the *opposite* — it's discarded and *unrecoverable* (gauge, unobservable in principle). There's no fact to recover. So as a model of purification it's actually backwards.

3. The right object for purification-as-Hopf is the two-qubit entanglement fibration ($S^7 \to S^4$, quaternionic Hopf, Mosseri-Dandoloff), where tracing out gives a genuinely mixed state and the discarded information is actually recoverable on the ancilla.

4. The deeper point: the global phase being irreducibly private and unrecoverable is where his framework should *diverge* from CDP — it's the FANOUT boundary made geometric. Rather than identifying his ignorance with purification, the global phase violates CDP's purification-uniqueness, which connects back to the structural question from last turn.

5. Ask which he means, or work it out together.

Now I'm checking the math: a single qubit state lives in $S^3$ within $\mathbb{C}^2$, and I need to verify how the Hopf fibration structure relates to the phase and density matrix geometry. Even with an ancilla system, global phase remains fundamentally unobservable because it's not a property of the physical state itself—only the ray matters. However, when dealing with mixed states and purifications, the information lost in the partial trace becomes recoverable if you have access to the purifying system; measuring that subsystem reveals which entangled branch you're in, recovering what was discarded.

Now I'm looking at how the quaternionic Hopf fibration structures two-qubit states: the $S^7$ sphere of normalized pure states maps to the $S^4$ base space through the $S^3$ fiber, where the fiber encodes entanglement properties and the base captures concurrence information. When you trace out one qubit, the remaining state becomes mixed, and this geometric structure captures that transition.

So the framework I'm developing is sound—discarding a subsystem produces a mixed state that's recoverable from the full pure state, which is exactly where purification lives geometrically. Though I should consider whether John might be making a different point: that the global phase marks a locus of self-referential ignorance in his Born-rule derivation, and he's trying to connect that separately to the CDP framework, rather than claiming the global phase itself models purification.

But he explicitly borrowed the phrase "discarded but always recoverable" from my description, so he is trying to link this to purification—which means my critique is the right one to make. I'll write this carefully in prose, flag the conceptual weakness clearly since he's asking for that, and keep it substantive without over-formatting.

The user wants independent stress-testing of his reasoning, not just a summary of his framework. He's aware his own project docs might contain mistakes, so pulling those risks me just echoing his framing back rather than giving him the critical check he values. I'll reason through the math directly instead.

Actually, I should do a quick search of his project knowledge to ground what his framework actually says about the Hopf global phase — that way my critique targets his real claim rather than a strawman version, which is more genuinely helpful.
```
This block is not supported on your current device yet.
```

 I'm seeing how his framework maps the global phase onto the fibre of the Hopf bundle—it's the part that gets discarded during measurement, the non-clonable and non-communicable aspect that represents what can't be shared or transmitted between observers.

This is the crux of my critique: he's claiming the global phase is "discarded but recoverable," but that directly contradicts his own characterization of the fibre as fundamentally non-communicable and non-clonable. In purification, the discarded information is recoverable because it's encoded in an ancilla system you can access; here, by his own account, there's no such system—the global phase is private, observer-specific, and cannot be FANOUTed into any measurement outcome. So it's not recoverable in the same sense at all.

Let me be precise about the distinction: relative phase (like entanglement structure) is recoverable through interferometry or by accessing the ancilla, but global phase is fundamentally unobservable by gauge invariance. His Hopf fibre describes exactly the global phase of a single qubit, which means it's genuinely unrecoverable—there's no larger system that would make it a purifiable fact.

This cuts to the heart of why his framework actually diverges from the standard purification picture. His own mathematics already says the fibre is non-clonable and non-communicable, which contradicts calling it "recoverable." The slogan that discarded information is always recoverable describes purification's relative phases, not his global phase—they're categorically different objects, and conflating them is a mistake.

So the real question is whether there's any sense in which "recoverable" could apply to his global phase that I'm missing.

Actually, yes—there's a genuine steelman here. The global phase becomes observable and communicable once you introduce a phase reference or second system in a known phase relation. Through this superselection / reference frame perspective, what was private and unobservable becomes a relative phase that's measurable and shareable. This is remarkably similar to purification's mechanism, where discarded information becomes recoverable by enlarging the system.

But now I'm seeing the real tension: whether global phase is truly unrecoverable depends entirely on whether a shared phase reference exists. Without one—if U(1) superselection holds—the global phase is genuinely private and unrecoverable, matching the "non-clonable, non-communicable self-referential ignorance" framing. With a reference, it's no longer the observer's private global phase at all; it becomes a relative phase between systems.

So his own logic—that the fibre represents something private and non-communicable—actually commits him to the first case, where global phase is structurally unrecoverable, not just "discarded but recoverable." This is actually a strength of his framework because it clarifies exactly where he diverges from CDP and CLHS. And there's a deeper tension lurking: he seems to want the global phase to be both the source of the Born rule *and* something private and unobservable simultaneously.

But here's the problem—the Born rule derivation *depends* on the phase being unrecoverable and private. If it were recoverable, the whole U(1) invariance argument that generates the squaring would collapse. So calling it "recoverable" would actually undermine his own derivation. The correct framing is that the phase is discarded and irreducibly private, not recoverable—that unrecoverability is essential to how the argument works.

Now I'm noticing a potential conflation in the framework between global phase (which is gauge, private, and unrecoverable—the load-bearing part) and the relative phase between pointer states that gets discarded at measurement (which is actually recoverable in principle through recoherence or echo experiments, and that's the purification content). These are different things, and mixing them up would blur the distinction between what's truly gauge-private versus what's entanglement-private. The quaternionic Hopf fibration S³→S⁷→S⁴ is the right geometric object for the recoverable, purified case—the fibre encodes entanglement with the environment, and tracing out the partner qubit gives a mixed marginal that's recoverable from the global pure state. By contrast, the complex Hopf S¹→S³→S² fibre represents global phase, which is gauge-invariant and unrecoverable—that's the Born-rule engine. This distinction is precise and connects directly to the Mosseri-Dandoloff framework already in the research summary. I'm settling on a prose-heavy approach here—no bullet points, just tight arguments that stand on their own. The math on global phase is solid ground (it's gauge-invariant, unrecoverable, textbook), so I'll be direct there. On the interpretive side, especially around how this connects to the Born rule and diverges from CDP, I'll be precise but not overqualified. Let me verify the Mosseri-Dandoloff reference is complete before I draft the response.Not quite — and the interesting thing is that your own framework says the *opposite*, which is why I'd flag this as a place to be careful rather than a clean identification.

Here's the tension. "Discarded but always recoverable" is the purification/CLHS reading: the missing information is a *fact about a larger system*, and you get it back by accessing the ancilla. The global phase of the complex Hopf fibration is not that kind of object. The $S^1$ fibre is *gauge* — every observable $\langle\psi|A|\psi\rangle$ is invariant under $|\psi\rangle \mapsto e^{i\theta}|\psi\rangle$, so there is no measurement, on the system *or on any enlarged system*, that reveals it. It isn't discarded-and-recoverable; it's discarded-and-*unrecoverable*, because there's no fact there to recover. Your March 27 notes say this explicitly: the fibre is "the non-clonable part," "the non-communicable self-referential component," what "cannot be FANOUTed." That's the antithesis of recoverable. So if you wrote "discarded but recoverable" into the global phase, you'd be contradicting the very property your Born-rule derivation rests on.

And that property is load-bearing. The whole engine of your $p=|\psi|^2$ argument is: the phase is private → can't be cloned → can't enter a measurement result → observables must be $U(1)$-invariant → minimum-degree invariant is quadratic. If the global phase were recoverable, the "can't be FANOUTed" step weakens and the squaring loses its motivation. So you actively do *not* want the global phase to be recoverable. Unrecoverability is the feature, not a bug.

I think there are two different "discarded" things being run together, and only one of them is the purification content:

The **global phase** ($S^1$ fibre of $S^1\!\to\! S^3\!\to\! S^2$) is gauge — private, unobservable in principle, unrecoverable. This is your Born-rule engine.

The **relative phase / correlation with another system** — the which-path information that leaks into an environment and turns a pure state into a mixed marginal — *is* recoverable in principle (echo/recoherence experiments). *This* is the purification/CLHS object: trace out the partner, get a mixed state; reunite with the partner, recover purity. But geometrically this does not live in the complex Hopf fibre at all. A single qubit going mixed moves *into* the Bloch ball, off $S^2$, and the natural home is the **quaternionic** Hopf fibration $S^3\!\to\! S^7\!\to\! S^4$ — exactly the two-qubit Mosseri–Dandoloff picture already in your notes, where the fibre encodes the entanglement and the mixedness of one qubit's marginal is read off the Hopf map of the joint $S^7$ pure state. That fibre is your "discarded but recoverable." The $S^1$ one is not.

So the clean statement is: your framework localises *irreducibly private, non-purifiable* information in the complex Hopf fibre, and *recoverable correlational* information in the quaternionic fibre. Conflating them would muddy both the Born-rule argument (which needs the first to be unrecoverable) and the purification analogy (which needs the second).

This is actually the good outcome from last turn's question. Recall I asked whether your inside/outside structure is *compatible* with purification-as-axiom (same point, different chart) or *violates* it (sibling in the GPT class). The complex Hopf fibre is the answer: it is precisely a piece of information with **no purifying account** — irreducibly private, no larger system on which it becomes a recoverable fact. That is a clean violation of CDP's purification *uniqueness* clause. So your framework is a sibling of quantum theory in their operational class that fails purification at exactly the gauge/global-phase locus — which, if you can state it that sharply, is a genuinely distinctive structural claim for Paper 1, and it doubles as a precise statement of *where* and *why* you part company with the Church of the Larger Hilbert Space.

One caveat to keep honest: there's a reference-frame subtlety (Bartlett–Rudolph–Spekkens) where a "global" phase becomes a measurable *relative* phase once you have a shared phase reference. But invoking that reference is exactly making the phase shared/communicable — which by your own definition stops it being the observer's private self-referential ignorance. So that escape hatch costs you the Born-rule premise; you can't have the phase both private (for $|\psi|^2$) and recoverable (for purification) at once. Worth a sentence in the paper pre-empting it.

Want me to write this up as a short structural note for the corpus — "the two Hopf fibres carry categorically different kinds of discarded information, and only the quaternionic one is purification" — with the CDP-uniqueness-violation stated as a formal claim? It would slot in next to the FANOUT-boundary material.

*(thinking)*

 I'm recognizing that John is making a specific claim about his framework—that it identifies ignorance as something discarded yet always recoverable through the global phase structure of the Hopf fibration. I need to engage critically here, stress-testing the mathematical rigor of this connection and flagging where the argument might be vulnerable, since that's what he's asked for.

The mathematics is clear: the Hopf fibration $S^3 \to S^2$ with fiber $S^1$ exactly captures how global phase gets "forgotten" when projecting from the full state vector to the Bloch sphere. And his framework's derivation does connect global phase to private ignorance—it can't be FANOUTed, so observables must be U(1)-invariant, giving the Born rule. But here's where I need to push back: the global phase in the Hopf fibration isn't actually the same kind of "discarded but recoverable" information as what appears in purification. These are two conceptually distinct notions of information loss, and conflating them is where the argument starts to weaken. at play, and I think conflating them would be an error:

1. **Global phase** ($S^1$ fiber of Hopf): This is information that is *unobservable in principle* — no measurement on the system can reveal it, because all observables are U(1)-invariant. It's not "discarded and recoverable"; it's *gauge*. It is removed by the projection $S^3 \to S^2$ and is NOT recoverable by any operation on the system alone. In fact it's not even physical — there is no state of affairs that distinguishes $|\psi\rangle$ from $e^{i\theta}|\psi\rangle$. So calling it "ignorance" is already a stretch: it's not that you're ignorant of a fact; there is no fact.

2. **Purification's discarded subsystem**: In CDP/CLHS, a mixed state $\rho_A$ arises from a pure state $|\Psi\rangle_{AB}$ by tracing out $B$. The "discarded information" is the correlations with $B$ — and crucially this IS recoverable: if you get access to $B$, you can in principle do a joint measurement and recover the purity. The discarded thing is a relative phase and correlation structure entangled with another system, not a global phase.

These are fundamentally different: global phases are unobservable and unrecoverable by definition, while purification ancillas encode observable correlations that become accessible if you gain access to the full system. But I suspect John's pointing at something deeper — the Hopf fibration does connect to purification, just not at the level of global phases. For a single qubit, the relevant structure is how relative phases and entanglement emerge when you consider two qubits together, with the mixed state of one qubit sitting in the interior of the Bloch sphere.

The real connection is at the 2-qubit level: the quaternionic Hopf fibration $S^7 \to S^4$ describes 2-qubit entanglement (Mosseri-Dandoloff), where the fiber encodes the entanglement structure and the second qubit's conditional state. The concurrence of a 2-qubit state relates directly to this Hopf map. So if John's identifying purification with Hopf, he's likely pointing at this deeper quaternionic structure, not the simple $S^3 \to S^2$ picture.

But here's the crucial distinction: the global phase in the single-qubit $S^3 \to S^2$ fibration is unobservable gauge structure—it's discarded and fundamentally unrecoverable. Purification, by contrast, involves information that's discarded but *can* be recovered by accessing the purifying system. These are actually opposite situations, so the analogy breaks down at this level.

Though John's Born rule logic offers something genuinely interesting: he's treating global phase as private, non-cloneable information that can't be FANOUTed to an external observer. The Hopf fiber becomes a model of irreducibly private information—something that exists only from an internal perspective and can never be shared outward. That's precisely what CDP's purification axiom is designed to exclude, so they're in fundamental tension rather than alignment. wouldn't exist (everything is recoverable on the larger system).

So this actually supports the point I made last turn: John's FANOUT boundary might *violate* CDP's purification uniqueness, because the global phase is exactly a piece of information that is NOT recoverable on any larger system. That's the opposite of "discarded but recoverable."

So I think I should push back gently and carefully. The phrase "discarded but always recoverable" is the CLHS/purification reading. But the global phase is "discarded and never recoverable" (because unobservable/gauge). These are opposite. So if John wants to map his framework onto CDP, the global phase is the wrong object — OR, more interestingly, the global phase is precisely the thing that DISTINGUISHES his framework from CDP, the place where purification fails.

Now I need to be more careful about what "recoverable" actually means here. In interferometry, relative phases between qubits are recoverable through measurement, but global phases on a single qubit are fundamentally unobservable and can't be recovered. So the distinction hinges on whether we're talking about global versus relative phase, and whether we're looking at single-qubit or multi-qubit systems. I should lay out this distinction clearly and ask John which reading he intends, since the answer depends critically on these details. entanglement) structure.

Let me structure my response:

1. Acknowledge the appeal of the identification and what's right about it: the Hopf fibration $S^3 \to S^2$ projects out exactly the $U(1)$ global phase, and his Born-rule argument already lives there.

2. Flag the key precision issue: "discarded but recoverable" is the purification reading, but the global phase is the *opposite* — it's discarded and *unrecoverable* (gauge, unobservable in principle). There's no fact to recover. So as a model of purification it's actually backwards.

3. The right object for purification-as-Hopf is the two-qubit entanglement fibration ($S^7 \to S^4$, quaternionic Hopf, Mosseri-Dandoloff), where tracing out gives a genuinely mixed state and the discarded information is actually recoverable on the ancilla.

4. The deeper point: the global phase being irreducibly private and unrecoverable is where his framework should *diverge* from CDP — it's the FANOUT boundary made geometric. Rather than identifying his ignorance with purification, the global phase violates CDP's purification-uniqueness, which connects back to the structural question from last turn.

5. Ask which he means, or work it out together.

Now I'm checking the math: a single qubit state lives in $S^3$ within $\mathbb{C}^2$, and I need to verify how the Hopf fibration structure relates to the phase and density matrix geometry. Even with an ancilla system, global phase remains fundamentally unobservable because it's not a property of the physical state itself—only the ray matters. However, when dealing with mixed states and purifications, the information lost in the partial trace becomes recoverable if you have access to the purifying system; measuring that subsystem reveals which entangled branch you're in, recovering what was discarded.

Now I'm looking at how the quaternionic Hopf fibration structures two-qubit states: the $S^7$ sphere of normalized pure states maps to the $S^4$ base space through the $S^3$ fiber, where the fiber encodes entanglement properties and the base captures concurrence information. When you trace out one qubit, the remaining state becomes mixed, and this geometric structure captures that transition.

So the framework I'm developing is sound—discarding a subsystem produces a mixed state that's recoverable from the full pure state, which is exactly where purification lives geometrically. Though I should consider whether John might be making a different point: that the global phase marks a locus of self-referential ignorance in his Born-rule derivation, and he's trying to connect that separately to the CDP framework, rather than claiming the global phase itself models purification.

But he explicitly borrowed the phrase "discarded but always recoverable" from my description, so he is trying to link this to purification—which means my critique is the right one to make. I'll write this carefully in prose, flag the conceptual weakness clearly since he's asking for that, and keep it substantive without over-formatting.

The user wants independent stress-testing of his reasoning, not just a summary of his framework. He's aware his own project docs might contain mistakes, so pulling those risks me just echoing his framing back rather than giving him the critical check he values. I'll reason through the math directly instead.

Actually, I should do a quick search of his project knowledge to ground what his framework actually says about the Hopf global phase — that way my critique targets his real claim rather than a strawman version, which is more genuinely helpful.

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*(thinking)*

 I'm seeing how his framework maps the global phase onto the fibre of the Hopf bundle—it's the part that gets discarded during measurement, the non-clonable and non-communicable aspect that represents what can't be shared or transmitted between observers.

This is the crux of my critique: he's claiming the global phase is "discarded but recoverable," but that directly contradicts his own characterization of the fibre as fundamentally non-communicable and non-clonable. In purification, the discarded information is recoverable because it's encoded in an ancilla system you can access; here, by his own account, there's no such system—the global phase is private, observer-specific, and cannot be FANOUTed into any measurement outcome. So it's not recoverable in the same sense at all.

Let me be precise about the distinction: relative phase (like entanglement structure) is recoverable through interferometry or by accessing the ancilla, but global phase is fundamentally unobservable by gauge invariance. His Hopf fibre describes exactly the global phase of a single qubit, which means it's genuinely unrecoverable—there's no larger system that would make it a purifiable fact.

This cuts to the heart of why his framework actually diverges from the standard purification picture. His own mathematics already says the fibre is non-clonable and non-communicable, which contradicts calling it "recoverable." The slogan that discarded information is always recoverable describes purification's relative phases, not his global phase—they're categorically different objects, and conflating them is a mistake.

So the real question is whether there's any sense in which "recoverable" could apply to his global phase that I'm missing.

Actually, yes—there's a genuine steelman here. The global phase becomes observable and communicable once you introduce a phase reference or second system in a known phase relation. Through this superselection / reference frame perspective, what was private and unobservable becomes a relative phase that's measurable and shareable. This is remarkably similar to purification's mechanism, where discarded information becomes recoverable by enlarging the system.

But now I'm seeing the real tension: whether global phase is truly unrecoverable depends entirely on whether a shared phase reference exists. Without one—if U(1) superselection holds—the global phase is genuinely private and unrecoverable, matching the "non-clonable, non-communicable self-referential ignorance" framing. With a reference, it's no longer the observer's private global phase at all; it becomes a relative phase between systems.

So his own logic—that the fibre represents something private and non-communicable—actually commits him to the first case, where global phase is structurally unrecoverable, not just "discarded but recoverable." This is actually a strength of his framework because it clarifies exactly where he diverges from CDP and CLHS. And there's a deeper tension lurking: he seems to want the global phase to be both the source of the Born rule *and* something private and unobservable simultaneously.

But here's the problem—the Born rule derivation *depends* on the phase being unrecoverable and private. If it were recoverable, the whole U(1) invariance argument that generates the squaring would collapse. So calling it "recoverable" would actually undermine his own derivation. The correct framing is that the phase is discarded and irreducibly private, not recoverable—that unrecoverability is essential to how the argument works.

Now I'm noticing a potential conflation in the framework between global phase (which is gauge, private, and unrecoverable—the load-bearing part) and the relative phase between pointer states that gets discarded at measurement (which is actually recoverable in principle through recoherence or echo experiments, and that's the purification content). These are different things, and mixing them up would blur the distinction between what's truly gauge-private versus what's entanglement-private. The quaternionic Hopf fibration S³→S⁷→S⁴ is the right geometric object for the recoverable, purified case—the fibre encodes entanglement with the environment, and tracing out the partner qubit gives a mixed marginal that's recoverable from the global pure state. By contrast, the complex Hopf S¹→S³→S² fibre represents global phase, which is gauge-invariant and unrecoverable—that's the Born-rule engine. This distinction is precise and connects directly to the Mosseri-Dandoloff framework already in the research summary. I'm settling on a prose-heavy approach here—no bullet points, just tight arguments that stand on their own. The math on global phase is solid ground (it's gauge-invariant, unrecoverable, textbook), so I'll be direct there. On the interpretive side, especially around how this connects to the Born rule and diverges from CDP, I'll be precise but not overqualified. Let me verify the Mosseri-Dandoloff reference is complete before I draft the response.

Not quite — and the interesting thing is that your own framework says the *opposite*, which is why I'd flag this as a place to be careful rather than a clean identification.

Here's the tension. "Discarded but always recoverable" is the purification/CLHS reading: the missing information is a *fact about a larger system*, and you get it back by accessing the ancilla. The global phase of the complex Hopf fibration is not that kind of object. The $S^1$ fibre is *gauge* — every observable $\langle\psi|A|\psi\rangle$ is invariant under $|\psi\rangle \mapsto e^{i\theta}|\psi\rangle$, so there is no measurement, on the system *or on any enlarged system*, that reveals it. It isn't discarded-and-recoverable; it's discarded-and-*unrecoverable*, because there's no fact there to recover. Your March 27 notes say this explicitly: the fibre is "the non-clonable part," "the non-communicable self-referential component," what "cannot be FANOUTed." That's the antithesis of recoverable. So if you wrote "discarded but recoverable" into the global phase, you'd be contradicting the very property your Born-rule derivation rests on.

And that property is load-bearing. The whole engine of your $p=|\psi|^2$ argument is: the phase is private → can't be cloned → can't enter a measurement result → observables must be $U(1)$-invariant → minimum-degree invariant is quadratic. If the global phase were recoverable, the "can't be FANOUTed" step weakens and the squaring loses its motivation. So you actively do *not* want the global phase to be recoverable. Unrecoverability is the feature, not a bug.

I think there are two different "discarded" things being run together, and only one of them is the purification content:

The **global phase** ($S^1$ fibre of $S^1\!\to\! S^3\!\to\! S^2$) is gauge — private, unobservable in principle, unrecoverable. This is your Born-rule engine.

The **relative phase / correlation with another system** — the which-path information that leaks into an environment and turns a pure state into a mixed marginal — *is* recoverable in principle (echo/recoherence experiments). *This* is the purification/CLHS object: trace out the partner, get a mixed state; reunite with the partner, recover purity. But geometrically this does not live in the complex Hopf fibre at all. A single qubit going mixed moves *into* the Bloch ball, off $S^2$, and the natural home is the **quaternionic** Hopf fibration $S^3\!\to\! S^7\!\to\! S^4$ — exactly the two-qubit Mosseri–Dandoloff picture already in your notes, where the fibre encodes the entanglement and the mixedness of one qubit's marginal is read off the Hopf map of the joint $S^7$ pure state. That fibre is your "discarded but recoverable." The $S^1$ one is not.

So the clean statement is: your framework localises *irreducibly private, non-purifiable* information in the complex Hopf fibre, and *recoverable correlational* information in the quaternionic fibre. Conflating them would muddy both the Born-rule argument (which needs the first to be unrecoverable) and the purification analogy (which needs the second).

This is actually the good outcome from last turn's question. Recall I asked whether your inside/outside structure is *compatible* with purification-as-axiom (same point, different chart) or *violates* it (sibling in the GPT class). The complex Hopf fibre is the answer: it is precisely a piece of information with **no purifying account** — irreducibly private, no larger system on which it becomes a recoverable fact. That is a clean violation of CDP's purification *uniqueness* clause. So your framework is a sibling of quantum theory in their operational class that fails purification at exactly the gauge/global-phase locus — which, if you can state it that sharply, is a genuinely distinctive structural claim for Paper 1, and it doubles as a precise statement of *where* and *why* you part company with the Church of the Larger Hilbert Space.

One caveat to keep honest: there's a reference-frame subtlety (Bartlett–Rudolph–Spekkens) where a "global" phase becomes a measurable *relative* phase once you have a shared phase reference. But invoking that reference is exactly making the phase shared/communicable — which by your own definition stops it being the observer's private self-referential ignorance. So that escape hatch costs you the Born-rule premise; you can't have the phase both private (for $|\psi|^2$) and recoverable (for purification) at once. Worth a sentence in the paper pre-empting it.

Want me to write this up as a short structural note for the corpus — "the two Hopf fibres carry categorically different kinds of discarded information, and only the quaternionic one is purification" — with the CDP-uniqueness-violation stated as a formal claim? It would slot in next to the FANOUT-boundary material.
