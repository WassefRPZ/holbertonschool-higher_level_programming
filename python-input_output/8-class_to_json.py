#!/usr/bin/python3
def class_to_json(obj):
    """Retourne le dictionnaire des attributs d'un objet."""
    return obj.__dict__
