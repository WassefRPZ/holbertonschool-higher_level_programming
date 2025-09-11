#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    i = list(a_dictionary.keys())[0]
    value = a_dictionary[i]
    for j, val in a_dictionary.items():
        if val > value:
            value = val
            i = j
    return i
