#!/usr/bin/python3
"""Module that contains a function to read a file"""
import json


def to_json_string(my_obj):
    """Convertit un objet Python en chaîne JSON."""
    return json.dumps(my_obj)
