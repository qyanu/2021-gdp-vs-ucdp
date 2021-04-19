#!/usr/bin/env python3

"""
this script reads the data-management-plan.yaml source file (in yaml format)
and outputs it as json format.

input file: code/data-management-plan.yaml
output file: data-management-plan.json

"""

import json
import os.path
import sys

from ruamel.yaml import YAML

SRCDIR = os.path.join(os.path.dirname(__file__))
DSTDIR = os.path.join(os.path.dirname(__file__), "..")

SRCFILE = os.path.join(SRCDIR, "data-management-plan.yaml")
DSTFILE = os.path.join(DSTDIR, "data-management-plan.json")

yaml = YAML()

data = None
with open(SRCFILE, mode='r', encoding='utf-8') as fpin:
    data = yaml.load(fpin)

with open(DSTFILE, mode='w', encoding='utf-8') as fpout:
    json.dump(data, fpout, indent=2)

sys.stdout.write(f"{sys.argv[0]} finished.\n")
