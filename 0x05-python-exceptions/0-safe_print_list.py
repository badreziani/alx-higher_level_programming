#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""
    try:
        for index in range(x):
            print(my_list[index], end="")
        print()
    except Exception:
        index += -1
        print()
    return index + 1
