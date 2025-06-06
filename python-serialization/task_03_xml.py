#!/usr/bin/python3
"""
Module pour la sérialisation et désérialisation XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire en XML et sauvegarde dans un fichier.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Chemin du fichier XML de destination.
    """
    root = ET.Element('root')
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.

    Args:
        filename (str): Chemin du fichier XML à désérialiser.

    Returns:
        dict: Dictionnaire contenant les données du fichier XML.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for element in root:
        dictionary[element.tag] = element.text

    return dictionary
