#!/usr/bin/env python3
"""
Module that execute type-annotated function sum_list
which take a list input_list of floats as argument
and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns the sum of input list

    Arg:
    input_list (floats): input list of floating numbers
    Return:
    float: the sum of the list of input
    """
    return sum(input_list)
