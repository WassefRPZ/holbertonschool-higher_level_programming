#!/usr/bin/python3
"""
Module pour la sérialisation d'objets personnalisés avec pickle.
"""
import pickle

class CustomObject:
    """
    Classe représentant un objet personnalisé avec capacités de sérialisation.
    """

    def __init__(self, name, age, is_student):
        """
        Initialise une nouvelle instance de CustomObject.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
            is_student (bool): Si la personne est étudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Sérialise cet objet dans un fichier avec pickle.

        Args:
            filename (str): Chemin du fichier de sauvegarde.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet depuis un fichier.

        Args:
            filename (str): Chemin du fichier contenant l'objet.

        Returns:
            CustomObject: L'objet désérialisé, ou None si erreur.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
