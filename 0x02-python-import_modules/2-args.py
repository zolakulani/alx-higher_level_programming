#!/usr/bin/python3

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Import the argv list from the sys module
    from sys import argv

    # Calculate the number of arguments
    x = len(argv) - 1

    # Check the number of arguments and print accordingly
    if x < 1:
        print("{} arguments:".format(x))
    elif x == 1:
        print("{} argument.".format(x))
    else:
        print("{} arguments:".format(x))

    # Print the position and value of each argument
    for i in range(x):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
