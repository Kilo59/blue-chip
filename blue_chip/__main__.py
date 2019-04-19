"""
blue_chip.__main__.py
~~~~~~~~~~~~~~~~~~~~~
"""
from invoke import Collection, Program  # pylint: disable=import-error
from blue_chip import tasks


# pylint: disable=invalid-name
program = Program(namespace=Collection.from_module(tasks), version="18.0a.1")
