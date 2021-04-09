Positional subpattern matching for custom classes.

**Note:** This is mostly a toy project. Using it will save you one line
of boiler-plate code at the cost of an additional decorator or argument.
In many cases, the problem this package solves can be more easily solved
using a dataclass.

Requirements
------------

Python 3.8 or higher.

**Note:** Although this package itself does not require Python 3.10,
its usage only makes sense with the new pattern matching feature
introduced in Python 3.10.

Installation
------------

.. code::

    pip install posmatch

Usage
-----

The ``pos_match`` decorator
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from posmatch import pos_match

    @pos_match
    class Color:

        def __init__(self, r, g, b):
            self.r = r
            self.g = g
            self.b = b


    color = Color(64, 64, 64)

    match color:
        case Color(r, g, b) if r == g == b:
            print('shade of grey')
        case _:
            print('other color')

Result:

.. code::

    shade of grey

The ``PosMatchMeta`` metaclass
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from posmatch import PosMatchMeta


    class Color(metaclass=PosMatchMeta):

        def __init__(self, r, g, b):
            self.r = r
            self.g = g
            self.b = b


    color = Color(0, 0, 64)

    match color:
        case Color(0, 0, b):
            print('shade of blue')
        case _:
            print('other color')

Result:

.. code::

    shade of blue

The ``PosMatchMixin`` mix-in class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from posmatch import PosMatchMixin


    class Color(PosMatchMixin):

        def __init__(self, r, g, b):
            super().__init__()
            self.r = r
            self.g = g
            self.b = b


    color = Color(255, 0, 0)

    match color:
        case Color(r, 0, 0):
            print('shade of red')
        case _:
            print('other color')

Result:

.. code::

    shade of red