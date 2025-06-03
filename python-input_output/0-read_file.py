#!/usr/bin/python3
"""
Module pour lire des fichiers texte.
"""


def read_file(filename=""):
    """
    Lit un fichier texte et affiche son contenu.

    Args:
        filename (str): Le chemin du fichier à lire.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        contenu = file.read()
        print(contenu, end="")
