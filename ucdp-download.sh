#!/bin/bash

##
## Changelog
##
## 2021-04-14 <e0425327@student.tuwien.ac.at>
##   - initial version of script
##

set -eu -o pipefail
MYDIR="$(realpath "$(dirname "$0")")"

cd "$MYDIR"
mkdir -p "ucdp-data"
cd "ucdp-data"

[[ -f "ucdp-prio-acd-201-csv.zip" ]] || {
    echo "downloading UCDP/PRIO Armed Conflict Dataset version 20.1"
    wget 'https://ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-201-csv.zip'
}
[[ -f "ucdp-prio-acd-201.pdf" ]] ||
    wget 'https://ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-201.pdf'
[[ -f "versionhistory-acd-201.pdf" ]] ||
    wget 'https://ucdp.uu.se/downloads/ucdpprio/versionhistory-acd-201.pdf'
[[ -f "ucdp-prio-acd-201.csv" ]] ||
    unzip 'ucdp-prio-acd-201-csv.zip'

cat >LICENSE <<"EOF"
At the time of writing the script 'ucdp-download.sh', **NO** license
information was specified on the webpage https://ucdp.uu.se/downloads/ in
general or specifically near the presented download links.

Aforementioned webpage was, and all download links presented there were,
publicly accessible without any restrictions, and easily findable on the
internet.

The script 'ucdp-download.sh' downloads files from urls easily available
at the time of writing this script; specifically no url-guessing or
url-mangling has been undertaken.
EOF

cat >CITE-AS <<"EOF"
• Pettersson, Therese & Magnus Öberg (2020) Organized violence, 1989-2019.
  Journal of Peace Research 57(4).
• Gleditsch, Nils Petter, Peter Wallensteen, Mikael Eriksson,
  Margareta Sollenberg, and Håvard Strand (2002) Armed Conflict 1946-2001:
  A New Dataset. Journal of Peace Research 39(5). 
EOF

echo "verifying downloaded data is as expected and was not damaged..."

expectedsha256='b797ffe37c35aba0a9f013e7019307753d4444655bf3c6a7090df85ba57382ae *ucdp-prio-acd-201.csv'
[[ "$expectedsha256" = "$(sha256sum -b ucdp-prio-acd-201.csv)" ]] || {
    echo "WARNING: the file ucdp-prio-acd-201.csv does not have expected content!" >&2
    echo "  either the data at https://ucdp.uu.se/downloads was changed, or the" >&2
    echo "  data was damaged during transport." >&2
}

echo "the end."
