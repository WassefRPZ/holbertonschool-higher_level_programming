#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """Sérialise un objet Python et l'enregistre dans un fichier JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Charge et désérialise un objet Python depuis un fichier JSON."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
