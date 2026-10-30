# Kaluza--Klein size versus S^7 algebra: what replaces the compactification radius

Session note, 2026-10-30, Fable 5.1 with JS (maintainer). Status: **parked**. JS: "These
thoughts are not ready to go in the paper, but preserve them so we can come back to them at
some point." Nothing in paper1/ or paper2/ was changed. No ledger entries written; proposals
are in section 7 for JS to label.

Starting point (JS): the spacetime section derives three long-range dimensions from the
non-associativity of composition on S^7. Corollary: the closed timelike curves of S^7 cannot form
a metric space, but the algebra remains. Kaluza--Klein (KK) and its higher-dimensional extensions
must explain why the hidden spacelike directions are rolled up; here that is automatic. But in KK
the size of the rolled-up dimension sets the strength of the force, and the framework has no size.
What does the work that R does?

Where the paper already stands: `paper1/spacetime_from_non-computability.tex`, paragraph "The
S^7 sector as internal structure", states the resemblance to compactified dimensions, that the
degrees of freedom "have no size because they have no metric", and that they are algebraic rather
than geometric. It does not say what replaces the radius's other jobs. Section 5 below is what a
future patch would add.

## 1. What R does in Kaluza--Klein

In five-dimensional KK the gauge transformation is a translation along the circle; the gauge
parameter is a coordinate with a period. R enters three ways.

1. Charge quantisation: charge is momentum round the circle, in units of 1/R. The integer is
   topological; the unit is a length.
2. Coupling strength: the gauge kinetic term is integrated over the internal volume, so the
   coupling is a ratio of two lengths, alpha ~ (l_P/R)^2 up to an O(1) factor, and the observed
   alpha needs R of order twenty Planck lengths. Weinberg 1983 (Phys. Lett. B 125, 265,
   "Charges from extra dimensions") generalises to coset spaces: couplings are functions of the
   internal metric alone. VERIFY-CITE: not read this session.
3. A modulus: R is a dynamical scalar with no classical potential (radion/dilaton), needs
   stabilisation, makes alpha cosmologically variable, and predicts a tower of recurrences of
   every field at n/R.

The conceptual point: KK manufactures a dimensionless coupling from two dimensionful quantities.
That is the move the framework cannot make and, given the no-size corollary, should not want to.

## 2. The period survives, the length does not

KK conflates two things R does. The period of the gauge coordinate gives quantisation; the length
gives the unit and the strength. The framework keeps a phase with period 2 pi and no length.
Charge quantisation comes from `lem:winding-number` (ESTABLISHED) and the Z_6 quotient of
`prop:gsm` in the quantum-numbers section (STRUCTURAL via Krasnov). A winding number is an integer
whatever the radius. KK's first job is done with no size, and more cleanly than in KK, where the
quantum is a length-dependent unit.

## 3. Ratios of couplings are ratios of dimensions, not of lengths

The paper's sin^2 theta_W = 1/4 is derived from "coupling squared scales with fibre dimension",
g^2 ~ dim S^3 = 3 and g'^2 ~ dim S^1 = 1 (`paper1/quantum_numbers_section_2026-06-08.tex`,
subsection "The weak mixing angle"; the paper itself flags the equal-weight metric as a
structural assumption). This is the direct replacement for KK's internal-volume factor, and the
two rules run in opposite directions:

- KK: 1/g_i^2 grows with the volume of the i-th internal factor; a larger factor gives a weaker
  coupling. A weight by volume.
- Framework: g^2 grows with the dimension of the fibre; a larger fibre gives a stronger
  coupling. A count of channels.

The opposite sign is a structural difference, not a detail: it is the difference between weighing
and counting.

## 4. The rule does not extend to S^7 unchanged (one-loop check)

The KK-shaped question "what is the size of the strong sector" becomes, in the framework, "does
g_s^2 ~ dim SU(3) = 8 hold at the same matching scale where sin^2 theta_W = 1/4?" Checked at one
loop with PDG 2024 MSbar inputs at M_Z (1/alpha = 127.951, sin^2 theta_W = 0.23121,
alpha_s = 0.1180), SM beta coefficients b_Y = -41/6 (g' unnormalised), b_2 = 19/6, b_3 = 23/3
below m_t and 7 above. No randomness. Script
`scripts/kk_coupling_ratio_check_2026-10-30T1200.py`, exact stdout:

```
mu =    91.2 GeV  sin2W = 0.2312  a2/a' = 3.325  a3/a' = 11.607  a3/a2 = 3.491
mu =   500.0 GeV  sin2W = 0.2398  a2/a' = 3.171  a3/a' = 9.247  a3/a2 = 2.916
mu =  1000.0 GeV  sin2W = 0.2433  a2/a' = 3.110  a3/a' = 8.542  a3/a2 = 2.747
mu =  2000.0 GeV  sin2W = 0.2468  a2/a' = 3.051  a3/a' = 7.929  a3/a2 = 2.599
mu =  3600.0 GeV  sin2W = 0.2499  a2/a' = 3.002  a3/a' = 7.468  a3/a2 = 2.488
mu =  5000.0 GeV  sin2W = 0.2516  a2/a' = 2.975  a3/a' = 7.230  a3/a2 = 2.430
mu = 10000.0 GeV  sin2W = 0.2552  a2/a' = 2.919  a3/a' = 6.770  a3/a2 = 2.319
sin2W = 1/4 at mu = 3686 GeV;  a3/a2 = 8/3 at mu = 1438 GeV;  a3/a' = 8 at mu = 1837 GeV
```

Reading: the electroweak ratio lands on 3 : 1 at the paper's matching scale (reproducing the
0.24989 quoted in the boson-masses section). The strong ratio reaches 8 : 1 about a factor two
lower, and the three ratios 1 : 3 : 8 have no common scale; at 3.6 TeV the strong ratio is about
seven per cent short. So the naive extension fails. The paper already contains the reason: the
equal-weight metric argument presupposes a Lie algebra on the fibre. S^1 + S^3 is a group; S^7 is
a Moufang loop, and the paper's own words are that S^7 is a filter and not a ruler. A filter
selects channels; it does not weigh them. Expect the S^7 sector to fix which strong channels exist
and not the number g_s; g_s would have to be set by SU(3) as the stabiliser inside G_2, consistent
with the reduction clause in `op:three-dimensions`. The 1438 GeV figure is one-loop, no threshold
treatment, and is not for the paper; its use is to close a route (section 7).

## 5. What the absence of size commits the framework to

Consequences that follow at once and would belong in the internal-structure paragraph if it is
ever extended:

- **No tower.** With no distance along S^7 there is no momentum along it, so no KK recurrences at
  any energy. The two sterile states at 3.6 TeV are two states, not a ladder. Sharpest empirical
  distinction from KK: KK can push 1/R up but can never make the tower vanish.
- **No radion.** No modulus, so no massless scalar, no fifth force from it, no moduli
  stabilisation problem.
- **No drifting alpha.** alpha cannot vary with cosmic time through a changing R; any variation is
  ordinary running. Oklo and quasar bounds become consistency checks rather than constraints on a
  modulus.
- **The one scale is on the ruler side.** KK's 1/R is both the scale where tree-level values are
  exact and the scale of the tower. The framework's 3.6 TeV matching scale (`op:matching-scale`)
  plays only the first role, and the paper locates it "just above the scale at which the
  quaternionic structure becomes physically operative": it belongs to S^3, which can be a ruler,
  not to S^7. Self-consistent: the only sizes live on the spheres that compose associatively.
- **The trilinear vertex (coincidence, noted not claimed).** A coupling constant is the
  coefficient of a three-leg vertex, and three-link composition is exactly what is
  bracketing-dependent on S^7. The no-leptoquark theorem closes all trilinear vertices under its
  four premises. If the connection holds, the S^7 sector cannot carry a single composable coupling
  number even in principle, a stronger form of "no size".

## 6. The debt: the absolute strength

KK has a mechanism for the absolute coupling (l_P/R). The framework has none. The inside-observer
argument (`op:vev`, masses section) excuses one dimensionful input, v, but alpha is dimensionless
and the argument does not cover it. Searched paper1/ and knowledge/: the fine-structure constant
is not addressed anywhere (the only "fine structure" hit is the superconductor section's unrelated
use of the phrase; "alpha" in invalid_routes.md is the Koide alpha = sqrt2).

The framework's pattern so far (1/4, 1/8, 2/9, y_t = 1) says couplings are small-integer ratios of
dimension counts, and the absence of size makes that a commitment rather than a hope. With no
length available, alpha at the matching scale must be either

(a) a pure combinatorial number from the group side (S^1 + S^3, or SU(3) as stabiliser), or
(b) tied to the only length ratio the framework owns: the bit's size in Planck lengths,
    `op:p2-coefficient` in Paper 2 (bits per bit-pair). Note the KK analogy is exact in shape
    here: alpha_KK = (l_P / R)^2 is gravity's length over the gauge length, and the framework's
    one such ratio is l_P over the bit.

No mechanism proposed for either. The discipline of invalid_routes.md (no guessing angles)
applies to couplings.

## 7. Proposals for JS (not written to the ledgers)

- **OPEN, proposed: the absolute coupling.** Derive alpha at the matching scale. PASS: a count
  from the algebra, or a derivation through the Paper 2 coefficient, giving alpha inside the band
  obtained by running the measured value up, with no fitted input. FAIL before checking: any
  route that introduces a continuous internal parameter; that is Kaluza--Klein under another name
  and the framework has denied itself the size. Constraint: the S^7 sector contributes a filter,
  not a weight, so the number must come from the group side or from the bit coefficient.
- **Invalid route, proposed:** extending the fibre-dimension rule to the strong sector as
  g'^2 : g^2 : g_s^2 = 1 : 3 : 8 at a single matching scale. One-loop check above: the 8 : 1 ratio
  is reached at about 1.4 to 1.8 TeV, not at the 3.7 TeV where 3 : 1 is reached. Closed unless a
  threshold or two-loop treatment moves the scales together, which nobody has checked and which
  is the only thing that would reopen it.
- **STRUCTURAL, proposed (reading, no new mathematics):** charge quantisation in the framework
  is period without length (winding number), whereas in KK it is period converted to a unit by a
  length (n/R). The framework's quantisation is size-free; KK's is not.
- **Paper patch, deferred:** one paragraph after "The S^7 sector as internal structure" carrying
  section 5, and the open problem of section 7. Not drafted. JS: not ready.

## 8. VERIFY-CITE

- Weinberg, S. (1983), "Charges from extra dimensions", Phys. Lett. B 125, 265--269. Cited above
  for: in KK on a coset space, the gauge couplings are determined by the internal metric. Not read
  this session; no bib batch written since nothing cites it in the paper yet.

## 9. Files

- `knowledge/sessions/kaluza_klein_size_vs_algebra_2026-10-30T1200.md` (this note)
- `scripts/kk_coupling_ratio_check_2026-10-30T1200.py` (new; no randomness; stdout in section 4)
- No .tex, .bib or ledger changes. Nothing committed.
