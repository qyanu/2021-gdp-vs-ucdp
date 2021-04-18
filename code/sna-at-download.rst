
Manual SNA-AT Downloading
=========================

As the data from Statistik Austria cannot be easily linked or automatically
downloaded, the following steps are manually followed to download the
SNA-AT data.

#. Verify that the license statement (see `sna-at-data/LICENSE` for the last
   seen incarnation) still applies and still consents to the use according to
   this project.
#. Perform the following steps within the web area of https://statistik.at/

   * Find and download the `Volkswirtschaftliche Gesamtrechnungen 1976-2007.pdf`
   * Find and download the `Volkswirtschaftliche Gesamtrechnungen 1995 - 2018.pdf`
   * Find and download the `Volkswirtschaftliche Gesamtrechnung Hauptgroessen.xlsx`

#. Save all files, in their original naming and with unchanged content, to the
   directory `sna-at-data/`, replacing any previously downloaded files there.
#. Update the license statement in file `sna-at-data/LICENSE`, according to
   the current situation.
#. update associated meta data in `sna-at-data/META.xml`, and
#. update information in file `sna-at-data/DATA-SOURCE` accordingly.

Note: If the content of the downloaded data has changed in a way that is
incompatible with the scripts in this project (e.g. change of data format), the
scripts and possibly other project files have to be adapted accordingly.

Expected future change: As the file `volkswirtschaftliche_gesamtrechnung_hauptgroessen.xlsx`
only contains the figures of the most recent years, and statistik austria
is expected to issue a more permanent publication of the figures for years
2016 to 2019 in the future, it is expected that exact reproducibility of the
download is **not** given. A future permanent pdf publication is expected to be
useable as replacement for the xlsx file. However note, that gdp figures up to
36 months prior to the creation of a certain downloaded file may only be
preliminary.


quality ensuring the downloaded data
------------------------------------

The downloader shall open all downloaded files, using a pdf viewer and/or
spreadsheet calculator, and verify that, according to the labelling contained
in the files, cummulatively the downloaded files contain (among othe content)
the figures on the austrian gross domestic product spanning at least the years
1977 to 2019.

Last time, the following software for inspecting the downloaded files
was used:

* :literal:`okular` v1.3.2
* :literal:`localc` from LibreOffice 6.1.5.2 10(Build:2)
