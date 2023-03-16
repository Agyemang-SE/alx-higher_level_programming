#!/usr/bin/python3
from functools import reduce
import random


def mult_by_2(num):
    return num * 2


times_two = mult_by_2
print("4 * 2 =", times_two(4))


def mult_by_2(num):
    return num * 2


def do_math(func, num):
    return func(num)


print("8 * 2 =", do_math(mult_by_2, 8))


def get_func_mult_by_num(num):
    def mult_by(value):
       return num * value
    return mult_by


generated_func = get_func_mult_by_num(5)
print("5 * 10 =", generated_func(10))

listofFuncs = [times_two, generated_func]
print("5 * 9 =", listofFuncs[1](9))


def check_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def odd_list(list, func):
    oddlist = []
    for i in list:
        if func(i):
            oddlist.append(i)
    return oddlist


alist = range(1, 20)
print(odd_list(alist, check_odd))


def random_func(name: str, age: int, weight: float) -> str:
    print("Name:", name)
    print("Age:", age)
    print("Weight:", weight)

    return "{} is {} years ols and weighs {} kg".format(name, age, weight)


print(random_func("Derek", 41, 165.6))
print(random_func.__annotations__)

#Anonymous functions

#lambda
#lambda arg1, arg2 ....: expressions
def sum(x, y): return x + y


print("Sum :", sum(4, 5))


def can_vote(age): return True if age >= 18 else False


print("Can Vote :", can_vote(19))

powerList = [lambda x: x**2,
             lambda x: x**3,
             lambda x: x**4]

for func in powerList:
    print(func(4))

attack = {'quick': (lambda: print("Quick Attack")),
          'power': (lambda: print("Power Attack")),
          'miss': (lambda: print("Missed Attack"))}
attack['quick']()

attackkey = random.choice(list(attack.keys()))
attack[attackkey]()

blist = []

for i in range(1, 101):
    blist += random.choice(['H', 'T'])
print("Heads :", blist.count('H'))
print("Tails :", blist.count('T'))

#map
oneTo10 = range(1, 11)


def dbl_num(num):
    return num * 2


print(list(map(dbl_num, oneTo10)))
print(list(map((lambda x: x * 3), oneTo10)))
clist = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(clist)

#filter
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))
randlist = list(random.randint(1, 1001) for i in range(100))
print(list(filter((lambda x: x % 9 == 0), randlist)))

#reduce
print(reduce((lambda x, y: x + y), range(1, 6)))
