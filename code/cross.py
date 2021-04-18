#!/usr/bin/env python3

"""
this script make a x-y cross-plot and csv file.

input dirs: ucdp-data-extracted and sna-at-data-extracted
output dir: ./output-data/
"""

import csv
from decimal import Decimal
import matplotlib.pyplot as plt
import os.path
import sys

SRCUDIR = os.path.join(os.path.dirname(__file__), "..", "ucdp-data-extracted")
SRCSDIR = os.path.join(os.path.dirname(__file__), "..", "sna-at-data-extracted")

DESTDIR = os.path.join(os.path.dirname(__file__), "..", "output-data")

DESTLICENSEFILE = os.path.join(DESTDIR, "LICENSE")
DESTSOURCESFILE = os.path.join(DESTDIR, "DATA-SOURCE")
DESTMETAFILE = os.path.join(DESTDIR, "META.xml")
DESTCSVFILE = os.path.join(DESTDIR, "output-data.csv")
DESTIMGFILE = os.path.join(DESTDIR, "output-data.pdf")


with open(DESTLICENSEFILE, mode='w', encoding="UTF-8") as fp:
    fp.write(
"""The data in this directory is the result of a calculation, with two
principal input data sets:

* UCDP data, which does not have a license statement associated (see file
  ``ucdp-data/LICENSE``)
* SNA-AT data, which does have a very permissive license associated
  (see file in other directory: ``sna-at-data/LICENSE``)

Whether the author of this project has the legal right to grant a license
for this data is unknown to this author -- the author does not have the
approrpiate education in law.

If you have determined, on your own accord, to your own satisfaction and to
your full liability, that this author has the lawful right to grant the same
license to the data in this directory as is stated in the file `LICENSE` in the
parent directory, then this author grants the same license to the data and
files in this directory as is stated in the file `LICENSE` in the parent
directory.
""")

with open(DESTSOURCESFILE, mode='w', encoding='UTF-8') as fp:
    fp.write("""Based on data from:

1) UCDP (https://ucdp.uu.se)

  • Pettersson, Therese & Magnus Öberg (2020) Organized violence, 1989-2019.
    Journal of Peace Research 57(4).
  • Gleditsch, Nils Petter, Peter Wallensteen, Mikael Eriksson,
    Margareta Sollenberg, and Håvard Strand (2002) Armed Conflict 1946-2001:
    A New Dataset. Journal of Peace Research 39(5). 

2) STATISTIK AUSTRIA (https://statistik.at)
  
  • Volkswirtschaftliche Gesamtrechnung
""")

with open(DESTMETAFILE, mode='w', encoding='UTF-8') as fp:
    fp.write("""<?xml version="1.0" encoding="utf-8"?>
<simpledc xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title xml:lang="en"
        >Correlating World Conflict with Local Economy Growth</dc:title>
    <dc:creator>Max-Julian Pogner &lt;max-julian@pogner.at&gt;</dc:creator>
    <dc:description xml:lang="en">For the average student, the
Uppsala Conflict Data Program &lt;https://ucdp.uu.se/&gt;
offers a fascinating periscope onto the conflicts of the world.
Together with economic figures as collected by
Statistik Austria &lt;https://www.statistik.at&gt;,
the local economic impact of world-wide conflict is calculated.

WARNING: While this student is fairly confident regarding the numerical
correctness of the calculations, any conclusions have to be regarded as having
worse-than-questionable statistical validity.</dc:description>
    <dc:publisher>Max-Julian Pogner &lt;max-julian@pogner.at&gt;</dc:publisher>
    <dc:date>2021-04-17</dc:date>
    <dc:type>http://purl.org/dc/dcmitype/Dataset</dc:type>
    <dc:format>text/csv</dc:format>
    <dc:relation>Uppsala Conflict Data Program https://ucdp.uu.se/downloads/</dc:relation>
    <dc:source>Pettersson, Therese &amp; Magnus Öberg (2020) Organized violence, 1989-2019. Journal of Peace Research 57(4).</dc:source>
    <dc:source>Gleditsch, Nils Petter, Peter Wallensteen, Mikael Eriksson, Margareta Sollenberg, and Håvard Strand (2002) Armed Conflict 1946-2001: A New Dataset. Journal of Peace Research 39(5).</dc:source>
    <dc:source>(c) STATISTIK AUSTRIA, die Daten wurden stark gefiltert und stark bearbeitet.</dc:source>
    <dc:coverage>1977-2019</dc:coverage>
    <dc:coverage>AUSTRIA</dc:coverage>
</simpledc>""")


DATA = { }

SRCUFILE = os.path.join(SRCUDIR, "ucdp-data-extracted.csv")
with open(SRCUFILE, mode='r', encoding="UTF-8", newline="") as fpu:
    csvu_input = csv.DictReader(fpu)
    for row in csvu_input:
        year = row["year"]
        intensity_level = row["intensity_level"]
        DATA[year] = [intensity_level, None]

SRCSFILE = os.path.join(SRCSDIR, "sna-at-data-extracted.csv")
with open(SRCSFILE, mode='r', encoding="UTF-8", newline="") as fps:
    csvs_input = csv.DictReader(fps)
    prevgdp = None
    for row in csvs_input:
        year = str(row["year"])
        gdp = Decimal(row["gdp"])
        if not prevgdp:
            prevgdp = gdp
        else:
            DATA[year][1] = (gdp - prevgdp)
            prevgdp = gdp

POINTS_X = [ ]
POINTS_Y = [ ]

with open(DESTCSVFILE, mode='w', encoding="UTF-8", newline="") as fpo:
    csv_output = csv.DictWriter(fpo, fieldnames=("intensity_level", "gdp", "label"))
    csv_output.writeheader()
    for year in sorted(DATA.keys()):
        label = str(year)
        intensity_level = DATA[year][0]
        gdp = DATA[year][1]
        csv_output.writerow({
            "intensity_level": intensity_level,
            "gdp": gdp,
            "label": label,
        })
        POINTS_X.append(int(intensity_level))
        POINTS_Y.append(gdp)


fig = plt.figure()
ax = fig.add_axes([0.14,0.10,0.80,0.82])
ax.scatter(POINTS_X, POINTS_Y)
ax.set_xlabel("world conflict intensity of a year [level]")
ax.set_ylabel("austrian GDP increase in a year [Billion EUR]")
ax.set_title('world conflict intensity VS austrian gdp')
plt.savefig(DESTIMGFILE)

sys.stdout.write(f"{sys.argv[0]} finished.\n")
