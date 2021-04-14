#!/usr/bin/env python3

"""
this script reads the UCDP data and processes it.
the result is placed into subdirectory ``ucdp-data-extracted/``.
"""

import csv
import os.path

SRCDIR = os.path.join(os.path.dirname(__file__), "ucdp-data")
DESTDIR = os.path.join(os.path.dirname(__file__), "ucdp-data-extracted")

SRCFILE = os.path.join(SRCDIR, "ucdp-prio-acd-201.csv")
SRCCITEAS = os.path.join(SRCDIR, "CITE-AS")
DESTFILE = os.path.join(DESTDIR, "ucdp-aggregated.csv")
DESTLICENSE = os.path.join(DESTDIR, "LICENSE")
DESTCITEAS = os.path.join(DESTDIR, "CITE-AS")

DATA = { }

with open(SRCFILE, mode='r', encoding="UTF-8", newline="") as fp:
    csv_input = csv.DictReader(fp)
    for row in csv_input:
        year = row["year"]
        if int(year) < 1977:
            continue
        intensity = int(row["intensity_level"])
        if year not in DATA:
            DATA[year] = 0
        DATA[year] += intensity

with open(DESTLICENSE, mode='w', encoding='UTF-8') as fpout:
    fpout.write(
"""Data in this directory is extracted from (is a sub-set of) the data
in directory ``ucdp-data/``.
See there for LICENSE.""")

with open(SRCCITEAS, mode='r', encoding='UTF-8') as fpin, \
     open(DESTCITEAS, mode='w', encoding='UTF-8') as fpout:
    fpout.write(fpin.read())

DSTFIELDNAMES = ("year", "intensity_level")

with open(DESTFILE, mode='w', encoding="UTF-8", newline="") as fp:
    csv_output = csv.DictWriter(fp,
        fieldnames=DSTFIELDNAMES)
    csv_output.writeheader()
    for key in sorted(DATA.keys()):
        csv_output.writerow({
            "year": key,
            "intensity_level": DATA[key],
            })
