#!/bin/bash
set -eu -o pipefail

#
# Dependencies:
#  apt install \
#    graphviz \
#    rst2pdf \
#

./ucdp-download.sh
./ucdp-extract.py
./cross.py
dot -Tpdf dataflow-overview.dot > dataflow-overview.pdf
rst2pdf README.rst
rst2pdf extract-and-combine-sna-at.rst
