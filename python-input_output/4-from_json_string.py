#!/usr/bin/python3
"""
Module contenant une fonction de désérialisation JSON.
"""
import json


def from_json_string(my_str):
    """
    Retourne un objet Python depuis une chaîne JSON.

    Args:
        my_str (str): La chaîne JSON à convertir.

    Returns:
        object: L'objet Python correspondant.
    """
    return json.loads(my_str)
