#!/usr/bin/python3
"""
Module pour ajouter du texte à des fichiers.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne à la fin d'un fichier et retourne le nombre de caractères ajoutés.

    Args:
        filename (str): Le nom du fichier à modifier.
        text (str): Le texte à ajouter au fichier.

    Returns:
        int: Le nombre de caractères ajoutés.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
