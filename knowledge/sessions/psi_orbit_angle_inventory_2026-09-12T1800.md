# Session note: the angle inventory re-run on the psi-orbit

Date: 2026-09-12T1800. Session: Claude Code (Opus 5), housekeeping.

## Why

Notebook M (2026-07-10) scanned eighteen structural angles of the sedenion
triple for delta_0 = 2/9 and found none, and that miss was logged as a closed
route. Notebook T (2026-08-27) then showed M had scanned the wrong triple:
Brown's S_3 stabilises each octonion copy `core (+) V_i`, so those are colour
structure, and the triple S_3 actually permutes is the three halvings
O, psi(O), psi^2(O). On 2026-09-12 I recorded that this superseded part of my
own 2026-09-11 entry: M closes the colour-triple frame and says nothing about
the generation frame. JS asked for the re-run on the correct triple.

## What was run

`scripts/sedenion_psi_orbit_angle_inventory_2026-09-12T1800.py`. Cayley-Dickson
convention A throughout, exact linear algebra on fixed bases, no seed needed.
The algebra is notebook M's; psi and eps are notebook T's, not reinvented:

    psi(a, b) = ( [a + 3a* + sqrt3 (b - b*)]/4, [b + 3b* - sqrt3 (a - a*)]/4 )
    eps(a, b) = (a, -b)

The basket was declared in the script's docstring before the run: P1 the
relative phase under psi for four vectors and three complex structures, P2 the
principal angles between the imaginary parts of two halvings, P3 the
cross-halving zero-divisor leakage, P4 dimension ratios. Twelve of the twenty
entries are principled; the e4 and e12 complex structures are carried only for
comparability with M's basket and are flagged, because Fix(psi) = span{e0, e8}
makes e8 the only imaginary unit psi fixes and so the only psi-equivariant
choice. The hit criterion is M's: |theta - 2/9| < 0.003 and a principled
construction.

## Exact stdout

```
== psi-orbit angle inventory (notebook M's basket, notebook T's triple) ==
(A) psi is an automorphism of S: worst violation 1.11e-16
(A) psi^3 = I: True; eps^2 = I: True; eps psi = psi^2 eps: True
(A) dim Fix(psi) = 2; basis units it contains: ['e0', 'e8']
(A) the three halvings are 8-dimensional subalgebras, pairwise intersection dim 1

== the inventory against delta_0 = 2/9 = 0.222222 ==
  P1 x=e1             s=e8  [principled]               = 2.094395  nearest: 2pi/9 (0.69813)  (= 2pi/3 exactly, to 4.4e-16)
  P1 x=e1             s=e4  [comparability]            = 3.141593  nearest: 2pi/9 (0.69813)  (= pi exactly, to 0.0e+00)
  P1 x=e1             s=e12 [comparability]            = 3.141593  nearest: 2pi/9 (0.69813)  (= pi exactly, to 0.0e+00)
  P1 x=(e0+e1)/sqrt2  s=e8  [principled]               = 1.047198  nearest: 2pi/9 (0.69813)  (= pi/3 exactly, to 2.2e-16)
  P1 x=(e0+e1)/sqrt2  s=e4  [comparability]            = 0.000000  nearest: 1/9 (0.11111)  (= 0 exactly)
  P1 x=(e0+e1)/sqrt2  s=e12 [comparability]            = 0.000000  nearest: 1/9 (0.11111)  (= 0 exactly)
  P1 x=uniform-Im(O)  s=e8  [principled]               = 2.094395  nearest: 2pi/9 (0.69813)  (= 2pi/3 exactly, to 0.0e+00)
  P1 x=uniform-Im(O)  s=e4  [comparability]            = 3.141593  nearest: 2pi/9 (0.69813)  (= pi exactly, to 0.0e+00)
  P1 x=uniform-Im(O)  s=e12 [comparability]            = 3.141593  nearest: 2pi/9 (0.69813)  (= pi exactly, to 0.0e+00)
  P1 x=uniform-O      s=e8  [principled]               = 1.961941  nearest: 2pi/9 (0.69813)
  P1 x=uniform-O      s=e4  [comparability]            = 2.601173  nearest: 2pi/9 (0.69813)
  P1 x=uniform-O      s=e12 [comparability]            = 2.808119  nearest: 2pi/9 (0.69813)
  P2 principal angle Im(H0),Im(H1)  x7 [principled]    = 1.047198  nearest: 2pi/9 (0.69813)  (= pi/3 exactly, to 2.2e-16)
  P3 leakage z from e1 [principled]                    = 0.785398  nearest: 2pi/9 (0.69813)  (= pi/4 exactly, to 2.2e-16)
  P3 leakage z from e2 [principled]                    = 0.785398  nearest: 2pi/9 (0.69813)  (= pi/4 exactly, to 2.2e-16)
  P3 leakage z from e3 [principled]                    = 0.785398  nearest: 2pi/9 (0.69813)  (= pi/4 exactly, to 2.2e-16)
  P3 leakage z from e5 [principled]                    = 0.785398  nearest: 2pi/9 (0.69813)  (= pi/4 exactly, to 2.2e-16)
  P4 dim Fix(psi)/dim S = 2/16 [principled]            = 0.125000  nearest: 1/9 (0.11111)
  P4 dim C / dim O = 2/8    [principled]               = 0.250000  nearest: 2/9 (0.22222)
  P4 pairwise intersection / halving = 1/8 [principled] = 0.125000  nearest: 1/9 (0.11111)

comparisons: 20; principled: 12; hits on 2/9 within 0.003: 0
```

## What it says

**Zero hits on 2/9, on the correct triple.** The route is closed for the
generation frame as well as the colour frame, and my 2026-09-12 caution that it
might not be was over-cautious.

**The closure is now stronger than M's, not merely equal to it.** Every
principled angle but one is an exact rational multiple of pi, to machine
precision: the relative phase under psi is 2pi/3 for an imaginary unit of a
halving and pi/3 for the real-imaginary mixture, and the cross-halving leakage
is pi/4. The single exception, `uniform-O` at 1.961941, is the one vector that
mixes the real part into the phase, so it is not a symmetry angle at all; it is
also nowhere near 2/9. This is exactly the signature the 2026-09-11T1600
natural-angle scan predicted a discrete symmetry would leave, and 2/9 radians
is not of that form. The generation frame does not merely fail to contain 2/9;
it is the wrong kind of object to contain it.

**The frame misalignment is pi/3 with multiplicity seven.** All seven principal
angles between Im(H_0) and Im(H_1) are equal, to 2e-16. The two generation
frames are maximally degenerate in their misalignment -- one angle, not seven.

**The pi/4 leakage survives the two-triples correction.** M found the bare
cross-algebra vertex at exactly pi/4 on the colour triple; the same value
appears on the psi-orbit for all four canonical zero divisors. So the
maximal-mixing verdict, and with it notebook N's pre-registered first
hypothesis and op:up-quark's route-closure clause, are unaffected in that
respect -- the flag the corrections ledger attaches to them can be discharged
for the value, though the interpretation still re-points to the psi-orbit.

## Proposed ledger entries

### invalid_routes.md, dated 2026-09-12

- The generation frame of the psi-orbit, as a source of delta_0 = 2/9. Re-run
  of notebook M's basket on the halvings O, psi(O), psi^2(O): twenty
  comparisons, twelve principled, zero hits. The principled angles are
  2pi/3, pi/3 and pi/4 exactly, to 2e-16. Supersedes the caution entered
  earlier the same day: the earlier entry was right that M scanned the colour
  triple, wrong to infer that the generation triple might still supply the
  number.

### results_ledger.md, dated 2026-09-12

- **STRUCTURAL** `[PROPOSED]` The three halvings O, psi(O), psi^2(O) of the
  sedenions meet pairwise in the real line alone, and the seven principal
  angles between the imaginary parts of any two are all equal to pi/3. The
  generation frames are misaligned by a single angle, not seven.
- **ESTABLISHED** `[PROPOSED]` The bare cross-halving zero-divisor leakage is
  pi/4 exactly, for all four canonical zero divisors -- the same value notebook
  M measured on the colour triple. Maximal mixing is a property of the doubling
  step, not of which triple is scanned.

## Not done

No build; nothing in the paper was touched. The corrections ledger's item 4,
the flag on op:up-quark's route-closure clause, is now answerable on the
evidence above but is JS's wording to settle.
