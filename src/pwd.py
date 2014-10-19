#!/usr/bin/env python

import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--version", action="store_true", dest="version", help="output version information and exit")
parser.add_option("-L", "--logical", action="store_true", dest="logical", help="use PWD from environment, even if it contains symlinks")
parser.add_option("-P", "--physical", action="store_true", dest="physical", help="avoid all symlinks")

(options, args) = parser.parse_args()

if options.version:
    print('pwd (pycoreutils) 0.1')
elif options.logical:
    print(os.getenv('PWD'))
elif options.physical:
    print(os.path.realpath(os.getcwd()))
else:
    print(os.getcwd())
