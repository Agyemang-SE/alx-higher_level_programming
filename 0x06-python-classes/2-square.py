#!/usr/bin/python3
"""Define class name Square"""


class Square():
    """ Class Square """

    def __init__(self, size = 0):
        """Initialize method.
        Args:
            self (class): This class
            size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
