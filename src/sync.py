#!/usr/bin/env python

import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--version", action="store_true", dest="version", help="output version information and exit")

(options, args) = parser.parse_args()

if options.version:
    print('sync (pycoreutils) 0.1')
else:
    os.sync()
