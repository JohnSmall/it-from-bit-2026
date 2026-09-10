# Session Summary / Onboarding: 2026-07-23 -- p-adics, CTCs, and the division-algebra ledger

Purpose: onboard a fresh conversation. This session opened the non-Archimedean front:
Khrennikov's dormant suggestion (p-adic analysis rehabilitates negative probability) was
crossed with JS's observation that a negative p-adic integer needs infinitely many digits
to the LEFT -- the shadow of an unnamed supertask -- and the task was to find how p-adics
rhyme with CTCs and hence division algebras, first as questions for Khrennikov, then as a
community-facing appendix. Companion documents (referenced, not duplicated):
`appendix_padic_ctc_division_2026-07-23T0617.tex` (the appendix, compile-verified),
`refs_padic_ctc_division_2026-07-23T0617.ris` (15-entry batch, Mendeley import owed).
Sits beside `open_problem_adelic_mass_constraints.md` (engages its Problems 2, 4(b), 4(c);
DISCHARGES its minimal-progress criterion (B) by citation; upgrades NOTHING) and the
continuity appendix `app:continuity-open` (whose Accumulation Lemma, solenoid witness,
Archimedean fork, and dyadic tower eq:dyadic-tower are load-bearing cross-references).

## 1. The thesis: complementarity, not competition

Why the idea languished: p-adic QM was pitched as a RIVAL home for quantum probability.
The framework's reading: Ostrowski's fork assigns the two tines complementary JOBS.
Records are counts of copies, and counting forces the Archimedean place (the Accumulation
Lemma seen from the copy side); the pre-FANOUT ledger, where sign cancellation is
thermodynamically free, owes Archimedes nothing; the adelic product formula
prod_v |x|_v = 1 is the treaty between the two descriptions of one bookkeeping
(Vladimirov-Volovich-Dragovich register). Records at infinity, ledger at the finite
places. STRUCTURAL.

## 2. Proved this session (appendix lemmas/propositions)

(a) DOUBLING LEMMA (`lem:doubling`), dual of the Accumulation Lemma: sum (p-1)p^k
diverges in R and every Q_l (l != p), converges to -1 in Q_p; emblem equation
`eq:fanout-tally`: 1+2+4+8+... = -1 in Q_2, and 2^n -> 0. Rightward digit-infinity
completes at infinity (Zeno/Thomson); leftward completes p-adically (borrowing). A
negative integer is the completed value of a borrowing supertask -- JS's observation now
a convergence statement. (b) FANOUT-BLINDNESS (`lem:fanout-blind`): non-Archimedean iff
|n| <= 1 for all integers; copying never accumulates at finite places; 2-adically an
unbounded doubling cascade has record count -> 0 and tally -> -1. Rereads Ostrowski +
Khrennikov frequency theory + Landauer accounting as three faces of one fork.
(c) CARRY MAP (`prop:carry`): f(x) = px + (p-1); unique fixed point -1 at every place;
REPELLING over R (the divergent supertask), CONTRACTING on Z_p (Banach, orbit p^n - 1).
One equation, two temperaments; Hensel = the general lifting machine.
(d) P-ADIC HOPF QUOTIENT (`prop:padic-hopf`): unimodular pairs -> P^1(Q_p), principal
Z_p^x-bundle; complete invariant of the phase action = the VALUATION |x|_p (the p-adic
Born datum; product formula = distributed Born ledger). Bundle is TRIVIAL
(zero-dimensional base) -- see cautions.

## 3. The ledger theorem (classical, cited) and its corollary

`thm:ledger`: (i) Hilbert reciprocity prod_v (a,b)_v = 1 (= quadratic reciprocity);
(ii) (-1,-1)_v = -1 EXACTLY at v in {2, infinity} -- Hamilton's partner is the prime 2,
the binary place; (iii) ABHN: even ramification, local invariants determine the algebra;
(iv) unique quaternion division algebra over each Q_p (odd p: (u,p) form, NOT (-1,-1));
(v) u(Q_p) = 4 => 8-dim norm forms isotropic => NO division octonions over any Q_p;
(vi) over Q exactly two octonion algebras, distinguished at the real place ALONE.
`cor:cd-tower`: the standard gamma = -1 Cayley-Dickson tower over Q_p splits at the
QUATERNION rung for odd p, survives to H at p = 2 only, splits at the octonion rung
everywhere. Discharges criterion (B) of the adelic document; failure modes DIFFER IN
KIND: real place topological (Hopf invariant one, one rung LATER, sedenions), finite
places arithmetic (u-invariant, one rung EARLIER). Reciprocity = conservation of
obstruction: bump in the carpet, adelic edition. Artin-Schreier inversion (in the Hopf
subsection): R is the unique orderable completion; every Q_p has finite level (s in
{1,2,4}), so POSITIVITY, not negativity, is the exotic (Archimedean-exclusive)
phenomenon.

## 4. Fenced RHYMEs and the CANDIDATE

RHYME 1: "what is a paradox at the Archimedean place is an attractor at the finite
places" -- CTC (geometric device) and p-adic metric (analytic device) as two resolutions
of one self-referential equation; Deutsch exists by Brouwer, Hensel delivers by Banach.
RHYME 2: "the Hopf twist obeys Gauss reciprocity" -- the twist has NO local p-adic
avatar (trivial bundle); its conservation law is global: (-1,-1)_inf = -1 forced to pair
at p = 2. RHYME 3: Tsirelson as ramification at two -- ladder 2, 2 sqrt 2, 4 has
v_2 = 1, 3/2, 2; the quantum bound is the unique half-integral (RAMIFIED) rung; Landau
identity C^2 = 4 - [A,A'] (x) [B,B']; the excess sqrt 2 is carried by the commutator
sector, and the even Clifford algebra C_0(<1,1,1>) = (-1,-1)_Q -- the ledger's algebra.
Upgrades the Vaxjo Khrennikov thread (product formula vs Tsirelson) from slogan to
target computation. CANDIDATE (dictionary reading): the quaternionic/bipartite layer
has a 2-adic shadow (compact unit group of the 2-adic quaternions); the GHZ/octonionic
layer has NONE -- predicts a CHSH/GHZ asymmetry for p-adic modelling.
SOLENOID + DUALITY: loop with p-adically tallied windings = the p-solenoid; adelic
solenoid = Pontryagin dual of Q; JEWEL: dual of the dyadic tower Z(2^inf) of
eq:dyadic-tower is Z_2 -- the prime two's SECOND independent appearance (after
Hamilton's partner). Coincidence or structure = op:padic-solenoid.

## 5. Six open problems (the invitation)

`op:padic-frequency` measurement as Archimedeanisation: FANOUT criterion inside
Khrennikov frequency theory; exhibit one pre-FANOUT cancellation as a p-adically
stabilising collective. `op:padic-hensel` Deutsch consistency as Hensel lifting: which
consistency maps are ultrametric contractions (constructive backend for the closed-loop
reading). `op:padic-ghz` CHSH/GHZ asymmetry: p-adic models of tripartite correlations
-- obstruction = first physical trace of the octonions' non-Archimedean splitting;
model = honest falsifier of the CANDIDATE. `op:padic-reciprocity` make RHYME 2 a
theorem via the Brauer class of (-1,-1)_Q. `op:padic-tsirelson` derive the exponent 3/2
from local invariants, not the operator norm. `op:padic-solenoid` circle or solenoid:
the U(1) exclusions (no-small-subgroups, Cartan) consume RECORD-SIDE Archimedean
premises; does any PRE-record condition distinguish U(1) from its solenoidal
completions? Each engageable without adopting the framework.

## 6. Cautions and closed naive routes (do not retry)

(a) The p-adic Hopf bundle is TRIVIAL: the twist analogy fails locally BY THEOREM;
only the global/reciprocity reading survives. (b) Hermitian anticommuting A, A'
generate the SPLIT algebra M_2 (Hilbert symbol (1,1)), NOT Hamilton; H enters only via
the even Clifford / bivector (commutator) sector -- the naive "CHSH observables
generate H" route is WRONG and closed. (c) The plain count 1, 2, 3, ... converges at NO
place; only the doubling filtration converges 2-adically -- resist the Thomson-lamp
parity temptation (assigning the lamp a 2-adic final state is NOT licensed).
(d) Deutsch's fixed point is compactness-existential; the Hensel rhyme is in ROLE, not
proof mechanism. (e) BRIDGE CONDITION governing everything: adelic identification
needs values in Q or a fixed number field (stabiliser bookkeeping: rational; Tsirelson:
Q(sqrt 2), places above 2). Irrational-in-general quantities must be located in a
number field first.

## 7. Deliverables, verification, owed actions

Appendix: pdflatex PASS x2 in amsthm harness, ASCII PASS, no bullets in prose
(theorem-clause romanettes only, sibling precedent). Nine external labels dangle BY
DESIGN: master `sec:self-reference`, `sec:fanout-boundary`, `sec:born`, `sec:hopf`
(last two = same mapping task as the Jaynes appendix, VERIFY); continuity appendix
`lem:accumulation`, `rem:witnesses`, `app:cont-scalar`, `eq:dyadic-tower`,
`app:continuity-open` (must be in the same document). Master preamble may need
\newtheorem{proposition}[theorem]{Proposition}. A MAIN-BODY INSERT paragraph for
sec:self-reference sits in the header comments. RIS: 15 entries, PASS (one AU per
line, keys in ID, native Unicode -- Gouvea accent, Koerper, fuer); DEDUPE WARNINGS on
import: tsirelson1980, chsh1969. Twelve keys assumed EXISTING (VERIFY): ostrowski1916,
thomson1954, khrennikov1995, khrennikov2009, vladimirovvolovich1989, dragovich1995,
hurwitz1898, adams1960, deutsch1991, aaronsonwatrous2009, laraudogoitia1998,
spekkens2008. OWED (JS): email Khrennikov (the six items; lead with complementarity
reframe and RHYME 3, his product-formula thread); Mendeley import; label mapping;
confirm continuity appendix co-present; optionally a dated addendum to
`open_problem_adelic_mass_constraints.md` recording the criterion-(B) discharge
(statuses unchanged).

## 8. Retrievables (compact facts)

(-1,-1)_v = -1 iff v in {2, inf}. Hilbert reciprocity prod_v (a,b)_v = 1. u(Q_p) = 4.
Levels s(Q_p): 1 (p = 1 mod 4), 2 (p = 3 mod 4), 4 (p = 2); all finite => no order =>
no sign for squared magnitudes. Octonion algebras classified by norm forms
(Jacobson/Springer-Veldkamp); split over every Q_p. Dual of Z(p^inf) = Z_p; dual of
adelic solenoid's building: (R x Zhat)/Z = dual of discrete Q. 1+2+4+... = -1 and
2^n -> 0 in Q_2. Carry map px + (p-1): contraction constant 1/p on Z_p, expansion p on
R. Tsirelson ladder v_2 = 1, 3/2, 2; C_0(<1,1,1>) = (-1,-1)_Q; Landau:
C^2 = 4 - [A,A'] (x) [B,B'].
