#!/usr/bin/python3
class Fish:
    """
    Classe représentant un poisson.
    Fournit des méthodes liées au comportement d'un poisson.
    """

    def swim(self):
        """
        Affiche un message indiquant que le poisson nage.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Affiche l'habitat typique d'un poisson : l'eau.
        """
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau.
    Fournit des méthodes liées au comportement d'un oiseau.
    """

    def fly(self):
        """
        Affiche un message indiquant que l'oiseau vole.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Affiche l'habitat typique d'un oiseau : le ciel.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant.
    Hérite de Fish et Bird pour combiner les comportements.
    Redéfinit certaines méthodes pour refléter son mode de vie particulier.
    """

    def swim(self):
        """
        Affiche un message indiquant que le poisson volant nage.
        (Redéfinit la méthode swim de Fish).
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Affiche un message indiquant que le poisson volant plane.
        (Redéfinit la méthode fly de Bird).
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Affiche l'habitat unique du poisson volant,
        qui vit à la fois dans l'eau et dans le ciel.
        (Redéfinit habitat des classes Fish et Bird).
        """
        print("The flying fish lives both in water and the sky!")
