#!/usr/bin/python3
"""
Module rectangle.

Définit une classe Rectangle capable de :
- calculer aire et périmètre,
- s'afficher avec un symbole personnalisable,
- suivre le nombre d'instances actives,
- comparer deux rectangles par leur aire.
"""


class Rectangle:
    """
    Classe Rectangle avec fonctionnalités avancées.

    Attributs de classe :
        number_of_instances (int): nombre d'instances actives
        print_symbol: symbole utilisé pour l'affichage

    Caractéristiques :
    - Largeur et hauteur validées par propriétés
    - Calculs : aire et périmètre
    - Méthodes spéciales pour affichage, récréation et suppression
    - Méthode statique pour comparer deux rectangles par aire
    """

    number_of_instances = 0   # Compteur d’instances
    print_symbol = "#"        # Symbole d’affichage

    def __init__(self, width=0, height=0):
        """
        Constructeur du rectangle.

        Incrémente le compteur d'instances.

        Args:
            width (int, optional): largeur (défaut 0)
            height (int, optional): hauteur (défaut 0)
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
            value (int): nouvelle largeur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est négatif
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
            value (int): nouvelle hauteur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est négatif
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
        """Retourne le périmètre ou 0 si une dimension vaut 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Affiche le rectangle avec print_symbol ou chaîne vide si nul."""
        if self.__width == 0 or self.__height == 0:
            return ""
        row = str(self.print_symbol) * self.__width
        return "\n".join([row for _ in range(self.__height)])

    def __repr__(self):
        """Retourne une chaîne recréant l'objet avec eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Message de suppression et décrémentation du compteur."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare deux rectangles et retourne le plus grand (aire).

        Args:
            rect_1 (Rectangle): premier rectangle
            rect_2 (Rectangle): second rectangle

        Returns:
            Rectangle: celui avec la plus grande aire,
            ou rect_1 si égalité

        Raises:
            TypeError: si rect_1 ou rect_2 n'est pas un Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
