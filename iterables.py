"""Iterable elements functions library"""

from collections.abc import Iterable

def flatten_list(list):
    """
    :param list: Nested list to flatten
    :return: List - Flattens given list and remove empty elements
    """
    flattened = []

    for i in iterable:
        if isinstance(i, Iterable):
            flattened = flattened + flatten(i)
        elif i != None:
            flattened.append(i)

    return flattened
