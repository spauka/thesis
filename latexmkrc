# $pdflatex = "xelatex %O %S";
$pdf_mode = 5;

# Pass specific options to bibtex
$bibtex     = "bibtex %S > '$ENV{'TMPDIR'}'${filesep}bibtex.out";
# $bibtex     = "bibtex %S";

# Define all output directories to be "tmp"
# All build files will now be placed in this directory
$aux_dir = "tmp";
$tmpdir  = "tmp";
$out_dir = 'tmp';