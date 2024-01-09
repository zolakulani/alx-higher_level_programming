#!/usr/bin/python3
"""
    Prints the integers in a given list in reverse order.

    Parameters:
        my_list (list): The list of integers to be printed in reverse order.

    Returns:
        None
"""
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
            