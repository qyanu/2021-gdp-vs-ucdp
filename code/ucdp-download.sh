#!/bin/bash

##
## Changelog
##
## 2021-04-14 <e0425327@student.tuwien.ac.at>
##   - initial version of script
##

set -eu -o pipefail
MYDIR="$(realpath "$(dirname "$0")")"

cd "$MYDIR/.."
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

cat >DATA-SOURCE <<"EOF"
Downloaded from https://ucdp.uu.se/downloads/
EOF

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

cat >META.xml <<"EOF"
<?xml version="1.0" encoding="utf-8"?>
<simpledc xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title xml:lang="en"
        >UCDP/PRIO Armed Conflict Dataset version 20.1</dc:title>
    <dc:creator>Uppsala Conflict Data Program https://ucdp.uu.se</dc:creator>
    <dc:description xml:lang="en">A conflict-year dataset with information on armed conflict where at least one party is the government of a state in the time period 1946-2019.</dc:description>
    <dc:publisher>Max-Julian Pogner &lt;max-julian@pogner.at&gt;</dc:publisher>
    <dc:date>2021-04-17</dc:date>
    <dc:type>http://purl.org/dc/dcmitype/Dataset</dc:type>
    <dc:format>text/csv</dc:format>
    <dc:source>https://ucdp.uu.se/downloads/</dc:source>
    <dc:source>Pettersson, Therese &amp; Magnus Öberg (2020) Organized violence, 1989-2019. Journal of Peace Research 57(4).</dc:source>
    <dc:source>Gleditsch, Nils Petter, Peter Wallensteen, Mikael Eriksson, Margareta Sollenberg, and Håvard Strand (2002) Armed Conflict 1946-2001: A New Dataset. Journal of Peace Research 39(5).</dc:source>
    <dc:coverage>1946-2019</dc:coverage>
</simpledc>
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
if [[ "$expectedsha256" = "$(sha256sum -b ucdp-prio-acd-201.csv)" ]];
then
    echo "verifying downloaded data is as expected and was not damaged... OK"
else
    echo "ERROR: the file ucdp-prio-acd-201.csv does not have expected content!" >&2
    echo "  either the data at https://ucdp.uu.se/downloads was changed, or the" >&2
    echo "  data was damaged during transport." >&2
    exit 1
fi

echo "$0 finished."
