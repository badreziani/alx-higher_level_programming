#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers."""

    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
        except (ValueError, TypeError):
            index += -1
    print()
    return index + 1
