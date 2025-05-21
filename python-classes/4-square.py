#!/usr/bin/python3
class Square:
    def __init__(self, size=0,):
        # Initialise la taille du carré
        self.size = size

    @property
    def size(self):
        # Getter pour accéder à la taille
        return self.__size

    @size.setter
    def size(self, value):
        # Setter avec vérification du type et de la valeur
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        # Calcule et retourne l'aire du carré
        return self.__size * self.__size
