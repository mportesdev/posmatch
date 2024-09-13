import pytest

from posmatch.core import _set_match_args, _param_names_from_init, _InitParamsGetter


@pytest.fixture
def minimal_class():
    class _Cls:
        def __init__(self, p, q):
            self.p = p
            self.q = q

    return _Cls


def test_set_match_args(minimal_class):
    _set_match_args(minimal_class)
    assert minimal_class.__match_args__ == ("p", "q")


def test_param_names_from_init(minimal_class):
    assert _param_names_from_init(minimal_class) == ("p", "q")


def test_attribute_getter(minimal_class):
    minimal_class.attr = _InitParamsGetter()
    assert minimal_class.attr == ("p", "q")
