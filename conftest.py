import pytest

from posmatch import pos_match, PosMatchMeta, PosMatchMixin


@pytest.fixture(params=['decorator', 'decorator call', 'metaclass', 'mix-in'])
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

    class WithMixin(PosMatchMixin):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    return {
        'decorator': WithDecorator,
        'decorator call': WithDecoratorCall,
        'metaclass': WithMetaClass,
        'mix-in': WithMixin,
    }[request.param]


@pytest.fixture(params=['decorator', 'decorator call', 'metaclass', 'mix-in'])
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

    class WithMixin(PosMatchMixin):
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
        'mix-in': WithMixin,
    }[request.param]


@pytest.fixture(params=['decorator', 'decorator call', 'metaclass', 'mix-in'])
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

    class WithMixin(PosMatchMixin):
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
        'mix-in': WithMixin,
    }[request.param]


@pytest.fixture(params=['decorator', 'decorator call', 'metaclass', 'mix-in'])
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

    class WithMixin(BaseClass, PosMatchMixin):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    return {
        'decorator': WithDecorator,
        'decorator call': WithDecoratorCall,
        'metaclass': WithMetaClass,
        'mix-in': WithMixin,
    }[request.param]


@pytest.fixture(params=['own', 'inherited', 'none'])
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

    @pos_match(force=True)
    class WithNoMatchArgs:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.x = a + 42
            self.y = b + 42

    return {
        'own': WithOwnMatchArgs,
        'inherited': WithInheritedMatchArgs,
        'none': WithNoMatchArgs,
    }[request.param]


@pytest.fixture
def mixin_first():
    """Return a class with the mix-in at the beginning of its MRO."""

    class BaseClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        __match_args__ = ('a', 'b')

    class MixinFirst(PosMatchMixin, BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    return MixinFirst


@pytest.fixture
def mixin_last():
    """Return a class with the mix-in at the end of its MRO."""

    class BaseClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        __match_args__ = ('a', 'b')

    class MixinLast(BaseClass, PosMatchMixin):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    return MixinLast
