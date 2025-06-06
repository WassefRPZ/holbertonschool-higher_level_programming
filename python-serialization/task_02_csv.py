#!/usr/bin/python3
"""
Module pour convertir des fichiers CSV en format JSON.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convertit des données d'un fichier CSV en format JSON.

    Args:
        filename (str): Chemin du fichier CSV à convertir.

    Returns:
        bool: True si la conversion réussit, False sinon.
    """
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            data = list(csv.DictReader(f))

        with open('data.json', 'w', encoding='utf-8') as json_f:
            json.dump(data, json_f)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
