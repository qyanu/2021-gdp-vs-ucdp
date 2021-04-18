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

DATADIR = os.path.join(os.path.dirname(__file__), "..", "ucdp-data-extracted")

SRCFILE = os.path.join(DATADIR, "ucdp-data-extracted.csv")
DSTFILE = os.path.join(DATADIR, "ucdp-data-extracted.pdf")

points_year = [ ]
points_intensity_level = [ ]

with open(SRCFILE, mode='r', encoding="UTF-8", newline="") as fps:
    csv_input = csv.DictReader(fps)
    for row in csv_input:
        year = int(row["year"])
        intensity_level = int(row["intensity_level"])
        points_year.append(year)
        points_intensity_level.append(intensity_level)

fig = plt.figure()
ax = fig.add_axes([0.14,0.10,0.80,0.80])
ax.plot(points_year, points_intensity_level)
ax.set_xlabel("year")
ax.set_ylabel("Cummulative Intensity Level")
ax.set_title('World Cummulative Intensity Level')
plt.savefig(DSTFILE)

sys.stdout.write(f"{sys.argv[0]} finished.\n")
