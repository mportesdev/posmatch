class TestPosMatch:
    """Test the `pos_match` decorator."""

    def test_class_1_first_attribute(self, decorated_class_1):
        instance = decorated_class_1(0, 1)

        match instance:
            case decorated_class_1(atr):
                result = atr
            case _:
                result = None

        assert result == 0


    def test_class_1_all_attributes(self, decorated_class_1):
        instance = decorated_class_1(42, 62)

        match instance:
            case decorated_class_1(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (42, 62)


    def test_class_2_first_attribute(self, decorated_class_2):
        instance = decorated_class_2(0, 1, d=2)

        match instance:
            case decorated_class_2(atr):
                result = atr
            case _:
                result = None

        assert result == 0


    def test_class_2_all_attributes(self, decorated_class_2):
        instance = decorated_class_2(10, 11, 12, d=42, x=62)

        match instance:
            case decorated_class_2(atr_1, atr_2, atr_3, atr_4, atr_5, atr_6):
                result = atr_1, atr_2, atr_3, atr_4, atr_5, atr_6
            case _:
                result = None

        assert result == (10, 11, (12,), 42, None, {'x': 62})


class TestPosMatchMeta:
    """Test the `PosMatchMeta` metaclass."""

    def test_class_1_first_attribute(self, class_from_metaclass_1):
        instance = class_from_metaclass_1(0, 1)

        match instance:
            case class_from_metaclass_1(atr):
                result = atr
            case _:
                result = None

        assert result == 0


    def test_class_1_all_attributes(self, class_from_metaclass_1):
        instance = class_from_metaclass_1(42, 62)

        match instance:
            case class_from_metaclass_1(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (42, 62)

    def test_class_2_first_attribute(self, class_from_metaclass_2):
        instance = class_from_metaclass_2(0, 1, d=2)

        match instance:
            case class_from_metaclass_2(atr):
                result = atr
            case _:
                result = None

        assert result == 0


    def test_class_2_all_attributes(self, class_from_metaclass_2):
        instance = class_from_metaclass_2(10, 11, 12, d=42, x=62)

        match instance:
            case class_from_metaclass_2(atr_1, atr_2, atr_3, atr_4, atr_5, atr_6):
                result = atr_1, atr_2, atr_3, atr_4, atr_5, atr_6
            case _:
                result = None

        assert result == (10, 11, (12,), 42, None, {'x': 62})
