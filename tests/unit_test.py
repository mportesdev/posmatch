from posmatch import pos_match, PosMatchMeta, PosMatchMixin


def test_class_1(decorated_class_1):
    """Test `pos_match` decorator."""
    assert decorated_class_1.__match_args__ == ('a', 'b')

    instance = decorated_class_1(1, 2)
    assert instance.__match_args__ == ('a', 'b')


def test_class_2(decorated_class_2):
    """Test `pos_match` decorator."""
    assert decorated_class_2.__match_args__ == ('a', 'b', 'c', 'd', 'e', 'f')

    instance = decorated_class_2(1, 2, 3, d=4)
    assert instance.__match_args__ == ('a', 'b', 'c', 'd', 'e', 'f')


def test_init_with_args_and_kwargs():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, *args, **kwargs):
            ...

    assert Class.__match_args__ == ('args', 'kwargs')

    instance = Class(1, 2, c=3)
    assert instance.__match_args__ == ('args', 'kwargs')


def test_call_to_decorator_with_no_args():
    """Test `pos_match` decorator."""

    @pos_match()
    class Class:
        def __init__(self, x, y):
            ...

    assert Class.__match_args__ == ('x', 'y')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('x', 'y')


def test_existing_match_args_not_overwritten():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    assert Class.__match_args__ == ('x', 'y')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('x', 'y')


def test_force_overwrite_existing_match_args():
    """Test `pos_match` decorator."""

    @pos_match(force=True)
    class Class:
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    assert Class.__match_args__ == ('a', 'b')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('a', 'b')


def test_inherited_match_args_not_overridden():
    """Test `pos_match` decorator."""

    class BaseClass:
        def __init__(self, a, b):
            ...

        __match_args__ = ('a', 'b', 'c')

    @pos_match
    class SubClass(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)

    assert SubClass.__match_args__ == ('a', 'b', 'c')

    instance = SubClass(1, 2)
    assert instance.__match_args__ == ('a', 'b', 'c')


def test_force_override_inherited_match_args():
    """Test `pos_match` decorator."""

    class BaseClass:
        def __init__(self, a, b):
            ...

        __match_args__ = ('a', 'b', 'c')

    @pos_match(force=True)
    class SubClass(BaseClass):
        def __init__(self, x, y):
            super().__init__(x, y)

    assert SubClass.__match_args__ == ('x', 'y')

    instance = SubClass(1, 2)
    assert instance.__match_args__ == ('x', 'y')
    assert SubClass.__base__.__match_args__ == ('a', 'b', 'c')


def test_meta_simple_init():
    """Test `PosMatchMeta` metaclass."""

    class Class(metaclass=PosMatchMeta):
        def __init__(self, x, y):
            ...

    assert Class.__match_args__ == ('x', 'y')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('x', 'y')


def test_meta_init_with_all_kinds_of_args():
    """Test `PosMatchMeta` metaclass."""

    class Class(metaclass=PosMatchMeta):
        def __init__(self, a, /, b, *c, d, e=None, **f):
            ...

    assert Class.__match_args__ == ('a', 'b', 'c', 'd', 'e', 'f')

    instance = Class(1, 2, 3, d=4)
    assert instance.__match_args__ == ('a', 'b', 'c', 'd', 'e', 'f')


def test_meta_init_with_args_and_kwargs():
    """Test `PosMatchMeta` metaclass."""

    class Class(metaclass=PosMatchMeta):
        def __init__(self, *args, **kwargs):
            ...

    assert Class.__match_args__ == ('args', 'kwargs')

    instance = Class(1, 2, c=3)
    assert instance.__match_args__ == ('args', 'kwargs')


def test_meta_existing_match_args_not_overwritten():
    """Test `PosMatchMeta` metaclass."""

    class Class(metaclass=PosMatchMeta):
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    assert Class.__match_args__ == ('x', 'y')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('x', 'y')


def test_meta_inherited_match_args_not_overridden():
    """Test `PosMatchMeta` metaclass."""

    class BaseClass:
        def __init__(self, a, b):
            ...

        __match_args__ = ('a', 'b', 'c')

    class SubClass(BaseClass, metaclass=PosMatchMeta):
        def __init__(self, x, y):
            super().__init__(x, y)

    assert SubClass.__match_args__ == ('a', 'b', 'c')

    instance = SubClass(1, 2)
    assert instance.__match_args__ == ('a', 'b', 'c')


def test_mixin_simple_init():
    """Test `PosMatchMixin` mixin class."""

    class Class(PosMatchMixin):
        def __init__(self, x, y):
            super().__init__()

    # in the case of mixin, class will only have the attribute after
    # the first instantiation
    assert not hasattr(Class, '__match_args__')

    instance = Class(1, 2)
    assert Class.__match_args__ == ('x', 'y')
    assert instance.__match_args__ == ('x', 'y')


def test_mixin_init_with_all_kinds_of_args():
    """Test `PosMatchMixin` mixin class."""

    class Class(PosMatchMixin):
        def __init__(self, a, /, b, *c, d, e=None, **f):
            super().__init__()

    # in the case of mixin, class will only have the attribute after
    # the first instantiation
    assert not hasattr(Class, '__match_args__')

    instance = Class(1, 2, 3, d=4)
    assert Class.__match_args__ == ('a', 'b', 'c', 'd', 'e', 'f')
    assert instance.__match_args__ == ('a', 'b', 'c', 'd', 'e', 'f')


def test_mixin_init_with_args_and_kwargs():
    """Test `PosMatchMixin` mixin class."""

    class Class(PosMatchMixin):
        def __init__(self, *args, **kwargs):
            super().__init__()

    # in the case of mixin, class will only have the attribute after
    # the first instantiation
    assert not hasattr(Class, '__match_args__')

    instance = Class(1, 2, c=3)
    assert Class.__match_args__ == ('args', 'kwargs')
    assert instance.__match_args__ == ('args', 'kwargs')


def test_mixin_existing_match_args_not_overwritten():
    """Test `PosMatchMixin` mixin class."""

    class Class(PosMatchMixin):
        def __init__(self, a, b):
            super().__init__()

        __match_args__ = ('x', 'y')

    assert Class.__match_args__ == ('x', 'y')

    instance = Class(1, 2)
    assert instance.__match_args__ == ('x', 'y')


def test_mixin_inherited_match_args_not_overridden():
    """Test `PosMatchMixin` mixin class."""

    class BaseClass:
        def __init__(self, a, b):
            super().__init__()

        __match_args__ = ('a', 'b', 'c')

    class SubClass(BaseClass, PosMatchMixin):
        def __init__(self, x, y):
            super().__init__(x, y)

    assert SubClass.__match_args__ == ('a', 'b', 'c')

    instance = SubClass(1, 2)
    assert instance.__match_args__ == ('a', 'b', 'c')
