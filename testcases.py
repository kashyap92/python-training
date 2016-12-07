#!/usr/bin/python
def average(values):
        """Computes the arithmetic mean of a list of
        numbers.
        >>> print average([20, 30, 70])
        40.0
        >>> print average([20, 30, 70])
        410.0
        >>> print average([20, 30, 70, 40])
        40.0
        >>> print average([20.5, 30.5, 70.5, 40])
        40.0
        """
        return sum(values,0.0) / len(values)

import doctest
doctest.testmod()
