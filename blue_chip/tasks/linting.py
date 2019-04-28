from shutil import get_terminal_size

from invoke import task

from blue_chip import constants
from blue_chip import config


# pylint:disable=protected-access


STAR_SEP = "*" * get_terminal_size().columns


@task
def cfg_lint(ctx):  # pylint:disable=unused-argument
    """Configure prospector profiles."""
    if constants.BC_LINTRC_PATH.exists():
        return
    config.lint._init(config.data.LINT_DATA, constants.BC_LINTRC_PATH)
    print(
        "Lint configuration profiles created at:",
        f" {constants.BC_LINTRC_PATH}\n{STAR_SEP}",
    )


@task(pre=[cfg_lint])
def lint(ctx, targets="."):
    """Run static analysis on python source code."""
    args = [
        "prospector",
        "--profile-path",
        str(constants.BC_LINTRC_PATH),
        "--profile",
        "bc_default",
    ]
    ctx.run(f"{' '.join(args)} {targets}")
