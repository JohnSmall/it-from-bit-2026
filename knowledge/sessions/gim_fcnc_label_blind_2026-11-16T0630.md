# Session note: flavour-changing neutral currents and the GIM mechanism in the framework

Date: 2026-11-16T0630. Session: Claude Code (Fable), thinking session.
Asked by JS: "think about this framework's view of flavour changing neutral
currents and the GIM mechanism (Glashow--Iliopoulos--Maiani mechanism)".

Sources read today: `paper1/interactions_circuits_section_2026-06-08.tex`
(header history lines 86--110; the subsection "No flavour-changing neutral
currents", prop:fcnc, prop:neutral-blind, op:fcnc-all-orders, sec:absent-gate),
`paper1/masses_section_2026-06-08.tex` (eq:z3 circulant, eq:quarkalpha,
eq:dilution, op:cabibbo), `paper1/predictions_section_2026-06-13.tex` lines
183--200, `lean/.../Fcnc.lean`, the PDG 2024 CKM review (PDF text), and my two
notes of 2026-11-07 on the B anomalies. Script:
`scripts/gim_fcnc_label_blind_2026-11-16T0630.py`, 33/33, stdout in section 9.

## 0. The answer in six lines

1. GIM is three separate facts, and the paper proves only the first.
   Tree level: a coupling proportional to 1 on the generation label is
   diagonal in every basis (prop:fcnc, Lean-checked). Loop level: the
   mass-independent part of a charged-current loop is again proportional to 1
   and cancels, so only mass differences survive. And both need the 3 x 3
   mixing matrix to be exactly unitary.
2. The framework's real addition is at the first step, and it is not the one
   the paper claims. The cancellation is not "arranged" in the Standard Model
   and "forced" here; in both it follows once every generation carries the
   same register. What the framework adds is that an incomplete generation
   is impossible, because the label is a component-group index.
3. Read consistently, every gauge gate, the W included, is 1 on the label.
   Flavour change is then entirely the failure of two mass operators to
   commute, and the framework is exactly minimal flavour violation with no
   new scale.
4. The paper's own quark mass forms, two circulants on one label, commute.
   Taken at face value they give no mixing, no loop FCNC and no CP violation,
   for every S_3 relabelling of either frame. Mixing needs a continuous
   relative unitary that the component group cannot supply.
5. The Higgs is the one neutral coupling that is not proportional to 1. It is
   a function of the mass operator, hence diagonal. prop:fcnc does not cover
   it and should.
6. Two data points bite. First-row CKM unitarity sits 2.3 sigma below 1, and
   the framework has no vector-like quark to explain a deficit. The
   identification of the Cabibbo angle with 2/9 is 4.6 to 6.8 sigma from the
   measured elements.

## 1. What GIM is, taken apart

**Tree level, 1970.** Before charm, the Cabibbo-rotated d' sat in a doublet
with u and the orthogonal s' was a singlet. The Z couples to T_3 - Q sin^2
theta_W. The charge part is proportional to 1 on (d, s) in any theory, since
only equal charges mix; so are the photon and the gluon. The T_3 part was
diag(-1/2, 0), and rotating to the mass basis gives an s-d entry of
-sin theta cos theta / 2 = -0.109 (script A1): K_L -> mu mu at the rate of an
allowed decay. GIM completed the second doublet with charm; T_3 became
proportional to 1 and the entry vanished. Glashow and Weinberg, and Paschos,
1977, state the general rule: tree-level neutral currents are diagonal if and
only if all quarks of one charge and chirality share T_3 (and take mass from
one Higgs). VERIFY-SUPPORT on those two papers, title and standard only.

**Loop level, 1970--1974.** A second-order charged-current loop inserts
V^dag F(D_u) V between down-type quarks, F a loop function of the internal
masses. The constant part of F drops out by the same identity as prop:fcnc;
what survives is a difference of F between generations, of order
(m_c^2 - m_u^2)/M_W^2 for kaons. Gaillard and Lee used this in 1974 to bound
the charm mass near 1.5 GeV before charm was seen.

**Unitarity.** Both steps use V^dag V = 1 on exactly the generations that
exist. A fourth generation, or a vector-like quark, makes the 3 x 3 block
non-unitary and returns a tree-level Z coupling.

## 2. What the paper says, and what it leaves unsaid

prop:fcnc proves the tree-level identity from the premise "none of [the
neutral gates] acts on the triality index". The discussion then says the
framework's flavour observables are "pinned at the charged-current-loop
floor". That floor is the second and third facts above. The paper relies on
them and states neither. In particular the claim that loops reproduce the
Standard Model values needs exactly three generations with an exactly unitary
V, which the framework has (no fourth generation, no vector-like quarks) but
does not connect to this subsection.

One sentence is imprecise: "In the Standard Model the cancellation
V^dag 1 V = 1 is arranged by the structure of the theory; here it is forced".
In the Standard Model it is forced too, once each generation is given the same
representation; the choice lies in the representation content. The accurate
contrast is: the Standard Model permits incomplete or vector-like generations
and observation excludes them; the framework has no way to write one down,
because the generation index is pi_0(Aut) = S_3 and the register is the same
object in each component. The framework's version of "charm had to exist" is
"a component of the automorphism group cannot carry half a register".

## 3. The structural points (script Part A)

**3.1 The loop form of prop:fcnc.** STRUCTURAL (linear algebra; ours to
state, not new mathematics). For any unitary V and real F_1, ..., F_n, the
off-diagonal part of V^dag diag(F) V is unchanged by F -> F + c, and every
off-diagonal entry is bounded by (max F - min F)/2, with equality for maximal
two-generation mixing. Proof: subtract the midpoint c; the remainder has
operator norm half the spread, and an entry is bounded by the norm. Script A2:
2000 Haar draws, largest ratio 0.987; bound attained at 0.500. prop:fcnc is
the case of zero spread. This is one lemma, not two mechanisms: tree-level and
loop-level GIM are the same identity applied to an operator that is, or is
not, proportional to 1 on the label.

**3.2 All gates are blind; flavour change is a commutator.** In the weak
basis the W is also 1 on the label: it flips the B qubit and pairs up-type
generation i with down-type generation i. V appears only when both mass
operators are diagonalised, V = U_u^dag U_d. The loop insertion in weak-basis
form is F(H_u), H = M M^dag, seen from the down mass basis (script A3,
deviation 3e-14), so

  flavour-changing neutral amplitude != 0  <=>  [H_u, H_d] != 0.

Jarlskog's 1985 commutator is the same object: det[H_u, H_d] = 2i J times the
product of the six mass-squared differences (script A5, six-figure
agreement, J = 3.117e-5 from the PDG 2024 angles against the quoted
3.12e-5). CP violation and FCNCs are two invariants of one commutator.

CANDIDATE reading for the paper: the gauge sector commutes with all of U(3)
on the label, not merely with S_3, and the only operators that do not are the
mass operators. Every amplitude is then a U(3)-covariant function of H_u and
H_d. That is the spurion argument of Chivukula and Georgi 1987 and
D'Ambrosio, Giudice, Isidori and Strumia 2002: minimal flavour violation.
The framework's "no mediator at any scale" is minimal flavour violation with
no new scale. It also gives op:fcnc-all-orders a precise dictionary-level
form: show that the dynamical layer adds no operator on the label besides
functions of the two mass operators.

This reading has one conflict with the paper's wording. The interactions
section calls the full charged current "the T_3 raise tensored with the CKM
rotation V", a gate acting on a generation wire, while prop:fcnc's premise is
that no gate acts on the label and my 2026-11-07 note showed the identity
component acts trivially on pi_0. V is a continuous unitary on C^3 and is not
in S_3. The two are compatible only if V is a relative frame between two mass
eigenbases and not an action of anything on the label.

**3.3 The circulant no-go.** STRUCTURAL as mathematics. The masses section
writes each sector's square-root masses as the eigenvalues of a circulant
(eq:z3), with alpha^2 = 2 + 2|Q|^{3/2} and delta = (2/9)/n. All Hermitian
circulants on one basis share the Z_3 Fourier eigenvectors and commute.
Script A4 with the paper's own parameters: [X_u, X_d] has norm 1e-17 and |V|
is the identity. A relative triality shift relabels and still commutes. So
does conjugating one frame by any of the six elements of S_3, since S_3
normalises Z_3 (largest commutator 1e-17; |V| a permutation). I first wrote
that check expecting an odd permutation to break commutation; it does not,
and the check was corrected before the final run.

Consequence: eq:z3 in both quark sectors on a common label gives zero mixing,
zero loop FCNC and J = 0. The measured V is the relative unitary R between
the two sectors' cyclic frames, V = F^dag R F (script: R unitary, 0.12 from a
permutation), four physical parameters, and no element of the component group
contributes to it. This sharpens op:cabibbo: the question is not which angle,
it is what continuous datum orients the down-sector cyclic frame against the
up-sector one, given that the label is discrete and the gates are blind.

CONJECTURE, direction only: the two sectors' democratic J_3(O) elements have
off-diagonal octonions in different complex lines of O. A circulant over one
C is the special case of a common line; the angle between the lines is a
continuous G_2 datum acting on the Jordan elements, not on pi_0, so it does
not contradict prop:fcnc. Nothing computed.

**3.4 The Higgs.** The Higgs coupling is not proportional to 1: it is the
mass operator over v. It is diagonal in the mass basis because there is one
source of mass. prop:fcnc lists photon, Z and gluon only. Script A6 gives the
link to the 2026-11-07 note: the all-ones matrix J is three times the
spectral projector on the tau, J = 3 (X - m_e)(X - m_mu) /
((m_tau - m_e)(m_tau - m_mu)) in square-root-mass units, a polynomial in the
lepton mass operator. So the "tau-only aligned coupling a 1 + b J" that I said
S_3-equivariance alone would allow is a function of the mass operator. It is
what a scalar coupled through the mass operator does, and the Higgs is such a
scalar. The exclusion the tau anomalies test is therefore better put as: one
mass source, no second scalar. That corrects the emphasis of my earlier
note, not its conclusion. Fence as before: circulant representative only.

## 4. Numbers (script Part B; leading-order one-loop estimates, not predictions)

| quantity | estimate | reference |
|---|---|---|
| Delta M_K, charm box, no QCD factor | 1.60e-15 GeV | measured 3.484e-15 GeV |
| same with the cancellation off | 6.4e-12 GeV | 1837 times too large |
| BR(B_s -> mu mu), top loop | 3.81e-9 | Bobeth et al. 2014: (3.65 +/- 0.23)e-9 |
| t -> cZ scaling | 9e-14 | about 1e-14 full; ATLAS 2023 limit 1.3e-4 |
| BR(mu -> e gamma), m_1 = 0, normal ordering | 4.5e-55 | MEG II 2025 limit 1.5e-13 |
| sterile-induced lepton non-unitarity | 1.4e-14 | seesaw, 3.6 TeV, 0.05 eV |

These are the Standard Model's numbers; the framework takes no credit for
them. The 1e-14 for t -> cZ is the paper's figure; I reproduced its scaling
only (VERIFY-SUPPORT on Aguilar-Saavedra 2004, abstract only).

**First-row unitarity.** PDG 2024: |V_ud|^2 + |V_us|^2 + |V_ub|^2 =
0.9984 +/- 0.0007, "a 2.3 sigma tension with unitarity in the 1st row". The
framework requires exactly 1 and excludes the usual explanations (vector-like
quarks, a fourth generation, right-handed currents). If the deficit hardens
it refutes the framework; if it goes away the framework was on the right
side. Same logical type as R(D(*)).

**The Cabibbo identification.** cos(2/9) = 0.97541 and sin(2/9) = 0.22040.
Against the direct PDG 2024 values, 0.97367 +/- 0.00032 and 0.22431 +/-
0.00085, these are +5.4 and -4.6 sigma; against the unitarity-constrained fit,
0.97435 +/- 0.00016 and 0.22501 +/- 0.00068, +6.6 and -6.8 sigma. The angle
itself is 2.1 per cent off. The masses section quotes 0.97435 (a fit value)
beside 0.22430 (a direct value), mixing two sources, and calls the agreement
"per-cent level", which is true and hides that it is excluded as an exact
statement. op:cabibbo already says "residual"; it should give the sigma.

## 5. What I think

The no-FCNC subsection is correct and undersold in one place and oversold in
another. Undersold: the one-line identity extends to loops, and with exactly
three generations it gives the whole GIM mechanism and the precise statement
"minimal flavour violation, no new scale". Oversold: the "forced, not
arranged" contrast, and the silence on the Higgs.

The uncomfortable finding is 3.3. The framework has a good account of why
the gates cannot see the label and no account of why the two mass operators
disagree about it. The paper's own mass formulae, read literally, commute.
"Mixing forced as the shadow of the zero divisors" is at present a sentence
pointing at a dedicated paper; the commutator [H_u, H_d] is the object that
paper has to produce, and S_3 cannot produce it.

## 6. Findings for JS's ruling

(a) Add the loop lemma (3.1) after prop:fcnc as a proposition, with a
    sentence that the charged-loop floor rests on it and on exact 3 x 3
    unitarity. Lean-checkable.
(b) Replace "arranged ... forced" with the completeness statement of
    section 2, citing Glashow--Weinberg and Paschos.
(c) Add the Higgs to prop:fcnc's discussion: diagonal because it is a
    function of the single mass operator.
(d) State in the interactions section that V is a relative frame, not a gate
    on the label; add the commutator criterion and the minimal-flavour-
    violation identification.
(e) Sharpen op:cabibbo with the circulant no-go and give the sigma for 2/9;
    fix the mixed-source quotation of V_ud.
(f) Add first-row CKM unitarity and mu -> e gamma to the predictions
    section's falsifiers.

## 7. Fences

- Part B is leading order with rounded inputs; agreement to a factor of two
  (K mixing) or 4 per cent (B_s) is the expected quality, nothing more.
- 3.3 assumes both sectors' circulants are written on one label basis in
  which the W pairs generation i with generation i. The paper does not say
  this; it does not say otherwise either.
- The B_s -> mu mu measurement is not quoted: I read only the CMS 2023
  abstract ("consistent with the standard model predictions").
- Inami--Lim functions written from memory and validated only by the
  B_s result and S0(x_t) = 2.30; VERIFY-SUPPORT.

## 8. Proposed ledger entries (not written)

- **STRUCTURAL** Loop form of the no-FCNC identity: offdiag(V^dag F V)
  depends on differences of F only and is bounded by half its spread.
- **STRUCTURAL** Hermitian circulants on one label commute; with eq:z3 in
  both quark sectors V is a permutation for every S_3 relabelling.
- **CANDIDATE** All gauge gates are 1 on the label; flavour change is
  [H_u, H_d]; the framework is minimal flavour violation with no new scale.
- **OPEN** (sharpening op:cabibbo) Produce the relative unitary between the
  up and down cyclic frames. PASS: a derived non-zero [H_u, H_d] with the
  measured J = 3.12(13)e-5 and angles. FAIL before checking: any route using
  only S_3 relabellings or triality shifts of circulants.
- **OPEN** First-row unitarity: PASS if the sum returns to 1 within errors;
  FAIL if a deficit is established at five sigma.
- invalid_routes.md, proposed: "CKM mixing from a discrete relabelling or
  triality shift between sector circulants" (closed by script A4).

## 9. Exact stdout

```
seed 20261116

== A1  tree level ==
  [PASS] V^dag (c 1) V = c 1 for a Haar V  (max deviation 9.0e-17)
    three-quark world: (d,s) entry of T_3 in the mass basis = -0.10930 = -sin cos / 2 = -0.10930
  [PASS] without charm the Z has a tree-level s-d coupling of order sin(theta_C)/2
  [PASS] with charm T_3 is proportional to 1 and the coupling vanishes
  [PASS] the charge (photon) part is diagonal with or without charm

== A2  loop level: only differences of F survive, bounded by half the spread ==
  [PASS] offdiag(V^dag F V) is unchanged by F -> F + c (2000 Haar draws)  (max relative change 8.1e-16)
  [PASS] |entry| <= (max F - min F)/2 in every draw  (largest ratio 0.9873)
  [PASS] the bound is attained by maximal two-generation mixing  (entry 0.500 at spread 1)
  [PASS] degenerate masses (F constant) give exactly zero

== A3  weak-basis form: the loop insertion is F(H_u); flavour change <=> [H_u, H_d] != 0 ==
  [PASS] V^dag F(D_u) V = U_d^dag F(H_u) U_d  (max deviation 3.2e-14)
  [PASS] generic H_u, H_d do not commute and the loop insertion is off-diagonal
  [PASS] commuting H_u, H_d give V = 1 and no off-diagonal insertion

== A4  the paper's circulant mass forms in one label basis ==
    leptons  sqrt-mass eigenvalues [0.04035 0.58021 2.37944]  squared ratios to heaviest [0.00029 0.05946]
    down     sqrt-mass eigenvalues [0.08431 0.3809  2.53479]  squared ratios to heaviest [0.00111 0.02258]
    up       sqrt-mass eigenvalues [0.01104 0.23632 2.75264]  squared ratios to heaviest [0.00002 0.00737]
  [PASS] [X_u, X_d] = 0 for the paper's up and down circulants  (norm 9.7e-18)
    |V| from the two circulants:
      [1. 0. 0.]
      [0. 1. 0.]
      [0. 0. 1.]
  [PASS] the resulting |V| is a permutation matrix: no mixing
  [PASS] a relative triality shift of 2 pi/3 only relabels: still commuting
    S_3 transposition applied to the down frame: commutator norm 1.3e-17; |V| =
      [0. 1. 0.]
      [1. 0. 0.]
      [0. 0. 1.]
  [PASS] an odd S_3 relabelling of one frame also keeps the circulant form (S_3 normalises Z_3): still commuting  (norm 1.3e-17)
  [PASS] and |V| is again a permutation: no element of the component group produces a mixing angle
  [PASS] all six elements of S_3: [X_u, g X_d g^-1] = 0  (largest norm 1.3e-17)
  [PASS] V = F^dag R F: the measured CKM is the relative unitary R of two cyclic frames (R is unitary, not a permutation)  (max | |R| - 1 | = 0.120)

== A5  Jarlskog commutator ==
    J from the PDG 2024 angles and phase: 3.117e-05 (PDG quotes 3.12e-5)
    det[H_u, H_d] = 1.8654e+05 i ; 2 J prod = 1.8654e+05
  [PASS] J reproduces the PDG value within its error
  [PASS] |det[H_u, H_d]| = 2 J prod(m_u^2 diffs) prod(m_d^2 diffs)

== A6  the all-ones matrix is a function of the Koide circulant ==
  [PASS] J = 3 P_tau = 3 (X - m_e)(X - m_mu) / ((m_tau - m_e)(m_tau - m_mu)) in sqrt-mass units  (max deviation 1.7e-17; eigenvalue index 2 (largest))
  [PASS] so a 1 + b J commutes with X_l: aligned, no lepton flavour violation

== B1  the Cabibbo identification and first-row unitarity (PDG 2024) ==
    |V_ud| = 0.97541 from 2/9 ; PDG direct 0.97367 +/- 0.00032 ; +0.18 % ; +5.4 sigma
    |V_ud| = 0.97541 from 2/9 ; PDG SM fit 0.97435 +/- 0.00016 ; +0.11 % ; +6.6 sigma
    |V_us| = 0.22040 from 2/9 ; PDG direct 0.22431 +/- 0.00085 ; -1.74 % ; -4.6 sigma
    |V_us| = 0.22040 from 2/9 ; PDG SM fit 0.22501 +/- 0.00068 ; -2.05 % ; -6.8 sigma
    fitted theta_12 = 0.22695 rad against 2/9 = 0.22222: -2.08 %
  [PASS] 2/9 is within 2.5 per cent of the Cabibbo angle
  [PASS] but outside the measurement by more than four sigma on each element
    first row: |V_ud|^2 + |V_us|^2 + |V_ub|^2 = 0.9984 +/- 0.0007 ; framework (exactly three generations) 1 ; pull -2.3 sigma
  [PASS] first-row unitarity deficit is between 2 and 3 sigma

== B2  how much GIM suppresses: K mixing ==
    x_c = m_c^2/M_W^2 = 2.497e-04 ; S0(x_c) = 2.497e-04 ; S0(x_t) = 2.301
    Delta M_K, charm box, no QCD correction: 1.60e-15 GeV ; measured 3.484e-15 GeV ; ratio 0.46
    same box with the cancellation switched off (loop function 1): 6.40e-12 GeV ; ratio to measured 1837
  [PASS] S0(x_c) = x_c to leading order: the amplitude is a mass difference
  [PASS] the charm box gives Delta M_K within a factor three (Gaillard and Lee)
  [PASS] without the cancellation K mixing would be over a thousand times too large

== B3  B_s -> mu mu from the top loop ==
    Y = 0.960 ; prompt BR = 3.57e-09 ; time-integrated (y_s = 0.064) = 3.81e-09 ; Bobeth et al. 2014: (3.65 +/- 0.23)e-9
  [PASS] leading-order top-loop estimate within 15 per cent of the full SM prediction  (ratio 1.04)
  [PASS] helicity and loop suppression: BR below 1e-8

== B4  floors ==
    t -> c Z scaling |V_cb|^2 (m_b/M_W)^4 (alpha/(4 pi s_W^2))^2 = 8.9e-14 (full calculation: about 1e-14) ; ATLAS 2023 limit 1.3e-4
  [PASS] the scaling estimate is within two orders of 1e-14 and ten orders below the limit
    mu -> e gamma with m_1 = 0, normal ordering: BR = 4.5e-55 ; MEG II 2025 limit 1.5e-13 ; gap 42 orders
  [PASS] the leptonic GIM floor is below 1e-50
    seesaw mixing of a 3.6 TeV sterile with 0.05 eV: theta^2 = 1.4e-14 (non-unitarity of the 3x3 lepton matrix)
  [PASS] sterile-induced non-unitarity is below 1e-12

33/33 checks passed
GIM FCNC LABEL BLIND: PASS
```
