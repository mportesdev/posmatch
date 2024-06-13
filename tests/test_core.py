class TestMatchArgsAttribute:
    def test_simple_class(self, simple_class):
        expected = ("a", "b")
        assert simple_class.__match_args__ == expected

        instance = simple_class(1, 2)
        assert instance.__match_args__ == expected

        # attribute must be defined on class, not instance
        assert "__match_args__" not in vars(instance)

    def test_multi_param_class(self, multi_param_class):
        expected = ("a", "b", "c", "d")
        assert multi_param_class.__match_args__ == expected

        instance = multi_param_class(1, 2, d=3)
        assert instance.__match_args__ == expected

        # attribute must be defined on class, not instance
        assert "__match_args__" not in vars(instance)

    def test_match_args_not_overridden_by_default(self, class_with_own_match_args):
        expected = ("x", "y")
        assert class_with_own_match_args.__match_args__ == expected

        instance = class_with_own_match_args(1, 2)
        assert instance.__match_args__ == expected

        # attribute must be defined on class, not instance
        assert "__match_args__" not in vars(instance)

    def test_inherited_match_args_not_overridden_by_default(
        self, class_with_inherited_match_args
    ):
        expected = ("a", "b")
        assert class_with_inherited_match_args.__match_args__ == expected

        instance = class_with_inherited_match_args(1, 2)
        assert instance.__match_args__ == expected

        # attribute must be defined on class, not instance
        assert "__match_args__" not in vars(instance)

    def test_match_args_overridden_optionally(self, class_with_force_true):
        expected = ("a", "b")
        assert class_with_force_true.__match_args__ == expected

        instance = class_with_force_true(1, 2)
        assert instance.__match_args__ == expected

        # attribute must be defined on class, not instance
        assert "__match_args__" not in vars(instance)

    def test_mixin_first(self, mixin_first):
        expected = ("x", "y")
        assert mixin_first.__match_args__ == expected

        instance = mixin_first(1, 2)
        assert instance.__match_args__ == expected

        # attribute must be defined on class, not instance
        assert "__match_args__" not in vars(instance)

    def test_mixin_last(self, mixin_last):
        expected = ("a", "b")
        assert mixin_last.__match_args__ == expected

        instance = mixin_last(1, 2)
        assert instance.__match_args__ == expected

        # attribute must be defined on class, not instance
        assert "__match_args__" not in vars(instance)

    def test_repeated_access_to_mixin_getter(self, mixin_first):
        expected = ("x", "y")
        assert mixin_first.__match_args__ == expected

        instance = mixin_first(1, 2)
        assert instance.__match_args__ == expected

        assert mixin_first.__match_args__ == expected
        assert instance.__match_args__ == expected
