#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    reminder = -number % 10
    reminder = -reminder
else:
    reminder = number % 10

if (reminder > 5):
    print(f'Last digit of {number} is {reminder} and is greater than 5')
elif (reminder > 0 and reminder < 6):
    print(f'Last digit of {number} is {reminder} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {reminder} and is 0')
