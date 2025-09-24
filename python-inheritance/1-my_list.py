#!/usr/bin/python3
"""
Module définissant une sous-classe de list avec méthode supplémentaire.

Ce module contient la classe MyList qui hérite de list et permet
d’afficher la liste triée sans modifier l’originale.
"""


class MyList(list):
    """
    Sous-classe de list avec méthode d’affichage trié.

    Méthodes :
        print_sorted(): affiche les éléments de la liste triés.
    """

    def print_sorted(self):
        """
        Affiche les éléments de la liste dans l’ordre croissant.

        Cette méthode utilise la fonction sorted() pour générer une
        version triée de la liste sans modifier la liste originale.
        """
        print(sorted(self))
