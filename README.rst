
******************************************************
 Correlating World Conflict with Local Economy Growth
******************************************************

Overview
========

For the average student, the
`Uppsala Conflict Data Program <https://ucdp.uu.se/>`_  offers
a fascinating periscope onto the conflicts of the world.
Together with economic figures as collected by
`Statistik Austria <https://www.statistik.at>`_,
the local economic impact of world-wide conflict is calculated.

WARNING: While this student is fairly confident regarding the numerical
correctness of the calculations, any conclusions have to be regarded as having
worse-than-questionable statistical validity.


Intended Applicability
======================

This work is intended to satisfy the curiosity of this student, and does not
lend itself to general deliberation.
However, one hopes to further the knowledge about the UCDP and suggests to
all readers to explore the insightes offered by the UCDP and related resources.


Ingested and Produced Data
==========================

Ingested data sets:

* "UCDP/PRIO Armed Conflict Dataset version 20.1", UCDP at
  Uppsala University, Sweden
* "Volkswirtschaftliche Gesamtrechnungen 1976-2007 (Standardpublikationen)",
  Statistik Austria, Austria
* "Volkswirtschaftliche Gesamtrechnungen 1995 - 2018 (Standardpublikationen)",
  from Statistik Austria, Austria
* "Volkswirtschaftliche Gesamtrechnung Hauptgrößen", from Statistik Austria,
  Austria; as published on 2021-04-14

Note, that the ODATA-portal operated by Statistik Austria does offers many
data sets via a machine-readable API, however the sought after GDP data set
is not available there.


.. image:: dataflow-overview.pdf
  :width: 100%
  :alt: Data Flow Overview


The data from Statistik Austria is filtered and combined as follows:

* from "Volkswirtschaftliche Gesamtrechnungen 1976-2007" the data for the
  years 1976 to 1994 are used.
* from "Volkswirtschaftliche Gesamtrechnungen 1995 - 2018" the data for the
  years 1995 to 2015 are used.
* from "Volkswirtschaftliche Gesamtrechnung Hauptgrößen" the data for years
  2016 to 2019 are used.
* all three data are combined, in order, into a single table, and the yearly
  gdp increase is calculated.
  see file ``sna-at-data-combined/gdp-at-data.csv``.
  (See file ``extract-and-combine-sna-at.pdf`` for details.)

From the UCDP the sum of all intensity level of all conflicts active each
year is used.


Produced Data
-------------

Cross calculates a x-y plot, comparing both input data sets for direct
calculation. This plot is generated as machine-parseable csv file, and
as human displayable svg file.
See directory ``output-data/``.


Result
======

.. image:: output-data/x-y-plot.pdf
  :width: 100%
  :alt: X-Y Result Plot

Raw scatter plot points: `<output-data/x-y-plot.csv>`_

There is no discernable correlation of yearly gdp change and yearly
world conflict intensity.
