#!/usr/bin/python3
for n in range(9):
    for m in range(n, 10):
        if n != m:
            print("{0}{1}".format(n, m), end="")
            if n == 8 and m == 9:
                print(end="\n")
            else:
                print(", ", end="")
