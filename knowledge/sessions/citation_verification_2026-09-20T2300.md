# Session note: citation verification and batching for the Fable session's work, 18--20 September

Date: 2026-09-20T2300. Session: Claude Code (Opus 5), citation verification.
Nothing built, nothing committed, nothing in `paper1/` edited.

Sixty-eight references across nine `.bib` batches, checked against records and
in seven cases against the sources themselves. Everything below is either a
database record or a quotation from a paper that was read; nothing is from
memory.

## 1. Method

Crossref by DOI wherever a DOI could be constructed or found, INSPIRE-HEP for
the high-energy literature, the arXiv API for preprints, OpenAlex and Semantic
Scholar as fallbacks for pagination. Where a claim in the paper or in a
project document rested on a source, the abstract was read, and the full text
where the abstract did not settle it. The helper used is at
`/tmp/.../scratchpad/verify.py` and is not kept; it is fifty lines of `urllib`
against four public APIs and is not worth a place in `scripts/`.

A source counts as **verified** here when its bibliographic record was
confirmed. That is not the same as read. Each entry's `note` says which, and
where only the record was checked the note says the body was not read, so that
the project's characterisation of the argument stays visibly the project's own.

## 2. What was found: the corrections that matter

Five things are worth a decision rather than a field.

**(a) 't Hooft 1976 does not say what the paper says he says.** The paper's new
absent-gate paragraph attributes a twelve-fermion vertex with
$\Delta B = \Delta L = 3$ to `thooft1976symmetry`. The scanned Letter was read.
Its Standard-Model application, Eq. (24) on page 10, is the **two-generation**
Weinberg--Salam model: $\Delta E = \Delta M = 1$,
$\Delta u + \Delta d^{C} = 3$, $\Delta u' + \Delta s^{C} = 3$, glossed as "a
proton and a neutron (two baryons equal six quarks) may annihilate to form two
antileptons, one of electron and one of muon type". That is **eight** fermions
with $\Delta B = \Delta L = 2$. The twelve-fermion form is the standard
three-generation extension and is correct physics; it is not his. $B-L$
conservation is implicit in his Eq. (24) and is asserted nowhere in the Letter.
The paper is not edited. The proposed wording is in section 13 of
`project-docs/sphaleron_slocc_collective_conversion_2026-09-20T2000.md`, and
the companion paper where the vertex is actually computed, Phys. Rev. D 14
(1976) 3432, is in the batch as `thooft1976quantum` for that fix.

**(b) `Aaronson2004h` in `references.bib` is two papers spliced together.** It
carries the title and eprint of "Is Quantum Mechanics An Island In
Theoryspace?" (arXiv:quant-ph/0401062) with the journal, volume and DOI of
"Quantum computing and hidden variables" (Phys. Rev. A 71, 032325). A reader
following the printed reference lands on the wrong paper. The island paper has
no Crossref record and no journal_ref on arXiv, so it appears never to have
been published and wants `@online`. The correction is in Zotero, not here; the
suggested fields are in the closing comment of
`bib/two_columns_action_refs_2026-09-20T2200.bib`.

**(c) The $\alpha_{W}^{5}$ sphaleron rate is not Kuzmin, Rubakov and
Shaposhnikov's.** The records document credits them with it. Their abstract
claims only that the rate "exceeds the expansion rate of the universe at
$T >$ (a few) $\times 10^{2}$ GeV". The fifth power is Arnold, Son and Yaffe,
Phys. Rev. D 55, 6264 (1997), whose abstract says the literature estimate was
$O(\alpha_{W}^{4}T^{4})$ and that damping "suppress[es] the rate by an extra
power of $\alpha_{W}$". Added to the records batch as
`arnoldsonyaffe1997rate`; the document is corrected to cite both.

**(d) The horizon viscosity coefficient is not Chirco and Liberati's.** The
Jacobson document proposes to "inherit the Chirco--Liberati coefficient". Their
paper was read. They state $\eta = 1/(16\pi G)$ as a **review**: "it is also
noticed in [2] ... in agreement with the value obtained for the shear viscosity
of the stretched horizon of a black hole in the so called membrane paradigm",
closing "This result concludes the review of the argument described in
[1, 2, 12]". Their [2] is Eling, Guedens and Jacobson. They re-derive it in
their own setting but never write $1/4\pi$ as a number. Their own result is
that the GR entropy production term "is identical to the so called tidal
heating term of Hartle-Hawking", which is a different statement.

**(e) Guryanova, Friis and Huber's infinite cost is energy-at-finite-time, not
entropy.** This was the specific question asked of the clock batch. Read in
full. Appendix A.IV.3: rank-reducing measurement procedures "use either
infinite energy $E$, take infinite time $t$ ... or are infinitely complex".
Section 6: "the energy cost for reaching the ground state in finite time is
infinite. Other paradigms allow cooling to the ground state using finite
energy, but require infinite time." Entropy appears only in bounding the work
cost from below; the third law is the reason for the divergence, not the coin.
Two fences follow, both recorded in section 4e of
`project-docs/complex_thermodynamic_cost_pre_fanout_2026-09-16T1305.md`: the
divergence holds only "unless pure states are freely available", and
"ideal measurements can be approximated by non-ideal, unbiased ones to
arbitrary precision at finite energy cost", so the infinity is in the last
step to perfect correlation and not in making a good record. The framework's
own cost of a copy diverges in its **real**, entropy-like part, so the two do
not line up and they cannot be cited as saying the same thing about the same
quantity.

## 3. Claims checked against sources and found sound

- Chitambar, Duan and Shi 2008, full text. Theorem 1(b) is
  $\mathrm{GHZ}^{\otimes 3} \to W^{\otimes 2}$ under SLOCC, so multi-copy
  inter-convertibility of the classes is their result and not an
  extrapolation. They also remark that "previously, only one copy of the W
  state is known to be convertible from three copies of GHZ", which is exactly
  the framework's own three-to-one construction at $3/64$, so the paper's
  construction is the pre-2008 rate and CDS improve on it rather than
  contradict it.
- The framework's own conversions were re-run for this check and reproduce
  exactly: 2 GHZ $\to$ W at $3/32$, 2 W $\to$ GHZ at $2/9$, 3 GHZ $\to$ W at
  $3/64$, all at fidelity 1.000000000000000.
- Foot 1994, full text: "$\theta = 45.000 \pm 0.001$", with
  $\cos\theta > 1/\sqrt{3}$ as Koide's bound, i.e. $\theta < 54.7$ degrees.
  Both numbers the Koide note uses are his. Never published in a journal.
- D'Onofrio and Rummukainen 2016: "$T_c = 159.5 \pm 1.5$ GeV" and "a smooth
  cross-over" of width about 5 GeV. Both the number and the word are theirs,
  which settles the "crossover" vocabulary the sphaleron passage uses.
- Maldacena, Shenker and Stanford 2016: $\lambda_{L} \le 2\pi k_{B}T/\hbar$,
  which is the records document's one turn per thermal period. **One word to
  change**: they say "We conjecture a sharp bound ... We give a precise
  mathematical argument, based on plausible physical assumptions, establishing
  this conjecture." The document says "derived". Conjectured, with an argument.
- Yu, Chitambar, Guo and Duan 2010: the non-multiplicativity of tensor rank is
  theirs and is about exactly the W and GHZ states the framework uses. **Their
  number is superseded**: see section 5.

## 4. Batches written

Nine files, sixty-eight entries, no key collision with `references.bib` and
none among themselves (checked programmatically).

| file | entries | what |
|---|---|---|
| `sphaleron_slocc_refs_2026-09-20T2100.bib` | 4 | corrected in place; **urgent**, the paper cites three of these keys now |
| `clock_thermodynamics_refs_2026-09-18T1100.bib` | 7 | corrected in place |
| `two_columns_action_refs_2026-09-20T2200.bib` | 14 | new |
| `indefinite_causal_order_refs_2026-09-20T2200.bib` | 14 | new |
| `records_high_temperature_refs_2026-09-20T2200.bib` | 9 | new |
| `jacobson_nonequilibrium_refs_2026-09-20T2200.bib` | 8 | new |
| `complex_cost_v2_refs_2026-09-20T2200.bib` | 8 | new |
| `koide_renyi_refs_2026-09-20T2200.bib` | 2 | new |
| `landauer_temperature_refs_2026-09-20T2200.bib` | 2 | new |

Every `VERIFY-CITE` marker in the nine source documents is discharged, and each
now says what was checked and against what.

Four entries are in a batch without having been asked for, each flagged in its
own note and deletable: `thooft1976quantum` (for the 't Hooft fix),
`arnoldsonyaffe1997rate` (for the rate attribution), `kolbturner1990early` and
`aaronson2005hidden` (the latter commented out, not an entry).

## 5. A collision with the Fable session, and it was right

While this pass was running, the Fable session wrote
`bib/multicopy_slocc_refs_2026-09-20T2300.bib`, covering the same two keys as
this session's 2200 file plus six more. The 2200 file is withdrawn to
`bib/attic_multicopy_slocc_refs_2026-09-20T2200.bib.superseded`, which holds
the explanation. **Import the 2300 file, not the attic one.**

Their file also caught an error this one had made. This session's note on Yu,
Chitambar, Guo and Duan repeated their 2010 claim that the tensor rank of two
copies of W is seven. It is **eight**: Chen and Friedland proved the lower
bound, Christandl, Jensen and Zuiddam the upper. Verified against
arXiv:1708.08578v2. Non-multiplicativity survives, since three squared is nine,
but the number was wrong and is now corrected in the sphaleron document.

Owed back to their file, and it is the only `VERIFY-CITE` left in it. Their
`chenfriedland2018tensorrank` asks for the journal volume and pages. Verified
2026-09-20 against Crossref:

    journaltitle = {Linear Algebra and its Applications}
    volume       = {543}
    pages        = {1--16}
    date         = {2018-04}
    doi          = {10.1016/j.laa.2017.12.015}

Not written into their file, because it was still being edited by the other
session.

## 6. What could not be found

- **Mandelstam and Tamm 1945**, named in the two-columns note beside Margolus
  and Levitin. No Crossref and no INSPIRE record. The standard citation is
  J. Phys. (USSR) 9, 249 (1945). Not batched; it needs a hand-made entry.
- **The pagination of Qureshi-Hurst and Pearson**, Zygon 55(3) (2020), doi
  10.1111/zygo.12621. Crossref, OpenAlex and Semantic Scholar all record
  volume and issue and no pages; the publisher's site answers with a bot wall
  and Wiley with a 403. The journal's move to Open Library of the Humanities is
  the likely reason. The entry has no pages; the PDF that was read for the note
  will carry them.
- Two ISBNs are the only fields in the nine batches that no database confirmed:
  Kolb and Turner 1990 and Peskin and Schroeder 1995. In both cases Crossref
  has only a later reissue **whose record drops the second author**, so the
  reissue could not be used. Check both against a copy.

## 7. Not done

- Nothing in `paper1/` was edited, including where a source contradicts it.
- No ledger was edited, and no status label was changed.
- No build was run and nothing was committed.
- Bodies were read for seven sources only: 't Hooft 1976, Chitambar, Duan and
  Shi 2008, Foot 1994, Guryanova, Friis and Huber 2020, Chirco and Liberati
  2010, and the abstracts of Maldacena, Shenker and Stanford, D'Onofrio and
  Rummukainen, Yu et al., Arnold, Son and Yaffe, Kuzmin et al. and Padmanabhan
  2012. The other fifty-odd are verified as records only.
