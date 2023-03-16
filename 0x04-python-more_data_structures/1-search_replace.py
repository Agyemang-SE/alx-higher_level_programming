#!/usr/bin/python3
def search_replace(my_list, search, replace):
    d_list = my_list.copy()
    for i in range(len(my_list)):
        d_list[i] = replace if my_list[i] == search else my_list[i]
    return d_list
