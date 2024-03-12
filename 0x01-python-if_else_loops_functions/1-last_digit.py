#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = ""
sign = ""
if number < 0:
    sign = "-"
    number = -1 * number
last_digit = number % 10
if last_digit > 5 and sign != "-":
    s = "and is greater than 5"
elif last_digit == 0:
    s = "and is 0"
else:
    s = "and is less than 6 and not 0"
print(f"Last digit of {sign}{number:d} is {sign}{last_digit:d} {s:s}")
