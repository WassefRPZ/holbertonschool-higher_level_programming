#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        # Vérifie que size est un entier
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Vérifie que size est positif ou nul
        if size < 0:
            raise ValueError("size must be >= 0")
        # Initialise l'attribut privé
        self.__size = size
