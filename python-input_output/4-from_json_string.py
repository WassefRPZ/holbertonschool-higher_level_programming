#!/usr/bin/python3
#!/usr/bin/python3
"""
Module contenant une fonction de désérialisation JSON.
"""
import json

def from_json_string(my_str):
    return json.loads(my_str)