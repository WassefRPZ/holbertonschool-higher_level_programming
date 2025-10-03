#!/usr/bin/python3
def read_file(filename=""):
    """Lit un fichier texte et affiche son contenu."""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
