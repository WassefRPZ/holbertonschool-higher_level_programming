#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.
    Elle définit l'interface que toutes les formes doivent respecter :
    - une méthode area() pour calculer l'aire
    - une méthode perimeter() pour calculer le périmètre
    """

    @abstractmethod
    def area(self):
        """
        Méthode abstraite.
        Doit retourner l'aire de la forme géométrique.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Méthode abstraite.
        Doit retourner le périmètre de la forme géométrique.
        """
        pass


class Circle(Shape):
    """
    Classe représentant un cercle.
    Hérite de Shape et implémente les méthodes area() et perimeter().
    """

    def __init__(self, radius):
        """
        Constructeur du cercle.
        :param radius: rayon du cercle
        """
        self.__radius = radius = abs(radius)

    def area(self):
        """
        Calcule l'aire du cercle avec la formule : π * r²
        """
        return math.pi * (self.__radius**2)

    def perimeter(self):
        """
        Calcule le périmètre (circonférence)
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Classe représentant un rectangle.
    Hérite de Shape et implémente les méthodes area() et perimeter().
    """

    def __init__(self, width, height):
        """
        Constructeur du rectangle.
        :param width: largeur
        :param height: hauteur
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule l'aire du rectangle avec la formule : largeur * hauteur
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Fonction qui affiche l'aire et le périmètre d'une forme.
    Utilise le duck typing
    :param shape: un objet ayant les méthodes area() et perimeter()
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
