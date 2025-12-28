directories = { './src/files': './build' }
template_files = { './src/files': './src/templates/template.html' }

global_variables = {
    'menu': 'Home &bull; <a href="me/index.html">About me</a>',
    'name': '{author}\'s Blog',
    'copyright': 'Copyright &copy; 2025-2026 {author}.',
    'author': 'John Doe',
    'powered_by': '<a href="https://github.com/ivan-movchan/xsitegen" target="_blank">Powered by XSiteGen</a>'
}

directory_variables = {
    './demo/src/files/blog': {
        'menu': '<a href="../index.html">Home</a> &bull; <a href="../me/index.html">About me</a>'
    },
    './demo/src/files/me': {
        'menu': '<a href="../index.html">Home</a> &bull; About me'
    }
}