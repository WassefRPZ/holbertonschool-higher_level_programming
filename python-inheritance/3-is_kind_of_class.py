#!/usr/bin/python3
"""
Module contenant une fonction pour vérifier l’appartenance à une classe.

La fonction is_kind_of_class permet de déterminer si un objet est
une instance d’une classe ou de l’une de ses sous-classes.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance d’une classe ou de ses sous-classes.

    Args:
        obj (any): L’objet à tester.
        a_class (type): La classe à comparer.

    Returns:
        bool: True si obj est une instance de a_class ou d’une de ses
              sous-classes, False sinon.
    """
    return isinstance(obj, a_class)
