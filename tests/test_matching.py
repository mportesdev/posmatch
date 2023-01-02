class TestFullMatch:
    def test_simple_class(self, simple_class):
        instance = simple_class(1, 2)

        match instance:
            case simple_class(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (1, 2)

    def test_multi_param_class(self, multi_param_class):
        instance = multi_param_class(1, 2, 3, d=4)

        match instance:
            case multi_param_class(atr_1, atr_2, atr_3, atr_4, atr_5, atr_6):
                result = atr_1, atr_2, atr_3, atr_4, atr_5, atr_6
            case _:
                result = None

        assert result == (1, 2, (3,), 4, None, {})

    def test_match_args_not_overridden_by_default(self, class_with_own_match_args):
        instance = class_with_own_match_args(1, 2)

        match instance:
            case class_with_own_match_args(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (43, 44)

    def test_inherited_match_args_not_overridden_by_default(
        self, class_with_inherited_match_args
    ):
        instance = class_with_inherited_match_args(1, 2)

        match instance:
            case class_with_inherited_match_args(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (1, 2)

    def test_match_args_overridden_optionally(self, class_with_force_true):
        instance = class_with_force_true(1, 2)

        match instance:
            case class_with_force_true(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (1, 2)

    def test_mixin_first(self, mixin_first):
        instance = mixin_first(1, 2)

        match instance:
            case mixin_first(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (43, 44)

    def test_mixin_last(self, mixin_last):
        instance = mixin_last(1, 2)

        match instance:
            case mixin_last(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (1, 2)

    def test_repeated_access_to_class_property_of_mixin(self, mixin_first):
        instance = mixin_first(1, 2)

        match instance:
            case mixin_first(atr_1, atr_2):
                result_1 = atr_1, atr_2
            case _:
                result_1 = None

        match instance:
            case mixin_first(i, j):
                result_2 = i, j
            case _:
                result_2 = None

        assert result_1 == result_2 == (43, 44)


class TestPartialMatch:
    def test_simple_class(self, simple_class):
        instance = simple_class(0, 1)

        match instance:
            case simple_class(atr):
                result = atr
            case _:
                result = None

        assert result == 0

    def test_multi_param_class(self, multi_param_class):
        instance = multi_param_class(0, 1, d=2)

        match instance:
            case multi_param_class(atr_1, atr_2):
                result = atr_1, atr_2
            case _:
                result = None

        assert result == (0, 1)

    def test_mixin_first(self, mixin_first):
        instance = mixin_first(1, 2)

        match instance:
            case mixin_first(atr):
                result = atr
            case _:
                result = None

        assert result == 43

    def test_mixin_last(self, mixin_last):
        instance = mixin_last(1, 2)

        match instance:
            case mixin_last(atr):
                result = atr
            case _:
                result = None

        assert result == 1
