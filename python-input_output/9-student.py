#!/usr/bin/python3
"""
Module contenant la classe Student.
"""

class Student:
    """
    Classe représentant un étudiant.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise un étudiant.

        Args:
            first_name (str): Prénom de l'étudiant.
            last_name (str): Nom de famille de l'étudiant.
            age (int): Âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retourne la représentation dictionnaire de l'étudiant.

        Returns:
            dict: Dictionnaire contenant tous les attributs.
        """
        return self.__dict__
