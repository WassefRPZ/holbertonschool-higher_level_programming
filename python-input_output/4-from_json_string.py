#!/usr/bin/python3
"""Module that contains a function to read a file"""
import json


def from_json_string(my_str):
    """Convertit une chaîne JSON en objet Python."""
    return json.loads(my_str)
