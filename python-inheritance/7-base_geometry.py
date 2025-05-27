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

    def integer_validator(self, name, value):
        """
        Valide qu'une valeur est un entier positif.

        Args:
            name (str): Le nom de la valeur (pour les messages d'erreur).
            value: La valeur à valider.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur ou égal à 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
