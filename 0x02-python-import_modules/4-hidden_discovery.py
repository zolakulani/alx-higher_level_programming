#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    
    """ Import all names from the hidden_4 module """
    from hidden_4 import *

    """ Get all names defined in the current  scope"""
    all_names = dir()

    """Iterate through the names and print those not starting with "__" """
    for i in range(len(all_funx)):
        if all_names[i][:2] != "__":
            print("{:s}".format(all_names[i]))
