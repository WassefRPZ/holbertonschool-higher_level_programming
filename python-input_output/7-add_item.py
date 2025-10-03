#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

"""Script qui ajoute les arguments passés en ligne de commande
dans une liste, et sauvegarde cette liste dans un fichier JSON.
"""

try:
    item = load_from_json_file(filename)
except Exception:
    item = []

item.extend(sys.argv[1:])
save_to_json_file(item, filename)
