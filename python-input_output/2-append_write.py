#!/usr/bin/python3
"""Module that contains a function to read a file"""


def append_write(filename="", text=""):
    """Ajoute du texte à la fin d’un fichier."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
