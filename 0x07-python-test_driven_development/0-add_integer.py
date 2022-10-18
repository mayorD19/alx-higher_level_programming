#!/usr/bin/python3
"""Create a function that adds two integers"""



def add_integer(a, b=98):
    """A function that adds two integers together, 
    and converts them when they are in the float type
    raise:
        TypeError: if a or b is not in the integer format
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
