#!/usr/bin/python3
"""
Module contenant une fonction de conversion objet vers dictionnaire.
"""


def class_to_json(obj):
    """
    Retourne la représentation dict d'un objet pour la sérialisation JSON.

    Args:
        obj: Instance d'une classe à convertir.

    Returns:
        dict: Dictionnaire contenant tous les attributs de l'objet.
    """
    return obj.__dict__
