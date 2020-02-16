"""
blue_chip.tasks.formatting.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from typing import List, Union

from invoke import task

from blue_chip import constants

__all__ = ["sort", "fmt", "fmt_only"]


@task(
    help={
        "line-length": "How many characters per line to allow. [default: {}]".format(
            constants.LINE_LENGTH
        ),
        "targets": "Paths/directories to format. [default: . ]",
    },
)
def sort(ctx, line_length=constants.LINE_LENGTH, targets="."):
    """Sort module imports."""
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


def _fmt_cmd(line_length: int, targets: Union[str, List[str]]) -> str:
    args = ["black", "--line-length", str(line_length)]
    if isinstance(targets, (list, tuple, set)):
        args.extend(targets)
    else:
        args.append(targets)
    return " ".join(args)


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
    """Format python source code & sort imports."""
    print("formatting ...")
    ctx.run(_fmt_cmd(line_length, targets))


@task(
    help={
        "line-length": "How many characters per line to allow. [default: {}]".format(
            constants.LINE_LENGTH
        ),
        "targets": "Paths/directories to format. [default: . ]",
    },
)
def fmt_only(ctx, line_length=constants.LINE_LENGTH, targets="."):
    """Format python source code."""
    ctx.run(_fmt_cmd(line_length, targets))
