#!/usr/bin/python3
"""
Module contenant la fonction lookup.
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles d'un objet.

    Args:
        obj: L'objet dont on veut connaître les attributs et méthodes.

    Returns:
        list: Liste des noms des attributs et méthodes de l'objet.
    """
    return dir(obj)
