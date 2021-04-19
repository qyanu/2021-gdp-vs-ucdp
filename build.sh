#!/bin/bash
set -eu -o pipefail
MYDIR="$(realpath "$(dirname "$0")")"

#####
##
## main build script for this project -- all you need to execute.
##
## this scripts performs all machine-automateable steps of downloading
## data, processing data and also creates and auxilliary artifacts such
## as documentation.
##
#####

trap '[[ 0 -eq $? ]] || echo "build error!"' EXIT

cd "$MYDIR"
./code/ucdp-download.sh
./code/ucdp-extract.py
./code/ucdp-extracted-render.py
./code/sna-at-extracted-render.py
./code/cross.py
dot -Tpdf dataflow-overview.dot > dataflow-overview.pdf
rst2pdf code/sna-at-download.rst
rst2pdf code/sna-at-extract-and-combine.rst
rst2pdf code/ucdp-quality-checklist.rst
rst2pdf data-management-plan.rst
./code/madmp-generate.py
rst2pdf README.rst
echo "build finished successfully."
