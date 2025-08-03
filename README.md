<div align="center">

![](images/logo.png)

# XSiteGen

#### [English](README.md) &bull; [Русский](README-RU.md)

</div>

**XSiteGen** is a minimalistic static site generator developed to be simple and easy to use, especially for users who do not wish to spend time and nerves on messing with more complex generators.

It has been written by me for my personal needs and for learning the basic principles of static site generator working. However, I will be happy if someone finds my work interesting and useful.

## Installation

Python 3.9+ and [Python-Markdown](https://pypi.org/project/Markdown/) module are required.

## Usage

Download XSiteGen (clone the repository or [grab the latest release](https://github.com/ivan-movchan/xsitegen/releases/latest)) and run `xsitegen.py` module.
Running `xsitegen.py` with `-v` or `--version` flag will display the version of the script.

The first line in every source file should contain the page title. The page content (Markdown-formatted text) should begin from the third line.

XSiteGen supports loading the configuration module from any directory other than the directory XSiteGen is located in. You can copy `config.py` module to the directory with source files of the website you are building, edit it and then run XSiteGen in that directory for building the website. XSiteGen should be available by `PATH` environment variable.

In `demo` folder you can find an example of a static site that can be generated using XSiteGen.

> [!WARNING]
> Python-Markdown is an implementation of *John Gruber's Markdown*, not widely used *CommonMark*. You may need to edit source files for more correct transforming source files into HTML.

## Version history

See [CHANGELOG.md](CHANGELOG.md) for details.

## Contributing

Any feedback and contributions are welcome. Report bugs and suggest new ideas using ["Issues"](https://github.com/ivan-movchan/xsitegen/issues) page or by contacting the developer privately. You are free to fork the repository, improve the project and send a pull request.

## Credits

- Idea and development: [Ivan Movchan](https://github.com/ivan-movchan).

## License

[MIT License](LICENSE)