#!/usr/bin/python3
# This file is a part of XSiteGen project.
# See LICENSE for copyright and licensing details.

import datetime

directories = {}
template_files = {}
file_encoding = 'UTF-8'
source_file_extension = 'md'
use_tab_indent = False
indent_size = 8
overwrite_pages = False
copy_files = True
overwrite_files = False
file_copy_blacklist = []
datetime_zone = datetime.timezone.utc
datetime_format = '%Y-%m-%d %H:%M:%S UTC'
global_variables = {}
directory_variables = {}
markdown_extensions = [ 'md_in_html', 'nl2br' ]