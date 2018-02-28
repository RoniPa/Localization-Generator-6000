# Localization Generator 6000
Simple python tool for generating localization json files for [Ngx-Translate](https://github.com/ngx-translate/core) from source code.
Uses RegExp match for finding translate pipe in templates and parses tags from them.

_Note: Doesn't support all formats of localization, only parses from templates!_

## Installation
1. Install [setuptools](https://pypi.python.org/pypi/setuptools)
2. Run ```python setup.py build``` to build
3. Run ```python setup.py install``` to install

## How to use
Run with command ```locgen```

### Options:
__-p, --path__
Source path (e.g. "./src/")

__-o, --output__
Output file (e.g. "./localizations/en-US.json")

__-e, --encoding__
File encoding (e.g. "utf-8")

__-a, --append / -na, --no-append__
Append content - if file exists, existing translations remain. Removed or moved tags are still destroyed. Enabled by default.

__--help__
Show this message and exit.

If source & output are not given with args, they're prompted for.

