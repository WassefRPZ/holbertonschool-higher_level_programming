#!/usr/bin/python3
"""
Module contenant la classe MyList qui hérite de list.
"""


class MyList(list):
    """
    Une classe qui hérite de list avec une méthode pour afficher un triée.
    """

    def print_sorted(self):
        """
        Affiche la liste triée par ordre croissant.

        La liste originale n'est pas modifiée.
        """
        print(sorted(self))
