#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        keys = sorted(list(a_dictionary.keys()))
    for key in keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
