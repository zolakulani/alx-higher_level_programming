#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum of all arguments."""
    from sys import argv
    
    totalint = 0
    for i in range(len(argv) - 1):
        totalint += int(argv[i + 1])
    print("{}".format(totalint))
