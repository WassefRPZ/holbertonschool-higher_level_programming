#!/usr/bin/python3
"""
Module for processing and formatting text.
"""


def text_indentation(text):
    """
    Adds 2 new lines after '.', '?', and ':' in the given text.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = [".", "?", ":"]
    line_buffer = ""

    index = 0
    while index < len(text):
        line_buffer += text[index]

        if text[index] in delimiters:
            print(line_buffer.strip())
            print()
            line_buffer = ""

        while index + 1 < len(text) and text[index + 1] == " ":
            index += 1
        index += 1

    if line_buffer.strip():
        print(line_buffer.strip(), end="")

