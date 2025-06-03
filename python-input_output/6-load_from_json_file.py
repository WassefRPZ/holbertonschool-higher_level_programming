#!/usr/bin/python3
"""
Module contenant une fonction pour charger des objets depuis un fichier JSON.
"""
import json

def load_from_json_file(filename):
    """
    Crée un objet Python depuis un fichier JSON.

    Args:
        filename (str): Le nom du fichier JSON à lire.

    Returns:
        object: L'objet Python correspondant au contenu JSON.
    """
    with open(filename, 'r', encoding='utf-8') as my_file:
        return json.load(my_file)
