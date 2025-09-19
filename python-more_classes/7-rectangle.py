#!/usr/bin/python3
"""
Module rectangle.

Définit une classe Rectangle capable de calculer son aire et son périmètre,
de s'afficher avec un symbole personnalisable, et de suivre le nombre
d'instances actives.
"""


class Rectangle:
    """
    Classe Rectangle avec affichage configurable et suivi d'instances.

    - Attributs de classe :
        number_of_instances : compte les instances actives
        print_symbol : symbole utilisé pour l'affichage visuel
    - Largeur et hauteur validées par propriétés
    - Méthodes de calcul (area, perimeter)
    - Méthodes spéciales pour l'affichage, la récréation et la suppression
    """

    # Attributs de classe
    number_of_instances = 0   # Nombre d’instances actives
    print_symbol = "#"        # Symbole utilisé pour l’affichage

    def __init__(self, width=0, height=0):
        """
        Constructeur du rectangle.

        Incrémente le compteur d'instances à chaque création.

        Args:
            width (int, optional): largeur (par défaut 0).
            height (int, optional): hauteur (par défaut 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter de la largeur."""
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
        """Getter de la hauteur."""
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
        """Retourne l'aire (width x height)."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre ou 0 si une dimension est nulle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Représentation textuelle avec print_symbol.

        Returns:
            str: rectangle dessiné avec print_symbol, ou chaîne vide
            si width ou height est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = str(self.print_symbol) * self.__width
        return "\n".join([row for _ in range(self.__height)])

    def __repr__(self):
        """
        Représentation officielle.

        Returns:
            str: chaîne permettant de recréer l'objet avec eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Destructeur : appelé à la suppression de l'instance.

        Affiche un message et décrémente le compteur d'instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
