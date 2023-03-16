#!/usr/python3
def multiply_by_2(a_dictionary):
    dup_dictionary = a_dictionary.copy()
    dup_dictionary = {key: value * 2 for key , value in a_dictionary.items()}
    return dup_dictionary
