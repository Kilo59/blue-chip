"""
blue_chip.tasks.formatting.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from invoke import task

from blue_chip import constants


@task(
    help={
        "line-length": "How many characters per line to allow. [default: {}]".format(
            constants.LINE_LENGTH
        ),
        "targets": "Paths/directories to format. [default: . ]",
    },
)
def sort(ctx, line_length=constants.LINE_LENGTH, targets="."):
    """Sort module imports"""
    print("sorting imports ...")
    args = [
        "isort",
        "--use-parentheses",
        "--trailing-comma",
        "--force-grid-wrap",
        "0",
        "--multi-line",
        "3",
        "-l",
        str(line_length),
        "-rc",
        "--atomic",
        targets,
    ]
    ctx.run(" ".join(args))


@task(
    pre=[sort],
    help={
        "line-length": "How many characters per line to allow. [default: {}]".format(
            constants.LINE_LENGTH
        ),
        "targets": "Paths/directories to format. [default: . ]",
    },
)
def fmt(ctx, line_length=constants.LINE_LENGTH, targets="."):
    """Format python source code."""
    print("formatting ...")
    if isinstance(targets, (list, tuple, set)):
        targets = " ".join(targets)
    ctx.run(f"black --line-length {line_length} {targets}")
