import pytest


class TestFullMatch:
    def test_simple_class(self, simple_class):
        instance = simple_class(1, 2)

        match instance:
            case simple_class(atr_1, atr_2):
                assert (atr_1, atr_2) == (1, 2)
            case _:
                pytest.fail("Instance did not match pattern")

    def test_multi_param_class(self, multi_param_class):
        instance = multi_param_class(1, 2, d=3)

        match instance:
            case multi_param_class(atr_1, atr_2, atr_3, atr_4):
                assert (atr_1, atr_2, atr_3, atr_4) == (1, 2, None, 3)
            case _:
                pytest.fail("Instance did not match pattern")

    def test_match_args_not_overridden_by_default(self, class_with_own_match_args):
        instance = class_with_own_match_args(1, 2)

        match instance:
            case class_with_own_match_args(atr_1, atr_2):
                assert (atr_1, atr_2) == (43, 44)
            case _:
                pytest.fail("Instance did not match pattern")

    def test_inherited_match_args_not_overridden_by_default(
        self, class_with_inherited_match_args
    ):
        instance = class_with_inherited_match_args(1, 2)

        match instance:
            case class_with_inherited_match_args(atr_1, atr_2):
                assert (atr_1, atr_2) == (1, 2)
            case _:
                pytest.fail("Instance did not match pattern")

    def test_match_args_overridden_optionally(self, class_with_force_true):
        instance = class_with_force_true(1, 2)

        match instance:
            case class_with_force_true(atr_1, atr_2):
                assert (atr_1, atr_2) == (1, 2)
            case _:
                pytest.fail("Instance did not match pattern")

    def test_mixin_first(self, mixin_first):
        instance = mixin_first(1, 2)

        match instance:
            case mixin_first(atr_1, atr_2):
                assert (atr_1, atr_2) == (43, 44)
            case _:
                pytest.fail("Instance did not match pattern")

    def test_mixin_last(self, mixin_last):
        instance = mixin_last(1, 2)

        match instance:
            case mixin_last(atr_1, atr_2):
                assert (atr_1, atr_2) == (1, 2)
            case _:
                pytest.fail("Instance did not match pattern")

    def test_repeated_access_to_class_property_of_mixin(self, mixin_first):
        instance = mixin_first(1, 2)

        match instance:
            case mixin_first(atr_1, atr_2):
                assert (atr_1, atr_2) == (43, 44)
            case _:
                pytest.fail("Instance did not match pattern")

        match instance:
            case mixin_first(i, j):
                assert (i, j) == (43, 44)
            case _:
                pytest.fail("Instance did not match pattern")


class TestPartialMatch:
    def test_simple_class(self, simple_class):
        instance = simple_class(0, 1)

        match instance:
            case simple_class(atr):
                assert atr == 0
            case _:
                pytest.fail("Instance did not match pattern")

    def test_multi_param_class(self, multi_param_class):
        instance = multi_param_class(0, 1, d=2)

        match instance:
            case multi_param_class(atr_1, atr_2):
                assert (atr_1, atr_2) == (0, 1)
            case _:
                pytest.fail("Instance did not match pattern")

    def test_mixin_first(self, mixin_first):
        instance = mixin_first(1, 2)

        match instance:
            case mixin_first(atr):
                assert atr == 43
            case _:
                pytest.fail("Instance did not match pattern")

    def test_mixin_last(self, mixin_last):
        instance = mixin_last(1, 2)

        match instance:
            case mixin_last(atr):
                assert atr == 1
            case _:
                pytest.fail("Instance did not match pattern")
