# Complex versus quaternionic amplitudes in quantum mechanics

- conversation uuid: `bfa86321-a7e4-430e-bd79-8fd8c3b1ef8f`
- created: 2026-05-10T15:13:28.358333Z  |  updated: 2026-05-10T15:16:05.440056Z
- messages: 2  |  keyword score: 5

## Summary (from the Claude export)

**Conversation Overview**

The person is engaged in developing a theoretical physics framework that derives quantum mechanical structure from first principles, specifically from an observer's self-ignorance leading to negative probability, which via Shannon Information Theory necessitates analytic continuation of the logarithm function, yielding complex amplitudes. The conversation focused on a technically precise question: why should the framework stop at complex numbers rather than extending to quaternionic amplitudes via the logarithm of quaternions.

The person framed this as a natural extension question within their existing Cayley-Dickson tower framework, which already incorporates ℝ, ℂ, ℍ, and 𝕆 at different structural levels. Claude searched the project knowledge base to locate existing documentation on Aaronson's critique of quaternionic quantum mechanics and the seven-step theorem deriving complex amplitudes, then synthesised a response connecting the multi-valuedness of log(ℍ) to the physical interpretation of gauge structure.

The core technical resolution Claude provided was that log(ℍ) is not rejected but rather assigned to a different level of the tower than amplitudes. For complex numbers, log(−1) = iπ uniquely (up to 2π), giving a single U(1) phase; for quaternions, log(−1) = uπ where u ranges over an S² of unit pure imaginary quaternions, making the logarithm multi-valued across a 2-sphere. Three independent obstructions prevent this from functioning as an amplitude phase: tensor products of quaternionic Hilbert spaces fail to close naturally due to non-commutativity, the global phase structure expands from the abelian U(1) to non-abelian Sp(1) ≅ SU(2) which cannot be invisibly quotiented, and the seven-step information-theoretic derivation requires a unique imaginary correction rather than a sphere of choices. However, the S² of imaginary units that obstructs single-valued log(ℍ) is identified as precisely the structure that becomes SU(2) gauge symmetry, with the complex Hopf fibration S¹ → S³ → S² decomposing unit quaternions into amplitude phase (S¹, U(1)) and gauge base (S²). The framework's Moufang loop self-referential closure selects a preferred ℂ direction within ℍ, collapsing the S² ambiguity to a unique complex embedding while the remaining S² reappears as the electroweak gauge connection acting on amplitudes already residing in ℂ. The Cayley-Dickson levels are thus assigned distinct physical roles: log(ℂ) for amplitudes and Born rule, log(ℍ) for SU(2) gauge structure, and log(𝕆) for colour, generation, and flavour, terminating through non-associativity. A falsifiable prediction was noted: any genuinely quaternionic treatment of the amplitude itself should reduce without remainder to the standard ℂ-amplitude plus SU(2)-connection construction.

## Transcript

### 1. human  ·  2026-05-10 15:13:29

Complex amplitudes or quaternionic amplitudes? We've argued that complex amplitudes arise quite naturally if we consider an observer's self-ignorance leads to negative probability which by Shannon Information Theory means we have to use analytic continuation of the log function and hence complex amplitudes. But why stop at complex numbers, can we use the log of quaternions?

Complex amplitudes or quaternionic amplitudes? We've argued that complex amplitudes arise quite naturally if we consider an observer's self-ignorance leads to negative probability which by Shannon Information Theory means we have to use analytic continuation of the log function and hence complex amplitudes. But why stop at complex numbers, can we use the log of quaternions?

### 2. assistant  ·  2026-05-10 15:16:05

  I'm recognizing this as a serious technical question from John about his framework—specifically why complex amplitudes emerge from his construction rather than quaternionic ones, given that analytic continuation of the logarithm on negative probabilities naturally produces complex values. The question seems to cut off mid-sentence, but the core issue is clear: he's asking whether there's something fundamental about the log function's analytic structure that constrains the theory to complex rather than higher-dimensional algebras.

Looking at the mathematical structures: complex logarithms have a clean exponential map and manageable branch cut structure, whereas quaternionic logarithms introduce a fundamental non-commutativity problem—the exponential map doesn't preserve the usual composition rules, which would break the algebraic foundations needed for quantum amplitudes. This non-commutativity seems to be the key obstruction that naturally selects for complex numbers in his framework. Lawvere arguments → negative probability appears
3. Negative probability is mathematically meaningful only via analytic continuation
4. log(-1) = iπ → forced into complex numbers
5. Born rule: p = |ψ|² emerges from U(1) invariance of the global phase

Now, for quaternions:
- log(-1) in ℍ is *not unique* — it's any unit pure quaternion times π. That's a 2-sphere of solutions.
- This means the "phase" structure is U(1) for ℂ but Sp(1) ≅ SU(2) for ℍ.

But wait — John's framework already uses Hurwitz's theorem to argue that the *full* division algebra tower (ℝ, ℂ, ℍ, 𝕆) is needed. The amplitudes are complex (Hilbert space over ℂ) but the *internal symmetries* live in ℍ and 𝕆.

So the question is really: why do *amplitudes* live in ℂ specifically, when the framework uses all four normed division algebras?

The key constraint is that amplitudes need both associativity for tensor products to compose and commutativity for the amplitude structure itself — ℂ is the only division algebra satisfying both beyond ℝ. Real numbers fail because they can't support the off-diagonal phases needed for interference patterns, while quaternions break down for amplitudes precisely because their non-commutativity prevents a canonical tensor product structure. ules isn't naturally an ℍ-module).

Actually, let me think about this more carefully in the Adler/Finkelstein literature on quaternionic quantum mechanics. There ARE attempts at quaternionic QM. The problems are:

1. **Tensor products don't work nicely**: If H_A and H_B are ℍ-Hilbert spaces, H_A ⊗_ℍ H_B is not naturally an ℍ-Hilbert space because of non-commutativity.

2. **Composite systems**: This is the fundamental issue. You can't do bipartite quantum mechanics over ℍ in any natural way.

3. **Stueckelberg's argument**: Time evolution in quaternionic QM doesn't reduce to standard QM in any natural limit.

4. **Born rule structure**: The norm |ψ|² works fine over ℍ since it's always real and positive, but the phase structure expands from U(1) to Sp(1), which is richer but breaks the compositional properties we need.

So John's framework actually resolves this through the Cayley-Dickson tower—each level plays a distinct role. Complex numbers handle the amplitudes themselves, quaternions govern the gauge structure, and this layering prevents the pathologies that plague naive quaternionic quantum mechanics.

Now looking at the logarithm structure: for complex numbers, log(-1) = iπ where the phase is e^{iθ} in U(1), but for quaternions, log(-1) = uπ where u² = -1 traces out a 2-sphere, making the phase structure fundamentally different and incompatible with standard composition rules.

The key insight is that if amplitudes were quaternionic, their phase would be SU(2)-valued, but that's precisely what the framework assigns to the weak gauge group instead. So the Cayley-Dickson tower naturally separates the U(1) global phase of complex amplitudes from the SU(2) gauge structure—they belong at different levels for physical reasons, not arbitrary ones.

Now looking at the Lawvere diagonal argument more carefully: when you try to represent an observer completely, you hit information-theoretic limits. In complex numbers, going below zero requires one extension (the imaginary unit), giving a single-valued phase. But in quaternions, the logarithm of negative numbers is multi-valued across a 2-sphere, which is exactly the gauge structure you'd expect—the SU(2) symmetry fibered over the complex projective line. So the framework's prediction is that the phase structure naturally encodes both the Born rule's U(1) phase and the weak interaction's SU(2) gauge symmetry at their proper levels in the number system hierarchy. the act of self-referential closure picks out a single direction, reducing it to log(ℂ). This is really elegant — the question cuts right to the core of the framework, and I can see how multiple lines of reasoning converge here. The composition argument shows that ℂ is the only commutative-and-associative case for amplitude composition under tensor product. The Moufang loop self-reference mechanism does exactly what's needed: it breaks the S² degeneracy by forcing a unique choice. And the quaternionic logarithm isn't discarded — it reappears as the gauge structure itself, not as amplitude phase.

So the S² of imaginary units becomes the source of SU(2) gauge symmetry, and the framework actually gives a layered answer: log(ℂ) for amplitudes, log(ℍ) for gauge, log(𝕆) for generation and flavor structure. Each level of the Cayley-Dickson tower serves a different physical role for principled mathematical reasons. This aligns with how John's developed the connections between these algebraic levels and physical structures.

I'm also thinking about Adler's quaternionic quantum mechanics from 1995 — he explored whether quaternions could replace complex numbers as the foundation, but ran into fundamental issues with how tensor products behave in that setting.  Without a natural way to handle composite systems or proper time evolution, Adler had to impose a preferred imaginary direction through complexification, which is exactly the kind of arbitrary choice the Moufang loop structure in this framework avoids.

Now I'm considering what negative probability actually means in quaternionic amplitudes. In complex QM, probabilities are always non-negative since |ψ|² is real and positive, though quasi-probabilities like Wigner functions can dip below zero. With quaternions, |ψ|² is still real and non-negative, but the phase structure becomes SU(2)-valued, making the quasi-probability landscape fundamentally richer. The difference is that achieving "negative" values in complex space requires rotating by π in one dimension, whereas in quaternions you're choosing an axis on the sphere.

The real resolution is that the framework doesn't force a choice between complex and quaternionic amplitudes — it deploys both at different levels of the Cayley-Dickson hierarchy, where complex handles the electromagnetic phase structure, quaternions encode the weak gauge connection, and octonions capture generation structure. Each level's logarithmic structure carries distinct physical meaning, and amplitudes stay complex because tensor product composition demands commutativity, but that constraint doesn't apply at higher structural levels. I should check the project knowledge to see if this extension has been addressed before, even though the user is asking for critical reasoning rather than documentation lookup—it's worth a quick search to make sure I'm not missing relevant context.
```
This block is not supported on your current device yet.
```

 The search results confirm the framework already covers Aaronson's critique of quaternions in the Pure_states_and_mixed_states document, so now I need to dig into the specific details about the log structure.
```
This block is not supported on your current device yet.
```

 I've found the relevant documentation in the project—there's already a detailed analysis of Aaronson's critique of quaternionic amplitudes, and I can see how the seven-step chain connects epistemological probability through Shannon entropy, negative quasi-probabilities, and logarithms to complex numbers. Now I can give John a substantive answer about why the framework stops at the logarithmic step.

The core issue is that quaternionic logarithms are fundamentally non-unique: for any quaternion, the logarithm's imaginary part can point in any direction on a 2-sphere of unit pure quaternions, whereas complex logarithms have only one solution up to 2π periodicity. Beyond this mathematical obstruction, Aaronson's three arguments—parameter counting for tensor products, the non-Hermiticity problem leading to superluminal signaling, and Wootters' constraint that random states must be uniform on the probability simplex—all force the framework back to complex numbers. But here's the key: the framework doesn't actually abandon quaternions entirely; it deploys them at a different structural level than the amplitude representation.

The multi-valuedness of log(ℍ) isn't a bug—it's the gauge structure itself. The 2-sphere of imaginary units that emerges from the non-uniqueness of quaternionic logarithms corresponds to the SU(2) gauge sector, and this pattern continues up the Cayley-Dickson tower: octonions introduce the flavor and generation structure that terminates the tower through non-associativity. So quaternions are used, but their logarithmic ambiguity encodes the gauge symmetries rather than the quantum amplitudes. Self-reference picks out a preferred complex direction within the quaternions, collapsing the multi-valued logarithm back to single-valued. For composition, amplitudes need both associativity and commutativity under tensor products—properties only complex numbers satisfy. The real insight is that the framework doesn't pit these algebras against each other; instead, it deploys each at its proper level: complex numbers for amplitudes and their phases, quaternions for the gauge structure that emerges from the multi-valuedness we quotient away. The logarithm's multi-valuedness is the key constraint — for quaternions, log(-1) doesn't have a unique value like it does for complex numbers, but rather a whole 2-sphere of solutions. This sphere structure creates fundamental problems when trying to build quantum amplitudes from quaternions. Now I'm working through three independent obstructions that prevent quaternionic amplitudes from working in practice, starting with how tensor products of quaternionic systems fail to close properly. ℋ_A ⊗_ℍ ℋ_B is not naturally an ℍ-module (non-commutativity blocks the canonical structure). Concretely: tensor products of quaternionic Hermitian matrices need not be Hermitian, which Aaronson exploits to derive superluminal signalling. Already in your project knowledge under the Aaronson arguments.

The Born rule also degenerates differently in quaternions. In ℂ, the global phase e^{iθ} ∈ U(1) is the kernel of the modulus map — exactly large enough to host unobservable self-referential ignorance and exactly small enough to be eliminable by FANOUT-incompatibility. But in ℍ, the analogous global phase would be Sp(1) ≅ SU(2) ≅ S³, which has internal structure and can't be quotiented out invisibly.

The seven-step theorem also breaks down because log(p) for negative p requires a well-defined imaginary correction. In ℂ, log(-|p|) = log|p| + iπ is unique up to 2π multiples, but in ℍ the same expression gives log|p| + uπ where u ranges over S² — the correction becomes a sphere rather than a number, and the information-theoretic argument can't conclude. Yet the framework does actually use log(ℍ).

The obstruction to single-valued log(ℍ) — that S² of imaginary units — is precisely what becomes gauge symmetry. The Hopf fibration S¹ → S³ → S² decomposes the unit quaternions: each choice of imaginary direction u ∈ S² gives a copy of ℂ_u inside ℍ, contributing an S¹ phase, with the S² of choices remaining as the base. That S¹ is the amplitude phase under U(1), while the S² is the weak isospin structure.

The Cayley-Dickson tower stratifies by physical meaning: log(ℂ) yields the amplitude phase (single-valued, U(1), Born rule), log(ℍ) produces the SU(2) gauge structure with its S² of choices forming the electroweak doublet base, and log(𝕆) terminates due to non-associativity, encoding colour, generation, and flavour. The Moufang loop closure selects a preferred ℂ direction at the self-referential step, collapsing the S² ambiguity in log(ℍ) to a unique ℂ — but that S² doesn't vanish; it reappears as gauge degrees of freedom acting on amplitudes already living in ℂ. So the dichotomy "why not log of quaternions?" dissolves: both happen, with log(ℂ) providing the amplitude itself. log(ℍ) gives you the connection that acts on amplitudes. They're not competing for the amplitude slot — they're at different levels of the same tower.

Let me verify the structure here: Sp(1) is indeed the unit quaternions, isomorphic to SU(2) and S³. For the Hopf fibration, I need to be precise — the complex version S¹ → S³ → S² describes how unit quaternions decompose, where S² parametrizes the choice of rotation axis and S¹ captures the rotation angle around that axis.

I should also note that the user's coding background in Elixir and Rails isn't relevant here since this is pure mathematics, so I'll stick with British spellings like "parametrises" to match the conversation style.

The framing matters too — John's already worked extensively on Cayley-Dickson levels and gauge structure, so I'm connecting his existing framework to the specific question about log(ℍ) rather than introducing something entirely new. The novel part is explicitly linking the multi-valuedness of log(ℍ) to SU(2) gauge structure, which he hasn't framed quite this way before.Good question — and the framework actually has a more interesting answer than "we just stop because amplitudes need to be commutative."

**The setup.** For q ∈ ℍ ∖ {0}, write q = |q|(cos θ + u sin θ) where u is a unit pure quaternion (u² = −1). Then log(q) = log|q| + uθ. The exponential map is fine, the algebra is closed, the norm is multiplicative. So log(ℍ) exists — but it is multi-valued in a way log(ℂ) is not. The set {u ∈ Im(ℍ) : u² = −1} is the **2-sphere** S² ⊂ ℝ³. So log(−1) has an entire S² of solutions in ℍ, not just iπ. Hold that sphere in mind — it's the whole story.

**Three independent obstructions to using log(ℍ) for amplitudes**

1. **Tensor product breaks.** Composition of subsystems requires the amplitude space to admit a tensor product that is itself an amplitude space of the same kind. For ℍ-modules, ℋ_A ⊗_ℍ ℋ_B is not naturally an ℍ-module — non-commutativity blocks the canonical structure. Aaronson's three arguments (parameter counting, non-Hermiticity of tensored Hermitians → superluminal signalling, Wootters' Goldilocks) all bite here. Already documented under the Pure-and-Mixed-States note.

2. **Born rule degenerates.** In ℂ, p = |ψ|² has a single global phase e^{iθ} ∈ U(1) — the kernel of the modulus map. Self-referential ignorance has to live somewhere unobservable, and U(1) is exactly large enough to host it and exactly small enough to be eliminable by FANOUT-incompatibility (your existing argument). In ℍ, the analogous "global phase" is Sp(1) ≅ SU(2) ≅ S³ — not a phase you can quietly quotient out. It's non-abelian, with three generators and internal structure that *would* be observable if it were the amplitude phase.

3. **The seven-step theorem can't close.** Step 6 needs log(−|p|) to land at a well-defined imaginary correction iπ. In ℍ the corresponding correction is log|p| + uπ with u ∈ S². The "imaginary correction" stops being a number and becomes a sphere of choices. The information-theoretic conclusion no longer follows.

**But — and this is the interesting bit — the framework does use log(ℍ).** Just not for amplitudes.

That S² of imaginary units obstructing a single-valued log(ℍ) is *exactly* the structure that becomes gauge. The unit quaternions form S³ = SU(2) as a group manifold. The complex Hopf fibration S¹ → S³ → S² unpacks it: pick u ∈ S², get an embedded copy ℂ_u = ℝ + ℝu ⊂ ℍ; each ℂ_u contributes an S¹ phase; the S² of choices is what remains. The S¹ becomes U(1) of amplitude phase; the S² is the base on which weak isospin lives.

The Cayley-Dickson tower partitions by physical role:

- log(ℂ): single-valued. Phase, U(1), Born rule, amplitude.
- log(ℍ): S² of choices. SU(2) gauge structure, electroweak doublet base.
- log(𝕆): non-associative, terminates the tower. Colour / generations / flavour.

The Moufang-loop "Seven Rights Can Make a Left" closure picks the preferred ℂ direction at the self-referential step, collapsing the S² ambiguity in log(ℍ) to a unique ℂ — but the rest of the S² isn't lost. It re-appears as the SU(2) connection acting on amplitudes that already live in ℂ.

So in framework language the dichotomy is wrong. log(ℂ) gives you the amplitude; log(ℍ) gives you the connection that acts on amplitudes. They aren't competing for the amplitude slot — they're at different levels of the same tower, and the framework needs both.

One falsifiable upshot worth flagging: this picture predicts that anything "quaternionic" about the amplitude itself (Adler-style quaternionic QM, or attempts to put SU(2) gauge content directly into the wavefunction phase rather than into an external connection) should be derivable from the standard ℂ-amplitude + SU(2)-gauge construction without remainder. Any genuine surplus would falsify the level-assignment.

 

*(thinking)*

 I'm recognizing this as a serious technical question from John about his framework—specifically why complex amplitudes emerge from his construction rather than quaternionic ones, given that analytic continuation of the logarithm on negative probabilities naturally produces complex values. The question seems to cut off mid-sentence, but the core issue is clear: he's asking whether there's something fundamental about the log function's analytic structure that constrains the theory to complex rather than higher-dimensional algebras.

Looking at the mathematical structures: complex logarithms have a clean exponential map and manageable branch cut structure, whereas quaternionic logarithms introduce a fundamental non-commutativity problem—the exponential map doesn't preserve the usual composition rules, which would break the algebraic foundations needed for quantum amplitudes. This non-commutativity seems to be the key obstruction that naturally selects for complex numbers in his framework. Lawvere arguments → negative probability appears
3. Negative probability is mathematically meaningful only via analytic continuation
4. log(-1) = iπ → forced into complex numbers
5. Born rule: p = |ψ|² emerges from U(1) invariance of the global phase

Now, for quaternions:
- log(-1) in ℍ is *not unique* — it's any unit pure quaternion times π. That's a 2-sphere of solutions.
- This means the "phase" structure is U(1) for ℂ but Sp(1) ≅ SU(2) for ℍ.

But wait — John's framework already uses Hurwitz's theorem to argue that the *full* division algebra tower (ℝ, ℂ, ℍ, 𝕆) is needed. The amplitudes are complex (Hilbert space over ℂ) but the *internal symmetries* live in ℍ and 𝕆.

So the question is really: why do *amplitudes* live in ℂ specifically, when the framework uses all four normed division algebras?

The key constraint is that amplitudes need both associativity for tensor products to compose and commutativity for the amplitude structure itself — ℂ is the only division algebra satisfying both beyond ℝ. Real numbers fail because they can't support the off-diagonal phases needed for interference patterns, while quaternions break down for amplitudes precisely because their non-commutativity prevents a canonical tensor product structure. ules isn't naturally an ℍ-module).

Actually, let me think about this more carefully in the Adler/Finkelstein literature on quaternionic quantum mechanics. There ARE attempts at quaternionic QM. The problems are:

1. **Tensor products don't work nicely**: If H_A and H_B are ℍ-Hilbert spaces, H_A ⊗_ℍ H_B is not naturally an ℍ-Hilbert space because of non-commutativity.

2. **Composite systems**: This is the fundamental issue. You can't do bipartite quantum mechanics over ℍ in any natural way.

3. **Stueckelberg's argument**: Time evolution in quaternionic QM doesn't reduce to standard QM in any natural limit.

4. **Born rule structure**: The norm |ψ|² works fine over ℍ since it's always real and positive, but the phase structure expands from U(1) to Sp(1), which is richer but breaks the compositional properties we need.

So John's framework actually resolves this through the Cayley-Dickson tower—each level plays a distinct role. Complex numbers handle the amplitudes themselves, quaternions govern the gauge structure, and this layering prevents the pathologies that plague naive quaternionic quantum mechanics.

Now looking at the logarithm structure: for complex numbers, log(-1) = iπ where the phase is e^{iθ} in U(1), but for quaternions, log(-1) = uπ where u² = -1 traces out a 2-sphere, making the phase structure fundamentally different and incompatible with standard composition rules.

The key insight is that if amplitudes were quaternionic, their phase would be SU(2)-valued, but that's precisely what the framework assigns to the weak gauge group instead. So the Cayley-Dickson tower naturally separates the U(1) global phase of complex amplitudes from the SU(2) gauge structure—they belong at different levels for physical reasons, not arbitrary ones.

Now looking at the Lawvere diagonal argument more carefully: when you try to represent an observer completely, you hit information-theoretic limits. In complex numbers, going below zero requires one extension (the imaginary unit), giving a single-valued phase. But in quaternions, the logarithm of negative numbers is multi-valued across a 2-sphere, which is exactly the gauge structure you'd expect—the SU(2) symmetry fibered over the complex projective line. So the framework's prediction is that the phase structure naturally encodes both the Born rule's U(1) phase and the weak interaction's SU(2) gauge symmetry at their proper levels in the number system hierarchy. the act of self-referential closure picks out a single direction, reducing it to log(ℂ). This is really elegant — the question cuts right to the core of the framework, and I can see how multiple lines of reasoning converge here. The composition argument shows that ℂ is the only commutative-and-associative case for amplitude composition under tensor product. The Moufang loop self-reference mechanism does exactly what's needed: it breaks the S² degeneracy by forcing a unique choice. And the quaternionic logarithm isn't discarded — it reappears as the gauge structure itself, not as amplitude phase.

So the S² of imaginary units becomes the source of SU(2) gauge symmetry, and the framework actually gives a layered answer: log(ℂ) for amplitudes, log(ℍ) for gauge, log(𝕆) for generation and flavor structure. Each level of the Cayley-Dickson tower serves a different physical role for principled mathematical reasons. This aligns with how John's developed the connections between these algebraic levels and physical structures.

I'm also thinking about Adler's quaternionic quantum mechanics from 1995 — he explored whether quaternions could replace complex numbers as the foundation, but ran into fundamental issues with how tensor products behave in that setting.  Without a natural way to handle composite systems or proper time evolution, Adler had to impose a preferred imaginary direction through complexification, which is exactly the kind of arbitrary choice the Moufang loop structure in this framework avoids.

Now I'm considering what negative probability actually means in quaternionic amplitudes. In complex QM, probabilities are always non-negative since |ψ|² is real and positive, though quasi-probabilities like Wigner functions can dip below zero. With quaternions, |ψ|² is still real and non-negative, but the phase structure becomes SU(2)-valued, making the quasi-probability landscape fundamentally richer. The difference is that achieving "negative" values in complex space requires rotating by π in one dimension, whereas in quaternions you're choosing an axis on the sphere.

The real resolution is that the framework doesn't force a choice between complex and quaternionic amplitudes — it deploys both at different levels of the Cayley-Dickson hierarchy, where complex handles the electromagnetic phase structure, quaternions encode the weak gauge connection, and octonions capture generation structure. Each level's logarithmic structure carries distinct physical meaning, and amplitudes stay complex because tensor product composition demands commutativity, but that constraint doesn't apply at higher structural levels. I should check the project knowledge to see if this extension has been addressed before, even though the user is asking for critical reasoning rather than documentation lookup—it's worth a quick search to make sure I'm not missing relevant context.

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*(thinking)*

 The search results confirm the framework already covers Aaronson's critique of quaternions in the Pure_states_and_mixed_states document, so now I need to dig into the specific details about the log structure.

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*(thinking)*

 I've found the relevant documentation in the project—there's already a detailed analysis of Aaronson's critique of quaternionic amplitudes, and I can see how the seven-step chain connects epistemological probability through Shannon entropy, negative quasi-probabilities, and logarithms to complex numbers. Now I can give John a substantive answer about why the framework stops at the logarithmic step.

The core issue is that quaternionic logarithms are fundamentally non-unique: for any quaternion, the logarithm's imaginary part can point in any direction on a 2-sphere of unit pure quaternions, whereas complex logarithms have only one solution up to 2π periodicity. Beyond this mathematical obstruction, Aaronson's three arguments—parameter counting for tensor products, the non-Hermiticity problem leading to superluminal signaling, and Wootters' constraint that random states must be uniform on the probability simplex—all force the framework back to complex numbers. But here's the key: the framework doesn't actually abandon quaternions entirely; it deploys them at a different structural level than the amplitude representation.

The multi-valuedness of log(ℍ) isn't a bug—it's the gauge structure itself. The 2-sphere of imaginary units that emerges from the non-uniqueness of quaternionic logarithms corresponds to the SU(2) gauge sector, and this pattern continues up the Cayley-Dickson tower: octonions introduce the flavor and generation structure that terminates the tower through non-associativity. So quaternions are used, but their logarithmic ambiguity encodes the gauge symmetries rather than the quantum amplitudes. Self-reference picks out a preferred complex direction within the quaternions, collapsing the multi-valued logarithm back to single-valued. For composition, amplitudes need both associativity and commutativity under tensor products—properties only complex numbers satisfy. The real insight is that the framework doesn't pit these algebras against each other; instead, it deploys each at its proper level: complex numbers for amplitudes and their phases, quaternions for the gauge structure that emerges from the multi-valuedness we quotient away. The logarithm's multi-valuedness is the key constraint — for quaternions, log(-1) doesn't have a unique value like it does for complex numbers, but rather a whole 2-sphere of solutions. This sphere structure creates fundamental problems when trying to build quantum amplitudes from quaternions. Now I'm working through three independent obstructions that prevent quaternionic amplitudes from working in practice, starting with how tensor products of quaternionic systems fail to close properly. ℋ_A ⊗_ℍ ℋ_B is not naturally an ℍ-module (non-commutativity blocks the canonical structure). Concretely: tensor products of quaternionic Hermitian matrices need not be Hermitian, which Aaronson exploits to derive superluminal signalling. Already in your project knowledge under the Aaronson arguments.

The Born rule also degenerates differently in quaternions. In ℂ, the global phase e^{iθ} ∈ U(1) is the kernel of the modulus map — exactly large enough to host unobservable self-referential ignorance and exactly small enough to be eliminable by FANOUT-incompatibility. But in ℍ, the analogous global phase would be Sp(1) ≅ SU(2) ≅ S³, which has internal structure and can't be quotiented out invisibly.

The seven-step theorem also breaks down because log(p) for negative p requires a well-defined imaginary correction. In ℂ, log(-|p|) = log|p| + iπ is unique up to 2π multiples, but in ℍ the same expression gives log|p| + uπ where u ranges over S² — the correction becomes a sphere rather than a number, and the information-theoretic argument can't conclude. Yet the framework does actually use log(ℍ).

The obstruction to single-valued log(ℍ) — that S² of imaginary units — is precisely what becomes gauge symmetry. The Hopf fibration S¹ → S³ → S² decomposes the unit quaternions: each choice of imaginary direction u ∈ S² gives a copy of ℂ_u inside ℍ, contributing an S¹ phase, with the S² of choices remaining as the base. That S¹ is the amplitude phase under U(1), while the S² is the weak isospin structure.

The Cayley-Dickson tower stratifies by physical meaning: log(ℂ) yields the amplitude phase (single-valued, U(1), Born rule), log(ℍ) produces the SU(2) gauge structure with its S² of choices forming the electroweak doublet base, and log(𝕆) terminates due to non-associativity, encoding colour, generation, and flavour. The Moufang loop closure selects a preferred ℂ direction at the self-referential step, collapsing the S² ambiguity in log(ℍ) to a unique ℂ — but that S² doesn't vanish; it reappears as gauge degrees of freedom acting on amplitudes already living in ℂ. So the dichotomy "why not log of quaternions?" dissolves: both happen, with log(ℂ) providing the amplitude itself. log(ℍ) gives you the connection that acts on amplitudes. They're not competing for the amplitude slot — they're at different levels of the same tower.

Let me verify the structure here: Sp(1) is indeed the unit quaternions, isomorphic to SU(2) and S³. For the Hopf fibration, I need to be precise — the complex version S¹ → S³ → S² describes how unit quaternions decompose, where S² parametrizes the choice of rotation axis and S¹ captures the rotation angle around that axis.

I should also note that the user's coding background in Elixir and Rails isn't relevant here since this is pure mathematics, so I'll stick with British spellings like "parametrises" to match the conversation style.

The framing matters too — John's already worked extensively on Cayley-Dickson levels and gauge structure, so I'm connecting his existing framework to the specific question about log(ℍ) rather than introducing something entirely new. The novel part is explicitly linking the multi-valuedness of log(ℍ) to SU(2) gauge structure, which he hasn't framed quite this way before.

Good question — and the framework actually has a more interesting answer than "we just stop because amplitudes need to be commutative."

**The setup.** For q ∈ ℍ ∖ {0}, write q = |q|(cos θ + u sin θ) where u is a unit pure quaternion (u² = −1). Then log(q) = log|q| + uθ. The exponential map is fine, the algebra is closed, the norm is multiplicative. So log(ℍ) exists — but it is multi-valued in a way log(ℂ) is not. The set {u ∈ Im(ℍ) : u² = −1} is the **2-sphere** S² ⊂ ℝ³. So log(−1) has an entire S² of solutions in ℍ, not just iπ. Hold that sphere in mind — it's the whole story.

**Three independent obstructions to using log(ℍ) for amplitudes**

1. **Tensor product breaks.** Composition of subsystems requires the amplitude space to admit a tensor product that is itself an amplitude space of the same kind. For ℍ-modules, ℋ_A ⊗_ℍ ℋ_B is not naturally an ℍ-module — non-commutativity blocks the canonical structure. Aaronson's three arguments (parameter counting, non-Hermiticity of tensored Hermitians → superluminal signalling, Wootters' Goldilocks) all bite here. Already documented under the Pure-and-Mixed-States note.

2. **Born rule degenerates.** In ℂ, p = |ψ|² has a single global phase e^{iθ} ∈ U(1) — the kernel of the modulus map. Self-referential ignorance has to live somewhere unobservable, and U(1) is exactly large enough to host it and exactly small enough to be eliminable by FANOUT-incompatibility (your existing argument). In ℍ, the analogous "global phase" is Sp(1) ≅ SU(2) ≅ S³ — not a phase you can quietly quotient out. It's non-abelian, with three generators and internal structure that *would* be observable if it were the amplitude phase.

3. **The seven-step theorem can't close.** Step 6 needs log(−|p|) to land at a well-defined imaginary correction iπ. In ℍ the corresponding correction is log|p| + uπ with u ∈ S². The "imaginary correction" stops being a number and becomes a sphere of choices. The information-theoretic conclusion no longer follows.

**But — and this is the interesting bit — the framework does use log(ℍ).** Just not for amplitudes.

That S² of imaginary units obstructing a single-valued log(ℍ) is *exactly* the structure that becomes gauge. The unit quaternions form S³ = SU(2) as a group manifold. The complex Hopf fibration S¹ → S³ → S² unpacks it: pick u ∈ S², get an embedded copy ℂ_u = ℝ + ℝu ⊂ ℍ; each ℂ_u contributes an S¹ phase; the S² of choices is what remains. The S¹ becomes U(1) of amplitude phase; the S² is the base on which weak isospin lives.

The Cayley-Dickson tower partitions by physical role:

- log(ℂ): single-valued. Phase, U(1), Born rule, amplitude.
- log(ℍ): S² of choices. SU(2) gauge structure, electroweak doublet base.
- log(𝕆): non-associative, terminates the tower. Colour / generations / flavour.

The Moufang-loop "Seven Rights Can Make a Left" closure picks the preferred ℂ direction at the self-referential step, collapsing the S² ambiguity in log(ℍ) to a unique ℂ — but the rest of the S² isn't lost. It re-appears as the SU(2) connection acting on amplitudes that already live in ℂ.

So in framework language the dichotomy is wrong. log(ℂ) gives you the amplitude; log(ℍ) gives you the connection that acts on amplitudes. They aren't competing for the amplitude slot — they're at different levels of the same tower, and the framework needs both.

One falsifiable upshot worth flagging: this picture predicts that anything "quaternionic" about the amplitude itself (Adler-style quaternionic QM, or attempts to put SU(2) gauge content directly into the wavefunction phase rather than into an external connection) should be derivable from the standard ℂ-amplitude + SU(2)-gauge construction without remainder. Any genuine surplus would falsify the level-assignment.
