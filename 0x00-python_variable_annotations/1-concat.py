#!/usr/bin/env python3
"""
Module that execute a type-annotated function concat
that takes a string str1 and a string str2 as arguments
and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """conctact two strings

    Args:
    str1 (string): fisrt string to be concatenated
    str2 (string): second string to be concatenated

    Return:
    contactenated strings
    """
    return str1 + str2
