#!/usr/bin/python3
"""Module that contains a function to read a file"""


def read_file(filename=""):
    """Lit un fichier texte et affiche son contenu."""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
