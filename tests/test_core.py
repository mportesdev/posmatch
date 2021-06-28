from posmatch import pos_match


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

    def test_force_overwrite_existing_match_args(self):
        @pos_match(force=True)
        class Class:
            def __init__(self, a, b):
                ...

            __match_args__ = ('x', 'y')

        expected = ('a', 'b')
        assert Class.__match_args__ == expected

        instance = Class(1, 2)
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_inherited_match_args_not_overridden(self, class_with_inherited):
        expected = ('a', 'b', 'c')
        assert class_with_inherited.__match_args__ == expected

        instance = class_with_inherited(1, 2)
        assert instance.__match_args__ == expected

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__

    def test_force_override_inherited_match_args(self):
        class BaseClass:
            def __init__(self, a, b):
                ...

            __match_args__ = ('a', 'b', 'c')

        @pos_match(force=True)
        class SubClass(BaseClass):
            def __init__(self, x, y):
                super().__init__(x, y)

        expected = ('x', 'y')
        assert SubClass.__match_args__ == expected

        instance = SubClass(1, 2)
        assert instance.__match_args__ == expected
        assert SubClass.__base__.__match_args__ == ('a', 'b', 'c')

        # attribute must not be defined on instance itself
        assert '__match_args__' not in instance.__dict__
