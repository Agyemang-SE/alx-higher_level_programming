#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    i = 0
    while a < x:
        try:
            print(my_list[a], end="")
            i += 1
        except IndexError:
            raise
        except:
            pass
        a += 1
    print("")
    return i
