# bib/

Dated batches of references, written here and then imported into Zotero. One
batch per import, named `description_YYYY-MM-DDTHHMM.bib`. Nothing here is
read by a build: the papers cite from `paper1/references.bib` and
`paper2/references_paper2.bib`, which Better BibTeX exports from Zotero. A
batch is the record of what was added and when.

## Write batches as `.bib`

A BibLaTeX entry key is a citation key, and Better BibTeX's own importer keeps
it and pins it --- the preference is `importCitationKey`, "On import, assign
the existing citation key to the item being imported", on by default. So the
entry key you write is the key the export will carry, and the citation in the
paper can be written before the import happens.

RIS cannot do this. Zotero's RIS importer has no citation-key field and
discards the `ID`, so BBT assigns a formula key instead and every citation has
to be re-pointed afterwards. The `.ris` files here are the batches imported
before this was understood, kept as they were imported. Do not write new ones.

## Writing a batch

Entry key is `author+year+keyword`, the convention inherited from the Mendeley
library the Zotero collections were built from: `koide1983new`,
`hurwitz1898composition`, `eakinsathaye1990automorphisms` --- surnames of one
or two authors, the year, one word from the title.

Authors go in one `author` field separated by ` and `, surname first:
`author = {Springer, Tonny A. and Veldkamp, Ferdinand D.}`. Native Unicode is
fine and must not be mangled back to TeX escapes; BBT emits it for author
names. Give a `doi` only when it is deterministic, and record provenance ---
where the metadata was checked, and against what --- in a `note` field, which
is where a VERIFY-CITE belongs.

Brace any word whose capitals must survive. BBT sentence-cases titles on
import (`importSentenceCase` defaults to `on+guess`), so
`title = {Octonions, {Jordan} Algebras and Exceptional Groups}` keeps the name
and `title = {The {Octonions}}` keeps the noun.

## Importing

File > Import, choose the `.bib`, import into the right collection. Then check
the Citation Key column shows your key. A key of the shape
`bakerTranscendentalNumberTheory1975` means the entry arrived unpinned and
`citekeyFormat` --- `auth.lower + shorttitle(3, 3) + year` in this library ---
generated one instead; pin the intended key by hand before exporting.

Export the collection afterwards, and the paper's `.aux` cite set and the
exported keys should agree.
