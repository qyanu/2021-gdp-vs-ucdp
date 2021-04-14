
Manual SNA-AT Data Ingesting
============================

As the data downloaded from Statistik Austria has inconvenient formats
(PDF and XLS), the following steps are manually followed to extract and
combine said data.

* From file ``sna-at-data/volkswirtschaftliche_gesamtrechnungen_1976-2007.pdf``
  from table ``Tabelle 1``,
  from column ``Brutto-inlands-produkt``,
  the rows of years 1976 to 1994 (19 values),
  together with their respective ``Jahr`` row label,
  are manually extracted.

* From file ``sna-at-data/volkswirtschaftliche_gesamtrechnungen_1995_-_2018.pdf``
  from part ``Tabellenteil`` (page 25 and following),
  from table ``Tabelle 1``,
  from column ``Brutto-inlands-produkt``,
  the rows of years 1995 to 2015 (21 values),
  together with their respective ``Jahr`` row label,
  are manually extracted.

* From file ``sna-at-data/volkswirtschaftliche_gesamtrechnung_hauptgroessen.xlsx``,
  from sheet ``VGR Hauptgrößen``,
  from column ``Bruttoinlandsprodukt``,
  from sub-column ``laufende Preise`` (also labelled number "1"),
  the rows of years 2016 to 2019 (4 values),
  together with their respective ``Jahr`` row label,
  are manually extracted.

* All the extracted data above is saved into file
  ``sna-at-data-extracted/gdp-at-data.csv`` in CSV format,
  with the first column containing the "Jahr" row labels,
  the second column containing the extracted values.
  Numbers have a dot "." as decimal separator, the column separator is a
  comma ",".
  Column labels (or headers) are inserted as first line, with column labels
  "year" and "gdp".
