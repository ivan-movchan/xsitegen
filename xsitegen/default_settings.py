#!/usr/bin/python3
# This file is a part of XSiteGen project.
# See LICENSE for copyright and licensing details.

import datetime

# Source and target directories.
# Required to be filled.
# 
# Example:
# 
# directories = {
#     'source1': 'target1',
#     'source2': 'target2'...
# }

directories = { }

# Template files used for page generating.
# Required to be filled, should contain paths of source directories.
# 
# Example:
# 
# template_files = {
#     'source1': 'template1',
#     'source2': 'template2'...
# }

template_files = { }

# The file encoding, used for file read/write operations.
# Default value is 'UTF-8'.

file_encoding = 'UTF-8'

# The file extension for source files which are used for page generating.
# Default value is 'md' (Markdown formatted text file).

source_file_extension = 'md'

# The flag defining if XSiteGen should use tabs (\t) for making indent in HTML-formatted source file text.
# 
# - True = yes, use tabs.
# - False = no, use spaces.
# 
# Default value is False.

use_tab_indent = False

# The size of text indent. Should be integer.
# Default value is 8.

indent_size = 8

# The flag defining if XSiteGen should overwrite already existing HTML pages (probably generated earlier).
# 
# - True = yes.
# - False = no.
# 
# Default value is False.

overwrite_pages = False

# The flag defining if XSiteGen should copy extra files located in source directories (like media files, archives, etc.).
# 
# - True = yes.
# - False = no.
# 
# Default value is True.

copy_files = True

# The flag defining if XSiteGen should overwrite already existing files (probably copied earlier).
# 
# - True = yes.
# - False = no.
# 
# Default value is False.

overwrite_files = False

# The list of extra files that should not be copied. Empty by default.
# 
# Example:
# 
# file_copy_blacklist = [ 'src/files/secret.txt' ]

file_copy_blacklist = [ ]

# Time zone, defined as datetime.timezone object. If set to None, your local time zone will be used.
# Used for date/time stamp that can be inserted by mentioning {datetime} variable.
# 
# Default value is datetime.timezone.utc (UTC).
# 
# Do not forget to import the datetime module by adding "import datetime" line at the beginning of your configuration module!

datetime_zone = datetime.timezone.utc

# A string defining date/time stamp format.
# Default value is '%Y-%m-%d %H:%M:%S UTC'.

datetime_format = '%Y-%m-%d %H:%M:%S UTC'

# A dictionary of global variables applied to every source file. Empty by default.
# 
# Example:
# 
# global_variables = {
#     'foo': '42'
# }

global_variables = { }

# A dictionary of directory variables applied to every source file in specified directories. Empty by default.
# 
# Example:
# 
# directory_variables = {
#     'some_special_directory': {
#         'foo': '42'
#     }
# }

directory_variables = { }

# A variable priority list. The latest item has the highest priority.
# Must be filled by these 3 values: 'global', 'directory', 'page'.
# 
# Default value is [ 'global', 'directory', 'page' ].

variable_priority_list = [ 'global', 'directory', 'page' ]

# A list of Python-Markdown extensions.
# 
# Default value is [ 'md_in_html', 'nl2br' ].

markdown_extensions = [ 'md_in_html', 'nl2br' ]