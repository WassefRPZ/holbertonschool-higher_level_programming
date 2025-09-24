#!/usr/bin/python3
"""
Module définissant une classe BaseGeometry avec méthode area().

Cette classe sert de base pour les objets géométriques et
implémente une méthode area() qui doit être redéfinie dans
les sous-classes.
"""


class BaseGeometry:
    """
    Classe de base pour la géométrie.

    Méthodes :
        area(): lève une exception, doit être implémentée par les sous-classes.
    """

    def area(self):
        """
        Méthode qui doit être redéfinie dans les sous-classes.

        Raises:
            Exception: indique que la méthode n'est pas implémentée.
        """
        raise Exception("area() is not implemented")
