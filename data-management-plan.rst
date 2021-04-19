
**********************
 Data Management Plan
**********************

Project Title
    `Correlating World Conflict with Local Economy Growth`

Project Abstract
    For the average student, the
    `Uppsala Conflict Data Program <https://ucdp.uu.se/> <https://ucdp.uu.se/>`_ 
    offers a fascinating periscope onto the conflicts of the world.
    Together with economic figures as collected by
    `Statistik Austria <https://www.statistik.at> <https://www.statistik.at>`_,
    the local economic impact of world-wide conflict is calculated.

Public Project Repository DOI
  https://doi.org/10.5281/zenodo.4699808

Public Project Repository URL
  https://github.com/qyanu/2021-gdp-vs-ucdp

Creator
  `Max-Julian Pogner <max-julian@pogner.at> <mailto:max-julian@pogner.at>`_,
  a student at `TU Wien <https://tuwien.ac.at> <https://tuwien.ac.at>`_
  (**without endorsement** on the part of `TU Wien`).

Organization
  The author of this project acts in his own right.

DMP Template
  `Practical Guide to the International Alignment of Research
  Data Management` (Extended Edition with DMP Evaluation Rubric),
  Science Europe, January 2021,
  https://www.scienceeurope.org/media/4brkxxe5/se_rdm_practical_guide_extended_final.pdf

DMP DOI
  https://doi.org/10.5281/zenodo.4699775

Last Modified
  19\. April 2021


.. footer::

   ###Page### / 18

.. raw:: pdf

   PageBreak



1. DATA DESCRIPTION AND COLLECTION OR RE-USE OF EXISTING DATA
=============================================================

This section describes how data collection is performed respectively
can be re-produced, as well as describes the type, format, size and license
considerations per data set. For there inseparable nature, both questions
are handled together:

* 1a. How will new data be collected or produced and/or how will existing data be re-used?
* 1b. What data (for example the kind, formats, and volumes), will be collected or produced?

Overview
--------

Collected source data comes from two sources

* `ucdp-data` is from the `Uppsala Conflict Data Program` (UCDP) at Uppsala
  University, Sweden, via download from https://ucdp.uu.se/downloads/ and
* `sna-at-data` is from the `Volkswirtschaftliche Gesamtrechnung` (SNA-AT) by
  STATISTIK AUSTRIA, Austria, via download from subpages of
  https://statistik.at.

Intermediate data is calculated based on the respective source data

* `ucdp-data-extracted` is based on `ucdp-data`, and
* `sna-at-data-extracted` is based on `sna-at-data`.

Final output data `output-data` is calculated based on both intermediate data
sets.

Quick Guide
-----------

So long as access to at least the public project git repository is given,
all manual steps have already been performed, and executing the steps detailed
in section "How to Build" of the `README <README.pdf> <README.pdf>`_
is sufficient. It basically boils down to executing a single bash script::

  $ build.sh

Uniform project CSV
-------------------

The `csv` data format is chosen by this project as the principal data format,
as it is the most simple and most universal data format still supporting all
relevant characteristics required by this project.

This data management plan often refers to a "uniform project csv"
data format. This names the csv data format adopted by this project. As CSV is
not formally standardized, each project has to ensure the most practical csv
variation is followed.

This project elects to follow the csv format as used by the python3.7 module
`csv` to maximize machine-processability as well as ensuring a widely
adopted csv variation is used.

Of specific remark are the following properties of the "uniform project `csv`"
data format:

* produced csv files always have column labels as first row.
* produced csv files never contains the newline character "\\n" within
  cell values.
* number values are rendered in a machine-friendly format, with dot '.' decimal
  separator and no thousands separator.
* date and time values are rendered as ISO8601 (e.g. `YYYY-MM-DD`)

SNA-AT Source Data from Statistik Austria
-----------------------------------------

SNA-AT data from Statistik Austria has to be downloaded manually, and is then
preserved in the directory `sna-at-data` of the project git repository.

This data set itself is tabular numeric data, split into multiple parts, and
wrapped in inconvenient container formats `pdf` and `xlsx`.
The contained information is concerned with the numeric calculation of common
key economic indicators.

If the download has already been performed, the previously downloaded data can
already be found stored in that directory.
A (re-)download is/was performed according to the steps laid out in the
document `Manual SNA-AT Downloading <code/sna-at-download.pdf>
<code/sna-at-download.pdf>`_ found in the project git repository.

Intermediate Data based on SNA-AT
---------------------------------

SNA-AT-EXTRACTED data is manually extracted from the files within the SNA-AT
data collection and manually combined, then the resulting intermediate data
is preserved in the directory `sna-at-data-extracted` of the project git
repository.

This data set itself is tabular numeric data, in uniform project `csv` format.
The contained information is a merged and converted sub-set of the `sna-at`
data set.

The process is detailed in the document `Manual SNA-AT Data Ingesting
<code/sna-at-extract-and-combine.pdf>
<code/sna-at-extract-and-combine.pdf>`_ found in the project git repository.

Source Data from UCDP
---------------------

Due to license considerations, the data downloaded from UCDP cannot be stored
in a public git repository. In case you have access to the non-public git
repository, the data is already downloaded and stored in the directory
`ucdp-data`. Otherwise, the data *must* be re-downloaded.

(Re-)download is automatically performed as a step within the general
buildscript `build.sh`, but can be performed explicitly with script
`code/ucdp-download.sh`. Note, that this script will compare the final
acquired `csv` file with a known sha256 content checksum, in order to ensure
an undamaged file was acquired.

The data format `csv` is chosen for it's highest compatibility and highest
world-wide and long-time support. The other available formats where either
rejected (`xlsx` was deemed unfit, due to the almost only 100% compatible
software, `Excel` likely to experience problems with some data-sets provided
by the UCDP, including the subject data set), or un-preferred (`RData` and
`STATA` due to less expected compatibility and providing features not required
by this project).

This data set itself is tabular numeric, labelling and categorizing data, in
ucdp `csv` format.

Intermediate Data based on UCDP
-------------------------------

Due to license considerations, the data extracted and aggregated from the
UCDP data cannot be stored in a public git repository. In case you have access
to the non-public git repository, the data is already extracted and aggregated
and stored in the directory `ucdp-data-extracted`.
Otherwise, the data *must* be re-processed to acquire the `ucdp-data-extracted`
data.

`ucdp-data-extracted` data is automatically extracted and aggregated as a
step within the general buildscript `build.sh`, but can be performed
explicitly with script `code/ucdp-extract.py`. This script will read the
`ucdp` data from the directory `ucdp-data`, process it, and put the result
intermediate data set `ucdp-extracted` data in directory `ucdp-data-extracted`.

This data set itself is tabular numeric data, in uniform project `csv` format.

Output Data
-----------

Due to license considerations, the final output data cannot be stored
in a public git repository. In case you have access to the non-public git
repository, the data is already calculated and stored in the directory
`output-data`. Otherwise, the data *must* be re-calculated.

`output` data is automatically calculated as a step within the general
buildscript `build.sh`, but calculations can be performed explicitly with
script `code/cross.py`. This script will read the `ucdp-extracted` and
`sna-at-extracted` data set, and process them, and put the resulting
`output` data set into the `output-data` directory.

This output data itself is a correlation-/xy-plot, with all points stored
in uniform project `csv` format.

The data points are additionally rendered as `pdf` format form human
consumption, but the rendering strictly contains only information also
contained within the `csv` format.

Overall Data Volume
-------------------

Total cummulative data size settles just below 10 MB, and if the
calculations of this project are repeated at a later time, the upper bound of
data volume is expected to follow a linear growth model with circa 1.1 MB
additional each year.

Methodology of Reproducibility
------------------------------

All operations on the data are implemented using scripts and programs, or are
undertaken manually by a human according to a step-by-step guide if
programmatic processing is not possible.
The main scripts and programs should not require any parameters.

By excluding other venues of data retrieval or data processing, all such
actions are automatically reproducible.

A single top-level `build.sh` script is provided to offer an easy way to
re-perform all automateable actions, ensuring that after `build.sh` has been
successfully executed, all artifacts correspond to a consistent state and
contain their respective reproducible content.

This method also provides documentation of the individual data collection and
processing steps, as per community conventions and traditions
(cf. the proverb `read the source!`).
Albeit, the quality of documentation is subject to the ability of the source
code writer to produce readable and well-structured source code (A feat
which includes providing a clear, coherent and thorough description of the
function and purpose of each script or program near the very beginning of the
respective source code files) and the ability of the person interested in
making use of the documentation to read source code files in the respective
scripting or programming language.

Data Preservation
-----------------

For data preservation and reproducibility purposes, the code, the source data,
the intermediate data, the output data as well as all auxilliary build
artifacts (such as the pdf rendering of this data management plan) are all
stored within the same project git repository.

Due to the magnitude of data overall size, this approach is feasible.
This approach is also advisable and practical, as reducing the number of
different places and packaging everything nicely together increases later
findability and aides in long-term preservation of the project in a functional
form.

For the purpose of licensing (see below) a distinction between public and
non-public copies of the project git repository is made. While non-public
data sets cannot be preserved in a public copy of the git repository, the
automatic general buildscript offers easy download of the non-public parts.
Non-public project git repository/-ies contain all data.

Data Licensing
--------------

The data from UCDP and STATISTIK AUSTRIA have to be treated separately, from a
license perspective.

Data from STATISTIK AUSTRIA is marked with a clear license statement,
effectively consenting to a wide range of activities, including re-publishing
of the original data as well as re-publishing of extractions of and derivative
works based on the data. Certain provisions to attach specific remarks and
notes to re-publications, extractions and derivative works must be observed.

Data from the UCDP lacks a clear copyright or license statement.
The download page (the webpage where download to the data is offered) does not
make any copyright or license statements, nor is such statement included in
the downloaded data set. And while the public restrictionless downloadability
of the UCDP data set can be legally construed as consenting to unlimited
downloading, inspecting and locally using all data from the UCDP, as far as
this author without any legal education knows, cannot be treated any form of
agreement to re-publishing the data;

As a consequence, such the data sets consisting of or being based on the
UCDP data is treated as non-public by this project.

Specifically the data sets `sna-at-data` and `sna-at-data-extracted`
bear the license from STATISTIK AUSTRIA and is marked public.
The data sets `ucdp-data` and `ucdp-data-extracted` do not bear a license
permitting re-publishing and is marked non-public.
The data set `output-data`, being principally based on both source data sets,
has unclear license status and is marked non-public.
Code and auxilliary files in this project, fully created by the project team,
will be separately licensed and is marked public.

The differing license situations of the individual parts of this project
are clearly documented/issued in the `LICENSE` files in the respective
(sub-)directories.

.. raw:: pdf

   PageBreak



2. DOCUMENTATION AND DATA QUALITY
=================================

2a. What metadata and documentation (for example the methodology of data collection and way of organising data) will accompany the data?
----------------------------------------------------------------------------------------------------------------------------------------

Each data set, as well as the code, has associated meta-data in a file
:literal:`META.xml`. The filename was chosen to follow the tradition and
convention of storing meta-data, such as LICENSE, TODO, etc, in files with
all-caps naming, if either the principal data does not support embedded
meta-data, or such embedding is deems impractical.

The `META.xml` files contain meta-data compliant with `simpledc.xsd` as
published by the Dublin Core Metadata Initiative, with as many terms from
`https://dublincore.org/schemas/xmls/qdc/2008/02/11/dc.xsd` filled with values
as was meaningful. Validity of all `META.xml` files can be verified with script
``code/meta-verify.sh``.

This author's upbringing is somewhat overlapping with the conventions and
traditions predominent within the Open Source Software-Development Community.
Not incidentally, this project commit to observe and refine these informal
standards and common processes. As such

* versioning, insofar as a new version of a data or files semantically replaces
  the previous version, is handled through the usage of a git repository,
* common meta-data is stored in files with all-caps and well-known filenames
  (with an optional additional lower-case file extention)
  such as `README`, `LICENSE`, etc,
* performed steps are clearly and reproducibily documented by way of source
  code,
* source code follows the principles of nice-to-read and clear-structured,
  beyond the functionally necessary,

  * for example, each script and program source code must have a description of
    it's purpose and function near the very beginning of it's content.

* binary or other source formats not easily readible by means of simple text
  editor are discouraged, maximizing compatibility and machine-actionability
  of source code files with future iterations of the software tools landscape.

  * for example with this reasoning, this Data Management Plan is **not**
    written using the **DMP-Online** tool for it's lack of compatibility
    with a wide range of editors (namely only a single homepage can be used)
    as well as difficulties to track edit changes through a version control
    system such as git.
  * with similar reasoning, the **reStructuredText** (:literal:`rst`) format is
    preferred by the relevant community over the *Markdown* (:literal:`md`)
    format en-vogue in some adjacent communities, due to Markdown suffering
    from the same problems as `csv`; in constrast to `md` (with multiple
    entities publishing partially conflicting specification, in addition to
    not being well-defined in the mathematical sense), `rst` is syntactically
    and semantically well-defined, does not suffer from certain security flaws
    (e.g. remote-code execution when viewing a `md` document, if the viewer
    does not exhibit the most zealous of input validation, in contrast of `rst`
    avoiding such parser problems already at the average input validation
    level).

* and many other implicitly followed best practices.


A note on directory structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Files with well-known purpose receive their respective well-known names
in all-caps, plus an optional lower-case file type and format extension.
Specifically this concerns the files `LICENSE`, `README.rst` and similar.

This project's main division of content is by data-set/code into
(sub-)directories. The names of directories are, disregarding encoding
intricacies (e.g. avoidance of whitespaces), identical to the names of the
respective data sets or project parts.

* :literal:`code/` contains scripts, program source code and auxilliary
  files created by this project team, only of interest to a person either
  editing the project, or interested in the project in a similar degree. Files
  in this directory are public.
* :literal:`output-data/` contains final output data set. An unknown license
  applies. Files in this directory are therefore non-public.
* :literal:`sna-at-data/` contains the data as downloaded from STATISTIK AUSTRIA.
  Their license statement applies. Files in this directory are publishable.
* :literal:`sna-at-data-extracted/` contains the merged, filtered and extracted
  sub-data set from the `sna-at-data` data. As this is a derivative work of
  `sna-at-data`, the same license statement from STATISTIK AUSTRIA applies.
  Files in this directory are publishable.
* :literal:`ucdp-data/` contains the data as downloaded from UCDP.
  As no license statement was given by UCDP, this data must not be re-published.
  Files in this directory are therefore non-public.
* :literal:`ucdp-data-extracted/` contains processed data result of the
  UCDP data set. As this is a derivative work of `ucdp-data`, the same
  license considerations apply. Files in this directory are therefore non-public.
* :literal:`/` contains such files as are of primary interest to a first-time
  casual reader of the project. All files are created by this project team and
  are public.

As the number of items per directory already reaches non-excessive magnitude,
and recalling the fact that humans find deep-nested directory structures less
easy to work with than flat structures (so long as the number of items does
not become excessive), no further sub-divisions are performed.

This sub-division of the project files conveniently also arranges the files
according to the respective licensing situation.

A note on file naming
^^^^^^^^^^^^^^^^^^^^^

Versioning of files is handled by the built-in features of a git repository,
and the default concept of git is followed in this respect. No version
information is included as part of file names, so long as a new version of
a file semantically replaces earlier versions of that file.

In the directories replicating the source data collected from external source
(`sna-at-data` and `ucdp-data`), the exact file naming as used by the external
source is preserved. This way a later reader of the project can more easily
trace which data exactly were downloaded.

All meta-data also managed by the git repository, such as researcher name,
date of edits, etc, are treated equivalent to versioning described above,
and therefore are also not included in file names.

Whitespaces and special symbols are avoided. In order to not crash windows
machines, certain names are prohibited: ``aux``, ``con``, ``com``, etc.

Note: The file naming conventions detailed in this documented have been
informed by
https://datamanagement.hms.harvard.edu/collect/file-naming-conventions.

Naming of data sets
^^^^^^^^^^^^^^^^^^^

The data sets where intentionally named, such that a first-time reader can
easily discern relationships (`-data` => `-data-extracted`), stage
("output") or category (`sna-at` vs `ucdp`).

A note on versioning in public repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the purpose of making the project git repository publicly available,
`squashing` the git repository might be decided to be done by the project
stakeholders, out of consideration for privacy (in order to not publish at which
times of day a particular project team member has worked on the project),
security (in order to not publish critical bits of information that erronously
were committed and then deleted), or public relations (in order to not publicly
present information that might be utilized by a malevolent third party).
In this case,

* the content (:literal:`commit^{tree}`) before and after the
  squashing must be verified to be byte-by-byte equal.
* the correspondence of private git repository version with squashed public git
  repository version is tracked using mechanisms already built-in into the
  git repository.


2b. What data quality control measures will be used?
----------------------------------------------------

Due to the limited size and scope of the project, and the absence of any other
person that participate in this project, relying on the good practices of
the author seems unavoidable. Peer review or four-eyes principle is
unattainable.

Regarding the quality of data itself, no domain-specific knowledge for the two
data sets exist within the project team for the domains of conflict data or
country economic data.

"layman-knowledge" can be applied for the verification of data,

* after the downloading step (at the source data sets),
* after part of the processing was performed (at the intermediate data sets),
* after complete processing has finished (at the output data set).

The verification is already part of the step-by-step guides for manual
data collection, extraction and merging (see files
`code/sna-at-download.pdf <code/sna-at-download.pdf>`_,
`code/sna-at-extract-and-combine.pdf <code/sna-at-extract-and-combine.pdf>`_),
and additional verification checklists are pointed to by section in the
README (see `README.rst <README.pdf>`_ section "How to Build", pointing
to `code/ucdp-quality-checklist.pdf <code/ucdp-quality-checklist.pdf>`_)
that also the most casual reader of this project must encounter -- It is
supposed that users who do not even read the "How to Build" secion of
the README would also never follow pointers to, or perform steps
recommended by, a data qualitiy checklist.

By placing the checklists (or pointer to them) at places where a user
performing or invoking a data collection or data processing, it is hoped
that an interested user is reminded of their presence just at the most
convenient time.

"layman-knowledge" verification is performed through aforementioned
checklists according to the following principles:

* numerical magnitude and range of values is known.
* interpretation (whether they indicate data errors or are expected in a normal
  data set) of outliers is not possible --

  For example to verify that the impact of major historical events such as
  the collapse of the soviet union, the ascention of EU membership of
  Austria, the 2008 crisis of the EU financial sector and currently the
  Covid-19 pandemic is duly reflected in the respective data sets, would
  require more-than-layman knowledge of the respective domain.

* humans more easily recognize patterns or anti-patterns on visualizations
  of data (e.g. graphs), compared to looking at the `csv` data directly.

The content of the data verification checklists was informed
by reading of https://old.dataone.org/best-practices/quality,
which was recommended by aforementioned DMP-Online webpage.
From that source, the following considerations decidedly do not apply
to this project.

Consider the compatibility of the data you are integrating
  The output data principally consists of a x-y-scatter plot, explicitly
  designed to support compatible as well as incompatible data, so long as
  the data for each axis is sortable in some capacity.

Identify outliers
  For the considerations laid out in the content of this section so far,
  the means are missing to decide whether outliers are indication of error
  or normal.


.. raw:: pdf

   PageBreak



3. STORAGE AND BACKUP DURING THE RESEARCH PROCESS
=================================================

3a. How will data and metadata be stored and backed up during the research?
---------------------------------------------------------------------------

In general, handling of data and program source code is undertaken on
the `Pogner Family IT Infrastructure` (from now on called "pogitsys").

A full copy of the project git repository is hosted as git repository on
pogitsys as part of the 'active data' storage. This full copy includes at
least the non-public and public variant of the git repository.

Insofar as data and program source code is designated as public-access
according to the previous section of this document (that is, all parts
except ones marked as non-public), a mirror of the public project git
repository is hosted and published on github.com.

As the project does not making any arrangements regarding backup, etc.,
the default arrangements of pogitsys are in effect, as detailed in this
chapter.

It is the responsibility of each project team member, to perform `commit
and push` (one of the most basic `git` functions) in a timely fashion
after each project edit. Only when `commit and push` has been performed
by the respective project team member, the services offered by pogitsys
spring into action.

Pogitsys is a robust, highly automated it infrastructure providing a range of
services to authorized users, the Pogner family members.
Clear policies are defined by the sysadmin team under guideance of the chief
sysadmin, and carried out by the sysadmin of the day.
Policies exist for a wide range of subjects, such as which services to provide,
what responsibility is taken up by the it-infrastruce and what responsibility
is taken up by the user, and what level of various services are provided.

Implemented policies include automated regular on-site and off-site backup
as well as append-only archivation of the 'active data' storage.
Service level guarantees an absolute maximum of 24h delay (with an average
delay of 6h) between some data stored, changed or deleted on the 'active data'
storage and that store, change or delete being recorded in the 'archive data'
storage and propagated to both 'on-site backup data' and 'off-site backup data'
storages.


3b. How will data security and protection of sensitive data be taken care of during the research?
-------------------------------------------------------------------------------------------------

Who will be responsible for backup and recovery?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The individual project team members are responsible

a. to include all project source code, data and auxilliary files in the
   git repository.
b. to 'commit & push' in a timely fashion.

As long as the git repository itself remains intact, the project team is
responsible to manage any and all data stored within the git repository.
This includes reverting to a previous version, merging multiple conflicting
versions, or recovering a deleted or damaged file which is still stored in a
different or previous version.

The sysadmin team is responsible to continually improve policies,
to provide services as prescribed in said policies and to offer training
to all pogitsys users.

The sysadmin team is also responsible to implement the necessary automated
processes, such that any and all data from the 'active data' storage is
continually backupped to backup storage and archived to archive storage, with
the maximum delay times prescribed in the policies.

The sysadmin of the day is responsible to effect recovery procedures, either
sparked by a user request (e.g. inadvertant damaging the git repository) or
as response to an it-infrastructure incident.

How will the data be recovered in the event of an incident?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The steps taken to recover from an incident are highly individual
to each incident. Generally speaking the following phases occur.

First, the sysadmin of the day follows the procedures laid out by the sysadmin
team, to reinstate the services offered by the it-infrastructure. This includes
re-installing damaged services, ordering replacement hardware, or identifying
that external it-security experts are required to recover from a particular
incident and coordinating with such external consultants.

Then the sysadmin reverts to his/her normal role of assisting users, should
they request recovery of certain data data from the data-archive or
data-backup.

The project team is responsible to return the project git repository into
good order. But this is expected to only consist of verifying good order, or
requesting appropriate backup-recovery from the sysadmin.

And lastly, when the inevitable death of the master sysadmin (this author) has
eventuated, instructions are laid out in the will and testament,
protected by Shamir's Secret Sharing, how to securely transfer the chief
sysadmin role to any successor.

What are the risks to data security and how will these be managed?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The main risk is accidental data loss or data corruption by a user inadvertently
commanding his/her computer to perform some action.
This main risk is managed by maintaining the data-archive, which has does not
perform any real delete function during normal operation (instead data is merely
marked).

The second greatest risk posed by generic worms, viruses and other malware, is
mitigated by the data-archive and data-backup be performed on dedicated machines
with the minimal amount of software necessary to perform their function.
Access to these machines is only granted through a special procedure, as also
any sysadmin is subject to the abovementioned main risk.
Of the software available to conduct the functions of the data-backup and
data-archive, after carefully comparing the choices, the software with the
highest likelyhood of small attack surface, highest long-term stability and
long-term bugfix support is selected.

The third greatest risk are posed by attacks specifically undertaken to target
a specific person associated with the it-infrastructure or the
it-infrastructure itself.
This risk is accepted as not preventable with the available resources, and
worst-case outcome is possible in this case.

How will you control access to keep the data secure?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under normal operations, access to the non-public git repository is restricted
to users that are

a. registered with the it-infrastructure
b. registered with the project

The sysadmin of the day is responsible for granting or revoking access.

Project team is responsible of a timely report to the Sysadmin, if new project
team members join or project team members leave.

The public repository at github.com grants read access to all users and all
third parties. Write access is restricted to this author only.

How will you ensure that collaborators can access your data securely?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The git repository is accessibly only via the :literal:`git+ssh` method, and
as such is protected by the secure `ssh` protocol.

The git repository is hosted on a server with 24/7 planned uptime and proper
internet connection, so any collaborator can access the git repository at a
time of his/her choosing.


If creating or collecting data in the field how will you ensure its safe transfer into your main secured systems?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While this does not apply to this project, the theoretical answer is as follows.

Project team member personal computers can edit and commit all content stored
in the git repository at all times (such is the feature offered by `git`).
However, for pushing one's changed to the it-infrastructure, and thereby
(a) making the edits available to all other project team members, and
(b) ensuring the proper backup and archive of the new edit,
a stable internet connection is required.

Each project team member is responsible for arrange for an internet connection
and pushing edits, in due course. (cf. the push-at-end-of-day policy)


.. raw:: pdf

   PageBreak



4. LEGAL AND ETHICAL REQUIREMENTS, CODES OF CONDUCT
===================================================

4a. If personal data are processed, how will compliance with legislation on personal data and on security be ensured?
---------------------------------------------------------------------------------------------------------------------

All data sets are not in relation, and are not relateable through
auxilliary data sets, to individual persons or small groups of persons.
All datasets can be truely regarded as anonymous with respect to
personal data. Therefore, considerations for the GDPR and similar do
not apply.

The data sets do not contain sensitive data in the privacy/ethical
sense.


4b. How will other legal issues, such as intellectual property rights and ownership, be managed? What legislation is applicable? 
--------------------------------------------------------------------------------------------------------------------------------

What copyright is applicable? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In case of the SNA-AT data from Statistik Austria, legal permission for usage,
preservation and re-publishing (and further actions) was given through the
license statement afixed to the respective webpage from where the data was
downloaded.

There was no visible indication, that the webpage incorrectly displayed wrong
content, or that the webpage was not from Statistik Austria.
The url was verified to be a subpage of https://statistik.at/ or
https://www.statistik.at/.

In case of the UCDP/PRIO data from the UCDP, no license statement acompanied
the downloaded data. However, as access to the data was without any restrictions
whatsoever, the files where easily findable on the internet, and the actual
download sub webpage https://ucdp.uu.se/downloads/ was easily linked from the
main page https://ucdp.uu.se/, consent to download, use, and locally store
is implicitly given. Consent to re-publish the data is assumed to be not
granted, or that if the required consent for re-publishing is given is at least
unclear; therefore the downloaded data cannot be re-published without further
consultation.

There was no visible indication, that the webpage incorrectly displayed wrong
content, or that the webpage was not from the UCDP.
The url was verified to be a subpage of https://ucdp.uu.se.

In case of the project files wholly created by the project team,
copyright and all associated rights, initially jointly lies with the
project team members.

In case of the output data set, license situation is unclear, and this
project acts under the assumption that publishing any part of the output
data set is proscibed.

How copyright is managed?
^^^^^^^^^^^^^^^^^^^^^^^^^

The SNA-AT and SNA-AT-EXTRACTED data sets are re-published under the
conditions laid out by STATISTIK AUSTRIA; specifically the source data
as downloaded is re-published unchanged, and the derived intermediate
data set is published having the prescribed notes affixed.

The UCDP, UCDP-EXTRACTED and OUTPUT data sets are not published, but
only retained in non-public copied of the project git repository.

The scripts, program source codes, and auxilliary files are published
with a CC0 license statement affixed to them (file ``LICENSE`` in the
project root directory).

4c. What ethical issues and codes of conduct are there, and how will they be taken into account?
------------------------------------------------------------------------------------------------

All data sets are either concerned with economic figures in relation to
nation states, or are concerned with conflict intensity levels in
relation to nation states.

The only thinkable ethical issue applying would be whether such data or
the performed analysis is subject to national security considerations.

However, as the data sources STATISTIK AUSTRIA is a state-operated
agency itself, an the Uppsala University can be said to be in good
standing with it's home state, and no controversy exists regarding the
source, nature or content of the data sets, matters of national security
are concluded to not imaginable.


.. raw:: pdf

   PageBreak



5. DATA SHARING AND LONG-TERM PRESERVATION
==========================================

5a. How and when will data be shared? Are there possible restrictions to data sharing or embargo reasons?
---------------------------------------------------------------------------------------------------------

Discoverability
^^^^^^^^^^^^^^^

Any third-party "surfing" to the github copy of the project repositoy
will have immediately full read access to all public parts of the
project, including the immediate rendering of the file ``README.rst``
which includes at the beginning the first overview-summary of the
project and furthermore pointers to other parts of the project.

There are no special provisions to advertise the existence of this data
set. In general, at least one other person is `following me` on
github.com, any such person is expected to get notified by github.com on
uploading the public part of repository to github.com.

General findability through the de-facto exclusive search engine Google
is likely, but will probably be restricted to only the most specific
search queries.

This approach follows the intended exposure for this project.

Long-Term Preservation
^^^^^^^^^^^^^^^^^^^^^^

The public git repository hosted at github.com will be retained as long
as possible, subject to policy changed on the part of Microsoft Inc, the
entity effectively controlling the strategic planning of github.com.

The full project git repository will be preserved until a catastrophic
event destroys the pogitsys it-infrastructure (e.g. a sudden and
hyper-expansive raise in hardware prices or other a targetted
it-security attack).

Data publication timeline
^^^^^^^^^^^^^^^^^^^^^^^^^

The public project git repository is scheduled to be uploaded to
github.com at or shortly before Monday, 19th April 2021, 23:59 CEST.
From that time of upload onwards, any third-party "finding" the github
project page will have full read access.

The full project git repository hosted on the pogitsys infrastructure
was already continuous made available to all authorized users from the
outset of the project.

The private parts will not be published. However, a reader can perform
the easy to use general buildscript `build.sh` in order to acquire
his/her own copy of the UCDP source data set and derived intermediate
data set.

Reusability of the project parts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any third-party establishing read-access to the project repository,
based on the various license statements, will be able to resuse the
various project parts under their respective license:

* the sna-at parts under the terms as layed out by STATISTIK AUSTRIA
* all parts wholly created by the project team under the CC0 permissive
  license.

The parts 'tainted' with ucdp data will only be useable to a third-party
after executing the respective download script, or the general
buildscript `build.sh`.


5b. How will data for preservation be selected, and where data will be preserved long-term (for example a data repository or archive)?
--------------------------------------------------------------------------------------------------------------------------------------

For long-term preservation, the full project repository will be left
as-is on the pogitsys, which already provides backup and archive
services. This decision was made by the project team.

While this author expects this project to perform purely in raising
general interest in the insights offerd by the UDCP, it is nevertheless
the intended purpose. As such, the publication at github.com is more
important than the secluded archivation within the pogitsys
infrastructure.

Lacking access to relevant directories or index services, this project
will not be registered with any data repository registration services.
Specifically attaining access to relevant index services would exceed
time resources allocated to this project and therefore will not be
pursued.

The project will remain findable through google search engine and
github search.

Publication at github.com will not incur any costs so long as the
current strategic objectives of Microsoft Inc remain in place; an
eventuality that cannot be estimated by the project team and therefore
will be handled on an ad-hoc basis by this author.

Archivation on the pogitsys will incur unnoticable costs, due to the
cummulative data size of the project being several orders of magnitude
smaller than the regularily managed data sizes on pogitsys.
The costs will be burdened on the general it-budget of the Pogner Family.


5c. What methods or software tools are needed to access and use data?
---------------------------------------------------------------------

Access to the public project git repository is subject to the access
methods implemented and maintained by github.com. Currently the latest
version of one the big-two web browsers (Google Chrome, Mozilla Firefox
-- With each having many rebranded incarnations, for example the
Microsoft Edge web browser) is required.

After access to the data has been established, the software listed in
the ``README`` file (see there) under section `Build Dependencies`, or
compatible software, is required to make full use of the project.

It is expected that the `csv` data format, used for all final and
intermediate data produced by this project, will remain usable with a
most wide range of software tools for many years to come.


5d. How will the application of a unique and persistent identifier (such as a Digital Object Identifier (DOI)) to each data set be ensured?
-------------------------------------------------------------------------------------------------------------------------------------------

As per the recommended reading of the github guide on zenodo integration,
only *public github repositories* can be issued with a DOI through the
github/zenodo partnership.

Additionally, detailed inspection of of the DOI homepage https://doi.org
indicates that one of the 10 listed DOI Registration Agencies **MUST**
be used if a doi is sought to be issued for this project. However, each
of the 10 agencies requires some kind of institutional relationship this
author, acting under his own right without institutional endorsement,
lacks.

As a result, only the following DOIs can be acquired as persistent
identifiers.

* a DOI for the the main github repository will be acquired through the
  github/zenodo partnership.

  Acquired DOI: https://doi.org/10.5281/zenodo.4699809

* for the `sna-at-data` and `sna-at-data-extracted` data sets, a
  snapshot will be each uploaded separately to zenodo to, and a separate
  DOI acquired for these snapshots.

  A variant with git submodules replacing the directories was
  considered, but discarded due to that feature's major compatibiltiy
  problems, including an implicit vendor lockin (the absolute inability
  to move the git repositories to a different hosting in the future).

  * `sna-at` data set: https://doi.org/10.5281/zenodo.4699804
  * `sna-at-extracted` data set: https://doi.org/10.5281/zenodo.4699806

* the `ucdp` and `ucdp-extracted` data sets will **not** receive DOIs,
  as publishing them to github as public repository is not possible,
  and therefore the github/zenodo partnership will not issue a DOI.


.. raw:: pdf

   PageBreak



6. DATA MANAGEMENT RESPONSIBILITIES AND RESOURCES
=================================================

6a. Who (for example role, position, and institution) will be responsible for data management (i.e. the data steward)?
----------------------------------------------------------------------------------------------------------------------

Due to the limited size of this project, a single person is charged with
handling all current and future responsibilities, including those
regarding data management and data stewardship, and including updating
all project content such as scripts, source code, auxilliary files,
data, and meta-data.

::

  Max-Julian Pogner
  max-julian@pogner.at
  https://orcid.org/0000-0001-6244-0173

6b. What resources (for example financial and time) will be dedicated to data management and ensuring that data will be FAIR (Findable, Accessible, Interoperable, Re-usable)?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Considering the relative abundance of personal projects and overlong
list of prospecting projects of this author, no resources, neither
financial nor time, will be alotted to the continued availabilty of the
public project git repository at github.com. Consequently, any external
incident at github.com might take the published project offline, without
being noticed.

However, due to the nature and inner workings of github.com, it is
expected that the project will be available at github.com for many years
to come without any efforts expended on part of this project's data
steward.

If a future project should make re-use of (parts of) this project, or
change parts of this project, such re-use or change will be treated as a
complete new project and resource planning will restart from scratch. No
resources need to be earmarked for this eventuality with respect to this
project's resource planning.

Long-term personal archive will be ensured through general service level
provided by pogitsys. If the data steward should become aware, despite
expending zero resources into relevant monitoring activities, that the
data from github.com became unpublished, it would be very little effort
to re-publish the project.
