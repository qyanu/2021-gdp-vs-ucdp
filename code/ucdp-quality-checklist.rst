
*****************************
 UCDP Data Quality Checklist
*****************************

This document details step-by-step the planned items to be performed
in order to assert a certain minimum data quality of the UCDP source data
and intermediate sets.

Preparations
============

* ensure, that the project's general buildscript ``build.sh`` has
  been successfully executed. See section `How to Build` in the README file.


UCDP source data set
====================

The UCDP source data set can be found in directory `ucdp-data/`.

#. does the file ``ucdp-prio-acd-201.csv`` exist in this directory?
#. did the general buildscript `build.sh` output a line?::

     verifying downloaded data is as expected and was not damaged...OK

UCDP intermediate data set
==========================

The intermediate UCDP data set extracted and aggregated from the UCDP
source data set can be found in directory `ucdp-data-extracted/`.

#. Inspect the rendering of the intermediate data set in that directory:
   `ucdp-data-extracted.pdf <ucdp-data-extracted/ucdp-data-extracted.pdf>`_

   * Are all values strictly positive?
   * Does the data encompas the year range 1977 to 2019?
