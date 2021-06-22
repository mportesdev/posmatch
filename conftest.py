import sys

import pytest

from posmatch import pos_match, PosMatchMeta

if sys.version_info < (3, 10):
    collect_ignore = ['tests/test_matching.py']


@pytest.fixture
def decorated_class_1():

    @pos_match
    class Class:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    return Class


@pytest.fixture
def decorated_class_2():

    @pos_match
    class Class:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

    return Class


@pytest.fixture
def class_from_metaclass_1():

    class Class(metaclass=PosMatchMeta):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    return Class


@pytest.fixture
def class_from_metaclass_2():

    class Class(metaclass=PosMatchMeta):
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

    return Class
