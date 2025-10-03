#!/usr/bin/python3
"""Module that contains a function to read a file"""


def write_file(filename="", text=""):
    """Écrit du texte dans un fichier (écrase si déjà existant)."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
