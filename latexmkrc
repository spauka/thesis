$pdf_mode = 4;
$postscript_mode = $dvi_mode = 0;

# Pass specific options to bibtex
$bibtex     = "bibtex %S > '$ENV{'TMPDIR'}'bibtex.out";
# $bibtex     = "bibtex %S";

# Define all output directories to be "tmp"
# All build files will now be placed in this directory
$aux_dir = "tmp";
$tmpdir  = "tmp";
$out_dir = 'tmp';