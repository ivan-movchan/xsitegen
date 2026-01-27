#!/usr/bin/python3
# This file is a part of XSiteGen project.
# See LICENSE for copyright and licensing details.

import datetime
from xsitegen.utils import *
from xsitegen.default_settings import *

verbose = is_verbose()

try:
    from markdown import markdown, __version_info__
    
    if verbose:
        print(f'Powered by Python-Markdown {'.'.join(map(str, __version_info__))}.')
except:
    print('Failed to import Python-Markdown. Markdown support is not available.')

try:
    if not os.getcwd() in sys.path:
        sys.path.insert(0, os.getcwd())
    
    import config
    from config import *
    
    if verbose:
        print(f'Using configuration module "{config.__file__}".')
except Exception as e:
    die(f'An error occurred while loading the configuration module:\n{e}', 1)

PAGE_VARIABLE_BLOCK_BEGIN = PAGE_VARIABLE_BLOCK_END = '---'

def get_page_variables(text):
    lines = text.splitlines()
    variables = {}
    
    variable_block_finished = False
    
    if len(lines) > 1:
        if lines[0] == PAGE_VARIABLE_BLOCK_BEGIN:
            for line in lines[1:]:
                if line == PAGE_VARIABLE_BLOCK_END:
                    variable_block_finished = True
                    break
                
                delimeter_index = line.find(':')
                variable_name = line
                variable_value = ''
                
                if delimeter_index != -1:
                    variable_name = line[:delimeter_index]
                    
                    if delimeter_index != (len(line) - 1):
                        variable_value = line[(delimeter_index + 1):].strip(' ')
                
                variables[variable_name] = variable_value
    
    return variables if variable_block_finished else None

def get_directory_variables(file_name):
    slash_index = -1
    variables = {}
    
    while True:
        slash_index = file_name.find('/', (slash_index + 1))
        
        if slash_index == -1:
            break
        
        directory = file_name[:slash_index]
        
        if directory in directory_variables:
            variables = {**variables, **directory_variables[directory]}
    
    return variables

def replace_variables(text, variables):
    result = text
    
    for variable in variables:
        result = result.replace(f'{{{variable}}}', variables[variable])
    
    return result

def generate_page(source_file_name, template_text, target_file_name):
    source_text = read_file(source_file_name, file_encoding)
    
    variables = { }
    page_variables = get_page_variables(source_text)
    my_directory_variables = get_directory_variables(source_file_name)
    
    if page_variables == None:
        return False
    else:
        if len(variable_priority_list) > 0:
            for item in variable_priority_list:
                if item == 'page':
                    variables = { **variables, **page_variables }
                elif item == 'directory':
                    variables = { **variables, **my_directory_variables }
                elif item == 'global':
                    variables = { **variables, **global_variables }
        else:
            variables = { **page_variables, **my_directory_variables, **global_variables }
    
    page_content_raw = '\n'.join(source_text.splitlines()[(len(page_variables) + 2):])
    
    try:
        page_content_raw = markdown(page_content_raw, output_format='html', extensions=markdown_extensions)
    except:
        pass
    
    page_content = ''
    
    for line in page_content_raw.splitlines():
        page_content += (('\t' * indent_size) if use_tab_indent else (' ' * indent_size)) + line
    
    page_text = template_text.replace('{content}', page_content)
    
    page_datetime = datetime.datetime.now().astimezone(datetime_zone).strftime(datetime_format)
    page_text = page_text.replace('{datetime}', page_datetime)
    
    page_text = replace_variables(page_text, variables)
    
    return write_file(target_file_name, page_text, file_encoding)

def main():
    if verbose:
        start_time = datetime.datetime.now()
    
    for source_directory in directories:
        if not os.path.exists(source_directory):
            print(f'"{source_directory}" directory does not exist. Ignoring.')
            continue
        
        if not os.path.isdir(source_directory):
            print(f'"{source_directory}" is not a directory. Ignoring.')
            continue
        
        if verbose:
            print(f'Working with directory "{source_directory}".')
        
        template_file_name = template_files[source_directory]
        template_text = read_file(template_file_name, file_encoding)
        
        if template_text == None:
            print(f'Failed to open and read template file "{template_file_name}". Ignoring.')
            continue
        
        if not '{content}' in template_text:
            print(f'Template file "{template_file_name}" does not contain', '{content}', 'variable mention. Ignoring.')
            continue
        
        target_directory = directories[source_directory]
        source_files = scan_directory(source_directory)
        
        if verbose:
            print(f'Target directory is "{target_directory}".')
            print(f'{len(source_files)} file(s) detected.')
        
        for source_file in source_files:
            source_file_name = f'{source_directory}/{source_file}'.replace('/./', '/')
            target_file_name = f'{target_directory}/{source_file}'.replace('/./', '/')
            
            is_page = source_file.endswith(f'.{source_file_extension}')
            target_file_name = target_file_name.replace(f'.{source_file_extension}', '.html') if is_page else target_file_name
            file_exists = os.path.isfile(target_file_name)
            writing = True
            
            if is_page:
                writing = (not file_exists) or (overwrite_pages)
            else:
                writing = (copy_files) and ((not source_file_name in file_copy_blacklist) and (file_exists and overwrite_files))
            
            if not writing:
                if verbose:
                    print(f'Not writing file "{target_file_name}".')
                continue
            
            if is_page or (not is_page and copy_files):
                if not prepare_directories(target_file_name):
                    print(f'Failed to prepare directories for the file "{target_file_name}".')
                    continue
            
            is_written = generate_page(source_file_name, template_text, target_file_name) if is_page else copy_file(source_file_name, target_file_name)
            
            if is_written:
                if verbose:
                    print(f'Written file "{target_file_name}".')
            else:
                print(f'Failed to write file "{target_file_name}".')
    
    if verbose:
        end_time = datetime.datetime.now()
        work_time = (end_time - start_time)
        print(f'Finished in {work_time}.')