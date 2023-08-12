#!/usr/bin/env python3
"""
Module that executea a type-annotated function
sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Returns the sum of a list of integers and
    floating-point numbers.

    Args:
    mxd_lst (List[Union[int, float]]): The list of mixed
    integers and floating-point numbers.

    Returns:
    float: The sum of the input list of mixed
    integers and floating-point numbers.
    """
    return sum(mxd_lst)
