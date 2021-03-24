def match_first(obj):
    """Match `obj` using positional subpatterns. Python 3.10+ only."""
    cls = obj.__class__

    match obj:
        case cls(atr):
            return atr


def match_two(obj):
    """Match `obj` using positional subpatterns. Python 3.10+ only."""
    cls = obj.__class__

    match obj:
        case cls(a, b):
            return a, b
