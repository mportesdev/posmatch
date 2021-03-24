import inspect


def auto_match_args(cls=None, /, *, force=False):

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
