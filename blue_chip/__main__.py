"""
blue_chip.__main__.py
~~~~~~~~~~~~~~~~~~~~~
"""
import pkg_resources
from invoke import Collection, Program  # pylint: disable=import-error

import blue_chip.tasks

PACKAGE_NAME = "blue-chip"


def get_version():
    """
    Get the package version.

    https://github.com/python-poetry/poetry/issues/144#issuecomment-559793020
    """
    try:
        distribution = pkg_resources.get_distribution(PACKAGE_NAME)
    except pkg_resources.DistributionNotFound:
        return "dev"
    else:
        return distribution.version


PKG_VERSION = get_version()

# pylint: disable=invalid-name
program = Program(
    namespace=Collection.from_module(blue_chip.tasks),
    name=PACKAGE_NAME,
    version=PKG_VERSION,
)
