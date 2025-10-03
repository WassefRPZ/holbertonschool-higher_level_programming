#!/usr/bin/python3
"""Module that contains a function to read a file"""


def class_to_json(obj):
    """Retourne le dictionnaire des attributs d'un objet."""
    return obj.__dict__
