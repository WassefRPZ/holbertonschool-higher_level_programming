#!/usr/bin/python3
"""
Ce fichier définit une classe Square.
Elle permet de représenter un carré à partir de sa taille
et de calculer son aire.
"""


class Square:
    """
    Classe qui représente un carré.

    Attributs :
        __size (int) : La taille du côté du carré.
    """

    def __init__(self, size=0):
        """
        Constructeur de la classe Square.

        Paramètres :
            size (int) : La taille du côté du carré (par défaut 0).

        Exceptions :
            TypeError : Si 'size' n'est pas un entier.
            ValueError : Si 'size' est négatif.
        """
        # Vérifie que size est bien un entier
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Vérifie que size est positif ou nul
        if size < 0:
            raise ValueError("size must be >= 0")

        # Définit l'attribut privé __size
        self.__size = size

    def area(self):
        """
        Retourne l'aire du carré.

        Retour :
            int : l'aire calculée comme côté².
        """
        # Aire = côté * côté
        return self.__size ** 2
