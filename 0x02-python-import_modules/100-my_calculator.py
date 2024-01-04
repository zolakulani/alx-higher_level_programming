#!/usr/bin/python3
# Import necessary modules
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, mul, div, sub

    # Check the number of command-line arguments
    num_args = len(argv)

    if num_args != 4:
        # Print usage message and exit if incorrect number of arguments
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # Parse command-line arguments
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    # Perform calculation based on the operator
    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        # Handle unknown operator
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
