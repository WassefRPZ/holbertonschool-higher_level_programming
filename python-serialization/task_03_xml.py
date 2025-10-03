#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Sérialise un dictionnaire en XML et l'enregistre dans un fichier."""
    try:
        root = ET.Element("data")  # élément racine

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        with open(filename, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=False)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """Désérialise un dictionnaire depuis un fichier XML."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except Exception:
        return None
