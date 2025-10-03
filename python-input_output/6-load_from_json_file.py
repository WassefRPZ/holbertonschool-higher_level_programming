#!/usr/bin/python3
"""Module that contains a function to read a file"""
import json


def load_from_json_file(filename):
    """Charge un objet Python depuis un fichier JSON."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
