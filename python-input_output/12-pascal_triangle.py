#!/usr/bin/python3
"""
Module pour générer le Triangle de Pascal.
"""


def pascal_triangle(n):
    """
    Génère le Triangle de Pascal avec n lignes.

    Args:
        n (int): Nombre de lignes du triangle.

    Returns:
        list: Liste de listes représentant le Triangle de Pascal.
              Liste vide si n <= 0.
    """
    if n <= 0:
        return []
    triangle = []
    triangle.append([1])
    if n == 1:
        return triangle
    for i in range(1, n):
        new_line = [1]
        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            new_line.append(value)
        new_line.append(1)
        triangle.append(new_line)

    return triangle
