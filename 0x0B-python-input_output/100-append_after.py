#!/usr/bin/python3
"""
100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    after each line containing a specific string
    """

    with open(filename) as f:
        lines = r_file.readlines()

    with open(filename, mode="w") as f:
        new_text = ""
        for line in lines:
            s += line
            if search_string in line:
                s += "\n{}".format(new_string)
        f.write(new_text)
