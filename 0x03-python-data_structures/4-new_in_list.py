#!/usr/bin/python3
"""
    Replaces the element at the specified index in a given list with a new element.

    Parameters:
        - my_list (list): The original list.
        - idx (int): The index at which the element needs to be replaced.
        - element: The new element to be inserted at the specified index.

    Returns:
        list: A new list with the element at the specified index replaced. If the index is out of range, the original list is returned.
"""
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
