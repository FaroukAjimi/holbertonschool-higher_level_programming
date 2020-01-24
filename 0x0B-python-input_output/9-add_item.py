#!/usr/bin/python3
import json
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
my_list = []
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
for i in range(len(sys.argv)):
    if i == 0:
        continue
    my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
