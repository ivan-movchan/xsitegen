# XSiteGen changelog

#### [English](CHANGELOG.md) &bull; [Русский](CHANGELOG-RU.md)

### 1.3 *(2025-08-03)*

- New project name: XSiteGen.
- Implemented specific variables that can be applied for different source files (or directories).
- Implemented showing configuration module file path (if imported successfully).

### 1.2 *(2025-07-15)*

This release brings some new features for more comfortable XSiteGen usage.

- Another project logo update.
- Implemented loading the configuration module (`config.py`) from the working directory XSiteGen has been executed in (i. e. if running in the command shell).
- Implemented recursive scanning of source directories. The user is no longer needed to specify every subdirectory in the configuration module, only the root directory.
- XSiteGen now displays the count of source files in every source directory.
- Removed useless checking if a source file has 3 and more lines of text.
- Removed a few useless exception handlers and checks.
- Other minor fixes and improvements.

### 1.1 *(2025-07-10)*

- New project logo.
- Added markers for improving the output of the script and categorizing messages (information, warning, error).
- Rewritten and improved README.
- Other fixes and improvements.

### 1.01 *(2025-06-23)*

Fixed file read error that could occur when opening a template file without specifying file encoding.

### 1.0 *(2025-06-17)*

The first public release of XSiteGen, then called "TinySSG".