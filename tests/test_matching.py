from posmatch import pos_match


def test_simple_class_pattern_matching_one_attribute():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    instance = Class(1, 2)

    # match instance using positional subpatterns
    match instance:
        case Class(atr):
            result = atr

    assert result == 1


def test_simple_class_pattern_matching_two_attributes():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    instance = Class(x='foo', y=42)

    # match instance using positional subpatterns
    match instance:
        case Class(atr_1, atr_2):
            result = atr_1, atr_2

    assert result == ('foo', 42)


def test_pattern_matching_one_attribute():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b

    instance = Class(1, 2, d=3)

    # match instance using positional subpatterns
    match instance:
        case Class(atr):
            result = atr

    assert result == 1


def test_pattern_matching_two_attributes():
    """Test `pos_match` decorator."""

    @pos_match
    class Class:
        def __init__(self, a, /, b, *c, d, e=None, **f):
            self.a = a
            self.b = b

    instance = Class('bar', b=[], d=42)

    # match instance using positional subpatterns
    match instance:
        case Class(atr_1, atr_2):
            result = atr_1, atr_2

    assert result == ('bar', [])
