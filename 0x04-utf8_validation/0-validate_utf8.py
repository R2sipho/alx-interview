#!/usr/bin/python3
"""
Module to check for valid UTF-8 encoding
"""

def validUTF8(data):
    """
    Check if the input list of integers represents a valid UTF-8 encoded sequence.

    Parameters:
    data (list): A list of integers representing bytes.

    Returns:
    bool: True if the input is a valid UTF-8 encoded sequence, False otherwise.
    """
    try:
        masked_data = [n & 255 for n in data]
        bytes(masked_data).decode("UTF-8")
        return True
    except UnicodeDecodeError:
        return False

