from invoke import Collection, Program  # pylint: disable=import-error
from . import tasks


# pylint: disable=invalid-name
program = Program(namespace=Collection.from_module(tasks), version="18.0a.1")
