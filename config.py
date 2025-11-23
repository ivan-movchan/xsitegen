#!/usr/bin/python3
# This file is a part of XSiteGen project.
# See LICENSE for copyright and licensing details.

import datetime

# Source and target directories.
directories = {
    './demo/src/files': './demo/build'
}

# Template files.
template_files = {
    './demo/src/files': './demo/src/templates/template.html'
}

# File encoding (should be specified to avoid file read/write errors).
file_encoding = 'UTF-8'

# Source file extension.
source_file_extension = 'md'

# Use tab indent? (False = use spaces.)
use_tab_indent = False

# Indent size.
indent_size = 8

# Overwrite existing pages?
overwrite_pages = False

# Copy files placed in source directories?
copy_files = True

# Overwrite files?
overwrite_files = False

# Files that should not be copied (copy_files must be active).
file_copy_blacklist = [ ]

# Date/time zone.
# datetime.timezone.utc = UTC, None = your local time zone.
# See https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone for details.
datetime_zone = datetime.timezone.utc

# Date/time string format.
# Default value is '%Y-%m-%d %H:%M:%S UTC'.
# See https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes for details.
datetime_format = '%Y-%m-%d %H:%M:%S UTC'

# Global variables, applied to every source file.
global_variables = {
    'menu': 'Home &bull; <a href="me/index.html">About me</a>',
    'name': '{author}\'s Blog',
    'copyright': 'Copyright &copy; 2025 {author}.',
    'author': 'John Doe',
    'powered_by': '<a href="https://github.com/ivan-movchan/xsitegen" target="_blank">Powered by XSiteGen</a>'
}

# Directory variables, applied to every source file in specified directories.
directory_variables = {
    './demo/src/files/blog': {
        'menu': '<a href="../index.html">Home</a> &bull; <a href="../me/index.html">About me</a>'
    },
    './demo/src/files/me': {
        'menu': '<a href="../index.html">Home</a> &bull; About me'
    }
}

# Python-Markdown extensions.
# Default value is [ 'md_in_html', 'nl2br' ].
# See https://python-markdown.github.io/extensions/ for details.
markdown_extensions = [ 'md_in_html', 'nl2br' ]