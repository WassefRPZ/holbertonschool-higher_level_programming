#!/usr/bin/python3
"""
module qui ajoute des arguments à une liste et sauvegarde

"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
args = sys.argv[1:]
try:
    existing_list = load_from_json_file("add_item.json")
except Exception:
    existing_list = []
existing_list.extend(args)
save_to_json_file(existing_list, "add_item.json")
