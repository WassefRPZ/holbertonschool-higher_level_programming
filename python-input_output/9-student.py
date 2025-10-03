#!/usr/bin/python3
class Student:
    """Représente un étudiant."""

    def __init__(self, first_name, last_name, age):
        """Initialise un étudiant avec prénom, nom et âge."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retourne le dictionnaire des attributs de l'objet."""
        return self.__dict__
