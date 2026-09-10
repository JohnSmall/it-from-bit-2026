**Purpose & context**

John is an independent theoretical physicist (MSc, Imperial College London, supervised by Fay Dowker) developing an original framework titled "It from Bit via Gödel" that derives Standard Model particle physics, quantum mechanics, and spacetime structure from first principles of self-reference and computability. The project has been in development since a 2005 CASYS conference paper and is now being prepared for journal publication as a multi-paper series. John's explicit working philosophy is "done beats perfect" — prioritising community engagement over complete formal rigour before submission.

The core framework derives complex probability amplitudes from an observer's in-principle self-ignorance (via Lawvere-Yanofsky diagonal obstruction), connects this to the Cayley-Dickson division algebra tower (ℂ → ℍ → 𝕆 → 𝕊), maps three-qubit entanglement classes (GHZ/W/Bell/product) to Standard Model particle types (quarks/leptons/gauge bosons/Higgs), and derives gauge group structure G_SM = SU(3)×SU(2)×U(1)/ℤ₆ from octonionic Hopf fibrations. The framework claims zero free dimensionless parameters.

Key collaborators and interlocutors include: Fay Dowker and Jonathan Halliwell (Imperial College), Andrei Khrennikov (Linnaeus/Växjö), Karl Svozil, Jochen Szangolies (DLR), Cohl Furey. John has presented at Växjö quantum foundations conferences (2022–2025) and [redacted 2026-09-10: private remark by a named third party; see knowledge/memory/CORRECTIONS.md]. John attended Filatov and Auzinsh's poster at the 2024 Växjö conference and encouraged their publication.

The project is housed in a private GitHub repository (`JohnSmith/self-ref-2026`), managed through Claude's Project knowledge panel sync. Bibliography is managed in Mendeley; references are delivered as `.ris` files. The paper uses LaTeX with biblatex/`\autocite`, booktabs, braket packages; British English; ASCII-only `.tex` content; dated filenames; attic prefixes for deprecated files.

---

**Current state**

*Paper 1* ("It from Bit via Gödel") is structurally complete except for John's four pieces of framing prose (introduction, abstract, preamble check, conclusions). Major sections finalised or in late draft include: the self-reference → complex amplitudes derivation chain, Born rule from Hopf fibration (U(1)-invariance forcing quadratic observables on S³), entanglement class → particle dictionary, fermion mass formula, boson sector predictions, no-leptoquark theorem, flavour-conservation-without-force splice, superconductor witness section, sedenion three-generations mechanism, and hardware appendix (ibm_fez Heron r2 batch). Outstanding `\input` lines in `main.tex` and several RIS batches (gw_energy, higgs_entanglement, brown_ref, fanout batches) await Mendeley import confirmation.

*Paper 2* ("Spacetime from the FANOUT Boundary") has a compilable skeleton with the gravitational wave energy objection answered (Isaacson averaging scale = chart re-emergence scale). Seven open problems are priced; next computation is the Newtonian limit (op:p2-newton).

Active theoretical work centres on the sedenion framework: zero-divisor structure, G₂-orbit, colour dictionary, sterile sector, and the D4 arena of four-qubit entanglement. A sedenion session (August 2026) produced double-verified Python scripts (seed-locked, Convention A Cayley-Dickson), session notes, RIS batches, and a D4-ledger addendum. One script (sedenion_zero_divisor_scan_2026-08-31.py) remains unechoed.

A housing seam between the K3 document's Class-4 placement and the psi-fixed line placement requires a bridge test.

Particle physics sub-thread: the up-quark mass paragraph in `masses_section` was patched (2026-08-24) to remove a GHZ–W interference fossil and replace it with the cross-algebra excursion / comparability condition language consistent with `op:up-quark`. Remaining fossils flagged but not yet patched: the following paragraph's "two-per-cent W component" and entries in `fermion_topology_table.py` and `fermion_topology_open_problems.md` §5.2.

GitHub integration operates via Project knowledge panel sync (not bash shell credentials). Compile verification uses `pdflatex -interaction=nonstopmode` with two passes; errors checked via `grep -E '^!' *.log`.

---

**On the horizon**

- Complete John's four framing prose sections to finalise Paper 1 for arXiv submission
- Bridge test resolving the K3 Class-4 / psi-fixed line housing seam
- Patch remaining fossils in `fermion_topology_table.py` and `fermion_topology_open_problems.md` §5.2
- Echo and verify sedenion_zero_divisor_scan_2026-08-31.py output
- Newtonian limit computation for Paper 2 (op:p2-newton)
- Email Andrei Khrennikov leading with the complementarity reframe and Tsirelson-as-ramification correspondence (p-adic/adelic session deliverable)
- Mendeley import with dedupe checks for multiple RIS batches
- Label mapping for four master-file section labels (`sec:hopf`, `sec:born`, `sec:fanout`, `sec:contextuality`) in the Jaynes appendix; two `%% PAPER2` / `%% PAPER3` comments await companion-paper citation keys
- Notebook T: extend Cayley-Dickson constructor to trigintaduonions to settle ℤ/2 vs S₃ branch dichotomy by construction
- `op:baryon-contact` (proton stability via quartic ε(qqq)ℓ structure): tied to op:heunen-functor Hopf-Frobenius machinery
- Attic rename of `entanglement_classes_section_2026-06-08.tex` once main.tex `\input` is confirmed

---

**Key learnings & principles**

**Established results (theorem or verified calculation):**
- Born rule derived from U(1)-invariance on S³ forcing minimum-degree quadratic observables; works for a single qubit (unlike Gleason's theorem)
- GHZ-class states map exclusively to the ℂ³ colour sector under the octonionic Hopf map (proved); W-class states access the ℂ lepton sector
- θ_QCD = 0 topologically forced (GHZ class has no oriented pairwise structure to carry a CP-violating phase)
- No-leptoquark theorem (conditional on four explicit premises); closes all trilinear vertices
- Flavour symmetry conserved but ungauged: forces come from identity component of Aut(𝕆) = G₂; generations come from component group π₀ = S₃, contributing nothing to any Lie algebra
- Coecke-Kissinger GHZ (special Frobenius) / W (anti-special) classification verified numerically; strong complementarity equivalent to anticommutation
- Winding-equals-ladder-number lemma (`lem:winding-number`) proved and verified to numerical zero
- Sedenion zero-divisor locus: single G₂-orbit, every annihilator exactly 4-dimensional; norm defect equals coassociative 4-form (theorem, not scan)
- Adams, Hurwitz, and Eakin-Sathaye collectively establish no new kinematic structure above the fourth qubit
- Koide ratio equals 2/3 when φ² = 1/3 with equal-weight frame reading (candidate)
- δ₀ = 2/9 reproduces charged lepton masses to <0.006% with zero free dimensionless parameters
- sin²θ_W = 1/4 at tree level (runs to 0.231 at M_Z with matching scale ~3.6 TeV); m_H = v/2 (−1.7%); y_t = 1 (+0.9%)

**Neutrino prediction (resolved 2026-06-12):** Σm_ν ≈ 52 meV per `fermion_mass_geodesic_calculation.md` (dilution rule, n=2). The earlier figure of 2.6 meV in `quark_neutrino_masses.md` is superseded. Δm²₂₁ ×30 tension and 0.6° θ_ν fine-tuning flagged open. Robust qualitative predictions: m₁ = 0 exactly, normal ordering, two sterile neutrinos ~3.6 TeV, no fourth generation.

**Invalid routes explicitly recorded (not to be retried):**
- Geodesic/path-length picture for quark mass (§7.8, March 18): retracted; replaced by associator debt framing
- GHZ–W superposition reading for quarks: fails — SLOCC classes are orbits not orthogonal summands; canonical orbit postulate requires zero pairwise concurrence
- Mass from Fano plane combinatorics: ruled out (all counting gives polynomial/binomial ratios; cannot produce super-exponential hierarchies)
- S⁷ as metric space for non-computable distance: excluded by non-associativity (Moufang loop, not group)
- Naive pushforward of W(F4) action: non-descent confirmed by three-coset argument

**Core structural principles:**
- FANOUT (first clonable record) marks the boundary between pre-measurement (signed/complex probability admissible, thermodynamically free) and post-measurement (Kolmogorov probability, Landauer cost kT ln2 per bit)
- The framework relocates non-computability rather than eliminating it ("bump in the carpet"); the residuum lands at the QM/GR interface
- Mass = associator debt (the extra information specifying bracketing in octonionic algebra, dimension [L⁻¹] in natural units); weak force = re-bracketing force
- Particles are causal channels between events, not objects with properties; quantum numbers are channel properties forced by Hopf chain consistency
- Interpretations of QM are coordinate systems on the same structure, not competing ontologies
- Open problems are a feature, not a weakness — framed as invitations to other researchers

---

**Approach & patterns**

**Document and file discipline:**
- Dated filenames (`description_YYYY-MM-DDTHHMM`); attic prefix (`attic_*.superseded`) for deprecated files, never deletion
- Sentinel-gated LaTeX splices (BEGIN/END markers); compile-verify with pdflatex two passes before delivery; zero errors required
- Patch scripts assert anchors whitespace-insensitively, write `.bak` files, add `EDITED` headers, refuse to run twice
- Status labels: ESTABLISHED / STRUCTURAL / CANDIDATE / CONJECTURE / RHYME / OPEN — never upgraded in place
- VERIFY-CITE and VERIFY-KEY flags on all unverified references
- Invalid routes logged explicitly in documents so they are not retried
- Session notes, ledger addenda, and RIS batches delivered as separate dated files
- Pure ASCII in `.tex` and `.md`; native Unicode in `.ris`

**Claim tracking:**
- Every claim requires explicit status encoding
- New conjectures formatted as PASS/FAIL open problems with explicit criteria
- Failed routes recorded alongside valid ones
- Cross-references resolved before file delivery; `MAP-LABEL` and `PAPER-COMPANION` markers used

**Collaboration style:**
- John drives all conceptual synthesis; Claude handles mathematical elaboration, critical engagement, literature connections, and document production
- John identifies inconsistencies between draft language and theoretical commitments; Claude diagnoses and proposes resolution
- Python scripts use fixed random seed and Convention A for Cayley-Dickson multiplication; John runs scripts independently and reports exact terminal output for reproduction verification
- Prose: paragraphs, no bullets in paper text; British English; `\autocite`; minimal formatting

---

**Tools & resources**

- **Computation:** Python (numpy, scipy, qiskit), IBM Quantum Platform (ibm_fez Heron r2), Docker/Jupyter for Qiskit environment; Qiskit credentials stored at `~/.qiskit/qiskit-ibm.json` (bind-mount recommended for persistence)
- **Writing:** LaTeX (pdflatex, biblatex, booktabs, braket, amsthm, draftwatermark/background); MacTeX via Homebrew; Overleaf for compilation; Biber 2.21
- **Bibliography:** Mendeley (`.ris` import); citation keys in `author+year+keyword` format; one `AU` line per author; native Unicode (never LaTeX escape macros such as `{\"o}` or any `{\...}` constructs — these break Mendeley import and cause LaTeX compilation errors); carry `\autocite` citation key in RIS `ID` field; DOIs included only where deterministic
- **Repository:** Private GitHub (`JohnSmith/self-ref-2026`); accessed via Claude Project knowledge panel sync (not bash shell); manual sync required after new commits; `project_knowledge_search` for content retrieval; `grep` on `/mnt/project` for label/delimiter auditing
- **Key literature anchors:** Moreno 1998, Biss-Dugger-Isaksen 2008, Cawagas 2004, Gunaydin-Gursey 1973, Eakin-Sathaye (J. Algebra 129, 1990), Adams 1960, Hurwitz 1898, Dür-Vidal-Cirac 2000, Coecke-Kissinger 2010, Verstraete et al. 2002, Szangolies 2025, Hardy 2001, Schack 2003, Abramsky-Brandenburger, Gillard-Gresnigt 2019; arXiv:2306.13098 flagged for priority assessment