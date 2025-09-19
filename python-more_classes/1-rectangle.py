#!/usr/bin/python3
"""
Module rectangle.

Ce module définit une classe Rectangle avec gestion de la largeur
et de la hauteur, en incluant l'encapsulation et la validation.
"""


class Rectangle:
    """
    Classe Rectangle.

    Représente un rectangle défini par sa largeur et sa hauteur.
    Les attributs sont protégés par des propriétés pour assurer
    la validation des valeurs.
    """

    def __init__(self, width=0, height=0):
        """
        Constructeur du rectangle.

        Args:
            width (int, optional): largeur du rectangle (par défaut 0).
            height (int, optional): hauteur du rectangle (par défaut 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter de la largeur.

        Returns:
            int: largeur actuelle du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter de la largeur.

        Args:
            value (int): nouvelle largeur.

        Raises:
            TypeError: si la valeur n'est pas un entier.
            ValueError: si la valeur est négative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter de la hauteur.

        Returns:
            int: hauteur actuelle du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter de la hauteur.

        Args:
            value (int): nouvelle hauteur.

        Raises:
            TypeError: si la valeur n'est pas un entier.
            ValueError: si la valeur est négative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
