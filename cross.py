#!/usr/bin/env python3

"""
this script make a x-y cross-plot and csv file.

inputs: ucdp-data-extracted and sna-at-data-extracted
output dir: ./output-data/
"""

import csv
import os.path
import matplotlib.pyplot as plt

SRCUDIR = os.path.join(os.path.dirname(__file__), "ucdp-data-extracted")
SRCSDIR = os.path.join(os.path.dirname(__file__), "sna-at-data-extracted")

DESTDIR = os.path.join(os.path.dirname(__file__), "output-data")

DESTLICENSEFILE = os.path.join(DESTDIR, "LICENSE")
DESTSOURCESFILE = os.path.join(DESTDIR, "SOURCES")
DESTCSVFILE = os.path.join(DESTDIR, "x-y-plot.csv")
DESTIMGFILE = os.path.join(DESTDIR, "x-y-plot.pdf")


with open(DESTLICENSEFILE, mode='w', encoding="UTF-8") as fp:
    fp.write(
"""The data in this directory is the result of a calculation, with two
principal input data sets:

* UCDP data, which does not have a license associated (see directory
  ``ucdp-data/``)
* SNA-AT data, which does have a very permissive license associated
  (see directory ``sna-at-data/``)
""")

with open(DESTSOURCESFILE, mode='w', encoding='UTF-8') as fp:
    fp.write(
"""
Based on data from:

1) UCDP (https://ucdp.uu.se)

  • Pettersson, Therese & Magnus Öberg (2020) Organized violence, 1989-2019.
    Journal of Peace Research 57(4).
  • Gleditsch, Nils Petter, Peter Wallensteen, Mikael Eriksson,
    Margareta Sollenberg, and Håvard Strand (2002) Armed Conflict 1946-2001:
    A New Dataset. Journal of Peace Research 39(5). 

2) STATISTIK AUSTRIA (https://statistik.at)
  
  • Volkswirtschaftliche Gesamtrechnung
""")


DATA = { }

SRCUFILE = os.path.join(SRCUDIR, "ucdp-aggregated.csv")
with open(SRCUFILE, mode='r', encoding="UTF-8", newline="") as fpu:
    csvu_input = csv.DictReader(fpu)
    for row in csvu_input:
        year = row["year"]
        intensity_level = row["intensity_level"]
        DATA[year] = [intensity_level, None]

SRCSFILE = os.path.join(SRCSDIR, "gdp-at-data.csv")
with open(SRCSFILE, mode='r', encoding="UTF-8", newline="") as fps:
    csvs_input = csv.DictReader(fps)
    prevgdp = None
    for row in csvs_input:
        year = str(row["year"])
        gdp = float(row["gdp"])
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
        POINTS_Y.append(float(gdp))


fig = plt.figure()
ax = fig.add_axes([0.14,0.10,0.80,0.82])
ax.scatter(POINTS_X, POINTS_Y)
ax.set_xlabel("world conflict intensity of a year [level]")
ax.set_ylabel("austrian GDP increase in a year [Million EUR]")
ax.set_title('world conflict intensity VS austrian gdp')
plt.savefig(DESTIMGFILE)
