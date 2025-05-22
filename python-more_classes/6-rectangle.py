#!/usr/bin/python3
"""
Module définissant la classe Rectangle.
"""


class Rectangle:
    """
    Classe représentant un rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Args:
            width (int): Largeur du rectangle (doit être un entier >= 0).
            height (int): Hauteur du rectangle (doit être un entier >= 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter pour accéder à la largeur du rectangle.

        Returns:
            int: La largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter pour modifier la largeur du rectangle avec vérification.

        Args:
            value (int): Nouvelle largeur à affecter.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter pour accéder à la hauteur du rectangle.

        Returns:
            int: La hauteur du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter pour modifier la hauteur du rectangle avec vérification.

        Args:
            value (int): Nouvelle hauteur à affecter.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
            int: L'aire du rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule et retourne le périmètre du rectangle.

        Returns:
            int: Le périmètre du rectangle, ou 0 si width ou height vaut 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retourne une chaîne représentant le rectangle avec le caractère #.

        Returns:
            str: Le rectangle avec des #, ou une chaîne vide
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            lignes = []  # Liste pour stocker chaque ligne du rectangle
            for _ in range(self.__height):
                lignes.append("#" * self.__width)
            return "\n".join(lignes)

    def __repr__(self):
        """
        Retourne une chaîne qui permet de recréer le rectangle avec eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Affiche un message lors de la suppression d'une instance de Rectangle.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
