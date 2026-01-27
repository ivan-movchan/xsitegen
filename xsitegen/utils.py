#!/usr/bin/python3
# This file is a part of XSiteGen project.
# See LICENSE for copyright and licensing details.

import os
import sys
import shutil

DEFAULT_ENCODING = 'UTF-8'

def die(message, code=0):
    print(message)
    sys.exit(code)

def read_file(file_name, encoding=DEFAULT_ENCODING):
    content = None
    
    try:
        file = open(file_name, 'r', encoding=encoding)
        content = file.read()
        file.close()
    except:
        pass
    
    return content

def write_file(file_name, content, encoding=DEFAULT_ENCODING):
    try:
        file = open(file_name, 'w', encoding=encoding)
        file.write(content)
        file.close()
        
        return True
    except:
        return False

def prepare_directories(file_name):
    try:
        os.makedirs(file_name[:file_name.rfind('/')], exist_ok=True)
        return True
    except:
        return False

def scan_directory(directory):
    content = []
    
    for root, directories, files in os.walk(directory):
        for file in files:
            item = root.replace(directory, '.') + '/' + file
            content.append(item.replace('\\', '/'))
    
    return content

def copy_file(source_file_name, target_file_name):
    try:
        shutil.copy2(source_file_name, target_file_name)
        return True
    except:
        return False

def is_verbose():
    return ('-v' in sys.argv)