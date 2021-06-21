from posmatch import pos_match


def match_first(obj):
    """Match `obj` using positional subpatterns. Python 3.10+ only."""
    cls = obj.__class__

    match obj:
        case cls(atr):
            return atr


def match_two(obj):
    """Match `obj` using positional subpatterns. Python 3.10+ only."""
    cls = obj.__class__

    match obj:
        case cls(a, b):
            return a, b


def test_simple_class_pattern_matching_one_attribute():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    instance = Class(1, 2)
    assert match_first(instance) == 1


def test_simple_class_pattern_matching_two_attributes():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    instance = Class(x='foo', y=42)
    assert match_two(instance) == ('foo', 42)


def test_pattern_matching_one_attribute():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b

    instance = Class(1, 2, d=3)
    assert match_first(instance) == 1


def test_pattern_matching_two_attributes():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b

    instance = Class('bar', b=[], d=42)
    assert match_two(instance) == ('bar', [])
