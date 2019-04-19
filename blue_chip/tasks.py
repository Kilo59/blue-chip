"""
blue_chip.tasks.py
~~~~~~~~~~~~~~~~~~
Invoke tasks file
"""
from invoke import task

from . import constants


@task
def fmt(ctx, line_length=constants.LINE_LENGTH, targets="."):
    """[summary]

    Parameters
    ----------
    ctx : [type]
        [description]
    targets : str, optional
        [description], by default "."
    """
    if isinstance(targets, (list, tuple, set)):
        targets = " ".join(targets)
    ctx.run(f"black --line-length {line_length} {targets}")
