r"""
cubing.py
===========
Provides a definition for the "cube" function. The function prototype should
be
    cube(x : type) -> type
Solution
--------
Do not modify the interface to `cube()`. This function can, however, call
other functions.
"""


def cube(x):
    """
    Return the cube of a `x`.
    Parameters
    ----------
    x : number
        Any numerical type that can be cubed.
    Returns
    -------
    value : number
        The square of `x`.
    """
    if type(x) != list:
        return x * x * x
    else:
        return [cube(a) for a in x]
