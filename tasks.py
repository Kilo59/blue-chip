"""tasks.py"""

from invoke import task

from blue_chip import constants


@task
def clean(ctx, docs=False, bytecode=False, lintrc=False, extra=""):
    """Cleanup"""
    patterns = ["build"]
    if docs:
        patterns.append("docs/_build")
    if bytecode:
        patterns.append("**/*.pyc")
    if lintrc:
        patterns.append("/".join(constants.BC_LINTRC_PATH.parts[-2:]))
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        print(f"cleaning {pattern}...")
        ctx.run(f"rm -rf {pattern}")
