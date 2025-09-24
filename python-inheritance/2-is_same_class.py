#!/usr/bin/python3
"""
Module contenant une fonction pour vérifier la classe exacte d'un objet.

La fonction is_same_class permet de déterminer si un objet est
exactement d'une classe donnée, sans tenir compte de l'héritage.
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement d’une classe spécifique.

    Args:
        obj (any): L’objet à tester.
        a_class (type): La classe à comparer.

    Returns:
        bool: True si obj est exactement une instance de a_class,
              False sinon.
    """
    return type(obj) is a_class
