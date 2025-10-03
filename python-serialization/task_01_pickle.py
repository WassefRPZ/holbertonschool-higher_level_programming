#!/usr/bin/python3
import pickle


class CustomObject:
    """Objet personnalisé pouvant être sérialisé avec pickle."""

    def __init__(self, name, age, is_student):
        """Initialise l'objet avec nom, âge et statut étudiant."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sauvegarde l'objet dans un fichier pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Charge un objet depuis un fichier pickle."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj if isinstance(obj, cls) else None
        except Exception:
            return None
