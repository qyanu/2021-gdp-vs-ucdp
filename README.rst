
******************************************************
 Correlating World Conflict with Local Economy Growth
******************************************************

Overview
========

For the average student, the
`Uppsala Conflict Data Program <https://ucdp.uu.se/> <https://ucdp.uu.se/>`_
offers a fascinating periscope onto the conflicts of the world.
Together with economic figures as collected by
`Statistik Austria <https://www.statistik.at> <https://www.statistik.at>`_,
the local economic impact of world-wide conflict is calculated.

WARNING: While this student is fairly confident regarding the numerical
quality of the calculations, any conclusions have to be regarded as having
worse-than-questionable statistical validity.

This project is also covered by an included
`Data Management Plan <data-management-plan.pdf>`_
(also available as `machine actionable version <data-management-plan.json>`_).


How to Build
============

1. Optionally, reproduce the manual download steps as described in file
   `sna-at-download <code/sna-at-download.pdf>`_

   Note: this git repository should already contain the results from a
   previous manual download of the SNA-AT data.

2. Optionally, reproduce the manual extract & combine steps as described in
   file `sna-at-extract-and-combine <code/sna-at-extract-and-combine.pdf>`_

   Note: this git repository should already contain the results from a
   previous extract & combine process.

3. Execute the build script::

   $ build.sh

4. Perform data quality verification according to the
   `UCDP Data Quality Checklist <code/ucdp-quality-checklist.pdf>`_

Build Output Description
------------------------

directory `output-data/`
\... the final output and result.

directory `ucdp-data`
\... the UCDP data as downloaded from UCDP webpage.

directory `ucdp-data-extracted`
\... the intermediate data based on the UCDP data.

directory `sna-at-data`
\... the SNA-AT data as downloaded from STATISTIK AUSTRIA webpage.

directory `sna-at-data-extracted`
\... the intermediate data based on the SNA-AT data.

Build Dependencies
------------------

* :literal:`bash5`
* :literal:`python3.7`
* :literal:`dot` from the graphviz package v2.40.1
* :literal:`python3-matplotlib` v3.0.2-2
* :literal:`python3-ruamel.yaml` v0.15.34-1+b1
* :literal:`rst2pdf` v0.93.dev0
* :literal:`curl` v7.64.0
* various tools from the :literal:`coreutils` package v8.30 are used.

Note: this project was developed on a Debian Linux "Buster" 10 operating
system with a K Desktop Environment.

Development Dependencies
------------------------

Only needed for scripts other than build.sh, which are not intended to
be used by the normal user.

* ``pip3 install 'jsonschema>=3.2.0'``


Intended Applicability
======================

This work is intended to satisfy the curiosity of this student, and does not
lend itself to general deliberation.
However, one hopes to further the knowledge about the UCDP and suggests to
all readers to explore the insightes offered by the UCDP and related resources.


Ingested and Produced Data
==========================

Ingested data sets:

* `UCDP/PRIO Armed Conflict Dataset version 20.1`,
  from the `UCDP at Uppsala University <https://ucdp.uu.se>`_, Sweden

  * Pettersson, Therese & Magnus Öberg (2020) `Organized violence, 1989-2019`.
    Journal of Peace Research 57(4).
  * Gleditsch, Nils Petter, Peter Wallensteen, Mikael Eriksson,
    Margareta Sollenberg, and Håvard Strand (2002) `Armed Conflict 1946-2001:
    A New Dataset`. Journal of Peace Research 39(5).

* `Volkswirtschaftliche Gesamtrechnungen`,
  from `STATISTIK AUSTRIA <https://www.statistik.at>`_, Austria

  * `Volkswirtschaftliche Gesamtrechnungen 1976-2007 (Standardpublikationen)`,
     Statistik Austria, Austria
  * `Volkswirtschaftliche Gesamtrechnungen 1995 - 2018 (Standardpublikationen)`,
     from Statistik Austria, Austria
  * `Volkswirtschaftliche Gesamtrechnung Hauptgrößen`, from Statistik Austria,
     Austria; as published on 2021-04-14

Note, that the ODATA-portal operated by Statistik Austria does offer many
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


Results
=======

.. image:: output-data/output-data.pdf
  :width: 100%
  :alt: Output Data Plot

Raw scatter plot points: `<output-data/output-data.pdf.csv>`_

There is no discernable correlation of yearly gdp change and yearly
world conflict intensity.
