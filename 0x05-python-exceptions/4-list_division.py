#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    a  = 0
    while a < list_length:
        try:
            c = my_list_1[a] / my_list_2[a]
        except TypeError:
            c = 0
            print("wrong type")
        except ZeroDivisionError:
            c = 0
            print("division by 0")
        except IndexError:
            c = 0
            print("out of range")
        finally:
            new_list.append(c)
        a += 1
    return new_list
