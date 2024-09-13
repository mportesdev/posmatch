import pytest

from posmatch import PosMatchMeta, PosMatchMixin, pos_match


@pytest.fixture(params=["decorator", "decorator call", "metaclass", "mixin"])
def simple_class(request):
    if request.param == "decorator":

        @pos_match
        class _Cls:
            def __init__(self, a, b):
                self.a = a
                self.b = b

        return _Cls

    if request.param == "decorator call":

        @pos_match()
        class _Cls:
            def __init__(self, a, b):
                self.a = a
                self.b = b

        return _Cls

    if request.param == "metaclass":

        class _Cls(metaclass=PosMatchMeta):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        return _Cls

    if request.param == "mixin":

        class _Cls(PosMatchMixin):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        return _Cls


@pytest.fixture(params=["decorator", "decorator call", "metaclass", "mixin"])
def multi_param_class(request):
    """Return a class with different kinds of parameters in the
    signature of `__init__`. (positional-only, positional, keyword,
    keyword-only)
    """

    if request.param == "decorator":

        @pos_match
        class _Cls:
            def __init__(self, a, /, b, c=None, *, d):
                self.a = a
                self.b = b
                self.c = c
                self.d = d

        return _Cls

    if request.param == "decorator call":

        @pos_match()
        class _Cls:
            def __init__(self, a, /, b, c=None, *, d):
                self.a = a
                self.b = b
                self.c = c
                self.d = d

        return _Cls

    if request.param == "metaclass":

        class _Cls(metaclass=PosMatchMeta):
            def __init__(self, a, /, b, c=None, *, d):
                self.a = a
                self.b = b
                self.c = c
                self.d = d

        return _Cls

    if request.param == "mixin":

        class _Cls(PosMatchMixin):
            def __init__(self, a, /, b, c=None, *, d):
                self.a = a
                self.b = b
                self.c = c
                self.d = d

        return _Cls


@pytest.fixture(params=["decorator", "decorator call", "metaclass", "mixin"])
def class_with_own_match_args(request):
    """Return a class with the `__match_args__` attribute set."""

    if request.param == "decorator":

        @pos_match
        class _Cls:
            def __init__(self, a, b):
                self.a = a
                self.b = b
                self.x = a + 42
                self.y = b + 42

            __match_args__ = ("x", "y")

        return _Cls

    if request.param == "decorator call":

        @pos_match()
        class _Cls:
            def __init__(self, a, b):
                self.a = a
                self.b = b
                self.x = a + 42
                self.y = b + 42

            __match_args__ = ("x", "y")

        return _Cls

    if request.param == "metaclass":

        class _Cls(metaclass=PosMatchMeta):
            def __init__(self, a, b):
                self.a = a
                self.b = b
                self.x = a + 42
                self.y = b + 42

            __match_args__ = ("x", "y")

        return _Cls

    if request.param == "mixin":

        class _Cls(PosMatchMixin):
            def __init__(self, a, b):
                self.a = a
                self.b = b
                self.x = a + 42
                self.y = b + 42

            __match_args__ = ("x", "y")

        return _Cls


@pytest.fixture(params=["decorator", "decorator call", "metaclass", "mixin"])
def class_with_inherited_match_args(request):
    """Return a class with the `__match_args__` attribute inherited."""

    class BaseClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        __match_args__ = ("a", "b")

    if request.param == "decorator":

        @pos_match
        class _Cls(BaseClass):
            def __init__(self, x, y):
                super().__init__(x, y)
                self.x = self.a + 42
                self.y = self.b + 42

        return _Cls

    if request.param == "decorator call":

        @pos_match()
        class _Cls(BaseClass):
            def __init__(self, x, y):
                super().__init__(x, y)
                self.x = self.a + 42
                self.y = self.b + 42

        return _Cls

    if request.param == "metaclass":

        class _Cls(BaseClass, metaclass=PosMatchMeta):
            def __init__(self, x, y):
                super().__init__(x, y)
                self.x = self.a + 42
                self.y = self.b + 42

        return _Cls

    if request.param == "mixin":

        class _Cls(BaseClass, PosMatchMixin):
            def __init__(self, x, y):
                super().__init__(x, y)
                self.x = self.a + 42
                self.y = self.b + 42

        return _Cls


@pytest.fixture(params=["own", "inherited", "no __match_args__", "manual decoration"])
def class_with_force_true(request):
    """Return a class decorated with `@pos_match(force=True)`."""

    if request.param == "own":

        @pos_match(force=True)
        class _Cls:
            def __init__(self, a, b):
                self.a = a
                self.b = b
                self.x = a + 42
                self.y = b + 42

            __match_args__ = ("x", "y")

        return _Cls

    if request.param == "inherited":

        class BaseClass:
            def __init__(self, x, y):
                self.x = x - 42
                self.y = y - 42

            __match_args__ = ("x", "y")

        @pos_match(force=True)
        class _Cls(BaseClass):
            def __init__(self, a, b):
                super().__init__(a, b)
                self.a = self.x + 42
                self.b = self.y + 42

        return _Cls

    if request.param == "no __match_args__":

        @pos_match(force=True)
        class _Cls:
            def __init__(self, a, b):
                self.a = a
                self.b = b
                self.x = a + 42
                self.y = b + 42

        return _Cls

    if request.param == "manual decoration":

        class _Cls:
            def __init__(self, a, b):
                self.a = a
                self.b = b
                self.x = a + 42
                self.y = b + 42

            __match_args__ = ("x", "y")

        return pos_match(_Cls, force=True)


@pytest.fixture
def mixin_first():
    """Return a class with the mix-in at the beginning of its MRO."""

    class BaseClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        __match_args__ = ("a", "b")

    class _Cls(PosMatchMixin, BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    return _Cls


@pytest.fixture
def mixin_last():
    """Return a class with the mix-in at the end of its MRO."""

    class BaseClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        __match_args__ = ("a", "b")

    class _Cls(BaseClass, PosMatchMixin):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = self.a + 42
            self.y = self.b + 42

    return _Cls
