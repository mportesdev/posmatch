"""
Enable positional subpattern matching for objects of custom classes.
"""

import inspect


def auto_match_args(cls=None, /, *, force=False):
    """Decorator to set `__match_args__` attribute to class `cls`.

    `__match_args__` will contain a sequence of names equal to
    parameter names in the signature of `cls.__init__`.

    If `cls` already has the `__match_args__` attribute (inherited or
    defined on its own) it will not be set, unless `force` is set to
    True.
    """
    def set_match_args(cls):
        init_params = inspect.signature(cls.__init__).parameters
        param_names = tuple(init_params.keys())

        # do not include the first parameter (self)
        setattr(cls, '__match_args__', param_names[1:])
        return cls

    if cls:
        # decorator used in the form @auto_match_args
        return cls if hasattr(cls, '__match_args__') else set_match_args(cls)

    if force:
        # decorator used in the form @auto_match_args(force=True)
        return set_match_args

    # @auto_match_args(), @auto_match_args(force=False) or equivalent
    # usage
    return auto_match_args
