#!/usr/bin/bash
set -eu -o pipefail
MYDIR="$(realpath "$(dirname "$0")")"

#####
##
## this scripts scans validates the file
## data-management-plan.json in the project root directory against the
## json schema found at
## https://raw.githubusercontent.com/RDA-DMP-Common/RDA-DMP-Common-Standard/master/examples/JSON/JSON-schema/1.0/maDMP-schema-1.0.json
##
## Note: the source file first has to be built, either with the
## general build script `build.sh`, or by the specific build step
## `madmp-generate.py`
##
#####

tmpdir="$(mktemp -d)"
trap "rm -Rf $tmpdir" EXIT

(
    set -eu -o pipefail
    cd "$tmpdir"
    wget -nv https://raw.githubusercontent.com/RDA-DMP-Common/RDA-DMP-Common-Standard/master/examples/JSON/JSON-schema/1.0/maDMP-schema-1.0.json
)

cd "$MYDIR/.."

SRCJSON="data-management-plan.json"
SCHEMAJSON="$tmpdir/maDMP-schema-1.0.json"

jsonschema -i "$SRCJSON" "$SCHEMAJSON" 

echo "$0 finished."
