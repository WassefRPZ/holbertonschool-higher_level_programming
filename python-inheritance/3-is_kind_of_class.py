#!/usr/bin/python3
"""
Module contenant la fonction is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance de la class spéc ou qui en hérite.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à comparer.

    Returns:
        True si obj est une instance de a_class ou hérite de a_class, False.
    """
    return isinstance(obj, a_class)
