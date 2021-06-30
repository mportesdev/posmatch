import sys

import pytest

from posmatch import pos_match, PosMatchMeta

if sys.version_info < (3, 10):
    collect_ignore = ['tests/test_matching.py']


@pytest.fixture(params=['decorator', 'decorator call', 'metaclass'])
def simple_class(request):

    @pos_match
    class ClassWithDecorator:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    @pos_match()
    class ClassWithDecoratorCall:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class ClassWithMetaClass(metaclass=PosMatchMeta):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    return {
        'decorator': ClassWithDecorator,
        'decorator call': ClassWithDecoratorCall,
        'metaclass': ClassWithMetaClass,
    }[request.param]


@pytest.fixture(params=['decorator', 'decorator call', 'metaclass'])
def six_pack_class(request):
    """Return a class with six kinds of args in signature.
    (positional-only, positional, packed positional, keyword-only,
    keyword, packed keyword)
    """
    @pos_match
    class ClassWithDecorator:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

    @pos_match()
    class ClassWithDecoratorCall:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

    class ClassWithMetaClass(metaclass=PosMatchMeta):
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

    return {
        'decorator': ClassWithDecorator,
        'decorator call': ClassWithDecoratorCall,
        'metaclass': ClassWithMetaClass,
    }[request.param]


@pytest.fixture(params=['decorator', 'decorator call', 'metaclass'])
def class_with_attr(request):
    """Return a class with the `__match_args__` attribute set."""

    @pos_match
    class ClassWithDecorator:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.x = a + 42
            self.y = b + 42

        __match_args__ = ('x', 'y')

    @pos_match()
    class ClassWithDecoratorCall:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.x = a + 42
            self.y = b + 42

        __match_args__ = ('x', 'y')

    class ClassWithMetaClass(metaclass=PosMatchMeta):
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.x = a + 42
            self.y = b + 42

        __match_args__ = ('x', 'y')

    return {
        'decorator': ClassWithDecorator,
        'decorator call': ClassWithDecoratorCall,
        'metaclass': ClassWithMetaClass,
    }[request.param]


@pytest.fixture(params=['decorator', 'decorator call', 'metaclass'])
def class_with_inherited(request):
    """Return a class with the `__match_args__` attribute inherited."""

    class BaseClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        __match_args__ = ('a', 'b')

    @pos_match
    class ClassWithDecorator(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    @pos_match()
    class ClassWithDecoratorCall(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    class ClassWithMetaClass(BaseClass, metaclass=PosMatchMeta):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    return {
        'decorator': ClassWithDecorator,
        'decorator call': ClassWithDecoratorCall,
        'metaclass': ClassWithMetaClass,
    }[request.param]


@pytest.fixture(params=['own', 'inherited'])
def forced_class(request):
    """Return a class decorated with `@pos_match(force=True)`."""

    @pos_match(force=True)
    class ClassWithOwnMatchArgs:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.x = a + 42
            self.y = b + 42

        __match_args__ = ('x', 'y')

    class BaseClass:
        def __init__(self, x, y):
            self.x = x - 42
            self.y = y - 42

        __match_args__ = ('x', 'y')

    @pos_match(force=True)
    class ClassWithInheritedMatchArgs(BaseClass):
        def __init__(self, a, b):
            super().__init__(a, b)
            self.a = self.x + 42
            self.b = self.y + 42

    return {
        'own': ClassWithOwnMatchArgs,
        'inherited': ClassWithInheritedMatchArgs,
    }[request.param]
