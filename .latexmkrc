$pdf_mode = 1;
$pdflatex = 'pdflatex -synctex=1 %O %S';
$biber = 'biber %O %S';
$bibtex_use = 2;
@default_files = ('main.tex');
$clean_ext = 'bbl bcf run.xml synctex.gz';

# PDF viewer: zathura. Used by `latexmk -pv` (open once after the build) and
# `latexmk -pvc` (watch and rebuild). A plain `latexmk` stays silent.
# zathura watches the file itself and reloads on change, so latexmk needs to
# do nothing to refresh it: update method 0 = "no update action required".
$pdf_previewer = 'zathura %O %S';
$pdf_update_method = 0;
