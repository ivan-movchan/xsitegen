<div align="center">

<img src="../images/logo.png" style="width: 128px;">

# XSiteGen: changelog
#### *English &bull; [Русский](CHANGELOG-RU.md)*

</div>

### XSiteGen 2.0 — 2026-02-01

- **Added:**   directory and page variables.
- **Added:**   variable priority list.
- **Added:**   copying files from source directories.
- **Added:**   Python-Markdown extensions support.
- **Added:**   text indent (applied to pages source text only).
- **Added:**   checking Python version at startup.
- **Added:**   printing Python and Python-Markdown versions at startup.
- **Added:**   printing working time on finishing.
- **Added:**   `-v` verbose flag.
- **Updated:** Python 3.10 or newer is now required for running XSiteGen. Python 3.9 support has been dropped by Python-Markdown library.
- **Updated:** old `-v` version flag is replaced with `-V`.
- **Updated:** documentation, now in `docs` directory.
- **Updated:** logo.
- **Updated:** log messages.
- **Updated:** configuration module import error handling.
  
  If the module has an error, a short message describing occurred error will be shown.
  If the module was not found, the user will be suggested to create a new configuration module or switch the directory and run XSiteGen in it.

- **Fixed:**   generating pages from templates not containing `{content}`.
- **Removed:** useless markers at the beginning of text messages.
- **Removed:** "specific" variables.
- **Removed:** the need of placing all supported (even unused) settings to the configuration module.

### XSiteGen 1.3 — 2025-08-03

- **Added:**   specific variables that can be applied for different source files or directories.
- **Added:**   showing configuration module file path if imported successfully.
- **Updated:** project name.
- **Updated:** logo.

### TinySSG 1.2 — 2025-07-15

This release brings some new features for more comfortable TinySSG usage.

- **Added:**   loading the configuration module (`config.py`) from any directory TinySSG has been executed in.
- **Added:**   recursive source directories scanning.
  
  The user is no longer needed to specify every subdirectory in the configuration module, only the root directory.
  
- **Added:**   showing the count of source files in every source directory.
- **Updated:** logo.
- **Removed:** checking if a source file has 3 and more lines of text (i. e. heading and at least one paragraph of text).
- **Removed:** a few useless exception handlers and checks.

## TinySSG 1.1 — 2025-07-10

- **Added:**   markers for improving the output of the script and categorizing messages (information, warning, error).
- **Updated:** logo.
- **Updated:** documentation.

## TinySSG 1.01 — 2025-06-23

- **Fixed:** file read error that could occur when opening a template file without specifying file encoding.

## TinySSG 1.0 — 2025-06-17

The first public release of XSiteGen, then called "TinySSG".