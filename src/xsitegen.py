#!/usr/bin/python3

VERSION = '1.2'
INFO_MARKER, WARNING_MARKER, ERROR_MARKER = '(i)', '(!)', '(x)'

import os, sys, datetime

def die(prefix, message, code=0):
    print(prefix, message, sep=('' if prefix == '' else ' '))
    exit(code)

if __name__ != '__main__':
    die(WARNING_MARKER, 'This module should not be imported.')

if '-v' in sys.argv or '--version' in sys.argv:
    die('', f'XSiteGen {VERSION}\nCopyright (с) 2025 Ivan Movchan\nhttps://github.com/ivan-movchan/xsitegen')

try:
    import markdown
except:
    print(WARNING_MARKER, 'Failed to import "markdown" module. Markdown support is not available.')

try:
    if not os.getcwd() in sys.path:
        sys.path.insert(0, os.getcwd())
    import config
    from config import *
    print(INFO_MARKER, f'Loaded configuration module from "{config.__file__}".')
except:
    die(ERROR_MARKER, 'Failed to import the configuration module ("config.py"). Please run the module manually to check it for errors, or create it from the template if it does not exist.', 1)

for source_dir in directories:
    if not os.path.isdir(source_dir):
        die(ERROR_MARKER, f'"{source_dir}" does not exist or is not a directory.', 2)
    
    try:
        template_file = open(template_files[source_dir], 'r', encoding=file_encoding)
        template_text = template_file.read()
        template_file.close()
    except:
        die(ERROR_MARKER, f'Failed to read "{template_files[source_dir]}" file.', 2)
    
    source_files = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(f'.{source_file_extension}'):
                new_file = root.replace(source_dir, '.').replace('\\', '/') + '/' + file.replace('\\', '/')
                source_files.append(new_file)
    
    print(INFO_MARKER, f'"{source_dir}" has {len(source_files)} source file(s).')
    
    target_dir = directories[source_dir]
    
    for file in source_files:
        source_file_name = f'{source_dir}/{file}'.replace('/./', '/')
        target_file_name = f'{target_dir}/{file}'.replace('/./', '/').replace(f'.{source_file_extension}', '.html')
        
        if os.path.isfile(target_file_name) and not overwrite_webpages:
            print(WARNING_MARKER, f'"{target_file_name}" already exists and will not be overwritten.')
            continue
        
        target_dirs = target_file_name[:target_file_name.rfind('/')]
        try:
            os.makedirs(target_dirs, exist_ok=True)
        except:
            die(ERROR_MARKER, f'Failed to create target directories ("{target_dirs}").', 2)
        
        print(INFO_MARKER, f'Generating "{target_file_name}" page.')
        
        source_file = open(source_file_name, 'r', encoding=file_encoding)
        source_file_content = source_file.read().split('\n')
        source_file.close()
        
        page_content = '\n'.join(source_file_content[2:])
        try:
            page_content = markdown.markdown(page_content, output_format='html')
        except:
            page_content = page_content
        
        page_datetime = datetime.datetime.now().astimezone(datetime_zone).strftime(datetime_format)
        
        page_text = template_text.replace('{content}', page_content).replace('{title}', source_file_content[0]).replace('{datetime}', page_datetime)
        
        file_dir = file[2:file.rfind('/')] + '/'
        if file_dir in spec_variables:
            for var in spec_variables[file_dir]:
                page_text = page_text.replace(('{' + var + '}'), spec_variables[file_dir][var])
        
        if file in spec_variables:
            for var in spec_variables[file]:
                page_text = page_text.replace(('{' + var + '}'), spec_variables[file][var])
        
        for var in text_variables:
            page_text = page_text.replace(('{' + var + '}'), text_variables[var])
        
        try:
            target_file = open(target_file_name, 'w', encoding=file_encoding)
            target_file.write(page_text)
            target_file.close()
        except:
            print(ERROR_MARKER, f'Failed to write "{target_file_name}" file.')