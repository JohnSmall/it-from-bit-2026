# Notebook T -- Trigintaduonion Automorphisms (2026-08-27)

Session record for the notebook ledger. Companion files:
`notebook_T_trigintaduonion_automorphisms_2026-08-27.py` (source) and
`notebook_T_output_2026-08-27.txt` (captured run, exit 0). Status vocabulary as usual.

**Claim.** The automorphism increments of the Cayley-Dickson tower beyond the octonions, locked to
corpus conventions (recursion `(a,b)(c,d) = (ac - conj(d)b, da + b conj(c))`, `conj(a,b) =
(conj(a), -b)`, doubling unit of rung n at index `2^(n-1)`). Three parts.

Part A (the ledger's Z/2-vs-S3 dichotomy). Brown's explicit maps on `A_n = A_{n-1} (+) A_{n-1}u`
-- the doubling involution `eps(a+bu) = a-bu` and the order-three
`psi(a+bu) = [a+3a*+sqrt3(b-b*)]/4 + [b+3b*-sqrt3(a-a*)]/4 u` (Gresnigt-Gourlay-Varma 2023 eqs
42-44, quoting Brown 1967) -- verified as exact algebra automorphisms at rungs n = 3, 4, 5, 6
(worst residual 1.1e-16 on all basis pairs); `psi^3 = I`, `eps^2 = I`, `eps psi = psi^2 eps`
(so `<eps, psi> = S_3`); psi mixes the two halves (not a lift); the new S_3 at rung n commutes
with the lifted S_3 from rung n-1 and the lifted psi is a distinct element (direct product,
independent factors). Derivation-algebra dimensions by nullspace count: dim Der(A_n) = 0, 3, 14,
14, 14 for n = 1..5. VERDICT: over R the Eakin-Sathaye branch is S_3 at every rung >= 4 (the Z/2
branch is the general-field case where psi's sqrt3 is unavailable); the identity component stays
g_2 from the octonions onward. The fifth rung is not silent but REPETITIVE: one further finite
S_3 per rung, no new continuous symmetry, ever.

Part B (the two triples). The corpus's sedenion mechanism used the core triple: three octonion
copies `core (+) V_i` through the quaternion core `<e0, e4, e8, e12>` (Gillard-Gresnigt 2019's
split; notebook M's V_i). Verified: Brown's S_3 stabilises the core and EACH V_i setwise; no
element of Brown's S_3 carries V_1 into V_2. The automorphism cycling V_1 -> V_2 -> V_3 is a
LIFTED G_2 element -- the colour-line three-cycle (e1->e2->e3, e5->e6->e7, e4 fixed, inside
SU(3) = Stab(e4)) -- which fixes the core pointwise and commutes with psi. Fix(psi_4) =
span{e0, e8}, dimension 2. VERDICT: the core triple is a colour-basis structure one rung up (the
March finding -- three Fano lines through the preferred direction are colours, not generations --
repeated at the sedenions; the constructor note's CP^2 of copies-through-the-core is colour CP^2).

Part C (the triple psi does permute). The three octonion HALVINGS `O, psi O, psi^2 O` of S:
each is an octonion subalgebra; pairwise and triple intersections are exactly R; each halving
together with the fixed unit e8 regenerates S (`S = H (+) H e8` for each); the three involutions
`eps psi^k` are the three doubling involutions, fixing halving k pointwise, one each. VERDICT:
the doubling's S_3 permutes the three halvings -- three ways of writing S as the completed link
doubled by the one tag direction, at relative orientations 0, 120, 240 degrees. Generations =
the psi-orbit, exactly as the Gresnigt line's later papers construct them; gauge-blindness of
the orbit follows from the DIRECT product (psi commutes with G_2), which is the framework's
structural reason for Gresnigt 2026's untriplicated gauge sector.

**Design.** Pure numpy on R^(2^n); recursion and maps exactly as in the corpus convention;
tolerance 1e-10, observed residuals ~1e-16 (exact to machine precision). Automorphism checks on
all basis pairs (up to 64 x 64 at rung 6). Derivations via the normal matrix of the sparse
Leibniz system, eigenvalue count below 1e-8. Subspace checks by rank; intersections by stacked
orthogonal complements. Brown's EQUALITY `Aut(A_{n-1}) x S_3 = Aut(A_n)` for n = 4, 5, 6 is
CITED (via Gresnigt-Gourlay-Varma sec. 4.3), not computed: the notebook verifies the inclusion,
the direct-product structure, and the derivation count.

**Verified outputs.** `notebook_T_output_2026-08-27.txt`: all Part A/B/C verdicts True; final
line `NOTEBOOK T: PASS`.

**Status.** Part A: confirmation of ESTABLISHED external results (Brown 1967; Eakin-Sathaye
1990, VERIFY-CITE for the exact general form; Schafer 1954, VERIFY volume). Parts B and C: exact
algebra, machine-verified. The physical identifications riding on C (generation = discrete
orientation of link against copy; the repeated higher-rung factor as what the redundancy ladder
consumes) are CANDIDATE and RHYME respectively, flagged where used (sedenion section 2026-08-27;
sec:wf-chain-type).

**Consistency.** Settles the ledger item "notebook T: trigintaduonion constructor, Z/2-vs-S3
dichotomy" on the S_3 side. Re-points notebook M: M's computations stand (the V_i are
subalgebras, the Klein grading holds, the bare cross-V_i vertex is pi/4), but they are
colour-side statements; the generation-side scan on the psi-orbit is OWED before M's
maximal-mixing verdict, the masses op:up-quark route-closure clause, and notebook N's
pre-registered dressing hypothesis are carried over. Re-points the classification ledger's
sec. 4(c) sentence and the 2026-08-12 constructor note (see
`corrections_ledger_sedenion_triples_2026-08-27.md`). Consonant with Gresnigt 2026 (sectors
`S_2 = psi_3(S_1)`, `S_3 = psi_3^2(S_1)`; gauge generators psi-fixed) and with the D4 arena
note's "structure at the fourth wire" (now sharpened: repetition, not silence, at the fifth).

**Invalid route (logged, do not retry).** "The three generations are the three octonion copies
through the H-core, permuted by the doubling's S_3; the shared core explains identical
electroweak numbers; the Klein-four grading {core, V_i} with S_3 = Aut is the shadow theorem's
secured half; the Fano-lines-to-V_i correspondence is the shadow bridge." Every clause attaches
generation language to colour structure: the copies are cycled inside G_2, the grading is the
colour grading, and both sides of the Fano bridge are colour-basis objects. The correct triple is
the halvings (Part C); the correct gauge-equivalence argument is the direct product; the shadow
problem is re-posed against the halvings in the 2026-08-27 section revision.
