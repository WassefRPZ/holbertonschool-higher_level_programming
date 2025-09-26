#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un Animal.
    Hérite de ABC pour indiquer que c'est une Abstract Base Class.
    Toutes les sous-classes doivent implémenter la méthode sound().
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite qui doit être redéfinie dans les sous-classes.
        Retourne le son que fait l’animal (ex: "Bark", "Meow").
        """
        pass


class Dog(Animal):
    """
    Classe Dog qui hérite de Animal.
    Elle implémente la méthode sound() pour renvoyer "Bark".
    """

    def sound(self):
        """
        Retourne le son spécifique d’un chien.
        """
        return "Bark"


class Cat(Animal):
    """
    Classe Cat qui hérite de Animal.
    Elle implémente la méthode sound() pour renvoyer "Meow".
    """

    def sound(self):
        """
        Retourne le son spécifique d’un chat.
        """
        return "Meow"
