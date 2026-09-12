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

A `note` does not round-trip. Zotero turns it into a child note on the item
rather than a field, so it stays in the library and in the batch file here but
never reaches the exported `.bib`. That is the right place for it; just do not
expect to see it in `paper1/references.bib`.

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

## Checking an entry without exporting

Better BibTeX answers on Zotero's local HTTP server, so a single entry can be
seen exactly as it will be exported:

    curl -s "http://127.0.0.1:23119/better-bibtex/export/item\
    ?citationKeys=<key>,<key>&translator=biblatex" \
      -H "Zotero-Server-ID: $(cat <zotsid>)"

No API key is needed: reads are open. This is the quickest way to confirm that
an import pinned the key and that brace protection survived. There is an
equivalent collection endpoint but its path syntax is not obvious, so a full
re-export is still a right-click in the GUI.

## Getting LaTeX into a field

Zotero stores plain text, so a title containing maths arrives as literal
characters and Better BibTeX escapes it on export: `$S_3$` becomes
`\${{S}}\_3\$`, which typesets as visible dollar signs. Two ways out,
both driven from the item's Extra field or its title.

For a subscript or an italic, use the markup Zotero itself understands ---
`S<sub>3</sub>` in the title field --- which BBT exports as
`{{S}}{\textsubscript{3}}`. That is the right tool for the common case.

For real mathematics, put the LaTeX in Extra as `tex.<field> = <value>`, with
an **equals sign**. BBT passes an `=` line through verbatim; a `:` line is
treated as text and escaped like anything else. So

    tex.title = Epistemic Horizons: This Sentence Is $\frac{1}{\sqrt{2}}(...)$

exports as that exact string, maths intact, while `tex.title:` would not. The
same `tex.<field>` mechanism supplies fields Zotero has no slot for --- a
`chapter` on a book, for instance.

Writes do need a key, and the local API takes them: `POST` to
`/api/users/0/items`, or `PATCH` a single item with
`If-Unmodified-Since-Version` set to the version last read. The key is minted
by Zotero, is not a zotero.org key, and is not stored in `prefs.js` or
`zotero.sqlite`, so it changes when Zotero restarts and has to be fetched again
from the settings panel where the local API is enabled.
