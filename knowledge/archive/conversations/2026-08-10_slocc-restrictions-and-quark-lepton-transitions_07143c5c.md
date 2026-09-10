# SLOCC restrictions and quark-lepton transitions

- conversation uuid: `07143c5c-f61a-444f-8189-a3efea9ae9a3`
- created: 2026-08-10T20:50:44.211851Z  |  updated: 2026-08-10T21:35:34.684824Z
- messages: 4  |  keyword score: 4

## Summary (from the Claude export)

**Conversation overview**

The person is developing a theoretical physics framework that maps quantum information structures (SLOCC classification of entanglement classes) onto particle physics, with octonions and division algebra providing the algebraic backbone. The conversation began with two speculative ideas: whether the muon g−2 anomaly might signal a sterile neutrino or whether SLOCC restrictions between GHZ and W states might be softened by an "associator debt" (identified with mass), permitting some quark-lepton mixing. Claude provided a ground-truth update that the g−2 anomaly has largely dissolved as of 2025–2026 due to lattice QCD reconciliation, then worked through both ideas experimentally as requested — tracing why each fails as an anomaly explanation while extracting what survives as structurally useful content.

From idea 1, the framework's exclusion of all popular beyond-Standard-Model explanations (SUSY, leptoquarks, dark photon, sterile neutrinos via g−2) was identified as a falsifiable structural commitment: the framework bets fully on the lattice HVP result, and a resurgent anomaly would falsify it. From idea 2, the associator/octonion cross-split structure was shown to correctly inventory the only equivariant doors between the colour sector and the record plane (the meson door via δ and the baryon door via ε), reproducing confinement from Schur's lemma. This led to the person asking whether "no leptoquarks" could be formalised as a theorem.

The session concluded with Claude drafting, compiling, and verifying a full LaTeX splice (`no_leptoquark_theorem_2026-08-10T2131.tex`) containing two supporting lemmas (Colour Doors, Fermion Parity), a corollary (Colour Triality), and the No Leptoquark Theorem itself, conditional on four explicitly stated premises (equivariance, sector populations, inventory completeness, spin-statistics). A key finding was that the theorem closes all trilinear vertices but cannot reach the quartic ε(qqq)ℓ structure, which was quarantined as open problem **op:baryon-contact** — deciding proton stability — with explicit PASS/FAIL criteria tied to the Hopf–Frobenius machinery of the existing open problem op:heunen-functor. Four new bibliography keys were delivered in a companion RIS file with VERIFY-CITE flags. The person's working style involves rigorous house conventions: dated filenames, sentinel-gated compilation before delivery, status labels (ESTABLISHED, STRUCTURAL, OPEN), explicit ledger entries for invalid routes, and VERIFY-KEY/VERIFY-CITE flags on all new references.

## Transcript

### 1. human  ·  2026-08-10 20:50:45

here's some crazy ideas. SLOCC restrictions prevent GHZ states being changed into W states and vice-versa. This maps to there being nothing that can turn a quark into a lepton and vice-versa

Calculating the g-2 discrepancy in muon magnetic moment relies on our understanding of the hadron sector because the mass of the muon means that more massive virtual particles, including hadrons have to be included in the calculation, and this involves a deeper understanding of the quark sector. Typically people do calculations using lattice QCD. And there is  discrepancy which either hints at new physics beyond the SM or a failure in our calculation methods. 

I'm wondering (1) if this discrepancy might be a sign of the sterile neutrino where we've estimated a max in the TeV range or (2) maybe the SLOCC restriction isn't as certain as we think and the associator debt, which we identify as mass, might permit some transitions between GHZ and W and therefore some mixing between quarks and leptons. 

Both ideas could be wrong, but thinking about them might yield interesting angles in the framework by working out why they're wrong. Or they might even be right. 

Be experimental in your thinking and tell me what thoughts these ideas prompt in your mind

here's some crazy ideas. SLOCC restrictions prevent GHZ states being changed into W states and vice-versa. This maps to there being nothing that can turn a quark into a lepton and vice-versa

Calculating the g-2 discrepancy in muon magnetic moment relies on our understanding of the hadron sector because the mass of the muon means that more massive virtual particles, including hadrons have to be included in the calculation, and this involves a deeper understanding of the quark sector. Typically people do calculations using lattice QCD. And there is  discrepancy which either hints at new physics beyond the SM or a failure in our calculation methods. 

I'm wondering (1) if this discrepancy might be a sign of the sterile neutrino where we've estimated a max in the TeV range or (2) maybe the SLOCC restriction isn't as certain as we think and the associator debt, which we identify as mass, might permit some transitions between GHZ and W and therefore some mixing between quarks and leptons. 

Both ideas could be wrong, but thinking about them might yield interesting angles in the framework by working out why they're wrong. Or they might even be right. 

Be experimental in your thinking and tell me what thoughts these ideas prompt in your mind

### 2. assistant  ·  2026-08-10 20:58:10

Before running with these, let me make sure we're standing on the current experimental ground — the g-2 story changed substantially in 2025.
```
This block is not supported on your current device yet.
```

First, a ground-truth update that matters for both ideas: the anomaly you're describing has largely dissolved since 2025. The Theory Initiative's 2025 White Paper moved from the data-driven HVP to lattice QCD, publishing a_μ = (116 592 033 ± 62) × 10⁻¹¹ — statistically incompatible with its own 2020 prediction at ~3σ, and now compatible with Fermilab's final measurement at well under 1σ. An April 2026 Nature paper (Borsanyi, Fodor et al.) sharpened the lattice HVP to 0.48%, bringing theory and experiment into near-perfect agreement. The live tension is no longer SM-vs-experiment; it's *internal to the hadronic sector* — CMD-3's e⁺e⁻→π⁺π⁻ cross-section is incompatible with the two most precise previous measurements, calling the data-driven method's systematics into question, and MUonE began taking data in 2025 as a third independent HVP determination, with competitive results not expected before 2027.

So both your ideas are now answers to a question the data has mostly withdrawn. But you asked me to work out *why* they're wrong and see what falls out, and quite a lot does.

**Idea 1 (sterile neutrino in g−2).** This fails on three independent grounds, which is worth recording precisely. Timing: the anomaly is gone. Sign: a heavy neutral lepton entering through W-loop mixing *lowers* a_μ relative to the SM — the old anomaly was experiment *above* theory, so steriles pushed the wrong way even when there was something to explain. Magnitude: the contribution scales as ~(G_F m_μ²/8√2π²)|U_μN|², so with EW-precision-allowed mixing you get |Δa_μ| ≲ 10⁻¹² — three orders below the old discrepancy, and invisible even in the current ~(4±6)×10⁻¹⁰ residual. The standard escape routes (chirality-flip enhancement via new scalars, extra gauge bosons) are exactly the structures your tower forbids.

But here's what survives, and it's sharper than the original idea: **the framework has systematically excluded every popular explanation of a g−2 excess** — no SUSY smuons, no leptoquarks (see below), no extra U(1)/dark photon because the gauge group is closed by the tower, no axion, no extra dimensions, and steriles too heavy and too weakly mixed to matter. The framework therefore *bets everything on WP25 being right*. If MUonE or a BaBar/KLOE reconciliation resurrects the data-driven HVP and the anomaly returns at 5σ, the framework has nowhere to hide — it cannot supply 25×10⁻¹⁰ from anything in its inventory. I'd label this a Structural consequence and I think it belongs somewhere in Paper 1's falsifiability discussion: it's a clean, honest, near-term-testable commitment that costs nothing if WP25 holds. Separately, the *actual* experimental handle on your 3.6 TeV steriles is charged lepton flavour violation, not g−2: with the PMNS structure and m₁=0 fixed, μ→eγ and μ→e conversion rates should be computable rather than free — a Notebook-shaped task for later.

**Idea 2 (associator softening SLOCC).** This one is generative. Let me first tighten your opening mapping, then push on it.

A pleasing tightening: the SLOCC group for three qubits is SL(2,ℂ)^×3 — and SL(2,ℂ) is precisely the group you've already identified with measurement-as-boost. So "particle type is a SLOCC invariant" reads, framework-internally, as "quark-ness/lepton-ness is invariant under local boosts and measurement-tippings" — the type label is Lorentz-scalar for structural reasons, not by stipulation. The invariant that does the separating is Cayley's hyperdeterminant (the 3-tangle): τ≠0 on GHZ, τ≡0 on the W stratum.

But the naive mapping needs two corrections before it can bear weight. First, the Dür–Vidal–Cirac structure is *asymmetric*: W lies in the closure of the GHZ orbit (reachable asymptotically, with diverging SLOCC operators and vanishing success probability), while GHZ is unreachable from W even in the limit, because τ is continuous and vanishes on the whole W-orbit closure. Second, "nothing turns quarks into leptons" cannot mean "no process with quarks in and leptons out" — Drell–Yan (qq̄ → ℓ⁺ℓ⁻) happens at every collider. That's GHZ ⊗ GHZ̄ composing through a Bell channel and decomposing into W ⊗ W̄ — cups and caps, not orbit maps. The invariant content is about *single-channel* conversion: ΔB ≠ 0, the leptoquark vertex. Pair-composition through the boson sector is always allowed; type-morphism on one leg is what's at stake.

Now the CPT block, which kills the strong form of the idea and should be recorded as an invalid route so we don't retry it. Suppose the closure asymmetry were promoted to a dynamical selection rule: q→ℓ allowed as a boundary limit, ℓ→q strictly forbidden. CPT relates any amplitude with a quark in and a lepton out to one with an antilepton in and an antiquark out, with equal modulus. Both GHZ and W classes are closed under complex conjugation, so CPT preserves type labels. Hence: either both conversion directions vanish, or both exist with equal suppression. A one-way rule violates CPT. The orbit-closure asymmetry is therefore *kinematic stratification* — which degenerations are continuous in state space — and can shape suppression structure (symmetrically), but cannot be an arrow.

With the strong form dead, here's where your associator instinct turns out to be *right in a way you didn't quite say*. Work in the ℓ-split 𝕆 ≅ ℂ_ℓ ⊕ ℂ³ and just do the SU(3) representation arithmetic. Leptons live in the record plane: SU(3)-singlets. Quarks are the 3. The octonion multiplication and associator, restricted across the split, are SU(3)_ℓ-equivariant maps, and Schur's lemma inventories the doors completely: Hom(3⊗3̄, 1) = ℂ (the hermitian pairing — colour–anticolour into the record plane: the *meson door*), Hom(3⊗3, 3̄) = ℂ (the ε-tensor — diquark into anticolour, whence 3⊗3⊗3 → 1: the *baryon door*), and Hom(3, 1) = 0. So the nonassociative structure absolutely does connect the sectors — but *only through colour-singlet composites*. Your existing statement "confinement = impossibility of incomplete classical record" is exactly this Hom-space arithmetic made physical. And the missing map, Hom(3,1) = 0, is the no-leptoquark statement. GUTs evade it by enlarging the gauge sector with coloured mediators to carry the 3 away; the tower termination says the shop is shut. So idea 2, pursued honestly, (a) rederives confinement from Schur's lemma, and (b) yields a new named structural exclusion — **no leptoquarks, at any scale** — falsifiable at the LHC, and it upgrades the physical payoff of op:heunen-functor: if the Hopf–Frobenius machinery shows the only admissible GHZ–W morphisms are Bell-composition and ε-contraction, "no leptoquarks" becomes theorem-shaped.

Two further threads worth logging. The hyperdeterminant that separates the classes is, via the Freudenthal triple system construction, built from the Jordan determinant of J₃ — the same object organising your mass structures. Borsten, Duff and Lévay's black-hole/qubit correspondence literature is the existing bridge between three-qubit SLOCC invariants and Freudenthal/Jordan algebra, and Lévay separately wrote on Hopf fibrations and entanglement geometry — possibly useful ammunition for op:ideal-orbit. So mass and class-membership are algebraic cousins: your instinct that the associator debt "knows about" the GHZ/W boundary is correct. The associator can *measure* the wall; it cannot open it.

And a RHYME, clearly labelled as such: "W reachable from GHZ only via diverging operators with vanishing probability" smells like sphaleron-mediated B+L violation — finite barrier (~9 TeV), exponentially suppressed at zero temperature, a boundary-crossing rather than a perturbative vertex. But the CPT argument above means the correspondence, if real, must be direction-symmetric, and it raises an uncomfortable flag: if cross-stratum conversion is *exactly* zero rather than sphaleron-suppressed, the framework quietly forbids leptogenesis, and the baryon asymmetry must originate in the GHZ sector directly or at channel-creation. That's an open cosmological liability worth a line in the ledger.

Proposed ledger entries, statuses per house rules:

1. **lem:associator-doors** (CANDIDATE, derivable): the only SU(3)_ℓ-equivariant maps between ℂ³ and ℂ_ℓ sectors are the pairing (meson door) and ε-contraction (baryon door); corollary Hom(3,1)=0 ⇒ no leptoquark channel. Feeds op:heunen-functor.
2. **Invalid route (recorded)**: directional q→ℓ selection rule from SLOCC orbit-closure asymmetry — blocked by CPT.
3. **Structural consequence**: framework predicts a_μ(exp) = a_μ(SM); commits fully to the lattice HVP; falsified if the data-driven anomaly returns.
4. **RHYME flags**: orbit-boundary crossing ↔ sphalerons (direction-symmetric only); baryogenesis-without-leptogenesis liability; Euclidean-lattice-as-imaginary-time computing the colour sector, adjacent to your imaginary-temperature clause.
5. **op candidate**: sterile-sector LFV rates (μ→eγ, μ→e conversion) from the fixed PMNS/mass structure — the real experimental window on the 3.6 TeV states.

The pattern across both ideas: they were wrong as anomaly-explanations, but each one, worked through, converted a vague permission ("maybe mixing is possible") into a sharp prohibition with a falsifier attached. That's the framework behaving well.

Before running with these, let me make sure we're standing on the current experimental ground — the g-2 story changed substantially in 2025.

*[tool_use: web_search]*

*[tool_result: web_search]*

First, a ground-truth update that matters for both ideas: the anomaly you're describing has largely dissolved since 2025. The Theory Initiative's 2025 White Paper moved from the data-driven HVP to lattice QCD, publishing a_μ = (116 592 033 ± 62) × 10⁻¹¹ — statistically incompatible with its own 2020 prediction at ~3σ, and now compatible with Fermilab's final measurement at well under 1σ. An April 2026 Nature paper (Borsanyi, Fodor et al.) sharpened the lattice HVP to 0.48%, bringing theory and experiment into near-perfect agreement. The live tension is no longer SM-vs-experiment; it's *internal to the hadronic sector* — CMD-3's e⁺e⁻→π⁺π⁻ cross-section is incompatible with the two most precise previous measurements, calling the data-driven method's systematics into question, and MUonE began taking data in 2025 as a third independent HVP determination, with competitive results not expected before 2027.

So both your ideas are now answers to a question the data has mostly withdrawn. But you asked me to work out *why* they're wrong and see what falls out, and quite a lot does.

**Idea 1 (sterile neutrino in g−2).** This fails on three independent grounds, which is worth recording precisely. Timing: the anomaly is gone. Sign: a heavy neutral lepton entering through W-loop mixing *lowers* a_μ relative to the SM — the old anomaly was experiment *above* theory, so steriles pushed the wrong way even when there was something to explain. Magnitude: the contribution scales as ~(G_F m_μ²/8√2π²)|U_μN|², so with EW-precision-allowed mixing you get |Δa_μ| ≲ 10⁻¹² — three orders below the old discrepancy, and invisible even in the current ~(4±6)×10⁻¹⁰ residual. The standard escape routes (chirality-flip enhancement via new scalars, extra gauge bosons) are exactly the structures your tower forbids.

But here's what survives, and it's sharper than the original idea: **the framework has systematically excluded every popular explanation of a g−2 excess** — no SUSY smuons, no leptoquarks (see below), no extra U(1)/dark photon because the gauge group is closed by the tower, no axion, no extra dimensions, and steriles too heavy and too weakly mixed to matter. The framework therefore *bets everything on WP25 being right*. If MUonE or a BaBar/KLOE reconciliation resurrects the data-driven HVP and the anomaly returns at 5σ, the framework has nowhere to hide — it cannot supply 25×10⁻¹⁰ from anything in its inventory. I'd label this a Structural consequence and I think it belongs somewhere in Paper 1's falsifiability discussion: it's a clean, honest, near-term-testable commitment that costs nothing if WP25 holds. Separately, the *actual* experimental handle on your 3.6 TeV steriles is charged lepton flavour violation, not g−2: with the PMNS structure and m₁=0 fixed, μ→eγ and μ→e conversion rates should be computable rather than free — a Notebook-shaped task for later.

**Idea 2 (associator softening SLOCC).** This one is generative. Let me first tighten your opening mapping, then push on it.

A pleasing tightening: the SLOCC group for three qubits is SL(2,ℂ)^×3 — and SL(2,ℂ) is precisely the group you've already identified with measurement-as-boost. So "particle type is a SLOCC invariant" reads, framework-internally, as "quark-ness/lepton-ness is invariant under local boosts and measurement-tippings" — the type label is Lorentz-scalar for structural reasons, not by stipulation. The invariant that does the separating is Cayley's hyperdeterminant (the 3-tangle): τ≠0 on GHZ, τ≡0 on the W stratum.

But the naive mapping needs two corrections before it can bear weight. First, the Dür–Vidal–Cirac structure is *asymmetric*: W lies in the closure of the GHZ orbit (reachable asymptotically, with diverging SLOCC operators and vanishing success probability), while GHZ is unreachable from W even in the limit, because τ is continuous and vanishes on the whole W-orbit closure. Second, "nothing turns quarks into leptons" cannot mean "no process with quarks in and leptons out" — Drell–Yan (qq̄ → ℓ⁺ℓ⁻) happens at every collider. That's GHZ ⊗ GHZ̄ composing through a Bell channel and decomposing into W ⊗ W̄ — cups and caps, not orbit maps. The invariant content is about *single-channel* conversion: ΔB ≠ 0, the leptoquark vertex. Pair-composition through the boson sector is always allowed; type-morphism on one leg is what's at stake.

Now the CPT block, which kills the strong form of the idea and should be recorded as an invalid route so we don't retry it. Suppose the closure asymmetry were promoted to a dynamical selection rule: q→ℓ allowed as a boundary limit, ℓ→q strictly forbidden. CPT relates any amplitude with a quark in and a lepton out to one with an antilepton in and an antiquark out, with equal modulus. Both GHZ and W classes are closed under complex conjugation, so CPT preserves type labels. Hence: either both conversion directions vanish, or both exist with equal suppression. A one-way rule violates CPT. The orbit-closure asymmetry is therefore *kinematic stratification* — which degenerations are continuous in state space — and can shape suppression structure (symmetrically), but cannot be an arrow.

With the strong form dead, here's where your associator instinct turns out to be *right in a way you didn't quite say*. Work in the ℓ-split 𝕆 ≅ ℂ_ℓ ⊕ ℂ³ and just do the SU(3) representation arithmetic. Leptons live in the record plane: SU(3)-singlets. Quarks are the 3. The octonion multiplication and associator, restricted across the split, are SU(3)_ℓ-equivariant maps, and Schur's lemma inventories the doors completely: Hom(3⊗3̄, 1) = ℂ (the hermitian pairing — colour–anticolour into the record plane: the *meson door*), Hom(3⊗3, 3̄) = ℂ (the ε-tensor — diquark into anticolour, whence 3⊗3⊗3 → 1: the *baryon door*), and Hom(3, 1) = 0. So the nonassociative structure absolutely does connect the sectors — but *only through colour-singlet composites*. Your existing statement "confinement = impossibility of incomplete classical record" is exactly this Hom-space arithmetic made physical. And the missing map, Hom(3,1) = 0, is the no-leptoquark statement. GUTs evade it by enlarging the gauge sector with coloured mediators to carry the 3 away; the tower termination says the shop is shut. So idea 2, pursued honestly, (a) rederives confinement from Schur's lemma, and (b) yields a new named structural exclusion — **no leptoquarks, at any scale** — falsifiable at the LHC, and it upgrades the physical payoff of op:heunen-functor: if the Hopf–Frobenius machinery shows the only admissible GHZ–W morphisms are Bell-composition and ε-contraction, "no leptoquarks" becomes theorem-shaped.

Two further threads worth logging. The hyperdeterminant that separates the classes is, via the Freudenthal triple system construction, built from the Jordan determinant of J₃ — the same object organising your mass structures. Borsten, Duff and Lévay's black-hole/qubit correspondence literature is the existing bridge between three-qubit SLOCC invariants and Freudenthal/Jordan algebra, and Lévay separately wrote on Hopf fibrations and entanglement geometry — possibly useful ammunition for op:ideal-orbit. So mass and class-membership are algebraic cousins: your instinct that the associator debt "knows about" the GHZ/W boundary is correct. The associator can *measure* the wall; it cannot open it.

And a RHYME, clearly labelled as such: "W reachable from GHZ only via diverging operators with vanishing probability" smells like sphaleron-mediated B+L violation — finite barrier (~9 TeV), exponentially suppressed at zero temperature, a boundary-crossing rather than a perturbative vertex. But the CPT argument above means the correspondence, if real, must be direction-symmetric, and it raises an uncomfortable flag: if cross-stratum conversion is *exactly* zero rather than sphaleron-suppressed, the framework quietly forbids leptogenesis, and the baryon asymmetry must originate in the GHZ sector directly or at channel-creation. That's an open cosmological liability worth a line in the ledger.

Proposed ledger entries, statuses per house rules:

1. **lem:associator-doors** (CANDIDATE, derivable): the only SU(3)_ℓ-equivariant maps between ℂ³ and ℂ_ℓ sectors are the pairing (meson door) and ε-contraction (baryon door); corollary Hom(3,1)=0 ⇒ no leptoquark channel. Feeds op:heunen-functor.
2. **Invalid route (recorded)**: directional q→ℓ selection rule from SLOCC orbit-closure asymmetry — blocked by CPT.
3. **Structural consequence**: framework predicts a_μ(exp) = a_μ(SM); commits fully to the lattice HVP; falsified if the data-driven anomaly returns.
4. **RHYME flags**: orbit-boundary crossing ↔ sphalerons (direction-symmetric only); baryogenesis-without-leptogenesis liability; Euclidean-lattice-as-imaginary-time computing the colour sector, adjacent to your imaginary-temperature clause.
5. **op candidate**: sterile-sector LFV rates (μ→eγ, μ→e conversion) from the fixed PMNS/mass structure — the real experimental window on the 3.6 TeV states.

The pattern across both ideas: they were wrong as anomaly-explanations, but each one, worked through, converted a vague permission ("maybe mixing is possible") into a sharp prohibition with a falsifier attached. That's the framework behaving well.

### 3. human  ·  2026-08-10 21:24:29

'"no leptoquarks" becomes theorem-shaped' can we make that into a theorem then? I thought it was obvious from GHZ, W mechanics, and so not worth mentioning, but if it's easy to turn it into a theorem then it's a nice addition

'"no leptoquarks" becomes theorem-shaped' can we make that into a theorem then? I thought it was obvious from GHZ, W mechanics, and so not worth mentioning, but if it's easy to turn it into a theorem then it's a nice addition

### 4. assistant  ·  2026-08-10 21:35:34

Yes — and it's worth doing carefully, because when I sat down to enumerate the cases, the result is *not* entirely obvious: the cubic (renormalisable) level is a clean theorem, but the famous GUT proton-decay structure ε(qqq)ℓ survives both colour equivariance and spin-statistics, so it has to be quarantined as a named open problem rather than smuggled into the theorem. Let me check the notation and labels in the existing splices first so this one plugs in cleanly.
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

Sentinel gate passes: two pdflatex passes, zero errors, all references resolved, no overfull boxes. Now the RIS batch for the four new keys.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done, and compile-verified: two pdflatex passes, zero errors, all cross-references resolved (via stub anchors in the harness — the harness is not for the corpus, and its `\autocite` is stubbed, so ledger key spellings still need the usual check).

The structure that emerged is worth a word, because your instinct that it was "obvious" turns out to be true for one part and importantly false for another. The proof runs on three filters: colour triality (Corollary: invariants need quark-minus-antiquark legs ≡ 0 mod 3, a one-line consequence of the Weyl FFT door inventory), fermion parity (odd spinor legs admit no SL(2,ℂ) singlet), and inventory completeness (P3: no bosonic species carries the 3, so no mediator, scalar or vector). Those three close *every* trilinear vertex — that's the theorem, and it's the precise form of what you had in mind. But exactly one quark-number-violating structure passes all three filters: ε(qqq)ℓ, four spinor legs, colour singlet through the ε door — which is precisely the GUT proton-decay operator — together with its square, the n–n̄ oscillation structure. The mechanics you thought made it obvious genuinely cannot reach these, so they're quarantined as **op:baryon-contact** with PASS/FAIL criteria: PASS is a proof that no connected invariant diagram with three GHZ legs and one W leg exists (the hyperdeterminant flagged as candidate obstruction carrier), giving an absolutely stable proton and a falsifier; FAIL means computing the CPT-symmetric suppression and confronting the Super-K bound. Either way it lands squarely on the Hopf–Frobenius machinery, which raises the physical stakes of op:heunen-functor considerably — it now decides proton stability.

Statuses as installed: the two lemmas Established (classical), the theorem Structural conditional on P1–P4, with P4 (spin–statistics) flagged honestly as imported rather than derived — the Koszul-sign colour cube is noted as its natural future home. The SLOCC remark records this session's route: why the naive reading proves too much (Drell–Yan) and too little (CPT kills the orbit-closure arrow), so the invalid route stays retired.

For your verification pass: the external labels are listed in the header (all taken from the split splice and the GHZ/W appendix, but confirm `sec:canonical-orbits` lives where I think it does); `durvidalcirac2000` is VERIFY-KEY against the ledger; the four new keys (Weyl, Procesi, Takenaka/Super-K, Doršner et al.) are in the .ris with VERIFY-CITE flags, including a note to check whether a stronger proton-decay bound has appeared. Placement suggestion is after the confinement discussion or with the structural exclusions — the exclusion list gains its sixth member either way.

Yes — and it's worth doing carefully, because when I sat down to enumerate the cases, the result is *not* entirely obvious: the cubic (renormalisable) level is a clean theorem, but the famous GUT proton-decay structure ε(qqq)ℓ survives both colour equivariance and spin-statistics, so it has to be quarantined as a named open problem rather than smuggled into the theorem. Let me check the notation and labels in the existing splices first so this one plugs in cleanly.

*[tool_use: view]*

*[tool_result: view]*

*[tool_use: view]*

*[tool_result: view]*

*[tool_use: project_knowledge_search]*

*[tool_result: project_knowledge_search]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: create_file]*

*[tool_result: create_file]*

*[tool_use: create_file]*

*[tool_result: create_file]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

Sentinel gate passes: two pdflatex passes, zero errors, all references resolved, no overfull boxes. Now the RIS batch for the four new keys.

*[tool_use: create_file]*

*[tool_result: create_file]*

*[tool_use: bash_tool]*

*[tool_result: bash_tool]*

*[tool_use: present_files]*

*[tool_result: present_files]*

Done, and compile-verified: two pdflatex passes, zero errors, all cross-references resolved (via stub anchors in the harness — the harness is not for the corpus, and its `\autocite` is stubbed, so ledger key spellings still need the usual check).

The structure that emerged is worth a word, because your instinct that it was "obvious" turns out to be true for one part and importantly false for another. The proof runs on three filters: colour triality (Corollary: invariants need quark-minus-antiquark legs ≡ 0 mod 3, a one-line consequence of the Weyl FFT door inventory), fermion parity (odd spinor legs admit no SL(2,ℂ) singlet), and inventory completeness (P3: no bosonic species carries the 3, so no mediator, scalar or vector). Those three close *every* trilinear vertex — that's the theorem, and it's the precise form of what you had in mind. But exactly one quark-number-violating structure passes all three filters: ε(qqq)ℓ, four spinor legs, colour singlet through the ε door — which is precisely the GUT proton-decay operator — together with its square, the n–n̄ oscillation structure. The mechanics you thought made it obvious genuinely cannot reach these, so they're quarantined as **op:baryon-contact** with PASS/FAIL criteria: PASS is a proof that no connected invariant diagram with three GHZ legs and one W leg exists (the hyperdeterminant flagged as candidate obstruction carrier), giving an absolutely stable proton and a falsifier; FAIL means computing the CPT-symmetric suppression and confronting the Super-K bound. Either way it lands squarely on the Hopf–Frobenius machinery, which raises the physical stakes of op:heunen-functor considerably — it now decides proton stability.

Statuses as installed: the two lemmas Established (classical), the theorem Structural conditional on P1–P4, with P4 (spin–statistics) flagged honestly as imported rather than derived — the Koszul-sign colour cube is noted as its natural future home. The SLOCC remark records this session's route: why the naive reading proves too much (Drell–Yan) and too little (CPT kills the orbit-closure arrow), so the invalid route stays retired.

For your verification pass: the external labels are listed in the header (all taken from the split splice and the GHZ/W appendix, but confirm `sec:canonical-orbits` lives where I think it does); `durvidalcirac2000` is VERIFY-KEY against the ledger; the four new keys (Weyl, Procesi, Takenaka/Super-K, Doršner et al.) are in the .ris with VERIFY-CITE flags, including a note to check whether a stronger proton-decay bound has appeared. Placement suggestion is after the confinement discussion or with the structural exclusions — the exclusion list gains its sixth member either way.
