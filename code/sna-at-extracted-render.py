#!/usr/bin/env python3

"""
this script renders the manually extracted file
sna-at-extracted/sna-at-data-extracted.csv

into file
sna-at-extracted/sna-at-data-extracted.pdf

for visual inspection.
"""

import csv
import matplotlib.pyplot as plt
import os.path
import sys
from decimal import Decimal

DATADIR = os.path.join(os.path.dirname(__file__), "..", "sna-at-data-extracted")

SRCFILE = os.path.join(DATADIR, "sna-at-data-extracted.csv")
DSTFILE = os.path.join(DATADIR, "sna-at-data-extracted.pdf")

points_year = [ ]
points_gdp = [ ]

with open(SRCFILE, mode='r', encoding="UTF-8", newline="") as fps:
    csv_input = csv.DictReader(fps)
    for row in csv_input:
        year = int(row["year"])
        gdp = Decimal(row["gdp"])
        points_year.append(year)
        points_gdp.append(gdp)

fig = plt.figure()
ax = fig.add_axes([0.14,0.10,0.80,0.80])
ax.plot(points_year, points_gdp)
ax.set_xlabel("year")
ax.set_ylabel("Austrian GDP [Billion EUR]")
ax.set_title('Austrian GDP (nominal)\nSource: STATISTIK AUSTRIA')
plt.savefig(DSTFILE)

sys.stdout.write(f"{sys.argv[0]} finished.\n")
