#!/usr/bin/python3
# This file is a part of XSiteGen project.
# See LICENSE for copyright and licensing details.

VERSION = '1.4-develop'

import os, sys, datetime, shutil

def die(message, code=0):
    print(message)
    exit(code)

def read_file(file_name, encoding='UTF-8'):
    content = None
    
    try:
        file = open(file_name, 'r', encoding=encoding)
        content = file.read()
        file.close()
    except:
        pass
    
    return content

def write_file(file_name, content, encoding='UTF-8'):
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

def generate_page(source_file_name, template_text, target_file_name):
    source_file_lines = read_file(source_file_name, file_encoding).splitlines()
    page_content_start = -1
    page_variables = {}
    
    if source_file_lines[0] == '---':
        page_content_start = 1
        
        while source_file_lines[page_content_start] != '---':
            if page_content_start == len(source_file_lines):
                print('The end of page variable block was not found.')
                return False
            
            current_line = source_file_lines[page_content_start]
            delimeter_index = current_line.find(':')
            page_variable_name = current_line
            page_variable_value = ''
            
            if delimeter_index != -1:
                page_variable_name = current_line[:delimeter_index]
                
                if delimeter_index != (len(current_line) - 1):
                    page_variable_value = current_line[delimeter_index+1:]
                    
                    while page_variable_value[0] == ' ':
                        page_variable_value = page_variable_value[1:]
            
            page_variables[page_variable_name] = page_variable_value
            page_content_start += 1
    
    page_content = '\n'.join(source_file_lines[page_content_start+1:])
    
    try:
        page_content = markdown(page_content, output_format='html', extensions=markdown_extensions)
    except:
        pass
    
    page_content_lines = page_content.splitlines()
    
    for i in range(len(page_content_lines)):
        new_line = (('\t' * indent_size) if use_tab_indent else (' ' * indent_size)) + page_content_lines[i]
        page_content_lines[i] = new_line
    
    page_content = '\n'.join(page_content_lines)
    
    page_datetime = datetime.datetime.now().astimezone(datetime_zone).strftime(datetime_format)
    
    page_text = template_text.replace('{content}', page_content)
    page_text = page_text.replace('{datetime}', page_datetime)
    
    for variable in page_variables:
        page_text = page_text.replace(('{' + variable + '}'), page_variables[variable])
    
    slash_index = -1
    while True:
        slash_index = source_file_name.find('/', slash_index+1)
        if slash_index == -1:
            break
        
        directory = source_file_name[:slash_index]
        if directory in directory_variables:
            for variable in directory_variables[directory]:
                page_text = page_text.replace(('{' + variable + '}'), directory_variables[directory][variable])
    
    for variable in global_variables:
        page_text = page_text.replace(('{' + variable + '}'), global_variables[variable])
    
    return write_file(target_file_name, page_text, file_encoding)

def main():
    start_time = datetime.datetime.now()
    
    for source_directory in directories:
        print(f'Working with directory "{source_directory}".')
        
        if not os.path.exists(source_directory):
            print('The directory does not exist. Ignoring.')
            continue
        
        if not os.path.isdir(source_directory):
            print('This is not a directory. Ignoring.')
            continue
        
        template_file_name = template_files[source_directory]
        template_text = read_file(template_file_name, file_encoding)
        
        if template_text == None:
            print(f'Failed to open and read template file "{template_file_name}". Ignoring.')
            continue
        
        target_directory = directories[source_directory]
        print(f'Target directory is "{target_directory}".')
        
        source_files = scan_directory(source_directory)
        print(f'{len(source_files)} file(s) detected.')
        
        for source_file in source_files:
            source_file_name = f'{source_directory}/{source_file}'.replace('/./', '/')
            target_file_name = f'{target_directory}/{source_file}'.replace('/./', '/')
            
            if source_file.endswith(f'.{source_file_extension}'):
                target_file_name = target_file_name.replace(f'.{source_file_extension}', '.html')
                
                if os.path.isfile(target_file_name) and not overwrite_pages:
                    print(f'Ignoring file "{target_file_name}".')
                    continue
                
                if not prepare_directories(target_file_name):
                    print(f'Failed to prepare directories for the file "{target_file_name}".')
                    continue
                
                if generate_page(source_file_name, template_text, target_file_name):
                    print(f'Written file "{target_file_name}".')
                else:
                    print(f'Failed to write file "{target_file_name}".')
            else:
                if copy_files:
                    if (source_file_name in file_copy_blacklist) or (os.path.isfile(target_file_name) and not overwrite_files):
                        print(f'Ignoring file "{target_file_name}".')
                        continue
                    
                    if not prepare_directories(target_file_name):
                        print(f'Failed to prepare directories for file "{target_file_name}".')
                        continue
                
                    if copy_file(source_file_name, target_file_name):
                        print(f'Written file "{target_file_name}".')
                    else:
                        print(f'Failed to write file "{target_file_name}".')
    
    end_time = datetime.datetime.now()
    work_time = (end_time - start_time)
    
    print(f'Finished in {work_time}.')
    
def pre_main():
    if '-v' in sys.argv or '--version' in sys.argv:
        die(f'XSiteGen {VERSION}\nCopyright (с) 2025 Ivan Movchan\nhttps://github.com/ivan-movchan/xsitegen')

if __name__ == '__main__':
    pre_main()
else:
    die('This module should not be imported.', 42)

try:
    if not os.getcwd() in sys.path:
        sys.path.insert(0, os.getcwd())
    
    import config
    from config import *
    
    print(f'Using configuration module "{config.__file__}".')
except Exception as e:
    if e == ModuleNotFoundError:
        die('The configuration module ("config.py") was not found.\nPlease create it from the template, or run XSiteGen in another directory\nwhere the module exists.', 1)
    else:
        die(f'The configuration module ("config.py") has an error:\n{e}', 1)

try:
    from markdown import markdown, __version_info__
    print(f'Powered by Python-Markdown {'.'.join(map(str, __version_info__))}.')
except:
    print('Failed to import Python-Markdown. Markdown support is not available.')

if __name__ == '__main__':
    main()