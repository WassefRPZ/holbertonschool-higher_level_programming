#!/usr/bin/python3
"""
Module contenant la classe BaseGeometry.
"""


class BaseGeometry:
    """
    Classe BaseGeometry pour les formes géométriques.

    Cette classe sert de base pour les futures classes géométriques.
    """

    def area(self):
        """
        Calcule l'aire de la forme géométrique.

        Raises:
            Exception: Toujours, car la méthode n'est pas implémentée.
        """
        raise Exception("area() is not implemented")
