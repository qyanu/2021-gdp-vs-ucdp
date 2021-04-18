#!/usr/bin/bash
set -eu -o pipefail
MYDIR="$(realpath "$(dirname "$0")")"

#####
##
## this scripts scans the project root directory and in all sub-directories
## for files named ``META.xml`` and validates them against the
## Dublin Core Metadata XML schema variant ``simpledc``.
##
#####

tmpdir="$(mktemp -d)"
trap "rm -Rf $tmpdir" EXIT

(
    set -eu -o pipefail
    cd "$tmpdir"
    wget -nv https://dublincore.org/schemas/xmls/qdc/2008/02/11/simpledc.xsd
    wget -nv https://dublincore.org/schemas/xmls/qdc/2008/02/11/dc.xsd
)

find "$MYDIR/" -name META.xml -type f -print0 \
    | xargs -0 --no-run-if-empty -n1 \
        xmllint --noout --schema "$tmpdir/simpledc.xsd"

echo "$0 finished."
