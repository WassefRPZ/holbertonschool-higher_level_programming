#!/usr/bin/python3
"""
Module contenant une fonction utilitaire pour l’inspection d’objets.

Cette fonction retourne la liste des attributs et méthodes disponibles
pour un objet donné.
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes d’un objet.

    Args:
        obj (any): Objet à inspecter

    Returns:
        list: Liste des noms d’attributs et de méthodes de l’objet
    """
    return dir(obj)
