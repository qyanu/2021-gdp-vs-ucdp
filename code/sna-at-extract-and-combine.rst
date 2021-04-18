
Manual SNA-AT Data Ingesting
============================

As the data downloaded from Statistik Austria has inconvenient formats
(PDF and XLS), the following steps are manually followed to extract and
combine said data.

Note the **error-resilient data-entry** method described **below**.

* From file ``sna-at-data/volkswirtschaftliche_gesamtrechnungen_1976-2007.pdf``
  from table ``Tabelle 1``,
  from column ``Brutto-inlands-produkt``,
  the rows of years 1976 to 1994 (19 values),
  together with their respective ``Jahr`` row label,
  are manually extracted.

  * check the first and last value of the pasted rectangular, if these two
    values exactly match the source value.

* From file ``sna-at-data/volkswirtschaftliche_gesamtrechnungen_1995_-_2018.pdf``
  from part ``Tabellenteil`` (page 25 and following),
  from table ``Tabelle 1``,
  from column ``Brutto-inlands-produkt``,
  the rows of years 1995 to 2015 (21 values),
  together with their respective ``Jahr`` row label,
  are manually extracted.

  * check the first and last value of the pasted rectangular, if these two
    values exactly match the source value.

* From file ``sna-at-data/volkswirtschaftliche_gesamtrechnung_hauptgroessen.xlsx``,
  from sheet ``VGR Hauptgrößen``,
  from column ``Bruttoinlandsprodukt``,
  from sub-column ``laufende Preise`` (also labelled number "1"),
  the rows of years 2016 to 2019 (4 values),
  together with their respective ``Jahr`` row label,
  are manually extracted.

  * check the first and last value of the pasted rectangular, if these two
    values exactly match the source value.

* All the extracted data above is saved into file
  ``sna-at-data-extracted/sna-at-data-extracted.csv`` in CSV format,
  with the first column containing the "Jahr" row labels,
  the second column containing the extracted values.
  Numbers have a dot "." as decimal separator, the column separator is a
  comma ",".
  Column labels (or headers) are inserted as first line, with column labels
  "year" and "gdp".

* Perform data quality checks:

  #. Count the number of copy & pasted cells after each copy&paste, if
     they match the intended number of years extracts.
  #. Check the magnitude of all copied data cells:

     * They must contain strictly positive values,
     * are expected to contain non-integer numbers (that is, with some
       decimal places) in the almost all cells.

  #. execute script
     `code/sna-at-extracted-render.py <code/sna-at-extracted-render.py>`_
  #. open the generated pdf
     `sna-at-data-extracted/sna-at-extracted.pdf
     <sna-at-data-extracted/sna-at-data-extracted.pdf>`_

     * is any GDP value below zero?
     * is the yearly range correct (1977 to 2019)?

error-resilient data-entry
--------------------------

The SNA-AT data manually extracted from pdf, should be done by using
copy & paste with a free-rectangular tool.

Using such a tool, internal details of the PDF are of no consideration
to the copy & paste process, only the arrangement of the data on screen
as displayed by the pdf viewer. Also, typos when typing a copy of the
values is mitigated.

By drawing said rectengular of the tool with the mouse around the table
values intended to be extracted, only the data intended to be extracted
is copy & pasted into `localc`.

The rectangular copy tool used is `okular` (version 1.3.2), a standard
tool included in the `K Desktop Environment` as distributed with the
operating system `Debian 10`.


software requirements
---------------------

Last time, the following software for working with the downloaded files
and to create the intermediate data set was used:

* :literal:`okular` v1.3.2
* :literal:`localc` from LibreOffice 6.1.5.2 10(Build:2)
