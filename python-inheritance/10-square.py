#!/usr/bin/python3
"""
Module définissant une classe Square héritant de Rectangle.

Cette classe permet de créer un carré avec validation de la taille
et calcul de l'aire.
"""

# Importation de la classe Rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe représentant un carré.

    Attribut privé :
        __size (int): taille du côté du carré, validée comme un entier > 0

    Méthodes :
        area(): calcule l'aire du carré
    """

    def __init__(self, size):
        """
        Initialise un carré avec une taille donnée.

        Args:
            size (int): taille du côté du carré

        Utilise integer_validator() de BaseGeometry (hérité via Rectangle)
        pour valider que size est un entier strictement positif, puis
        appelle le constructeur de Rectangle avec width = height = size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: aire du carré (size × size)
        """
        return self.__size ** 2
