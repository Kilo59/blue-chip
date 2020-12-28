[![PyPI version](https://badge.fury.io/py/blue-chip.svg)](https://badge.fury.io/py/blue-chip)
[![Build Status](https://travis-ci.com/Kilo59/blue-chip.svg?branch=master)](https://travis-ci.com/Kilo59/blue-chip)
[![Coverage Status](https://coveralls.io/repos/github/Kilo59/blue-chip/badge.svg?branch=master)](https://coveralls.io/github/Kilo59/blue-chip?branch=master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Kilo59/blue-chip.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Kilo59/blue-chip/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/Kilo59/blue-chip.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Kilo59/blue-chip/alerts/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# blue-chip
One click Python code quality package

`blue-chip` uses [`black`](https://github.com/ambv/black), [`isort`](https://github.com/timothycrosley/isort), [`invoke`](http://www.pyinvoke.org/) and [`prospector`](https://prospector.readthedocs.io/en/master/) configured to work well together out of the box.

-----------------------
## Install

The recommended installation method when installing globally is to use [`pipx`](https://github.com/pipxproject/pipx)

```
pipx install blue-chip
```
Otherwise (for best results) use `pip` to install directly into your project's virtual environment.
```
pip install blue-chip
```
Using [`poetry`](https://python-poetry.org/).
```
poetry add --dev blue-chip
```
Using [`pipenv`](https://pipenv.pypa.io/en/latest/) you need to pin the version.
```
pipenv install --dev blue-chip==0.0.8
```

## Command-line use

List the possible `blue-chip` commands with `bc --list`
```
$bc --list

Subcommands:

  fmt    Format python source code.
  lint   Run static analysis on python source code.
  sort   Sort module imports.
```

----------------------

## Enterprise use
Enterprise teams may find it useful to fork and redistribute this package with their own custom defined standards.


In many cases this is a simple as changing the package name and values in [`blue_chip/constants.py`](https://github.com/Kilo59/blue-chip/blob/master/blue_chip/constants.py).

For fine grain control of the static analysis tools, edit the `prospector` profiles in [`blue_chip/config`](https://github.com/Kilo59/blue-chip/blob/master/blue_chip/config/data.py).
