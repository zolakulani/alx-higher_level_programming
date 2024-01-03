#!/usr/bin/python3
for doest in range(0, 10):
    for second in range(doest + 1, 10):
        if doest == 8 and second == 9:
            print("{}{}".format(doest, second))
        else:
            print("{}{}".format(doest, second), end=", ")
