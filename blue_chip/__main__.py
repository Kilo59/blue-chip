"""
blue_chip.__main__.py
~~~~~~~~~~~~~~~~~~~~~
"""
from invoke import Collection, Program  # pylint: disable=import-error

from blue_chip import __version__, tasks

# pylint: disable=invalid-name
program = Program(
    namespace=Collection.from_module(tasks), name="blue-chip", version=__version__
)
