# Session note: echoing the zero-divisor arc

Date: 2026-09-12T1930. Session: Claude Code (Opus 5), housekeeping.

## Why

`sessions/session_note_zero_divisor_arc_2026-08-31.md` carries its own
reproduction ledger, and it is explicit about a gap:

> Reproduction ledger: scripts 2 and 3 echoed back from the second environment,
> seed-locked values bit-identical, deviations last-digit float noise only
> (different BLAS). Script 1 delivered but NOT yet echoed; full
> double-verification of the arc awaits that run.

`notes/todo.md` has carried "Echo and verify the output of
`sedenion_zero_divisor_scan_2026-08-31.py`" since the project memory was
imported. The three scripts arrived in `~/Downloads` on 2026-09-12 and are now
in `scripts/`. All three were run here, so script 1 has its second environment
and scripts 2 and 3 have a third.

## Exact stdout

### 1. `sedenion_zero_divisor_scan_2026-08-31.py` --- the outstanding echo

```
Octonion table in this convention (e_i e_j = s e_k, i<j, both imaginary):
  Fano lines: [[1, 2, 3], [1, 4, 5], [1, 6, 7], [2, 4, 6], [2, 5, 7], [3, 4, 7], [3, 5, 6]]
[PASS] norm-defect identity, max |lhs-rhs| = 1.99e-13
[PASS] orthonormal imaginary pair -> ker L_z dims {4}; non-orthonormal -> {0}
[PASS] Ann(z) = {u + (uj)ell}: max |z w| = 1.01e-15; annihilator direction (uv).j = [-1. -1. -1. -1.]
[PASS] phi restricted to span(a,b,c,d) of a ZD pair vanishes: max|phi| = 6.94e-17
[PASS] 35 lines, 15 planes: 8 octonion + 7 quasi-octonion
   lines inside O        -> (octonion, quasi) planes through = (2, 1) : 7 lines
   lines mixed           -> (octonion, quasi) planes through = (1, 2) : 21 lines
   lines through tag e8  -> (octonion, quasi) planes through = (3, 0) : 7 lines
[PASS] census: 7 tag lines (3,0); 7 register lines (2,1); 21 mixed lines (1,2)
[PASS] psi = 1 (+) R_omega is an automorphism; the same with exp(i pi/4) is not; tau is
[PASS] Fix(psi) has dimension 2 (= span{1, e8}); psi^3 = 1: True
[PASS] tau psi tau = psi^{-1}  (<psi, tau> = S3)
[PASS] g = diagonal lift of the Fano rotation (e1 e2 e3) is an automorphism of S
[PASS] psi commutes with g (direct product G2 x S3 witnessed on one non-trivial g)
[PASS] ZD locus invariant under all of U(1)_ell; the three halvings O, O.omega, O.omega^2 contain no ZDs

ALL PASS
```

### 2. `sedenion_debt_koide_scan_2026-08-31.py`

```
[PASS] norm defect against a fixed frame is U(1)_ell-invariant (hence psi-degenerate): max dev 1.7e-13
[PASS] ratio = 0.000 (zero divisor) and 1.4142 (= sqrt2, same plane, flipped orientation); random max 1.3225 <= sqrt2
[PASS] |[p,q,r]|^2 = 4(1 - phi^2) on orthonormal imaginary triples: max dev 3.1e-15
[PASS] rotated-associator identity: max dev 1.5e-15; tag component on the six halving angles 3.1e-15
[PASS] |orbit debt|/|tag debt| = sqrt(1-phi^2)/(|phi| |sin 3theta|): max dev 8.7e-13
[PASS] phi^2 = 1/3, theta = pi/6, equal-weight frame: Koide ratio = 0.666667 for every frame azimuth (spread 6.7e-16); generic triple (phi^2 = 0.001): 248.8206
      sample at frame azimuth delta = 2/9: sqrt(m_k) proportional to [ 1.     -3.7418 -5.1646], m ratios [0.03749 0.52492 1.     ]  (Koide-parametrised e/mu/tau: 1 + sqrt2 cos(2/9 + 2 pi k/3))

ALL PASS
```

### 3. `sedenion_zd_colour_scan_2026-08-31.py`

```
[PASS] j = xy: L_j rotates span(x,y) (jx = y, jy = -x); z = x + (jx) ell has ker dim 4
[PASS] unit ZDs with direction j <-> unit colour vectors x in C^3_j (an S^5); x(jx) = j
[PASS] dim Der(O) = 14 (g2); dim{Dj=0} = 8 (su3); exp = automorphism fixing j; colour matrix special unitary
[PASS] tag phase on a ZD = colour phase of x (dev 3.4e-16); psi = central colour Z3 ON the ZD locus (dev 4.3e-16) but NOT off it (dev 1.73)
[PASS] colour x anti-colour lands in the core <1, j, ell, j ell>; |zw|^2 = 4|h(x,u)|^2 (ZD <=> singlet = 0)
[PASS] su(3)_j closes on ZD pairs over j, matches the dictionary, and its orbit map has rank 8 = dim of the fibre (14 - 6 = 8): the fibre of Z = G2 over S^6 is colour SU(3)
[PASS] z^2 = -|z|^2: every ZD is invertible (two-sided), yet z^{-1}(zw) = 0 =/= w -- the loss sits in the channel, not the element
[PASS] G-G blocks V_i = colour line i (x) tag (L_{e4} e_i ~ e_{i+4}); V_iV_i -> core (singlet channel), V_iV_j -> V_k (epsilon: 3x3 -> 3bar)

ALL PASS
```

## What this settles

**The arc is double-verified.** Script 1 passes every check in a second
environment, so the qualification in the 2026-08-31 note is discharged. Scripts
2 and 3 pass in a third.

**Two paper claims now have their machine verification in the repository.** The
masses section's bridge splice cites
`sedenion_debt_koide_scan_2026-08-31.py` for the norm-defect identity
`eq:debt-defect`; script 1 reports that identity at max |lhs - rhs| = 1.99e-13
and script 2 reports the rotated-associator identity at 1.5e-15. The results
ledger's CANDIDATE entry "Koide ratio equals 2/3 when phi^2 = 1/3 with the
equal-weight frame reading" is script 2's sixth line: the ratio is 0.666667 for
every frame azimuth, spread 6.7e-16, against 248.8206 for a generic triple.

**An independent corroboration of today's inventory.** Script 1 reports
`Fix(psi) has dimension 2 (= span{1, e8}); psi^3 = 1: True`, and that psi
commutes with a lifted Fano rotation, witnessing the direct product G2 x S3.
`sedenion_psi_orbit_angle_inventory_2026-09-12T1800.py`, written this afternoon
from notebook T without reference to this script, reports the same fixed
subspace and the same S_3 relations. Two independently written programmes, one
answer. The direct product is also the footing on which the corrections ledger
puts gauge-blindness after the core-triple route failed, so that argument is
machine-witnessed too.

**And one line bears on the psi-orbit question directly.** Script 1's last
check: "ZD locus invariant under all of U(1)_ell; the three halvings O, O.omega,
O.omega^2 contain no ZDs". The generation halvings are zero-divisor-free, which
is consistent with this afternoon's finding that their mutual geometry is all
rational multiples of pi: there is no degenerate direction inside a halving for
an irrational angle to hide in.

## Proposed ledger entries

None new. This is verification of entries that already exist, and the existing
wording stands; what changes is that the 2026-08-31 note's "awaits that run"
qualification can be retired.

## Not done

No build. The `bib/zd_structure_refs_2026-08-31.bib` batch (5 keys:
moreno1998zerodivisors, biss2008annihilators, cawagas2004sedenion,
demarrais2000assessors, gunaydin1973quark) supports the 2026-08-31 session note
but is cited by no `.tex` in the repository, so it is not needed for the build
and importing it is optional.
