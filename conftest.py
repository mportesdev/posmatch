import sys

if sys.version_info < (3, 10):
    collect_ignore = ['tests/test_matching.py']
