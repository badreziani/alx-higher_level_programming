#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    the_int = 0
    for r in roman_string:
        the_int += int(roman.get(r))
    return the_int
