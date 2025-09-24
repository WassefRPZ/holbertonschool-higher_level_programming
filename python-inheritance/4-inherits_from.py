#!/usr/bin/python3
"""
Module contenant une fonction pour vérifier l'héritage d'une classe.

La fonction inherits_from détermine si un objet est une instance
d'une classe qui hérite d'une autre classe spécifique.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d’une classe qui hérite
    d’une classe spécifique, sans être exactement cette classe.

    Args:
        obj (any): L’objet à tester.
        a_class (type): La classe parente à comparer.

    Returns:
        bool: True si obj est une instance d’une sous-classe de
              a_class, False sinon.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
