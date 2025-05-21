#!/usr/bin/python3
class Square:
    def __init__(self, size=0,):
        # Vérifie le type et la valeur de size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        # Initialise l'attribut privé
        self.__size = size

    def area(self):
        # Retourne l'aire du carré
        return self.__size * self.__size
