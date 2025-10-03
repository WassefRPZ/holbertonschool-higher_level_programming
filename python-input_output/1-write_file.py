#!/usr/bin/python3
def write_file(filename="", text=""):
    """Écrit du texte dans un fichier (écrase si déjà existant)."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
