#!/usr/bin/python3
"""
Module définissant une classe Rectangle héritant de BaseGeometry.

Cette classe permet de créer un rectangle avec validation de
largeur et hauteur, calcul de l'aire, et représentation textuelle.
"""

# Importation de la classe de base BaseGeometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle.

    Attributs privés :
        __width (int): largeur du rectangle, validée comme un entier > 0
        __height (int): hauteur du rectangle, validée comme un entier > 0

    Méthodes :
        area(): calcule l'aire du rectangle
        __str__(): retourne une représentation textuelle du rectangle
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec largeur et hauteur.

        Args:
            width (int): largeur du rectangle
            height (int): hauteur du rectangle

        Utilise integer_validator() de BaseGeometry pour valider
        que width et height sont des entiers strictement positifs.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: aire du rectangle (width × height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne une représentation textuelle du rectangle.

        Format : [Rectangle] <width>/<height>

        Returns:
            str: chaîne représentant le rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
