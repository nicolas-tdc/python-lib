"""Numerics functions library"""

def is_leap_year(year):
    """
    :param year: Int
    :return: Bool - True if year is a leap year
    """
    if ( year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
        return True
    else:
        return False


import math

def prime_factors(value):
    """
    :param value: Int
    :return: List - Prime factors of given value
    """
    prime_factors = []
    while value % 2 == 0:
        value = update_list_and_value(value, 2, prime_factors)

    value_sqrt = int(math.sqrt(value)) + 1
    for odd in range(3, value_sqrt):
        while value % odd == 0:

            value = update_list_and_value(value, odd, prime_factors)
    if value != 1:
        prime_factors.append(value)

    return prime_factors
