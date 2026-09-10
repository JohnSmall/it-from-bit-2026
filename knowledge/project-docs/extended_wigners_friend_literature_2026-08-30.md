# The Extended Wigner's Friend Literature: Survey and Positioning (2026-08-30)

Session document. Purpose: JS asked what the "extended Wigner's friend" (EWF) literature reveals,
noting that none of it mentions Hopf fibrations or sedenions. This note surveys the field
(web-verified 2026-08-30 except where flagged VERIFY-CITE = from memory), maps each argument's
assumptions onto the framework's commitments, records the gap the framework occupies, and lists
the risks and the recommended Paper 1 actions. Status vocabulary as usual. Nothing here is
patched into the paper; the positioning splice is a decision for JS (section 10).

## 1. The landscape: six arguments, one taxonomy

The field's organising reference is the Schmid-Ying-Leifer review (arXiv:2308.16220,
SEARCH-VERIFIED), which unifies six EWF arguments: Brukner's no-go for observer-independent
facts (Entropy 20, 350 (2018)); the Local Friendliness (LF) theorem of Bong et al. (Nature
Physics 16, 1199 (2020)); the Pusey-Masanes argument (same setup as LF, metaphysical
assumptions, systematised by the review); Frauchiger-Renner (Nature Communications 9, 3711
(2018) -- already in the library as Frauchiger_2018); Gao's argument (sequential measurements
plus a shared pair); and Guerin et al.'s (sequential measurements on a single system, no
entanglement needed -- "no-go for the persistent reality of the friend's perception",
Communications Physics 4, 93 (2021), VERIFY-CITE). Two structural findings of the review matter
most for us. First, none of the six invokes classical-realism assumptions; they are pitched as
stronger in kind than the classical no-gos. Second -- their headline diagnostic -- every one of
the six hinges on assumptions about correlations between measurement outcomes that are NOT
ACCESSIBLE TO ANY OBSERVER, EVEN IN PRINCIPLE; and the authors conclude that the most compelling
reading of the strongest theorems is that measurement outcomes are PERSPECTIVAL rather than
absolute. That is the framework's chart-relativity, stated by outsiders with no stake in it.

## 2. The Local Friendliness line (the sharpest edge)

LF = the conjunction of Absoluteness of Observed Events (AOE: any event observed by any observer
has an absolute, not relative, value) and Local Agency (interventions uncorrelated with events
outside their future light cone). These are STRICTLY WEAKER than Bell's assumptions -- AOE is
contained in Bell's realism, Local Agency in local causality -- so LF violation bounds reality
more tightly than Bell violation (Cavalcanti-Wiseman, Entropy 23, 925 (2021), causal-principles
reformulation; SEARCH-VERIFIED). Proof-of-principle photonic experiments exist: Proietti et al.
tested the Brukner-type inequality (Science Advances 5, eaaw9832 (2019), VERIFY-CITE), Bong et
al. tested LF proper with a photonic qubit as each "friend". The line has since been sharpened
in every direction: a possibilistic version needing no probability theory, weaker still
(Haddara-Cavalcanti, New J. Phys. 25 (2023), VERIFY-CITE for the number); "events in quantum
mechanics are maximally non-absolute" (Moreno-Nery-Duarte-Chaves, Quantum 6, 785 (2022));
timelike-scenario limits on AOE (Phys. Rev. Research, April 2026, SEARCH-VERIFIED as existing);
LF inequalities derived from Kochen-Specker noncontextuality with the LF polytope equal to the
Bell polytope in wide ranges (Quantum 9, 1819 (2025)); a Noncontextual Friendliness variant
(arXiv:2502.02461); and connections to nonclassical causal compatibility, MONOGAMY RELATIONS,
and fine-tuning (Ying-Ansanelli-Di Biagio-Wolfe-Schmid-Cavalcanti, Quantum 8, 1485 (2024)) --
the monogamy connection is a to-read against the paper's own budget/monogamy aside.

## 3. The observer question, and the field's graded turn

The original LF paper was deliberately noncommittal on what counts as an observer. The line's
response has been to make observerhood the experimental variable -- which is precisely the
framework's graded FANOUT, arrived at independently and operationally.

- Wiseman-Cavalcanti-Rieffel, "A 'thoughtful' Local Friendliness no-go theorem" (Quantum 7,
  1112 (2023), SEARCH-VERIFIED): takes "having thoughts" as sufficient for observerhood, derives
  LF from four assumptions (three thought-related, one called Friendliness), and proposes the
  target experiment: a human-level artificial intelligence running reversibly on a large
  universal quantum computer as the friend. Explicitly designed to give experimentalists a goal.
- Russo et al., "Towards violations of Local Friendliness with quantum computers" (Quantum 9,
  1851 (2025), arXiv:2409.15302, SEARCH-VERIFIED; VERIFY-AUTHORS for the full list): encodes the
  EWF scenario as circuits, runs it on IBM, Quantinuum and Braket hardware, and proposes the
  "BRANCH FACTOR" as a statistical measure of the friend's "observerness", demonstrating LF
  violations (with loopholes) at branch factor 16 -- the highest yet -- using GHZ-state friends
  to scale the branch, and asking outright: what is the branch factor of a photon detector, the
  human eye, the human brain? An explicit experimental programme of LF violations at increasing
  branch factor on increasingly powerful processors.
- Adjacent: Xu-Steinberg-Nguyen-Guehne, a no-go from Wigner's incomplete information about his
  friend (Phys. Rev. A 107, 022424 (2023)); Baumann-Brukner on the friend's memory and
  no-signalling (arXiv:2305.15497); Baumann on classical information and collapse in WF setups
  (Entropy 25, 1420 (2023)); "Emergence of classicality in Wigner's friend scenarios"
  (arXiv:2507.21221, 2025) -- when do Wigner's and the friend's probability assignments
  converge, i.e. the field's version of the high-redundancy limit.

The kinship is exact and should be said plainly: the branch factor is a laboratory-internal
instance of the framework's redundancy parameter R (the number of degrees of freedom into which
the outcome has been copied); the framework's claims -- LF violation available at any finite R
where the un-copying can actually be performed, difficulty growing with R, absoluteness the
asymptotic limit, the whole boundary graded with no metaphysical threshold, the grading priced
thermodynamically at kT ln 2 per stabilised copy -- are exactly the shape the experimental
programme presupposes, and the framework supplies the mechanism the programme currently lacks.
And the hardware kinship is direct: the branch-factor experiments run on the same IBM devices
as the paper's own executed Cabibbo and interference circuits.

## 4. The Frauchiger-Renner line

FR assumptions: (Q) universal validity of quantum theory, (C) consistency of inferences chained
across agents, (S) single outcomes; the contradiction requires an agent's measurement to be
UNDONE while inferences conditioned on its outcome are retained. Diagnoses in the literature:
Nurgalieva-Renner formalise the failure as a breakdown of the trust axiom in multi-agent
epistemic logic when memories are manipulated (Contemp. Phys. 61 (2020), VERIFY-CITE;
Nurgalieva, ETH PhD thesis 2023); Walleghem-Barbosa-Pusey-Weigert refine FR via strong
contextuality (arXiv:2409.05491); the review classifies FR's assumptions as epistemological
where Pusey-Masanes's are metaphysical. CORPUS STATUS: Frauchiger_2018 is cited in the
self-reference section's lineage subsection, which PROMISES that sec:wigners-friend "dissolves
[it] relationally rather than paradoxically" -- but the WF section never mentions FR. A referee
will find that promissory note. The framework's actual answer is already built: an inference
transported through an un-done FANOUT has no carrier -- the record it conditioned on has been
recovered into the fibre and no longer exists at base level; (C) holds along persisting records
and only along them. This is the geometric form of Nurgalieva-Renner's diagnosis, with
Proposition f1-dictionary as the mechanism (obsolescence-as-cancellation).

## 5. Responses and dissent (the debate the paper should not pretend is settled)

Relational QM answers with relative facts (Di Biagio-Rovelli, already cited) -- attacked by
Lawrence-Markiewicz-Zukowski, "Relative facts do not exist..." (Quantum 7, 1015 (2023),
VERIFY-CITE), with replies from Cavalcanti-Di Biagio-Rovelli and comment by Brukner (VERIFY);
Zukowski-Markiewicz argue premeasurements have no results (Phys. Rev. Lett. 126, 130402 (2021),
VERIFY-CITE). QBism answers agent-locally (DeBrota-Fuchs-Schack, "Respecting one's fellow",
Found. Phys. 50, 1859 (2020), VERIFY-CITE). Bohmians answer with a preferred account
(Lazarovici-Hubert, Sci. Rep. 9, 470 (2019), VERIFY-CITE); Everettians deny (S). Copenhagenish
positions are systematised in Leifer et al. (arXiv:2506.00112, 2025). On the sceptical side,
Okon argues both Brukner's theorem and LF fail to impose significant constraints (Entropy 27,
563 (2025), SEARCH-VERIFIED); Adlam dissects what "(non)-absoluteness of observed events" even
means (Found. Phys. 54, 13 (2024)). The framework should cite the dissent: its own claims do
not stand or fall with the theorems' maximal readings, because the framework's denial of
absolute low-R facts is derived from its own machinery, not imported from the no-gos.

## 6. The gap (JS's observation, verified)

Targeted searches ("Wigner's friend" + Hopf fibration; + octonions/sedenions/division algebras)
return NOTHING connecting the EWF literature to the Hopf tower or the Cayley-Dickson ladder.
The only intersection of "Wigner" and octonions the search surfaces is the historical one:
Jordan-von Neumann-Wigner 1934 -- Wigner's own name is on the paper that opened octonionic
quantum mechanics, a footnote the paper is entitled to enjoy. Structurally, the whole EWF
literature treats agents as INTERCHANGEABLE and the chain as combinatorially extendable but
STRUCTURELESS: more friends and more superobservers strengthen the theorems, and no property of
the world depends on which rung of the chain an agent occupies. Absent from the literature,
therefore, is everything the framework's treatment consists of: (i) a geometric bookkeeping of
what a superobserver can and cannot recover (fibre vs base); (ii) a physical grading parameter
for the boundary with a thermodynamic price (though the branch-factor programme has begun
inventing it operationally); (iii) any connection between the observer chain and PHYSICAL
CONTENT -- that the fourth wire carries a flavour label and the fifth and later carry only
copies (sec:wf-chain-type; notebook T) has no analogue, or competitor, anywhere in the field.

## 7. The assumption map (where the framework sits, precisely)

- AOE: DENIED at finite R, RECOVERED asymptotically as R grows -- a quantitative AOE. The
  framework predicts LF violation at every finite branch factor where the un-copying is
  actually performable, with difficulty (and Landauer cost of the record's stabilisation)
  growing in R; "absolute" is the limit, never a threshold crossed. This is a prediction the
  branch-factor programme can track, not a metaphysical posture.
- Local Agency: KEPT. Nothing in the framework touches it.
- FR's (Q): kept as the pre-FANOUT description; (S): kept per chart; (C): restricted to
  inferences carried by persisting records -- the restriction is derived (f1-dictionary), not
  postulated.
- The review's diagnostic ("all six arguments hinge on correlations between outcomes not
  accessible to any observer, even in principle"): the framework has a home for exactly this
  class -- such correlations involve fibre-committed or fibre-recovered data, which are not
  merely inaccessible but UNDEFINED at base level once the record is gone. The theorems'
  load-bearing assumptions are assumptions about quantities the framework's ontology declines
  to define; that is why the framework violates their conclusions without paradox.
- "Outcomes are perspectival" (the review's preferred reading): the framework's two charts on
  one manifold, with the addition the literature lacks -- an exact statement of what the
  perspectives share (the base; everything both can check) and what they cannot (the fibre),
  and a parameter for when perspectives merge (R large).

## 8. What the framework adds (the claim, stated at the right size)

Not a new resolution of the paradox -- the perspectival conclusion is common property, and the
paper should say so with citations. What is new: the geometry (which datum lives where, and why
Wigner's recovery is bounded by exactly the fibre), the grading (R, with thermodynamic
pricing, meeting the branch-factor programme from the theory side), and above all the PAYLOAD:
the chain of observers is unbounded in length and bounded in type, with the bound located by
the division algebras -- forces at three wires, one family label at the fourth, copies
thereafter. The EWF literature extends the chain to strengthen no-go theorems; the framework
extends it and finds the Standard Model's generation structure. That is a different genre of
claim, and it is the paper's to make.

## 9. Risks

(a) Genre risk: leaning on the no-gos as if they proved the framework. They do not; they carve
the assumption space, and dissent (Okon; the relative-facts controversy) is live. The paper
should position, not recruit. (b) The relative-facts attack on RQM transfers: the framework
must (and can) answer Lawrence et al. with the no-disagreement-on-checkables theorem -- the
charts agree on everything both can check, which is exactly what the attack claims relative
facts cannot secure; worth one sentence with citations. (c) Experimental risk runs the right
way: LF satisfaction at low branch factor would contradict quantum theory itself, and LF
violation at growing branch factor is the framework's prediction; the framework is not
falsified by the programme's success but calibrated by it. The genuinely exposed claim is
gradedness -- evidence of a SHARP observer threshold (e.g. violations vanishing
discontinuously at some system class with reversal still performable) would wound the
R-grading. No such evidence exists. (d) VERIFY-CITE discipline: several references above are
from memory; the refs-first gate applies before any of this enters the paper.

## 10. Recommended Paper 1 actions (JS's decision)

1. A short positioning passage -- likely in sec:wf-reconciliation, or a compact new subsection
   before sec:wf-chain-type -- doing four things: (i) name the landscape through the six-
   argument review; (ii) state the framework's location in assumption space (graded AOE; Local
   Agency kept; C restricted to persisting records) with the fibre/base reading of the
   "inaccessible correlations" diagnostic; (iii) meet the branch-factor programme explicitly as
   the experimental face of R, noting the shared hardware with the paper's own circuits; (iv)
   DISCHARGE the self-reference section's FR promissory note by name. Two paragraphs suffice.
2. Import the RIS batch (extended_wigners_friend_refs_2026-08-30.ris; all keys VERIFY-flagged).
3. Optionally, one sentence in sec:wf-chain-type noting that the EWF literature's chain is
   structureless while this one is not -- the coda already carries the content, so this is
   flavour only.
