#!/usr/bin/python3
class Square:
    """
    Classe représentant un carré.
    """

    def __init__(self, size=0):
        """
        Initialise un carré avec une taille donnée.

        Args:
            size (int): La taille du carré (doit être un entier >= 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter pour accéder à la taille du carré.

        Returns:
            int: La taille du carré.
        """
        return self.__size

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

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Affiche le carré avec le caractère #.
        Si la taille est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
