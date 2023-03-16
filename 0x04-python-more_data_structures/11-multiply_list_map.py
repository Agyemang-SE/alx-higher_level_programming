#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    dup_list = my_list.copy()
    dup_list = list(map((lambda x: x * number), my_list))
    return dup_list
