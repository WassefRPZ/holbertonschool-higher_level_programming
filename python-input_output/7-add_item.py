#!/usr/bin/python3
"""
Script qui ajoute les arguments passés en ligne de commande
dans une liste, et sauvegarde cette liste dans un fichier JSON.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if __name__ == "__main__":
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
