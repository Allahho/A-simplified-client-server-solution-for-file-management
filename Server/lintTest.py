from pylint.lint import Run
import os
import sys
import inspect

results = Run(['usertests.py'], do_exit=False)
# `exit` is deprecated, use `do_exit` instead
print(results.linter.stats['global_note'])