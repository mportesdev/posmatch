import pytest


class TestPosMatch:
    """Test the `pos_match` decorator."""

    def test_class_1(self, decorated_class_1):
        instance = decorated_class_1(42, 62)

        match instance:
            case decorated_class_1(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (42, 62)

    def test_class_1_less_attributes(self, decorated_class_1):
        instance = decorated_class_1(0, 1)

        match instance:
            case decorated_class_1(atr):
                result = atr
            case _:
                result = None

        assert result == 0

    def test_class_2(self, decorated_class_2):
        instance = decorated_class_2(10, 11, 12, d=42, x=62)

        match instance:
            case decorated_class_2(a_1, a_2, a_3, a_4, a_5, a_6):
                result = a_1, a_2, a_3, a_4, a_5, a_6
            case _:
                result = None

        assert result == (10, 11, (12,), 42, None, {'x': 62})

    def test_class_2_less_attributes(self, decorated_class_2):
        instance = decorated_class_2(0, 1, d=2)

        match instance:
            case decorated_class_2(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (0, 1)


class TestPosMatchMeta:
    """Test the `PosMatchMeta` metaclass."""

    def test_class_1(self, class_from_metaclass_1):
        instance = class_from_metaclass_1(42, 62)

        match instance:
            case class_from_metaclass_1(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (42, 62)

    def test_class_1_less_attributes(self, class_from_metaclass_1):
        instance = class_from_metaclass_1(0, 1)

        match instance:
            case class_from_metaclass_1(atr):
                result = atr
            case _:
                result = None

        assert result == 0

    def test_class_2(self, class_from_metaclass_2):
        instance = class_from_metaclass_2(10, 11, 12, d=42, x=62)

        match instance:
            case class_from_metaclass_2(a_1, a_2, a_3, a_4, a_5, a_6):
                result = a_1, a_2, a_3, a_4, a_5, a_6
            case _:
                result = None

        assert result == (10, 11, (12,), 42, None, {'x': 62})

    def test_class_2_less_attributes(self, class_from_metaclass_2):
        instance = class_from_metaclass_2(0, 1, d=2)

        match instance:
            case class_from_metaclass_2(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (0, 1)


class TestRegularClass:
    """Test positional matching of undecorated class."""

    def test_class_1_raises_error(self, class_1):
        instance = class_1(0, 1)

        with pytest.raises(TypeError):
            match instance:
                case class_1(atr_1, atr_2):
                    result = atr_1, atr_2
                case _:
                    result = None
