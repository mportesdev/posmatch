========
posmatch
========

Positional sub-pattern matching for custom classes.

Requirements
============

Python 3.8 or higher.

**Note:** Although this package can be installed and used in
Python 3.8+, its usage only makes sense with the pattern matching
feature introduced in Python 3.10. All code snippets below require
Python 3.10+.

Installation
============

.. code::

    pip install posmatch

Usage
=====

The ``pos_match`` decorator
---------------------------

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
        case Color(0, 0, b):
            print('Shade of blue')
        case Color(r, g, b) if r == g == b:
            print('Shade of grey')
        case _:
            print('Other color')

Output:

.. code::

    Shade of grey

The ``PosMatchMeta`` metaclass
------------------------------

.. code-block:: python

    from posmatch import PosMatchMeta

    class Date(metaclass=PosMatchMeta):

        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

    date = Date(2968, 5, 5)

    match date:
        case Date(_, month, day) if month == 5 and day == 1:
            print('May Day')
        case Date(year) if year > 2100:
            print('Distant future')
        case _:
            print('Other')

Output:

.. code::

    Distant future
