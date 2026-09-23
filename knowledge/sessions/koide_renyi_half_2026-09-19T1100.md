# The Koide ratio as an entropy of order one half: what the identity says and does not say

Date: 2026-09-19T1100. Fable session, at JS's request to expand the remark in
`project-docs/two_columns_shannon_thermodynamics_action_2026-09-18T1200.md`
section 7 that "the Koide ratio is exactly the exponential of minus the
Rényi entropy of order one half of the mass fractions". Computation:
`scripts/koide_renyi_profile_2026-09-19T1100.py`, exact stdout in section 7.
Labels proposed; the ledger's existing entries on Koide (2026-09-10 and
2026-09-11) are the context and nothing here supersedes them.

## 1. The identity

Write $p_k = m_k/\sum m$ for the mass fractions and $q_k = \sqrt{m_k}/\sum\sqrt{m}$
for the amplitude-level distribution, the $p_k$ of the 2026-09-11 fit-free
reading. The Rényi entropy of order $a$ is $H_a(p) = \frac{1}{1-a}\ln\sum p_k^{a}$.
At $a = 1/2$,

$$H_{1/2}(p) = 2\ln\sum_k\sqrt{p_k} = \ln\frac{(\sum\sqrt{m})^{2}}{\sum m} = -\ln K ,$$

so $K = e^{-H_{1/2}(p)}$ identically, for any three positive numbers. Also
$\sum q_k^{2} = \sum m/(\sum\sqrt m)^{2} = K$, so $K = e^{-H_{2}(q)}$: the
same number is the collision entropy of the amplitude distribution. The
ledger's "K = sum p_k^2" of 2026-09-11 is this second form. Part A: on PDG
2024 central values, $H_{1/2}(p) = 0.40546841$ against $\ln(3/2) =
0.40546511$, the difference $3.3\times10^{-6}$ nats being the $K - 2/3$ of the
data. Koide's relation is therefore the statement

$$H_{1/2}(p) = \ln 3 - \ln 2 ,$$

the max-entropy of the charged-lepton mass fractions is one bit below the
value $\ln 3$ of three equal masses; equivalently the effective number of
generations at order one half is $3/2$. Since $3/2$ is the harmonic mean of
$1$ and $3$ and $2/3$ the arithmetic mean of $1/3$ and $1$, this is Koide's
original "halfway between one generation and three" said in one more way.

## 2. Four equivalent forms [STRUCTURAL as arithmetic]

All four are the same equation $\alpha^{2} = 2$; the value of listing them is
that each names the one half as a familiar quantity.

*Foot's angle.* The fidelity of $p$ with the uniform distribution is
$F^{2} = \frac13(\sum\sqrt{p_k})^{2} = 1/(3K)$, so $K = 2/3$ is $F^{2} = 1/2$:
the vector $(\sqrt{m_e}, \sqrt{m_\mu}, \sqrt{m_\tau})$ makes an angle of
exactly $45^{\circ}$ with $(1,1,1)$ (Part A: $44.999905^{\circ}$). This is the
known geometric form of Koide's relation (Foot 1994, hep-ph/9402242,
verified 2026-09-20: the preprint was read and gives
$\theta = 45.000 \pm 0.001$ degrees, with $\cos\theta > 1/\sqrt{3}$, i.e.
$\theta < 54.7$ degrees, as Koide's bound). In the framework's vocabulary the square-root-mass vector and
the democratic vector are mutually unbiased, the same $1/2$ that the
2026-09-11 reading of $\alpha = \sqrt2$ assigns to each pair of generation
states.

*Negativity.* A pure bipartite state with Schmidt coefficients $\sqrt{p_k}$
has negativity $N = ((\sum\sqrt{p_k})^{2} - 1)/2$, and $e^{H_{1/2}} = 1 + 2N$;
Koide is $N = 1/4$ (Part A: $0.25000248$). Recorded because the framework's
objects are entanglement classes; not pursued, since no bipartition of the
generation register is on offer.

*Purity of the democratic mixture.* Let the three generation states have
Gram matrix $G$ (unit diagonal, off-diagonal modulus $1/\sqrt2$, Bargmann
phase $\Phi = 3\delta$). The frame operator $\sum_k|\psi_k\rangle\langle\psi_k|$
has the spectrum of $G$, so $\rho = \frac13\sum_k|\psi_k\rangle\langle\psi_k|$,
the equal mixture of the three generation states, has spectrum $g_k/3 = q_k$:
the amplitude-level distribution *is* the spectrum of the democratic mixture
(Part C, to $10^{-15}$). Then $K = \sum q_k^{2} = \mathrm{Tr}\,\rho^{2}$ is
its purity, and $\mathrm{tr}\,G^{2} = 3 + 2\sum_{j<k}|\langle\psi_j|\psi_k\rangle|^{2} = 6$
gives $K = 6/9$ with no reference to the phase. Three orthogonal states would
give purity $1/3$, three identical states $1$; pairwise unbiased states give
$2/3$. This is, I take it, the content of the ledger's "equal-weight frame
reading" (2026-09-10, CANDIDATE), now with the entropy named: the collision
entropy of the democratic mixture is $\ln(3/2)$.

*The power sums.* With $q_k = (1 + \alpha c_k)/3$, $c_k = \cos(\delta + 2\pi k/3)$:
$\sum q = 1$; $\sum q^{2} = (1 + \alpha^{2}/2)/3$, which depends on $\alpha$
only; $\sum q^{3} = \frac{1}{27}\big(3 + \tfrac92\alpha^{2} + \tfrac34\alpha^{3}\cos 3\delta\big)$,
which is where the invariant phase first appears (Part B, formula checked
to eight figures at five values of $\delta$; Part C, $\mathrm{tr}\,G^{3} = 12 +
\tfrac{3\sqrt2}{2}\cos 3\delta = 13.66711863$). In Gram language the
quadratic trace counts pairwise overlaps and the cubic trace contains the
cyclic product $G_{12}G_{23}G_{31}$, the Bargmann invariant. Added
2026-09-20, after JS's remark that adding the surprisal of an amplitude to
that of its conjugate is just $|\psi|^{2}$: that is the mechanism of the
blindness. $\mathrm{tr}\,G^{2} = \sum_{jk}G_{jk}G_{kj} = \sum|G_{jk}|^{2}$ is
a sum over two-step loops $j \to k \to j$, each an overlap times its own
conjugate, phase-free by the Born rule; $\mathrm{tr}\,G^{3}$ is a sum over
three-step loops whose reverse is a different loop, and carries
$2|G_{12}G_{23}G_{31}|\cos\Phi$ because the loop and its reverse are added,
not multiplied.

## 3. What is new in it, and it is small [CANDIDATE]

The one fact not already in the ledger is the blindness. $H_{1/2}(p)$ is
constant at $\ln(3/2)$ as $\delta$ ranges over the whole positivity window
$|\delta| \le \pi/12$ (Part B), while the Shannon entropy and the order-$3/2$
entropy move with it. So the entropy of order one half sees the amplitude
$\alpha$ and nothing of the phase; the phase enters the spectrum's
invariants first at cubic order, through $\cos 3\delta$. In the two-columns
vocabulary: the quadratic invariant of the generation triple (the purity, an
overlap-squared, real column) fixes the Koide ratio, and the cubic invariant
(the Bargmann phase, imaginary column) fixes where the three masses sit at
that ratio. The 2026-09-11 division of labour, "$\alpha$ for the ratio
$K$, $\delta$ for the ratios themselves", is now the statement that $K$ is a
Rényi entropy blind to the phase and the individual masses are not.

Why order one half and not one. Because the natural variable is $\sqrt{m}$,
Koide's own insight, and a Rényi entropy of order one half of the
probability-level distribution is a Shannon-type quantity of the
amplitude-level one: $2\ln\sum\sqrt{p}$ is the log of a sum of amplitudes,
the max-entropy of single-shot information theory (König, Renner and
Schaffner 2009, verified 2026-09-20 against Crossref
10.1109/TIT.2009.2025545; body not read), the same order at which the complex cost's real
part lives (two-columns note, section 5). That the Koide data are simplest at
this order is one more sign that the framework's amplitude-level bookkeeping
is the right level for the masses; it is not a derivation of anything.

## 4. What it does not do

It does not derive $\alpha = \sqrt2$: "$H_{1/2} = \ln 3 - \ln 2$" and
"pairwise unbiased" and "$45^{\circ}$" and "purity $2/3$" are one assumption
in four vocabularies, and the ledger already carries it as the CANDIDATE
reading of $\alpha$. It does not touch $\delta$, which op:koide-delta owns
and which no entropy of the mass fractions of order one half can see. It
does not open a route and should not be added to invalid_routes, since a
re-description cannot fail a PASS/FAIL test. It should not go in the paper
beyond, at most, one clause beside the $\alpha = \sqrt2$ reading: "the
democratic mixture of the three generation states has purity $2/3$, which is
the Koide ratio; its collision entropy is one bit below maximal and is blind
to the phase". JS's call.

## 5. One question it sharpens, not answers

A principle that fixed the purity of the democratic mixture of generation
states at $2/3$ would derive $\alpha = \sqrt2$ and the Koide ratio at once.
"Pairwise mutually unbiased" is such a principle stated on the states; "one
bit of max-entropy below democracy" is the same principle stated on the
spectrum. Whether either follows from the framework's $S_3$ component group
acting on three copies of $\mathbb{C}$ in $\mathbb{O}$ is the question the
Jordan reading (prop:koide-jordan) already poses; this note adds no route to
it, only the observation that the target number is an entropy of the
simplest kind, one bit.

## 6. Proposed ledger entries

- **STRUCTURAL** (arithmetic) $K = e^{-H_{1/2}(p)} = e^{-H_{2}(q)}$; at
  $K = 2/3$, $H_{1/2}(p) = \ln 3 - \ln 2$, the mass-root vector is at
  $45^{\circ}$ to $(1,1,1)$ (Foot), and the equal mixture of the three
  generation states has purity $2/3$ with spectrum $q_k$. Verified on PDG
  2024 and on an explicit Gram matrix to $10^{-15}$.
- **STRUCTURAL** (arithmetic) $H_{1/2}(p)$ depends on $\alpha$ only,
  $\sum q^{2} = (1 + \alpha^{2}/2)/3$; the phase $3\delta$ first enters the
  spectrum's power sums at cubic order, $\sum q^{3}$, through
  $\mathrm{tr}\,G^{3}$ and the Bargmann invariant.
- **CANDIDATE** The reading: the quadratic (real-column) invariant of the
  generation triple fixes the Koide ratio, the cubic (imaginary-column)
  invariant fixes the individual masses; the Koide relation is a max-entropy
  statement, one bit below democratic, at the amplitude level where the
  framework does its bookkeeping. Refines, does not replace, the 2026-09-10
  "equal-weight frame reading" and the 2026-09-11 reading of $\alpha = \sqrt2$.
- **RHYME** $N = 1/4$ for the Schmidt state; $3/2$ as the harmonic mean of
  $1$ and $3$.
- References, verified 2026-09-20 and batched in
  `bib/koide_renyi_refs_2026-09-20T2200.bib`: Foot, "A note on Koide's
  lepton mass relation", hep-ph/9402242 (1994), read in full, and never
  published in a journal, so it is an `@online` entry; König, Renner and
  Schaffner, "The operational meaning of min- and max-entropy", IEEE Trans.
  Inf. Theory 55(9), 4337--4347 (2009), doi 10.1109/TIT.2009.2025545, body
  not read. Neither was already in the library.

## 7. Exact stdout of `scripts/koide_renyi_profile_2026-09-19T1100.py`

```
=== Part A: PDG 2024 central values (MeV) ===
K = 0.66666446 ; sum q^2 = 0.66666446 ; exp(-H_1/2(p)) = 0.66666446 ; exp(-H_2(q)) = 0.66666446
H_1/2(p) = 0.40546841 ; ln(3/2) = 0.40546511 ; difference = 3.30e-06 nats
(a) fidelity^2 with uniform = (1/3)(sum sqrt p)^2 = 0.50000165 ; 1/(3K) = 0.50000165 ; angle to (1,1,1) = 44.999905 deg (45 at K = 2/3)
(b) negativity of the Schmidt state = 0.25000248 ; 1 + 2N = 1.50000496 = exp(H_1/2) = 1.50000496
effective numbers: exp(H_1/2(p)) = 1.500005 ; exp(H_1(p)) = 1.244343 ; exp(H_3/2(p)) = 1.156381 ; exp(H_2(q)) = 1.500005
harmonic mean of 1 and 3 = 1.500000 ; arithmetic mean of 1/3 and 1 = 0.666667 = K at Koide

=== Part B: Z3 form sqrt(m_k) = 1 + alpha cos(delta + 2 pi k/3), alpha = sqrt2 ===
   delta            K     H_1/2(p)       H_1(p)     H_3/2(p)        sum q^3        formula
 -0.1500   0.66666667   0.40546511   0.18107305   0.11004273     0.51519025     0.51519025
  0.0000   0.66666667   0.40546511   0.14964637   0.07990693     0.52301186     0.52301186
  0.1000   0.66666667   0.40546511   0.16363211   0.09337096     0.51950277     0.51950277
  0.2222   0.66666667   0.40546511   0.21860446   0.14529271     0.50618958     0.50618958
  0.2500   0.66666667   0.40546511   0.23711240   0.16218851     0.50193135     0.50193135
  0.2618  (a root is non-positive; skipped)
H_1/2(p) is constant at ln(3/2) = 0.40546511 across delta; H_1 and H_3/2 move; sum q^3 carries cos(3 delta)
sum q^2 = (1 + alpha^2/2)/3 in general: alpha = 1.0 gives 0.500000, alpha = sqrt2 gives 0.666667, alpha = 2 gives 1.000000

=== Part C: Gram matrix of three mutually unbiased states with Bargmann phase Phi = 3 delta, delta = 2/9 ===
eigenvalues of G      : 0.04034991 0.58021192 2.37943817
triality form         : 0.04034991 0.58021192 2.37943817
max |difference| = 1.0e-15 ; Bargmann phase arg(G12 G23 G31) = 0.66666667 = 3 delta = 0.66666667
tr G = 3.000000 ; tr G^2 = 6.000000 (= 3 + 6 x 1/2, phase-free) ; K = tr G^2 / (tr G)^2 = 0.66666667
tr G^3 = 13.66711863 ; 12 + (3 sqrt2 / 2) cos(3 delta) = 13.66711863
(c) purity of the equal mixture, Tr rho^2 = 0.66666667 ; spectrum of rho = q_k: 0.013450 0.193404 0.793146 ; q from the triality form: 0.013450 0.193404 0.793146
```
