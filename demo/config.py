directories = { 'src/files': './build' }
template_files = { 'src/files': 'src/templates/template.html' }

global_variables = {
    'menu': 'Home &bull; <a href="me/index.html">About me</a>',
    'name': '{author}\'s Blog',
    'copyright': 'Copyright &copy; 2025-2026 {author}.',
    'author': 'John Doe',
    'stylesheet': 'assets/css/style.css'
}

directory_variables = {
    'src/files/blog': {
        'menu': '<a href="../index.html">Home</a> &bull; <a href="../me/index.html">About me</a>',
        'stylesheet': '../assets/css/style.css'
    },
    'src/files/me': {
        'menu': '<a href="../index.html">Home</a> &bull; About me',
        'stylesheet': '../assets/css/style.css'
    }
}

variable_priority_list = [ 'page', 'global', 'directory' ]

indent_size = 8

overwrite_pages = overwrite_files = True