$pdf_mode = 1;
$pdflatex = 'pdflatex -synctex=1 %O %S';
$biber = 'biber %O %S';
$bibtex_use = 2;
$clean_ext = 'bbl bcf run.xml synctex.gz';

# Each paper lives in its own directory and is built there. $do_cd makes
# latexmk chdir to the document before running, so \input paths inside a
# paper stay relative to that paper and need no rewriting; it also keeps
# build artefacts beside their source instead of in the shared root.
$do_cd = 1;

# Both papers are default targets: a bare `latexmk` builds both, and
# `latexmk -C` cleans both. Name one explicitly to work on it alone.
@default_files = ('paper1/main.tex', 'paper2/paper2_main_2026-07-07.tex');

# PDF viewer: zathura. Used by `latexmk -pv` (open once after the build) and
# `latexmk -pvc` (watch and rebuild). A plain `latexmk` stays silent.
# zathura watches the file itself and reloads on change, so latexmk needs to
# do nothing to refresh it: update method 0 = "no update action required".
$pdf_previewer = 'zathura %O %S';
$pdf_update_method = 0;
