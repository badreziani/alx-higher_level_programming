#!/usr/bin/python3
s = ""
for ascii_code in range(97, 123):
    s = f"{s}{chr(ascii_code)}"
print("{}".format(s), end="")
