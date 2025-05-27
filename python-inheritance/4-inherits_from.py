#!/usr/bin/python3
"""
module

"""


def inherits_from(obj, a_class):
    """
    Retourne True si l'objet hérite de la classe .

    Args:
        obj: L'objet à vérifier
        a_class: La classe parent potentielle

    Returns:
        bool: True si obj hérite de a_class, False sinon
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
