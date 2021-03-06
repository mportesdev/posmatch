class TestMatchArgsAttribute:

    def test_simple_class(self, simple_class):
        expected = ('a', 'b')
        assert simple_class.__match_args__ == expected

        instance = simple_class(1, 2)
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_six_pack_class(self, six_pack_class):
        expected = ('a', 'b', 'c', 'd', 'e', 'f')
        assert six_pack_class.__match_args__ == expected

        instance = six_pack_class(1, 2, 3, d=4)
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_existing_match_args_not_overwritten(self, class_with_attr):
        expected = ('x', 'y')
        assert class_with_attr.__match_args__ == expected

        instance = class_with_attr(1, 2)
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_inherited_match_args_not_overridden(self, class_with_inherited):
        expected = ('a', 'b')
        assert class_with_inherited.__match_args__ == expected

        instance = class_with_inherited(1, 2)
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_force_override_existing_match_args(self, forced_class):
        expected = ('a', 'b')
        assert forced_class.__match_args__ == expected

        instance = forced_class(1, 2)
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_data_class(self, data_class):
        """Test that a decorated dataclass works both in Python <3.10
        and >=3.10.
        """
        expected = ('a', 'b', 'c')
        assert data_class.__match_args__ == expected

        instance = data_class(1, False, 'X')
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_mixin_first(self, mixin_first):
        expected = ('x', 'y')
        assert mixin_first.__match_args__ == expected

        instance = mixin_first(1, 2)
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_mixin_last(self, mixin_last):
        expected = ('a', 'b')
        assert mixin_last.__match_args__ == expected

        instance = mixin_last(1, 2)
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_repeated_access_to_class_property_of_mixin(self, mixin_first):
        expected = ('x', 'y')
        assert mixin_first.__match_args__ == expected

        instance = mixin_first(1, 2)
        assert instance.__match_args__ == expected

        assert mixin_first.__match_args__ == expected
        assert instance.__match_args__ == expected
