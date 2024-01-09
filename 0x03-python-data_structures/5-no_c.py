#!/usr/bin/python3
"""
    Removes all occurrences of the letter 'c' (case insensitive) from the given string.

    Parameters:
        my_string (str): The input string from which the letter 'c' and 'C' will be removed.

    Returns:
        str: The resulting string after removing all occurrences of the letter 'c' and 'C'.
"""
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string