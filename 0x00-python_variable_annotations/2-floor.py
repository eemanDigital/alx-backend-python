#!usr/bin/env python3
"""
Module that execute type-annotated function floor which takes
a float n as argument and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """ execute a floor program on a float arg

    Args:
    n (float): input float number to be floored
    Return:
    int: value of the floored float arg
    """
    return math.floor(n)