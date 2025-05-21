#!/usr/bin/python3

class Square:
    """
    Classe représentant un carré avec gestion de la taille et de la position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un carré avec une taille et une position.

        Args:
            size (int): Taille du carré (doit être un entier >= 0).
            position (tuple): Position (tuple de 2 entiers positifs).

        Raises:
            TypeError: Si size ou position ne sont pas valides.
            ValueError: Si size est négatif.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter pour accéder à la taille du carré.

        Returns:
            int: La taille du carré.
        """
        return self.__size

    @property
    def position(self):
        """
        Getter pour accéder à la position du carré.

        Returns:
            tuple: La position du carré.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setter pour modifier la taille du carré avec vérification.

        Args:
            value (int): Nouvelle taille à affecter.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Setter pour modifier la position du carré avec vérification.

        Args:
            value (tuple): Nouvelle position à affecter.

        Raises:
            TypeError: Si value n'est pas un tuple de 2 entiers positifs.
        """
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
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Affiche le carré avec le caractère #, en tenant compte de la position.
        Si la taille est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
