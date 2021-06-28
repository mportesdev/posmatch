class TestPatternMatching:

    def test_simple_class(self, simple_class):
        instance = simple_class(1, 2)

        match instance:
            case simple_class(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (1, 2)

    def test_six_pack_class(self, six_pack_class):
        instance = six_pack_class(1, 2, 3, d=4)

        match instance:
            case six_pack_class(atr_1, atr_2, atr_3, atr_4, atr_5, atr_6):
                result = atr_1, atr_2, atr_3, atr_4, atr_5, atr_6
            case _:
                result = None

        assert result == (1, 2, (3,), 4, None, {})


class TestPatternMatchingWithLessSubPatterns:

    def test_simple_class(self, simple_class):
        instance = simple_class(0, 1)

        match instance:
            case simple_class(atr):
                result = atr
            case _:
                result = None

        assert result == 0

    def test_six_pack_class(self, six_pack_class):
        instance = six_pack_class(0, 1, d=2)

        match instance:
            case six_pack_class(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (0, 1)
