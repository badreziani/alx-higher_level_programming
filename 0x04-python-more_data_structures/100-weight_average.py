#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average
    of all integers tuple (<score>, <weight>)
    """
    if not my_list:
        return 0
    return sum([x * y for x, y in my_list])/sum([y for x, y in my_list])
