#!/usr/bin/python3
"""
Ce fichier définit une classe Square.
Elle permet de représenter un carré à partir de sa taille,
de calculer son aire et de l'afficher avec des '#'.
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

        Utilise le setter 'size' pour vérifier et initialiser l'attribut privé.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter pour l'attribut 'size'.

        Retourne :
            int : La taille actuelle du côté du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour l'attribut 'size'.

        Paramètres :
            value (int) : La nouvelle taille à attribuer au carré.

        Exceptions :
            TypeError : Si 'value' n'est pas un entier.
            ValueError : Si 'value' est négatif.
        """
        # Vérifie que la valeur est un entier
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Vérifie que la valeur est >= 0
        if value < 0:
            raise ValueError("size must be >= 0")

        # Assigne la valeur validée à l'attribut privé
        self.__size = value

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Retour :
            int : l'aire du carré, calculée comme côté².
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré avec le caractère '#'.

        Si la taille est 0, affiche simplement une ligne vide.
        """
        # Si la taille est 0, on affiche juste une ligne vide
        if self.size == 0:
            print("")
            return

        # Crée une ligne de '#' de la longueur de size
        line = "#" * self.size

        # Affiche le carré ligne par ligne
        for i in range(self.size):
            print(line)
