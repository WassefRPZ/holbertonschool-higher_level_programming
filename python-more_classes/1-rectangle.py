#!/usr/bin/python3
"""
Module définissant la classe Rectangle.
"""


class Rectangle:
    """
    Classe représentant un rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Args:
            width (int): Largeur du rectangle (doit être un entier >= 0).
            height (int): Hauteur du rectangle (doit être un entier >= 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter pour accéder à la largeur du rectangle.

        Returns:
            int: La largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter pour modifier la largeur du rectangle avec vérification.

        Args:
            value (int): Nouvelle largeur à affecter.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter pour accéder à la hauteur du rectangle.

        Returns:
            int: La hauteur du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter pour modifier la hauteur du rectangle avec vérification.

        Args:
            value (int): Nouvelle hauteur à affecter.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
