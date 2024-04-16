#!/usr/bin/python3
"""
7-add_item.py
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []

try:
    load_from_json_file("add_item.json")
    argv = sys.argv
    if len(argv) > 1:
        for arg in argv[1:]:
            my_list.append(arg)
    save_to_json_file(my_list, "add_item.json")
except Exception:
    save_to_json_file(my_list, "add_item.json")
