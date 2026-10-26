# op:parallelisable-renormalisable, attempted: the self-energy as a winding sum

Date: 2026-09-27T1100. Fable session, at JS's instruction ("try the
computation you suggested"), the day after proposing it (Tang reading note,
section 7). Script `scripts/self_energy_winding_recast_2026-09-27T1100.py`,
exact stdout in section 4. Result: **FAIL** for every recasting tried, with an
analytic reason that closes the finiteness reading of the guess and leaves
the paper's renormalisability question exactly where the paper put it.

## 1. What was tried

The problem as proposed: recast the one-loop electron self-energy as a closed
computational path, a sum over windings on a compact fibre with a bounded
phase, and see whether the ultraviolet divergence goes without a cutoff put
in by hand. Four recastings, against a baseline.

- *Baseline.* The one-loop mass shift with a Euclidean cutoff $\Lambda$,
  Feynman gauge, on shell: $\delta m/m = (3\alpha/4\pi)\ln(\Lambda^{2}/m^{2}) +
  5\alpha/4\pi$, quadrature against the closed form to eight figures, slope
  $3\alpha/4\pi = 0.00174211$ per unit of $\ln\Lambda^{2}$. Logarithmic.
- *Recasting 1, the loop as a closed path in time.* Euclidean time on a circle
  of circumference $\beta$ turns the frequency integral into a winding sum
  over Matsubara frequencies: the loop is literally a closed timelike curve
  in Euclidean signature, which is Hawking's CTC bath and the framework's
  "closed computational path" in its most direct form. On the scalar analogue
  with the same divergence, $\int d^{4}k/(k^{2}+m^{2})^{2}$, and the same
  four-dimensional cutoff region, the winding sum and the continuous integral
  have the same slope, $\pi^{2}$ per unit $\ln\Lambda^{2}$, at every $\beta$;
  their difference converges to a finite $\beta$-dependent constant
  ($23.150$ at $\beta m = 1$, $0.146$ at $5$, $0$ at $20$). The winding sum
  discretises the modes and adds a finite thermal part; it removes nothing.
- *Recasting 2, the phase bounded modulo $2\pi$.* By inspection: in Minkowski
  signature the loop weight $e^{iS}$ already has modulus one for every mode,
  so reducing $S$ modulo $2\pi$ is the identity on it. What diverges is the
  integral of the modulus over the modes, the number of modes, not the
  range of the phase.
- *Recasting 3, a compact momentum space.* $S^{3}$ of radius $\Lambda$ with
  $\Lambda$ one of the framework's own scales gives a finite shift,
  $\delta m/m = 0.058$ at $3.6$ TeV and $0.182$ at the Planck grain, and no
  prediction: the shift is absorbed into the measured mass and every
  cutoff-independent observable is unchanged. This is a cutoff by hand, the
  problem's own FAIL criterion.
- *The finite quantity.* The Schwinger term $\alpha/2\pi = 0.001161410$ needs
  none of this; it is the target for a framework-native vertex computation
  and is untouched here.

## 2. The reason, in one sentence

A compact fibre bounds the phase and discretises the modes; the ultraviolet
divergence is the number of modes. Parallelisability, Adams and the Hopf
tower say what can be transported consistently around a loop, not how many
modes run in it, and no recasting of the loop as a path on $S^{1}$, $S^{3}$
or $S^{7}$ touches the second. This is the standard objection to
division-algebra field theories, now checked rather than cited: the
divergence lives in the momentum measure.

## 3. What this settles and what it does not [labels proposed]

- **ESTABLISHED (computation).** The finiteness reading of the guess, "only
  division-algebra theories can have their infinities removed by recasting
  them as transport on parallelisable spheres", fails for the three
  recastings that make it concrete. Tang's claim of a finite, unrenormalised
  QED is the same reading and fails for the same reason, in addition to the
  Yukawa error already noted.
- **Untouched.** The paper's actual question, "does parallelisability
  determine renormalisability?", is about removability, not finiteness, and
  none of this bears on it: whether the divergences of the $S^{1}, S^{3},
  S^{7}$ gauge theories are removable *because* those spheres are
  parallelisable, and gravity's irremovable because its sphere is not, is
  not a statement about a loop integral being finite. The paper's wording,
  "a direction, not a claim", stands unchanged.
- **CANDIDATE, one remark worth keeping.** In the two-columns vocabulary the
  divergence is an unbounded *real* cost the loop would carry if every mode
  were a record; renormalisation pays it once at the record, the measured
  mass, and the counter-term is the settled debt. That is a reading of why
  the divergence is harmless, not of why it is absent, and it is consistent
  with the FAIL above rather than in tension with it: the framework's cost
  accounting says a bare loop is not a record and its cost is not physical
  until settled, which is what renormalisation says in other words. Whether
  this reading can be turned into the removability criterion the paper asks
  for is the surviving form of the problem.
- op:parallelisable-renormalisable should therefore be restated before it is
  minted: drop the finiteness PASS; ask instead for a structural derivation
  of removability (the counter-terms of a gauge theory on a parallelisable
  fibre are finitely many and settle at the record) and its failure for
  gravity. No route is proposed for that here.

## 4. Exact stdout of `scripts/self_energy_winding_recast_2026-09-27T1100.py`

```
=== Part A: baseline, the one-loop mass shift with a Euclidean cutoff (m = 1) ===
  Lambda/m     quadrature    closed form
     1e+01     0.01092625     0.01092626
     1e+02     0.01894899     0.01894899
     1e+03     0.02697172     0.02697173
     1e+04     0.03499446     0.03499446
     1e+05     0.04301719     0.04301720
slope per unit ln(Lambda^2): 0.00174211 ; 3 alpha/4 pi = 0.00174211 ; logarithmic divergence confirmed

=== Part B: the loop as a closed path in time (winding sum) against the continuous loop ===
  Lambda/m   continuous      beta m = 1      beta m = 5     beta m = 20
     1e+01     35.77753        59.07390        35.92237        35.77758
     1e+02     81.03479       104.18496        81.18122        81.03479
     1e+03    126.48404       149.63427       126.63046       126.48404
     1e+04    171.93523       195.08546       172.08165       171.93523
differences winding minus continuous (should converge to a finite, beta-dependent constant):
     1e+01         23.29637         0.14485         0.00005
     1e+02         23.15017         0.14643        -0.00000
     1e+03         23.15023         0.14642         0.00000
     1e+04         23.15023         0.14642         0.00000
slope per unit ln(Lambda^2), continuous: 9.86960 ; winding (beta m = 5): 9.86960 ; pi^2 = 9.86960
VERDICT B: the winding sum discretises the loop frequency and adds a finite thermal part; the logarithmic divergence is unchanged. FAIL.

=== Part C: the phase bounded modulo 2 pi ===
In Minkowski signature the loop weight exp(i S) is already of modulus one for every mode; reducing S modulo 2 pi is the identity on it.
The divergence is the integral of the modulus over the modes, i.e. the number of modes, not the range of the phase. No computation changes this. FAIL by inspection.

=== Part D: a compact momentum space, radius fixed by the framework's own scales (electron) ===
matching scale 3.6 TeV   delta m / m = 0.0578 (finite)
Planck grain             delta m / m = 0.1824 (finite)
finite, but not a prediction: the shift is absorbed into the measured mass, and every cutoff-independent observable is unchanged by the choice. A cutoff put in by hand. FAIL by the problem's own criterion.

=== Part E: the finite one-loop quantity ===
Schwinger term a_e = alpha/2 pi = 0.001161410 ; ultraviolet finite with no recasting; the target for any framework-native vertex computation
```
