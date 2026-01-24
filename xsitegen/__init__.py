#!/usr/bin/python3
# This file is a part of XSiteGen project.
# See LICENSE for copyright and licensing details.

VERSION = '1.4-develop'
PYTHON_VERSION_MINOR_REQUIRED = 9

from xsitegen.utils import die

if __name__ != 'xsitegen':
    die('This module was incorrectly imported. Terminating.', 42)

import os
import sys

def version():
    die(f'XSiteGen {VERSION}\nCopyright (с) 2025 Ivan Movchan\nhttps://github.com/ivan-movchan/xsitegen')

def usage():
    die(f'Usage: xsitegen [-hv]')

def check_arguments():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg == '-v':
                version()
            elif arg == '-h':
                usage()
            else:
                print(f'Unknown argument: {arg}.')
                usage()

def check_python_version():
    if sys.version_info.minor < PYTHON_VERSION_MINOR_REQUIRED:
        die(f'Python 3.{PYTHON_VERSION_MINOR_REQUIRED} or newer is required.', 3)
    else:
        print(f'Powered by Python {'.'.join(map(str, sys.version_info))}.')

check_arguments()
check_python_version()