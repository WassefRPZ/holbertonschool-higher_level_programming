#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    """Convertit un fichier CSV en JSON et l'enregistre dans data.json."""
    try:
        data = []
        with open(filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception:
        return False
