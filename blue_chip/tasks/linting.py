"""
blue_chip.tasks.linting
~~~~~~~~~~~~~~~~~~~~~~~
"""
import pathlib
from shutil import get_terminal_size

from invoke import task

from blue_chip import config, constants

__all__ = ["cfg_lint", "lint"]


STAR_SEP = "*" * get_terminal_size().columns


@task
def cfg_lint(ctx, force=False):  # pylint:disable=unused-argument
    """Configure prospector profiles."""
    if constants.BC_LINTRC_PATH.exists() and not force:
        return
    lintrc_path = pathlib.Path(constants.BC_LINTRC_PATH)
    lintrc_path.mkdir(exist_ok=True)
    for profile_name, profile_content in config.data.LINT_DATA.items():
        profile_path = lintrc_path / profile_name
        print(f"  Initializing {profile_name} ...")
        with open(profile_path, mode="w", encoding="utf-8") as f_out:
            f_out.write(profile_content)
    print(
        "Lint configuration profiles created at:\n",
        f"\t{constants.BC_LINTRC_PATH}\n{STAR_SEP}",
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
