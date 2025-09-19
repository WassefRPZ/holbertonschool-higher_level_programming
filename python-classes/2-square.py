#!/usr/bin/python3
"""
Ce fichier définit une classe Square.
Elle permet de représenter un carré à partir de sa taille.
"""


class Square:
    """
    Classe qui représente un carré.
    Attributs :
        __size (int) : La taille du carré, défini lors de l'initialisation.
    """
    def __init__(self, size=0):
        """
        Constructeur de la classe Square.

        Paramètres :
            size (int) : La taille du côté du carré (par défaut 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
