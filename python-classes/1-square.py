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

    def __init__(self, size):
        """
        Constructeur de la classe Square.

        Paramètres :
            size (int) : La taille du côté du carré.
        """
        # On définit un attribut privé __size qui stocke la taille du carré
        self.__size = size
