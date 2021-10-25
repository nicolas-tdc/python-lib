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


def compare_lists(list_one, list_two):
    """
    :param list_one: List
    :param list_two: List
    :return: String - Status of list one compared to list two.
    This function requires the function is_sublist(list_one, list_two)
    """
    if list_one == list_two:
        return 'equal'
    elif (not list_one and list_two) or is_sublist(list_one, list_two):
        return 'sublist'
    elif (list_one and not list_two) or is_sublist(list_two, list_one):
        return 'superlist'
    else:
        return 'unequal'

def is_sublist(list_one, list_two):
    """
    :param list_one: list
    :param list_two: list
    :return: string - Sublist category
    """
    is_sublist = False
    if list_one[0] in list_two:

        superitems_indexes = [i for i, x in enumerate(list_two) if x == list_one[0]]
        for superitem_index in superitems_indexes:
            for index_one, item in enumerate(list_one):

                index_two = index_one + superitem_index
                if index_two < len(list_two):

                    if item == list_two[index_two]:
                        is_sublist = True
                    else:
                        is_sublist = False
                        break

                else:
                    is_sublist = False
                    break

            if is_sublist == True:
                break

    return is_sublist
