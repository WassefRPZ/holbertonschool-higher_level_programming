#!/usr/bin/python3
"""
Module pour additionner deux entiers
Contient une fonction pour additionner deux nombres
et gérer les erreurs de type
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
