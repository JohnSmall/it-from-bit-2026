# The observer is constituted by the selection of $i$ (2026-10-08T1500)

Session 2026-10-08, Fable 5.1. JS: "there is no observer without the
possibility of making an observation and therefore selecting an $i$, making
an observation, is an inseparable part of being an observer, it defines
what it even means to be an observer. This extends Markus Müller's ideas
about the first person perspective." Read against the paper's existing
statements and the day's computations (`woit_right_handed_spacetime_2026-10-08T1000.md`,
sections 3 and 9; `twistor_hopf_maps_2026-10-07T1600.md`, section 4). No
new computation; everything used is already verified. Müller's "Law without
law" abstract read from the arXiv API (body not read; Crossref-verified);
the library has his group's reconstruction papers (`HohnMueller2016`,
`GarnerMuellerDahlsten2017`, `MuellerMasanes2013`, `MasanesMuellerEtAl2014`)
but not this one.

## 0. The answer in brief

The paper does not define "observer" anywhere, and JS's sentence is the
definition it has been using without stating: *an observer is a system
that carries a classical structure*, a copyable basis, which is the
standing possibility of a FANOUT; and a classical structure, by
`prop:f1-dictionary`, is a committed direction with its section, which is
the selection of a complex structure in the sense of `sec:fanout-direction`.
So observer-hood is not something that then makes observations; it *is*
the possession of the capacity to commit a direction, and the $i$ of
quantum theory is the shadow of that capacity. This closes a loop the
paper runs in one direction only. The self-reference section derives the
$i$ from the observer (self-reference forces non-computable information,
additivity forces commutativity, the two force complex amplitudes, and the
global phase is "the observer's self-referential ignorance of their own
computational state", `main.tex` and `sec:jacobson`). JS's sentence is the
converse: having an $i$ is what makes an observer. Together they are a
biconditional the paper can state as its definition: *a system is an
observer if and only if it carries a classical structure, i.e. a committed
complex direction.* The extension of Müller is then specific. Müller
starts from the observer as primitive, an observer state being a finite
string of observations with universal induction fixing what comes next.
The framework says what an observation is (a copy fired in a committed
basis) and therefore what an observer must be (a carrier of such a
structure), and derives from that the complex structure, hence quantum
theory's $i$, the Minkowski signature's $i$ (`sec:jacobson`), and the
chirality split of the inferred spacetime (today's note). Müller's
first-person perspective is not a string of bits; it is a standing
commitment of a complex structure, and that is why the physics it sees is
quantum with a definite $i$, Lorentzian with the same $i$, and chiral.

## 1. The definition, in the paper's own objects [CANDIDATE; the pieces STRUCTURAL]

1. A measurement result "must be copyable from one observer to another",
   the COPY of the calculus (`derivation_of_the_quantum_postulates`,
   Postulate 2). A copy is a dagger-special commutative Frobenius algebra,
   and these are exactly orthonormal bases (Coecke, Pavlovic and Vicary,
   `coeckepavlovicvicary2013orthogonal`, cited). STRUCTURAL.
2. On a qubit such a structure is a lifted antipodal skeleton: an axis of
   the Bloch sphere with a section over its two poles
   (`prop:f1-dictionary`). The copier is "fibre-committed, the committed
   direction the record direction". STRUCTURAL (the paper's proposition).
3. In the two-qubit Hopf model a point of the Bloch sphere of one qubit is
   a point of the twistor fibre, a complex structure on the quaternionic
   line (twistor note, section 4: "the second qubit's Bloch sphere is the
   sphere of choices of $i$"). So the axis a classical structure commits
   *is* a complex structure, in the precise sense of today's note: the
   continuous part of "selecting $i$". STRUCTURAL, verified 2026-10-07.
4. "The 'preferred' complex line is nothing over and above the standing
   commitment of the network's record-making. No copy, no $\mathbb{C}$."
   (`sec:fanout-direction`, CANDIDATE.)

Put together: to be able to observe is to carry a classical structure; to
carry one is to have committed a direction; a committed direction is a
complex structure. Hence JS's sentence, with the paper's labels: the
possibility of observation and the selection of $i$ are the same
possession, and "observer" is the name of a system that has it. The
definition makes no reference to consciousness, size, or classicality as
a separate property: a qubit with a copier is an observer of the smallest
kind, and the gradation of `sec:fanout-boundary` (a location is as
definite as the interactions fixing it are redundant) grades observers by
the redundancy of their commitments.

## 2. What it adds to Müller [CANDIDATE]

Müller's programme ("Law without law", Quantum 4, 301, 2020; the
reconstruction papers already cited) takes the first-person perspective as
fundamental: the observer and its observation string are primitive, and
the world is what the observer's predictions converge on. Three things the
framework adds, each a claim rather than a reading of his text (not read):

- *What an observation is.* Not a bit appended to a string but a copy
  fired in a committed basis, with the committed direction the record and
  the orthogonal data what no record carries. The bit is the real column;
  the commitment is what makes a column real.
- *Why the observer's physics is complex, Lorentzian and chiral.* The
  commitment is a complex structure; the global phase is the observer's
  self-referential ignorance (Born rule, `sec:born-rule`); the Minkowski
  $i$ is the same $i$ (`sec:jacobson`, conjectural); and at every inferred
  point the isotropy splits by that $i$ into the gauge $SU(2)$ and the
  chirality that becomes spacetime (2026-10-08 note). None of this is
  available to a theory in which the observer is a string.
- *Intersubjectivity without a shared direction.* Section 9 of today's
  note: observers in one record-forming network can differ in the
  continuous part of their commitment (which $i$, which axis) and still
  share the discrete part (which chirality is spacetime), since regions
  of opposite type would be each other's partial transposes and not
  states relative to each other. So many first-person perspectives agree
  on the handedness of spacetime while disagreeing on their preferred
  direction. Chirality is intersubjective; direction is subjective. This
  is the first-person perspective made relational in the paper's sense
  (`sec:relationalism`): the shared world is what the commitments agree
  on, and they are forced to agree on exactly the discrete datum.

## 3. Pushback and fences

- *Possibility versus act.* JS's sentence rests on the possibility of
  observing, not the act. The paper's `sec:fanout-direction` says a copy
  "fires" and thereby commits. The reconciliation is in
  `prop:f1-dictionary`: the classical structure exists as section data
  before any firing, so the commitment is the structure's, and firing
  writes a record in it. "Observer" should be defined by the structure,
  not the firing, or a system between measurements would not be an
  observer. The paper's wording in `sec:fanout-direction` ("every fired
  copy is a committed direction") should be read with this gloss.
- *Which $i$.* As in section 9 of the Woit note, the structure commits
  the continuous part. Whether all observers' structures share a type is
  `op:chirality`; the prediction that they must is CANDIDATE and rests on
  the two-qubit model.
- *Uniqueness.* That the commitments of a connected network patch into
  one global $\mathbb{C}\subset\mathbb{O}$ is `op:fanout-selection`, OPEN. The
  definition of observer does not need it; the definition of *the* world
  does.
- *Müller not read.* The characterisation above is from his abstract and
  from the group's reconstruction papers the paper already cites. Before
  the paper says "extends Müller", the 2020 paper should be read for what
  it says an observation and an observer are, and whether he already has
  the commitment structure in some form. VERIFY-SUPPORT.
- *Circularity.* The self-reference section derives $i$ from the observer;
  this note derives the observer from $i$. A biconditional is not a
  circle if one side is a definition and the other a derivation; the paper
  should say which is which. Proposed: the definition is this note's
  (observer = carrier of a classical structure), the derivation is the
  self-reference section's (such a carrier must use complex amplitudes).

## 4. Proposed wording and references

- A definition, for the self-reference section or the register section's
  opening, JS to place: "An observer, in this paper, is any system that
  carries a classical structure: a copyable basis, which by
  Proposition~\ref{prop:f1-dictionary} is a committed direction with its
  section. The possibility of making an observation and the selection of a
  complex direction are the same possession; there is no observer without
  it, and nothing more is required to be one. This is the first-person
  starting point of Müller \autocite{mueller2020lawwithoutlaw}, with the
  observer's primitive act given a structure: a copy fired in a committed
  basis."
- Ledger: **CANDIDATE** An observer is a system carrying a classical
  structure, equivalently a committed complex direction; observer-hood
  and the selection of $i$ are one possession. Converse to the
  self-reference section's derivation of $i$ from the observer; the two
  form the paper's definition and derivation respectively.
- Batch `bib/mueller_law_without_law_ref_2026-10-08T1500.bib`, one entry,
  Crossref-verified, abstract read, VERIFY-SUPPORT for the
  characterisation of his observer.


## 5. The counterfactual possibility of observation (added 2026-10-08T1700)

JS: "We're getting close to the idea that the counterfactual possibility
of making an observation defines what being an observer is." Yes, and the
word "counterfactual" is the one that joins this thread to the spacetime
thread, because it is the word the antitelephone note used for the
spacelike loops. Three identifications, each already in the paper or in a
verified note, now read together.

*The possibility is section data, and section data is the imaginary
column.* `prop:f1-dictionary`: a classical structure is a committed
direction together with a section; the copyable states are the section's
image; and "the fibre freedom, a torsor for $\mathrm{Map}(P,U(1))$, is
exactly the data absent from the classical record a structure induces".
So the structure, as it stands before any firing, is precisely what no
record carries: it is possibility, not record, and in the two-column
ledger (2026-09-18) what no record carries is the imaginary column, the
phase. The observer's capacity to observe lives in the column that is not
written. An observer is a standing counterfactual: a system of which it
is true that *if* a copy fired in its structure *then* a record would be
written in that basis, while nothing has been written. That is JS's
sentence with the paper's two columns under it: observer-hood is
imaginary cost, observation is real cost.

*Counterfactual observation is physical, and the paper's ledger says
why.* Elitzur and Vaidman's interaction-free measurement
(`elitzurvaidman1993interactionfree`, Crossref-verified, not read this
session; realised by Kwiat, Weinfurter, Herzog, Zeilinger and Kasevich,
`kwiat1995interactionfree`; discussed by Penrose in `Penrose1994`, in the
library, VERIFY-SUPPORT for the section) is the textbook demonstration
that a detector which *could* have fired and did not changes the outcome
statistics: the dark port of the interferometer lights with probability
$\tfrac14$ when the bomb is present and never when it is absent. In the
ledger the bomb is an observer by this note's definition, a classical
structure on the which-path qubit; its presence does not write a record on
the dark-port runs, yet it removes the closed loop through which the two
arms would have cancelled, so the imaginary column changes without the
real column being touched. The physical effect of a counterfactual
observation is the paper's imaginary cost made visible, and it is the
cleanest laboratory fact the two-column reading has to point to. A
paragraph on it belongs beside the Born-rule-as-closed-loop material
(2026-09-18, section 2a), where "the anti-event contributes $i\pi$" is the
same arithmetic.

*The counterfactual possibilities between observers are spacelike
separation.* The spacetime section, as patched on 2026-09-27: two
observers are spacelike separated when an antitelephone between them
would close a loop; the loops such telephones would close, and carry
nothing round, are what spacelike separation is; their number is the
distance, counted imaginary. Read with this note: a loop that would carry
a record if one were sent is a counterfactual observation of one observer
by another, and the spatial network is the network of such
counterfactuals. So the same object, the unfired possibility of a record,
does two jobs. Within a system it is what makes the system an observer;
between systems it is what makes them spatially separated. Observer-hood
and spatial extension are one column of the ledger read at two scales.
The real column, the records, is the other column at both scales: within
a system the record is the act of observation, between systems the
records are the causal order, time. This is the framework's "duration is a
record, order is a phase" (records thread) now with the observer in it.

*A distinction the paper must keep.* Counterfactual *possibility* is not
counterfactual *definiteness*. The structure exists and would write a
record if fired; it does not follow that the record it would have written
has a value now, and Bell's theorem is the proof that it does not
(`sec:contextuality`, the paper's negativity-and-contextuality chain). The
observer is defined by the possibility, and quantum mechanics is the
statement that possibilities are not values: the imaginary column is not
a hidden real column. JS's sentence is therefore exactly right as stated,
"the counterfactual possibility of making an observation", and would be
wrong if "possibility" were replaced by "outcome". Müller's observer
state, a string of definite past observations, is the real column; the
framework's observer is the imaginary column that the string is written
from.

*Where this leaves the definition.* An observer is a system carrying a
classical structure, equivalently a standing counterfactual record,
equivalently a committed complex direction with nothing yet written in it.
Observation converts a unit of the imaginary column into the real column
in that direction. Observers are spacelike separated by the counterfactual
records between them and timelike ordered by the actual ones. CANDIDATE
throughout; the pieces (the dictionary proposition, the two columns, the
antitelephone definition, the interaction-free measurement) are
STRUCTURAL or the paper's own, and the join is this note's.

Wording owed: the definition sentence of section 4 can take one more
clause, "a standing counterfactual: a record that would be written if a
copy fired, and has not been"; and one paragraph on interaction-free
measurement in the two-columns material, citing Elitzur--Vaidman, Kwiat et
al. and Penrose. Batch
`bib/interaction_free_measurement_refs_2026-10-08T1700.bib`.
