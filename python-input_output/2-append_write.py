#!/usr/bin/python3
def append_write(filename="", text=""):
    """Ajoute du texte à la fin d’un fichier."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
