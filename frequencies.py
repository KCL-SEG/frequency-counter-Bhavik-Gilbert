"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for item in items:
        item_str = str(item)

        if item_str in frequencies.keys():
            count = frequencies[item_str]
            frequencies[item_str] = count + 1
        else:
            frequencies[item_str] = 1

    return frequencies
