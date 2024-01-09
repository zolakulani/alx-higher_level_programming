#!/usr/bin/python3
"""
Replaces an element at a specific index in a list.

Parameters:
my_list (list): The list in which the element should be replaced.
idx (int): The index of the element to be replaced.
element: The element to replace the existing element at the specified index.

Returns:
list: The modified list with the element replaced at the specified index.
"""
def replace_in_list(my_list, idx, element):
    for inx in range(len(my_list)):
        if inx == idx:
            my_list[inx] = element
        if inx > idx:
            break
    return my_list
              