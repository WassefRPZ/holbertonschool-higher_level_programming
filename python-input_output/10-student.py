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

    def to_json(self, attrs=None):
        """
        Retourne la représentation dictionnaire de l'étudiant.

        Args:
            attrs (list, optional): Liste des attributs à inclure.
                                   Si None, inclut tous les attributs.

        Returns:
            dict: Dictionnaire contenant les attributs demandés.
        """
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            new_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
            return new_dict
