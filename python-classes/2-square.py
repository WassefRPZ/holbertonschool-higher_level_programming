#!/usr/bin/python3
"""
Module définissant la classe Square.
"""


class Square:
    """
    Classe représentant un carré.
    """
    def __init__(self, size=0):
        """
        Initialise un carré avec une taille donnée.

        Args:
            size (int): La taille du carré (doit être un entier >= 0).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est négatif.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
