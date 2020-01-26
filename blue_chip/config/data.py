"""
blue_chip.config.data.py
~~~~~~~~~~~~~~~~~~~~~~~~
"""
from blue_chip.constants import LINE_LENGTH

LINT_DATA = {
    "bc_root.yaml": f"""pylint:
  disable:
    # covered by pep8
    - line-too-long
    # black conflict
    - bad-continuation
  options:
    logging-format-style: "fstr"

pep8:
  options:
    max-line-length: {LINE_LENGTH}

pep257:
  disable:
    - D400
    # First line rules conflict with sphinx requirements.
    - D415
    # blank line required between summary line and description
    - D205
    # Multi-line docstring summary should start at the first line
    - D212
""",
    "bc_audit.yaml": f"""strictness: veryhigh
test-warnings: false
doc-warnings: true

inherits:
  - bc_root.yaml

pylint:
  options:
    # max-args default = 5
    max-args: 4
    # max-locals default = 15
    max-locals: 12
    # max-branches default = 15
    max-branches: 12

mccabe:
  options:
    max-complexity: 7

pyroma:
  run: True
  disable:
    - PYR18
""",
    "bc_default.yaml": f"""strictness: veryhigh
test-warnings: false
doc-warnings: true

inherits:
  - bc_audit.yaml

pylint:
  options:
    # max-args default = 5
    max-args: 6
    # max-locals default = 15
    max-locals: 15
    # max-branches default = 15
    max-branches: 15
    good-names: E,i,j,d,k,v,_
  disable:
    - locally-disabled
    - fixme

pyflakes:
  disable:
    # covered by pylint
    - F841

mccabe:
  options:
    max-complexity: 10

pep257:
  run: True
""",
    "bc_tests.yaml": f"""inherits:
  - bc_default.yaml

strictness: high
test-warnings: true
doc-warnings: false

pyroma:
  run: False

pep257:
  run: False
""",
}
