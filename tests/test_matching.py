def test_class_1_first_attribute(decorated_class_1):
    """Test `pos_match` decorator."""

    instance = decorated_class_1(0, 1)

    # match instance using positional subpatterns
    match instance:
        case decorated_class_1(atr):
            result = atr

    assert result == 0


def test_class_1_all_attributes(decorated_class_1):
    """Test `pos_match` decorator."""

    instance = decorated_class_1(42, 62)

    # match instance using positional subpatterns
    match instance:
        case decorated_class_1(atr_1, atr_2):
            result = atr_1, atr_2

    assert result == (42, 62)


def test_class_2_first_attribute(decorated_class_2):
    """Test `pos_match` decorator."""

    instance = decorated_class_2(0, 1, d=2)

    # match instance using positional subpatterns
    match instance:
        case decorated_class_2(atr):
            result = atr

    assert result == 0


def test_class_2_all_attributes(decorated_class_2):
    """Test `pos_match` decorator."""

    instance = decorated_class_2(10, 11, 12, d=42, x=62)

    # match instance using positional subpatterns
    match instance:
        case decorated_class_2(atr_1, atr_2, atr_3, atr_4, atr_5, atr_6):
            result = atr_1, atr_2, atr_3, atr_4, atr_5, atr_6

    assert result == (10, 11, (12,), 42, None, {'x': 62})
