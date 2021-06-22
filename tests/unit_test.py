from posmatch import pos_match, PosMatchMeta, PosMatchMixin


def test_class_1(decorated_class_1):
    """Test `pos_match` decorator."""
    expected = ('a', 'b')
    assert decorated_class_1.__match_args__ == expected

    instance = decorated_class_1(1, 2)
    assert instance.__match_args__ == expected


def test_class_2(decorated_class_2):
    """Test `pos_match` decorator."""
    expected = ('a', 'b', 'c', 'd', 'e', 'f')
    assert decorated_class_2.__match_args__ == expected

    instance = decorated_class_2(1, 2, 3, d=4)
    assert instance.__match_args__ == expected


def test_init_with_args_and_kwargs():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, *args, **kwargs):
            ...

    expected = ('args', 'kwargs')
    assert Class.__match_args__ == expected

    instance = Class(1, 2, c=3)
    assert instance.__match_args__ == expected


def test_call_to_decorator_with_no_args():
    """Test `pos_match` decorator."""

    @pos_match()
    class Class:
        def __init__(self, x, y):
            ...

    expected = ('x', 'y')
    assert Class.__match_args__ == expected

    instance = Class(1, 2)
    assert instance.__match_args__ == expected


def test_existing_match_args_not_overwritten():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    expected = ('x', 'y')
    assert Class.__match_args__ == expected

    instance = Class(1, 2)
    assert instance.__match_args__ == expected


def test_force_overwrite_existing_match_args():
    """Test `pos_match` decorator."""

    @pos_match(force=True)
    class Class:
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    expected = ('a', 'b')
    assert Class.__match_args__ == expected

    instance = Class(1, 2)
    assert instance.__match_args__ == expected


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

    expected = ('a', 'b', 'c')
    assert SubClass.__match_args__ == expected

    instance = SubClass(1, 2)
    assert instance.__match_args__ == expected


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

    expected = ('x', 'y')
    assert SubClass.__match_args__ == expected

    instance = SubClass(1, 2)
    assert instance.__match_args__ == expected
    assert SubClass.__base__.__match_args__ == ('a', 'b', 'c')


def test_meta_simple_init():
    """Test `PosMatchMeta` metaclass."""

    class Class(metaclass=PosMatchMeta):
        def __init__(self, x, y):
            ...

    expected = ('x', 'y')
    assert Class.__match_args__ == expected

    instance = Class(1, 2)
    assert instance.__match_args__ == expected


def test_meta_init_with_all_kinds_of_args():
    """Test `PosMatchMeta` metaclass."""

    class Class(metaclass=PosMatchMeta):
        def __init__(self, a, /, b, *c, d, e=None, **f):
            ...

    expected = ('a', 'b', 'c', 'd', 'e', 'f')
    assert Class.__match_args__ == expected

    instance = Class(1, 2, 3, d=4)
    assert instance.__match_args__ == expected


def test_meta_init_with_args_and_kwargs():
    """Test `PosMatchMeta` metaclass."""

    class Class(metaclass=PosMatchMeta):
        def __init__(self, *args, **kwargs):
            ...

    expected = ('args', 'kwargs')
    assert Class.__match_args__ == expected

    instance = Class(1, 2, c=3)
    assert instance.__match_args__ == expected


def test_meta_existing_match_args_not_overwritten():
    """Test `PosMatchMeta` metaclass."""

    class Class(metaclass=PosMatchMeta):
        def __init__(self, a, b):
            ...

        __match_args__ = ('x', 'y')

    expected = ('x', 'y')
    assert Class.__match_args__ == expected

    instance = Class(1, 2)
    assert instance.__match_args__ == expected


def test_meta_inherited_match_args_not_overridden():
    """Test `PosMatchMeta` metaclass."""

    class BaseClass:
        def __init__(self, a, b):
            ...

        __match_args__ = ('a', 'b', 'c')

    class SubClass(BaseClass, metaclass=PosMatchMeta):
        def __init__(self, x, y):
            super().__init__(x, y)

    expected = ('a', 'b', 'c')
    assert SubClass.__match_args__ == expected

    instance = SubClass(1, 2)
    assert instance.__match_args__ == expected


def test_mixin_simple_init():
    """Test `PosMatchMixin` mixin class."""

    class Class(PosMatchMixin):
        def __init__(self, x, y):
            super().__init__()

    # in the case of mixin, class will only have the attribute after
    # the first instantiation
    assert not hasattr(Class, '__match_args__')

    instance = Class(1, 2)
    expected = ('x', 'y')
    assert Class.__match_args__ == expected
    assert instance.__match_args__ == expected


def test_mixin_init_with_all_kinds_of_args():
    """Test `PosMatchMixin` mixin class."""

    class Class(PosMatchMixin):
        def __init__(self, a, /, b, *c, d, e=None, **f):
            super().__init__()

    # in the case of mixin, class will only have the attribute after
    # the first instantiation
    assert not hasattr(Class, '__match_args__')

    instance = Class(1, 2, 3, d=4)
    expected = ('a', 'b', 'c', 'd', 'e', 'f')
    assert Class.__match_args__ == expected
    assert instance.__match_args__ == expected


def test_mixin_init_with_args_and_kwargs():
    """Test `PosMatchMixin` mixin class."""

    class Class(PosMatchMixin):
        def __init__(self, *args, **kwargs):
            super().__init__()

    # in the case of mixin, class will only have the attribute after
    # the first instantiation
    assert not hasattr(Class, '__match_args__')

    instance = Class(1, 2, c=3)
    expected = ('args', 'kwargs')
    assert Class.__match_args__ == expected
    assert instance.__match_args__ == expected


def test_mixin_existing_match_args_not_overwritten():
    """Test `PosMatchMixin` mixin class."""

    class Class(PosMatchMixin):
        def __init__(self, a, b):
            super().__init__()

        __match_args__ = ('x', 'y')

    expected = ('x', 'y')
    assert Class.__match_args__ == expected

    instance = Class(1, 2)
    assert instance.__match_args__ == expected


def test_mixin_inherited_match_args_not_overridden():
    """Test `PosMatchMixin` mixin class."""

    class BaseClass:
        def __init__(self, a, b):
            super().__init__()

        __match_args__ = ('a', 'b', 'c')

    class SubClass(BaseClass, PosMatchMixin):
        def __init__(self, x, y):
            super().__init__(x, y)

    expected = ('a', 'b', 'c')
    assert SubClass.__match_args__ == expected

    instance = SubClass(1, 2)
    assert instance.__match_args__ == expected
