#!/usr/bin/python3
"""
Module contenant la classe Square qui hérite de Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe Square qui hérite de Rectangle.

    Représente un carré (rectangle avec largeur = hauteur).
    """

    def __init__(self, size):
        """
        Initialise un carré avec une taille donnée.

        Args:
        size (int): La taille du côté du carré (doit être un entier positif).
        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur ou égal à 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"