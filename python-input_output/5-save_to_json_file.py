#!/usr/bin/python3
"""
Module contenant une fonction pour sauvegarder en JSON.
"""
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)