import sys

import pytest

from posmatch.core import auto_match_args


def test_simple_init():

    @auto_match_args
    class Class:
        def __init__(self, x, y):
            ...

    assert Class.__match_args__ == ('x', 'y')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('x', 'y')


def test_init_with_all_kinds_of_args():

    @auto_match_args
    class Class:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            ...

    assert Class.__match_args__ == ('a', 'b', 'c', 'd', 'e', 'f')

    instance = Class(1, 2, 3, d=4)
    assert instance.__match_args__ == ('a', 'b', 'c', 'd', 'e', 'f')


def test_init_with_args_and_kwargs():

    @auto_match_args
    class Class:
        def __init__(self, *args, **kwargs):
            ...

    assert Class.__match_args__ == ('args', 'kwargs')

    instance = Class(1, 2, c=3)
    assert instance.__match_args__ == ('args', 'kwargs')


def test_call_to_decorator_with_no_args():

    @auto_match_args()
    class Class:
        def __init__(self, x, y):
            ...

    assert Class.__match_args__ == ('x', 'y')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('x', 'y')


def test_existing_match_args_not_overwritten():

    @auto_match_args
    class Class:
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    assert Class.__match_args__ == ('x', 'y')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('x', 'y')


def test_force_overwrite_existing_match_args():

    @auto_match_args(force=True)
    class Class:
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    assert Class.__match_args__ == ('a', 'b')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('a', 'b')


def test_inherited_match_args_not_overridden():

    class BaseClass:
        def __init__(self, a, b):
            ...

        __match_args__ = ('a', 'b', 'c')

    @auto_match_args
    class SubClass(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)

    assert SubClass.__match_args__ == ('a', 'b', 'c')

    instance = SubClass(1, 2)
    assert instance.__match_args__ == ('a', 'b', 'c')


def test_force_override_inherited_match_args():

    class BaseClass:
        def __init__(self, a, b):
            ...

        __match_args__ = ('a', 'b', 'c')

    @auto_match_args(force=True)
    class SubClass(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)

    assert SubClass.__match_args__ == ('x', 'y')

    instance = SubClass(1, 2)
    assert instance.__match_args__ == ('x', 'y')
    assert SubClass.__base__.__match_args__ == ('a', 'b', 'c')


@pytest.mark.skipif(sys.version_info < (3, 10), reason='requires Py 3.10+')
def test_simple_class_pattern_matching_one_attribute():

    @auto_match_args
    class Class:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    from matching import match_first

    instance = Class(1, 2)
    assert match_first(instance) == 1


@pytest.mark.skipif(sys.version_info < (3, 10), reason='requires Py 3.10+')
def test_simple_class_pattern_matching_two_attributes():

    @auto_match_args
    class Class:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    from matching import match_two

    instance = Class(x='foo', y=42)
    assert match_two(instance) == ('foo', 42)


@pytest.mark.skipif(sys.version_info < (3, 10), reason='requires Py 3.10+')
def test_pattern_matching_one_attribute():

    @auto_match_args
    class Class:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b

    from matching import match_first

    instance = Class(1, 2, d=3)
    assert match_first(instance) == 1


@pytest.mark.skipif(sys.version_info < (3, 10), reason='requires Py 3.10+')
def test_pattern_matching_two_attributes():

    @auto_match_args
    class Class:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b

    from matching import match_two

    instance = Class('bar', b=[], d=42)
    assert match_two(instance) == ('bar', [])
