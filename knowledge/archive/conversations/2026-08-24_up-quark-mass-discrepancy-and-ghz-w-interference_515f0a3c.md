# Up quark mass discrepancy and GHZ-W interference

- conversation uuid: `515f0a3c-49a1-4d71-8b24-be2447f2bb26`
- created: 2026-08-24T17:48:04.920275Z  |  updated: 2026-08-24T18:18:08.587987Z
- messages: 4  |  keyword score: 2

## Summary (from the Claude export)

**Conversation Overview**

The person is working on a physics framework paper that derives charged fermion masses from an entanglement-class-based formalism. The conversation centred on a specific internal inconsistency: the existing text in `masses_section_2026-06-08.tex` explained the up-quark mass discrepancy (formula predicts 2.78 MeV against observed 2.16 ± 0.07 MeV) by invoking "tripartite (GHZ) and pairwise (W) contributions" interfering to shorten an effective path — but the framework elsewhere establishes that quarks do not participate in the W sector. The person asked how GHZ–W interference could be invoked for a quark state, identifying this as a fossil from an earlier drafting pass.

Claude diagnosed the problem across three layers: the word "W" was doing double duty as both an SLOCC class label and a description of pairwise entanglement; the canonical GHZ orbit (on which physical particle states are computed by the framework's own postulate) has Bloch radius zero on every cut and therefore zero pairwise tangle, leaving nothing for anything to interfere with; and the actual mechanism — cross-algebra excursions in the sedenion sector, priced at the leptonic ninth — was already in `op:up-quark` from a July 2026 revision but had not been propagated back into the masses paragraph. Claude also identified the exact reason the discrepancy must land on the up quark specifically: its triality-form residue (ρ_u = 0.0110) is the smallest in the full nine-fermion table by a factor of 3.65, making it by construction the most sensitive number the formula produces, with the entire discrepancy corresponding to a 0.13% amplitude displacement.

The person then requested the paragraph be re-voiced. Claude produced a sentinel-gated replacement fragment (`up_quark_revoice_fragment_2026-08-24T0900.tex`) and a patch script (`patch_up_quark_revoice_2026-08-24T0900.py`) covering three files: the masses section (full paragraph replacement), `confinement_section_2026-06-13.tex` (two sentences in `sec:budget-converse` correcting "GHZ-class register" to "canonical GHZ orbit"), and `entanglement_classes_and_gauge_groups_2026-06-08.tex` (the tilted-states sentence in `sec:canonical-orbits`). The script asserts all anchors whitespace-insensitively before writing, writes `.bak_2026-08-24T0900` files, adds `EDITED` headers under each ruler, and refuses to run twice. The patched text was compile-checked with pdflatex twice against fixtures, producing zero errors. The new text names and defines "the comparability condition" as a statement about the triality form's two terms, so that `op:up-quark`'s existing reference to it resolves to something exact. Outstanding fossils not touched — the following paragraph's "two-per-cent W component" and entries in `fermion_topology_table.py` and `fermion_topology_open_problems.md` §5.2 — were flagged explicitly. The sector-specificity inference (that the omitted effect must single out the up-type channel, n = 3) was marked CANDIDATE status, not corpus-grade.

**Tool Knowledge**

Project knowledge search was used extensively with precise technical anchors drawn from the corpus (equation labels, section labels, theorem names, operator names such as `op:up-quark`, `app:hw-ninth`, `app:qiskit-interference`) rather than prose descriptions; this reliably retrieved the relevant passage on the first query. Bash was used to build LaTeX fixtures reconstructed from the quoted corpus text and wrapped at a deliberately different column width than the patch script's target width, in order to verify that the whitespace-insensitive anchor matching worked across reformatting. The compile check used a minimal `\documentclass{article}` wrapper with `\input{}` of the three patched files; undefined-reference warnings were expected and counted separately from errors, confirming zero actual compile errors. The re-run guard (sentinel already present → abort) was tested explicitly on the fixture directory after a live run.

## Transcript

### 1. human  ·  2026-08-24 17:48:06

I need a good explanation of why the up quark doesn't fit our derivation of quark masses in the project context, github import `masses_section_2026-06-08.tex` we have "Eight of the nine charged fermions are reproduced to about one per cent.
The ninth is not. The up quark comes out at $2.78$~MeV against an observed $2.16 \pm 0.07$~MeV, an
error of some twenty-nine per cent and far outside the quoted uncertainty. This is a genuine failure
of the formula as it stands, not a rounding issue. Two mitigating
observations follow, neither a resolution. The up-quark mass is never measured directly --- it is
extracted from lattice QCD with chiral perturbation theory, and determinations range over roughly
$1.9$--$2.5$~MeV, at the top of which range the discrepancy shrinks to about twelve per cent. And a
candidate mechanism is identified: at the first generation, and only there, the tripartite (GHZ) and
pairwise (W) contributions to the mass are of comparable size, and their interference shortens the
effective path. The clause that keeps this consistent with the framework's species assignment: the
quark state remains GHZ-class throughout --- the pairwise structure is forced \emph{within} that
class by the Cayley--Dickson nesting $\mathbb{C} \subset \mathbb{H} \subset \mathbb{O}$, and
the interference is between contributions to the mass functional, never a superposition of
species, which are class-discrete. The mechanism is consistent with the up quark also being the
one fermion whose $T_3 = +\tfrac12$ member is \emph{lighter} than its doublet partner, the
competition between the amplitude effect (larger $\alpha$ for up-type) and the dilution effect
(smaller $\delta$) tipping the other way at the lightest generation."

But we're also stating that quarks don't participate in the W sector, so how do we get an interference between GHZ and W accounting for the up quark discrepancy?

I need a good explanation of why the up quark doesn't fit our derivation of quark masses in the project context, github import `masses_section_2026-06-08.tex` we have "Eight of the nine charged fermions are reproduced to about one per cent.
The ninth is not. The up quark comes out at $2.78$~MeV against an observed $2.16 \pm 0.07$~MeV, an
error of some twenty-nine per cent and far outside the quoted uncertainty. This is a genuine failure
of the formula as it stands, not a rounding issue. Two mitigating
observations follow, neither a resolution. The up-quark mass is never measured directly --- it is
extracted from lattice QCD with chiral perturbation theory, and determinations range over roughly
$1.9$--$2.5$~MeV, at the top of which range the discrepancy shrinks to about twelve per cent. And a
candidate mechanism is identified: at the first generation, and only there, the tripartite (GHZ) and
pairwise (W) contributions to the mass are of comparable size, and their interference shortens the
effective path. The clause that keeps this consistent with the framework's species assignment: the
quark state remains GHZ-class throughout --- the pairwise structure is forced \emph{within} that
class by the Cayley--Dickson nesting $\mathbb{C} \subset \mathbb{H} \subset \mathbb{O}$, and
the interference is between contributions to the mass functional, never a superposition of
species, which are class-discrete. The mechanism is consistent with the up quark also being the
one fermion whose $T_3 = +\tfrac12$ member is \emph{lighter} than its doublet partner, the
competition between the amplitude effect (larger $\alpha$ for up-type) and the dilution effect
(smaller $\delta$) tipping the other way at the lightest generation."

But we're also stating that quarks don't participate in the W sector, so how do we get an interference between GHZ and W accounting for the up quark discrepancy?

### 2. assistant  ·  2026-08-24 17:57:53

I'll pull the relevant pieces from the project first — the masses section, the GHZ/W dictionary, and whatever the monogamy/three-tangle material says — since the answer turns on exactly what "pairwise contribution" is allowed to mean inside the GHZ class.
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


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The short answer: your instinct is right, and the corpus already half-knows it. The appendix `app:qiskit-interference` was re-voiced on 2026-07-11 after the class-discreteness retirement; the masses paragraph you quote was not, and it still carries three fossils. The word "W" is doing two jobs in it — naming an SLOCC class (a species label) and naming a *kind* of entanglement (pairwise) — and the mechanism is defensible only under the second reading, and even then it cannot live where the paragraph puts it. Here is the argument in three layers, then the "why the up quark and nowhere else" arithmetic, which I think is the cleanest explanation available and isn't yet in the corpus.

**Layer 1 — class versus kind.** SLOCC classes are orbits, so the probe family α|GHZ⟩ + β|W⟩ is generically GHZ-class; no W-class state is involved. What *is* involved is the CKW budget: for any cut, the one-tangle τ_A = 1 − r² = 4 det ρ_A splits exactly (pure three-qubit states) as C²_AB + C²_AC + τ₃. The canonical GHZ representative puts the whole budget into τ₃ with pairwise concurrences exactly zero; the canonical W puts all of it pairwise with τ₃ = 0; a generic point of the GHZ *class* has both. So "tripartite (GHZ) and pairwise (W) contributions" is class-consistent only if it means the τ₃ share and the pairwise-concurrence share of a GHZ-class register's budget. The quantity Notebook B actually measures, the Bloch radius of the cut, is r = √(1 − τ_A): the unspent budget, which by your own Ceiling lemma is also the orbit ceiling of the ℂ-projection, sup C_frac = r². The "interference" is real and precise — the off-diagonal of ρ_A acquires a cross term of modulus αβ/√6, first order in β, hence r ∝ β rather than β² — but it is interference between components of a vector inside one class, not between species. The double use traces to the April 2 summary's "GHZ has both nonzero 2-tangles and 3-tangle, so quarks participate in both forces": true of the class generically, false of the canonical representative, where the 2-tangles vanish exactly.

**Layer 2 — class membership is not enough.** The clause "the quark state remains GHZ-class throughout" is necessary but not sufficient, because the framework's load-bearing postulate in `sec:canonical-orbits` is stronger: a physical one-particle state is the canonical maximally entangled *orbit*, and the masses are computed on canonical orbits. On that orbit Theorem `app:thm:char` gives r = 0 on every cut — zero ℂ-projection (Corollary, instance (i), which *is* confinement), zero pairwise concurrence, zero external tangle. There is no pairwise budget in the register for anything to interfere with, at generation one or anywhere. A register displaced toward the W boundary by β² ≈ 0.02 has r ≈ 0.11, hence a ℂ-projection ceiling of r² ≈ 0.013 and, by `sec:budget-converse`, that much external pairwise tangle available: a fractionally lepton-plane-accessible, fractionally unconfined up quark. The same section says no downstream result depends on the tilted states; the up-quark paragraph as written is the one place that does. That is the sharp form of your objection: not "quarks aren't W-class" but "quark registers sit on the r = 0 orbit, and an in-register interference needs r ≠ 0."

**Layer 3 — what the corpus already did, and what is stale.** The 2026-07-06 retirement moved the carrier out of the three-qubit register altogether: the register stays canonical, as confinement requires, and the generation-one admixture lives in the sedenion cross-algebra sector on the fourth qubit. Notebook B is then a proxy — it fixes how the mass-relevant invariant responds to *any* effective admixture (first order, phase-rigid), which is why it survives its first framing. The W sector enters legitimately but differently: not as a component of the quark's state but as the *price* of a cross-algebra excursion — the leptonic ninth, 1/9, which is exactly the canonical W orbit's slack r² = 1 − 8/9 (Notebook J, your most-measured number). Two excursions, which-path-recorded by FANOUT, give δm/m = −2/9 = −δ₀, the July 12 result now in `op:up-quark`. So "how does W get in" answers: through the ledger price of an excursion into the record plane, priced at the W orbit's unspent ninth. The paragraph predates this. Its fossils are "pairwise (W) contributions to the mass", "shortens the effective path" (March 18 geodesic language), and "the pairwise structure is forced within that class by the Cayley–Dickson nesting" — which on the canonical orbit cannot mean pairwise concurrence of the colour register (exactly zero there), only the ℍ-level isospin structure the paper carries on the doublet/Filatov side, so the clause must say which structure it means or go.

**Why the up quark, and only the up quark.** The triality form makes √m_k = M(1 + α cos θ_k) the residue of a cancellation between the identity term and the rotation term, deepest at the lightest generation. The residues across the nine fermions, smallest first: u 0.0110, e 0.0403, d 0.0843, c 0.236, s 0.381, μ 0.580, then the heavy three. The up quark's residue is 3.65× smaller than the next (electron) and 7.6× smaller than the down; since δm/m = 2 δρ/ρ, it is by construction the most sensitive number in the table. The entire 28.5% discrepancy is an amplitude displacement of 0.13% of M_up. That same 0.13% would move charm by 1.1% and top by 0.09% — invisible at the paper's tolerance — but the electron by 6.5% and the down by 3.1%, which are not seen. Two conclusions: the one failure landing on the up quark is what a small omitted effect *must* look like, since it shows up there first and there alone within its sector; and the effect cannot be universal across sectors — it must be specific to the up-type channel (n = 3, T₃ = +½), which is where the March 18 note already located the larger deviations and where the neutrino tensions also sit. This reads the "comparability condition" — the selection residue `op:up-quark` left open on July 12 — as an exact statement about the triality form rather than about W content, cleanly separated from the pricing. A discriminator falls out: the recorded candidate is multiplicative and generation-one-selected (charm untouched, +0.11%); if the dressed shift instead acts additively at amplitude level and sector-universally, charm moves to 1259 MeV (−0.90%), outside its PDG band. Charm decides between the two readings of "selection", and that is worth pre-registering when the dressed operator gets its selection clause.

Statuses: layers 1–2 are theorem-grade on your own results; layer 3 is the corpus's CANDIDATE; the residue arithmetic is exact on the formula; the up-sector-specific inference is a CANDIDATE reading of mine, not in the corpus. Two consistency nits surfaced on the way: `sec:budget-converse` says "for a GHZ-class register the same bound reads zero, exactly, always", an orbit fact in class words (the Remark [Orbit, not class] says the class contains r ≠ 0 states) — should read "canonical GHZ orbit"; and `main_debug.tex`'s table footnote still says "W-class interference mechanism".
```
This block is not supported on your current device yet.
```

The script reproduces your table (2.776, 1271.4, 4.624, 94.4, 0.511, 105.65) and prints the three hypotheses as PASS/FAIL with the charm discriminator.

Want the re-voiced paragraph as a sentinel-gated splice for `masses_section_2026-06-08.tex`, with the `sec:budget-converse` one-word fix and the tilted-states sentence in `sec:canonical-orbits` amended to match?

I'll pull the relevant pieces from the project first — the masses section, the GHZ/W dictionary, and whatever the monogamy/three-tangle material says — since the answer turns on exactly what "pairwise contribution" is allowed to mean inside the GHZ class.

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

The short answer: your instinct is right, and the corpus already half-knows it. The appendix `app:qiskit-interference` was re-voiced on 2026-07-11 after the class-discreteness retirement; the masses paragraph you quote was not, and it still carries three fossils. The word "W" is doing two jobs in it — naming an SLOCC class (a species label) and naming a *kind* of entanglement (pairwise) — and the mechanism is defensible only under the second reading, and even then it cannot live where the paragraph puts it. Here is the argument in three layers, then the "why the up quark and nowhere else" arithmetic, which I think is the cleanest explanation available and isn't yet in the corpus.

**Layer 1 — class versus kind.** SLOCC classes are orbits, so the probe family α|GHZ⟩ + β|W⟩ is generically GHZ-class; no W-class state is involved. What *is* involved is the CKW budget: for any cut, the one-tangle τ_A = 1 − r² = 4 det ρ_A splits exactly (pure three-qubit states) as C²_AB + C²_AC + τ₃. The canonical GHZ representative puts the whole budget into τ₃ with pairwise concurrences exactly zero; the canonical W puts all of it pairwise with τ₃ = 0; a generic point of the GHZ *class* has both. So "tripartite (GHZ) and pairwise (W) contributions" is class-consistent only if it means the τ₃ share and the pairwise-concurrence share of a GHZ-class register's budget. The quantity Notebook B actually measures, the Bloch radius of the cut, is r = √(1 − τ_A): the unspent budget, which by your own Ceiling lemma is also the orbit ceiling of the ℂ-projection, sup C_frac = r². The "interference" is real and precise — the off-diagonal of ρ_A acquires a cross term of modulus αβ/√6, first order in β, hence r ∝ β rather than β² — but it is interference between components of a vector inside one class, not between species. The double use traces to the April 2 summary's "GHZ has both nonzero 2-tangles and 3-tangle, so quarks participate in both forces": true of the class generically, false of the canonical representative, where the 2-tangles vanish exactly.

**Layer 2 — class membership is not enough.** The clause "the quark state remains GHZ-class throughout" is necessary but not sufficient, because the framework's load-bearing postulate in `sec:canonical-orbits` is stronger: a physical one-particle state is the canonical maximally entangled *orbit*, and the masses are computed on canonical orbits. On that orbit Theorem `app:thm:char` gives r = 0 on every cut — zero ℂ-projection (Corollary, instance (i), which *is* confinement), zero pairwise concurrence, zero external tangle. There is no pairwise budget in the register for anything to interfere with, at generation one or anywhere. A register displaced toward the W boundary by β² ≈ 0.02 has r ≈ 0.11, hence a ℂ-projection ceiling of r² ≈ 0.013 and, by `sec:budget-converse`, that much external pairwise tangle available: a fractionally lepton-plane-accessible, fractionally unconfined up quark. The same section says no downstream result depends on the tilted states; the up-quark paragraph as written is the one place that does. That is the sharp form of your objection: not "quarks aren't W-class" but "quark registers sit on the r = 0 orbit, and an in-register interference needs r ≠ 0."

**Layer 3 — what the corpus already did, and what is stale.** The 2026-07-06 retirement moved the carrier out of the three-qubit register altogether: the register stays canonical, as confinement requires, and the generation-one admixture lives in the sedenion cross-algebra sector on the fourth qubit. Notebook B is then a proxy — it fixes how the mass-relevant invariant responds to *any* effective admixture (first order, phase-rigid), which is why it survives its first framing. The W sector enters legitimately but differently: not as a component of the quark's state but as the *price* of a cross-algebra excursion — the leptonic ninth, 1/9, which is exactly the canonical W orbit's slack r² = 1 − 8/9 (Notebook J, your most-measured number). Two excursions, which-path-recorded by FANOUT, give δm/m = −2/9 = −δ₀, the July 12 result now in `op:up-quark`. So "how does W get in" answers: through the ledger price of an excursion into the record plane, priced at the W orbit's unspent ninth. The paragraph predates this. Its fossils are "pairwise (W) contributions to the mass", "shortens the effective path" (March 18 geodesic language), and "the pairwise structure is forced within that class by the Cayley–Dickson nesting" — which on the canonical orbit cannot mean pairwise concurrence of the colour register (exactly zero there), only the ℍ-level isospin structure the paper carries on the doublet/Filatov side, so the clause must say which structure it means or go.

**Why the up quark, and only the up quark.** The triality form makes √m_k = M(1 + α cos θ_k) the residue of a cancellation between the identity term and the rotation term, deepest at the lightest generation. The residues across the nine fermions, smallest first: u 0.0110, e 0.0403, d 0.0843, c 0.236, s 0.381, μ 0.580, then the heavy three. The up quark's residue is 3.65× smaller than the next (electron) and 7.6× smaller than the down; since δm/m = 2 δρ/ρ, it is by construction the most sensitive number in the table. The entire 28.5% discrepancy is an amplitude displacement of 0.13% of M_up. That same 0.13% would move charm by 1.1% and top by 0.09% — invisible at the paper's tolerance — but the electron by 6.5% and the down by 3.1%, which are not seen. Two conclusions: the one failure landing on the up quark is what a small omitted effect *must* look like, since it shows up there first and there alone within its sector; and the effect cannot be universal across sectors — it must be specific to the up-type channel (n = 3, T₃ = +½), which is where the March 18 note already located the larger deviations and where the neutrino tensions also sit. This reads the "comparability condition" — the selection residue `op:up-quark` left open on July 12 — as an exact statement about the triality form rather than about W content, cleanly separated from the pricing. A discriminator falls out: the recorded candidate is multiplicative and generation-one-selected (charm untouched, +0.11%); if the dressed shift instead acts additively at amplitude level and sector-universally, charm moves to 1259 MeV (−0.90%), outside its PDG band. Charm decides between the two readings of "selection", and that is worth pre-registering when the dressed operator gets its selection clause.

Statuses: layers 1–2 are theorem-grade on your own results; layer 3 is the corpus's CANDIDATE; the residue arithmetic is exact on the formula; the up-sector-specific inference is a CANDIDATE reading of mine, not in the corpus. Two consistency nits surfaced on the way: `sec:budget-converse` says "for a GHZ-class register the same bound reads zero, exactly, always", an orbit fact in class words (the Remark [Orbit, not class] says the class contains r ≠ 0 states) — should read "canonical GHZ orbit"; and `main_debug.tex`'s table footnote still says "W-class interference mechanism".

*[tool_use: present_files]*

*[tool_result: present_files]*

The script reproduces your table (2.776, 1271.4, 4.624, 94.4, 0.511, 105.65) and prints the three hypotheses as PASS/FAIL with the charm discriminator.

Want the re-voiced paragraph as a sentinel-gated splice for `masses_section_2026-06-08.tex`, with the `sec:budget-converse` one-word fix and the tilted-states sentence in `sec:canonical-orbits` amended to match?

### 3. human  ·  2026-08-24 18:11:13

Yes, re-voice the paragraph.

Yes, re-voice the paragraph.

### 4. assistant  ·  2026-08-24 18:18:08


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


```
This block is not supported on your current device yet.
```

The fragment is the replacement text on its own (sentinel-gated, with the two ancillary edits recorded in its footer); the script applies all three edits to the repo.

Run from the repo root: `python3 patch_up_quark_revoice_2026-08-24T0900.py --dry-run` first, then without the flag. It asserts every anchor whitespace-insensitively and exactly once *before* writing anything, so if your local masses file differs from the synced copy (your quote lacked the "we record it as such" sentence — the anchors bracket that, so either version matches) it aborts with nothing touched. It writes `<file>.bak_2026-08-24T0900` for each target, re-wraps only the affected paragraphs at 100 columns, adds an `EDITED 2026-08-24` line under each header ruler, and refuses to run twice.

What was verified here: the classes edit was applied to the real mounted file (diff clean); masses and confinement were tested on fixtures rebuilt from the synced text at a different wrap width; the patched text compiles under pdflatex twice with zero errors (only `??` refs, since the labels live in main.tex); everything is pure ASCII.

Two things to know about the new text. It names and defines "the comparability condition" — as a statement about the two terms of the triality form, not about W content — so `op:up-quark`'s existing phrase "the comparability condition above" now resolves to something exact. And it cites `\S\ref{sec:register}` for the weak-isospin doublet as a structure of the full register; that follows the classes section's own deferral of weak isospin to the register section, but if the register section places the quark doublet elsewhere, that one reference is the thing to retarget.

Still untouched, deliberately: the following paragraph's "a two-per-cent W component" and "GHZ--W admixture" (probe-family language, now covered by the proxy clause) and the ledger's known fossils in `fermion_topology_table.py` and `fermion_topology_open_problems.md` §5.2.

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: create_file]*

*[tool_result: create_file]*

*[tool_use: create_file]*

*[tool_result: create_file]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: view]*

*[tool_result: view]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: present_files]*

*[tool_result: present_files]*

The fragment is the replacement text on its own (sentinel-gated, with the two ancillary edits recorded in its footer); the script applies all three edits to the repo.

Run from the repo root: `python3 patch_up_quark_revoice_2026-08-24T0900.py --dry-run` first, then without the flag. It asserts every anchor whitespace-insensitively and exactly once *before* writing anything, so if your local masses file differs from the synced copy (your quote lacked the "we record it as such" sentence — the anchors bracket that, so either version matches) it aborts with nothing touched. It writes `<file>.bak_2026-08-24T0900` for each target, re-wraps only the affected paragraphs at 100 columns, adds an `EDITED 2026-08-24` line under each header ruler, and refuses to run twice.

What was verified here: the classes edit was applied to the real mounted file (diff clean); masses and confinement were tested on fixtures rebuilt from the synced text at a different wrap width; the patched text compiles under pdflatex twice with zero errors (only `??` refs, since the labels live in main.tex); everything is pure ASCII.

Two things to know about the new text. It names and defines "the comparability condition" — as a statement about the two terms of the triality form, not about W content — so `op:up-quark`'s existing phrase "the comparability condition above" now resolves to something exact. And it cites `\S\ref{sec:register}` for the weak-isospin doublet as a structure of the full register; that follows the classes section's own deferral of weak isospin to the register section, but if the register section places the quark doublet elsewhere, that one reference is the thing to retarget.

Still untouched, deliberately: the following paragraph's "a two-per-cent W component" and "GHZ--W admixture" (probe-family language, now covered by the proxy clause) and the ledger's known fossils in `fermion_topology_table.py` and `fermion_topology_open_problems.md` §5.2.
