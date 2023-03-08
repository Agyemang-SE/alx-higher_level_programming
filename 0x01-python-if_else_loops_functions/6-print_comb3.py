#!/usr/bin/python3
num1 = 0
num2 = 1
while num1 <= 8:
    while num2 <= 9:
        if num1 != num2:
            print("{:d}".format(num1), end='')
            if num1 != 8:
                print("{:d}, ".format(num2), end='')
            else:
                print('{:d}'.format(num2))
        num2 += 1
    num2 = num1 + 1
    num1 = num1 + 1
