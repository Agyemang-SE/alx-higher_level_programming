#!/usr/bin/python3
number = 97
while number < 123:
    if (number != 101 and number != 113):
        print("{:s}".format(chr(number)), end='')
    number += 1
