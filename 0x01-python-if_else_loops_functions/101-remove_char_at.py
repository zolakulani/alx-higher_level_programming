#!/usr/bin/python3
def remove_char_at(str, n):
    count = ''
    i = 0
    for c in str:
        if i != n:
            count += str[i]
        i += 1
        return (count)
