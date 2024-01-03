#!/usr/bin/python3
def uppercase(str):
    for up in str:
        temp = up
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(up) - 32)
        print("{}".format(temp), end="")
    print()
