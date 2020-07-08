r"""
squaring.py
===========
Provides a definition for the "square" function. The function prototype should
be
    square(x : type) -> type
Solution
--------
Do not modify the interface to `square()`. This function can, however, call
other functions.
"""


def square(x):
    """
    Return the square of a `x`.
    Parameters
    ----------
    x : number
        Any numerical type that can be squared.
    Returns
    -------
    value : number
        The square of `x`.
    """
    if type(x) != list:
        return x * x
    else:
        return [square(a) for a in x]
