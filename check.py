"""Run one function's public doctests: python3 check.py is_even."""

import doctest
import sys

import lab


if len(sys.argv) != 2:
    raise SystemExit('Usage: python3 check.py FUNCTION_NAME')
name = sys.argv[1]
function = getattr(lab, name, None)
if not callable(function) or name.startswith('_'):
    raise SystemExit('No function named ' + name + ' in lab.py')
runner = doctest.DocTestRunner(verbose=True)
for test in doctest.DocTestFinder().find(function, name, globs=vars(lab)):
    runner.run(test)
result = runner.summarize()
raise SystemExit(1 if result.failed else 0)
