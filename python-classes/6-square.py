#!/usr/bin/python3
"""
Ce fichier définit une classe Square.
Elle permet de représenter un carré à partir de sa taille
et de l'afficher avec un décalage horizontal et vertical.
"""


class Square:
    """
    Classe qui représente un carré.

    Attributs :
        __size (int) : La taille du côté du carré.
        __position (tuple) : Position (x, y) du carré pour l'affichage,
                             x = décalage horizontal,
                             y = décalage vertical.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructeur de la classe Square.

        Paramètres :
            size (int) : La taille du côté du carré (par défaut 0).

        Utilise les setters pour initialiser les attributs avec vérification.
        """
        self.position = position  # Appelle le setter pour vérifier la position
        self.size = size          # Appelle le setter pour vérifier la taille

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter pour l'attribut 'position'.

        Retourne :
            tuple : La position actuelle du carré.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter pour l'attribut 'position'.

        Paramètres :
            value (tuple) : Nouveau décalage pour le carré (x, y).

        Exceptions :
            TypeError : Si 'value' n'est pas un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Retour :
            int : Aire du carré, calculée comme côté².
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré avec le caractère '#' en tenant compte de la position.

        Décalage vertical : imprimé sous forme de lignes vides avant le carré.
        Décalage horizontal : espaces ajoutés au début de chaque ligne.
        Si la taille est 0, affiche une ligne vide.
        """
        if self.size == 0:
            print("")
            return

        # Décalage vertical
        for i in range(self.position[1]):
            print()

        # Affichage ligne par ligne avec décalage horizontal
        for i in range(self.size):
            line = " " * self.position[0] + "#" * self.size
            print(line)
