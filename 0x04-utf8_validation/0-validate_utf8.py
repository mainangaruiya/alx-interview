#!/usr/bin/python3
"""Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
"""
def validUTF8(data):
    """
    if data is a valid UTF-8 encoding, else return False
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
            if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
                return False
            elif data[i] <= 0x7f:
                skip = 0
            elif data[i] & 0b11111000 == 0b11110000:
                span = 4
                # Check if there are enough bytes in the list to represent the 4-byte character.
            if n - i >= span:

                # Create a list of boolean values, where each value indicates whether the corresponding byte is a continuation byte.
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))

                # If any of the following bytes are not continuation bytes, return False.
                if not all(next_body):
                    return False

                # Set skip to span - 1, indicating the number of bytes to skip.
                skip = span - 1
            else:
                return False

        # Check for 3-byte UTF-8 characters, following a similar pattern as for 4-byte characters.
        elif data[i] & 0b11110000 == 0b11100000:
            # This condition checks if the integer represents the start of a 3-byte UTF-8 character.

            span = 3

            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))

                if not all(next_body):
                    return False

                skip = span - 1
            else:
                return False

        # Check for 2-byte UTF-8 characters, following a similar pattern as for 4-byte characters.
        elif data[i] & 0b11100000 == 0b11000000:
            # This condition checks if the integer represents the start of a 2-byte UTF-8 character.

            span = 2

            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))

                if not all(next_body):
                    return False

                skip = span - 1
            else:
                return False

        # If none of the above conditions are met, return False, as the current integer does not conform to any valid UTF-8 encoding rules.
        else:
            return False

    # If the loop completes without any issues, return True, indicating that the data is valid UTF-8.
    return True