#!/usr/bin/python3

# Check if the script is being run as the main program
if __name__ == "__main__":
    """Print the sum of all arguments."""

    # Import the argv list from the sys module
    from sys import argv

    # Initialize a variable to store the sum of integers
    totalint = 0

    # Iterate through the arguments starting from index 1
    for i in range(1, len(argv)):
        # Convert each argument to an integer and add to totalint
        totalint += int(argv[i])

    # Print the total sum of integers
    print("{}".format(totalint))
