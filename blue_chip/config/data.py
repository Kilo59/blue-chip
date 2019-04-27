from blue_chip.constants import LINE_LENGTH

LINT_DATA = {
    "bc_root.yaml": f"""pylint:
  disable:
    # covered by pep8
    - line-too-long
    - logging-fstring-interpolation
    # black conflict
    - bad-continuation

pep8:
  options:
    max-line-length: {LINE_LENGTH}
""",
    "bc_audit.yaml": f"""strictness: veryhigh
test-warnings: false
doc-warnings: true

inherits:
  - bc_root.yaml.yaml

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
