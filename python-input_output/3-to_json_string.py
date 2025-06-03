#!/usr/bin/python3
"""
Module contenant une fonction de sérialisation JSON.
"""
import json


def to_json_string(my_obj):
    """
    Retourne la représentation JSON d'un objet.

    Args:
        my_obj: L'objet Python à convertir en JSON.

    Returns:
        str: La chaîne JSON représentant l'objet.
    """
    return json.dumps(my_obj)
