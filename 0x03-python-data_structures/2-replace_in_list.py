#!/usr/bin/python3 
def replace_in_list(my_list, idx, element):
    for inx in range(len(my_list)):
        if inx == idx:
            my_list[inx] = element
        if inx > idx:
            break
    return my_list
