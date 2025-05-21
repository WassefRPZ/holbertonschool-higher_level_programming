#!/usr/bin/python3
class Square:
    def __init__(self, size=0,):
        # Initialise la taille
        self.size = size

    @property
    def size(self):
        # Getter taille
        return self.__size

    @size.setter
    def size(self, value):
        # Setter taille avec vérif
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        # Calcule l'aire
        return self.__size * self.__size

    def my_print(self):
        # Affiche le carré avec #
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
