#!/usr/bin/python3
"""
Module rectangle.

Définit une classe Rectangle permettant de calculer l'aire,
le périmètre, d'afficher une représentation textuelle,
et de notifier lors de la destruction d'une instance.
"""


class Rectangle:
    """
    Classe Rectangle.

    Représente un rectangle défini par sa largeur et sa hauteur.
    - Attributs width et height validés par propriétés
    - Méthodes de calcul (area, perimeter)
    - Représentations spéciales (__str__, __repr__)
    - Notification à la suppression (__del__)
    """

    def __init__(self, width=0, height=0):
        """
        Constructeur du rectangle.

        Args:
            width (int, optional): largeur (par défaut 0).
            height (int, optional): hauteur (par défaut 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter de la largeur.

        Returns:
            int: largeur actuelle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter de la largeur.

        Args:
            value (int): nouvelle largeur.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter de la hauteur.

        Returns:
            int: hauteur actuelle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter de la hauteur.

        Args:
            value (int): nouvelle hauteur.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcule l'aire du rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: 2 x (width + height), ou 0 si une dimension est nulle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Représentation textuelle avec des '#'.

        Returns:
            str: rectangle dessiné en '#', ou chaîne vide si vide.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        row = "#" * self.__width
        return "\n".join([row for _ in range(self.__height)])

    def __repr__(self):
        """
        Représentation officielle de l'objet.

        Returns:
            str: appel du constructeur pour recréer le rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Notification à la destruction de l'objet.

        Affiche un message lors de la suppression du rectangle.
        """
        print("Bye rectangle...")
