#!/usr/bin/python3
"""
Module pour écrire dans des fichiers texte.
"""


def write_file(filename="", text=""):
    """
    Écrit une chaîne dans un fichier et retourne le nombre de caractères.

    Args:
        filename (str): Le nom du fichier à écrire.
        text (str): Le texte à écrire dans le fichier.

    Returns:
        int: Le nombre de caractères écrits.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
