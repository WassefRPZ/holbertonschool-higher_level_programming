#!/usr/bin/python3
"""
Module définissant une classe BaseGeometry avec validation d'entiers.

Cette classe sert de base pour les objets géométriques et fournit :
- une méthode area() à implémenter dans les sous-classes
- une méthode integer_validator() pour valider les entiers positifs
"""


class BaseGeometry:
    """
    Classe de base pour la géométrie.

    Méthodes :
        area(): lève une exception, doit être redéfinie par les sous-classes
        integer_validator(name, value): valide qu'un entier est positif
    """

    def area(self):
        """
        Méthode qui doit être redéfinie dans les sous-classes.

        Raises:
            Exception: indique que la méthode n'est pas implémentée
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Vérifie que value est un entier strictement positif.

        Args:
            name (str): Nom de la variable (utilisé dans les messages d'erreur)
            value (any): Valeur à valider

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
