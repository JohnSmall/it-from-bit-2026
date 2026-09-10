# Continuity from self-reference: limit-realisability, the closedness lemma, and the super-task connection

**Session document, 2026-07-04.** Consolidates the self-reference ⟺ reversible-continuity thread:
the May 2026 record, the Lagrange episode (which until this document existed only in conversation
memory), today's closedness lemma that compresses the residual to a single premise, the corrected
form of the diagonalisation instinct, and the super-task/Thomson-lamp integration — the last
connecting founding corpus material (Session 1) to this session's loops-as-supertasks prospect and
to today's lemma, all as consumers of one premise: limit-realisability.

**Status flags used throughout:** RECORDED (in a project document, cited by file and line);
MEMORY-ONLY (established in an untranscribed session, written down here for the first time);
NEW-TODAY (2026-07-04, this conversation); JS-TODAY (John's point this conversation, refined here).

---

## 1. The recorded structure (RECORDED: dynamics_companion_fanout_unitarity_2026-05-20T1430.md)

The pre-FANOUT regime is characterised five equivalent ways — "not five premises to be combined;
one regime under five descriptions": (1) negative probability available; (2) anti-events /
reversibility; (3) no classical record; (4) no preferred basis; (5) Hardy's continuity (a continuous
reversible transformation between any two pure states). FANOUT is the single event that fails all
five at once.

The proved core is **4 ⇔ 5** (§4.3 of the May doc): a preferred basis is a distinguished finite set
of pure states, whose structure-preserving reversible maps are permutations — a discrete group — so
continuous reversibility ⇒ no basis selected; conversely, with no privileged finite set the
reversible transformations cannot be pinned to permutations, so the pure-state space is homogeneous
under them. Slogan: *the selection of a basis is exactly the collapse of a continuous transformation
group to a discrete one.* The strategic conversion: Hardy's theorem then does all downstream work as
a citation (continuity + his mild axioms → complex Hilbert space, quadratic norm, U(n)), so the
framework owes **one arrow**: self-reference ⟹ the pre-FANOUT regime. The May doc's own words:
"plausible but not written down." Over-determination keystone: reversibility alone = GL(n, ℂ) =
Aaronson's superluminal-signalling-plus-PP option, so the quadratic cut is physically forced.

Recorded caveat: Hardy needs continuity *plus* his subspace/composition axioms — to be confirmed
derived, not assumed free. (Adjacent recorded asset: inside/outside equivalence ⟹ local tomography,
Pure_states_and_mixed_states doc, line 87; and the division-algebra section's composition ledger,
drafted 2026-07-03, is the natural home of the tensor/composition story.)

## 2. The Lagrange episode (MEMORY-ONLY until this document)

A later, untranscribed session attacked the gap in §4.3's converse — "not permutations" does not by
itself give *continuous*; the group could be discrete-but-infinite. The recorded-in-memory result:

**Premise (divisibility).** The framework's pre-FANOUT structure forces the reversible-transformation
group to be divisible: every transformation has an n-th root for every n. *Flag:* the exact recorded
derivation of divisibility from the anti-event/no-distinguished-step structure was not written down
and needs its own justification when sec:self-reference is drafted. Candidate form: a reversible
transformation with no selected basis has no distinguished step size; any transformation must be
realisable in n equal describable stages for every n. OWED.

**Finite exclusion (Lagrange).** A nontrivial finite group is never divisible: with |G| = m, every h
satisfies hᵐ = e, so no g ≠ e has an m-th root. Finite escape hatch closed. PROVED (one line;
recorded in memory, now here).

**Residual as then recorded:** countably infinite divisible discrete groups exist (ℚ, ℚ/ℤ, the
Prüfer groups) — can they satisfy the full premise? OPEN as of the May–June record.

## 3. NEW-TODAY: the closedness lemma — the residual compresses to one premise

**Setting (standard).** Hardy's reversible transformations preserve the state body, a compact convex
set with nonempty interior in ℝᴷ; the symmetry group of such a body is compact. So the reversible
transformations sit inside a compact group, and the only question is what subgroup they form.

**Lemma.** If the group G of reversible transformations is divisible and topologically closed, then
G is a compact connected Lie group.
*Proof.* Closed in compact ⟹ compact; a compact group of matrices is Lie with finitely many
connected components (Cartan). The component group π₀(G) = G/G₀ is a quotient of a divisible group,
hence divisible; a finite divisible group is trivial — the same Lagrange argument as §2, promoted
from closing the finite case to closing the disconnectedness case. Hence G = G₀ connected. ∎

**Corollary (the countable case dies without the diagonal).** A countable closed subgroup of a
compact group is compact and countable, hence has an isolated point (Baire), hence is discrete,
hence finite, hence trivial by Lagrange.

**Corollary (Hardy A5).** Divisible + closed + transitive on pure states ⟹ a connected (hence
path-connected) Lie group acting transitively ⟹ a continuous reversible path between any two pure
states: Hardy's continuity axiom.

**The compression.** Finite, countable, and uncountable-totally-disconnected escape hatches all fall
to divisible + closed. The entire residual is now **one owed premise: closedness** — the group
contains its limits. Two routes to it:

*Route A (framework-native, primary — see §4):* closedness = completeness = limit-realisability,
derived from self-referential closure: a Cauchy sequence of physically available transformations
whose convergence the system can itself describe must have its limit available, or the system's own
description refers to a transformation that does not exist. Lawvere-shaped. OWED, sharply posed.

*Route B (independent mathematical attack):* automatic continuity — Steinhaus/Pettis-type theorems
(a measurable homomorphism into a Polish group is continuous), with measurability physically
grounded (transformations must yield well-defined record probabilities) rather than imported.
Recorded as an alternative; not attempted.

## 4. The diagonalisation instinct, corrected and cashed (JS + NEW-TODAY)

**JS's instinct (this conversation):** self-reference in Cantor's diagonal creates the uncountable,
"fills the gaps in ℚ," hence ℝ from ℚ — a direct route from self-reference to continuity. The
corpus already carries the strong slogan (RECORDED, framework_summary_for_llm_review.md:190): "The
completeness of ℝ simultaneously enables convergent supertasks (∑2⁻ⁿ = 1) and Cantor's diagonal
argument — these are the same theorem."

**Dead-route box (NEW-TODAY, recorded so it is not retried in this form).** Two things the diagonal
does not do. (i) It is a non-exhaustion argument, not a construction: given a listing it exhibits
one unlisted element, relative to that listing; it does not enumerate the gaps or build the
completion. Completion (Dedekind/Cauchy) fills the gaps, and the gaps were known without
self-reference (√2). (ii) **Uncountability is not continuity**: the irrationals, the Cantor set,
and an uncountable proper ℚ-subspace of ℝ are all uncountable and totally disconnected — the last
is moreover divisible, so the diagonal at full strength only moves the residual from "countable
divisible" to "uncountable totally-disconnected divisible." Only completion gives connectedness,
and connectedness is what Hardy A5 asserts.

**The corrected relation (NEW-TODAY), preserving the corpus slogan's insight.** The diagonal's
output is an infinite decimal — a Cauchy sequence of rationals — and its existence *as a point*
is completeness. The supertask's terminal moment likewise (see §5). So "same theorem" refines to
**same licence**: limit-realisability underwrites both the diagonal number's existence and the
supertask's terminal moment; the diagonal then shows the completed line outruns every internal
listing. The instinct's correct home is Route A: closedness as completeness, demanded by
self-referential closure over describable limits.

**The jewel (NEW-TODAY).** The computable reals are countable, hence Lebesgue-null: the completion
is non-computable almost everywhere. Hardy's continuity axiom — the postulate every reconstruction
programme imports — is on this reading the demand that the transformation group contain its
*non-computable* limits. **Continuity is the topological face of the founding non-computability.**

## 5. Super-tasks and Thomson's lamp: the point drawn in (JS-TODAY + RECORDED, founding)

**Founding record.** The lamp is Session-1 material (RECORDED, e8_self_reference_bott_periodicity.md:203:
"Supertasks and Thomson's lamp (Session 1): Where classical computation meets its boundary — the
entry points for complex probability"). The committed resolution (RECORDED,
research_summary_neg_prob.md §4.1 and table): the lamp has no classical final state; the framework
assigns the complex fixed point (1+i)/2, the imaginary part encoding *when* it would have stopped —
"the Thomson lamp supertask physically instantiates the diagonal construction, producing
superposition as the fixed point" (framework_summary:190). Spelling note for all documents:
**Thomson** (James F. Thomson, who coined "super-task", Analysis 1954), not Thompson.

**JS's point today, refined.** "Super-tasks need the completion of the reals in order to become
super-tasks." Sharp form: (i) the textbook lamp's accumulation point is t = 1 ∈ ℚ, so that
particular sequence's limit exists in ℚ; the general claim is that *generic* super-tasks — arbitrary
summable step-durations — have accumulation points that exist only in the completed line; (ii) more
fundamentally, the super-task *form* ("the state after all the steps") presupposes the terminal
moment as an actual point of the timeline: **limit-realisability of time**. Super-tasks are
downstream consumers of exactly the premise §3 compressed the residual to.

**The lamp's double duty (NEW-TODAY synthesis, reconciling founding record with today's lemma).**
(a) The classical undetermination — any terminal on/off value is consistent with all finite data
(Thomson's point; Benacerraf's diagnosis) — is the proof that the **record algebra is not
limit-closed**: classical records cannot be completed. Theorem-level. (b) The committed (1+i)/2
resolution is the statement that the **amplitude side is limit-closed**: the limit exists there, as
a superposed fixed point. Structural/framework-level (the specific value inherited from the
negative-probability thread). Together: **the FANOUT boundary is the edge of limit-realisability** —
complete on the reversible/amplitude side (which *is* Hardy continuity), incomplete on the record
side (which *is* Thomson's undetermination). One boundary; the lamp exhibits both sides at once.
The founding fixed-point assignment and today's closedness lemma corroborate each other from
opposite ends of the corpus, sixteen months apart.

**Operational-time note.** With time as operation count (the framework's loop-counting; Paper 2),
there is no operational moment "after ω operations": the lamp packs ω FANOUTs into *emergent*
continuum time. The paradox is a category confusion between container (the emergent, completed
continuum, whose completeness is the pre-FANOUT side's property) and contents (the discrete record
sequence). The framework does not have to answer "on or off at t = 1"; it explains why the question
has no record-level referent and what the amplitude-level referent is.

**The loops stitch (RECORDED, this session pre-compaction).** The Växjö-prompted prospect
("Loops, supertasks, and a second route to parallelisability",
loops_renormalizability_prospects_2026-06-13.tex, destined for the summary section) reads a Feynman
loop as "a supertask, an infinite computation closed into a finite process." That reading itself
presupposes the completed continuum — i.e. the prospects consume the limit-realisability that
sec:self-reference will derive. Optional one-clause enrichment to that paragraph when it is placed:
tie the supertask reading back to the foundations ("...a supertask, an infinite computation closed
into a finite process — a form whose very statement presupposes the completed continuum derived in
\S\ref{sec:self-reference}"). Paper-2 prospects thereby visibly rest on Paper-1 foundations.

## 6. The owed arrow, restated

**Primary:** self-reference ⟹ limit-realisability of the reversible-transformation group under
describable Cauchy limits (Route A). Everything downstream is then the lemma of §3 plus Hardy as a
citation. **Secondary owed:** the derivation of divisibility (§2 flag); confirmation of Hardy's
subspace/composition axioms (division-algebra ledger + inside/outside ⟹ local tomography).

## 7. Paper placement (recommendations)

sec:self-reference, continuity passage, when drafted: the five-way regime; a Proposition for 4 ⇔ 5;
the closedness lemma (or its statement with proof in an appendix); a numbered open problem for the
owed arrow carrying the Lagrange/closedness status; and a short super-task paragraph — completeness
licenses both the diagonal's output and the super-task's terminal moment; the lamp's classical
undetermination as the record side's incompleteness, its superposed fixed point as the amplitude
side's closure; the boundary as the edge of limit-realisability. Cite Thomson 1954 (Benacerraf 1962
optional). Cross-refs: sec:fanout-boundary; the prospects paragraph's optional clause (§5).

## 8. References (informal; verify and RIS at paper-drafting stage)

Hardy, "Quantum Theory From Five Reasonable Axioms", arXiv:quant-ph/0101012 — note the May doc cites
this as "(2003)"; the arXiv posting is January 2001 — fix at citation time. Thomson, "Tasks and
Super-Tasks", Analysis 15(1), 1–13 (1954). Benacerraf, "Tasks, Super-Tasks, and the Modern
Eleatics", J. Phil. 59 (1962) — details to verify. Cartan closed-subgroup theorem and the compactness
of convex-body symmetry groups: standard; choose a textbook citation at drafting. Steinhaus/Pettis
automatic continuity: standard; Route B only. Aaronson "Is Quantum Mechanics An Island In Theoryspace?"
and Wigner's theorem: as in the May doc's settled list.
