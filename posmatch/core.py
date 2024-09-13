"""
Enable positional sub-pattern matching for objects of custom classes by
defining the `__match_args__` class attribute.

This module provides the following functions and classes:

    pos_match      -  class decorator defining the `__match_args__` class attribute
    PosMatchMeta   -  metaclass defining the `__match_args__` class attribute
    PosMatchMixin  -  mix-in class defining the `__match_args__` class attribute
"""

import inspect
from functools import partial


def pos_match(cls=None, /, *, force=False):
    """Class decorator defining the `__match_args__` class attribute.

    `__match_args__` will contain a sequence of names equal to
    parameter names in the signature of `cls.__init__` (not including
    `self`).

    If `cls` already has the `__match_args__` attribute (inherited or
    defined on its own) it will not be overwritten unless `force` is
    set to True.
    """
    if cls is None:
        # @pos_match() or @pos_match(force=True) usage
        return partial(pos_match, force=force)

    if not hasattr(cls, "__match_args__") or force:
        _set_match_args(cls)
    return cls


def _set_match_args(cls):
    cls.__match_args__ = _param_names_from_init(cls)


def _param_names_from_init(cls):
    init_params = inspect.signature(cls.__init__).parameters

    # exclude the first parameter (self)
    return tuple(init_params)[1:]


class PosMatchMeta(type):
    """Metaclass defining the `__match_args__` class attribute.

    `__match_args__` will contain a sequence of names equal to
    parameter names in the signature of the class' `__init__` method
    (not including `self`).

    If the class already has the `__match_args__` attribute (inherited
    or defined on its own) it will not be overwritten.
    """

    def __new__(mcs, *args):
        cls = super().__new__(mcs, *args)
        if not hasattr(cls, "__match_args__"):
            _set_match_args(cls)
        return cls


class _InitParamsGetter:
    def __get__(self, instance, owner):
        result = _param_names_from_init(owner)
        owner.__match_args__ = result
        return result


class PosMatchMixin:
    """Mix-in class defining the `__match_args__` class attribute.

    `__match_args__` will contain a sequence of names equal to
    parameter names in the signature of the class' `__init__` method
    (not including `self`).
    """

    __match_args__ = _InitParamsGetter()
