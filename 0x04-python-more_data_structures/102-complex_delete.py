#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = [k for k in a_dictionary.keys() if a_dictionary.get(k) is value]
    for key in keys:
        del a_dictionary[key]
    return a_dictionary
