#!/usr/bin/python3
"""
Module pour la sérialisation et désérialisation JSON de base.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise et sauvegarde des données dans un fichier.

    Args:
        data: Données à sérialiser.
        filename (str): Nom du fichier de destination.
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Charge et désérialise des données depuis un fichier.

    Args:
        filename (str): Nom du fichier à charger.

    Returns:
        object: Données désérialisées.
    """
    with open(filename, "r") as file:
        return json.load(file)
