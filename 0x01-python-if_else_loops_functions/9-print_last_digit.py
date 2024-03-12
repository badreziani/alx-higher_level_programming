#!/usr/bin/python3
def print_last_digit(number):
    sign = ""
    if number < 0:
        number = -1 * number
        sign = "-"
    print("{0}{1}".format(sign, number % 10), end="")
