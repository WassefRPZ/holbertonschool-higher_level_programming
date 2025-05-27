#!/usr/bin/python3
"""
Module contenant la classe Rectangle qui hérite de BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.

    Représente un rectangle avec une largeur et une hauteur validées.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Args:
            width (int): La largeur du rectangle (doit être un entier positif).
            height (int): La hauteur du \\ (doit être un entier positif).

        Raises:
            TypeError: Si width ou height n'est pas un entier.
            ValueError: Si width ou height est inférieur ou égal à 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
