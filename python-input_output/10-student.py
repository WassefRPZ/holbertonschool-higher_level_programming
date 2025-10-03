#!/usr/bin/python3
class Student:
    """Représente un étudiant."""

    def __init__(self, first_name, last_name, age):
        """Initialise un étudiant avec prénom, nom et âge."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne les attributs de l'objet sous forme de dict.
        Si 'attrs' est une liste de chaînes, filtre uniquement ces clés.
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            result = {}
            for j in attrs:
                if j in self.__dict__:
                    result[j] = self.__dict__[j]
            return result
        else:
            return self.__dict__
