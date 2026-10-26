# The standard objections to division-algebra field theories, and the framework's exposure

Date: 2026-09-27T1300. Fable session, at JS's request after the self-energy
attempt ("tell me more about the standard objections to division-algebra
field theories"). Every source below is from memory: VERIFY-CITE for the
metadata and VERIFY-SUPPORT for the claim, per CLAUDE.md, before any is cited.
None was read in this session.

## 0. A correction

"The standard objection" in the self-energy note was shorthand for a
structural fact and a historical record, not a citation. The fact:
ultraviolet divergences are set by the spacetime dimension and the momentum
dependence of propagators (power counting; the BPHZ subtraction theorem),
which tie them to the measure over modes; changing the coefficient algebra of
the fields changes numerators and symmetry factors, not the measure. The
record: no quaternionic or octonionic formulation has produced a finite
theory, and the non-associative ones have not produced a well-defined
perturbative expansion, ordering ambiguities leaving the path integral
under-defined rather than finite. Tang 2025 is the current instance.

## 1. The objections

| objection | aimed at | source (VERIFY-CITE) | the framework's exposure |
|---|---|---|---|
| No tensor product: the tensor product of two quaternionic modules is not a quaternionic module (H non-commutative), so composite systems have no natural description | quaternionic QM as a Hilbert-space theory | Adler 1995, *Quaternionic Quantum Mechanics and Quantum Fields* (OUP); Baez 2012, "Division algebras and quantum theory", Found. Phys. 42, 819 | none: the framework's Hilbert space is the complex one of qubits |
| Reduction: when the Hamiltonian commutes with a fixed imaginary unit, quaternionic QM is complex QM in disguise, and in practice it must | same | Adler 1995 | none, same reason |
| No octonionic Hilbert space: non-associativity breaks operator composition and exponentiation; the only consistent octonionic QM is the exceptional Jordan algebra J3(O), for three-level systems only | octonionic QM | Jordan, von Neumann and Wigner 1934, Ann. Math. 35, 29; Günaydin, Piron and Ruegg 1978, Commun. Math. Phys. 61, 69 | none; and the one place octonionic QM proper appears, prop:koide-jordan, is J3(O), the allowed case |
| Null experiments: no quaternionic phase in neutron interferometry or in a single-photon metamaterial test | theories predicting hypercomplex phases | Kaiser, George and Werner 1984, Phys. Rev. A 29, 2276; Procopio et al. 2017, Nat. Commun. 8, 15044; Peres 1979 for the proposal | consistent: amplitudes are complex, no hypercomplex phase is predicted |
| Wrong dimension: SL(2,K) = Spin(1, dim K + 1) gives Lorentz groups in 3, 4, 6, 10 dimensions; the octonions point to ten; four needs a preferred complex direction | octonionic spacetime | Kugo and Townsend 1983, Nucl. Phys. B 221, 357; Baez and Huerta 2011, "Division algebras and supersymmetry I" | met head-on: Szangolies leaves the direction free, the paper derives it from FANOUT (hopf_justification); the derivation carries the weight |
| No dynamics: the division-algebra Standard Model programme reproduces representation content (one generation of SU(3) x U(1) from Cl(6) and G2) but no Lagrangian, couplings or masses; chirality and SU(2)_L need extra structure | Dixon, Furey, Gresnigt and successors | Dixon 1994, *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics*; Furey 2016 (thesis; Phys. Lett. B 785, 84 (2018)); the critique is folklore | owed and said: the interactions section's circuits; Paper 2 and companions for rates and propagators |
| Three generations by hand: octonions give one generation; three come from Cl(8), the sedenions or three copies, and constructions disagree | same | Gresnigt lines (gresnigtgourlayvarma2023three, gourlaygresnigt2024algebraic, in the library) | answered by notebook T: which triple the S3 permutes |
| Sedenions are not an algebra to do physics in: zero divisors break the norm, the Hopf sequence stops, the S3 may be an artefact of presentation | sedenion proposals | Adams 1960 (adams1960hopf, in the library); Brown 1967 (brown1967generalized, in the library) | turned around: the zero divisors are where the norm fails to compose, read as the settlement of the associator debt (prop:zd-defect) |
| No finiteness from non-associativity | claims that the algebra regulates loops | this session, `sessions/parallelisable_renormalisable_attempt_2026-09-27T1100.md` | checked: FAIL for the recastings; the paper asks only about removability |

## 2. For the paper

One paragraph, probably in the Hopf-justification section beside the
existing Szangolies comparison, saying that the first four objections do not
apply because the division algebras classify entanglement on a complex
Hilbert space rather than replacing its scalars, that the preferred
direction is derived rather than chosen, that dynamics is owed, and that
finiteness is not claimed. Not drafted; JS to decide whether it is wanted
in v2.

## 3. References to verify and batch (Opus)

Adler 1995 (book); Baez 2012; Jordan--von Neumann--Wigner 1934;
Günaydin--Piron--Ruegg 1978; Peres 1979 (Phys. Rev. Lett. 42, 683); Kaiser,
George and Werner 1984; Procopio et al. 2017; Kugo--Townsend 1983; Baez--Huerta
2011 (Adv. Theor. Math. Phys. 15, 1373); Dixon 1994 (Kluwer); Furey 2018.
All metadata from memory.
