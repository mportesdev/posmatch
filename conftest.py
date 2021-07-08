from dataclasses import dataclass
import sys

import pytest

from posmatch import pos_match, PosMatchMeta

if sys.version_info < (3, 10):
    collect_ignore = ['tests/test_matching.py']

BY_DECORATOR = pytest.fixture(
    params=['decorator', 'decorator call']
)

BY_DECORATOR_OR_METACLASS = pytest.fixture(
    params=['decorator', 'decorator call', 'metaclass']
)


@BY_DECORATOR_OR_METACLASS
def simple_class(request):

    @pos_match
    class WithDecorator:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    @pos_match()
    class WithDecoratorCall:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class WithMetaClass(metaclass=PosMatchMeta):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    return {
        'decorator': WithDecorator,
        'decorator call': WithDecoratorCall,
        'metaclass': WithMetaClass,
    }[request.param]


@BY_DECORATOR_OR_METACLASS
def six_pack_class(request):
    """Return a class with six kinds of args in signature.
    (positional-only, positional, packed positional, keyword-only,
    keyword, packed keyword)
    """
    @pos_match
    class WithDecorator:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

    @pos_match()
    class WithDecoratorCall:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

    class WithMetaClass(metaclass=PosMatchMeta):
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

    return {
        'decorator': WithDecorator,
        'decorator call': WithDecoratorCall,
        'metaclass': WithMetaClass,
    }[request.param]


@BY_DECORATOR_OR_METACLASS
def class_with_attr(request):
    """Return a class with the `__match_args__` attribute set."""

    @pos_match
    class WithDecorator:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.x = a + 42
            self.y = b + 42

        __match_args__ = ('x', 'y')

    @pos_match()
    class WithDecoratorCall:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.x = a + 42
            self.y = b + 42

        __match_args__ = ('x', 'y')

    class WithMetaClass(metaclass=PosMatchMeta):
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.x = a + 42
            self.y = b + 42

        __match_args__ = ('x', 'y')

    return {
        'decorator': WithDecorator,
        'decorator call': WithDecoratorCall,
        'metaclass': WithMetaClass,
    }[request.param]


@BY_DECORATOR_OR_METACLASS
def class_with_inherited(request):
    """Return a class with the `__match_args__` attribute inherited."""

    class BaseClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        __match_args__ = ('a', 'b')

    @pos_match
    class WithDecorator(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    @pos_match()
    class WithDecoratorCall(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    class WithMetaClass(BaseClass, metaclass=PosMatchMeta):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    return {
        'decorator': WithDecorator,
        'decorator call': WithDecoratorCall,
        'metaclass': WithMetaClass,
    }[request.param]


@pytest.fixture(params=['own', 'inherited'])
def forced_class(request):
    """Return a class decorated with `@pos_match(force=True)`."""

    @pos_match(force=True)
    class WithOwnMatchArgs:
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
    class WithInheritedMatchArgs(BaseClass):
        def __init__(self, a, b):
            super().__init__(a, b)
            self.a = self.x + 42
            self.b = self.y + 42

    return {
        'own': WithOwnMatchArgs,
        'inherited': WithInheritedMatchArgs,
    }[request.param]


@BY_DECORATOR
def data_class(request):

    @pos_match
    @dataclass
    class WithDecorator:
        a: int
        b: bool
        c: str

    @pos_match()
    @dataclass
    class WithDecoratorCall:
        a: int
        b: bool
        c: str

    return {
        'decorator': WithDecorator,
        'decorator call': WithDecoratorCall,
    }[request.param]
