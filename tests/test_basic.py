"""tests/test_basic.py"""
import importlib
import pathlib
import subprocess

import pytest
from setuptools import find_packages

ROOT = pathlib.Path(__file__).joinpath("..").resolve()


def test_for_fire():
    all_modules = find_packages(exclude=["tests"])
    on_fire = {}

    for module in all_modules:
        try:
            importlib.import_module(module)
            print(f"✔️  {module}")
        except ImportError as import_error:
            on_fire[module] = import_error
            print(f"❌  {module}")
        except Exception as error:
            on_fire[module] = error
            print(f"❌  {module}")

    if on_fire:
        raise ImportError(", ".join(on_fire.keys()))


@pytest.mark.parametrize("cmd", ["fmt", "lint", "sort"])
def test_noarg_cli_task(cmd):
    cmplt_process = subprocess.run(["bcp", cmd])
    print(cmplt_process.stdout)
    assert cmplt_process.returncode is 0


@pytest.mark.parametrize(
    "targets_arg",
    ["foo.py", ("foo.py", "bar.py"), ["foo.py", "bar.py"], {"foo.py", "bar.py"}],
)
def test_fmt_cmd(targets_arg):
    from blue_chip.tasks.formatting import _fmt_cmd

    cmd_string = _fmt_cmd(88, targets_arg)
    assert isinstance(cmd_string, str)


if __name__ == "__main__":
    print(ROOT)
    pytest.main(args=[__file__, "-v"])
