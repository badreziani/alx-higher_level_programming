#!/usr/bin/python3
s = ""
for n in range(97, 123):
    if n % 2 != 0:
        s = f"{s}{chr(n - 32)}"
    else:
        s = f"{s}{chr(n)}"
s = s[::-1]
print(s)

