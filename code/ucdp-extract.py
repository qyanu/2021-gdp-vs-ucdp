#!/usr/bin/env python3

"""
this script reads the UCDP data and processes it.
the result is placed into subdirectory ``ucdp-data-extracted/``.
"""

import csv
import os.path
import sys

SRCDIR = os.path.join(os.path.dirname(__file__), "..", "ucdp-data")
DESTDIR = os.path.join(os.path.dirname(__file__), "..", "ucdp-data-extracted")

SRCFILE = os.path.join(SRCDIR, "ucdp-prio-acd-201.csv")
SRCCITEAS = os.path.join(SRCDIR, "CITE-AS")
DESTFILE = os.path.join(DESTDIR, "ucdp-data-extracted.csv")
DESTLICENSE = os.path.join(DESTDIR, "LICENSE")
DESTDATASOURCE = os.path.join(DESTDIR, "DATA-SOURCE")
DESTMETA = os.path.join(DESTDIR, "META.xml")

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

with open(DESTMETA, mode='w', encoding='UTF-8') as fpout:
    fpout.write(
"""<?xml version="1.0" encoding="utf-8"?>
<simpledc xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title xml:lang="en"
        >World conflict cummulative intensity per year, 1977 - 2019</dc:title>
    <dc:contributor>Max-Julian Pogner &lt;max-julian@pogner.at&gt;</dc:contributor>
    <dc:description xml:lang="en"
        >Based on the UCDP/PRIO 20.1 dataset, the per-year cummulative world conflict level is calculated as the sum of all `intensity_level` values of all conflicts active in a particular year.</dc:description>
    <dc:publisher>Max-Julian Pogner &lt;max-julian@pogner.at&gt;</dc:publisher>
    <dc:date>2021-04-17</dc:date>
    <dc:type>http://purl.org/dc/dcmitype/Dataset</dc:type>
    <dc:format>text/csv</dc:format>
    <dc:relation>Uppsala Conflict Data Program https://ucdp.uu.se/downloads/</dc:relation>
    <dc:source>Pettersson, Therese &amp; Magnus Öberg (2020) Organized violence, 1989-2019. Journal of Peace Research 57(4).</dc:source>
    <dc:source>Gleditsch, Nils Petter, Peter Wallensteen, Mikael Eriksson, Margareta Sollenberg, and Håvard Strand (2002) Armed Conflict 1946-2001: A New Dataset. Journal of Peace Research 39(5).</dc:source>
    <dc:coverage>1977-2019</dc:coverage>
</simpledc>
"""
)

with open(SRCCITEAS, mode='r', encoding='UTF-8') as fpin, \
     open(DESTDATASOURCE, mode='w', encoding='UTF-8') as fpout:
    fpout.write("The data in this directory is calculated based on:\n\n\n")
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

sys.stdout.write(f"{sys.argv[0]} finished.\n")
