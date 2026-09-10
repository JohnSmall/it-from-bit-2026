# Hopf fibrations and division algebras bibliography

- conversation uuid: `4151200f-a88a-4018-a18b-9f2768c3f18e`
- created: 2026-06-01T11:27:12.808962Z  |  updated: 2026-06-01T11:28:54.600980Z
- messages: 2  |  keyword score: 3

## Summary (from the Claude export)

**Conversation Overview**

The person requested precise bibliographic references for two foundational mathematics papers: J.F. Adams' 1960 paper on the non-existence of elements of Hopf invariant one (establishing that Hopf fibrations terminate at S⁷), and Adolf Hurwitz's 1898 paper on the composition of quadratic forms (proving that normed division algebras exist only in dimensions 1, 2, 4, and 8, with no division algebra beyond the octonions). The person asked for these as a downloadable `.bib` file for use with LaTeX/BibTeX.

Claude used web search to verify precise bibliographic details including volume numbers, page ranges, and journal names, then generated a `.bib` file (`hopf_division_algebras.bib`) with two entries: `Adams1960` and `Hurwitz1898`. The entries used LaTeX-escaped umlauts for the German title to ensure compatibility with pdflatex without requiring UTF-8 input encoding. Claude also noted the existence of a related posthumous Hurwitz 1923 paper in *Mathematische Annalen* as a potential third entry, and explained the conceptual distinction between the two cited papers — Hurwitz providing the algebraic termination result and Adams the topological one — framing them as arriving at the same 1/2/4/8 dimensional conclusion via independent routes. The conversation used domain-specific terminology including Hopf fibrations, Hopf invariant, parallelisable spheres, normed division algebras, octonions, and homotopy theory.

## Transcript

### 1. human  ·  2026-06-01 11:27:13

I need a references to Adams paper on the termination of the Hopf fibrations and also Hurwitz, no division algebras beyond the Octonions. Please provide a downloadable *.bib file

I need a references to Adams paper on the termination of the Hopf fibrations and also Hurwitz, no division algebras beyond the Octonions. Please provide a downloadable *.bib file

### 2. assistant  ·  2026-06-01 11:28:54

 I need to recall Adams' foundational work on Hopf invariant one, which established that Hopf fibrations can only exist in dimensions 1, 2, 4, and 8—corresponding to the real, complex, quaternionic, and octonionic cases. The key reference is his paper in the Annals of Mathematics on the non-existence of elements of Hopf invariant one.

For Hurwitz's theorem on normed division algebras, I'm tracking down the precise citations—there's his original 1898 work on composition of quadratic forms published in the Göttingen Nachrichten, and a later posthumous paper from 1923 in Mathematische Annalen. Since this is for John's physics bibliography on "It from Bit via Gödel," I want to make sure the citations are exact and properly formatted. I should verify the exact bibliographic details for these citations since the user needs precise information for their LaTeX workflow—the Adams 1960 paper I'm confident about, but I want to double-check the Hurwitz 1898 page numbers and publication details to make sure the .bib entry is accurate. I'll search for the exact Hurwitz publication details to ensure accuracy, then generate the .bib file with both references properly formatted.I'll verify the precise bibliographic details for these two before building the file — getting volume and page numbers right matters for a citation file.
```
This block is not supported on your current device yet.
```

 I'm verifying the citations I've gathered—Adams's 1960 paper on Hopf invariant one from the Annals of Mathematics is solid and I'll include it, and I'm cross-checking the Hurwitz 1898 reference on quadratic forms.

For Hurwitz, there are spelling variations across different sources and OCR scans, but the canonical form "Über die Composition der quadratischen Formen von beliebig vielen Variabeln" is what's commonly cited. Since the user specifically asked for the result about no division algebras beyond the octonions—which is the 1, 2, 4, 8 theorem—the 1898 paper is the right primary source, though there's also a 1923 posthumous paper on the general Hurwitz-Radon composition. I'll go with the 1898 as the main citation since that's what directly addresses their request.

For Adams, I'm confident in the citation: J.F. Adams, "On the non-existence of elements of Hopf invariant one", Ann. of Math. (2) 72 (1960), 20–104. This is the foundational paper that, together with the Hopf invariant one problem, shows why the Hopf fibrations and parallelizable spheres only exist in dimensions 1, 3, and 7. Now I'll compile the bibliography entries.

Building the BibTeX file with proper formatting for the German titles. I need to decide on encoding for umlauts — UTF-8 is cleaner and what Mendeley typically exports, though LaTeX escapes would be more portable. I'll go with UTF-8 and use braces to protect capitalization. Writing BibTeX entries... I'm finalizing the BibTeX entry with proper LaTeX escaping for the German characters and completing the reprint information from the Mathematische Werke. I'll save this to the outputs folder and keep my response brief, mentioning the optional 1923 paper as well.Both citations confirmed. Adams 1960 is the Hopf-invariant-one paper that closes off the parallelisable spheres (so the Hopf chain terminates at S⁷), and Hurwitz 1898 is the original composition-algebra result giving the 1, 2, 4, 8 dimensions.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Two entries, with the German title using LaTeX-escaped umlauts so it compiles under pdflatex without an `inputenc`/UTF-8 dependency.

A couple of things worth flagging for your purposes:

The Hurwitz 1898 paper is the right citation for the "1, 2, 4, 8 and no further" claim — it's the original proof that multiplicative composition of quadratic forms exists only in those dimensions. If you ever want the *unital normed division algebra* classification stated as a theorem (R, C, H, O exactly), that result is usually attributed to the posthumous Hurwitz, "Über die Komposition der quadratischen Formen", Math. Ann. **88** (1923), 1–25. Say the word and I'll add it as a third entry.

For the framework's logic the two papers do slightly different jobs, which is worth keeping straight in the prose: Hurwitz gives you the algebraic termination (no normed division algebra past O), whereas Adams gives you the *topological* termination (no Hopf-invariant-one map, hence no Hopf fibration, past S⁷). They land on the same 1/2/4/8 but via independent routes — algebraic versus homotopy-theoretic — which is exactly the kind of distinction your Hopf–Frobenius functor conjecture is probing.

*(thinking)*

 I need to recall Adams' foundational work on Hopf invariant one, which established that Hopf fibrations can only exist in dimensions 1, 2, 4, and 8—corresponding to the real, complex, quaternionic, and octonionic cases. The key reference is his paper in the Annals of Mathematics on the non-existence of elements of Hopf invariant one.

For Hurwitz's theorem on normed division algebras, I'm tracking down the precise citations—there's his original 1898 work on composition of quadratic forms published in the Göttingen Nachrichten, and a later posthumous paper from 1923 in Mathematische Annalen. Since this is for John's physics bibliography on "It from Bit via Gödel," I want to make sure the citations are exact and properly formatted. I should verify the exact bibliographic details for these citations since the user needs precise information for their LaTeX workflow—the Adams 1960 paper I'm confident about, but I want to double-check the Hurwitz 1898 page numbers and publication details to make sure the .bib entry is accurate. I'll search for the exact Hurwitz publication details to ensure accuracy, then generate the .bib file with both references properly formatted.

I'll verify the precise bibliographic details for these two before building the file — getting volume and page numbers right matters for a citation file.

*[tool_use: web_search]*

*[tool_result: web_search]*

*(thinking)*

 I'm verifying the citations I've gathered—Adams's 1960 paper on Hopf invariant one from the Annals of Mathematics is solid and I'll include it, and I'm cross-checking the Hurwitz 1898 reference on quadratic forms.

For Hurwitz, there are spelling variations across different sources and OCR scans, but the canonical form "Über die Composition der quadratischen Formen von beliebig vielen Variabeln" is what's commonly cited. Since the user specifically asked for the result about no division algebras beyond the octonions—which is the 1, 2, 4, 8 theorem—the 1898 paper is the right primary source, though there's also a 1923 posthumous paper on the general Hurwitz-Radon composition. I'll go with the 1898 as the main citation since that's what directly addresses their request.

For Adams, I'm confident in the citation: J.F. Adams, "On the non-existence of elements of Hopf invariant one", Ann. of Math. (2) 72 (1960), 20–104. This is the foundational paper that, together with the Hopf invariant one problem, shows why the Hopf fibrations and parallelizable spheres only exist in dimensions 1, 3, and 7. Now I'll compile the bibliography entries.

Building the BibTeX file with proper formatting for the German titles. I need to decide on encoding for umlauts — UTF-8 is cleaner and what Mendeley typically exports, though LaTeX escapes would be more portable. I'll go with UTF-8 and use braces to protect capitalization. Writing BibTeX entries... I'm finalizing the BibTeX entry with proper LaTeX escaping for the German characters and completing the reprint information from the Mathematische Werke. I'll save this to the outputs folder and keep my response brief, mentioning the optional 1923 paper as well.

Both citations confirmed. Adams 1960 is the Hopf-invariant-one paper that closes off the parallelisable spheres (so the Hopf chain terminates at S⁷), and Hurwitz 1898 is the original composition-algebra result giving the 1, 2, 4, 8 dimensions.

*[tool_use: create_file]*

*[tool_result: create_file]*

*[tool_use: present_files]*

*[tool_result: present_files]*

Two entries, with the German title using LaTeX-escaped umlauts so it compiles under pdflatex without an `inputenc`/UTF-8 dependency.

A couple of things worth flagging for your purposes:

The Hurwitz 1898 paper is the right citation for the "1, 2, 4, 8 and no further" claim — it's the original proof that multiplicative composition of quadratic forms exists only in those dimensions. If you ever want the *unital normed division algebra* classification stated as a theorem (R, C, H, O exactly), that result is usually attributed to the posthumous Hurwitz, "Über die Komposition der quadratischen Formen", Math. Ann. **88** (1923), 1–25. Say the word and I'll add it as a third entry.

For the framework's logic the two papers do slightly different jobs, which is worth keeping straight in the prose: Hurwitz gives you the algebraic termination (no normed division algebra past O), whereas Adams gives you the *topological* termination (no Hopf-invariant-one map, hence no Hopf fibration, past S⁷). They land on the same 1/2/4/8 but via independent routes — algebraic versus homotopy-theoretic — which is exactly the kind of distinction your Hopf–Frobenius functor conjecture is probing.
