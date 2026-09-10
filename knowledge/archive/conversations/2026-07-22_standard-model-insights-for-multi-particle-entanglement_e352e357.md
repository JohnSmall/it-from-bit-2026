# Standard Model insights for multi-particle entanglement

- conversation uuid: `e352e357-31cf-439a-9525-d7870364dac6`
- created: 2026-07-22T20:31:03.210983Z  |  updated: 2026-07-23T05:13:59.931442Z
- messages: 4  |  keyword score: 3

## Summary (from the Claude export)

**Conversation Overview**

The person is working on a research paper that develops a correspondence dictionary between the mathematical structure of multipartite quantum entanglement and the Standard Model of particle physics. The prior work has moved in one direction — using entanglement classification to deduce Standard Model features including free parameters. In this session, the person asked Claude to explore the reverse direction: using empirically secure Standard Model facts as generators of conjectures and exploratory areas in multipartite entanglement theory. The explicit framing was that outputs should not be well-posed open problems but rather loosely sketched areas of potential interest for other researchers, suitable for inclusion as an appendix in the paper.

Claude generated thirteen such areas, organized around underived Standard Model facts (confinement dynamics, asymptotic freedom, CP violation magnitude, the dark sector) to avoid circularity with already-derived results. Areas included: a string tension analogue for entanglement extraction, broadcast theorems refined by entanglement class, anomaly cancellation as circuit sum rules, beta functions as entanglement renormalization flow, the mass functional as a potential monotone, charge quantization and entanglement polytopes, flavour mixing data as a four-qubit experiment, CP violation and the resource theory of imaginarity, electroweak decoherence spectroscopy, bound entanglement as a gauge-blind/dark sector, confining sectors as quantum memories, Standard Model vertices as a gate library, and measurement-induced phase transitions as a symmetry-breaking analogue. Claude drafted these into a complete LaTeX appendix splice (`appendix_reverse_flow_2026-07-23.tex`) deliberately avoiding the paper's `openproblem` environment, with an explicit preamble stating the circularity discipline and a coda framing the appendix as an open invitation.

The appendix was compiled and verified: pure ASCII, no internal `\ref` cross-references to main-text labels (avoiding label-mapping debt), an optional one-sentence main-body insert provided as a comment, and a PASS/FAIL cross-check confirming all 28 citation keys resolve — 6 reused from the existing library and 22 new entries delivered in an accompanying RIS file (`reverse_flow_refs_2026-07-23.ris`). The RIS follows established Mendeley conventions with native Unicode author names, one author per line, and DOIs included only where deterministic. Three entries (Gross–Wilczek, Politzer, 't Hooft naturalness) were flagged as potential duplicates to check on import if the asymptotic freedom material already cited them under other keys.

## Transcript

### 1. human  ·  2026-07-22 20:31:05

We have been working on finding the common structures in entanglement and particle physics. So far we've used that to deduce free parameters of the Standard Model. The flow has been one way, but it must be possible to take knowledge about the Standard Model and use it to solve problems in multi-particle entanglement. 

Think deeply about that and come up with some ideas. They don't need to be fully formed ideas, hazy guesses we can work on can be included in the list

We have been working on finding the common structures in entanglement and particle physics. So far we've used that to deduce free parameters of the Standard Model. The flow has been one way, but it must be possible to take knowledge about the Standard Model and use it to solve problems in multi-particle entanglement. 

Think deeply about that and come up with some ideas. They don't need to be fully formed ideas, hazy guesses we can work on can be included in the list

### 2. assistant  ·  2026-07-22 20:36:04


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Inverting the arrow is the right instinct, and there's a discipline worth fixing at the outset: the reverse flow is most valuable where the SM fact is *empirically secure but framework-underived* (confinement dynamics, running couplings, CP magnitude, dark sector), because there the dictionary converts hard data into genuinely new conjectures in entanglement theory. Where the framework has already derived the SM fact (three-ness, hypercharge, sin²θ_W), the reverse reading collapses into a consistency check — still useful, but not new information. I'll tag the circularity risk per item. Here's the list, roughly ordered from computable to hazy:

1. **An entanglement string tension.** The kinematic side of confinement is proved (GHZ confinement theorem, zero budget slack). The dynamical side — string breaking, hadronisation, pair creation when you pull quarks apart — has never been translated. Conjecture: any LOCC protocol attempting to isolate one party of a GHZ-class state either fails or *generates new GHZ triples*, with a resource cost scaling linearly in operational separation (circuit distance, intervening FANOUTs) — a string tension for entanglement extraction. First step: define separation operationally and cost out the best-known extraction protocols looking for linear scaling. Status: CANDIDATE; non-circular (the framework has kinematic confinement, not the dynamics).

2. **Anomaly cancellation as sum rules on closed circuits.** The SM's anomaly conditions (ΣY = ΣY³ = 0 per generation) are consistency constraints on which charges may *coexist*. Pulled back: a closed reversible network's state, decomposed into Coecke–Kissinger primitives, should satisfy sum rules over class-invariants of the coexisting components — a "no anomalous ensembles" theorem, a genuinely new constraint type in entanglement theory. 't Hooft anomaly matching then says these sums are preserved under blocking/coarse-graining, which is exactly the kind of LOCC-and-RG-protected invariant the many-body community wants for classifying phases. First step: hunt for conserved combinations on small closed ZX diagrams numerically. Partially circular via the hypercharge derivation, but the closed-circuit sum-rule form is new.

3. **Beta functions as predictions for entanglement renormalisation.** Asymptotic freedom is an open problem in the framework, so this direction is clean. The measured b₀ = 11 − 2n_f/3 should predict how three-tangle density flows under successive blocking steps in a MERA or random-circuit coarse-graining — logarithmic running with a computable coefficient. This is checkable in existing tensor-network numerics and might feed back into `open_problem_asymptotic_freedom.md` from the other end.

4. **The mass functional as the canonical multipartite monotone.** Multipartite entanglement famously lacks an agreed measure. The geodesic-distance mass functional is a specific functional on states with a physically calibrated spectrum (the Yukawas). Conjecture: it is, or tightly bounds, an entanglement monotone under LOCC. First step is cheap: a PASS/FAIL numerical monotonicity check on random states and random LOCC maps. If it passes, entanglement theory acquires a preferred measure with experimental calibration — a striking export.

5. **Quantum numbers as a generating family of invariants.** τ₃ already functions as the colour-charge indicator (1 for GHZ, 0 for W). Extend systematically: each SM quantum number should pull back to a computable invariant, and *charge quantisation* becomes the prediction that these invariants have discrete spectra on physical classes. The natural home is entanglement polytopes (Klyachko; Walter–Doran–Gross–Christandl): one-body marginal spectra ↔ single-particle quantum numbers, so the SM's rigid charge assignments predict specific vertex structure for higher-n polytopes. Status: RHYME with a concrete computation attached.

6. **Flavour data as a measured chart of the four-qubit landscape.** This inverts your existing Conjecture 1. Rather than deriving mixing from the AME deficit, use the *measured* Wolfenstein hierarchy and PMNS angles as precision experimental data *about* the geometry of the four-qubit SLOCC landscape near the Higuchi–Sudbery frustration optimum — locating which of the nine Verstraete families nature's tag state occupies, whose known invariants then become predictions. Flavour physics as the world's most precisely measured four-qubit experiment. Non-circular provided the angles enter as empirical inputs.

7. **The Jarlskog quartic as the canonical imaginarity monotone.** δ_CP is underived (the §7 phase construction is open), so the flow is clean: J's rephasing-invariant quartic structure suggests the natural conjugation-sensitive invariant for four-partite states, connecting directly to the recent resource theory of imaginarity (Hickey–Gour; Wu et al.). Conjecture: the maximal "entanglement chirality" of physical four-qubit configurations is bounded by max J = 1/(6√3). This also gives the outstanding chirality lemma a second front to attack from.

8. **Electroweak decoherence spectroscopy.** The photon is the unbroken massless combination; the Z the broken massive one; mass-as-debt already reads debt as fragility. Reverse: the two orthogonal correlation combinations at the ℂ⊗ℍ level should show systematically different robustness under decoherence — one near-protected mode, one decaying, with rate ratio tied to 1/cos θ_W. This is a fez notebook: prepare the quartet structure, track both combinations under native noise, uncommissioned-harvest style. Status: hazy RHYME until the mass→rate mechanism is written, but the hardware test is cheap.

9. **Bound entanglement as the gauge-blind sector.** Gauge bosons are Bell-class edges; distillable entanglement is precisely extractable-Bell-pair content, i.e. gauge-visible correlation. Bound entanglement (PPT-entangled, undistillable) is then correlated matter with no gauge edge available — structurally dark, converging on Paper 4's relational solitons from the entanglement side. Reverse flow proper: dark-sector phenomenology (abundance, self-interaction bounds, portal activation) predicts large-N behaviour of bound entanglement — genericity, activation phenomena. First step: a literature pass on the measure of bound-entangled states as party number grows.

10. **A confining sector as a self-correcting quantum memory.** Read confinement plus the mass gap as code properties: logical information lives in the singlet (gauge-invariant) sector, non-singlet errors are gap-penalised, and the logical operators are the colour-singlet composites — baryon as a weight-three GHZ composite, meson as GHZ with its conjugate. Conjecture: the dictionary image of a confining sector is a finite-temperature self-correcting memory below the gap scale, attacking a famous open question (self-correction below four dimensions) from the SM side. Very hazy, but it says exactly where to look: GHZ-primitive networks under the budget-saturation constraint.

11. **Broadcastable content = invariant ring of the class stabiliser.** Confinement's operational face is that only singlet combinations get classically recorded; the Jaynes resolution already established broadcastable content as an invariant ring for the phase action. Generalise: the FANOUT-broadcastable content of *any* multipartite class is exactly the invariant ring of its stabiliser — a class-by-class refinement of the no-broadcasting and local-broadcasting theorems, with quark observables as the motivating instance. First step: state and prove it for GHZ, where the stabiliser is explicit, and check against quantum Darwinism results.

12. **SM vertices as a preferred gate set.** There's already a beachhead in the literature you should claim kinship with: Beane, Kaplan, Klco and Savage showed low-energy QCD scattering *minimises* entanglement generation, correlating with emergent Wigner symmetry — the community discovering the reverse flow empirically. The framework can systematise it: the dictionary images of the SM vertices form a small universal gate library whose entangling powers should sit at derived values (functions of 2/9, 1/4). Computing the entangling power of the vertex gates is an afternoon's numerics.

13. **Symmetry breaking as a measurement-induced phase transition.** Measurement-induced phase transitions are among the hottest open areas in multi-particle entanglement, and FANOUT density is the framework's native tuning parameter. Hazy guess: the SM's breaking pattern (SU(2)×U(1) → U(1)) predicts the order-parameter structure of the transition — condensation of the product class (Higgs) with a residual unbroken correlation subgroup — and possibly a critical FANOUT density expressible in framework constants. This is the haziest item on the list, but it points the framework at a community actively looking for organising principles.

For triage: items 4, 2 and 12 have same-day PASS/FAIL numerics; item 8 is the natural next hardware notebook; items 1 and 11 are the ones I'd draft as open-problem documents in the Heunen style, since each has a crisp theorem-shaped target. Tell me which you'd like worked up first and I'll produce the document with explicit pass/fail criteria.

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

Inverting the arrow is the right instinct, and there's a discipline worth fixing at the outset: the reverse flow is most valuable where the SM fact is *empirically secure but framework-underived* (confinement dynamics, running couplings, CP magnitude, dark sector), because there the dictionary converts hard data into genuinely new conjectures in entanglement theory. Where the framework has already derived the SM fact (three-ness, hypercharge, sin²θ_W), the reverse reading collapses into a consistency check — still useful, but not new information. I'll tag the circularity risk per item. Here's the list, roughly ordered from computable to hazy:

1. **An entanglement string tension.** The kinematic side of confinement is proved (GHZ confinement theorem, zero budget slack). The dynamical side — string breaking, hadronisation, pair creation when you pull quarks apart — has never been translated. Conjecture: any LOCC protocol attempting to isolate one party of a GHZ-class state either fails or *generates new GHZ triples*, with a resource cost scaling linearly in operational separation (circuit distance, intervening FANOUTs) — a string tension for entanglement extraction. First step: define separation operationally and cost out the best-known extraction protocols looking for linear scaling. Status: CANDIDATE; non-circular (the framework has kinematic confinement, not the dynamics).

2. **Anomaly cancellation as sum rules on closed circuits.** The SM's anomaly conditions (ΣY = ΣY³ = 0 per generation) are consistency constraints on which charges may *coexist*. Pulled back: a closed reversible network's state, decomposed into Coecke–Kissinger primitives, should satisfy sum rules over class-invariants of the coexisting components — a "no anomalous ensembles" theorem, a genuinely new constraint type in entanglement theory. 't Hooft anomaly matching then says these sums are preserved under blocking/coarse-graining, which is exactly the kind of LOCC-and-RG-protected invariant the many-body community wants for classifying phases. First step: hunt for conserved combinations on small closed ZX diagrams numerically. Partially circular via the hypercharge derivation, but the closed-circuit sum-rule form is new.

3. **Beta functions as predictions for entanglement renormalisation.** Asymptotic freedom is an open problem in the framework, so this direction is clean. The measured b₀ = 11 − 2n_f/3 should predict how three-tangle density flows under successive blocking steps in a MERA or random-circuit coarse-graining — logarithmic running with a computable coefficient. This is checkable in existing tensor-network numerics and might feed back into `open_problem_asymptotic_freedom.md` from the other end.

4. **The mass functional as the canonical multipartite monotone.** Multipartite entanglement famously lacks an agreed measure. The geodesic-distance mass functional is a specific functional on states with a physically calibrated spectrum (the Yukawas). Conjecture: it is, or tightly bounds, an entanglement monotone under LOCC. First step is cheap: a PASS/FAIL numerical monotonicity check on random states and random LOCC maps. If it passes, entanglement theory acquires a preferred measure with experimental calibration — a striking export.

5. **Quantum numbers as a generating family of invariants.** τ₃ already functions as the colour-charge indicator (1 for GHZ, 0 for W). Extend systematically: each SM quantum number should pull back to a computable invariant, and *charge quantisation* becomes the prediction that these invariants have discrete spectra on physical classes. The natural home is entanglement polytopes (Klyachko; Walter–Doran–Gross–Christandl): one-body marginal spectra ↔ single-particle quantum numbers, so the SM's rigid charge assignments predict specific vertex structure for higher-n polytopes. Status: RHYME with a concrete computation attached.

6. **Flavour data as a measured chart of the four-qubit landscape.** This inverts your existing Conjecture 1. Rather than deriving mixing from the AME deficit, use the *measured* Wolfenstein hierarchy and PMNS angles as precision experimental data *about* the geometry of the four-qubit SLOCC landscape near the Higuchi–Sudbery frustration optimum — locating which of the nine Verstraete families nature's tag state occupies, whose known invariants then become predictions. Flavour physics as the world's most precisely measured four-qubit experiment. Non-circular provided the angles enter as empirical inputs.

7. **The Jarlskog quartic as the canonical imaginarity monotone.** δ_CP is underived (the §7 phase construction is open), so the flow is clean: J's rephasing-invariant quartic structure suggests the natural conjugation-sensitive invariant for four-partite states, connecting directly to the recent resource theory of imaginarity (Hickey–Gour; Wu et al.). Conjecture: the maximal "entanglement chirality" of physical four-qubit configurations is bounded by max J = 1/(6√3). This also gives the outstanding chirality lemma a second front to attack from.

8. **Electroweak decoherence spectroscopy.** The photon is the unbroken massless combination; the Z the broken massive one; mass-as-debt already reads debt as fragility. Reverse: the two orthogonal correlation combinations at the ℂ⊗ℍ level should show systematically different robustness under decoherence — one near-protected mode, one decaying, with rate ratio tied to 1/cos θ_W. This is a fez notebook: prepare the quartet structure, track both combinations under native noise, uncommissioned-harvest style. Status: hazy RHYME until the mass→rate mechanism is written, but the hardware test is cheap.

9. **Bound entanglement as the gauge-blind sector.** Gauge bosons are Bell-class edges; distillable entanglement is precisely extractable-Bell-pair content, i.e. gauge-visible correlation. Bound entanglement (PPT-entangled, undistillable) is then correlated matter with no gauge edge available — structurally dark, converging on Paper 4's relational solitons from the entanglement side. Reverse flow proper: dark-sector phenomenology (abundance, self-interaction bounds, portal activation) predicts large-N behaviour of bound entanglement — genericity, activation phenomena. First step: a literature pass on the measure of bound-entangled states as party number grows.

10. **A confining sector as a self-correcting quantum memory.** Read confinement plus the mass gap as code properties: logical information lives in the singlet (gauge-invariant) sector, non-singlet errors are gap-penalised, and the logical operators are the colour-singlet composites — baryon as a weight-three GHZ composite, meson as GHZ with its conjugate. Conjecture: the dictionary image of a confining sector is a finite-temperature self-correcting memory below the gap scale, attacking a famous open question (self-correction below four dimensions) from the SM side. Very hazy, but it says exactly where to look: GHZ-primitive networks under the budget-saturation constraint.

11. **Broadcastable content = invariant ring of the class stabiliser.** Confinement's operational face is that only singlet combinations get classically recorded; the Jaynes resolution already established broadcastable content as an invariant ring for the phase action. Generalise: the FANOUT-broadcastable content of *any* multipartite class is exactly the invariant ring of its stabiliser — a class-by-class refinement of the no-broadcasting and local-broadcasting theorems, with quark observables as the motivating instance. First step: state and prove it for GHZ, where the stabiliser is explicit, and check against quantum Darwinism results.

12. **SM vertices as a preferred gate set.** There's already a beachhead in the literature you should claim kinship with: Beane, Kaplan, Klco and Savage showed low-energy QCD scattering *minimises* entanglement generation, correlating with emergent Wigner symmetry — the community discovering the reverse flow empirically. The framework can systematise it: the dictionary images of the SM vertices form a small universal gate library whose entangling powers should sit at derived values (functions of 2/9, 1/4). Computing the entangling power of the vertex gates is an afternoon's numerics.

13. **Symmetry breaking as a measurement-induced phase transition.** Measurement-induced phase transitions are among the hottest open areas in multi-particle entanglement, and FANOUT density is the framework's native tuning parameter. Hazy guess: the SM's breaking pattern (SU(2)×U(1) → U(1)) predicts the order-parameter structure of the transition — condensation of the product class (Higgs) with a residual unbroken correlation subgroup — and possibly a critical FANOUT density expressible in framework constants. This is the haziest item on the list, but it points the framework at a community actively looking for organising principles.

For triage: items 4, 2 and 12 have same-day PASS/FAIL numerics; item 8 is the natural next hardware notebook; items 1 and 11 are the ones I'd draft as open-problem documents in the Heunen style, since each has a crisp theorem-shaped target. Tell me which you'd like worked up first and I'll produce the document with explicit pass/fail criteria.

### 3. human  ·  2026-07-23 05:04:37

This should be included in the paper as an appendix. The objective is not to solve them but to leave them as interesting areas for other people to explore. Not even well posed open problems, just areas that might be worth exploring. So write them up with that in mind and add references

This should be included in the paper as an appendix. The objective is not to solve them but to leave them as interesting areas for other people to explore. Not even well posed open problems, just areas that might be worth exploring. So write them up with that in mind and add references

### 4. assistant  ·  2026-07-23 05:13:59


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

Both files are in the outputs. What was done and how it was verified:

**The appendix** (`appendix_reverse_flow_2026-07-23.tex`) carries thirteen areas plus a two-paragraph preamble and a coda, written to the brief: nothing is posed, the `openproblem` environment is deliberately not used, and the preamble says so explicitly. The preamble also states the circularity discipline in the open — where the paper derives a Standard-Model fact, the reverse reading is only a consistency check, so the appendix leans on the underived facts (confinement dynamics, running couplings, CP magnitude, the dark sector) as its generators. The coda frames the whole thing as an invitation and asks readers to report failures as well as successes.

Three deliberate structural choices worth flagging. First, there are *no* internal `\ref`s to main-text labels — everything is referred to in words ("the budget-saturation constraint of the main text", "the companion programme flagged in the interactions section") — so this splice carries zero label-mapping debt, unlike the Jaynes appendix. Second, an optional one-sentence main-body insert for the conclusions is included as a comment block at the top. Third, it follows the `appendix_ghz_w_proofs` usage convention: plain `\section`, to be `\input` inside the existing appendices wrapper:

```latex
\input{appendix_reverse_flow_2026-07-23}
```

**Verification.** The splice compiles clean (exit 0, six pages) under a minimal driver. One honest caveat: this container has pdflatex but no biblatex/biber, so the compile test used an `\autocite` shim — syntax, maths and brace structure are exercised, but biber itself ran only in the sense of the key cross-check below; the Overleaf build is the real test. The tex is pure ASCII (grep-verified). A PASS/FAIL script confirmed all 28 citation keys resolve: 6 reused from your library (`coeckekissinger2010compositional`, `durvidalcirac2000three`, `coffmankunduwootters2000`, `higuchisudbery2000`, `hubersiewert2026`, `gillardgresnigt2019three` — the first three verified against the master section file's actual `\autocite`s, the last three against the fourth-qubit doc), and all 22 new keys have matching `ID` fields in the `.ris`, with no orphans.

**The RIS** follows the Mendeley conventions: native Unicode (Düssel, Guifré, Paweł, Życzkowski), one author per `AU` line, citation key in `ID`. DOIs are included only where deterministic (APS pattern, plus Dennis et al. and the Science polytopes paper); omitted where I wasn't certain, since a wrong DOI corrupts the import worse than a missing one. Three entries to dedupe-check on import: `grosswilczek1973ultraviolet`, `politzer1973reliable` and `thooft1980naturalness` may already exist under other keys if the asymptotic-freedom material cited them.

One editorial judgement you may want to reverse: I kept Zurek's quantum Darwinism and the Dür–Vidal–Cirac/Coecke–Kissinger staples cited only where load-bearing, referring to Darwinism by name alone since the main text will already carry its key — if you'd rather re-cite it in the broadcast subsection, it's a one-key addition.

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

*[tool_use: create_file]*

*[tool_result: create_file]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: present_files]*

*[tool_result: present_files]*

Both files are in the outputs. What was done and how it was verified:

**The appendix** (`appendix_reverse_flow_2026-07-23.tex`) carries thirteen areas plus a two-paragraph preamble and a coda, written to the brief: nothing is posed, the `openproblem` environment is deliberately not used, and the preamble says so explicitly. The preamble also states the circularity discipline in the open — where the paper derives a Standard-Model fact, the reverse reading is only a consistency check, so the appendix leans on the underived facts (confinement dynamics, running couplings, CP magnitude, the dark sector) as its generators. The coda frames the whole thing as an invitation and asks readers to report failures as well as successes.

Three deliberate structural choices worth flagging. First, there are *no* internal `\ref`s to main-text labels — everything is referred to in words ("the budget-saturation constraint of the main text", "the companion programme flagged in the interactions section") — so this splice carries zero label-mapping debt, unlike the Jaynes appendix. Second, an optional one-sentence main-body insert for the conclusions is included as a comment block at the top. Third, it follows the `appendix_ghz_w_proofs` usage convention: plain `\section`, to be `\input` inside the existing appendices wrapper:

```latex
\input{appendix_reverse_flow_2026-07-23}
```

**Verification.** The splice compiles clean (exit 0, six pages) under a minimal driver. One honest caveat: this container has pdflatex but no biblatex/biber, so the compile test used an `\autocite` shim — syntax, maths and brace structure are exercised, but biber itself ran only in the sense of the key cross-check below; the Overleaf build is the real test. The tex is pure ASCII (grep-verified). A PASS/FAIL script confirmed all 28 citation keys resolve: 6 reused from your library (`coeckekissinger2010compositional`, `durvidalcirac2000three`, `coffmankunduwootters2000`, `higuchisudbery2000`, `hubersiewert2026`, `gillardgresnigt2019three` — the first three verified against the master section file's actual `\autocite`s, the last three against the fourth-qubit doc), and all 22 new keys have matching `ID` fields in the `.ris`, with no orphans.

**The RIS** follows the Mendeley conventions: native Unicode (Düssel, Guifré, Paweł, Życzkowski), one author per `AU` line, citation key in `ID`. DOIs are included only where deterministic (APS pattern, plus Dennis et al. and the Science polytopes paper); omitted where I wasn't certain, since a wrong DOI corrupts the import worse than a missing one. Three entries to dedupe-check on import: `grosswilczek1973ultraviolet`, `politzer1973reliable` and `thooft1980naturalness` may already exist under other keys if the asymptotic-freedom material cited them.

One editorial judgement you may want to reverse: I kept Zurek's quantum Darwinism and the Dür–Vidal–Cirac/Coecke–Kissinger staples cited only where load-bearing, referring to Darwinism by name alone since the main text will already carry its key — if you'd rather re-cite it in the broadcast subsection, it's a one-key addition.
