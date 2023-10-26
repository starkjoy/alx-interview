#!/usr/bin/python3
"""
This module contains a method that validates UTF-8 characters
"""

def validUTF8(data):
        """
    Validates whether the given data represents a valid UTF-8 encoding.

    Parameters:
        data (list of int): A list of integers representing bytes of data.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """

    num_bytes_to_follow = 0

    for byte in data:
        if num_bytes_to_follow == 0:
            if byte >> 5 == 0b110:
                num_bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                num_bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                num_bytes_to_follow = 3
            elif byte >> 7 == 0:
                num_bytes_to_follow = 0
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes_to_follow -= 1
    
    return num_bytes_to_follow == 0
