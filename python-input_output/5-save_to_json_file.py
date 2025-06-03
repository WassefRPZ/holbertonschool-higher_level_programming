#!/usr/bin/python3
"""
Module contenant une fonction pour sauvegarder en JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Sauvegarde un objet dans un fichier au format JSON.

    Args:
        my_obj: L'objet Python à sauvegarder.
        filename (str): Le nom du fichier de destination.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
