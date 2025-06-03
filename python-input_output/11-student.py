#!/usr/bin/python3
"""
Module contenant la classe Student avec sérialisation/désérialisation.
"""


class Student:
    """
    Classe représentant un étudiant avec sérialisation JSON.
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

        Returns:
            dict: Dictionnaire contenant les attributs demandés.
        """
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            new_dict = {}
            for attrs in attrs:
                if attrs in self.__dict__:
                    new_dict[attrs] = self.__dict__[attrs]
            return new_dict

    def reload_from_json(self, json):
        """
        Met à jour les attributs de l'étudiant depuis un dictionnaire JSON.

        Args:
            json (dict): Dictionnaire contenant les nouveaux attributs.
        """
        for key, value in json.items():
            setattr(self, key, value)
