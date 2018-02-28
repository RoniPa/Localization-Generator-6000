# Localization Generator 6000
Simple python cli tool for generating (empty) localization json files for [Ngx-Translate](https://github.com/ngx-translate/core) from source code.
Uses RegExp match for finding translate pipe in templates and parses tags from them.

_Note: Doesn't support all formats of translation, only parses from templates!_

## Installation
1. Install [setuptools](https://pypi.python.org/pypi/setuptools)
2. Run ```python setup.py build``` to build
3. Run ```python setup.py install``` to install

## How to use
Run with command ```locgen```

### Options:
* __--help:__ Display help
* __--p:__ Source path (e.g. "./src/")
* __--o:__ Output file (e.g. "./localizations/en-US.json")
* __--e:__ File encoding (e.g. "utf-8"). Defaults to utf-8.

If source & output are not given with args, they're prompted for.

