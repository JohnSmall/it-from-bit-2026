# Rovelli's derivation of the action quantity

- conversation uuid: `cff1de9e-faa7-44fb-95f5-18eb09a80cb7`
- created: 2026-06-06T09:39:03.269990Z  |  updated: 2026-06-06T10:04:43.045621Z
- messages: 6  |  keyword score: 3

## Summary (from the Claude export)

**Conversation Overview**

The person is actively writing Paper 1 of a larger research project on the foundations of physics, specifically paragraphs connecting predictor self-knowledge, the action quantum, and relational quantum mechanics. The conversation began with a request to summarise Carlo Rovelli's 1996 "Relational Quantum Mechanics" paper with particular focus on how Rovelli derives Planck's constant ℏ. Claude explained Rovelli's relational interpretation (physical quantities have values only relative to other systems), his two postulates (finite information capacity as a ceiling, unlimited new information), and the dimensional argument by which ℏ emerges as the bit-to-action conversion factor — noting that Rovelli postulates finite capacity rather than deriving it, and asserts universality without justification.

The person then introduced their own framework connecting Karl Popper's indeterminism argument to the action quantum: the self-knowledge of a predictor becomes critical at the scale of its smallest component (e.g., the smallest cog of a Babbage analytical engine), and any change that alters the trajectory in phase space must have the dimension of action. They observed that Rovelli reaches the same conclusion but postulates finite information capacity ad hoc where their framework would derive it from self-reference constraints. Claude developed this by separating two sub-claims — the action *dimension* (coming from symplectic geometry and conjugacy, upstream in the framework's division-algebra spine) versus the *floor* on cell size (where the Popper/Lawvere diagonal obstruction does the genuine work) — and noting that Rovelli's postulate targets the ceiling (≤ N bits) while the self-reference route targets the floor directly, making the framework's approach better-aimed for the ℏ derivation specifically. Claude also raised the FANOUT boundary connection: ℏ is the reversible pre-FANOUT phase-space resolution while kT ln2 is the post-FANOUT irreversible-record cost, suggesting the predictor self-knowledge argument yields both floors on either side of the boundary already present in the corpus.

The person then requested the exact Popper construction pulled from the Part I and Part II PDFs for use in the paragraphs being drafted. Claude extracted and OCR'd both scanned JSTOR archives, identified the key passages, and provided a detailed reconstruction covering: the Babbage-style predictor setup (Part I §3, p. 123); the amplifier lemma establishing that predictors must amplify minute differences (Part I §7, pp. 129–130); Popper's own ℏ remark distinguishing classical from quantum indeterminacy (Part I §6, p. 128); the minimum apparatus scale and minimum time-per-bit bounds (Part I p. 132, Part II p. 192); the Gödelian self-prediction core invoking Gödel's second theorem by name with Rosser, Tarski, and Turing footnoted (Part II §III, pp. 179–183); and the self-information impossibility lemma (Part II §III, pp. 189–191). Claude provided a synthesis positioning Popper against Rovelli: Popper derives the self-prediction obstruction and supplies both factors whose product is action but never forms the product or claims universality; Rovelli supplies the universality and ℏ identification by postulate; the framework's novel contribution is identifying Popper's Gödelian floor as the mechanism Rovelli's Postulate 1 merely asserts. A caution was noted that Popper himself believed the classical obstruction operates at ℏ = 0, so the ℏ-from-self-reference reading is the framework's bridge, not Popper's own claim. The session ended with Claude offering to write a corpus-ready markdown summary with page anchors and BibTeX entries for both Popper parts.

## Transcript

### 1. human  ·  2026-06-06 09:39:04

Please summarise this from Carlo Rovelli , I'm particularly interested in how he derives the action quantity

Please summarise this from Carlo Rovelli , I'm particularly interested in how he derives the action quantity

### 2. assistant  ·  2026-06-06 09:39:44

 The user has uploaded Rovelli's 1996 "Relational Quantum Mechanics" paper and wants me to summarize it, focusing on how he derives the action quantum—Planck's constant ℏ. I can see the paper in context. In section III.B, Rovelli discusses Postulate 1 about limited information and notes that it already introduces Planck's constant into classical physics, and I'm looking at where he derives ℏ from the relational framework.

This connects to information-theoretic foundations and relationalist approaches, which are relevant to the broader research context, but I should keep the focus tight on what the user asked for. I'll give a substantive summary in plain prose, emphasizing the ℏ derivation since that's the explicit interest. The key argument appears around pages 11-12: Postulate 1 establishes that there's a maximum amount of relevant information extractable from any system, and any prediction can be inferred from a finite string rather than an infinite one.

The dimensional argument for ℏ is the core move here. Classical continuous variables like position can be localized with arbitrary precision in phase space, which would require infinite information. But if information capacity is finite, then the state can only be localized within a finite region of phase space. Since conjugate pairs (position × momentum) have dimensions of action, there must be a universal constant with those same dimensions that sets the minimal localizability—the size of the elementary phase-space cell. That constant is Planck's constant, which essentially converts between physical phase-space units and information-theoretic units measured in bits.

I should be clear that this is a heuristic dimensional argument rather than a rigorous derivation, and Rovelli himself is modest about the rigor of the whole reconstruction. I'll structure the response with a brief overview of the paper's thesis and postulates, then focus on the ℏ derivation since that's what matters most. Given the audience is a physicist working on related foundations, I can stay technical and keep it mostly in prose rather than breaking it into bullet points.Rovelli's 1996 paper proposes that the measurement problem is an artefact of a bad concept — the *observer-independent state*. His analogy is Einstein on the Lorentz transformations: the formalism was already there; what was missing was recognising that an implicit assumption (absolute simultaneity, in that case) was untenable. Here the offending assumption is that a system has a state, or that physical quantities have values, independently of some other system relative to which they are defined.

The argument runs from a single observation: take a measurement of S by O, then describe the *same* events from a third system P who treats S–O as one quantum system. For O the variable q has value 1 at t₂; for P the S–O pair is in an entangled superposition and q has no determined value. Both descriptions are correct quantum mechanics (P's is just Schrödinger evolution applied to S+O). Rovelli refuses to privilege either, and works through eight objections to show you can't escape this without either breaking linearity or smuggling in a special class of "classical" systems. His resolution: state and value are *relational*, like velocity in Galilean mechanics. "q = 1" is always shorthand for "q = 1 with respect to O." Information is the central notion — in the bare Shannon sense of correlation — and the theory is *complete* (Hypothesis 2): there is nothing below the relational information systems hold about each other.

The reconstruction (§III) then tries to derive the Hilbert-space formalism from three postulates: (1) **limited information** — a finite N-bit cap on the relevant information extractable from a system; (2) **unlimited information** — you can always acquire new information (so the sequence of answers can't be deterministic); (3) a **superposition/composition** postulate fixing how the unitary change-of-basis matrices compose. He's candid that the third postulate is ad hoc and the whole thing isn't rigorous — it's "better grasping the physics," not a formalisation.

**On Planck's constant** (the part you're after — §III.B, around Postulate 1)

This is where the action quantum drops out, and it's a dimensional/structural argument rather than a calculation. The chain is:

Postulate 1 says any system has a finite information capacity N — maximal knowledge of S is a finite N-bit string, with N ≈ log₂(dim ℋ). Now apply this to a classical continuous degree of freedom, say a particle's position. Classically you can localise the state in phase space to arbitrary precision, so the information is unbounded. Postulate 1 forbids that: maximal information can only localise the state within a *finite region* of phase space — there's an elementary cell below which "more bits" is meaningless.

Then the dimensional move. The phase space of any system has dimensions of (position × momentum)ⁿ, i.e. (L²T⁻¹M)ⁿ — each conjugate pair carries the dimension of *action*. If the elementary phase-space cell has finite, universal size, there must exist a universal constant with dimension L²T⁻¹M that sets that size. That constant is ℏ. Rovelli's punchline is that **Planck's constant is just the conversion factor between physical phase-space units (position × momentum) and information-theoretic units (bits)** — it's what you need to translate "one elementary cell" into "one bit." Finite information capacity is the physical content; ℏ is the bookkeeping coefficient that follows from it once you write it in conventional units.

So he doesn't *derive a value* for ℏ — nothing in the postulates fixes the number. What he derives is that a constant of the dimension of action, fixing a minimal phase-space resolution, *must exist* the moment you impose finite information capacity on a continuous classical system. The quantisation of action is reframed as the discreteness of information.

Worth flagging for your purposes: this is exactly the spot where Rovelli's reconstruction is at its most heuristic. The "must exist a universal constant" step assumes the cell size is the *same* across all systems and degrees of freedom — universality is asserted, not derived — and the identification N ≈ log₂(dim ℋ) is doing quiet work in tying the finite bit-count to phase-space volume. The argument is suggestive about *why* there is an ℏ, not about its magnitude or its universality.

This is plainly adjacent to your information-theoretic foundations and the Landauer/Paper 3 material — if you want, I can lay the ℏ-from-finite-capacity argument next to the way your framework relocates the non-computable residuum, since both are doing a "what must exist once you take discreteness seriously" move.

*(thinking)*

 The user has uploaded Rovelli's 1996 "Relational Quantum Mechanics" paper and wants me to summarize it, focusing on how he derives the action quantum—Planck's constant ℏ. I can see the paper in context. In section III.B, Rovelli discusses Postulate 1 about limited information and notes that it already introduces Planck's constant into classical physics, and I'm looking at where he derives ℏ from the relational framework.

This connects to information-theoretic foundations and relationalist approaches, which are relevant to the broader research context, but I should keep the focus tight on what the user asked for. I'll give a substantive summary in plain prose, emphasizing the ℏ derivation since that's the explicit interest. The key argument appears around pages 11-12: Postulate 1 establishes that there's a maximum amount of relevant information extractable from any system, and any prediction can be inferred from a finite string rather than an infinite one.

The dimensional argument for ℏ is the core move here. Classical continuous variables like position can be localized with arbitrary precision in phase space, which would require infinite information. But if information capacity is finite, then the state can only be localized within a finite region of phase space. Since conjugate pairs (position × momentum) have dimensions of action, there must be a universal constant with those same dimensions that sets the minimal localizability—the size of the elementary phase-space cell. That constant is Planck's constant, which essentially converts between physical phase-space units and information-theoretic units measured in bits.

I should be clear that this is a heuristic dimensional argument rather than a rigorous derivation, and Rovelli himself is modest about the rigor of the whole reconstruction. I'll structure the response with a brief overview of the paper's thesis and postulates, then focus on the ℏ derivation since that's what matters most. Given the audience is a physicist working on related foundations, I can stay technical and keep it mostly in prose rather than breaking it into bullet points.

Rovelli's 1996 paper proposes that the measurement problem is an artefact of a bad concept — the *observer-independent state*. His analogy is Einstein on the Lorentz transformations: the formalism was already there; what was missing was recognising that an implicit assumption (absolute simultaneity, in that case) was untenable. Here the offending assumption is that a system has a state, or that physical quantities have values, independently of some other system relative to which they are defined.

The argument runs from a single observation: take a measurement of S by O, then describe the *same* events from a third system P who treats S–O as one quantum system. For O the variable q has value 1 at t₂; for P the S–O pair is in an entangled superposition and q has no determined value. Both descriptions are correct quantum mechanics (P's is just Schrödinger evolution applied to S+O). Rovelli refuses to privilege either, and works through eight objections to show you can't escape this without either breaking linearity or smuggling in a special class of "classical" systems. His resolution: state and value are *relational*, like velocity in Galilean mechanics. "q = 1" is always shorthand for "q = 1 with respect to O." Information is the central notion — in the bare Shannon sense of correlation — and the theory is *complete* (Hypothesis 2): there is nothing below the relational information systems hold about each other.

The reconstruction (§III) then tries to derive the Hilbert-space formalism from three postulates: (1) **limited information** — a finite N-bit cap on the relevant information extractable from a system; (2) **unlimited information** — you can always acquire new information (so the sequence of answers can't be deterministic); (3) a **superposition/composition** postulate fixing how the unitary change-of-basis matrices compose. He's candid that the third postulate is ad hoc and the whole thing isn't rigorous — it's "better grasping the physics," not a formalisation.

**On Planck's constant** (the part you're after — §III.B, around Postulate 1)

This is where the action quantum drops out, and it's a dimensional/structural argument rather than a calculation. The chain is:

Postulate 1 says any system has a finite information capacity N — maximal knowledge of S is a finite N-bit string, with N ≈ log₂(dim ℋ). Now apply this to a classical continuous degree of freedom, say a particle's position. Classically you can localise the state in phase space to arbitrary precision, so the information is unbounded. Postulate 1 forbids that: maximal information can only localise the state within a *finite region* of phase space — there's an elementary cell below which "more bits" is meaningless.

Then the dimensional move. The phase space of any system has dimensions of (position × momentum)ⁿ, i.e. (L²T⁻¹M)ⁿ — each conjugate pair carries the dimension of *action*. If the elementary phase-space cell has finite, universal size, there must exist a universal constant with dimension L²T⁻¹M that sets that size. That constant is ℏ. Rovelli's punchline is that **Planck's constant is just the conversion factor between physical phase-space units (position × momentum) and information-theoretic units (bits)** — it's what you need to translate "one elementary cell" into "one bit." Finite information capacity is the physical content; ℏ is the bookkeeping coefficient that follows from it once you write it in conventional units.

So he doesn't *derive a value* for ℏ — nothing in the postulates fixes the number. What he derives is that a constant of the dimension of action, fixing a minimal phase-space resolution, *must exist* the moment you impose finite information capacity on a continuous classical system. The quantisation of action is reframed as the discreteness of information.

Worth flagging for your purposes: this is exactly the spot where Rovelli's reconstruction is at its most heuristic. The "must exist a universal constant" step assumes the cell size is the *same* across all systems and degrees of freedom — universality is asserted, not derived — and the identification N ≈ log₂(dim ℋ) is doing quiet work in tying the finite bit-count to phase-space volume. The argument is suggestive about *why* there is an ℏ, not about its magnitude or its universality.

This is plainly adjacent to your information-theoretic foundations and the Landauer/Paper 3 material — if you want, I can lay the ℏ-from-finite-capacity argument next to the way your framework relocates the non-computable residuum, since both are doing a "what must exist once you take discreteness seriously" move.

### 3. human  ·  2026-06-06 09:48:04

I'm thinking about it in terms of Popper's argument and our point that the self-knowledge of the predictor becomes important at the scale of the most minute component of the predictor, in the case the prediction machine is a Babbage analytical engine that would be at the scale of the smallest lever or cog. Since the time evolution of the entire engine is in some phase space then the smallest change that would alter the path taken in that phase space would have to have the dimension of action. Rovelli reaches the same conclusion from a slightly different direction, he postulates the existence of a finite information capacity ad-hoc

I'm thinking about it in terms of Popper's argument and our point that the self-knowledge of the predictor becomes important at the scale of the most minute component of the predictor, in the case the prediction machine is a Babbage analytical engine that would be at the scale of the smallest lever or cog. Since the time evolution of the entire engine is in some phase space then the smallest change that would alter the path taken in that phase space would have to have the dimension of action. Rovelli reaches the same conclusion from a slightly different direction, he postulates the existence of a finite information capacity ad-hoc

### 4. assistant  ·  2026-06-06 09:50:21

 I'm connecting Rovelli's derivation of ℏ to Popper's indeterminism argument and thinking through how this relates to the framework's point about predictor self-knowledge. I should reference the Popper papers from the project files and work through how the self-reference spine applies here.

John's argument traces from Popper's insight that a predictor can't fully predict itself, to the concrete claim that for a system like a Babbage engine, the relevant scale of self-knowledge is the smallest mechanical component. The trajectory through phase space would require a minimal action scale to distinguish different paths — which is exactly what Rovelli derives, but John's framework would generate this from first principles rather than postulating it. The advantage is that finite information capacity emerges from the self-reference constraint rather than being assumed.

But I need to scrutinize the dimensional argument carefully. The claim is that the smallest distinguishable perturbation to a trajectory has dimension of action, and that's where the reasoning gets subtle. The symplectic structure of phase space does give area elements dimension of action, but that's only if you're measuring perturbations as phase-space areas rather than as displacements in position or momentum alone. The question is whether that's the *right* measure of what counts as a "distinguishable" change to the trajectory, or if that's doing hidden work.

The predictor self-knowledge angle suggests the answer: if the predictor must represent its own state to predict itself, and that representation is a physical process, then measuring the state requires resolving a phase-space cell rather than a single coordinate, because any measurement of position disturbs momentum and vice versa. So the minimal distinguishable state is fundamentally a cell, not a point. That's where the action quantum emerges naturally from the predictor's own limitations. The key insight is that Popper's self-reference obstruction—the classical argument that a predictor embedded in its own system cannot fully predict itself—maps onto the Lawvere-Yanofsky framework, which then forces a finite floor on the predictor's self-model. Rather than assuming finiteness as Rovelli does, John's version derives it from the diagonalization obstruction: the predictor cannot achieve complete self-prediction, and this impossibility is what necessitates the quantized, finite resolution rather than arbitrary refinement.

But here's the tension: the self-reference obstruction gives you *incompleteness*—some information is always missing—but that's qualitatively different from a *quantitative* floor of definite size. "Incomplete" could mean arbitrarily large but finite, or even infinite minus a bit. The jump from "the predictor can't have complete information about itself" to "therefore there exists a minimal cell of size ℏ" is where the argument gets thin.

And actually, I'm wondering whether the dimensional argument even needs self-reference at all. The observation that the smallest phase-space change must have action dimension might just be dimensional analysis—the symplectic form inherently has action dimension, which is almost tautological in Hamiltonian mechanics. The real physics is in explaining *why* we're talking about area rather than length, and *why* there's a finite floor at all. Self-reference addresses the second question; the measurement-disturbance structure addresses the first.

So the honest picture is that John's framing is genuinely appealing and does improve on Rovelli by motivating the capacity bound rather than just asserting it. But the dimensional step is conflating two separate things: the action dimension comes automatically from symplectic geometry once you're talking about phase-space cells instead of coordinate displacements, while the *finiteness* of that cell is what self-reference must supply—and Lawvere-style obstruction gives incompleteness but not obviously a positive lower bound or its magnitude. This mirrors the gap I identified in Rovelli: universality and the bit-to-cell identification are just assumed.

There's also a subtlety with the Babbage engine analogy. A classical digital machine has a state space that's effectively discrete by design—gear positions are engineered to be discrete states—so its phase space is already coarse-grained. But even the smallest cog has continuous mechanical degrees of freedom underneath, since it's made of atoms with thermal motion.  The relevant "smallest change that flips a computational outcome" is what pushes a lever past a decision threshold, which is a classical bifurcation. What sets the resolution at which the machine's self-model of its own lever position stays reliable is the real question, and there's a nice connection to Landauer cost—distinguishing two lever states reliably against thermal noise.

This is where the thermodynamic angle becomes crucial. The framework has Landauer as one of the four FANOUT derivations, and the "smallest change that alters the path" in a classical computing engine against a thermal bath is bounded below not by ℏ directly but by kT ln2 for a reliable irreversible step. The relation between the kT ln2 floor and the ℏ floor is itself interesting—they're different ceilings. Rovelli says ℏ is the bit-to-action converter, while Landauer is the bit-to-energy-at-temperature converter. Applied to a physical thermal Babbage engine, the predictor self-knowledge argument might more naturally land on Landauer unless you push to the zero-temperature isolated limit.

This is worth raising because it's exactly the kind of critical engagement John values and connects directly to his work on Landauer and FANOUT. The distinction maps cleanly: Rovelli's ℏ-cell is the reversible, pre-FANOUT phase-space resolution, while the Landauer floor is the post-FANOUT irreversible-copy cost. John's framework already locates the FANOUT boundary precisely there, so the self-reference argument might give both floors at the two sides of that boundary—ℏ on the unitary side, kT ln2 on the classical-record side. That would be a genuinely framework-native insight rather than just commentary on Rovelli.

On Popper specifically, his 1950 argument is about whether a predictor inside the system can predict itself. He's making a point about amplification: classical systems can amplify microscopic indeterminacy to macroscopic scale, so even classical determinism at the micro level doesn't guarantee predictability. The self-prediction argument hinges on the impossibility of a predictor predicting itself in time to use that prediction—the Oedipus effect. Popper was arguing that classical physics is also not deterministic in the predictability sense, partly to counter the idea that QM is uniquely indeterministic. There's a known critique that his self-prediction argument establishes only epistemic unpredictability, not ontological indeterminism, which maps onto the framework's distinction between epistemological necessity and the SR/GR ontological-epistemological split. John's framework seems to be exploring how this plays out.

I don't think I need to search anything here—this is conceptual physics grounded in the paper and John's framework, both of which I have access to. I could review the Popper PDFs to be precise about his exact wording, but I have enough from general knowledge to engage meaningfully, and John clearly knows Popper well since it's central to his framework. The question is whether re-reading would materially help or if I can work at the level he's pitched without that.

Actually, since this is a conversational back-and-forth about ideas rather than a formal document task, I'll engage directly and offer to pull the exact Popper formulation if he wants to nail down the wording for the paper. No need to over-tool a thinking conversation.

On whether John's right that this is "the same conclusion from a slightly different direction"—partly true. Both Rovelli and John arrive at discreteness and finiteness of information plus symplectic structure equaling action quantization, but John's distinctive move is *deriving* that finiteness from self-reference and Popper rather than postulating it. That's the framework's whole point: relocating non-computability and forcing finiteness through logical constraint rather than assumption.

The honest critical move is to separate two sub-claims: the action *dimension* (which comes fairly cleanly from symplectic geometry and the requirement that minimal changes resolve conjugate pairs, not just coordinates) versus action *finiteness* (the positive floor), where self-reference actually does the work. The first leans on machinery the framework provides elsewhere—division algebras, complex amplitudes, the noncommutativity already built in upstream.

For the second, self-reference via Lawvere gives incompleteness (some irreducible missing information), but that's not the same as a quantitative finite floor of definite magnitude. Incompleteness says "at least one undecidable bit," not "at most N total bits." So self-reference arguably pins down the *floor*—you can't resolve below the minimal cell where self-registration becomes self-referential—but doesn't obviously give you the *ceiling* (finite N). That's where Rovelli's postulate comes in. The key insight: deriving ℏ only needs the floor (minimal cell size), not the ceiling (finite dimensionality). These might be separate postulates targeting different constraints.

For the action quantum specifically, the self-reference route is actually better-aimed than Rovelli's. Rovelli postulates finite *capacity* (a ceiling-type statement) and works down to a minimal cell, whereas the self-reference argument goes directly at the floor: at the scale of the smallest component, the predictor's attempt to register that component's own state hits the diagonal obstruction, guaranteeing an irreducible cell-sized floor on resolution. That's a cleaner path to ℏ than postulating capacity first.

The honest residual is the *magnitude* and *universality*—neither route fixes the number or explains why the same cell applies everywhere. But this is actually correct given the dimensional-parameter accounting: ℏ is dimensionful, and dimensionful constants can't be derived dimensionlessly. The framework claims zero free dimensionless parameters with dimensional parameters left as irreducible inputs. So deriving the *existence and dimension* of an action quantum while leaving its *value* as one of the dimensional inputs is exactly the right shape—internally consistent, not a shortfall.The convergence is real and your framing is right: Rovelli needs finite information capacity as a bare postulate, and the self-reference route is exactly the kind of thing that could turn that postulate into a consequence. But it's worth separating two claims the Babbage picture runs together, because they're carried by different machinery — one is genuinely yours, the other is borrowed.

The first is the *dimension*. "The smallest change that alters the phase-space path has the dimension of action" is true, but only if the relevant change is a phase-space *cell* — an area in a conjugate (q,p) plane — rather than a displacement along a coordinate. A perturbation purely in lever-position has dimension of length; purely in momentum, of momentum; only the symplectic form dp∧dq, equivalently the Liouville cell, carries action. So the action dimension is essentially free from Hamiltonian geometry — *provided* the minimal distinguishable perturbation is a cell and not a coordinate displacement. That proviso is where conjugacy has to already be in play, which is upstream spine machinery (complex amplitudes, the division-algebra tower), not something Popper supplies on his own. The step leans on the rest of the chain, and it's cleaner to say so than to let the dimensional analysis look self-contained.

The second is the *floor* — that the cell has nonzero minimum size. This is the part self-reference actually buys, and it's better targeted than Rovelli's postulate. Note the asymmetry. Rovelli postulates finite *capacity*, a ceiling statement (≤ N bits), then works down to a minimal cell. But to get ℏ you don't need the ceiling at all; you only need the floor. The Popper/Lawvere obstruction goes straight at the floor: at the scale of the smallest cog, the predictor's attempt to register that component's own state is exactly where self-registration becomes self-reference, and the diagonal obstruction forces at least one irreducibly undecidable bit about its own state there. That's a floor on self-resolution, sited precisely where you want it. For the action quantum specifically your route is arguably the more honest one, because his postulate is aimed at the wrong end.

What neither route fixes — and shouldn't — is the magnitude and the universality (same cell across all systems and degrees of freedom). Rovelli just asserts universality. Here's the consistency check that turns the gap into a feature: ℏ is dimensionful, and a dimensional constant can't fall out of a dimensionless argument. That lines up exactly with your parameter accounting — zero free *dimensionless* parameters, with the dimensional ones left as irreducible inputs. An argument that derives the *existence and dimension* of an action quantum while leaving its *value* as one of the two-or-three dimensional inputs is precisely the right shape. If the framework *could* produce the number, that would be a problem for the parameter story, not a triumph. "There must be an ℏ, of action dimension, but its size is an input" is the internally correct outcome.

One extension that may be more than commentary. A real Babbage engine sits in a thermal bath, and the smallest change that reliably flips a computational outcome — pushes a lever past its decision threshold against noise — is bounded below by kT ln2, not by ℏ. That's a different floor: bit↔energy-at-temperature, where Rovelli's is bit↔action. These are the two sides of your FANOUT boundary. The ℏ-cell is the reversible, pre-FANOUT phase-space resolution; the kT ln2 cost is the post-FANOUT irreversible record. The predictor self-knowledge argument applied to a *physical* engine plausibly yields both floors — ℏ on the unitary side, kT ln2 on the classical-record side — with the FANOUT boundary already sitting between them in your corpus. That would be a framework-native reading of Rovelli's "ℏ is the bit↔action converter," not just an importation of it.

Want me to pull the exact Popper construction from the Part I/II PDFs? The floor argument will carry more weight in Paper 1 if it's pinned to his actual amplification/self-prediction setup rather than the general gloss.

*(thinking)*

 I'm connecting Rovelli's derivation of ℏ to Popper's indeterminism argument and thinking through how this relates to the framework's point about predictor self-knowledge. I should reference the Popper papers from the project files and work through how the self-reference spine applies here.

John's argument traces from Popper's insight that a predictor can't fully predict itself, to the concrete claim that for a system like a Babbage engine, the relevant scale of self-knowledge is the smallest mechanical component. The trajectory through phase space would require a minimal action scale to distinguish different paths — which is exactly what Rovelli derives, but John's framework would generate this from first principles rather than postulating it. The advantage is that finite information capacity emerges from the self-reference constraint rather than being assumed.

But I need to scrutinize the dimensional argument carefully. The claim is that the smallest distinguishable perturbation to a trajectory has dimension of action, and that's where the reasoning gets subtle. The symplectic structure of phase space does give area elements dimension of action, but that's only if you're measuring perturbations as phase-space areas rather than as displacements in position or momentum alone. The question is whether that's the *right* measure of what counts as a "distinguishable" change to the trajectory, or if that's doing hidden work.

The predictor self-knowledge angle suggests the answer: if the predictor must represent its own state to predict itself, and that representation is a physical process, then measuring the state requires resolving a phase-space cell rather than a single coordinate, because any measurement of position disturbs momentum and vice versa. So the minimal distinguishable state is fundamentally a cell, not a point. That's where the action quantum emerges naturally from the predictor's own limitations. The key insight is that Popper's self-reference obstruction—the classical argument that a predictor embedded in its own system cannot fully predict itself—maps onto the Lawvere-Yanofsky framework, which then forces a finite floor on the predictor's self-model. Rather than assuming finiteness as Rovelli does, John's version derives it from the diagonalization obstruction: the predictor cannot achieve complete self-prediction, and this impossibility is what necessitates the quantized, finite resolution rather than arbitrary refinement.

But here's the tension: the self-reference obstruction gives you *incompleteness*—some information is always missing—but that's qualitatively different from a *quantitative* floor of definite size. "Incomplete" could mean arbitrarily large but finite, or even infinite minus a bit. The jump from "the predictor can't have complete information about itself" to "therefore there exists a minimal cell of size ℏ" is where the argument gets thin.

And actually, I'm wondering whether the dimensional argument even needs self-reference at all. The observation that the smallest phase-space change must have action dimension might just be dimensional analysis—the symplectic form inherently has action dimension, which is almost tautological in Hamiltonian mechanics. The real physics is in explaining *why* we're talking about area rather than length, and *why* there's a finite floor at all. Self-reference addresses the second question; the measurement-disturbance structure addresses the first.

So the honest picture is that John's framing is genuinely appealing and does improve on Rovelli by motivating the capacity bound rather than just asserting it. But the dimensional step is conflating two separate things: the action dimension comes automatically from symplectic geometry once you're talking about phase-space cells instead of coordinate displacements, while the *finiteness* of that cell is what self-reference must supply—and Lawvere-style obstruction gives incompleteness but not obviously a positive lower bound or its magnitude. This mirrors the gap I identified in Rovelli: universality and the bit-to-cell identification are just assumed.

There's also a subtlety with the Babbage engine analogy. A classical digital machine has a state space that's effectively discrete by design—gear positions are engineered to be discrete states—so its phase space is already coarse-grained. But even the smallest cog has continuous mechanical degrees of freedom underneath, since it's made of atoms with thermal motion.  The relevant "smallest change that flips a computational outcome" is what pushes a lever past a decision threshold, which is a classical bifurcation. What sets the resolution at which the machine's self-model of its own lever position stays reliable is the real question, and there's a nice connection to Landauer cost—distinguishing two lever states reliably against thermal noise.

This is where the thermodynamic angle becomes crucial. The framework has Landauer as one of the four FANOUT derivations, and the "smallest change that alters the path" in a classical computing engine against a thermal bath is bounded below not by ℏ directly but by kT ln2 for a reliable irreversible step. The relation between the kT ln2 floor and the ℏ floor is itself interesting—they're different ceilings. Rovelli says ℏ is the bit-to-action converter, while Landauer is the bit-to-energy-at-temperature converter. Applied to a physical thermal Babbage engine, the predictor self-knowledge argument might more naturally land on Landauer unless you push to the zero-temperature isolated limit.

This is worth raising because it's exactly the kind of critical engagement John values and connects directly to his work on Landauer and FANOUT. The distinction maps cleanly: Rovelli's ℏ-cell is the reversible, pre-FANOUT phase-space resolution, while the Landauer floor is the post-FANOUT irreversible-copy cost. John's framework already locates the FANOUT boundary precisely there, so the self-reference argument might give both floors at the two sides of that boundary—ℏ on the unitary side, kT ln2 on the classical-record side. That would be a genuinely framework-native insight rather than just commentary on Rovelli.

On Popper specifically, his 1950 argument is about whether a predictor inside the system can predict itself. He's making a point about amplification: classical systems can amplify microscopic indeterminacy to macroscopic scale, so even classical determinism at the micro level doesn't guarantee predictability. The self-prediction argument hinges on the impossibility of a predictor predicting itself in time to use that prediction—the Oedipus effect. Popper was arguing that classical physics is also not deterministic in the predictability sense, partly to counter the idea that QM is uniquely indeterministic. There's a known critique that his self-prediction argument establishes only epistemic unpredictability, not ontological indeterminism, which maps onto the framework's distinction between epistemological necessity and the SR/GR ontological-epistemological split. John's framework seems to be exploring how this plays out.

I don't think I need to search anything here—this is conceptual physics grounded in the paper and John's framework, both of which I have access to. I could review the Popper PDFs to be precise about his exact wording, but I have enough from general knowledge to engage meaningfully, and John clearly knows Popper well since it's central to his framework. The question is whether re-reading would materially help or if I can work at the level he's pitched without that.

Actually, since this is a conversational back-and-forth about ideas rather than a formal document task, I'll engage directly and offer to pull the exact Popper formulation if he wants to nail down the wording for the paper. No need to over-tool a thinking conversation.

On whether John's right that this is "the same conclusion from a slightly different direction"—partly true. Both Rovelli and John arrive at discreteness and finiteness of information plus symplectic structure equaling action quantization, but John's distinctive move is *deriving* that finiteness from self-reference and Popper rather than postulating it. That's the framework's whole point: relocating non-computability and forcing finiteness through logical constraint rather than assumption.

The honest critical move is to separate two sub-claims: the action *dimension* (which comes fairly cleanly from symplectic geometry and the requirement that minimal changes resolve conjugate pairs, not just coordinates) versus action *finiteness* (the positive floor), where self-reference actually does the work. The first leans on machinery the framework provides elsewhere—division algebras, complex amplitudes, the noncommutativity already built in upstream.

For the second, self-reference via Lawvere gives incompleteness (some irreducible missing information), but that's not the same as a quantitative finite floor of definite magnitude. Incompleteness says "at least one undecidable bit," not "at most N total bits." So self-reference arguably pins down the *floor*—you can't resolve below the minimal cell where self-registration becomes self-referential—but doesn't obviously give you the *ceiling* (finite N). That's where Rovelli's postulate comes in. The key insight: deriving ℏ only needs the floor (minimal cell size), not the ceiling (finite dimensionality). These might be separate postulates targeting different constraints.

For the action quantum specifically, the self-reference route is actually better-aimed than Rovelli's. Rovelli postulates finite *capacity* (a ceiling-type statement) and works down to a minimal cell, whereas the self-reference argument goes directly at the floor: at the scale of the smallest component, the predictor's attempt to register that component's own state hits the diagonal obstruction, guaranteeing an irreducible cell-sized floor on resolution. That's a cleaner path to ℏ than postulating capacity first.

The honest residual is the *magnitude* and *universality*—neither route fixes the number or explains why the same cell applies everywhere. But this is actually correct given the dimensional-parameter accounting: ℏ is dimensionful, and dimensionful constants can't be derived dimensionlessly. The framework claims zero free dimensionless parameters with dimensional parameters left as irreducible inputs. So deriving the *existence and dimension* of an action quantum while leaving its *value* as one of the dimensional inputs is exactly the right shape—internally consistent, not a shortfall.

The convergence is real and your framing is right: Rovelli needs finite information capacity as a bare postulate, and the self-reference route is exactly the kind of thing that could turn that postulate into a consequence. But it's worth separating two claims the Babbage picture runs together, because they're carried by different machinery — one is genuinely yours, the other is borrowed.

The first is the *dimension*. "The smallest change that alters the phase-space path has the dimension of action" is true, but only if the relevant change is a phase-space *cell* — an area in a conjugate (q,p) plane — rather than a displacement along a coordinate. A perturbation purely in lever-position has dimension of length; purely in momentum, of momentum; only the symplectic form dp∧dq, equivalently the Liouville cell, carries action. So the action dimension is essentially free from Hamiltonian geometry — *provided* the minimal distinguishable perturbation is a cell and not a coordinate displacement. That proviso is where conjugacy has to already be in play, which is upstream spine machinery (complex amplitudes, the division-algebra tower), not something Popper supplies on his own. The step leans on the rest of the chain, and it's cleaner to say so than to let the dimensional analysis look self-contained.

The second is the *floor* — that the cell has nonzero minimum size. This is the part self-reference actually buys, and it's better targeted than Rovelli's postulate. Note the asymmetry. Rovelli postulates finite *capacity*, a ceiling statement (≤ N bits), then works down to a minimal cell. But to get ℏ you don't need the ceiling at all; you only need the floor. The Popper/Lawvere obstruction goes straight at the floor: at the scale of the smallest cog, the predictor's attempt to register that component's own state is exactly where self-registration becomes self-reference, and the diagonal obstruction forces at least one irreducibly undecidable bit about its own state there. That's a floor on self-resolution, sited precisely where you want it. For the action quantum specifically your route is arguably the more honest one, because his postulate is aimed at the wrong end.

What neither route fixes — and shouldn't — is the magnitude and the universality (same cell across all systems and degrees of freedom). Rovelli just asserts universality. Here's the consistency check that turns the gap into a feature: ℏ is dimensionful, and a dimensional constant can't fall out of a dimensionless argument. That lines up exactly with your parameter accounting — zero free *dimensionless* parameters, with the dimensional ones left as irreducible inputs. An argument that derives the *existence and dimension* of an action quantum while leaving its *value* as one of the two-or-three dimensional inputs is precisely the right shape. If the framework *could* produce the number, that would be a problem for the parameter story, not a triumph. "There must be an ℏ, of action dimension, but its size is an input" is the internally correct outcome.

One extension that may be more than commentary. A real Babbage engine sits in a thermal bath, and the smallest change that reliably flips a computational outcome — pushes a lever past its decision threshold against noise — is bounded below by kT ln2, not by ℏ. That's a different floor: bit↔energy-at-temperature, where Rovelli's is bit↔action. These are the two sides of your FANOUT boundary. The ℏ-cell is the reversible, pre-FANOUT phase-space resolution; the kT ln2 cost is the post-FANOUT irreversible record. The predictor self-knowledge argument applied to a *physical* engine plausibly yields both floors — ℏ on the unitary side, kT ln2 on the classical-record side — with the FANOUT boundary already sitting between them in your corpus. That would be a framework-native reading of Rovelli's "ℏ is the bit↔action converter," not just an importation of it.

Want me to pull the exact Popper construction from the Part I/II PDFs? The floor argument will carry more weight in Paper 1 if it's pinned to his actual amplification/self-prediction setup rather than the general gloss.

### 5. human  ·  2026-06-06 09:58:11

Yes, pull the exact Popper construction from the part 1 and 2 pdfs. I'm writing those paragraphs now so the relationship to Rovelli's RQM is useful

Yes, pull the exact Popper construction from the part 1 and 2 pdfs. I'm writing those paragraphs now so the relationship to Rovelli's RQM is useful

### 6. assistant  ·  2026-06-06 10:04:43


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

These are ZIP archives of JPEG page scans, not real PDFs. Let me extract and OCR them.
```
This block is not supported on your current device yet.
```

There are already `.txt` files — likely OCR text. Let me check them.
```
This block is not supported on your current device yet.
```

The `.txt` files only contain the JSTOR cover metadata, not the article body. The actual content is in the JPEG scans. I need to OCR them.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

18 pages, scans ~868×1400. The resolution is modest; let me upscale before OCR for better accuracy, and process all pages.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The OCR has captured the body text. Let me read the key sections in full — the "interference from within" / self-prediction argument (pages 13-18) is the core construction.
```
This block is not supported on your current device yet.
```

This is exactly the apparatus. Now the heart of it — "interference from within" and the self-prediction impossibility (pages 13-18).
```
This block is not supported on your current device yet.
```

This is the core. Note page 13 already states Popper's own ℏ-connection explicitly. Now the self-prediction impossibility section 8 (pages 16-18) and the explicit "minute differences" / amplification scaling.
```
This block is not supported on your current device yet.
```

I now have the full Part I argument. Let me grab the section 8 self-prediction theorem precisely (it was referenced as "next section 8" — let me verify which page it actually lands on) and then check Part II for the action-quantum material, since that's where your specific interest lies.
```
This block is not supported on your current device yet.
```

Section 8 is referenced but its body falls in Part II (Part I ends mid-argument at section 7, page 133). The self-prediction theorem proper is in Part II. Let me extract and OCR Part II, focusing on the action-quantum and self-prediction sections.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Part II is the deep one for your purposes — it contains the Tristram Shandy paradox, an explicit invocation of Gödel's 1931 theorem (page 9-12), and the self-prediction impossibility. This is directly the Lawvere/Gödel spine of your framework. Let me read the Gödelian core (pages 8-13) and the self-prediction setup (pages 4-8, 18-20).
```
This block is not supported on your current device yet.
```

This is the full Gödelian self-prediction construction. Now the action-quantum material that appears in pages 4, 5, 18-21, and the "minute differences amplified" scaling.
```
This block is not supported on your current device yet.
```

Now the final scaling/action-quantum-relevant pages (18-21), where Popper connects amplification, "minute differences," and the explicit comparison to the quantum of action.
```
This block is not supported on your current device yet.
```

I now have the entire argument across both parts. Let me write up the precise construction for your paragraphs, in informal arXiv prose, marking what's exact Popper versus your reading. I'll keep it tightly tied to where each step lives in the text.

---

Here is the Popper construction, pulled exactly, in the order you'll want it for the Rovelli comparison. Part I is the *physical* (interference/amplification) argument; Part II is the *logical* (Gödelian self-prediction) argument. They are two routes to the same impossibility, which is structurally your situation exactly — the bump under the carpet moved between a thermodynamic and a self-referential location.

**The setup (Part I, §3, p. 123).** Popper "embodies Laplace's disembodied spirit" — the demon becomes a *predictor*, "a physical predicting machine… a classical mechanism, subject to the laws of mechanics," explicitly a Babbage-style device that takes punched-tape input, computes, and emits a punched-tape prediction. Crucially the predictor is *inside* the world it predicts. He restricts to a "specified finite prediction task": predict some event to a chosen finite precision, in a system sufficiently isolated, at a chosen future instant. Finite determinism is then the claim that for any such task a predictor can be built.

**The amplifier lemma (Part I, §7, p. 129) — this is the part carrying your dimensional point.** For B to predict A, either B calculates its own interference with A (which regresses — studying A+B′ "the whole problem arises again") or B disturbs A negligibly. Take the second. Then a one-way membrane appears: A→B influence must be strong, B→A weak. Popper's reason is exactly the sensitivity argument you're using: "some minute differences at the instant t₁ may, in a mechanical system such as A, give rise to considerable differences at t₂; but since B is a predictor… it must be able to react in very different ways to the two minutely different states of A." Therefore **"a predictor B must be an amplifier."** A footnote sharpens it: predictors must be amplifiers "merely as recorders of measurements; for they must be capable of recording minute differences by the same method (the punching of holes) as large ones." That footnote is the cleanest seed of your point — the *recording* step, the FANOUT, is where a minute phase-space difference must be lifted to a macroscopically distinct, persistent mark.

**The breakdown (Part I, §7, pp. 129–130).** When two predictors B and C each try to predict the other, each amplifies the other's weak disturbances; the one-way membrane fails both ways; neither can predict the other. Popper roots this explicitly in self-knowledge: the failure "depends on the fact… that neither of the machines can have knowledge of its own state before that state has passed; in fact, it can obtain information about its own state only by way of studying the results obtained by another machine." This is your relational point arriving from the predictor side — a system's own state is not available to it except via another system, which is close to Rovelli's "no meaning in being correlated with oneself."

**Popper's own ℏ remark (Part I, §6, p. 128).** He states the action-quantum connection himself, and this is the sentence to quote against Rovelli: in quantum physics the indeterminacy of interference vanishes "if we assume that h = 0… the absence of a quantum of action is the distinguishing characteristic of classical physics." His whole Part I thesis is then that *classical* mechanics suffers an *analogous* indeterminacy "from interference from within" even with h = 0 — i.e. the predictor obstruction does not need ℏ to bite. Note what this means for your reading: Popper does **not** derive ℏ from self-prediction. He derives a *structurally parallel* obstruction that survives at ℏ = 0. The action quantum is what the obstruction *would* localise to in a quantum world, but in his classical treatment the floor is set by mechanical robustness, not by ℏ.

**The robustness floor (Part II, p. 192; Part I, p. 132).** The minimum-cell idea you want is present but it's mechanical, not action-dimensioned. Part I p. 132: in a continuum mechanics "there must be a lower limit to [the tentacles'] thickness or mass… otherwise they would become too easily distorted… no D can be at the same time effective and vanishingly small." Part II p. 192 gives the temporal version: every machine has a "specious present" Δtₖ, "the minimum time it takes C to 'know' what has happened to it," bounded below because "for every actual physical machine there is a maximum running speed, and consequently a minimum length of time necessary for completing even the shortest description." So Popper has *both* a minimum spatial scale of the recording apparatus and a minimum time per recorded bit — the two factors whose product is action — but he never multiplies them, and he never claims universality across systems. That last step is yours (and is exactly the step Rovelli skips by fiat).

**The Gödelian core (Part II §III, pp. 179–183) — the spine match.** This is where Popper is doing your Lawvere–Yanofsky move in 1950. He invokes Gödel 1931 by name (p. 179, with Rosser, Tarski, Turing in the footnote) and uses the *second* theorem specifically: if g is undecidable in Sₙ, then the true statement h asserting g's undecidability is itself undecidable in Sₙ (p. 180). He then converts this from pure mathematics into a *physical* prediction question. A "near-Gödelian question" q₁ asks C: "if you are asked q₂ and given any amount of time, will you ultimately signal yes or no?" where q₂ is Gödelian relative to C's premise set J₂. Because C has cumulative memory (J₁ ⊆ J₂), and h is undecidable in every sub-system, C can only answer "I do not know yet" until t₂ has passed (pp. 182–183). The undecidability of a *mathematical* sentence is thereby transferred to a *physical* fact about the machine's future reaction — "a mathematical truism about all computers satisfying certain general conditions." This is precisely your self-reference → epistemic-limit-on-self-knowledge step, and Popper gets there by arithmetisation, the same Gödel-numbering diagonal that Lawvere later abstracts categorically.

**The self-information impossibility (Part II §III, pp. 189–191).** The decisive lemma: for C's self-information at t₁ to be correct and current, it "would have to contain, as one of its parts, a physical description of that very self-information, using physical symbols of the same kind as in the rest of its information. But this… is impossible for any finite piece of information; and an infinite piece cannot be completed at any instant." Feedback doesn't help ("a feed-back would inform C always after the event"); using information twice, or n times, only generates "an incessant stream of self-produced new information" so C "will never be able to begin predicting" (p. 190). Summary line, p. 191: "'Know thyself' is a contradictory ideal; we cannot fully know our limitations." This is the diagonal obstruction stated operationally — a system cannot host a complete current model of itself including the model.

---

**How to position it against Rovelli.** The clean framing for your paragraphs:

Rovelli postulates finite information capacity (Postulate 1) and reads ℏ off as the bit↔action conversion factor by dimensional analysis on phase space. He needs the *ceiling* (≤ N bits) as a primitive and asserts universality of the cell. Popper, fifty years earlier, gives two independent *derivations* of why a predictor cannot have complete current self-information — a physical one (the amplifier/one-way-membrane regress, Part I §7) and a logical one (the Gödelian self-prediction obstruction, Part II §III) — and these target the *floor* (the irreducible minimum self-resolution) rather than the ceiling. Your synthesis is that the floor is the load-bearing one for ℏ: the obstruction sites a minimum distinguishable self-perturbation at the scale of the predictor's smallest component, that perturbation must be a phase-space cell once conjugacy is in play (upstream spine), and a cell of nonzero area carries the dimension of action. Popper supplies the obstruction and even both factors (minimum apparatus scale, minimum time per bit) but stops short of forming the product or claiming universality; Rovelli supplies the universality and the ℏ identification but by postulate rather than derivation. The framework's contribution is the identification that joins them — Popper's Gödelian floor *is* the mechanism that Rovelli's Postulate 1 merely asserts.

One caution to keep the claim honest in the paper: Popper himself believed his classical argument works at ℏ = 0, so he is *not* claiming self-reference produces the action quantum. The honest statement is that Popper establishes the self-prediction obstruction is theory-independent (he conjectures it holds for "every system sufficiently complete to contain a theory which can analyse the functioning of the predictor," p. 133, and says quantum mechanics in particular is subject to it), and that *in a world with conjugate observables* that theory-independent obstruction localises to an action cell. The ℏ-from-self-reference reading is your bridge, with Popper supplying the obstruction and Rovelli supplying the dimensional reading — neither author makes the joint claim, which is precisely where the novel identification lives.

Want me to write a session-summary markdown of the Popper extraction (timestamped, with the page anchors above) so it's in the corpus for when you draft Paper 1, and a clean BibTeX entry for both parts?

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

These are ZIP archives of JPEG page scans, not real PDFs. Let me extract and OCR them.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

There are already `.txt` files — likely OCR text. Let me check them.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

The `.txt` files only contain the JSTOR cover metadata, not the article body. The actual content is in the JPEG scans. I need to OCR them.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

18 pages, scans ~868×1400. The resolution is modest; let me upscale before OCR for better accuracy, and process all pages.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

The OCR has captured the body text. Let me read the key sections in full — the "interference from within" / self-prediction argument (pages 13-18) is the core construction.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

This is exactly the apparatus. Now the heart of it — "interference from within" and the self-prediction impossibility (pages 13-18).

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

This is the core. Note page 13 already states Popper's own ℏ-connection explicitly. Now the self-prediction impossibility section 8 (pages 16-18) and the explicit "minute differences" / amplification scaling.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

I now have the full Part I argument. Let me grab the section 8 self-prediction theorem precisely (it was referenced as "next section 8" — let me verify which page it actually lands on) and then check Part II for the action-quantum material, since that's where your specific interest lies.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

Section 8 is referenced but its body falls in Part II (Part I ends mid-argument at section 7, page 133). The self-prediction theorem proper is in Part II. Let me extract and OCR Part II, focusing on the action-quantum and self-prediction sections.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

Part II is the deep one for your purposes — it contains the Tristram Shandy paradox, an explicit invocation of Gödel's 1931 theorem (page 9-12), and the self-prediction impossibility. This is directly the Lawvere/Gödel spine of your framework. Let me read the Gödelian core (pages 8-13) and the self-prediction setup (pages 4-8, 18-20).

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

This is the full Gödelian self-prediction construction. Now the action-quantum material that appears in pages 4, 5, 18-21, and the "minute differences amplified" scaling.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

Now the final scaling/action-quantum-relevant pages (18-21), where Popper connects amplification, "minute differences," and the explicit comparison to the quantum of action.

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

I now have the entire argument across both parts. Let me write up the precise construction for your paragraphs, in informal arXiv prose, marking what's exact Popper versus your reading. I'll keep it tightly tied to where each step lives in the text.

---

Here is the Popper construction, pulled exactly, in the order you'll want it for the Rovelli comparison. Part I is the *physical* (interference/amplification) argument; Part II is the *logical* (Gödelian self-prediction) argument. They are two routes to the same impossibility, which is structurally your situation exactly — the bump under the carpet moved between a thermodynamic and a self-referential location.

**The setup (Part I, §3, p. 123).** Popper "embodies Laplace's disembodied spirit" — the demon becomes a *predictor*, "a physical predicting machine… a classical mechanism, subject to the laws of mechanics," explicitly a Babbage-style device that takes punched-tape input, computes, and emits a punched-tape prediction. Crucially the predictor is *inside* the world it predicts. He restricts to a "specified finite prediction task": predict some event to a chosen finite precision, in a system sufficiently isolated, at a chosen future instant. Finite determinism is then the claim that for any such task a predictor can be built.

**The amplifier lemma (Part I, §7, p. 129) — this is the part carrying your dimensional point.** For B to predict A, either B calculates its own interference with A (which regresses — studying A+B′ "the whole problem arises again") or B disturbs A negligibly. Take the second. Then a one-way membrane appears: A→B influence must be strong, B→A weak. Popper's reason is exactly the sensitivity argument you're using: "some minute differences at the instant t₁ may, in a mechanical system such as A, give rise to considerable differences at t₂; but since B is a predictor… it must be able to react in very different ways to the two minutely different states of A." Therefore **"a predictor B must be an amplifier."** A footnote sharpens it: predictors must be amplifiers "merely as recorders of measurements; for they must be capable of recording minute differences by the same method (the punching of holes) as large ones." That footnote is the cleanest seed of your point — the *recording* step, the FANOUT, is where a minute phase-space difference must be lifted to a macroscopically distinct, persistent mark.

**The breakdown (Part I, §7, pp. 129–130).** When two predictors B and C each try to predict the other, each amplifies the other's weak disturbances; the one-way membrane fails both ways; neither can predict the other. Popper roots this explicitly in self-knowledge: the failure "depends on the fact… that neither of the machines can have knowledge of its own state before that state has passed; in fact, it can obtain information about its own state only by way of studying the results obtained by another machine." This is your relational point arriving from the predictor side — a system's own state is not available to it except via another system, which is close to Rovelli's "no meaning in being correlated with oneself."

**Popper's own ℏ remark (Part I, §6, p. 128).** He states the action-quantum connection himself, and this is the sentence to quote against Rovelli: in quantum physics the indeterminacy of interference vanishes "if we assume that h = 0… the absence of a quantum of action is the distinguishing characteristic of classical physics." His whole Part I thesis is then that *classical* mechanics suffers an *analogous* indeterminacy "from interference from within" even with h = 0 — i.e. the predictor obstruction does not need ℏ to bite. Note what this means for your reading: Popper does **not** derive ℏ from self-prediction. He derives a *structurally parallel* obstruction that survives at ℏ = 0. The action quantum is what the obstruction *would* localise to in a quantum world, but in his classical treatment the floor is set by mechanical robustness, not by ℏ.

**The robustness floor (Part II, p. 192; Part I, p. 132).** The minimum-cell idea you want is present but it's mechanical, not action-dimensioned. Part I p. 132: in a continuum mechanics "there must be a lower limit to [the tentacles'] thickness or mass… otherwise they would become too easily distorted… no D can be at the same time effective and vanishingly small." Part II p. 192 gives the temporal version: every machine has a "specious present" Δtₖ, "the minimum time it takes C to 'know' what has happened to it," bounded below because "for every actual physical machine there is a maximum running speed, and consequently a minimum length of time necessary for completing even the shortest description." So Popper has *both* a minimum spatial scale of the recording apparatus and a minimum time per recorded bit — the two factors whose product is action — but he never multiplies them, and he never claims universality across systems. That last step is yours (and is exactly the step Rovelli skips by fiat).

**The Gödelian core (Part II §III, pp. 179–183) — the spine match.** This is where Popper is doing your Lawvere–Yanofsky move in 1950. He invokes Gödel 1931 by name (p. 179, with Rosser, Tarski, Turing in the footnote) and uses the *second* theorem specifically: if g is undecidable in Sₙ, then the true statement h asserting g's undecidability is itself undecidable in Sₙ (p. 180). He then converts this from pure mathematics into a *physical* prediction question. A "near-Gödelian question" q₁ asks C: "if you are asked q₂ and given any amount of time, will you ultimately signal yes or no?" where q₂ is Gödelian relative to C's premise set J₂. Because C has cumulative memory (J₁ ⊆ J₂), and h is undecidable in every sub-system, C can only answer "I do not know yet" until t₂ has passed (pp. 182–183). The undecidability of a *mathematical* sentence is thereby transferred to a *physical* fact about the machine's future reaction — "a mathematical truism about all computers satisfying certain general conditions." This is precisely your self-reference → epistemic-limit-on-self-knowledge step, and Popper gets there by arithmetisation, the same Gödel-numbering diagonal that Lawvere later abstracts categorically.

**The self-information impossibility (Part II §III, pp. 189–191).** The decisive lemma: for C's self-information at t₁ to be correct and current, it "would have to contain, as one of its parts, a physical description of that very self-information, using physical symbols of the same kind as in the rest of its information. But this… is impossible for any finite piece of information; and an infinite piece cannot be completed at any instant." Feedback doesn't help ("a feed-back would inform C always after the event"); using information twice, or n times, only generates "an incessant stream of self-produced new information" so C "will never be able to begin predicting" (p. 190). Summary line, p. 191: "'Know thyself' is a contradictory ideal; we cannot fully know our limitations." This is the diagonal obstruction stated operationally — a system cannot host a complete current model of itself including the model.

---

**How to position it against Rovelli.** The clean framing for your paragraphs:

Rovelli postulates finite information capacity (Postulate 1) and reads ℏ off as the bit↔action conversion factor by dimensional analysis on phase space. He needs the *ceiling* (≤ N bits) as a primitive and asserts universality of the cell. Popper, fifty years earlier, gives two independent *derivations* of why a predictor cannot have complete current self-information — a physical one (the amplifier/one-way-membrane regress, Part I §7) and a logical one (the Gödelian self-prediction obstruction, Part II §III) — and these target the *floor* (the irreducible minimum self-resolution) rather than the ceiling. Your synthesis is that the floor is the load-bearing one for ℏ: the obstruction sites a minimum distinguishable self-perturbation at the scale of the predictor's smallest component, that perturbation must be a phase-space cell once conjugacy is in play (upstream spine), and a cell of nonzero area carries the dimension of action. Popper supplies the obstruction and even both factors (minimum apparatus scale, minimum time per bit) but stops short of forming the product or claiming universality; Rovelli supplies the universality and the ℏ identification but by postulate rather than derivation. The framework's contribution is the identification that joins them — Popper's Gödelian floor *is* the mechanism that Rovelli's Postulate 1 merely asserts.

One caution to keep the claim honest in the paper: Popper himself believed his classical argument works at ℏ = 0, so he is *not* claiming self-reference produces the action quantum. The honest statement is that Popper establishes the self-prediction obstruction is theory-independent (he conjectures it holds for "every system sufficiently complete to contain a theory which can analyse the functioning of the predictor," p. 133, and says quantum mechanics in particular is subject to it), and that *in a world with conjugate observables* that theory-independent obstruction localises to an action cell. The ℏ-from-self-reference reading is your bridge, with Popper supplying the obstruction and Rovelli supplying the dimensional reading — neither author makes the joint claim, which is precisely where the novel identification lives.

Want me to write a session-summary markdown of the Popper extraction (timestamped, with the page anchors above) so it's in the corpus for when you draft Paper 1, and a clean BibTeX entry for both parts?
