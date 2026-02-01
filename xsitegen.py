#!/usr/bin/python3
# This file is a part of XSiteGen project.
# See LICENSE for copyright and licensing details.

VERSION = '2.0-develop'
PYTHON_VERSION_MINOR_REQUIRED = 10

import os
import sys

from xsitegen.utils import is_verbose, die

def version():
    die(f'''XSiteGen {VERSION}
Copyright (с) 2025-2026 Ivan Movchan
https://github.com/ivan-movchan/xsitegen

This is free software released under the terms of the MIT license.
See the LICENSE file for further details.''')

def usage():
    die('''Usage: xsitegen [-hvV]

Commands:
-h:    Show this help message
-V:    Show program version and exit

Options:
-v:    Verbose mode

See the documentation for further details.''')

def check_arguments():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg == '-h':
                usage()
            elif arg == '-v':
                print(f'This is XSiteGen {VERSION}, running in verbose mode.')
            elif arg == '-V':
                version()
            else:
                print(f'Unknown argument: {arg}.')
                usage()

def check_python_version():
    if sys.version_info.minor < PYTHON_VERSION_MINOR_REQUIRED:
        die(f'Python 3.{PYTHON_VERSION_MINOR_REQUIRED} or newer is required.', 3)
    else:
        if is_verbose():
            print(f'Powered by Python {'.'.join(map(str, sys.version_info))}.')

if __name__ != '__main__':
    die('This module was incorrectly imported. Terminating.', 42)

check_arguments()
check_python_version()

from xsitegen.core import main

main()