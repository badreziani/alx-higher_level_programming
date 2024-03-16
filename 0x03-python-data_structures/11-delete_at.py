#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.
    """
    if len(my_list) > 0 and 0 <= idx < len(my_list):
        return [el for el in my_list if my_list.index(el) != idx]
    return my_list
