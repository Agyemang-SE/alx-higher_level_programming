#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    list_uq = list(set(my_list))
    for i in range(len(list_uq)):
        sum += list_uq[i]
    return sum
