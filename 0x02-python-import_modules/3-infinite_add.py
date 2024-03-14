#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    numbers = sys.args[1:]
    sum = 0
    for number in numbers:
        sum += int(number)
    print(sum)
