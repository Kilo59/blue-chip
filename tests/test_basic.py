"""tests/test_basic.py"""
import subprocess
import pathlib
import importlib
from setuptools import find_packages

import pytest

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


@pytest.mark.parametrize("cmd", ["fmt", "lint"])
def test_noarg_cli_task(cmd):
    cmplt_process = subprocess.run(["bc", cmd])
    print(cmplt_process.stdout)
    assert cmplt_process.returncode is 0


if __name__ == "__main__":
    print(ROOT)
    pytest.main(args=[__file__, "-v"])
