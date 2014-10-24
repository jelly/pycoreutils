#!/usr/bin/env python

import os
import platform
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--version", action="store_true", dest="version", help="output version information and exit")
parser.add_option("-a", "--all", action="store_true", dest="all", help="print all information, in the following order, except omit -p and -i if unknown:")
parser.add_option("-s", "--kernel-name", action="store_true", dest="kernelname", help="print the kernel name")
parser.add_option("-n", "--node-name", action="store_true", dest="nodename", help="print the netework node hostname")
parser.add_option("-r", "--kernel-release", action="store_true", dest="kernelrelease", help="print the kernel release")
parser.add_option("-v", "--kernel-version", action="store_true", dest="kernelversion", help="print the kernel version")
parser.add_option("-m", "--machine", action="store_true", dest="machine", help="print the machine hardware name")
parser.add_option("-p", "--processor", action="store_true", dest="processor", help="print the processor type or \"unknown\"")
parser.add_option("-i", "--hardware-platform", action="store_true", dest="hardwareplatform", help="print the hardware platform or \"unknown\"")
parser.add_option("-o", "--operating-system", action="store_true", dest="os", help="print the operating system")

(options, args) = parser.parse_args()

uname = os.uname()
if options.version:
    print('uname (pycoreutils) 0.1')
elif options.all:
    print('%s %s %s %s %s' % (uname.sysname, uname.nodename, uname.release, uname.version, uname.machine))
elif options.kernelname:
    print(uname.sysname)
elif options.nodename:
    print(uname.nodename)
elif options.kernelrelease:
    print(uname.release)
elif options.kernelversion:
    print(uname.version)
elif options.machine:
    print(uname.machine)
elif options.processor:
    platform.processor()
elif options.hardwareplatform:
    print(' '.join(platform.architecture()))
elif options.os:
    print(platform.system())
