#!/usr/bin/python3
"""Check if the script is being run as the main program"""
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    """Import the argv list from the sys module"""
    from sys import argv

    """Calculate the number of arguments"""
    count = len(argv) - 1
    """Check the number of arguments and print accordingly"""
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))
    """Print the position and value of each argument"""
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i + 1]))
