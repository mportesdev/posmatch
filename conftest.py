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

    @pos_match
    class ClassWithDecorator:
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    @pos_match()
    class ClassWithDecoratorCall:
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    class ClassWithMetaClass(metaclass=PosMatchMeta):
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    return {
        'decorator': ClassWithDecorator,
        'decorator call': ClassWithDecoratorCall,
        'metaclass': ClassWithMetaClass,
    }[request.param]


@pytest.fixture(params=['decorator', 'decorator call', 'metaclass'])
def class_with_inherited(request):

    class BaseClass:
        def __init__(self, a, b):
            ...

        __match_args__ = ('a', 'b', 'c')

    @pos_match
    class ClassWithDecorator(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)

    @pos_match()
    class ClassWithDecoratorCall(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)

    class ClassWithMetaClass(BaseClass, metaclass=PosMatchMeta):
        def __init__(self, x, y):
            super().__init__(x, y)

    return {
        'decorator': ClassWithDecorator,
        'decorator call': ClassWithDecoratorCall,
        'metaclass': ClassWithMetaClass,
    }[request.param]
