#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        # Initialisation de la taille et de la position via les setters
        self.size = size
        self.position = position

    @property
    def size(self):
        # Getter pour récupérer la taille privée
        return self.__size

    @property
    def position(self):
        # Getter pour récupérer la position privée
        return self.__position

    @size.setter
    def size(self, value):
        # Setter pour modifier la taille avec vérif du type et de la valeur
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        # Setter pour modifier la position avec toutes les vérif nécessaires
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        # Retourne l'aire du carré (size * size)
        return self.__size * self.__size

    def my_print(self):
        # Affiche le carré avec le caractère #, en tenant compte de la position
        if self.__size == 0:
            print()  # Affiche une ligne vide si la taille est 0
        else:
            # Affiche les lignes vides en haut selon position[1]
            for _ in range(self.__position[1]):
                print()
            # Affiche chaque ligne du carré avec les espaces à gauche 
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
