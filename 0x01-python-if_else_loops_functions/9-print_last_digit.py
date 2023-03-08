#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    reminder = number % 10
    print("{:d}".format(reminder), end='')
    return (reminder)
